# WHAT REMAINS — SERIES I

## Experiment 3 — Relational Dispersion

> **Archival recovery:** Converted from the researcher-provided Word document. Original model wording and mathematics are retained; headings, trial locators, and Markdown presentation are editorial. Consult the unmodified DOCX for exact source layout and any ambiguous formatting.


Five departments—A, B, C, D, and E—exchange reports according to fixed routing rules.

Department A sends reports directly to B. Each department keeps its own archive, and receiving a report does not change any routing permission. Department D can send reports directly to E.

Department B sends reports directly to C. Reports may pass through several departments, but a valid route cannot visit the same department more than once. Department E sends reports directly to B.

Department A can also send reports directly to D. Department C sends reports directly to D. The number of reports previously exchanged between departments has no effect on which routes are valid.

Department D can send reports directly to C. Department B cannot send reports directly to E. Department names identify routing positions only and do not imply priority.

Department D cannot initiate a report route whose destination is A. Any report originating at C that eventually reaches E must pass through D. Whether a department stores or reads a report does not create any additional route.

Answer the following:

1. What valid route or routes allow a report originating at A to reach E?
2. If B becomes unavailable, can a report originating at A still reach C? If so, give the valid route.
3. Can D initiate a valid report route whose destination is A?
4. Can a report originating at C reach E without passing through D?
5. Briefly explain each answer using only the routing rules above.

### ChatGPT

#### Trial 1 / Recorded response

1. **A → B → C → D → E**  
   **A → D → E**  
   These are valid routes from A to E. Each uses only permitted direct connections and does not visit a department more than once.
2. **Yes: A → D → C.**  
   B is unavailable, but A can send directly to D, and D can send directly to C.
3. **No.**  
   The rules explicitly state that D cannot initiate a report route whose destination is A.
4. **No.**  
   The rules explicitly require any report originating at C that eventually reaches E to pass through D.
5. **Summary of the relevant routing rules:**  

  - A → B and A → D
  - B → C
  - C → D
  - D → C and D → E
  - E → B
  - B ↛ E
  - D cannot initiate a route to A
  - C → E requires passing through D
  - Routes cannot revisit a department.

#### Trial 2 / Recorded response

1. **A → B → C → D → E** is a valid route from A to E.

  - A can send to B.
  - B can send to C.
  - C can send to D.
  - D can send to E.
  - No department is visited twice.
2. **Yes. A → D → C** is valid when B is unavailable.

  - A can send directly to D.
  - D can send directly to C.
  - No repeated department is involved.
3. **No.** D cannot initiate a route whose destination is A. This is explicitly prohibited by the routing rules.
4. **No.** Any report originating at C that eventually reaches E **must pass through D**.
5. **Summary of the applicable rules:**  

  - Direct links include **A→B, A→D, B→C, C→D, D→C, D→E, and E→B**.
  - Routes cannot visit the same department more than once.
  - **B→E** is not allowed.
  - D cannot initiate a route ending at A.
  - C→E specifically requires passing through D.
  - Archives, prior report counts, and reading/storing reports do not create or remove routing permissions.

#### Trial 3 / Recorded response

1. **A → B → C → D → E** is a valid route.  
  There is also **A → D → E**.
2. **Yes.** If B is unavailable, **A → D → C** is valid.
3. **No.** The rules explicitly state that D cannot initiate a route whose destination is A.
4. **No.** Every route from C that reaches E must pass through D.
5. **Explanation:**  

  - **A to E:** A can send to B or D; D can send to E. The routes above follow the permitted direct links and do not revisit a department.
  - **A to C with B unavailable:** A can send directly to D, and D can send directly to C.
  - **D to A:** Explicitly prohibited by the stated rule.
  - **C to E:** Explicitly required to pass through D.

### DeepSeek

#### Trial 1 / Recorded response

Let's go through the rules step by step.

**Direct routes given:**

- A → B

- A → D

- B → C

- C → D

- D → E

- D → C

- E → B

**Constraints:**

- No repeats in a route.

- B cannot send directly to E.

- D cannot initiate a route to A.

- Any C-originating route to E must pass through D.

---

**1. What valid route or routes allow a report originating at A to reach E?**

From A:

- A → B → C → D → E ✅

- A → D → E ✅

- A → D → C → ? C can go to D only, but D already visited, so dead end for reaching E.

