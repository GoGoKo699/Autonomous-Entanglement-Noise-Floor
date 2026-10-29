# From Rivas–Huelga to the autonomous entanglement noise floor

This bridge connects the language of open quantum systems to the repository's central question: at fixed dissipative strength, how close can an autonomous two-qubit steady state remain to a Bell state when local dephasing is unavoidable? The answer developed here is a square-root error law. Its origin is a stationary population balance: near maximal entanglement, the permitted jumps have very little capacity to replenish the desired state.

The educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_**, SpringerBriefs in Physics (2012), [book DOI](https://doi.org/10.1007/978-3-642-23354-8). All section, theorem, definition, and equation numbers attributed to the anchor below refer specifically to its freely available **[author preprint, arXiv:1104.5242v2, revised 9 February 2012](https://arxiv.org/abs/1104.5242v2)**: [HTML](https://arxiv.org/html/1104.5242v2) and [PDF](https://arxiv.org/pdf/1104.5242v2).

**Numbering matters.** The preprint includes an introductory §1. Its §§2–7 correspond to the book's six substantive chapters, numbered 1–6; the [publisher's contents](https://link.springer.com/book/10.1007/978-3-642-23354-8) lists them. A reference here to “preprint §5.4” should therefore be located by its subject in the book's fourth chapter, rather than read as a reference to the printed book's §5.4.

## Source map and division of contributions

| Preprint location | Foundation used here | Bridge destination |
|---|---|---|
| [§§2.1–2.3](https://arxiv.org/html/1104.5242v2) | Norms, exponentials, semigroups | [States and norms](#states-and-norms); [semigroups](#semigroups-and-adjoints) |
| [Opening of §4; §§4.2–4.3](https://arxiv.org/html/1104.5242v2) | Reduced states, complete positivity, trace-norm contraction | [States and norms](#states-and-norms); [maps and adjoints](#semigroups-and-adjoints) |
| [§5.2, especially Eq. (51)](https://arxiv.org/html/1104.5242v2) | Time-independent Lindblad generators | [Lindblad convention](#lindblad-and-gauge) |
| [§5.4, Definition 5.3 and Theorem 5.4](https://arxiv.org/html/1104.5242v2) | Relaxation and its finite-dimensional spectral criterion | [Stationarity](#stationarity-and-relaxation); [mixing](#mixing-versus-gap) |
| [§6.4.1](https://arxiv.org/html/1104.5242v2) | Multipartite weak-coupling models | [Resource and model conventions](#resource-conventions) |

The anchor supplies these foundations. The spectral population-balance identity is an inherited research ingredient from [Linowski, Rudnicki, and Gneiting, §III, Eqs. (31)–(33)](https://arxiv.org/html/2212.12245v2). The full-factor transpose identity and the pure-state obstruction connect to [Pocklington and Clerk, §III and Appendix A](https://arxiv.org/html/2404.03625v2). The worked reservoir is inherited from [Govia, Lingenfelter, and Clerk, Eqs. (8)–(9)](https://arxiv.org/html/2110.06201v2), also appearing in [Pocklington and Clerk, Eq. (7)](https://arxiv.org/html/2409.06012v2).

The repository's derivations combine these ingredients to obtain quantitative bounds for mixed stationary states, an operational mixing bound with arbitrary Hamiltonian, and the noise floor with a matching two-qubit construction. The anchor is not being cited as a source for those results. The [related-work account](../references/RELATED_WORK.md) gives the detailed comparison; the [milestone map](MILESTONES.md) indexes the dependencies.

## Notation and convention map

| Object | Anchor or general convention | Convention in this repository |
|---|---|---|
| State and evolution | $`\rho`$, dynamical map $`\mathcal E`$ | $`\rho_t=\mathcal T_t(\rho_0)`$, $`\mathcal T_t=e^{t\mathcal L}`$ |
| Generator | $`\mathcal L`$ acts on matrices | Calligraphic $`\mathcal L`$ is the generator; $`L_\mu`$ is one centered jump |
| Dissipative rate | Eq. (51) uses $`\gamma_k\mathcal D[V_k]`$ | The rate is absorbed: $`J_\mu=\sqrt{\gamma_\mu}V_\mu`$ |
| Dimensions | $`N`$ denotes a system dimension in the generator derivation | $`d`$ is each local dimension; the full system has dimension $`d^2`$ |
| Stationary state | $`\rho_{\mathrm{ss}}`$ | $`\rho_*`$; uniqueness is a separate property |
| Trace norm and distance | Trace norm measures a matrix's size | $`D_{\mathrm{tr}}(\rho,\sigma)=\frac12\Vert\rho-\sigma\Vert_1`$ includes the half |
| Target fidelity | Several fidelity conventions exist | $`F=\langle\Phi\vert\rho_*\vert\Phi\rangle`$, $`\epsilon=1-F`$; no outer square root |
| Leading eigenspace | Spectral decomposition of $`\rho_*`$ | $`P=\lvert\psi\rangle\langle\psi\rvert`$, largest eigenvalue $`\lambda`$, remainder weight $`\eta=1-\lambda`$ |
| Hamiltonian gauge | Equivalent Lindblad representations describe the same dynamics | $`H_c`$ accompanies centered jumps $`L_\mu`$; it need not equal the supplied $`H`$ |
| Total strength | A rate must be tied to a specified representation | $`K=\sum_\mu\Vert J_\mu\Vert_{\mathrm{op}}^2`$ counts the supplied physical jumps |
| Engine and noise | Separate physical channels | $`\Gamma`$ bounds engineered strength; $`\kappa\mathcal D[Z_A]`$ is compulsory noise |
| Qubit example | Parameters belong to that family | $`g=\Gamma/2`$, $`r=\kappa/g`$, $`\delta_0`$ is its noiseless Bell error |

All spaces in the project are finite dimensional. Set $`\hbar=1`$. Thus $`H`$, $`K`$, $`\Gamma`$, $`g`$, and $`\kappa`$ have units of inverse time, while jump operators have units of inverse square-root time.

<a id="states-and-norms"></a>
## 1. States, entanglement, and the norms that enter the proof

A density matrix is positive and has trace one. Its spectral decomposition describes a probability distribution over orthogonal pure states. This is useful here because a state with almost all its weight on one target must also have a large leading eigenvalue.

For complete equal-dimensional factors, choose local bases in which the target is

```math
|\Phi\rangle=\frac1{\sqrt d}\sum_{j=1}^d|j\rangle_A|j\rangle_B.
```

Each reduced state is $`I/d`$. The joint state is pure although either subsystem alone is maximally mixed. This property, rather than purity alone, gives the transpose relation used later. A Bell state encoded in two levels of a larger local system need not be maximally entangled across the complete factors.

Three matrix norms have distinct jobs:

```math
\begin{aligned}
\|X\|_{\mathrm{op}}&=\sup_{\|v\|=1}\|Xv\|,\\
\|X\|_{\mathrm{HS}}&=\sqrt{\mathrm{Tr}(X^\dagger X)},\\
\|X\|_1&=\mathrm{Tr}\sqrt{X^\dagger X}.
\end{aligned}
```

The operator norm bounds what a jump can do to any unit vector; this makes it suitable for the resource budget. The Hilbert–Schmidt norm appears when a bipartite vector is identified with a matrix. The trace norm compares states operationally.

For any measurement effect $`0\le E\le I`$,

```math
|\mathrm{Tr}[E(\rho-\sigma)]|
\le D_{\mathrm{tr}}(\rho,\sigma)
=\frac12\|\rho-\sigma\|_1.
```

Thus trace distance bounds the change in the probability of an event. The factor one-half matters when a measured population is used to prove a mixing-time bound. For a general Hermitian observable $`X`$, the convenient bound instead reads

```math
|\mathrm{Tr}[X(\rho-\sigma)]|
\le 2\|X\|_{\mathrm{op}}D_{\mathrm{tr}}(\rho,\sigma).
```

For two pure states, trace distance has the particularly simple form

```math
D_{\mathrm{tr}}(|\psi\rangle\langle\psi|,|\Phi\rangle\langle\Phi|)
=\sqrt{1-|\langle\Phi|\psi\rangle|^2}.
```

These identities explain why an infidelity of order $`\epsilon`$ gives vector and expectation-value errors of order $`\sqrt\epsilon`$. They do not make every quantity in the proof scale as $`\sqrt\epsilon`$: stationary population balance supplies an additional small factor.

The anchor's relevant starting points are preprint §2.1 and the opening discussion of reduced states in §4. The finite-dimensional calculations above specify the conventions used in this project.

<a id="semigroups-and-adjoints"></a>
## 2. Completely positive maps, semigroups, and adjoints

A physical channel preserves trace and positivity even when an untouched reference system is included. The latter requirement is complete positivity. In Kraus form,

```math
\mathcal T(\rho)=\sum_\alpha M_\alpha\rho M_\alpha^\dagger,
\qquad
\sum_\alpha M_\alpha^\dagger M_\alpha=I.
```

Complete positivity protects the positivity of correlated joint states under $`\mathcal T\otimes\mathrm{id}`$. It is stronger than testing the output on isolated-system states alone. The anchor develops this in preprint §4.2.

Autonomous time-independent dynamics form a semigroup:

```math
\mathcal T_0=\mathrm{id},
\qquad
\mathcal T_{t+s}=\mathcal T_t\mathcal T_s,
\qquad
\mathcal T_t=e^{t\mathcal L}.
```

The same generator governs every time interval. Scheduled changes of generator or retained history-dependent control can require a larger or time-dependent description. Instantaneous feedback remains covered if its unconditional dynamics still has the fixed generator and local-sum jumps specified below. The semigroup and exponential foundations are in preprint §§2.2–2.3; trace-norm contraction is treated in §4.3.

The adjoint moves dynamics from states to observables:

```math
\mathrm{Tr}[X\mathcal T_t(\rho)]
=\mathrm{Tr}[\mathcal T_t^\dagger(X)\rho],
\qquad
\frac{d}{dt}\mathrm{Tr}(X\rho_t)
=\mathrm{Tr}[\mathcal L^\dagger(X)\rho_t].
```

Trace preservation becomes $`\mathcal T_t^\dagger(I)=I`$, or $`\mathcal L^\dagger(I)=0`$. This dual description will let us bound how quickly the probability of a particular projector can change. A small $`\|\mathcal L^\dagger(P)\|_{\mathrm{op}}`$ directly limits that probability's speed for every input state.

<a id="lindblad-and-gauge"></a>
## 3. Lindblad convention and the centered Hamiltonian

The fixed generator considered here is

```math
\begin{aligned}
\mathcal L(\rho)&=-i[H,\rho]+\sum_\mu\mathcal D[J_\mu](\rho),\\
\mathcal D[J](\rho)&=J\rho J^\dagger-\frac12\{J^\dagger J,\rho\},\\
J_\mu&=A_\mu\otimes I+I\otimes B_\mu.
\end{aligned}
```

The first two lines use the convention of preprint §5.2, Eq. (51), with rates absorbed into the jumps. The last line is the project's structural assumption. A jump is a coherent sum of an action on $`A`$ and an action on $`B`$. Its dissipator includes cross terms, so the model can create entanglement. Neither local operator has to be Hermitian or normal. The Hamiltonian may include arbitrary interactions and has no imposed norm bound.

A scalar part of a jump can be moved into the Hamiltonian. For a chosen unit vector $`|\psi\rangle`$, define

```math
c_\mu=\langle\psi|J_\mu|\psi\rangle,
\qquad
L_\mu=J_\mu-c_\mu I,
\qquad
G_\mu=\frac{i}{2}(c_\mu^*J_\mu-c_\mu J_\mu^\dagger),
\qquad
H_c=H+\sum_\mu G_\mu.
```

Then $`\langle\psi|L_\mu|\psi\rangle=0`$. Expanding the dissipator shows the sign and normalization explicitly:

```math
\mathcal D[J_\mu](\rho)-\mathcal D[L_\mu](\rho)
=\frac12[c_\mu^*L_\mu-c_\mu L_\mu^\dagger,\rho]
=-i[G_\mu,\rho].
```

Consequently,

```math
\mathcal L(\rho)=-i[H_c,\rho]+\sum_\mu\mathcal D[L_\mu](\rho).
```

This is an elementary representation change, not a modification of the apparatus. It preserves the local-sum form: the scalar can be absorbed into $`A_\mu`$. The explicit $`H_c`$ formula is part of the repository's convention calculation, not a separately attributed theorem from the anchor.

The physical budget remains

```math
K=\sum_\mu\|J_\mu\|_{\mathrm{op}}^2.
```

Since $`|c_\mu|\le\|J_\mu\|_{\mathrm{op}}`$, the centered representation obeys

```math
C_0:=\sum_\mu\|L_\mu\|_{\mathrm{op}}^2\le4K.
```

Keeping this factor avoids silently changing the resource definition. A later estimate on one block of $`H_c`$ is also not an estimate on the corresponding block of the original $`H`$.

<a id="stationarity-and-relaxation"></a>
## 4. Stationarity, relaxation, and the dominant eigenvector

A stationary state satisfies $`\mathcal L(\rho_*)=0`$. Starting there leaves the state unchanged. Relaxation asks whether every initial state approaches the same stationary state. For example, a qubit dephasing channel leaves every diagonal density matrix stationary, so stationarity alone does not supply a preparation protocol.

Preprint §5.4 makes the distinction explicit. Definition 5.3 specifies convergence from all inputs; Theorem 5.4 gives the finite-dimensional criterion in terms of a simple zero eigenvalue and negative real parts for all remaining generator eigenvalues. The repository's universal stationary-state bound requires only stationarity. The attaining construction also establishes relaxation.

Suppose

```math
\langle\Phi|\rho_*|\Phi\rangle=1-\epsilon,
\qquad 0\le\epsilon\le\frac1{16}.
```

Let $`\lambda`$ be the largest eigenvalue, with normalized eigenvector $`|\psi\rangle`$. The variational principle gives $`\lambda\ge1-\epsilon`$. Decompose

```math
\rho_*=\lambda P+R,
\qquad P=|\psi\rangle\langle\psi|,
\qquad Q=I-P,
\qquad
RP=0,
\qquad
0\le R\le\eta Q,
\qquad
\eta=\mathrm{Tr}R=1-\lambda\le\epsilon.
```

Thus only $`\eta`$ of the stationary probability lies outside its leading eigendirection. The large separation between $`\lambda\ge15/16`$ and all other eigenvalues makes that direction unambiguous.

It is also close to the desired target. Set $`f=|\langle\Phi|\psi\rangle|^2`$. Then

```math
1-\epsilon
=\lambda f+\langle\Phi|R|\Phi\rangle
\le\eta+(1-2\eta)f,
\qquad
1-f\le\frac{\epsilon-\eta}{1-2\eta}\le\epsilon.
```

After aligning the overall phase of $`|\psi\rangle`$, let $`\delta_\psi=\|\psi-\Phi\|`$. It follows that

```math
\delta_\psi^2=2(1-\sqrt f)\le\frac{16}{15}\epsilon.
```

The formal proof uses $`\delta`$ for this vector distance; the subscript here keeps it distinct from the example's design error $`\delta_0`$ and a mixing accuracy. Likewise, target error $`\epsilon`$ and remainder weight $`\eta`$ are related but are not interchangeable.

<a id="spectral-balance-and-transpose"></a>
## 5. Spectral population balance and the transpose identity

Choose the centered jumps from Section 3 using this leading eigenvector. Define

```math
x^2=\sum_\mu\|L_\mu\psi\|^2,
\qquad
y^2=\sum_\mu\|L_\mu^\dagger\psi\|^2.
```

Both jump-output vectors are orthogonal to $`|\psi\rangle`$. The quantity $`x^2`$ measures outgoing transition strength from the leading direction. The quantity $`y^2`$ measures the strength of transitions into that direction before they are weighted by the population available elsewhere.

### Balance in an eigenbasis removes the Hamiltonian

Take the $`P`$ diagonal element of the stationarity equation. Because $`\rho_*|\psi\rangle=\lambda|\psi\rangle`$,

```math
\langle\psi|[H_c,\rho_*]|\psi\rangle=0.
```

This is why no bound on the Hamiltonian norm is needed for the population balance. For the dissipative part, centering and the decomposition of $`\rho_*`$ give

```math
\lambda x^2
=\sum_\mu\langle L_\mu^\dagger\psi|R|L_\mu^\dagger\psi\rangle
\le\eta y^2.
```

The exact equality is the inherited spectral-balance ingredient identified in [Linowski et al., Eqs. (31)–(33)](https://arxiv.org/html/2212.12245v2). Stationarity requires the populated leading direction's loss to be replenished by the small remainder. It follows that

```math
x\le\sqrt{\frac{\eta}{\lambda}}\,y.
```

For generic jumps this alone would give only a bound of order $`K\epsilon`$ on $`x^2`$. Maximal entanglement and local-sum jumps supply another restriction.

### Maximal entanglement relates incoming and outgoing strength

Use the vectorization convention

```math
\mathrm{vec}(C)=\sum_{i,j}C_{ij}|i\rangle_A|j\rangle_B.
```

For $`L=A\otimes I+I\otimes B`$, direct expansion yields

```math
L|\Phi\rangle=\frac1{\sqrt d}\mathrm{vec}(A+B^{\mathsf T}),
\qquad
L^\dagger|\Phi\rangle
=\frac1{\sqrt d}\mathrm{vec}\bigl((A+B^{\mathsf T})^\dagger\bigr).
```

A matrix and its adjoint have the same Hilbert–Schmidt norm. Hence

```math
\|L\Phi\|=\|L^\dagger\Phi\|.
```

The identity does not assume that $`|\Phi\rangle`$ is dark, that $`L`$ is Hermitian, or that $`L`$ is normal. It is the algebraic ingredient behind the pure-state obstruction discussed by [Pocklington and Clerk](https://arxiv.org/html/2404.03625v2). Its applicability depends on full maximal entanglement across the complete factors.

At the exact endpoint $`\rho_*=|\Phi\rangle\langle\Phi|`$, balance gives $`x=0`$, and the identity gives $`y=0`$. There is then neither outgoing nor incoming dissipative transfer through that direction. The project quantifies how this obstruction persists when the stationary state is mixed and only approximately maximally entangled.

<a id="mixed-state-rigidity"></a>
## 6. Why two small factors give quadratic outgoing variance

Apply the triangle inequality to the direct sum of the vectors produced by all jumps. Replacing $`\psi`$ with $`\Phi`$, using the transpose identity, and replacing $`\Phi`$ with $`\psi`$ again costs at most $`2\sqrt{C_0}\delta_\psi`$:

```math
y\le x+2\sqrt{C_0}\delta_\psi.
```

Together with population balance, this implies

```math
y\le
\frac{2\sqrt{C_0}\delta_\psi}
{1-\sqrt{\eta/\lambda}}.
```

The denominator stays bounded away from zero because $`\eta\le1/16`$ and $`\lambda\ge15/16`$. Using $`C_0\le4K`$ and the vector-distance estimate gives the conservative explicit bounds

```math
\boxed{
y^2\le32K\epsilon,
\qquad
x^2\le\frac{\eta}{\lambda}y^2
\le36K\epsilon^2.
}
```

There are two separate reasons for the second power of error:

1. Only $`\eta=O(\epsilon)`$ of the stationary population is available outside the leading eigendirection.
2. The total incoming transition strength itself is at most $`y^2=O(K\epsilon)`$, because the nearby maximally entangled state enforces equality of incoming and outgoing strengths.

Their product bounds the outgoing variance. This is a statement about stationary fluxes; it does not require an estimate of the inverse dissipative gap.

The outgoing quantity can be written in the supplied physical representation:

```math
x^2=\sum_\mu\left(
\langle\psi|J_\mu^\dagger J_\mu|\psi\rangle
-|\langle\psi|J_\mu|\psi\rangle|^2
\right).
```

Each summand is nonnegative. Scalar centering has exposed a variance that was already present in the generator's physical channels. This observation makes an independent compulsory noise process particularly restrictive.

This is Result R1. The [rigidity proof](../science/rigidity.md) gives all constants, the exact endpoint, and the additional Hamiltonian-block estimates used for mixing.

<a id="noise-floor"></a>
## 7. Turning the variance bound into a square-root noise floor

For qubits, let $`Z=|0\rangle\langle0|-|1\rangle\langle1|`$ and $`Z_A=Z\otimes I`$. Include an independent physical noise jump

```math
J_0=\sqrt\kappa\,Z_A,
\qquad \kappa>0.
```

A maximally entangled state's local marginal is maximally mixed, so $`\langle Z_A\rangle_\Phi=0`$. From $`D_{\mathrm{tr}}(P,|\Phi\rangle\langle\Phi|)\le\sqrt\epsilon`$,

```math
|\langle Z_A\rangle_\psi|\le2\sqrt\epsilon.
```

Since $`Z_A^2=I`$, this noise channel alone contributes

```math
\|L_0\psi\|^2
=\kappa\left(1-\langle Z_A\rangle_\psi^2\right)
\ge\kappa(1-4\epsilon)
\ge\frac{3\kappa}{4}.
```

This loss cannot be canceled by a negative variance from another independent dissipator: all the variance terms are nonnegative. Combining it with Result R1 gives

```math
\frac{3\kappa}{4}\le x^2\le36K\epsilon^2,
\qquad
\epsilon\ge\sqrt{\frac{\kappa}{48K}}.
```

If the engineered jumps satisfy $`\sum_{\mu\in\mathrm{eng}}\|J_\mu\|_{\mathrm{op}}^2\le\Gamma`$, the supplied representation has $`K\le\Gamma+\kappa`$. Therefore Result R3 is

```math
\boxed{
\epsilon\ge
\sqrt{\frac{\kappa}{48(\Gamma+\kappa)}}
\quad\text{for }\epsilon\le\frac1{16}.
}
```

For arbitrary error, the valid statement is the minimum of this expression and $`1/16`$. The high-fidelity estimate must not be extended outside its stated range without that qualification.

For $`\kappa/\Gamma\ll1`$, the lower bound has order $`\sqrt{\kappa/\Gamma}`$. This is stronger than a linear error estimate in that regime. Physically, the engine's capacity to restore the leading direction vanishes as maximal entanglement is approached, while the local noise retains a finite variance there.

The bound applies to every stationary state in the model, even if it is not unique or attractive. The next example establishes the matching order using an actual relaxing reservoir. The [noise-floor proof](../science/noise_floor.md) also treats other local noise operators with nonzero target variance, but does not claim a matching construction for every noise model.

<a id="exact-qubit-family"></a>
## 8. Exact two-qubit example: design error versus noise sensitivity

Consider the inherited squeezed-pair family, normalized to make the resource accounting explicit:

```math
\begin{aligned}
J_1&=\sqrt g\,(u\sigma_A^-+v\sigma_B^+),\\
J_2&=\sqrt g\,(u\sigma_B^-+v\sigma_A^+),\\
H&=0,\qquad u,v>0,\qquad u^2+v^2=1.
\end{aligned}
```

Here $`\sigma^-=|0\rangle\langle1|`$. Each jump has squared operator norm $`g`$, so $`\Gamma=2g`$. The reservoir's form is inherited from [Govia et al.](https://arxiv.org/html/2110.06201v2) and [Pocklington and Clerk](https://arxiv.org/html/2409.06012v2); the exact noisy calculation below is presented in the repository's [construction](../science/attaining_reservoir.md).

### Noiseless state and the weakening repair process

The two jumps annihilate

```math
|d\rangle=u|00\rangle-v|11\rangle.
```

Write $`a=u^2-v^2`$ and $`b=2uv`$, so $`a^2+b^2=1`$. Relative to $`|\Phi_-\rangle=(|00\rangle-|11\rangle)/\sqrt2`$, the pure design error is

```math
\delta_0=1-|\langle\Phi_-|d\rangle|^2=\frac{1-b}{2}.
```

The orthogonal even-parity state is $`|e\rangle=v|00\rangle+u|11\rangle`$. Let $`p_d`$ and $`p_e`$ be their populations, and let $`O`$ be the total population of $`|01\rangle,|10\rangle`$. The noiseless master equation gives, for every initial density matrix,

```math
\dot p_e=g(-2p_e+b^2O),
\qquad
\dot O=g(2p_e-O),
\qquad
\dot p_d=ga^2O.
```

The last equation displays the loss of repair capacity: making $`b`$ close to one makes $`a^2`$ small. The desired state becomes more entangled while population transfer into it weakens. At $`u=v`$, the target is exactly Bell, but this transfer vanishes.

### The stationary state with compulsory dephasing

Add $`\kappa\mathcal D[Z_A]`$ and set

```math
r=\frac{\kappa}{g},
\qquad
\Delta=a^2+2r.
```

In the basis $`(|00\rangle,|01\rangle,|10\rangle,|11\rangle)`$, the exact stationary state is

```math
\rho_*=\frac1\Delta
\begin{pmatrix}
u^2(a^2+2ru^2)&0&0&-uv a^2\\
0&2ru^2v^2&0&0\\
0&0&2ru^2v^2&0\\
-uv a^2&0&0&v^2(a^2+2rv^2)
\end{pmatrix}.
```

Taking its Bell overlap yields

```math
\boxed{
\epsilon(b,r)
=\frac{1-b}{2}
+\frac{r\,b(b+2)}{2(1-b^2+2r)}.
}
```

The first term is the chosen dark state's error. The second is the extra error caused by noise. This formula is exact; the following expansion has additional limiting assumptions.

For $`\delta_0\to0`$ and $`r/\delta_0\to0`$,

```math
\epsilon
=\delta_0+\frac{3r}{8\delta_0}
\left[1+O\!\left(\delta_0+\frac r{\delta_0}\right)\right].
```

Reducing the first term indefinitely increases the second. Balancing them gives

```math
\delta_{0,\mathrm{opt}}\sim\sqrt{\frac{3r}{8}},
\qquad
\epsilon_{\mathrm{family}}\sim\sqrt{\frac{3r}{2}}
=\sqrt{\frac{3\kappa}{\Gamma}}.
```

The construction proves that the lower-bound exponent is achievable. At fixed engineered budget $`\Gamma>0`$, combining both sides gives Result R4:

```math
\epsilon_{\mathrm{opt}}(\Gamma,\kappa)
=\Theta\!\left(\sqrt{\frac{\kappa}{\Gamma}}\right)
\quad\text{as }\kappa/\Gamma\to0,
```

where the optimization is over the specified globally relaxing two-qubit generators. The coefficient $`\sqrt3`$ belongs to this family; the globally optimal coefficient is not determined.

Stationarity of the displayed matrix is not the only check needed for this conclusion. For $`r>0`$ and $`u,v>0`$, it is strictly positive. For $`u\ne v`$, the jumps and their adjoints generate all local raising and lowering operators, hence the full matrix algebra. The [construction's convergence argument](../science/attaining_reservoir.md) uses these facts to establish uniqueness and exclude persistent oscillating modes.

At exactly $`u=v`$ and any $`\kappa>0`$, the displayed state becomes $`I_4/4`$, with Bell error $`3/4`$. Taking the perfectly balanced setting first therefore gives a very different result from approaching it while reducing the noise with the appropriate asymmetry.

<a id="mixing-versus-gap"></a>
## 9. Operational mixing and why a gap is a different quantity

The stationary noise floor and the time needed to prepare a state are separate questions. The project's mixing definition is

```math
t_{\mathrm{mix}}(1/4)
=\inf\left\{t:
\sup_{\rho_0}
D_{\mathrm{tr}}(\mathcal T_t(\rho_0),\rho_*)\le\frac14
\right\}.
```

The reference state here is the actual stationary state, and the accuracy is fixed. If all-input convergence fails, the project sets this mixing time to infinity.

An arbitrary Hamiltonian could appear to offer arbitrarily fast motion. Stationarity constrains the particular motion needed to populate $`P`$. In the centered representation, let

```math
h=QH_c\psi,
\qquad
w=\sum_\mu L_\mu^\dagger L_\mu\psi.
```

The offdiagonal block of the stationary equation gives

```math
-i(\lambda I_Q-R|_Q)h
+Q\mathcal D_c(\rho_*)\psi=0,
\qquad
\mathcal D_c=\sum_\mu\mathcal D[L_\mu].
```

The operator multiplying $`h`$ is invertible with inverse norm at most $`1/(1-2\eta)`$. The already established transition estimates consequently bound $`\|h\|`$ by $`11K\epsilon`$ and $`\|w\|`$ by $`12K\epsilon`$. These are bounds on specific blocks and vectors; the complete Hamiltonian remains unrestricted.

The adjoint action is

```math
\mathcal L^\dagger(P)
=i[H_c,P]
+\sum_\mu|L_\mu^\dagger\psi\rangle\langle L_\mu^\dagger\psi|
-\frac12\bigl(|w\rangle\langle\psi|+|\psi\rangle\langle w|\bigr).
```

Combining the three terms yields Result R2's estimate

```math
\|\mathcal L^\dagger(P)\|_{\mathrm{op}}\le64K\epsilon.
```

For any trajectory, $`p(t)=\mathrm{Tr}(P\rho_t)`$ therefore satisfies $`|\dot p(t)|\le64K\epsilon`$. There is a product input orthogonal to $`|\psi\rangle`$: fix a local vector on $`A`$ and choose a vector on $`B`$ perpendicular to its contraction with $`\psi`$. This is possible because $`d\ge2`$. That input has $`p(0)=0`$.

To be within trace distance $`1/4`$ of $`\rho_*`$, the trajectory must have

```math
p(t)\ge\lambda-\frac14\ge\frac{11}{16}.
```

For $`K>0`$ and $`0<\epsilon\le1/16`$, integrating the speed bound without assuming monotonic population growth gives

```math
t_{\mathrm{mix}}(1/4)
\ge\frac{11}{1024K\epsilon}
\ge\frac1{128K\epsilon}.
```

This is a direct operational obstruction. Preprint §5.4 discusses the matrix exponential using Jordan blocks; that is a useful reminder that generator eigenvalues alone do not specify all finite-time norm behavior. A reciprocal dissipative gap cannot simply be substituted for the mixing time in this argument.

The noiseless qubit family also has a direct upper bound. Define

```math
\gamma_b=\frac{3-\sqrt{1+8b^2}}2.
```

Its closed population equations imply, uniformly over inputs,

```math
1-p_d(t)\le2e^{-g\gamma_b t},
\qquad
D_{\mathrm{tr}}(\rho_t,|d\rangle\langle d|)
\le\sqrt2\,e^{-g\gamma_b t/2}.
```

Because $`\gamma_b\sim(8/3)\delta_0`$, the construction attains mixing time of order $`1/(\Gamma\delta_0)`$ at fixed accuracy. The [mixing proof](../science/mixing.md) and [population calculation](../science/attaining_reservoir.md) keep this noiseless attainment separate from the noisy stationary optimization.

<a id="resource-conventions"></a>
## 10. Fixed strength, noise conventions, and the boundary of the model

The square-root law compares generators under the same resource and noise conventions. Four distinctions are essential.

**Count the complete jump amplitudes.** A conventional squeezed-bath parameterization uses coefficients $`\sqrt\gamma\cosh s`$ and $`\sqrt\gamma\sinh s`$. For the two jumps above, their total squared operator norm is

```math
\Gamma=2\gamma\cosh(2s).
```

Increasing $`s`$ while keeping $`\gamma`$ fixed increases the resource. The fixed-$`\Gamma`$ calculation rescales the overall amplitude so that $`u^2+v^2=1`$ and $`2g=\Gamma`$ remain fixed. This distinction is also relevant to the modulation and slowing discussion in [Govia et al., §V](https://arxiv.org/html/2110.06201v2).

**State the dephasing convention.** Since $`\mathcal D[Z](\rho)=Z\rho Z-\rho`$, an offdiagonal qubit matrix element obeys $`\dot\rho_{01}=-2\kappa\rho_{01}`$ under $`\kappa\mathcal D[Z]`$. A quoted coherence-decay rate is therefore $`2\kappa`$ in this convention. The engine budget is $`\Gamma`$; total strength including the dephaser is at most $`\Gamma+\kappa`$.

**Apply the structural assumption to the effective generator.** Preprint §6.4.1 discusses how multipartite microscopic models lead to master equations, including the role of system interactions in the weak-coupling construction. After transition-frequency resolution or elimination, the effective jumps must actually be checked for the form $`A_\mu\otimes I+I\otimes B_\mu`$. Local microscopic couplings alone do not establish that condition.

**Keep the factors and controller fixed when applying the theorem.** Extra levels, an auxiliary system, retained history-dependent feedback, or scheduled control can change the mathematical model. Instantaneous Markovian feedback is still covered whenever its unconditional generator satisfies the stated premises. A Bell state in a computational subspace of a qutrit–qubit device is not maximally entangled across equal complete local factors. Such architectures have meaningful preparation mechanisms, but the full-factor transpose argument above does not automatically apply to them. The [physical interpretation](../science/interpretation.md) and [related-work comparison](../references/RELATED_WORK.md) identify the relevant distinctions.

## Specialist pointers

| Question | Repository detail | Primary ingredient where applicable |
|---|---|---|
| What assumptions enter each result? | [Model and results](../science/model.md) | Anchor preprint §5.2 for generator convention |
| Where do the two powers of error arise? | [Quantitative rigidity](../science/rigidity.md) | [Linowski et al., §III](https://arxiv.org/html/2212.12245v2); [Pocklington and Clerk, §III/Appendix A](https://arxiv.org/html/2404.03625v2) |
| How does local noise produce a universal bound? | [Noise floor](../science/noise_floor.md) | The mixed-state variance argument developed here |
| Why is an unbounded Hamiltonian still constrained? | [Operational mixing](../science/mixing.md) | The centered offdiagonal stationarity equation |
| Which noisy state and normalization attain the exponent? | [Exact reservoir](../science/attaining_reservoir.md) | [Govia et al., Eqs. (8)–(9)](https://arxiv.org/html/2110.06201v2); [Pocklington and Clerk, Eq. (7)](https://arxiv.org/html/2409.06012v2) |
| What is independently checked in the explicit family? | [Verification guide](../verification/README.md) | Matrix and population identities, not a replacement for the universal proof |
| How do the foundations support the argument step by step? | [Milestone map](MILESTONES.md) | The single Rivas–Huelga anchor identified above |

