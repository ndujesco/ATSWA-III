"""Phrase evidence shared by chapter and section retrieval.

Whole phrases retain distinctions bag-of-words loses (production budget vs
materials budget, audit evidence vs audit report). Gates are unchanged.
"""
import re

PHRASES = {
    'AUD': {
        1: 'audire; expectation gap; attributes of auditing; objectives of an audit; reasonable assurance; absolute assurance',
        2: 'appointment of auditors; removal of auditors; resignation of auditors; remuneration of auditors; audit committee; rights of auditors',
        3: 'professional ethics; ethical principle; professional misconduct; threat to independence; self interest; self review; professional independence',
        4: 'auditor liability; auditors liability; duty of care; professional negligence; caparo; hedley byrne',
        5: 'audit planning; working paper; audit documentation; audit risk; inherent risk; detection risk; audit planning memorandum; permanent file; current file',
        6: 'audit evidence; external confirmation; representation letter; third party evidence; management representation; peer review',
        7: 'audit sampling; analytical procedure; substantive procedure; substantive test; tolerable error; systematic sampling; asset register; sampling risk',
        8: 'internal control; internal check; segregation of duties; control environment; control questionnaire',
        9: 'auditor general; public accounts committee; public procurement; due process; public sector; financial regulations',
        10: 'computer assisted; audit software; test data; information technology; computer files; it systems; idea; caats',
        11: 'audit qualification; qualified opinion; qualified report; adverse opinion; disclaimer of opinion; unmodified opinion; audit report; true and fair view',
        12: 'audit completion; completion checklist; final review; management letter; completion of field work',
    },
    'CA': {
        1: 'cost accounting report; cost information; qualities of a good cost; objectives of cost accounting; cost object; cost objective',
        2: 'cost classification; high low; variable cost per unit; cost codification; cost centre; cost unit; semi variable',
        3: 'economic order quantity; inventory valuation; first in first out; last in first out; reorder level; stock level; materials control; stock turnover',
        4: 'labour turnover; labour remuneration; idle time; overtime premium; halsey; rowan; piece rate; job evaluation',
        5: 'overhead absorption; overhead apportionment; service department; machine hour rate; under absorbed; over absorbed; classification of overhead',
        6: 'integrated account; interlocking account; cost ledger; financial accounts; reconciliation statement; reconciliation of profit',
        7: 'job costing; batch costing; contract costing; service costing; operating costing; work certified',
        8: 'process costing; joint product; by product; equivalent unit; abnormal loss; normal loss; abnormal gain',
        9: 'marginal costing; absorption costing; make or buy; limiting factor; relevant cost; sunk cost; opportunity cost',
        10: 'break even; breakeven; margin of safety; target profit; cost volume profit; contribution ratio',
        11: 'net present value; payback period; investment appraisal; accounting rate of return; internal rate of return; discounted cash flow',
        12: 'production budget; materials purchase budget; sales budget; cash budget; budgetary control; flexible budget; budget centre; zero based budgeting; master budget',
        13: 'standard costing; material price variance; material usage variance; labour efficiency variance; labour rate variance; sales margin variance',
        14: 'just in time; backflush; life cycle costing; target costing; throughput; total quality management; activity based costing; advanced manufacturing',
        15: 'cost reduction; cost control; value analysis; value engineering; method study; work study; cost audit',
    },
    'TAX': {
        1: 'tax evasion; tax avoidance; principles of taxation; good tax system; tax yield; tax rate; direct tax; indirect tax; tax base',
        2: 'relevant tax authority; composition of the board; joint tax board; federal inland revenue service board; state board; local government revenue committee',
        3: 'ethical principle; conflict of interest; professional ethics; confidentiality; professional competence',
        4: 'tax return; filing of returns; tax identification number; tax id; best of judgement; additional assessment; self assessment; notice of assessment',
        5: 'notice of objection; tax appeal tribunal; notice of refusal; advance ruling; tax ombud',
        6: 'tax clearance certificate; contents of a tax clearance; issuance of tax clearance',
        7: 'value added tax; input vat; output vat; input tax; output tax; vat return; taxable supply',
        8: 'stamp duty; stamp duties; methods of stamping; adhesive stamp; ad valorem; adjudication',
        9: 'withholding tax; withholding taxes; deduction at source; final tax; withholding credit',
        10: 'customs duty; customs duties; excise duty; excise duties; import duty; export duty; customs service',
        11: 'fossil fuel; surcharge on fuel',
        12: 'benefit in kind; benefits in kind; official quarters; employment income; contract of service; pay as you earn; leave passage',
        13: 'consolidated relief; personal income tax; taxable income; rent relief; dependent relative; life assurance premium',
        14: 'unearned income; investment income; rental income; rental expense; franked investment; dividend income',
        15: 'badges of trade; sole trader; self employed; commencement rule; cessation rule; basis period',
        16: 'capital allowance; capital allowances; qualifying capital expenditure; balancing allowance; balancing charge; investment allowance; written down value',
        17: 'partnership profit; partnership agreement; divisible profit; partner salary; partners salary',
        18: 'settlement trust; trusts and estates; trustee; settlor; estate income; beneficiary',
        19: 'loss relief; carry forward loss; losses carried forward; current year loss',
        20: 'allowable expense; disallowable expense; adjusted profit; assessable profit; medium sized company; small company; large company',
        21: 'minimum tax; total profit; dividend basis; turnover basis; assessment on turnover; companies income tax liability; excess dividend',
        22: 'pioneer company; pioneer status; pioneer relief; export processing zone; petroleum profit; insurance company; agricultural production; shipping company; non resident company',
        23: 'education tax; tertiary education; development levy; police trust fund; information technology development levy; nitda; naseni',
        24: 'capital gain; capital gains; chargeable gain; chargeable gains; loss of office; roll over relief; rollover relief',
        25: 'taxpro max; rev360; technologies disrupting tax; technology in taxation; electronic filing',
    },
    'MAN': {
        1: 'business environment; objective of business; objectives of a business; corporate governance; corporate social responsibility; business ownership; sole proprietorship; manufacturing industries; general partner',
        2: 'scientific management; administrative theory; management theory; human relations; managerial role; managerial skill; levels of management; principles of management; bureaucracy',
        3: 'decision making; programmed decision; strategic management; planning process; importance of planning; effective planning; span of control; delegation of authority; functional department; organisation structure; organisational structure; type of control',
        4: 'human resource; job evaluation; job analysis; job specification; job description; employee development; staff development; recruitment; selection process; consumer goods; marketing mix; product life cycle; capital market; money market',
        5: 'motivation theory; leadership style; communication barrier; group norm; team building; emotional intelligence; conflict resolution; resistance to change; maslow; herzberg',
        6: 'business process reengineering; business process re engineering; bpr; process redesign',
        7: 'organisational effectiveness; organizational effectiveness; organisational efficiency',
        8: 'office layout; office machine; office practice; filing system; health and safety; hazard; protective measure; risk assessment; office form; facsimile; fax machine',
        9: 'mentoring; coaching; outsourcing; knowledge management; talent management; succession planning; workforce diversity',
        10: 'entrepreneur; entrepreneurship; intrapreneur; venture capital',
    },
}