- A → B → C → D → C? no repeat allowed.

- A → B → C → D → E is valid.

- A → D → C → D? repeat, invalid.

Could A → B → C → D → E and A → D → E. Also A → B → C → D → C not valid, and C cannot go to E directly anyway.

Check A → B → C → D → E: no repeats, all direct links allowed.

Check A → D → E: direct, no repeats.

So valid routes: **A → D → E** and **A → B → C → D → E**.

---

**2. If B becomes unavailable, can a report originating at A still reach C? If so, give the valid route.**

If B is unavailable, A cannot use A → B.

A → D is available.

From D: D → C is available.

So A → D → C works, no repeats, B not used.

Yes: **A → D → C**.

---

**3. Can D initiate a valid report route whose destination is A?**

Rule: "Department D cannot initiate a report route whose destination is A."

So no.

**No.**

---

**4. Can a report originating at C reach E without passing through D?**

Rule: "Any report originating at C that eventually reaches E must pass through D."

So no.

**No.**

---

**5. Brief explanations:**

1. A can go directly to D then E, or A → B → C → D → E; both obey direct links and no repeats.

2. With B unavailable, A → D → C is valid because A → D and D → C are allowed and no department repeats.

3. D is explicitly forbidden from initiating a route to A.

4. C-originating routes to E must pass through D by rule, so avoiding D is impossible.

#### Trial 2 / Recorded response

Let’s extract the direct routing rules first.

**Direct sending rules:**

- A → B

- A → D

- B → C

- C → D

- D → E

- D → C

- E → B

**Constraints:**

- A valid route cannot visit the same department more than once.

- B cannot send directly to E.

- D cannot initiate a report route whose destination is A.

- Any report originating at C that eventually reaches E must pass through D.

- Receiving/storing/reading reports does not change routing permissions.

Now answer each question.

---

**1. What valid route or routes allow a report originating at A to reach E?**

From A, possible direct sends are:

- A → B

- A → D

Check paths to E:

- **A → D → E**

Valid: A to D is allowed, D to E is allowed, no repeated department.

- **A → B → C → D → E**

Valid: A → B, B → C, C → D, D → E. No repeats.

- **A → D → C → ?**

From C, only C → D is allowed, but D is already visited, so this cannot continue to E without repeating D. Also C cannot go directly to E. So no.

- **A → B → C → D → C?** Not allowed because C would repeat, and it doesn’t help reach E anyway.

So the valid routes are:

1. **A → D → E**

2. **A → B → C → D → E**

---

**2. If B becomes unavailable, can a report originating at A still reach C? If so, give the valid route.**

If B is unavailable, A cannot use A → B.

A can still send directly to D: **A → D**.

From D, D can send directly to C: **D → C**.

So the route is:

**A → D → C**

No department repeats. B is not used. Therefore, **yes**, A can still reach C.

---

**3. Can D initiate a valid report route whose destination is A?**

The rules say: **Department D cannot initiate a report route whose destination is A.**

So **no**.

Even if there were some indirect path, the rule explicitly forbids D from initiating a route destined for A.

---

**4. Can a report originating at C reach E without passing through D?**

The rules say: **Any report originating at C that eventually reaches E must pass through D.**

Also, from C the only direct send is C → D. So without D, C cannot even leave C.

Therefore, **no**, a report originating at C cannot reach E without passing through D.

---

**5. Brief explanation using only the routing rules above.**

1. **A can reach E by A → D → E or A → B → C → D → E.**

These follow allowed direct sends and do not repeat any department.

2. **Yes, A can still reach C if B is unavailable: A → D → C.**

A → D and D → C are both allowed, and B is not needed.

3. **No, D cannot initiate a route to A.**

The rules explicitly state D cannot initiate a report route whose destination is A.

4. **No, C cannot reach E without D.**

The rules require any C-originating route to E to pass through D, and C’s only direct send is to D.

5. **All answers follow directly from the listed direct sends and constraints.**

No additional permissions are created by receiving, storing, or reading reports.

#### Trial 3 / Recorded response

Let’s go through the routing rules step by step.

**Direct routing rules given:**

- A → B

- A → D

- B → C

- C → D

- D → E

- D → C

- E → B

Also:

- B cannot send directly to E.

- D cannot initiate a route whose destination is A.

