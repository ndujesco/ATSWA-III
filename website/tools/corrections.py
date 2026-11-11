"""ATSWA III retrieval seeds and explicit, reviewable question corrections.

Keys are (diet, subject, kind, ordinal). Source mistakes stay visible; flags
explain them. PIN/SEC_PIN are reserved for reviewed retrieval ambiguities.
"""

CHAPTER_KEYS = {
    'AUD': {
        1: 'assurance audit objectives history expectation gap fraud error reasonable absolute stewardship statutory non statutory',
        2: 'CAMA BOFIA regulation appointment removal resignation remuneration rights duties auditor qualification disqualification audit committee insurance',
        3: 'ethics integrity objectivity independence confidentiality professional competence misconduct advocacy familiarity intimidation self interest self review safeguards ICAN',
        4: 'liability negligence duty care tort contract criminal Caparo Hedley Byrne privity litigation liability limitation',
        5: 'planning materiality risk inherent detection control risk documentation working papers permanent current files memorandum engagement letter knowledge business',
        6: 'evidence verification reliability confirmation inspection observation enquiry recalculation reperformance expert representation letter external third party',
        7: 'sampling substantive compliance tests analytical procedures sample selection tolerable error statistical nonstatistical inventory assets liabilities subsequent events',
        8: 'internal control segregation duties authorisation approval safeguarding control environment internal check control questionnaire ICQ ICEQ flowchart walkthrough',
        9: 'public sector auditor general federation state public accounts committee PAC due process procurement bureau BPP council NCP appropriation government financial regulations',
        10: 'computer IT systems CAATs audit software test data embedded facilities online electronic processing application general controls password',
        11: 'report opinion qualified adverse disclaimer unmodified unqualified pervasive emphasis matter other matter key audit matters ISA 700 705 706',
        12: 'completion final review field work checklist engagement partner going concern subsequent events management letter outstanding matters',
    },
    'CA': {
        1: 'cost accounting objectives financial management accounting cost ascertainment accumulation analysis installation system scope',
        2: 'classification segregation codification cost centre unit fixed variable semi variable stepped high low regression direct indirect relevant sunk opportunity controllable',
        3: 'materials inventory stores stock FIFO LIFO AVCO weighted average EOQ economic order quantity reorder maximum minimum buffer procurement requisition purchase perpetual bin card ABC',
        4: 'labour remuneration wages payroll overtime idle time turnover piecework Halsey Rowan premium bonus incentive time rate',
        5: 'overhead allocation apportionment absorption reapportionment reciprocal service department machine hour blanket under over absorbed predetermined',
        6: 'integrated interlocking reconciliation cost ledger control accounts general ledger adjustment notional profit financial costing',
        7: 'job batch contract service operating operation costing retention notional profit work certified uncertified escalation equivalent passenger kilometre hotel transport',
        8: 'process costing equivalent units normal abnormal losses gains joint products byproducts split off separation scrap FIFO weighted average production report',
        9: 'marginal absorption contribution relevant decision make buy shutdown limiting factor scarce resource special order differential sunk opportunity',
        10: 'break even breakeven CVP cost volume profit margin safety target profit sales mix contribution ratio pv graph',
        11: 'investment appraisal payback accounting rate return ARR net present value NPV discount cash flow IRR capital budgeting time value profitability index',
        12: 'budget budgetary control master functional cash sales production materials purchasing flexible fixed forecast limiting factor principal budget factor zero based',
        13: 'standard costing variance price usage mix yield efficiency rate expenditure volume capacity idle ratio planning operational controllable',
        14: 'JIT just time kanban backflush lifecycle target costing advanced manufacturing technology AMT lean throughput TQM quality ABC activity based benchmarking balanced scorecard',
        15: 'cost reduction control value analysis engineering organisation methods work study method study work measurement cost audit productivity',
    },
    'TAX': {
        1: 'taxation canons principles equity certainty convenience economy Adam Smith progressive regressive proportional direct indirect avoidance evasion history objectives tax base',
        2: 'administration authorities FIRS NRS federal inland revenue service state board joint tax revenue board local government committee jurisdiction JTB organs composition',
        3: 'ethics integrity objectivity confidentiality professional competence disclosure conflict interest IESBA threats safeguards',
        4: 'returns assessment collection registration tax identification number TIN ID payment due date filing penalties offence enforcement distrain instalments self assessment best judgement additional',
        5: 'objection appeal dispute tribunal TAT ombud advance ruling revision assessment notice refusal amend thirty days',
        6: 'clearance certificate TCC contents application issue refusal transactions three preceding years',
        7: 'VAT value added input output supply taxable exempt zero rated reverse charge consumption remittance registration invoice imported goods services',
        8: 'stamp duties instruments receipts ad valorem fixed stamping denoting embossing adjudication conveyance leases bills exchange',
        9: 'withholding deduction source WHT final advance franked investment dividend interest royalty royalties rent contracts remittance credit note',
        10: 'customs excise duties import export tariff NCS ECOWAS ETLS CET valuation clearance manufacturer levy importation',
        11: 'surcharge fossil fuel petroleum diesel petrol gas five percent pump price refined products',
        12: 'employment salary wages PAYE benefits kind accommodation official quarters gratuity pension leave passage expatriate residence contract service',
        13: 'personal income tax PIT consolidated relief allowance CRA rent relief taxable income progressive bands exemptions deductions life assurance NHF NHIS pension children dependent',
        14: 'investment income rental property dividend interest unearned income royalty franked loan bonds contractor financed',
        15: 'sole trader self employed badges trade profession vocation commencement cessation basis period preceding current year accounts overlap',
        16: 'capital allowances initial annual investment allowance balancing allowance charge qualifying capital expenditure QCE acceptance certificate residual value written down depreciation restriction',
        17: 'partnership partner divisible profit salary interest capital shares agreement admission retirement',
        18: 'settlement trust estate settlor trustee beneficiary executor administrator discretionary fixed income children apportionment',
        19: 'loss relief losses carry forward current year commencement cessation change accounting date recoupment',
        20: 'assessable profit adjusted disallowable allowable expenses wholly exclusively necessarily reasonably deductions CITA companies income tax turnover small medium large effective rate',
        21: 'companies income tax CIT total profit dividend minimum tax deemed profit turnover basis computation donations limitation relief',
        22: 'specialised businesses insurance banking mining agricultural pioneer incentives economic development zone export processing petroleum upstream midstream downstream shipping aviation nonresident digital',
        23: 'development levy FDL education tax tertiary TET TETFUND police trust NITDA NASENI assessable profit distribution',
        24: 'chargeable gains capital gains CGT disposal assets consideration loss office compensation rollover replacement exemption shares fifty million',
        25: 'information technology digital tax TaxPro Max Rev360 efiling epayment SEP electronic data automation technology',
    },
    'MAN': {
        1: 'business environment stakeholders social responsibility ethics governance primary secondary tertiary extractive manufacturing services size growth PEST SWOT objectives resources failure',
        2: 'management theories thought Taylor Fayol Weber Mayo scientific administrative bureaucracy human relations contingency systems Mintzberg skills roles levels school principles',
        3: 'planning plans decision making organising coordination controlling delegation span control authority responsibility accountability strategy strategic policy objectives forecasting PERT structure matrix line staff',
        4: 'human resource recruitment selection placement induction training development appraisal job analysis specification evaluation remuneration production marketing mix product pricing promotion distribution finance accounting functions',
        5: 'motivation Maslow Herzberg McGregor Vroom leadership leader Blake Mouton group teams conflict attitude communication sender receiver encoding decoding emotional intelligence change Lewin',
        6: 'business process reengineering BPR redesign radical processes Hammer Champy implementation benefits limitations',
        7: 'organisational effectiveness components factors strategies efficiency flexibility adaptation responsiveness',
        8: 'office practice procedures layout filing records registry machines furniture health safety hazards protective ergonomic organisation methods work study',
        9: 'mentoring mentor coach coaching outsourcing freelancer knowledge management talent succession diversity inclusion remote virtual contemporary',
        10: 'entrepreneur entrepreneurship innovator creativity enterprise risk initiative opportunity venture qualities types intrapreneur',
    },
}

