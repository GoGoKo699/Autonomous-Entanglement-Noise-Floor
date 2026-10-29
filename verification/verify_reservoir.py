#!/usr/bin/env python3
"""Deterministic checks of the explicit attaining two-qubit reservoir.

Run from the repository root:
    python verification/verify_reservoir.py

The checked-in expected_results.json contains reference numerical values and
an exact rational example. Numerical residuals are checked against explicit
tolerances, not compared byte for byte with another machine's roundoff.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import platform
from typing import Any

import numpy as np
import scipy
from scipy.linalg import eigvals, expm

from reservoir import (
    I2,
    P_ODD,
    P_PHI,
    Z,
    adjoint_action,
    amplitudes,
    generator_action,
    infidelity,
    jumps,
    noisy_state,
    optimal_b,
    optimizer_polynomial,
    population_rates,
    projector,
    pure_vectors,
    superoperator,
    survival,
    trace_distance,
    unvec,
    vec,
)

TOLERANCES = {
    "matrix_identity": 2e-12,
    "stationary_solve": 2e-9,
    "propagation": 2e-9,
    "eigenvalue_zero": 1e-10,
    "reference_atol": 5e-13,
    "reference_rtol": 5e-10,
}


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def small(value: float, tolerance: float, label: str) -> None:
    require(np.isfinite(value) and value <= tolerance, f"{label}: {value:.6g} > {tolerance:.6g}")


def spectral_summary(generator: np.ndarray) -> tuple[int, float]:
    eigenvalues = eigvals(generator)
    zero_tol = TOLERANCES["eigenvalue_zero"]
    nullity = int(np.count_nonzero(np.abs(eigenvalues) < zero_tol))
    require(np.max(eigenvalues.real) < zero_tol, "generator has a growing eigenvalue")
    decays = -eigenvalues.real[eigenvalues.real < -zero_tol]
    require(len(decays) > 0, "no decaying modes found")
    return nullity, float(np.min(decays))


def check_vectorization() -> dict[str, Any]:
    """Complex coefficients make an incorrect transpose convention visible."""
    unitary = np.kron(np.diag([1, 1j]), I2)
    jump_ops = [unitary @ jump @ unitary.conj().T for jump in jumps(0.73, 1.7, 0.09)]
    x = np.array([[0, 1], [1, 0]], complex)
    y = np.array([[0, -1j], [1j, 0]], complex)
    hamiltonian = 0.17 * np.kron(x, y) + 0.23 * np.kron(Z, I2) + 0.11 * np.kron(I2, x)
    generator = superoperator(jump_ops, hamiltonian)
    action_error = 0.0
    hermiticity_error = 0.0
    for row in range(4):
        for column in range(4):
            unit = np.zeros((4, 4), complex)
            unit[row, column] = 1
            direct = generator_action(jump_ops, unit, hamiltonian)
            action_error = max(action_error, float(np.linalg.norm(generator @ vec(unit) - vec(direct))))
            conjugate_action = generator_action(jump_ops, unit.conj().T, hamiltonian)
            hermiticity_error = max(hermiticity_error, float(np.linalg.norm(conjugate_action - direct.conj().T)))
    trace_error = float(np.linalg.norm(vec(np.eye(4)).conj() @ generator))
    for label, value in [
        ("column-vectorization identity", action_error),
        ("trace preservation", trace_error),
        ("Hermiticity preservation", hermiticity_error),
    ]:
        small(value, TOLERANCES["matrix_identity"], label)
    return {
        "generator_shape": list(generator.shape),
        "matrix_units_checked": 16,
        "complex_jumps_and_hamiltonian": True,
        "column_action_error": action_error,
        "trace_preservation_error": trace_error,
        "hermiticity_preservation_error": hermiticity_error,
    }


def check_pure_case(delta0: float) -> dict[str, Any]:
    b, g = 1 - 2 * delta0, 1.0
    _, _, a = amplitudes(b)
    jump_ops = jumps(b, g)
    generator = superoperator(jump_ops)
    dark, bright = pure_vectors(b)
    pd, pe = projector(dark), projector(bright)
    odd = np.diag([0, 1, 0, 0]).astype(complex)
    gamma, beta = population_rates(b)
    cb = beta / (beta - gamma)

    stationary_error = float(np.linalg.norm(generator @ vec(pd)))
    squared_norms = [float(np.linalg.norm(jump, 2) ** 2) for jump in jump_ops]
    norm_error = max(abs(value - g) for value in squared_norms)
    identities = [
        adjoint_action(jump_ops, pe) - g * (-2 * pe + b * b * P_ODD),
        adjoint_action(jump_ops, P_ODD) - g * (2 * pe - P_ODD),
        adjoint_action(jump_ops, pd) - g * a * a * P_ODD,
    ]
    population_error = max(float(np.linalg.norm(value)) for value in identities)
    nullity, numerical_gap = spectral_summary(generator)
    require(nullity == 1, "pure case does not have one zero eigenvalue")
    small(abs(numerical_gap - g * gamma), TOLERANCES["matrix_identity"], "pure numerical gap versus population rate")

    survival_error = 0.0
    lower_bound_excess = 0.0
    upper_bound_excess = 0.0
    distance_bound_excess = 0.0
    coherent = projector(np.array([1, 1j, -1, 1], complex) / 2)
    product = np.diag([1, 0, 0, 0]).astype(complex)
    for time in [0.2 / g, 1 / (g * gamma), 3 / (g * gamma)]:
        channel = expm(generator * time)
        evolved_bright = unvec(channel @ vec(pe))
        exact_bright = survival(b, g, time, "bright")
        observed_bright = 1 - float(np.trace(pd @ evolved_bright).real)
        observed_odd = 1 - float(np.trace(pd @ unvec(channel @ vec(odd))).real)
        survival_error = max(
            survival_error,
            abs(observed_bright - exact_bright),
            abs(observed_odd - survival(b, g, time, "odd")),
        )
        lower_bound_excess = max(lower_bound_excess, np.exp(-g * gamma * time) - observed_bright)
        upper = cb * np.exp(-g * gamma * time)
        for initial in [pe, odd, coherent, product]:
            evolved = unvec(channel @ vec(initial))
            remaining = 1 - float(np.trace(pd @ evolved).real)
            upper_bound_excess = max(upper_bound_excess, remaining - upper)
            distance_bound_excess = max(distance_bound_excess, trace_distance(evolved, pd) - np.sqrt(upper))

    for label, value in [
        ("pure stationary residual", stationary_error),
        ("jump norms", norm_error),
        ("population adjoint identities", population_error),
    ]:
        small(value, TOLERANCES["matrix_identity"], label)
    for label, value in [
        ("survival formulas", survival_error),
        ("bright survival lower bound", float(lower_bound_excess)),
        ("uniform survival upper bound on selected states", float(upper_bound_excess)),
        ("trace-distance upper bound on selected states", float(distance_bound_excess)),
    ]:
        small(value, TOLERANCES["propagation"], label)
    return {
        "design_error": delta0,
        "g": g,
        "b": b,
        "engineered_budget": sum(squared_norms),
        "gamma_b": gamma,
        "beta_b": beta,
        "gamma_over_design_error": gamma / delta0,
        "survival_at_one_slow_time": survival(b, g, 1 / (g * gamma), "bright"),
        "zero_eigenvalues": nullity,
        "numerical_gap": numerical_gap,
        "stationary_residual": stationary_error,
        "jump_norm_error": norm_error,
        "population_identity_error": population_error,
        "survival_formula_error": survival_error,
        "survival_lower_bound_excess": float(lower_bound_excess),
        "survival_upper_bound_excess": float(upper_bound_excess),
        "trace_distance_bound_excess": float(distance_bound_excess),
    }


def check_noisy_case(r: float) -> dict[str, Any]:
    b, g, kappa = optimal_b(r), 1.0, r
    jump_ops = jumps(b, g, kappa)
    generator = superoperator(jump_ops)
    state = noisy_state(b, r)
    stationary_error = float(np.linalg.norm(generator @ vec(state)))

    # The numerical solve uses all 16 unknown entries, with no X-state ansatz.
    augmented = generator.copy()
    augmented[0, :] = vec(np.eye(4))
    right = np.zeros(16, complex)
    right[0] = 1
    numerical_state = unvec(np.linalg.solve(augmented, right))
    solve_error = float(np.linalg.norm(numerical_state - state))
    trace_error = float(abs(np.trace(state) - 1))
    formula_error = float(abs(1 - np.trace(P_PHI @ state).real - infidelity(b, r)))
    eigenvalues = np.linalg.eigvalsh(state)
    nullity, gap = spectral_summary(generator)
    total_budget = float(sum(np.linalg.norm(jump, 2) ** 2 for jump in jump_ops))
    require(nullity == 1, "noisy case does not have one zero eigenvalue")
    require(float(eigenvalues[0]) > 0, "noisy stationary state is not faithful")
    root_error = abs(optimizer_polynomial(b, r))
    require(infidelity(b, r) < min(infidelity(0, r), infidelity(1, r)), "interior optimum fails endpoint comparison")
    for label, value in [
        ("noisy stationarity", stationary_error),
        ("noisy trace", trace_error),
        ("noisy fidelity formula", formula_error),
        ("optimizer root", root_error),
        ("total physical budget", abs(total_budget - (2 * g + kappa))),
    ]:
        small(value, TOLERANCES["matrix_identity"], label)
    small(solve_error, TOLERANCES["stationary_solve"], "unconstrained stationary solve")
    epsilon = infidelity(b, r)
    return {
        "r": r,
        "g": g,
        "kappa": kappa,
        "engineered_budget": 2 * g,
        "total_budget": total_budget,
        "optimal_b": b,
        "optimal_design_error": (1 - b) / 2,
        "optimal_infidelity": epsilon,
        "infidelity_over_sqrt_r": epsilon / np.sqrt(r),
        "infidelity_over_sqrt_kappa_over_Gamma": epsilon / np.sqrt(kappa / (2 * g)),
        "minimum_state_eigenvalue": float(eigenvalues[0]),
        "zero_eigenvalues": nullity,
        "numerical_gap": gap,
        "stationary_residual": stationary_error,
        "unconstrained_solve_error": solve_error,
        "trace_error": trace_error,
        "fidelity_formula_error": formula_error,
        "optimizer_polynomial_residual": root_error,
    }


def rational_example() -> dict[str, Any]:
    """Exact arithmetic on a full 4x4 model, without a symbolic dependency."""
    u, v, g, kappa = F(4, 5), F(3, 5), F(3, 2), F(1, 80)
    r, a, b = kappa / g, u * u - v * v, 2 * u * v
    denominator = a * a + 2 * r
    q, w = 2 * r * u * u * v * v / denominator, -u * v * a * a / denominator
    p, s = u * u - q, v * v - q
    rho = [[p, F(0), F(0), w], [F(0), q, F(0), F(0)], [F(0), F(0), q, F(0)], [w, F(0), F(0), s]]

    def multiply(left: list[list[F]], right: list[list[F]]) -> list[list[F]]:
        return [[sum((left[i][k] * right[k][j] for k in range(4)), F(0)) for j in range(4)] for i in range(4)]

    def transpose(matrix: list[list[F]]) -> list[list[F]]:
        return [[matrix[j][i] for j in range(4)] for i in range(4)]

    # Unscaled jumps are rational; g and kappa multiply their dissipators.
    l1 = [[F(0), F(0), u, F(0)], [v, F(0), F(0), u], [F(0), F(0), F(0), F(0)], [F(0), F(0), v, F(0)]]
    l2 = [[F(0), u, F(0), F(0)], [F(0), F(0), F(0), F(0)], [v, F(0), F(0), u], [F(0), v, F(0), F(0)]]
    za = [[F(int(i == j) * (1 if i < 2 else -1)) for j in range(4)] for i in range(4)]
    residual = [[F(0) for _ in range(4)] for _ in range(4)]
    for weight, jump in [(g, l1), (g, l2), (kappa, za)]:
        adjoint = transpose(jump)
        gram = multiply(adjoint, jump)
        gain = multiply(multiply(jump, rho), adjoint)
        loss_left, loss_right = multiply(gram, rho), multiply(rho, gram)
        for i in range(4):
            for j in range(4):
                residual[i][j] += weight * (gain[i][j] - (loss_left[i][j] + loss_right[i][j]) / 2)
    require(all(value == 0 for row in residual for value in row), "exact rational full-matrix stationarity failed")
    epsilon = 1 - (p + s - 2 * w) / 2
    formula = (1 - b) / 2 + r * b * (b + 2) / (2 * (1 - b * b + 2 * r))
    require(epsilon == formula, "exact rational fidelity formula failed")
    require(p + s + 2 * q == 1, "exact rational normalization failed")
    require(q > 0 and p > 0 and s > 0 and p * s - w * w > 0, "exact rational positivity failed")
    return {
        "u": str(u),
        "v": str(v),
        "g": str(g),
        "kappa": str(kappa),
        "r": str(r),
        "b": str(b),
        "p00": str(p),
        "p01_p10": str(q),
        "p11": str(s),
        "coherence_00_11": str(w),
        "even_block_determinant": str(p * s - w * w),
        "infidelity": str(epsilon),
        "trace": "1",
        "full_matrix_stationarity_exact": True,
        "fidelity_formula_exact": True,
    }


def build_report() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "status": "passed",
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "tolerances": TOLERANCES,
        "vectorization": check_vectorization(),
        "pure_cases": [check_pure_case(delta0) for delta0 in [1e-1, 1e-2, 1e-3, 1e-4]],
        "noisy_cases": [check_noisy_case(r) for r in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8]],
        "rational_case": rational_example(),
    }


def reference_data(report: dict[str, Any]) -> dict[str, Any]:
    """Stable quantities retained in the checked-in reference output."""
    pure_keys = ["design_error", "g", "gamma_b", "beta_b", "gamma_over_design_error", "survival_at_one_slow_time", "zero_eigenvalues"]
    noisy_keys = ["r", "g", "optimal_b", "optimal_design_error", "optimal_infidelity", "infidelity_over_sqrt_r", "infidelity_over_sqrt_kappa_over_Gamma", "minimum_state_eigenvalue", "zero_eigenvalues"]
    return {
        "schema_version": 1,
        "vectorization": {
            key: report["vectorization"][key]
            for key in ["generator_shape", "matrix_units_checked", "complex_jumps_and_hamiltonian"]
        },
        "pure_cases": [{key: row[key] for key in pure_keys} for row in report["pure_cases"]],
        "noisy_cases": [{key: row[key] for key in noisy_keys} for row in report["noisy_cases"]],
        "rational_case": report["rational_case"],
    }


def check_reference(actual: Any, expected: Any, path: str = "reference") -> None:
    if isinstance(expected, dict):
        require(isinstance(actual, dict) and actual.keys() == expected.keys(), f"{path}: keys differ")
        for key in expected:
            check_reference(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        require(isinstance(actual, list) and len(actual) == len(expected), f"{path}: list length differs")
        for index, (value, target) in enumerate(zip(actual, expected)):
            check_reference(value, target, f"{path}[{index}]")
    elif isinstance(expected, float):
        require(np.isclose(actual, expected, rtol=TOLERANCES["reference_rtol"], atol=TOLERANCES["reference_atol"]), f"{path}: {actual!r} != {expected!r} within tolerance")
    else:
        require(actual == expected, f"{path}: {actual!r} != {expected!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="also write the full JSON report to this path")
    args = parser.parse_args()
    report = build_report()
    expected_path = Path(__file__).with_name("expected_results.json")
    expected = json.loads(expected_path.read_text())
    check_reference(reference_data(report), expected)
    report["reference_output_matches"] = True
    encoded = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if args.report is not None:
        args.report.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