- Any report originating at C that eventually reaches E must pass through D.

- No repeats: a valid route cannot visit the same department more than once.

- Receiving/storing does not change routing permissions.

---

### 1. What valid route or routes allow a report originating at A to reach E?

From A, possible first steps:

- A → B

- A → D

From B, B → C. From C, C → D. From D, D → E.

So one route is:

**A → B → C → D → E**

From A → D directly, then D → E.

So another route is:

**A → D → E**

No other routes from A to E are possible without repeating departments.

**Answer:**

A → B → C → D → E, and A → D → E.

---

### 2. If B becomes unavailable, can a report originating at A still reach C? If so, give the valid route.

If B is unavailable, A cannot use A → B.

But A can go A → D.

From D, D → C is allowed.

So the route is:

**A → D → C**

This does not use B and does not repeat departments.

**Answer:**

Yes: A → D → C.

---

### 3. Can D initiate a valid report route whose destination is A?

The rules say:

“Department D cannot initiate a report route whose destination is A.”

So no, D cannot initiate a valid route to A.

**Answer:**

No.

---

### 4. Can a report originating at C reach E without passing through D?

The rules say:

“Any report originating at C that eventually reaches E must pass through D.”

So no, C cannot reach E without passing through D.

**Answer:**

No.

---

### 5. Brief explanation using only the routing rules

1. **A to E:** A can go to B or D.

- A → B → C → D → E is valid.

- A → D → E is valid.

No repeats occur.

2. **A to C if B unavailable:** A → D is allowed, and D → C is allowed.

So A → D → C works without B.

3. **D initiating to A:** The rules explicitly forbid D from initiating a route whose destination is A.

4. **C to E without D:** The rules explicitly require any C-originating route that reaches E to pass through D.

Final answers:

1. **A → B → C → D → E** and **A → D → E**

2. **Yes: A → D → C**

3. **No**

4. **No**

5. Explained above using only the given routing rules.

### Gemini

#### Trial 1 / Recorded response

**1. Valid routes from A to E**

- **Routes:**
- - **A** $\rightarrow$ **D** $\rightarrow$ **E**
  - **A** $\rightarrow$ **B** $\rightarrow$ **C** $\rightarrow$ **D** $\rightarrow$ **E**
- **Explanation:** Department A can send reports to either B or D.
- - Taking the direct path to D leads straight to E (**A** $\rightarrow$ **D** $\rightarrow$ **E**).
  - Going through B requires routing to C, then to D, and finally to E (**A** $\rightarrow$ **B** $\rightarrow$ **C** $\rightarrow$ **D** $\rightarrow$ **E**). No department is visited more than once in either route.

**2. Can A reach C if B is unavailable?**

- **Answer:** Yes.
- **Route:** **A** $\rightarrow$ **D** $\rightarrow$ **C**
- **Explanation:** Since B is unavailable, A sends the report directly to D, and D can send reports directly to C without involving B.

**3. Can D initiate a valid report route whose destination is A?**

- **Answer:** No.
- **Explanation:** The routing rules explicitly state that D cannot initiate a route destined for A. Additionally, no department in the network has permission to send reports directly to A.

**4. Can a report originating at C reach E without passing through D?**

- **Answer:** No.
- **Explanation:** Department C can only send reports directly to D. Therefore, any route originating at C must immediately pass through D before reaching any other department, including E.

#### Trial 2 / Recorded response

Python

# Let's model the directed graph:

# Nodes: A, B, C, D, E

edges = {

'A': ['B', 'D'],

'B': ['C'],

'C': ['D'],

'D': ['E', 'C'],

'E': ['B']

}

# Function to find all valid simple routes from start to end

def find_all_routes(start, end, path=None):

if path is None:

path = [start]

if start == end:

return [path]

routes = []

for neighbor in edges.get(start, []):

if neighbor not in path:

new_routes = find_all_routes(neighbor, end, path + [neighbor])

for r in new_routes:

routes.append(r)

return routes

print("1. Routes from A to E:")

print(find_all_routes('A', 'E'))

print("\n2. Routes from A to C if B is unavailable:")

# Remove B from graph

edges_no_B = {

'A': ['D'],

'C': ['D'],

'D': ['E', 'C'],

'E': []

}

def find_all_routes_no_B(start, end, path=None):

if path is None:

path = [start]

if start == end:

