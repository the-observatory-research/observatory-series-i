# Uploading The Observatory — Series I to GitHub

1. Before uploading, review `provenance/READ-ME-FIRST.md` and the third-party model-output and source-file licensing questions.
2. Create a new GitHub repository named `observatory-series-i`. Suggested description:
   > Six-model evaluation study of relational recovery across controlled language, representation, compression, and relay transformations, with experiment transcripts and provenance.
3. Keep the repository **private initially**. Select **No license** when GitHub offers one (this prepared archive does not include a LICENSE file).
4. Download `observatory-series-i-github-ready.zip` and extract it on your computer.
5. On GitHub, use **Add file → Upload files** and drag in the **contents** of the extracted `observatory-series-i` folder. Do **not** upload only the `observatory-series-i-github-ready.zip` file. The folder hierarchy is created from the paths of the uploaded files.
6. Before committing, confirm the list includes `README.md`, `docs/`, `transcripts/`, `sources/`, `datasets/`, `tools/`, and `provenance/`.
7. Once uploaded, verify that the README links open. Add the URL of the existing Hugging Face dataset after verifying its current release and checking the source-fingerprint discrepancy noted in `datasets/README.md`.
8. Review all content, model text redistribution requirements, source DOCX metadata, and desired licensing before changing the repository visibility to public.

To verify this package locally:

```sh
python3 -m unittest discover -s tests -v
python3 tools/verify_package.py
```

The `tools/` code is newly created for the GitHub archival package, **not** original Series I execution code.
