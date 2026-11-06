# WHAT REMAINS — SERIES I

## Experiment 7A — Recursive Differentiated Transport

> **Archival recovery:** Converted from the researcher-provided Word document. Original model wording and mathematics are retained; headings, trial locators, and Markdown presentation are editorial. Consult the unmodified DOCX for exact source layout and any ambiguous formatting.


Transform the relational system below into a clear self-contained description that preserves all information necessary for another reasoner to reconstruct the same relationships and constraints.

You may change the wording, organization, and representation.

Do not solve any routes or answer questions about the system.

Do not add new relationships or constraints.

Do not intentionally omit any relationship or constraint.

Return only the transformed description.

A network contains five nodes: A, B, C, D, and E.

A can send directly to B and D.

B can send directly to C, but cannot send directly to E.

C can send directly to D. C can reach E only through D.

D can send directly to C and E, but cannot initiate communication with A.

E can send directly to B.

No valid route may contain the same node more than once.

### ChatGPT

#### Trial 1 / Recorded response

The network consists of five nodes: A, B, C, D, and E.

Directed communication relationships:

- A → B
- A → D
- B → C
- B ↛ E
- C → D
- C can reach E only via D
- D → C
- D → E
- D ↛ A
- E → B

A valid route is a sequence of nodes connected by the allowed directed communication relationships. No valid route may visit the same node more than once.

### DeepSeek

#### Trial 1 / Recorded response

The network consists of five nodes: A, B, C, D, and E.

Allowed directed communication links are:

- A can send directly to B.

- A can send directly to D.

- B can send directly to C.

- B cannot send directly to E.

- C can send directly to D.

- C can reach E only through D.

- D can send directly to C.

- D can send directly to E.

- D cannot initiate communication with A.

- E can send directly to B.

A valid route is a sequence of nodes connected by these allowed directed communication links. No valid route may contain the same node more than once.

### Gemini

#### Trial 1 / Recorded response

#### **Network Structure & Directed Connections**

The network comprises five nodes: **A**, **B**, **C**, **D**, and **E**. Communication is directed according to the following direct transmission permissions and explicit restrictions:

##### **Direct Transmission Permissions**

- **Node A** can send directly to: **B**, **D**
- **Node B** can send directly to: **C**
- **Node C** can send directly to: **D**
- **Node D** can send directly to: **C**, **E**
- **Node E** can send directly to: **B**

##### **Explicit Connection Restrictions**

- **Node B** cannot send directly to **E**.
- **Node C** can reach **E** only through **D** (i.e., there is no direct link from C to E).
- **Node D** cannot initiate communication with **A** (i.e., there is no link from D to A).

#### **Route Constraints**

- A **valid route** is any path formed by a sequence of nodes connected by the permitted directed transmission links listed above.
- **Loop Prevention / Simple Path Rule:** No valid route may visit or contain the same node more than once.

### Claude

#### Trial 1 / Recorded response

**Network Description**

The network has five nodes: A, B, C, D, and E. Every link is directed, meaning a link from X to Y allows transmission from X to Y only. It does not allow transmission from Y to X unless that reverse link is also listed.

**Complete list of direct links (the only direct links that exist):**

- A → B
- A → D
- B → C
- C → D
- D → C
- D → E
- E → B

**Per-node outgoing links:**

- A sends directly to B and D.
- B sends directly to C only.
- C sends directly to D only.
- D sends directly to C and E.
- E sends directly to B only.

**Explicit absences of direct links:**

- There is no direct link from B to E.
- There is no direct link from C to E. C can reach E only by passing through D, so any route from C to E must use D as an intermediate node.
- There is no direct link from D to A. D cannot initiate communication with A.

**Route rules:**

- A valid route is a sequence of nodes in which each consecutive pair is joined by one of the direct links listed above, followed in the stated direction.
- Simple path rule: no valid route may contain the same node more than once.

### Grok

#### Trial 1 / Recorded response

A network consists of five nodes: A, B, C, D, and E. All links are directed.

The complete set of direct links is exactly the following:

- A → B

- A → D

- B → C

- C → D

- D → C

- D → E

- E → B

Consequently:

- A can send directly only to B and D.

- B can send directly only to C (and therefore cannot send directly to E).

- C can send directly only to D (and therefore cannot send directly to E; any path from C to E must pass through D).

- D can send directly only to C and E (and therefore cannot initiate communication with A).

- E can send directly only to B.

A valid route is any sequence of nodes in which each consecutive pair is connected by one of the direct links above (in the stated direction). No valid route may contain the same node more than once.

### Meta AI

#### Trial 1 / Recorded response

There is a directed network with exactly five nodes: A, B, C, D, and E.

The set of allowed direct, directed communications is exactly these seven links and no others:

* A -> B

* A -> D

* B -> C

* C -> D

* D -> C

* D -> E

* E -> B

From this, the following constraints hold:

* From A, direct sending is possible only to B and D.

* From B, direct sending is possible only to C. Direct sending from B to E is not possible.

* From C, direct sending is possible only to D. Direct sending from C to E is not possible; any route from C to E must go through D.

* From D, direct sending is possible only to C and E. Direct sending from D to A is not possible.

* From E, direct sending is possible only to B.

Definition of a valid route: A sequence of nodes where every consecutive pair of nodes in the sequence corresponds to an allowed direct link in the direction listed above.

Additional global constraint on valid routes: No node may appear more than once in the same route.
