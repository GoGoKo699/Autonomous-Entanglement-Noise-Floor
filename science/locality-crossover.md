# The stationary noise floor with approximately local-sum jumps

How much nonlocal dissipation is needed to lower the square-root error of
autonomous entanglement stabilization? For weak imposed noise, a nonlocal
jump amplitude of order $`(\kappa/\Gamma)^{1/4}`$ marks the crossover. The
bound applies to mixed stationary states and arbitrary static coherent
control. Two explicit reservoirs attain the order on the two sides of the
crossover.

## Model and result

Let both local factors have the same fixed finite dimension $`d\ge2`$ and
let $`P_0=|\Phi\rangle\langle\Phi|`$ project onto a maximally entangled
state of the complete factors. Use the dissipator
$`\mathcal D[J](\rho)=J\rho J^\dagger-\{J^\dagger J,\rho\}/2`$ and
consider time-independent generators

```math
\mathcal L=-i[H,\,\cdot\,]+\sum_\mu\mathcal D[J_\mu]+\kappa\mathcal N,
\qquad
\mathcal N=-i[H_N,\,\cdot\,]+\sum_a\mathcal D[N_a].
```

The independent additive noise generator $`\mathcal N`$ is fixed, and
$`\kappa>0`$ sets its rate. The noise jumps can act on either or both
factors. Their normalization is held fixed as $`\kappa/\Gamma`$ varies.
Assume that the noise transfers population out of the target at a positive
initial rate

```math
\nu=\operatorname{Tr}[(I-P_0)\mathcal N(P_0)]
=\sum_a\left(\langle\Phi|N_a^\dagger N_a|\Phi\rangle
   -|\langle\Phi|N_a|\Phi\rangle|^2\right)>0.
```

Allow any Hermitian $`H`$ and any finite list of engineered jumps
admitting the decomposition and budgets

```math
J_\mu=L_\mu+E_\mu,\qquad L_\mu=A_\mu\otimes I+I\otimes B_\mu,\qquad
\sum_\mu\|J_\mu\|_{\rm op}^2\le\Gamma,\qquad
\sum_\mu\|E_\mu\|_{\rm op}^2\le\Gamma\delta^2 .
```

Here $`\Gamma>0`$ and $`0\le\delta\le1`$. The budget on the
full jumps and the budget on their departures from local-sum form refer to
an admissible physical jump representation of the engineered dynamics.
The operator norm is used throughout. The noise jumps are charged through
$`\kappa\mathcal N`$ independently of these two budgets. See the
[model conventions](model.md) for the exact-local case and the earlier
[noise floor](noise_floor.md) for compulsory local noise.

Let $`\epsilon_{\rm opt}`$ be the infimum of
$`1-\operatorname{Tr}(P_0\rho_*)`$ over allowed generators with a
unique stationary state to which every initial state converges. Put
$`f=\kappa/\Gamma`$. There exist positive constants $`c,C,f_0`$,
depending only on the fixed dimension and noise, such that for every
$`0<f\le f_0`$ and every $`\delta\in[0,1]`$,

```math
c\min\!\left\{\sqrt f,\frac{f}{\delta^2}\right\}
\;\le\;\epsilon_{\rm opt}
\;\le\;C\min\!\left\{\sqrt f,\frac{f}{\delta^2}\right\}.
```

At $`\delta=0`$ the fraction is interpreted as infinity. The lower
bound applies to every stationary state, with or without convergence
from all initial states. Uniformity in $`\delta`$ permits the departure
from exact locality to shrink with the noise. Dimension and noise are
fixed before taking the weak-noise limit.

## Converse from stationary population balance

Write $`\epsilon=1-\operatorname{Tr}(P_0\rho_*)`$. For
$`\epsilon\le1/16`$, the argument in
[mixed-state rigidity](rigidity.md) gives a simple leading eigenvalue
$`\lambda\ge1-\epsilon`$ and normalized eigenvector $`\psi`$
of $`\rho_*`$. The remainder has trace $`\eta=1-\lambda\le\epsilon`$
and is bounded above by $`\eta(I-|\psi\rangle\langle\psi|)`$.
Also $`|\langle\Phi|\psi\rangle|^2\ge1-\epsilon`$, so phases
can be chosen with $`\|\psi-\Phi\|\le\sqrt{2\epsilon}`$.

Center each jump at its expectation in $`\psi`$. In particular, put
$`C_\mu=J_\mu-\langle\psi|J_\mu|\psi\rangle I`$ and define

```math
x_e^2=\sum_\mu\|C_\mu\psi\|^2,\qquad
y_e^2=\sum_\mu\|C_\mu^\dagger\psi\|^2 .
```

