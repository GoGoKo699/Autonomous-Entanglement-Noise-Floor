# Quantitative rigidity near maximal entanglement

This note proves that a stationary state close to a maximally entangled pure state forces both small dissipative transition strengths and an approximately conserved rank-one projector. The stationary state may be mixed, and the Hamiltonian is unrestricted. The estimates use the norm budget of the supplied physical jump operators.

## Model and conventions

Let $`\mathcal H=\mathcal H_A\otimes\mathcal H_B`$, with $`\dim\mathcal H_A=\dim\mathcal H_B=d\ge2`$. All spaces are finite dimensional. In units with $`\hbar=1`$, consider the time-independent generator

```math
\mathcal L(\rho)
=-i[H,\rho]+\sum_{\mu=1}^{m}\mathcal D[J_\mu](\rho),
\qquad
\mathcal D[J](\rho)
=J\rho J^\dagger-\frac12\{J^\dagger J,\rho\},
```

where $`H=H^\dagger`$ and every physical jump has the form

```math
J_\mu=A_\mu\otimes I_B+I_A\otimes B_\mu.
```

The operators $`A_\mu`$ and $`B_\mu`$ need not be Hermitian or normal. There is no bound on $`H`$, including its interactions between the two factors. The finite number of jumps is arbitrary. Define

```math
K:=\sum_{\mu=1}^{m}\|J_\mu\|_{\mathrm{op}}^2.
```

This is a budget for the specified jump representation. It is not defined by minimizing over equivalent Lindblad representations, and it is not replaced by the norm of a gauge-shifted representation below. Operator norms are denoted by $`\|\cdot\|_{\mathrm{op}}`$; norms of vectors are Hilbert-space norms.

Fix a normalized vector $`|\Phi\rangle`$ that is maximally entangled across the **entire** two factors. Let $`\rho_*`$ be a stationary density operator,

```math
\mathcal L(\rho_*)=0,
\qquad
\epsilon:=1-\langle\Phi|\rho_*|\Phi\rangle.
```

The parameter $`\epsilon`$ is exactly the target-state infidelity. It is not the impurity of $`\rho_*`$ or a distance to its leading eigenvector. No uniqueness or convergence assumption is imposed on $`\rho_*`$.

The local-sum condition is a condition on the actual jump operators in the generator. A microscopic coupling that is local before eliminating a reservoir or resolving transition frequencies does not, by itself, establish this condition.

## Theorem

Suppose $`0\le\epsilon\le1/16`$. The largest eigenvalue $`\lambda`$ of $`\rho_*`$ is simple. Let $`|\psi\rangle`$ be its normalized eigenvector and set

```math
P:=|\psi\rangle\langle\psi|,
\qquad Q:=I-P,
\qquad c_\mu:=\langle\psi|J_\mu|\psi\rangle,
\qquad L_\mu:=J_\mu-c_\mu I.
```

Define the two centered transition strengths

```math
x^2:=\sum_\mu\|L_\mu|\psi\rangle\|^2,
\qquad
y^2:=\sum_\mu\|L_\mu^\dagger|\psi\rangle\|^2.
```

**Result R1: stationary outgoing variance.** The eigenvector estimates and transition-strength bounds are

```math
\boxed{
\begin{gathered}
\lambda\ge1-\epsilon,
\qquad
|\langle\Phi|\psi\rangle|^2\ge1-\epsilon,\\
y^2\le32K\epsilon,
\qquad
x^2\le36K\epsilon^2.
\end{gathered}
}
```

**Adjoint estimate for Result R2.** For the adjoint generator, defined by $`\operatorname{Tr}[X\mathcal L(\rho)]=\operatorname{Tr}[\mathcal L^\dagger(X)\rho]`$, one also has

```math
\boxed{
\|\mathcal L^\dagger(P)\|_{\mathrm{op}}
\le55K\epsilon
\le64K\epsilon.
}
```

The constants are deliberately conservative. They are independent of $`d`$, the number of jumps, the spectrum of $`H`$, and the rank of $`\rho_*`$.

The observable in the last bound is the projector onto the **leading eigenvector of the stationary state**. It is not assumed to coincide with $`|\Phi\rangle\langle\Phi|`$.

## Proof

### 1. The leading eigenvector is close to the target

The variational characterization of the largest eigenvalue gives

```math
\lambda\ge\langle\Phi|\rho_*|\Phi\rangle=1-\epsilon.
```

Write

```math
\rho_*=\lambda P+R,
\qquad R\ge0,
\qquad RP=PR=0,
\qquad \eta:=\operatorname{Tr}R=1-\lambda\le\epsilon.
```

