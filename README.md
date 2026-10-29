# Autonomous Entanglement Noise Floor

**Unavoidable local dephasing imposes a square-root limit on the accuracy of
autonomous Bell-state stabilization at fixed engineered dissipative strength.**
The limit allows arbitrary static coherent control and mixed stationary
states. An explicit two-qubit reservoir attains the exponent.

The dynamics are time-independent and Markovian, with jump operators of the
form

```math
J_\mu=A_\mu\otimes I+I\otimes B_\mu.
```

For two qubits, an independent noise term $`\kappa\mathcal D[Z\otimes I]`$
remains present. The engineered budget is
$`\sum_{\mu\in\mathrm{eng}}\|J_\mu\|_{\mathrm{op}}^2\le\Gamma`$.
Writing the stationary Bell infidelity as
$`\epsilon=1-\langle\Phi|\rho_*|\Phi\rangle`$, the optimum over all
allowed globally relaxing generators satisfies

```math
\boxed{
\epsilon_{\mathrm{opt}}(\Gamma,\kappa)
=\Theta\!\left(\sqrt{\frac{\kappa}{\Gamma}}\right)
\quad\text{as }\kappa/\Gamma\to0.
}
```

The lower bound holds for every stationary state, including mixed states
and states of nonunique stationary dynamics. The upper bound is attained by
an [inherited squeezed-pair reservoir](references/RELATED_WORK.md#govia2022)
whose noisy stationary state is solved exactly and is globally attracting.
Its optimized error approaches $`\sqrt{3\kappa/\Gamma}`$; the globally
optimal prefactor is not determined.

## Why the error has a square root

Near a maximally entangled target, stationarity and the local-sum jump
structure force the total outgoing jump variance in the dominant stationary
eigenvector to be at most $`36K\epsilon^2`$, where
$`K=\sum_\mu\|J_\mu\|_{\mathrm{op}}^2`$ includes noise. Independent
dephasing contributes at least $`3\kappa/4`$ in the high-fidelity range.
Their comparison gives

```math
\epsilon\ge\sqrt{\frac{\kappa}{48(\Gamma+\kappa)}}
\qquad (\epsilon\le1/16).
```

The argument bounds stationary probability flow directly. It does not
require an inverse-gap perturbation approximation or a bound on the
Hamiltonian's norm. The [physical account](science/interpretation.md)
explains how a small population outside the target and a small incoming
transition strength jointly limit repair.

## Read the science

Start with the [model, conventions and exact results](science/model.md).
The complete account is organized by topic:

| To inspect | Read |
|---|---|
| Stationary-state eigenvector control, spectral balance and quadratic outgoing variance | [Mixed-state rigidity](science/rigidity.md) |
| Compulsory dephasing, the sharp qubit law and a variance-normalized general-noise lower bound | [Noise floor](science/noise_floor.md) |
| A worst-input preparation-time lower bound with unrestricted coherent control | [Operational mixing](science/mixing.md) |
| The exact noisy state, its optimal parameter, uniqueness and convergence | [Attaining two-qubit reservoir](science/attaining_reservoir.md) |
| Budget normalization, physical mechanism and architectural boundaries | [Interpretation](science/interpretation.md) |
| Established ingredients, nearby results and experimental motivation | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Reproducible checks and their analytical limits | [Verification](verification/README.md) |

A second consequence applies in every equal finite local dimension:

```math
t_{\mathrm{mix}}(1/4)\ge\frac{1}{128K\epsilon}
\qquad (0<\epsilon\le1/16).
```

Here mixing is measured in half trace distance to the actual stationary
state, uniformly over all initial states. A product input witnesses the
lower bound. The noiseless two-qubit construction attains the same order
at fixed accuracy. This is an operational mixing result; no general
dissipative-gap theorem is inferred from it.

## Attribution and scope

The [pure-state time–entanglement obstruction](references/RELATED_WORK.md#pocklington2024),
the [spectral population-balance condition](references/RELATED_WORK.md#linowski2023),
and the [squeezed-pair construction](references/RELATED_WORK.md#govia2022)
are established ingredients. The account develops a quantitative
mixed-state variance bound and its optimized noise and mixing consequences.

The full-dimension converse requires maximal entanglement across the
**entire equal-dimensional local factors**. A Bell target in an enlarged
computational subspace, retained auxiliary memory, time-dependent feedback,
or more general effective jump operators changes the model. Microscopic
local bath coupling alone does not establish the required jump-operator
form. The strength budget counts actual jump norms; increasing squeezing
at fixed bare coupling can increase that budget.

The explicit sharp noise construction is two-qubit dephasing. The
general-dimensional and other-noise statements in the scientific account
are lower bounds with their stated hypotheses.

## Reproduce the checks

Using Python 3, install the pinned numerical dependencies and run:

```bash
python3 -m pip install -r requirements.txt
python3 verification/verify_reservoir.py
```

The [verification guide](verification/README.md) documents the checked
identities, numerical instances, tolerances and committed results. The
written proofs establish the universal converses and asymptotic statements;
finite computations check the explicit construction and its formulas.

[The LLM reading guide](llms.txt) maps scientific questions to the
authoritative files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
