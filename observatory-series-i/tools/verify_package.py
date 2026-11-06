#!/usr/bin/env python3
"""Verify package checksums and recovered source DOCX against original QA records."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[1]

def check() -> None:
    manifest=ROOT/'provenance/files.sha256'
    checked=0
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip():continue
        digest, rel=line.split('  ',1)
        path=ROOT/rel
        if not path.is_file() or sha256(path.read_bytes()).hexdigest()!=digest:
            raise ValueError(f'Checksum mismatch or missing file: {rel}')
        checked+=1
    qa=json.loads((ROOT/'provenance/QA_Report.json').read_text(encoding='utf-8'))
    for entry in qa:
        source=ROOT/'sources/word-conversion-bundle'/entry['original_filename']
        if sha256(source.read_bytes()).hexdigest()!=entry['sha256_source']:
            raise ValueError(f'Original conversion source SHA mismatch: {source.name}')
    print(f'PASS: {checked} package files checked; {len(qa)} recovered DOCX checks matched QA report')

if __name__ == '__main__': check()
