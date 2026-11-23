# Autonomous Entanglement Noise Floor

**How much nonlocal dissipation improves autonomous entanglement stabilization?**
With strictly local-sum engineered jumps, optimal stationary infidelity scales
as the square root of the noise-to-engineering ratio. A nonlocal component
changes that scaling when its amplitude exceeds the fourth root of the ratio.

The dynamics are time-independent and Markovian. The model charges the total
squared operator norm of the engineered jumps against $`\Gamma`$ and that of
their nonlocal components against $`\Gamma\delta^2`$.

```math
J_\mu=A_\mu\otimes I+I\otimes B_\mu+E_\mu,
\qquad
\sum_\mu\|J_\mu\|_{\mathrm{op}}^2\le\Gamma,
\qquad
\sum_\mu\|E_\mu\|_{\mathrm{op}}^2\le\Gamma\delta^2.
```

Write $`f=\kappa/\Gamma`$ for the strength of fixed additive noise relative
to the engineered budget. At fixed equal local dimension and for noise
with positive jump variance at the maximally entangled target, the optimal
stationary infidelity satisfies

```math
\boxed{
\epsilon_{\mathrm{opt}}
=\Theta\!\left(\min\left\{\sqrt f,\frac{f}{\delta^2}\right\}\right)
\quad\text{as } f\to0.
}
```

The bound is uniform in $`0\le\delta\le1`$. At $`\delta=0`$ use the
square-root branch. The converse allows arbitrary static coherent control
and all stationary states, including mixed states. A tilted local-sum
reservoir and a weak nonlocal reset attain the two regimes. See the
[crossover proof](science/locality-crossover.md) for the precise model.

## Why the error has a square root

When the target infidelity is $`\epsilon`$, the population outside the
dominant stationary eigenvector is at most $`\epsilon`$. The local-sum
geometry and the nonlocality budget limit how quickly that population can
refill the dominant state. Stationary balance requires
$`\kappa\lesssim\Gamma\epsilon(\epsilon+\delta^2)`$ for fixed noise and
small infidelity. The two terms in the repair rate are comparable at
$`\delta\asymp f^{1/4}`$.

For two qubits with local dephasing $`\kappa\mathcal D[Z\otimes I]`$ and
strict local-sum engineering, the converse gives an explicit bound.

```math
\epsilon\ge\sqrt{\frac{\kappa}{48(\Gamma+\kappa)}}
\qquad (\epsilon\le1/16).
```

The exact [squeezed-pair example](science/attaining_reservoir.md) attains
the square-root order, with optimized family error asymptotic to
$`\sqrt{3\kappa/\Gamma}`$. The global optimal prefactor is open.

## Read the science

Start with the [model, conventions and exact results](science/model.md).

| Question | Account |
|---|---|
| How much departure from local-sum jumps changes the optimal error? | [Locality crossover](science/locality-crossover.md) |
| How does stationarity constrain the dominant eigenvector and jump variance? | [Mixed-state rigidity](science/rigidity.md) |
| What are the explicit strict-local bounds for dephasing and other local noise? | [Noise floor](science/noise_floor.md) |
| What constrains the worst-input preparation time with unrestricted coherent control? | [Operational mixing](science/mixing.md) |
| What does the exact two-qubit stationary state look like? | [Attaining two-qubit reservoir](science/attaining_reservoir.md) |
| How do the resource convention and architecture affect the comparison? | [Interpretation](science/interpretation.md) |
| Which ingredients and comparison results come from prior work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Which finite cases and identities were checked? | [Verification](verification/README.md) |

The strict local-sum model also gives the worst-input mixing bound
$`t_{\mathrm{mix}}(1/4)\ge 1/(128K\epsilon)`$ for
$`0<\epsilon\le1/16`$ and total squared jump norm $`K>0`$. The distance
is half trace distance to the actual stationary state. A noiseless
two-qubit construction attains this order at fixed accuracy.

## Attribution and scope

The [pure-state time–entanglement obstruction and dark-state jumps](references/RELATED_WORK.md#pocklington2024),
[spectral population balance](references/RELATED_WORK.md#linowski2023),
and [squeezed-pair reservoir](references/RELATED_WORK.md#govia2022) give
the starting ingredients. The project develops a mixed-state converse
and determines the stationary error as the allowed nonlocality varies.

The target is maximally entangled across the entire equal-dimensional
local factors. The budgets are for effective jump operators in a declared
representation. Applying the result to a microscopic bath model requires
deriving those effective jumps and their norms.

## Learn the project

The single educational anchor is **Ángel Rivas and Susana F. Huelga,
*Open Quantum Systems: An Introduction* (2012)**. The
[source-to-project bridge](learning/RIVAS_HUELGA_BRIDGE.md) uses the freely
available [author preprint, version 2](https://arxiv.org/html/1104.5242v2).
It connects norms, completely positive maps, Lindblad generators and
relaxation to stationary balance, the exact example and the crossover.

The [30-milestone understanding map](learning/MILESTONES.md) follows the
proof from the foundations to the two regimes. Each milestone gives a
question, an understanding target, dependencies and source pointers.

## Reproduce the checks

```bash
python3 -m pip install -r requirements.txt
python3 verification/verify_reservoir.py
python3 verification/verify_locality_crossover.py
```

The [verification guide](verification/README.md) specifies the test cases,
tolerances and committed results. Finite calculations check the
constructions. The written proofs establish the general bounds.

[The LLM reading guide](llms.txt) maps scientific questions to the
authoritative files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
