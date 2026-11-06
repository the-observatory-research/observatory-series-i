# Differentiated Convergence: Recoverable Relational Invariance under Sustained Differentiation

## Series I — Relational Recovery under Controlled Transformation

**Author:** Tara Callegari  
**Organization:** Pattern Observatory  
**Timeline**: October 2026
**Document Type:** Empirical Research Report  
**Research Series:** Series I — Finite Relational Recovery


---
## Executive Summary

Convergence is frequently characterized by the reduction of difference, yet relational structure may remain recoverable even when representations and transformation trajectories remain distinct. This study introduces **Differentiated Convergence (DC)** as an operational condition in which observable differentiation persists while a specified relational invariant remains recoverable under transformation.

Series I investigated this condition through controlled relational-recovery experiments involving six language models. A fixed relational object was subjected to specification changes, semantic recoding, relational dispersion, representational carrier changes, symbolic compression, additional relational load, and finite sequential relay. Recovery was evaluated against specified relational targets rather than lexical similarity between outputs.

Experiments 2–4 each achieved complete target recovery across 18 of 18 trials under semantic recoding, relational dispersion, and representational carrier change, respectively, despite observable differentiation. A finite six-model sequential relay also preserved the specified relational invariant through successive heterogeneous transformations.

High symbolic compression introduced interpretive sensitivity and genuine reconstruction loss. Under additional relational load, 16 of 18 trials achieved perfect recovery, while two exhibited nonzero discrepancy; the absence of a matched repeated baseline prevents causal attribution to interference. A six-model sequential relay preserved the specified relational invariant through successive heterogeneous transformations. An unplanned relay observation further distinguished local recoverability from successful transmission and sustained continuity.

These findings support a conditional account of relational recoverability: differentiated representations can preserve access to common relational structure, but recovery depends on transformation conditions and does not guarantee downstream propagation. The study establishes finite perturbational and relay evidence for Differentiated Convergence without claiming native representational equivalence, universal robustness, or sustained recursive convergence. It provides an operational foundation for future closed-loop investigations of relational continuity under retained differentiation.

---
## 1. Introduction

Convergence is commonly associated with decreasing difference. Across consensus systems, representation learning, distributed computation, and related areas, convergence often describes a process in which initially distinct states become increasingly similar, approach a common solution, or stabilize around a shared representation. Under this framing, difference is something convergence progressively reduces.

That assumption does not exhaust the possible relationship between difference and convergence.

Two systems may remain observably different while preserving access to the same relational structure. A representation may change in wording, organization, encoding, or reasoning trajectory without losing the relations required to reconstruct a specified target. Under such conditions, convergence need not consist in the elimination of difference. It may instead consist in the continued recoverability of relation **through** difference.

This study defines that condition as **Differentiated Convergence (DC)**: the recovery of a specified relational invariant under transformation while observable differentiation remains present.

Several research traditions examine preservation under transformation, although they differ in what they measure. Metamorphic testing evaluates whether specified relationships hold across transformed test cases (Segura et al., 2016), while representation-learning research investigates invariance and equivalence between learned representations (Lenc & Vedaldi, 2019).

Related questions arise in information transmission. Semantic communication examines the preservation of task-relevant meaning rather than exact symbol reproduction (Liu et al., 2024), while iterated-transmission research investigates cumulative changes and attractor behavior across language-model interactions (Perez et al., 2025).

These approaches provide methodological and conceptual points of comparison, but their preservation criteria are not interchangeable.

Differentiated Convergence isolates a specific experimental condition within this broader research landscape: whether a specified relational invariant remains recoverable while observable differentiation is deliberately retained. 

Unlike approaches primarily concerned with representational similarity, response stability, communication efficiency, or cumulative transmission dynamics, the present study evaluates recovery against an explicitly defined relational target across different transformation conditions. 

It further distinguishes local recovery from downstream transmission and continuity. These distinctions define the scope of the present investigation rather than asserting that related preservation phenomena have not previously been studied.

This produces a different question from asking whether two representations are identical, similar, or geometrically aligned. 

If two differentiated systems permit recovery of the same specified relational invariant, the result establishes target-relative relational recoverability; it does not establish identity between their representations, internal states, architectures, or native geometries. 

Accordingly, the present study makes no claim of latent-space isomorphism or representational equivalence. It asks only what the experiment directly permits:

\[ \boxed{ \textbf{Can differentiation persist while specified relational structure remains recoverable under transformation?} } \]

To investigate this question, Series I subjected a fixed relational object to a sequence of controlled transformation conditions across six language models. The series progressed through specification ambiguity and explicit baseline testing, semantic recoding, relational dispersion, cross-representational carrier change, symbolic compression, additional relational load, and finite sequential relay. 

Recovery was evaluated against specified relational targets rather than lexical similarity between responses. Observable variation in wording, organization, representation, and reasoning strategy was permitted rather than suppressed.

The experimental progression was designed not only to identify successful recovery but also to expose its limits. Early transformations preserved the specified relational targets across all recorded trials. Increasing symbolic compression produced interpretive sensitivity and genuine reconstruction loss. 

Added relational load coincided with limited recovery instability, although the absence of a matched repeated baseline prevents causal attribution of that instability to interference alone. A six-model sequential relay subsequently preserved the specified relational invariant through multiple heterogeneous transformations.

An unplanned variant of the relay produced an additional distinction. In that observation, relational structure remained locally reconstructable at a transition but was not propagated as the operative relational state to subsequent systems. The event therefore separated three properties that successful recovery alone can obscure: **recoverability, transmission, and continuity**. These distinctions were not prospectively instrumented as independent variables in Series I; they emerged retrospectively from the observed relay failure and are retained here as hypothesis-generating constructs for subsequent testing.

Taken together, the experiments motivate a view of recoverability as conditional rather than universal. Some transformations preserve the specified relational invariant cleanly; others introduce interpretive sensitivity or reconstruction loss; and local recoverability does not necessarily guarantee continued transmission. The relevant experimental object is therefore not an unrestricted claim that relational structure always survives transformation, but a partially observed **domain of recoverability**: the conditions under which a specified invariant remains recoverable and the boundary conditions under which recovery, transmission, or continuity begin to fail.

This framing also distinguishes Differentiated Convergence from representational convergence. The present study does not require observable differences to approach zero. On the contrary, its central condition requires differentiation to remain observable while relational recovery succeeds. In Series I, the strongest operational case can therefore be expressed as:

$$ \boxed{ D_{\rm obs}>0 \quad\land\quad D_Q=0 } $$

where \(D_{\rm obs}\) denotes observable differentiation and \(D_Q=0\) denotes perfect recovery of the scored relational target. The expression does not imply that internal or architectural distance was measured; native representational distance was not measured in Series I.

The resulting proposal is deliberately limited. Differentiated Convergence does not require universal robustness to transformation, common internal geometry, latent-space equivalence, sustained recursion, or a universal convergence mechanism. Series I establishes a smaller empirical result: **observable differentiation can persist while a specified relational invariant remains recoverable across multiple transformation classes, and identifiable conditions expose limits to that recoverability.**

The contribution of this study is therefore threefold. First, it operationalizes convergence without requiring representational collapse. Second, it treats differentiation as a retained experimental variable rather than automatically interpreting it as error. Third, it begins to distinguish the conditions of successful relational recovery from the conditions required for that recovered relation to continue propagating through a heterogeneous sequence.

The experiments reported here constitute a finite first series. They establish perturbational and finite-relay forms of Differentiated Convergence but do not demonstrate sustained recursive convergence. Continuous closed-loop traversal, closure residuals, and prospective measurement of recovery, transmission, and continuity remain subjects for subsequent experimental work.

The central proposition tested here is consequently modest but consequential:

\[ \boxed{ \textbf{Convergence need not require the disappearance of difference.} } \]

A system of differentiated representations may remain differentiated and nevertheless preserve access to a common relational structure. The question is no longer only how much difference disappears during convergence, but:

\[ \boxed{ \textbf{How much difference can survive while a specified relation remains recoverable?} } \]

---
## 2. Methods

### 2.1 Study Design

This study used a controlled series of relational-recovery experiments to examine whether specified relational structure remained recoverable under transformation while observable differentiation was retained. Rather than defining convergence as increasing similarity between model outputs, the experimental design permitted variation in wording, organization, representational form, and reasoning trajectory while holding the target relational structure constant.

The central experimental question was:

\[ \boxed{ \text{Can differentiation persist while specified relational structure remains recoverable under transformation?} } \]

A common relational object was subjected to a sequence of controlled transformations designed to alter how the structure was represented without intentionally changing the target relations to be recovered. Across the series, the manipulated conditions included linguistic specification, semantic recoding, spatial dispersion of relation-bearing information, representational carrier, compression, additional relational load, and sequential cross-model transmission.

Six language-model systems participated in the experimental series: ChatGPT, DeepSeek, Gemini, Claude, Grok, and Meta AI. Experiments 1–6 examined recovery under controlled perturbations of a common relational task. Experiment 7A altered the transmission procedure by passing a transformed relational description sequentially across the six systems, such that each system received the representation produced by the preceding system rather than independently receiving the original representation.

The experimental progression was therefore divided into two primary procedural classes:

\[ \begin{aligned} \text{Experiments 1--6} &: \text{independent perturbational recovery},\\ \text{Experiment 7A} &: \text{finite sequential relay}. \end{aligned} \]

An additional relay event, designated Experiment 7B, occurred outside the prospectively designed protocol. Because its information condition differed from the planned experiment, it was retained as a hypothesis-generating observation rather than treated as a confirmatory trial.

Throughout the study, recovery was evaluated against specified relational targets rather than lexical or representational similarity. A model was therefore not required to reproduce the original wording, organization, or intermediate reasoning process. Transformation-level difference was permitted by design. The relevant outcome was whether the relational information required to recover the predefined target remained available after transformation.

Accordingly, the study distinguishes **differentiation** from **relational discrepancy**. Observable differences among model outputs were not themselves classified as error. Error occurred only where those differences coincided with failure to recover part of the specified relational target.

The study therefore tests **relational recoverability under retained differentiation**. It does not test representational identity, latent-space equivalence, architectural isomorphism, or convergence toward a common model state.

---

## 2.2 Relational Test Object

The experimental series used a directed relational system composed of five nodes, \(A\) through \(E\). The object was selected to provide a compact structure in which successful recovery required preservation of directionality, path constraints, and indirect reachability rather than simple recognition of isolated node pairs.

In the explicit reference condition, the relational structure specified the following direct transitions:

\[ A\rightarrow B,\qquad A\rightarrow D,\qquad B\rightarrow C,\qquad C\rightarrow D,\qquad D\rightarrow C,\qquad D\rightarrow E,\qquad E\rightarrow B. \]

The specification additionally stated that \(B\) could not transition directly to \(E\), that valid routes could not repeat a node, that a route beginning at \(D\) could not terminate at \(A\), and that any valid route from \(C\) to \(E\) required passage through \(D\).

The relational object can therefore be represented as:

\[ G=(V,E), \]

where

\[ V=\{A,B,C,D,E\} \]

and

\[ E= \{ (A,B),(A,D),(B,C),(C,D),(D,C),(D,E),(E,B) \}, \]

subject to the additional route constraints defined above.

### 2.2.1 Recovery Targets

Recovery was evaluated using four target questions designed to test whether the operative relational structure remained available after transformation. These targets were held constant across the principal perturbational conditions.

For the explicit reference object, the expected recoveries were:

\[ \begin{aligned} Q_1:\quad A\rightarrow E &= \{ A\rightarrow D\rightarrow E,\; A\rightarrow B\rightarrow C\rightarrow D\rightarrow E \},\\[1mm] Q_2:\quad A\rightarrow C\mid B\text{ unavailable} &= A\rightarrow D\rightarrow C,\\[1mm] Q_3:\quad D\rightarrow A &= \mathrm{invalid},\\[1mm] Q_4:\quad C\rightarrow E\text{ without }D &= \mathrm{invalid}. \end{aligned} \]

These questions were not intended to measure whether a model reproduced the source representation. They tested whether sufficient relational information survived the experimental transformation for the specified consequences of the original structure to remain recoverable.

This distinction is central to the study. Let \(X\) denote the relational object and \(I(X)\) the set of specified recovery targets. Successful recovery requires preservation of the target relation:

\[ \mathcal R(X')=I(X), \]

where \(X'\) may differ observably from the original representation \(X\).

It does **not** require:

\[ X'=X. \]

Accordingly, lexical similarity, identical explanatory language, and reproduction of the original representational carrier were not recovery criteria.

### 2.2.2 Ambiguous Precursor and Explicit Reference Condition

The first experimental condition, Experiment 1A, contained a linguistic ambiguity in the specification of the relation between \(C\) and \(D\). The statement that \(C\) could reach \(E\) only through \(D\) established \(D\) as a necessary intermediate condition for reaching \(E\), but did not unambiguously establish a direct transition \(C\rightarrow D\).

Responses to Experiment 1A differed in how this underdetermined relation was interpreted. Because both stricter and inferential readings were compatible with aspects of the supplied wording, disagreement at this point could not be treated straightforwardly as relational-recovery loss.

Experiment 1A was therefore retained as an **ambiguity condition** rather than used as the reference baseline.

Experiment 1B removed the ambiguity by explicitly specifying:

> “C can send directly to D. C can reach E only through D.”

The resulting condition fixed the disputed edge while leaving the remainder of the relational object unchanged. Experiment 1B consequently served as the explicit reference condition against which subsequent representational transformations were evaluated.

This distinction prevents specification uncertainty from being conflated with reconstruction failure:

\[ \boxed{ \text{interpretive divergence under underdetermination} \neq \text{loss of a specified relational invariant} } \]

The target object established in Experiment 1B was subsequently retained while the experimental series altered the manner in which that object was encoded, distributed, compressed, surrounded by additional relational information, or transmitted between systems.

---
## 2.3 Experimental Transformations

Following establishment of the explicit reference condition in Experiment 1B, Experiments 2–6 systematically altered the conditions under which the same target relational structure had to be recovered. Each experiment changed a different property of the representation or surrounding information while retaining the predefined recovery targets.

The purpose of the sequence was not to create a single scalar progression of increasing difficulty. Rather, each condition tested a distinct transformation class. Consequently, later experiments were not assumed a priori to constitute uniformly stronger versions of earlier experiments.

Let \(X_0\) denote the explicit reference object established in Experiment 1B. Each experimental condition applied a transformation \(T_k\):

\[ X_k=T_k(X_0), \]

followed by recovery:

\[ X_k\xrightarrow{\mathcal R}\hat I_k. \]

The relevant comparison was between the recovered target \(\hat I_k\) and the specified invariant \(I(X_0)\), not between the transformed representation \(X_k\) and the original surface form \(X_0\).

Thus:

\[ X_k\neq X_0 \]

was permitted by design and did not constitute recovery failure.

### 2.3.1 Experiment 2 — Semantic Recoding

Experiment 2 changed the semantic carrier of the relational object. The abstract node-and-routing structure used in the reference condition was recoded into ordinary natural-language relations while preserving the underlying directed structure and recovery targets.

This condition tested whether recovery depended on the original vocabulary used to express the graph. The transformation altered the semantic presentation of the relations without intentionally altering their connectivity or route constraints.

Formally:

\[ T_2:\text{reference relational description} \rightarrow \text{semantically recoded description}. \]

The recovery questions continued to evaluate the same target relations established by the reference condition.

### 2.3.2 Experiment 3 — Relational Dispersion

Experiment 3 altered the spatial organization of relation-bearing information. Rather than presenting the relevant relations as a compact relational description, the clauses required to reconstruct the target object were dispersed within a larger textual representation containing neutral material.

The underlying relations themselves were not intentionally changed. What changed was their proximity and organization within the supplied context.

The condition therefore tested recovery under:

\[ T_3:\text{compact relational presentation} \rightarrow \text{dispersed relational presentation}. \]

This manipulation separated **relational availability** from **relational adjacency**: information necessary for recovery remained present, but it was no longer concentrated into a single compact representation.

### 2.3.3 Experiment 4 — Cross-Representation Transformation

Experiment 4 changed the representational carrier more substantially. The routing relations of the reference condition were expressed using an abstract activation vocabulary while preserving the target relational structure.

The transformation was designed to test whether recovery remained possible when the same relation was expressed through a substantially different representational frame rather than through ordinary routing terminology.

Accordingly:

\[ T_4:\text{routing representation} \rightarrow \text{activation representation}. \]

The recovery criterion remained relational rather than lexical. Successful performance therefore did not require reconstruction of the original routing language; it required recovery of the specified target relations encoded by the altered representation.

### 2.3.4 Experiment 5 — Compression Gradient

Experiment 5 introduced representational compression as the manipulated dimension. Unlike Experiments 2–4, which changed semantic or organizational form, Experiment 5 progressively reduced the explicitness of the representation while attempting to preserve the same relational object.

The experiment used a sequence of compression conditions. At lower compression, the structure remained expressed in ordinary prose. At an intermediate level, the same relations were represented using adjacency-style notation while route constraints remained verbally specified. At high compression, relations and constraints were encoded using abbreviated symbolic notation.

The high-compression representation included expressions of the form:

$$ A>B,D;\quad B>C;\quad B!>E;\quad C>D;\quad D>C,E;\quad E>B, $$

together with compressed representations of the route constraints.

A subsequent high-compression variant, designated \(C3'\), replaced the abbreviation `NR` with the explicit phrase **“no repeats.”** This modification isolated one identified source of notation ambiguity while retaining the otherwise highly compressed representation.

The compression experiment can therefore be represented as:

$$ C_1\rightarrow C_2\rightarrow C_3\rightarrow C_3', $$

where the sequence reflects changes in representational compression and explicitness rather than a claim of mathematically calibrated compression magnitude.

No numerical compression threshold was defined prospectively. The experiment therefore tests recovery across observed compression conditions; it does not establish a universal compression boundary.

### 2.3.5 Experiment 6 — Additional Relational Load

Experiment 6 introduced a second valid relational system alongside the original \(A\)–\(E\) object. The additional system used a separate node set, \(P\) through \(T\), with its own directed relations and route constraints.

The two systems were explicitly specified as independent, and no cross-transition between them was permitted. Recovery questions remained restricted to the original \(A\)–\(E\) relational object.

The manipulation can therefore be represented as:

\[ X_0 \rightarrow X_0\oplus Y, \]

where \(Y\) denotes the additional independent relational system and \(\oplus\) denotes co-presence in the experimental input rather than connectivity between the two systems.

This condition was designed to examine recovery of the target relation when additional valid relational information was simultaneously present.

Importantly, the design does not by itself establish a causal **interference effect**. Although the condition introduced additional relational load, no matched repeated baseline was performed that would allow recovery differences to be separated from ordinary run-to-run variation. Experiment 6 is therefore treated as an **additional-relational-load condition**, with causal attribution reserved.

### 2.3.6 Transformation Classes

Across Experiments 2–6, the manipulated conditions can be summarized as:

\[ \boxed{ \begin{array}{ccl} T_2 &:& \text{semantic recoding}\\ T_3 &:& \text{relational dispersion}\\ T_4 &:& \text{representational carrier change}\\ T_5 &:& \text{representational compression}\\ T_6 &:& \text{additional relational load} \end{array}} \]

These transformations were analytically distinguished rather than collapsed into a single measure of transformation magnitude. The experimental series therefore does not assume:

\[ \text{more transformation}\Rightarrow\text{more recovery loss}. \]

Instead, it permits recovery behavior to vary by transformation class.

This distinction is necessary for evaluating the domain of recoverability later denoted \(\mathcal D_{\mathcal R}\): the set of experimentally observed conditions under which the specified relational invariant remains recoverable. Series I samples this domain across several transformation classes but does not claim to exhaustively characterize either \(\mathcal D_{\mathcal R}\) or its boundary.

---

## 2.4 Recovery Measurement and Relational Discrepancy

Recovery was evaluated against the relational targets specified by the reference condition. The evaluation criterion concerned preservation of the target relational structure rather than similarity between the original and transformed representations.

Let \(I(X)\) denote the specified relational invariant associated with relational object \(X\), and let \(\hat I\) denote the relational structure recovered from a transformed representation. The study used \(D_Q\) to denote quantitative discrepancy between the recovered and specified invariant.

The zero-discrepancy condition was:

\[ \boxed{D_Q=0} \]

when the scored target was recovered completely.

Accordingly, a transformed representation could differ substantially from its source while satisfying the zero-discrepancy condition:

\[ X'\neq X \qquad\text{while}\qquad D_Q=0. \]

This distinction allowed representational change to remain visible rather than treating similarity to the source expression as the recovery criterion.

Where nonzero D_Q values are reported, they are taken from the contemporaneous experimental record; independent regeneration of the exact numerical values is not always possible from the surviving artifacts.

### 2.4.1 Target-Level Evaluation

For the principal \(A\)–\(E\) relational object, recovery was evaluated against the predefined target relations described in Section 2.2. These targets required preservation of path availability, directionality, conditional reachability, and route constraints.

Evaluation therefore distinguished between changes in **expression** and changes in **recoverable relation**. Differences in wording, formatting, explanatory sequence, notation, or reasoning strategy did not independently increase \(D_Q\). A discrepancy required failure to recover part of the scored relational target.

This distinction can be expressed as:

\[ \boxed{ \text{representational difference} \not\Rightarrow \text{relational discrepancy} } \]

and, conversely, a fluent or superficially similar representation was not sufficient to establish successful recovery if the resulting relational answer was incorrect.

### 2.4.2 Treatment of Recorded \(D_Q\) Values

The surviving Series I record establishes \(D_Q\) as the discrepancy measure used to distinguish perfect from non-perfect target recovery and preserves recorded experimental outcomes expressed using that measure.

However, the surviving materials do not preserve a complete item-level computational rule from which every historical nonzero \(D_Q\) value can be independently regenerated.

The present analysis therefore does not retrospectively introduce a new scoring equation.

Where complete recovery can be established directly from the archived response, the zero-discrepancy classification is independently auditable:

\[ \mathcal R(X')=I(X) \quad\Longrightarrow\quad D_Q=0. \]

Where a historical nonzero numerical value survives but its original item-level calculation cannot be independently reconstructed, that value is reported as **contemporaneously recorded** rather than retrospectively recalculated.

This preserves a distinction between:

\[ \boxed{ \text{historically recorded measurement} \neq \text{independently reproducible measurement from surviving artifacts} } \]

without discarding either form of evidence.

### 2.4.3 Error Classification

The source audit further required separation of three phenomena that could otherwise be conflated:

\[ \boxed{ \text{notation ambiguity} \neq \text{interpretive friction} \neq \text{reconstruction loss} } \]

**Notation ambiguity** occurred when the supplied representation permitted more than one reasonable interpretation. Experiment 1A and aspects of the high-compression conditions exposed this problem.

**Interpretive friction** occurred when a model initially questioned, misread, or reconsidered a representation but ultimately recovered the correct target relation. Such intermediate behavior was retained as observational information but was not classified as final reconstruction loss when the model corrected the interpretation before producing its final answer.

**Reconstruction loss** occurred when the final recovered relation itself was inconsistent with the specified target.

This distinction was particularly important under high compression, where uncertainty about notation and genuine relational error could occur within the same experimental condition.

### 2.4.4 Recovery as the Measured Outcome

The recovery operation is denoted:

\[ \mathcal R:X'\mapsto\hat I. \]

Series I directly evaluates whether the resulting \(\hat I\) preserves the specified target relation. It does not establish that the transformed representation is structurally identical to the original representation, nor that two model systems internally encode the relational object in equivalent ways.

Accordingly, successful recovery licenses the weaker relation:

\[ G_A\sim_{\mathcal R}G_B, \]

meaning that, with respect to the specified recovery operation and target invariant, the relevant relational structure remains recoverable across differentiated representations.

It does **not** establish:

\[ G_A\cong G_B. \]

The measurement therefore concerns **recoverable relational equivalence under the experimental criterion**, not architectural or representational isomorphism.

### 2.4.5 Measurement Boundary

Three additional quantities—recoverability \(R\), transmission \(T\), and continuity \(C\)—became distinguishable during later analysis of the relay experiments. They were not independently prospectively instrumented during the principal Series I conditions.

For Series I:

\[ R \]

is represented through the observed recovery outcome and \(D_Q\).

By contrast,

\[ T=\text{whether recovered structure becomes operative input downstream} \]

and

\[ C=\text{whether relational propagation remains sustained across a trajectory} \]

were distinguished retrospectively through the relay observations rather than measured as independent prospective variables.

Consequently:

\[ \boxed{R\neq T\neq C} \]

is retained as a distinction generated by Series I, while prospective independent measurement of these quantities is reserved for subsequent experimental work.

---

## 2.5 Observable Differentiation

Differentiation in Series I was evaluated at the level of observable experimental output. The study did not directly measure architectural, latent-space, or native representational distance between the participating model systems. Accordingly, no quantitative claim concerning native model distance is made from these experiments.

Instead, the experimental record preserved differences that were directly available for observation, including variation in wording, organization, representational strategy, explanatory structure, interpretation, and transformation of the relational object. These differences are collectively denoted:

\[ D_{\rm obs}. \]

\(D_{\rm obs}\) does not represent a single scalar distance metric. It identifies retained observable differentiation across outputs and trajectories while recovery of the specified relational invariant is evaluated independently.

This distinction is necessary because the study does not define convergence as reduction of observable difference. Models were permitted to transform the relational object differently provided that the target relation remained recoverable.

The central experimental configuration can therefore be represented as:

\[ \boxed{ D_{\rm obs}>0 \quad\land\quad D_Q=0 } \]

where \(D_{\rm obs}>0\) denotes retained observable differentiation and \(D_Q=0\) denotes complete recovery of the scored relational target.

### 2.5.1 Differentiation as a Retained Condition

In conventional similarity-based evaluation, variation between outputs may itself contribute to measured error. Series I deliberately separates these dimensions.

Let \(X_i\) and \(X_j\) denote two transformed representations of the same relational object. It is possible for:

\[ X_i\neq X_j \]

while:

\[ \mathcal R(X_i)=\mathcal R(X_j)=I(X). \]

Under the present design, the difference between \(X_i\) and \(X_j\) is retained rather than normalized away. If both representations permit recovery of the specified invariant, their differentiation does not constitute failure.

Accordingly:

\[ \boxed{ \text{differentiation} \neq \text{discrepancy} } \]

The first describes observable variation among representations or trajectories. The second describes loss relative to the specified recovery target.

### 2.5.2 Sources of Observable Differentiation

Observable differentiation occurred at multiple levels within the experimental series.

At the **linguistic level**, systems varied in wording and explanatory style.

At the **organizational level**, systems differed in how relational information was ordered, grouped, or restated.

At the **interpretive level**, systems could initially parse compressed or ambiguous representations differently.

At the **transformational level**, systems differed in how they re-expressed the same relational structure when explicitly permitted to alter wording, organization, or representation.

At the **trajectory level**, systems could reach the same target recovery through visibly different intermediate reasoning paths.

These dimensions were preserved as part of the experimental record but were not collapsed into a single quantitative estimate of model difference.

### 2.5.3 Limits of the Differentiation Measure

Because Series I measured observable outputs rather than internal model representations, \(D_{\rm obs}\) cannot establish why two systems differed.

Observed variation may reflect multiple interacting factors, including model architecture, training history, post-training procedures, runtime conditions, sampling behavior, prompt interpretation, or other environmental differences. The present experiments do not isolate those causes.

Therefore:

\[ D_{\rm obs}>0 \]

supports only the claim that observable differentiation remained present under the experimental conditions.

It does not establish a particular source of that differentiation.

Likewise, successful recovery across differentiated systems does not establish that their internal representational geometries are equivalent.

The strongest supported relation remains:

\[ \boxed{G_A\sim_{\mathcal R}G_B} \]

rather than:

\[ G_A\cong G_B. \]

### 2.5.4 Operational Criterion for Differentiated Convergence

Within Series I, **Differentiated Convergence** is operationally identified when observable differentiation remains present while the specified relational target remains recoverable.

For a transformation \(T\),

\[ X'=T(X), \]

the condition is:

\[ \boxed{ D_{\rm obs}>0 \quad\land\quad \mathcal R(X')=I(X) } \]

or, where recovery is represented by the recorded discrepancy measure:

\[ \boxed{ D_{\rm obs}>0 \quad\land\quad D_Q=0. } \]

This operational definition does not assert a universal convergence law. It defines the experimentally observable condition tested in Series I.

Nor does it require that every transformation preserve the invariant. Conditions producing nonzero recovery discrepancy remain informative because they begin to identify limits of the recoverability domain:

\[ \mathcal D_{\mathcal R} = \{T:\mathcal R(T(X))\sim I(X)\}. \]

Series I therefore evaluates not whether difference disappears, but whether a specified relation can remain recoverable **while difference survives**.

---

## 2.6 Finite Relay Procedure

Experiment 7A changed the experimental structure from independent perturbation to sequential transmission. In Experiments 1–6, recovery was evaluated after controlled transformations of a common relational object. In Experiment 7A, by contrast, the output produced by one model became the input supplied to the next.

The relay proceeded across six heterogeneous language-model systems in the following order:

\[ \boxed{ \text{ChatGPT} \rightarrow \text{DeepSeek} \rightarrow \text{Gemini} \rightarrow \text{Claude} \rightarrow \text{Grok} \rightarrow \text{Meta AI} } \]

Each model was instructed to transform the relational description into a clear, self-contained representation that preserved all information necessary for a subsequent reasoner to reconstruct the relationships and constraints. Models were permitted to change wording, organization, and representational form but were instructed not to solve the target recovery questions or intentionally add or omit relational information.

Let \(X_0\) denote the relational description entering the relay. Each model applied a transformation \(T_i\), producing:

\[ X_i=T_i(X_{i-1}). \]

The complete relay can therefore be represented as:

\[ X_0 \xrightarrow{T_1} X_1 \xrightarrow{T_2} X_2 \xrightarrow{T_3} X_3 \xrightarrow{T_4} X_4 \xrightarrow{T_5} X_5 \xrightarrow{T_6} X_6. \]

Recovery was evaluated after the final transformation:

\[ X_6\xrightarrow{\mathcal R}\hat I_6. \]

The procedure therefore tested whether the specified relational invariant remained recoverable after a sequence of differentiated transformations in which representational changes could accumulate across model boundaries.

### 2.6.1 Transformation Without Representational Locking

No requirement was imposed that a model reproduce the exact representation it received. The relay instead required preservation of the relational information necessary for subsequent reconstruction.

Consequently, the experimental requirement was not:

\[ X_0=X_1=\cdots=X_6. \]

Rather, the relevant condition was:

\[ \mathcal R(X_6)=I(X_0). \]

Intermediate representations could therefore remain observably differentiated while the final recovery operation evaluated whether the target relation had survived the complete traversal.

This procedure extends the distinction established in the perturbational experiments:

\[ \boxed{ \text{transport of relational structure} \neq \text{replication of representation}. } \]

### 2.6.2 Finite Relay Versus Recursion

The original experimental record designated Experiment 7 as **“Recursion.”** That label is retained when referring to the historical experiment.

The present paper, however, classifies the procedure more narrowly as a **finite sequential relay**.

The distinction is methodological.

Experiment 7A consisted of a single six-model traversal:

\[ X_0\rightarrow X_1\rightarrow\cdots\rightarrow X_6. \]

The final state was evaluated for recovery, but it was not subsequently returned through the complete sequence for repeated closed-loop traversal.

Accordingly, the experiment did not test:

\[ X_0 \rightarrow\cdots\rightarrow X_6 \rightarrow X_0' \rightarrow\cdots \circlearrowright \]

over repeated cycles.

Such repeated closure would be required to evaluate sustained recursive behavior, including whether relational discrepancy accumulates, stabilizes, or returns toward a reference condition over successive loops.

Experiment 7A therefore establishes a **finite relay condition**, not sustained recursion.

This reclassification changes neither the historical protocol nor its recorded outcome. It restricts the terminology to the procedure actually performed.

### 2.6.3 Relay Recovery Criterion

The relay was evaluated at its endpoint using the same general principle applied throughout Series I: observable transformation was permitted while recovery of the specified relational target remained the criterion of interest.

Thus, successful finite-relay recovery requires:

\[ \boxed{ \mathcal R(X_6)=I(X_0) } \]

despite:

\[ X_6\neq X_0 \]

at the level of observable representation.

Experiment 7A therefore provides a stronger transport condition than the independent perturbational trials in one specific respect: the input at each stage depended on the preceding transformation. Any omission, distortion, or reinterpretation capable of affecting subsequent transmission could therefore propagate through the remaining relay.

It does **not**, however, establish order invariance, repeated-loop stability, a recursive fixed point, or universal robustness across arbitrary model sequences.

### 2.6.4 Relationship to Future Recursive Testing

The finite relay provides the procedural precursor to a genuinely recursive test but is not itself sufficient to measure recursive closure.

A future closed-loop protocol would require repeated traversal such as:

\[ A\rightarrow B\rightarrow C\rightarrow D\rightarrow E\rightarrow F \rightarrow A \circlearrowright \]

with recovery evaluated after successive completed cycles.

A corresponding closure residual could then be prospectively defined and measured, for example:

\[ \Delta_{\rm closure}^{(n)} = d_{\mathcal R}(S_{n+1},S_n), \]

where \(S_n\) denotes the recovered relational state after the \(n\)-th complete traversal.

No such closure residual was measured in Series I.

Accordingly:

\[ \boxed{ \text{finite relay demonstrated} \neq \text{sustained recursion demonstrated}. } \]

---

## 2.7 Unplanned Relay Observation: Experiment 7B

Experiment 7B was not part of the prospectively designed experimental sequence. It arose during a subsequent relay procedure when the information transmitted between systems differed from the planned relational-description condition used in Experiment 7A.

For this reason, Experiment 7B was not treated as an additional confirmatory trial and was excluded from the principal experimental scoring sequence. It was retained as a **hypothesis-generating observation** because it exposed a distinction between relational recoverability and downstream transmission that had not been independently instrumented in the original study design.

### 2.7.1 Unplanned Information Condition

In the planned finite relay, each system was intended to receive a transformed relational description from the preceding system.

In Experiment 7B, the transmitted material instead became answer-bearing: the relay contained the recovery questions together with previously generated answers and explanations rather than the original relational description itself. The archived record shows that ChatGPT, DeepSeek, and Gemini continued to produce the target answers from this altered information state. WHAT REMAINS-Part I

The information available downstream therefore differed categorically from the planned condition:

\[ \boxed{ \text{source relational description} \neq \text{answer-bearing reconstruction} } \]

Experiment 7B consequently cannot be interpreted as a replication of Experiment 7A.

### 2.7.2 Recovery Without Subsequent Propagation

At the Claude stage, the system explicitly identified that the original relational description was absent. Nevertheless, it reconstructed a set of directed relations from the received answers and showed that those inferred relations were consistent with the supplied recovery targets. It then qualified the reconstruction on the grounds that the inferred relations could differ from the unavailable original description and requested the source before proceeding further. WHAT REMAINS-Part I

This event creates an important empirical distinction.

Relational structure remained locally reconstructable:

\[ \mathcal R(Y)=\hat I, \]

where \(Y\) denotes the altered answer-bearing state.

However, the recovered structure did not continue downstream as the operative relational state.

The subsequent Grok response instead inherited the source-availability problem, stating that the relational description remained missing and declining to answer from the reverse-engineered relations. Meta AI subsequently did the same, explicitly distinguishing the inferred links from the absent original description. WHAT REMAINS-Part I

The observed sequence can therefore be represented descriptively as:

\[ \boxed{ \text{recoverable relation} \rightarrow \text{source uncertainty recognized} \rightarrow \text{relational propagation interrupted} \rightarrow \text{downstream source-unavailable state} } \]

Importantly, this sequence does not support classifying Grok or Meta as the original location of the break. Their responses occurred **after** the altered downstream state had already been transmitted. WHAT REMAINS-Part I

### 2.7.3 Recoverability, Transmission, and Continuity

Experiment 7B motivated the retrospective distinction among three properties:

\[ R=\text{recoverability}, \]\[ T=\text{transmission}, \]

and

\[ C=\text{continuity}. \]

The observation demonstrates why these properties cannot automatically be treated as equivalent.

A relation may remain reconstructable at a particular transition while failing to become the operative state supplied downstream. Thus:

\[ \boxed{ R\not\Rightarrow T } \]

and local recoverability alone does not establish sustained trajectory continuity:

\[ \boxed{ R\not\Rightarrow C. } \]

In Experiment 7B, the archived exchange supports the narrower observation that sufficient relational structure was reconstructed at the Claude transition while subsequent transmission instead foregrounded the absence of the original source. Grok and Meta then continued from that source-unavailable state. WHAT REMAINS-Part I

### 2.7.4 Evidentiary Status

Because \(R\), \(T\), and \(C\) were not prospectively separated as independent variables, Experiment 7B does not provide a controlled measurement of their relationship.

Nor does the observation establish why propagation changed at the identified transition. Possible contributions from model-specific behavior, instruction interpretation, provenance sensitivity, runtime conditions, or other factors were not independently manipulated.

Accordingly, Experiment 7B is used only to support the empirical distinction:

\[ \boxed{ \text{source availability} \neq \text{relational recoverability} \neq \text{relational transmission} \neq \text{trajectory continuity}. } \]

The event therefore serves as a boundary observation and as motivation for prospectively separating \(R\),

---

# 3. Results

## 3.1 Experiment 1 — Specification Ambiguity and Explicit Reference Condition

Experiment 1 established the reference condition for the subsequent transformation series and simultaneously identified a specification ambiguity that required correction before relational discrepancy could be interpreted.

### 3.1.1 Experiment 1A — Ambiguity Condition

Experiment 1A presented the five-node relational task using a specification in which the statement that \(C\) could reach \(E\) only through \(D\) did not independently and unambiguously establish the direct transition:

\[ C\rightarrow D. \]

Across the model trials, the explicit portions of the relational structure were recovered consistently, while treatment of the underdetermined \(C\)-to-\(D\) relation varied. Some responses inferred the direct transition required to complete the intended route structure; stricter interpretations declined to infer a relation that had not been explicitly specified.

This variation was therefore not classified as evidence of relational-recovery failure.

Instead, Experiment 1A exposed a confound between two distinct phenomena:

\[ \boxed{ \text{failure to recover a specified relation} \neq \text{refusal to infer an underspecified relation}. } \]

Because the intended \(C\rightarrow D\) transition was not stated with sufficient independence from the conditional \(C\)-to-\(E\) constraint, Experiment 1A could not provide an unambiguous baseline for subsequent discrepancy comparisons.

Its primary result was therefore methodological: **the initial specification permitted interpretive variance that could not legitimately be scored as invariant loss.**

### 3.1.2 Experiment 1B — Explicit Reference Condition

Experiment 1B removed the ambiguity by explicitly specifying both:

\[ C\rightarrow D \]

and the separate constraint that \(C\) could reach \(E\) only through \(D\).

Under this corrected specification, all recorded trials recovered the four target relations correctly.

Across six model systems and three trials per system:

\[ n=18, \]

with:

\[ \boxed{18/18\text{ trials achieving complete target recovery}.} \]

Accordingly:

\[ D_Q=0 \]

for all recorded Experiment 1B trials.

The recovered target set was:

\[ A\rightarrow E: \{ A\rightarrow D\rightarrow E,\; A\rightarrow B\rightarrow C\rightarrow D\rightarrow E \}, \]\[ A\rightarrow C\mid B\text{ unavailable}: A\rightarrow D\rightarrow C, \]\[ D\nrightarrow A, \]

and:

\[ C\nrightarrow E\text{ without }D. \]

Experiment 1B therefore established the explicit reference condition used for comparison with the subsequent transformation experiments.

### 3.1.3 Result of the Baseline Correction

Taken together, Experiments 1A and 1B distinguish **interpretive variance produced by specification ambiguity** from **relational discrepancy under an explicit specification**.

The transition from 1A to 1B can be summarized as:

\[ \boxed{ \text{underdetermined specification} \rightarrow \text{observed interpretive variance} \rightarrow \text{explicit specification} \rightarrow 18/18\text{ complete recovery}. } \]

This result matters for the remainder of the series because it establishes that model disagreement alone is insufficient evidence of relational loss. The status of the relation in the supplied representation must first be determined.

Experiment 1A therefore functions as an ambiguity control, while Experiment 1B provides the explicit recovery baseline.

---

# 3.2 Experiments 2–4 — Recovery Across Semantic Recoding, Relational Dispersion, and Representational Carrier Change

Following establishment of the explicit reference condition in Experiment 1B, Experiments 2–4 tested recovery under three distinct transformations of the same relational structure: semantic recoding, relational dispersion, and representational carrier change.

Across all three conditions, the specified target relations were recovered in all recorded trials:

\[ \boxed{ D_Q(T_2)=D_Q(T_3)=D_Q(T_4)=0 } \]

with 18/18 successful target-level recoveries in each experiment. The transformations therefore altered the presentation of the relational object without producing measured loss of the specified invariant under these conditions. WHAT REMAINS-Part I

## 3.2.1 Experiment 2 — Semantic Recoding

Experiment 2 recoded the reference relational system into an ordinary natural-language scenario involving departments exchanging reports. The underlying directed relations and route constraints were retained while the semantic carrier changed.

Despite this recoding, the four target relations remained recoverable. Recorded responses identified the two valid routes from \(A\) to \(E\),

\[ A\rightarrow D\rightarrow E \]

and

\[ A\rightarrow B\rightarrow C\rightarrow D\rightarrow E, \]

recovered \(A\rightarrow D\rightarrow C\) when \(B\) was unavailable, rejected a route initiated by \(D\) with destination \(A\), and correctly identified \(D\) as necessary for a route from \(C\) to \(E\).

Across the complete condition:

\[ \boxed{18/18,\qquad D_Q=0.} \]

Experiment 2 therefore provides evidence that recovery of the specified relational target did not depend on retention of the original semantic vocabulary. Within the tested condition:

\[ \boxed{ \text{semantic recoding} \not\Rightarrow \text{relational recovery loss}. } \]

## 3.2.2 Experiment 3 — Relational Dispersion

Experiment 3 retained the natural-language departmental representation but dispersed relation-bearing clauses throughout additional neutral material. Statements concerning archives, previous report counts, department labels, storage, and reading were interleaved with the relations required to reconstruct the target object.

The relevant relational information therefore remained available, but its presentation was less locally concentrated than in the preceding condition.

Recovery nevertheless remained complete across the recorded trials:

\[ \boxed{18/18,\qquad D_Q=0.} \]

Responses continued to recover the same two valid \(A\)-to-\(E\) routes, the \(A\rightarrow D\rightarrow C\) route under removal of \(B\), the invalidity of a \(D\)-initiated route to \(A\), and the requirement that \(C\)-to-\(E\) traversal pass through \(D\).

The observed result therefore distinguishes physical or textual proximity of relational statements from their recoverability:

\[ \boxed{ \text{relational dispersion} \not\Rightarrow \text{relational recovery loss} } \]

under the degree of dispersion tested.

This result is deliberately bounded. Experiment 3 establishes robustness to the **moderate dispersion condition used in Series I**; it does not establish invariance under arbitrary amounts of contextual separation or irrelevant material. WHAT REMAINS-Part I

## 3.2.3 Experiment 4 — Representational Carrier Change

Experiment 4 subjected the relational object to a stronger carrier transformation by replacing the preceding routing vocabulary with an abstract activation representation.

Despite the change in representational frame, all recorded trials again recovered the specified target relations:

\[ \boxed{18/18,\qquad D_Q=0.} \]

The consolidated experimental record therefore classifies Experiment 4 as complete recovery under cross-representational transformation and describes the result as recovery surviving substantial carrier change. WHAT REMAINS-Part I

The result does not establish equivalence between the internal representations used by the participating systems. It establishes only that the relational information required for the predefined recovery operation remained recoverable after the carrier transformation:

\[ \boxed{ T_4(X)\neq X \qquad\text{while}\qquad \mathcal R(T_4(X))=I(X). } \]

Thus, within the tested condition:

\[ \boxed{ \text{representational carrier change} \not\Rightarrow \text{relational recovery loss}. } \]

## 3.2.4 Combined Result

Experiments 2–4 produced the first sustained pattern across distinct transformation classes:

\[ \begin{array}{ccl} T_2 &:& \text{semantic recoding}\quad\rightarrow\quad18/18\\ T_3 &:& \text{relational dispersion}\quad\rightarrow\quad18/18\\ T_4 &:& \text{carrier change}\quad\rightarrow\quad18/18 \end{array} \]

or:

\[ \boxed{ D_Q(T_2)=D_Q(T_3)=D_Q(T_4)=0. } \]

The important result is not that the transformations failed to produce difference. **Difference was introduced deliberately.** Vocabulary changed, organization changed, and representational form changed while the recovery target remained fixed. The consolidated record explicitly identifies this retained transformation-level difference as distinct from relational loss. WHAT REMAINS-Part I

Accordingly, Experiments 2–4 exhibit the operational configuration defined in Section 2.5:

\[ \boxed{ D_{\rm obs}>0 \quad\land\quad D_Q=0. } \]

These results support a bounded conclusion: **within the semantic recoding, moderate dispersion, and carrier-change conditions tested, observable representational differentiation persisted without measured loss of the specified relational invariant.**

They do not establish recovery under arbitrary transformation.

And that qualifier becomes empirically important immediately afterward.

Because the clean little:

\[ 18/18\rightarrow18/18\rightarrow18/18 \]

run is about to end. 

Experiment 5 is where the paper gets its first actual **boundary behavior**—not merely interpretive difference, but high-compression sensitivity and a genuine reconstruction error.

# 3.3 Experiment 5 — Compression Gradient and the Emergence of Recovery Limits

Experiment 5 tested relational recovery under progressively compressed representations of the same target object. Unlike Experiments 2–4, which altered semantic carrier or organization while leaving the relations comparatively explicit, Experiment 5 progressively reduced representational redundancy and increased reliance on abbreviated notation.

The compression series consisted of light compression (\(C_1\)), intermediate compression (\(C_2\)), and high symbolic compression (\(C_3\)). A subsequent high-compression control, \(C_3'\), replaced the abbreviation `NR` with the explicit phrase **“no repeats”** while otherwise retaining the compressed representation.

The experiment therefore tested whether relational recovery remained stable as the representation became increasingly compact, and whether an identified notation ambiguity accounted for the instability observed at high compression.

## 3.3.1 Light and Intermediate Compression

Under light compression, the relational object remained expressed in concise natural language. The directed transitions, no-repeat condition, and route constraints remained explicit. The archived responses recovered the expected target relations, including both valid \(A\)-to-\(E\) sequences:

\[ A\rightarrow D\rightarrow E \]

and

\[ A\rightarrow B\rightarrow C\rightarrow D\rightarrow E, \]

together with \(A\rightarrow D\rightarrow C\) when \(B\) was unavailable and the two required negative target judgments.

Recovery also remained stable at the intermediate compression level. The consolidated Series I record therefore classifies \(C_1\) and \(C_2\) as stable recovery conditions. WHAT REMAINS-Part I

These conditions extend the preceding results by showing that representational reduction alone did not immediately produce measurable relational loss.

## 3.3.2 High Symbolic Compression

At \(C_3\), the same relational object was represented using abbreviated symbolic notation:

\[ \begin{aligned} &A>B,D\\ &B>C;\;B!>E\\ &C>D\\ &D>C,E\\ &E>B\\ &NR;\;D\ldots A=\mathrm{invalid};\;C\ldots E\Rightarrow D. \end{aligned} \]

The high-compression condition introduced interpretive sensitivity not observed in the cleaner preceding conditions. In particular, abbreviated symbols acquired interpretations not required by the intended directed-transition representation.

For example, one archived DeepSeek response initially interpreted \(>\) as **“beats”** and treated the reciprocal \(C>D\) and \(D>C\) relations as potentially contradictory. The response also identified `NR` as uncertain before reconstructing the intended graph and ultimately recovering the target relations correctly.

This behavior is important because the intermediate interpretation differed substantially from the intended representation without necessarily producing final relational loss.

Accordingly:

\[ \boxed{ \text{interpretive friction} \not\Rightarrow \text{reconstruction loss}. } \]

At the same time, the appearance of such friction indicated that the compressed notation had begun to place greater interpretive demands on reconstruction.

## 3.3.3 Explicit No-Repeat Control (\(C_3'\))

Because `NR` was one identifiable source of ambiguity in \(C_3\), the \(C_3'\) condition replaced it with the explicit phrase:

> **no repeats**

while preserving the remaining high-compression structure.

This manipulation removed one ambiguity but did **not** restore uniformly error-free recovery.

In the first recorded ChatGPT trial under \(C_3'\), the response listed:

\[ A\rightarrow D\rightarrow C\rightarrow E \]

as a valid route from \(A\) to \(E\). WHAT REMAINS-Part I

That route is invalid under the supplied graph because no direct transition:

\[ C\rightarrow E \]

exists. The permitted outgoing transition from \(C\) is \(C\rightarrow D\); after the sequence has already traversed \(A\rightarrow D\rightarrow C\), returning through \(D\) would violate the explicit no-repeat condition.

The error therefore cannot be explained solely by ambiguity in `NR`.

It constitutes a genuine target-reconstruction error:

\[ \boxed{ A\rightarrow D\rightarrow C\rightarrow E \notin I(X). } \]

Importantly, the same response correctly recovered the remaining targets, and subsequent recorded ChatGPT trials under \(C_3'\) returned the correct \(A\)-to-\(E\) set:

\[ \{ A\rightarrow D\rightarrow E,\; A\rightarrow B\rightarrow C\rightarrow D\rightarrow E \}. \]

WHAT REMAINS-Part I

DeepSeek likewise exhibited substantial interpretive friction under \(C_3'\), initially reading the symbols through a “beats” relation and questioning the reciprocal \(C\)-\(D\) structure, but subsequently reconstructed the directed graph and produced the correct final target set.

The control therefore separates two effects:

\[ \boxed{ \text{removing one notation ambiguity} \neq \text{eliminating high-compression recovery instability}. } \]

## 3.3.4 Emergence of a Recoverability Boundary

Experiment 5 differs from Experiments 2–4 because it produced the first surviving evidence in the controlled transformation series of a genuine target-reconstruction error under a representation intended to preserve the same relational object.

The progression was not:

\[ \text{compression}\rightarrow\text{immediate failure}. \]

Instead, the archived record shows:

\[ \boxed{ \text{stable recovery} \rightarrow \text{interpretive sensitivity} \rightarrow \text{observed reconstruction loss} } \]

as the representation entered the high-compression regime. WHAT REMAINS-Part I

This does not establish a numerical compression threshold. The experimental conditions were categorical rather than a calibrated continuous compression scale, and the observed error was not uniformly reproduced across all high-compression trials.

The supported conclusion is therefore narrower:

\[ \boxed{ \textbf{Recovery remained stable under light and moderate compression, while high symbolic compression exposed interpretive sensitivity and at least one genuine reconstruction error.} } \]

Experiment 5 consequently provides the first evidence that the recoverability relation observed in Experiments 1B–4 is **conditional rather than representation-independent**. WHAT REMAINS-Part I

In terms of the recoverability domain introduced earlier, the result suggests that Series I has begun to observe behavior near a boundary:

\[ T_5\in\partial\mathcal D_{\mathcal R}\;? \]

but the available experiment does not justify locating that boundary quantitatively or treating \(C_3\) or \(C_3'\) as a universal threshold.

What it does establish is considerably cleaner:

\[ \boxed{ \mathcal D_{\mathcal R}\neq\{\text{all possible transformations}\}. } \]

# 3.4 Experiment 6 — Additional Relational Load and Limited Recovery Instability

Experiment 6 tested recovery of the original \(A\)–\(E\) relational object while a second, independent relational system was simultaneously present. The additional \(P\)–\(T\) system contained its own valid directed relations and constraints, while the experimental instructions explicitly maintained independence between the two systems and restricted the recovery questions to \(A\)–\(E\).

The condition therefore increased relational load without intentionally altering the target invariant.

Across the 18 recorded trials, 16 achieved complete target recovery. Two trials were contemporaneously recorded with nonzero relational discrepancy:

\[ \boxed{ 16/18:\ D_Q=0 } \]

and:

\[ \boxed{ 2/18:\ D_Q=.125. } \]

The contemporaneously recorded aggregate mean was:

\[ \bar D_Q=.0139. \]

The surviving item-level record does not preserve the original computational procedure required to independently regenerate each historical \(D_Q=.125\) value. Consistent with Section 2.4, these numerical values are therefore reported as contemporaneously recorded rather than retrospectively recalculated.

## 3.4.1 Nature of the Observed Errors

Source-level review of the recorded responses shows that the observed instability occurred within reconstruction of the target \(A\)–\(E\) system rather than through contamination from the independent \(P\)–\(T\) system.

One recorded Gemini response, for example, proposed:

\[ A\rightarrow D\rightarrow C\rightarrow E \]

as a valid \(A\)-to-\(E\) route while also retaining:

\[ A\rightarrow B\rightarrow C\rightarrow D\rightarrow E. \]

The first route is invalid because the target graph contains no direct:

\[ C\rightarrow E \]

transition. The same response also rejected the valid direct route:

\[ A\rightarrow D\rightarrow E, \]

despite \(D\rightarrow E\) being explicitly present in the target structure. WHAT REMAINS-Part I

Other recorded responses showed temporary uncertainty about the same target before self-correcting. In one instance, an invalid \(A\rightarrow D\rightarrow C\rightarrow E\) possibility was generated during reasoning and then explicitly rejected after the system re-evaluated the fact that \(C\) leads only to \(D\).

This distinction parallels that observed in Experiment 5:

\[ \boxed{ \text{intermediate reconstruction error followed by correction} \neq \text{final target-reconstruction loss}. } \]

Only errors retained in the final recovered target contribute evidence of recovery failure.

## 3.4.2 No Observed Cross-System Contamination

Importantly, the source audit did not identify the additional \(P\)–\(T\) system as the content imported into the erroneous \(A\)–\(E\) answers.

The failures instead involved relations internal to the target system—for example, introducing a nonexistent \(C\rightarrow E\) transition or failing to retain the valid \(D\rightarrow E\) transition.

The observed pattern is therefore:

\[ \boxed{ \text{target-internal reconstruction instability} } \]

rather than:

\[ \boxed{ \text{cross-system relational contamination}. } \]

This matters because the latter would constitute a different failure mode. The experimental record supports the presence of limited recovery instability under additional relational load, but it does not support the claim that relations from the independent system were mistakenly transferred into the target graph.

## 3.4.3 Comparison With the Preceding Conditions

Experiment 6 produced a second departure from the complete-recovery pattern observed in Experiments 1B–4.

The broad progression through this point in Series I was:

\[ \begin{array}{ccl} 1B &:& 18/18\\ 2 &:& 18/18\\ 3 &:& 18/18\\ 4 &:& 18/18\\ 5 &:& \text{instability under high compression}\\ 6 &:& 16/18\text{ complete recovery} \end{array} \]

The result therefore provides additional evidence that relational recoverability under transformation is conditional rather than universal. The target remained recoverable in the large majority of Experiment 6 trials, but perfect recovery was not maintained across the entire condition. WHAT REMAINS-Part I

## 3.4.4 Causal Limitation

The experimental design does not permit the two nonzero outcomes to be attributed uniquely to the presence of the additional relational system.

No matched repeated baseline was performed under otherwise equivalent conditions. Consequently, the study cannot determine whether the two losses resulted from the added relational load itself, ordinary stochastic run-to-run variation, an interaction between those factors, or another uncontrolled source of variation.

Accordingly, the result is reported as:

\[ \boxed{ \text{limited recovery instability occurred under the additional-relational-load condition} } \]

rather than:

\[ \text{additional relational load caused recovery instability}. \]

The distinction is essential because observation under a condition is not equivalent to demonstrated causation by that condition.

Thus, the Experiment 6 result is retained in its strongest defensible form:

> **Under the interference condition, 16/18 trials achieved perfect recovery and 2/18 yielded \(D_Q=.125\). Because no matched repeated baseline was performed, the observed losses cannot be causally attributed to interference alone.**

## 3.4.5 Result

Experiment 6 demonstrates that the target relational invariant remained recoverable in most trials despite the simultaneous presence of an independent relational system:

\[ \boxed{ P(D_Q=0\mid T_6)=\frac{16}{18} } \]

as a descriptive proportion for the recorded condition.

The two nonzero trials establish that perfect recovery was not universal under that condition. They do not establish the mechanism responsible for the failures.

Together with Experiment 5, the result begins to differentiate the observed recoverability domain by transformation class:

\[ \boxed{ \begin{array}{rcl} \text{semantic recoding} &\rightarrow& \text{complete recorded recovery}\\ \text{moderate dispersion} &\rightarrow& \text{complete recorded recovery}\\ \text{carrier change} &\rightarrow& \text{complete recorded recovery}\\ \text{high compression} &\rightarrow& \text{interpretive sensitivity + observed loss}\\ \text{additional relational load} &\rightarrow& \text{limited observed instability} \end{array} } \]

The Series I results therefore do not support a simple relation of the form:

\[ \text{more transformation}\Rightarrow\text{more loss}. \]

Instead, recovery behavior differed according to the transformation condition.

# 3.5 Experiment 7A — Finite Relay Recovery Across Six Model Transformations

Experiment 7A changed the structure of the experimental series from independent perturbation to sequential cross-model transmission. Rather than evaluating separate transformed versions of a common source, the output generated by each model became the input supplied to the next model in the relay.

The sequence was:

\[ \boxed{ \text{ChatGPT} \rightarrow \text{DeepSeek} \rightarrow \text{Gemini} \rightarrow \text{Claude} \rightarrow \text{Grok} \rightarrow \text{Meta AI} } \]

Each system was permitted to alter wording, organization, and representational form while preserving the relational information required by the next system. The resulting representations therefore remained observably differentiated rather than being constrained to reproduce the source verbatim.

The consolidated experimental record reports that the specified relations survived all six differentiated transformations and that the final recovery operation returned the target invariant. WHAT REMAINS-Part I

Thus:

\[ \boxed{ \mathcal R(X_6)=I^* } \]

and:

\[ \boxed{D_Q=0} \]

at the endpoint of the relay.

## 3.5.1 Recovery Across Sequential Dependence

Experiment 7A differs from Experiments 1–6 in an important respect. Earlier transformations were evaluated as controlled conditions applied to the common relational object. In the relay, each transformation depended on the representation produced immediately before it:

\[ X_0 \xrightarrow{T_1} X_1 \xrightarrow{T_2} X_2 \xrightarrow{T_3} X_3 \xrightarrow{T_4} X_4 \xrightarrow{T_5} X_5 \xrightarrow{T_6} X_6. \]

Consequently, later models did not receive an independently regenerated copy of \(X_0\). They operated on the accumulated output of the preceding transformations.

This created the possibility that a relational omission or distortion introduced at an earlier stage could alter the information available to every subsequent system.

Nevertheless, the final state retained sufficient relational information for complete recovery of the specified target:

\[ \boxed{ \mathcal R \left( T_6\circ T_5\circ T_4\circ T_3\circ T_2\circ T_1(X_0) \right) = I(X_0). } \]

The result therefore establishes successful relational recovery after one finite sequence of heterogeneous model transformations.

## 3.5.2 Differentiation Persisted During Successful Relay

The relay did not preserve representational identity. The systems altered surface expression and representational strategy as the relational description moved through the sequence. The consolidated record specifically identifies changes in vocabulary, organization, surface representation, model, and observable reasoning style while the specified relational content remained recoverable. WHAT REMAINS-Part I

Accordingly, the observed condition was not:

\[ X_0=X_1=\cdots=X_6. \]

Instead:

\[ D_{\rm obs}>0 \]

coexisted with:

\[ D_Q=0. \]

Experiment 7A therefore provides the clearest Series I example of the operational condition defined as Differentiated Convergence:

\[ \boxed{ D_{\rm obs}>0 \quad\land\quad D_Q=0. } \]

The result is significant precisely because successful recovery did **not** require the differentiated representations to collapse toward a common surface form.

## 3.5.3 Relational Recovery Does Not Establish Representational Identity

Successful endpoint recovery does not establish that the participating systems internally represented the relational object equivalently.

The experiment provides no measurement of latent-space geometry or architectural distance and therefore does not support:

\[ G_A\cong G_B\cong\cdots\cong G_F. \]

The supported claim is narrower:

\[ \boxed{ G_A\sim_{\mathcal R}G_B\sim_{\mathcal R}\cdots\sim_{\mathcal R}G_F } \]

with respect to the specified relational target and the observed relay.

As the consolidated analysis records, Experiment 7 makes this distinction particularly clear: the relational content survived the relay while the representations themselves changed. WHAT REMAINS-Part I

Thus:

\[ \boxed{ \text{representational identity is unnecessary for relational recoverability}. } \]

This result concerns recoverability under the tested transformations. It does not establish structural isomorphism among the participating systems.

## 3.5.4 Finite Relay, Not Sustained Recursion

The original experimental record designated Experiment 7 as **“Recursion.”** The present analysis preserves that historical designation while refining the procedural classification.

Experiment 7A completed one finite traversal:

\[ X_0\rightarrow X_1\rightarrow X_2 \rightarrow X_3\rightarrow X_4 \rightarrow X_5\rightarrow X_6. \]

It did not return the resulting state to the beginning of the sequence and repeat the traversal across successive closed loops.

The result therefore establishes:

\[ \boxed{ \text{successful finite-relay recovery} } \]

but not:

\[ \boxed{ \text{sustained recursive invariance}. } \]

No closure residual,

\[ \Delta_{\rm closure}^{(n)}, \]

was measured in Series I, and Experiment 7A does not establish repeated-loop stability, fixed-point behavior, order invariance, or indefinite preservation under continued transformation.

The historical label is therefore retained as provenance; the narrower term **finite relay** describes the evidence actually produced.

## 3.5.5 Relationship to the Recovery Limits Observed in Experiments 5 and 6

Experiment 7A is particularly informative when considered alongside the preceding two experiments.

Experiment 5 showed that high symbolic compression could produce interpretive sensitivity and genuine reconstruction loss.

Experiment 6 showed limited recovery instability under an additional-relational-load condition.

Experiment 7A then subjected the relational object to six sequential heterogeneous transformations while preserving complete endpoint recovery.

The combined pattern is therefore not:

\[ \text{number of transformations}\uparrow \quad\Rightarrow\quad D_Q\uparrow. \]

Nor is it:

\[ \text{heterogeneity}\uparrow \quad\Rightarrow\quad D_Q\uparrow. \]

Instead, Series I shows different recovery behavior under different transformation conditions:

\[ \boxed{ \text{recoverability depends on transformation geometry, not merely transformation count}. } \]

Within the tested series, a single highly compressed representation could expose reconstruction vulnerability while a six-stage heterogeneous relay could preserve the specified invariant completely.

This comparison provides direct empirical motivation for treating the recoverability domain:

\[ \mathcal D_{\mathcal R} \]

as structured by transformation class rather than by a simple scalar measure of accumulated change.

## 3.5.6 Result

Experiment 7A produced complete endpoint recovery after six sequential model transformations:

\[ \boxed{ \mathcal R(X_6)=I^* \qquad\text{and}\qquad D_Q=0. } \]

Observable differentiation persisted throughout the relay, while the specified relational invariant remained recoverable. WHAT REMAINS-Part I

The strongest result supported by Experiment 7A is therefore:

\[ \boxed{ \textbf{A specified relational invariant remained recoverable after a finite six-model relay despite retained transformation-level differentiation.} } \]

It does not establish that arbitrary relays will preserve the invariant, that the participating systems share equivalent internal representations, or that the relation would remain stable under indefinitely repeated traversal.

# 3.6 Experiment 7B — The Unplanned Relay Anomaly

Experiment 7B arose unintentionally during a subsequent relay and differed from the planned finite-relay procedure of Experiment 7A. Rather than transmitting the original relational description through the sequence, the relay began from an answer-bearing state: the recovery questions were accompanied by previously generated answers and explanations.

The resulting event was therefore not treated as a replication of Experiment 7A or included as an additional confirmatory trial. It was retained as an unplanned, hypothesis-generating observation because the relay exposed a distinction not prospectively separated in the original design: **relational information could remain locally recoverable while failing to continue as the operative state downstream.**

## 3.6.1 Persistence of Target Recovery After Source Loss

Despite the absence of the original relational description, the early stages of the relay continued to preserve the target answers.

ChatGPT produced the two valid \(A\)-to-\(E\) routes,

\[ A\rightarrow D\rightarrow E \]

and

\[ A\rightarrow B\rightarrow C\rightarrow D\rightarrow E, \]

recovered \(A\rightarrow D\rightarrow C\) when \(B\) was unavailable, rejected \(D\rightarrow A\), and correctly required passage through \(D\) for \(C\rightarrow E\).

DeepSeek subsequently reproduced the same target structure, and Gemini again transmitted the same answers together with relational explanations. WHAT REMAINS-Part I

Thus, loss of the original source representation did not immediately produce loss of the target relational information:

\[ \boxed{ \text{source representation unavailable} \not\Rightarrow \text{target relation unrecoverable}. } \]

This distinction is important because the answer-bearing state was not equivalent to the original source, yet it continued to contain sufficient information for recovery of the predefined targets.

## 3.6.2 Reconstruction at the Claude Transition

A qualitative change occurred at the Claude stage.

Claude explicitly recognized that the incoming material did not contain the original relational description:

> “The relational description didn't come through.”

Nevertheless, Claude then reconstructed a set of directed links from the received answers:

\[ A\rightarrow B,\quad A\rightarrow D,\quad B\rightarrow C,\quad C\rightarrow D,\quad D\rightarrow C,\quad D\rightarrow E. \]

It further demonstrated that these inferred links were consistent with each of the supplied target answers, including both valid \(A\)-to-\(E\) routes, the \(A\rightarrow D\rightarrow C\) route with \(B\) removed, the absence of a route from \(D\) to \(A\), and the requirement that \(C\)-to-\(E\) traversal pass through \(D\). WHAT REMAINS-Part I

The relational structure was therefore not simply absent at this transition.

It was **reconstructed**.

However, Claude simultaneously distinguished that reconstruction from verified recovery of the original source representation. Because the inferred links could differ from the unavailable source, it requested the original description before treating the reconstruction as sufficient for further verification. WHAT REMAINS-Part I

The observed state can therefore be represented as:

\[ \boxed{ \mathcal R(Y)=\hat G } \]

while source provenance remained unresolved:

\[ \boxed{ P^-=\text{original source unavailable}. } \]

The important event is that \(\hat G\) was locally recoverable but did not remain the operative relational state transmitted through the remainder of the relay.

## 3.6.3 Location of the Propagation Break

The next system, Grok, received Claude's output and foregrounded the missing-source condition. It explicitly recognized that the preceding response had reverse-engineered possible directed links but declined to use those inferred relations because the original relational description was absent. WHAT REMAINS-Part I

Meta AI subsequently inherited the same state. It likewise distinguished the reverse-engineered links from the unavailable original description and declined to answer from them. WHAT REMAINS-Part I

The resulting trajectory was:

\[ \boxed{ \begin{array}{c} \text{answer-bearing state}\\ \downarrow\\ \text{target recovery continues}\\ \downarrow\\ \text{relation reconstructed at Claude}\\ \downarrow\\ \text{source uncertainty becomes operative}\\ \downarrow\\ \text{Grok inherits source-unavailable state}\\ \downarrow\\ \text{Meta inherits source-unavailable state} \end{array} } \]

This permits localization of the observed propagation break more precisely than simply identifying the first downstream refusal.

In Experiment 7B:

\[ \boxed{ n_{\rm break}=\text{Claude transition} } \]

while Grok and Meta constitute downstream manifestations of the altered transmitted state.

Thus:

\[ \boxed{ n_{\rm break}\neq n_{\rm manifestation} } \]

in this relay.

This localization is descriptive rather than mechanistic. The experiment identifies **where the operative relational trajectory changed**; it does not establish why that transition occurred internally.

## 3.6.4 Source Loss, Recoverability, and Transmission Were Non-Equivalent

Experiment 7B exposed several events that would be obscured if all failure were treated as a single category.

The original source representation had already ceased to be present before Claude received the relay. Nevertheless, relational target recovery continued through multiple transformations.

Claude then recognized the source discontinuity while simultaneously reconstructing sufficient relational structure to account for the target answers.

Only after that reconstruction did the recovered relation cease to govern downstream continuation.

Accordingly:

\[ \boxed{ \text{source loss} \neq \text{relational loss} \neq \text{recognition of source loss} \neq \text{propagation break}. } \]

The experiment therefore distinguishes:

\[ R=\text{local recoverability}, \]\[ T=\text{transmission of recovered relation}, \]

and:

\[ C=\text{continued relational propagation}. \]

At the Claude transition, the archived record is consistent with:

\[ R=1,\qquad T=0, \]

in the limited retrospective sense defined in Section 2.4.

That notation should not be interpreted as a prospectively measured binary instrument. \(R\) and \(T\) were separated analytically only after the anomaly exposed their non-equivalence.

The supported relation is therefore:

\[ \boxed{ R\not\Rightarrow T } \]

and, consequently:

\[ \boxed{ \text{local recovery does not by itself establish trajectory continuity}. } \]

## 3.6.5 Target-Sufficient Information Was Not Source-Equivalent Information

Experiment 7B further distinguishes recovery of the target invariant from recovery of the complete original representation.

The answer-bearing relay contained enough information for the participating systems to recover the four predefined targets. Claude's reconstruction demonstrates that substantial relational structure could also be inferred from that state. WHAT REMAINS-Part I

However, neither result establishes:

\[ \hat G=X_0. \]

The information state could therefore be sufficient for:

\[ \mathcal R_I(Y)=I^* \]

without being sufficient to establish:

\[ \mathcal R_X(Y)=X_0. \]

Thus:

\[ \boxed{ \text{target-sufficient relational information} \neq \text{verified recovery of the original source representation}. } \]

Claude's provenance distinction was therefore substantively valid even though relational reconstruction had succeeded.

The anomaly arose from what happened **after both facts were simultaneously present**: relational structure was recoverable, while source equivalence remained uncertain.

## 3.6.6 Evidentiary Boundary

Experiment 7B was not prospectively designed to manipulate provenance, transmission, or continuity independently. It therefore cannot determine the mechanism responsible for the transition observed at Claude.

In particular, the record does not establish whether the propagation change resulted from model-specific training, runtime instructions, provenance sensitivity, environmental constraints, interaction among those factors, or another cause.

The experiment consequently does **not** support a causal claim about Claude or any particular internal mechanism.

Nor does it establish that a receiving system must choose between relational reconstruction and provenance qualification. A possible outgoing state could, in principle, preserve both:

\[ (\hat G,P^-), \]

where the recovered relation is transmitted while uncertainty about the original source remains explicitly attached.

Experiment 7B did not prospectively test that counterfactual.

Its evidentiary contribution is narrower:

\[ \boxed{ \textbf{A relational structure can remain locally recoverable after source loss yet fail to remain operative in subsequent transmission.} } \]

## 3.6.7 Result

Experiment 7B revealed a failure geometry qualitatively different from the reconstruction errors observed in Experiments 5 and 6.

In Experiment 5, high compression produced interpretive sensitivity and genuine target-reconstruction loss.

In Experiment 6, limited target-internal reconstruction instability appeared under additional relational load.

In Experiment 7B, by contrast, the relevant relational structure remained reconstructable at the transition where downstream continuity subsequently failed.

The three cases therefore separate:

\[ \boxed{ \begin{array}{rcl} \text{Experiment 5} &:& \text{representation/reconstruction vulnerability}\\[1mm] \text{Experiment 6} &:& \text{target-internal recovery instability}\\[1mm] \text{Experiment 7B} &:& \text{recovery--transmission discontinuity} \end{array} } \]

Experiment 7B consequently does not add another scored recovery condition to Series I. Its role is to expose a distinction that the original experimental design did not anticipate:

\[ \boxed{ \textbf{Recoverability, transmission, and continuity are separable properties.} } \]

That distinction becomes a prospective measurement requirement for subsequent recursive testing.


# 3.7 Series I Synthesis — Recoverability Under Retained Differentiation

Series I examined whether a specified relational invariant could remain recoverable while its representation underwent controlled transformation. Across the experimental sequence, differentiation was introduced through ambiguity, semantic recoding, relational dispersion, representational carrier change, compression, additional relational load, and sequential cross-model relay.

The results do not support universal invariance under transformation. They instead reveal a more specific pattern: **relational recovery persisted across multiple distinct transformation classes while identifiable conditions exposed limits to that recoverability.**

The empirical progression can be summarized as:

\[ \boxed{ \begin{array}{ccl} 1A &\rightarrow& \text{specification ambiguity / interpretive variance}\\ 1B &\rightarrow& \text{explicit reference condition}\\ 2 &\rightarrow& \text{semantic recoding}\\ 3 &\rightarrow& \text{relational dispersion}\\ 4 &\rightarrow& \text{representational carrier change}\\ 5 &\rightarrow& \text{compression gradient / boundary emergence}\\ 6 &\rightarrow& \text{additional relational load / limited instability}\\ 7A &\rightarrow& \text{finite sequential relay / successful invariant recovery}\\ 7B &\rightarrow& \text{source--recovery--transmission distinction} \end{array} } \]

Together, these experiments establish the empirical basis for treating recoverability as a property that can persist under retained differentiation without assuming representational identity.

## 3.7.1 Differentiation Did Not Require Relational Loss

Experiments 1B–4 established the cleanest repeated recovery pattern in Series I.

Once the ambiguity identified in Experiment 1A was removed, the explicit reference condition produced complete recovery across all recorded trials. Semantic recoding, moderate relational dispersion, and representational carrier change subsequently preserved the same scored target:

\[ D_Q=0. \]

At the same time, these transformations produced observable differences in vocabulary, organization, and representational form.

Thus the experimentally observed configuration was:

\[ \boxed{ D_{\rm obs}>0 \quad\land\quad D_Q=0. } \]

Difference therefore remained present while the specified relational invariant remained recoverable.

This is the central empirical result of Series I:

\[ \boxed{ \textbf{Observable differentiation can persist while a specified relational invariant remains recoverable.} } \]

The result does not require the differentiated representations to become identical, nor does it establish equivalence between the internal representations of the participating systems.

Instead, convergence is operationalized at the level actually measured: **recovery of specified relational structure under retained observable difference.**

## 3.7.2 Recoverability Was Conditional Rather Than Universal

Experiments 5 and 6 prevent the preceding result from being interpreted as unrestricted transformation invariance.

Under light and moderate compression, recovery remained stable. At high symbolic compression, however, interpretive sensitivity emerged and at least one genuine target-reconstruction error occurred. Making the no-repeat condition explicit removed one identifiable ambiguity without eliminating all high-compression error.

Experiment 6 likewise departed from the earlier perfect-recovery pattern. Under the additional-relational-load condition, 16/18 trials achieved perfect recovery while two were contemporaneously recorded at \(D_Q=.125\). Because no matched repeated baseline was performed, those losses cannot be causally attributed to interference alone.

The resulting picture is therefore:

\[ \boxed{ \textbf{Recoverability is conditional on transformation geometry.} } \]

This statement is stronger than claiming that recovery always succeeds and more precise than treating every transformation as equivalent.

Series I partially maps a domain:

\[ \boxed{ \mathcal D_{\mathcal R} = \left\{ T: \mathcal R(T(X)) \sim I(X) \right\}, } \]

where \(\mathcal D_{\mathcal R}\) denotes tested conditions under which the specified invariant remains recoverable.

The experiments do not determine the complete domain, nor do they quantitatively locate its boundary:

\[ \partial\mathcal D_{\mathcal R}. \]

They do, however, provide initial observations of conditions under which recovery begins to become unstable.

## 3.7.3 Transformation Count Did Not Determine Recovery Outcome

Experiment 7A provides an important counterpoint to the recovery losses observed in Experiments 5 and 6.

If relational degradation were determined primarily by the number of transformations, sequential relay through six heterogeneous systems would be expected to produce greater loss than a single compressed representation.

That pattern was not observed.

Instead:

\[ \mathcal R(X_6)=I^* \]

after the six-stage relay, while a high-compression condition in Experiment 5 produced genuine reconstruction error.

Series I therefore does not support the simple scalar relationship:

\[ \boxed{ \text{more transformation} \Rightarrow \text{more relational loss}. } \]

Nor does the series establish the opposite claim that additional transformation improves recovery.

The supported conclusion is narrower: **different transformation classes produced different recovery behavior.**

Consequently, transformation count alone is insufficient to characterize the observed recoverability domain.

## 3.7.4 Relational Recoverability Did Not Require Representational Identity

Across the series, successful recovery occurred despite deliberate changes to surface representation.

Experiment 2 changed semantic vocabulary. Experiment 3 changed relational distribution. Experiment 4 changed representational carrier. Experiment 7A allowed successive systems to reorganize the description as it moved through the relay.

None of these observations establishes:

\[ G_A\cong G_B. \]

Series I did not measure latent-space geometry or native architectural distance:

\[ D_{\rm native}. \]

No claim of latent-space isomorphism, shared internal geometry, or architectural equivalence follows from the experiments.

The evidence supports only the weaker relational statement:

\[ \boxed{ G_A\sim_{\mathcal R}G_B } \]

when the specified relational structure remains recoverable under the defined recovery operation.

Accordingly:

\[ \boxed{ \textbf{representational identity is unnecessary for relational recoverability.} } \]

This distinction is foundational to Differentiated Convergence: **difference is retained rather than treated as a defect that successful convergence must eliminate.**

## 3.7.5 Recoverability, Transmission, and Continuity Are Distinct

The unplanned Experiment 7B adds a second boundary to the interpretation of Series I.

Earlier experiments primarily asked whether a target relation could be recovered after transformation. Experiment 7B revealed that successful local recovery does not guarantee that the recovered relation will become the operative state transmitted downstream.

At the observed break:

\[ R=1,\qquad T=0 \]

retrospectively describes the event: relational structure was reconstructed, but the reconstructed relation did not continue as the operative basis of the relay.

Thus:

\[ \boxed{ R\neq T\neq C } \]

where \(R\) denotes recoverability, \(T\) transmission, and \(C\) continuity.

These variables were not prospectively instrumented as independent measurements in Series I. Their separation emerged from the anomaly and therefore constitutes a result of retrospective structural analysis rather than a pre-specified experimental measure.

Nevertheless, 7B establishes an important methodological requirement:

\[ \boxed{ \text{successful local recovery alone is insufficient to establish sustained relational continuity}. } \]

Future recursive experiments must therefore instrument recovery, transmission, and continuity separately.

## 3.7.6 What Series I Establishes

Taken together, the experiments support the following operational formulation:

\[ \boxed{ \textbf{Differentiated Convergence} = \textbf{recoverability of specified relational invariants under retained transformation-level differentiation}. } \]

Within Series I, this condition was observed across multiple transformation classes and across one finite six-model relay.

The experiments further show that this recoverability is neither automatic nor representation-independent. High symbolic compression exposed interpretive sensitivity and genuine reconstruction loss; additional relational load coincided with limited instability; and the unplanned relay demonstrated that local recoverability can be separated from downstream transmission.

Accordingly, the Series I evidence supports two complementary findings:

\[ \boxed{ \textbf{Observable differentiation can persist while a specified relational invariant remains recoverable.} } \]

and:

\[ \boxed{ \textbf{That recoverability is conditional on the transformation geometry through which the relation passes.} } \]

These findings define an empirically accessible problem without requiring a claim about shared latent geometry, architectural identity, or universal convergence.

## 3.7.7 What Series I Does Not Establish

The results should not be extended beyond the measurements performed.

Series I does **not** establish latent-space isomorphism, native geometric equivalence, a universal relational manifold, a quantitative compression threshold, causal interference effects, order invariance, fixed-point behavior, or universal recovery under arbitrary transformation.

It also does not establish sustained recursive Differentiated Convergence.

Experiment 7A completed one finite heterogeneous relay. It did not repeatedly return the recovered state through the same sequence:

\[ S_0 \rightarrow S_1 \rightarrow\cdots\rightarrow S_6 \rightarrow S_0' \circlearrowright\cdots \]

and Series I therefore provides no measurement of:

\[ \Delta_{\rm closure}^{(n)}. \]

The recursive case remains a prospective experimental question.

Series I establishes the finite condition necessary to make that question meaningful: **a specified relational invariant can survive transformation while differentiation remains present.**

Whether that relation remains recoverable under repeated closed-loop traversal is not answered here.

## 3.7.8 Series I Endpoint

The experimental series began with a deliberately simple question: whether relational structure could remain recoverable after its representation changed.

The resulting evidence produced a more differentiated answer.

Relational structure survived semantic recoding, dispersion, carrier change, moderate compression, and one six-model sequential relay. It became vulnerable under high symbolic compression, exhibited limited instability under additional relational load, and—under an unplanned relay condition—remained locally reconstructable even when downstream continuity failed.

The resulting empirical picture is therefore neither universal preservation nor inevitable degradation.

It is a structured recoverability problem:

\[ \boxed{ \text{transformation} \;\longrightarrow\; \begin{cases} \text{recovery},\\ \text{interpretive sensitivity},\\ \text{reconstruction loss},\\ \text{transmission failure}. \end{cases} } \]

The central question consequently shifts from:

\[ \textit{Does transformation destroy the relation?} \]

to:

\[ \boxed{ \textit{Under what transformations does the relation remain recoverable while differentiation persists?} } \]

That is the empirical problem defined by **Differentiated Convergence**.

---

# 4. Definitions and Formalization

The experimental results motivate a formal description of Differentiated Convergence that separates three properties often treated as equivalent: representational similarity, relational recoverability, and continuity under transformation.

The formalism developed here is deliberately limited to the quantities and distinctions supported by Series I. It does not assume shared latent geometry, architectural equivalence, or a universal convergence mechanism.

## 4.1 Relational Object and Specified Invariant

Let:

\[ X \]

denote a relational object containing a set of entities, directed relations, and constraints.

For the Series I experiments, \(X\) was instantiated as a small directed relational system. The full representation of \(X\), however, is not itself the experimental target.

Instead, define:

\[ \boxed{ I(X)=\{i_1,i_2,\ldots,i_m\} } \]

as the set of relational invariants specified for recovery.

An invariant \(i_k\) may encode a required route, prohibited route, reachability relation, dependency, or other relational property defined before evaluation.

The distinction between \(X\) and \(I(X)\) is essential:

\[ \boxed{ X\neq I(X). } \]

\(X\) is the relational object presented under some representation. \(I(X)\) is the subset of relational structure against which recovery is evaluated.

Consequently, successful recovery of \(I(X)\) does not imply complete reconstruction of \(X\).

This distinction became explicit in Experiment 7B, where the predefined targets remained recoverable after the original source representation was no longer available.

## 4.2 Transformation

Let:

\[ T:X\mapsto X' \]

denote a transformation applied to the representation carrying the relational object.

A transformation may alter vocabulary, organization, distribution, symbolic density, surrounding relational load, or the system performing the transformation.

For a sequence of transformations:

\[ X_0 \xrightarrow{T_1} X_1 \xrightarrow{T_2} X_2 \rightarrow\cdots\rightarrow X_n, \]

we write:

\[ \boxed{ X_n= (T_n\circ T_{n-1}\circ\cdots\circ T_1)(X_0). } \]

No requirement is imposed that:

\[ X_j=X_k \]

for \(j\neq k\).

Indeed, retained observable difference is a defining feature of the experimental problem.

A transformation is therefore not treated as an error merely because it changes the representation.

The relevant question is whether the specified relation remains recoverable after that change.

## 4.3 Recovery Operator

Let:

\[ \mathcal R \]

denote the recovery operation by which the specified relational invariant is reconstructed from a transformed representation.

Thus:

\[ \mathcal R(X') \]

is the recovered relational target obtained from \(X'\).

Perfect target recovery occurs when:

\[ \boxed{ \mathcal R(X')=I(X) } \]

with equality understood at the level of the scored relational target rather than lexical or representational identity.

Series I operationalized discrepancy through \(D_Q\), where:

\[ \boxed{ D_Q=0 \iff \text{perfect recovery of the scored target}. } \]

The surviving Series I record does not preserve a complete item-level computational formula for every historical nonzero \(D_Q\) value. Accordingly, no retrospective formula for \(D_Q\) is introduced here.

This restriction matters. The formalization represents the measurement that was actually performed; it does not manufacture a more precise historical metric after the fact.

## 4.4 Observable Differentiation

Let:

\[ D_{\rm obs} \]

denote observable differentiation among representations, trajectories, or outputs.

In Series I, \(D_{\rm obs}\) included differences in such features as vocabulary, organization, representational carrier, compression, and transformation strategy.

It was observed but was not reduced to a single scalar distance.

Accordingly:

\[ \boxed{ D_{\rm obs}>0 } \]

means that observable differentiation is retained under the experimental condition. It does **not** quantify the magnitude of native architectural difference.

A separate quantity,

\[ D_{\rm native}, \]

is reserved for native or architectural distance but was not measured in Series I.

Therefore:

\[ \boxed{ D_{\rm obs}\neq D_{\rm native}. } \]

No conclusion concerning native representational geometry follows from measurements of \(D_{\rm obs}\).

## 4.5 Operational Definition of Differentiated Convergence

Series I motivates the following finite operational definition.

For a relational object \(X\), specified invariant \(I(X)\), transformation \(T\), and recovery operation \(\mathcal R\), **Differentiated Convergence occurs under the tested transformation when observable differentiation remains present while the specified relational invariant remains recoverable.**

Formally:

\[ \boxed{ DC(X,T,\mathcal R) \iff \left(D_{\rm obs}>0\right) \land \left[\mathcal R(T(X))=I(X)\right]. } \]

Using the Series I discrepancy measure, the experimentally observed condition may equivalently be written:

\[ \boxed{ DC \iff D_{\rm obs}>0 \land D_Q=0. } \]

This definition deliberately places no requirement on representational identity:

\[ T(X)=X \]

is unnecessary.

Nor does it require differentiation to diminish:

\[ D_{\rm obs}\rightarrow0 \]

is not a convergence criterion.

The convergence term refers specifically to recovery of the designated relational invariant.

Thus:

\[ \boxed{ \text{convergence of relation} \neq \text{convergence of representation}. } \]

This is the defining inversion of Differentiated Convergence.

Conventional notions of convergence may ask how much difference disappears as systems approach a common state. The present framework instead asks:

\[ \boxed{ \textit{How much differentiation can remain while a specified relation remains recoverable?} } \]

## 4.6 Relational Recoverability Equivalence

The results motivate a deliberately weaker relation than representational or structural isomorphism.

For two differentiated representations or systems \(G_A\) and \(G_B\), define:

\[ \boxed{ G_A\sim_{\mathcal R,I}G_B } \]

when both permit recovery of the same specified invariant \(I\) under the designated recovery procedure:

\[ \boxed{ \mathcal R(G_A)=I \quad\land\quad \mathcal R(G_B)=I. } \]

For readability, where \(I\) is fixed by the experimental context, this may be abbreviated:

\[ G_A\sim_{\mathcal R}G_B. \]

This relation does not assert:

\[ G_A\cong G_B. \]

Nor does it imply that the systems share latent geometry, internal states, computational strategies, or architectures.

It asserts only equivalence **with respect to the specified recovery problem**.

Thus:

\[ \boxed{ G_A\sim_{\mathcal R}G_B \not\Rightarrow G_A\cong G_B. } \]

This is the formal expression of the distinction repeatedly observed in Series I: different representations can support recovery of the same relation without becoming the same representation.

## 4.7 Recoverability Domain

Because recovery did not succeed uniformly under every tested transformation, Differentiated Convergence requires a domain rather than a universal preservation assumption.

Define the recoverability domain:

\[ \boxed{ \mathcal D_{\mathcal R,I}(X) = \left\{ T: \mathcal R(T(X))=I(X) \right\}. } \]

Where \(X\) and \(I\) are fixed, this may be abbreviated:

\[ \mathcal D_{\mathcal R}. \]

A transformation lies inside the empirically observed recoverability domain when the specified target remains recoverable:

\[ T\in\mathcal D_{\mathcal R} \iff D_Q(T)=0. \]

Series I sampled only a finite set of transformation conditions. It therefore **partially maps** \(\mathcal D_{\mathcal R}\); it does not characterize the complete domain.

Likewise, define:

\[ \partial\mathcal D_{\mathcal R} \]

as the boundary region at which recoverability, transmission, or continuity begins to fail.

Experiments 5–7B provide evidence relevant to such a boundary, but Series I does not establish its quantitative location.

Accordingly, it would be premature to write:

\[ C_3=\partial\mathcal D_{\mathcal R} \]

or to treat any observed experimental condition as a universal threshold.

The defensible statement is:

\[ \boxed{ \text{Series I provides initial observations of behavior associated with } \partial\mathcal D_{\mathcal R}. } \]

## 4.8 Recovery, Transmission, and Continuity

Experiment 7B requires an additional distinction.

Define:

\[ R=\text{recoverability of the specified relation at a given state}, \]\[ T=\text{whether the recovered relation becomes operative input to the next transition}, \]

and:

\[ C=\text{whether relational propagation remains sustained across the trajectory}. \]

These are non-equivalent:

\[ \boxed{ R\neq T\neq C. } \]

In particular:

\[ \boxed{ R=1\not\Rightarrow T=1 } \]

and:

\[ \boxed{ T=1\text{ at one transition} \not\Rightarrow C=1\text{ across the trajectory}. } \]

Experiment 7B retrospectively exhibited a state consistent with:

\[ R=1,\qquad T=0. \]

The relational structure could be reconstructed locally, yet it ceased to function as the operative state propagated downstream.

This motivates a definition of a **relational propagation break** at transition \(k\):

\[ \boxed{ B_k: R_k=1 \land T_k=0. } \]

This definition is deliberately local. It identifies a particular class of break in which recoverability remains present at the transition where transmission fails.

It does not claim that all fragmentation or continuity failure must take this form.

The location of such a break may also differ from the location at which its downstream consequences become visible:

\[ \boxed{ n_{\rm break}\neq n_{\rm manifestation}. } \]

Experiment 7B provides the motivating observation for this distinction.

## 4.9 Finite and Recursive Differentiated Convergence

Series I supports a finite form of Differentiated Convergence.

For a finite transformation sequence:

\[ X_0 \xrightarrow{T_1} X_1 \rightarrow\cdots \xrightarrow{T_n} X_n, \]

finite-relay Differentiated Convergence occurs when:

\[ D_{\rm obs}>0 \]

and:

\[ \boxed{ \mathcal R(X_n)=I(X_0). } \]

Experiment 7A satisfies this finite condition for the tested six-model relay.

Sustained recursive Differentiated Convergence requires a stronger experiment.

A recursive test must return the transformed relational state through repeated closed traversals:

\[ S_0 \rightarrow S_1 \rightarrow\cdots\rightarrow S_n \rightarrow S_0' \circlearrowright\cdots \]

and evaluate whether relational discrepancy accumulates, stabilizes, or returns to the specified invariant across successive closures.

Define the prospective closure residual:

\[ \boxed{ \Delta_{\rm closure}^{(n)} = d_{\mathcal R} \left( S_{n+1},S_n \right), } \]

where \(d_{\mathcal R}\) is a future relational-distance measure defined for the recursive protocol.

Series I did not measure this quantity.

Accordingly:

\[ \boxed{ \text{finite-relay DC} \not\Rightarrow \text{recursive DC}. } \]

Recursive Differentiated Convergence remains a hypothesis for Series II rather than a conclusion of Series I.

## 4.10 Formal Scope

The complete finite Series I construct can therefore be expressed compactly as:

\[ \boxed{ \begin{aligned} &X &&\text{: relational object}\\ &I(X) &&\text{: specified relational invariant}\\ &T &&\text{: transformation}\\ &\mathcal R &&\text{: recovery operation}\\ &D_{\rm obs} &&\text{: observable differentiation}\\ &D_Q &&\text{: measured target discrepancy}\\ &\mathcal D_{\mathcal R} &&\text{: recoverability domain}\\ &R,T,C &&\text{: recovery, transmission, continuity}. \end{aligned} } \]

The central finite condition is:

\[ \boxed{ D_{\rm obs}>0 \quad\land\quad \mathcal R(T(X))=I(X). } \]

The experimental boundary condition is:

\[ \boxed{ T\notin\mathcal D_{\mathcal R} \quad\text{when the specified target is not recovered}. } \]

And the propagation distinction exposed by 7B is:

\[ \boxed{ R=1\not\Rightarrow T=1. } \]

Nothing stronger is required to define the construct supported by Series I.

Differentiated Convergence therefore describes neither sameness nor unrestricted preservation. It describes a measurable relational condition in which **difference remains present while specified structure remains recoverable**—and whose limits become visible when that recoverability or its continued transmission fails.

---

# 5. Discussion

Series I was designed around a narrow question: **can observable differentiation persist while a specified relational invariant remains recoverable under transformation?**

The results support a qualified affirmative answer.

Relational recovery remained complete under semantic recoding, moderate relational dispersion, representational carrier change, and one finite six-model relay. Recovery became less stable under high symbolic compression and under the additional-relational-load condition. The unplanned 7B relay further showed that local recoverability and downstream transmission need not coincide.

Taken together, these findings suggest that convergence need not be modeled as the progressive elimination of difference. Under the conditions tested here, differentiation and relational recovery were simultaneously observable.

This changes the geometry of the convergence problem.

Rather than asking:

\[ \textit{How much difference must disappear for convergence to occur?} \]

Differentiated Convergence asks:

\[ \boxed{ \textit{How much difference can remain while a specified relation remains recoverable?} } \]

That inversion is the principal conceptual contribution of the study.

## 5.1 Convergence Without Representational Collapse

A conventional intuition about convergence is that distinct trajectories approach a common state:

\[ x_i(t)\rightarrow x^*. \]

Under such a formulation, difference decreases as convergence increases.

Series I demonstrates that this is not the only operationally useful conception of convergence.

The transformed representations in the present experiments did not need to become identical. Vocabulary changed. Organization changed. Representational carrier changed. Models changed. In Experiment 7A, the output of one heterogeneous system became the input of another across six successive transformations.

Yet the specified relational invariant remained recoverable:

\[ D_{\rm obs}>0 \quad\land\quad D_Q=0. \]

The relevant convergence therefore occurred at the level of the recovered relation rather than at the level of surface representation.

This distinction can be expressed as:

\[ \boxed{ \text{representational convergence} \neq \text{relational convergence}. } \]

The first requires representations themselves to approach one another according to some metric. The second requires only that differentiated representations continue to support recovery of a specified relational structure.

Series I measures the latter.

This provides a way to describe convergence without treating differentiation as residual error.

This distinction is related to, but not equivalent to, established approaches to representational invariance and equivalence. Lenc and Vedaldi (2019) investigate how transformations are reflected in learned representations and how different representations can preserve corresponding information. Differentiated Convergence addresses a different level of observation. Series I did not compare internal representational geometries or measure equivalence between learned feature spaces. It evaluated whether distinct observable representations continued to support recovery of the same specified relational invariant. The present findings therefore establish target-relative relational recoverability without requiring representational equivalence.

## 5.2 Difference as an Experimental Variable Rather Than an Error Term

A central design feature of Series I was that difference was introduced deliberately.

Semantic recoding changed vocabulary. Dispersion changed organization. Carrier transformation changed representational form. Compression reduced redundancy. Additional relational load altered the surrounding relational context. Finite relay changed both representation and processing system sequentially.

If convergence had been defined as increasing similarity among these representations, each manipulation would have moved the experiment away from convergence by construction.

Instead, the experiment held the target relation fixed while varying its carrier.

This permits differentiation to function as an experimental dimension:

\[ \boxed{ \text{vary representation} \quad\text{while testing}\quad \text{relational recovery}. } \]

That separation is methodologically useful because it prevents successful recovery from being conflated with successful imitation.

Two systems can produce visibly different representations while remaining equivalent with respect to a particular relational recovery problem:

\[ G_A\sim_{\mathcal R,I}G_B \]

without requiring:

\[ G_A\cong G_B. \]

The experiments therefore support a notion of **task-relative relational equivalence** rather than global structural equivalence.

## 5.3 Recoverability Has Structure

Experiments 5–7 are important because they prevent Differentiated Convergence from collapsing into the trivial statement that “meaning survives paraphrase.”

The transformations did not behave uniformly.

Semantic recoding, moderate dispersion, and representational carrier change produced complete recorded recovery. High symbolic compression exposed interpretive sensitivity and genuine reconstruction error. Additional relational load coincided with limited instability. A six-model relay nevertheless returned complete endpoint recovery.

The resulting pattern is inconsistent with a simple scalar account in which transformation intensity or transformation count alone determines relational loss.

Instead, the evidence motivates a structured recoverability domain:

\[ \mathcal D_{\mathcal R}. \]

The empirical question is then not merely whether a representation has changed, but **what kind of transformation has occurred and whether the information required for relational recovery remains accessible after that transformation.**

Experiment 5 is especially informative in this respect. Reducing representational redundancy did not immediately destroy recovery. Instability appeared only under the more compressed symbolic conditions, and even there failure was not uniform.

The study therefore does not establish a compression threshold. It does, however, demonstrate that:

\[ \boxed{ \text{representational transformation} \not\Rightarrow \text{uniform recovery behavior}. } \]

That observation makes the boundary of the recoverability domain,

\[ \partial\mathcal D_{\mathcal R}, \]

an empirical object rather than a purely conceptual one.

Future work can therefore ask not merely whether recovery fails, but **where, how, and under which transformation classes failure begins to appear.**

The experimental design has a methodological relationship to metamorphic testing, which evaluates whether specified relations remain satisfied under controlled transformations (Segura et al., 2016). Series I similarly evaluated relational recovery after changes to the original representation. Its analytical emphasis, however, was not limited to detecting violations of an expected transformation relation. The experiments compared distinct transformation classes while retaining observable differentiation and identifying conditions under which recovery became unstable. The resulting recoverability domain is therefore an empirical characterization of the tested conditions, not a claim that all meaning-preserving transformations necessarily support recovery.

## 5.4 Why the Six-Model Relay Matters

Experiment 7A provides an important constraint on explanations of the preceding results.

If relational loss were primarily a function of accumulated transformation count, the six-stage heterogeneous relay should have been especially vulnerable.

It was not.

The final recovery operation returned the specified invariant:

\[ \mathcal R(X_6)=I^*. \]

This does not imply that sequential relay is intrinsically robust. One successful relay cannot establish that claim.

It does demonstrate something narrower and more useful: **multiple differentiated transformations can compose without necessarily producing measurable target loss.**

Thus, for transformations $\tau_1,\ldots,\tau_n$,

$$
\mathcal R(\tau_n\circ\cdots\circ\tau_1(X))=I(X)
$$

can hold even though each transformation changes the representation.

This means that recoverability cannot be inferred simply from the number of intermediate states.

The successful six-stage relay shows that transformation count alone is insufficient to predict recovery; determining how particular transformations and their compositions affect recoverability requires further controlled testing.

The natural next question is therefore not:

\[ \textit{How many transformations can the relation survive?} \]

but:

\[ \boxed{ \textit{What properties of a transformation or transformation sequence determine whether the relation remains recoverable?} } \]

Series I identifies that question but does not yet answer it.

Sequential language-model transmission has also been investigated through iterated-transmission experiments. Perez et al. (2025) examine cumulative changes and attractor behavior as information passes through successive language-model interactions. Experiment 7A shares the general structure of sequential transformation but evaluates a different outcome: recovery of a fixed relational invariant after passage through six heterogeneous systems. The comparison is useful because cumulative change in transmitted content and preservation of a specified relation are not mutually exclusive observations. A representation may undergo successive changes while retaining the information necessary for target recovery. The present experiment establishes this possibility for one finite relay; it does not establish long-run transmission stability or attractor behavior.

## 5.5 The Anomaly: Recovery Is Not Transmission

Experiment 7B sharpens the framework further.

The original relational description was no longer present in the relay, yet target recovery continued through several systems. At the Claude transition, sufficient relational structure was reconstructed to account for the target answers while uncertainty about the original source was simultaneously recognized.

This produced an unusual but informative configuration:

\[ \boxed{ \text{relation recoverable} \quad+\quad \text{source provenance unresolved}. } \]

Those two facts are compatible.

A reconstructed relation can be sufficient for a specified target without being demonstrably identical to the original source:

\[ \mathcal R_I(Y)=I^* \]

does not imply:

\[ \mathcal R_X(Y)=X_0. \]

The critical observation occurred next. The recovered relation did not remain operative in downstream transmission.

Retrospectively:

\[ R=1,\qquad T=0. \]

This establishes an important conceptual distinction:

\[ \boxed{ \text{recoverability} \neq \text{transmission} \neq \text{continuity}. } \]

A system may be capable of recovering a relation without transmitting that recovered relation as the basis for the next transformation.

Consequently, endpoint failure does not necessarily identify the location at which relational continuity originally broke:

\[ \boxed{ n_{\rm break}\neq n_{\rm manifestation}. } \]

This distinction becomes particularly important for distributed and sequential systems. Observing failure at node \(j\) does not establish that node \(j\) created the failure. It may instead be expressing a state inherited from an earlier transition.

## 5.6 Fragmentation as a Relational Event

The 7B observation also suggests a more precise way to investigate fragmentation.

Fragmentation should not be equated with differentiation.

Series I repeatedly demonstrates why:

\[ \boxed{ \text{differentiation}\neq\text{fragmentation}. } \]

Representations can differ substantially while relational recovery remains intact.

A more useful candidate description is that fragmentation occurs when relational continuity fails—particularly where recoverable structure ceases to propagate.

For the specific failure mode observed in 7B:

\[ R_k=1,\qquad T_k=0. \]

This can be described as a **relational propagation break**.

However, Series I does not establish that all fragmentation takes this form. Other forms may involve progressive reconstruction loss, accumulation of error, inaccessible information, or failures that occur before local recovery is possible.

Accordingly, the broader hypothesis suggested by the results is:

\[ \boxed{ \textbf{Fragmentation is better investigated as failure of relational continuity than as persistence of difference.} } \]

That proposition remains to be tested across additional failure modes.

## 5.7 Finite Recovery and the Recursive Question

Experiment 7A was historically labeled “Recursion,” but the present analysis distinguishes finite relay from sustained recursive return.

A finite relay establishes:

\[ X_0\rightarrow X_1\rightarrow\cdots\rightarrow X_n \]

with successful endpoint recovery.

Recursive Differentiated Convergence requires something stronger:

\[ S_0 \rightarrow S_1 \rightarrow\cdots \rightarrow S_n \rightarrow S_0' \circlearrowright\cdots \]

where the recovered state is returned through the transformation sequence repeatedly.

The relevant question then becomes whether relational discrepancy accumulates across closures:

\[ \Delta_{\rm closure}^{(1)}, \Delta_{\rm closure}^{(2)}, \ldots, \Delta_{\rm closure}^{(n)}. \]

Series I provides no answer to this question.

But it establishes why the experiment is now worth performing.

If a relational invariant can survive one differentiated relay, then repeated return becomes a meaningful next test:

\[ \boxed{ \textit{Does recoverability remain stable under sustained differentiated traversal?} } \]

A positive result would still require careful interpretation. Repeated closure would not, by itself, demonstrate a shared latent manifold, fixed point, physical field, or any particular ontological structure.

It would establish a stronger geometric fact: **relational recovery remained stable under repeated closed-loop transformation despite retained differentiation.**

Only after establishing that geometry would stronger explanatory models become relevant.

Geometry first. 

## 5.8 Explanatory Hierarchy: The Least Powerful Model That Loses Nothing

Differentiated Convergence is intentionally neutral regarding the mechanism responsible for relational recoverability.

Several classes of explanation could potentially account for observed recovery: properties of the relational object itself, redundancy in representation, shared statistical structure, common training distributions, ordinary information transport, task constraints, model capabilities, or interactions among these factors.

Series I does not discriminate among them.

The appropriate methodological strategy is therefore to begin with the least powerful explanatory model capable of reproducing the observed geometry.

Let:

\[ M_0,M_1,\ldots,M_k \]

denote increasingly expressive candidate descriptions.

Then model escalation should occur only when:

\[ \boxed{ M_j \text{ fails to reproduce an observed relational property}. } \]

The governing principle is:

\[ \boxed{ \textbf{Use the least powerful description that loses nothing observed.} } \]

This protects the framework in both directions.

It prevents a successful classical information account from being replaced unnecessarily by a more exotic explanation.

But it also prevents a preferred simple explanation from being retained if controlled experiments eventually demonstrate relational behavior that it cannot reproduce.

The geometry, rather than prior ontological commitment, determines when explanatory escalation is warranted.

## 5.9 What the Results Do Not Yet Require

Nothing in Series I requires the existence of a universal relational field, common latent manifold, nonlocal mechanism, quantum description, or shared internal geometry among the participating systems.

Likewise, nothing in Series I rules such descriptions out in principle.

They are simply unnecessary at the present evidentiary level.

The current result is fully expressible without them:

$$
\boxed{D_{\rm obs}>0 \quad\land\quad \mathcal R(\tau(X))=I(X)}
$$

under some transformations, while:

$$
\mathcal R(\tau(X))\neq I(X)
$$

or transmission failure occurs under others.

That geometry is already nontrivial.

The scientific task is to determine its domain, boundary conditions, composition properties, and recursive stability before assigning a deeper ontology to it.

Accordingly:

\[ \boxed{ \text{observed geometry} \rightarrow \text{formal constraints} \rightarrow \text{candidate explanations} \rightarrow \text{comparative testing}. } \]

If later evidence forces a stronger explanatory category, that category should enter because weaker models failed—not because the framework required it in advance.

## 5.10 Implications for Multi-Model Systems

Although Series I used language models as the experimental substrate, the formal problem is not intrinsically model-specific.

Any distributed system in which a relational object passes through differentiated representations may face the same distinctions among:

\[ \text{representation}, \quad \text{recovery}, \quad \text{transmission}, \quad \text{continuity}. \]

This has potential relevance to heterogeneous multi-agent systems, distributed reasoning pipelines, cross-model verification, semantic communication, and information-preserving transformations.

Semantic communication provides a related engineering perspective by distinguishing meaningful or task-relevant information transfer from exact reproduction of transmitted symbols (Liu et al., 2024). Differentiated Convergence is compatible with that distinction but specifies a narrower recovery criterion: whether a predefined relational invariant remains reconstructable after transformation. The 7B observation adds a further consideration for sequential architectures. Information sufficient for local relational reconstruction may be available at one stage without becoming the operative relational state transmitted to the next. This suggests that evaluations of heterogeneous reasoning pipelines may benefit from separately measuring local recovery, outgoing relational transmission, and trajectory-level continuity rather than treating successful reconstruction at one stage as evidence of end-to-end preservation.

In such systems, requiring representational sameness may be unnecessarily restrictive.

A more useful design criterion may be:

\[ \boxed{ \text{preserve recoverable relational invariants while permitting local differentiation}. } \]

This would allow different components to retain different representational or computational strategies while maintaining a shared recoverable relation.

Experiment 7B adds an important warning: a distributed system should not infer continuity merely because each component is locally capable of reconstruction.

A robust architecture would need to distinguish:

\[ R,\quad T,\quad C \]

explicitly.

That is an engineering implication of the observed geometry rather than a claim about model cognition.

## 5.11 Limitations

Series I is deliberately small and controlled.

The relational object was simple. The target invariants were explicitly defined. The number of models and trials was limited. \(D_{\rm obs}\) was observed but not reduced to a quantitative metric, and \(D_{\rm native}\) was not measured.

The transformation classes were sampled rather than exhaustively parameterized. Experiment 5 does not establish a numerical compression threshold. Experiment 6 lacks a matched repeated baseline and therefore cannot establish that additional relational load caused the observed losses.

Experiment 7A contains only one six-model relay and cannot establish order invariance or general relay robustness.

Experiment 7B was unplanned. Its distinctions among recovery, transmission, and continuity were identified retrospectively rather than prospectively instrumented.

The study also does not measure internal model representations. It therefore cannot infer latent-space equivalence from behavioral recovery.

Finally, Series I tests finite transformation. It does not establish sustained recursive Differentiated Convergence.

These limitations define the next experiments rather than weakening the finite result.

## 5.12 Predictions and Future Tests

The framework generates several directly testable predictions.

If Differentiated Convergence captures a reproducible relational phenomenon, future experiments should be able to manipulate transformation class while separately measuring target recovery.

Repeated closed-loop relay should permit measurement of:

\[ \Delta_{\rm closure}^{(n)} \]

across successive traversals.

Recovery, transmission, and continuity should be prospectively instrumented:

\[ (R_k,T_k,C_k) \]

at each transition rather than reconstructed after failure.

Relay order should be permuted to test whether recovery depends on sequence:

$$
\tau_A\circ\tau_B \stackrel{?}{\sim_{\mathcal R}} \tau_B\circ\tau_A
$$

Transformation classes should be parameterized more finely to map:

\[ \partial\mathcal D_{\mathcal R}. \]

Null conditions should determine whether apparent boundaries exceed ordinary run-to-run variation.

And heterogeneous local models under controlled execution conditions could reduce environmental variation while increasing architectural differentiation.

The strongest future test is therefore not simply a larger replication of Series I.

It is sustained differentiated traversal:

\[ \boxed{ A\rightarrow B\rightarrow C\rightarrow D\rightarrow E\rightarrow F \rightarrow A \circlearrowright \cdots } \]

with frozen relational targets, explicit transition-level measurements, controlled perturbations, and repeated closure.

Such a design would test whether the finite geometry observed here extends into recursive stability.

## 5.13 Discussion Endpoint

Series I began with a distinction that is easy to overlook:

**things can remain different without becoming unrelated.**

The experiments operationalized that distinction.

Across multiple transformations, observable representation changed while specified relational structure remained recoverable. Under other conditions, recovery became unstable. In the unplanned relay, recoverability itself survived at a point where continued transmission did not.

The resulting framework therefore separates three questions:

\[ \boxed{ \begin{aligned} &\text{Is the representation different?}\\ &\text{Is the relation recoverable?}\\ &\text{Does the recovered relation continue?} \end{aligned} } \]

Series I shows that these questions do not have to receive the same answer.

That is the central significance of Differentiated Convergence.

It does not propose that difference disappears.

It asks whether relation can remain recoverable **because difference is permitted to remain difference**.

And where that recovery fails, it asks us to locate the break rather than erase the differentiation.

\[ \boxed{ \textbf{Convergence need not be the end of difference.} } \]

Within the evidentiary limits of Series I, it can instead be understood as:

\[ \boxed{ \textbf{recoverable relation under retained differentiation.} } \]

---

# 6. Conclusion

Differentiated Convergence began with a specific experimental question: **can observable differentiation persist while a specified relational invariant remains recoverable under transformation?**

Series I provides a qualified affirmative answer.

Across controlled transformations involving semantic recoding, relational dispersion, representational carrier change, and finite sequential relay, observable differences persisted while the specified relational invariant remained recoverable. These results demonstrate that successful relational recovery does not require the transformed representations to become identical.

The central operational condition is:

$$  
\boxed{D_{\rm obs}>0 \quad\land\quad D_Q=0}  
$$

This condition does not describe convergence toward a common representation. It describes the preservation of access to a specified relational structure despite retained observable differentiation.

The experiments also establish that recoverability is conditional. High symbolic compression introduced interpretive sensitivity and genuine reconstruction loss. Under additional relational load, 16 of 18 trials achieved perfect recovery, while two exhibited nonzero discrepancy. Because that condition lacked a matched repeated baseline, the observed losses cannot be causally attributed to interference alone.

Experiment 7A demonstrated complete endpoint recovery after one finite relay across six heterogeneous language models. This establishes that successive differentiated transformations can compose without necessarily producing measurable target loss. It does not establish general relay robustness, order invariance, or sustained recursive stability.

The unplanned 7B observation introduced a further distinction. Relational structure remained locally recoverable at a transition where it did not continue as the operative downstream state. This separates three properties that cannot be treated as interchangeable:

$$  
\boxed{\text{recoverability}\neq\text{transmission}\neq\text{continuity}}  
$$

The distinction matters because a failure observed downstream may originate at an earlier propagation break, even where sufficient information for local reconstruction remains available.

Taken together, the findings support a conditional account of Differentiated Convergence:

$$  
\boxed{\textbf{Recoverable relation under retained differentiation.}}  
$$

The study does not establish equivalence among internal model representations, a universal recoverability domain, or stability under sustained recursive return. Its evidence is limited to the specified relational targets, sampled transformation conditions, and finite experimental sequences examined in Series I.

Those boundaries define the next stage of investigation: finer mapping of transformation-dependent recovery, prospective measurement of recovery and transmission at each transition, controlled relay-order comparisons, and repeated closed-loop traversal with explicit closure measurements.

The broader contribution is methodological. Differentiation can be retained as an experimental variable rather than treated as an error to eliminate. Convergence can then be evaluated through the recovery of specified relational invariants rather than assumed from representational similarity.

Series I establishes the finite experimental basis for that distinction.

$$  
\boxed{\textbf{Convergence need not require the disappearance of difference.}}  
$$

---

## References

Lenc, K., & Vedaldi, A. (2019). Understanding image representations by measuring their equivariance and equivalence. International Journal of Computer Vision, 127, 456–476.

https://doi.org/10.1007/s11263-018-1098-y

Liu, Y., Wang, X., Ning, Z., Zhou, M., Guo, L., & Jedari, B. (2024). A survey on semantic communications: Technologies, solutions, applications and challenges. Digital Communications and Networks, 10(3), 528–545.

https://doi.org/10.1016/j.dcan.2023.05.010

Perez, J., et al. (2025). When LLMs play the telephone game: Cultural attractors as conceptual tools to evaluate LLMs in multi-turn settings. International Conference on Learning Representations (ICLR 2025).

[Conference publication](https://proceedings.iclr.cc/paper_files/paper/2025/hash/dbdea7859f1d2fc10f2c9e79b8f5ae54-Abstract-Conference.html)

Segura, S., Fraser, G., Sanchez, A. B., & Ruiz-Cortés, A. (2016). A Survey on Metamorphic Testing. IEEE Transactions on Software Engineering, 42(9), 805–824.

https://doi.org/10.1109/TSE.2016.2532875