Every eigenvalue of $`R`$ is at most its trace, so

```math
0\le R\le\eta Q,
\qquad
\|R\|_{\mathrm{op}}\le\eta.
```

Since $`\lambda\ge15/16`$ and $`\eta\le1/16`$, the top eigenvalue is separated from every other eigenvalue and is therefore simple.

Let $`f:=|\langle\Phi|\psi\rangle|^2`$. The bound on $`R`$ implies

```math
1-\epsilon
=\lambda f+\langle\Phi|R|\Phi\rangle
\le\lambda f+\eta(1-f)
=\eta+(1-2\eta)f.
```

Consequently,

```math
1-f\le\frac{\epsilon-\eta}{1-2\eta}\le\epsilon.
```

For the last inequality, multiply by the positive denominator and use $`\eta(1-2\epsilon)\ge0`$. Choose the phase of $`|\psi\rangle`$ so that $`\langle\Phi|\psi\rangle=\sqrt f`$ is real and nonnegative. With $`\delta:=\||\psi\rangle-|\Phi\rangle\|`$,

```math
\delta^2
=2(1-\sqrt f)
=\frac{2(1-f)}{1+\sqrt f}
\le\frac{2\epsilon}{1+\sqrt{1-\epsilon}}
\le\frac{16}{15}\epsilon.
```

The final bound follows on the stated interval $`0\le\epsilon\le1/16`$; it is a convenient loose estimate.

### 2. Centering the jumps and keeping the Hamiltonian gauge explicit

For each jump, the scalar shift $`L_\mu=J_\mu-c_\mu I`$ preserves the local-sum form, for example by replacing $`A_\mu`$ with $`A_\mu-c_\mu I_A`$. Define the Hermitian operator

```math
G_\mu
:=\frac{i}{2}\left(c_\mu^*L_\mu-c_\mu L_\mu^\dagger\right)
=\frac{i}{2}\left(c_\mu^*J_\mu-c_\mu J_\mu^\dagger\right),
\qquad
H_c:=H+\sum_\mu G_\mu.
```

Expanding $`J_\mu=L_\mu+c_\mu I`$ gives, for every operator $`\rho`$,

```math
\begin{aligned}
\mathcal D[J_\mu](\rho)-\mathcal D[L_\mu](\rho)
&=\frac12\left[c_\mu^*L_\mu-c_\mu L_\mu^\dagger,\rho\right]\\
&=-i[G_\mu,\rho].
\end{aligned}
```

Thus the **same** generator can be written as

```math
\mathcal L(\rho)
=-i[H_c,\rho]+\mathcal D_c(\rho),
\qquad
\mathcal D_c:=\sum_\mu\mathcal D[L_\mu].
```

All later occurrences of the centered Hamiltonian refer to $`H_c`$. No bound on this Hamiltonian is introduced.

By construction,

```math
\langle\psi|L_\mu|\psi\rangle
=\langle\psi|L_\mu^\dagger|\psi\rangle=0.
```

Both $`L_\mu|\psi\rangle`$ and $`L_\mu^\dagger|\psi\rangle`$ are therefore orthogonal to $`|\psi\rangle`$. Also,

```math
|c_\mu|\le\|J_\mu\|_{\mathrm{op}},
\qquad
\|L_\mu\|_{\mathrm{op}}\le2\|J_\mu\|_{\mathrm{op}},
\qquad
C_0:=\sum_\mu\|L_\mu\|_{\mathrm{op}}^2\le4K.
```

### 3. Spectral population balance

Take the $`P`$ diagonal matrix element of the stationarity equation. The Hamiltonian contribution vanishes because $`\rho_*|\psi\rangle=\lambda|\psi\rangle`$:

```math
\langle\psi|[H_c,\rho_*]|\psi\rangle=0.
```

For one centered jump,

```math
\begin{aligned}
\langle\psi|L_\mu\rho_*L_\mu^\dagger|\psi\rangle
&=\langle L_\mu^\dagger\psi|R|L_\mu^\dagger\psi\rangle,\\
\frac12\langle\psi|\{L_\mu^\dagger L_\mu,\rho_*\}|\psi\rangle
&=\lambda\|L_\mu|\psi\rangle\|^2.
\end{aligned}
```

Summing the resulting identities gives the exact flux balance

```math
\lambda x^2
=\sum_\mu\langle L_\mu^\dagger\psi|R|L_\mu^\dagger\psi\rangle
\le\eta y^2.
```