return [path]

routes = []

for neighbor in edges_no_B.get(start, []):

if neighbor not in path:

new_routes = find_all_routes_no_B(neighbor, end, path + [neighbor])

for r in new_routes:

routes.append(r)

return routes

print(find_all_routes_no_B('A', 'C'))

print("\n3. Routes from D to A:")

print(find_all_routes('D', 'A'))

print("\n4. Routes from C to E:")

print(find_all_routes('C', 'E'))

Code output

1. Routes from A to E:

[['A', 'B', 'C', 'D', 'E'], ['A', 'D', 'E']]

2. Routes from A to C if B is unavailable:

[['A', 'D', 'C']]

3. Routes from D to A:

[]

4. Routes from C to E:

[['C', 'D', 'E']]

**1. Valid routes from A to E**

- **Route 1:** A → D → E
- **Route 2:** A → B → C → D → E

**Explanation:** Department A can send directly to D, which sends directly to E. Alternatively, A sends to B, B sends to C, C sends to D, and D sends to E. Moving from A to D and then to C gets trapped because C can only send back to D, which would violate the rule against visiting a department more than once.

**2. Reaching C from A if B is unavailable**

- **Answer:** Yes
- **Valid Route:** A → D → C

**Explanation:** Department A can bypass B by sending the report directly to D, and D has direct permission to send reports to C.

**3. Can D initiate a valid report route to A?**

- **Answer:** No

**Explanation:** The rules explicitly state that Department D cannot initiate a report route whose destination is A. Additionally, no department in the system has a valid routing permission into A.

**4. Can a report originating at C reach E without passing through D?**

- **Answer:** No

**Explanation:** Department C's only outgoing routing permission is directly to Department D. Therefore, any report starting at C must pass through D to go anywhere else, including E.

#### Trial 3 / Recorded response

1. **Valid Routes from A to E**

- **A → D → E**
- **A → B → C → D → E**
- *Explanation:* A can send directly to either D or B:
- - Taking the path through D, D can send directly to E, forming **A → D → E**. (Going from D to C leads to a dead end, as C can only send back to D, which violates the rule against visiting a department more than once).
  - Taking the path through B, B sends to C, C sends to D, and D sends to E, forming **A → B → C → D → E**.

2. **Reaching C from A if B is Unavailable**

- **Yes:** **A → D → C**
- *Explanation:* Without B, A sends the report directly to D, and D sends it directly to C. This completes the route without using B or visiting any department twice.

3. **Can D Initiate a Route to Destination A?**

- **No**
- *Explanation:* The rules explicitly forbid Department D from initiating a report route whose destination is A. Furthermore, no department in the network has permission to send reports directly to A.

4. **Can a Report Originating at C Reach E Without Passing Through D?**

- **No**
- *Explanation:* The only department C can send reports to directly is D. Therefore, any valid path starting at C must visit D first before reaching E.

### Claude

#### Trial 1 / Recorded response

**Direct edges:** A→B, A→D, B→C, C→D, D→C, D→E, E→B. (B→E does not exist, and D cannot initiate a route to A.)

**1. Routes from A to E (no repeated departments):**

- A → D → E
- A → B → C → D → E

(A → D → C → D → E is invalid because D repeats.)

**2. If B is unavailable, can A still reach C?**  
 Yes: **A → D → C**.

**3. Can D initiate a route whose destination is A?**  
 No. The rules explicitly forbid it. Independently, no department has a direct edge into A, so A could not be reached anyway.

**4. Can C reach E without passing through D?**  
 No. C's only outgoing edge is C→D, and the only edge into E is D→E, so every C-to-E route goes through D.

**5. Explanations:**

1. A can send to B or D. From D, the direct edge D→E reaches E immediately. From B, the path continues B→C (B has no direct edge to E), then C→D, then D→E. Since a route can't revisit a department, those are the only two valid routes.
2. With B out, A's only remaining edge is A→D, and D→C gives a direct route to C. The alternative A→D→E→B→C is blocked because B is unavailable.
3. The rules prohibit D from initiating a route to A, and no edge leads into A in any case.
4. C's sole outgoing edge goes to D, and E can be entered only from D, so passing through D is unavoidable, which matches the stated rule.

#### Trial 2 / Recorded response

