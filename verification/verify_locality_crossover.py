#!/usr/bin/env python3
"""Deterministic full-generator checks of the locality crossover constructions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import eigvals, expm, solve

from reservoir import superoperator, trace_distance, unvec, vec


GAMMA = 1.7
IDENTITY_TOLERANCE = 2e-12
ZERO_TOLERANCE = 1e-10
REFERENCE_RTOL = 5e-6
REFERENCE_ATOL = 5e-12


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def strength(jumps):
    return sum(np.linalg.norm(jump, ord=2) ** 2 for jump in jumps)


def local_reservoir(dimension, bias):
    diagonal = np.ones(dimension)
    diagonal[0] += bias * np.sqrt(dimension / 2)
    diagonal[1] -= bias * np.sqrt(dimension / 2)
    target = np.diag(diagonal).ravel() / np.linalg.norm(diagonal)
    identity = np.eye(dimension)
    jumps = []
    budget = 0.0
    for row in range(dimension):
        for column in range(dimension):
            if row == column:
                continue
            unit = np.zeros_like(identity)
            unit[row, column] = 1.0
            weight = diagonal[column] / diagonal[row]
            jumps.append(np.kron(unit, identity) - weight * np.kron(identity, unit.T))
            budget += 1 + weight**2
    require(abs(strength(jumps) - budget) < IDENTITY_TOLERANCE, "Unscaled local budget")
    scaled = [np.sqrt(GAMMA / budget) * jump for jump in jumps]
    require(abs(strength(scaled) - GAMMA) < IDENTITY_TOLERANCE, "Local strength budget")
    require(max(np.linalg.norm(jump @ target) for jump in scaled) < IDENTITY_TOLERANCE,
            "Local dark state")
    return superoperator(scaled) / GAMMA, target, budget


def reset_reservoir(dimension, bell):
    """Build the normalized complete reset, with physical budgets tested by its caller."""
    size = dimension**2
    identity = np.eye(size)
    basis = [
        identity[row * dimension + column]
        for row in range(dimension)
        for column in range(dimension)
        if row != column
    ]
    diagonal = identity[::dimension + 1]
    for index in range(1, dimension):
        basis.append((diagonal[:index].sum(axis=0) - index * diagonal[index])
                     / np.sqrt(index * (index + 1)))
    frame = np.array(basis).T
    complement = identity - np.outer(bell, bell)
    require(np.max(np.abs(frame @ frame.T - complement)) < IDENTITY_TOLERANCE,
            "Reset frame completes the target")
    jumps = [np.outer(bell, direction) / np.sqrt(size - 1) for direction in basis]
    generator = superoperator(jumps)
    require(np.linalg.norm(generator.conj().T @ vec(complement) + vec(complement) / (size - 1))
            < IDENTITY_TOLERANCE, "Reset complement-population identity")
    spectrum = eigvals(generator)
    expected = np.array([-1 / (size - 1)] * ((size - 1) ** 2)
                        + [-1 / (2 * (size - 1))] * (2 * (size - 1)) + [0])
    require(np.max(np.abs(np.sort(spectrum.real) - expected)) < IDENTITY_TOLERANCE
            and np.max(np.abs(spectrum.imag)) < IDENTITY_TOLERANCE, "Exact reset spectrum")
    return generator, jumps, complement


def spectral_gap(generator, zero_modes):
    values = eigvals(generator)
    zero = np.abs(values) < ZERO_TOLERANCE
    require(np.count_nonzero(zero) == zero_modes, "Unexpected number of stationary modes")
    require(np.all(values[~zero].real < -ZERO_TOLERANCE), "Nondecaying or unstable mode")
    return float(-np.max(values[~zero].real))


def stationary(generator, target):
    size = len(target)
    trace = vec(np.eye(size))
    require(np.linalg.norm(trace @ generator) < IDENTITY_TOLERANCE, "Trace conservation")
    normalized = generator / np.linalg.norm(generator, ord=np.inf)
    target_vector = vec(target)
    # Solve for the traceless correction to the target. Scaling keeps the
    # linear system well conditioned when the whole reset becomes weak.
    correction = solve(normalized + np.outer(target_vector, trace), -normalized @ target_vector)
    state = target + unvec(correction, size)
    residual = np.linalg.norm(generator @ vec(state))
    require(residual < IDENTITY_TOLERANCE, "Full stationary equation")
    require(abs(np.trace(state) - 1) < IDENTITY_TOLERANCE, "Stationary state trace")
    require(np.max(np.abs(state - state.conj().T)) < IDENTITY_TOLERANCE,
            "Stationary state Hermiticity")
    require(np.min(np.linalg.eigvalsh(state)) >= -IDENTITY_TOLERANCE,
            "Stationary state positivity")
    return state, float(residual)


def check_relaxation(generator, state, gap):
    size = len(state)
    basis = np.eye(size, dtype=complex)
    initial_vectors = (basis[1], (basis[0] + 1j * basis[1]) / np.sqrt(2))
    propagator = expm(16 * generator / gap)
    distances = []
    for initial in initial_vectors:
        density = np.outer(initial, initial.conj())
        evolved = unvec(propagator @ vec(density), size)
        require(np.max(np.abs(evolved - evolved.conj().T)) < IDENTITY_TOLERANCE,
                "Propagation Hermiticity")
        distances.append(trace_distance(evolved, state))
    require(max(distances) < 1e-6, "Time evolution has not approached the stationary state")
    return max(distances)


def check_dimension(dimension):
    size = dimension**2
    bell = np.eye(dimension).ravel() / np.sqrt(dimension)
    target = np.outer(bell, bell)
    local_noise = np.zeros((dimension, dimension))
    local_noise[0, 1] = 1
    bright = np.zeros(size, dtype=complex)
    bright[1], bright[dimension] = 1 / np.sqrt(2), 1j / np.sqrt(2)
    noises = {
        "local_relaxation": np.kron(local_noise, np.eye(dimension)),
        "nonlocal_leakage": np.outer(bright, bell),
    }
    residuals = {"stationarity": [], "trace_distance_after_16_inverse_gaps": []}

    zero, _, unscaled_budget = local_reservoir(dimension, 0.0)
    require(abs(unscaled_budget - 2 * dimension * (dimension - 1)) < IDENTITY_TOLERANCE,
            "Unbiased strength identity")
    require(np.linalg.norm(zero - zero.conj().T) < IDENTITY_TOLERANCE,
            "Unbiased Hilbert-Schmidt symmetry")
    require(spectral_gap(zero, zero_modes=2) > 1e-3, "Unbiased fast spectrum")

    beta = 4 / ((dimension - 1) * (size - 1))
    gap_ratios = []
    biases = (0.08, 0.04, 0.02)
    for bias in biases:
        generator, dark, _ = local_reservoir(dimension, bias)
        expected_overlap = 1 / (1 + bias**2)
        require(abs(abs(np.vdot(bell, dark)) ** 2 - expected_overlap) < IDENTITY_TOLERANCE,
                "Exact dark-state target overlap")
        gap_ratios.append(spectral_gap(generator, zero_modes=1) / (beta * bias**2))
    require(abs(gap_ratios[-1] - 1) < 0.005, "Local gap coefficient")

    reset, reset_jumps, complement = reset_reservoir(dimension, bell)
    noise_results = {}
    noise_ratios = (1e-6, 1e-8, 1e-10)
    for name, jump in noises.items():
        noise = superoperator([jump])
        variance = float(np.linalg.norm(complement @ jump @ bell) ** 2)
        require(variance > 0, "Positive outgoing noise variance")
        normalized_local = []
        normalized_reset = []
        for ratio in noise_ratios:
            bias = (ratio * variance / beta) ** 0.25
            local, _, _ = local_reservoir(dimension, bias)
            full_local = local + ratio * noise
            local_state, residual = stationary(full_local, target)
            residuals["stationarity"].append(residual)
            local_gap = spectral_gap(full_local, zero_modes=1)
            local_error = np.trace(complement @ local_state).real
            normalized_local.append(float(local_error / (2 * np.sqrt(ratio * variance / beta))))
            if ratio == noise_ratios[0]:
                residuals["trace_distance_after_16_inverse_gaps"].append(
                    check_relaxation(full_local, local_state, local_gap)
                )

            # Evaluate the crossover scale and a fixed nonlocal budget.
            row = []
            for defect in (ratio**0.25, 0.2):
                physical = [np.sqrt(GAMMA) * defect * reset_jump for reset_jump in reset_jumps]
                used = strength(physical)
                require(abs(used - GAMMA * defect**2) < IDENTITY_TOLERANCE
                        and used <= GAMMA, "Reset strength and nonlocal deviation budget")
                full_reset = defect**2 * reset + ratio * noise
                reset_state, residual = stationary(full_reset, target)
                residuals["stationarity"].append(residual)
                reset_gap = spectral_gap(full_reset, zero_modes=1)
                reset_rate = defect**2 / (size - 1)
                reset_error = np.trace(complement @ reset_state).real
                source = np.vdot(vec(complement), noise @ vec(reset_state)).real
                require(np.isclose(reset_rate * reset_error, ratio * source, rtol=1e-6, atol=2e-16),
                        "Exact noisy reset population balance")
                row.append(float(reset_error / (ratio * variance / reset_rate)))
                if ratio == noise_ratios[0] and defect == 0.2:
                    residuals["trace_distance_after_16_inverse_gaps"].append(
                        check_relaxation(full_reset, reset_state, reset_gap)
                    )
            normalized_reset.append(row)
        require(abs(normalized_local[-1] - 1) < 0.025, "Optimized local noise coefficient")
        require(max(abs(value - 1) for value in normalized_reset[-1]) < 0.01,
                "Reset noise coefficient at both tested nonlocal budgets")
        noise_results[name] = {
            "variance_at_target": variance,
            "optimized_local_error_over_asymptotic": normalized_local,
            "reset_error_over_asymptotic": normalized_reset,
        }

    reference = {
        "local_gap_coefficient": beta,
        "biases": biases,
        "local_gap_over_asymptotic": gap_ratios,
        "noise_to_strength_ratios": noise_ratios,
        "reset_defects_in_each_row": ("f^(1/4)", 0.2),
        "noise_cases": noise_results,
    }
    return reference, {key: max(values) for key, values in residuals.items()}


def check_reference(actual, expected, path="reference"):
    if isinstance(expected, dict):
        require(actual.keys() == expected.keys(), f"{path}: keys differ")
        for key in expected:
            check_reference(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        require(len(actual) == len(expected), f"{path}: lengths differ")
        for index, target in enumerate(expected):
            check_reference(actual[index], target, f"{path}[{index}]")
    elif isinstance(expected, float):
        require(np.isclose(actual, expected, rtol=REFERENCE_RTOL, atol=REFERENCE_ATOL),
                f"{path}: {actual!r} differs from {expected!r}")
    else:
        require(actual == expected, f"{path}: {actual!r} differs from {expected!r}")


def run():
    reference = {"schema_version": 1, "engineered_strength": GAMMA, "dimensions": {}}
    residuals = {}
    for dimension in (2, 3, 4):
        reference["dimensions"][str(dimension)], residuals[str(dimension)] = check_dimension(dimension)
    return reference, residuals


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="also write the full JSON report to this path")
    args = parser.parse_args()
    reference, residuals = run()
    expected = json.loads(Path(__file__).with_name("locality_crossover_results.json").read_text())
    check_reference(reference, expected)
    report = {
        "schema_version": 1,
        "status": "passed",
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "reference_output_matches": True,
        "reference": reference,
        "maximum_residuals": residuals,
    }
    encoded = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if args.report is not None:
        args.report.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
