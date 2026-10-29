# Thirty milestones through the entanglement noise-floor argument

This map follows the scientific structure of the project: the geometry of a high-fidelity stationary state, the restrictions imposed by local-sum dissipation, the resulting noise and mixing limits, and an explicit reservoir that attains the exponents.

The single educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_**, [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2). The [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md) connects its background material to the public science notes. The project's research antecedents have a different role: their identities, constructions, and scope are credited in [Related work](../references/RELATED_WORK.md).

There are **12 foundation milestones and 18 milestones on the argument and its contributions**. The foundations give state geometry, quantum dynamical maps, stationary-state language, and representation-sensitive resource accounting enough room to remain distinct. The larger second part reflects the project's actual structure: two universal consequences, a separately analyzed attaining model, and a comparison that keeps global conclusions apart from properties of one family. The milestones are conceptual units, not equal-sized portions of a text. Dependencies refer only to earlier milestones; every unit also has a direct route into the scientific account.

## Part I — Foundations and inherited structural tools

<a id="milestone-01"></a>
### M01. The state and the system boundary

**Central question:** Which degrees of freedom belong to the state whose stationary entanglement is being constrained?

**Understanding target:** The object is a density operator on the complete finite space $`\mathcal H_A\otimes\mathcal H_B`$, with equal local dimension $`d\ge2`$. Positivity, unit trace, tensor factors, and partial traces have distinct roles. A reduced two-qubit state obtained after tracing out a retained cavity or memory need not obey the same closed dynamical model as the full system.

**Dependencies:** None.

**Conceptual connection:** Choosing the system boundary determines both the meaning of maximal entanglement and which dissipative generators are admissible. The boundary is therefore part of the theorem, rather than a choice of notation.

