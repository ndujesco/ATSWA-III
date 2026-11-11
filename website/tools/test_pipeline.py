"""Regressions for observed source-loss and extraction-association defects."""
import ast
import json
import unittest
from pathlib import Path
from unittest.mock import patch
from common import strip_furniture, money
from extract_papers import pdf_lines, RE_EXAM
from build_exams import split_secb
from citation_reviews import reviewed_pins

ROOT = Path(__file__).resolve().parents[1]


class SourceRegressions(unittest.TestCase):
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
