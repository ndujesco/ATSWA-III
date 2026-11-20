#!/usr/bin/env python3
"""Fail on missing questions/answers, stale citations or lost revision sources.

This is a structural/content-integrity audit, not a claim that every printed
answer or legal computation has been independently recomputed.
"""
import hashlib
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path

from build_exams import split_secb, CH_CONF_MIN
from source_recoveries import FIGURE_PAGES
from corrections import KEY_CORRECTIONS, SAQ_CORRECTIONS, PIN, SEC_PIN

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SUBJECTS = {'AUD': 12, 'CA': 15, 'TAX': 25, 'MAN': 10}


def payload(name, key):
    text = (DATA / f'{name}.js').read_text()
    match = re.fullmatch(r'ATSWA\.put\("' + key + r'",\s*(.*)\);\s*', text, re.S)
    assert match, f'{name}: invalid data wrapper'
    return json.loads(match[1])


def run(papers=None, published=True):
    papers = papers if papers is not None else json.loads((DATA / 'papers.json').read_text())
    diets = {re.search(r'(\d{4}-\d{2})', p.name)[1]
             for p in (ROOT.parent / 'materials/past-questions').glob('*.pdf')}
    assert len(diets) == 15, f'Update the audited inventory before adding diets: {len(diets)}'
    assert len(papers) == 60
    assert {(p['diet'], p['subject']) for p in papers} == {
        (diet, code) for diet in diets for code in SUBJECTS}
    totals, source_keys = Counter(), set()
    chapters = {}
    for code, count in SUBJECTS.items():
        chapters[code] = {}
        for number in range(1, count+1):
            path = ROOT / 'content' / code.lower() / f'ch{number:02d}.py'
            spec = importlib.util.spec_from_file_location(f'audit_{code}_{number}', path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sections = [str(section['n']) for section in module.CH['secs']]
            assert len(sections) == len(set(sections)), f'{code}/{number}: duplicate section IDs'
            chapters[code][number] = set(sections)

    for paper in papers:
        prefix = paper['diet'] + '/' + paper['subject']
        assert set(paper['mcq_key']) == {str(i) for i in range(1, 31)}, prefix + ': key incomplete'
        for kind, field, expected in [('mcq', 'mcq', 30), ('saq', 'saq', 20),
                                      ('secb', 'secb_solutions', 6)]:
            questions = paper[field]
            assert [q['n'] for q in questions] == list(range(1, expected+1)), prefix + '/' + kind
            totals[kind] += len(questions)
            for q in questions:
                source_keys.add(f"{prefix}/{kind}/{q['n']}")
                if q.get('sec'):
                    assert str(q['sec']) in chapters[paper['subject']][q['ch']], f'{prefix}: stale section {q}'
                pre = q.get('pre') or []
                if pre:
                    header = ' '.join(pre[:2])
                    match = re.search(r'questions?\s+([\d\s,&–—toand.]+)', header, re.I)
                    assert match, f'{prefix}/{kind}/{q["n"]}: shared range not understood'
                    numbers = [int(n) for n in re.findall(r'\d+', match[1])]
                    assert numbers and min(numbers) <= q['n'] <= max(numbers), f'{prefix}: leaking shared preamble'
        for q in paper['mcq']:
            want = 4 if (prefix, q['n']) == ('2024-03/TAX', 25) else 5
            assert len(q['options']) == want, f'{prefix}/mcq/{q["n"]}: options'
            assert q['stem']['t'].strip()
            key = paper['mcq_key'][str(q['n'])]
            assert key == 'BONUS' or all(len(k) == 1 and k in 'ABCDE'[:want] for k in key.split('/')), (prefix, key)
            for option in q['options']:
                assert option['t'].strip() or option.get('pre'), (prefix, q['n'], 'empty option')
        assert [q['n'] for q in paper['saq_solutions']] == list(range(1, 21)), prefix + ': short key'
        assert all(''.join(q['body']).strip() for q in paper['saq_solutions']), prefix + ': blank answer'
        essay_questions = split_secb(paper['secb_paper'])
        assert set(essay_questions) == set(range(1, 7)), prefix + ': Section B paper split'
        for q in paper['secb_solutions']:
            assert len(' '.join(q['solution']).strip()) > 20, prefix + ': empty essay solution'
            assert len(' '.join(essay_questions[q['n']]).strip()) > 20, prefix + ': empty essay question'
    assert totals == {'mcq': 1800, 'saq': 1200, 'secb': 360}, totals
    if not published:
        return dict(totals)

    exams = payload('exams', 'EXAMS')
    revision = payload('revision', 'REVISION')
    published_keys, citation_counts = set(), {}
    source_pdfs, question_pages, reference_tables, reading_links = set(), 0, 0, 0
    for paper in exams['papers']:
        code = paper['subject']
        counts = citation_counts.setdefault(code, Counter())
        raw = next(p for p in papers if (p['diet'], p['subject']) == (paper['diet'], code))
        source = paper['source']
        source_file = ROOT / source['src']
        assert source_file.is_file() and source_file.read_bytes().startswith(b'%PDF-'), source
        assert hashlib.sha256(source_file.read_bytes()).hexdigest() == source['sha256'], 'Original PDF changed'
        assert source['sha256'] == hashlib.sha256((ROOT.parent / 'materials/past-questions' / source['filename']).read_bytes()).hexdigest()
        source_pdfs.add(source['src'])
        assert paper['referenceTables'] == raw.get('referenceTables', []), 'Reference appendix changed'
        if code == 'TAX':
            assert paper['referenceTables'], 'Tax reference tables lost'
            reference_tables += 1
            assert 'NIGERIAN TAX RATES' not in '\n'.join(paper['secb'][-1]['q']), 'Reference appendix leaked into question 6'
        for kind in ('mcq', 'saq', 'secb'):
            raw_items = raw['secb_solutions' if kind == 'secb' else kind]
            for q, original in zip(paper[kind], raw_items, strict=True):
                published_keys.add(f"{paper['diet']}/{code}/{kind}/{q['n']}")
                if q.get('sourcePage'):
                    assert source['startPage'] <= q['sourcePage'] <= source['endPage']
                    question_pages += 1
                assert bool(q['ch']) == ((original.get('chConf') or 0) >= CH_CONF_MIN), 'Confidence gate changed'
                assert not q['sec'] or q['ch'], 'Section without chapter'
                if q['sec']:
                    assert str(q['sec']) in chapters[code][q['ch']], (code, q['ch'], q['sec'])
                for reading in q.get('readings', []):
                    assert reading['sec'] in chapters[code][reading['ch']], (code, reading)
                    reading_links += 1
                counts['all'] += 1
                counts['chapter'] += bool(q['ch'])
                counts['section'] += bool(q['sec'])
                for figure in q.get('sourceFigures', []):
                    assert (ROOT / figure['src']).is_file(), figure
                if kind == 'mcq':
                    assert q['stem'] == original['stem'] and q['options'] == original['options'], 'Printed MCQ changed'
                elif kind == 'saq':
                    assert q['body'] == original['body'], 'Printed short question changed'
                    answer = next(s['body'] for s in raw['saq_solutions'] if s['n'] == q['n'])
                    assert q['ans'] == answer, 'Printed short answer overwritten'
                else:
                    assert q['solution'] == original['solution'] and q['examiner'] == original.get('examiner', []), 'Official essay material changed'
    assert published_keys == source_keys, 'Questions lost on publication'
    assert question_pages == 3360, 'A question lost its exact original-PDF page'
    for code, counts in citation_counts.items():
        assert counts['chapter'] == counts['section'] == counts['all'], f'{code}: unresolved question citation'
    assert set(exams['flags']) <= source_keys, 'Flag points at absent question'
    for key, corrected in KEY_CORRECTIONS.items():
        diet, code, kind, number = key
        paper = next(p for p in exams['papers'] if (p['diet'], p['subject']) == (diet, code))
        q = next(q for q in paper['mcq'] if q['n'] == number)
        assert q['studyKey'] == corrected and '/'.join(map(str, key)) in exams['flags']
        assert q['studyKey'] != paper['key'][str(number)], 'Correction lost its original key'
    for key, corrected in SAQ_CORRECTIONS.items():
        paper = next(p for p in exams['papers'] if (p['diet'], p['subject']) == key[:2])
        q = next(q for q in paper['saq'] if q['n'] == key[3])
        assert q['studyAns'] == corrected and q['studyAns'] != q['ans']
    assert all('/'.join(map(str, key)) in source_keys for key in PIN), 'Review points at absent question'
    revision_keys = []
    for code, bank in revision.items():
        for kind in ('mcq', 'saq', 'essay'):
            source_kind = 'secb' if kind == 'essay' else kind
            for q in bank[kind]:
                assert q['freq'] == len(set(q['diets'])), 'Wrong repetition count'
                for source in q['sources']:
                    revision_keys.append(f"{source['diet']}/{code}/{source_kind}/{source['n']}")
                    flag = exams['flags'].get(revision_keys[-1])
                    if flag:
                        assert any(item['text'] == flag for item in q['flags']), 'Revision lost a source warning'
    assert set(revision_keys) == source_keys, 'Revision lost a question'
    assert len(revision_keys) == len(set(revision_keys)) == 3360, 'Revision duplicates a source question'
    for diet, page in FIGURE_PAGES:
        assert (ROOT / f'assets/source-figures/{diet}-p{page}.png').is_file()
    law_sources = json.loads((DATA / 'law-sources.json').read_text())
    for source in law_sources['sources']:
        path = ROOT.parent / source['localFile']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256'], source['title']
    study_figures = json.loads((DATA / 'study-figures.json').read_text())
    assert hashlib.sha256((ROOT.parent / study_figures['source']).read_bytes()).hexdigest() == study_figures['sourceSha256']
    assert all((ROOT / item['src']).is_file() for item in study_figures['pages'])
    report = {'papers': len(papers), 'diets': len(diets), 'questions': dict(totals),
              'studyFigurePages': len(study_figures['pages']),
              'studyFigureAndTableCaptions': len(study_figures['captions']),
              'citations': {code: dict(counts) for code, counts in citation_counts.items()},
              'additionalReadingLinks': reading_links,
              'flags': len(exams['flags']), 'revisionSourceQuestions': len(revision_keys),
              'sourceFigures': len(FIGURE_PAGES), 'originalPdfs': len(source_pdfs),
              'questionsWithSourcePage': question_pages, 'referenceTables': reference_tables,
              'manualCitationReviews': len(PIN), 'reviewedKeyCorrections': len(KEY_CORRECTIONS),
              'reviewedShortAnswerCorrections': len(SAQ_CORRECTIONS)}
    (DATA / 'audit-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return report


if __name__ == '__main__':
    run()
