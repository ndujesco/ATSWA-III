#!/usr/bin/env python3
"""
Turn all downloaded ATSWA Part III INSIGHT packs into structured JSON.

Each pack holds four papers (AUD, CA, TAX, MAN). Each paper is:
    Section A Part I   30 multiple-choice questions      (30 marks)
    Section A Part II  20 short-answer questions         (20 marks)
    Section B          6 questions, attempt any four     (50 marks)
followed by the official solutions for all three, plus examiner comments.

Output: data/papers.json
"""
import hashlib, json, re, shutil, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import FURNITURE, strip_furniture, tidy, money, squeeze, desymbol
from source_recoveries import SAQ_RECOVERIES

ROOT = Path(__file__).resolve().parents[2]
PQ   = ROOT / 'materials' / 'past-questions'
OUT  = ROOT / 'website' / 'data'

DIETS = []
for path in sorted(PQ.glob('INSIGHT Part III - *.pdf')):
    m = re.fullmatch(r'INSIGHT Part III - (\d{4}-\d{2}) (.+)\.pdf', path.name)
    if not m:
        raise ValueError(f'Unexpected pack filename: {path.name}')
    DIETS.append((m[1], m[2], path.name))
SUBJECTS = [
    ('AUD', 'AUDITING'),
    ('CA', 'COST ACCOUNTING'),
    ('TAX', 'TAX'),
    ('MAN', 'MANAGEMENT'),
]

# ── markers ───────────────────────────────────────────────────────────────
RE_PAPERHEAD = re.compile(r'PART\s+III\s+EXAMINATIONS?\s*[-–]', re.I)

# Older diets wrap "MULTIPLE-CHOICE QUESTIONS" / "SHORT-ANSWER QUESTIONS" onto
# their own line below the "SECTION A: PART I/II ATTEMPT ALL QUESTIONS" banner
# rather than trailing it on the same line, and print "SECTION B" with no
# colon at all — so none of these three markers require what follows on the
# same physical line, only the banner phrase itself, which is distinctive
# enough on its own not to appear anywhere but at each part's true start.
# One diet drops "PART II" from the Part II banner entirely ("SECTION A:
# SHORT-ANSWER QUESTIONS"), so both banners also accept "SECTION A" directly
# followed, on the same line, by the part's own keyword.
# One diet drops "SECTION A:" entirely from the Part II banner, leaving a
# bare "PART II   SHORT-ANSWER QUESTIONS (20 Marks)" — safe to accept without
# that prefix specifically because it still requires the part's own keyword
# on the same line, unlike the page-footer "ATSWA PART II <diet>" that
# repeats on every page and never carries that keyword.
RE_SECA1 = re.compile(r'^\s*SECTION\s+A[:\s–—-]*PART\s+(?:I|1)\b|'
                      r'^\s*SECTION\s+A[:\s]*MU(?:L)?TI(?:PLE|PLIE)?[\s\-–—:()]*CHOICE|'
                      r'^\s*PART\s+(?:I|1)\b[:\s]*MU(?:L)?TI(?:PLE|PLIE)?[\s\-–—:()]*CHOICE', re.I)
RE_SECA2 = re.compile(r'^\s*SECTION\s+A[:\s–—-]*PART\s+(?:II|11|2)(?=\b|SHORT)|'
                      r'^\s*SECTION\s+A[:\s]*SHORT[\s\-–—]*ANSWERS?\b|'
                      r'^\s*PART\s+(?:II|11|2)(?=\b|SHORT)[:\s]*SHORT[\s\-–—]*ANSWERS?', re.I)
