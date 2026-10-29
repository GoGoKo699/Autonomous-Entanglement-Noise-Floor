# Related work and attribution

This project concerns a specified autonomous architecture: a time-independent Lindblad generator on two finite, equal-dimensional factors, with jumps

```math
J_\mu=A_\mu\otimes I+I\otimes B_\mu,
\qquad K=\sum_\mu\|J_\mu\|_{\mathrm{op}}^2,
```

and an otherwise unrestricted Hamiltonian. The target is maximally entangled across the **entire** two factors. The resource convention uses the supplied physical jump decomposition.

The contribution developed here is a uniform robustness bound for a possibly mixed stationary state. If its target infidelity is $`\epsilon`$, the total centered outgoing jump variance of its leading eigenvector is $`O(K\epsilon^2)`$. Compulsory local noise with nonzero variance at the target therefore produces an infidelity floor of order $`\sqrt{\kappa/K}`$. For the explicit independent qubit-dephasing model, a known two-qubit reservoir attains this order. A separate stationary-block argument bounds the rate of change of a rank-one observable and gives an operational mixing-time lower bound without imposing a Hamiltonian norm limit.

The spectral balance identity, the maximally entangled transpose identity, the pure-state slowdown mechanism, and the attaining reservoir all have antecedents below. The claimed addition is the uniform mixed-state optimization and its consequences. It does not rest on inventing a new reservoir or on an informal estimate of noise rate multiplied by inverse spectral gap.

## Contribution and source map