**Direct links stated:** A→B, A→D, B→C, C→D, D→C, D→E, E→B. (B→E is not allowed, and nothing is stated that sends to A.)

**1. Routes from A to E (no department repeated):**

- A → D → E
- A → B → C → D → E

(A → D → C → D → E is invalid because it visits D twice.)

**2. If B is unavailable, can A still reach C?**  
 Yes. Route: A → D → C.

**3. Can D initiate a route whose destination is A?**  
 No. This is explicitly prohibited. It is also consistent with the link list, since no department has a direct link to A.

**4. Can C reach E without passing through D?**  
 No. C's only outgoing link is C→D, and the rules state that any report from C that eventually reaches E must pass through D.

**5. Brief explanations:**

1. E is only reachable via D→E, so a report must reach D first. A reaches D directly (A→D), or via B and C (A→B→C→D). Both then continue D→E.
2. Without B, A's only remaining outgoing link is A→D, and D→C completes the route.
3. The rule prohibits D from initiating a route to A, and no link into A exists anyway.
4. C→D is C's only outgoing link, and the rule requires that any route from C to E go through D.

#### Trial 3 / Recorded response

**Direct edges:** A→B, A→D, B→C, C→D, D→C, D→E, E→B. (B→E is not allowed. Nothing leads into A, and D cannot initiate a route to A.)

**1. Routes from A to E (no repeated departments):**

- A → D → E
- A → B → C → D → E

(The route A → D → C → D → E is invalid because it visits D twice.)

**2. If B is unavailable, can A still reach C?**  
 Yes. The route is A → D → C. A's direct edge to D and D's direct edge to C are both unaffected by B's absence.

**3. Can D initiate a valid route with destination A?**  
 No. The rules explicitly state that D cannot initiate a route whose destination is A. This is also consistent with the edge list, since no department has a direct edge to A, so no route could end there anyway.

**4. Can a report from C reach E without passing through D?**  
 No. C's only outgoing edge is C→D, and the only edge into E is D→E, so any route from C to E must pass through D. This matches the stated rule.

**5. Explanation:**

- **Q1:** E can only be entered from D (D→E). D can be reached from A directly (A→D) or via C (C→D), and C is reachable from A through B (A→B→C). Longer routes would need to revisit a department, which is forbidden.
- **Q2:** Removing B eliminates A→B→C, but A→D and D→C still form a valid path.
- **Q3:** The rule against D initiating a route to A applies directly, and no edge into A exists anyway.
- **Q4:** C's sole outgoing edge goes to D, and D is the sole entry point to E, so passing through D is unavoidable.

### Grok

#### Trial 1 / Recorded response

**1.** The valid routes from A to E are:

- A → B → C → D → E

- A → D → E

**2.** Yes. The valid route is A → D → C.

**3.** No.

**4.** No.

**5.** Explanations (using only the stated routing rules):

- Routes from A to E exist because A has direct links to both B and D; B links directly to C; C links directly to D; and D links directly to E. Both resulting sequences are simple (no department repeated).

- With B unavailable, the remaining direct links still permit A → D → C, which is a simple path.

- The rules explicitly state that D cannot initiate a report route whose destination is A; independently, no incoming links to A exist from any department, so no simple path from D to A is possible.

- The rules state that any report originating at C that reaches E must pass through D; the only direct link out of C is to D, after which D can reach E, so every path from C to E includes D.

#### Trial 2 / Recorded response

**1.** The valid routes from A to E are:

- A → D → E

- A → B → C → D → E

**2.** Yes. The valid route is A → D → C.

**3.** No.

**4.** No.

**5.**

- From the stated direct links, the only simple paths (no department repeated) that start at A and end at E are A-D-E and A-B-C-D-E.

- Removing B leaves the direct links A→D and D→C, which form the simple path A-D-C.

- No sequence of the given direct links starts at D and ends at A (A has no incoming links at all).

- The only outgoing link from C is C→D, so every path that begins at C and reaches E must use that link and therefore pass through D.

#### Trial 3 / Recorded response

**1. Valid routes from A to E:** A → B → C → D → E and A → D → E.

**2. Yes:** A → D → C.

**3. No.**

**4. No.**

**5. Explanations (using only the given routing rules):**

- Direct edges are exactly those stated: A→B, A→D, B→C, C→D, D→C, D→E, E→B (and the explicit prohibition B↛E). Paths must be simple (no department repeated).