RE_SECB = re.compile(r'^\s*SECTION\s+B\b|^\s*SECTION\s+A[:\s]+ATTEMPT\s+ANY\s+FOUR', re.I)
# The header introducing the printed MCQ/SAQ answer key varies a lot across
# diets — "MULTIPLE CHOICE QUESTIONS", "MULTIPLE – CHOICE QUESTION", "MCQ –
# SOLUTION", "SOLUTION TO MULTIPLE CHOICE QUESTIONS (MCQ)", "SOLUTIONS - MCQ",
# "SOLUTION TO SAQ", "SHORT-ANSWER SOLUTIONS", etc. Matching is therefore a
# search for the *combination* of words anywhere on the line, not an anchored
# exact heading, and callers use .search() rather than .match().
RE_MCSOL = re.compile(r'MU(?:L)?TI(?:PLE|PLIE)?[\s\-–—:()]*CHOICE|MCQ[\s\-–—:()]*'
                      r'SOLUTIONS?|SOLUTIONS?[\s\-–—:()]*(?:TO\s*)?MCQ|'
                      r'^\s*MCQ\s*[:\-–—]?\s*$', re.I)
RE_SASOL = re.compile(r'SHORT[\s\-–—]*ANSWERS?|SAQ[\s\-–—:()]*SOLUTIONS?|'
                      r'SOLUTIONS?[\s\-–—:()]*(?:TO\s*)?SAQ|'
                      r'^\s*SAQ\s*[:\-–—]?\s*$|'
                      # one diet labels this "SECTION A: PART II ANSWER", with
                      # no "SHORT" at all — safe only in this exact combination.
                      r'PART\s+(?:II|11|2)(?=\b|SHORT)[:\s]*ANSWER\b', re.I)
RE_WORK  = re.compile(r'^\s*WORKINGS?\b', re.I)
# "SOLUTION 1", "SOLUTION TO QUESTION 1" and (one diet) "SOLUTION TO QUESTION
# ONE" all mark a Section B answer; Section B never runs past six questions,
# so a spelled-out word is only ever one of these.
RE_BSOL  = re.compile(r'^\s*SOLUTION\s*(?:TO\s*)?(?:QUESTION\s*)?'
                      r'(\d+|ONE|TWO|THREE|FOUR|FIVE|SIX)\s*[A-Za-z]?\s*$', re.I)
NUM_WORD = {'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6}


def bsol_num(m):
    g = m.group(1).upper()
    return NUM_WORD.get(g) or int(g)
RE_EXAM  = re.compile(r"^\s*EXAMIN(?:ER|E['’‘‟]R)S?\s*['’‘‟]?\s*S?\s+(COMMENT|REPORT)", re.I)

RE_QNUM_P = re.compile(r'^\s{0,14}(\d{1,2})[.)]\s*(.*)$')
RE_QNUM_B = re.compile(r'^\s{0,14}(\d{1,2})\s{2,24}([^\s\d].*)$')

class _QNum:
    """A question number is `7.` / `7)` / a bare `7` followed by prose."""
    @staticmethod
    def match(line):
        return RE_QNUM_P.match(line) or RE_QNUM_B.match(line)

RE_QNUM = _QNum

# A few diets number the short-answer questions (only ever up to 20) with
# lower-case roman numerals — "i.", "ii.", … "xx." — instead of arabic
# digits; parse_numbered() tries this once the arabic match fails.
_ROMANS = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',
           'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx']
ROMAN_VAL = {w: i + 1 for i, w in enumerate(_ROMANS)}
RE_QNUM_ROMAN = re.compile(
    r'^\s{0,14}(' + '|'.join(sorted(_ROMANS, key=len, reverse=True)) +
    r')[.)]\s*(.*)$', re.I)
RE_OPT = re.compile(r'^\s{0,24}([A-Ja-e])(?:[.,)]\s*|\s{2,})(\S.*)?$')
RE_PRE   = re.compile(r'^\s*Use\s+the\s+(following|data|table|information|Euler)', re.I)
RE_PRE_RANGE = re.compile(r'questions?\s+(.+)', re.I)
RE_KEY   = re.compile(r'^\s*(\d{1,2})[.)]?\s*([A-E])[.)]?\s*$')


TABULAR = re.compile(r'\S {3,}\S')

def is_tabular(lines):
    """A wide internal gap means pdftotext preserved a column layout."""
    return any(TABULAR.search(l) for l in lines)


# A stray page number occasionally lands on the same line as the next
# question, immediately before its real number, when pdftotext -layout
# collapses a two-column page footer into the body text — e.g. "4.   2.
# Which of the following...". Genuine prose never opens with two separate
# "N." tokens back to back, so stripping the first is safe.
RE_STRAY_NUM = re.compile(r'^\s*\d{1,2}[.)]\s+(?=\d{1,2}[.)]\s)')