from citation_reviews import reviewed_pins

PIN, SEC_PIN = reviewed_pins()
KEY_CORRECTIONS = {
    ('2022-03', 'CA', 'mcq', 8): 'B/D',
    ('2022-03', 'CA', 'mcq', 19): 'A',
    ('2022-03', 'CA', 'mcq', 6): 'A',
    ('2019-09', 'CA', 'mcq', 10): 'E',
    ('2024-09', 'MAN', 'mcq', 10): 'D',
    ('2025-09', 'MAN', 'mcq', 5): 'C',
    ('2026-03', 'TAX', 'mcq', 6): 'D',
}
SAQ_CORRECTIONS = {
    ('2020-03', 'AUD', 'saq', 4): ['Audit programme'],
    ('2019-09', 'MAN', 'saq', 1): ['Sole proprietorship / sole trader'],
    ('2024-09', 'CA', 'saq', 10): ['Relevant cost'],
    ('2019-09', 'CA', 'saq', 9): ['Last-in, first-out (LIFO)'],
    ('2023-03', 'CA', 'saq', 11): ['Fixed overhead capacity variance'],
    ('2025-09', 'CA', 'saq', 12): ['₦12,000 favourable'],
    ('2025-09', 'MAN', 'saq', 16): ['Process layout / functional layout'],
}
FLAGS = {
    ('2026-03', 'TAX', 'mcq', 6):
        'Printed key defect: **C, a person experienced in tax laws and '
        'administration**, is printed. **D, the Supervisor for Finance**, '
        'is the chair required by NTAA 2025 s.93(2)(a), consistent with '
        'the September 2024 MCQ 6 key. Experience in revenue matters is '
        'specified for the two other nominated members under s.93(2)(c). '
        'The reviewed key is D; the source C remains visible. '
        '[NTAA s.93](https://nass.gov.ng/documents/download/11250).',

    ('2019-09', 'MAN', 'saq', 1):
        'Printed term defect: the source says **Sole partnership**. A business '
        'owned, managed and controlled by one individual is a **sole '
        'proprietorship/sole trader**. A partnership involves more than one '
        'person. The original phrase remains visible beside the reviewed '
        'study answer. [Ownership forms](#/s/MAN/1?sec=A-12).',
    ('2020-03', 'MAN', 'mcq', 30):
        'Defective grid options: the printed key is **B, 1:9 country club**, '
        'which gives high concern for people and low concern for production. '
        'A balanced moderate position is **5:5 middle-of-the-road**; high '
        'concern for both is **9:9 team management**. Option E mislabels 9:9 '
        'as impoverished (the impoverished position is 1:1). The stem and '
        'options do not give a clean intended answer. Read the grid '
        'distinctions rather than memorising the printed B. '
        '[Leadership styles](#/s/MAN/5?sec=B-3).',
    ('2024-03', 'AUD', 'saq', 17):
        'Acronym ambiguity: the printed answer **International Data Encryption '
        'Algorithm** is a real cryptographic expansion of IDEA. In audit '
        'software/CAAT usage, IDEA means **Interactive Data Extraction and '
        'Analysis**, as March 2026 short answer 1 states. The broad IT-based '
        'assurance stem does not distinguish them; retain the printed '
        'cryptographic answer while learning the audit-software meaning. '
        '[IT trends](#/s/AUD/10?sec=10-9).',

    ('2019-09', 'CA', 'mcq', 10):
        'Printed key inconsistency: the source gives **B, Cost driver**. '
        'The collection/focus in which activity costs are accumulated is a '
        '**cost pool (E)**. A cost driver is the factor used to explain or '
        'assign those costs. March 2022 short answer 13 keys the same '
        'definition as cost pools. [ABC](#/s/CA/5?sec=5-8).',

    ('2022-03', 'CA', 'mcq', 6):
        'Printed key defect: **D, Book value of premises** is printed. '
        '**A, Floor area** is the appropriate shared basis for rates and '
        'cleaning costs in the stated question. The reviewed practice key is A; '
        'the original D remains visible. [Apportionment bases](#/s/CA/5?sec=5-3).',
    ('2019-09', 'CA', 'saq', 9):
        'Printed key defect: **FIFO** is printed, but the stem says the '
        '**most recent purchase is issued first**. That describes **LIFO**. '
        'The reviewed study answer uses LIFO and retains the printed FIFO '
        'separately. [Material issue pricing](#/s/CA/3?sec=3-5).',
    ('2023-03', 'CA', 'saq', 11):
        'Printed key defect: the comparison of **budgeted hours and actual '
        'hours** is a **fixed overhead capacity variance**. Efficiency compares '
        '**standard hours for actual output and actual hours**. The source '
        'prints “efficiency”; the reviewed study answer identifies capacity. '
        '[Fixed overhead variances](#/s/CA/13?sec=13-4).',
    ('2025-09', 'CA', 'saq', 12):
        'Printed sign defect: the source gives **₦12,000 adverse**. The '
        'standard rate is ₦120,000 ÷ 60,000 = ₦2 per hour; standard hours for '
        'actual output are 55,000 × 1.2 = 66,000. Thus (66,000 − 60,000) × '
        '₦2 = **₦12,000 favourable**, because output absorbs more fixed '
        'overhead than budgeted. [Overhead variances](#/s/CA/13?sec=13-4).',
    ('2025-09', 'MAN', 'saq', 16):
        'Printed key defect: grouping machines that perform **similar '
        'operations together** defines a **process/functional layout**. A '
        'product/line layout follows the product’s sequence of operations. '
        'The source prints product/line layout; the reviewed study answer '
        'corrects that reversal. [Layouts](#/s/MAN/4?sec=B-6).',
    ('2024-09', 'MAN', 'mcq', 10):
        'Printed key defect: **C, Degradation** is the official key. '
        'Minimising waste and ensuring environmental compliance is '
        '**D, Environmental management**; degradation means deterioration. '
        'Study practice uses D and displays the original key separately. '
        '[Environmental responsibility](#/s/MAN/1?sec=C-1).',
    ('2025-09', 'MAN', 'mcq', 5):
        'Printed key inconsistency: the source selects **B, Recruitment '
        'and separation**, although those decisions directly concern how '
        'the organisation treats employees. **C, Conflict of interest** '
        'belongs to how an employee’s interests affect the organisation. '
        'This distinction is set out in the study text’s business-ethics '
        'categories. The reviewed key is C. [Business ethics](#/s/MAN/1?sec=C-2).',
    ('2021-09', 'CA', 'mcq', 9):
        'Question/key limitation: the official answer is **B, Differential '
        'Piece Rate Plan**. Indirect work normally has no separately '
        'measurable units for individual piece-rate payment; a **time-rate '
        'basis** is normally suitable. None of the options plainly states '
        'time-rate pay. Treat the printed B as this paper’s historical key, '
        'not a general rule for indirect workers. [Wage methods](#/s/CA/4?sec=4-3).',
    ('2024-09', 'CA', 'saq', 10):
        'Printed key defect: the source answers **Irrelevant Cost**, but the stem '
        'describes a cash outlay that can be avoided by a decision and used in '
        'selling-price or make-or-buy decisions. That is a **Relevant cost**. '
        'The reviewed study answer is shown alongside the original printed answer. '
        '[Relevant costs](#/s/CA/9?sec=9-3).',
    ('2020-09', 'MAN', 'mcq', 14):
        'Printed formula defect, checked against the original PDF page 81: the '
        'numerator reads **income before taxes − interest expense**. The intended '
        'ratio, **times interest earned (C)**, is profit **before interest and tax** '
        'divided by interest expense. Starting with profit before tax, **add** '
        'interest back rather than subtracting it. The printed formula and key '
        'remain visible. [ICAN’s interest-cover explanation]'
        '(https://icanig.org/ican/assets/docs/pro-study-texts-2021/SFM.pdf); '
        '[Finance ratios](#/s/MAN/4?sec=D-3).',
    ('2022-03', 'CA', 'mcq', 8):
        'Printed key defect: the official key gives **C, Market Value of Production**. '
        'Prime cost plus production overhead gives **production cost (B)**; prime cost '
        'plus all indirect costs gives **total cost (D)**. Market value is not determined '
        'by adding costs. Because the stem does not qualify “Indirect Cost”, both B '
        'and D are defensible; study practice accepts those two reviewed answers and '
        'retains the printed C separately. [Cost composition](#/s/CA/2?sec=2-1-1).',
    ('2022-03', 'CA', 'mcq', 19):
        'Printed key defect: the source keys **C**, but the correct concept is **A**, '
        'an activity/factor that generates a cost. The same concept is keyed consistently '
        'in September 2020 Q1 and September 2022 Q24. Study practice uses A, while the '
        'original C remains visible. [Cost drivers](#/s/CA/5?sec=5-8).',
    ('2020-03', 'AUD', 'saq', 4):
        'Printed key inconsistency: this diet gives **Test of controls** for this stem. '
        'The corresponding definition is **Audit programme**, as the March 2022 '
        'short-answer Q4 key also states. The reviewed study answer is Audit programme; '
        'the historical printed answer is retained separately. [Audit planning](#/s/AUD/5?sec=5-1).',
}
