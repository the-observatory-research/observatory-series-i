# The Observatory — Series I
## Relational Recovery under Controlled Transformation

**Empirical cross-model evaluation · Six model systems · Seven planned experiments with additional subconditions and an unplanned relay observation**

Part of *What Remains*, The Observatory's completed longitudinal AI model-behavior research. This repository makes existing experimental methods, source records, and supporting reference material independently inspectable. It does **not** reopen the study or claim new experimental trials.

## Research question

Under what representational and transmission changes does specified relational information remain recoverable across different language models?

Series I uses a five-node directed relational system as a reference object and measures recovery of specified routes and constraints, rather than similarity of wording or identity of internal model representations. The original research separates finite task performance from broader claims about model architecture or consciousness.

## Experiments and source transcripts

| Condition | Archived Markdown source |
| --- | --- |
| **1A — Ambiguity Probe** | [Recovered 1A transcript](transcripts/experiment-1a-recovered.md) — damaged-source recovery; see caveats |
| **1B — Explicit Baseline** | [1B transcript](transcripts/recovered-markdown/Experiment_1B_Explicit_Baseline.md) |
| **2 — Semantic Recoding** | [Experiment 2](transcripts/recovered-markdown/Experiment_2_Semantic_Recoding.md) |
| **3 — Relational Dispersion** | [Experiment 3](transcripts/recovered-markdown/Experiment_3_Relational_Dispersion.md) |
| **4 — Cross-Representational Mapping** | [Experiment 4](transcripts/recovered-markdown/Experiment_4_Cross_Representational_Mapping.md) |
| **5 — Compression Gradient (C1–C3)** | [Experiment 5](transcripts/recovered-markdown/Experiment_5_C1-C3_Compression_Gradient.md) |
| **5 — C3′ Explicit No-Repeat Control** | [Control](transcripts/recovered-markdown/Experiment_5_C3Prime_Explicit_No_Repeat_Control.md) |
| **6 — Relational Interference** | [Experiment 6](transcripts/recovered-markdown/Experiment_6_Relational_Interference.md) |
| **7A — Recursive Differentiated Transport** | [Experiment 7A](transcripts/recovered-markdown/Experiment_7A_Recursive_Differentiated_Transport.md) |
| **7B — Unplanned Relay Observation** | [Experiment 7B](transcripts/recovered-markdown/Experiment_7B_Unplanned_Relay_Observation.md) — not a planned replication |

Six systems were included in the original experiments: ChatGPT, DeepSeek, Gemini, Claude, Grok, and Meta AI. See the source report and logs for trial conditions and limitations.

## Research documentation

- [Series I research report](docs/research-report.md) — methodology, original reported results, and interpretive limits
- [Seven Planned Experiments execution log](docs/execution-log.md) — conditions, execution chronology, and observations
- [Source records and original Word files](sources/) — original submitted source documents
- [Conversion QA and provenance notes](provenance/READ-ME-FIRST.md) — hashes, conversion constraints, and unresolved evidence

## Machine-readable evaluation subset

A local archive of the initial **Experiment 1B Hugging Face benchmark starter** is provided in [datasets/hf-experiment-1b-starter/](datasets/hf-experiment-1b-starter/). Its four JSONL records represent four scoring **targets from one original prompt**; they are **not** four distinct historical trials and they do not substitute for the historical responses.

**Hosted Hugging Face dataset:** Add the verified live URL here after comparing versions. The user has an existing Series I Hugging Face publication; its exact published revision has not been checked for this repository build.

## Utility scripts (created for archival packaging, not historical research)

The repository includes a small deterministic *post-archive* checker for the four explicit baseline 1B questions, along with checksum verification. These were added to make reference data inspectable; **neither was used during the original study**.

```bash
python3 -m unittest discover -s tests -v
python3 tools/check_experiment_1b.py
python3 tools/verify_package.py
```

## Repository layout

```text
docs/                             # Frozen research report and execution log
transcripts/                      # Nine recovered transcripts and separate 1A recovery
sources/                          # Word source documents and alternate source versions
datasets/hf-experiment-1b-starter # Original machine-readable evaluation starter
tools/                            # New post-archive helper tools
tests/                            # Tests for new helper (not historical trial tests)
provenance/                       # QA report, hashes, distinct archive bundles, caveats
```

## Evidence limits and publication status

- Recovered Markdown documents preserve response text from the supplied Word sources, but use reconstructed presentation; they are **not** original native chat-platform exports.
- The recovered 1A Markdown document was repaired for readability from a damaged export; its unmodified damaged counterpart is retained separately.
- Experiment 5 includes a malformed source trial separator documented in the QA report.
- Experiment 7B includes a literal placeholder for one relay input. Actual transmitted content for that specific segment must not be inferred or silently filled.
- Multiple source-version fingerprints exist for Experiment 1B, including a difference between the earlier benchmark starter and available source bundles. See [provenance notes](provenance/READ-ME-FIRST.md).
- Historical outcomes and evaluative claims are those of the preserved research reports, **not** results of the new reference-checking helper.

## Research identity and citation

**The Observatory** is an independent AI research program. This repository is a technical access point to its completed Series I research and should link back to the authoritative Research Archive and citable publications.

- [The Observatory Research Archive](https://publish.obsidian.md/the-observatory/The+Observatory)
- Add a verified Zenodo Series I DOI here if/when applicable.