def pdf_lines(path, with_pages=False):
    txt = subprocess.run(['pdftotext', '-layout', str(path), '-'],
                         capture_output=True, text=True, check=True).stdout
    lines, page_numbers = [], []
    for page_number, page in enumerate(txt.split('\f'), 1):
        page_lines = page.split('\n')
        nonempty = [i for i, line in enumerate(page_lines) if line.strip()]
        # Remove a bare page number only at the actual PDF page footer.
        # The old global furniture rule also deleted legitimate stand-alone
        # figures (including zeroes) from questions and official workings.
        tail = [i for i in nonempty if not any(pattern.match(page_lines[i]) for pattern in FURNITURE)]
        if tail and re.fullmatch(r'\s*\d{1,3}\s*', page_lines[tail[-1]]):
            value = int(page_lines[tail[-1]])
            if 0 <= page_number - value <= 10:
                page_lines[tail[-1]] = ''
        lines.extend(RE_STRAY_NUM.sub('', line) for line in page_lines)
        page_numbers.extend([page_number] * len(page_lines))
    return (lines, page_numbers) if with_pages else lines


def find(lines, rx, start=0, end=None):
    end = len(lines) if end is None else end
    for i in range(start, end):
        if rx.search(lines[i]):
            return i
    return -1


def split_papers(lines):
    """Locate each subject's paper by its 'PART II EXAMINATIONS' banner."""
    heads = [i for i, l in enumerate(lines) if RE_PAPERHEAD.search(l)]
    # March 2021 CA omits its exam banner. Its title + time + question
    # banner identify the same start without mistaking a contents entry.
    for i, line in enumerate(lines):
        if (any(name in line.upper() for _, name in SUBJECTS)
                and re.search(r'Time Allowed', ' '.join(lines[i+1:i+4]), re.I)
                and any(RE_SECA1.search(l) for l in lines[i+1:i+7])
                and not any(0 <= i-h <= 6 for h in heads)):
            heads.append(i-1)
    heads.sort()
    out = []
    for i, h in enumerate(heads):
        title = ''
        for l in lines[h + 1:h + 6]:
            t = l.strip()
            if t and not re.match(r'^\(?PART', t, re.I) and 'Time Allowed' not in t:
                title = t
                break
        code = None
        for c, name in SUBJECTS:
            # older diets title the FA paper "PRINCIPLES [AND/&] PRACTICE OF
            # FINANCIAL ACCOUNTING"; match the subject name anywhere in the
            # title, not just as a prefix, so both eras are found.
            if name in title.upper():
                code = c
        if code is None:
            continue
        end = heads[i + 1] if i + 1 < len(heads) else len(lines)
        out.append((code, h, end))
    return out


# ── question parsing ──────────────────────────────────────────────────────
def _finish(part):
    """A stem or option becomes prose, or keeps its lines when it is a table."""
    lines = squeeze(part)
    if not lines:
        return {'t': ''}
    if is_tabular(lines):
        return {'t': tidy(' '.join(lines[:1])),
                'pre': [money(desymbol(l)) for l in lines]}
    return {'t': money(tidy(' '.join(l.strip() for l in lines if l.strip())))}


def pre_range_end(pre_lines):
    """The last question number a "Use the following ... to answer questions
    9 to 12" preamble applies to — the max of every integer following the
    word "question(s)" in it, which survives every phrasing seen in these
    papers ("9 to 12", "9 & 10", "13" alone, "4, 5 and 6", "16 – 19", ...).
    None if the preamble does not name a range at all (rare; those keep the
    old unbounded behaviour rather than being dropped outright). Only the
    preamble's own first line is examined — the range is always stated
    there ("...to answer questions 9 to 12") — never the scenario text
    that follows on later lines, which is often full of unrelated numbers
    (amounts, years) that would otherwise be mistaken for question numbers."""
    if not pre_lines:
        return None
    m = RE_PRE_RANGE.search(pre_lines[0])
    if not m:
        return None
    nums = [int(x) for x in re.findall(r'\d+', m.group(1))]
    return max(nums) if nums else None


