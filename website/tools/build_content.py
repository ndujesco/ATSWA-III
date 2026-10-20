#!/usr/bin/env python3
"""
content/<code>/ch*.py  ->  data/<code>.js

Each chapter module defines CH = {...}; meta.py defines META = {...}.
The builder checks the chapter set is complete and that every block is a
shape the renderer knows, so a typo fails the build instead of the page.
"""
import importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT, DATA = ROOT / 'content', ROOT / 'data'
SUBJECTS = {'ca': ('CA', 15), 'aud': ('AUD', 12), 'tax': ('TAX', 25), 'man': ('MAN', 10)}
# man not yet added — confirm its total chapter count from its own study-text
# TOC before adding, per ATSWA III/PLAN.md Phase 2.
# aud confirmed from 2025_Aud.pdf's own TOC: 12 chapters (Nature/Purpose/Scope of
# Auditing; Regulatory Framework; Professional Ethics; Auditors' Liability; Audit
# Planning & Documentation; Audit Evidence & Verification; Audit Tests & Sampling;
# Internal Control System; Public Sector Assurance; IT-Based Audit Assurance;
# Reports on Financial Statements; Audit Completion).
# tax confirmed from Taxation_2026_Study_Text.pdf's own TOC (5th edition, reflecting
# the Nigeria Tax Act 2025 / Nigeria Tax Administration Act 2025 reform, effective the
# September 2026 diet): 25 chapters — Introduction to Taxation; Administration of
# Taxation; Basic Ethical Issues in Taxation; Returns/Assessments/Collection Procedures;
# Objections & Appeal Procedures; Tax Clearance Certificate; VAT; Stamp Duties;
# Withholding Tax; Customs & Excise Duties; Surcharge on Fossil Fuel Products; Taxation
# of Employment Income; Computation of Personal Income Tax; Taxation of Investment
# Income; Taxation of Sole Traders/Self-Employed Individuals; Capital Allowances;
# Taxation in Partnerships; Settlement, Trusts & Estates; Loss Relief; Ascertainment of
# Assessable Profit; Computation of Companies Income Tax; Taxation of Specialised
# Businesses; Federal Development Levy; Chargeable Gains; Application of IT in Taxation.

BLOCKS = {'p', 'h3', 'h4', 'ul', 'ol', 'steps', 'tex', 'def', 'note', 'key',
          'warn', 'pre', 'table', 'eg', 'tacc', 'stmt', 'fbox'}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_blocks(blocks, where, errs):
    if not isinstance(blocks, list):
        errs.append(f'{where}: blocks must be a list')
        return
    for i, b in enumerate(blocks):
        if isinstance(b, str):
            continue
        if not isinstance(b, dict):
            errs.append(f'{where}[{i}]: not a dict')
            continue
        keys = [k for k in b if k in BLOCKS]
        if not keys:
            errs.append(f'{where}[{i}]: unknown block {list(b)[:3]}')
        if 'eg' in b:
            check_blocks(b['eg'].get('q', []), f'{where}[{i}].eg.q', errs)
            check_blocks(b['eg'].get('a', []), f'{where}[{i}].eg.a', errs)


def check_tex(obj, where, errs):
    """Unbalanced braces in a TeX string are the one error the renderer
       cannot recover from, so catch them here."""
    def walk(x, w):
        if isinstance(x, str):
            for m in re.finditer(r'\$\$?([^$]+?)\$\$?', x):
                t = m.group(1)
                if t.count('{') != t.count('}'):
                    errs.append(f'{w}: unbalanced braces in inline tex: {t[:60]}')
        elif isinstance(x, dict):
            for k, v in x.items():
                if k == 'tex' and isinstance(v, str):
                    if v.count('{') != v.count('}'):
                        errs.append(f'{w}.tex: unbalanced braces: {v[:60]}')
                walk(v, w + '.' + str(k))
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f'{w}[{i}]')
    walk(obj, where)


def build(code):
    d = CONTENT / code
    if not d.exists():
        return None
    meta = {}
    if (d / 'meta.py').exists():
        meta = load(d / 'meta.py', code + '_meta').META
    chapters, errs = [], []
    for f in sorted(d.glob('ch*.py')):
        mod = load(f, f'{code}_{f.stem}')
        ch = mod.CH
        for sec in ch.get('secs', []):
            check_blocks(sec.get('b', []), f'{code} ch{ch["n"]} sec {sec.get("n")}', errs)
        check_tex(ch, f'{code} ch{ch["n"]}', errs)
        # every MCQ needs a defensible answer index
        for j, q in enumerate(ch.get('quiz', {}).get('mcq', [])):
            if not (0 <= q.get('a', -1) < len(q.get('o', []))):
                errs.append(f'{code} ch{ch["n"]} mcq[{j}]: answer index out of range')
            if len(q.get('o', [])) < 4:
                errs.append(f'{code} ch{ch["n"]} mcq[{j}]: fewer than four options')
        chapters.append(ch)
    if errs:
        for e in errs[:25]:
            print('  ERROR', e)
        raise SystemExit(f'{code}: {len(errs)} content errors')
    chapters.sort(key=lambda c: c['n'])
    want = SUBJECTS[code][1]
    have = [c['n'] for c in chapters]
    missing = [i for i in range(1, want + 1) if i not in have]
    blob = dict(meta); blob['chapters'] = chapters
    js = f'ATSWA.put("{SUBJECTS[code][0]}", ' + \
         json.dumps(blob, ensure_ascii=False, separators=(',', ':')) + ');\n'
    (DATA / f'{code}.js').write_text(js)
    nq = sum(len(c.get('quiz', {}).get('mcq', [])) for c in chapters)
    nt = sum(len(c.get('quiz', {}).get('theory', [])) for c in chapters)
    ns = sum(len(c.get('secs', [])) for c in chapters)
    nf = sum(len(c.get('formulas', []) or []) for c in chapters)
    print(f'data/{code}.js  {len(js)//1024:>4} KB  {len(chapters):>2}/{want} chapters, '
          f'{ns:>3} sections, {nf:>3} formulas, {nq:>3} MCQ, {nt:>3} theory'
          + (f'   MISSING {missing}' if missing else ''))
    return missing


if __name__ == '__main__':
    DATA.mkdir(exist_ok=True)
    which = sys.argv[1:] or list(SUBJECTS)
    for c in which:
        build(c)