**Pointers:** [Model: dynamics and resource convention](../science/model.md#1-dynamics-and-the-resource-convention); [interpretation: architectures and premises](../science/interpretation.md#4-architectures-and-tasks-that-change-the-premises); [bridge: states and norms](RIVAS_HUELGA_BRIDGE.md#states-and-norms).

<a id="milestone-02"></a>
### M02. Maximal entanglement on the full factors

**Central question:** What does the maximally entangled target require of both local reduced states?

**Understanding target:** A full-space maximally entangled vector has uniform Schmidt coefficients and reduced states $`I_d/d`$. Local Schmidt bases put it in the form $`d^{-1/2}\sum_j|j,j\rangle`$ without changing operator norms. A Bell vector embedded in a larger computational subspace may be maximally entangled in the smaller-dimension sense while failing this equal-full-factor premise.

**Dependencies:** [M01](#milestone-01).

**Conceptual connection:** Uniform marginals make a local traceless observable have zero target expectation; the same uniformity later makes forward and adjoint jump strengths equal at the target.

**Pointers:** [Rigidity: model and conventions](../science/rigidity.md#model-and-conventions); [rigidity: maximally entangled transpose identity](../science/rigidity.md#4-the-maximally-entangled-transpose-identity); [bridge: spectral balance and transpose](RIVAS_HUELGA_BRIDGE.md#spectral-balance-and-transpose).

<a id="milestone-03"></a>
### M03. Target fidelity, purity, and spectral weight

**Central question:** Which notion of error appears in the results, and what does it say about a mixed state?

**Understanding target:** The error is exactly $`\epsilon=1-\langle\Phi|\rho_*|\Phi\rangle`$. It is neither $`1-\mathrm{Tr}\rho_*^2`$ nor the population outside an eigenvector chosen in advance. The largest eigenvalue satisfies the Rayleigh-quotient bound $`\lambda\ge1-\epsilon`$, but the corresponding eigenvector can differ from $`|\Phi\rangle`$.

**Dependencies:** [M01](#milestone-01), [M02](#milestone-02).

**Conceptual connection:** High target fidelity controls a spectral component without making the stationary state pure. Allowing that component to rotate is essential to the mixed-state optimization.

**Pointers:** [Model: fidelity and mixing](../science/model.md#2-fidelity-and-mixing); [rigidity: the leading eigenvector](../science/rigidity.md#1-the-leading-eigenvector-is-close-to-the-target); [bridge: states and norms](RIVAS_HUELGA_BRIDGE.md#states-and-norms).

<a id="milestone-04"></a>
### M04. Trace distance as an observable-probability bound

**Central question:** How does a bound on a state distance constrain a particular measurement probability?

**Understanding target:** The convention is half trace distance, $`D_{\mathrm{tr}}(\rho,\sigma)=\|\rho-\sigma\|_1/2`$. An effect $`0\le E\le I`$ has probability difference at most this distance. For two pure states, the distance is $`\sqrt{1-|\langle\phi|\psi\rangle|^2}`$. Operator-norm/trace-norm duality also bounds the change of an expectation, including a complex expectation of a non-Hermitian operator.

**Dependencies:** [M01](#milestone-01), [M03](#milestone-03).

**Conceptual connection:** The same geometry transfers high fidelity into a small noise-expectation change and turns a slowly varying projector into an operational mixing obstruction.

**Pointers:** [Mixing: required observable change](../science/mixing.md#3-mixing-requires-a-finite-change-in-that-observable); [noise floor: local dephasing](../science/noise_floor.md#1-local-dephasing); [bridge: states and norms](RIVAS_HUELGA_BRIDGE.md#states-and-norms).

<a id="milestone-05"></a>
### M05. A fixed quantum dynamical semigroup

**Central question:** What is assumed when the evolution is written as $`\mathcal T_t=e^{t\mathcal L}`$?

**Understanding target:** Complete positivity, trace preservation, and the semigroup law describe one time-independent Markovian evolution on the declared system. Contractivity of trace distance applies to two states under the same channel. It does not identify a reduced evolution with a semigroup merely because an enlarged system has a Markovian description.

**Dependencies:** [M01](#milestone-01), [M04](#milestone-04).

**Conceptual connection:** The semigroup assumption gives a precise meaning to autonomous stabilization and makes distance from a stationary state nonincreasing. Retained memory and scheduled changes of the generator alter this structure.

**Pointers:** [Mixing: model and convention](../science/mixing.md#model-and-mixing-convention); [interpretation: architectures and premises](../science/interpretation.md#4-architectures-and-tasks-that-change-the-premises); [bridge: semigroups and adjoints](RIVAS_HUELGA_BRIDGE.md#semigroups-and-adjoints).

<a id="milestone-06"></a>
### M06. The generator and independent physical channels

**Central question:** Which part of the Lindblad generator represents coherent dynamics, and which part supplies irreversible transitions?

**Understanding target:** The convention is $`\mathcal D[J](\rho)=J\rho J^\dagger-\{J^\dagger J,\rho\}/2`$. The physical jumps are local sums $`A\otimes I+I\otimes B`$, not arbitrary operators on the pair. An independently specified background channel is added as its own dissipator. For the displayed dephaser, $`\kappa\mathcal D[Z_A]`$ damps a single-qubit coherence at rate $`2\kappa`$.

**Dependencies:** [M01](#milestone-01), [M05](#milestone-05).

**Conceptual connection:** Adding independent channels adds their outgoing variances with nonnegative signs. Coherently replacing the amplitude of the background jump is a different noise model.

**Pointers:** [Model: dynamics](../science/model.md#1-dynamics-and-the-resource-convention); [model: compulsory dephasing](../science/model.md#4-compulsory-dephasing-and-optimal-bell-error); [bridge: Lindblad form and gauge](RIVAS_HUELGA_BRIDGE.md#lindblad-and-gauge).

<a id="milestone-07"></a>
### M07. Schrödinger and Heisenberg descriptions

**Central question:** How can the same generator describe motion of states and motion of observable expectations?

**Understanding target:** The adjoint is defined by the trace pairing, so $`d\mathrm{Tr}(X\rho_t)/dt=\mathrm{Tr}(\mathcal L^\dagger(X)\rho_t)`$. A small operator norm of $`\mathcal L^\dagger(X)`$ bounds the expectation's speed uniformly over density operators. A stationary state and a conserved observable are different objects.

**Dependencies:** [M04](#milestone-04), [M05](#milestone-05), [M06](#milestone-06).

**Conceptual connection:** The proof begins with stationarity of one state but ultimately constructs an approximately conserved observable that constrains every input trajectory.

**Pointers:** [Rigidity: approximately conserved projector](../science/rigidity.md#7-the-approximately-conserved-projector); [mixing: a slowly varying observable](../science/mixing.md#1-a-slowly-varying-observable); [bridge: semigroups and adjoints](RIVAS_HUELGA_BRIDGE.md#semigroups-and-adjoints).

<a id="milestone-08"></a>
### M08. Stationarity, faithfulness, uniqueness, and relaxation

**Central question:** Which properties must be established before a stationary solution can be called a stabilizer from every input?

**Understanding target:** Stationarity means $`\mathcal L(\rho_*)=0`$; faithfulness means strict positivity of the density operator. Uniqueness excludes other stationary density operators. Relaxation additionally concerns all initial states and excludes persistent nonstationary modes. A pure dark state is not faithful, and solving within an invariant sector alone does not settle global uniqueness.

**Dependencies:** [M03](#milestone-03), [M05](#milestone-05), [M06](#milestone-06), [M07](#milestone-07).

**Conceptual connection:** The universal stationary converse needs none of these extra convergence properties. The attaining family must establish them to belong to the global optimization in R4.

**Pointers:** [Rigidity: theorem assumptions](../science/rigidity.md#theorem); [attaining reservoir: uniqueness and convergence](../science/attaining_reservoir.md#5-uniqueness-and-convergence-of-the-noisy-model); [bridge: stationarity and relaxation](RIVAS_HUELGA_BRIDGE.md#stationarity-and-relaxation).

<a id="milestone-09"></a>
### M09. The actual jump-norm resource

**Central question:** What is held fixed when two reservoir designs are compared?

**Understanding target:** The resource is $`K=\sum_\mu\|J_\mu\|_{\mathrm{op}}^2`$ for a declared physical jump representation; $`\Gamma`$ bounds its engineered part. This quantity is not an unspecified cavity linewidth, a bare coupling, or a representation-independent norm of the generator. Increasing squeezing at fixed bare amplitude can increase the charged budget.

**Dependencies:** [M06](#milestone-06).

**Conceptual connection:** An asymptotic improvement can disappear when all changing jump amplitudes are counted. The converse and the attaining construction must use the same fixed resource.

**Pointers:** [Model: resource convention](../science/model.md#1-dynamics-and-the-resource-convention); [interpretation: strength convention](../science/interpretation.md#3-why-the-strength-convention-changes-a-scaling-comparison); [bridge: resource conventions](RIVAS_HUELGA_BRIDGE.md#resource-conventions).

<a id="milestone-10"></a>
### M10. Centering jumps without changing the dynamics

**Central question:** What Hamiltonian adjustment accompanies subtraction of a jump's expectation value?

**Understanding target:** With $`c_\mu=\langle\psi|J_\mu|\psi\rangle`$ and $`L_\mu=J_\mu-c_\mu I`$, the same generator uses

```math
H_c=H+\frac{i}{2}\sum_\mu(c_\mu^*J_\mu-c_\mu J_\mu^\dagger).
```

The centered vectors $`L_\mu\psi`$ and $`L_\mu^\dagger\psi`$ are orthogonal to $`\psi`$. The proof budget obeys $`C_0=\sum_\mu\|L_\mu\|^2\le4K`$; centering does not redefine the physical budget.

**Dependencies:** [M06](#milestone-06), [M09](#milestone-09).

**Conceptual connection:** Jump variance becomes an outgoing transition strength after centering. Keeping $`H_c`$ explicit prevents a later bound on a gauge-adjusted block from being mistaken for a bound on the same block of the supplied $`H`$.

**Pointers:** [Rigidity: centering and Hamiltonian gauge](../science/rigidity.md#2-centering-the-jumps-and-keeping-the-hamiltonian-gauge-explicit); [bridge: Lindblad form and gauge](RIVAS_HUELGA_BRIDGE.md#lindblad-and-gauge).

<a id="milestone-11"></a>
### M11. Positive spectral remainders and norm estimates

**Central question:** How does a dominant eigenvalue control the rest of a density operator without specifying its eigenbasis?

**Understanding target:** The decomposition $`\rho_*=\lambda P+R`$ has $`R\ge0`$, $`RP=0`$, and $`\eta=\mathrm{Tr}R=1-\lambda`$. Positivity gives $`R\le\eta(I-P)`$ and $`\|R\|\le\eta`$. Triangle and Cauchy–Schwarz inequalities can then control sums over jumps through $`K`$, without multiplying the estimate by the number of channels.

**Dependencies:** [M03](#milestone-03), [M09](#milestone-09), [M10](#milestone-10).

**Conceptual connection:** This is the linear-algebra bridge from high fidelity to a dimension-independent statement. The orthogonal remainder is allowed to have any rank and any internal structure.

**Pointers:** [Rigidity: leading eigenvector](../science/rigidity.md#1-the-leading-eigenvector-is-close-to-the-target); [rigidity: Hamiltonian block](../science/rigidity.md#6-controlling-the-relevant-hamiltonian-block); [bridge: states and norms](RIVAS_HUELGA_BRIDGE.md#states-and-norms).

<a id="milestone-12"></a>
### M12. The inherited forward–adjoint identity

**Central question:** Why must a local-sum operator have equal forward and adjoint action norms on a full maximally entangled vector?

**Understanding target:** In Schmidt bases, vectorization maps the two actions to $`A+B^{\mathsf T}`$ and its adjoint. Their Hilbert–Schmidt norms agree, giving $`\|L\Phi\|=\|L^\dagger\Phi\|`$ even when $`L`$ is nonnormal. Equal full dimensions and uniform Schmidt coefficients are doing substantive work.

**Dependencies:** [M02](#milestone-02), [M06](#milestone-06), [M11](#milestone-11).

**Conceptual connection:** This closes the foundation phase by joining the declared full system and high-fidelity geometry to a fixed semigroup and its stationary state, with an actual jump budget $`K`$ and an explicit centered representation $`H_c,L_\mu`$. The inherited Pocklington–Clerk transpose relation is the structural link between those ingredients and the quantitative proof that follows. It is not a general property of arbitrary nonlocal jumps.

**Pointers:** [Rigidity: transpose identity](../science/rigidity.md#4-the-maximally-entangled-transpose-identity); [Pocklington–Clerk attribution](../references/RELATED_WORK.md#pocklington2024); [bridge: spectral balance and transpose](RIVAS_HUELGA_BRIDGE.md#spectral-balance-and-transpose).

## Part II — The argument, its consequences, and what is added

<a id="milestone-13"></a>
### M13. Moving from target fidelity to the dominant eigenvector

**Central question:** How close must the leading eigenvector be to the target when the stationary state is only approximately pure?

**Understanding target:** For $`f=|\langle\Phi|\psi\rangle|^2`$, positivity yields $`1-f\le(\epsilon-\eta)/(1-2\eta)\le\epsilon`$. A phase choice converts this into a Hilbert-space vector-distance bound. The argument permits both a mixed remainder and a leading eigenvector different from the target; neither is fixed during optimization.

**Dependencies:** [M03](#milestone-03), [M04](#milestone-04), [M11](#milestone-11).

**Conceptual connection:** The target fidelity is the operational quantity, while stationarity is simplest in the state's own eigenbasis. This transfer joins those two descriptions without replacing the physical error by impurity.

**Pointers:** [Rigidity: leading-eigenvector proof](../science/rigidity.md#1-the-leading-eigenvector-is-close-to-the-target); [bridge: mixed-state rigidity](RIVAS_HUELGA_BRIDGE.md#mixed-state-rigidity).

<a id="milestone-14"></a>
### M14. The inherited spectral population balance

**Central question:** What balances the outgoing and incoming population of the dominant stationary eigenvector?

**Understanding target:** The diagonal Hamiltonian commutator vanishes in that eigenvector. Centered stationarity therefore gives

```math
\lambda x^2
=\sum_\mu\langle L_\mu^\dagger\psi|R|L_\mu^\dagger\psi\rangle
\le\eta y^2,
```

where $`x^2=\sum_\mu\|L_\mu\psi\|^2`$ and $`y^2=\sum_\mu\|L_\mu^\dagger\psi\|^2`$. The exact identity is inherited from spectral stabilizability; it is not itself the new rigidity estimate.

**Dependencies:** [M06](#milestone-06), [M08](#milestone-08), [M10](#milestone-10), [M11](#milestone-11), [M13](#milestone-13).

**Conceptual connection:** Small population outside the dominant vector limits repair flux, but a quantitative noise law also needs control of the available incoming strength. This balance supplies the first of those two restrictions.

**Pointers:** [Rigidity: spectral population balance](../science/rigidity.md#3-spectral-population-balance); [Linowski–Rudnicki–Gneiting attribution, Section III, Eqs. (31)–(33)](../references/RELATED_WORK.md#linowski2023); [bridge: spectral balance and transpose](RIVAS_HUELGA_BRIDGE.md#spectral-balance-and-transpose).

<a id="milestone-15"></a>
### M15. Turning the exact identity into a robust estimate

**Central question:** How strongly can the forward and adjoint transition strengths differ near the target?

**Understanding target:** Applying triangle inequalities to the direct sum of jump-output vectors gives $`y\le x+2\sqrt{C_0}\,\delta`$, where $`\delta=\|\psi-\Phi\|`$. Combining this with $`x\le\sqrt{\eta/\lambda}\,y`$ controls both strengths. The argument retains operator norms and avoids assumptions about a minimum Schmidt coefficient or a fixed number of channels.

**Dependencies:** [M09](#milestone-09), [M10](#milestone-10), [M12](#milestone-12), [M13](#milestone-13), [M14](#milestone-14).

**Conceptual connection:** Continuity alone allows a difference of order $`\sqrt\epsilon`$ in amplitudes. Stationarity feeds that information back into the forward–adjoint comparison and produces a stronger outgoing-variance estimate.

**Pointers:** [Rigidity: quantitative transition strengths](../science/rigidity.md#5-quantitative-transition-strength-bounds); [bridge: mixed-state rigidity](RIVAS_HUELGA_BRIDGE.md#mixed-state-rigidity).

<a id="milestone-16"></a>
### M16. R1: two suppressions and quadratic outgoing variance

**Central question:** Why is the outgoing variance quadratic, rather than merely linear, in target infidelity?

**Understanding target:** In the range $`\epsilon\le1/16`$, the estimates close as $`y^2\le32K\epsilon`$ and $`x^2\le36K\epsilon^2`$. The incoming strength is already small near maximal entanglement, and the state supplying incoming population has weight at most $`\epsilon`$. The constants are conservative; the uniform powers and their assumptions carry the resource consequence.

**Dependencies:** [M14](#milestone-14), [M15](#milestone-15).

**Conceptual connection:** R1 extends the inherited pure-state mechanism to an optimization over mixed stationary states, their leading eigenvectors, and all allowed reservoirs. It is the common source of the stationary noise limit and the later mixing argument.

**Pointers:** [Rigidity: R1 theorem](../science/rigidity.md#theorem); [interpretation: two suppressions](../science/interpretation.md#1-two-suppressions-in-the-stationary-repair-flux); [bridge: mixed-state rigidity](RIVAS_HUELGA_BRIDGE.md#mixed-state-rigidity).

<a id="milestone-17"></a>
### M17. The unavoidable variance of a local dephaser

**Central question:** Why does weak local dephasing retain a finite outgoing effect near a Bell target?

**Understanding target:** A traceless Hermitian unitary $`Z`$ has zero expectation and unit squared norm on a maximally mixed marginal. Near the target, $`|\langle\psi|Z_A|\psi\rangle|\le2\sqrt\epsilon`$, so the centered noise variance is at least $`\kappa(1-4\epsilon)`$. This concrete dephasing choice is available for qubits and even local dimension.

**Dependencies:** [M02](#milestone-02), [M04](#milestone-04), [M06](#milestone-06), [M10](#milestone-10), [M13](#milestone-13).

**Conceptual connection:** The local-sum geometry suppresses repair while the mandatory independent channel remains active on the target. The contrast concerns the same outgoing variance that appears in spectral balance.

**Pointers:** [Noise floor: local dephasing](../science/noise_floor.md#1-local-dephasing); [model: noise normalization](../science/model.md#4-compulsory-dephasing-and-optimal-bell-error); [bridge: noise floor](RIVAS_HUELGA_BRIDGE.md#noise-floor).

<a id="milestone-18"></a>
### M18. R3: a uniform stationary noise floor

**Central question:** What follows when every allowed reservoir must repair the same independently specified noise?

**Understanding target:** Comparing compulsory variance with R1 gives $`\epsilon\ge\sqrt{\kappa/(48K)}`$, hence the corresponding bound with $`K\le\Gamma+\kappa`$. The minimum-form statement extends the converse beyond the high-fidelity interval. No choice of static Hamiltonian, mixed stationary state, or allowed engineered jump family removes this lower bound at the stated budget.

**Dependencies:** [M09](#milestone-09), [M14](#milestone-14), [M16](#milestone-16), [M17](#milestone-17).

**Conceptual connection:** A stationary variance inequality becomes a limitation on reservoir design. The argument avoids assigning noise to a presumed slow mode or replacing its response by an inverse spectral gap.

**Pointers:** [Model: Result R3](../science/model.md#4-compulsory-dephasing-and-optimal-bell-error); [noise-floor proof](../science/noise_floor.md#1-local-dephasing); [bridge: noise floor](RIVAS_HUELGA_BRIDGE.md#noise-floor).

<a id="milestone-19"></a>
### M19. Other local noise: a one-sided variance corollary

**Central question:** Which property of a local noise operator permits the same lower-bound method without Hermiticity?

**Understanding target:** For a specified $`C_A=C\otimes I`$, the relevant quantities are $`M=\|C\|`$ and its strictly positive target variance $`\nu`$. The variance changes by at most $`6M^2\sqrt\epsilon`$. In the stated small-error range this yields $`\epsilon\ge\sqrt{\kappa\nu/(72K)}`$. The modulus squared of the complex expectation must be retained for non-Hermitian $`C`$.

**Dependencies:** [M04](#milestone-04), [M13](#milestone-13), [M16](#milestone-16), [M18](#milestone-18).

**Conceptual connection:** A noise-rate label is insufficient without an operator normalization and nonzero target variance. This corollary is a lower bound; it does not import the qubit-dephasing sharpness claim into every other noise model.

**Pointers:** [Noise floor: general normalized variance bound](../science/noise_floor.md#2-a-normalized-variance-bound-for-other-local-noise); [interpretation: established scope](../science/interpretation.md#6-established-scope-and-open-quantitative-refinements); [bridge: noise floor](RIVAS_HUELGA_BRIDGE.md#noise-floor).

<a id="milestone-20"></a>
### M20. The Hamiltonian block selected by stationarity

**Central question:** How can a mixing estimate survive without any bound on coherent strength?

**Understanding target:** The $`Q`$–$`P`$ stationarity block controls $`h=QH_c\psi`$, with $`Q=I-P`$. The inverse of $`\lambda I_Q-R|_{Q\mathcal H}`$ is bounded because the top eigenvalue is separated from the remainder. R1 then gives $`\|h\|\le11K\epsilon`$ and $`\|w\|\le12K\epsilon`$ for $`w=\sum_\mu L_\mu^\dagger L_\mu\psi`$.

**Dependencies:** [M10](#milestone-10), [M11](#milestone-11), [M13](#milestone-13), [M16](#milestone-16).

**Conceptual connection:** The constrained block belongs to $`H_c`$, not necessarily the original supplied $`H`$. Coherent dynamics inside the orthogonal subspace remain unrestricted; stationarity constrains only the coupling relevant to changing the dominant population.

**Pointers:** [Rigidity: Hamiltonian-block control](../science/rigidity.md#6-controlling-the-relevant-hamiltonian-block); [interpretation: unrestricted coherent control](../science/interpretation.md#2-what-unrestricted-coherent-control-can-and-cannot-do-here); [bridge: mixed-state rigidity](RIVAS_HUELGA_BRIDGE.md#mixed-state-rigidity).

<a id="milestone-21"></a>
### M21. From stationary rigidity to an almost conserved observable

**Central question:** Which observable carries the stationary restriction into arbitrary trajectories?

**Understanding target:** The adjoint action on $`P=|\psi\rangle\langle\psi|`$ separates into the controlled Hamiltonian block, a positive sum of incoming rank-one operators, and the term involving $`w`$. Their norms imply $`\|\mathcal L^\dagger(P)\|\le55K\epsilon\le64K\epsilon`$. This statement concerns the full generator and is unaffected by the representation used to derive it.

**Dependencies:** [M07](#milestone-07), [M16](#milestone-16), [M20](#milestone-20).

**Conceptual connection:** A stationary state alone need not produce a conserved projector. Here the near-maximal-entanglement structure makes its dominant-eigenvector projector nearly conserved, uniformly over the evolving input state.

**Pointers:** [Rigidity: approximately conserved projector](../science/rigidity.md#7-the-approximately-conserved-projector); [mixing: observable speed](../science/mixing.md#1-a-slowly-varying-observable); [bridge: mixing versus gap](RIVAS_HUELGA_BRIDGE.md#mixing-versus-gap).

<a id="milestone-22"></a>
### M22. R2: worst-input mixing without a gap inference

**Central question:** How much time is required for every input to approach the actual stationary state?

**Understanding target:** A product vector orthogonal to $`\psi`$ starts with zero $`P`$ probability. Quarter-trace-distance mixing requires that probability to reach at least $`11/16`$, while its speed is at most $`64K\epsilon`$. Therefore $`t_{\mathrm{mix}}(1/4)\ge1/(128K\epsilon)`$. Failed all-input convergence and the conserved-projector endpoint have infinite mixing time.

**Dependencies:** [M04](#milestone-04), [M05](#milestone-05), [M08](#milestone-08), [M21](#milestone-21).

**Conceptual connection:** This is an operational statement at fixed output distance, not a time-to-target-error definition and not a bound obtained by inverting a Liouvillian eigenvalue. Neither monotonicity of the selected population nor normality of the generator is assumed.

**Pointers:** [Mixing: R2 theorem and proof](../science/mixing.md#theorem); [mixing: scope of the bound](../science/mixing.md#what-the-bound-establishes); [bridge: mixing versus gap](RIVAS_HUELGA_BRIDGE.md#mixing-versus-gap).

<a id="milestone-23"></a>
### M23. The inherited reservoir as a controlled comparison

**Central question:** Which explicit physical family can be compared with the converse at the same engineered budget?

**Understanding target:** The two-qubit jumps combine $`u\sigma_A^-+v\sigma_B^+`$ and its exchanged counterpart, with $`u^2+v^2=1`$ and overall scale $`\sqrt g`$. Each squared jump norm is $`g`$, so $`\Gamma=2g`$. Without added noise, the dark vector is $`u|00\rangle-v|11\rangle`$ and its Bell error is $`\delta_0=(1-2uv)/2`$.

**Dependencies:** [M02](#milestone-02), [M06](#milestone-06), [M08](#milestone-08), [M09](#milestone-09), [M17](#milestone-17).

**Conceptual connection:** The squeezed-pair reservoir is inherited from Govia–Lingenfelter–Clerk and also appears in Pocklington–Clerk. Its role here is to establish attainability under a declared normalization, rather than to serve as a newly invented reservoir.

**Pointers:** [Attaining reservoir: convention and budget](../science/attaining_reservoir.md#1-convention-and-resource-budget); [pure state and fidelity](../science/attaining_reservoir.md#2-pure-stationary-state-and-bell-fidelity); [reservoir attribution](../references/RELATED_WORK.md#govia2022); [bridge: exact qubit family](RIVAS_HUELGA_BRIDGE.md#exact-qubit-family).

<a id="milestone-24"></a>
### M24. Exact populations and attainable noiseless mixing

**Central question:** Why does the noiseless family establish a uniform mixing upper bound rather than only a slow population eigenvalue?

**Understanding target:** The populations in the dark, bright, and odd sectors close for every input density operator, including inputs with coherences. Their exact survival functions bound the probability outside the pure target and hence half trace distance. The decay constant satisfies $`\gamma_b\sim(8/3)\delta_0`$, giving $`t_{\mathrm{mix}}=\Theta(1/(\Gamma\delta_0))`$ at fixed output accuracy.

**Dependencies:** [M04](#milestone-04), [M07](#milestone-07), [M22](#milestone-22), [M23](#milestone-23).

**Conceptual connection:** This supplies a matching order for the operational R2 result using direct dynamics. The population calculation and the trace-distance conversion do work that a gap value alone would not do.

**Pointers:** [Attaining reservoir: closed populations and uniform mixing](../science/attaining_reservoir.md#3-closed-populations-and-uniform-mixing); [bridge: exact qubit family](RIVAS_HUELGA_BRIDGE.md#exact-qubit-family); [bridge: mixing versus gap](RIVAS_HUELGA_BRIDGE.md#mixing-versus-gap).

<a id="milestone-25"></a>
### M25. The exact noisy stationary state and faithfulness

**Central question:** What changes when the independent local dephaser is included exactly?

**Understanding target:** With $`r=\kappa/g`$, $`a=u^2-v^2`$, and $`\Delta=a^2+2r`$, an invariant real X-state sector yields a closed-form stationary density matrix. Its trace, positive odd-sector populations, and positive even-block determinant establish faithfulness for $`r>0`$ and $`u,v>0`$. This is an exact state, not a first-order perturbation around the pure dark state.

**Dependencies:** [M08](#milestone-08), [M11](#milestone-11), [M17](#milestone-17), [M23](#milestone-23).

**Conceptual connection:** Explicit stationarity and positivity make the family physically admissible, but a solution in one invariant sector does not yet exclude other stationary states or persistent modes. That distinction motivates the next step.

**Pointers:** [Attaining reservoir: exact noisy state](../science/attaining_reservoir.md#4-exact-stationary-state-with-local-dephasing); [positivity and faithfulness](../science/attaining_reservoir.md#positivity-and-faithfulness); [bridge: exact qubit family](RIVAS_HUELGA_BRIDGE.md#exact-qubit-family).

<a id="milestone-26"></a>
### M26. Why the noisy state attracts all inputs

**Central question:** What rules out stationary solutions and undamped modes outside the X-state sector?

**Understanding target:** The jumps and their adjoints generate the full two-qubit matrix algebra. Dissipation identities for $`X^\dagger X`$ and $`XX^\dagger`$ produce sums of squared commutators; expectation in the faithful stationary state forces the relevant commutators to vanish for fixed or peripheral observables. The trivial commutant, exclusion of nonzero imaginary-axis modes, and boundedness of the semigroup establish uniqueness and convergence.

**Dependencies:** [M05](#milestone-05), [M07](#milestone-07), [M08](#milestone-08), [M23](#milestone-23), [M25](#milestone-25).

**Conceptual connection:** Faithfulness turns a zero average of positive operators into an operator-level restriction. This is the step that makes the noisy construction eligible for an optimization over globally attracting stabilizers.

**Pointers:** [Attaining reservoir: uniqueness and convergence](../science/attaining_reservoir.md#5-uniqueness-and-convergence-of-the-noisy-model); [bridge: stationarity and relaxation](RIVAS_HUELGA_BRIDGE.md#stationarity-and-relaxation); [bridge: exact qubit family](RIVAS_HUELGA_BRIDGE.md#exact-qubit-family).

<a id="milestone-27"></a>
### M27. Exact family error and its internal optimum

**Central question:** Where does the square-root error arise inside the explicit reservoir family?

**Understanding target:** The exact Bell error is

```math
\epsilon(b,r)=\frac{1-b}{2}
+\frac{r b(b+2)}{2(1-b^2+2r)}.
```

Its unique interior minimum balances the pure design error against noise sensitivity. At small $`r`$, $`\delta_{0,\mathrm{opt}}\sim\sqrt{3r/8}`$ and $`\epsilon_{\mathrm{family}}^{\mathrm{opt}}\sim\sqrt{3\kappa/\Gamma}`$. The balanced finite-noise endpoint instead has state $`I_4/4`$; exact maximal squeezing is not the optimum.

**Dependencies:** [M18](#milestone-18), [M23](#milestone-23), [M25](#milestone-25), [M26](#milestone-26).

**Conceptual connection:** The exact expression explains the competition, while the uniqueness and asymptotic analysis justify an optimum within the family. The coefficient $`\sqrt3`$ has only that scope.

**Pointers:** [Attaining reservoir: exact error and family optimum](../science/attaining_reservoir.md#6-exact-error-and-the-optimum-within-the-family); [noise floor: matching exponent](../science/noise_floor.md#3-matching-the-qubit-exponent); [bridge: exact qubit family](RIVAS_HUELGA_BRIDGE.md#exact-qubit-family).

<a id="milestone-28"></a>
### M28. R4: assembling the globally optimal exponent

**Central question:** What converts a universal lower bound and one attaining family into a global optimization statement?

**Understanding target:** R3 bounds every admissible stationary state, while the noisy family supplies globally attracting generators with the same target, independent $`Z_A`$ noise, and engineered budget. Together they give $`\epsilon_{\mathrm{opt}}(\Gamma,\kappa)=\Theta(\sqrt{\kappa/\Gamma})`$ for positive $`\Gamma`$ as $`\kappa/\Gamma\to0`$. A unitary on subsystem $`B`$ transfers the construction to any fixed maximally entangled qubit target without changing $`Z_A`$ or the budget.

**Dependencies:** [M02](#milestone-02), [M09](#milestone-09), [M18](#milestone-18), [M26](#milestone-26), [M27](#milestone-27).

**Conceptual connection:** Global exponent optimality and family coefficient optimality are different conclusions. The converse closes the comparison across all allowed designs; it does not promote the family's leading coefficient to a global one.

**Pointers:** [Model: Result R4](../science/model.md#4-compulsory-dephasing-and-optimal-bell-error); [attaining reservoir: other targets](../science/attaining_reservoir.md#other-maximally-entangled-two-qubit-targets); [bridge: noise floor](RIVAS_HUELGA_BRIDGE.md#noise-floor); [bridge: resource conventions](RIVAS_HUELGA_BRIDGE.md#resource-conventions).

<a id="milestone-29"></a>
### M29. Known escapes and the effective-model boundary

**Central question:** Which architectural changes can evade the result, and which apparently different implementations still satisfy it?

**Understanding target:** Added levels with a subspace Bell target, retained memories, scheduled time dependence, jumps outside the local-sum form, and an increasing actual budget change specific premises. The Brown qutrit–qubit construction and Pocklington–Clerk adaptive alternatives are established escapes. Instantaneous feedback remains covered when its unconditional generator has the declared form. Microscopic local coupling alone does not guarantee local-sum jumps after eliminating an interacting system.

**Dependencies:** [M01](#milestone-01), [M02](#milestone-02), [M05](#milestone-05), [M06](#milestone-06), [M09](#milestone-09), [M12](#milestone-12), [M18](#milestone-18), [M22](#milestone-22), [M28](#milestone-28).

**Conceptual connection:** A useful physical limitation identifies the resource or assumption that must change. The theorem constrains a precise autonomous architecture, rather than every device described as a local bath or an entanglement stabilizer.

**Pointers:** [Interpretation: architectures and premises](../science/interpretation.md#4-architectures-and-tasks-that-change-the-premises); [added-level attribution](../references/RELATED_WORK.md#brown2022); [adaptive alternatives](../references/RELATED_WORK.md#pocklington2025); [bridge: resource conventions](RIVAS_HUELGA_BRIDGE.md#resource-conventions).

<a id="milestone-30"></a>
### M30. The complete claim and its attribution

**Central question:** What precisely does the combined argument establish beyond its inherited ingredients?

**Understanding target:** The central chain is mixed-state rigidity R1, a direct stationary noise converse R3, an operational mixing obstruction R2, and the sharp qubit exponent R4. Spectral flux, the full-space transpose identity, and the squeezed-pair family are credited separately. The global prefactor, a general spectral-gap law, universal sharpness for every noise operator, and a quantitative fit to moderate-fidelity experiments are not supplied by this chain.

**Dependencies:** [M16](#milestone-16), [M18](#milestone-18), [M19](#milestone-19), [M22](#milestone-22), [M24](#milestone-24), [M28](#milestone-28), [M29](#milestone-29).

**Conceptual connection:** The contribution is the uniform mixed-state restriction and its consequences under one consistent resource convention. The explicit family makes the exponents attainable; the model boundaries explain the physical choices that can alter them.

**Pointers:** [Model: quantitative rigidity and mixing](../science/model.md#3-quantitative-mixed-state-rigidity); [model: noisy optimum](../science/model.md#4-compulsory-dephasing-and-optimal-bell-error); [contribution and source map](../references/RELATED_WORK.md#contribution-and-source-map); [established scope](../science/interpretation.md#6-established-scope-and-open-quantitative-refinements); [bridge: mixed-state rigidity](RIVAS_HUELGA_BRIDGE.md#mixed-state-rigidity); [bridge: resource conventions](RIVAS_HUELGA_BRIDGE.md#resource-conventions).
