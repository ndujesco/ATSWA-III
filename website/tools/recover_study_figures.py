#!/usr/bin/env python3
"""Preserve original study-text diagram/table pages, with source provenance."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / 'data/study-figures.json').read_text())
    original = ROOT.parent / manifest['source']
    assert hashlib.sha256(original.read_bytes()).hexdigest() == manifest['sourceSha256'], 'Study text changed'
    for page in manifest['pages']:
        dest = ROOT / page['src']
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            subprocess.run(['pdftoppm', '-f', str(page['pdfPage']), '-l', str(page['pdfPage']),
                            '-r', '140', '-singlefile', '-png', str(original), str(dest.with_suffix(''))],
                           check=True)
        assert dest.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'), str(dest)
    print(f"Preserved {len(manifest['captions'])} source captions on {len(manifest['pages'])} original study-text pages.")


if __name__ == '__main__':
    main()
