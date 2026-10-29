# An attaining two-qubit reservoir

An established squeezed-reservoir family attains the two asymptotic orders in this project. Without compulsory noise, it mixes from every initial state in time of order the inverse Bell infidelity. With a fixed local dephaser, optimizing the same family gives

```math
\inf_{u,v}\bigl(1-\langle\Phi_-|\rho_*|\Phi_-\rangle\bigr)
\sim \sqrt{\frac{3\kappa}{\Gamma}},
\qquad \frac{\kappa}{\Gamma}\longrightarrow0.
```

The coefficient $`\sqrt{3}`$ is the optimum **within this family**. Combined with the general converse, the construction establishes the global order $`\Theta(\sqrt{\kappa/\Gamma})`$; it does not establish the globally optimal coefficient.

The reservoir itself is inherited. See [Govia, Lingenfelter, and Clerk (2022)](../references/RELATED_WORK.md#govia2022), particularly [Eqs. (8)–(9)](https://arxiv.org/html/2110.06201v2), and [Pocklington and Clerk (2025)](../references/RELATED_WORK.md#pocklington2025), [Eq. (7) with one qubit in each subsystem](https://arxiv.org/html/2409.06012v2). The purpose of this page is to make its resource normalization, operational mixing estimate, and exact noisy stationary state explicit.

## 1. Convention and resource budget

Use the computational basis $`(|00\rangle,|01\rangle,|10\rangle,|11\rangle)`$, with

```math
\sigma^- = |0\rangle\langle1|,
\qquad \sigma^+=(\sigma^-)^\dagger,
\qquad Z=|0\rangle\langle0|-|1\rangle\langle1|.
```

Our dissipator convention is

```math
\mathcal D[J](\rho)
=J\rho J^\dagger-\frac12\{J^\dagger J,\rho\}.
```

Let $`g>0`$, $`u,v>0`$, and $`u^2+v^2=1`$. Define

```math
J_1=\sqrt g\,(u\sigma_A^-+v\sigma_B^+),
\qquad
J_2=\sqrt g\,(u\sigma_B^-+v\sigma_A^+),
\qquad H=0.
```

Each term on the right includes the identity on the other qubit. Both jumps have the required local-sum form. For the noisy model add

```math
J_0=\sqrt\kappa\,Z_A,
\qquad
\mathcal L=\mathcal D[J_1]+\mathcal D[J_2]+\kappa\mathcal D[Z_A].
```

The dephasing parameter $`\kappa`$ is the coefficient of $`\mathcal D[Z_A]`$: an isolated offdiagonal matrix element of qubit $`A`$ decays at rate $`2\kappa`$ under this convention.

Write

```math
|d\rangle=u|00\rangle-v|11\rangle,
\qquad |e\rangle=v|00\rangle+u|11\rangle,
\qquad a=u^2-v^2,
\qquad b=2uv.
```

Then $`a^2+b^2=1`$. Setting $`\ell_j=J_j/\sqrt g`$, direct multiplication gives

```math
\ell_1^\dagger\ell_1=P_e+|10\rangle\langle10|,
\qquad
\ell_2^\dagger\ell_2=P_e+|01\rangle\langle01|,
```

where $`P_e=|e\rangle\langle e|`$. Each right-hand side is a projector. Consequently

```math
\|J_1\|_{\mathrm{op}}^2=\|J_2\|_{\mathrm{op}}^2=g,
\qquad \Gamma=2g,
\qquad K=\Gamma+\kappa.
```

The engine strength held fixed below is $`\Gamma`$. This counts the complete jump amplitudes, including the normalization of any physical squeezing parameters.

## 2. Pure stationary state and Bell fidelity

The elementary jump actions are

```math
\begin{aligned}
\ell_1|d\rangle&=\ell_2|d\rangle=0,\\
\ell_1|e\rangle&=|01\rangle,
&\ell_2|e\rangle&=|10\rangle,\\
\ell_1|10\rangle&=a|d\rangle+b|e\rangle,
&\ell_2|01\rangle&=a|d\rangle+b|e\rangle,\\
\ell_1|01\rangle&=0,
&\ell_2|10\rangle&=0.
\end{aligned}
```

Thus $`P_d=|d\rangle\langle d|`$ is stationary when $`\kappa=0`$. Its fidelity with

```math
|\Phi_-\rangle=\frac{|00\rangle-|11\rangle}{\sqrt2}
```

is

```math
F_0=\frac{(u+v)^2}{2}=\frac{1+b}{2},
\qquad \delta_0=1-F_0=\frac{1-b}{2}.
```

For $`u\ne v`$, the population calculation below proves uniqueness and convergence from all inputs. At the balanced point $`u=v`$, $`\delta_0=0`$ and the pumping rate into the dark state vanishes. This singular endpoint is not a finite-time maximally entangled preparation protocol.

## 3. Closed populations and uniform mixing

Let

```math
p_d=\mathrm{Tr}(P_d\rho),
\qquad p_e=\mathrm{Tr}(P_e\rho),
\qquad O=\rho_{01,01}+\rho_{10,10}.
```

These populations sum to one. The noiseless master equation gives, for **every** density operator, including states with coherences in this basis,

```math
\frac{d}{dt}
\begin{pmatrix}p_e\\O\end{pmatrix}
=g\begin{pmatrix}-2&b^2\\2&-1\end{pmatrix}
\begin{pmatrix}p_e\\O\end{pmatrix},
\qquad \dot p_d=g a^2O.
```

One way to see that coherences do not enter is to calculate the adjoint action on the three population projectors. The identities are

```math
\begin{aligned}
\mathcal L^\dagger(P_e)&=-2gP_e+gb^2P_O,\\
\mathcal L^\dagger(P_O)&=2gP_e-gP_O,\\
\mathcal L^\dagger(P_d)&=ga^2P_O,
\end{aligned}
\qquad
P_O=|01\rangle\langle01|+|10\rangle\langle10|.
```

Define the dimensionless population decay constants

```math
\gamma_b=\frac{3-\sqrt{1+8b^2}}2,
\qquad
\beta_b=\frac{3+\sqrt{1+8b^2}}2.
```

The physical rates in the population block are $`g\gamma_b`$ and $`g\beta_b`$. For $`0<b<1`$, both are positive. If the input is $`P_e`$, its total probability outside the dark state is exactly

```math
S_e(t)=1-p_d(t)
=\frac{\beta_b e^{-g\gamma_b t}-\gamma_b e^{-g\beta_b t}}
{\beta_b-\gamma_b}.
```

For an input wholly in the odd subspace, the corresponding survival probability is

```math
S_O(t)
=\frac{(\beta_b-a^2)e^{-g\gamma_b t}
 +(a^2-\gamma_b)e^{-g\beta_b t}}
{\beta_b-\gamma_b}.
```

Their difference is nonnegative:

```math
S_e(t)-S_O(t)
=\frac{a^2(e^{-g\gamma_b t}-e^{-g\beta_b t})}
{\beta_b-\gamma_b}\geq0.
```

An arbitrary initial state therefore obeys

```math
1-p_d(t)=p_e(0)S_e(t)+O(0)S_O(t)
\leq S_e(t)
\leq C_b e^{-g\gamma_b t},
\qquad
C_b=\frac{\beta_b}{\beta_b-\gamma_b}\leq2.
```

The pure-state fidelity inequality now gives a uniform operational estimate,

```math
\frac12\|e^{t\mathcal L}(\rho)-P_d\|_1
\leq\sqrt{1-p_d(t)}
\leq\sqrt{C_b}\,e^{-g\gamma_b t/2}.
```

In particular, define

```math
t_{\mathrm{mix}}(\delta)
=\inf\left\{t:\sup_\rho
\frac12\|e^{t\mathcal L}(\rho)-P_d\|_1\leq\delta\right\},
\qquad 0<\delta<1.
```

The preceding estimate and the input $`P_e`$ give the two-sided bound

```math
\frac{\log(1/\delta)}{g\gamma_b}
\leq t_{\mathrm{mix}}(\delta)
\leq\frac{\log(C_b/\delta^2)}{g\gamma_b}.
```

For the lower bound, measuring $`P_d`$ distinguishes the evolved state from $`P_d`$ with probability difference $`S_e(t)`$, and $`S_e(t)\geq e^{-g\gamma_b t}`$. These are direct population and trace-distance bounds. They require no inference from a Liouvillian gap or a normality assumption.

Finally,

```math
\gamma_b
=\frac{16\delta_0(1-\delta_0)}
{3+\sqrt{9-32\delta_0(1-\delta_0)}}
\sim\frac83\delta_0.
```

At any fixed output distance $`0<\delta<1`$, this proves

```math
t_{\mathrm{mix}}(\delta)
=\Theta_\delta\!\left(\frac1{g\delta_0}\right)
=\Theta_\delta\!\left(\frac1{\Gamma\delta_0}\right).
```

## 4. Exact stationary state with local dephasing

Now take $`\kappa>0`$, and set

```math
r=\frac\kappa g,
\qquad \Delta=a^2+2r.
```

An invariant real X-state sector has the form

```math
\rho=
\begin{pmatrix}
p&0&0&w\\
0&q&0&0\\
0&0&q&0\\
w&0&0&s
\end{pmatrix},
\qquad p+s+2q=1.
```

Within this sector the equations are

```math
\begin{aligned}
\dot p/g&=2u^2q-2v^2p-2uv w,\\
\dot s/g&=2v^2q-2u^2s-2uv w,\\
\dot q/g&=v^2p+u^2s+2uv w-q,\\
\dot w/g&=uv(4q-1)-(1+2r)w.
\end{aligned}
```

Solving these equations gives

```math
\boxed{
\rho_*=
\frac1\Delta
\begin{pmatrix}
u^2(a^2+2ru^2)&0&0&-uv a^2\\
0&2ru^2v^2&0&0\\
0&0&2ru^2v^2&0\\
-uv a^2&0&0&v^2(a^2+2rv^2)
\end{pmatrix}.}
```

Equivalently,

```math
q=\frac{r b^2}{2\Delta},
\qquad w=-\frac{b a^2}{2\Delta},
\qquad p=u^2-q,
\qquad s=v^2-q.
```

This is an exact stationary solution of the full generator, rather than a small-noise expansion. Inserting it in the four equations proves stationarity in the invariant X sector; all other matrix elements remain zero. The uniqueness argument in the next section excludes additional stationary solutions outside that sector.

### Positivity and faithfulness

The trace of $`\rho_*`$ is one. For $`r>0`$ and $`u,v>0`$, the odd-sector eigenvalues $`q`$ are strictly positive, and the two even-sector diagonal entries are strictly positive. The determinant of the even block is

```math
ps-w^2
=\frac{2ru^2v^2(a^2+2ru^2v^2)}{\Delta^2}>0.
```

Both even-sector eigenvalues are therefore positive. Hence $`\rho_*`$ is faithful. The limit $`r\to0`$ at fixed $`u\ne v`$ recovers $`P_d`$.

## 5. Uniqueness and convergence of the noisy model

For $`u\ne v`$ the operators $`\ell_1`$ and $`\ell_2^\dagger`$ satisfy

```math
\begin{pmatrix}\ell_1\\\ell_2^\dagger\end{pmatrix}
=\begin{pmatrix}u&v\\v&u\end{pmatrix}
\begin{pmatrix}\sigma_A^-\\\sigma_B^+\end{pmatrix}.
```

The coefficient matrix is invertible. The jumps and their adjoints thus generate the local raising and lowering operators on both qubits, and consequently the full two-qubit matrix algebra.

For completeness, the role of faithfulness can be seen without assuming a mixing-gap theorem. For a Hermitian observable $`X`$,

```math
\mathcal L^\dagger(X^2)
-\mathcal L^\dagger(X)X-X\mathcal L^\dagger(X)
=\sum_\mu[J_\mu,X]^\dagger[J_\mu,X].
```

If $`\mathcal L^\dagger(X)=0`$, the expectation of the left side in $`\rho_*`$ is zero by stationarity. Faithfulness forces every commutator on the right to vanish. Since $`X`$ is Hermitian, it commutes with the jumps' adjoints as well. The generated algebra is full, so $`X`$ is scalar. Hermitian and anti-Hermitian parts then show that the entire adjoint fixed space is one-dimensional. The generator and its adjoint have equal nullity, establishing uniqueness of the stationary state.

The same identity for $`X^\dagger X`$ and $`XX^\dagger`$ excludes other imaginary-axis eigenoperators: if $`\mathcal L^\dagger(X)=i\omega X`$, taking stationary expectations makes both sums of squared commutators vanish. Thus $`X`$ commutes with the full generated algebra and is scalar, requiring $`\omega=0`$. A finite-dimensional channel semigroup is bounded, so it cannot have a nontrivial Jordan block at an imaginary-axis eigenvalue. All remaining modes decay. It follows that every initial state converges to $`\rho_*`$.

At $`u=v`$ and $`\kappa>0`$, the same conclusion also holds. The available $`Z_A`$ and its commutator with $`\ell_1`$ isolate $`\sigma_A^-`$; subtracting this contribution isolates $`\sigma_B^+`$. The algebra remains full. The exact state at this balanced point is $`I_4/4`$, with Bell infidelity $`3/4`$. Thus the balanced and zero-noise limits do not commute.

## 6. Exact error and the optimum within the family

For the target $`\Phi_-`$,

```math
F=\frac{p+s-2w}{2}=\frac12-q-w.
```

Using the exact state,

```math
\boxed{
\epsilon(b,r)=1-F
=\frac{1-b}{2}
+\frac{r b(b+2)}{2(1-b^2+2r)}.}
```

The first term is the pure design error. The second is the increase caused by the fixed dephaser. A more entangled dark state reduces the first term while weakening the population transfer that repairs dephasing errors.

There is a unique optimizer in $`0<b<1`$ for every $`r>0`$. Differentiation gives

```math
\frac{\partial\epsilon}{\partial b}
=-\frac{Q_r(b)}{2(1-b^2+2r)^2},
```

where

```math
Q_r(b)=(1-b^2)^2+2r(1-b-3b^2)-4r^2b.
```

Indeed,

```math
Q_r(0)=1+2r>0,
\qquad Q_r(1)=-6r-4r^2<0,
```

and

```math
Q_r'(b)=-4b(1-b^2)-2r(1+6b)-4r^2<0
\qquad(0\leq b\leq1).
```

The unique root of $`Q_r`$ is therefore the global minimum over the family. It also gives a stable scalar equation for numerical optimization.

To identify its asymptotic value, write $`\delta_0=(1-b)/2`$. In the regime $`\delta_0\to0`$ and $`r/\delta_0\to0`$,

```math
\epsilon
=\delta_0+\frac{3r}{8\delta_0}
\left[1+O\!\left(\delta_0+\frac r{\delta_0}\right)\right].
```

The trial choice $`\delta_0=\sqrt{3r/8}`$ has error tending to zero. Any global minimizer must consequently have $`\delta_0\to0`$. Its noise term could not tend to zero if $`r/\delta_0`$ stayed bounded away from zero, so $`r/\delta_0\to0`$ also holds at the minimizer. The displayed expansion is therefore applicable there. The arithmetic–geometric mean inequality, together with the trial choice, proves

```math
\delta_{0,\mathrm{opt}}\sim\sqrt{\frac{3r}{8}},
\qquad
\epsilon_{\mathrm{family}}^{\mathrm{opt}}\sim\sqrt{\frac{3r}{2}}
=\sqrt{\frac{3\kappa}{\Gamma}}.
```

No claim about the globally optimal leading coefficient is needed to attain the universal square-root order.

### Other maximally entangled two-qubit targets

Every maximally entangled two-qubit vector has the form $`(I_A\otimes U_B)|\Phi_-\rangle`$ for a unitary $`U_B`$. Conjugate both engineered jumps by $`I_A\otimes U_B`$. Their local-sum form and operator norms are unchanged, and the compulsory dephaser $`Z_A`$ is unchanged. The transformed stationary state has exactly the same target fidelity and mixing behavior. Thus the construction applies to any fixed maximally entangled two-qubit target while preserving the specified dephasing operator.

## 7. Why the normalization matters

In a conventional squeezed-bath parametrization, the jumps can contain $`\sqrt{\gamma}\cosh s`$ and $`\sqrt{\gamma}\sinh s`$. Their summed squared operator norm is then

```math
\Gamma=2\gamma\cosh(2s).
```

Holding the bare coefficient $`\gamma`$ fixed while increasing $`s`$ spends increasing dissipative strength. That optimization is different from the fixed-$`\Gamma`$ optimization above. The construction can instead be implemented with an overall amplitude rescaling that keeps $`u^2+v^2=1`$ and $`\Gamma`$ fixed, as the modulation discussion in [Govia et al.](https://arxiv.org/html/2110.06201v2) makes explicit. Comparisons must count the actual jump amplitudes.

## 8. Reproducible checks

The [verification guide](../verification/README.md) describes the deterministic full-generator checks and their expected outputs. They include a direct matrix-action check of column vectorization using complex jumps and a Hermitian Hamiltonian, exact population-observable identities, the pure survival formulas, the full noisy stationary state, and the unique scalar family optimum. A rational-arithmetic example verifies full-matrix stationarity and fidelity exactly.

The numerical eigenvalue checks concern this explicit two-qubit family at the listed parameter values. They neither prove a general spectral-gap bound nor replace the written arguments for arbitrary inputs, faithfulness, uniqueness, convergence, and asymptotic optimization.