Define $`x_n,y_n`$ in the same way for $`N_a`$, before multiplication
by $`\sqrt\kappa`$. The Hamiltonian term has zero diagonal matrix
element at an eigenvector of a stationary state. Scalar centering
affects the commutator part only. Spectral population balance therefore gives

```math
x_e^2+\kappa x_n^2\le r^2(y_e^2+\kappa y_n^2),
\qquad r=\sqrt{\eta/\lambda}.
```

For a local-sum operator $`M`$, the transpose identity at maximal
entanglement gives $`\|M\Phi\|=\|M^\dagger\Phi\|`$. Apply it to
$`C_\mu-E_\mu`$. Comparing the two norms in the direct sum of all
engineered jump outputs costs at most $`2\sqrt\Gamma\delta`$
at $`\Phi`$. Moving from $`\Phi`$ to $`\psi`$ in each norm
costs at most $`2\sqrt\Gamma\|\psi-\Phi\|`$, because
$`\sum_\mu\|C_\mu\|_{\rm op}^2\le4\Gamma`$. Thus

```math
y_e\le x_e+B,\qquad
B=\sqrt\Gamma\,(4\sqrt{2\epsilon}+2\delta),\qquad
B^2\le64\Gamma(\epsilon+\delta^2).
```

The population balance implies $`x_e\le r(y_e+\sqrt\kappa y_n)`$.
Combining these inequalities and using $`r\le1/3`$ gives

```math
y_e^2\le \frac{2B^2+2r^2\kappa y_n^2}{(1-r)^2}
\le \frac92 B^2+\frac12\kappa y_n^2 .
```

Let $`K_N=\sum_a\|N_a\|_{\rm op}^2`$. Centered incoming noise
strength satisfies $`y_n^2\le K_N`$. The trace-norm distance between
the projectors of $`\psi`$ and $`\Phi`$ is at most
$`2\sqrt\epsilon`$. Applying this to both terms defining each
jump variance gives $`|x_n^2-\nu|\le6K_N\sqrt\epsilon`$.
Inserting the engineered bound in the population balance and using
$`r^2\le(16/15)\epsilon`$ yields

```math
\kappa x_n^2\le \frac{24}{5}\epsilon B^2
                       +\frac85\epsilon\kappa K_N.
```

For $`\epsilon\le\min\{1/16,(\nu/(12K_N))^2\}`$, the left
side is at least $`\kappa\nu/2`$ and the noise inflow term on the
right is at most $`\kappa\nu/4`$. Consequently,

```math
\kappa\nu\le1280\Gamma\,\epsilon(\epsilon+\delta^2).
```

At least one of $`\epsilon^2`$ and $`\epsilon\delta^2`$ is at
least half the lower bound on their sum. This gives the claimed minimum
of the two scales. At errors above the fixed threshold the same order
bound follows after decreasing its constant, since
$`\min\{\sqrt f,f/\delta^2\}\le1`$ for $`f\le1`$.

## Exact-local witness in every fixed dimension

Choose Schmidt bases for $`\Phi=d^{-1/2}\sum_a|aa\rangle`$.
Choose fixed real numbers $`h_a`$ with $`\sum_a h_a=0`$ and
$`\sum_a h_a^2=d`$. For example, take
$`h_1=\sqrt{d/2}`$, $`h_2=-\sqrt{d/2}`$ and the others zero.
For small real $`t`$, set

```math
s_a=1+t h_a,\qquad
|\psi_t\rangle=\frac{\sum_a s_a|aa\rangle}{\sqrt{d(1+t^2)}},\qquad
P_t=|\psi_t\rangle\langle\psi_t|,\qquad
Q_t=I-P_t .
```

Use the off-diagonal matrix units $`F_{ab}=|a\rangle\langle b|`$
and the local-sum jumps

```math
W_{ab}=F_{ab}\otimes I-\frac{s_b}{s_a}I\otimes F_{ba},
\qquad a\ne b .
```

They annihilate $`\psi_t`$. The squared operator norm of $`W_{ab}`$
is $`1+(s_b/s_a)^2`$. In fact, on $`|ba\rangle`$ the two
terms have orthogonal outputs, and on the span of $`|aa\rangle`$
and $`|bb\rangle`$ they form a single row with output
$`|ab\rangle`$. The remaining nonzero inputs are mapped to distinct
orthogonal outputs with amplitudes of magnitude $`1`$ or
$`s_b/s_a`$. The two nontrivial blocks each attain the stated norm.
With

```math
K(t)=\sum_{a\ne b}\|W_{ab}\|_{\rm op}^2=2d(d-1)+O(t^2),
\qquad
\mathcal A_t=\frac{1}{K(t)}\sum_{a\ne b}\mathcal D[W_{ab}],
```