def parse_mcq(block):
    """Numbered stems with A-E options; a shared preamble carries onto its
    group — but only for the range of question numbers it actually names.
    Without this a preamble like "Use the following information to answer
    questions 9 to 12" would keep attaching to every question from 13
    onward until (if ever) the next "Use the following..." line appears,
    silently mixing an unrelated scenario's vocabulary into every question
    in between — confirmed happening live (a Public Procurement question
    was carrying a pensions preamble meant only for questions 9-12)."""
    qs, cur, pre, pending = [], None, [], []
    pre_end = None
    expect = 1

    def close():
        """Materialise the open question's raw buffers."""
        if not cur:
            return
        cur['stem'] = _finish(cur['_stem'])
        cur['options'] = [_finish(o) for o in cur['_opts']]
        del cur['_stem'], cur['_opts']

    def flush():
        nonlocal cur
        if cur:
            close()
            if len(cur['options']) >= 2:
                qs.append(cur)
        cur = None

    for raw in block:
        line = raw.rstrip()
        if not line.strip():
            if cur and cur['_opts']:
                cur['_opts'][-1].append('')
            elif cur:
                cur['_stem'].append('')
            elif pending:
                pending.append('')
            continue

        mq = RE_QNUM.match(line)
        if mq and int(mq.group(1)) == expect:
            flush()
            if pending:
                pre = squeeze(pending)
                pending = []
                pre_end = pre_range_end(pre)
            if pre_end is not None and expect > pre_end:
                pre, pre_end = [], None
            cur = {'n': expect, '_stem': [mq.group(2)], '_opts': [], 'pre': pre}
            expect += 1
            continue

        if RE_PRE.match(line):
            flush()
            pre, pre_end = [], None
            pending = [line.strip()]
            continue

        mo = RE_OPT.match(line)
        if cur and mo and ord(mo.group(1).upper()) == ord(cur.get('optionStart', 'A')) + len(cur['_opts']):
            cur['_opts'].append([mo.group(2) or ''])
            continue

        if cur and cur['_opts']:
            cur['_opts'][-1].append(raw.rstrip())
        elif cur:
            cur['_stem'].append(raw.rstrip())
        elif pending:
            pending.append(raw.rstrip())
    flush()
    return qs


def parse_numbered(block, limit=40, expect=1):
    """Short-answer questions or their solutions: numbered prose, table-tolerant.

    A shared preamble stays attached for exactly the range of question
    numbers it names (see pre_range_end / parse_mcq above) — not just the
    single question right after it (which would leave the rest of the
    range with no shared data at all) and not forever (which would smear
    it onto every later question until, if ever, a new preamble appears).

    Once the first item has matched arabic or roman numbering, that choice
    is locked in for the rest of the block. Without this, a multi-part
    answer's own "i. / ii. / iii. ..." sub-bullets are indistinguishable
    from top-level roman question numbers whenever a sub-bullet's roman
    value happens to coincide with the next expected arabic question
    number — e.g. an arabic item 3's third sub-bullet "iii." is read as a
    new roman-numbered item 3, silently shredding that item's own answer
    across the two neighbouring items and shifting everything after it by
    one. Confirmed live on FA 2024-03's short-answer key (items 2-5)."""
    items, cur, pre, pending = [], None, [], []
    pre_end = None
    scheme = None  # locked to 'arabic' or 'roman' once item 1 is found
    for raw in block:
        line = raw.rstrip()
        if not line.strip():
            if cur:
                cur['body'].append('')
            elif pending:
                pending.append('')
            continue

        m = RE_QNUM.match(line) if scheme != 'roman' else None
        if m and int(m.group(1)) == expect and expect <= limit:
            scheme = 'arabic'
            if cur:
                items.append(cur)
            if pending:
                pre = squeeze(pending)
                pending = []
                pre_end = pre_range_end(pre)
            if pre_end is not None and expect > pre_end:
                pre, pre_end = [], None
            cur = {'n': expect, 'body': [tidy(m.group(2))], 'pre': pre}
            expect += 1
            continue

        mr = RE_QNUM_ROMAN.match(line) if scheme != 'arabic' else None
        if mr and ROMAN_VAL.get(mr.group(1).lower()) == expect and expect <= limit:
            scheme = 'roman'
            if cur:
                items.append(cur)
            if pending:
                pre = squeeze(pending)
                pending = []
                pre_end = pre_range_end(pre)
            if pre_end is not None and expect > pre_end:
                pre, pre_end = [], None
            cur = {'n': expect, 'body': [tidy(mr.group(2))], 'pre': pre}
            expect += 1
            continue

        if RE_PRE.match(line):
            if cur:
                items.append(cur)
                cur = None
            pre, pre_end = [], None
            pending = [line.strip()]
            continue

        if cur:
            cur['body'].append(raw.rstrip())
        elif pending:
            pending.append(raw.rstrip())
    if cur:
        items.append(cur)
    for it in items:
        it['body'] = squeeze(it['body'])
    return items


