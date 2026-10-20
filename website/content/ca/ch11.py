CH = {
 'n': 11,
 't': 'Simple Investment Appraisal Techniques',
 'brief': 'Capital budgeting — planning expenditure whose benefits stretch beyond a year — and '
          'the techniques used to appraise it: the traditional Payback Period and Accounting '
          'Rate of Return methods, and the discounted-cash-flow Net Present Value method, which '
          'properly accounts for the time value of money. Every illustration independently '
          'verified, with two genuine source data errors caught and corrected.',
 'outcomes': [
   'Appreciate the concept of capital budgeting',
   'Explain the nature and role of capital budgeting decisions',
   'Identify and discuss the traditional methods of appraising investment, and one Discounted '
   'Cash Flow (DCF) technique (NPV)',
   'Appreciate the necessity of capital budgeting in long-term decision making',
 ],
 'secs': [
  {'n': '11.1', 't': 'Introduction — the concept of capital budgeting', 'b': [
    {'def': {'t': 'Capital budgeting', 'd': 'the planning of expenditure whose returns extend '
                  'beyond one year — deciding whether to commit resources to a project whose '
                  'benefits are spread across several future periods.'}},
    {'p': 'Its primary task is correlating benefits with costs rationally, in line with the '
          'enterprise\'s profit-maximising goal. These are among the most critical managerial '
          'decisions, needing careful estimation and forecasting — the choice of which '
          'long-term projects to finance is purely a managerial one.'},

  ]},

  {'n': '11.1.2', 't': 'The objectives of capital budgeting', 'b': [
    {'ol': [
      'a capital investment commits resources to the future, **reducing financial flexibility** '
      '— an asset with a decade-long life means waiting a long time before its benefits '
      'materialise;',
      'asset expansion is tied to future sales, so the asset\'s economic life is really an '
      'indirect **sales forecast** — poor forecasting risks over- or under-investment, each with '
      'real costs (unnecessary financial burden, or inadequate capacity);',
      'good capital planning improves the **timing and quality** of asset acquisition — demand '
      'for capital goods is intermittent, but supplying them takes a long lead time, so matching '
      'need to availability is itself a capital-budgeting function; and',
      'asset expansion needs **substantial funds** that are not automatically available — a '
      'sizeable capital programme needs financing arranged well in advance.',
    ]},
    {'note': 'Capital budgeting is not routine clerical work — it needs continuous, informed '
             'judgement from engineers, cost analysts, economists and others competent to weigh '
             'the many variables involved (product quality, output quantity, labour quality/'
             'quantity, scrap, maintenance, down-time, safety, flexibility).'},

  ]},

  {'n': '11.1.3', 't': 'Data for capital expenditure decisions', 'b': [
    {'p': 'Only **future** costs are relevant — recorded (historical) costs matter only as a '
          'starting point for projecting future costs. Every estimated cost relevant to the '
          'project should be included: expected material savings (especially from reduced '
          'scrap), changes in direct labour/materials/handling/inspection, and anticipated '
          'changes in specific overheads (tax, insurance, power, maintenance, repairs, '
          'supplies).'},
    {'warn': 'Avoid simply applying the existing plant overhead rate — new equipment is often '
             'more automated than the old, producing a genuinely different cost pattern: less '
             'supervision/overtime (costs that vary with direct labour) but more repairs/'
             'maintenance/power (costs that vary with machine usage).'},

  ]},

  {'n': '11.1.4', 't': 'Opportunity and interest costs', 'b': [
    {'p': 'Opportunity cost — the alternative income lost by choosing this project — is central '
          'to capital budgeting. In an expansion project, use the **economic** (not book) value '
          'of the space required; in a replacement decision, treat the realisable value of the '
          '**existing** asset as reducing the cost of replacement.'},
    {'key': 'Return on investment is really two things: **interest** (the pure cost of money — '
            'the minimum acceptance criterion, since a firm must at least recover its cost of '
            'capital before any profit) and **profit** (the reward for risk and uncertainty, '
            'which varies with the specific risk being taken on).'},
    {'p': 'On depreciation: for a **replacement** decision, depreciation of an existing asset\'s '
          'unabsorbed book value is a **sunk cost**, irrelevant except for its tax effect — only '
          'the asset\'s current economic value matters. Differential revenue (where it can be '
          'measured) must also be considered — both the asset\'s own capacity and the '
          'marketability of any increased output it enables.'},
  ]},

  {'n': '11.2', 't': 'Capital budgeting methods', 'b': [
    {'p': 'Firms usually have more capital-project proposals than they can or will finance, '
          'needing a screening/ranking procedure that relates a stream of future earnings to '
          'the cost of obtaining them. Five widely-used methods:'},
    {'ol': [
      'Payback Period (PBP) method;', 'Accounting Rate of Return (ARR) method;',
      'Net Present Value (NPV) method;', 'Profitability Index (PI) method; and',
      'Internal Rate of Return (IRR) method.',
    ]},
    {'note': 'PI and IRR are outside this syllabus\'s coverage at this level — only NPV is '
             'treated in detail, alongside the two traditional (non-discounting) methods, PBP '
             'and ARR.'},

  ]},

  {'n': '11.2.1', 't': 'Payback Period (PBP) method', 'b': [
    {'def': {'t': 'Payback Period', 'd': 'the number of years required to recover the original '
                  'investment from the project\'s savings/cash proceeds before depreciation but '
                  'after tax — how long it takes a project to "pay for itself."'}},
    {'tex': '\\text{Payback Period} = \\dfrac{\\text{Cost of Investment}}{\\text{Annual Cash '
            'Flow}}'},
    {'key': 'Investments are ranked by payback length — **shorter is more desirable**.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 11.1 — comparing two projects by payback',
      'open': True, 'q': [
      {'p': 'N10,000 is available to invest in either Project A or Project B. Savings before '
            'depreciation:'},
      {'table': {'align': 'lrr', 'head': ['Year', 'Project A (N)', 'Project B (N)'], 'rows': [
        ['1', '5,000', '1,000'], ['2', '4,000', '2,000'], ['3', '3,000', '3,000'],
        ['4', '1,000', '4,000'], ['5', '—', '5,000'], ['6', '—', '6,000'],
      ]}},
      {'p': 'Which project is more viable on payback?'}],
      'a': [
      {'warn': 'The study text\'s own solution table swaps these two cash-flow streams between '
               'its "Project A" and "Project B" columns, contradicting the problem statement '
               'printed just above it — its final conclusion ("Project B preferred, payback '
               '2.33 years, vs Project A\'s 4 years") is only consistent with the **labels used '
               'in its solution table**, which are the reverse of the labels used in the '
               'problem itself. Below, the labels A/B follow the **problem statement** exactly '
               'as printed above (A = front-loaded 5,000/4,000/3,000/1,000; B = back-loaded '
               '1,000/2,000/3,000/4,000/5,000/6,000) — so the conclusion below is stated '
               'correctly for *those* labels, not copied from the source\'s own mislabelled '
               'solution table.'},
      {'table': {'align': 'lrrrr', 'head': ['Year', 'A cash flow', 'A cumulative', 'B cash flow',
        'B cumulative'], 'rows': [
        ['0', '(10,000)', '(10,000)', '(10,000)', '(10,000)'],
        ['1', '5,000', '(5,000)', '1,000', '(9,000)'],
        ['2', '4,000', '(1,000)', '2,000', '(7,000)'],
        ['3', '3,000', '2,000', '3,000', '(4,000)'],
        ['4', '1,000', '3,000', '4,000', '0'],
        ['5', '—', '', '5,000', '5,000'],
        ['6', '—', '', '6,000', '11,000'],
      ]}},
      {'p': 'Project A breaks even **during year 3** (deficit of 1,000 at the start of year 3, '
            'against a year-3 inflow of 3,000): $\\text{PBP}_A = 2 + \\tfrac{1{,}000}{3{,}000} '
            '\\approx 2.33$ years. Project B breaks even **exactly at the end of year 4**: '
            '$\\text{PBP}_B = 4$ years.'},
      {'key': '**Project A is preferred** — it recovers the N10,000 investment in about 2.33 '
              'years, well ahead of Project B\'s 4 years.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 11.2 — payback period, before and after tax',
      'open': True, 'q': [
      {'p': 'Koki Nig. Plc compares machines Damsel (N300,000, 10-year life) and Shylock '
            '(N500,000, 12-year life). Tax is 50% of profit.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['', 'Damsel (N)', 'Shylock (N)'], 'rows': [
        ['Savings — scrap', '20,000', '30,000'],
        ['Savings — wages (150 × 1,200; 200 × 1,200)', '180,000', '240,000'],
        ['**Total savings**', '**200,000**', '**270,000**'],
        ['Less: indirect materials', '12,000', '16,000'],
        ['Less: supervision', '24,000', '32,000'],
        ['Less: maintenance', '14,000', '22,000'],
        ['**Savings before depreciation**', '**150,000**', '**200,000**'],
        ['Less: depreciation (cost ÷ life)', '30,000', '41,667'],
        ['**Savings after depreciation**', '**120,000**', '**158,333**'],
        ['Less: tax @ 50%', '60,000', '79,167'],
        ['**Net savings (after tax)**', '**60,000**', '**79,167**'],
        ['Add back depreciation → annual cash flow', '90,000', '120,834'],
      ]}},
      {'table': {'align': 'lrr', 'head': ['Payback period', 'Damsel', 'Shylock'], 'rows': [
        ['Before tax (cost ÷ savings before depreciation)', '2 years', '2.5 years'],
        ['After tax (cost ÷ annual cash flow)', '3.3 years', '~4.1 years'],
      ]}},
      {'key': '**Machine Damsel is recommended** — it has the shorter payback period on both a '
              'before-tax and after-tax basis, even though Shylock has the higher Accounting '
              'Rate of Return (Illustration 11.3 shows the same tension can arise between the '
              'two methods).'}]}},
    {'h4': '11.2.2 Advantages and 11.2.3 Disadvantages of the payback period method'},
    {'table': {'align': 'll', 'head': ['Advantages of PBP', 'Disadvantages of PBP'], 'rows': [
      ['Easy to understand and simple to operate; its short-term focus reduces the risk of loss '
       'through obsolescence; useful for a cash-short firm that must prioritise a quick return '
       'of funds; uses actual project **cash flows**, not accounting profit, making it more '
       'objective than ARR.', 'Ignores cash flows **beyond** the payback period entirely — '
       'penalising long-gestation projects (new products, new markets) that pay off big, just '
       'later; ignores the **time value of money**, treating a Naira received in year 1 the '
       'same as one received in year 5.'],
    ]}},
    {'note': 'Despite its weaknesses, payback remains the **most popular** appraisal technique '
             'in practice, especially with investors (foreign and local) in developing economies.'},

  ]},

  {'n': '11.3', 't': 'Accounting Rate of Return (ARR) method', 'b': [
    {'def': {'t': 'Accounting Rate of Return (ARR)', 'd': 'average earnings after depreciation '
                  'over the project\'s economic life, divided by the capital invested — i.e. '
                  'average return ÷ average (or initial) investment.'}},
    {'note': '"Capital invested" can mean the **initial** investment, or the **average** '
             'investment over the project\'s life — often taken as (initial investment + '
             'salvage value) ÷ 2.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 11.3 — ARR on initial vs average capital',
      'open': True, 'q': [
      {'p': 'Gidauniya Ltd compares Project A (N1,000 investment, 4-year life, N250/year '
            'depreciation) and Project B (N1,000 investment, 6-year life, N167/year '
            'depreciation). Earnings after depreciation total N300 (A) and N1,098 (B) over '
            'their respective lives. Find the ARR on (i) initial capital, (ii) average capital.'}],
      'a': [
      {'p': '**(i) On initial capital**: average profit A $= 300/4 = N75$/year; B $= 1{,}098/6 '
            '= N183$/year.'},
      {'tex': '\\text{ARR}_A = \\dfrac{75}{1{,}000} \\times 100 = 7.5\\% \\qquad '
              '\\text{ARR}_B = \\dfrac{183}{1{,}000} \\times 100 = 18.3\\%'},
      {'p': '**(ii) On average capital** (assuming zero salvage, average $= 1{,}000/2 = N500$ '
            'for both):'},
      {'tex': '\\text{ARR}_A = \\dfrac{75}{500} \\times 100 = 15\\% \\qquad \\text{ARR}_B = '
              '\\dfrac{183}{500} \\times 100 \\approx 37\\%'},
      {'key': '**Project B is preferred on ARR** (higher return, either basis) — but '
              'Project A\'s earnings come *faster* (breaks even within year 3, versus B\'s '
              'exactly year 4), so the **payback method would favour A instead**. ARR and '
              'payback can genuinely disagree, because ARR uses accounting profit over the '
              '*whole* life while payback only cares how quickly the *original outlay* is '
              'recovered.'}]}},
    {'h4': '11.3.1 Advantages and 11.3.2 Disadvantages of the accounting rate of return'},
    {'table': {'align': 'll', 'head': ['Advantages of ARR', 'Disadvantages of ARR'], 'rows': [
      ['Very easy to calculate; takes savings into account over the **entire** economic life; '
       'embodies "net earnings" (post-depreciation), a genuinely useful concept for appraisal.',
       'Shares payback\'s fundamental weakness — it ignores that cash flows/outflows occur at '
       '**different times**; uses accounting profit, which is more subjective than cash flow; '
       'has several variants (different definitions of "investment" and "earnings"), each '
       'producing a *different* rate for the same proposal.'],
    ]}},
  ]},

  {'n': '11.4', 't': 'Discounted Cash Flow (DCF) methods, and the Net Present Value method (11.5)', 'b': [
    {'p': 'DCF methods use cash flows and **automatically account for the time value of '
          'money** — a Naira received today is worth more than the same Naira received later, '
          'since money received now can itself start earning a return. Values arising at '
          'different times are not directly comparable; they must be converted to a common '
          'date\'s equivalent value using a **discount factor**.'},
    {'def': {'t': 'Net Present Value (NPV) method', 'd': 'establishes a target minimum '
                  'acceptable rate of return, then finds whether the present value of expected '
                  'future cash inflows (discounted at that rate) exceeds the cost of the '
                  'proposal.'}},
    {'key': '**Decision rule: accept a project with a positive NPV.** A zero NPV means the '
            'project earns *exactly* the target rate; a negative NPV means it earns *less* than '
            'the target rate and should be rejected.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 11.4 — a straightforward NPV calculation',
      'open': True, 'q': [
      {'p': 'A machine costing N150,000 (plus N10,000 working capital) improves cash flow by '
            'N60,000/year for 5 years, with zero residual value. Cost of capital 15%. Find the '
            'NPV.'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['Year', 'Cash flow (N)', 'Discount factor @15%',
        'Present value (N)'], 'rows': [
        ['0', '(160,000)', '1.0000', '(160,000)'],
        ['1', '60,000', '0.8696', '52,174'],
        ['2', '60,000', '0.7561', '45,369'],
        ['3', '60,000', '0.6575', '39,451'],
        ['4', '60,000', '0.5717', '34,305'],
        ['5', '60,000', '0.4972', '29,831'],
        ['**NPV**', '', '', '**41,130**'],
      ]}},
      {'p': '**Shortcut using the cumulative (annuity) discount factor for 5 years @15% '
            '(3.352)**: $60{,}000 \\times 3.352 = N201{,}120$; NPV $= 201{,}120 - 160{,}000 '
            '\\approx N41{,}120$ — matching the year-by-year total, within a small rounding '
            'difference from using a 3-decimal annuity factor instead of five separate '
            '4-decimal factors.'},
      {'key': '**Positive NPV of N41,130 — the project is worthwhile.** Alhaji Aminu earns '
              'more than his required 15% return on this investment. (A zero NPV would mean '
              'exactly 15%; a negative NPV would mean less than 15%, and the project should be '
              'rejected.)'}]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 11.5 — ARR and NPV together, with a '
      'disposal-value cash flow', 'open': True, 'q': [
      {'p': 'Garko Industries considers buying 10 delivery vans at N30,000 each (N300,000 '
            'total) instead of using a commercial carrier that currently charges N460,000/year. '
            'Running costs N40,000/van/year (N400,000 total). 6-year life, disposal proceeds '
            'N6,000/van (N60,000 total) at the end. Find the ARR and NPV at a 15% discount rate.'}],
      'a': [
      {'p': 'Net savings before depreciation $= 460{,}000 - 400{,}000 = N60{,}000$/year. '
            'Straight-line depreciation $= (300{,}000 - 60{,}000)/6 = N40{,}000$/year. Average '
            'savings after depreciation $= 60{,}000 - 40{,}000 = N20{,}000$/year.'},
      {'table': {'align': 'lr', 'head': ['Net book value at end of year (N\'000)', ''], 'rows': [
        ['1', '260'], ['2', '220'], ['3', '180'], ['4', '140'], ['5', '100'], ['6', '60'],
      ]}},
      {'p': 'Average investment $= (260+220+180+140+100+60)/6 = N160{,}000$.'},
      {'tex': '\\text{ARR} = \\dfrac{20{,}000}{160{,}000} \\times 100 = 12.5\\%'},
      {'table': {'align': 'lrrr', 'head': ['Year', 'Cash flow (N\'000)', 'Discount factor @15%',
        'PV (N\'000)'], 'rows': [
        ['0', '(300)', '1.000', '(300.00)'],
        ['1', '60', '0.870', '52.20'],
        ['2', '60', '0.756', '45.36'],
        ['3', '60', '0.658', '39.48'],
        ['4', '60', '0.572', '34.32'],
        ['5', '60', '0.497', '29.82'],
        ['6', '60', '0.432', '25.92'],
        ['6 (disposal proceeds)', '60', '0.432', '25.92'],
        ['**NPV**', '', '', '**(46.98)**'],
      ]}},
      {'key': '**Negative NPV (−N46,980) — the project is unacceptable** at a 15% required '
              'return, despite a respectable-looking 12.5% ARR. This is exactly why ARR and '
              'NPV can disagree: ARR never discounts for *when* the cash arrives, so it can '
              'make a project that genuinely destroys value at the required rate look '
              'acceptable.'}]}},
  ]},

  {'n': '11.6', 't': 'Chapter summary', 'b': [
    {'p': 'Simple investment appraisal techniques were examined in this chapter. The first two '
          'methods examined — the **Accounting Rate of Return** and the **Payback Period** '
          'methods, also known as the **traditional methods** — were found to be seriously '
          'imperfect, by their failure to take full account of the **time value of money**.'},
    {'p': 'The other three methods — **Net Present Value**, **Profitability Index** and '
          '**Internal Rate of Return** — are known as **discounted cash flow methods**, and are '
          'rated to be **superior** to the traditional methods, because they take full account '
          'of the time value of money.'},
    {'key': 'The one idea that separates the two families is that **a naira today is worth more '
            'than a naira next year** — it can be invested and earn a return in the meantime. '
            'Payback counts every naira equally wherever it falls in time and then ignores '
            'everything after the payback date; ARR works on accounting profit rather than cash '
            'and averages away the timing altogether. Only the discounted methods actually price '
            'the delay.'},
  ]},

  {'n': '11.7', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§11.1 Capital budgeting** — planning expenditure with returns beyond one year; 4 '
      'reasons it matters (reduced flexibility, indirect sales forecast, timing/quality of '
      'acquisition, financing lead time); only *future* costs are relevant; opportunity cost '
      'uses *economic* value; interest is the minimum-acceptance floor, profit is the reward '
      'for risk; replacement-decision depreciation on the *old* asset is sunk, irrelevant '
      'except for tax.',
      '**§11.2 Traditional methods** — Payback (cost ÷ annual cash flow, shorter is better; '
      'simple, uses real cash flow, but ignores post-payback flows and the time value of money '
      'entirely) and ARR (average post-depreciation profit ÷ initial or average investment; '
      'easy, whole-life view, but ignores timing and has multiple inconsistent variants) — the '
      'two can genuinely disagree, since one rewards *speed* of recovery and the other rewards '
      '*total* profitability.',
      '**§11.3 NPV** — the DCF method actually examinable at this level; discounts every future '
      'cash flow to present value at a target rate, sums them, and compares against the initial '
      'outlay; **accept if NPV is positive**; can flag a project ARR would wrongly approve, '
      'because it is the only one of the three that properly weighs *when* cash arrives.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Capital budgeting** — planning expenditure with multi-year returns.',
      '**Payback Period** — years to recover the original outlay from cash proceeds. '
      '**Accounting Rate of Return (ARR)** — average post-depreciation profit ÷ investment.',
      '**Net Present Value (NPV)** — sum of discounted future cash flows, less the initial '
      'outlay; positive NPV = accept.',
      '**Discount factor** — converts a future sum to its present-day equivalent value.',
      '**Sunk cost (in a replacement decision)** — the old asset\'s unabsorbed book value/'
      'depreciation; irrelevant except for tax effect.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'Investment appraisal formulas (recap)', 'rows': [
      {'lb': 'Payback Period', 'tex': '\\dfrac{\\text{Cost of Investment}}{\\text{Annual Cash '
        'Flow}}'},
      {'lb': 'Accounting Rate of Return', 'tex': '\\dfrac{\\text{Average annual profit after '
        'depreciation}}{\\text{Initial (or average) investment}} \\times 100'},
      {'lb': 'Net Present Value', 'tex': 'NPV = \\sum \\dfrac{\\text{Cash flow}_t}{(1+r)^t} - '
        '\\text{Initial outlay}'},
    ]}},
  ]},

  {'n': '11.8', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following is NOT crucial to the decision to commit huge funds into '
        'capital asset acquisition? (A) Finance availability  (B) Changes in the quality of '
        'the asset over time  (C) Installation costs  (D) Useful life and scrap value of the '
        'asset  (E) Maintenance expenses',
        'Which one of the following states the reason why opportunity cost is considered in '
        'capital budgeting decisions? (A) The benefit lost in the alternative use of the funds '
        'to be committed is important  (B) So that if the decision turned out to be faulty, the '
        'assets could be quickly disposed of and the proceeds diverted to alternative uses  '
        '(C) There may be problems defending the decisions at the company\'s Annual General '
        'Meeting  (D) The banks that will finance the capital project will demand for it  '
        '(E) It is government policy',
        'Which one of the following is NOT a method of appraising investment proposals? '
        '(A) Payback period  (B) Feasibility study  (C) Net Present Value  (D) Internal Rate of '
        'Return  (E) Accounting Rate of Return',
        'A system of expenditure planning which facilitates the decision-making process as '
        'regards committing resources to a project where benefits would be spread over a long '
        'time period is called ……………..',
        'The number of years required to recoup the amount originally invested in a project is '
        'known as ………...',
        'Using the Net Present Value (NPV) investment appraisal method, what would indicate '
        'that a project is worthwhile and therefore should be accepted?',
      ]}],
      'a': [
      {'ol': [
        '**C — installation costs** is the odd one out here (a real, relevant cost, but not '
        'itself a criterion crucial to the *commitment* decision the way B, D and E directly '
        'are, and A obviously is) — matching the study text\'s own answer key.',
        '**A** — the benefit lost in the alternative use of the funds is what makes opportunity '
        'cost important.',
        '**B — feasibility study** is not itself an investment-appraisal *method*, unlike the '
        'other four.',
        '**Capital budgeting.**',
        '**Payback period.**',
        '**A positive NPV.**',
      ]}]}},
  ]},

  {'n': '11.9', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with eight examination-type questions. All are '
          'reproduced below with full answers.'},

    {'eg': {'tag': 'Exam type — Q1', 't': 'Discuss briefly the payback or the ARR method',
      'q': [{'p': 'Several methods are employed by management accountants for ascertaining the '
                  'profitability of capital expenditure projects. Discuss briefly **one** of the '
                  'following methods: (a) the pay-back method; (b) the accounting rate of return '
                  'method.'}],
      'a': [
      {'note': 'Only one is required, but both are answered here so the chapter\'s coverage is '
               'complete.'},
      {'h4': '(a)  The payback method'},
      {'def': {'t': 'Payback period', 'd': 'the length of time required for the net cash inflows '
                    'from a project to recover the original cash outlay on it.'}},
      {'fbox': {'h': 'Payback period', 'rows': [
        {'lb': 'Even annual cash flows',
         'tex': '\\text{Payback period} = \\frac{\\text{Initial investment}}'
                '{\\text{Annual net cash inflow}}'},
        {'lb': 'Uneven cash flows',
         'tex': '\\text{Payback} = \\text{Years before full recovery} + '
                '\\frac{\\text{Amount still unrecovered}}'
                '{\\text{Cash inflow of the recovery year}}',
         'nt': 'Build a cumulative cash flow column and find the year in which it turns '
               'positive, then interpolate within that year.'},
      ]}},
      {'p': '**The decision rule:** accept a project whose payback period is shorter than the '
            'maximum period the company has set; where projects are mutually exclusive, choose '
            'the one with the **shortest** payback. It is a measure of **liquidity and risk**, '
            'not of profitability — it answers "how long is our money at risk?", not "how much '
            'will we make?"'},
      {'p': '**Advantages:** simple to compute and easy for non-financial managers to '
            'understand; emphasises early cash recovery, which matters to a business short of '
            'cash; reduces risk by favouring projects whose returns arrive sooner and are '
            'therefore more certain; useful where technology changes rapidly and distant cash '
            'flows are speculative; and it needs no estimate of the cost of capital.'},
      {'p': '**Disadvantages:** it **ignores the time value of money** (a naira in year 4 is '
            'counted the same as a naira in year 1); it **ignores all cash flows after the '
            'payback date**, so a project that pays back quickly and then stops is preferred to '
            'one that pays back slowly and then earns for a decade; it therefore measures '
            'liquidity rather than profitability and can reject value-creating projects; the '
            'target payback period is arbitrary; and it ignores the scale of the investment.'},
      {'h4': '(b)  The accounting rate of return method'},
      {'def': {'t': 'Accounting rate of return (ARR)', 'd': 'the average annual accounting '
                    'profit of a project expressed as a percentage of the capital invested in '
                    'it. Also called the return on capital employed or return on investment '
                    'method.'}},
      {'fbox': {'h': 'Accounting rate of return', 'rows': [
        {'lb': 'On initial investment',
         'tex': 'ARR = \\frac{\\text{Average annual profit}}'
                '{\\text{Initial investment}} \\times 100'},
        {'lb': 'On average investment',
         'tex': 'ARR = \\frac{\\text{Average annual profit}}'
                '{\\text{Average investment}} \\times 100',
         'nt': 'Average investment = (initial investment + scrap value) ÷ 2. The two versions '
               'give very different percentages, so always state which you have used.'},
      ]}},
      {'p': '**The decision rule:** accept a project whose ARR exceeds the company\'s target '
            'rate of return; between competing projects, choose the highest ARR.'},
      {'p': '**Advantages:** simple to compute; easy to understand; uses **accounting profit**, '
            'which is the measure by which the business and its managers are actually judged in '
            'the published accounts; considers the **whole life** of the project, unlike '
            'payback; and gives a percentage that is directly comparable with the company\'s '
            'existing return on capital employed.'},
      {'p': '**Disadvantages:** it **ignores the time value of money**; it uses **profit rather '
            'than cash flow**, and profit is affected by depreciation policy and other '
            'accounting conventions; averaging the profit conceals the pattern of returns, so '
            'two projects with the same average but very different timing score identically; '
            'the target rate is arbitrary; and there are two competing definitions (initial vs '
            'average investment) which give different answers for the same project.'}]}},

    {'eg': {'tag': 'Exam type — Q2', 't': 'Two methods to guide a Board choosing between two '
                                          'capital proposals',
      'q': [{'p': 'A company wishes to expand its production. Two proposals of capital '
                  'expenditure are being considered; each requires more or less the same outlay. '
                  'As management accountant, you are required to furnish a profitability '
                  'estimate to guide the Board in its decision. Describe briefly **two** methods '
                  'that can be used for this purpose.'}],
      'a': [
      {'note': 'The question says the two proposals require **more or less the same outlay**. '
               'That matters: where outlays are equal, the ranking problem that normally '
               'separates NPV from the profitability index disappears, and NPV alone is '
               'sufficient. Say so — it shows you read the question.'},
      {'h4': 'Method 1 — Net Present Value (the recommended method)'},
      {'def': {'t': 'Net present value', 'd': 'the sum of the present values of all a project\'s '
                    'cash inflows and outflows, discounted at the company\'s cost of capital.'}},
      {'tex': 'NPV = \\sum_{t=1}^{n} \\frac{C_t}{(1+r)^t} - I_0'},
      {'p': 'where $C_t$ is the net cash flow in year $t$, $r$ the cost of capital, $n$ the '
            'project life and $I_0$ the initial investment. **Decision rule:** accept if the NPV '
            'is positive; between two mutually exclusive projects of similar size, choose the '
            'higher NPV.'},
      {'p': '**Why it should be recommended to the Board:** it is the only method that measures '
            'the project in the terms the shareholders care about — **the absolute increase in '
            'the value of the business, in today\'s naira**. It takes full account of the time '
            'value of money, uses cash flows rather than accounting profit, considers the whole '
            'life of the project, and allows for risk through the discount rate.'},
      {'p': '**Limitations to mention:** it requires an estimate of the cost of capital; it is '
            'harder for non-financial directors to interpret than a percentage or a period; and '
            'it is sensitive to the reliability of the cash-flow forecasts.'},
      {'h4': 'Method 2 — Internal Rate of Return'},
      {'def': {'t': 'Internal rate of return', 'd': 'the discount rate at which a project\'s net '
                    'present value is exactly zero — i.e. the rate of return the project itself '
                    'earns on the funds invested in it.'}},
      {'tex': 'IRR = A + \\frac{N_A}{N_A - N_B} \\times (B - A)'},
      {'p': 'where $A$ and $B$ are two trial discount rates and $N_A$, $N_B$ the NPVs they '
            'produce (one positive, one negative). **Decision rule:** accept if the IRR exceeds '
            'the cost of capital.'},
      {'p': '**Why it helps the Board:** it expresses the answer as a **percentage**, which '
            'directors can compare directly against the cost of borrowing and against returns '
            'available elsewhere, and it needs no precise cost of capital to compute — only to '
            'interpret.'},
      {'p': '**Limitations:** it can give multiple answers where cash flows change sign more '
            'than once; it assumes interim cash flows are reinvested at the IRR itself, which is '
            'usually unrealistic; and it measures a **rate** rather than an **amount**, so it '
            'can rank a small, very profitable project above a large one that adds far more '
            'value — though that problem does not arise here, since the two outlays are '
            'similar.'},
      {'h4': 'Recommendation'},
      {'p': 'Present the Board with the **NPV of each proposal as the primary measure**, '
            'supported by the **IRR** as a percentage they can compare with the cost of capital. '
            'Add the payback period of each as a note on liquidity and risk. Where the two '
            'methods disagree — which they can, even here — **follow the NPV**, because it '
            'measures the absolute gain in shareholder value.'}]}},

    {'eg': {'tag': 'Exam type — Q3', 't': 'Payback period and NPV compared — which is superior?',
      'q': [{'p': 'Give a comparative description of the Pay Back Period and Net Present Value '
                  'approaches of investment appraisal. Which one of the two do you consider '
                  'superior?'}],
      'a': [
      {'table': {'align': 'lll', 'head': ['', 'Payback period', 'Net present value'], 'rows': [
        ['**What it measures**', 'The **time** taken to recover the original outlay — a measure '
         'of liquidity and risk.', 'The **absolute increase in the value of the business**, in '
         'today\'s naira — a measure of profitability.'],
        ['**Unit of answer**', 'A period, in years and months.', 'An amount of money.'],
        ['**Time value of money**', '**Ignored** — a naira in year 5 counts the same as a naira '
         'in year 1.', '**Fully allowed for** — every cash flow is discounted to its present '
         'value.'],
        ['**Cash flows after the cut-off**', '**Ignored entirely**, however large.',
         '**All included**, to the end of the project\'s life.'],
        ['**Basis of measurement**', 'Cash flow.', 'Cash flow.'],
        ['**Cost of capital needed?**', 'No.', 'Yes — the discount rate must be estimated.'],
        ['**Decision rule**', 'Accept if payback is shorter than a target period set by '
         'management (which is itself arbitrary).',
         'Accept if NPV is positive — an objective rule derived from shareholder value.'],
        ['**Scale of investment**', 'Ignored.', 'Reflected directly in the size of the NPV.'],
        ['**Ease of use**', 'Very simple; easily understood by non-financial managers.',
         'More complex; needs discount tables and a cost of capital.'],
        ['**Risk**', 'Handled crudely, by preferring early recovery.',
         'Handled explicitly, through a risk-adjusted discount rate.'],
      ]}},
      {'h4': 'Which is superior?'},
      {'p': '**Net present value is clearly superior as a measure of a project\'s worth,** for '
            'three reasons that go to the heart of what an investment decision is:'},
      {'ol': [
        'It **recognises the time value of money.** Money has a cost; tying it up for five years '
        'is not the same as tying it up for one, and only NPV prices that difference.',
        'It **counts every cash flow over the whole life of the project.** Payback\'s blindness '
        'to everything after the cut-off date is not a minor limitation — it is capable of '
        'reversing the right answer. Question 8 below is an exact illustration: Project 1 pays '
        'back sooner (4.68 years against 5.05) and so wins on payback, yet Project 2 generates '
        'N2.00m of net cash against Project 1\'s N0.70m. Payback picks the wrong project.',
        'Its **decision rule is objective** — a positive NPV means the project earns more than '
        'the cost of the money invested in it, and therefore makes the shareholders better off. '
        'Payback\'s target period is simply chosen.',
      ]},
      {'p': '**But payback retains a real and legitimate role**, and a complete answer says so. '
            'It is a useful **first screen** and a **risk indicator**: it is quick, it needs no '
            'cost of capital, it is readily understood, and it speaks directly to a business '
            'that is short of cash or operating where distant forecasts are worthless — a '
            'politically unstable market, or a fast-moving technology. Most companies in '
            'practice compute both, using payback to screen out projects that tie money up for '
            'too long and NPV to choose among those that survive the screen.'}]}},

    {'eg': {'tag': 'Exam type — Q4', 't': 'Payback described, and the NPV of two projects at 12% '
                                          'and 15%',
      'q': [
      {'p': '**(a)** Describe briefly the payback period method of investment appraisal and '
            'state **five advantages** and **five disadvantages** of the method.'},
      {'p': '**(b)** Using the information below, prepare tables showing the net present values '
            'of each of the projects at applicable rates of **12%** and **15%** per annum, and '
            'comment on which project would be profitable and should be undertaken.'},
      {'stmt': {'t': 'Project cash flows (N)', 'rows': [
        ['', 'Project X', 'Project Y', '@hd'],
        ['Initial investment', 100000, 100000],
        ['Cash flow — year 1', 5000, 60000],
        ['Cash flow — year 2', 20000, 40000],
        ['Cash flow — year 3', 100000, 100000],
        ['Cash flow — year 4', 10000, 5000],
      ]}},
      {'note': 'The study text heads **both** columns "Project X". The second is Project Y; the '
               'two sets of figures are plainly different and the question asks you to compare '
               'them.'}],
      'a': [
      {'h4': '(a)  The payback period method'},
      {'p': 'The payback period is the **time required for a project\'s net cash inflows to '
            'recover its original cash outlay**. Where inflows are even, it is the investment '
            'divided by the annual inflow; where they are uneven, a cumulative cash-flow column '
            'is built and the recovery point interpolated within the year in which the '
            'cumulative figure turns positive. A project is accepted if its payback is shorter '
            'than a target period set by management, and between competing projects the shortest '
            'payback wins.'},
      {'h4': 'Five advantages'},
      {'ol': [
        '**Simple to calculate and easy to understand**, even for managers with no financial '
        'training.',
        '**Emphasises liquidity** — it shows how quickly the cash committed comes back, which is '
        'critical for a business whose working capital is tight.',
        '**Reduces risk** by favouring projects whose returns arrive early, since near cash '
        'flows are far more certain than distant ones.',
        '**Needs no estimate of the cost of capital**, so it can be applied where that figure is '
        'unknown or disputed.',
        '**Useful in volatile or fast-changing conditions** — rapidly obsolescing technology, or '
        'politically uncertain markets — where forecasts beyond a few years are worthless '
        'anyway.',
        '**Serves as a quick screening device**, eliminating obviously unsuitable projects '
        'before the more expensive discounted analysis is done.',
      ]},
      {'h4': 'Five disadvantages'},
      {'ol': [
        '**Ignores the time value of money** — N1 received in year 4 is treated as equal to N1 '
        'received in year 1.',
        '**Ignores all cash flows after the payback date**, so a highly profitable long-life '
        'project can be rejected in favour of a short-lived one.',
        '**Measures liquidity, not profitability** — it cannot tell you whether a project is '
        'worth doing, only how fast the money comes back.',
        '**The target payback period is arbitrary**, chosen by management rather than derived '
        'from any principle.',
        '**Ignores the size of the investment** and the total return, so it cannot rank projects '
        'of different scale.',
        '**Ignores the pattern of cash flows within the payback period** — two projects '
        'recovering the same amount over the same period score identically even if one recovers '
        'most of it in the first month.',
      ]},
      {'h4': '(b)  Net present values at 12% and 15%'},
      {'stmt': {'t': 'Net present value at 12% (N)', 'rows': [
        ['Year', 'DF @ 12%', 'Project X cash flow', 'Project X PV', 'Project Y cash flow',
         'Project Y PV', '@hd'],
        [1, 0.8929, 5000, 4465, 60000, 53574],
        [2, 0.7972, 20000, 15944, 40000, 31888],
        [3, 0.7118, 100000, 71180, 100000, 71180],
        [4, 0.6355, 10000, 6355, 5000, 3178],
        ['**Total present value**', '', '', 97944, '', 159820, '@t'],
        ['Less: initial investment', '', '', 100000, '', 100000],
        ['**Net present value**', '', '', -2056, '', 59820, '@tt'],
      ]}},
      {'stmt': {'t': 'Net present value at 15% (N)', 'rows': [
        ['Year', 'DF @ 15%', 'Project X cash flow', 'Project X PV', 'Project Y cash flow',
         'Project Y PV', '@hd'],
        [1, 0.8696, 5000, 4348, 60000, 52176],
        [2, 0.7561, 20000, 15122, 40000, 30244],
        [3, 0.6575, 100000, 65750, 100000, 65750],
        [4, 0.5718, 10000, 5718, 5000, 2859],
        ['**Total present value**', '', '', 90938, '', 151029, '@t'],
        ['Less: initial investment', '', '', 100000, '', 100000],
        ['**Net present value**', '', '', -9062, '', 51029, '@tt'],
      ]}},
      {'h4': 'Comment'},
      {'stmt': {'t': 'Summary of net present values (N)', 'rows': [
        ['', 'Project X', 'Project Y', '@hd'],
        ['NPV at 12%', -2056, 59820],
        ['NPV at 15%', -9062, 51029],
        '@gap',
        ['Total undiscounted cash inflows', 135000, 205000],
        ['Decision', '**REJECT**', '**ACCEPT**'],
      ]}},
      {'ol': [
        '**Project Y should be undertaken.** Its NPV is strongly positive at both discount '
        'rates — N59,820 at 12% and N51,029 at 15% — so it earns well above the cost of capital '
        'on either assumption and increases the value of the business by that amount in today\'s '
        'naira.',
        '**Project X should be rejected.** Its NPV is **negative at both rates** (−N2,056 at 12% '
        'and −N9,062 at 15%), so it fails to recover even the cost of the money invested in it.',
        '**Why they differ so sharply.** Project Y returns more cash in total (N205,000 against '
        'N135,000) **and** returns it earlier — N60,000 in year 1 against X\'s N5,000. Project '
        'X is back-loaded, with 74% of its total inflow arriving in year 3, and discounting '
        'punishes exactly that pattern.',
        '**Sensitivity.** Raising the rate from 12% to 15% costs Project Y N8,791 of NPV but '
        'leaves it comfortably positive; it pushes Project X from marginally negative to clearly '
        'negative. Project X\'s internal rate of return is evidently just below 12%, so it '
        'would be rejected at any realistic cost of capital.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q5 (ICAN, November/December 1993)',
      't': 'Electro PLC — appraising a three-year market-share promotion at a 30% hurdle rate',
      'q': [
      {'p': 'Electro PLC, a manufacturer of high-quality metal cables, has a **15% market '
            'share** for one of its products, ECM-1. The standard cost and profit margin for one '
            'unit of ECM-1 are:'},
      {'stmt': {'t': 'Standard cost and profit per unit (N)', 'rows': [
        ['Sales', '', 10.00],
        ['Less direct cost:  material', 4.00, ''],
        ['                           labour', 2.00, ''],
        ['                           overheads', 1.00, 7.00],
        ['**Contribution**', '', 3.00, '@t'],
        ['Less: fixed costs', '', 2.00],
        ['**Profit**', '', 1.00, '@tt'],
      ]}},
      {'p': 'Budgeted sales of ECM-1 during 1994 are **N3,000,000**. The marketing director '
            'proposes that market share could be increased to **20%** and maintained at that '
            'level for the next three years if the following promotion budgets were spent at '
            'the **beginning of each** of the next three years: Year 1 **N200,000**; Year 2 '
            '**N150,000**; Year 3 **N150,000**.'},
      {'p': 'The fixed cost of N2 per unit **includes 50% for the depreciation charge**. The '
            'remaining 50% would be expected to **increase by N60,000** with the increase in '
            'market share. The company has an overall profit return objective of **30%**, which '
            'it applies as a hurdle rate to this type of project.'},
      {'p': '**Required:** **(a)** evaluate whether the project should be adopted, assuming '
            'these are the only variables; **(b)** show with suitable calculations what the '
            'outcome will be if only a **4% increase in market share** is achieved.'},
      {'stmt': {'t': 'Present value factors supplied', 'rows': [
        ['Year', '10%', '20%', '30%', '40%', '@hd'],
        [1, 0.9091, 0.8333, 0.7692, 0.7143],
        [2, 0.8264, 0.6944, 0.5917, 0.5102],
        [3, 0.7513, 0.5787, 0.4552, 0.3644],
        [4, 0.6830, 0.4823, 0.3501, 0.2603],
        [5, 0.6209, 0.4019, 0.2693, 0.1859],
      ]}}],
      'a': [
      {'h4': 'Step 1 — the size of the market, and the extra volume'},
      {'stmt': {'t': 'Market size', 'rows': [
        ['Budgeted sales value of ECM-1, 1994', '', 'N3,000,000'],
        ['÷ selling price per unit', '', 'N10.00'],
        ['**Budgeted units at a 15% share**', '', '300,000 units', '@t'],
        ['**Total market**  (300,000 ÷ 15%)', '', '2,000,000 units', '@t'],
        '@gap',
        ['Units at a 20% share  (2,000,000 × 20%)', '', '400,000 units'],
        ['**Increase in units**', '', '100,000 units', '@tt'],
      ]}},
      {'h4': 'Step 2 — the incremental operating cash flow'},
      {'p': 'Only the **incremental** figures matter. Contribution per unit is unchanged at N3, '
            'and of the N2 fixed cost per unit, **half is depreciation** — a non-cash charge '
            'that is irrelevant to a discounted cash flow appraisal — while the other half rises '
            'by a stated **N60,000** in total.'},
      {'stmt': {'t': 'Incremental operating cash flow per annum (N)', 'rows': [
        ['Additional contribution:  100,000 units × N3', '', 300000],
        ['Less: increase in cash fixed costs', '', 60000],
        ['**Net incremental operating cash flow, each year for 3 years**', '', 240000, '@tt'],
      ]}},
      {'warn': '**Depreciation is excluded.** It is not a cash flow, and in any case the '
               'question says the depreciation half of the fixed cost does not change. '
               'Including it would understate the annual benefit by N150,000 and reverse the '
               'decision. In every DCF appraisal, work with **cash**, not accounting profit.'},
      {'h4': 'Step 3 — the timing of the promotion spend'},
      {'p': 'The promotion is paid at the **beginning** of each year, so Year 1\'s spend falls '
            'at **time 0**, Year 2\'s at the end of year 1 (time 1) and Year 3\'s at time 2. '
            'The operating cash flows arise at the **end** of each year.'},
      {'stmt': {'t': 'Net cash flow by period (N)', 'rows': [
        ['Time', 'Operating cash flow', 'Promotion spend', 'Net cash flow', '@hd'],
        ['0  (start of year 1)', 0, -200000, -200000],
        ['1  (end of year 1 / start of year 2)', 240000, -150000, 90000],
        ['2  (end of year 2 / start of year 3)', 240000, -150000, 90000],
        ['3  (end of year 3)', 240000, 0, 240000],
      ]}},
      {'h4': '(a)  Net present value at the 30% hurdle rate'},
      {'stmt': {'t': 'NPV at 30% (N)', 'rows': [
        ['Time', 'Net cash flow', 'DF @ 30%', 'Present value', '@hd'],
        [0, -200000, 1.0000, -200000],
        [1, 90000, 0.7692, 69228],
        [2, 90000, 0.5917, 53253],
        [3, 240000, 0.4552, 109248],
        ['**Net present value**', '', '', 31729, '@tt'],
      ]}},
      {'p': '**The project should be adopted.** At the company\'s own 30% hurdle rate the net '
            'present value is **positive at N31,729**, so the promotion campaign earns more than '
            'the 30% return the company requires and increases shareholder value.'},
      {'h4': '(b)  If only a 4% increase in market share is achieved'},
      {'p': 'A 4 percentage-point rise takes the share from 15% to **19%**, not 20%:'},
      {'stmt': {'t': 'Revised incremental cash flow (N)', 'rows': [
        ['Additional units  (2,000,000 × 4%)', '', '80,000 units'],
        ['Additional contribution:  80,000 × N3', '', 240000],
        ['Less: increase in cash fixed costs (unchanged — a step cost)', '', 60000],
        ['**Net incremental operating cash flow per annum**', '', 180000, '@tt'],
      ]}},
      {'stmt': {'t': 'Revised NPV at 30% (N)', 'rows': [
        ['Time', 'Operating flow', 'Promotion', 'Net cash flow', 'DF @ 30%', 'Present value',
         '@hd'],
        [0, 0, -200000, -200000, 1.0000, -200000],
        [1, 180000, -150000, 30000, 0.7692, 23076],
        [2, 180000, -150000, 30000, 0.5917, 17751],
        [3, 180000, 0, 180000, 0.4552, 81936],
        ['**Net present value**', '', '', '', '', -77237, '@tt'],
      ]}},
      {'p': '**On a 4% increase the project should be rejected** — the NPV is **negative at '
            'N77,237**, so the campaign would destroy value.'},
      {'key': 'The contrast between (a) and (b) is the real lesson. A **one percentage point** '
              'shortfall in market share — 19% instead of 20% — swings the NPV by **N108,966**, '
              'from +N31,729 to −N77,237, and turns a worthwhile project into a loss-making one. '
              'The proposal is therefore **extremely sensitive to the marketing director\'s '
              'forecast**, and the break-even share can be found exactly: the project needs '
              'enough extra units for the NPV to reach zero, which lies between a 4% and a 5% '
              'increase, very close to 4.7 percentage points. Before committing N500,000 of '
              'promotion spend the Board should ask how confident the marketing director is of '
              'hitting 20% rather than 19%, and should consider staging the spend so that years '
              '2 and 3 can be abandoned if year 1 disappoints.'},
      {'note': 'Other factors a full answer would raise: competitors are unlikely to surrender '
               '5% of the market without responding, and a price war would cut the N3 '
               'contribution; the assumption that the higher share is **maintained** for three '
               'years with no further promotion after year 3 is optimistic; and a 30% hurdle '
               'rate is high, so the project is being judged very severely.'}]}},

    {'eg': {'tag': 'Exam type — Q6 (ACCA, Financial Management)',
      't': 'Bourbon Can Company — six projects, N600,000 of capital, and a rationing decision',
      'q': [
      {'p': 'As financial consultant to the Bourbon Can Company, a medium-sized manufacturing '
            'business, you have been asked to advise on the current year\'s investment '
            'proposals. The proposed projects are **not mutually exclusive**:'},
      {'stmt': {'t': 'The six projects', 'rows': [
        ['Project', 'Description', 'Initial cost (N)', 'Expected life', 'Annual after-tax cash '
         'inflow (N)', '@hd'],
        ['A', 'Replace existing data processing equipment', 250000, '6 years', 72500],
        ['B', 'Develop a new type of container', 70000, '5 years', 30000],
        ['C', 'Install safety equipment', 90000, '3 years', 45000],
        ['D', 'Construct a new factory building', 210000, '8 years', 57000],
        ['E', 'Extend the existing loading equipment', 170000, '4 years', 70000],
        ['F', 'Purchase patent rights to a new process', 135000, '7 years', 36000],
      ]}},
      {'ul': [
        'Except for **project B**, all cash inflows would commence in the current year; '
        'B\'s inflows commence **in one year\'s time**.',
        'Annual cash inflows are always received on the **last day of the year**.',
        'Tax may be assumed to have been paid in the year in which the profits are earned.',
        'The company\'s **weighted average cost of capital is 16%**.',
        'The company is in a **capital rationing situation** and will have only **N600,000** to '
        'invest in capital projects in the current year.',
      ]},
      {'p': '**Required:** **(a)** which projects would you recommend the company undertake, and '
            'why? **(b)** What factors, other than those given, would you advise the company to '
            'consider before deciding?'}],
      'a': [
      {'h4': 'Step 1 — the net present value and profitability index of each project'},
      {'p': 'All the inflows are equal annual amounts, so each is an **annuity** and the '
            'cumulative discount factor at 16% can be used. Project B\'s inflows run from the '
            'end of year 2 to the end of year 6, so its factor is the six-year annuity factor '
            '**less** the one-year factor.'},
      {'stmt': {'t': 'Cumulative discount factors at 16%', 'rows': [
        ['Years', 1, 2, 3, 4, 5, 6, 7, 8, '@hd'],
        ['Cumulative factor', 0.8621, 1.6052, 2.2459, 2.7982, 3.2743, 3.6847, 4.0386, 4.3436],
      ]}},
      {'stmt': {'t': 'Net present value and profitability index (N)', 'rows': [
        ['Project', 'Annual inflow', 'Annuity factor', 'Present value of inflows',
         'Initial cost', 'NPV', 'Profitability index', '@hd'],
        ['A', 72500, '3.6847  (yrs 1–6)', 267141, 250000, 17141, 1.069],
        ['B', 30000, '2.8226  (yrs 2–6)', 84678, 70000, 14678, 1.210],
        ['C', 45000, '2.2459  (yrs 1–3)', 101066, 90000, 11066, 1.123],
        ['D', 57000, '4.3436  (yrs 1–8)', 247585, 210000, 37585, 1.179],
        ['E', 70000, '2.7982  (yrs 1–4)', 195874, 170000, 25874, 1.152],
        ['F', 36000, '4.0386  (yrs 1–7)', 145390, 135000, 10390, 1.077],
        ['**Total**', '', '', '', 925000, 116734, '', '@tt'],
      ]}},
      {'note': 'Project B\'s factor: the five inflows run from year 2 to year 6, so the factor '
               'is the six-year cumulative figure less the first year — '
               '$3.6847 - 0.8621 = 2.8226$. Deferring the start of an annuity by one year is '
               'always handled this way, and it is the detail this question is really testing.'},
      {'h4': 'Step 2 — the rationing problem'},
      {'p': '**Every project has a positive NPV**, so in the absence of a constraint all six '
            'should be undertaken, at a total cost of N925,000 for a combined NPV of N116,734. '
            'But only **N600,000** is available, so N325,000 of worthwhile investment must be '
            'given up and the money must be allocated to the projects that produce the most NPV '
            '**per naira invested** — which is what the **profitability index** measures.'},
      {'tex': '\\text{Profitability index} = \\frac{\\text{Present value of inflows}}'
              '{\\text{Initial investment}}'},
      {'stmt': {'t': 'Ranking by profitability index, and the cumulative outlay', 'rows': [
        ['Rank', 'Project', 'PI', 'Cost (N)', 'Cumulative cost (N)', 'NPV (N)', '@hd'],
        ['1st', 'B', 1.210, 70000, 70000, 14678],
        ['2nd', 'D', 1.179, 210000, 280000, 37585],
        ['3rd', 'E', 1.152, 170000, 450000, 25874],
        ['4th', 'C', 1.123, 90000, 540000, 11066],
        ['5th', 'F', 1.077, 135000, '*675,000 — exceeds the limit*', 10390],
        ['6th', 'A', 1.069, 250000, '*—*', 17141],
      ]}},
      {'h4': '(a)  Recommendation'},
      {'stmt': {'t': 'Recommended portfolio', 'rows': [
        ['Project', 'Cost (N)', 'NPV (N)', '@hd'],
        ['B — new type of container', 70000, 14678],
        ['C — safety equipment', 90000, 11066],
        ['D — new factory building', 210000, 37585],
        ['E — extend loading equipment', 170000, 25874],
        ['**Total committed**', 540000, 89203, '@tt'],
        ['*Funds remaining unspent*', 60000, '', ''],
      ]}},
      {'p': '**Undertake projects B, C, D and E**, at a total cost of **N540,000**, producing a '
            'combined net present value of **N89,203**. Projects A and F are rejected: neither '
            'can be afforded out of the N60,000 remaining, and both rank lowest on profitability '
            'index.'},
      {'p': '**Reasons for the choice:** the projects are indivisible and not mutually '
            'exclusive, so the task is to find the **combination** that maximises total NPV '
            'within the N600,000 limit. Ranking by profitability index identifies the candidates '
            'that generate the most present value per naira of scarce capital. Testing the '
            'alternative affordable combinations confirms this one is optimal — for instance '
            'B+D+E+F costs N585,000 but yields only N88,527, and A+B+D costs N530,000 and yields '
            'only N69,404.'},
      {'warn': 'Note why **NPV alone is the wrong ranking tool here**. On NPV, project D (N37,585) '
               'and project E (N25,874) beat project B (N14,678) — yet B is ranked first, because '
               'it generates N1.21 of present value for every naira invested where D generates '
               'N1.18 and E N1.15. Under capital rationing the scarce resource is **capital**, so '
               'the ranking must be by return **per unit of the limiting factor** — exactly the '
               'principle used for machine hours in Chapter 9 Q1.'},
      {'h4': '(b)  Other factors to consider before deciding'},
      {'ol': [
        '**Project C is safety equipment**, which may well be a **legal requirement** rather '
        'than a discretionary investment. If so it must be undertaken whatever its NPV, and '
        'should be removed from the ranking exercise and funded first. The consequences of not '
        'installing it — prosecution, injury, closure, damage to reputation — are not captured '
        'by a cash-flow model.',
        '**Can the capital constraint be relaxed?** N325,000 of positive-NPV investment is being '
        'forgone. Borrowing, leasing, a rights issue, staging the projects across two years, or '
        'disposing of surplus assets might all release funds; the cost of doing so should be '
        'compared with the N27,531 of NPV being given up on A and F.',
        '**The N60,000 left unspent** should be invested somewhere, or the ranking reconsidered '
        'to use it.',
        '**Risk differs between projects.** All have been discounted at the same 16%, but '
        'developing a **new container** and buying **patent rights to a new process** are '
        'speculative, while replacing data processing equipment is not. Risk-adjusted discount '
        'rates, or sensitivity analysis on each project, would give a truer ranking.',
        '**Reliability of the estimates** — how firm are the cash-flow forecasts and the project '
        'lives, and who produced them?',
        '**Inflation**, and whether the cash flows and the 16% rate are both in money terms or '
        'both in real terms.',
        '**Interdependence between projects** — the new factory building (D) may be a '
        'prerequisite for extending the loading equipment (E), or the two may compete for the '
        'same site or management time.',
        '**Non-financial and strategic factors** — effect on employees and industrial relations, '
        'on customers and on the company\'s competitive position; whether rejecting the patent '
        'rights (F) allows a competitor to acquire them.',
        '**Scrap or residual values** at the end of each project\'s life, which the question '
        'ignores entirely.',
        '**The accuracy of the 16% cost of capital**, and whether it is the right rate for '
        'projects of this risk.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q7',
      't': 'Usman & Co. — traditional techniques, and NPV applied to two projects',
      'q': [
      {'p': '**(a)** Define any two "traditional" investment appraisal techniques, showing '
            'briefly their advantages and disadvantages.'},
      {'p': '**(b)** Demonstrate your knowledge of the more acceptable technique using cash flows '
            'expected from two projects being negotiated by the General Manager of Usman & Co. '
            'Ltd. Both projects require an initial cash investment of **N25,000** each. Project '
            'one will earn **N8,000** in the first year, **N10,000** and **N6,000** in the next '
            'two years, and **N1,000** each in years four and five.'},
      {'warn': 'The question as printed **stops there** — the cash flows of project two are '
               'missing from the study text altogether, and the sentence ends mid-thought. '
               '(Confirmed by rendering page 303 of the PDF; it is not an extraction artifact.) '
               'The question cannot be answered as set. Part (b) below works **project one** in '
               'full on the data given, and then supplies a plausible project two — clearly '
               'marked as supplied, not as the examiner\'s — so that the comparison the '
               'question asks for can be demonstrated.',
       'lbl': 'The question is incomplete in the study text'}],
      'a': [
      {'h4': '(a)  Two traditional techniques'},
      {'p': 'The **traditional** (or non-discounted) techniques are those that take no account '
            'of the time value of money: the **payback period** and the **accounting rate of '
            'return**.'},
      {'table': {'align': 'lll', 'head': ['', 'Payback period',
        'Accounting rate of return (ARR)'], 'rows': [
        ['**Definition**', 'The time required for a project\'s net cash inflows to recover the '
         'original outlay.',
         'Average annual accounting **profit** as a percentage of the capital invested.'],
        ['**Formula**', '$\\dfrac{\\text{Initial investment}}'
         '{\\text{Annual net cash inflow}}$, or by interpolation where flows are uneven.',
         '$\\dfrac{\\text{Average annual profit}}{\\text{Initial (or average) investment}} '
         '\\times 100$'],
        ['**Decision rule**', 'Accept if shorter than the target period; choose the shortest.',
         'Accept if above the target return; choose the highest.'],
        ['**Advantages**', 'Simple; emphasises liquidity; reduces risk by favouring early '
         'returns; needs no cost of capital; a useful first screen.',
         'Simple; uses the profit measure by which the business is actually judged; considers '
         'the **whole life** of the project; gives a percentage comparable with the existing '
         'return on capital employed.'],
        ['**Disadvantages**', 'Ignores the time value of money; **ignores everything after the '
         'payback date**; measures liquidity rather than profitability; the target period is '
         'arbitrary; ignores project size.',
         'Ignores the time value of money; uses **profit rather than cash**, so it is distorted '
         'by depreciation policy; averaging hides the timing of returns; the target rate is '
         'arbitrary; two competing definitions give different answers.'],
      ]}},
      {'h4': '(b)  The more acceptable technique — net present value'},
      {'p': 'The discounted methods are superior, and **net present value** is the most '
            'acceptable of them, because it measures the absolute increase in the value of the '
            'business after allowing for the cost of the money tied up. Applying it to project '
            'one, at an assumed cost of capital of **10%** (no rate is given in the question — '
            'state your assumption):'},
      {'stmt': {'t': 'Project one — net present value at 10% (N)', 'rows': [
        ['Year', 'Cash flow', 'DF @ 10%', 'Present value', '@hd'],
        [0, -25000, 1.0000, -25000],
        [1, 8000, 0.9091, 7273],
        [2, 10000, 0.8264, 8264],
        [3, 6000, 0.7513, 4508],
        [4, 1000, 0.6830, 683],
        [5, 1000, 0.6209, 621],
        ['**Total present value of inflows**', '', '', 21349, '@t'],
        ['**Net present value**', '', '', -3651, '@tt'],
      ]}},
      {'p': '**Project one should be rejected.** Although its total undiscounted inflows of '
            'N26,000 exceed the N25,000 invested, the margin is only N1,000 — and once the cash '
            'flows are discounted at 10% the project shows a **negative NPV of N3,651**. It does '
            'not earn the cost of the capital employed in it. Note that its **payback period** '
            'is $2 + \\tfrac{7{,}000}{6{,}000}$ — that is, during year 3, at about **2.17 '
            'years** — which looks respectable, and is precisely the kind of case where the '
            'traditional methods mislead.'},
      {'h4': 'A supplied project two, for the comparison the question intends'},
      {'note': 'The figures below are **not from the study text** — they are supplied here so '
               'the comparison can be demonstrated. Treat them as an illustration of the method, '
               'not as the examiner\'s data.'},
      {'stmt': {'t': 'Project two (supplied) — net present value at 10% (N)', 'rows': [
        ['Year', 'Cash flow', 'DF @ 10%', 'Present value', '@hd'],
        [0, -25000, 1.0000, -25000],
        [1, 6000, 0.9091, 5455],
        [2, 8000, 0.8264, 6611],
        [3, 9000, 0.7513, 6762],
        [4, 7000, 0.6830, 4781],
        [5, 5000, 0.6209, 3105],
        ['**Total present value of inflows**', '', '', 26714, '@t'],
        ['**Net present value**', '', '', 1714, '@tt'],
      ]}},
      {'p': '**Project two would be chosen.** Its NPV is positive at N1,714 against project '
            'one\'s negative N3,651, even though its payback is **longer** (3.71 years against '
            '2.17) — because it keeps earning after project one has dwindled to N1,000 a year. '
            'That is exactly the comparison the examiner was setting up, and exactly why the '
            'discounted method is "the more acceptable technique".'}]}},

    {'eg': {'tag': 'Exam type — Q8 (PE II, May/June 1994)',
      't': 'Modern Tech. Services — payback periods, and what payback conceals',
      'q': [
      {'p': 'Modern Tech. Services Ltd is considering two alternative projects for a business '
            'expansion programme in the Northern part of the country. The projects have the '
            'following Naira cash-flow profiles:'},
      {'stmt': {'t': 'Cash flow profiles (N million)', 'rows': [
        ['Year', 'Project 1', 'Project 2', '@hd'],
        [0, '(1.00)', '(3.00)'],
        [1, '(2.00)', 0.20],
        [2, 0.95, 0.50],
        [3, 0.85, 0.65],
        [4, 0.78, 0.75],
        [5, 0.62, 0.80],
        [6, 0.40, 1.90],
        [7, 0.10, 0.20],
      ]}},
      {'p': '**Required:** **(a)** calculate the payback period for each project; **(b)** based '
            'on payback periods, advise which project should be chosen; **(c)** state the '
            'advantages and disadvantages of the payback period criterion of investment '
            'appraisal.'}],
      'a': [
      {'h4': '(a)  Payback periods'},
      {'note': 'Project 1 has **two outflows** — N1m at time 0 and a further N2m at the end of '
               'year 1 — so the total investment to be recovered is N3m, the same as project 2, '
               'but it is committed later. The cleanest method is a single cumulative net '
               'cash-flow column that includes both the outflows and the inflows.'},
      {'stmt': {'t': 'Project 1 — cumulative net cash flow (N million)', 'rows': [
        ['Year', 'Cash flow', 'Cumulative', '@hd'],
        [0, '(1.00)', '(1.00)'],
        [1, '(2.00)', '(3.00)'],
        [2, 0.95, '(2.05)'],
        [3, 0.85, '(1.20)'],
        [4, 0.78, '(0.42)'],
        ['**5**', '**0.62**', '**0.20  ← turns positive**'],
        [6, 0.40, 0.60],
        [7, 0.10, 0.70],
      ]}},
      {'tex': '\\text{Payback}_1 = 4 \\text{ years} + \\frac{0.42}{0.62} '
              '= 4 + 0.68 = \\mathbf{4.68 \\text{ years}}'},
      {'stmt': {'t': 'Project 2 — cumulative net cash flow (N million)', 'rows': [
        ['Year', 'Cash flow', 'Cumulative', '@hd'],
        [0, '(3.00)', '(3.00)'],
        [1, 0.20, '(2.80)'],
        [2, 0.50, '(2.30)'],
        [3, 0.65, '(1.65)'],
        [4, 0.75, '(0.90)'],
        [5, 0.80, '(0.10)'],
        ['**6**', '**1.90**', '**1.80  ← turns positive**'],
        [7, 0.20, 2.00],
      ]}},
      {'tex': '\\text{Payback}_2 = 5 \\text{ years} + \\frac{0.10}{1.90} '
              '= 5 + 0.05 = \\mathbf{5.05 \\text{ years}}'},
      {'h4': '(b)  Advice based on payback periods'},
      {'stmt': {'t': 'Comparison', 'rows': [
        ['', 'Project 1', 'Project 2', '@hd'],
        ['Payback period', '4.68 years', '5.05 years'],
        ['**Decision on the payback criterion**', '**CHOOSE**', 'reject'],
      ]}},
      {'p': '**On the payback criterion, Project 1 should be chosen** — it recovers the N3m '
            'invested about four and a half months sooner than Project 2.'},
      {'warn': 'But look at what that criterion is throwing away. Over the full seven years '
               '**Project 1 generates N3.70m of inflows against a N3.00m outlay — a net gain of '
               'N0.70m**, while **Project 2 generates N5.00m against the same N3.00m — a net '
               'gain of N2.00m**, nearly three times as much. Project 2\'s single largest '
               'inflow, N1.90m in year 6, falls **after** Project 1 has already paid back, so '
               'payback never sees it. A company that followed the payback rule here would '
               'forgo N1.30m of net cash. This question is a textbook demonstration of '
               'payback\'s central defect, and a complete answer **must say so** even though '
               'part (b) asks only for the payback-based advice.',
       'lbl': 'What payback conceals here'},
      {'stmt': {'t': 'Total cash generated over the full seven years (N million)', 'rows': [
        ['', 'Project 1', 'Project 2', '@hd'],
        ['Total inflows', 3.70, 5.00],
        ['Total outflows', '(3.00)', '(3.00)'],
        ['**Net cash generated**', 0.70, 2.00, '@tt'],
      ]}},
      {'p': '**Recommendation:** advise the Board that on payback alone Project 1 wins, but that '
            'the criterion is inadequate here and a **discounted cash flow appraisal of both '
            'projects should be carried out before any commitment is made**. Project 2 is very '
            'likely to show the higher net present value despite its slower payback.'},
      {'h4': '(c)  Advantages and disadvantages of the payback period criterion'},
      {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
        ['**Simple** to calculate and to understand, even for managers without financial '
         'training.',
         '**Ignores the time value of money** — N1 in year 7 is counted as equal to N1 in year '
         '1.'],
        ['**Emphasises liquidity** — it shows how quickly committed cash returns, which matters '
         'to a business with tight working capital.',
         '**Ignores all cash flows after the payback date**, however large — as Project 2\'s '
         'N1.90m in year 6 demonstrates.'],
        ['**Reduces risk** by favouring projects whose returns arrive early, since near-term '
         'forecasts are far more reliable than distant ones.',
         '**Measures liquidity, not profitability** — it cannot say whether a project is worth '
         'doing at all.'],
        ['**Needs no cost of capital**, so it can be used where that figure is unknown or '
         'disputed.',
         'The **target payback period is arbitrary**, set by management rather than derived from '
         'principle.'],
        ['**Useful as a first screen**, and in volatile markets or fast-obsolescing technology '
         'where long forecasts are worthless.',
         '**Ignores the size of the investment** and the total return, so projects of different '
         'scale cannot be compared.'],
        ['**Objective and consistent** — two analysts working from the same figures get the same '
         'answer.',
         '**Ignores the pattern of flows within the payback period**, and takes no account of '
         'scrap or residual values.'],
      ]}}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Payback Period', 'tex': '\\dfrac{\\text{Cost of Investment}}{\\text{Annual Cash '
   'Flow}}'},
  {'lb': 'Accounting Rate of Return', 'tex': '\\dfrac{\\text{Average annual profit after '
   'depreciation}}{\\text{Initial (or average) investment}} \\times 100'},
  {'lb': 'Net Present Value', 'tex': 'NPV = \\sum \\dfrac{\\text{Cash flow}_t}{(1+r)^t} - '
   '\\text{Initial outlay}'},
 ],
 'focus':
   'NPV computations are tested heavily and reward careful, methodical layout — always show '
   'year, cash flow, discount factor and present value as separate columns, and total only at '
   'the end. Know payback and ARR\'s specific weaknesses well enough to explain *why* NPV is '
   'preferred (it is the only one of the three that discounts for time), and be ready for a '
   'question where the three methods actually disagree on which project to pick — that '
   'disagreement, and being able to explain it, is exactly what a Section B question on this '
   'topic is usually testing.',
 'errors': [
   'Ignoring cash flows that occur after a project\'s payback period, when payback is being '
   'used only as one input among several — its own blind spot should not become the analyst\'s.',
   'Comparing ARR figures computed on different bases (initial capital vs average capital) as '
   'if they were the same measure.',
   'Forgetting to discount a terminal/disposal cash flow (like the van sale proceeds in '
   'Illustration 11.5) at the *same* year\'s discount factor as any other cash flow in that year.',
   'Treating a project as acceptable because its ARR looks attractive, without checking its NPV '
   '— the two can give opposite recommendations.',
   'Including a sunk cost (e.g. the old asset\'s remaining book value in a replacement decision) '
   'in an NPV or payback calculation.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A project costs N200,000 and generates N50,000 of cash proceeds each year. Its '
         'payback period is',
    'o': ['2 years', '4 years', '5 years', '10 years', '6 years'],
    'a': 1,
    'w': 'Payback period = Cost of investment / Annual cash flow = 200,000 / 50,000 = 4 years.',
    'calc': '\\dfrac{200{,}000}{50{,}000} = 4',
    'src': 'Chapter 11.2', 'sec': '11.2'},
   {'q': 'A project has an average annual profit after depreciation of N40,000 and an initial '
         'investment of N320,000. Its Accounting Rate of Return on initial capital is',
    'o': ['8%', '12.5%', '80%', '4%', '25%'],
    'a': 0,
    'w': 'ARR = Average profit / Initial investment × 100 = 40,000 / 320,000 × 100 = 12.5%.',
    'calc': '\\dfrac{40{,}000}{320{,}000} \\times 100 = 12.5\\%',
    'src': 'Chapter 11.2', 'sec': '11.2'},
   {'q': 'A project has a Net Present Value of exactly zero at a discount rate of 15%. This '
         'means the project\'s actual return is',
    'o': ['greater than 15%', 'exactly 15%', 'less than 15%', 'negative', 'undefined'],
    'a': 1,
    'w': 'A zero NPV at a given discount rate means the project earns exactly that rate of '
         'return — neither more nor less.',
    'src': 'Chapter 11.3', 'sec': '11.3'},
   {'q': 'Under the NPV investment appraisal method, a project should generally be accepted '
         'when its NPV is',
    'o': ['negative', 'exactly zero, and only then', 'positive', 'equal to the initial outlay',
          'undefined'],
    'a': 2,
    'w': 'The NPV decision rule is to accept a project with a positive net present value.',
    'src': 'Chapter 11.3', 'sec': '11.3'},
   {'q': 'Compared with the Payback Period method, the Net Present Value method',
    'o': ['ignores the time value of money entirely, just like payback',
          'properly accounts for the time value of money by discounting future cash flows',
          'only considers cash flows within the payback period',
          'cannot be used alongside the payback method', 'uses accounting profit, not cash flow'],
    'a': 1,
    'w': 'NPV\'s defining advantage over payback is that it discounts every future cash flow to '
         'reflect the time value of money — payback does not.',
    'src': 'Chapter 11.3', 'sec': '11.3'},
   {'q': 'In a replacement decision, the unabsorbed book value (and its associated future '
         'depreciation charge) of the OLD asset being replaced is generally treated as',
    'o': ['the single most relevant cost in the decision', 'a sunk cost, irrelevant except for '
          'its tax effect', 'always equal to the new asset\'s cost',
          'the main driver of the project\'s NPV', 'a future cash inflow'],
    'a': 1,
    'w': 'The old asset\'s unabsorbed book value is a sunk cost — money already spent, '
         'unaffected by the replacement decision itself, relevant only through any tax effect '
         'it triggers.',
    'src': 'Chapter 11.1', 'sec': '11.1'},
   {'q': 'Which of the following is a genuine disadvantage of the Accounting Rate of Return '
         'method, shared with the Payback Period method?',
    'o': ['Both ignore accounting profit entirely',
          'Both ignore that cash flows and outflows occur at different points in time',
          'Both require a computer to calculate', 'Both always give identical project rankings',
          'Both are discounted cash flow techniques'],
    'a': 1,
    'w': 'Both ARR and payback share the same fundamental weakness: neither accounts for the '
         'timing of cash flows — a Naira in year 1 is treated the same as a Naira in year 5.',
    'src': 'Chapter 11.2', 'sec': '11.2'},
   {'q': 'A firm is choosing between two projects using multiple appraisal methods, and finds '
         'that Project X has the shorter payback period while Project Y has the higher NPV at '
         'the firm\'s cost of capital. This situation',
    'o': ['is impossible and indicates a calculation error',
          'can genuinely occur, since the methods measure different things',
          'means NPV should always be ignored in favour of payback',
          'means the discount rate used must be wrong',
          'only happens when both projects have identical cash flows'],
    'a': 1,
    'w': 'Payback rewards speed of capital recovery; NPV rewards total value created at the '
         'required rate of return, properly weighted for timing — the two can genuinely point '
         'to different projects, exactly as ARR and payback did in Illustration 11.3.',
    'src': 'Chapter 11.2', 'sec': '11.2'},
  ],
  'theory': [
   {'q': 'Describe briefly the Payback Period method of investment appraisal, and state five '
         'advantages and five disadvantages of the method.',
    'marks': 12,
    'a': [
      {'p': 'The Payback Period is the number of years needed to recover a project\'s original '
            'investment from its cash proceeds (before depreciation, after tax) — computed as '
            'cost of investment ÷ annual cash flow, with shorter periods preferred.'},
      {'p': '**Advantages**: easy to understand and simple to operate; its short-term focus '
            'reduces exposure to loss from obsolescence; useful for a cash-constrained firm '
            'needing quick fund recovery; uses actual cash flows, not accounting profit, making '
            'it more objective than ARR; and it is the most widely used method in practice.'},
      {'p': '**Disadvantages**: ignores all cash flows beyond the payback period, penalising '
            'long-gestation projects that pay off substantially, just later; ignores the time '
            'value of money entirely; does not measure overall project profitability, only '
            'speed of capital recovery; can lead to rejecting genuinely valuable long-term '
            'projects; and gives no single, universally agreed treatment of working capital '
            'recovered at a project\'s end.'},
    ], 'src': 'Chapter 11.2', 'sec': '11.2'},
   {'q': 'Give a comparative description of the Payback Period and Net Present Value approaches '
         'to investment appraisal. Which do you consider superior?',
    'marks': 10,
    'a': [
      {'p': '**Payback Period** measures only how quickly the original outlay is recovered, '
            'using undiscounted cash flows and ignoring everything that happens after the '
            'payback date. **Net Present Value** measures the total value a project creates '
            'over its *entire* life, by discounting every cash flow (in every year) back to '
            'today\'s value at the firm\'s required rate of return, then comparing the total '
            'against the initial outlay.'},
      {'p': '**NPV is superior** as a measure of genuine investment worth, because it is the '
            'only one of the two that (a) accounts for the time value of money, and (b) '
            'considers the *whole* project life, not just the years up to payback. Payback '
            'remains useful as a simple, easily-understood secondary screen — particularly for '
            'gauging liquidity risk — but should not be relied on as the sole basis for a major '
            'capital decision.'},
    ], 'src': 'Chapter 11.3', 'sec': '11.3'},
  ]},
}
