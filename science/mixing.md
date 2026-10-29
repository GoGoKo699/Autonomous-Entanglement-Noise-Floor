# A worst-input mixing-time lower bound

This note derives an operational lower bound on preparation by a fixed autonomous Lindblad generator. The argument uses a stationary state close to a maximally entangled target to identify an observable whose expectation can change only slowly. It applies even when the coherent Hamiltonian has unrestricted strength.

## Model and mixing convention

Use the model and norm budget of [rigidity.md](rigidity.md): the two full factors have equal finite dimension $`d\ge2`$,

```math
\mathcal L(\rho)
=-i[H,\rho]+\sum_\mu\mathcal D[J_\mu](\rho),
\qquad
J_\mu=A_\mu\otimes I+I\otimes B_\mu,
\qquad
K=\sum_\mu\|J_\mu\|_{\mathrm{op}}^2,
```

with the dissipator convention

```math
\mathcal D[J](\rho)
=J\rho J^\dagger-\frac12\{J^\dagger J,\rho\}.
```

Let $`\mathcal T_t:=e^{t\mathcal L}`$ be its completely positive, trace-preserving semigroup. Fix a stationary density operator $`\rho_*`$ and a maximally entangled vector $`|\Phi\rangle`$ across the full equal-dimensional factors. Define

```math
\epsilon:=1-\langle\Phi|\rho_*|\Phi\rangle,
\qquad
D_{\mathrm{tr}}(\rho,\sigma):=\frac12\|\rho-\sigma\|_1.
```

The worst-input distance at time $`t`$ is

```math
d_*(t):=
\sup_{\rho_0\in\mathsf D(\mathcal H)}
D_{\mathrm{tr}}\!\left(\mathcal T_t(\rho_0),\rho_*\right),
```

where $`\mathsf D(\mathcal H)`$ is the set of all density operators on the bipartite system.

If the dynamics does not converge to $`\rho_*`$ from every initial density operator, define $`t_{\mathrm{mix}}(a;\rho_*)=+\infty`$. Otherwise define, for $`0<a<1`$,

```math
t_{\mathrm{mix}}(a;\rho_*)
:=\inf\{t\ge0:d_*(t)\le a\}.
```

An empty infimum is $`+\infty`$. In finite dimension, convergence from every density operator is uniform over density operators: one can choose a finite spanning set of Hermitian matrices, express its elements as linear combinations of density operators, and apply convergence to the finitely many resulting basis images. Thus $`d_*(t)\to0`$ in the convergent case.

The distance envelope is nonincreasing. Indeed, stationarity and trace-distance contractivity imply, for $`s,t\ge0`$,

```math
\begin{aligned}
D_{\mathrm{tr}}\!\left(\mathcal T_{t+s}(\rho_0),\rho_*\right)
&=D_{\mathrm{tr}}\!\left(\mathcal T_s(\mathcal T_t(\rho_0)),\mathcal T_s(\rho_*)\right)\\
&\le D_{\mathrm{tr}}\!\left(\mathcal T_t(\rho_0),\rho_*\right).
\end{aligned}
```

Taking the supremum establishes $`d_*(t+s)\le d_*(t)`$. Once all inputs are within the specified tolerance, they remain within that tolerance under the same autonomous dynamics.

## Theorem

**Result R2: operational mixing obstruction.** If $`0<\epsilon\le1/16`$ and $`K>0`$, then

```math
\boxed{
t_{\mathrm{mix}}(1/4;\rho_*)
\ge\frac{11}{1024K\epsilon}
\ge\frac{1}{128K\epsilon}.
}
```

If $`K\epsilon=0`$ while $`0\le\epsilon\le1/16`$, then

```math
t_{\mathrm{mix}}(1/4;\rho_*)=+\infty.
```

The lower bound is independent of the norm and interaction structure of $`H`$. A product initial state is sufficient to witness it.

## Proof

### 1. A slowly varying observable

