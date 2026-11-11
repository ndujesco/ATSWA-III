"""Visual recoveries checked against rendered INSIGHT PDF pages.

These are source content, not newly invented answers. Page numbers are PDF
pages (the printed page number can differ). recover_figures.py makes the assets.
"""
SAQ_RECOVERIES = {
    ('2019-03', 'TAX', 9): [
        'Adjusted Profit Ratio = (Adjusted Profit / Worldwide Income) × 100%'
    ],
}

FIGURE_PAGES = {
    ('2019-03', 45): 'Labour turnover formulas and official workings',
    ('2019-03', 51): 'High-low method: the complete original repair-cost calculation',
    ('2021-09', 50): 'Cost per tonne, cost per kilometre and efficiency ratio',
    ('2021-09', 51): 'Printed activity, capacity and efficiency ratio workings',
    ('2023-03', 42): 'Official short-answer workings including the annuity factor',
    ('2024-09', 83): 'Three levels of management: the original marked diagram',
    ('2026-03', 41): 'Contract costing fraction and official MCQ workings',
}


def figures(*pages):
    return [{'src': f'assets/source-figures/{diet}-p{page}.png',
             'alt': FIGURE_PAGES[(diet, page)], 'page': page}
            for diet, page in pages]


SOURCE_FIGURES = {
    '2019-03/CA/secb/4': figures(('2019-03', 51)),
    '2019-03/CA/saq/9': figures(('2019-03', 45)),
    '2019-03/CA/saq/10': figures(('2019-03', 45)),
    '2019-03/CA/saqWorkings': figures(('2019-03', 45)),
    '2021-09/CA/secb/3': figures(('2021-09', 50)),
    '2021-09/CA/secb/4': figures(('2021-09', 50), ('2021-09', 51)),
    '2023-03/CA/saq/7': figures(('2023-03', 42)),
    '2023-03/CA/saqWorkings': figures(('2023-03', 42)),
    '2024-09/MAN/secb/1': figures(('2024-09', 83)),
    '2026-03/CA/mcq/3': figures(('2026-03', 41)),
    '2026-03/CA/mcqWorkings': figures(('2026-03', 41)),
}