def norm(text):
    text = re.sub(r'[^a-z ]', ' ', text.lower())
    words = []
    for word in text.split():
        for suffix in ('ies', 'ing', 'ers', 'es', 's'):
            if word.endswith(suffix) and len(word) - len(suffix) >= 4:
                word = word[:-len(suffix)] + ('y' if suffix == 'ies' else '')
                break
        words.append(word)
    return ' ' + ' '.join(words) + ' '


def phrase_boost(scores, code, query):
    query = norm(query)
    top = max(scores.values(), default=0)
    for chapter, phrases in PHRASES.get(code, {}).items():
        hits = sum(norm(phrase) in query for phrase in phrases.split('; '))
        if hits and chapter in scores:
            scores[chapter] += top * 0.85 * hits


def answer_boost(scores, answer, texts):
    """Use a distinctive answer phrase only when ONE target contains it.

    Callers exclude negative questions: their answer is the distractor that
    should be absent. One-word/numeric answers never create evidence here.
    """
    phrase = norm(answer)
    words = phrase.split()
    if not 2 <= len(words) <= 6 or len(phrase) < 12:
        return
    matches = [target for target, text in texts.items() if phrase in text]
    if len(matches) == 1:
        target = matches[0]
        scores[target] += max(scores.values(), default=0) * 0.65


def heading_phrases(headings):
    """Index specific multiword phrases appearing in exactly one heading."""
    generic = {'the', 'and', 'for', 'with', 'from', 'into', 'this', 'that',
               'what', 'how', 'are', 'type', 'typ', 'definition', 'introduction'}
    owners = {}
    for section, title in headings.items():
        words = norm(title).split()
        for width in range(2, min(6, len(words)) + 1):
            for start in range(len(words) - width + 1):
                part = words[start:start+width]
                if len({w for w in part if len(w) > 2 and w not in generic}) < 2:
                    continue
                phrase = ' ' + ' '.join(part) + ' '
                owners.setdefault(phrase, set()).add(section)
    return {phrase: next(iter(sections)) for phrase, sections in owners.items()
            if len(sections) == 1}


def heading_boost(scores, query, phrases):
    query = norm(query)
    hits = set(section for phrase, section in phrases.items() if phrase in query)
    top = max(scores.values(), default=0)
    for section in hits:
        scores[section] += top * 0.65