Let $`\lambda`$ be the largest eigenvalue of $`\rho_*`$, and let $`P=|\psi\rangle\langle\psi|`$ project onto its normalized eigenvector. The [rigidity theorem](rigidity.md#theorem) gives

```math
\lambda\ge1-\epsilon\ge\frac{15}{16},
\qquad
\|\mathcal L^\dagger(P)\|_{\mathrm{op}}\le64K\epsilon.
```

For any initial density operator $`\rho_0`$, set $`\rho_t:=\mathcal T_t(\rho_0)`$ and $`p(t):=\mathrm{Tr}(P\rho_t)`$. Finite-dimensional semigroup evolution is differentiable, so

```math
\frac{d}{dt}p(t)
=\mathrm{Tr}\!\left(P\mathcal L(\rho_t)\right)
=\mathrm{Tr}\!\left(\mathcal L^\dagger(P)\rho_t\right).
```

For every Hermitian operator $`X`$ and density operator $`\rho`$, $`|\mathrm{Tr}(X\rho)|\le\|X\|_{\mathrm{op}}`$. Hence

```math
\left|\frac{d}{dt}p(t)\right|\le64K\epsilon
```

at all times and for all initial states. This estimate does not assume that $`p(t)`$ is monotone.

### 2. An orthogonal product input exists

Choose any normalized $`|a\rangle\in\mathcal H_A`$, and define

```math
|v\rangle:=(\langle a|\otimes I_B)|\psi\rangle\in\mathcal H_B.
```

If $`|v\rangle=0`$, any normalized $`|b\rangle\in\mathcal H_B`$ satisfies $`\langle a,b|\psi\rangle=0`$. If $`|v\rangle\ne0`$, the condition $`d\ge2`$ guarantees a normalized $`|b\rangle`$ orthogonal to $`|v\rangle`$, with the same conclusion. Therefore the product state

```math
\rho_0=|a,b\rangle\langle a,b|
```

has $`p(0)=0`$. Integrating the observable-speed bound for this input gives

```math
p(t)\le64K\epsilon\,t.
```

### 3. Mixing requires a finite change in that observable

The stationary expectation is

```math
\mathrm{Tr}(P\rho_*)=\lambda.
```

For two density operators, the difference in the probabilities of any measurement effect is bounded by their half trace distance. In particular,

```math
|\mathrm{Tr}(P\rho_t)-\mathrm{Tr}(P\rho_*)|
\le D_{\mathrm{tr}}(\rho_t,\rho_*).
```

This convention is important: no extra factor of two occurs, because $`P`$ is an effect with $`0\le P\le I`$ and $`\rho_t-\rho_*`$ is traceless.

At any time at which every input lies within trace distance $`1/4`$ of $`\rho_*`$, the selected product input must therefore satisfy

```math
p(t)\ge\lambda-\frac14
\ge\frac{15}{16}-\frac14
=\frac{11}{16}.
```

Combining this necessary population change with the speed bound yields

```math
64K\epsilon\,t\ge\frac{11}{16},
\qquad
t\ge\frac{11}{1024K\epsilon}.
```

Every time appearing in the defining set for the mixing time obeys this inequality, so its infimum obeys it as well. If the convergence condition fails or the defining set is empty, the mixing time is infinite and the lower bound remains valid. Finally, $`11/1024\ge1/128`$ gives the stated simpler constant.

If $`K\epsilon=0`$, the rigidity theorem gives $`\mathcal L^\dagger(P)=0`$. The selected product input then has $`p(t)=0`$ at every time, whereas the stationary value is $`\lambda\ge15/16`$. Its trace distance from $`\rho_*`$ is consequently at least $`\lambda`$ for all times. It cannot converge to $`\rho_*`$, and $`t_{\mathrm{mix}}(1/4;\rho_*)=+\infty`$.

## What the bound establishes

The statement concerns convergence **from all inputs under one fixed autonomous generator** to its stationary state. It does not bound the time needed to prepare one known state by a prescribed time-dependent sequence of coherent gates. It also does not impose a bound on coherent dynamics inside the subspace orthogonal to $`|\psi\rangle`$.

The mixed-state rigidity proof inherits the spectral population balance from [Linowski, Rudnicki, and Gneiting, Section III, Eqs. (31)–(33)](../references/RELATED_WORK.md#linowski2023) and the local-sum maximally entangled identity from [Pocklington and Clerk](../references/RELATED_WORK.md#pocklington2024). The latter work establishes the corresponding pure-state dynamical obstruction. Here the approximately conserved observable is obtained from a generally mixed stationary state with small target infidelity, and the displayed bound follows directly by measuring its required change from a product input.

No dissipative spectral-gap bound is asserted. The proof uses a bounded rate of change of a specific observable and the operational worst-input mixing definition. It does not identify that rate with an eigenvalue of $`\mathcal L`$, assume normality, or infer a spectral gap by taking the reciprocal of a mixing time.