This is the spectral population-balance condition used in [Linowski, Rudnicki, and Gneiting, Section III, Eqs. (31)–(33)](../references/RELATED_WORK.md#linowski2023); see also the [primary text](https://arxiv.org/html/2212.12245v2). The identity itself is an inherited ingredient.

Set

```math
r:=\sqrt{\frac{\eta}{\lambda}}.
```

Then $`x\le r y`$, and

```math
0\le r\le\frac1{\sqrt{15}}\le\frac4{15}<1.
```

### 4. The maximally entangled transpose identity

Choose orthonormal Schmidt bases of the two factors in which

```math
|\Phi\rangle=\frac1{\sqrt d}\sum_{j=1}^d|j\rangle_A\otimes|j\rangle_B.
```

This entails no restriction on the specified target: every maximally entangled vector on equal-dimensional factors has this form in suitable local bases, and local basis changes preserve the operator norms and the local-sum form of the jumps.

For any local-sum operator $`L=A\otimes I+I\otimes B`$, use the vectorization convention

```math
\operatorname{vec}(C):=\sum_{i,j}C_{ij}|i\rangle_A\otimes|j\rangle_B.
```

Directly expanding the two actions gives

```math
\begin{aligned}
L|\Phi\rangle
&=\frac1{\sqrt d}\operatorname{vec}(A+B^{\mathsf T}),\\
L^\dagger|\Phi\rangle
&=\frac1{\sqrt d}\operatorname{vec}(A^\dagger+\overline B)
=\frac1{\sqrt d}\operatorname{vec}\!\left((A+B^{\mathsf T})^\dagger\right).
\end{aligned}
```

Since vectorization preserves the Hilbert–Schmidt norm and a matrix and its adjoint have the same Hilbert–Schmidt norm,

```math
\|L|\Phi\rangle\|=\|L^\dagger|\Phi\rangle\|.
```

This is the local-sum identity underlying [Pocklington and Clerk's pure-state obstruction](../references/RELATED_WORK.md#pocklington2024), particularly Section III and Appendix A of their [primary text](https://arxiv.org/html/2404.03625v2). It does not require $`L|\Phi\rangle=0`$.

### 5. Quantitative transition-strength bounds

Apply the triangle inequality in the direct sum of the jump-output Hilbert spaces. Using the preceding identity for every $`L_\mu`$ yields

```math
\begin{aligned}
y
&\le
\left(\sum_\mu\|L_\mu^\dagger|\Phi\rangle\|^2\right)^{1/2}
+\sqrt{C_0}\,\delta\\
&=
\left(\sum_\mu\|L_\mu|\Phi\rangle\|^2\right)^{1/2}
+\sqrt{C_0}\,\delta\\
&\le x+2\sqrt{C_0}\,\delta.
\end{aligned}
```

Together with $`x\le r y`$, this gives

```math
y\le\frac{2\sqrt{C_0}\,\delta}{1-r},
\qquad
y^2\le\frac{4C_0\delta^2}{(1-r)^2},
\qquad
x^2\le\frac{\eta}{\lambda}\frac{4C_0\delta^2}{(1-r)^2}.
```

Substituting the bounds already proved,

```math
y^2
\le\frac{4(4K)(16\epsilon/15)}{(11/15)^2}
=\frac{3840}{121}K\epsilon
\le32K\epsilon.
```

Therefore,

```math
x^2
\le\frac{\epsilon}{1-\epsilon}\,32K\epsilon
\le\frac{512}{15}K\epsilon^2
\le36K\epsilon^2.
```

The distinction between these estimates is essential: the incoming strength is at most linear in $`\epsilon`$, whereas the outgoing centered variance is at most quadratic. The latter also has the gauge-independent expression

```math
x^2
=\sum_\mu\left(
\langle\psi|J_\mu^\dagger J_\mu|\psi\rangle
-|\langle\psi|J_\mu|\psi\rangle|^2
\right).
```

### 6. Controlling the relevant Hamiltonian block

Define

```math
h:=QH_c|\psi\rangle,
\qquad
w:=\sum_\mu L_\mu^\dagger L_\mu|\psi\rangle.
```

The Cauchy–Schwarz inequality gives

```math
\|w\|
\le\sum_\mu\|L_\mu\|_{\mathrm{op}}\|L_\mu|\psi\rangle\|
\le\sqrt{C_0}\,x
\le12K\epsilon.
```

Projecting stationarity onto the $`Q`$–$`P`$ block gives

```math
-i(\lambda I_Q-R|_{Q\mathcal H})h
+Q\mathcal D_c(\rho_*)|\psi\rangle=0.
```

Here $`I_Q`$ is the identity on $`Q\mathcal H`$. To evaluate the dissipative term, use $`R|\psi\rangle=0`$ and the centering identities. The contribution from $`\lambda P`$ is $`-(\lambda/2)Qw`$: its jump term vanishes after applying it to $`|\psi\rangle`$, and one anticommutator term is annihilated by $`Q`$. The contribution from $`R`$ gives the remaining two terms. Thus

```math
Q\mathcal D_c(\rho_*)|\psi\rangle
=-\frac\lambda2 Qw
+\sum_\mu QL_\mu R L_\mu^\dagger|\psi\rangle
-\frac12 Rw.
```

Each term can be bounded without $`\|H_c\|_{\mathrm{op}}`$:

```math
\begin{aligned}
\left\|\sum_\mu QL_\mu R L_\mu^\dagger|\psi\rangle\right\|
&\le\eta\sum_\mu\|L_\mu\|_{\mathrm{op}}\|L_\mu^\dagger|\psi\rangle\|\\
&\le\eta\sqrt{C_0}\,y,\\
\|Rw\|&\le\eta\sqrt{C_0}\,x.
\end{aligned}
```

Since $`\lambda+\eta=1`$,

```math
\|Q\mathcal D_c(\rho_*)|\psi\rangle\|
\le\frac12\sqrt{C_0}\,x+\eta\sqrt{C_0}\,y.
```

On $`Q\mathcal H`$, the positive operator $`\lambda I_Q-R|_{Q\mathcal H}`$ has smallest eigenvalue at least

```math
\lambda-\|R\|_{\mathrm{op}}
\ge1-2\eta
\ge\frac78.
```

It follows that

```math
\|h\|
\le\frac{\frac12\sqrt{C_0}\,x+\eta\sqrt{C_0}\,y}{1-2\eta}.
```

For an explicit conservative constant, use $`\sqrt{C_0}\le2\sqrt K`$, $`x\le6\sqrt K\,\epsilon`$, $`y\le6\sqrt K\,\sqrt\epsilon`$, $`\eta\le\epsilon`$, and $`\sqrt\epsilon\le1/4`$. Then

```math
\|h\|
\le\frac{6K\epsilon+12K\epsilon\sqrt\epsilon}{7/8}
\le\frac{72}{7}K\epsilon
\le11K\epsilon.
```

Only the block connecting $`|\psi\rangle`$ to its orthogonal complement has been bounded. The Hamiltonian within the orthogonal complement may have arbitrarily large norm.

### 7. The approximately conserved projector

In the centered representation, the adjoint generator acting on $`P`$ is

```math
\mathcal L^\dagger(P)
=i[H_c,P]
+\sum_\mu|L_\mu^\dagger\psi\rangle\langle L_\mu^\dagger\psi|
-\frac12\left(|w\rangle\langle\psi|+|\psi\rangle\langle w|\right).
```

Because $`h\perp\psi`$,

```math
i[H_c,P]=i\left(|h\rangle\langle\psi|-|\psi\rangle\langle h|\right),
\qquad
\|i[H_c,P]\|_{\mathrm{op}}=\|h\|.
```

The sum of rank-one operators is positive and has trace $`y^2`$, so its operator norm is at most $`y^2`$. Each outer product with a normalized $`|\psi\rangle`$ has operator norm $`\|w\|`$, and the triangle inequality therefore bounds the final Hermitian term by $`\|w\|`$. Combining the estimates,

```math
\|\mathcal L^\dagger(P)\|_{\mathrm{op}}
\le\|h\|+y^2+\|w\|
\le(11+32+12)K\epsilon
=55K\epsilon
\le64K\epsilon.
```

This proves the theorem.

## Endpoints and interpretation

The proof also covers $`\epsilon=0`$: then $`\rho_*=|\Phi\rangle\langle\Phi|`$, $`x=y=0`$, $`h=w=0`$, and $`\mathcal L^\dagger(P)=0`$. This recovers the exact conserved-projector obstruction in the pure maximally entangled case. If $`K=0`$, the same conserved-projector conclusion holds under the stated stationary-state assumption.

The quantitative statement above concerns every stationary state with small target infidelity, including mixed states. It does not require detailed balance, normality of the generator, a bound on coherent control, or a lower bound on the nonzero eigenvalues of $`\rho_*`$. Its operational mixing consequence is proved in [mixing.md](mixing.md).