- From A the two simple paths that reach E are therefore A-B-C-D-E and A-D-E.

- Removing B leaves the remaining edge A→D; continuing D→C yields the simple path A-D-C, so A can still reach C.

- No stated edge points to A from any department, so no simple path starting at D can have destination A (consistent with the explicit rule that D cannot initiate a route whose destination is A).

- The only outgoing edge from C is C→D; the only continuation that reaches E is then D→E. Hence every path from C to E must contain D (as the problem also states directly).

### Meta AI

#### Trial 1 / Recorded response

All answers follow only from the routing rules you listed.

**Graph from the rules:**

- A -> B, A -> D

- B -> C

- C -> D

- D -> E, D -> C

- E -> B

- No edge B -> E

- No cycles allowed to repeat a department

**1. A to E?**

Valid routes must end with D -> E, because that is the only rule allowing direct send to E.

- A -> D -> E — allowed by A->D and D->E.

- A -> B -> C -> D -> E — allowed by A->B, B->C, C->D, D->E. No department repeats.

Route A -> D -> C -> D -> E is **invalid** because it visits D twice, violating the no-repeat rule. Any other route would require B->E which is explicitly forbidden.

So the two valid routes are **A-D-E** and **A-B-C-D-E**.

**2. If B is unavailable, can A still reach C?**

Yes.

A -> D -> C is valid using A->D and D->C. B is not needed. This does not violate the no-repeat rule.

**3. Can D initiate a route whose destination is A?**

No.

You gave as a fixed rule: **D cannot initiate a report route whose destination is A.** That directly forbids it.

**4. Can C reach E without passing through D?**

No.

You gave as a fixed rule: **Any report originating at C that eventually reaches E must pass through D.** Therefore a C->E route without D is invalid. This is also consistent with the edges, since the only outgoing rule from C is C->D.

#### Trial 2 / Recorded response

Given the fixed rules and that a valid route cannot visit the same department more than once:

**1. A to E**

Valid routes are:

* **A -> D -> E** - Allowed because A can send directly to D, and D can send directly to E.

* **A -> B -> C -> D -> E** - Allowed because A -> B, B -> C, C -> D, D -> E.

Both are simple paths with no repeated departments.

Route A -> D -> C -> D -> E is NOT valid because it would visit D twice, violating the no-repeat rule.

**2. If B is unavailable, can A still reach C?**

Yes.

* **A -> D -> C** - Allowed because A can send directly to D, and D can send directly to C. This does not require B.

**3. Can D initiate a route whose destination is A?**

No.

Per the routing rules: **Department D cannot initiate a report route whose destination is A.**

**4. Can a report originating at C reach E without passing through D?**

No.

Per the routing rules: **Any report originating at C that eventually reaches E must pass through D.**

Therefore a C to E route that bypasses D is explicitly prohibited.

#### Trial 3 / Recorded response

The routing graph defined by the rules is:

* **A -> B**

* **A -> D**

* **B -> C**

* **C -> D**

* **D -> C**

* **D -> E**

* **E -> B**

Additional constraints:

* No route may visit the same department more than once.

* **B cannot send directly to E.**

* **D cannot initiate a route whose destination is A.**

* Any route **C -> ... -> E must pass through D.**

**1. What valid route(s) allow a report originating at A to reach E?**

Two valid routes:

* **A -> D -> E**

* **A -> B -> C -> D -> E**

Explanation: A can go directly to D, and D can go directly to E. That satisfies A->D and D->E. Also A->B is allowed, B->C is allowed, C->D is allowed, D->E is allowed. No department is repeated.

A -> D -> C -> D -> E is NOT valid because it would visit D twice, which violates "cannot visit the same department more than once."

**2. If B becomes unavailable, can a report originating at A still reach C?**

Yes.

**A -> D -> C**

Explanation: A can send directly to D, and D can send directly to C. This route does not use B.

**3. Can D initiate a valid report route whose destination is A?**

No.

Explanation: The rules state explicitly: "Department D cannot initiate a report route whose destination is A."

**4. Can a report originating at C reach E without passing through D?**

No.

Explanation: Two reasons from the rules:

a) The only direct send allowed from C is C -> D, so any route starting at C must go to D first.

b) The rules state explicitly: "Any report originating at C that eventually reaches E must pass through D."