def parse_key(block):
    """Preserve multiple accepted answers and official bonus awards."""
    key = {}
    rx = re.compile(r'(?:^|\s)(\d{1,2})(?:[.)]|\s+)\s*'
                    r'(Bonus\b|[A-E](?:\s*[/&]\s*[A-E])*)(?=[\s.)]|$)', re.I)
    for line in block:
        for m in rx.finditer(line):
            number = int(m[1])
            if 1 <= number <= 30 and number not in key:
                key[number] = re.sub(r'\s+', '', m[2]).upper()
    return key


def parse_paper(lines, code, diet):
    n = len(lines)
    i_a1 = find(lines, RE_SECA1)
    i_a2 = find(lines, RE_SECA2, i_a1 + 1)
    i_b = find(lines, RE_SECB, i_a2 + 1)
    # Locate solution keys before finding essay solutions. Some diets use
    # QUESTION 1 rather than SOLUTION 1 for answers as well as questions.
    i_mc = next((i for i in range(i_b + 1, n)
                 if RE_MCSOL.search(lines[i]) or
                 re.match(r'^\s*(?:SUGGESTED\s+)?SOLUTIONS?\s*$', lines[i], re.I)), -1)
    i_sa = next((i for i in range(i_mc + 1, n)
                 if RE_SASOL.search(lines[i]) or RE_SECA2.search(lines[i])), -1)
    if min(i_a1, i_a2, i_b, i_mc, i_sa) < 0:
        raise ValueError(f'{diet}/{code}: missing section boundary '
                         f'{(i_a1, i_a2, i_b, i_mc, i_sa)}')

    essay_heading = re.compile(r'^\s*(?:SOLUTION\s*(?:TO\s*)?(?:QUESTION\s*)?|QUESTION\s+)'
                               r'(\d+|ONE|TWO|THREE|FOUR|FIVE|SIX)\s*[A-Za-z]?\s*$', re.I)
    # MCQ/SAQ workings may themselves be headed 'Question 3' etc.
    # Prefer the explicit first essay solution; only use QUESTION 1 when
    # that is genuinely how the pack labels its entire solution set.
    first = next((i for i in range(i_sa+1, n)
                  if (m := RE_BSOL.match(lines[i])) and bsol_num(m) == 1), None)
    if first is None:
        first = next((i for i in range(i_sa+1, n)
                      if re.match(r'^\s*(?:QUESTION\s+1|Solution)\s*$', lines[i], re.I)), n)
    raw_sols = []
    unnumbered = 0
    for i in range(first, n):
        m = essay_heading.match(lines[i])
        if m:
            raw_sols.append((bsol_num(m), i))
        elif re.match(r'^\s*Solution\s*$', lines[i], re.I):
            unnumbered += 1
            raw_sols.append((unnumbered, i))
    sols, last, sols_end = [], 0, n
    for number, i in raw_sols:
        if number < last:
            sols_end = i
            break
        sols.append((number, i))
        last = number
    if not sols:
        raise ValueError(f'{diet}/{code}: no Section B solutions')
    sol_start = sols[0][1]

    def seg(a, b):
        return strip_furniture(lines[a+1:b])

    mcq_lines = seg(i_a1, i_a2)
    # Verified printed defect, March 2020 Management PDF pp74-80: the
    # first 29 stems are numbered 16..44 and the first four use F..J.
    # Keep those labels as metadata; internal ordinals follow its 1..30 key.
    printed_numbers, printed_labels = {}, set()
    if (diet, code) == ('2020-03', 'MAN'):
        ordinal = 0
        for i, line in enumerate(mcq_lines):
            m = RE_QNUM.match(line)
            if m:
                ordinal += 1
                printed_numbers[ordinal] = int(m[1])
                mcq_lines[i] = re.sub(r'^(\s*)\d+[.)]', lambda m: m[1]+str(ordinal)+'.', line, count=1)
            if ordinal:
                mo = re.match(r'^(\s*)([F-J])[.)](.*)$', mcq_lines[i])
                if mo:
                    printed_labels.add(ordinal)
                    mcq_lines[i] = mo[1] + chr(ord(mo[2])-5) + '.' + mo[3]
    mcq = parse_mcq(mcq_lines)
    for q in mcq:
        if q['n'] in printed_numbers:
            q['printedN'] = printed_numbers[q['n']]
            if q['n'] in printed_labels:
                q['printedOptionLabels'] = 'FGHIJ'
    saq = parse_numbered(seg(i_a2, i_b), limit=20)
    secb_q = squeeze(seg(i_b, i_mc))
    reference_tables = []
    if code == 'TAX':
        reference_at = next((i for i, line in enumerate(secb_q)
                             if re.fullmatch(r'\s*NIGERIAN\s+TAX\s+RATES\s*', line, re.I)), None)
        if reference_at is not None:
            # These are exam-wide supplied tables, not part of Question 6.
            # Retain every rate/allowance but keep the appendix out of the
            # question's retrieval evidence and scheme-change flags.
            reference_tables = squeeze(secb_q[reference_at:])
            secb_q = squeeze(secb_q[:reference_at])
            while reference_tables and re.match(r'^\s*SECTION\s+A\b', reference_tables[-1], re.I):
                reference_tables.pop()

    def key_region(a, b):
        block = seg(a, b)
        examiner_at = find(block, RE_EXAM)
        examiner = squeeze(block[examiner_at+1:]) if examiner_at >= 0 else []
        if examiner_at >= 0:
            block = block[:examiner_at]
        workings_at = find(block, RE_WORK)
        workings = squeeze(block[workings_at+1:]) if workings_at >= 0 else []
        if workings_at >= 0:
            block = block[:workings_at]
        return block, workings, examiner

    mc_block, mc_work, mc_note = key_region(i_mc, i_sa)
    sa_block, sa_work, sa_note = key_region(i_sa, sol_start)
    key = parse_key(mc_block)
    sa_sol = parse_numbered(sa_block, limit=20)
    for answer in sa_sol:
        recovery = SAQ_RECOVERIES.get((diet, code, answer['n']))
        if recovery:
            if ''.join(answer['body']).strip():
                raise ValueError(f'{diet}/{code}: source recovery would overwrite text')
            answer['body'] = recovery[:]
            answer['recoveredFromImage'] = True
    secb = []
    for j, (number, at) in enumerate(sols):
        stop = sols[j+1][1] if j+1 < len(sols) else sols_end
        body = squeeze(strip_furniture(lines[at+1:stop]))
        # A pack's next subject cover/instructions must never be appended
        # to the preceding paper's final examiner comment.
        cutoff = next((i for i, line in enumerate(body)
                       if re.search(r'EXAMINATIONS?\s*\(PART\s+III\)|'
                                    r'ASSOCIATION OF ACCOUNTANCY|ACCOUNTING TECHNICIANS SCHEME', line, re.I)), len(body))
        body = squeeze(body[:cutoff])
        e = find(body, RE_EXAM)
        comment = squeeze(body[e+1:]) if e >= 0 else []
        if e >= 0:
            body = squeeze(body[:e])
        if secb and secb[-1]['n'] == number:
            secb[-1]['solution'].extend(body)
            secb[-1]['examiner'].extend(comment)
        else:
            secb.append({'n': number, 'solution': body, 'examiner': comment})
    return {
        'diet': diet, 'subject': code,
        'mcq': mcq, 'mcq_key': key, 'mcq_workings': mc_work, 'mcq_examiner': mc_note,
        'saq': saq, 'saq_solutions': sa_sol, 'saq_workings': sa_work,
        'saq_examiner': sa_note, 'secb_paper': secb_q, 'secb_solutions': secb,
        'referenceTables': reference_tables,
        '_sourceRanges': {'mcq': (i_a1+1, i_a2), 'saq': (i_a2+1, i_b), 'secb': (i_b+1, i_mc)},
    }


