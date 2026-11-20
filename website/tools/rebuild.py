#!/usr/bin/env python3
"""Rebuild and verify the complete dependency chain. Add --extract for PDFs."""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract', action='store_true')
    args = parser.parse_args()
    commands = []
    if args.extract:
        commands.append([sys.executable, 'tools/extract_papers.py'])
    commands += [
        [sys.executable, 'tools/recover_study_figures.py'],
        [sys.executable, 'tools/build_content.py'],
        [sys.executable, 'tools/aim.py'],
        [sys.executable, 'tools/aim_sec.py', 'AUD', 'CA', 'TAX', 'MAN'],
        [sys.executable, 'tools/recover_figures.py'],
        [sys.executable, 'tools/build_exams.py'],
        [sys.executable, 'tools/final_revision.py'],
        ['sh', 'build.sh'],
        [sys.executable, 'tools/audit_papers.py'],
        [sys.executable, 'tools/test_pipeline.py'],
        ['node', 'tools/test.mjs'],
    ]
    for command in commands:
        print('Running ' + ' '.join(command[1:] if command[0] == sys.executable else command), flush=True)
        subprocess.run(command, cwd=ROOT, check=True)


if __name__ == '__main__':
    main()
