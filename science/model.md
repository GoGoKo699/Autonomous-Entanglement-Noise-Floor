# Model and results

An engineered environment can drive two qubits into an entangled stationary
state without monitoring and correcting them after every error. The relevant
resource question is how accurately that state can be maintained when an
independent local noise process remains present. Coherent control, reservoir
design and the stationary state are all allowed to vary here; the total
engineered dissipative strength is fixed.

The main result is a square-root law for the smallest stationary Bell-state
error under compulsory local dephasing. It follows from a quantitative
restriction on the noise variance of any stationary state close to full
maximal entanglement. A separate consequence bounds the time needed to mix
uniformly over initial states. The [attaining reservoir](attaining_reservoir.md)
makes both resource scalings explicit.

## 1. Dynamics and the resource convention

Let $`\mathcal H_A\simeq\mathcal H_B\simeq\mathbb C^d`$, with finite
$`d\ge2`$. The dynamics act on these complete local factors. Fix a maximally
entangled unit vector $`|\Phi\rangle`$ and consider

```math
\begin{aligned}
\dot\rho&=\mathcal L(\rho)
 =-i[H,\rho]+\sum_{\mu=1}^{m}\mathcal D[J_\mu](\rho),\\
\mathcal D[J](\rho)&=J\rho J^\dagger
 -\frac12\{J^\dagger J,\rho\},\\
J_\mu&=A_\mu\otimes I+I\otimes B_\mu,\\
K&=\sum_{\mu=1}^{m}\|J_\mu\|_{\mathrm{op}}^2.
\end{aligned}
```

The Hamiltonian $`H`$ is any Hermitian operator on $`AB`$, including
interactions. There is no bound on its norm. The finite list of jump operators
is time independent and has the displayed **local-sum form**. Individual
$`A_\mu`$ and $`B_\mu`$ need not be Hermitian, normal or traceless. We set
$`\hbar=1`$. The quantities $`K`$, $`\Gamma`$ and $`\kappa`$ below have units
of inverse time.

The budget refers to a declared jump representation. A generator can have
several Lindblad representations, and their sums of operator norms need not
coincide. A bound stated for an admissible representation applies whenever
such a representation with the advertised budget exists. Scalar shifts of
jumps can be absorbed into $`H`$; in the proof this changes the estimate to
$`\sum_\mu\|L_\mu\|^2\le4K`$, rather than silently redefining the budget.
We do not identify $`K`$ with an unspecified microscopic coupling or linewidth.

The form of the **effective jump operators** is an assumption. A microscopic
model with local couplings to a bath can yield dressed operators outside this
class after eliminating interacting degrees of freedom. The model therefore
does not cover every system described informally as locally coupled to a
common environment. See the [physical interpretation](interpretation.md).

## 2. Fidelity and mixing

Let $`\rho_*`$ be any stationary state:

```math
\mathcal L(\rho_*)=0,
\qquad F=\langle\Phi|\rho_*|\Phi\rangle,
\qquad \epsilon=1-F.
```

This is the overlap fidelity with a pure target. The state $`\rho_*`$ may be
mixed, and the stationary-state statements do not assume uniqueness or
convergence. Their quantitative high-fidelity range is
$`0\lt\epsilon\le1/16`$. The exactly maximally entangled endpoint is treated
separately in the [rigidity argument](rigidity.md).

For the mixing statement use half trace distance. If all initial states
converge to $`\rho_*`$, define

```math
D_{\mathrm{tr}}(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
\qquad
t_{\mathrm{mix}}(\delta)
=\inf\left\{t\ge0:
 \sup_\rho D_{\mathrm{tr}}(e^{t\mathcal L}(\rho),\rho_*)\le\delta\right\}.
```

If all-input convergence fails, set $`t_{\mathrm{mix}}(\delta)=+\infty`$;
an empty defining set also has infinite infimum. Contractivity and stationarity
make the supremum nonincreasing in time. This definition concerns a fixed
accuracy relative to the actual stationary state, uniformly over inputs.
It does not measure a specially prepared input's convergence time or the
time to achieve target error $`\epsilon`$ from every input.

## 3. Quantitative mixed-state rigidity

Because $`F\ge1-\epsilon`$, the largest eigenvalue $`\lambda`$ of
$`\rho_*`$ is at least $`1-\epsilon`$ and is simple in this range. Choose its
unit eigenvector $`|\psi\rangle`$ and set

```math
P=|\psi\rangle\langle\psi|,
\quad L_\mu=J_\mu-\langle\psi|J_\mu|\psi\rangle I,
\quad x^2=\sum_\mu\|L_\mu\psi\|^2,
\quad y^2=\sum_\mu\|L_\mu^\dagger\psi\|^2.
```

**Result R1: stationary outgoing variance.** For the model above,

```math
x^2\le36K\epsilon^2,
\qquad y^2\le32K\epsilon.
```