def main():
    from build_exams import split_secb
    papers = []
    copies = OUT.parent / 'assets' / 'papers'
    copies.mkdir(parents=True, exist_ok=True)
    for dcode, dname, fname in DIETS:
        pdf = PQ / fname
        lines, page_numbers = pdf_lines(pdf, with_pages=True)
        shutil.copy2(pdf, copies / f'{dcode}.pdf')
        sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
        for code, a, b in split_papers(lines):
            p = parse_paper(lines[a:b], code, dcode)
            source_ranges = p.pop('_sourceRanges')
            p['dietName'] = dname
            actual_pages = sorted(set(page_numbers[i] for i in range(a, b) if lines[i].strip()))
            p['source'] = {'src': f'assets/papers/{dcode}.pdf', 'filename': fname,
                           'startPage': min(actual_pages), 'endPage': max(actual_pages), 'sha256': sha}
            by_page = {}
            for i in range(a, b):
                by_page.setdefault(page_numbers[i], []).append(lines[i])

            def normal(text):
                return re.sub(r'\W+', ' ', money(tidy(desymbol(text))).lower()).strip()

            page_text = {number: normal(' '.join(text)) for number, text in by_page.items()}

            def locate(text, kind=None, ordinal=None):
                searched = page_text
                if kind:
                    start, end = source_ranges[kind]
                    selected = {}
                    for i in range(a+start, a+end):
                        selected.setdefault(page_numbers[i], []).append(lines[i])
                    searched = {number: ' ' + normal(' '.join(text)) + ' ' for number, text in selected.items()}
                words = normal(text).split()
                for length in (24, 16, 10):
                    prefix = ' '.join(words[:length])
                    if len(prefix) < (6 if kind else 15):
                        continue
                    variants = ([' ' + str(ordinal) + ' ' + prefix + ' '] if ordinal else []) + [prefix]
                    for variant in variants:
                        found = [number for number, text in searched.items() if variant in text]
                        if len(found) == 1:
                            return found[0]
                return None

            for question in p['mcq']:
                question['sourcePage'] = locate(question['stem']['t'], 'mcq', question.get('printedN') or question['n'])
            for question in p['saq']:
                question['sourcePage'] = locate(' '.join(question['body']), 'saq', question['n'])
            essay_questions = split_secb(p['secb_paper'])
            for question in p['secb_solutions']:
                question['sourcePage'] = locate(' '.join(essay_questions.get(question['n'], [])), 'secb')
                question['solutionPage'] = locate(' '.join(question['solution']))
            papers.append(p)
            print(f'{dcode} {code}: {len(p["mcq"])} mcq '
                  f'(key {len(p["mcq_key"])}), {len(p["saq"])} saq '
                  f'(sol {len(p["saq_solutions"])}), {len(p["secb_solutions"])} section-B solutions')
    # decode Symbol-font glyphs and naira signs everywhere a raw line survived
    def clean(node):
        if isinstance(node, str):
            return money(desymbol(node))
        if isinstance(node, list):
            return [clean(v) for v in node]
        if isinstance(node, dict):
            return {k: clean(v) for k, v in node.items()}
        return node
    papers = clean(papers)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'papers.json').write_text(json.dumps(papers, ensure_ascii=False, indent=1))
    print(f'\nwrote {OUT/"papers.json"}  ({(OUT/"papers.json").stat().st_size//1024} KB)')


if __name__ == '__main__':
    main()
