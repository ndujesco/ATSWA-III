"""Question-level historical-law notes, using the existing FLAGS mechanism.

Rules state the current provision rather than changing the printed question
or its official key. Primary law versions and hashes: data/law-sources.json.
Numbers refer to the National Assembly's January 2026 corrected gazettes,
not the earlier circulating copies. Run by build_exams.py after extraction.
"""
import re

NTA = 'https://nass.gov.ng/documents/download/11249'
NTAA = 'https://nass.gov.ng/documents/download/11250'
JRB = 'https://nass.gov.ng/documents/download/11247'
NRS = 'https://nass.gov.ng/documents/download/11251'
CAMA = 'https://www.cac.gov.ng/wp-content/uploads/2020/12/CAMA-NOTE-BOOK-FULL-VERSION.pdf'
WHT = 'https://www.fiscalreforms.ng/news/deduction-of-withholding-tax-regulations-takes-effect-1st-january-2025'


def cite(label, url):
    return f'[{label}]({url})'


RULES = [
    ('vat_zero_transition', r'(?=.*\b(?:VAT|value added tax)\b)(?=.*exempt)(?=.*(?:basic food|medical|pharmaceutical|educational books|fertilis|fertiliz|tuition|exported (?:goods|services)))',
     'The old exemption list must be checked against the new distinction '
     'between **exempt** and **zero-rated** supplies. NTA s.186 now '
     'zero-rates the listed basic foods, medical/pharmaceutical products, '
     'educational books/materials, medical services and tuition, among '
     'other specified supplies. Zero rating is not exemption: eligible '
     'input tax may be credited under s.155. ' + cite('NTA ss.155, 185–186', NTA)),
    ('pension_approval', r'(?:pension fund.*?approv|contribution.*?pension.*?approv)',
     'The printed JTB pension-approval formulation is historical. Current '
     'individual relief is for contributions **under the Pension Reform '
     'Act** (NTA s.30(2)(a)(iii)); current business deductions must meet '
     'the applicable NTA provision and pension legislation. Do not simply '
     'replace JTB with JRB as the pension-approval authority. ' + cite('NTA ss.20, 30', NTA)),
    ('vat_old_rate', r'(?=.*\b(?:VAT|value added tax)\b)(?=.*(?<![\d.])5\s*%)',
     'The question/solution uses the historical **5% VAT** rate. The current '
     'standard rate is **7.5%** under NTA 2025 s.147. Recompute a current '
     'transaction at 7.5%, while retaining the rate for the period actually '
     'asked in this paper. ' + cite('NTA s.147', NTA)),
    ('vat_distribution', r'(?:VAT|value added tax).*?(?:shar|distribut)|(?:shar|distribut).*?(?:VAT|value added tax)',
     'The historical VAT sharing formula is superseded. NTAA 2025 s.81 '
     'allocates net VAT revenue **10% Federal, 55% States/FCT and 35% Local '
     'Governments**. The further allocation basis is 50% equality, 20% '
     'population and 30% consumption. Do not substitute the old 15/50/35 '
     'formula in a current-law answer. ' + cite('NTAA s.81', NTAA)),
    ('vat_input_credit', r'(?:input (?:VAT|tax).*?(?:capital|services|restrict)|(?:capital goods|fixed assets).*?(?:VAT|input tax))',
     'Input-VAT treatment has widened. Under NTA s.155(4)–(5), eligible '
     'input tax includes **services and fixed assets** used to make taxable '
     'supplies. Mixed use must be apportioned; deduction is within five '
     'years of the relevant period and applies to supplies from the Act’s '
     'commencement. The old blanket exclusion/capitalisation of input VAT '
     'on services or fixed assets is not the current rule. ' + cite('NTA s.155', NTA)),
    ('vat_small_business', r'(?:VAT|value added tax|taxable supplies).*?(?:25\s*million|25,?000,?000)',
     'The printed ₦25m VAT-compliance threshold is historical. NTAA s.147 '
     'defines a small business using **turnover up to ₦100m and fixed '
     'assets up to ₦250m**, excluding professional-service businesses. '
     'Section 22 provides the small-business return exemption and written '
     'opt-in, with its stated exceptions; the ordinary return is due on '
     'the following month’s 21st. ' + cite('NTAA ss.22, 147', NTAA)),
    ('vat_committee', r'(?:VAT|value added tax) technical committee',
     'The VAT Technical Committee belongs to the repealed VAT Act '
     'administration. Current VAT is administered by NRS under NTAA s.3 '
     'and NTA Chapter Six. There is no matching current committee-composition '
     'answer to memorise in place of this historical list. ' + cite('NTAA s.3', NTAA) + '; ' + cite('NTA ss.144–157, 195', NTA)),
    ('old_appeal_body', r'body of appeal commissioners|VAT tribunal|value added tax tribunal',
     'The historical appeal-body title is superseded. The **Tax Appeal '
     'Tribunal** is now established under JRB Act 2025 s.23; its members '
     'are Tax Appeal Commissioners under s.24. Appeal to the Federal High '
     'Court follows the Second Schedule. Distinguish the institution from '
     'the title of its members. ' + cite('JRB Act ss.23–24 and Second Schedule', JRB)),
    ('capital_basis', r'(?:end|close).*?(?:government.*fiscal year)|capital allowances?.*?(?:government.*fiscal year)',
     'The printed government-fiscal-year rule is historical. The current '
     'capital-allowance basis period follows the basis period for assessable '
     'profit/income under the NTA First Schedule, read with ss.22–26. '
     'A 31 December government year-end is not a universal replacement '
     'for the business’s relevant accounting period. ' + cite('NTA ss.22–26 and First Schedule ¶1', NTA)),
    ('terminal_allowance', r'terminal capital allowance|unutilised capital allowance.*(?:back|cessation)',
     'The printed terminal-capital-allowance/five-year carry-back rule '
     'belongs to the previous framework. The current NTA First Schedule '
     'Part I has annual allowances, disposal adjustments and transitional '
     'rules, but no equivalent general five-year terminal carry-back. '
     'Do not apply that historical answer to a new Part I computation. ' + cite('NTA First Schedule Part I', NTA)),
    ('early_payment_bonus', r'(?:bonus.*?90 days|90 days.*?bonus)',
     'The old CITA early-payment bonus for small/medium companies is '
     'historical. NTAA s.49 now governs the time for paying assessed tax; '
     'it does not reproduce that 1%/2% bonus. Small-company exemption '
     'under NTA s.56 is a separate rule. ' + cite('NTAA s.49', NTAA) + '; ' + cite('NTA s.56', NTA)),
    ('relief', r'consolidated relief|\bCRA\b|200,000.*20%',
     'The printed question uses consolidated relief allowance under PITA. '
     'NTA 2025 s.30 has no CRA deduction: eligible deductions include rent relief '
     'of 20% of rent actually paid, capped at ₦500,000. The old CRA amount has '
     'no current equivalent; current relief needs the taxpayer’s actual rent. ' + cite('NTA s.30', NTA)),
    ('pit_rates', r'first\s+300,000|next\s+300,000|\b7\s*%.*\b11\s*%|personal income tax liability|computation of (?:personal )?income tax liability',
     'This is a historical income-tax computation. The current individual bands '
     'after eligible deductions are: first ₦800,000 at 0%; next ₦2.2m at 15%; '
     'next ₦9m at 18%; next ₦13m at 21%; next ₦25m at 23%; excess over ₦50m '
     'at 25%. Keep the printed answer for the period asked; a current-year '
     'computation must use these bands and s.30 deductions. ' + cite('NTA s.58 and Fourth Schedule', NTA)),
    ('development', r'education tax|education trust|TETFUND|\bTET\b|police trust fund|information technology development levy|\bNITDA\b|\bNASENI\b',
     'This question uses a separate legacy education/development levy or its '
     'distribution. NTA 2025 s.59 instead imposes a 4% development levy on '
     'assessable profits of liable companies, excluding small and non-resident '
     'companies. Its fund allocations differ from the old universities/'
     'polytechnics/colleges 2:1:1 split; there is no separate current TET rate '
     'to substitute for the printed 2%, 2.5% or 3%. ' + cite('NTA ss.59, 196', NTA)),
    ('company_size', r'small compan|medium.?sized compan|medium compan|turnover.*25.?000.?000|turnover.*25\s*million',
     'The old small/medium company thresholds are historical. The 2026 '
     'framework uses gross turnover up to ₦100m and fixed assets up to ₦250m '
     'for the small-company definition (see also the NTAA definition’s '
     'professional-services exclusion). NTA s.56 charges small companies at '
     '0% and other companies at 30%; the former medium-company 20% band is '
     'absent. ' + cite('NTA ss.56, 201', NTA) + '; ' + cite('NTAA s.147', NTAA)),
    ('minimum_tax', r'minimum tax',
     'The printed minimum-tax regime belongs to the repealed CITA/PITA '
     'framework. NTA 2025 does not carry forward the old general turnover '
     'minimum tax or individual 1% minimum tax. NTA s.57 instead provides a '
     '15% minimum effective rate for the specified MNE entities and companies '
     'with aggregate turnover of at least ₦50bn; it is a different test. '
     'Individuals use s.58 and the Fourth Schedule. ' + cite('NTA ss.57–58, 195', NTA)),
    ('loss_office', r'compensation for (?:the )?loss of office|loss of office.*compensation',
     'The old ₦10,000/₦10m compensation threshold is superseded. Under '
     'NTA 2025 s.50, compensation for personal injury or loss of office up to '
     '₦50m is exempt; only the excess is chargeable, using the applicable '
     'individual income-tax rates rather than the old flat 10% CGT. ' + cite('NTA ss.50, 58', NTA)),
    ('basis_election', r'right of election|penultimate|commencement rule|cessation rule|change of accounting date|second year of (?:a new|assessment)|first three years|first 3 years',
     'This question uses legacy commencement/cessation or accounting-date '
     'rules. NTA ss.22–24 use the relevant accounting periods: commencement '
     'to the first accounting date, the following accounting period, and the '
     'final period to cessation. The old second/third-year election and '
     'Revenue’s penultimate-year comparison do not have an equivalent '
     'election under these provisions. A change of date follows s.23. ' + cite('NTA ss.22–24', NTA)),
    ('capital_allowances', r'initial allowance|investment allowance|rural investment|66\s*(?:2/3|⅔)|two.thirds|capital allowance.*restrict|capital allowances.*restrict',
     'The paper uses the old capital-allowance structure. NTA 2025 s.27 and '
     'First Schedule Part I provide the current annual capital allowances; '
     'the general initial/investment/rural-investment allowances and the '
     'blanket two-thirds-of-assessable-profit restriction are not the '
     'current Part I computation. Petroleum provisions and transitional '
     'balances require their own schedule treatment. ' + cite('NTA s.27 and First Schedule', NTA)),
    ('pioneer', r'pioneer|industrial development.*income tax relief',
     'The old pioneer certificate/tax-holiday framework is historical. NTA '
     '2025 Chapter Eight replaces it with the economic development incentive '
     'certificate and qualifying-expenditure tax-credit regime (including '
     'transitional treatment for existing incentives). A printed four-plus-two '
     'or three-plus-two-year pioneer holiday is not a new certificate under '
     'the current regime. ' + cite('NTA ss.165–183, 195, 198', NTA)),
    ('registration_penalty', r'failure to register|fails? to register',
     'The old registration penalty is superseded. Failure to register under '
     'NTAA s.4 attracts ₦50,000 in the first month and ₦25,000 for each '
     'subsequent month of default. ' + cite('NTAA s.100', NTAA)),
    ('returns_penalty', r'fails? to file|failure to file|defaulting company.*returns|non.compliance.*55\(3\)|employer.*fine|employer.*penalt',
     'The printed filing fine is historical. Under NTAA s.101, failure/refusal '
     'to file, or knowingly filing incomplete/inaccurate returns, attracts '
     '₦100,000 in the first month and ₦50,000 in each subsequent month. '
     'Employer PAYE returns are governed by s.14; this is not the old fixed '
     '₦500,000 corporate-employer fine. ' + cite('NTAA ss.14, 101', NTAA)),
    ('records_penalty', r'failure to keep proper records|fails? to keep.*records|penalty.*keep.*records',
     'The printed monthly VAT record-keeping fine is superseded. NTAA s.102 '
     'provides an administrative penalty of ₦10,000 for a person other than '
     'a company and ₦50,000 for a company. ' + cite('NTAA ss.31, 102', NTAA)),
    ('technology_penalty', r'prevents?.*(?:access|records)|daily administrative penalty',
     'The printed ₦25,000 daily obstruction figure is historical. For refusing '
     'access to deploy technology after 30 days’ notice, NTAA s.103 specifies '
     '₦1m on the first day and ₦10,000 for each subsequent day. This '
     'provision concerns technology access; other obstruction offences '
     'must be identified separately. ' + cite('NTAA s.103', NTAA)),
    ('deduction_penalty', r'failure to (?:deduct|withhold|collect)|fails? to (?:deduct|withhold|collect)|failure to.*remit|fails? to.*remit',
     'Distinguish non-deduction from non-remittance. NTAA s.105 imposes 40% '
     'of tax not deducted/collected. Under s.107, tax deducted but not '
     'remitted by the following month’s 21st attracts the tax, a 10% per '
     'annum penalty and CBN monetary-policy-rate interest, with separate '
     'conviction provisions. The old flat fine/150% formulation is historical. ' + cite('NTAA ss.105, 107', NTAA)),
    ('address', r'change (?:in |of )?address|deregister|deregistration|de.?registered',
     'The old VAT-only notice/penalty is historical. NTAA ss.9–10 require '
     'notice of changes and permanent cessation within 30 days. Section 112 '
     'provides ₦100,000 for the first month of default and ₦50,000 for each '
     'subsequent month. ' + cite('NTAA ss.9–10, 112', NTAA)),
    ('registration_time', r'(?:register|registration).*?(?:six|6|eighteen|18|months|commencement)|vatable person.*register',
     'The old six/eighteen-month registration window is not the current '
     'registration rule. NTAA s.4 requires every taxable person to register '
     'and obtain a Tax ID; s.10 governs suspension/deregistration. Company '
     'return deadlines under s.11 are separate from registration. ' + cite('NTAA ss.4, 10–11', NTAA)),
    ('remittance_time', r'(?:withholding|\bWHT\b).*?(?:remittance|remit|returns|time limit|following month|30 days)|time limit.*withholding',
     'The old individual-WHT end-of-month/30-day deadline must not be '
     'used as the general current rule. NTAA s.107 identifies the 21st day '
     'of the immediately following month for non-remittance liability. '
     'Returns for deductions at source are governed by s.28. ' + cite('NTAA ss.28, 107', NTAA)),
    ('pre_operation', r'pre.?operation|pre.?operational|yet to commence operation',
     'The old pre-operation levy for a company seeking a TCC is historical. '
     'NTAA s.72 issues a TCC when assessed tax is paid or no tax is due, '
     'within two weeks of demand (or reasons for refusal). It contains '
     'no equivalent ₦20,000/₦25,000 pre-operation levy. ' + cite('NTAA s.72', NTAA)),
    ('bank_returns', r'banks?.*(?:new customers|submit a return)|names and addresses of new customers',
     'The old monthly new-customer return within seven days is historical. '
     'NTAA s.29 provides annual information returns by financial institutions '
     'for specified customer/transaction thresholds, plus information '
     'requested by the authority. ' + cite('NTAA s.29', NTAA)),
    ('joint_board', r'joint tax board|\bJTB\b',
     'This refers to the former Joint Tax Board. The Joint Revenue Board '
     'of Nigeria (Establishment) Act 2025 ss.3–5 now establish the JRB, '
     'its composition and functions; the NRS Executive Chairman chairs the JRB. Its First Schedule governs proceedings '
     'and quorum. A PITA section number or the former seven-member quorum '
     'is not the current statutory reference. ' + cite('JRB Act ss.3–5 and First Schedule', JRB)),
    ('firs', r'\bFIRS\b|FIRSB|federal inland revenue|federal board of inland revenue',
     'The printed authority name is historical. The Nigeria Revenue Service '
     '(Establishment) Act 2025 establishes NRS in place of FIRS. NTAA s.3 '
     'sets its jurisdiction, including company taxes and the specified '
     'federal individual categories; State/FCT jurisdiction continues '
     'under that section. Today use **Nigeria Revenue Service (NRS)** where '
     'the paper names FIRS. ' + cite('NRS Act', NRS) + '; ' + cite('NTAA s.3', NTAA)),
    ('benefit_accommodation', r'official quarters|rateable value.*quarter|residential accommodation.*benefit',
     'The old official-quarters percentage/formulation must not be applied '
     'unchanged. NTA s.14(6) values employer-provided accommodation at its '
     'annual rental value, capped at 20% of annual gross employment income '
     'excluding that rental value. ' + cite('NTA s.14(6)–(7)', NTA)),
    ('wht_construction', r'(?:withholding|\bWHT\b).*construction|construction.*(?:withholding|\bWHT\b|tax rate)|roads.*bridges.*(?:withholding|\bWHT\b)',
     'The old 2.5% construction WHT is superseded by the 2024 Deduction '
     'of Tax at Source Regulations, First Schedule (implemented January '
     '2025): roads/bridges/buildings/power plants use 2% for residents and '
     '5% for non-residents. Other construction/related activities have '
     'separate 5%/10% rates. Residence, classification and exemptions matter. '
     + cite('2024 Regulations implementation', WHT) + '; '
     '[2026 study text rates](#/s/TAX/9?sec=9-10)'),
    ('wht_supply', r'contract of suppl|contracts of suppl',
     'The printed general 5% supplies rate is historical. The 2024 '
     'Withholding Regulations, First Schedule use 2% for resident recipients '
     'and 5% for non-residents on general goods/material supplies, subject '
     'to the specified exclusions (including qualifying manufacturer/'
     'producer supplies). ' + cite('2024 Regulations implementation', WHT) + '; '
     '[2026 rates](#/s/TAX/9)'),
    ('partnership_interest', r'absence of a partnership agreement.*interest|absence of.*deed.*interest',
     'Key inconsistency: several diets print 6%, while March 2026 prints 5%. '
     'The 2026 study text §17.3 gives **5% per annum on a partner’s advance '
     'beyond agreed capital**, absent agreement; there is no automatic '
     'interest on capital. Keep the printed key as a historical answer. '
     '[2026 partnership notes](#/s/TAX/17?sec=17-3)'),
]


