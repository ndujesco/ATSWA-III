#!/usr/bin/env python3
"""Assemble the verified zero-dependency static site in ATSWA III/dist/."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT.parent / 'dist'
FILES = ['index.html']
DATA = ['ca.js', 'aud.js', 'tax.js', 'man.js', 'exams.js', 'revision.js']


def main():
    report = json.loads((ROOT / 'data/audit-report.json').read_text())
    assert report['questions'] == {'mcq': 1800, 'saq': 1200, 'secb': 360}
    assert report['questionsWithSourcePage'] == 3360
    assert all(c['chapter'] == c['section'] == c['all'] for c in report['citations'].values())
    # Only this generated output directory is replaced. Authored sources,
    # notes, local progress and original materials are never modified.
    if DEST.exists():
        shutil.rmtree(DEST)
    (DEST / 'data').mkdir(parents=True)
    for name in FILES:
        shutil.copy2(ROOT / name, DEST / name)
    for name in DATA:
        shutil.copy2(ROOT / 'data' / name, DEST / 'data' / name)
    for name in ['assets', 'guides']:
        shutil.copytree(ROOT / name, DEST / name,
                        ignore=shutil.ignore_patterns('.DS_Store', '__pycache__'))
    files = sorted(path for path in DEST.rglob('*') if path.is_file())
    manifest = {str(path.relative_to(DEST)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in files}
    (DEST / 'release.json').write_text(json.dumps({'inventory': report, 'sha256': manifest},
                                                 indent=2, ensure_ascii=False) + '\n')
    print(f'Packaged {len(files)} files in {DEST} ({sum(p.stat().st_size for p in files):,} bytes)')


if __name__ == '__main__':
    main()