| Ingredient or comparison | Source | Role here |
|---|---|---|
| Stationarity in an eigenbasis; population flux balance | [Linowski, Rudnicki and Gneiting](#linowski2023), Proposition 1 and Eqs. (31)–(33) | Inherited identity |
| Local-sum jumps, full-space maximal entanglement, and pure-state dynamical isolation | [Pocklington and Clerk, 2024](#pocklington2024), Secs. II–III | Inherited structural mechanism |
| Squeezed-pair two-qubit reservoir | [Govia, Lingenfelter and Clerk](#govia2022), Eqs. (8)–(9); [Pocklington and Clerk, 2025](#pocklington2025), Eq. (7) | Inherited family used for sharpness |
| Fidelity limits with a prescribed coherent-control variance | [O'Connor, Ma and Genoni](#oconnor2025), Sec. II.2 | Different resource assumption |
| Added levels and retained adaptive memory | [Brown et al.](#brown2022); [Pocklington and Clerk, 2025](#pocklington2025) | Established ways to change the architecture |
| Remote stationary-entanglement experiments with local losses | [Irfan et al.](#irfan2026); [Andrés-Juanes et al.](#andres2026) | Physical motivation and protocol-specific comparisons |

The bibliography is available in [references.bib](references.bib). Equation and appendix locations below identify the inspected arXiv versions; published article metadata are used in the bibliography.

<a id="linowski2023"></a>
## Spectral stationarity

**Tomasz Linowski, Łukasz Rudnicki and Clemens Gneiting, “Spectral stabilizability,” Physical Review A 107, 042218 (2023).** [Published article](https://doi.org/10.1103/PhysRevA.107.042218) · [Full text, arXiv:2212.12245v2](https://arxiv.org/html/2212.12245v2).

Proposition 1 characterizes stabilizability through the eigenstructure of the target density matrix. Section III, Eqs. (31)–(33), decomposes a mixed state into a distinguished pure eigenvector and an orthogonal remainder, then balances dissipative population flow into and out of that eigenvector. This is precisely the population identity used here; Eq. (5) also gives the related Hamiltonian reconstruction principle.

The identity can be applied parametrically to engineered dissipators. Thus the fact that particular examples in that paper fix a dissipator is not, by itself, a novelty distinction. The additional step here bounds the flux uniformly as the leading eigenvector approaches a full-space maximally entangled vector, while allowing that eigenvector, the mixed remainder, the engineered local-sum jumps and the Hamiltonian to vary.

<a id="pocklington2024"></a>
## Pure-state entanglement and relaxation

**Andrew Pocklington and Aashish A. Clerk, “Universal Time-Entanglement Trade-off in Open Quantum Systems,” PRX Quantum 5, 040305 (2024).** [Published article](https://doi.org/10.1103/PRXQuantum.5.040305) · [Full text, arXiv:2404.03625v2](https://arxiv.org/html/2404.03625v2).

Sections II–III treat the same local-sum jump structure with arbitrary Hamiltonian interactions and an exactly pure stationary state. At maximal entanglement, the dark-state condition also eliminates incoming jumps; the target projector becomes a strong symmetry. The resulting dynamical isolation and the quantitative pure-state slowdown are inherited. Their commutator argument and the equivalent transpose/vectorization identity supply the structural input to the present proof.

A mixed stationary state need not satisfy the individual dark-state conditions. The present argument replaces them by spectral flux balance and controls the leading eigenvector uniformly. It also establishes an observable-based mixing bound rather than inferring a general spectral-gap bound from it.

Appendix A.5 discusses unequal local dimensions. Appendix F's microscopic derivation assumes a noninteracting system Hamiltonian before frequency decomposition. Microscopic local bath couplings alone therefore do not establish the required jump form for arbitrary dressed, interacting systems.

<a id="govia2022"></a>
## The inherited squeezed-pair reservoir

**L. C. G. Govia, A. Lingenfelter and A. A. Clerk, “Stabilizing two-qubit entanglement by mimicking a squeezed environment,” Physical Review Research 4, 023010 (2022).** [Published article](https://doi.org/10.1103/PhysRevResearch.4.023010) · [Full text, arXiv:2110.06201v2](https://arxiv.org/html/2110.06201v2).

Equations (8)–(9) give two dissipative channels combining one qubit's lowering operator with the other's raising operator. Choosing matched amplitudes produces the squeezed-pair family used here. Section V discusses the preparation-time/entanglement tradeoff and competition with uncontrolled decoherence; Sec. V.1, Eq. (32), identifies a slow mode.

The reservoir and its pure entangled stationary state are established constructions. Here the same family is used to compute the exact stationary state with an added, independently specified local dephasing channel and to attain the order of the model-wide converse. Protocol-specific slowing or optimizing this one family alone would not prove the lower bound over all allowed generators.

The beginning of Sec. V also explains that increasing squeezing while keeping modulation amplitudes bounded changes the overall dissipative rate. This distinction matters for the resource comparison below.

<a id="pocklington2025"></a>
## Adaptive, auxiliary and fermionic alternatives

**Andrew Pocklington and Aashish A. Clerk, “Accelerating Dissipative State Preparation with Adaptive Open Quantum Dynamics,” Physical Review Letters 134, 050603 (2025).** [Published article](https://doi.org/10.1103/PhysRevLett.134.050603) · [Full text, arXiv:2409.06012v2](https://arxiv.org/html/2409.06012v2).

Equation (7), restricted to one qubit on each side and zero Hamiltonian, is another explicit source for the attaining reservoir. The paper also shows how fermionic anticommutation, jump-parity tracking with one classical memory bit, and an auxiliary-qubit autonomous implementation can remove the pure-state slowdown.

These are established architectural alternatives. A retained memory changes the reduced, two-factor Markovian description; fermionic locality need not become a local-sum qubit jump after a Jordan–Wigner transformation. The present result does not supersede these schemes. It quantifies the noise penalty while remaining in the declared architecture.

Feedback is not automatically outside the theorem: an unconditional, time-independent feedback generator that retains the stated tensor factors and local-sum jumps still satisfies its premises. The relevant issue is the resulting mathematical model.

<a id="brown2022"></a>
## An experimental added-level escape

**T. Brown et al., “Trade off-free entanglement stabilization in a superconducting qutrit-qubit system,” Nature Communications 13, 3994 (2022).** [Published article](https://doi.org/10.1038/s41467-022-31638-0) · [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271051/).

The protocol uses a transmon's second-excited level and engineered dissipation to transfer population into a Bell state without the usual coherent leakage. The effective jump in Eq. (2) and the mechanism in Fig. 2 make the added level operationally important.

The target is maximally entangled in a selected two-level subspace of a qutrit–qubit system. It is not maximally entangled across two equal-dimensional, entire local spaces. Consequently this known experiment lies outside the full-space premise of the present bound. The project does not claim that all autonomous entanglement stabilizers, or all models with local-sum effective jumps regardless of target support, obey the same floor.

<a id="oconnor2025"></a>
## Fidelity bounds with a coherent-control constraint

**Eoin O'Connor, Hailan Ma and Marco G. Genoni, “Bounding fidelity in quantum feedback control: theory and applications to Dicke state preparation,” Quantum Science and Technology 10, 035049 (2025).** [Published article](https://doi.org/10.1088/2058-9565/ade55f) · [Full text, arXiv:2503.19151v2](https://arxiv.org/html/2503.19151v2).

Section II.2, Eq. (9), imposes an upper bound on the Hamiltonian variance in the target state, and Sec. II.4 combines coherent and dissipative estimates into a fidelity bound. Appendix B compares this with the earlier [Kobayashi–Yamamoto control bound, Physical Review A 99, 052347 (2019)](https://doi.org/10.1103/PhysRevA.99.052347).

The constraint is on target-state variance, not the global Hamiltonian norm; it already allows arbitrarily strong dynamics inside the orthogonal subspace. Removing the variance budget removes the nontrivial coherent-control restriction in that argument. The present result instead uses stationarity and the local-sum structure to bound the relevant block of the gauge-adjusted Hamiltonian after centering the jumps, without prescribing a variance or norm budget. Its assumptions are more specific in architecture and stationarity, while the feedback-control treatment covers broader trajectories and monitoring choices.

<a id="irfan2026"></a>
## Cascaded-network experiment

**Abdullah Irfan et al., “Autonomous Stabilization of Remote Entanglement in a Cascaded Quantum Network,” Physical Review X 16, 031004 (2026), published 13 July 2026.** [Published article](https://doi.org/10.1103/z6zz-vw5q) · [Full text, arXiv:2509.11872v3](https://arxiv.org/html/2509.11872v3).

This experiment stabilizes remote superconducting-qubit entanglement with nonreciprocal waveguide coupling and local drives. Synthetic-squeezing symmetry improves robustness to coupling mismatch. Appendix G's “Effect of local noise” explains competition between unwanted decay and engineered repumping; Appendix I optimizes concurrence within the available drive family.

The work motivates a bound that allows alternative autonomous Hamiltonians and dissipators rather than optimizing only those drives. Its reported concurrence approaching 0.5 is not evidence for the present near-unit-fidelity asymptotic law. Concurrence, target-state fidelity and the declared dissipative budget must be distinguished before making quantitative comparisons.

<a id="andres2026"></a>
## Nonlocal squeezed-reservoir experiment

**A. Andrés-Juanes et al., “Distributing Stationary Qubit Entanglement through a Nonlocal Squeezed Reservoir,” Physical Review X 16, 031005 (2026), published 13 July 2026.** [Published article](https://doi.org/10.1103/r4jt-j39w) · [Inspected preprint, arXiv:2510.07139v1](https://arxiv.org/html/2510.07139v1), titled *Entangling remote qubits through a two-mode squeezed reservoir*.

A Josephson parametric converter supplies correlated propagating fields to separate superconducting qubits. The preprint's Eq. (18) gives an effective qubit master equation after eliminating the converter, including local dephasing and relaxation. Appendix H optimizes squeezing in the presence of specified experimental imperfections.

This supplies a current physical setting for the competition between engineered correlations and local noise. The reported data and protocol-specific optimization are not a validation of a uniform high-fidelity theorem. Applying that theorem requires a justified reduced Markovian description, a local-sum jump representation, an independently fixed noise channel, and a consistent resource normalization.

## Normalization and scope when comparing results

Use the convention

```math
\mathcal D[J](\rho)=J\rho J^\dagger-\tfrac12\{J^\dagger J,\rho\}.
```

Then $`\kappa\mathcal D[Z]`$ damps a single-qubit off-diagonal matrix element at rate $`2\kappa`$. For example, the dephasing convention in Andrés-Juanes et al., Eq. (18), uses $`(\gamma_\phi/2)\mathcal D[Z]`$. Its $`\gamma_\phi`$ therefore corresponds to $`2\kappa`$, not $`\kappa`$, in this project's explicit dephasing example.

For squeezed jumps

```math
\sqrt{\gamma}\bigl(\cosh s\,\sigma_A^-+\sinh s\,\sigma_B^+\bigr),
\qquad
\sqrt{\gamma}\bigl(\cosh s\,\sigma_B^-+\sinh s\,\sigma_A^+\bigr),
```

the sum of squared operator norms is $`2\gamma\cosh(2s)`$. Holding the bare coefficient $`\gamma`$ fixed while increasing squeezing therefore increases the charged resource. It is a different optimization from holding $`K`$ fixed. A cavity linewidth, drive amplitude or cooperativity cannot be substituted for $`K`$ without deriving the effective jumps and their normalization.

The budget is attached to the declared physical representation; it is not claimed to be a gauge-invariant norm of the generator. Centering jumps in the proof is an analytical step with a controlled norm cost, not an uncharged change of the physical noise model. Compulsory noise is an independent additive Lindblad channel. If control changes its correlations or cancels its amplitude at the bath level, that premise must be reconsidered.

The result also does not bound Bell fidelity after tracing out retained cavities or local memories. Added levels, retained memory, time dependence and effective product-type nonlocal jumps must be assessed through the precise model and target support. The exact spectral identities and known escape protocols above help identify those boundaries; they are not new contributions of this project.