def flatten(node):
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return ' '.join(flatten(value) for value in node)
    if isinstance(node, dict):
        return ' '.join(flatten(value) for value in node.values())
    return ''


def make_flags(papers, split_secb):
    flags, review = {}, []
    for paper in papers:
        code, diet = paper['subject'], paper['diet']
        short_solutions = {q['n']: q for q in paper['saq_solutions']}
        essays = split_secb(paper['secb_paper'])
        for kind, questions in (('mcq', paper['mcq']), ('saq', paper['saq']),
                                ('secb', paper['secb_solutions'])):
            for q in questions:
                key = (diet, code, kind, q['n'])
                notes, hits = [], []
                if kind == 'mcq':
                    stem = flatten(q['stem']) + ' ' + flatten(q.get('pre', []))
                    answer_key = paper['mcq_key'][str(q['n'])]
                    answer = ' '.join(flatten(q['options']['ABCDE'.index(letter)])
                                      for letter in answer_key.split('/')
                                      if len(letter) == 1 and letter in 'ABCDE'
                                      and 'ABCDE'.index(letter) < len(q['options']))
                    text = stem + ' ' + answer
                    if answer_key == 'BONUS':
                        notes.append('The official key awards a **bonus mark to every candidate**, '
                                     'including an unanswered question. Practice scoring follows that award.')
                    elif '/' in answer_key:
                        notes.append('The official key accepts **' + ' or '.join(answer_key.split('/')) +
                                     '**. Both answers are accepted in practice scoring.')
                    if q.get('printedN') and q['printedN'] != q['n']:
                        notes.append(f"The source prints question {q['printedN']}; it is displayed as "
                                     f"question {q['n']} to align with the source’s 1–30 answer key.")
                    if q.get('printedOptionLabels'):
                        notes.append('The source labels these five options F–J; the site labels them '
                                     'A–E in the same order to align with the official answer key.')
                    if key == ('2024-03', 'TAX', 'mcq', 25):
                        notes.append('Printed defect verified on PDF page 53: only four options A–D '
                                     'appear, and they do not supply a percentage for the stem. '
                                     'The official key’s A is preserved, rather than inventing a fifth option.')
                elif kind == 'saq':
                    text = flatten(q['body']) + ' ' + flatten(short_solutions[q['n']]['body'])
                else:
                    text = flatten(essays.get(q['n'], [])) + ' ' + flatten(q['solution'])
                text = re.sub(r'\s+', ' ', text)
                if code == 'TAX':
                    for rule, pattern, note in RULES:
                        if rule == 'minimum_tax' and re.search(r'shipping|air (?:and |or )?sea|air transport|sea transport', text, re.I):
                            continue
                        if re.search(pattern, text, re.I):
                            notes.append(note)
                            hits.append(rule)
                    # The governing statute changed even where the tested
                    # concept remains. Do not assert that every old rate changed.
                    if re.search(r'\bCITA\b|companies? income tax act', text, re.I):
                        notes.append('The CITA citation is historical: NTA 2025 s.195 repeals '
                                     'CITA. Current company income rules are in NTA Chapter Two '
                                     '(including ss.20–27 and 56); administration is under NTAA. '
                                     + cite('NTA s.195', NTA))
                        hits.append('cita_reference')
                    if re.search(r'\bPITA\b|personal income tax (?:\(amendment\) )?act', text, re.I):
                        notes.append('The PITA citation is historical: NTA 2025 s.195 repeals '
                                     'PITA. Use NTA Chapter Two for income/deductions and '
                                     'NTAA for administration. See the other note for any '
                                     'specific changed rate or allowance. ' + cite('NTA s.195', NTA))
                        hits.append('pita_reference')
                    if re.search(r'capital gains? tax|\bCGTA?\b', text, re.I):
                        notes.append('The standalone CGT framework is historical. NTA ss.33–55 '
                                     'now govern chargeable gains; the old flat 10% CGT rate '
                                     'is replaced by the applicable company/individual rates '
                                     'under ss.56 and 58. Repeal is in s.195. Exemptions and '
                                     'thresholds must be checked under the new provisions; '
                                     'the original period’s computation remains printed here. '
                                     + cite('NTA ss.33–58, 195', NTA))
                        hits.append('gains_framework')
                    if re.search(r'(?:value added tax|VAT) act', text, re.I):
                        notes.append('The VAT Act citation is historical. NTA s.195 repeals '
                                     'it; current VAT is NTA Chapter Six and NTAA s.22. '
                                     'The standard rate remains **7.5%** (NTA s.147), '
                                     'and the regular return remains due on the following '
                                     'month’s **21st** (NTAA s.22). Those unchanged figures '
                                     'must be distinguished from changed exemptions and '
                                     'input-credit rules. ' + cite('NTA Chapter Six', NTA) + '; '
                                     + cite('NTAA s.22', NTAA))
                        hits.append('vat_reference')
                    if re.search(r'stamp dut(?:y|ies) act', text, re.I):
                        notes.append('The Stamp Duties Act citation is historical: NTA s.195 '
                                     'repeals it. Current instruments/rates are in NTA '
                                     'Chapter Five and Ninth Schedule, with exemptions '
                                     'under s.184. Fixed/ad-valorem terminology remains '
                                     'usable; check a named instrument against that schedule. '
                                     + cite('NTA Chapter Five, s.184, Ninth Schedule', NTA))
                        hits.append('stamp_reference')
                if code in ('AUD', 'MAN') and re.search(r'CAMA.*(?:1990|2004)|(?:1990|2004).*CAMA|section\s+(?:331|357|358|359|360|361|362|364|368)\b', text, re.I):
                    notes.append('The CAMA 1990/2004 reference is historical. In CAMA 2020, '
                                 'proper accounting records are in s.374; appointment of '
                                 'auditors s.401; qualifications s.403; report/audit '
                                 'committee s.404; duties/powers s.407; remuneration '
                                 's.408; removal s.409; resignation s.412; negligence '
                                 's.415. Use the matching current provision rather than '
                                 'the old section number. ' + cite('CAMA 2020', CAMA))
                    hits.append('cama_reference')
                if code == 'AUD' and re.search(r'Insurance Act(?:,?\s+2003)?', text, re.I):
                    notes.append('The Insurance Act 2003 citation is historical. The '
                                 '**Nigerian Insurance Industry Reform Act 2025 (NIIRA) s.229** '
                                 'repealed and consolidated that framework. Use NIIRA’s '
                                 'current audit provisions (ss.33–34) rather than the old '
                                 'section number. [NAICOM’s Act]' 
                                 '(https://naicom.gov.ng/wp-content/uploads/2025/08/NIIRA-2025.pdf).')
                    hits.append('insurance_act')
                if code == 'AUD' and re.search(r'\bISQC\s*1\b|quality control.*ISA\s*220', text, re.I):
                    notes.append('Historical quality-control standard: **ISQM 1** replaced '
                                 'ISQC 1, alongside ISQM 2 and ISA 220 (Revised), effective '
                                 '15 December 2022. Read the old terminology separately '
                                 'from today’s system of quality management. '
                                 '[IAASB’s current framework]' 
                                 '(https://www.iaasb.org/focus-areas/quality-management).')
                    hits.append('quality_management')
                if key == ('2021-09', 'CA', 'secb', 4):
                    notes.append('Printed numerator typo in part (b)(i): actual hours are '
                                 '24 × 8 × 100 = **19,200**, not the 19,000 shown in the '
                                 'capacity fraction on the source page. Efficiency is '
                                 '18,000/19,200 = **93.75%**, activity is '
                                 '18,000/20,000 = **90%**, and capacity is '
                                 '19,200/20,000 = **96%**. Parts (ii) and (iii) supply '
                                 'different, independent ratios: their printed answers '
                                 '**93.75%** and **102.4%** are correct for those givens.')
                if key in {('2023-09', 'AUD', 'mcq', 13), ('2025-09', 'AUD', 'mcq', 12)}:
                    notes.append('Printed-key limitation: the paper excludes **value-for-money '
                                 'audit** from internal-audit duties. Internal audit can review '
                                 'economy, efficiency and effectiveness where included in its '
                                 'mandate; this is not an inherent exclusion. The historical '
                                 'key remains visible, but the options do not establish a '
                                 'universal exception. [Internal audit scope](#/s/AUD/8?sec=8-12); '
                                 '[IIA standards](https://www.theiia.org/en/standards/).')
                if key == ('2020-03', 'AUD', 'mcq', 15):
                    notes.append('Historical practice-list answer: “approximately three years” '
                                 'is the printed key for reuse of an ICQ. It is not a universal '
                                 'audit-standard validity period. The auditor must update the '
                                 'understanding and evidence for changes and the current audit. '
                                 '[Understanding controls](#/s/AUD/8?sec=8-5).')
                if code == 'TAX' and re.search(r'most productive.*tax|tax.*most productive', text, re.I):
                    notes.append('Historical ranking: the most productive tax depends on the '
                                 'revenue year, scope and data source. The printed petroleum '
                                 'profits-tax answer is not a timeless current-law ranking; '
                                 'no replacement ranking can be determined from this stem alone.')
                if notes:
                    flags[key] = '\n\n'.join(dict.fromkeys(notes))
                review.append({'key': '/'.join(map(str, key)), 'rules': hits,
                               'flagged': bool(notes)})
    return flags, review
