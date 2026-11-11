#!/usr/bin/env python3
"""Recover source formulas/diagrams that pdftotext cannot represent."""
import subprocess
from pathlib import Path
from source_recoveries import FIGURE_PAGES

ROOT = Path(__file__).resolve().parents[1]


def main():
    dest = ROOT / 'assets/source-figures'
    dest.mkdir(parents=True, exist_ok=True)
    for diet, page in FIGURE_PAGES:
        pdf, = (ROOT.parent / 'materials/past-questions').glob(f'*{diet}*.pdf')
        output = dest / f'{diet}-p{page}'
        if not output.with_suffix('.png').exists():
            subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page),
                            '-r', '140', '-singlefile', '-png', str(pdf), str(output)],
                           check=True)
        print(output.with_suffix('.png').relative_to(ROOT))


if __name__ == '__main__':
    main()
