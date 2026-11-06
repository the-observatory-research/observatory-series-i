# Series I machine-readable dataset material

The `hf-experiment-1b-starter/` directory is a previously prepared **evaluation-only starter** for Experiment 1B. It contains four scoring targets extracted from **one prompt**, not four independent historical trials. It is **not** a dataset of the historical model transcripts.

The user has previously published a Series I subset on Hugging Face, but the URL and exact live revision have **not been verified** for this packaging release. Add the canonical Hugging Face dataset URL to the root `README.md` after confirming it.

Important version discrepancy: the starter dataset card names the source DOCX SHA-256 as `81a7ab858494a82686c72c94b70b83ce591da1c63f832b1970abd1967c27295b`, while the DOCX in the recovered-transcript conversion bundle hashes to `2c2d3d3be9eb81000d86e4a08eec5953464ce2492e22d9b8ea751b8913f90556`, and the distinct DOCX in the older source bundle hashes to `b6ecbec347c85894ed14c87f59004180a7dcc1ad64d593654ae026ba4273d484`. These differ **as files**. Do not attribute the starter data to either bundled DOCX without checking its original provenance. The prompt text can be compared separately.

The dataset card and text are included **unchanged** from the historic starter package; this note documents the discrepancy without rewriting earlier releases.
