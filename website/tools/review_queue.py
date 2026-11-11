#!/usr/bin/env python3
"""Print the remaining citation review queue, with full question requirements.

Usage: python3 tools/review_queue.py AUD --offset 0 --limit 25 [--sections]
The queue does not change data or silently relax a confidence threshold.
"""
import argparse
import json
from pathlib import Path
from build_exams import split_secb
from citation_reviews import reviewed_pins

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('subject', choices=['AUD', 'CA', 'TAX', 'MAN'])
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--limit', type=int, default=25)
    parser.add_argument('--sections', action='store_true')
    args = parser.parse_args()
    chapters, sections = reviewed_pins()
    rows = []
    for paper in json.loads((ROOT / 'data/papers.json').read_text()):
        if paper['subject'] != args.subject:
            continue
        short = {q['n']: q['body'] for q in paper['saq_solutions']}
        essays = split_secb(paper['secb_paper'])
        for kind, field in [('mcq', 'mcq'), ('saq', 'saq'), ('secb', 'secb_solutions')]:
            for question in paper[field]:
                key = (paper['diet'], paper['subject'], kind, question['n'])
                if key in chapters:
                    continue
                if question.get('chConf', 0) >= .12 and (not args.sections or question.get('sec')):
                    continue
                if kind == 'mcq':
                    text = question['stem']['t']
                    accepted = paper['mcq_key'][str(question['n'])]
                    answer = ' / '.join(question['options']['ABCDE'.index(letter)]['t']
                                        for letter in accepted.split('/') if len(letter) == 1 and letter in 'ABCDE')
                elif kind == 'saq':
                    text, answer = ' '.join(question['body']), ' '.join(short[question['n']])
                else:
                    full = ' '.join(essays[question['n']])
                    text = full if len(full) < 1000 else full[:300] + ' … ' + full[-700:]
                    answer = ''
                shared = ' '.join(question.get('pre', []))
                rows.append((key, text, answer, shared, question))
    print(f'{args.subject}: {len(rows)} remaining ' + ('chapter/section' if args.sections else 'chapter') + ' reviews')
    for key, text, answer, shared, question in rows[args.offset:args.offset+args.limit]:
        print('/'.join(map(str, key)) + ' | ' + text + ' | ANSWER: ' + answer +
              ((' | SHARED: ' + shared[:350]) if shared else '') +
              f" | candidate {question.get('ch')}/{question.get('sec')} ({question.get('chConf')})")


if __name__ == '__main__':
    main()
