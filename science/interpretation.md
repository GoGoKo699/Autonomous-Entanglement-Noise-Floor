# Physical meaning and resource boundaries

The [square-root noise law](noise_floor.md) concerns a practical control
question: once the available engineered dissipation has been fixed, can a
different static Hamiltonian or a different allowed reservoir maintain a Bell
state with an error proportional to the weak local noise rate? In the stated
two-qubit model, the answer is constrained by

```math
\epsilon_{\mathrm{opt}}
=\Theta\!\left(\sqrt{\frac{\kappa}{\Gamma}}\right).
```

The exponent holds after optimizing the stationary state as well as the
generator. In particular, the state is not assumed to remain an exact pure
dark state when noise is added.

## 1. Two suppressions in the stationary repair flux

Write the stationary state as its dominant eigenvector plus its orthogonal
remainder,

```math
\rho_* =\lambda|\psi\rangle\langle\psi|+R,
\qquad \mathrm{Tr}R=\eta.
```

High Bell fidelity implies both $`\eta\le\epsilon`$ and closeness of
$`|\psi\rangle`$ to the Bell target. After centering the jumps at
$`|\psi\rangle`$, the exact stationary balance is

```math
\lambda x^2
=\sum_\mu\langle L_\mu^\dagger\psi|R|L_\mu^\dagger\psi\rangle
\le\eta y^2.
```

