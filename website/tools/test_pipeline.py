"""Regressions for observed source-loss and extraction-association defects."""
import ast
import hashlib
import json
import re
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch
from common import strip_furniture, money
from extract_papers import pdf_lines, RE_EXAM
from build_exams import split_secb
from citation_reviews import reviewed_pins

ROOT = Path(__file__).resolve().parents[1]


class SourceRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapters = {str(p.relative_to(ROOT)): runpy.run_path(str(p))['CH']
                        for p in (ROOT / 'content').glob('*/ch*.py')}

    def section(self, path, number):
        return next(s for s in self.chapters[path]['secs'] if s['n'] == number)

    def test_reviewed_original_heading_and_section_numbers_are_retained(self):
        review = json.loads((ROOT / 'data/source-fidelity-review.json').read_text())
        for item in review['headingRestorations']:
            blocks = self.section(item['path'], item['section'])['b']
            expected = '§' + item['source_number'] + ' ' + item['heading']
            self.assertTrue(any(b.get(item['tag']) == expected for b in blocks), expected)
        for item in review['sectionReferenceRestorations']:
            numbers = item['source_numbers']
            label = (numbers[0] if len(numbers) == 1 else numbers[0] + '–' + numbers[-1]) if numbers else ''
            self.assertEqual(self.section(item['path'], item['section'])['sourceN'], label)

    def test_full_original_specimen_text_is_not_replaced_with_excerpts(self):
        review = json.loads((ROOT / 'data/source-fidelity-review.json').read_text())
        def fingerprints(value):
            if isinstance(value, dict):
                if isinstance(value.get('pre'), str):
                    yield hashlib.sha256(value['pre'].encode()).hexdigest()
                for child in value.values():
                    yield from fingerprints(child)
            elif isinstance(value, list):
                for child in value:
                    yield from fingerprints(child)
        self.assertGreaterEqual(len(review['sourceTextFingerprints']), 11)
        for item in review['sourceTextFingerprints']:
            self.assertIn(item['sha256'], set(fingerprints(self.section(item['path'], item['section'])['b'])), item)

    def test_original_control_questionnaires_have_every_question(self):
        blocks = self.section('content/aud/ch08.py', '8.7')['b']
        tables = [b['table'] for b in blocks if b.get('table', {}).get('head') == ['Question', 'Yes', 'No', 'N/A', 'Date of Answer']]
        self.assertEqual([len(t['rows']) for t in tables], [10, 6, 5])
        blocks = self.section('content/aud/ch08.py', '8.8')['b']
        start = next(i for i, b in enumerate(blocks) if b.get('h4', '').startswith('Full study-text Internal Control Evaluation'))
        self.assertEqual([len(b['ul']) for b in blocks[start:] if 'ul' in b], [13, 9, 4, 8, 7, 4, 7])

    def test_original_study_figure_pages_and_captions_are_preserved(self):
        manifest = json.loads((ROOT / 'data/study-figures.json').read_text())
        self.assertEqual(len(manifest['captions']), 42)
        self.assertEqual(len(manifest['pages']), 37)
        self.assertEqual(hashlib.sha256((ROOT.parent / manifest['source']).read_bytes()).hexdigest(), manifest['sourceSha256'])
        for page in manifest['pages']:
            self.assertTrue((ROOT / page['src']).read_bytes().startswith(b'\x89PNG\r\n\x1a\n'))
        for item in manifest['captions']:
            blocks = self.section(item['chapter_file'], item['suggested_section'])['b']
            self.assertTrue(any(item['caption'] in b.get('figure', {}).get('cap', '') for b in blocks), item)

    def test_management_essay_answers_are_self_contained(self):
        for path, number in [('content/man/ch04.py', 'B.9'), ('content/man/ch09.py', 'A.10'),
                             ('content/man/ch09.py', 'B.7'), ('content/man/ch09.py', 'C.8')]:
            examples = [b['eg'] for b in self.section(path, number)['b'] if 'eg' in b]
            self.assertTrue(examples)
            for example in examples:
                for block in example.get('a', []):
                    self.assertNotIn('Answer at', json.dumps(block))
                self.assertGreater(len(json.dumps(example.get('a', []))), 1000)

    def test_dynamic_supplements_are_not_also_embedded_in_chapter_literals(self):
        def words(value):
            if isinstance(value, str):
                return re.findall(r'\w+', value)
            if isinstance(value, dict):
                return sum((words(v) for v in value.values()), [])
            if isinstance(value, list):
                return sum((words(v) for v in value), [])
            return []
        for path, final in self.chapters.items():
            tree = ast.parse((ROOT / path).read_text())
            node = next(n.value for n in tree.body if isinstance(n, ast.Assign)
                        and any(isinstance(t, ast.Name) and t.id == 'CH' for t in n.targets))
            original = ast.literal_eval(node)
            for before, after in zip(original['secs'], final['secs'], strict=True):
                additions = after['b'][len(before['b']):]
                fingerprints = {tuple(words(block)) for block in additions}
                self.assertFalse(any(tuple(words(block)) in fingerprints for block in before['b']),
                                 (path, before['n'], 'duplicated trailing supplement'))

    def test_real_figures_are_not_global_page_furniture(self):
        self.assertEqual(strip_furniture(['200', '2', '/3', '0']), ['200', '2', '/3', '0'])

    def test_page_numbers_are_removed_on_either_side_of_the_footer_label(self):
        text = 'Cost\n 91,000\n200\nvalue\n 1\nATSWA PART III MARCH 2019 DIET\f'
        with patch('extract_papers.subprocess.run') as run:
            run.return_value.stdout = text
            lines = pdf_lines(Path('source.pdf'))
        self.assertIn('200', lines)
        self.assertNotIn(' 1', lines)

    def test_printed_currency_glyph_recovery(self):
        self.assertEqual(money('LË455 and GH Ë3.25 and N500'), 'L¢455 and GH¢3.25 and ₦500')

    def test_misspelled_source_report_headers(self):
        for heading in ['EXAMINER ‘S REPORT', 'EXAMINE’R COMMENTS', 'EXAMINER’S COMMENT']:
            self.assertIsNotNone(RE_EXAM.match(heading))

    def test_restored_real_workings(self):
        papers = json.loads((ROOT / 'data/papers.json').read_text())
        paper = next(p for p in papers if (p['diet'], p['subject']) == ('2019-03', 'CA'))
        solution = next(q for q in paper['secb_solutions'] if q['n'] == 4)['solution']
        self.assertIn('200', [line.strip() for line in solution])
        self.assertTrue(any('91,000' in line for line in solution))

    def test_tax_reference_tables_are_preserved_outside_question_six(self):
        papers = json.loads((ROOT / 'data/papers.json').read_text())
        for paper in papers:
            if paper['subject'] != 'TAX':
                continue
            self.assertIn('NIGERIAN TAX RATES', '\n'.join(paper['referenceTables']))
            self.assertNotIn('NIGERIAN TAX RATES', '\n'.join(split_secb(paper['secb_paper'])[6]))
            self.assertTrue(any('CAPITAL ALLOWANCES' in line for line in paper['referenceTables']))

    def test_manual_review_groups_have_no_duplicate_literal_keys_or_question_ids(self):
        path = ROOT / 'tools/citation_reviews.py'
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Dict):
                values = [ast.literal_eval(key) for key in node.keys if isinstance(key, ast.Constant)]
                self.assertEqual(len(values), len(set(values)), 'Duplicate review group')
        chapters, sections = reviewed_pins()
        self.assertEqual(set(chapters), set(sections))


if __name__ == '__main__':
    unittest.main()
