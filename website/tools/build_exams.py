#!/usr/bin/env python3
"""papers.json -> data/exams.js, the form the app consumes."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from corrections import FLAGS, KEY_CORRECTIONS, SAQ_CORRECTIONS
from law_flags import make_flags
from source_recoveries import SOURCE_FIGURES
from essay_readings import readings_for
try:
    from expansions import NOTES, SECB_NOTES
except ImportError:
    NOTES, SECB_NOTES = {}, {}

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
RE_Q = re.compile(r'^\s*QUESTION\s+(\d)\b', re.I)

# Below this, aim.py's own retrieval margin is too thin to trust — better to
# show no "found in chapter X" link at all than to send the reader to the
# wrong one. aim_sec.py already applies its own (separate, stricter) gate
# before it ever writes 'sec', so only 'ch' needs gating here.
CH_CONF_MIN = 0.12


def chsec(q):
    if (q.get('chConf') or 0) < CH_CONF_MIN:
        return None, None
    return q.get('ch'), q.get('sec')


def split_secb(lines):
    """Cut the Section B paper into its six questions."""
    marks = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := RE_Q.match(l))]
    out = {}
    for j, (i, n) in enumerate(marks):
        end = marks[j + 1][0] if j + 1 < len(marks) else len(lines)
        body = [l.rstrip() for l in lines[i + 1:end]]
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        out[n] = body
    return out


def main():
    papers = json.loads((DATA / 'papers.json').read_text())
    out = []
    for p in papers:
        qs = split_secb(p['secb_paper'])
        sol = {s['n']: s for s in p['saq_solutions']}
        mcq_out = []
        for q in p['mcq']:
            ch, sec = chsec(q)
            mcq_out.append({'n': q['n'], 'stem': q['stem'], 'options': q['options'],
                             'pre': q.get('pre') or [], 'ch': ch, 'sec': sec, 'sourcePage': q.get('sourcePage'),
                             **{k: q[k] for k in ('printedN', 'printedOptionLabels') if k in q}})
            correction = KEY_CORRECTIONS.get((p['diet'], p['subject'], 'mcq', q['n']))
            if correction:
                mcq_out[-1]['studyKey'] = correction
        saq_out = []
        for q in p['saq']:
            ch, sec = chsec(q)
            saq_out.append({'n': q['n'], 'body': q['body'], 'pre': q.get('pre') or [],
                             'ch': ch, 'sec': sec, 'sourcePage': q.get('sourcePage'),
                             'ans': sol[q['n']]['body'] if q['n'] in sol else None})
            correction = SAQ_CORRECTIONS.get((p['diet'], p['subject'], 'saq', q['n']))
            if correction:
                saq_out[-1]['studyAns'] = correction
        secb_out = []
        for s in p['secb_solutions']:
            ch, sec = chsec(s)
            secb_out.append({'n': s['n'], 'q': qs.get(s['n'], []), 'solution': s['solution'],
                              'readings': readings_for(p['diet'], p['subject'], s['n']),
                              'examiner': s.get('examiner') or [], 'ch': ch, 'sec': sec,
                              'sourcePage': s.get('sourcePage'), 'solutionPage': s.get('solutionPage'),
                              'note': SECB_NOTES.get(f"{p['diet']}/{p['subject']}/{s['n']}")})
        for kind, questions in (('mcq', mcq_out), ('saq', saq_out), ('secb', secb_out)):
            for question in questions:
                question['sourceFigures'] = SOURCE_FIGURES.get(f"{p['diet']}/{p['subject']}/{kind}/{question['n']}", [])
        out.append({
            'diet': p['diet'], 'name': p['dietName'], 'subject': p['subject'], 'source': p.get('source'),
            'referenceTables': p.get('referenceTables', []),
            'key': {str(k): v for k, v in p['mcq_key'].items()},
            'mcq': mcq_out, 'saq': saq_out, 'secb': secb_out,
            'mcqWorkings': p.get('mcq_workings', []),
            'saqWorkings': p.get('saq_workings', []),
            'mcqExaminer': p.get('mcq_examiner', []),
            'saqExaminer': p.get('saq_examiner', []),
            'mcqFigures': SOURCE_FIGURES.get(f"{p['diet']}/{p['subject']}/mcqWorkings", []),
            'saqFigures': SOURCE_FIGURES.get(f"{p['diet']}/{p['subject']}/saqWorkings", []),
        })
    generated_flags, review = make_flags(papers, split_secb)
    for key, value in FLAGS.items():
        generated_flags[key] = '\n\n'.join(filter(None, (generated_flags.get(key), value)))
    flags = {'/'.join([k[0], k[1], k[2], str(k[3])]): v for k, v in generated_flags.items()}
    (DATA / 'law-review.json').write_text(json.dumps({'reviewDate': '2026-11-11',
        'method': 'Rule pass over every question and its official answer; targeted primary-law verification. No claim of individual legal re-computation for every essay.',
        'questions': review}, ensure_ascii=False, indent=1) + '\n')
    blob = {'papers': out, 'notes': NOTES, 'flags': flags}
    js = 'ATSWA.put("EXAMS", ' + json.dumps(blob, ensure_ascii=False, separators=(',', ':')) + ');\n'
    (DATA / 'exams.js').write_text(js)
    print(f'data/exams.js  {len(js)//1024} KB  ({len(out)} papers, {len(flags)} flagged questions)')


if __name__ == '__main__':
    main()