the engineered generator $`\Gamma\mathcal A_t`$ uses exactly
$`\Gamma`$ and has $`E_\mu=0`$. The linear term in $`K(t)`$
cancels between ordered pairs.

### Slow eigenvalue and its noise response

At $`t=0`$, vectorization identifies $`W_{ab}`$ with the
commutator action of $`F_{ab}`$. The list is closed under adjoints.
On operator space, $`\mathcal A_0`$ is therefore self-adjoint and
negative semidefinite in the Hilbert–Schmidt inner product. Its quadratic
form is the negative sum of squared commutators with the jumps, divided
by $`2K(0)`$. Its kernel is their commutant. The off-diagonal matrix
units generate $`\mathfrak{sl}_d(\mathbb C)`$ under commutators,
and its adjoint action on traceless matrices is irreducible by simplicity.
The scalar and traceless matrix subspaces are inequivalent irreducible
representations. The commutant is exactly the span of $`P_0`$ and
$`Q_0=I-P_0`$. All other eigenvalues are strictly negative in this
fixed dimension.

For small $`t`$, use the orthogonal splitting into $`P_t`$ and
$`Q_t`$. Each jump has a block matrix of the form

```math
W_{ab}=\begin{pmatrix}0&b_{ab}^\dagger\\0&T_{ab}\end{pmatrix}.
```

The derivative of a state's $`Q_t\rho Q_t`$ block depends only on
that block. On this space the induced map $`\mathcal B_t`$ is

```math
\mathcal B_t(X)=\frac1{K(t)}\sum_{a\ne b}
\left(T_{ab}XT_{ab}^\dagger
  -\tfrac12\{T_{ab}^\dagger T_{ab}+b_{ab}b_{ab}^\dagger,X\}\right).
```

The trace of this block obeys

```math
\operatorname{Tr}\mathcal B_t(X)
=-\frac{1}{K(t)}\sum_{a\ne b} b_{ab}^\dagger Xb_{ab}.
```

At $`t=0`$ this block has a simple zero eigenvalue with trace-one
eigenmatrix $`Q_0/(d^2-1)`$. Identify the moving subspaces with their
values at zero by a smooth analytic unitary rotation that takes
$`\psi_t`$ to $`\Phi`$. Finite-dimensional perturbation at the
isolated simple eigenvalue then gives a trace-one eigenmatrix
$`R_t=Q_t/(d^2-1)+O(t)`$ for $`\mathcal B_t`$.

The component of $`W_{ab}^\dagger\psi_t`$ in $`Q_t`$ is the
whole vector, and its explicit value is

```math
b_{ab}=W_{ab}^\dagger\psi_t
=\frac{s_a^2-s_b^2}{s_a\sqrt{d(1+t^2)}}|ba\rangle .
```

Hence $`\sum_{a\ne b}\|b_{ab}\|^2=8dt^2+O(t^3)`$. Taking the
trace of $`\mathcal B_t(R_t)`$ gives its eigenvalue

```math
z(t)=-\beta_d t^2+O(t^3),\qquad
\beta_d=\frac{4}{(d-1)(d^2-1)}.
```

The block dependence shows that $`z(t)`$ is also an eigenvalue of
$`\mathcal A_t`$. For small nonzero $`t`$ it is the only eigenvalue
approaching zero on the trace-zero subspace. Indeed, at zero the
restriction to that subspace has a simple zero eigenvalue,
and the other eigenvalues remain bounded away from the imaginary axis.
The corresponding spectral projection $`\Pi_t`$ therefore has a
bounded analytic continuation with

```math
\Pi_0(X)=\left(\frac{Q_0}{d^2-1}-P_0\right)\operatorname{Tr}(Q_0X),
\qquad \operatorname{Tr}X=0 .
```

On this subspace the inverse is $`z(t)^{-1}\Pi_t+O(1)`$.
The bounded term is the inverse on the complementary spectral subspace,
which stays invertible as $`t\to0`$.

Now use the full generator $`\Gamma(\mathcal A_t+f\mathcal N)`$
with engineered $`H=0`$. The simple slow eigenvalue on the trace-zero
subspace changes by $`O(f)`$ uniformly near $`t=0`$.
This follows from analytic perturbation in both $`t`$ and $`f`$
using a fixed contour that isolates that eigenvalue from the fast spectrum.
When $`f/t^2\to0`$, every trace-zero eigenvalue has negative real
part, including the slow one. The finite-dimensional quantum dynamical
semigroup has a stationary density matrix, and negativity on the
trace-zero subspace establishes uniqueness and convergence from every
initial state.

