---
pretty_name: The Observatory — Series I Relational Recovery (Experiment 1B)
language:
- en
size_categories:
- n<1K
tags:
- model-evaluation
- relational-recovery
- semantic-coherence
- source-invariance
- multi-agent-systems
---

# The Observatory — Series I Relational Recovery

**Release:** Initial benchmark subset — Experiment 1B (Explicit Baseline) only.  
**Study:** *What Remains*, Series I — independent longitudinal research by The Observatory.  
**Author:** Tara Callegari, Independent AI Systems Researcher.  
**Dataset type:** Evaluation-only reference example; **not** a training corpus or a record of independent new trials.

## What's in this release?

`test.jsonl` contains **four scoring targets from one original Experiment 1B prompt**, not four separately administered prompts. Each of the four rows repeats the full original task text and records the expected answer for one target. The fifth item in the original prompt requests explanations; it is included in the original text but is not separately scored here.

### Experiment 1B

The recorded network has five nodes, seven directed edges, a no-repeat rule, and restrictions on direct communication and mandatory intermediate nodes. Valid routes are evaluated from the **full original task**, not from isolated questions without their rules.

**Canonical answers:**
1. A → E: **A → D → E** and **A → B → C → D → E** (complete set).
2. A → C without B: **A → D → C**.
3. D → A: **No valid route**.
4. C → E without D: **No valid route**.

## Important provenance distinction

This dataset provides a **new machine-readable evaluation view of a historical experiment**. It does **not** publish the historical response transcripts, original trial-level scores, or a retrospectively computed success rate. The four benchmark rows are facets of **one original prompt**. A model should receive that full prompt once per trial, with all four responses assessed as a single response set.

The source is the original Word file **`Explicit Baseline - Experiment 1B.docx`**, retained in The Observatory's research archive; SHA-256 of the source DOCX: `81a7ab858494a82686c72c94b70b83ce591da1c63f832b1970abd1967c27295b`. The prompt's text is reproduced here with list numbering and whitespace normalized for machine use. The source DOCX remains the archival authority for formatting and historical answers.

Experiment **1A (Ambiguity Probe)** used deliberately different wording and is **not interchangeable** with 1B. The other Series I experiments (semantic recoding, dispersion, cross-representation, compression conditions, added relational load, and finite/unplanned relays) are **not included in this first subset**.

## Fields

- `id`: Stable identifier for a scoring target.
- `series`, `condition`: Research provenance.
- `original_prompt`: Full task as delivered, with normalized list formatting.
- `target_number`, `target_question`: One of the four canonical recovery targets.
- `expected_answer`, `expected_paths`: Canonical reference (paths empty for 'no path').
- `answer_type`, `evaluation_note`: Guidance for evaluator implementation.
- `provenance`: Source note.

## Recommended evaluation

Submit `original_prompt` **once per trial** and extract answers to its four recovery questions. Score exact set agreement on Target 1 (both routes, no invalid additions) and target-specific validity on Targets 2–4. A prospective equal-weight 4-target discrepancy measure may be defined as the fraction of incorrect target answers. **Do not call this prospective score the original Series I historical scoring method.**

Preserve model/version, decoding settings, session conditions, raw outputs, and evaluation decisions when reporting new results. No trial-level model results are contained in this release.

## Limitations

- Only one graph configuration/one prompt, with four canonical targets; not a comprehensive measure of intelligence or of general reasoning ability.
- Correct task answers alone do not identify model mechanisms or demonstrate consciousness.
- Historical Series I model outputs and source records should be linked or uploaded separately **only after provenance and privacy review**.
- A public Hugging Face upload makes the example and answer keys accessible, so it is an **open evaluation set**, not a secret held-out test.

## Research links

- The Observatory Research Archive: https://publish.obsidian.md/the-observatory/The+Observatory
- Cite the corresponding *What Remains* study and its research archive for historical interpretation. Add a precise version or DOI once selected by the researcher.

**Research theme:** What remains stable when continuity is disrupted?
