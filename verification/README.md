# Verification of the attaining reservoir

These deterministic checks compare the analytical two-qubit construction with its full $`16\times16`$ Lindblad generator. The written [reservoir derivation](../science/attaining_reservoir.md) supplies the arguments for arbitrary inputs and parameters. The scripts check conventions, algebraic formulas, and numerical consistency at the declared values.

## Run

From the repository root, install the dependencies in the root requirements file and run:

```bash
python3 -m pip install -r requirements.txt
python3 verification/verify_reservoir.py
```

The verifier prints a JSON report and exits nonzero if a check fails. To retain the full report locally:

```bash
python3 verification/verify_reservoir.py --report verification/run_report.json
```

The recorded reference run used Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. NumPy supplies dense matrix operations and SciPy supplies the matrix exponential, eigensolver, and bracketed scalar root solver. Exact rational checks use only Python's standard-library `fractions` module.

## Files and expected outputs

| File | Role |
|---|---|
| [reservoir.py](reservoir.py) | Full generator, direct matrix action, state formulas, population solutions, and scalar optimizer |
| [verify_reservoir.py](verify_reservoir.py) | Deterministic checks, tolerances, and JSON reporting |
| [expected_results.json](expected_results.json) | Checked-in reference values for all parameter cases and the exact rational example |

The expected output stores stable physical quantities, including population rates, the family optimizer, its infidelity, stationary-state eigenvalues, and exact fractions. Runtime versions and floating-point residuals appear in the generated report. Those residuals are bounded explicitly rather than required to match another machine's last bits.

Reference numbers are compared with relative tolerance $`5\times10^{-10}`$ and absolute tolerance $`5\times10^{-13}`$. Matrix identities, normalization, jump norms, and stationarity must have residual at most $`2\times10^{-12}`$. The direct stationary solve and long-time matrix-exponential comparisons allow $`2\times10^{-9}`$, accommodating the conditioning near the balanced limit. These are numerical checking tolerances, not bounds on physical preparation error.

## What is checked

### Full generator and column vectorization

The basis is $`(|00\rangle,|01\rangle,|10\rangle,|11\rangle)`$. Operator vectors stack columns, so

```math
\operatorname{vec}(AXB)=(B^T\otimes A)\operatorname{vec}(X).
```

The generator matrix is constructed as

```math
G=-i(I\otimes H-H^T\otimes I)
+\sum_\mu\left[
J_\mu^*\otimes J_\mu
-\frac12 I\otimes J_\mu^\dagger J_\mu
-\frac12(J_\mu^\dagger J_\mu)^T\otimes I
\right].
```

A separate direct matrix implementation evaluates $`-i[H,X]+\sum_\mu\mathcal D[J_\mu](X)`$ on all 16 matrix units and compares it with $`G\operatorname{vec}(X)`$. This check uses complex jumps obtained by a local phase rotation and a complex Hermitian Hamiltonian. It therefore detects transpose/conjugation mistakes that could remain hidden for purely real matrices. Trace preservation and Hermiticity preservation are checked on the same full operator basis.

### Pure reservoir

The four pure cases have $`g=1`$ and design errors $`\delta_0=10^{-1},10^{-2},10^{-3},10^{-4}`$. The checks cover:

- Both engineered squared jump norms equal $`g`$, giving $`\Gamma=2g`$.
- The inherited dark state is stationary.
- The three adjoint population identities hold as matrix identities, so the closed population equations apply to arbitrary input coherences.
- Full matrix-exponential evolution agrees with both exact survival functions, for initial bright and odd states.
- The population and trace-distance bounds hold for the bright state, an odd state, a computational product state, and a state with complex coherences at the specified times.
- The numerical generator has one zero eigenvalue, and its numerical gap agrees with the population decay rate for these cases.

The operational mixing bound is proved in [Section 3 of the derivation](../science/attaining_reservoir.md#3-closed-populations-and-uniform-mixing) using populations and trace distance. The finite eigenvalue checks are not its proof and imply no general spectral-gap theorem.

### Noisy reservoir and optimization

The six noisy cases use $`g=1`$ and $`r=\kappa/g\in\{10^{-2},10^{-3},10^{-4},10^{-5},10^{-6},10^{-8}\}`$. For each case, the unique root of the strictly decreasing polynomial $`Q_r(b)`$ determines the global optimum within the family. The checks compare the exact X-state with a numerical stationary solve using all 16 operator entries, without an X-state constraint. They also check positivity, trace, full-generator stationarity, the exact Bell infidelity, the physical jump budget, and the optimizer equation.

For orientation, the reference values include:

| $`r`$ | Optimal infidelity | $`\epsilon_{\mathrm{opt}}/\sqrt{\kappa/\Gamma}`$ |
|---:|---:|---:|
| $`10^{-4}`$ | 0.01213508083 | 1.716159589 |
| $`10^{-6}`$ | 0.001223619999 | 1.730459998 |
| $`10^{-8}`$ | 0.0001224632373 | 1.731891710 |

The last column approaches $`\sqrt3\simeq1.732050808`$. The asymptotic coefficient follows from the written optimization proof; a numerical trend alone would not establish it. This coefficient is specific to the squeezed-pair family. The comparison with the universal converse establishes a global order, not an optimal global coefficient.

### Exact rational stationarity

An additional example uses

```math
u=\frac45,\qquad v=\frac35,\qquad
g=\frac32,\qquad\kappa=\frac1{80},\qquad r=\frac1{120}.
```

The unscaled jumps and all state entries are rational. The script multiplies the complete $`4\times4`$ matrices using exact fractions and verifies all entries of

```math
g\mathcal D[\ell_1](\rho_*)
+g\mathcal D[\ell_2](\rho_*)
+\kappa\mathcal D[Z_A](\rho_*)=0.
```

It also checks unit trace, positive diagonal entries and even-block determinant, and agreement of the exact fidelity with the derived formula. The resulting Bell infidelity is exactly $`5153/35650`$. This check resolves algebraic consistency independently of floating-point stationarity residuals and covers a nonunit value of $`g`$.

## Recorded residuals and limits

In the reference run, the largest column-vectorization discrepancy was $`4.45\times10^{-16}`$ or smaller. Pure stationary and population-identity residuals were below $`3\times10^{-16}`$, and the largest pure survival discrepancy was below $`1.27\times10^{-12}`$. Noisy stationary residuals were below $`3.20\times10^{-16}`$; the unconstrained stationary solve agreed with the exact state within $`5.17\times10^{-13}`$. The rational example had exactly zero stationary residual in every entry.

The checks concern this explicitly specified family. The general variance, mixing, and noise-floor converses require their written proofs. Likewise, the arguments for faithfulness, uniqueness, convergence, and the asymptotic family optimum are analytical; finite samples corroborate their formulas and do not replace those arguments.
