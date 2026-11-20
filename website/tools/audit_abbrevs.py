#!/usr/bin/env python3
"""
Find exam-tested abbreviations used without an expansion in an ATSWA III
chapter. Run with AUD, CA, TAX or MAN (defaults to AUD). These are review
candidates, not proven omissions.

Method: collect every "(ABBR)" the chapter already writes out somewhere
(e.g. "Pension Fund Administrator (PFA)") — that's a defined abbreviation.
Then collect every bare use of an all-caps 2-6 letter token. Anything used
bare that was never defined *anywhere in that chapter* is flagged.

Common cross-chapter abbreviations that are conventionally assumed known
throughout the site (IPSAS, VAT, etc. — defined once, early, used site-wide)
are excluded via a fixed allow-list rather than flagged in every chapter
that merely uses them.
"""
import importlib.util, json, re, sys
from pathlib import Path
from abbreviations import chapter_terms

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = (sys.argv[1] if len(sys.argv) > 1 else 'AUD').upper()
COUNTS = {'AUD': 12, 'CA': 15, 'TAX': 25, 'MAN': 10}
if SUBJECT not in COUNTS:
    raise SystemExit('Usage: python3 tools/audit_abbrevs.py [AUD|CA|TAX|MAN]')
CONTENT = ROOT / 'website' / 'content' / SUBJECT.lower()

ALLOW = set('''IPSAS IPSASB IFAC IASB IFRS VAT GDP PDF ATSWA CIT PPT PAYE PII NASS
FCT ICAN ANAN CBN SEC NDIC NCC NAICOM DVEA MDA MDAs LGA LGAs FRN NGO NGOs
FGN CRF USD GBP NGN CAP LFN FR ATC OK CEO CFO MD PLC USA UK UN AI IT ID
NOT EXCEPT ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ALL ANY NO YES
AND OR IN ON AT BY FOR FROM THE DO BE IS AS TO OF IF SO UP GO NEW OLD OWN
CASH COST ASSETS ASSET EQUITY NET TOTAL YEAR FLOWS NIL XX XXX XXXX DR CR NGN
I II III IV V VI VII VIII IX X TV UV PV DF BB US TB PS DG HQ CS
TRUE FALSE PART DOES XYZ AB CD TAXPRO MAX
'''.split())

RE_ABBR_TOKEN = re.compile(r'\b([A-Z]{2,6})s?\b')
RE_DEFINED = re.compile(r'\(([A-Z]{2,6})s?\)')


def bag_of(node, acc):
    if node is None:
        return
    if isinstance(node, str):
        acc.append(node)
    elif isinstance(node, list):
        for v in node:
            bag_of(v, acc)
    elif isinstance(node, dict):
        for v in node.values():
            bag_of(v, acc)


def def_terms(node, acc):
    """A def block's own 't' (e.g. {'def': {'t': 'GIFMIS', 'd': '...'}}) also
    counts as defining that term, even with no "(ABBR)" in sight."""
    if isinstance(node, list):
        for v in node:
            def_terms(v, acc)
    elif isinstance(node, dict):
        if 'def' in node and isinstance(node['def'], dict) and 't' in node['def']:
            acc.append(node['def']['t'])
        for v in node.values():
            def_terms(v, acc)


def load_chapter(n):
    path = CONTENT / f'ch{n:02d}.py'
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f'{SUBJECT}_{n}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CH


def main():
    papers = json.loads((ROOT / 'website' / 'data' / 'papers.json').read_text())
    stems = []
    for paper in papers:
        if paper['subject'] != SUBJECT:
            continue
        for question in paper['mcq']:
            stem = question['stem']
            stems.append(stem.get('t', '') if isinstance(stem, dict) else stem)
        for question in paper['saq']:
            stems.extend(question['body'])
        stems.extend(paper['secb_paper'])
    tested = set(RE_ABBR_TOKEN.findall(' '.join(stems))) - ALLOW
    checked, candidates = 0, 0
    for n in range(1, COUNTS[SUBJECT] + 1):
        ch = load_chapter(n)
        if not ch:
            raise FileNotFoundError(f'Missing {SUBJECT} chapter {n}; audit incomplete')
        checked += 1
        words = []
        bag_of(ch.get('t'), words)
        bag_of(ch.get('secs'), words)
        # Routes and URLs are destinations, not visible abbreviation uses.
        text = re.sub(r'\]\([^)]*\)', ']', ' '.join(words))
        defs = []
        def_terms(ch.get('secs'), defs)
        defined = set(RE_DEFINED.findall(text))
        defined |= {entry['term'] for entry in chapter_terms(ch)}
        defined |= {match[1] for entry in chapter_terms(ch)
                    if (match := re.fullmatch(r'([A-Z]{2,6})s', entry['term']))}
        # Texts also use the equally valid reverse form "FIFO (First In,
        # First Out)". Bold/italic markers must not hide that expansion.
        plain = text.replace('*', '')
        defined |= set(re.findall(r'\b([A-Z]{2,6})\s*\([A-Za-z][A-Za-z ,/-]{7,}\)', plain))
        for t in defs:
            defined |= set(RE_ABBR_TOKEN.findall(t))
        used = set(RE_ABBR_TOKEN.findall(text)) & tested
        if not re.search(r'activity[\s-]+based\s+cost', text, re.I):
            used.discard('ABC')  # A/B/C category or example-company label
        undefined = sorted(used - defined)
        if undefined:
            candidates += len(undefined)
            print(f'ch{n:02d} ({ch.get("t","")[:40]}): undefined -> {undefined}')
    print(f'{SUBJECT}: {checked} chapters checked; {candidates} exam-tested abbreviation uses to review.')


if __name__ == '__main__':
    main()
