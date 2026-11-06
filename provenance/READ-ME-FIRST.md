# Provenance and interpretation boundaries

This repository is a **publication packaging layer**, not a retrospective rewrite or re-execution of the completed *What Remains* Series I study.

## Distinct source classes
- `docs/`: existing authored Series I research report and execution log, copied without editorial rewriting from the archive.
- `sources/word-conversion-bundle/`: original DOCX files embedded with the nine-file recovered Markdown package. Their SHA-256 values match `QA_Report.json`.
- `transcripts/recovered-markdown/`: nine Markdown conversions from the named DOCX sources, **not** verified byte-identical native platform exports. These retain substantive model response text but recreate presentation and trial headings.
- `sources/additional-source-versions/`: separate Experiment 1A source and experiment results, plus an alternate Experiment 1B DOCX from an older bundle. These are not silently substituted for source files used in the Markdown conversion.
- `transcripts/experiment-1a-recovered.md`: readability reconstruction of a damaged export; `provenance/experiment-1a-damaged-export-unmodified.md` preserves the unmodified damaged Markdown.
- `provenance/original-bundles/`: intact archive ZIP files from which the sources were assembled.
- `datasets/hf-experiment-1b-starter/`: archived machine-readable reference dataset starter, not verified against a current hosted Hugging Face revision.

## Caveats requiring attention
1. Experiment 1A is deliberately **ambiguous** and is not interchangeable with the explicit 1B baseline.
2. Experiment 5 source includes one malformed trial divider; the transcript-recovery QA report records how it was interpreted.
3. Experiment 7A is the planned finite relay; 7B is an **unplanned answer-bearing relay observation**, not an independently replicated confirmatory trial.
4. Experiment 7B's source contains `[PASTE META'S FINAL OUTPUT FROM EXPERIMENT 7A HERE]` for one payload. The transmitted input cannot be established from that placeholder; no repair is attempted here.
5. Multiple *Experiment 1B* DOCX file versions exist. The Hugging Face starter quotes a third fingerprint not matched by the two source bundles. See `datasets/README.md`.
6. Reconstructed Markdown formatting, retrospective summaries, and newly written verification tools should **not** be mistaken for unchanged model-platform exports or historical analysis code.
7. Historical research results remain attributed to the frozen source report and original evidence. No metric is recalculated as an historical result by the new helper script.

## Before public publication
Verify model-output redistribution terms, original attachments, personal information, any source metadata embedded in DOCX files, and licensing. This starter intentionally contains **no LICENSE** file pending the author's decision.
