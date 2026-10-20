CH = {
 'n': 13,
 't': 'Standard Costing Techniques',
 'brief': 'Standard costing as a control mechanism: the four types of standards, the process of '
          'setting them for materials/labour/overheads/selling price, the standard cost card, '
          'and the full variance-analysis toolkit — material, labour, overhead, and sales '
          'margin variances — culminating in a full reconciliation of budgeted profit to actual '
          'profit, and the activity/capacity/efficiency ratios. Every illustration '
          'independently verified against its own raw data.',
 'outcomes': [
   'Explain the concept of standards',
   'Explain types of standards',
   'Explain the uses of standard cost, its merits and limitations',
   'Explain methods of determining standard cost',
   'Compute a standard cost card',
   'Compute basic variances, including sales, materials, labour and overheads',
   'Compute standard ratios, including activity, capacity and efficiency',
   'Analyse the causes of variances',
 ],
 'secs': [
  {'n': '13.1', 't': 'Standards and standard costing', 'b': [
    {'p': 'Setting standards — as a planning basis and a performance yardstick — makes '
          'budgeting easier and lets the control process compare standard against actual to '
          'find variances, investigate them, and take corrective action.'},
    {'def': {'t': 'Standards (as a concept)', 'd': 'control mechanisms establishing '
                  'predetermined estimates of the cost of products/services, compared against '
                  'actual costs as incurred to find variances, which are then analysed into '
                  'their components and investigated.'}},

    {'h4': 'Four types of standards'},
    {'table': {'align': 'lll', 'head': ['Type', 'Meaning', 'Used for'], 'rows': [
      ['**Basic**', 'Long-term, unchanged over several years — a base from which current '
       'standards can be developed.', 'Showing long-term trends (material prices, labour '
       'rates, efficiency, the long-term effect of changed methods); as a basis for setting '
       'current standards. **Cannot** highlight current efficiency/inefficiency, and does not '
       'normally feature in reporting except as statistical background.'],
      ['**Ideal**', 'Attainable only under the **most favourable** conditions — no breakdowns, '
       'no wastage, no stoppages, no idle time, no spoilage, no shrinkage.', 'Long-term targets; '
       'long-term development purposes; investigative purposes.'],
      ['**Attainable**', 'Achievable if a standard unit of work is done efficiently, a machine '
       'properly run, material properly used — allows for normal losses/breakdowns. Represents '
       'reasonably-met future performance.', 'Routine control (tough-but-realistic targets, or '
       'motivation); stock valuation (product costing, cost control). Should be revised '
       'periodically for new conditions/prices/methods/technology.'],
      ['**Current**', 'Set for a **short** period, reflecting current conditions — same as '
       'attainable when conditions are stable, but set specifically to handle a temporary '
       'problem otherwise.', 'A temporary material-quality problem; an unexpected inflationary '
       'price rise; an energy crisis; standards with subjective elements.'],
    ]}},
    {'key': 'Two important points: the **type** of standard used directly affects the size and '
            'meaning of any variance computed against it — and every standard, whichever type, '
            'contains some **subjective** element.'},

    {'h4': 'Standard cost — definition, uses, merits, limitations'},
    {'def': {'t': 'Standard cost', 'd': 'a predetermined calculation of how much cost *should* '
                  'be, under specified working conditions — expressed in monetary terms and '
                  'built up from the value of each cost element. Used for control by exception '
                  'reporting, stock valuation, and fixing selling prices.'}},
    {'warn': 'Standard cost is **not** an average of past costs — past cost can embed past '
             'mistakes/inefficiencies, and comparing standard against past cost is usually '
             'inappropriate given likely changes in method, technology and prices.'},
    {'p': 'Uses of standard costing: assessing performance/efficiency; cost control (setting '
          'standards, analysing variances, finding reasons for them); management by exception; '
          'easing budget preparation; stock/WIP valuation, profit planning and decision making, '
          'and pricing policy (especially cost-plus pricing); and motivating staff.'},
    {'table': {'align': 'll', 'head': ['Merits', 'Limitations'], 'rows': [
      ['Assesses performance/efficiency; enhances cost control by prompting re-appraisal of '
       'methods/materials/technique; eases budgeting; enables management by exception; guides '
       'performance improvement; aids estimation/forecasting; motivates (with real '
       'participation); simplifies stock valuation and pricing; assigns responsibility for '
       'off-standard performance.',
       'Its whole philosophy is sometimes challenged as inappropriate; only really works '
       'within a budgetary-system framework; variance analysis only *points at* a problem, it '
       'does not solve it (that\'s a management task); every standard involves subjective '
       'forecasting; the process can be too complex for most line managers; variance analysis '
       'is essentially a post-mortem on past events; can be expensive/time-consuming to '
       'install; standards can go out of date fast in volatile conditions; and the usefulness '
       'of some variances is genuinely questionable.'],
    ]}},
  ]},

  {'n': '13.2', 't': 'The process of standard costing, and setting standards', 'b': [
    {'p': 'Five steps: (a) set the standard cost, built up from each cost element; (b) measure '
          'actual cost, per element and in total; (c) compare standard vs actual — the '
          'difference is a **variance**, either **favourable** (better than planned) or '
          '**adverse/unfavourable** (worse than planned); (d) analyse the variance into its '
          'smallest components; (e) investigate the real causes, for material/significant '
          'variances only.'},
    {'key': 'Standard costing gives the most value where production is highly **repetitive** — '
            'mass production or repetitive assembly work.'},

    {'h4': 'Setting each element\'s standard'},
    {'table': {'align': 'll', 'head': ['Element', 'How the standard is set'], 'rows': [
      ['**Materials**', 'Materials content per product is found via engineering study (raw '
       'materials, sub-assemblies, piece parts, finishing materials); quantities allow for '
       'normal loss (machining loss, evaporation, expected breakage/rejection); prices come '
       'from purchasing/procurement, using **forecast/expected** prices (not past costs), '
       'reflecting price trends, purchasing-policy changes, quantity/cash discounts, and '
       'carriage/packing.'],
      ['**Labour**', 'Specify the exact labour grade (via work-study/measurement techniques); '
       'determine the **standard hour** — the quantity of work achievable at standard '
       'performance in one hour/minute; personnel forecasts the relevant wage rate for the '
       'control period; standard labour cost = standard hours × standard wage rate.'],
      ['**Overheads**', 'The predetermined overhead absorption rate itself becomes the standard '
       'rate, using budgeted standard labour hours as the activity base.'],
      ['**Selling price**', 'A top-management decision, weighing anticipated market demand, '
       'competing products, inflation estimates, and elasticity of demand.'],
    ]}},
    {'fbox': {'h': 'Overhead absorption rates as standards', 'rows': [
      {'lb': 'Variable Overhead Rate (VOR)', 'tex': 'VOR = \\dfrac{\\text{Budgeted variable '
        'overhead}}{\\text{Budgeted standard labour hours}}'},
      {'lb': 'Fixed Overhead Rate (FOAR)', 'tex': 'FOAR = \\dfrac{\\text{Budgeted fixed '
        'overhead}}{\\text{Budgeted standard labour hours}}'},
    ]}},
    {'def': {'t': 'Standard sales margin', 'd': 'the difference between standard selling price '
                  'and standard cost — or, under standard **marginal** costing, standard '
                  'selling price less standard **marginal** cost, giving the standard '
                  'contribution margin instead.'}},
  ]},

  {'n': '13.3', 't': 'The standard cost card', 'b': [
    {'p': 'Once every standard is set, they are summarised in one place:'},
    {'table': {'align': 'lr', 'head': ['Standard cost card', 'N'], 'rows': [
      ['Standard direct materials cost per unit', 'xx'],
      ['Standard direct labour cost per unit', 'xx'],
      ['Standard direct expenses per unit', 'xx'],
      ['Standard overhead cost per unit', 'xx'],
      ['**Standard cost per unit**', 'xx'],
      ['Standard profit margin', 'xx'],
      ['**Standard selling price**', 'xx'],
    ]}},
    {'key': 'The standard cost card is the single reference point everything else in this '
            'chapter is built from — budgets, and every variance, trace straight back to it.'},
  ]},

  {'n': '13.4', 't': 'Material, labour and overhead cost variances', 'b': [
    {'def': {'t': 'Variance', 'd': 'the difference between the standard level of performance '
                  'that ought to have been achieved, and the actual level achieved.'}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 13.1 — the shared dataset for material, '
      'labour and overhead variances', 'open': True, 'q': [
      {'p': 'Ghartex Ltd, budgeted production 120,000 metres of Kente: Material A 0.5kg/metre '
            '@¢1,200/kg; Material B 0.5kg/metre @¢1,600/kg; direct labour 30 minutes/metre '
            '@¢6,000/hour; budgeted variable overhead ¢30 million; budgeted fixed overhead '
            '¢15 million. Overhead is absorbed on direct labour hours. Actual: production '
            '130,000 metres; Material A 80,000kg purchased/used costing ¢88 million; Material B '
            '70,000kg costing ¢98 million; 80,000 direct labour hours costing ¢400 million; '
            'variable overhead ¢28 million; fixed overhead ¢18 million.'}],
      'a': [{'p': 'Standard quantities/hours for the **actual** 130,000-metre output: Material '
                  'A and B each $130{,}000 \\times 0.5 = 65{,}000$kg; labour $130{,}000 \\times '
                  '0.5 = 65{,}000$ hours. Worked through the sub-sections below.'}]}},

    {'h4': 'Material cost variance (MCV)'},
    {'fbox': {'h': 'Material variance formulas', 'rows': [
      {'lb': 'Material Cost Variance', 'tex': '(\\text{SQ for actual output} \\times SP) - '
        '(\\text{AQ used} \\times AP)'},
      {'lb': 'Material Price Variance', 'tex': 'AQ_{\\text{purchased}} \\times (SP - AP)'},
      {'lb': 'Material Usage Variance', 'tex': 'SP \\times (\\text{SQ for actual output} - AQ)'},
    ]}},
    {'p': 'Possible causes of a **price** variance: paying more/less than planned (purchasing '
          'efficiency/inefficiency, market changes, emergency purchases from poor stock '
          'control, different discounts, quality differences, or substitute materials).'},
    {'p': 'Possible causes of a **usage** variance: careful or careless material handling, '
          'quality differences, pilferage, actual vs normal scrap, changed quality-control '
          'measures, or gains/losses from substitute materials.'},
    {'table': {'align': 'lrrr', 'head': ['', 'Material A', 'Material B', 'Total'], 'rows': [
      ['Cost variance: (65,000×1,200)−88,000,000; (65,000×1,600)−98,000,000', '10,000,000 A',
       '6,000,000 F', '**4,000,000 A**'],
      ['Price variance: (80,000×1,200)−88,000,000; (70,000×1,600)−98,000,000', '8,000,000 F',
       '14,000,000 F', '**22,000,000 F**'],
      ['Usage variance: 1,200×(65,000−80,000); 1,600×(65,000−70,000)', '18,000,000 A',
       '8,000,000 A', '**26,000,000 A**'],
    ]}},
    {'key': 'Check: Price variance + Usage variance = Cost variance, for every material and in '
            'total — 22,000,000 F − 26,000,000 A = 4,000,000 A, exactly matching. This identity '
            'always holds and is the fastest way to catch an arithmetic slip.'},

    {'h4': 'Labour cost variance'},
    {'fbox': {'h': 'Labour variance formulas', 'rows': [
      {'lb': 'Labour Total Cost Variance', 'tex': '(SH \\times SR) - (AH \\times AR)'},
      {'lb': 'Labour Rate Variance', 'tex': 'AH \\times (SR - AR)'},
      {'lb': 'Labour Efficiency Variance', 'tex': 'SR \\times (SH - AH)'},
    ]}},
    {'p': 'Rate-variance causes: a higher/lower rate than planned (wage awards, wrong labour '
          'grade used, unplanned overtime/bonus). Efficiency-variance causes: wrong labour '
          'grade, poor workshop organisation/supervision, wrong materials/machines. A separate '
          '**idle time variance** = idle hours × standard rate, from causes like machine '
          'breakdown, power outages, work stoppages, or poor staff coordination.'},
    {'table': {'align': 'lr', 'head': ['', ''], 'rows': [
      ['Total cost variance: (65,000×6,000)−400,000,000', '10,000,000 A'],
      ['Rate variance: 80,000×(6,000−5,000) — actual rate = 400,000,000÷80,000 = ¢5,000/hr',
       '80,000,000 F'],
      ['Efficiency variance: 6,000×(65,000−80,000)', '90,000,000 A'],
    ]}},
    {'key': 'Check: 80,000,000 F − 90,000,000 A = 10,000,000 A = total, confirmed.'},

    {'h4': 'Total Overhead Cost Variance (TOCV)'},
    {'p': 'Standard Total Overhead Rate (STOR) $= \\dfrac{30{,}000{,}000+15{,}000{,}000}'
          '{60{,}000\\text{ budgeted hrs}} = ¢750$/hr.'},
    {'tex': 'TOCV = (65{,}000 \\times 750) - (28{,}000{,}000 + 18{,}000{,}000) = '
            '48{,}750{,}000 - 46{,}000{,}000 = ¢2{,}750{,}000\\text{ F}'},

    {'h4': 'Variable Overhead Cost Variance (VOCV)'},
    {'p': 'Variable Overhead Rate (VOR) $= 30{,}000{,}000 / 60{,}000 = ¢500$/hr.'},
    {'fbox': {'h': 'Variable overhead sub-variances', 'rows': [
      {'lb': 'Variable Overhead Cost Variance', 'tex': '(SH \\times VOR) - \\text{Actual VOH}'},
      {'lb': 'Expenditure Variance', 'tex': '(AH \\times VOR) - \\text{Actual VOH}'},
      {'lb': 'Efficiency Variance', 'tex': '(SH - AH) \\times VOR'},
    ]}},
    {'table': {'align': 'lr', 'head': ['', ''], 'rows': [
      ['VOCV: (65,000×500)−28,000,000', '4,500,000 F'],
      ['Expenditure: (80,000×500)−28,000,000', '12,000,000 F'],
      ['Efficiency: (65,000−80,000)×500', '7,500,000 A'],
    ]}},
    {'key': 'Check: 12,000,000 F − 7,500,000 A = 4,500,000 F, confirmed.'},

    {'h4': 'Fixed Overhead Variance'},
    {'p': 'FOAR $= 15{,}000{,}000 / 60{,}000 = ¢250$/hr.'},
    {'fbox': {'h': 'Fixed overhead sub-variances', 'rows': [
      {'lb': 'Fixed Overhead Total Variance', 'tex': '(SH \\times FOAR) - \\text{Actual FOH}'},
      {'lb': 'Expenditure Variance', 'tex': '\\text{Budgeted FOH} - \\text{Actual FOH}'},
      {'lb': 'Volume Variance', 'tex': '(SH - \\text{Budgeted hours}) \\times FOAR'},
    ]}},
    {'table': {'align': 'lr', 'head': ['', ''], 'rows': [
      ['Total: (65,000×250)−18,000,000', '1,750,000 A'],
      ['Expenditure: 15,000,000−18,000,000', '3,000,000 A'],
      ['Volume: (65,000−60,000)×250', '1,250,000 F'],
    ]}},
    {'key': 'Check: 3,000,000 A − 1,250,000 F = 1,750,000 A, confirmed. And overall, '
            'TOCV = VOCV + Fixed OH total = 4,500,000 F + 1,750,000 A = **2,750,000 F**, '
            'exactly matching TOCV computed directly above.'},
    {'p': 'Volume variance itself splits further into two sub-variances:'},
    {'fbox': {'h': 'Fixed overhead volume sub-variances', 'rows': [
      {'lb': 'Volume Efficiency Variance', 'tex': '(SH - AH) \\times FOAR'},
      {'lb': 'Volume Capacity Variance', 'tex': '(AH - \\text{Budgeted hours}) \\times FOAR'},
    ]}},
    {'note': 'CIMA defines the fixed overhead volume variance as measuring the **over- or '
             'under-absorption of overhead caused by actual output differing from budgeted** — '
             'it is purely a physical-volume story, not a spending story (that\'s what '
             'expenditure variance is for).'},

    {'eg': {'tag': 'Study text', 't': 'Illustration 13.2 — the same variances, a second dataset',
      'open': True, 'q': [
      {'p': 'Lagos Ltd, product J standard cost card: materials 5kg@¢1,000 = ¢5,000; labour 1hr@'
            '¢9,000; variable overhead ¢1,000/hr; fixed overhead ¢5,000/hr (from budgeted '
            'fixed overhead ¢19,000,000 ÷ 3,800 budgeted units/hours over a 50-week year). In '
            'the first 4 weeks, 3,000 units were produced: materials 16,000kg@¢1,100 = '
            '¢17,600,000; labour cost ¢27,000,000; variable overhead, 2,800hrs actual costing '
            '¢2,520,000 (¢900/hr); fixed overhead ¢16,000,000 actual. Compute the material, '
            'variable overhead and fixed overhead variances.'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['Material variances', ''], 'rows': [
        ['Total: (3,000×5,000)−17,600,000', '2,600,000 A'],
        ['Price: (1,100−1,000)×16,000', '1,600,000 A'],
        ['Usage: (16,000−15,000)×1,000', '1,000,000 A'],
      ]}},
      {'table': {'align': 'lr', 'head': ['Variable overhead variances', ''], 'rows': [
        ['Total: (3,000×1,000)−2,520,000', '480,000 F'],
        ['Expenditure: (2,800×1,000)−2,520,000', '280,000 F'],
        ['Efficiency: (3,000−2,800)×1,000', '200,000 F'],
      ]}},
      {'table': {'align': 'lr', 'head': ['Fixed overhead variances', ''], 'rows': [
        ['Total: (3,000×5,000)−16,000,000', '1,000,000 A'],
        ['Expenditure: 19,000,000−16,000,000', '3,000,000 F'],
        ['Volume: (3,000−3,800)×5,000', '4,000,000 A'],
        ['— Volume efficiency: (3,000−2,800)×5,000', '1,000,000 F'],
        ['— Volume capacity: (2,800−3,800)×5,000', '5,000,000 A'],
      ]}},
      {'note': 'This question compares 4 weeks\' *actual* output (3,000 units) against the '
               '*full annual* budgeted output (3,800 units) when finding the fixed overhead '
               'volume variance — every check (price+usage=total; expenditure+volume=total; '
               'efficiency+capacity=volume) still reconciles exactly on this basis, confirming '
               'it is how the question is deliberately set up, not an oversight to correct.'}]}},

    {'eg': {'tag': 'Study text', 't': 'Illustration 13.3 — variable and fixed overhead '
      'variances from a flexible budget (high-low method)', 'open': True, 'q': [
      {'p': 'A flexible budget gives 90,000 standard labour hours → ¢7,000,000 overhead, and '
            '100,000 hours → ¢7,500,000 — the increase is entirely variable expense. Actual: '
            'output in standard hours 80,000; clock hours worked 90,000; actual variable '
            'overhead ¢4,800,000; actual fixed overhead ¢2,600,000. Compute the variable and '
            'fixed overhead variances.'}],
      'a': [
      {'p': 'Variable rate $= (7{,}500{,}000-7{,}000{,}000)/(100{,}000-90{,}000) = ¢50$/hr. At '
            '100,000 hrs, variable overhead $= 100{,}000 \\times 50 = ¢5{,}000{,}000$, so fixed '
            'overhead $= 7{,}500{,}000 - 5{,}000{,}000 = ¢2{,}500{,}000$ (budgeted). '
            '$FOAR = 2{,}500{,}000/100{,}000 = ¢25$/hr.'},
      {'table': {'align': 'lr', 'head': ['Variable overhead variances', ''], 'rows': [
        ['Total: (80,000×50)−4,800,000', '800,000 A'],
        ['Expenditure: (90,000×50)−4,800,000', '300,000 A'],
        ['Efficiency: (80,000−90,000)×50', '500,000 A'],
      ]}},
      {'table': {'align': 'lr', 'head': ['Fixed overhead variances', ''], 'rows': [
        ['Total: (80,000×25)−2,600,000', '600,000 A'],
        ['Expenditure: 2,500,000−2,600,000', '100,000 A'],
        ['Volume: (100,000−80,000)×25', '500,000 A'],
        ['— Volume efficiency: (80,000−90,000)×25', '250,000 A'],
        ['— Volume capacity: (90,000−100,000)×25', '250,000 A'],
      ]}}]}},
  ]},

  {'n': '13.5', 't': 'Sales margin variances', 'b': [
    {'p': 'Sales variances are measured in **profit or contribution margin**, not price — since '
          'the sales function\'s real objective is influencing profit, and cost variances '
          '(above) already cover the cost side.'},
    {'table': {'align': 'll', 'head': ['Variance', 'Meaning'], 'rows': [
      ['**Total sales margin variance**', 'Actual margin vs. budgeted margin (standard profit/'
       'contribution margin basis) — splits into a price variance and a volume variance.'],
      ['**Sales margin price variance**', 'Actual margin per unit vs. standard margin per unit, '
       'for the **actual** volume sold.'],
      ['**Sales margin volume variance**', 'Actual sales volume vs. budgeted sales volume, at '
       'the **standard** margin per unit.'],
    ]}},
    {'key': 'Two computation approaches: the **marginal costing approach** (evaluated on '
            '**contribution** margin — selling price less standard marginal/variable cost) and '
            'the **absorption costing approach** (evaluated on full **profit** margin — selling '
            'price less standard *total* cost, including fixed overhead). Whichever approach is '
            'used, standard cost is always what values both the actual and the standard margin '
            '— only the selling price/quantity varies between "actual" and "standard" lines.'},

    {'eg': {'tag': 'Study text', 't': 'Illustration 13.4 — sales quantity, price and total '
      'margin variances, three products', 'open': True, 'q': [
      {'p': 'Dzifa Manufacturing, budgeted sales mix (\'000 units): Q 200, R 300, S 500 — total '
            '1,000. Standard profit margin/unit: Q ¢10,000, R ¢6,000, S ¢4,000. Actual (\'000 '
            'units): Q 150, R 350, S 600. Actual profit margin/unit: Q ¢12,000, R ¢6,000, S '
            '¢3,000. Find the sales quantity variance, sales margin price variance, and sales '
            'margin total variance.'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['Product', 'Sales quantity variance', 'Sales margin '
        'price variance', 'Sales margin total variance'], 'rows': [
        ['Q — (150−200)×10; (12−10)×150; (150×12)−(200×10)', '500,000 A', '300,000 F',
         '200,000 A'],
        ['R — (350−300)×6; (6−6)×350; (350×6)−(300×6)', '300,000 F', 'Nil', '300,000 F'],
        ['S — (600−500)×4; (3−4)×600; (600×3)−(500×4)', '400,000 F', '600,000 A', '200,000 A'],
        ['**Total**', '**200,000 F**', '**300,000 A**', '**100,000 A**'],
      ]}},
      {'warn': 'The study text\'s own printed total for the Sales Margin Total Variance shows '
               '"100,000 F" — but summing its own three product-level figures (200,000 A + '
               '300,000 F + 200,000 A) gives **100,000 A**, not F, and this is confirmed '
               'independently by the identity Total Variance = Sales Quantity Variance + Sales '
               'Margin Price Variance = 200,000 F + 300,000 A = 100,000 A. The sign shown above '
               'is corrected accordingly.'}]}},

    {'h4': 'Reconciling budgeted profit to actual profit'},
    {'p': 'Starting from budgeted profit, every variance is added (if favourable) or subtracted '
          '(if adverse) until actual profit is reached.'},
    {'key': 'Two rules of thumb: (1) all cost variances are based on the **actual** level of '
            'production achieved, not the budgeted level; and (2) under **marginal costing**, '
            'only the fixed overhead **expenditure** variance features (fixed overhead volume '
            'variance has no meaning when fixed cost is a period cost, not absorbed into '
            'units); under **absorption costing**, fixed overhead and *all* its sub-variances '
            '(expenditure, volume, and volume\'s own efficiency/capacity split) are included.'},

    {'eg': {'tag': 'Study text', 't': 'Illustration 13.5 — a full reconciliation, marginal and '
      'absorption approaches', 'open': True, 'q': [
      {'p': 'ABC/Ayedin Ltd, product Alpha, standard cost card: materials 2kg A@¢1 + 1kg B@¢3 = '
            '¢5.00; labour 3hrs@¢3 = ¢9.00; variable overhead 3hrs@¢2 = ¢6.00; fixed overhead '
            '3hrs@¢4 = ¢12.00; total standard cost ¢32.00; standard profit margin ¢8.00; '
            'standard selling price ¢40.00. Budgeted: 10,000 units, 30,000 direct labour hours, '
            'budgeted fixed overhead ¢120,000 (FOAR ¢4/hr), budgeted profit ¢80,000. Actual: '
            '9,000 units sold @¢42; materials, labour and overhead costs as detailed in the '
            'source; actual profit ¢69,620. Reconcile budgeted to actual profit.'}],
      'a': [
      {'p': 'The individual variances (independently verified, and cross-checked to reconcile '
            'exactly to the given actual profit of ¢69,620):'},
      {'table': {'align': 'lrr', 'head': ['Variance', 'Marginal approach', 'Absorption '
        'approach'], 'rows': [
        ['Sales margin price', '18,000 F', '18,000 F'],
        ['Sales margin volume', '20,000 A', '8,000 A'],
        ['Material price (A 1,900 A, B 1,720 F)', '180 A', '180 A'],
        ['Material usage (A 1,000 A, B 3,000 A)', '4,000 A', '4,000 A'],
        ['Labour rate', '5,700 A', '5,700 A'],
        ['Labour efficiency', '4,500 A', '4,500 A'],
        ['Variable overhead expenditure', '5,000 F', '5,000 F'],
        ['Variable overhead efficiency', '3,000 A', '3,000 A'],
        ['Fixed overhead expenditure', '4,000 F', '4,000 F'],
        ['Fixed overhead volume efficiency', '— (not used)', '6,000 A'],
        ['Fixed overhead volume capacity', '— (not used)', '6,000 A'],
      ]}},
      {'table': {'align': 'lr', 'head': ['Reconciliation (marginal costing approach)', '¢'],
        'rows': [
        ['Budgeted profit', '80,000'],
        ['+ Sales margin price variance', '18,000'],
        ['− Sales margin volume variance', '(20,000)'],
        ['− Material price variance', '(180)'],
        ['− Material usage variance', '(4,000)'],
        ['− Labour rate variance', '(5,700)'],
        ['− Labour efficiency variance', '(4,500)'],
        ['+ Variable overhead expenditure variance', '5,000'],
        ['− Variable overhead efficiency variance', '(3,000)'],
        ['+ Fixed overhead expenditure variance', '4,000'],
        ['**Actual profit**', '**69,620**'],
      ]}},
      {'table': {'align': 'lr', 'head': ['Reconciliation (absorption costing approach)', '¢'],
        'rows': [
        ['Budgeted profit', '80,000'],
        ['+ Sales margin price variance', '18,000'],
        ['− Sales margin volume variance', '(8,000)'],
        ['− Material price variance', '(180)'],
        ['− Material usage variance', '(4,000)'],
        ['− Labour rate variance', '(5,700)'],
        ['− Labour efficiency variance', '(4,500)'],
        ['+ Variable overhead expenditure variance', '5,000'],
        ['− Variable overhead efficiency variance', '(3,000)'],
        ['+ Fixed overhead expenditure variance', '4,000'],
        ['− Fixed overhead volume efficiency variance', '(6,000)'],
        ['− Fixed overhead volume capacity variance', '(6,000)'],
        ['**Actual profit**', '**69,620**'],
      ]}},
      {'warn': 'The study text\'s own printed reconciliation tables for this illustration are '
               'badly disordered by scanning — rows visibly out of sequence, several figures '
               'duplicated across the wrong lines. Both tables above were **independently '
               'rebuilt** from the individually-verified variances, and each is confirmed to '
               'reconcile **exactly** to the given actual profit of ¢69,620 — the surest check '
               'available that the reconstruction is correct, since the source\'s own printed '
               'totals could not be trusted at face value here.'},
      {'note': 'The absorption approach\'s sales margin volume variance is 8,000 A, not the '
               '"8,000 F" the source prints — using the standard **profit** margin (¢8/unit, '
               'not the ¢20 contribution margin the marginal approach uses): '
               '$(9{,}000-10{,}000) \\times 8 = -8{,}000$, an adverse variance since actual '
               'volume fell short of budget — consistent with the marginal approach\'s own '
               '(correctly-signed) adverse volume variance on the same shortfall.'}]}},
  ]},

  {'n': '13.6', 't': 'Activity, capacity and efficiency ratios', 'b': [
    {'p': 'In place of (or alongside) the volume/capacity/efficiency **variances** above, the '
          'same relationships can be expressed as **ratios**.'},
    {'fbox': {'h': 'Activity, capacity and efficiency ratios', 'rows': [
      {'lb': 'Efficiency ratio', 'tex': '\\dfrac{\\text{Standard hours for actual output}}'
        '{\\text{Actual hours worked}} \\times 100'},
      {'lb': 'Activity ratio', 'tex': '\\dfrac{\\text{Standard hours for actual output}}'
        '{\\text{Budgeted hours}} \\times 100'},
      {'lb': 'Capacity ratio', 'tex': '\\dfrac{\\text{Actual hours worked}}{\\text{Budgeted '
        'hours}} \\times 100'},
    ]}},
    {'key': 'A useful identity to check any set of these ratios: '
            '$\\text{Activity ratio} = \\text{Capacity ratio} \\times \\text{Efficiency ratio}$ '
            '(as a fraction, before converting to %).'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 13.6 — the three ratios, on the same data '
      'as Illustration 13.3', 'open': True, 'q': [
      {'p': 'Budgeted hours 100,000; standard hours for actual output 80,000; actual hours '
            'worked 90,000. Compute the efficiency, activity and capacity ratios.'}],
      'a': [
      {'tex': '\\text{Efficiency ratio} = \\dfrac{80{,}000}{90{,}000} \\times 100 \\approx '
              '88.89\\%'},
      {'tex': '\\text{Activity ratio} = \\dfrac{80{,}000}{100{,}000} \\times 100 = 80\\%'},
      {'tex': '\\text{Capacity ratio} = \\dfrac{90{,}000}{100{,}000} \\times 100 = 90\\%'},
      {'key': 'Check via the identity: $90\\% \\times 88.89\\% \\approx 80\\%$ — matches the '
              'activity ratio exactly, confirming all three figures.'}]}},
  ]},

  {'n': '13.7', 't': 'Causes of variances, and deciding what to investigate', 'b': [
    {'p': 'Establishing the *real* cause of a variance takes genuine investigative skill — '
          'observation, enquiry, checking — much like an audit investigation.'},
    {'p': 'Factors influencing the decision to investigate a variance:'},
    {'table': {'align': 'll', 'head': ['Factor', 'How it points the decision'], 'rows': [
      ['**History of the variance**', 'The more frequently a deviation recurs, the *less* '
       'likely it will be investigated (it is a known, ongoing pattern); the less frequent, '
       'the *more* likely.'],
      ['**Reliability of the standard**', 'The more reliable the standard is thought to be, the '
       'higher the chance of investigating any deviation from it (and vice versa).'],
      ['**Significance of the deviation**', 'Immaterial variances are unlikely to be '
       'investigated; material ones are.'],
      ['**Cost-benefit**', 'Investigate when the benefit of investigating exceeds its cost.'],
      ['**Effect on future planning/control**', 'Even a costly investigation may be worthwhile '
       'if it genuinely improves future operations and control.'],
    ]}},
    {'key': 'Practically, management sets upper and lower **control limits** around the '
            'standard — investigation is triggered only when actual results fall **outside** '
            'those limits, not for every single deviation.'},
  ]},

  {'n': '13.10', 't': 'Chapter summary', 'b': [
    {'p': '**Standard costing is a useful control tool** that assists business organisations to '
          'ensure that their budgets are achieved, by pinpointing the areas of standard '
          'performance where corrective action needs to be taken.'},
    {'p': 'The chapter explained standard costing and variance analysis in three sections:'},
    {'ol': [
      '**Section one** explained the concept of a standard, the types of standards, standard '
      'costing, and its uses, merits and limitations.',
      '**Section two** concentrated on the analysis of the various variances — materials cost, '
      'labour cost and overhead variances.',
      '**The last section** continued the discussion of variance analysis by explaining '
      '**sales margin variances**, dealt with the **reconciliation of budgeted profit with '
      'actual profit**, explained the use of **activity, capacity and efficiency ratios**, and '
      'concluded with the **causes of variances** and the factors that influence the decision '
      'to **investigate** them.',
    ]},
    {'key': 'Hold on to the shape of the subject rather than memorising formulae one by one. '
            'Every cost variance splits the same two ways: a **price/rate/expenditure** part '
            '(you paid a different amount per unit of input than you planned) and a '
            '**usage/efficiency/volume** part (you used a different quantity of input than the '
            'output should have needed). Fixed overhead is the one exception — its "usage" half '
            'is a **volume** variance, because fixed cost does not vary with usage at all, only '
            'with how many units are available to absorb it.'},
  ]},

  {'n': '13.11', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§13.1 Standards** — 4 types (basic/ideal/attainable/current), each with its own valid '
      'use and its own blind spot; standard cost is *not* an average of past costs; 6 uses, '
      'several merits and limitations.',
      '**§13.2–13.3 Process & setting standards** — 5-step process (set→measure→compare→'
      'analyse→investigate); materials/labour/overhead/selling-price standards each set from '
      'different inputs; the standard cost card is the single reference point for everything '
      'downstream.',
      '**§13.4 Cost variances** — material (cost=price+usage), labour (cost=rate+efficiency, '
      'plus a separate idle-time variance), and overhead (TOCV=VOCV+fixed OH total; VOCV='
      'expenditure+efficiency; fixed OH total=expenditure+volume; volume=efficiency+capacity) — '
      'every level of this tree should reconcile exactly to the level above it.',
      '**§13.5 Sales margin variances & reconciliation** — measured in profit/contribution '
      'margin, not price; total = price variance + volume variance; marginal costing '
      'reconciliation uses only fixed OH expenditure variance, absorption costing uses the '
      'full fixed-overhead variance tree.',
      '**§13.6 Ratios** — efficiency/activity/capacity, an alternative lens on the same '
      'volume/capacity/efficiency story as the variances; Activity = Capacity × Efficiency is '
      'a built-in cross-check.',
      '**§13.7 Investigating variances** — 5 factors (history, standard reliability, '
      'materiality, cost-benefit, effect on future control); practically applied via control '
      'limits, not investigating every deviation.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'Standard costing formulas (recap)', 'rows': [
      {'lb': 'Material Cost Variance', 'tex': '(SQ \\times SP) - (AQ \\times AP)'},
      {'lb': 'Material Price Variance', 'tex': 'AQ \\times (SP - AP)'},
      {'lb': 'Material Usage Variance', 'tex': 'SP \\times (SQ - AQ)'},
      {'lb': 'Labour Cost Variance', 'tex': '(SH \\times SR) - (AH \\times AR)'},
      {'lb': 'Labour Rate Variance', 'tex': 'AH \\times (SR - AR)'},
      {'lb': 'Labour Efficiency Variance', 'tex': 'SR \\times (SH - AH)'},
      {'lb': 'Fixed Overhead Volume Variance', 'tex': '(SH - \\text{Budgeted hours}) \\times '
        'FOAR'},
      {'lb': 'Efficiency ratio', 'tex': '\\dfrac{SH}{AH} \\times 100'},
      {'lb': 'Activity ratio', 'tex': '\\dfrac{SH}{\\text{Budgeted hours}} \\times 100'},
      {'lb': 'Capacity ratio', 'tex': '\\dfrac{AH}{\\text{Budgeted hours}} \\times 100'},
    ]}},
  ]},

  {'n': '13.12', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following conditions explains when attainable standards can be achieved? '
        '(A) Under the best possible conditions  (B) Under the most possible conditions  '
        '(C) When there is no idle time  (D) When the same trends have been maintained over a '
        'long period of time  (E) When allowances are made for normal losses and possible '
        'machine breakdown',
        'What is the purpose of computing variances? (A) To detect fraud  (B) To punish '
        'inefficient managers  (C) To investigate why standards are not met, and take '
        'corrective actions  (D) To maintain good records  (E) To settle long-standing issues',
        'What type of variance can result from machine breakdown, power outages and work '
        'stoppages? (A) Direct labour efficiency variance  (B) Machine breakdown variance  '
        '(C) Material wastage variance  (D) Idle time variance  (E) Electricity wastage '
        'variance',
        'When we record substantial favourable variances, (A) It shows that we are working '
        'hard  (B) We investigate and break it down because it may be concealing some hidden '
        'weaknesses  (C) We give bonuses to employees  (D) We raise the standards  (E) We '
        'proudly publish it for others to see',
        'If the cost of investigating a particular variance is higher than the benefit to be '
        'derived from it, ……………. (A) The investigation is dropped  (B) We still go ahead and '
        'investigate for the records  (C) We keep the investigation till the cases pile up  '
        '(D) We spread the cost over a number of years  (E) The investigation is done in piece '
        'meal',
        'Standards which can only be attained under the most favourable working conditions are '
        'called ………………………',
        'Which costing concept best describes situations when actual costs are compared with '
        'standard costs?',
        'The official document showing the components of the standard cost of a product is '
        'known as ………………………….',
        'The addition of direct material price variance and direct material usage variance '
        'will give us a………………………………………….',
        'The difference between the standard direct labour rate and actual direct labour rate '
        'per hour for the actual total hours worked and paid for is called ……………',
      ]}],
      'a': [
      {'ol': [
        '**E** — when allowances are made for normal losses and possible machine breakdown.',
        '**C** — to investigate why standards are not met, and take corrective action.',
        '**D — idle time variance.**',
        '**B** — we investigate and break it down, since it may be concealing hidden '
        'weaknesses.',
        '**A — the investigation is dropped.**',
        '**Ideal standards.**',
        '**Variance (analysis).**',
        '**Standard Cost Card.**',
        '**Direct material cost variance.**',
        '**Direct labour rate variance.**',
      ]}]}},
  ]},

  {'n': '13.13', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with nine examination-type questions. All are '
          'reproduced below with full answers, each carrying the examining body and diet the '
          'study text credits it to, and its mark allocation.'},

    {'eg': {'tag': 'Exam type — Q13.1 (20 marks) — adapted from ICAG, November 2005',
      't': 'Investigating variances; Pass Company Limited — material, labour and variable '
           'overhead variances',
      'q': [
      {'p': '**(a)** Outline the factors that should be considered when deciding whether or not '
            'to investigate variances revealed in a standard costing and budgetary control '
            'system *(5 marks)*.'},
      {'p': '**(b)** Pass Company Limited operates a **standard marginal costing system**. The '
            'company produces a standardised product called "success" using a single raw '
            'material called material papa. During **August 2021, 5,000 units of "success" were '
            'produced**. The following data relate to actual performance during the month:'},
      {'ol': [
        'The company purchased **50,000 kg of material papa** at a cost of **¢144,000,000**.',
        'Stock levels of material papa were: **1/8/2021 — 20,000 kg; 31/8/2021 — 15,000 kg**.',
        'The company paid workers for **26,000 hours** at a total wages cost of '
        '**¢48,360,000**.',
        'The company incurred **¢16,800,000** for variable production overheads.',
      ]},
      {'stmt': {'t': 'Standard cost card — cost per unit (¢)', 'rows': [
        ['Direct material cost  12 kg @ ¢3,000 per kg', '', 36000],
        ['Direct labour cost  5 hours @ ¢1,800 per hour', '', 9000],
        ['**Prime cost**', '', 45000, '@t'],
        ['Variable production overhead cost  5 hours @ ¢600', '', 3000],
        ['**Variable production cost**', '', 48000, '@tt'],
      ]}},
      {'p': '**Required:** calculate (i) the direct material cost variance, analysed into price '
            'and usage variances; (ii) the direct wages cost variance, analysed into rate and '
            'efficiency variances; (iii) the variable production overhead cost variance, '
            'analysed into expenditure and efficiency variances *(15 marks)*.'},
      {'note': 'The study text\'s requirement (i) reads "analysed into price and **wage** '
               'variances". It means **price and usage** — the wage variances are requirement '
               '(ii).'}],
      'a': [
      {'h4': '(a)  Factors in deciding whether to investigate a variance'},
      {'ol': [
        '**The size of the variance — in absolute terms and as a percentage** of the standard. '
        'A ¢50,000 variance on a ¢100,000 standard demands attention; the same amount on a '
        '¢50 million standard probably does not.',
        '**Whether the variance is controllable.** There is no point investigating a variance '
        'caused by a factor outside the organisation\'s control, such as a national wage award '
        'or a world commodity price movement — except to revise the standard.',
        '**The trend.** A small variance that recurs in the same direction every month matters '
        'far more than a single larger one, and may signal that the standard itself is wrong. '
        'A cumulative or statistical control chart will reveal a trend that month-by-month '
        'exception reporting hides.',
        '**The cost of the investigation against the likely benefit.** Investigating consumes '
        'management time; it is worth doing only if the expected saving from correcting the '
        'cause exceeds that cost.',
        '**The likelihood that the cause can be found and corrected.** Some variances are '
        'random and will not recur; investigating them yields nothing.',
        '**The interrelationship between variances.** A favourable material price variance and '
        'an adverse usage variance usually have a single cause — cheaper, poorer material — and '
        'should be investigated together, not separately.',
        '**Whether the variance is adverse or favourable.** Both should be investigated: a large '
        '**favourable** variance may mean quality has been cut, maintenance deferred, or the '
        'standard set too loosely.',
        '**The reliability of the standard and of the measurement.** If the standard is out of '
        'date or the recording is suspect, the variance is measuring the system, not '
        'performance.',
        '**Statistical significance.** Where the distribution of a cost is known, a variance '
        'outside (say) two standard deviations from the expected value is unlikely to be chance '
        'and warrants investigation.',
      ]},
      {'h4': '(b)  Workings'},
      {'stmt': {'t': 'Materials used, and the actual prices', 'rows': [
        ['Opening stock of material papa', '', '20,000 kg'],
        ['Add: purchases', '', '50,000 kg'],
        ['Less: closing stock', '', '(15,000) kg'],
        ['**Material used in production**', '', '55,000 kg', '@t'],
        '@gap',
        ['Actual purchase price  (¢144,000,000 ÷ 50,000 kg)', '', '¢2,880 per kg'],
        ['Actual labour rate  (¢48,360,000 ÷ 26,000 hours)', '', '¢1,860 per hour'],
        ['Actual variable overhead rate  (¢16,800,000 ÷ 26,000 hours)', '', '¢646.15 per hour'],
        '@gap',
        ['Standard quantity of material for actual output  (5,000 × 12 kg)', '', '60,000 kg'],
        ['Standard hours for actual output  (5,000 × 5 hours)', '', '25,000 hours'],
      ]}},
      {'h4': '(b)(i)  Direct material cost variance'},
      {'stmt': {'t': 'Direct material variances (¢)', 'rows': [
        ['Standard material cost of actual production  (5,000 units × ¢36,000)', '', 180000000],
        ['Actual material cost of material used  (55,000 kg × ¢2,880)', '', 158400000],
        ['**Direct material cost variance**', '', '21,600,000  **FAVOURABLE**', '@tt'],
        '@gap',
        ['**Price variance**  (¢3,000 − ¢2,880) × 55,000 kg used', '',
         '6,600,000  **FAVOURABLE**'],
        ['**Usage variance**  (60,000 − 55,000 kg) × ¢3,000 standard price', '',
         '15,000,000  **FAVOURABLE**'],
        ['**Total**', '', '21,600,000  F', '@tt'],
      ]}},
      {'note': 'The price variance is computed on the **quantity used** (55,000 kg) rather than '
               'on purchases, because the question does not say that stock is valued at '
               'standard. Where it does — as in Q13.7 below — the price variance is isolated on '
               '**purchases** instead, and the two sub-variances then no longer sum to the total '
               'usage-based variance.'},
      {'h4': '(b)(ii)  Direct wages cost variance'},
      {'stmt': {'t': 'Direct labour variances (¢)', 'rows': [
        ['Standard labour cost of actual production  (5,000 units × ¢9,000)', '', 45000000],
        ['Actual wages paid', '', 48360000],
        ['**Direct wages cost variance**', '', '3,360,000  **ADVERSE**', '@tt'],
        '@gap',
        ['**Rate variance**  (¢1,800 − ¢1,860) × 26,000 hours', '',
         '1,560,000  **ADVERSE**'],
        ['**Efficiency variance**  (25,000 − 26,000 hours) × ¢1,800', '',
         '1,800,000  **ADVERSE**'],
        ['**Total**', '', '3,360,000  A', '@tt'],
      ]}},
      {'h4': '(b)(iii)  Variable production overhead cost variance'},
      {'stmt': {'t': 'Variable production overhead variances (¢)', 'rows': [
        ['Standard variable overhead for actual production  (5,000 units × ¢3,000)', '',
         15000000],
        ['Actual variable production overhead', '', 16800000],
        ['**Variable production overhead cost variance**', '', '1,800,000  **ADVERSE**', '@tt'],
        '@gap',
        ['**Expenditure variance**  (¢600 × 26,000 hours) − ¢16,800,000', '',
         '1,200,000  **ADVERSE**'],
        ['**Efficiency variance**  (25,000 − 26,000 hours) × ¢600', '',
         '600,000  **ADVERSE**'],
        ['**Total**', '', '1,800,000  A', '@tt'],
      ]}},
      {'key': 'Read the variances together, as part (a) says you should. The **material price '
              'variance is favourable** (¢2,880 paid against a ¢3,000 standard) and the '
              '**usage variance is also favourable** — material was bought cheaply *and* used '
              'sparingly, which is an unusually good result and worth understanding. But '
              '**every labour and overhead variance is adverse**, and the labour efficiency '
              'variance (1,000 hours over standard) directly causes the variable overhead '
              'efficiency variance too. One plausible story: the cheaper material was harder to '
              'work, so it took 1,000 extra hours — in which case the favourable material '
              'variances and the adverse labour ones share a single cause, and the net saving '
              'of ¢16.44 million is the figure that matters, not any one variance alone.'}]}},

    {'eg': {'tag': 'Exam type — Q13.2 (20 marks) — adapted from ICAG, November 2000',
      't': 'Four types of standard; Nsawam Poultry — labour variances with idle time',
      'q': [
      {'p': '**(a)** State and explain briefly **four** different types of standards '
            '*(8 marks)*.'},
      {'p': '**(b)** Nsawam Poultry Products Ltd employs different grades of labour on its farm. '
            'The direct labour cost of its product is **three hours of grade A labour at ¢250 '
            'per hour, resulting in ¢750 per unit** of the product. During **March 2000, 300 '
            'units** of the product were made, and the labour cost of grade A was **¢220,000 '
            'for 910 hours**. During the month there was a machine breakdown and **40 hours were '
            'recorded as idle time**.'},
      {'p': '**Required:** calculate the (i) direct labour total cost variance; (ii) direct '
            'labour rate variance; (iii) idle time variance; (iv) direct labour efficiency '
            'variance *(12 marks)*.'}],
      'a': [
      {'h4': '(a)  Four types of standard'},
      {'table': {'align': 'll', 'head': ['Type of standard', 'Explanation'], 'rows': [
        ['**1. Ideal (perfection) standard**', 'A standard set under **perfect operating '
         'conditions** — no machine breakdowns, no idle time, no wastage, no spoilage, materials '
         'always available, workers always working at peak efficiency. It represents the '
         'absolute minimum cost possible. **Rarely used for control**, because it can never be '
         'attained; variances are always adverse, which demotivates. It is useful only as a '
         'long-run target showing the theoretical limit.'],
        ['**2. Attainable (expected/current) standard**', 'A standard set at a level that '
         '**can be achieved under efficient but realistic operating conditions** — allowing for '
         'normal wastage, normal idle time and normal machine downtime. It is **demanding but '
         'achievable**, and is therefore the standard most used in practice, because it '
         'motivates and because the variances it produces are meaningful.'],
        ['**3. Basic standard**', 'A standard **left unchanged over a long period** — often '
         'years — so that trends in performance can be observed over time. Because it is not '
         'updated for changes in prices, methods or technology, it becomes progressively less '
         'useful for current control, and the variances it produces measure how much conditions '
         'have changed rather than how well the period was managed.'],
        ['**4. Current standard**', 'A standard set for a **short period** and reflecting the '
         'conditions actually prevailing in that period, including temporary and abnormal ones '
         '— a short-term shortage of a material, for example. It gives realistic variances for '
         'the period but is useless for comparison between periods, and it can conceal '
         'inefficiency by building current problems into the standard.'],
      ]}},
      {'note': 'A fifth, often added: the **normal standard**, an average standard expected to '
               'be achieved over a future period long enough to cover one trade cycle, '
               'smoothing out cyclical fluctuations.'},
      {'h4': '(b)  Workings'},
      {'stmt': {'t': 'Workings', 'rows': [
        ['Standard hours for actual production  (300 units × 3 hours)', '', '900 hours'],
        ['Standard cost of actual production  (900 hours × ¢250)', '', '¢225,000'],
        '@gap',
        ['Hours **paid for**', '', '910 hours'],
        ['Less: idle time', '', '(40) hours'],
        ['**Hours actually worked**', '', '870 hours', '@t'],
        ['Actual wages paid', '', '¢220,000'],
        ['Actual rate per hour  (¢220,000 ÷ 910)', '', '¢241.76'],
      ]}},
      {'h4': '(b)  The four variances'},
      {'stmt': {'t': 'Direct labour variances (¢)', 'rows': [
        ['**(i) Direct labour total cost variance**', '', '', '@hd'],
        ['Standard cost of actual production', 225000, ''],
        ['Actual wages paid', 220000, '5,000  **FAVOURABLE**'],
        '@gap',
        ['**(ii) Direct labour rate variance**', '', '', '@hd'],
        ['Hours paid at standard rate  (910 × ¢250)', 227500, ''],
        ['Actual wages paid', 220000, '7,500  **FAVOURABLE**'],
        '@gap',
        ['**(iii) Idle time variance**', '', '', '@hd'],
        ['Idle hours × standard rate  (40 × ¢250)', '', '10,000  **ADVERSE**'],
        '@gap',
        ['**(iv) Direct labour efficiency variance**', '', '', '@hd'],
        ['(Standard hours 900 − hours **worked** 870) × ¢250', '', '7,500  **FAVOURABLE**'],
        '@gap',
        ['**Reconciliation:  7,500 F − 10,000 A + 7,500 F**', '', '5,000  **FAVOURABLE**',
         '@tt'],
      ]}},
      {'warn': 'The whole question turns on the distinction between **hours paid for (910)** and '
               '**hours worked (870)**. The **rate** variance uses hours **paid**, because the '
               'company paid the rate on all 910 hours. The **efficiency** variance uses hours '
               '**worked**, because the 40 idle hours were not available for production and are '
               'dealt with separately by the **idle time variance**. Mixing the two is the '
               'commonest error: computing efficiency on 910 hours would give '
               '$(900-910) \\times 250 = ¢2{,}500$ adverse and the reconciliation would then '
               'fail.'},
      {'key': 'Note what the analysis reveals. On the face of it the month looks good — a '
              '¢5,000 **favourable** total variance. But that masks a **¢10,000 adverse idle '
              'time variance** caused by the machine breakdown, offset by a cheaper labour rate '
              'and genuinely efficient working in the hours that were available (870 hours doing '
              '900 hours\' work). Management should be told about the breakdown, not reassured '
              'by the net figure.'}]}},

    {'eg': {'tag': 'Exam type — Q13.3 (20 marks) — ICAG, May 2000',
      't': 'Working backwards from variances to units produced, usage variance and actual price',
      'q': [
      {'p': 'A company produces a product which has a **standard variable production cost of '
            '¢8,000 per unit**, made up as follows:'},
      {'stmt': {'t': 'Standard variable production cost per unit (¢)', 'rows': [
        ['Direct materials  (2 kg × ¢2,300 per kg)', '', 4600],
        ['Direct labour  (0.7 hours × ¢3,000 per hour)', '', 2100],
        ['Variable overhead', '', 1300],
        ['**Standard variable production cost**', '', 8000, '@tt'],
      ]}},
      {'p': 'Fixed manufacturing costs are treated as period costs. The following information is '
            'available for the period just ended:'},
      {'stmt': {'t': 'Information for the period (¢)', 'rows': [
        ['Variable manufacturing cost of sales (at standard cost)', '', 263520000],
        ['Opening stock of finished goods (at standard cost)', '', 120800000],
        ['Closing stock of finished goods (at standard cost)', '', 146080000],
        ['Direct material price variance', '', '2,571,000 adverse'],
        ['Raw material used in manufacture (at actual cost)', '', 170310000],
      ]}},
      {'p': '**Required:** **(a)** determine for the period (i) the number of units produced; '
            '(ii) the raw materials usage variance; (iii) the total actual direct labour cost; '
            '(iv) the total actual cost per kg of raw material used. **(b)** Outline the '
            'possible causes of the raw material variances.'}],
      'a': [
      {'h4': '(a)(i)  Number of units produced'},
      {'p': 'All three finished-goods figures are at **standard cost**, so the finished goods '
            'identity can be rearranged to give the cost of production, and the units follow by '
            'dividing by the ¢8,000 standard cost per unit.'},
      {'stmt': {'t': 'Units produced (¢)', 'rows': [
        ['Variable manufacturing cost of sales, at standard', '', 263520000],
        ['Add: closing stock of finished goods, at standard', '', 146080000],
        ['', '', 409600000, '@t'],
        ['Less: opening stock of finished goods, at standard', '', -120800000],
        ['**Cost of production for the period, at standard**', '', 288800000, '@t'],
        ['÷ standard variable production cost per unit', '', '¢8,000'],
        ['**Number of units produced**', '', '36,100 units', '@tt'],
      ]}},
      {'h4': '(a)(ii)  Raw materials usage variance'},
      {'stmt': {'t': 'Raw materials usage variance (¢)', 'rows': [
        ['Actual cost of raw material used', '', 170310000],
        ['Less: direct material price variance (adverse — so actual cost is this much **above** '
         'the standard price for the quantity used)', '', -2571000],
        ['**Actual quantity used, valued at standard price**', '', 167739000, '@t'],
        '@gap',
        ['Standard material cost of actual production  (36,100 units × ¢4,600)', '', 166060000],
        ['**Raw materials usage variance**', '', '1,679,000  **ADVERSE**', '@tt'],
      ]}},
      {'h4': '(a)(iii)  Total actual direct labour cost'},
      {'stmt': {'t': 'Direct labour cost (¢)', 'rows': [
        ['Standard direct labour cost of actual production  (36,100 units × ¢2,100)', '',
         75810000],
        ['**Total actual direct labour cost**', '', 75810000, '@tt'],
      ]}},
      {'warn': 'The question supplies **no labour variance of any kind**. The only defensible '
               'reading is therefore that there was none — i.e. the actual direct labour cost '
               '**equalled the standard cost of the actual production**, ¢75,810,000. State '
               'this assumption explicitly. If a labour rate or efficiency variance had been '
               'given, it would be added to (if adverse) or deducted from (if favourable) the '
               'standard figure to arrive at the actual.',
       'lbl': 'An assumption the question forces'},
      {'h4': '(a)(iv)  Total actual cost per kg of raw material used'},
      {'stmt': {'t': 'Actual cost per kg', 'rows': [
        ['Actual quantity used, valued at standard price (from (ii))', '', '¢167,739,000'],
        ['÷ standard price per kg', '', '¢2,300'],
        ['**Actual quantity of raw material used**', '', '72,930 kg', '@t'],
        '@gap',
        ['Actual cost of raw material used', '', '¢170,310,000'],
        ['÷ actual quantity used', '', '72,930 kg'],
        ['**Actual cost per kg**', '', '¢2,335.25', '@tt'],
      ]}},
      {'note': 'Cross-check: the price variance per kg is '
               '$¢2{,}571{,}000 \\div 72{,}930 = ¢35.25$ adverse, and '
               '$¢2{,}300 + ¢35.25 = ¢2{,}335.25$ ✓. A second cross-check on the usage '
               'variance: standard quantity for 36,100 units is '
               '$36{,}100 \\times 2 = 72{,}200$ kg against 72,930 kg used, a difference of '
               '730 kg at ¢2,300 = **¢1,679,000 adverse** ✓'},
      {'h4': '(b)  Possible causes of the raw material variances'},
      {'p': '**Adverse price variance (¢2,571,000):**'},
      {'ul': [
        'a general **increase in the market price** of the material since the standard was set;',
        '**buying in smaller quantities** than planned, so losing quantity discounts;',
        '**emergency purchases** at short notice to avoid a stockout, at premium prices and '
        'carriage;',
        '**buying a higher grade** of material than the standard specifies;',
        '**change of supplier**, or loss of a negotiated contract price;',
        '**inflation, exchange rate movement or import duty** on an imported material;',
        'an **out-of-date standard price** that no longer reflects the market.',
      ]},
      {'p': '**Adverse usage variance (¢1,679,000):**'},
      {'ul': [
        '**poor quality material**, causing more scrap, rejects and rework;',
        '**careless handling, pilferage, deterioration or evaporation** in store or on the shop '
        'floor;',
        '**inefficient or inexperienced labour**, or inadequate supervision;',
        '**faulty or badly maintained machinery** producing more defective output;',
        '**change in the method of production** or in the product specification;',
        '**theft** or unrecorded issues;',
        'an **unrealistically tight standard** quantity that never allowed enough for normal '
        'wastage.',
      ]},
      {'key': 'The two variances here are **adverse together**, which rules out the commonest '
              'single explanation (cheap material used wastefully). A more likely story is that '
              'a **higher-grade or emergency-purchased material** was bought at a premium and '
              'then used by labour unfamiliar with it, or that the **standards themselves are '
              'out of date** in both price and quantity. The question asks for possible causes; '
              'a good answer groups them and then says which combination best fits the '
              'direction of both variances.'}]}},

    {'eg': {'tag': 'Exam type — Q13.4 (15 marks) — ICAG, November 1997',
      't': 'Three standard-costing terms, the steps in setting up a system, and causes of three '
           'variances',
      'q': [
      {'p': '**(a)** Explain the terms: (i) ideal standard; (ii) attainable standard; '
            '(iii) standard hour or minute *(3 marks)*.'},
      {'p': '**(b)** List **four** main steps in setting up a standard costing system '
            '*(6 marks)*.'},
      {'p': '**(c)** Identify **three** causes of each of the following variances: (i) direct '
            'material price variances; (ii) direct labour efficiency variances; (iii) overheads '
            'expenditure variances *(6 marks)*.'}],
      'a': [
      {'h4': '(a)  The three terms'},
      {'def': {'t': '(i) Ideal standard', 'd': 'a standard set under **perfect operating '
                    'conditions**, making no allowance for wastage, spoilage, idle time, machine '
                    'breakdown or inefficiency of any kind. It represents the theoretical '
                    'minimum cost. Because it can never be attained in practice, every variance '
                    'against it is adverse, which makes it demotivating and of little use for '
                    'routine control.'}},
      {'def': {'t': '(ii) Attainable standard', 'd': 'a standard set at a level that **can be '
                    'achieved under efficient but realistic operating conditions**, allowing for '
                    'normal levels of wastage, idle time and machine downtime. It is demanding '
                    'but achievable, and is the type of standard most widely used, because it '
                    'motivates and produces meaningful variances.'}},
      {'def': {'t': '(iii) Standard hour (or standard minute)', 'd': 'a measure of **output**, '
                    'not of time: the quantity of work that **should** be performed in one hour '
                    '(or minute) under standard conditions. It allows dissimilar products to be '
                    'added together into a single measure of output — a factory producing 100 '
                    'units of a product with a standard time of 2 hours and 300 units of one '
                    'with a standard time of 0.5 hours has produced $200 + 150 = 350$ standard '
                    'hours of output — and it is the basis of the activity, capacity and '
                    'efficiency ratios of §13.6.'}},
      {'h4': '(b)  Four main steps in setting up a standard costing system'},
      {'steps': [
        '**Establish the cost centres and the products** for which standards are to be set, and '
        'define the **standard operating conditions** — the methods, the plant, the activity '
        'level and the grades of labour that the standards will assume.',
        '**Set the standard quantities** of each input for each unit of output: the standard '
        'material specification (quantity and grade, with an allowance for normal wastage), '
        'determined from the engineering specification and from test runs; and the standard '
        'labour times, determined by **work study and time and motion study** for each grade and '
        'operation.',
        '**Set the standard prices and rates**: standard material prices (from the purchasing '
        'department, reflecting expected market prices, contract terms and quantity discounts), '
        'standard wage rates (from the personnel department, reflecting agreed rates for each '
        'grade), and **standard overhead absorption rates** (budgeted overhead ÷ budgeted '
        'activity, for variable and fixed overhead separately).',
        '**Prepare the standard cost card** for each product, bringing all of the above '
        'together to give the standard cost per unit, and obtain its approval.',
        '**Establish the recording and reporting procedures** — the documents that will capture '
        'actual quantities, hours and costs on a basis comparable with the standards, the '
        'variance calculations, the reporting format and timetable, and the procedure for '
        'investigating and acting on variances.',
        '**Set up a procedure for reviewing and revising the standards** as prices, methods and '
        'conditions change, so that the system does not decay into measuring how out-of-date the '
        'standards have become.',
      ]},
      {'h4': '(c)(i)  Three causes of direct material price variances'},
      {'ol': [
        '**A change in the market price** of the material since the standard was set — inflation, '
        'a commodity price movement, an exchange rate change on an imported material.',
        '**Buying in a different quantity** from that assumed — losing (or gaining) quantity '
        'discounts, or making emergency purchases in small lots at premium prices.',
        '**Buying a different grade or quality** of material from the standard specification, or '
        'changing supplier.',
        '*(Also: inefficient or efficient buying; an out-of-date standard price; a change in '
        'carriage or duty.)*',
      ]},
      {'h4': '(c)(ii)  Three causes of direct labour efficiency variances'},
      {'ol': [
        '**The grade or experience of the labour used** — a lower grade, or newly recruited and '
        'untrained workers, take longer than standard; a higher grade may take less.',
        '**The quality of materials and the condition of machinery** — poor material, or badly '
        'maintained machines, slow the work and cause rework; conversely, better material or new '
        'equipment speeds it.',
        '**Working conditions, supervision and motivation** — poor layout, interruptions, poor '
        'supervision, low morale or the absence of an incentive scheme all lengthen the time '
        'taken.',
        '*(Also: an unrealistic standard time; a change in the production method; the learning '
        'effect on a new product.)*',
      ]},
      {'h4': '(c)(iii)  Three causes of overhead expenditure variances'},
      {'ol': [
        '**Price changes in the individual overhead items** — rent reviews, insurance premiums, '
        'energy tariffs, rates, salaries of indirect staff.',
        '**A change in the quantity of overhead resources consumed** — more or less indirect '
        'material, indirect labour, power, maintenance or supervision than budgeted.',
        '**Inefficiency or economy in the control of overhead spending**, or an unplanned event '
        'such as a major repair, a reorganisation or a one-off cost not in the budget.',
        '*(Also: an unrealistic or out-of-date overhead budget; a change in the classification of '
        'a cost between departments.)*',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q13.5 (20 marks) — adapted from ICAG, November 2005',
      't': 'End Times Limited — full variance analysis and reconciliation of budgeted to actual '
           'profit',
      'q': [
      {'p': 'End Times Limited manufactures and sells a single product, the standard cost of '
            'which is as follows:'},
      {'stmt': {'t': 'Standards per unit (¢)', 'rows': [
        ['Selling price', '', 107200],
        '@gap',
        ['**Standard cost**', '', '', '@hd'],
        ['Materials:  64 units @ ¢400', 25600, ''],
        ['Labour:  16 hours @ ¢300', 4800, ''],
        ['Overheads:  16 hours @ ¢2,400', 38400, 68800],
        ['**Standard profit margin**', '', 38400, '@tt'],
      ]}},
      {'p': 'The following information relates to the activities of End Times for the month of '
            'September 2021:'},
      {'stmt': {'t': 'Budgeted and actual figures', 'rows': [
        ['', 'Budgeted', 'Actual', '@hd'],
        ['Production and sales (units)', 60000, 50000],
        ['Direct labour hours', 960000, '820,000  *(see note)*'],
        ['Wage rate per hour (¢)', 300, 450],
        ['Fixed overheads (¢)', 768000000, 800000000],
        ['Variable overheads (¢)', 1536000000, 1614000000],
        ['Material units', 3840000, 3840000],
        ['Material price per unit (¢)', 400, 300],
      ]}},
      {'p': 'The actual selling price during September 2021 was **¢105,000** and there were no '
            'opening or closing stocks of finished goods. End Times Limited uses an '
            '**absorption costing** system.'},
      {'p': '**Required:** **(a)** prepare profit statements to ascertain the budgeted profit '
            'and the actual profit for September 2021 *(6 marks)*; **(b)** calculate all the '
            'relevant variances and reconcile the budgeted and actual profits *(14 marks)*.'},
      {'warn': 'The study text prints the **actual** direct labour hours as **20,000**, which is '
               'impossible — the budget is 960,000 hours for 60,000 units, so 50,000 units at '
               'standard would need 800,000 hours. The figure cannot be recovered from the '
               'printed data (the PDF page was checked directly). **820,000 hours has been '
               'assumed** below, and the assumption is validated by the fact that the '
               'reconciliation at (b) then closes **exactly** on the independently computed '
               'actual profit of ¢1,315,000,000. State the assumption in any answer.',
       'lbl': 'A figure missing from the study text'},
      {'note': 'The variable and fixed overhead figures are printed without their scale. They '
               'are in **¢\'000** — because $768{,}000{,}000 + 1{,}536{,}000{,}000 = '
               '¢2{,}304{,}000{,}000$, which is exactly '
               '$60{,}000 \\text{ units} \\times ¢38{,}400$, the budgeted overhead on the '
               'standard cost card. That check also gives the split of the ¢2,400 hourly '
               'overhead rate into **¢800 fixed and ¢1,600 variable**.'}],
      'a': [
      {'h4': 'Workings — splitting the standard overhead rate'},
      {'stmt': {'t': 'Standard overhead rates', 'rows': [
        ['Budgeted fixed overhead ÷ budgeted hours  (¢768,000,000 ÷ 960,000)', '',
         '¢800 per hour'],
        ['Budgeted variable overhead ÷ budgeted hours  (¢1,536,000,000 ÷ 960,000)', '',
         '¢1,600 per hour'],
        ['**Total standard overhead rate**', '', '**¢2,400 per hour** ✓'],
        '@gap',
        ['Fixed overhead per unit  (16 hours × ¢800)', '', '¢12,800'],
        ['Variable overhead per unit  (16 hours × ¢1,600)', '', '¢25,600'],
        ['**Total overhead per unit**', '', '**¢38,400** ✓'],
        '@gap',
        ['Standard hours for actual output  (50,000 units × 16 hours)', '', '800,000 hours'],
        ['Standard material units for actual output  (50,000 × 64)', '', '3,200,000 units'],
      ]}},
      {'h4': '(a)  Budgeted and actual profit statements'},
      {'stmt': {'t': 'Budgeted profit statement, September 2021 (¢)', 'rows': [
        ['Sales  (60,000 units × ¢107,200)', '', 6432000000],
        ['Less: standard cost of sales  (60,000 × ¢68,800)', '', 4128000000],
        ['**Budgeted profit**  (60,000 × ¢38,400)', '', 2304000000, '@tt'],
      ]}},
      {'stmt': {'t': 'Actual profit statement, September 2021 (¢)', 'rows': [
        ['Sales  (50,000 units × ¢105,000)', '', 5250000000],
        '@gap',
        ['**Actual costs**', '', '', '@hd'],
        ['Materials  (3,840,000 units × ¢300)', 1152000000, ''],
        ['Labour  (820,000 hours × ¢450)', 369000000, ''],
        ['Fixed overheads', 800000000, ''],
        ['Variable overheads', 1614000000, 3935000000],
        ['**Actual profit**', '', 1315000000, '@tt'],
      ]}},
      {'h4': '(b)  The variances'},
      {'stmt': {'t': 'Sales variances (¢)', 'rows': [
        ['**Sales price variance**  (¢105,000 − ¢107,200) × 50,000 units', '',
         '110,000,000  **ADVERSE**'],
        ['**Sales volume profit variance**  (50,000 − 60,000) × ¢38,400 standard profit', '',
         '384,000,000  **ADVERSE**'],
      ]}},
      {'stmt': {'t': 'Direct material variances (¢)', 'rows': [
        ['Standard material cost of actual production  (50,000 × ¢25,600)', '', 1280000000],
        ['Actual material cost  (3,840,000 × ¢300)', '', 1152000000],
        ['**Total material cost variance**', '', '128,000,000  **FAVOURABLE**', '@t'],
        '@gap',
        ['**Price variance**  (¢400 − ¢300) × 3,840,000 units', '',
         '384,000,000  **FAVOURABLE**'],
        ['**Usage variance**  (3,200,000 − 3,840,000) × ¢400', '',
         '256,000,000  **ADVERSE**'],
      ]}},
      {'stmt': {'t': 'Direct labour variances (¢)', 'rows': [
        ['Standard labour cost of actual production  (50,000 × ¢4,800)', '', 240000000],
        ['Actual labour cost  (820,000 × ¢450)', '', 369000000],
        ['**Total labour cost variance**', '', '129,000,000  **ADVERSE**', '@t'],
        '@gap',
        ['**Rate variance**  (¢300 − ¢450) × 820,000 hours', '',
         '123,000,000  **ADVERSE**'],
        ['**Efficiency variance**  (800,000 − 820,000) × ¢300', '',
         '6,000,000  **ADVERSE**'],
      ]}},
      {'stmt': {'t': 'Variable overhead variances (¢)', 'rows': [
        ['Standard variable overhead for actual production  (800,000 hrs × ¢1,600)', '',
         1280000000],
        ['Actual variable overhead', '', 1614000000],
        ['**Total variable overhead variance**', '', '334,000,000  **ADVERSE**', '@t'],
        '@gap',
        ['**Expenditure variance**  (820,000 hrs × ¢1,600) − ¢1,614,000,000', '',
         '302,000,000  **ADVERSE**'],
        ['**Efficiency variance**  (800,000 − 820,000) × ¢1,600', '',
         '32,000,000  **ADVERSE**'],
      ]}},
      {'stmt': {'t': 'Fixed overhead variances (¢)', 'rows': [
        ['Fixed overhead absorbed  (50,000 units × ¢12,800)', '', 640000000],
        ['Actual fixed overhead', '', 800000000],
        ['**Total fixed overhead variance**', '', '160,000,000  **ADVERSE**', '@t'],
        '@gap',
        ['**Expenditure variance**  budgeted ¢768,000,000 − actual ¢800,000,000', '',
         '32,000,000  **ADVERSE**'],
        ['**Volume variance**  (50,000 − 60,000) × ¢12,800', '',
         '128,000,000  **ADVERSE**'],
        '@gap',
        ['*of which — capacity variance*  (820,000 − 960,000 hrs) × ¢800', '',
         '*112,000,000  ADVERSE*'],
        ['*of which — efficiency variance*  (800,000 − 820,000 hrs) × ¢800', '',
         '*16,000,000  ADVERSE*'],
      ]}},
      {'h4': '(b)  Reconciliation of budgeted profit with actual profit'},
      {'stmt': {'t': 'Reconciliation statement, September 2021 (¢)', 'rows': [
        ['**Budgeted profit**  (60,000 units × ¢38,400)', '', 2304000000],
        ['Sales volume profit variance', '', -384000000],
        ['**Standard profit on actual sales**  (50,000 × ¢38,400)', '', 1920000000, '@t'],
        '@gap',
        ['', 'Favourable', 'Adverse', '@hd'],
        ['Sales price variance', '', 110000000],
        ['Material price variance', 384000000, ''],
        ['Material usage variance', '', 256000000],
        ['Labour rate variance', '', 123000000],
        ['Labour efficiency variance', '', 6000000],
        ['Variable overhead expenditure variance', '', 302000000],
        ['Variable overhead efficiency variance', '', 32000000],
        ['Fixed overhead expenditure variance', '', 32000000],
        ['Fixed overhead volume variance', '', 128000000],
        ['', 384000000, 989000000, '@t'],
        ['**Net adverse variances**', '', -605000000],
        '@gap',
        ['**Actual profit**', '', 1315000000, '@tt'],
      ]}},
      {'key': 'The reconciliation closes **exactly** on the ¢1,315,000,000 computed '
              'independently in the actual profit statement at (a) — which validates both the '
              'variance calculations and the 820,000-hour assumption. **Always finish a '
              'reconciliation by checking it against the directly computed actual profit**; if '
              'the two do not agree, a variance has been omitted, double-counted, or given the '
              'wrong sign.'},
      {'note': 'What the figures say to management: the only good news is the **material price '
               'variance of ¢384 million favourable** — material was bought at ¢300 against a '
               '¢400 standard, a 25% saving. But material **usage** was 3,840,000 units for an '
               'output that should have needed 3,200,000 — a 20% overconsumption costing ¢256 '
               'million. The cheap material was almost certainly inferior, and the same cause '
               'probably explains the 20,000 excess labour hours. Set against a wage rate 50% '
               'above standard and output 17% below budget, the month cost the company ¢989 '
               'million of adverse variances against ¢384 million favourable.'}]}},

    {'eg': {'tag': 'Exam type — Q13.6 (15 marks)',
      't': 'The procedure for setting standard material and labour costs',
      'q': [{'p': 'Outline the procedure for setting standard costs of the following cost '
                  'elements: (i) materials cost; (ii) labour cost.'}],
      'a': [
      {'h4': '(i)  Setting the standard materials cost'},
      {'p': 'The standard material cost per unit is **standard quantity × standard price**, and '
            'the two are set by different people from different information.'},
      {'h4': 'Setting the standard quantity (the material specification)'},
      {'steps': [
        '**Obtain the product specification** — the engineering drawing, bill of materials or '
        'recipe — identifying every material and component required, and its grade and quality.',
        '**Determine the net quantity** of each material required in the finished product, from '
        'the specification and from **test runs and technical analysis**.',
        '**Add an allowance for normal, unavoidable losses** — evaporation, trimming, offcuts, '
        'rejects and shrinkage — determined from past experience and work study. Only '
        '**normal** losses are included; abnormal losses must remain visible as variances.',
        '**Decide the standard mix** where more than one material is combined, and the standard '
        'yield expected from it.',
        '**Review and agree** the specification with production and engineering, and document it '
        'on the standard cost card.',
      ]},
      {'h4': 'Setting the standard price'},
      {'steps': [
        '**The purchasing department** establishes the price, since it is responsible for buying '
        'and will be held accountable for the price variance.',
        '**Review current and past prices paid**, supplier quotations and contracts, and price '
        'lists.',
        '**Forecast price movements** over the period the standard will cover — inflation, '
        'commodity trends, exchange rates for imported material, and duty.',
        '**Allow for the normal purchase quantity and its discounts**, and for carriage, '
        'insurance and duty, so that the standard is a **delivered** cost.',
        '**Decide the type of standard** — an attainable standard reflecting expected prices is '
        'normal — and agree who is accountable for departures from it.',
      ]},
      {'h4': '(ii)  Setting the standard labour cost'},
      {'p': 'The standard labour cost per unit is **standard time × standard rate**, and again '
            'the two come from different sources.'},
      {'h4': 'Setting the standard time'},
      {'steps': [
        '**Carry out method study** — determine the best method of performing each operation, '
        'the sequence, the layout, the tools and the working conditions. The standard time must '
        'be the time for the **agreed best method**, not for however the job happens to be done.',
        '**Carry out work measurement (time and motion study)** on that method, timing a '
        'qualified worker performing it at a defined level of effort, and **rating** the '
        'observed performance to convert it to a basic time.',
        '**Add relaxation and contingency allowances** for rest, personal needs, fatigue and '
        'unavoidable short delays, to convert basic time into standard time.',
        '**Add an allowance for normal idle time, set-up time and machine downtime** where '
        'policy is to build these into the standard.',
        '**Express the result as standard hours or standard minutes per unit**, by operation and '
        'by grade of labour, and agree it with production management and, where necessary, with '
        'employee representatives.',
      ]},
      {'h4': 'Setting the standard rate'},
      {'steps': [
        '**The personnel (human resources) department** establishes the rate, from the agreed '
        'wage structure for each grade of labour.',
        '**Identify the grade of labour** each operation requires, from the method study, and '
        'the rate payable to that grade.',
        '**Take account of negotiated wage agreements** in force or anticipated, and of expected '
        'increases during the period the standard will cover.',
        '**Allow for the method of remuneration** — time rate, piece rate or bonus scheme — and '
        'for any shift or overtime premium that is a normal part of the work.',
        '**Compute a weighted average rate** where an operation is performed by a mix of grades, '
        'and document the result on the standard cost card.',
      ]},
      {'key': 'The common thread is that **quantity standards are technical** and come from '
              'engineering and work study, while **price standards are commercial** and come '
              'from purchasing and personnel. That division is deliberate: it is what allows the '
              'resulting variance to be analysed into a price part, for which the buyer or the '
              'personnel department answers, and a usage or efficiency part, for which '
              'production answers.'}]}},

    {'eg': {'tag': 'Exam type — Q13.7 (20 marks) — ICAG Management Accounting, November 2000',
      't': 'Benefits of standard costing; Success Company Ltd — variances with stock at standard',
      'q': [
      {'p': '**(a)** Outline the benefits which a company may derive from a standard costing '
            'system *(5 marks)*.'},
      {'p': '**(b)** Success Company Ltd, a manufacturer of aluminium roofing sheets, operates a '
            '**standard marginal costing system**. It produces a standardised roofing sheet '
            'using a single raw material, Alumina. Standard costs relating to one unit have been '
            'calculated as follows:'},
      {'stmt': {'t': 'Standard cost per unit of roofing sheet (¢)', 'rows': [
        ['Direct material:  10 kg @ ¢3,000 per kg', '', 30000],
        ['Direct labour:  5 hours @ ¢1,800 per hour', '', 9000],
        ['**Prime cost**', '', 39000, '@t'],
        ['Variable production overhead:  5 hours @ ¢600 per hour', '', 3000],
        ['**Total variable production cost**', '', 42000, '@tt'],
      ]}},
      {'p': 'During the first week of November, **1,000 units** of roofing sheets were produced. '
            'The relevant information on actual performance is:'},
      {'ol': [
        'Opening stock of raw material, Alumina, was **4,000 kg**.',
        '**10,000 kg** of Alumina were bought during the week at a cost of **¢28,800,000**.',
        'Stock at the close of the week was **3,000 kg**.',
        '**Stocks of raw materials are valued at the standard price of ¢3,000 per kg.**',
        '**5,200 direct labour hours** were worked during the week at a total wage bill of '
        '**¢9,672,000**.',
        'Actual variable production overhead for the week was **¢3,360,000**.',
      ]},
      {'p': '**Required:** compute the following cost variances for the week: (i) the variable '
            'production cost variance; (a) direct wages cost variance analysed into rate and '
            'efficiency; (b) direct material cost variance analysed into price and usage; '
            '(c) variable production overhead variance *(15 marks)*.'}],
      'a': [
      {'h4': '(a)  Benefits of a standard costing system'},
      {'ol': [
        '**It provides a basis for cost control.** Comparing actual with standard produces '
        'variances that pinpoint exactly where performance departed from plan and by how much, '
        'so management attention goes where it is needed.',
        '**It enables management by exception.** Only significant variances are reported, '
        'freeing management time from the mass of results that are in line with expectation.',
        '**It assists budgeting and planning.** Standard costs are the building blocks of the '
        'production cost budget and of forecasts at any activity level.',
        '**It simplifies inventory valuation and bookkeeping.** Inventory and work-in-progress '
        'are valued at standard, so the records are simpler, costing is faster, and the clerical '
        'effort of tracking actual costs through the ledgers is avoided.',
        '**It assists pricing and decision-making**, by providing a reliable, consistent, '
        'predetermined cost per unit for quotations and tenders rather than a historical figure '
        'that arrives too late.',
        '**It motivates and evaluates.** Standards are targets, and variance reports provide an '
        'objective basis for assessing the performance of each responsibility centre.',
        '**It promotes cost consciousness and efficiency**, because the exercise of setting '
        'standards itself requires methods, specifications and working practices to be examined '
        'and improved.',
        '**It delegates authority without losing control**, since managers can be given freedom '
        'to operate while being held to a clear, quantified standard.',
      ]},
      {'h4': '(b)  Workings'},
      {'stmt': {'t': 'Workings', 'rows': [
        ['Opening stock of Alumina', '', '4,000 kg'],
        ['Add: purchases', '', '10,000 kg'],
        ['Less: closing stock', '', '(3,000) kg'],
        ['**Material used in production**', '', '11,000 kg', '@t'],
        '@gap',
        ['Actual purchase price  (¢28,800,000 ÷ 10,000 kg)', '', '¢2,880 per kg'],
        ['Actual labour rate  (¢9,672,000 ÷ 5,200 hours)', '', '¢1,860 per hour'],
        '@gap',
        ['Standard quantity of material for actual output  (1,000 × 10 kg)', '', '10,000 kg'],
        ['Standard hours for actual output  (1,000 × 5 hours)', '', '5,000 hours'],
      ]}},
      {'warn': 'Note point (iv) of the question: **raw material stocks are valued at the '
               'standard price**. That means the material price variance must be isolated at the '
               'point of **purchase**, on the **10,000 kg bought**, not on the 11,000 kg used. '
               'The stores account is then kept wholly at standard, and all material issued to '
               'production carries the standard ¢3,000 price. Compare with Q13.1 above, where '
               'no such statement is made and the price variance is computed on usage.'},
      {'h4': '(b)(b)  Direct material cost variance'},
      {'stmt': {'t': 'Direct material variances (¢)', 'rows': [
        ['**Price variance**  (¢3,000 − ¢2,880) × 10,000 kg **purchased**', '',
         '1,200,000  **FAVOURABLE**'],
        ['**Usage variance**  (10,000 − 11,000 kg) × ¢3,000 standard price', '',
         '3,000,000  **ADVERSE**'],
        ['**Direct material cost variance**', '', '1,800,000  **ADVERSE**', '@tt'],
      ]}},
      {'h4': '(b)(a)  Direct wages cost variance'},
      {'stmt': {'t': 'Direct labour variances (¢)', 'rows': [
        ['Standard labour cost of actual production  (1,000 × ¢9,000)', '', 9000000],
        ['Actual wage bill', '', 9672000],
        ['**Direct wages cost variance**', '', '672,000  **ADVERSE**', '@t'],
        '@gap',
        ['**Rate variance**  (¢1,800 − ¢1,860) × 5,200 hours', '', '312,000  **ADVERSE**'],
        ['**Efficiency variance**  (5,000 − 5,200 hours) × ¢1,800', '',
         '360,000  **ADVERSE**'],
        ['**Total**', '', '672,000  A', '@tt'],
      ]}},
      {'h4': '(b)(c)  Variable production overhead variance'},
      {'stmt': {'t': 'Variable production overhead variances (¢)', 'rows': [
        ['Standard variable overhead for actual production  (1,000 × ¢3,000)', '', 3000000],
        ['Actual variable production overhead', '', 3360000],
        ['**Variable production overhead variance**', '', '360,000  **ADVERSE**', '@t'],
        '@gap',
        ['**Expenditure variance**  (¢600 × 5,200 hours) − ¢3,360,000', '',
         '240,000  **ADVERSE**'],
        ['**Efficiency variance**  (5,000 − 5,200 hours) × ¢600', '',
         '120,000  **ADVERSE**'],
        ['**Total**', '', '360,000  A', '@tt'],
      ]}},
      {'h4': '(b)(i)  Variable production cost variance'},
      {'stmt': {'t': 'Total variable production cost variance (¢)', 'rows': [
        ['Direct material cost variance', '', '1,800,000  ADVERSE'],
        ['Direct wages cost variance', '', '672,000  ADVERSE'],
        ['Variable production overhead variance', '', '360,000  ADVERSE'],
        ['**Variable production cost variance**', '', '2,832,000  **ADVERSE**', '@tt'],
      ]}},
      {'key': 'Every variance but the material price is adverse, and they share a likely common '
              'cause: Alumina was bought 4% below standard price (¢2,880 against ¢3,000), and '
              '**11,000 kg were consumed where 10,000 should have sufficed** — a 10% '
              'overconsumption. Labour took 5,200 hours against a 5,000-hour standard, and the '
              'variable overhead efficiency variance follows automatically from those same extra '
              '200 hours. A cheaper, poorer grade of Alumina that scrapped more and worked '
              'harder explains all four at once, and the net effect is a ¢2.83 million loss '
              'against a ¢1.2 million purchasing "saving".'}]}},

    {'eg': {'tag': 'Exam type — Q13.8 (20 marks)',
      't': 'The relevance of five variances to management, and why variances are interrelated',
      'q': [
      {'p': '**(a)** Discuss the relevance to management of the following variances, and for '
            'each variance give a specific example of how it could arise: (i) direct material '
            'usage variance; (ii) direct material price variance; (iii) direct wages cost '
            'variance; (iv) direct labour efficiency variance; (v) fixed production overhead '
            'expenditure variance *(15 marks)*.'},
      {'p': '**(b)** Briefly explain the statement that "in standard costing systems, variances '
            'are interrelated and should not be considered in isolation" *(5 marks)*.'}],
      'a': [
      {'h4': '(a)(i)  Direct material usage variance'},
      {'p': '**Relevance:** it measures whether **more or less material was consumed than the '
            'output should have required**, valued at standard price so that price movements do '
            'not contaminate it. It is the responsibility of the **production manager**, and it '
            'is the primary indicator of material efficiency — scrap, waste, spoilage, rework '
            'and pilferage all show up here. It directs attention to the shop floor, to material '
            'quality and to the adequacy of the standard specification.'},
      {'p': '**Specific example:** a batch of timber of a lower grade than specified contains '
            'more knots, so 110 planks are consumed to produce the 100 table tops the standard '
            'allows for — a 10-plank adverse usage variance at the standard price per plank.'},
      {'h4': '(a)(ii)  Direct material price variance'},
      {'p': '**Relevance:** it measures whether material was **bought above or below the '
            'standard price**, and is the responsibility of the **purchasing manager**. It '
            'assesses buying performance, signals changes in market conditions, and warns when '
            'the standard price itself has become out of date. It must be read alongside the '
            'usage variance, because a favourable price often buys an adverse usage.'},
      {'p': '**Specific example:** the buyer accepts a supplier\'s offer of a 5% discount for '
            'taking a full container-load instead of the usual pallet, producing a favourable '
            'price variance — though it also increases inventory holding cost and, if the '
            'material deteriorates, the usage variance too.'},
      {'h4': '(a)(iii)  Direct wages cost variance'},
      {'p': '**Relevance:** it is the **total** labour variance — the difference between the '
            'standard labour cost of the actual output and the wages actually paid. On its own '
            'it tells management only the overall size of the labour problem, which is why it is '
            'always **analysed into its rate and efficiency components** before anything can be '
            'done about it: the rate element belongs to personnel and to wage negotiation, the '
            'efficiency element to production.'},
      {'p': '**Specific example:** a month in which a negotiated 6% wage award (adverse rate '
            'variance) coincides with the new machinery finally running at speed (favourable '
            'efficiency variance) may show a small total wages variance that conceals two large '
            'and quite separate movements.'},
      {'h4': '(a)(iv)  Direct labour efficiency variance'},
      {'p': '**Relevance:** it measures whether the output took **more or fewer hours than the '
            'standard allows**, valued at the standard rate so that wage-rate changes do not '
            'contaminate it. It is the responsibility of the **production manager** and is the '
            'main measure of labour productivity. Because variable overhead is usually absorbed '
            'on labour hours, it also drives the variable overhead efficiency variance, and '
            'under absorption costing the fixed overhead efficiency variance as well.'},
      {'p': '**Specific example:** three experienced operators leave and are replaced by '
            'trainees, who take 2,200 hours to complete work with a standard time of 2,000 '
            'hours — a 200-hour adverse efficiency variance at the standard rate, with a '
            'matching adverse variable overhead efficiency variance behind it.'},
      {'h4': '(a)(v)  Fixed production overhead expenditure variance'},
      {'p': '**Relevance:** it measures the difference between the **budgeted** fixed production '
            'overhead and the **actual** amount spent, and is therefore a pure **spending** '
            'measure, unaffected by the level of activity. It is the responsibility of the '
            'managers who control the individual overhead items, and it is the only fixed '
            'overhead variance that reflects controllable spending — the volume variance '
            'reflects only activity. A useful answer notes that it is best analysed further by '
            'individual cost item (rent, insurance, supervision, depreciation), since the total '
            'alone identifies nothing actionable.'},
      {'p': '**Specific example:** the factory\'s insurance premium is renewed at ¢4.2 million '
            'against the ¢3.8 million budgeted after a claim in the previous year — a ¢400,000 '
            'adverse fixed overhead expenditure variance that has nothing to do with the level '
            'of production.'},
      {'h4': '(b)  Why variances are interrelated and must not be considered in isolation'},
      {'p': 'A variance identifies **where** a difference arose, not **why**. Very often a '
            'single decision or event produces several variances at once, in opposite '
            'directions, and judging any one of them alone leads to the wrong conclusion — and '
            'sometimes to blaming the wrong manager. Common interrelationships:'},
      {'ol': [
        '**Material price and material usage.** Buying a cheaper, inferior material gives a '
        'favourable price variance and an adverse usage variance — and often an adverse labour '
        'efficiency variance too, because the poorer material is harder to work. Praising the '
        'buyer for the price saving would be exactly wrong if the net effect is a loss.',
        '**Labour rate and labour efficiency.** Employing a higher grade of labour than standard '
        'gives an adverse rate variance but a favourable efficiency variance; employing a lower '
        'grade does the reverse. Either may be the better decision overall.',
        '**Labour efficiency and variable (and fixed) overhead efficiency.** Where overhead is '
        'absorbed on labour hours, every adverse labour efficiency variance mechanically '
        'produces an adverse overhead efficiency variance. The second is not independent '
        'evidence of anything.',
        '**Sales price and sales volume.** Cutting the selling price gives an adverse price '
        'variance and, if the cut works, a favourable volume variance.',
        '**Material price and inventory decisions.** Bulk buying for a favourable price variance '
        'raises holding costs, obsolescence risk and the capital tied up — none of which appear '
        'as a variance at all.',
        '**Maintenance expenditure and efficiency.** Cutting planned maintenance gives a '
        'favourable fixed overhead expenditure variance this month and adverse labour and '
        'overhead efficiency variances, from breakdowns, in later months.',
      ]},
      {'key': 'The practical rule follows directly: **investigate variances in related groups, '
              'look for a single cause behind several of them, and judge the decision by its '
              'net effect on profit** rather than by any individual variance. It also follows '
              'that a manager should not be held responsible for a variance that another '
              'manager\'s decision caused — which is the controllability principle applied to '
              'variance analysis.'}]}},

    {'eg': {'tag': 'Exam type — Q13.9 (12½ marks)',
      't': 'TYT — defining standard costing, and the fixed overhead variances',
      'q': [
      {'p': '**(a)** Define standard costing *(1 mark)*.'},
      {'p': '**(b)** Mention the variance that is attributed to under- and over-absorption, and '
            'interpret the meaning of under-absorption *(3½ marks)*.'},
      {'p': '**(c)** TYT uses the standard costing technique for determining its operational '
            'performance. The firm uses an overhead absorption rate to estimate its overhead '
            'costs. Relevant data provided are as follows:'},
      {'stmt': {'t': 'Budgeted figures', 'rows': [
        ['Output', '', '10,000 units'],
        ['Production hours to utilise', '', '20,000 hours'],
        ['Fixed production overhead', '', 'N40,000'],
      ]}},
      {'p': '**Actual figures achieved:** *(see the note below — none are printed in the study '
            'text)*'},
      {'p': '**Required:** **(a)** compute variances for (i) the fixed overhead cost variance; '
            '(ii) the components of the fixed overhead cost variance. **(b)** Interpret the '
            'variance that identifies under- and over-absorption *(8 marks)*.'},
      {'warn': 'The study text prints the heading **"Actual figures achieved"** followed by '
               '**nothing at all** — no output, no hours and no actual overhead. (Page 410 of '
               'the PDF was rendered and inspected directly; the space below the heading is '
               'blank.) Part (c) therefore **cannot be answered as printed**. Parts (a) and (b) '
               'are answered in full below, the method for (c) is set out, and a plausible set '
               'of actual figures is then supplied — **clearly marked as supplied, not as the '
               'examiner\'s** — so the computation can be demonstrated end to end.',
       'lbl': 'Data missing from the study text'}],
      'a': [
      {'h4': '(a)  Definition of standard costing'},
      {'def': {'t': 'Standard costing', 'd': 'a costing technique in which **predetermined '
                    '(standard) costs** are established for each unit of output, actual costs '
                    'are compared with those standards, and the differences — **variances** — '
                    'are analysed by cause and reported to management for investigation and '
                    'corrective action.'}},
      {'h4': '(b)  The variance attributed to under- and over-absorption'},
      {'p': 'It is the **fixed production overhead (total) variance** — the difference between '
            'the fixed overhead **absorbed** into production at the standard rate and the fixed '
            'overhead **actually incurred**. It is identical to the under- or over-absorption of '
            'fixed overhead described in §5.7.'},
      {'tex': '\\text{Fixed overhead total variance} = \\text{Fixed overhead absorbed} - '
              '\\text{Actual fixed overhead incurred}'},
      {'p': '**Interpreting under-absorption:** fixed overhead is **under-absorbed** when the '
            'amount charged to production at the predetermined rate is **less than the amount '
            'actually spent**. It appears as an **adverse** fixed overhead total variance and is '
            'written off as an **additional expense** in the costing profit and loss account, '
            'reducing profit. It has exactly two possible causes, which the two components '
            'separate:'},
      {'ul': [
        '**actual expenditure exceeded the budget** — the expenditure variance; and/or',
        '**actual activity fell below the level on which the absorption rate was built**, so '
        'there were too few units or hours to carry the overhead — the volume variance.',
      ]},
      {'h4': '(c)  The method, and the standard overhead rate'},
      {'stmt': {'t': 'Standard fixed overhead absorption rates', 'rows': [
        ['Budgeted fixed production overhead', '', 'N40,000'],
        ['÷ budgeted production hours', '', '20,000 hours'],
        ['**Standard fixed overhead absorption rate**', '', '**N2.00 per hour**', '@t'],
        '@gap',
        ['Budgeted hours per unit  (20,000 hours ÷ 10,000 units)', '', '2 hours per unit'],
        ['**Standard fixed overhead per unit**  (2 hours × N2.00)', '', '**N4.00 per unit**',
         '@t'],
      ]}},
      {'fbox': {'h': 'Fixed production overhead variances', 'rows': [
        {'lb': 'Total (under/over absorption)',
         'tex': '(\\text{Actual output} \\times \\text{Std FOH per unit}) - '
                '\\text{Actual FOH incurred}'},
        {'lb': 'Expenditure variance',
         'tex': '\\text{Budgeted FOH} - \\text{Actual FOH incurred}'},
        {'lb': 'Volume variance',
         'tex': '(\\text{Actual output} - \\text{Budgeted output}) \\times '
                '\\text{Std FOH per unit}'},
        {'lb': 'Volume — capacity component',
         'tex': '(\\text{Actual hours} - \\text{Budgeted hours}) \\times '
                '\\text{Std FOH rate per hour}'},
        {'lb': 'Volume — efficiency component',
         'tex': '(\\text{Std hours for actual output} - \\text{Actual hours}) \\times '
                '\\text{Std FOH rate per hour}'},
      ]}},
      {'h4': '(c)  Worked demonstration on supplied actual figures'},
      {'note': 'The figures below are **supplied for demonstration only** — they are not in the '
               'study text. Assume: **actual output 9,000 units; actual hours worked 19,000; '
               'actual fixed production overhead N42,000.**'},
      {'stmt': {'t': 'Fixed overhead variances on the supplied figures (N)', 'rows': [
        ['Fixed overhead absorbed  (9,000 units × N4.00)', '', 36000],
        ['Actual fixed overhead incurred', '', 42000],
        ['**(i) Fixed overhead cost variance (under-absorption)**', '',
         '6,000  **ADVERSE**', '@t'],
        '@gap',
        ['**(ii) Components**', '', '', '@hd'],
        ['**Expenditure variance**  budgeted N40,000 − actual N42,000', '',
         '2,000  **ADVERSE**'],
        ['**Volume variance**  (9,000 − 10,000 units) × N4.00', '', '4,000  **ADVERSE**'],
        ['**Total**', '', '6,000  A', '@tt'],
        '@gap',
        ['*Volume — capacity component*  (19,000 − 20,000 hours) × N2.00', '',
         '*2,000  ADVERSE*'],
        ['*Volume — efficiency component*  (18,000 std hrs − 19,000 actual hrs) × N2.00', '',
         '*2,000  ADVERSE*'],
      ]}},
      {'h4': '(c)(b)  Interpretation'},
      {'p': 'The **N6,000 adverse fixed overhead cost variance is the under-absorption**, and '
            'the components explain it:'},
      {'ol': [
        '**N2,000 is an expenditure overspend** — N42,000 was spent against a N40,000 budget. '
        'This is the controllable element, and the managers responsible for the individual '
        'overhead items should explain it.',
        '**N4,000 is a volume shortfall** — only 9,000 units were produced against the 10,000 on '
        'which the N4 per unit rate was built, so 1,000 units\' worth of overhead was never '
        'charged to production. Splitting it further, **N2,000 is capacity** (1,000 fewer hours '
        'were worked than budgeted — the factory was open for less time) and **N2,000 is '
        'efficiency** (the 9,000 units should have taken 18,000 hours but took 19,000).',
      ]},
      {'p': 'The whole N6,000 is written off as an **additional expense** in the costing profit '
            'and loss account. Had output exceeded 10,000 units and spending come in under '
            'N40,000, the variance would have been favourable and the overhead **over-absorbed**, '
            'with the excess credited to profit.'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Material Cost Variance', 'tex': '(SQ \\times SP) - (AQ \\times AP)'},
  {'lb': 'Material Price Variance', 'tex': 'AQ \\times (SP - AP)'},
  {'lb': 'Material Usage Variance', 'tex': 'SP \\times (SQ - AQ)'},
  {'lb': 'Labour Cost Variance', 'tex': '(SH \\times SR) - (AH \\times AR)'},
  {'lb': 'Labour Rate Variance', 'tex': 'AH \\times (SR - AR)'},
  {'lb': 'Labour Efficiency Variance', 'tex': 'SR \\times (SH - AH)'},
  {'lb': 'Variable Overhead Expenditure Variance', 'tex': '(AH \\times VOR) - \\text{Actual '
   'VOH}'},
  {'lb': 'Fixed Overhead Volume Variance', 'tex': '(SH - \\text{Budgeted hours}) \\times FOAR'},
  {'lb': 'Efficiency ratio', 'tex': '\\dfrac{SH}{AH} \\times 100'},
  {'lb': 'Activity ratio', 'tex': '\\dfrac{SH}{\\text{Budgeted hours}} \\times 100'},
  {'lb': 'Capacity ratio', 'tex': '\\dfrac{AH}{\\text{Budgeted hours}} \\times 100'},
 ],
 'focus':
   'Standard costing variance analysis is consistently one of the most heavily-weighted topics '
   'in the whole paper. Learn the variance *tree* (cost variance splits into two sub-variances, '
   'each level reconciling exactly to the one above) as one structure applied identically to '
   'materials, labour, variable overhead and fixed overhead — do not memorise four unrelated '
   'formula sets. Always compute the sub-variances and add them back to confirm they match the '
   'total — this single habit catches almost every arithmetic slip before it reaches the '
   'answer. For sales margin variances, remember marginal costing uses contribution margin '
   'throughout; absorption costing uses full profit margin, including a share of fixed overhead.',
 'errors': [
   'Mixing up SQ (standard quantity for the *actual* output achieved) with the *budgeted* '
   'quantity — every variance in this chapter is based on actual output, never budgeted output.',
   'Getting the sign convention backwards on a variance — a rise in cost/rate/usage above '
   'standard is Adverse; a fall below standard is Favourable, and mixing this up flips every '
   'downstream reconciliation.',
   'Forgetting that under marginal costing, only the fixed overhead *expenditure* variance '
   'belongs in a profit reconciliation — fixed overhead volume variance has no meaning once '
   'fixed cost is treated as a period cost, not absorbed into units.',
   'Using budgeted hours instead of actual hours (or vice versa) in the wrong ratio formula — '
   'efficiency uses actual hours in the denominator; activity and capacity both use budgeted '
   'hours.',
   'Reporting a variance total without cross-checking that its own sub-variances actually sum '
   'to it — the single most reliable way to catch a sign or arithmetic error in this topic.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Standard quantity for a product is 4kg at ¢500/kg. Actual usage was 4,500kg for '
         '1,000 units produced, at an actual price of ¢520/kg. The material usage variance is',
    'o': ['250,000 Favourable', '250,000 Adverse', '90,000 Adverse', '90,000 Favourable',
          '500,000 Adverse'],
    'a': 1,
    'w': 'Standard quantity for 1,000 units = 4,000kg. Usage variance = SP × (SQ − AQ) = 500 × '
         '(4,000 − 4,500) = −250,000, i.e. 250,000 Adverse.',
    'calc': '500 \\times (4{,}000 - 4{,}500) = -250{,}000',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'Standard labour rate is ¢2,000/hour. 5,000 hours were actually worked at a total cost '
         'of ¢11,000,000. The labour rate variance is',
    'o': ['1,000,000 Adverse', '1,000,000 Favourable', '10,000,000 Adverse', '9,000,000 '
          'Favourable', '2,000,000 Adverse'],
    'a': 0,
    'w': 'Actual rate = 11,000,000/5,000 = ¢2,200/hr. Rate variance = AH × (SR − AR) = 5,000 × '
         '(2,000 − 2,200) = −1,000,000, i.e. 1,000,000 Adverse.',
    'calc': '5{,}000 \\times (2{,}000 - 2{,}200) = -1{,}000{,}000',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'A material price variance of ¢50,000 Favourable and a material usage variance of '
         '¢80,000 Adverse together give a material cost variance of',
    'o': ['130,000 Adverse', '30,000 Adverse', '30,000 Favourable', '130,000 Favourable',
          '50,000 Adverse'],
    'a': 1,
    'w': 'Cost variance = Price variance + Usage variance = 50,000 F − 80,000 A = −30,000, i.e. '
         '30,000 Adverse.',
    'calc': '50{,}000 - 80{,}000 = -30{,}000',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'The fixed overhead volume variance measures',
    'o': ['the difference between actual and budgeted spending on fixed overheads',
          'the over- or under-absorption of overhead caused by actual output differing from '
          'budgeted output', 'the difference between standard and actual labour rates',
          'the material price variance only', 'a variance that only arises under marginal '
          'costing'],
    'a': 1,
    'w': 'Per CIMA\'s own definition, quoted in the chapter, the volume variance measures over-'
         'or under-absorption of overhead caused by actual production volume differing from '
         'the budget — spending itself is captured separately by the expenditure variance.',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'Under a standard MARGINAL costing system, which fixed overhead variance is used in '
         'reconciling budgeted profit to actual profit?',
    'o': ['Only the volume variance', 'Only the capacity variance',
          'Only the expenditure variance', 'All of expenditure, volume, efficiency and capacity',
          'None — fixed overhead variances are never used under marginal costing'],
    'a': 2,
    'w': 'Under marginal costing, fixed cost is a period cost (never absorbed into units), so '
         'only the fixed overhead expenditure variance is meaningful for the reconciliation — '
         'volume (and its sub-variances) only make sense under absorption costing.',
    'src': 'Chapter 13.5', 'sec': '13.5'},
   {'q': 'Budgeted hours are 50,000, standard hours for actual output are 44,000, and actual '
         'hours worked are 40,000. The efficiency ratio is',
    'o': ['88%', '80%', '110%', '90.9%', '113.6%'],
    'a': 2,
    'w': 'Efficiency ratio = SH/AH × 100 = 44,000/40,000 × 100 = 110%.',
    'calc': '\\dfrac{44{,}000}{40{,}000} \\times 100 = 110\\%',
    'src': 'Chapter 13.6', 'sec': '13.6'},
   {'q': 'Using the same data (budgeted 50,000hrs, standard 44,000hrs, actual 40,000hrs), the '
         'activity ratio is',
    'o': ['110%', '80%', '88%', '90.9%', '125%'],
    'a': 2,
    'w': 'Activity ratio = SH/Budgeted hours × 100 = 44,000/50,000 × 100 = 88%.',
    'calc': '\\dfrac{44{,}000}{50{,}000} \\times 100 = 88\\%',
    'src': 'Chapter 13.6', 'sec': '13.6'},
   {'q': 'A standard is set for use over a long period, remaining unchanged over several years, '
         'and is used mainly to show long-term trends rather than to highlight current '
         'efficiency. This describes a',
    'o': ['current standard', 'ideal standard', 'attainable standard', 'basic standard',
          'flexible standard'],
    'a': 3,
    'w': 'A basic standard is set for long-term use, remaining unchanged over several years — '
         'useful for showing trends, but explicitly not able to highlight current efficiency or '
         'inefficiency.',
    'src': 'Chapter 13.1', 'sec': '13.1'},
   {'q': 'Which factor makes a variance MORE likely to be investigated, all else equal?',
    'o': ['It recurs very frequently, following a well-known pattern',
          'It is immaterial in size', 'It is unusual and has not been seen before',
          'The standard it is measured against is known to be unreliable',
          'The cost of investigating clearly exceeds the benefit'],
    'a': 2,
    'w': 'An unusual, non-recurring variance is more likely to be investigated than one with a '
         'frequent, well-understood history — the opposite of options A, B, D and E, each of '
         'which points toward *not* investigating.',
    'src': 'Chapter 13.7', 'sec': '13.7'},
  ],
  'theory': [
   {'q': 'What is a variance? Identify and discuss briefly the two basic causes of variances.',
    'marks': 6,
    'a': [
      {'p': 'A variance is the difference between the standard level of performance that ought '
            'to have been achieved under given working conditions, and the actual level '
            'achieved for that same output.'},
      {'p': '**Two basic causes**: (i) using more or less quantity of material or labour hours '
            'per unit of output than expected — from using superior/inferior inputs, or more/'
            'less efficient use of them; and (ii) paying a higher or lower rate per unit of '
            'material or labour than expected — influenced by input quality and market '
            'conditions.'},
    ], 'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'Outline the factors that should be considered when deciding whether or not to '
         'investigate variances revealed in a standard costing and budgetary control system.',
    'marks': 5,
    'a': [
      {'ol': [
        'the **history** of the variance — a recurring, well-understood deviation is less '
        'likely to need investigation than an unusual one;',
        'the **reliability of the standard** — a more reliable standard raises the chance any '
        'deviation from it is worth investigating;',
        'the **significance (materiality)** of the deviation — immaterial variances are less '
        'likely to be investigated;',
        'a **cost-benefit** comparison — investigate only where the benefit exceeds the cost of '
        'investigating; and',
        'the **effect on future planning and control** — even a costly investigation can be '
        'worthwhile if it genuinely improves future operations.',
      ]},
    ], 'src': 'Chapter 13.7', 'sec': '13.7'},
  ]},
}