With $`\rho_*=P_t+X`$ and $`\operatorname{Tr}X=0`$, stationarity
gives $`X=-f(\mathcal A_t+f\mathcal N)^{-1}\mathcal N(P_t)`$.
Expanding the inverse about $`\mathcal A_t^{-1}`$ is controlled by
$`f\|\mathcal A_t^{-1}\|=O(f/t^2)`$. The projection formula and
$`\operatorname{Tr}(Q_0\mathcal N(P_0))=\nu`$ then give

```math
X=\frac{\nu f}{\beta_d t^2}
    \left(\frac{Q_0}{d^2-1}-P_0\right)
    +O\left(\frac{f}{|t|}+\frac{f^2}{t^4}\right).
```

The infidelity of $`P_t`$ to the target is $`t^2/(1+t^2)`$.
With $`t^2=\sqrt{\nu f/\beta_d}`$, the two leading errors balance
and the stationary infidelity is

```math
\epsilon
=2\sqrt{\frac{\nu}{\beta_d}}\sqrt f+o(\sqrt f)
=\sqrt{(d-1)(d^2-1)\nu}\,\sqrt f+o(\sqrt f).
```

This is a coefficient for the chosen reservoir. With $`d=2`$ and
$`\mathcal N=\mathcal D[Z\otimes I]`$, it recovers the
$`\sqrt3`$ coefficient of the
[exact dephasing example](attaining_reservoir.md).

## Nonlocal witness above the crossover

Let $`m=d^2-1`$, fix an orthonormal basis
$`\{|q_j\rangle\}_{j=1}^m`$ of $`Q_0`$, and take

```math
J_j=E_j=\sqrt\gamma\,|\Phi\rangle\langle q_j|,
\qquad L_j=0,\qquad \gamma=\frac{\Gamma\delta^2}{m}.
```

These jumps return the orthogonal population to the target, with total
squared norm $`m\gamma=\Gamma\delta^2\le\Gamma`$. Set the
engineered Hamiltonian to zero. In the absence of imposed noise,
the $`Q_0\rho Q_0`$ block decays at rate $`\gamma`$, and
the $`P_0\rho Q_0`$ and $`Q_0\rho P_0`$ blocks decay at
rate $`\gamma/2`$. On the trace-zero subspace these are all the
decay rates.

On the branch $`\delta^2\ge\sqrt f`$ the perturbation strength
after division by $`\gamma`$ is
$`\kappa/\gamma=mf/\delta^2\le m\sqrt f`$. For small $`f`$
the perturbed trace-zero spectrum therefore lies strictly in the left
half-plane uniformly on this branch. The unique globally attracting
stationary state satisfies $`\rho_*=P_0+O(\kappa/\gamma)`$, by the
inverse on the trace-zero subspace. Its orthogonal population satisfies
the exact evolution equation

```math
\frac{d}{du}\operatorname{Tr}(Q_0\rho(u))
=-\gamma\operatorname{Tr}(Q_0\rho(u))
 +\kappa\operatorname{Tr}(Q_0\mathcal N(\rho(u))) ,
```

where $`u`$ denotes physical time. At stationarity this gives

```math
\epsilon=\nu\,\frac{mf}{\delta^2}
            +O\!\left(\frac{m^2 f^2}{\delta^4}\right).
```

Use the exact-local reservoir for $`\delta^2\le\sqrt f`$ and
the reset reservoir for $`\delta^2\ge\sqrt f`$. These bounds
give the uniform upper order. The two branches meet at
$`\delta\asymp f^{1/4}`$.

## Attribution and physical scope

The proof uses the spectral balance of
[Linowski, Rudnicki and Gneiting](../references/RELATED_WORK.md#linowski2023)
and the maximal-entanglement transpose identity used by
[Pocklington and Clerk](../references/RELATED_WORK.md#pocklington2024).
Pocklington and Clerk also give the modular dark-jump construction
in Eq. (24), the incoming norm in Appendix B.2, and an extra return
term from unused levels in Appendix A.5. The present model keeps the
full factors equal and quantifies the stationary noise penalty when the
effective engineered jumps carry a bounded departure from local-sum
form. The local-sum witness uses their construction with a deterministic
matrix-unit choice and computes the response to additive noise through
its isolated slow mode. The second witness is pure-target dissipative
reset of the type studied in
[Kraus et al., Physical Review A 78, 042307 (2008)](https://doi.org/10.1103/PhysRevA.78.042307),
with its rate charged to the departure budget.

The departure budget concerns effective jump operators. Using it to
predict a laboratory crossover requires deriving those operators and
their budgets from the device model. In particular, the microscopic
derivation in Appendix F of Pocklington and Clerk assumes a
noninteracting bare system Hamiltonian. A quantitative link from a
microscopic interaction to $`\delta`$ and estimates uniform in dimension
require separate analysis. The result requires a positive outgoing noise
rate at the target.