Here $`x^2`$ is the outgoing jump variance and $`y^2`$ bounds the strength
of transitions into the dominant vector. This population balance is an
[established spectral stationarity condition](../references/RELATED_WORK.md#linowski2023).

At exact maximal entanglement, a local-sum jump has equal norms when acting
forward or backward on the target. That transpose identity is inherited
from the [pure-state obstruction](../references/RELATED_WORK.md#pocklington2024).
Near the target, the difference of the two norms is bounded by the vector's
distance from maximal entanglement and the total jump budget. Combining
this estimate with stationarity yields

```math
y^2=O(K\epsilon),
\qquad x^2=O(K\epsilon^2).
```

The repair flux therefore contains two small factors. The population outside
the dominant eigenvector is at most order $`\epsilon`$, and the allowed
incoming transition strength is itself at most order $`K\epsilon`$.
An independent local dephaser still causes outgoing variance of order
$`\kappa`$. Balancing that unavoidable variance against the largest
possible repair flux forces $`\kappa=O(K\epsilon^2)`$.

This is a stationary argument. It does not require noise to overlap a
particular slow mode or require a perturbative inverse of a nonnormal
generator. Such assumptions would be needed to turn a heuristic
noise-rate-times-relaxation-time estimate into a universal statement.

## 2. What unrestricted coherent control can and cannot do here

The Hamiltonian commutator has zero diagonal expectation in an eigenvector
of $`\rho_*`$. It therefore cannot cancel the outgoing noise variance in
the stationary population equation. This explains why the fidelity converse
contains no bound on the Hamiltonian's norm.

For the separate mixing theorem, off-diagonal stationarity does matter.
After centering the jumps, it bounds $`(I-P)H_c|\psi\rangle`$ for the
gauge-adjusted Hamiltonian $`H_c`$ in terms of the same dissipative budget
and error, even if other matrix elements are arbitrarily large. This is a
bound in the centered representation; it need not hold separately for the
same block of the original supplied $`H`$.
The resulting observable-speed bound applies to an initial product state
orthogonal to $`|\psi\rangle`$ and proves a worst-input mixing obstruction.
The [full argument](mixing.md) controls this operational quantity directly.

Thus uncharged coherent strength is allowed by the mathematics. This does
not assert that arbitrarily strong laboratory driving leaves a microscopic
bath model unchanged. If increasing the drive changes the effective jump
operators, the resulting generator must be checked against the stated model
before applying the theorem.

## 3. Why the strength convention changes a scaling comparison

The physical jumps in a common squeezed-reservoir parameterization are
proportional to

```math
\sqrt\gamma\,
\bigl(\cosh s\,\sigma_A^-+\sinh s\,\sigma_B^+\bigr),
\qquad
\sqrt\gamma\,
\bigl(\cosh s\,\sigma_B^-+\sinh s\,\sigma_A^+\bigr).
```

Their summed squared operator norms are

```math
\Gamma=2\gamma\cosh(2s).
```

Holding $`\gamma`$ fixed while increasing the squeezing $`s`$ therefore
increases the resource charged here. A noise exponent expressed relative
to a fixed bare $`\gamma`$ is a different optimization problem.

The [normalized construction](attaining_reservoir.md) instead uses
$`u^2+v^2=1`$ and fixes $`\Gamma=2g`$ while changing the ratio of its
two amplitudes. Its exact error formula and the universal lower bound then
use the same budget. This normalization is also consistent with the
amplitude-rescaling discussion in [Govia et al.](../references/RELATED_WORK.md#govia2022).

The independent noise channel is kept as a separate additive dissipator.
Engineering an additional channel can provide repair, but the outgoing
variances of independent Lindblad terms add with nonnegative signs.
Interfering coherently with the *amplitude* of the background noise to
replace its jump operator changes that noise assumption.

At the level of scaling, maintaining a smaller error requires a
dissipation-to-noise ratio of order $`\epsilon^{-2}`$. This is a statement
about the specified generator resource, not a complete account of laboratory
power, cooling, bandwidth or fabrication cost.

## 4. Architectures and tasks that change the premises

The theorem distinguishes the full local Hilbert spaces from a selected
computational subspace. Its target is maximally entangled across complete
equal-dimensional factors. Adding a level while retaining a Bell target in
only a two-level subspace can create new dissipative pathways; that target
does not satisfy the full-space premise.

| Change | Why the present theorem does not decide the new problem |
|---|---|
| A qutrit–qubit system with a Bell target in a two-level subspace | The full local dimensions differ, and the qutrit marginal is not $`I_3/3`$. The equal-full-factor premise fails. |
| Retained auxiliary qubits, cavities or memory, with Bell fidelity measured only on a reduced target pair | The reduced target pair need not obey a closed, time-independent Markovian generator of the specified form. |
| Retained, history-dependent records or scheduled switching of generators | The allowed dynamics include memory or time dependence beyond the fixed generator. Instantaneous feedback whose unconditional dynamics still has the stated form remains covered. |
| Jump operators outside $`A\otimes I+I\otimes B`$ | The forward/backward norm identity that drives the converse need not hold. |
| Increasing the actual jump-norm budget while approaching maximal entanglement | The fixed-budget optimization has been changed. |

These boundaries have concrete precedents. The qutrit–qubit stabilization
scheme of [Brown et al.](../references/RELATED_WORK.md#brown2022) uses an
additional level. [Pocklington and Clerk](../references/RELATED_WORK.md#pocklington2025)
develop adaptive and auxiliary routes that evade the earlier pure-state
tradeoff. The present work does not claim those bypass mechanisms as new.

Local coupling in a microscopic Hamiltonian is also insufficient by itself
to establish the jump contract. In particular, the common-bath derivation
in Appendix F of [Pocklington and Clerk's 2024 paper](../references/RELATED_WORK.md#pocklington2024)
uses a bare system Hamiltonian of the form $`H_A+H_B`$. Secular decomposition
with interacting energy eigenstates can produce dressed jumps outside the
local-sum class. This observation is compatible with allowing arbitrary
$`H`$ inside a generator that already satisfies the operator contract.

## 5. Relation to experiments and to the pure-state tradeoff

Two recent remote-entanglement experiments study local-noise competition
in driven dissipative networks: [Irfan et al.](../references/RELATED_WORK.md#irfan2026)
analyze a cascaded network, and [Andres-Juanes et al.](../references/RELATED_WORK.md#andres2026)
use a nonlocal squeezed reservoir. Their noise analyses and optimization
within specific experimental families motivate asking which limitation
persists under broader reservoir and Hamiltonian design.

The stationary converse addresses that question under its exact effective
operator and resource assumptions. It is not a quantitative fit to those
experiments. In particular, a result stated in a high-fidelity asymptotic
regime should not be used as an accurate finite-parameter prediction at
moderate observed entanglement.

The earlier [pure-state theorem](../references/RELATED_WORK.md#pocklington2024)
already identifies maximal entanglement as a dynamical obstruction in this
class. The additions here are the quantitative mixed-state variance bound,
the resulting optimized noisy fidelity law, and a mixed-state operational
mixing bound. The [related-work account](../references/RELATED_WORK.md)
credits the spectral machinery and the attaining reservoir separately.

## 6. Established scope and open quantitative refinements

The sharp two-qubit statement determines the exponent of the optimal
dephasing error. It does not determine the best global prefactor: the
converse constants are conservative, while $`\sqrt3`$ is the leading
coefficient achieved by the explicit family at fixed $`\Gamma`$.

The general-dimension theorem supplies lower bounds near full maximal
entanglement. The matching construction used for the headline law is
two-qubit. A fixed local noise operator with nonzero target variance also
gives a lower bound, but a universal classification of attaining protocols
for every noise operator is not established.

The mixing theorem concerns fixed half-trace-distance accuracy and worst
initial state. A spectral-gap estimate, a complete finite-time target-fidelity
curve, and optimal performance from selected prepared inputs are different
quantities. The [verification account](../verification/README.md) identifies
the finite computations actually performed alongside these analytical limits.
