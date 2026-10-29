# From stationary rigidity to a noise floor

The [rigidity theorem](rigidity.md) bounds the total outgoing jump variance
in the dominant eigenvector of a high-fidelity stationary state. Independent
local noise contributes a positive amount to exactly that variance. Comparing
the two quantities gives a stationary fidelity limit directly, without a
perturbation expansion in an inverse dissipative gap.

## 1. Local dephasing

Use the [model and conventions](model.md), with $`\kappa>0`$.
Suppose the physical jump list
contains

```math
J_0=\sqrt\kappa\, Z_A,
\qquad Z_A=Z\otimes I,
\qquad Z=Z^\dagger,\quad Z^2=I,\quad\mathrm{Tr}Z=0.
```

Such a $`Z`$ exists for qubits and for even local dimension. Let
$`|\psi\rangle`$ be the leading eigenvector of $`\rho_*`$. The fidelity
transfer in [rigidity](rigidity.md) proves

```math
|\langle\Phi|\psi\rangle|^2\ge1-\epsilon,
\qquad
D_{\mathrm{tr}}(|\psi\rangle\langle\psi|,
|\Phi\rangle\langle\Phi|)\le\sqrt\epsilon.
```

A maximally entangled state has a maximally mixed marginal, so
$`\langle\Phi|Z_A|\Phi\rangle=0`$. Hölder's inequality then gives

```math
|\langle\psi|Z_A|\psi\rangle|
\le\|Z_A\|_{\mathrm{op}}
\bigl\||\psi\rangle\langle\psi|-|\Phi\rangle\langle\Phi|\bigr\|_1
\le2\sqrt\epsilon.
```

Centering this particular physical jump at $`|\psi\rangle`$ yields

```math
\|L_0\psi\|^2
=\kappa\left(1-\langle\psi|Z_A|\psi\rangle^2\right)
\ge\kappa(1-4\epsilon).
```

For $`\epsilon\le1/16`$, this is at least $`3\kappa/4`$. Every jump's
variance is nonnegative, including every engineered jump. Therefore R1 gives

```math
\frac34\kappa
\le\|L_0\psi\|^2
\le\sum_\mu\|L_\mu\psi\|^2
\le36K\epsilon^2,
```

and hence

```math
\boxed{\epsilon\ge\sqrt{\frac{\kappa}{48K}}.}
```

If the engineering budget is at most $`\Gamma`$, the declared decomposition
has $`K\le\Gamma+\kappa`$, establishing R3. A state with error above
$`1/16`$ automatically obeys the minimum-form bound in [model.md](model.md).
This also justifies using the high-fidelity theorem in the asymptotic
optimization over all allowed stationary states.

The Hamiltonian drops out of the diagonal stationary population balance.
Thus this proof never bounds $`\|H\|`$, never assumes detailed balance, and
never replaces a mixing time by the inverse of a spectral gap.

## 2. A normalized variance bound for other local noise

The dephasing operator permits especially simple constants. The same method
also gives a one-sided result for a specified bounded local noise operator.
Let the physical jump list contain $`J_0=\sqrt\kappa C_A`$, where
$`C_A=C\otimes I`$, $`M=\|C\|_{\mathrm{op}}>0`$, and

```math
\nu=\langle\Phi|C_A^\dagger C_A|\Phi\rangle
 -|\langle\Phi|C_A|\Phi\rangle|^2
=\frac{\mathrm{Tr}(C^\dagger C)}{d}
 -\left|\frac{\mathrm{Tr}C}{d}\right|^2>0.
```

The expectation of $`C_A^\dagger C_A`$ changes by at most
$`2M^2\sqrt\epsilon`$ between $`|\Phi\rangle`$ and $`|\psi\rangle`$.
The expectation of $`C_A`$ changes by at most $`2M\sqrt\epsilon`$, while
each expectation has magnitude at most $`M`$. Consequently

```math
\begin{aligned}
\mathrm{Var}_\psi(C_A)
&:=\langle\psi|C_A^\dagger C_A|\psi\rangle
 -|\langle\psi|C_A|\psi\rangle|^2\\
&\ge\nu-6M^2\sqrt\epsilon.
\end{aligned}
```

If

```math
\epsilon\le\min\left\{\frac1{16},
\frac{\nu^2}{144M^4}\right\},
```

then $`\mathrm{Var}_\psi(C_A)\ge\nu/2`$. It follows that

```math
\epsilon\ge\sqrt{\frac{\kappa\nu}{72K}}.
```

With engineered budget $`\Gamma`$ and only this additional noise channel,
$`K\le\Gamma+\kappa M^2`$. For a fixed noise operator with $`\nu>0`$,
the result supplies a square-root lower order in the small-noise,
high-fidelity limit. It does not prove that every such noise model admits a
matching construction. The explicit sharp R4 concerns qubit dephasing.

For example, a qubit lowering operator has $`M=1`$ and $`\nu=1/2`$ on a
Bell target, so the lower-order argument also applies to additive local
relaxation under its declared normalization. An operator proportional to
the identity has $`\nu=0`$ and is excluded for the physical reason that it
produces no dissipative noise. These cases show why the variance condition,
rather than an unspecified noise-rate label, belongs in the claim.

## 3. Matching the qubit exponent

The [exact construction](attaining_reservoir.md) uses

```math
J_1=\sqrt g\,(u\sigma_A^-+v\sigma_B^+),
\qquad
J_2=\sqrt g\,(u\sigma_B^-+v\sigma_A^+),
\qquad u^2+v^2=1.
```

Here $`\Gamma=2g`$. Write $`b=2uv`$, $`r=\kappa/g`$ and
$`\delta_0=(1-b)/2`$. The noisy stationary Bell error is

```math
\epsilon(b,r)=\frac{1-b}{2}
 +\frac{r b(b+2)}{2(1-b^2+2r)}.
```

As $`\delta_0\to0`$ with $`r/\delta_0\to0`$,

```math
\epsilon(b,r)=\delta_0+\frac{3r}{8\delta_0}
 +o\!\left(\delta_0+\frac{r}{\delta_0}\right).
```

Taking $`\delta_0\sim\sqrt{3r/8}`$ gives

```math
\epsilon\sim\sqrt{\frac{3r}{2}}
=\sqrt{\frac{3\kappa}{\Gamma}}.
```

For each positive sufficiently small $`r`$, choose $`u,v>0`$ with
$`u\ne v`$. The construction has a unique faithful stationary state and
converges from all inputs. It is therefore admissible for the optimization
in R4. Combining this upper bound with R3 establishes the sharp exponent.

The two terms in the displayed expansion express a concrete competition:
moving away from a Bell dark state introduces ideal error $`\delta_0`$,
while moving too close makes the state more vulnerable to fixed local
dephasing. The universal converse establishes that optimizing a different
Hamiltonian or a different allowed reservoir cannot improve the resulting
exponent at the same budget. The family itself and its pure-state slowing
are [established ingredients](../references/RELATED_WORK.md#govia2022).