Here $`x^2`$ is the total jump variance in $`|\psi\rangle`$; it is unaffected
by scalar shifts of the individual jumps. The quadratic dependence on
$`\epsilon`$ is the ingredient that constrains unavoidable noise. The proof
uses the inherited spectral population balance and the local-sum transpose
identity, with their attributions given in [rigidity](rigidity.md).

**Result R2: operational mixing obstruction.** If $`K>0`$,

```math
\|\mathcal L^\dagger(P)\|_{\mathrm{op}}\le64K\epsilon,
\qquad
t_{\mathrm{mix}}(1/4)\ge\frac{1}{128K\epsilon}.
```

This holds even with unrestricted $`H`$: after centering the jumps,
stationarity bounds the corresponding block of the gauge-adjusted
Hamiltonian $`H_c`$. The proof
exhibits an initial product state orthogonal to $`|\psi\rangle`$ and bounds
the velocity of its $`P`$ probability. It makes no general dissipative-gap
claim. A two-qubit family attains the $`1/(K\epsilon)`$ order for fixed
mixing accuracy in the noiseless case; see [mixing](mixing.md) and the
[construction](attaining_reservoir.md).

## 4. Compulsory dephasing and optimal Bell error

For the noise-floor statements take $`\kappa>0`$ and $`\Gamma\ge0`$.
For the sharp qubit law take $`d=2`$, $`Z=|0\rangle\langle0|-|1\rangle\langle1|`$
and $`Z_A=Z\otimes I`$. Consider

```math
\mathcal L(\rho)=-i[H,\rho]
 +\sum_{\mu\in\mathrm{eng}}\mathcal D[J_\mu](\rho)
 +\kappa\mathcal D[Z_A](\rho),
\qquad
\sum_{\mu\in\mathrm{eng}}\|J_\mu\|_{\mathrm{op}}^2\le\Gamma.
```

The noise term is additive and independent of the engineered channels.
Its physical jump $`\sqrt\kappa Z_A`$ remains in the representation, so the
total budget satisfies $`K\le\Gamma+\kappa`$. The convention means that this
term alone damps a coherence between the two eigenvalues of $`Z_A`$ at rate
$`2\kappa`$.

**Result R3: stationary noise floor.** Every stationary state with
$`\epsilon\le1/16`$ obeys

```math
\epsilon\ge
\sqrt{\frac{\kappa}{48(\Gamma+\kappa)}}.
```

An unconditional version is

```math
\epsilon\ge\min\left\{\frac1{16},
 \sqrt{\frac{\kappa}{48(\Gamma+\kappa)}}\right\}.
```

The same lower bound holds for even local dimension when the compulsory
local operator is a traceless Hermitian unitary. General local noise with
specified nonzero target variance has a related one-sided bound in
[noise_floor.md](noise_floor.md); a matching upper law for every such noise
operator is not asserted.

**Result R4: sharp qubit scaling.** For $`\Gamma>0`$ let
$`\epsilon_{\mathrm{opt}}(\Gamma,\kappa)`$ be the infimum of stationary
Bell infidelity over the allowed two-qubit generators that converge to a
unique stationary state from every initial state. Then

```math
\epsilon_{\mathrm{opt}}(\Gamma,\kappa)
=\Theta\!\left(\sqrt{\frac{\kappa}{\Gamma}}\right)
\quad\text{as }\kappa/\Gamma\longrightarrow0.
```

The lower bound even allows nonunique stationary states. For the upper bound,
an inherited squeezed-pair reservoir with engineered strength
$`\Gamma=2g`$ has an exactly solvable noisy stationary state. Optimizing this
family gives

```math
\epsilon_{\mathrm{family}}\sim\sqrt{\frac{3\kappa}{\Gamma}}.
```

This coefficient belongs to that family. The globally optimal numerical
coefficient is not determined here. The equality of orders in R4 concerns
the same two-qubit target, noise convention and engineered budget on both
sides.

## 5. Reading and verification routes

| Question | Authoritative account |
|---|---|
| Why does stationarity force quadratic outgoing variance? | [Mixed-state rigidity](rigidity.md) |
| How does compulsory noise turn that estimate into a fidelity limit? | [Noise floor](noise_floor.md) |
| Why can an arbitrarily strong Hamiltonian not make mixing arbitrarily fast? | [Operational mixing](mixing.md) |
| Which reservoir attains the exponents, and is its noisy state globally attracting? | [Exact two-qubit construction](attaining_reservoir.md) |
| What resource and architecture changes matter? | [Physical interpretation](interpretation.md) |
| Which ingredients are established and what comparison is supported? | [Related work](../references/RELATED_WORK.md) |
| Which finite identities and numerical instances were checked? | [Verification](../verification/README.md) |

The written arguments establish the universal statements. Finite calculations
check the explicit construction and algebraic ingredients; they do not turn
a sampled family into a universal converse.
