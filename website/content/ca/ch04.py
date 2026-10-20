CH = {
 'n': 4,
 't': 'Accounting for Labour',
 'brief': 'Labour cost end to end: recruitment, induction, timing and behavioural control; job '
          'evaluation, merit rating and work study; the remuneration methods (time-based, piece '
          'rate, and the Halsey/Halsey-Weir/Rowan premium bonus schemes) with fully worked and '
          'verified illustrations; overtime and idle time; direct versus indirect labour cost; '
          'labour turnover (three measurement formulas, its costs, causes and reduction); '
          'payroll fraud controls; and payroll preparation.',
 'outcomes': [
   'Explain recording and monitoring procedures — time-keeping and time-booking',
   'Explain job evaluation, merit rating, work study, methods study and work measurement',
   'State and explain the basic labour remuneration methods, including time-based systems, '
   'piecework systems, and individual and group incentive schemes',
   'Explain the treatment of overtime and idle time in labour costing',
   'Explain and prepare entries in payroll accounting',
   'Explain the causes of labour turnover and ascertain the costs of labour turnover',
 ],
 'secs': [
  {'n': '4.1', 't': 'Introduction', 'b': [
    {'p': 'Labour is the second element of cost, after materials. Labour cost is the '
          'remuneration for employees\' effort in the production process, and controlling it is '
          'complex — just as controlling human beings and their behaviour is complex. This '
          'chapter covers the determination and control of labour cost from recruitment through '
          'to payroll.'},
  ]},

  {'n': '4.2', 't': 'Labour administration and documentation', 'b': [
    {'h4': 'Labour as a factor of production'},
    {'p': 'Labour is the collective effort of employees in a production process — the form it '
          'takes is employee knowledge, effort, expertise and experience — transforming raw '
          'materials into finished goods. It spans every level of the workforce, from top '
          'management to the grassroots. Because it has huge cost implications, its determination '
          'and control matter. Labour cost consists of recruitment cost, training and staff-'
          'development cost, wages and salaries, employee bonuses, overtime premium, group '
          'incentives, and more — left uncontrolled, total labour cost is not minimised.'},

    {'h4': 'Labour recruitment process'},
    {'def': {'t': 'Labour recruitment', 'd': 'the process of engaging employees to render '
                  'services for an organisation — carried out internally, externally, or both, '
                  'depending on policy.'}},
    {'steps': [
      'Carry out a job analysis, to determine the roles, responsibilities and specifications '
      'required for the position.',
      'For internal recruitment, circulate the advertisement widely within the organisation '
      '(including notice boards), so qualified internal staff can apply.',
      'For external recruitment, advertise through labour offices, newspapers, social media, job '
      'fairs, outsourcing, headhunting or executive search.',
      'Shortlist qualified applicants from those who respond, for the selection process.',
      'Select — via a structured interview (an agreed format, with questions ordered to '
      'evaluate applicants) or an unstructured one — choosing the most qualified candidate '
      'against a pre-determined criterion.',
    ]},
    {'h4': 'Induction, placement and training'},
    {'def': {'t': 'Induction', 'd': 'a programme integrating new employees into the '
                  'organisation\'s culture, through acquaintance with its values and norms.'}},
    {'def': {'t': 'Placement', 'd': 'fixing a newly employed person into their post, based on '
                  'their qualifications, competencies and experience.'}},
    {'p': 'Training, considered thereafter, involves: a training-needs analysis; assessing the '
          'training budget; prioritising the most critical needs; defining the skills, knowledge, '
          'abilities and objectives desired after training; considering the training method; and '
          'evaluating the training.'},
    {'table': {'align': 'll', 'head': ['Cost group', 'What it includes'], 'rows': [
      ['**Recruitment cost**', 'Advertising cost; interviewing expenses; cost of inducting new '
       'employees; training expenses.'],
      ['**Total labour cost**', 'Recruitment cost, **plus** wages and salaries; overtime '
       'premiums; employee bonuses; retirement payments; and more.'],
    ]}},

    {'h4': 'Labour timing and assessment'},
    {'p': 'Once engaged, employees must be tracked at work — to assess performance, and to make '
          'costing the work possible. Methods used include:'},
    {'ul': ['Attendance Register;', 'Clock Cards;', 'Attendance Boards;', 'Job Sheets;',
      'Job Books.']},
    {'p': 'These records gather evidence of: hours worked; time spent by each employee on a '
          'particular job or service; and hours of idleness.'},

    {'h4': 'Labour behaviour and control'},
    {'p': 'Human behaviour is relatively difficult to control, but the organisation must still '
          'try. Mechanisms devised to aid labour control:'},
    {'table': {'align': 'll', 'head': ['Mechanism', 'How it works'], 'rows': [
      ['**Time-keeping**', 'Employees record the time they report for and leave work, and the '
       'time spent on each job/work handled.'],
      ['**Monitoring and supervision**', 'Senior officers supervise employees and observe work '
       'attitude.'],
      ['**Evaluation**', 'The employee\'s work is evaluated by peers, clients and management — '
       'usually motivating positive workplace attitudes.'],
      ['**Reward schemes**', 'Bonuses and incentives for effective employees drive hard work.'],
    ]}},

    {'h4': 'Job evaluation, merit rating and work study'},
    {'def': {'t': 'Job evaluation', 'd': 'a technique showing the relative worth of each job, to '
                  'rank it against other jobs and establish the appropriate weight of '
                  'remuneration to attach to it — analysing job content against yardsticks such '
                  'as degree of responsibility, decisions involved, training/experience required '
                  'and working conditions, awarding points for each.'}},
    {'def': {'t': 'Merit rating', 'd': 'measures the *jobholder\'s* performance (not the job '
                  'itself), to decide whether the employee should be promoted, demoted or given '
                  'a special reward — using yardsticks such as accuracy, initiative, level of '
                  'responsiveness and willingness. Most industries rate staff at year-end to '
                  'track progress.'}},
    {'key': 'Job evaluation ranks **the job**; merit rating ranks **the person doing it**. A '
            'question asking which one determines a pay grade, and which determines a bonus or '
            'promotion, is testing exactly this distinction.'},
    {'def': {'t': 'Work study', 'd': 'a system of maximising an operating unit\'s productivity by '
                  'reorganising its work — subdivided into **method study** and **work '
                  'measurement**.'}},
    {'ul': [
      '**Method study** — recording and critically examining existing methods of doing work, '
      'comparing them with proposed methods, to find easier, more effective and cheaper methods.',
      '**Work measurement** — measures the time a qualified worker needs to complete a specific '
      'assignment at a specified level of performance.',
    ]},
  ]},

  {'n': '4.3', 't': 'Labour remuneration methods', 'b': [
    {'p': 'Two basic families of remuneration: **time-based** and **output-based**.'},

    {'h4': 'Time rate'},
    {'p': 'Pay depends on the number of hours worked, **not** the quantity produced.'},
    {'tex': '\\text{Gross wage} = \\text{Hours worked} \\times \\text{Rate per hour}'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 4.1 — time rate', 'open': True, 'q': [
      {'p': 'An employee works 50 hours at ¢2,000/hour. Find the gross wage.'}],
      'a': [{'tex': '\\text{Gross wage} = 2{,}000 \\times 50 = ¢100{,}000'}]}},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Simple to operate and easy to understand; quality tends to be higher, since the worker '
       'is not rushing to finish for extra pay.', 'No financial incentive to produce more than '
       'the minimum; sometimes an incentive to produce as little as possible; supervision costs '
       'are needed to monitor idleness; unfair, since lazy and hard-working staff are paid the '
       'same rate.'],
    ]}},

    {'h4': 'Piece rate (payment by result)'},
    {'p': 'Pay depends on the number of **units produced**, in one of three forms:'},
    {'table': {'align': 'lll', 'head': ['Form', 'Mechanism', 'Notes'], 'rows': [
      ['**Straight piece rate**', 'Payment = number of units produced × rate per unit — a fixed '
       'rate per unit, regardless of how long it took.', 'Earnings depend purely on output '
       'volume.'],
      ['**Piece rate with guaranteed day rate**', 'Compares piece-rate earnings against normal '
       'day-rate earnings for the same hours; the employee is paid whichever is **higher**.',
       'Protects the employee against low output through no fault of their own.'],
      ['**Differential piece rate**', 'The rate per unit itself rises at higher levels of '
       'efficiency/production (e.g. ¢10,000/unit below 7 units/hour, ¢15,000/unit for 7–10 '
       'units/hour, ¢20,000/unit above 10 units/hour).', 'Gives a strong incentive to reach the '
       'maximum production rate.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration — piece rate with guaranteed day rate',
      'open': True, 'q': [
      {'p': 'Rate per hour ¢15,000; 8,800 hours worked to produce 8,000 units at a piece rate of '
            '¢15,000/unit. Which rate does the employee receive?'}],
      'a': [
      {'p': 'Piece-rate earnings $= 8{,}000 \\times 15{,}000 = ¢120{,}000{,}000$. Time-rate '
            'earnings $= 8{,}800 \\times 15{,}000 = ¢132{,}000{,}000$. Since the guaranteed '
            'hourly-rate earnings are higher, the employee is paid **¢132,000,000**.'}]}},
    {'table': {'align': 'll', 'head': ['Advantages (piece rate generally)',
      'Disadvantages (piece rate generally)'], 'rows': [
      ['Rewards effort, incentivising higher output; employees are self-motivated, so less '
       'supervision is needed; the employer benefits from lower overhead cost per unit.',
       'Quality may be sacrificed, requiring more inspection/quality-control spend; workers may '
       'slacken, arrive late or stay away once satisfied with a week\'s earnings, leaving plant '
       'idle; setting standard times (and negotiating them with unions) takes considerable time; '
       'if a rate is set too high by mistake, it is hard to reduce afterwards, hurting product '
       'cost.'],
    ]}},

    {'h4': 'Premium bonus schemes'},
    {'p': 'Bonus schemes reward employees for efficiency — saving cost for the organisation by '
          'saving *time* — and are, conceptually, a way of sharing extra profit with employees. '
          'Three concepts drive every bonus calculation:'},
    {'table': {'align': 'll', 'head': ['Term', 'Meaning'], 'rows': [
      ['**Time allowed**', 'The expected time fixed to carry out a piece of work — e.g. if the '
       'time set for one unit is 5 hours, 100 units are expected to take 500 hours.'],
      ['**Time taken**', 'The number of hours actually spent doing the work.'],
      ['**Time saved**', 'Time allowed minus time taken (only meaningful when time allowed '
       'exceeds time taken).'],
    ]}},
    {'p': 'Premium bonus schemes are either **individual** (Halsey, Halsey-Weir, Rowan) or '
          '**group** incentive schemes.'},
    {'table': {'align': 'lll', 'head': ['Scheme', 'Formula', 'How time saved is split'], 'rows': [
      ['**Halsey**', '$\\text{Bonus} = \\tfrac12 \\times \\text{Time saved} \\times \\text{Day '
       'rate}$', 'Equally between employer and employee — the employee keeps half the value of '
       'the time they saved.'],
      ['**Halsey-Weir**', '$\\text{Bonus} = \\tfrac13 \\times \\text{Time saved} \\times '
       '\\text{Day rate}$', '2:1 in favour of the *employer* — the employee gets only a third of '
       'the value of the time saved.'],
      ['**Rowan**', '$\\text{Bonus} = \\dfrac{\\text{Time saved}}{\\text{Time allowed}} \\times '
       '\\text{Time taken} \\times \\text{Day rate}$', 'Proportional — the bonus is the same '
       'fraction of pay-for-time-taken as time saved is of time allowed. Total remuneration = '
       '(time taken × day rate) + bonus.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'All three bonus schemes compared on the same data',
      'open': True, 'q': [
      {'p': 'Time allowed = 12 hours; day rate = ¢18,000/hour. Compute the bonus under Halsey, '
            'Halsey-Weir and Rowan for (a) an employee who takes 6 hours, and (b) an employee '
            'who takes 9 hours.'}],
      'a': [
      {'p': '**(a) Time taken 6 hours** (time saved $= 12-6=6$ hours):'},
      {'table': {'align': 'lr', 'head': ['Scheme', 'Bonus (₵)'], 'rows': [
        ['Halsey — $\\tfrac12 \\times 6 \\times 18{,}000$', '54,000'],
        ['Halsey-Weir — $\\tfrac13 \\times 6 \\times 18{,}000$', '36,000'],
        ['Rowan — $\\tfrac{6}{12} \\times 6 \\times 18{,}000$', '54,000'],
      ]}},
      {'p': '**(b) Time taken 9 hours** (time saved $= 12-9=3$ hours):'},
      {'table': {'align': 'lr', 'head': ['Scheme', 'Bonus (₵)'], 'rows': [
        ['Halsey — $\\tfrac12 \\times 3 \\times 18{,}000$', '27,000'],
        ['Halsey-Weir — $\\tfrac13 \\times 3 \\times 18{,}000$', '18,000'],
        ['Rowan — $\\tfrac{3}{12} \\times 9 \\times 18{,}000$', '40,500'],
      ]}},
      {'note': 'At exactly half the time allowed being saved (case (a)), Halsey and Rowan give '
               'the **same** bonus — this is not a coincidence, it is the one point where the '
               'two formulas always cross. Away from that point, Rowan gives a *smaller* bonus '
               'for very large time savings than Halsey does (Rowan is self-limiting — the '
               'bonus can never exceed the pay for time taken, however much time is saved), '
               'which is exactly why some employers prefer it: it discourages a worker from '
               'cutting corners on quality purely to report an enormous time saving.'}]}},
    {'p': 'Factors that influence the actual size of a negotiated bonus: time saved by '
          'employees; cost saved; improved productivity; the level of super-profits made by the '
          'business; achievement of other budgetary targets; and market demand for the product.'},
    {'h4': 'Individual versus group incentive schemes'},
    {'table': {'align': 'lll', 'head': ['', 'Individual incentive schemes',
      'Group incentive schemes'], 'rows': [
      ['**What it is**', 'Rewards each employee for their own efficiency.', 'A bonus awarded to '
       'a team, shared among every member by an agreed formula.'],
      ['**Advantages**', 'Motivates efficiency and productivity; can generate healthy '
       'competition; raises morale, since individual effort is rewarded; both employee and '
       'employer gain.', 'Enhances team spirit and organisational cohesiveness; quality is not '
       'unduly compromised; relatively easy and inexpensive to administer; avoids unhealthy '
       'rivalry between employees.'],
      ['**Disadvantages**', 'Quality may be sacrificed for bonus; excessive competition can '
       'cause unhealthy rivalry; setting standard performance levels can itself cause conflict; '
       'more difficult and expensive to administer than a group scheme.', 'Lazy team members are '
       'rewarded alongside hard-working ones; does not motivate individual hard work as directly.'],
    ]}},
  ]},

  {'n': '4.4', 't': 'Overtime and idle time', 'b': [
    {'h4': 'Overtime'},
    {'def': {'t': 'Overtime', 'd': 'time spent beyond the normal working hours or days.'}},
    {'p': 'Overtime wage rates are expressed as **time** plus a fraction or multiple, e.g. time '
          'and a half, time and one-third, double time, time and one-fifth.'},
    {'table': {'align': 'll', 'head': ['Term', 'Meaning'], 'rows': [
      ['**Time**', 'The basic rate — if the normal rate is ¢500/hour, the "time" is ¢500.'],
      ['**Overtime premium**', 'The *additional* rate over and above the basic rate — found by '
       'multiplying the description by the basic rate. E.g. at "time and a half" with a ¢500 '
       'basic rate, the premium is $\\tfrac12 \\times 500 = ¢250$.'],
    ]}},
    {'key': 'Overtime premium is normally treated as **indirect wages** — the exception is when '
            'overtime is worked *specifically at a customer\'s request*, to complete their order '
            'within a specified period, in which case the premium is a **direct** cost of that '
            'job.'},

    {'h4': 'Idle (waiting) time'},
    {'def': {'t': 'Idle (waiting) time (CIMA)', 'd': 'the period for which a workstation is '
                  'available for production but is not utilised, due to a shortage of tooling, '
                  'material or operators.'}},
    {'p': 'Idle time is time lost with no production — but employees are usually still paid for '
          'it. It splits into:'},
    {'ul': [
      '**Normal idle time** — uncontrollable; its cost is charged to work-in-progress, so '
      'customers bear the burden.',
      '**Abnormal idle time** — controllable; management should ensure facilities are in good '
      'condition and materials are readily available. Its cost is normally written off to the '
      'profit and loss account/income statement, though some organisations treat it as an '
      'indirect cost instead.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Illustration 4.2 — idle time, bonus and overtime together',
      'open': True, 'q': [
      {'p': 'Operative X is given 189 units at a 20-standard-minute allowance each; operative Y '
            'is given 204 units at 15 standard minutes each. Bonus is 50% of the basic rate '
            '(¢200/hour) for every hour saved. The basic week is 42 hours; hours in excess are '
            'paid at time and a half. X completes his units in 45 hours; Y completes his in 39 '
            'hours but is paid for a full guaranteed week. Because of defective material, 6 of '
            'X\'s units and 4 of Y\'s units are subsequently scrapped, though all units produced '
            'are paid for. Find, for each employee: (a) the bonus payable, (b) the total gross '
            'wage payable, (c) the wages cost per good unit made.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['', 'X', 'Y'], 'rows': [
        ['Time allowed ($189\\times20/60$; $204\\times15/60$)', '63 hrs', '51 hrs'],
        ['Time taken', '45 hrs', '39 hrs'],
        ['Time saved', '18 hrs', '12 hrs'],
      ]}},
      {'p': '**(a) Bonus** $= \\tfrac12 \\times \\text{time saved} \\times ₵200$: X $= '
            '\\tfrac12 \\times 18 \\times 200 = ₵1{,}800$; Y $= \\tfrac12 \\times 12 \\times 200 '
            '= ₵1{,}200$.'},
      {'p': '**(b) Gross wage** — both are paid for the full 42-hour guaranteed week as basic '
            'wage (₵8,400 each, $42\\times200$); X additionally worked 3 hours\' overtime '
            '($45-42$) at time-and-a-half $= 3 \\times 1.5 \\times 200 = ₵900$; Y worked fewer '
            'than 42 hours so has no overtime.'},
      {'table': {'align': 'lrr', 'head': ['', 'X (₵)', 'Y (₵)'], 'rows': [
        ['Basic wage (42 hrs guaranteed)', '8,400', '8,400'],
        ['Overtime premium', '900', '—'],
        ['Bonus', '1,800', '1,200'],
        ['**Gross wage**', '**11,100**', '**9,600**', '@tot'],
      ]}},
      {'p': '**(c) Wages cost per good unit.** Good units: X $= 189-6 = 183$; Y $= 204-4 = 200$. '
            'Before dividing, strip out any **non-productive** pay — Y was paid for 42 hours but '
            'spent only 39 on the job, so 3 hours of his guaranteed week is idle time, which is '
            'an overhead and not a cost of the units he made:'},
      {'stmt': {'t': 'Wages cost per good unit', 'rows': [
        ['', 'X (₵)', 'Y (₵)', '@hd'],
        ['Gross wage', 11100, 9600],
        ['Less: non-productive (idle) pay — Y, 3 hrs × ₵200', '—', -600],
        ['**Productive wages cost**', 11100, 9000, '@t'],
        ['Good units made', 183, 200],
        ['**Wages cost per good unit**', '₵60.66', '₵45.00', '@tt'],
      ]}},
      {'warn': 'The study text\'s own printed solution shows the N600 idle-time deduction and '
               'the resulting ₵9,000 in its working, but then prints the answer as "₵48" — which '
               'is $9{,}600 \\div 200$, i.e. the **gross** wage divided by good units, ignoring '
               'the deduction it had just made. The correct figure on its own working is '
               '$9{,}000 \\div 200 = **₵45.00**$. (Its X column is printed as "₵9,600", which is '
               'simply Y\'s gross wage copied into the wrong cell; X is '
               '$11{,}100 \\div 183 = ₵60.66$.)', 'lbl': 'Errors in the study text\'s answer'},
      {'key': 'Three separate traps in one short question. **(1)** Y is paid for 42 hours though '
              'he worked 39 — the guaranteed week creates idle time. **(2)** Bonus is calculated '
              'on hours **saved against the time allowed**, not on hours worked. **(3)** The '
              'scrapped units are still **paid for** but are not **good units**, so they inflate '
              'the numerator\'s wage without adding to the denominator — which is exactly why '
              'the cost per good unit exceeds what the bonus scheme appears to promise.'}]}},

    {'eg': {'tag': 'Study text — Illustration 4.3 (ICAG, January 1992)',
      't': 'Kokonsekyi Ltd — bonus hours, overtime, gross wages and the cost per unit accepted',
      'open': True, 'q': [
      {'p': 'Kokonsekyi Ltd presents the following information relating to a week\'s work of '
            'three of its employees:'},
      {'stmt': {'t': 'Kokonsekyi Ltd — week\'s data', 'rows': [
        ['', 'Mumu', 'Opi', 'Adam', '@hd'],
        ['Work issued (units)', 400, 600, 120],
        ['Time allowed (hours per unit)', 0.2, 0.1, 0.4],
        ['Output rejected (units)', 60, 90, 40],
        ['Hours worked', 52, 45, 40],
        ['Basic hourly rate (₵)', 30, 40, 25],
      ]}},
      {'ul': [
        'The basic working week is **40 hours**; the first 6 hours\' overtime are paid at time '
        'plus ½ and the next 10 hours at time plus ¾.',
        '**Adam spent 8 hours on indirect work**, these hours being included in the 40 hours he '
        'worked.',
        'Bonus is paid at **½ of the basic rate for all time saved**.',
        'The high rate of rejection was considered **abnormal**, due to faulty materials, and it '
        'was agreed to **credit all output** for bonus purposes.',
      ]},
      {'p': '**Required:** present in tabular form, for each employee: (a) number of bonus hours '
            'worked *(3 marks)*; (b) basic wages including overtime *(4 marks)*; (c) amount of '
            'bonus earned *(4 marks)*; (d) gross wages *(3 marks)*; (e) direct wages cost per '
            'unit accepted when overtime is worked (i) regularly throughout the year, as company '
            'policy, due to labour shortages, and (ii) specifically at the customer\'s request '
            'to expedite delivery.'}],
      'a': [
      {'h4': '(a)  Bonus hours'},
      {'note': 'Two subtleties decide this part. **All** output counts towards the time allowed, '
               'rejects included, because the question says the rejection was abnormal and all '
               'output is to be credited for bonus purposes. And Adam\'s **8 indirect hours are '
               'excluded** from his time taken — he cannot be penalised on a direct-work bonus '
               'for hours he spent on something else.'},
      {'stmt': {'t': '(a)  Time allowed, time taken and time saved', 'rows': [
        ['', 'Mumu', 'Opi', 'Adam', '@hd'],
        ['Time allowed  (400 × 0.2;  600 × 0.1;  120 × 0.4)', '80 hrs', '60 hrs', '48 hrs'],
        ['Time taken on direct work  (Adam: 40 − 8 indirect)', '52 hrs', '45 hrs', '32 hrs'],
        ['**Time saved = bonus hours**', '**28 hrs**', '**15 hrs**', '**16 hrs**', '@tt'],
      ]}},
      {'h4': '(b)  Basic wages, including overtime'},
      {'stmt': {'t': '(b)  Basic wages including overtime premium', 'rows': [
        ['', 'Mumu (₵)', 'Opi (₵)', 'Adam (₵)', '@hd'],
        ['Hours worked × basic rate  (52×30; 45×40; 40×25)', 1560, 1800, 1000],
        ['Overtime premium — first 6 hrs at ½  (Mumu 6×½×30; Opi 5×½×40)', 90, 100, '—'],
        ['Overtime premium — next hours at ¾  (Mumu 6×¾×30)', 135, '—', '—'],
        ['**Basic wages including overtime**', 1785, 1900, 1000, '@tt'],
      ]}},
      {'note': 'Mumu worked 52 hours, i.e. **12** hours of overtime: the first 6 at time plus ½ '
               'and the remaining 6 at time plus ¾ (the second band runs to 10 hours, so all 6 '
               'fall inside it). Opi worked 45 hours, i.e. 5 overtime hours, all within the '
               'first band. Adam worked exactly 40 hours, so no overtime.'},
      {'h4': '(c)  Bonus earned'},
      {'stmt': {'t': '(c)  Bonus = ½ × basic rate × time saved', 'rows': [
        ['', 'Mumu (₵)', 'Opi (₵)', 'Adam (₵)', '@hd'],
        ['½ × 30 × 28;  ½ × 40 × 15;  ½ × 25 × 16', 420, 300, 200],
      ]}},
      {'h4': '(d)  Gross wages'},
      {'stmt': {'t': '(d)  Gross wages', 'rows': [
        ['', 'Mumu (₵)', 'Opi (₵)', 'Adam (₵)', '@hd'],
        ['Basic wages including overtime', 1785, 1900, 1000],
        ['Bonus earned', 420, 300, 200],
        ['**Gross wages**', 2205, 2200, 1200, '@tt'],
      ]}},
      {'h4': '(e)  Direct wages cost per unit accepted'},
      {'p': 'Units accepted: Mumu $400-60 = 340$; Opi $600-90 = 510$; Adam $120-40 = 80$. The '
            'two cases differ in **one thing only** — whether the overtime premium is a direct '
            'cost of the job or an overhead:'},
      {'stmt': {'t': '(e)(i)  Overtime worked regularly as company policy', 'rows': [
        ['', 'Mumu', 'Opi', 'Adam', '@hd'],
        ['Direct wages = hours × basic rate *(premium excluded — it is an overhead)*',
         '₵1,560', '₵1,800', '₵800'],
        ['Units accepted', 340, 510, 80],
        ['**Direct wages cost per unit accepted**', '**₵4.59**', '**₵3.53**', '**₵10.00**',
         '@tt'],
      ]}},
      {'stmt': {'t': '(e)(ii)  Overtime worked at the customer\'s request', 'rows': [
        ['', 'Mumu', 'Opi', 'Adam', '@hd'],
        ['Direct wages = basic wages **including** overtime premium', '₵1,785', '₵1,900',
         '₵800'],
        ['Units accepted', 340, 510, 80],
        ['**Direct wages cost per unit accepted**', '**₵5.25**', '**₵3.73**', '**₵10.00**',
         '@tt'],
      ]}},
      {'key': 'This is **the** examinable principle on overtime. When overtime is worked '
              '**generally** — because the factory is short of labour, or to meet overall '
              'budgeted output — the extra hours are a cost of running the factory, so the '
              '**premium** is treated as **production overhead** and only the basic rate is '
              'charged to the job. When overtime is worked at a **specific customer\'s '
              'request**, the premium is caused by that customer and is a **direct cost** of '
              'their job. In both cases the basic rate for the hours worked is always direct. '
              'Adam\'s figure is unchanged between the two because he worked no overtime — note '
              'also that only his **32 direct hours** (₵800) are charged to the product; his 8 '
              'indirect hours are overhead.'},
      {'warn': 'The study text\'s printed solution for this illustration is heavily garbled and '
               'internally inconsistent: its "summary of answers" gives Mumu\'s basic wages as '
               '₵1,650 while its own working shows ₵1,785; it gives Adam\'s as ₵1,135 while its '
               'working shows ₵1,000 (the stray ₵135 is Mumu\'s second overtime premium, copied '
               'into the wrong column); and its gross wages row carries those errors forward '
               '(₵2,070 for Mumu, ₵1,135 for Adam). Every figure above has been recomputed from '
               'the question data. Its part (e)(ii) figure for Opi, ₵3.75, should be '
               '$1{,}900 \\div 510 = **₵3.73**$.',
       'lbl': 'Errors in the study text\'s solution'}]}},
  ]},

  {'n': '4.5', 't': 'Direct and indirect cost of labour; minimising labour cost', 'b': [
    {'p': 'As already covered in Chapters 1–2, labour cost is either direct or indirect.'},
    {'def': {'t': 'Direct labour cost', 'd': 'labour cost incurred on employees directly '
                  'transforming raw materials into finished goods. Only the **basic wages** paid '
                  'to direct workers constitute direct labour cost.'}},
    {'warn': 'Policy-related costs incurred on a direct worker are **not** direct labour cost — '
             'they are indirect labour, even though the worker themselves is a direct worker. '
             'Examples: workers\' compensation insurance premiums; the employer\'s social '
             'security fund contribution; bonuses paid to employees; and overtime premium paid '
             'where overtime is worked *regularly, as company policy* (not at a customer\'s '
             'specific request — see §4.4). Wages cost on **indirect** workers is, straight-'
             'forwardly, indirect wages.'},

    {'eg': {'tag': 'Study text — Illustration 4.4',
      't': 'Charging overtime to jobs — the same hours, two different answers',
      'open': True, 'q': [
      {'p': 'A company\'s basic wage rate is **¢0.45 per hour**, and its overtime rates are: '
            'evenings **1⅓** (time and a third); weekends **double time**. During the previous '
            'year the following hours were worked:'},
      {'stmt': {'t': 'Hours worked in the year', 'rows': [
        ['Normal time', '', '440,000 clock hours'],
        ['Time plus ⅓ (evenings)', '', '40,000 clock hours'],
        ['Double time (weekends)', '', '20,000 clock hours'],
      ]}},
      {'p': 'The following times were worked on the stated jobs:'},
      {'stmt': {'t': 'Clock hours by job', 'rows': [
        ['', 'Job X', 'Job Y', 'Job Z', '@hd'],
        ['Normal time', 6000, 10000, 8000],
        ['Evening overtime', 600, 1200, 2100],
        ['Weekend overtime', 200, 100, 600],
        ['**Total clock hours**', 6800, 11300, 10700, '@tt'],
      ]}},
      {'p': '**Required:** calculate the labour cost chargeable to each job in each of the '
            'following circumstances: **(a)** where overtime is worked regularly throughout the '
            'year as company policy, due to a labour shortage; **(b)** where overtime is worked '
            'specifically at the customer\'s request, to expedite delivery.'},
      {'warn': 'The study text prints Job X\'s normal time as **60,000** clock hours. It is '
               '**6,000** — its own solution totals Job X at 6,800 hours, which is only possible '
               'as $6{,}000 + 600 + 200$.', 'lbl': 'Source typo corrected'}],
      'a': [
      {'h4': '(a)  Overtime worked regularly as company policy'},
      {'p': 'The overtime premium is caused by the general shortage of labour, not by any '
            'particular customer, so it is **production overhead**. Each job is charged only '
            'with its clock hours at the **basic rate**:'},
      {'stmt': {'t': '(a)  Labour cost chargeable to each job', 'rows': [
        ['', 'Job X', 'Job Y', 'Job Z', '@hd'],
        ['Total clock hours', 6800, 11300, 10700],
        ['× basic rate ¢0.45', '', '', ''],
        ['**Labour cost chargeable (¢)**', 3060, 5085, 4815, '@tt'],
      ]}},
      {'h4': '(b)  Overtime worked at the customer\'s request'},
      {'p': 'The premium is now caused by the specific customer and is charged to their job. '
            'The **premium** is the excess over the basic rate: ⅓ of basic for evening work, and '
            'a further 1 × basic for weekend (double-time) work.'},
      {'stmt': {'t': '(b)  Labour cost chargeable to each job', 'rows': [
        ['', 'Job X (¢)', 'Job Y (¢)', 'Job Z (¢)', '@hd'],
        ['Clock hours at basic rate (as in (a))', 3060, 5085, 4815],
        ['Evening overtime premium: hours × ⅓ × ¢0.45', 90, 180, 315],
        ['Weekend overtime premium: hours × 1 × ¢0.45', 90, 45, 270],
        ['**Labour cost chargeable**', 3240, 5310, 5400, '@tt'],
      ]}},
      {'note': 'Working the premiums: Job X evening $600 \\times \\tfrac13 \\times 0.45 = 90$; '
               'Job Y $1{,}200 \\times \\tfrac13 \\times 0.45 = 180$; Job Z '
               '$2{,}100 \\times \\tfrac13 \\times 0.45 = 315$. Weekend: Job X '
               '$200 \\times 1 \\times 0.45 = 90$; Job Y $100 \\times 0.45 = 45$; Job Z '
               '$600 \\times 0.45 = 270$.'},
      {'key': 'Job Z is the one to look at. Under (a) it is the **cheapest** of the three jobs '
              'by labour cost; under (b) it becomes the **dearest**, overtaking Job Y — because '
              'it absorbed far more overtime (2,700 of its 10,700 hours) than the others. '
              'Nothing about the work changed between the two answers. Only the **reason** for '
              'the overtime changed, and with it the question of who should bear its cost. That '
              'is why an examiner can set the same figures twice and expect two different '
              'answers.'}]}},

    {'h4': 'Labour cost minimisation techniques'},
    {'ul': [
      'effective labour monitoring and control;',
      'reduction of labour turnover;',
      'elimination or reduction of labour-related fraud.',
    ]},

    {'eg': {'tag': 'Study text — Illustration 4.5 (ICAG, November 1999, 20 marks)',
      't': 'Mame Coins — the full cost of farm labour, and the net wages paid',
      'open': True, 'q': [
      {'p': 'Mame Coins employs on her farm **120 workers as direct labour** and **15 workers as '
            'indirect labour**. The farm remunerates its labour as follows:'},
      {'ol': [
        'Direct labour is paid regularly **based on units of output** at the rate of **¢12,250 '
        'per unit**.',
        'Indirect labour is paid regularly **based on hours worked** at the rate of **¢14,000 '
        'per hour**.',
        'Overtime premium is paid to all factory workers for the hours worked at the following '
        'rates: **¢26,000 per hour for direct labour**; **¢28,000 per hour for indirect '
        'labour**.',
        'The firm makes deductions and contributions to the social security scheme. The employer '
        'and employee contribute **10%** and **5%** respectively of gross pay.',
        'Each worker contributes dues to the local workers\' union at **¢50,000 per direct '
        'labour per month** and **¢80,000 per indirect labour per month**, deducted at source.',
        'The firm operates a **workmen\'s compensation insurance** scheme for all factory '
        'workers. The monthly premium is **¢7,500,000**, divisible between direct and indirect '
        'labour in the ratio **4 : 1**.',
        '**PAYE tax** is approximately **8% of monthly gross income**.',
      ]},
      {'p': 'During June 1999 the farm produced **30,000 units** during regular working time of '
            '**8 hours a day for 22 days**. The farm worked overtime of **6 hours a day for 4 '
            'days** during the month and produced **3,200 more units**.'},
      {'p': '**Required:** determine (i) the cost to Mame Coins of farm labour for June 1999, '
            'distinguishing between direct and indirect labour costs; and (ii) the total net '
            'wages paid to the workers for June 1999.'}],
      'a': [
      {'h4': 'Step 1 — the hours and the output'},
      {'stmt': {'t': 'Analysis of hours and units', 'rows': [
        ['', 'Direct workers', 'Indirect workers', '@hd'],
        ['Number of workers', 120, 15],
        ['Regular hours each (8 hrs × 22 days)', '176 hrs', '176 hrs'],
        ['Overtime hours each (6 hrs × 4 days)', '24 hrs', '24 hrs'],
        '@gap',
        ['Total regular hours', '21,120', '2,640'],
        ['Total overtime hours', '2,880', '360'],
        ['**Total hours worked**', '**24,000**', '**3,000**', '@t'],
        '@gap',
        ['Units produced in regular time', '30,000', '—'],
        ['Units produced in overtime', '3,200', '—'],
        ['**Total units produced**', '**33,200**', '—', '@t'],
      ]}},
      {'h4': 'Step 2 — basic wages'},
      {'p': 'Direct workers are paid **by output**, indirect workers **by hours**:'},
      {'stmt': {'t': 'Basic wages', 'rows': [
        ['Direct: 33,200 units × ¢12,250', '', 406700000],
        ['Indirect: 3,000 hours × ¢14,000', '', 42000000],
      ]}},
      {'h4': 'Step 3 — overtime premium'},
      {'p': 'The overtime **rates** given are the full rates for overtime hours, so the '
            '**premium** is the excess of overtime pay over what those hours have already '
            'earned in basic wages.'},
      {'stmt': {'t': 'Direct labour overtime premium', 'rows': [
        ['Overtime pay: 2,880 hrs × ¢26,000', '', 74880000],
        ['Overtime piece rate per unit: ¢74,880,000 ÷ 3,200 units', '', '¢23,400'],
        ['Less: normal piece rate already in basic wages', '', '¢12,250'],
        ['**Premium per unit produced in overtime**', '', '¢11,150', '@t'],
        ['**Overtime premium: 3,200 units × ¢11,150**', '', 35680000, '@tt'],
      ]}},
      {'stmt': {'t': 'Indirect labour overtime premium', 'rows': [
        ['Overtime pay: 360 hrs × ¢28,000', '', 10080000],
        ['Less: those hours already paid at basic rate (360 × ¢14,000)', '', -5040000],
        ['**Overtime premium**', '', 5040000, '@tt'],
      ]}},
      {'h4': 'Step 4 — employer-borne on-costs'},
      {'stmt': {'t': 'Workmen\'s compensation and employer\'s social security', 'rows': [
        ['', 'Direct', 'Indirect', 'Total', '@hd'],
        ['Workmen\'s compensation premium, ¢7,500,000 in the ratio 4 : 1', 6000000, 1500000,
         7500000],
        ['Employer\'s SSF, 10% of basic wages', 40670000, 4200000, 44870000],
      ]}},
      {'h4': '(i)  Cost to Mame Coins of farm labour for June 1999'},
      {'stmt': {'t': 'Total labour cost, June 1999', 'rows': [
        ['', 'Direct (¢)', 'Indirect (¢)', 'Total (¢)', '@hd'],
        ['Basic wages', 406700000, 42000000, 448700000],
        ['Overtime premium', 35680000, 5040000, 40720000],
        ['Workmen\'s compensation premium', 6000000, 1500000, 7500000],
        ['Employer\'s social security contribution (10%)', 40670000, 4200000, 44870000],
        ['**Total cost of farm labour**', 489050000, 52740000, 541790000, '@tt'],
      ]}},
      {'key': 'Only the **basic wages of direct workers** — ¢406,700,000 — are *direct* labour '
              'cost in the costing sense. The overtime premium (overtime here is regular company '
              'practice, not customer-driven), the compensation insurance and the employer\'s '
              'social security contribution are all **policy-related on-costs** and are treated '
              'as **indirect** labour, i.e. production overhead, even though they are incurred '
              'on direct workers. The question asks for the split between direct and indirect '
              '**workers**, which is what the columns above show; be ready to be asked for the '
              'split between direct and indirect **cost**, which is a different cut of the same '
              'figures.'},
      {'h4': '(ii)  Total net wages paid for June 1999'},
      {'stmt': {'t': 'Payroll — direct and indirect workers', 'rows': [
        ['', 'Direct workers (¢)', 'Indirect workers (¢)', '@hd'],
        ['Basic wages', 406700000, 42000000],
        ['Less: employee social security contribution, 5%', -20335000, -2100000],
        ['', 386365000, 39900000, '@t'],
        ['Add: overtime premium', 35680000, 5040000],
        ['**Taxable pay**', 422045000, 44940000, '@t'],
        ['Less: PAYE at 8%', -33763600, -3595200],
        ['Less: local union dues (120 × ¢50,000;  15 × ¢80,000)', -6000000, -1200000],
        ['**Net wages paid**', 382281400, 40144800, '@tt'],
        '@gap',
        ['Number of employees', 120, 15],
        ['**Net wage per employee**', '¢3,185,678', '¢2,676,320'],
      ]}},
      {'stmt': {'t': 'Total net wages paid for June 1999', 'rows': [
        ['Direct workers', '', 382281400],
        ['Indirect workers', '', 40144800],
        ['**Total net wages paid**', '', 422426200, '@tt'],
      ]}},
      {'note': 'Note the order of the deductions in the official solution: the employee\'s 5% '
               'social security is taken off the **basic wages** first, and the overtime premium '
               'is then added to arrive at taxable pay, so the premium escapes the social '
               'security charge but not PAYE. That is the treatment the model answer uses; if a '
               'question tells you social security is charged on **gross** pay, the deduction '
               'would instead be 5% of basic plus premium. Read the question, and state the '
               'basis you have used.'},
      {'warn': 'The cost to the employer (¢541,790,000) and the net wages paid to the employees '
               '(¢422,426,200) are two different questions and two different answers — the gap '
               'of ¢119,363,800 is made up of the employer\'s own contributions (social security '
               'and compensation insurance, ¢52,370,000) plus the deductions withheld from the '
               'employees and paid over to third parties (PAYE ¢37,358,800, employee social '
               'security ¢22,435,000 and union dues ¢7,200,000). Candidates routinely answer one '
               'when the examiner asked for the other.'}]}},
  ]},

  {'n': '4.6', 't': 'Labour turnover', 'b': [
    {'def': {'t': 'Labour turnover', 'd': 'the percentage change in the labour force during a '
                  'given period — also called the labour turnover ratio (or rate).'}},
    {'p': 'Three ways to measure it:'},
    {'fbox': {'h': 'Labour turnover formulas', 'rows': [
      {'lb': 'Labour turnover rate',
       'tex': '\\dfrac{\\text{Number of employees leaving during the period}}{\\text{Average '
              'number of employees for the period}} \\times 100'},
      {'lb': 'Flux method',
       'tex': '\\dfrac{\\text{Workers joining} + \\text{Workers leaving during the period}}'
              '{\\text{Average number of employees during the period}}'},
      {'lb': 'Separation method',
       'tex': '\\dfrac{\\text{Number of workers replaced during the period}}{\\text{Average '
              'number of employees during the period}}'},
      {'lb': 'Average number of employees',
       'tex': '\\tfrac12 \\times (\\text{Number at beginning of period} + \\text{Number at end '
              'of period})'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration — labour turnover rate', 'open': True, 'q': [
      {'p': 'At the start of March there were 201 employees; 3 started and 5 left during the '
            'month. Find the labour turnover rate.'}],
      'a': [
      {'p': 'Employees at end of month $= 201 + 3 - 5 = 199$. Average number of employees '
            '$= \\tfrac12(201+199) = 200$.'},
      {'tex': '\\text{Labour turnover rate} = \\dfrac{5}{200} \\times 100 = 2.50\\%'}]}},
    {'key': 'To be useful, a labour turnover rate must be **compared** — against previous '
            'periods, and (where available) against other businesses in the area and the '
            'industry as a whole. A rising rate follows either more leavers or a smaller total '
            'workforce.'},

    {'h4': 'The cost of a high labour turnover rate'},
    {'p': 'A high rate causes loss of output, lower morale and higher cost. Output is lost '
          'because of: the gap between a leaver and their replacement; the time needed to train '
          'a new employee up to the departing employee\'s efficiency; and reduced effort from an '
          'employee in the days/weeks immediately before they leave.'},
    {'p': 'On top of the higher unit cost from reduced production and low morale, these costs '
          'tend to rise as turnover rises:'},
    {'ol': [
      'advertising for personnel, and interviewing expenses;',
      'reimbursing removal/settling-in expenses (furniture removal, subsistence allowance '
      'between the commencement and move dates);',
      'training — the new employee\'s wages during training, instructors\' wages/salaries, and '
      'training materials;',
      'scrap and defective work during a new employee\'s initial stages;',
      'machine breakdown; and',
      'pension-scheme administration.',
    ]},

    {'h4': 'Causes of labour turnover'},
    {'ul': [
      'dissatisfaction with the job or wages;',
      'hours of work or working conditions;',
      'discontent with supervisors or colleagues;',
      'lack of promotion opportunities;',
      'personal matters — ill health, marriage, pregnancy, relocation; and',
      'discharge for redundancy, incompetence, lateness, absenteeism or discipline.',
    ]},

    {'h4': 'Reducing the labour turnover rate'},
    {'ol': [
      'provide regular statistics analysing turnover by cause, flagging avoidable/unavoidable '
      'and voluntary/dismissed — though leavers do not always give their true reason;',
      'improve applicant selection, to prevent discontented or unsuitable hires;',
      'plan labour requirements properly, to avoid redundancy;',
      'consider a high-wage plan or other incentives;',
      'keep the working environment congenial;',
      'consider transferring a dissatisfied employee to another department;',
      'hold annual medical check-ups, to catch ill-health early;',
      'ensure fringe benefits (pension, subsidised meals, sports/social facilities) are '
      'competitive; and',
      'develop better management-worker relationships.',
    ]},
    {'note': 'A target labour turnover rate can be set, with the personnel manager held '
             'accountable when the actual rate exceeds it.'},

    {'h4': 'Payroll fraud and internal check'},
    {'p': 'There is ample scope for fraud at every stage of preparing and paying wages, so '
          'controls must exist to prevent it, or detect it early. Two classic dangers:'},
    {'ul': [
      '**Ghost workers** — paying wages to employees who do not actually exist.',
      'Paying a real employee **more** than they are entitled to.',
    ]},
    {'p': 'Precautions to reduce payroll fraud:'},
    {'ol': [
      'segregate duties — e.g. the clerk who prepares the wage sheet should not also make up or '
      'distribute the pay packets;',
      'adopt adequate authorisation — piece-work tickets signed by an inspector and the '
      'employee\'s foreman; only properly authorised overtime is paid; wage-rate/salary changes '
      'processed only on a signed form from the personnel manager;',
      'supervise the distribution of pay envelopes by a senior official who can identify '
      'recipients;',
      'institute suitable procedures, e.g. for handling unclaimed wages;',
      'run a programme of internal checks — the personnel officer periodically checking the '
      'payroll for fictitious employees; and',
      'in a sufficiently large organisation, involve internal audit in building and running the '
      'internal-check programme.',
    ]},
  ]},

  {'n': '4.7', 't': 'Payroll preparation and accounting', 'b': [
    {'h4': 'Types of payroll'},
    {'def': {'t': 'Payroll', 'd': 'the process of determining each employee\'s net wage '
                  'earnings — carried out **manually** (by human effort) or via a '
                  '**computerised** system, which processes inputs such as hours worked, '
                  'overtime hours, units produced, the wage rate per unit/hour, and statutory '
                  'and voluntary deductions, to arrive at net earnings and total deductions.'}},

    {'h4': 'Preparing the payroll'},
    {'steps': [
      'Determine each employee\'s basic wages — hours worked (or units produced) × the agreed '
      'wage rate.',
      'Add all other allowances to basic wages, to obtain gross wages.',
      'Calculate the deductions, of two types: **statutory** (required by law — social security '
      'contributions, employee Personal Income Tax/PAYE, National Health Insurance) and '
      '**voluntary** (trade-union contributions, provident-fund contribution, employee-welfare '
      'contribution).',
      'Deduct total deductions from gross wages, to obtain net wages.',
    ]},
    {'fbox': {'h': 'Payroll build-up', 'rows': [
      {'lb': 'Basic wages', 'tex': '\\text{Hours worked (or units produced)} \\times '
        '\\text{agreed rate}'},
      {'lb': 'Gross wages', 'tex': '\\text{Basic wages} + \\text{other allowances}'},
      {'lb': 'Net wages', 'tex': '\\text{Gross wages} - \\text{statutory deductions} - '
        '\\text{voluntary deductions}'},
    ]}},

    {'h4': 'Labour cost accounting versus payroll accounting'},
    {'table': {'align': 'll', 'head': ['', 'Labour cost accounting', 'Payroll accounting'],
      'rows': [
      ['**Objective**', 'Ascertain the labour cost chargeable to products, services, jobs, '
       'customers, clients and overhead accounts.', 'Compute each employee\'s earnings, and the '
       'various payments made for/on behalf of employees.'],
      ['**What it covers**', 'Wages and salaries; workers\' compensation insurance; employee '
       'bonuses; employee share schemes.', 'The employer\'s social security contribution; the '
       'employee\'s social security contribution; personal income tax; welfare deductions.'],
      ['**What it excludes**', '—', 'Labour costs such as workmen\'s compensation and employee '
       'insurance — payroll accounting only considers amounts payable **to or on behalf of** '
       'employees.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 4.6 — Clay Products Ltd: three remuneration '
      'methods compared', 'open': True, 'q': [
      {'p': 'Clay Products Ltd is choosing an incentive scheme. July 2005 payroll extract for '
            'four employees:'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Michael', 'Gerald', 'Cynthia', 'William'],
        'rows': [
        ['Actual hours worked', '152', '144', '160', '136'],
        ['Wage rate per hour (₵)', '45,000', '30,000', '37,500', '54,000'],
        ['Output — Product A (units)', '168', '480', '—', '480'],
        ['Output — Product B (units)', '288', '304', '—', '1,080'],
        ['Output — Product C (units)', '368', '—', '200', '—'],
      ]}},
      {'p': 'Standard time per unit: Product A 6 minutes, Product B 9 minutes, Product C 15 '
            'minutes; each minute earned is valued at ₵750 for piecework purposes. Required: '
            '(a) each employee\'s earnings under (i) the guaranteed hourly-rate method, '
            '(ii) piecework with earnings guaranteed at 75% of basic pay, and (iii) a premium '
            'bonus scheme in which the employee receives two-thirds of time saved, in addition '
            'to hourly pay. *(ICAG, Nov. 2005, 14 marks)*'}],
      'a': [
      {'h4': '(a)(i) Guaranteed hourly-rate (basic wage) method'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Michael', 'Gerald', 'Cynthia', 'William'],
        'rows': [
        ['Hours worked × rate/hour', '152×45,000', '144×30,000', '160×37,500', '136×54,000'],
        ['**Basic wage (₵)**', '**6,840,000**', '**4,320,000**', '**6,000,000**',
         '**7,344,000**'],
      ]}},
      {'h4': '(a)(ii) Piecework, guaranteed at 75% of basic pay'},
      {'p': 'Piece rate per unit = standard minutes × ₵750/minute: Product A = $6\\times750 = '
            '₵4{,}500$; Product B = $9\\times750 = ₵6{,}750$; Product C = $15\\times750 = '
            '₵11{,}250$.'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Michael', 'Gerald', 'Cynthia', 'William'],
        'rows': [
        ['Piecework earnings (₵)', '168×4,500 + 288×6,750 + 368×11,250 = 6,840,000',
         '480×4,500 + 304×6,750 = 4,212,000', '200×11,250 = 2,250,000',
         '480×4,500 + 1,080×6,750 = 9,450,000'],
        ['75% of basic wage (₵)', '5,130,000', '3,240,000', '4,500,000', '5,508,000'],
        ['**Entitlement (the higher of the two) (₵)**', '**6,840,000 (piecework)**',
         '**4,212,000 (piecework)**', '**4,500,000 (the 75% guarantee)**',
         '**9,450,000 (piecework)**'],
      ]}},
      {'key': 'Cynthia is the one employee whose piecework earnings (₵2,250,000) fall *below* '
              'the 75%-of-basic guarantee (₵4,500,000) — she alone is paid the guaranteed '
              'minimum rather than her piece-rate output; all three other employees out-earn '
              'their guarantee on piecework and are paid the piecework figure.'},
      {'h4': '(a)(iii) Premium bonus — two-thirds of time saved, plus hourly pay'},
      {'p': 'Time allowed = $\\sum(\\text{output} \\times \\text{standard minutes per unit})/60$, '
            'compared with actual hours worked (= time taken):'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Michael', 'Gerald', 'Cynthia', 'William'],
        'rows': [
        ['Time allowed (hrs)',
         '(168×6+288×9+368×15)/60 = 152.0', '(480×6+304×9)/60 = 93.6',
         '(200×15)/60 = 50.0', '(480×6+1,080×9)/60 = 210.0'],
        ['Time taken (hrs)', '152', '144', '160', '136'],
        ['Time saved (hrs)', '0', 'nil (took longer than allowed)',
         'nil (took longer than allowed)', '74'],
        ['Bonus (₵)', '—', '—', '—', '⅔×74×54,000 = 2,664,000'],
        ['**Total wages (₵)**', '**6,840,000** (basic only)', '**4,320,000** (basic only)',
         '**6,000,000** (basic only)', '**10,008,000** (basic 7,344,000 + bonus 2,664,000)'],
      ]}},
      {'note': 'Gerald and Cynthia both took *longer* than their standard time allowed (Gerald '
               '144 hrs actual against 93.6 hrs allowed; Cynthia 160 hrs actual against 50 hrs '
               'allowed) — time saved cannot be negative, so neither earns any bonus under this '
               'scheme, and each simply receives their guaranteed hourly basic wage, same as '
               'under method (i).'}]}},
  ]},

  {'n': '4.8', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§4.2 Administration** — recruitment (job analysis → advertise internally/externally → '
      'shortlist → select); induction (culture) vs placement (post-fitting); 4 control '
      'mechanisms (time-keeping, monitoring/supervision, evaluation, reward schemes); job '
      'evaluation ranks the **job**, merit rating ranks the **jobholder**; work study = method '
      'study + work measurement.',
      '**§4.3 Remuneration** — time rate (hours × rate, simple but no output incentive) vs '
      'piece rate (units × rate, in straight/guaranteed-day-rate/differential forms); the three '
      'premium bonus schemes (Halsey ½, Halsey-Weir ⅓, Rowan proportional — Rowan and Halsey '
      'coincide exactly at 50% time saved); individual vs group incentive schemes.',
      '**§4.4 Overtime & idle time** — overtime premium is indirect wages unless worked at a '
      'customer\'s specific request (then direct); idle time is normal (uncontrollable, charged '
      'to WIP) or abnormal (controllable, written off to P&L).',
      '**§4.5 Direct/indirect labour, minimisation** — only *basic* wages of a direct worker are '
      'direct labour cost; policy-related add-ons (insurance, SSF, bonuses, regular-policy '
      'overtime premium) are always indirect, even on a direct worker; 3 cost-minimisation '
      'techniques.',
      '**§4.6 Labour turnover** — 3 formulas (turnover rate, flux method, separation method), '
      'all needing the average-employees denominator; causes and 9 named reduction measures; '
      'ghost workers and payroll-fraud controls (segregation of duties, authorisation, '
      'supervision, internal checks).',
      '**§4.7 Payroll** — manual vs computerised; the 4-step preparation procedure; statutory vs '
      'voluntary deductions; labour cost accounting (cost to products) vs payroll accounting '
      '(amounts payable to/for employees) are **not** the same scope.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Time allowed** — the expected time for a task. **Time taken** — actual time spent. '
      '**Time saved** — allowed minus taken.',
      '**Job evaluation** — ranks the job. **Merit rating** — ranks the jobholder\'s performance.',
      '**Method study** — finds a better way to do work. **Work measurement** — times the '
      'chosen way.',
      '**Normal idle time** — uncontrollable, costed to WIP. **Abnormal idle time** — '
      'controllable, written off to P&L.',
      '**Overtime premium** — indirect wages, unless the overtime was at a customer\'s specific '
      'request.',
      '**Labour turnover** — the percentage change in the workforce over a period. **Ghost '
      'worker** — a non-existent employee wages are fraudulently paid to.',
      '**Labour cost accounting** — costing labour to products/jobs. **Payroll accounting** — '
      'computing and paying what is owed to/for employees.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'Labour cost formulas (recap)', 'rows': [
      {'lb': 'Gross wage (time rate)', 'tex': '\\text{Hours worked} \\times \\text{Rate/hour}'},
      {'lb': 'Straight piece rate', 'tex': '\\text{Units produced} \\times \\text{Rate/unit}'},
      {'lb': 'Halsey bonus', 'tex': '\\tfrac12 \\times \\text{Time saved} \\times \\text{Day '
        'rate}'},
      {'lb': 'Halsey-Weir bonus', 'tex': '\\tfrac13 \\times \\text{Time saved} \\times '
        '\\text{Day rate}'},
      {'lb': 'Rowan bonus', 'tex': '\\dfrac{\\text{Time saved}}{\\text{Time allowed}} \\times '
        '\\text{Time taken} \\times \\text{Day rate}'},
      {'lb': 'Labour turnover rate', 'tex': '\\dfrac{\\text{Leavers}}{\\text{Average employees}} '
        '\\times 100'},
    ]}},
  ]},

  {'n': '4.9', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Under labour incentive schemes, bonus is paid (A) Every December  (B) Each time the '
        'company receives a large order  (C) To very good employees  (D) Anytime there is '
        'surplus money in the treasury  (E) Over and above the basic pay to reward extra time '
        'worked or time saved',
        'Overtime is (A) Work done over a period of time  (B) Time spent calling over '
        'production figures  (C) Time spent by the employee working beyond the normal working '
        'hours  (D) Time spent by the employee in the changing room  (E) Time wasted when '
        'production machines are idle',
        'PAYE is an acronym for (A) Pay As You Engage  (B) Pay According to Your Expectation  '
        '(C) Pay All Your Employees  (D) Payment At Year End  (E) Pay As You Earn',
        'Ghost workers are (A) Former employees who are now dead  (B) Employees involved in an '
        'accident whilst working  (C) Employees always on sick leave  (D) Workers who do not '
        'exist but in whose names salaries are being paid  (E) Those who work in the cemetery',
        'Gross wages are calculated by adding (A) All allowances to basic wages  '
        '(B) All deductions to basic wages  (C) Pension deduction to PAYE  (D) Bonuses and '
        'allowances together  (E) Twelve months\' wages together',
        'Time allowed minus time taken equals …………',
        'Labour costs incurred on employees engaged in directly transforming raw materials into '
        'finished goods are referred to as ……………….',
        'The extent to which employees leave an organisation is known as …………………',
        'The product of hours worked and wage rate per hour is …………………………….',
        'The card issued in the name of each employee, inserted into an electronic recording '
        'machine to capture time spent at work, is called...…………',
      ]}],
      'a': [
      {'ol': [
        '**E** — over and above the basic pay, to reward extra time worked or time saved.',
        '**C** — time spent by the employee working beyond the normal working hours.',
        '**E — Pay As You Earn.**',
        '**D** — workers who do not exist but in whose names salaries are being paid.',
        '**A** — all allowances added to basic wages.',
        '**Time saved.**',
        '**Direct labour cost(s).**',
        '**Labour turnover.**',
        '**Basic wage.**',
        '**Clock card.**',
      ]}]}},
  ]},

  {'n': '4.10', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with nine examination-type questions. All are '
          'reproduced below with full answers. (The book leaves the ACCA Costing question '
          'between 4.4 and 4.6 unnumbered; it is shown here as 4.5.)'},

    {'eg': {'tag': 'Exam type — Q4.1 (20 marks) — ICAG, November 2003',
      't': 'Cee Ltd — a group bonus scheme, net pay, and a cost-plus charge per household',
      'q': [
      {'p': 'Cee Ltd is a waste collection company engaged in the collection of household refuse '
            'in the Gonor District. The District is divided into **three areas** made up of a '
            'total of **1,000 households**. Each area enjoys 2 days of refuse collection during '
            'the **6-day working week of 48 hours**.'},
      {'p': 'During April, the company employed **2 drivers and 4 labourers**, grouped into **2 '
            'gangs**, Gang A and Gang B. A gang is made up of 1 driver and 2 labourers. A driver '
            'is paid **¢2,500 per hour** and a labourer **¢3,125 per hour**.'},
      {'p': 'A **group bonus scheme** is in operation, which requires that hours over the normal '
            'working hours are **shared equally among members of a gang** and paid at a rate of '
            '**¢10,000 per driver** and **¢12,000 per labourer**. During April, Gang A worked '
            '**219 hours** and Gang B worked **228 hours**.'},
      {'p': '**Required:** (a) calculate the total cost of providing this service in the '
            'district for April *(8 marks)*; (b) calculate the net pay due to the workers for '
            'April *(8 marks)*; (c) the company charges the households at cost plus 20% — how '
            'much should Cee Ltd charge each household for the month? *(4 marks)*'},
      {'p': '**Assume:** (1) an income tax rate of 10% of total earnings; (2) statutory social '
            'security deductions of 12% for the employer and 5% for the employee; (3) 4 weeks in '
            'the month of April.'}],
      'a': [
      {'h4': 'Step 1 — normal hours and excess hours'},
      {'stmt': {'t': 'Hours', 'rows': [
        ['Normal hours for the month (48 hours × 4 weeks)', '', '192 hours'],
        '@gap',
        ['Gang A — hours worked', '', '219 hours'],
        ['Gang A — hours over normal (219 − 192)', '', '27 hours'],
        ['Shared equally among the 3 gang members (27 ÷ 3)', '', '9 hours each'],
        '@gap',
        ['Gang B — hours worked', '', '228 hours'],
        ['Gang B — hours over normal (228 − 192)', '', '36 hours'],
        ['Shared equally among the 3 gang members (36 ÷ 3)', '', '12 hours each'],
      ]}},
      {'h4': 'Step 2 — basic wages and group bonus'},
      {'stmt': {'t': 'Basic wages for the month (192 normal hours each)', 'rows': [
        ['Drivers:  2 × 192 hrs × ¢2,500', '', 960000],
        ['Labourers:  4 × 192 hrs × ¢3,125', '', 2400000],
        ['**Total basic wages**', '', 3360000, '@t'],
      ]}},
      {'stmt': {'t': 'Group bonus', 'rows': [
        ['', 'Gang A (¢)', 'Gang B (¢)', 'Total (¢)', '@hd'],
        ['Driver:  9 hrs × ¢10,000;  12 hrs × ¢10,000', 90000, 120000, 210000],
        ['Labourers:  2 × 9 × ¢12,000;  2 × 12 × ¢12,000', 216000, 288000, 504000],
        ['**Bonus**', 306000, 408000, 714000, '@tt'],
      ]}},
      {'h4': '(a)  Total cost of providing the service for April'},
      {'stmt': {'t': 'Total cost to the company', 'rows': [
        ['Basic wages', '', 3360000],
        ['Group bonus', '', 714000],
        ['**Gross earnings**', '', 4074000, '@t'],
        ['Employer\'s social security contribution, 12% of ¢4,074,000', '', 488880],
        ['**Total cost of providing the service**', '', 4562880, '@tt'],
      ]}},
      {'h4': '(b)  Net pay due to the workers for April'},
      {'stmt': {'t': 'Net pay', 'rows': [
        ['Gross earnings', '', 4074000],
        ['Less: income tax at 10% of total earnings', '', -407400],
        ['Less: employee social security at 5%', '', -203700],
        ['**Net pay due to the workers**', '', 3462900, '@tt'],
      ]}},
      {'h4': '(c)  Charge per household'},
      {'stmt': {'t': 'Cost plus 20%', 'rows': [
        ['Total cost (from (a))', '', 4562880],
        ['Add: mark-up at 20%', '', 912576],
        ['**Total charge to the district**', '', 5475456, '@t'],
        ['Number of households', '', 1000],
        ['**Charge per household for the month**', '', '¢5,475.46', '@tt'],
      ]}},
      {'key': 'The three parts answer three different questions and must not be confused. '
              '**(a)** is the cost to the **employer** — gross earnings *plus* the employer\'s '
              'own social security contribution. **(b)** is what the **workers receive** — gross '
              'earnings *less* the deductions withheld from them. The employer\'s 12% never '
              'appears in (b), and the employee\'s 5% and the 10% tax never appear in (a). '
              '**(c)** builds on (a), because a price must recover what the service actually '
              'costs the company, not what the workers take home.'},
      {'note': 'The three areas and the two collection days per week are context, not '
               'computation — nothing in the answer depends on them. Examiners include such '
               'detail deliberately; identify what each figure is *for* before using it.'}]}},

    {'eg': {'tag': 'Exam type — Q4.2',
      't': 'Five sequential hand operations — workers required and weekly labour cost',
      'q': [
      {'p': 'An item passes through 5 successive hand operations in sequence as follows:'},
      {'stmt': {'t': 'Operation data', 'rows': [
        ['Operation', 'Time per article (minutes)', 'Grade of employee', 'Wage rate per hour',
         '@hd'],
        [1, 12, 'A', '50p'],
        [2, 20, 'B', '55p'],
        [3, 30, 'C', '60p'],
        [4, 10, 'D', '70p'],
        [5, 15, 'E', '80p'],
      ]}},
      {'p': 'A 40-hour week is worked and a production target of **720 dozen items** has been '
            'set. **Required:** calculate (a) the number of workers required; (b) the weekly '
            'cost of each operation; (c) the total labour cost per week.'},
      {'warn': 'The study text prints the working week as "An Hour week", with the number lost. '
               'A **40-hour week** is assumed below — the standard figure in this question and '
               'the only one that gives whole-ish worker numbers. State the assumption if you '
               'meet this question in an exam.', 'lbl': 'Source gap'}],
      'a': [
      {'h4': 'Step 1 — convert the target into articles'},
      {'tex': '720 \\text{ dozen} \\times 12 = 8{,}640 \\text{ articles per week}'},
      {'h4': '(a)  Number of workers required'},
      {'p': 'Every article passes through **every** operation, so each operation must handle all '
            '8,640 articles. Hours required = articles × minutes per article ÷ 60; workers = '
            'hours required ÷ 40.'},
      {'stmt': {'t': '(a)  Workers required, by operation', 'rows': [
        ['Operation', 'Minutes per article', 'Total minutes', 'Hours required',
         'Workers (÷ 40 hrs)', '@hd'],
        [1, 12, '103,680', '1,728', '43.2  →  **44**'],
        [2, 20, '172,800', '2,880', '72.0  →  **72**'],
        [3, 30, '259,200', '4,320', '108.0  →  **108**'],
        [4, 10, '86,400', '1,440', '36.0  →  **36**'],
        [5, 15, '129,600', '2,160', '54.0  →  **54**'],
        ['**Total**', '**87**', '**751,680**', '**12,528**', '**314**', '@tt'],
      ]}},
      {'note': 'Operation 1 needs 43.2 workers. You cannot employ two-tenths of a person, so '
               '**44** must be engaged — the 44th works only part of the week, or the whole gang '
               'works slightly below capacity. Rounding **up** is the only safe direction: '
               'rounding down to 43 would leave the target unmet, and because the operations are '
               '**in sequence**, a shortfall at operation 1 starves all four downstream '
               'operations.'},
      {'h4': '(b)  Weekly cost of each operation'},
      {'stmt': {'t': '(b)  Weekly cost by operation, on hours actually required', 'rows': [
        ['Operation', 'Hours required', 'Rate per hour', 'Weekly cost', '@hd'],
        [1, '1,728', '50p', '£864.00'],
        [2, '2,880', '55p', '£1,584.00'],
        [3, '4,320', '60p', '£2,592.00'],
        [4, '1,440', '70p', '£1,008.00'],
        [5, '2,160', '80p', '£1,728.00'],
        ['**Total**', '**12,528**', '', '**£7,776.00**', '@tt'],
      ]}},
      {'h4': '(c)  Total labour cost per week'},
      {'p': 'On the hours actually required, **£7,776.00**.'},
      {'note': 'If instead the workers engaged are paid for a full 40-hour week whether or not '
               'the hours are needed, operation 1 costs $44 \\times 40 \\times 50p = £880$ '
               'instead of £864, and the weekly total becomes **£7,792.00** — the extra £16 '
               'being the idle time of the part-used 44th worker at operation 1. Only operation '
               '1 is affected; the other four divide exactly. State which basis you have used.'},
      {'key': 'The point of a sequential-operation question is **line balancing**. Operation 3 '
              'needs 108 workers and operation 4 only 36 — a three-to-one imbalance. The output '
              'of the whole line is set by its slowest stage, so if the staffing is wrong at any '
              'one operation, work piles up in front of it and the stages after it stand idle, '
              'whatever the headcount elsewhere.'}]}},

    {'eg': {'tag': 'Exam type — Q4.3 (20 marks) — ICAG, January 1989',
      't': 'Handcraft Ltd — standard hours, bonus, overtime and total wages for three craftsmen',
      'q': [
      {'p': 'Kofi, Yaw and Kwesi are three craftsmen employed by Handcraft Ltd on the carving of '
            'two models of traditional sculpture known as **"SS 77"** and **"SS 88"**. Each '
            'craftsman completes **8 "SS 77"** and **10 "SS 88"** sculptures per week. Production '
            'is then inspected for defective work.'},
      {'p': 'The remuneration scheme provides for a **40-hour week**, for which Kofi is paid '
            '**¢48 per hour**, Yaw **¢54** and Kwesi **¢60**. Time worked in excess of 40 hours '
            'in any week is paid: the **first 4 hours** at time and a third; **additional '
            'hours** at time and a half. In addition, a **bonus of 25% of time saved** is paid '
            'on work completed during the week, at a bonus hourly rate of **¢50** for all '
            'workers. **No bonus is paid on defective work.**'},
      {'p': 'The time allowance in hours per completed sculpture passing inspection is:'},
      {'stmt': {'t': 'Time allowance (hours per good sculpture)', 'rows': [
        ['', 'Kofi', 'Yaw', 'Kwesi', '@hd'],
        ['"SS 77" model', 5, 4, 3],
        ['"SS 88" model', 3, 5, 2],
      ]}},
      {'p': 'The following facts relate to week No. 34:'},
      {'stmt': {'t': 'Week 34 data', 'rows': [
        ['', 'Kofi', 'Yaw', 'Kwesi', '@hd'],
        ['(a) Hours worked in week 34', 44, 46, 40],
        ['(b) Hours worked in week 33 on uncompleted sculptures brought forward', 8, 7, 5],
        ['(c) Hours worked on uncompleted sculptures carried forward to week 35', 7, 8, 3],
        ['(d) Defective "SS 77" sculptures', 1, 2, '—'],
        ['(d) Defective "SS 88" sculptures', '—', 1, 1],
      ]}},
      {'p': '**Required:** calculate the total wages earned by each craftsman for week 34, '
            'showing separately (i) the standard hours allowed, excluding time for defective '
            'work; (ii) bonus hours and bonus payable; (iii) overtime payable; (iv) basic wage '
            'payable.'}],
      'a': [
      {'h4': '(i)  Standard hours allowed, excluding defective work'},
      {'p': 'Each craftsman completed 8 "SS 77" and 10 "SS 88". Deduct the defectives, then '
            'apply each craftsman\'s **own** time allowance — the allowances differ by person:'},
      {'stmt': {'t': '(i)  Standard hours allowed', 'rows': [
        ['', 'Kofi', 'Yaw', 'Kwesi', '@hd'],
        ['"SS 77" completed', 8, 8, 8],
        ['Less defective', -1, -2, 0],
        ['Good "SS 77"', 7, 6, 8],
        ['× time allowance (hrs)', 5, 4, 3],
        ['Standard hours — "SS 77"', 35, 24, 24],
        '@gap',
        ['"SS 88" completed', 10, 10, 10],
        ['Less defective', 0, -1, -1],
        ['Good "SS 88"', 10, 9, 9],
        ['× time allowance (hrs)', 3, 5, 2],
        ['Standard hours — "SS 88"', 30, 45, 18],
        '@gap',
        ['**Total standard hours allowed**', 65, 69, 42, '@tt'],
      ]}},
      {'h4': '(ii)  Bonus hours and bonus payable'},
      {'p': 'The bonus is paid on **work completed during the week**, so the time taken must be '
            'the time spent on *those* sculptures — hours worked this week, **plus** the hours '
            'brought forward from week 33 on sculptures finished this week, **less** the hours '
            'spent this week on sculptures not yet finished:'},
      {'stmt': {'t': '(ii)  Time saved and bonus', 'rows': [
        ['', 'Kofi', 'Yaw', 'Kwesi', '@hd'],
        ['Hours worked in week 34', 44, 46, 40],
        ['Add: hours brought forward from week 33', 8, 7, 5],
        ['Less: hours carried forward to week 35', -7, -8, -3],
        ['**Time taken on work completed**', 45, 45, 42, '@t'],
        ['Standard hours allowed (from (i))', 65, 69, 42],
        ['**Time saved**', '20 hrs', '24 hrs', 'nil', '@t'],
        '@gap',
        ['**Bonus hours (25% of time saved)**', '5 hrs', '6 hrs', 'nil'],
        ['**Bonus payable at ¢50 per bonus hour**', '¢250', '¢300', '¢—', '@tt'],
      ]}},
      {'note': 'Kwesi saved no time at all — his 42 standard hours exactly equal his 42 hours '
               'taken — so he earns no bonus, even though he produced the most good "SS 77" '
               'sculptures of the three. His time allowances are the tightest (3 and 2 hours '
               'against Kofi\'s 5 and 3), which is the price of being the fastest worker when '
               'allowances are set per person.'},
      {'h4': '(iii)  Overtime payable'},
      {'p': 'Overtime is the excess over the 40-hour week. Only the **premium** is shown here, '
            'since the hours themselves are already paid in the basic wage at (iv):'},
      {'stmt': {'t': '(iii)  Overtime premium', 'rows': [
        ['', 'Kofi', 'Yaw', 'Kwesi', '@hd'],
        ['Hours worked', 44, 46, 40],
        ['Overtime hours (above 40)', 4, 6, 0],
        ['First 4 hrs at time and a third — premium ⅓ × rate × hrs',
         '4 × ⅓ × ¢48 = ¢64', '4 × ⅓ × ¢54 = ¢72', '—'],
        ['Additional hrs at time and a half — premium ½ × rate × hrs',
         '—', '2 × ½ × ¢54 = ¢54', '—'],
        ['**Overtime premium payable**', '¢64', '¢126', '¢—', '@tt'],
      ]}},
      {'h4': '(iv)  Basic wage payable'},
      {'stmt': {'t': '(iv)  Basic wage = hours worked × hourly rate', 'rows': [
        ['', 'Kofi', 'Yaw', 'Kwesi', '@hd'],
        ['Hours worked × rate  (44 × 48;  46 × 54;  40 × 60)', '¢2,112', '¢2,484', '¢2,400'],
      ]}},
      {'h4': 'Total wages earned in week 34'},
      {'stmt': {'t': 'Total wages, week 34', 'rows': [
        ['', 'Kofi (¢)', 'Yaw (¢)', 'Kwesi (¢)', '@hd'],
        ['Basic wage', 2112, 2484, 2400],
        ['Overtime premium', 64, 126, 0],
        ['Bonus', 250, 300, 0],
        ['**Total wages earned**', 2426, 2910, 2400, '@tt'],
      ]}},
      {'key': 'The hinge of this question is the **brought-forward / carried-forward '
              'adjustment**. The bonus rewards time saved on sculptures *finished*, so the hours '
              'compared against the standard allowance must cover exactly those sculptures — '
              'including hours spent on them last week, and excluding hours spent this week on '
              'pieces still on the bench. A candidate who simply compares the standard hours '
              'against the hours worked gets Kofi\'s time saved as 21 instead of 20 and Yaw\'s '
              'as 23 instead of 24, and loses the marks for parts (i) and (ii) together.'}]}},

    {'eg': {'tag': 'Exam type — Q4.4 (20 marks)',
      't': 'End Times Co. Ltd — wages control, work-in-progress and production overhead accounts',
      'q': [
      {'p': 'End Times Co. Ltd manufactures two products, **Miaweni** and **Yirewoho**. Below is '
            'a summary of the payroll data of the production department for March 2006:'},
      {'stmt': {'t': 'Payroll data, March 2006', 'rows': [
        ['', 'Direct workers', 'Indirect workers', '@hd'],
        ['Hours worked — ordinary time', '3,600 hrs', '800 hrs'],
        ['Hours worked — overtime', '650 hrs', '80 hrs'],
        ['Wage rate per hour', '¢15,000', '¢20,000'],
      ]}},
      {'p': 'The company pays overtime at **time and a half**. Overtime is generally worked to '
            'meet **budgeted production targets**. Analysis of the time used by the direct '
            'workers on the two products reveals:'},
      {'stmt': {'t': 'Direct workers\' time analysis', 'rows': [
        ['Miaweni', '', '2,400 hours'],
        ['Yirewoho', '', '1,150 hours'],
        ['Idle time', '', '700 hours'],
        ['**Total**', '', '**4,250 hours**', '@tt'],
      ]}},
      {'p': '**Required:** **(a)** prepare (i) the wages control account, (ii) the '
            'work-in-progress control account, (iii) the production overhead control account '
            '*(12 marks)*; **(b)** explain the term "labour turnover cost" and state four '
            'examples *(3 marks)*; **(c)** outline five causes of labour turnover *(5 marks)*.'}],
      'a': [
      {'h4': 'Step 1 — total wages incurred'},
      {'stmt': {'t': 'Wages incurred, March 2006', 'rows': [
        ['', 'Direct workers (¢)', 'Indirect workers (¢)', 'Total (¢)', '@hd'],
        ['Total hours × basic rate  (4,250 × 15,000;  880 × 20,000)', 63750000, 17600000,
         81350000],
        ['Overtime premium  (650 × ½ × 15,000;  80 × ½ × 20,000)', 4875000, 800000, 5675000],
        ['**Total wages**', 68625000, 18400000, 87025000, '@tt'],
      ]}},
      {'h4': 'Step 2 — splitting the wages between direct and indirect'},
      {'p': 'Overtime is worked **generally, to meet budgeted targets**, not at any customer\'s '
            'request, so the overtime premium is production overhead. Idle time is always '
            'overhead. What is left of the direct workers\' basic pay is direct labour:'},
      {'stmt': {'t': 'Analysis of the ¢87,025,000', 'rows': [
        ['**Direct labour — to work-in-progress**', '', '', '@hd'],
        ['Miaweni: 2,400 hrs × ¢15,000', 36000000, ''],
        ['Yirewoho: 1,150 hrs × ¢15,000', 17250000, 53250000],
        '@gap',
        ['**Indirect labour — to production overhead**', '', '', '@hd'],
        ['Direct workers\' idle time: 700 hrs × ¢15,000', 10500000, ''],
        ['Direct workers\' overtime premium', 4875000, ''],
        ['Indirect workers\' basic wages: 880 hrs × ¢20,000', 17600000, ''],
        ['Indirect workers\' overtime premium', 800000, 33775000],
        ['**Total wages**', '', 87025000, '@tt'],
      ]}},
      {'h4': '(a)(i)  Wages Control Account'},
      {'tacc': {'t': 'Wages Control Account', 'drl': 'Dr  (¢)', 'crl': 'Cr  (¢)',
        'dr': [['Bank / wages payable', 87025000], ['', 87025000, '@tot']],
        'cr': [['Work-in-progress control (direct labour)', 53250000],
               ['Production overhead control (indirect labour)', 33775000],
               ['', 87025000, '@tot']]}},
      {'h4': '(a)(ii)  Work-in-Progress Control Account'},
      {'tacc': {'t': 'Work-in-Progress Control Account', 'drl': 'Dr  (¢)', 'crl': 'Cr  (¢)',
        'dr': [['Wages control — Miaweni', 36000000],
               ['Wages control — Yirewoho', 17250000], ['', 53250000, '@tot']],
        'cr': [['*(materials, overhead absorbed and transfers to finished goods would also '
                'appear here — only the labour entries are required)*', '']]}},
      {'h4': '(a)(iii)  Production Overhead Control Account'},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (¢)', 'crl': 'Cr  (¢)',
        'dr': [['Wages control — idle time of direct workers', 10500000],
               ['Wages control — overtime premium, direct workers', 4875000],
               ['Wages control — indirect workers\' wages', 17600000],
               ['Wages control — overtime premium, indirect workers', 800000],
               ['', 33775000, '@tot']],
        'cr': [['*(absorbed into work-in-progress at the overhead absorption rate; any balance '
                'is the under- or over-absorption)*', '']]}},
      {'h4': '(b)  Labour turnover cost'},
      {'p': '**Labour turnover cost** is the total cost a business incurs as a consequence of '
            'employees leaving and having to be replaced. It falls into two groups: '
            '**preventive costs**, incurred to stop people leaving, and **replacement costs**, '
            'incurred because they left.'},
      {'ol': [
        '**Recruitment and selection costs** — advertising, agency fees, interviewing, testing '
        'and the administrative time of processing applicants.',
        '**Training and induction costs** of the new employee, and the time of the experienced '
        'staff who train them.',
        '**Lost output and lower productivity** while the post is vacant and during the new '
        'employee\'s learning period, plus the overtime or temporary labour used to cover.',
        '**Increased scrap, rework and machine breakdown** caused by inexperienced operators, '
        'and higher accident and inspection costs.',
      ]},
      {'note': 'Two further examples that earn marks: **preventive costs** such as improved '
               'welfare facilities, pension and medical schemes, and higher wage rates paid to '
               'retain staff; and **leaving costs** such as redundancy or terminal payments, '
               'and the administrative cost of processing the departure.'},
      {'h4': '(c)  Causes of labour turnover'},
      {'ol': [
        '**Poor remuneration** — wages, bonuses or conditions below those available elsewhere in '
        'the industry.',
        '**Lack of promotion prospects, training or career development**, so ambitious staff '
        'leave to progress.',
        '**Poor working conditions** — unsafe, uncomfortable or badly equipped workplaces, '
        'unsocial hours or excessive overtime.',
        '**Poor supervision and management**, including unfair treatment, favouritism, bad '
        'industrial relations and lack of recognition.',
        '**Job dissatisfaction** — monotonous or repetitive work, or work that does not use the '
        'employee\'s skills.',
        '**Unavoidable or personal causes** — retirement, illness, death, marriage, pregnancy, '
        'relocation of the employee or of a spouse, further education, or dismissal and '
        'redundancy.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q4.5 (15 marks) — ACCA Costing',
      't': 'How the cost accountant helps control labour cost, and the problems faced',
      'q': [{'p': 'How can the Cost Accountant help to control labour cost in an organisation, '
                  'and what are some of the problems to be faced in labour cost control?'}],
      'a': [
      {'h4': 'How the Cost Accountant helps to control labour cost'},
      {'ol': [
        '**Designing the time-recording system** — clock cards, job cards, time sheets, idle '
        'time cards and route cards — so that every hour paid for can be traced either to a job '
        'or to a reason for not being on a job.',
        '**Analysing wages into direct and indirect**, and into productive and non-productive '
        'time, so that the cost of idle time, overtime premium and labour-related on-costs is '
        'visible instead of buried in a single wages figure.',
        '**Setting standard times and standard rates** for each operation, and reporting the '
        '**labour rate** and **labour efficiency variances** monthly to the managers who can act '
        'on them (Chapter 13).',
        '**Preparing labour budgets** and comparing actual hours and cost against them for each '
        'cost centre.',
        '**Measuring and reporting labour turnover**, its cost, and the departments where it is '
        'concentrated.',
        '**Reporting idle time by cause** — machine breakdown, material shortage, power failure, '
        'waiting for instructions — so the cause rather than the symptom is attacked.',
        '**Evaluating incentive and bonus schemes** — calculating whether a proposed scheme '
        'actually reduces cost per unit once the bonus is paid, and monitoring whether it is '
        'still doing so.',
        '**Assisting in payroll control** — reconciling the payroll to the time records, and '
        'operating controls against ghost workers and other payroll fraud.',
        '**Providing information for make-or-buy, overtime-versus-extra-shift and recruitment '
        'decisions.**',
      ]},
      {'h4': 'Problems faced in labour cost control'},
      {'ol': [
        '**Unreliable source data** — time sheets completed carelessly or dishonestly, hours '
        'booked to the wrong job, and idle time concealed as productive time.',
        '**Resistance from employees and trade unions** to time study, standard setting and '
        'incentive schemes, which may be seen as a speed-up.',
        '**Difficulty of setting fair standard times**, especially for non-repetitive work, and '
        'the lengthy negotiation needed before rates can be agreed.',
        '**Standards going out of date** as methods, equipment or product mix change, so that '
        'variances measure the staleness of the standard rather than performance.',
        '**Labour cost is largely fixed in the short run** — staff cannot be laid off and '
        're-engaged week by week, so "control" over a short period is limited to how the hours '
        'are used, not how many are paid for.',
        '**Conflict between cost and quality** — pressure on labour cost can increase scrap, '
        'rework and accidents, which cost more than the labour saved.',
        '**Allocating indirect and policy-related labour costs** (overtime premium, bonus, '
        'social security, idle time) to products on a basis that is both fair and understood.',
        '**The cost of the control system itself** — detailed time recording and analysis '
        'consume clerical effort, and must be justified by the savings they produce.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q4.6 (20 marks)',
      't': 'Labour cost control versus labour cost reduction',
      'q': [{'p': 'Explain the differences between labour cost control and labour cost '
                  'reduction, and outline five practical ways of achieving labour cost control '
                  'as well as labour cost reduction.'}],
      'a': [
      {'h4': 'The difference'},
      {'table': {'align': 'lll', 'head': ['', 'Labour cost **control**',
        'Labour cost **reduction**'], 'rows': [
        ['**Aim**', 'To keep labour cost **within a predetermined target** — a standard or '
         'budget.', 'To achieve a **permanent, real reduction** in labour cost per unit, below '
         'the existing target.'],
        ['**Reference point**', 'A standard or budget already set; success means not exceeding '
         'it.', 'The existing level of cost itself; success means a new, lower level.'],
        ['**Nature**', '**Preventive and corrective** — monitor, compare, investigate variances, '
         'act.', '**Innovative** — challenge the existing method, not merely police it.'],
        ['**Duration**', 'Continuous and ongoing, period by period.',
         'Once achieved, the saving is **permanent**; the exercise is typically a project.'],
        ['**Effect on the standard**', 'The standard is **maintained**.',
         'The standard itself is **revised downwards**.'],
        ['**Quality and function**', 'Assumes the present method and quality are right.',
         'Must be achieved **without** reducing the quality or utility of the product.'],
      ]}},
      {'h4': 'Five practical ways of achieving labour cost **control**'},
      {'ol': [
        '**Set standard times and standard rates** for every operation, and report labour rate '
        'and efficiency variances against them regularly.',
        '**Prepare labour budgets** for each cost centre and compare actual hours and cost '
        'against them, investigating significant differences.',
        '**Maintain accurate time records** — clock cards for attendance time and job cards for '
        'job time — and reconcile the two, so that all attendance time is accounted for.',
        '**Record and report idle time by cause**, and act on the causes (breakdowns, material '
        'shortages, poor scheduling) rather than merely recording the hours.',
        '**Control overtime by requiring prior authorisation**, and report the overtime premium '
        'separately so its true cost is visible.',
        '**Monitor labour turnover** and the ratio of indirect to direct labour, and investigate '
        'adverse trends.',
      ]},
      {'h4': 'Five practical ways of achieving labour cost **reduction**'},
      {'ol': [
        '**Work study and method study** — redesign the operation itself so that it takes fewer '
        'labour hours, then re-time it and reset the standard.',
        '**Mechanisation and automation** — substitute capital for labour where the investment '
        'is justified by the saving.',
        '**Improved training and better job placement**, so that each employee works faster, '
        'produces less scrap and needs less supervision.',
        '**Redesign the product (value analysis)** so that it needs fewer or simpler operations '
        'to make, without loss of quality or utility.',
        '**Introduce or redesign incentive schemes** that genuinely raise output per hour, so '
        'that fixed overhead and supervision are spread over more units and the labour cost per '
        'unit falls even though the hourly wage rises.',
        '**Improve working conditions, layout and material flow** to cut handling, waiting and '
        'avoidable idle time, and to reduce labour turnover and absenteeism.',
      ]},
      {'key': 'The sentence that distinguishes the two in one line: **cost control stops costs '
              'rising above a standard; cost reduction lowers the standard itself.** A business '
              'that only controls cost can never become cheaper than it already is. Chapter 15 '
              'develops cost reduction in full.'}]}},

    {'eg': {'tag': 'Exam type — Q4.7 (20 marks)',
      't': 'Individual versus group incentive schemes',
      'q': [{'p': 'What is the difference between an individual incentive scheme and a group '
                  'incentive scheme? Outline **three** advantages and **three** disadvantages '
                  'for each of the two types of incentive scheme.'}],
      'a': [
      {'h4': 'The difference'},
      {'p': 'An **individual incentive scheme** rewards each employee according to **their own** '
            'output or time saved — the Halsey, Halsey-Weir and Rowan premium bonus schemes, and '
            'straight and differential piece rates, are all of this kind. A **group incentive '
            'scheme** rewards a **team** according to the team\'s collective output or saving, '
            'the bonus then being shared among the members on an agreed formula. Group schemes '
            'are used where output cannot sensibly be attributed to one person — on an assembly '
            'line, in a process plant, or where a gang works together, as in Q4.1 above.'},
      {'h4': 'Individual incentive schemes'},
      {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
        ['**Direct link between effort and reward** — each employee sees that their own extra '
         'effort produces their own extra pay, which is the strongest motivator available.',
         '**Quality may be sacrificed for speed**, so more must be spent on inspection and '
         'rectification.'],
        ['**The efficient are distinguished from the inefficient**, so the scheme is seen as '
         'fair and the better workers are retained.',
         '**Unhealthy rivalry and poor co-operation** between employees; workers may hoard '
         'materials, tools or easy jobs.'],
        ['**Less supervision is needed**, since employees are self-motivated; and fixed overhead '
         'per unit falls as output rises.',
         '**Costly and slow to administer** — standard times must be set for every operation, '
         'negotiated with the union, and kept up to date, and individual output must be measured '
         'and recorded.'],
      ]}},
      {'h4': 'Group incentive schemes'},
      {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
        ['**Enhances team spirit and organisational cohesiveness**, and encourages members to '
         'help each other.',
         '**Lazy members are rewarded equally with hard-working ones**, which the hard workers '
         'resent.'],
        ['**Quality of output is not unduly compromised**, because the group polices its own '
         'members and no individual gains by rushing.',
         '**Weaker link between individual effort and reward**, so the incentive to work harder '
         'is diluted — the larger the group, the weaker the link.'],
        ['**Relatively easy and less expensive to administer** than individual schemes, and it '
         'avoids unhealthy competitive rivalry.',
         '**Disputes over the sharing formula**, and the scheme is unusable where a group\'s '
         'output genuinely cannot be measured.'],
      ]}}]}},

    {'eg': {'tag': 'Exam type — Q4.8 (20 marks)',
      't': 'Labour cost accounting versus payroll accounting; turnover costs; reducing turnover',
      'q': [
      {'p': '**(a)** Explain the differences between labour cost accounting and payroll '
            'accounting *(6 marks)*.'},
      {'p': '**(b)** List examples of labour turnover cost *(7 marks)*.'},
      {'p': '**(c)** Explain **seven** ways of avoiding or reducing labour turnover '
            '*(7 marks)*.'}],
      'a': [
      {'h4': '(a)  Labour cost accounting versus payroll accounting'},
      {'table': {'align': 'lll', 'head': ['', 'Payroll accounting', 'Labour cost accounting'],
        'rows': [
        ['**Question it answers**', '**How much is each employee to be paid, and what must be '
         'deducted?**', '**What did labour cost each job, product, process and cost centre?**'],
        ['**Starting point**', 'Attendance time — the clock card.',
         'Job time — the job card, time sheet or route card.'],
        ['**Output**', 'The payroll: gross pay, statutory and voluntary deductions, net pay, and '
         'the payslip for each employee.',
         'The analysis of wages into direct labour charged to jobs, and indirect labour charged '
         'to production overhead.'],
        ['**Purpose**', 'To **pay people correctly and lawfully**, and to account to the '
         'authorities for tax and social security withheld.',
         'To **cost products and control performance** — pricing, variance analysis, '
         'decision-making.'],
        ['**Users**', 'Employees, the revenue authority, the social security authority.',
         'Management, internally.'],
        ['**Link between them**', 'The payroll establishes the **total** wages bill.',
         'Labour cost accounting takes that total and **analyses where it went** — and the two '
         'must reconcile exactly.'],
      ]}},
      {'note': 'The relationship in one line: **payroll accounting decides what is paid; labour '
               'cost accounting decides what it is charged to.** Every naira on the payroll must '
               'appear somewhere in the cost accounts — as direct labour in work-in-progress, or '
               'as indirect labour in production overhead.'},
      {'h4': '(b)  Examples of labour turnover cost'},
      {'p': '**Preventive costs** — incurred to stop employees leaving:'},
      {'ul': [
        'personnel and welfare department costs;',
        'medical services, canteen, sports and recreation facilities;',
        'pension, gratuity and other retirement benefit schemes;',
        'higher wage rates and fringe benefits paid to retain staff;',
        'training and career development provided to improve prospects.',
      ]},
      {'p': '**Replacement costs** — incurred because employees did leave:'},
      {'ul': [
        'advertising, recruitment agency fees, interviewing and selection costs;',
        'induction and training of the replacement, and the trainer\'s time;',
        'lost output while the post is vacant and during the learning period;',
        'lower productivity, higher scrap, defectives and rework by inexperienced staff;',
        'increased machine breakdowns, tool damage and accidents;',
        'overtime, temporary staff or sub-contracting used to cover the gap;',
        'extra supervision and inspection of new employees;',
        'terminal payments, redundancy pay and the administrative cost of leaving.',
      ]},
      {'h4': '(c)  Seven ways of avoiding or reducing labour turnover'},
      {'ol': [
        '**Pay competitive wages and fringe benefits**, reviewed against the rates available in '
        'the same industry and locality.',
        '**Improve working conditions** — a safe, healthy, well-lit and well-equipped workplace, '
        'with reasonable hours and no excessive compulsory overtime.',
        '**Provide training and clear promotion prospects**, so that ambitious employees can '
        'advance inside the organisation rather than outside it.',
        '**Select and place employees properly**, matching the person to the job at recruitment '
        'so that neither boredom nor inability causes them to leave.',
        '**Improve supervision and industrial relations** — fair treatment, effective grievance '
        'procedures, recognition of good work, and genuine consultation with employee '
        'representatives.',
        '**Introduce job rotation, job enlargement and job enrichment** to relieve the monotony '
        'of repetitive work.',
        '**Provide security and welfare** — pension and gratuity schemes, medical cover, housing '
        'or transport assistance, and reasonable job security.',
        '**Conduct exit interviews** and act on what they reveal, so that the real causes of '
        'leaving are addressed rather than guessed at.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q4.9',
      't': 'PUCT — remuneration under the time rate, payment by result and a bonus scheme',
      'q': [
      {'p': '**(a)** Write formulae for remuneration payable using (i) the time rate system and '
            '(ii) payment by result.'},
      {'p': '**(b)** PUCT provides the extracted details of its employees\' labour records:'},
      {'stmt': {'t': 'PUCT — employee records', 'rows': [
        ['', 'Sanity', 'Moses', '@hd'],
        ['Units produced', 90, 80],
        ['Standard time allowed (minutes per unit produced)', 30, 30],
        ['Actual time worked (hours)', 35, 40],
        ['Rate per hour', 'N200', 'N250'],
        ['Rate per unit', 'N66.70', 'N68.00'],
      ]}},
      {'p': '**Required:** **1.** Determine the remuneration payable using (i) the time rate '
            'system, (ii) payment by result, and (iii) a bonus scheme in which the bonus is the '
            'product of time saved and the hourly rate. **2.** Which of the two employees is '
            'efficient?'}],
      'a': [
      {'h4': '(a)  The formulae'},
      {'fbox': {'h': 'Remuneration formulae', 'rows': [
        {'lb': '(i)  Time rate system',
         'tex': '\\text{Earnings} = \\text{Hours worked} \\times \\text{Rate per hour}',
         'nt': 'Pay depends on time spent at work, not on output. Where overtime is worked, the '
               'premium is added.'},
        {'lb': '(ii)  Payment by result (piece rate)',
         'tex': '\\text{Earnings} = \\text{Units produced} \\times '
                '\\text{Rate per unit}',
         'nt': 'Pay depends on output, not on time taken.'},
        {'lb': 'Bonus scheme (as specified in this question)',
         'tex': '\\text{Earnings} = (\\text{Hours worked} \\times \\text{Rate per hour}) '
                '+ (\\text{Time saved} \\times \\text{Rate per hour})',
         'nt': 'Time saved = time allowed − time taken. Note this scheme gives the employee '
               '**all** of the time saved; the Halsey scheme gives half and the Halsey-Weir a '
               'third.'},
      ]}},
      {'h4': 'Working — time allowed and time saved'},
      {'stmt': {'t': 'Time allowed and time saved', 'rows': [
        ['', 'Sanity', 'Moses', '@hd'],
        ['Units produced', 90, 80],
        ['Standard time per unit', '30 min', '30 min'],
        ['Time allowed  (90 × 30 ÷ 60;  80 × 30 ÷ 60)', '45 hrs', '40 hrs'],
        ['Time taken (actual hours worked)', '35 hrs', '40 hrs'],
        ['**Time saved**', '**10 hrs**', '**nil**', '@tt'],
      ]}},
      {'h4': '1.  Remuneration under each system'},
      {'stmt': {'t': 'Remuneration payable', 'rows': [
        ['', 'Sanity (N)', 'Moses (N)', '@hd'],
        ['**(i) Time rate**  (35 × 200;  40 × 250)', 7000, 10000],
        '@gap',
        ['**(ii) Payment by result**  (90 × 66.70;  80 × 68.00)', 6003, 5440],
        '@gap',
        ['**(iii) Bonus scheme** — basic pay (hours worked × hourly rate)', 7000, 10000],
        ['            add bonus (time saved × hourly rate: 10 × 200;  0 × 250)', 2000, 0],
        ['            **total under the bonus scheme**', 9000, 10000, '@t'],
      ]}},
      {'h4': '2.  Which employee is efficient?'},
      {'p': 'Efficiency compares the work **done** with the time **taken** to do it:'},
      {'tex': '\\text{Efficiency ratio} = \\frac{\\text{Standard hours allowed for the '
              'work done}}{\\text{Actual hours taken}} \\times 100'},
      {'stmt': {'t': 'Efficiency ratios', 'rows': [
        ['', 'Sanity', 'Moses', '@hd'],
        ['Standard hours allowed', '45 hrs', '40 hrs'],
        ['Actual hours taken', '35 hrs', '40 hrs'],
        ['**Efficiency ratio**', '**128.6%**', '**100.0%**', '@tt'],
      ]}},
      {'p': '**Sanity is the efficient employee.** She produced 45 standard hours of work in 35 '
            'actual hours, beating the standard by 28.6%, whereas Moses produced exactly the '
            'standard output for the time he took and so is merely working to standard, not '
            'above it.'},
      {'key': 'Note how differently the three systems treat the same two people. Under the '
              '**time rate** Moses earns more (N10,000 against N7,000), purely because his '
              'hourly rate is higher and he sat at work longer — the system rewards attendance, '
              'not performance, and so pays the *less* efficient worker *more*. Under **payment '
              'by result** Sanity earns more (N6,003 against N5,440), because she produced more '
              'units. Under the **bonus scheme** Sanity gains N2,000 for her 10 saved hours '
              'while Moses gains nothing. This contrast is the entire argument for incentive '
              'schemes in one table.'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Gross wage (time rate)', 'tex': 'W = h \\times r',
   'nt': 'h = hours worked, r = rate per hour.'},
  {'lb': 'Straight piece rate', 'tex': 'W = u \\times r', 'nt': 'u = units produced, r = rate '
   'per unit.'},
  {'lb': 'Overtime premium', 'tex': '\\text{Premium} = \\text{Basic rate} \\times '
   '\\text{(overtime fraction)}'},
  {'lb': 'Halsey bonus', 'tex': 'B = \\tfrac12 (T_a - T_t) \\times D',
   'nt': 'Ta = time allowed, Tt = time taken, D = day rate.'},
  {'lb': 'Halsey-Weir bonus', 'tex': 'B = \\tfrac13 (T_a - T_t) \\times D'},
  {'lb': 'Rowan bonus', 'tex': 'B = \\dfrac{T_a - T_t}{T_a} \\times T_t \\times D'},
  {'lb': 'Labour turnover rate', 'tex': '\\dfrac{\\text{Leavers}}{\\text{Average employees}} '
   '\\times 100'},
  {'lb': 'Flux method', 'tex': '\\dfrac{\\text{Joiners} + \\text{Leavers}}{\\text{Average '
   'employees}}'},
  {'lb': 'Separation method', 'tex': '\\dfrac{\\text{Workers replaced}}{\\text{Average '
   'employees}}'},
 ],
 'focus':
   'This chapter is tested almost as heavily as materials, and the same discipline applies: '
   'learn the four bonus-scheme formulas (time rate, piece rate, Halsey/Halsey-Weir, Rowan) as a '
   'family, and always establish time allowed, time taken and time saved explicitly before '
   'plugging into any of them. The direct/indirect split for labour (only *basic* wages of a '
   'direct worker are direct cost — every policy add-on is indirect, even on a direct worker) is '
   'a frequent trap. Labour turnover\'s three formulas share one denominator (average employees) '
   'but different numerators — know which measures leavers only, which counts joiners too.',
 'errors': [
   'Applying the Rowan formula\'s time-saved/time-allowed fraction to *time allowed* instead of '
   '*time taken* in the multiplication.',
   'Treating overtime premium as always indirect — it is direct when worked specifically at a '
   'customer\'s request.',
   'Classifying a bonus or insurance premium paid to a direct worker as direct labour cost — '
   'only the basic wage is direct; everything else is indirect regardless of who earns it.',
   'Confusing job evaluation (ranks the job) with merit rating (ranks the jobholder\'s '
   'performance).',
   'Using the number of leavers alone, without dividing by average employees, when quoting a '
   'labour turnover "rate."',
 ],
 'quiz': {
  'mcq': [
   {'q': 'An employee works 48 hours in a week at a basic rate of ¢1,500 per hour. The gross '
         'wage under the time rate method is',
    'o': ['¢48,000', '¢72,000', '¢1,500', '¢69,500', '¢75,000'],
    'a': 1,
    'w': 'Gross wage = hours worked × rate per hour = 48 × 1,500 = ¢72,000.',
    'calc': 'W = 48 \\times 1{,}500 = 72{,}000',
    'src': 'Chapter 4.3', 'sec': '4.3'},
   {'q': 'Under a straight piece rate scheme, an employee\'s earnings depend on',
    'o': ['the number of hours spent at work', 'the volume of units produced',
          'the employee\'s seniority', 'the company\'s annual profit', 'the day of the week'],
    'a': 1,
    'w': 'Straight piece rate pays units produced × rate per unit — time taken is irrelevant to '
         'the wage itself.',
    'src': 'Chapter 4.3', 'sec': '4.3'},
   {'q': 'Time allowed for a job is 20 hours; time taken is 16 hours; the day rate is ¢5,000/'
         'hour. Under the Halsey scheme, the bonus is',
    'o': ['¢10,000', '¢20,000', '¢6,667', '¢4,000', '¢16,000'],
    'a': 0,
    'w': 'Time saved = 20 − 16 = 4 hours. Halsey bonus = ½ × 4 × 5,000 = ¢10,000.',
    'calc': 'B = \\tfrac12 \\times (20-16) \\times 5{,}000 = 10{,}000',
    'src': 'Chapter 4.3', 'sec': '4.3'},
   {'q': 'Using the same data (time allowed 20 hrs, time taken 16 hrs, day rate ¢5,000/hr), the '
         'bonus under the Rowan scheme is',
    'o': ['¢10,000', '¢8,000', '¢16,000', '¢4,000', '¢20,000'],
    'a': 1,
    'w': 'Rowan bonus = (time saved / time allowed) × time taken × day rate = (4/20) × 16 × '
         '5,000 = 0.2 × 16 × 5,000 = ¢16,000.',
    'calc': 'B = \\dfrac{4}{20} \\times 16 \\times 5{,}000 = 16{,}000',
    'src': 'Chapter 4.3', 'sec': '4.3'},
   {'q': 'Overtime premium paid to a direct worker is normally treated as',
    'o': ['direct labour cost, always', 'indirect labour cost, unless worked at a customer\'s '
          'specific request', 'a period cost only', 'part of prime cost, always',
          'excluded from labour cost entirely'],
    'a': 1,
    'w': 'Overtime premium is indirect wages, except where the overtime is worked specifically '
         'at a customer\'s request to meet their deadline — then it is direct.',
    'src': 'Chapter 4.5', 'sec': '4.5'},
   {'q': 'A workstation available for production but unused because materials have not arrived '
         'is an example of',
    'o': ['abnormal idle time', 'normal idle time', 'overtime', 'direct labour cost',
          'a stepped cost'],
    'a': 1,
    'w': 'A material shortage is exactly the CIMA definition of idle time; whether it is normal '
         '(uncontrollable, expected) depends on context, but a routine material-delivery gap of '
         'this kind is the textbook example of normal idle time, charged to WIP.',
    'src': 'Chapter 4.4', 'sec': '4.4'},
   {'q': 'A company had 300 employees at the start of the month and 280 at the end, after 10 '
         'joined and 30 left. The labour turnover rate (leavers/average employees × 100) is',
    'o': ['10%', '9.3%', '10.3%', '3.3%', '30%'],
    'a': 1,
    'w': 'Average employees = ½(300+280) = 290. Turnover rate = 30/290 × 100 ≈ 10.3%.',
    'calc': '\\dfrac{30}{\\tfrac12(300+280)} \\times 100 \\approx 10.3\\%',
    'src': 'Chapter 4.6', 'sec': '4.6'},
   {'q': 'Which of the following is an example of a "ghost worker" fraud?',
    'o': ['A real employee is overpaid due to a clerical error',
          'Wages are paid to an employee who has genuinely resigned',
          'Wages are paid in the name of a person who does not actually exist',
          'An employee is paid late due to a bank error',
          'An employee\'s bonus is calculated using the wrong day rate'],
    'a': 2,
    'w': 'A ghost worker is a fictitious employee whose "wages" are actually being '
         'misappropriated by whoever set up the fraud.',
    'src': 'Chapter 4.6', 'sec': '4.6'},
   {'q': 'In preparing a payroll, National Health Insurance and Social Security contributions '
         'are examples of',
    'o': ['voluntary deductions', 'statutory deductions', 'gross wages', 'overtime premiums',
          'group incentive bonuses'],
    'a': 1,
    'w': 'Statutory deductions are required by law (Social Security, PAYE, National Health '
         'Insurance); trade-union and provident-fund contributions are voluntary deductions.',
    'src': 'Chapter 4.7', 'sec': '4.7'},
   {'q': 'Which technique measures the *jobholder\'s* performance, to decide on promotion, '
         'demotion or reward, rather than ranking the job itself?',
    'o': ['Job evaluation', 'Merit rating', 'Work measurement', 'Method study',
          'Labour turnover analysis'],
    'a': 1,
    'w': 'Merit rating assesses the person doing the job (accuracy, initiative, '
         'responsiveness); job evaluation ranks the job itself against other jobs.',
    'src': 'Chapter 4.2', 'sec': '4.2'},
  ],
  'theory': [
   {'q': 'Distinguish between labour cost accounting and payroll accounting.',
    'marks': 6,
    'a': [
      {'p': '**Labour cost accounting** relates to determining the cost of labour chargeable to '
            'jobs, products, customers and overhead accounts — its scope includes wages/'
            'salaries, workmen\'s compensation insurance, employee bonuses and employee share '
            'schemes.'},
      {'p': '**Payroll accounting** relates to computing what is owed to, or paid on behalf of, '
            'employees — the employer\'s and employee\'s social security contributions, personal '
            'income tax and welfare deductions. It does not consider costs like workmen\'s '
            'compensation insurance, which labour cost accounting does — the two have '
            'genuinely different scopes, not just different names for the same thing.'},
    ], 'src': 'Chapter 4.7', 'sec': '4.7'},
   {'q': 'Outline FIVE causes of labour turnover.',
    'marks': 5,
    'a': [
      {'ol': [
        'dissatisfaction with the job or wages;',
        'poor hours of work or working conditions;',
        'discontent with supervisors or colleagues;',
        'lack of promotion opportunities;',
        'personal matters such as ill health, marriage, pregnancy or relocation.',
      ]},
    ], 'src': 'Chapter 4.6', 'sec': '4.6'},
   {'q': 'Explain SEVEN ways of avoiding or reducing labour turnover.',
    'marks': 7,
    'a': [
      {'ol': [
        'analyse turnover regularly by cause, distinguishing avoidable from unavoidable and '
        'voluntary from dismissed;',
        'improve applicant selection, to avoid hiring discontented or unsuitable staff;',
        'plan labour requirements properly, to avoid redundancy;',
        'introduce a high-wage plan or other incentives;',
        'keep the working environment congenial;',
        'offer competitive fringe benefits — pension scheme, subsidised meals, sports/social '
        'facilities;',
        'develop better relationships between management and workers.',
      ]},
    ], 'src': 'Chapter 4.6', 'sec': '4.6'},
  ]},
}
