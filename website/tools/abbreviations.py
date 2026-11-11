"""Reader glossary for abbreviations actually used in a chapter.

These are explanatory additions, not replacements for the study text.
Historical institution/Act names are labelled as historical.
"""
import re

TERMS = {
    'ISA': 'International Standard on Auditing (plural: International Standards on Auditing)',
    'CAMA': 'Companies and Allied Matters Act',
    'ICQ': 'Internal Control Questionnaire',
    'ICEQ': 'Internal Control Evaluation Questionnaire',
    'CAAT': 'Computer-Assisted Audit Technique',
    'CAATs': 'Computer-Assisted Audit Techniques',
    'FIFO': 'First In, First Out',
    'LIFO': 'Last In, First Out',
    'WIP': 'Work in Progress',
    'EOQ': 'Economic Order Quantity',
    'FC': 'Fixed Cost',
    'CGT': 'Capital Gains Tax (the historical tax name; the 2026 text treats chargeable gains under NTA 2025)',
    'INEC': 'Independent National Electoral Commission',
    'NTP': 'National Tax Policy',
    'TIN': 'Taxpayer Identification Number (the current NTAA also uses Tax ID)',
    'FIRS': 'Federal Inland Revenue Service (historical; succeeded by the Nigeria Revenue Service)',
    'NRS': 'Nigeria Revenue Service',
    'SIRS': 'State Internal Revenue Service',
    'HS': 'Harmonized System (customs classification)',
    'PITA': 'Personal Income Tax Act (historical; repealed by NTA 2025)',
    'WHT': 'Withholding Tax',
    'NHF': 'National Housing Fund',
    'NHIS': 'National Health Insurance Scheme (the historical name used in the source)',
    'YOA': 'Year of Assessment',
    'CITA': 'Companies Income Tax Act (historical; repealed by NTA 2025)',
    'TET': 'Tertiary Education Tax (historical; distinguish it from the current development levy)',
    'SWOT': 'Strengths, Weaknesses, Opportunities and Threats',
    'ICT': 'Information and Communication Technology',
    'PERT': 'Programme Evaluation and Review Technique',
    'COVID': 'Coronavirus Disease (COVID-19 means Coronavirus Disease 2019)',
    'NTA': 'Nigeria Tax Act 2025',
    'NTAA': 'Nigeria Tax Administration Act 2025',
    'BPR': 'Business Process Re-engineering',
    'NPV': 'Net Present Value',
    'IRR': 'Internal Rate of Return',
    'ARR': 'Accounting Rate of Return',
    'CVP': 'Cost-Volume-Profit',
    'JIT': 'Just-in-Time',
    'TQM': 'Total Quality Management',
    'IDEA': 'Interactive Data Extraction and Analysis (audit software); International Data Encryption Algorithm in cryptography — the March 2024 paper uses the latter meaning',
    'ISQM': 'International Standard on Quality Management',
    'ISQC': 'International Standard on Quality Control (historical; ISQM 1 replaced ISQC 1)',
    'NIIRA': 'Nigerian Insurance Industry Reform Act 2025',
    'PESTEL': 'Political, Economic, Social, Technological, Environmental and Legal',
    'ABM': 'Activity-Based Management',
    'MRP': 'Materials Requirements Planning',
    'ABC': 'Activity-Based Costing in costing; ABC inventory classification uses categories A, B and C for stock control',
}


def strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, list):
        for item in node:
            yield from strings(item)
    elif isinstance(node, dict):
        for item in node.values():
            yield from strings(item)


def chapter_terms(chapter):
    text = ' '.join(strings(chapter.get('secs', [])))
    return [{'term': term, 'meaning': meaning} for term, meaning in sorted(TERMS.items())
            if re.search(r'\b' + re.escape(term) + r's?\b', text)
            and (term != 'ABC' or re.search(r'activity[\s-]+based', text, re.I))]
