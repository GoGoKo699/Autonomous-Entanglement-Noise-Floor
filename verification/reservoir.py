"""Explicit two-qubit squeezed reservoir and independently usable formulas.

Basis order is |00>, |01>, |10>, |11>. Vectors of operators stack columns.
D[J](rho) = J rho J^dagger - {J^dagger J, rho}/2.
The engineered budget is Gamma=2*g; the compulsory noise is kappa*D[Z_A].
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import brentq

Matrix = NDArray[np.complex128]
I2 = np.eye(2, dtype=complex)
SM = np.array([[0, 1], [0, 0]], dtype=complex)
SP = SM.conj().T
Z = np.diag([1, -1]).astype(complex)
Z_A = np.kron(Z, I2)
PHI = np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2)
P_PHI = np.outer(PHI, PHI.conj())
P_ODD = np.diag([0, 1, 1, 0]).astype(complex)


def vec(matrix: Matrix) -> NDArray[np.complex128]:
    """Column vectorization, in Fortran order."""
    return np.asarray(matrix, dtype=complex).reshape(-1, order="F")


def unvec(vector: NDArray[np.complex128], dim: int = 4) -> Matrix:
    return np.asarray(vector, dtype=complex).reshape((dim, dim), order="F")


def projector(vector: NDArray[np.complex128]) -> Matrix:
    return np.outer(vector, vector.conj())


def amplitudes(b: float) -> tuple[float, float, float]:
    """Choose u>=v>=0 with 2*u*v=b and u^2+v^2=1."""
    if not 0 <= b <= 1:
        raise ValueError("b must lie in [0, 1]")
    a = float(np.sqrt((1 - b) * (1 + b)))
    u = float(np.sqrt((1 + a) / 2))
    # This expression avoids cancellation in 1-a when b is small.
    v = float(b / (2 * u))
    return u, v, a


def jumps(b: float, g: float = 1.0, kappa: float = 0.0) -> list[Matrix]:
    if g <= 0 or kappa < 0:
        raise ValueError("require g>0 and kappa>=0")
    u, v, _ = amplitudes(b)
    result = [
        np.sqrt(g) * (u * np.kron(SM, I2) + v * np.kron(I2, SP)),
        np.sqrt(g) * (u * np.kron(I2, SM) + v * np.kron(SP, I2)),
    ]
    if kappa > 0:
        result.append(np.sqrt(kappa) * Z_A)
    return result


def dissipator_action(jump: Matrix, matrix: Matrix) -> Matrix:
    gram = jump.conj().T @ jump
    return jump @ matrix @ jump.conj().T - (gram @ matrix + matrix @ gram) / 2


def generator_action(
    jump_operators: list[Matrix], matrix: Matrix, hamiltonian: Matrix | None = None
) -> Matrix:
    """Direct matrix action, separate from the Kronecker implementation."""
    out = np.zeros_like(matrix, dtype=complex)
    if hamiltonian is not None:
        out -= 1j * (hamiltonian @ matrix - matrix @ hamiltonian)
    for jump in jump_operators:
        out += dissipator_action(jump, matrix)
    return out


def adjoint_action(jump_operators: list[Matrix], observable: Matrix) -> Matrix:
    out = np.zeros_like(observable, dtype=complex)
    for jump in jump_operators:
        gram = jump.conj().T @ jump
        out += jump.conj().T @ observable @ jump
        out -= (gram @ observable + observable @ gram) / 2
    return out


def superoperator(
    jump_operators: list[Matrix], hamiltonian: Matrix | None = None
) -> Matrix:
    """Full generator using vec(A X B)=(B^T tensor A) vec(X)."""
    dim = jump_operators[0].shape[0]
    identity = np.eye(dim, dtype=complex)
    result = np.zeros((dim * dim, dim * dim), dtype=complex)
    if hamiltonian is not None:
        result -= 1j * (
            np.kron(identity, hamiltonian) - np.kron(hamiltonian.T, identity)
        )
    for jump in jump_operators:
        gram = jump.conj().T @ jump
        result += np.kron(jump.conj(), jump)
        result -= (np.kron(identity, gram) + np.kron(gram.T, identity)) / 2
    return result


def pure_vectors(b: float) -> tuple[NDArray[np.complex128], NDArray[np.complex128]]:
    u, v, _ = amplitudes(b)
    return np.array([u, 0, 0, -v], complex), np.array([v, 0, 0, u], complex)


def population_rates(b: float) -> tuple[float, float]:
    discriminant = np.sqrt(1 + 8 * b * b)
    beta = (3 + discriminant) / 2
    # Rationalized expression avoids subtracting nearly equal numbers.
    gamma = 4 * (1 - b) * (1 + b) / (3 + discriminant)
    return float(gamma), float(beta)


def survival(b: float, g: float, time: float, initial: str) -> float:
    gamma, beta = population_rates(b)
    slow, fast = np.exp(-g * gamma * time), np.exp(-g * beta * time)
    if initial == "bright":
        return float((beta * slow - gamma * fast) / (beta - gamma))
    if initial == "odd":
        a2 = (1 - b) * (1 + b)
        return float(((beta - a2) * slow + (a2 - gamma) * fast) / (beta - gamma))
    raise ValueError("initial must be 'bright' or 'odd'")


def noisy_state(b: float, r: float) -> Matrix:
    if r <= 0:
        raise ValueError("noisy_state requires r>0")
    u, v, a = amplitudes(b)
    denominator = a * a + 2 * r
    q = 2 * r * u * u * v * v / denominator
    w = -u * v * a * a / denominator
    return np.array(
        [
            [u * u * (a * a + 2 * r * u * u) / denominator, 0, 0, w],
            [0, q, 0, 0],
            [0, 0, q, 0],
            [w, 0, 0, v * v * (a * a + 2 * r * v * v) / denominator],
        ],
        dtype=complex,
    )


def infidelity(b: float, r: float) -> float:
    if r <= 0 or not 0 <= b <= 1:
        raise ValueError("require r>0 and b in [0,1]")
    return float((1 - b) / 2 + r * b * (b + 2) / (2 * ((1 - b) * (1 + b) + 2 * r)))


def optimizer_polynomial(b: float, r: float) -> float:
    return float(((1 - b) * (1 + b)) ** 2 + 2 * r * (1 - b - 3 * b * b) - 4 * r * r * b)


def optimal_b(r: float) -> float:
    """Unique global family optimum: Q_r strictly decreases across its root."""
    if r <= 0:
        raise ValueError("r must be positive")
    return float(brentq(lambda b: optimizer_polynomial(b, r), 0, 1, xtol=5e-15, rtol=1e-15))


def trace_distance(left: Matrix, right: Matrix) -> float:
    difference = left - right
    hermitian_part = (difference + difference.conj().T) / 2
    return float(np.sum(np.abs(np.linalg.eigvalsh(hermitian_part))) / 2)
