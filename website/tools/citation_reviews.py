"""Manually reviewed residual chapter/section matches.

Each group is a real passage in the authored study notes. Entries are kept
by diet/kind/ordinal so the decision is reviewable and repeatable. These
resolve ambiguous retrieval after the systemic phrase/preamble fixes;
confidence thresholds in the automatic matcher are unchanged.
"""

REVIEWED = {
    'AUD': {
        '7/7.6': ['2019-03/mcq/25', '2019-09/saq/17'],
        '2/2.10': ['2019-03/mcq/27', '2019-09/mcq/28'],
        '12/12.12': ['2019-03/mcq/28', '2019-03/secb/5'],
        '4/4.2': ['2019-03/saq/4'],
        '7/7.3': ['2019-03/saq/10'],
        '7/7.5': ['2019-03/saq/17'],
        '9/9.2': ['2019-03/saq/19'],
        '2/2.5': ['2019-03/secb/1', '2019-09/mcq/4', '2019-09/mcq/5'],
        '1/1.12': ['2019-09/mcq/7', '2019-09/saq/4', '2020-03/mcq/2', '2020-03/mcq/3'],
        '8/8.12': ['2019-09/mcq/8'],
        '5/5.5': ['2019-09/mcq/12'],
        '2/2.9': ['2019-09/mcq/16'],
        '10/10.3': ['2019-09/saq/6'],
        '6/6.7': ['2019-09/saq/8'],
        '1/1.4': ['2019-09/secb/1'],
        '1/1.7': ['2020-03/mcq/5'],
        '7/7.4': ['2020-03/mcq/9'],
        '3/3.3': ['2020-03/saq/3'],
    },
    'CA': {
        '1/1.2': ['2019-03/mcq/1', '2019-09/mcq/3'],
        '2/2.1.1': ['2019-03/mcq/5', '2019-03/mcq/11', '2019-09/mcq/4',
                    '2020-03/mcq/4', '2020-03/saq/2', '2021-03/mcq/14', '2021-03/mcq/21'],
        '3/3.3': ['2019-03/saq/4'],
        '9/9.2': ['2019-03/saq/13'],
        '9/9.1': ['2019-09/mcq/23'],
        '2/2.3': ['2019-09/saq/5', '2020-03/saq/3'],
        '3/3.6': ['2019-09/secb/1'],
        '3/3.1': ['2020-03/mcq/7'],
        '5/5.2': ['2020-03/mcq/30'],
        '5/5.1': ['2020-03/saq/1'],
        '9/9.3': ['2020-03/saq/8', '2021-03/mcq/20'],
        '5/5.8': ['2020-09/mcq/1'],
        '2/2.1.2a': ['2020-09/saq/7'],
        '10/10.2': ['2020-09/saq/18'],
        '9/9.4': ['2020-09/secb/2'],
        '14/14.6': ['2020-09/secb/6'],
        '13/13.2': ['2021-03/mcq/10'],
    },
    'TAX': {
        '1/1.10.2': ['2019-03/mcq/1', '2020-03/mcq/2'],
        '1/1.5': ['2019-03/mcq/5'],
        '15/15.8': ['2019-03/mcq/8', '2019-03/mcq/9', '2019-03/saq/17',
                      '2019-09/saq/20', '2019-03/secb/6'],
        '17/17.7': ['2019-03/mcq/19', '2019-09/mcq/21'],
        '23/23.4': ['2019-03/mcq/26'],
        '7/7.38': ['2019-03/saq/12'],
        '21/21.2': ['2019-03/saq/14'],
        '2/2.6': ['2019-09/mcq/4'],
        '1/1.8': ['2019-09/mcq/9', '2020-03/mcq/22'],
        '2/2.5': ['2019-09/saq/9'],
        '7/7.3': ['2019-09/saq/11'],
        '24/24.15': ['2020-03/mcq/7'],
        '1/1.3': ['2020-03/mcq/9', '2020-03/mcq/21'],
        '4/4.7': ['2020-03/mcq/17'],
        '12/12.9': ['2020-03/saq/8'],
        '16/16.5': ['2020-03/saq/9'],
        '9/9.16': ['2020-03/saq/17'],
        '18/18.2': ['2020-09/mcq/17'],
    },
    'MAN': {
        '4/A.5': ['2019-03/mcq/13', '2019-03/mcq/14'],
        '4/C.2': ['2019-03/mcq/15', '2019-03/saq/9'],
        '3/C.1': ['2019-03/mcq/22'],
        '7/7.4': ['2019-09/mcq/18'],
        '3/C.6': ['2019-09/mcq/24'],
        '3/C.9': ['2019-09/mcq/25', '2019-09/saq/17'],
        '1/A.12': ['2019-09/saq/2', '2020-09/mcq/3'],
        '4/A.13': ['2019-09/saq/10'],
        '4/C.6': ['2019-09/saq/12'],
        '5/A.1': ['2019-09/saq/20'],
        '2/2.7': ['2020-03/mcq/5'],
        '3/D.1': ['2020-03/mcq/24'],
        '1/A.7': ['2020-03/saq/1'],
        '4/A.17': ['2020-03/saq/8'],
        '2/2.16': ['2020-03/saq/14'],
        '4/D.4': ['2020-03/saq/18'],
        '4/A.14': ['2020-09/mcq/2'],
        '4/C.9': ['2020-09/mcq/19'],
        '5/A.4': ['2020-09/mcq/22'],
        '1/A.13': ['2020-09/saq/2'],
        '2/2.4': ['2020-09/saq/5'],
        '4/C.8': ['2020-09/saq/14'],
    },
}


from citation_review_batches import BATCHES

for _code, _target, _references in BATCHES:
    REVIEWED.setdefault(_code, {}).setdefault(_target, []).extend(_references)


def reviewed_pins():
    chapters, sections = {}, {}
    for code, targets in REVIEWED.items():
        for target, references in targets.items():
            chapter, section = target.split('/', 1)
            for reference in references:
                diet, kind, number = reference.split('/')
                key = (diet, code, kind, int(number))
                if key in chapters:
                    raise ValueError(f'Duplicate citation review: {key}')
                chapters[key], sections[key] = int(chapter), section
    # A later semantic review can refine an earlier plausible destination.
    # Keep that review history explicit, rather than duplicating a PIN entry.
    from citation_refinements import REFINEMENTS
    refined = set()
    for code, target, references, reason in REFINEMENTS:
        chapter, section = target.split('/', 1)
        if not reason.strip():
            raise ValueError('A citation refinement needs its review reason')
        for reference in references:
            diet, kind, number = reference.split('/')
            key = (diet, code, kind, int(number))
            if key in refined:
                raise ValueError(f'Duplicate citation refinement: {key}')
            refined.add(key)
            chapters[key], sections[key] = int(chapter), section
    from source_restoration_reviews import REVIEWS
    restored = set()
    for key, chapter, section, reason in REVIEWS:
        if key in restored or not reason.strip():
            raise ValueError(f'Invalid source-restoration review: {key}')
        restored.add(key)
        chapters[key], sections[key] = chapter, section
    return chapters, sections
