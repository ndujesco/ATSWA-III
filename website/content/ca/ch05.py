CH = {
 'n': 5,
 't': 'Elements of Cost: Overheads',
 'brief': 'The third and most complex element of cost: what overheads are, how they are '
          'classified, the allocation/apportionment/absorption sequence that gets an overhead '
          'from the general ledger onto a cost unit, the three methods for re-apportioning '
          'reciprocal service-centre costs, the six bases for calculating an overhead absorption '
          'rate, why predetermined rates are used, the treatment of over- and under-absorbed '
          'overhead, and Activity-Based Costing as the modern alternative to a single blanket rate.',
 'outcomes': [
   'Define overheads and identify the various ways of classifying overheads',
   'Distinguish between overheads allocation, overheads apportionment and overheads absorption',
   'Use the overheads analysis sheet to allocate and apportion overheads to cost centres',
   'Calculate overheads absorption rates using six methods',
   'Explain why predetermined overheads absorption rates are often used',
   'Explain the reasons for preferring departmental to blanket overhead absorption rates',
   'Calculate and explain the alternative treatments of overhead under- and over-absorption',
   'Make accounting entries with respect to overheads',
 ],
 'secs': [
  {'n': '5.1', 't': 'Introduction and definition', 'b': [
    {'def': {'t': 'Overheads', 'd': 'the aggregate of indirect materials, indirect labour and '
                  'indirect expenses.'}},
    {'p': 'Overheads matter a great deal in cost accounting: they are made up of three separate '
          'cost elements (materials, labour, expenses), making their determination and control '
          'complex and challenging, and in many organisations the overhead component of total '
          'cost is significant — demanding careful analysis, monitoring and control to minimise '
          'total cost and maximise profitability.'},
    {'p': 'Typical items making up overhead cost: cleaning materials, stationery, consumable '
          'materials, supervision cost, employee bonuses, indirect workers\' salaries, lighting '
          'and heating, rent and rates, insurance premiums, and depreciation of fixed assets. '
          'The objective of determining overhead cost is (a) to enable it to be absorbed by '
          'products, and (b) to provide useful information for management decision making and '
          'cost control.'},
  ]},

  {'n': '5.2', 't': 'Types and classification of overheads', 'b': [
    {'p': 'Overheads classify by function into four groups (already introduced in Chapter 2 '
          '§2.1(c), repeated here in overheads\' own terms):'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning'], 'rows': [
      ['**Production overheads**', 'The indirect costs of manufacturing a cost unit — indirect '
       'materials consumed in the factory, indirect factory wages, and other indirect expenses '
       'connected with production.'],
      ['**Administrative overheads**', 'Costs of formulating policy and directing/controlling '
       'operations, not directly related to production, selling, distribution or R&D.'],
      ['**Marketing, selling and distribution overheads**', 'Costs of securing orders, '
       'publicising and presenting products attractively at acceptable prices, delivering goods '
       'to customers, and after-sales service.'],
      ['**Research and development overheads**', 'Costs of seeking new ideas, materials, '
       'production methods and improved products, and designing them for formal production.'],
    ]}},
    {'p': 'Overheads can equally be analysed by **element** (indirect materials, indirect '
          'labour, indirect expenses — Chapter 1 §1.3) or by **behaviour** (fixed or variable — '
          'Chapter 2 §2.1(d)).'},
    {'key': 'Because overheads by their nature cannot be assigned to any one specific cost unit, '
            'charging them to products requires a three-stage sequence: **allocation** → '
            '**apportionment** → **absorption**. Every part of this chapter builds on getting '
            'that sequence exactly right.'},
  ]},

  {'n': '5.3', 't': 'Overhead allocation and apportionment', 'b': [
    {'table': {'align': 'll', 'head': ['Term', 'Meaning'], 'rows': [
      ['**Overhead allocation**', 'Assigning overhead directly to a cost centre, with **no '
       'sharing** — used where a cost is specifically incurred for one particular cost centre '
       'and can be wholly charged to it.'],
      ['**Overhead apportionment**', 'Sharing overhead incurred for a **number of** cost centres '
       '(sometimes the whole organisation) among them, on a fair and equitable basis, because '
       'such costs cannot be allocated to just one.'],
    ]}},
    {'p': 'Common bases of apportionment, matched to the type of overhead they best fit:'},
    {'table': {'align': 'll', 'head': ['Basis', 'Typical overhead it fits'], 'rows': [
      ['**Floor space/area occupied**', 'Rent; rates; heating and lighting; insurance of '
       'buildings.'],
      ['**Kilowatt hours**', 'Electricity; power.'],
      ['**Value of plant and machinery**', 'Depreciation of plant/machinery; insurance of '
       'plant; plant maintenance.'],
      ['**Number of employees**', 'Canteen expenses; supervisors\' wages; personnel department '
       'expenses.'],
      ['**Number of materials requisitions**', 'Stores expenses; indirect material expenses.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 5.1 — a complete overhead analysis sheet',
      'open': True, 'q': [
      {'p': 'Apple Ltd makes wooden crates (40,000 made in the year), through three production '
            'departments (Sawing, Assembly, Finishing) and two service departments (Maintenance, '
            'Materials Handling).'},
      {'table': {'align': 'lrrr', 'head': ['', 'Sawing (₵)', 'Assembly (₵)', 'Finishing (₵)'],
        'rows': [
        ['Materials issued', '800,000', '600,000', '100,000'],
        ['Direct wages', '300,000', '150,000', '250,000'],
        ['Overheads', '120,000', '80,000', '30,000'],
      ]}},
      {'p': 'Materials handling wages ₵21,000; maintenance wages ₵45,000; consumable stores '
            '₵15,000 (all maintenance). Service-department benefit percentages:'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Sawing', 'Assembly', 'Finishing',
        'Mat. Handling'], 'rows': [
        ['Maintenance', '30%', '40%', '20%', '10%'],
        ['Materials Handling', '50%', '20%', '30%', '—'],
      ]}},
      {'p': 'Required: (a) the overheads allotted to each production department; (b) the unit '
            'cost of a wooden crate.'}],
      'a': [
      {'table': {'align': 'lrrrrr', 'head': ['', 'Sawing', 'Assembly', 'Finishing',
        'Maintenance', 'Mat. Handling'], 'rows': [
        ['Overheads', '120,000', '80,000', '30,000', '45,000', '21,000'],
        ['Consumables', '—', '—', '—', '15,000', '—'],
        ['Subtotal', '120,000', '80,000', '30,000', '60,000', '21,000'],
        ['Apportion Maintenance (30:40:20:10)', '18,000', '24,000', '12,000', '(60,000)',
         '6,000'],
        ['Apportion Mat. Handling (50:20:30)', '13,500', '5,400', '8,100', '—', '(27,000)'],
        ['**Overheads to production depts.**', '**151,500**', '**109,400**', '**50,100**', 'Nil',
         'Nil'],
      ]}},
      {'p': '**(b) Unit cost**:'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Sawing', 'Assembly', 'Finishing', 'Total'],
        'rows': [
        ['Material cost', '800,000', '600,000', '100,000', '1,500,000'],
        ['Direct wages', '300,000', '150,000', '250,000', '700,000'],
        ['Overheads', '151,500', '109,400', '50,100', '311,000'],
        ['**Total cost**', '', '', '', '**2,511,000**'],
      ]}},
      {'tex': '\\text{Unit cost per crate} = \\dfrac{2{,}511{,}000}{40{,}000} = ₵62.78'}]}},
  ]},

  {'n': '5.4', 't': 'Re-apportioning reciprocal service-centre overheads', 'b': [
    {'p': 'Cost units are only produced in **production** cost centres, so a service centre\'s '
          'overhead must be re-apportioned into production cost centres before it can be '
          'absorbed. Where service centres do **not** serve each other, this is simple: '
          're-apportion the service centre that serves the *most* other centres first, then '
          'repeat — once a centre\'s overhead is re-apportioned, it never receives any more.'},
    {'warn': 'Where service centres **do** serve each other (**reciprocal service** — e.g. '
             'Maintenance services Administration and Administration services Maintenance back), '
             'that simple one-pass approach breaks down, and one of three dedicated methods is '
             'needed: **elimination**, **continuous allotment**, or **simultaneous equations**.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 5.2 — the shared data for all three '
      'reciprocal-service methods', 'open': True, 'q': [
      {'p': 'Lamina Manufacturing Company: four production departments (Grinding, Blending, '
            'Firing, Polishing) and three service departments (Personnel, Administration, '
            'Maintenance).'},
      {'table': {'align': 'lrrrrrrr', 'head': ['₵\'000', 'Grinding', 'Blending', 'Firing',
        'Polishing', 'Personnel', 'Admin.', 'Maint.'], 'rows': [
        ['Indirect labour', '4,600', '3,300', '5,400', '2,900', '700', '1,800', '800'],
        ['Other indirect costs', '1,400', '1,200', '2,800', '1,600', '500', '300', '1,200'],
      ]}},
      {'p': 'Service-department costs are re-apportioned by these percentages:'},
      {'table': {'align': 'lrrrrrr', 'head': ['', 'Grinding', 'Blending', 'Firing', 'Polishing',
        'Admin.', 'Maint.'], 'rows': [
        ['Personnel', '15%', '25%', '30%', '20%', '5%', '5%'],
        ['Administration', '10%', '30%', '40%', '15%', '—', '5%'],
        ['Maintenance', '15%', '30%', '40%', '5%', '10%', '—'],
      ]}},
      {'p': 'Grinding and Firing absorb overhead per machine hour (budgeted 620 and 520 hours '
            'respectively); Blending and Polishing absorb per direct labour hour (budgeted '
            '1,050 and 450 hours respectively). Required: total overheads for each production '
            'cost centre, and the overhead absorption rate for each.'}],
      'a': [{'p': 'Worked in full below, by all three methods — the study text uses this one '
                  'dataset throughout to show that they converge on (almost) the same answer.'}]}},

    {'h4': 'Method 1 — Elimination'},
    {'p': 'Once a service centre\'s overhead has been re-apportioned, that centre is '
          '**eliminated** from every later re-apportionment. Order of elimination: the service '
          'centre receiving service from **no other** service centre goes first (here, '
          'Personnel — nothing flows *into* Personnel from Administration or Maintenance); then '
          'the centre receiving the **least** from the remaining service centres.'},
    {'table': {'align': 'lrrrrrrr', 'head': ['₵\'000', 'Grinding', 'Blending', 'Firing',
      'Polishing', 'Personnel', 'Admin.', 'Maint.'], 'rows': [
      ['Subtotal (labour + other)', '6,000', '4,500', '8,200', '4,500', '1,200', '2,100',
       '2,000'],
      ['Personnel (15:25:30:20:—:5:5)', '180', '300', '360', '240', '(1,200)', '60', '60'],
      ['Maintenance, now 2,060 (15:30:40:5:—:10:—)', '309', '618', '824', '103', '—', '206',
       '(2,060)'],
      ['Admin., now 2,366 — re-normalised over the 4 open production centres only '
       '(10:30:40:15, scaled to sum to 100)', '249', '747', '996', '374', '—', '(2,366)', '—'],
      ['**Overheads to production centres**', '**6,738**', '**6,165**', '**10,380**', '**5,217**',
       'Nil', 'Nil', 'Nil'],
    ]}},
    {'key': 'The subtlety that trips people up: by the time **Administration**\'s turn comes, '
            '**Maintenance** has already been closed — but Administration\'s own percentages '
            '(10:30:40:15:—:5, with that last 5% meant for Maintenance) still add up to 100% '
            'only including Maintenance. Since Maintenance can no longer receive anything, '
            'Administration\'s remaining ₵2,366 is re-apportioned **only** across the four still-'
            'open production centres, using the *same relative weights* (10:30:40:15) scaled up '
            'to sum to 100% instead of 95% — e.g. Grinding\'s true share becomes '
            '$10/95 = 10.53\\%$ of ₵2,366, not $10\\%$. Always check whether a closed-out '
            'centre\'s share needs re-normalising this way once a reciprocal partner is already '
            'gone.'},

    {'h4': 'Method 2 — Continuous allotment (repeated distribution)'},
    {'p': 'Every service centre keeps re-apportioning its overhead to the *other* service '
          'centres as well as the production centres, in repeated passes, until the residual '
          'amount left to redistribute becomes **insignificant** — at which point it is simply '
          'ignored. Reciprocal centres therefore feed each other small, shrinking amounts over '
          'several rounds rather than being closed off after one pass. Every row below uses the '
          'same percentages given in the base data (Personnel 15:25:30:20:—:5:5; Maintenance '
          '15:30:40:5:—:10 [to Admin]; Administration 10:30:40:15:—:5 [to Maint]) applied each '
          'time to whatever balance is currently sitting in that service centre:'},
    {'table': {'align': 'lrrrrrrr', 'head': ['₵\'000', 'Grinding', 'Blending', 'Firing',
      'Polishing', 'Personnel', 'Admin.', 'Maint.'], 'rows': [
      ['Indirect labour (allocated)', '4,600', '3,300', '5,400', '2,900', '700', '1,800', '800'],
      ['Other indirect costs (allocated)', '1,400', '1,200', '2,800', '1,600', '500', '300',
       '1,200'],
      ['Subtotal', '6,000', '4,500', '8,200', '4,500', '1,200', '2,100', '2,000'],
      ['Round 1 — Personnel\'s 1,200 (15:25:30:20:—:5:5)', '180', '300', '360', '240', '(1,200)',
       '60', '60'],
      ['Round 2 — Maintenance\'s 2,060 [2,000+60] (15:30:40:5:—:10)', '309', '618', '824', '103',
       '—', '206', '(2,060)'],
      ['Round 3 — Admin\'s 2,366 [2,100+60+206] (10:30:40:15:—:5)', '237', '710', '947', '354',
       '—', '(2,366)', '118'],
      ['Round 4 — Maintenance\'s 118 (15:30:40:5:—:10)', '18', '35', '47', '6', '—', '12', '(118)'],
      ['Round 5 — Admin\'s 12 (10:30:40:15:—:5)', '1', '4', '5', '2', '—', '(12)', '1'],
      ['Residual left in Maintenance (≈1) — small enough to ignore', '—', '—', '—', '—', '—',
       '—', 'Nil'],
      ['**Overheads to production centres**', '**6,745**', '**6,167**', '**10,383**', '**5,205**',
       'Nil', 'Nil', 'Nil'],
    ]}},
    {'key': 'Personnel is distributed first and never receives anything back, because nothing in '
            'the data flows *into* Personnel — only Maintenance and Administration feed each '
            'other back and forth, in shrinking amounts (2,060 → 118 → 12 → ≈1), which is exactly '
            'the "continuous" part of this method\'s name. Each production centre\'s final total '
            'is simply its subtotal plus every round\'s contribution to it, e.g. Grinding '
            '$= 6{,}000+180+309+237+18+1 = 6{,}745$.'},

    {'h4': 'Method 3 — Simultaneous equations'},
    {'p': 'The total overhead ultimately carried by each service centre (including what it '
          'receives back from the others) is treated as an unknown, and the reciprocal '
          'relationships are solved as a system of equations. Letting $P$, $A$, $M$ be the '
          'total (self-incurred plus received) overhead of Personnel, Administration and '
          'Maintenance — each built from that centre\'s own subtotal, plus its *share* of '
          'whatever the other two service centres pass to it, using the same base-data '
          'percentages as before (Personnel passes 5% of $P$ to Admin and 5% to Maintenance; '
          'Maintenance passes 10% of $M$ to Admin; Administration passes 5% of $A$ to '
          'Maintenance):'},
    {'tex': 'P = 1{,}200 \\qquad A = 2{,}100 + 0.05P + 0.10M \\qquad M = 2{,}000 + 0.05P + 0.05A'},
    {'p': '**Step 1 — substitute $P=1{,}200$ into both remaining equations:**'},
    {'tex': 'A = 2{,}100 + 0.05(1{,}200) + 0.10M = 2{,}160 + 0.10M \\quad\\text{...(1)}'},
    {'tex': 'M = 2{,}000 + 0.05(1{,}200) + 0.05A = 2{,}060 + 0.05A \\quad\\text{...(2)}'},
    {'p': '**Step 2 — substitute (2) into (1)**, so everything is in terms of $A$ alone:'},
    {'tex': 'A = 2{,}160 + 0.10(2{,}060 + 0.05A) = 2{,}160 + 206 + 0.005A = 2{,}366 + 0.005A'},
    {'p': '**Step 3 — collect the $A$ terms and solve:**'},
    {'tex': 'A - 0.005A = 2{,}366 \\quad\\Rightarrow\\quad 0.995A = 2{,}366 \\quad\\Rightarrow'
            '\\quad A = \\dfrac{2{,}366}{0.995} = ₵2{,}377.89\\text{ thousand}'},
    {'p': '**Step 4 — substitute $A$ back into (2)** to find $M$:'},
    {'tex': 'M = 2{,}060 + 0.05(2{,}377.89) = 2{,}060 + 118.89 = ₵2{,}178.89\\text{ thousand}'},
    {'p': 'So $P=1{,}200$, $A\\approx 2{,}377.89$, $M\\approx 2{,}178.89$ (all in ₵\'000). '
          '**Step 5 — redistribute each of these three totals out to the four production '
          'centres**, one more time, using each service centre\'s own fixed percentage split '
          '(Personnel 15:25:30:20:—:5:5; Administration 10:30:40:15:—:—:5; Maintenance '
          '15:30:40:5:—:10:—, for Grinding:Blending:Firing:Polishing:self:Admin:Maintenance in '
          'that order):'},
    {'table': {'align': 'lrrrr', 'head': ['₵\'000', 'Grinding', 'Blending', 'Firing',
      'Polishing'], 'rows': [
      ['Subtotal (from Illustration 5.2\'s own table)', '6,000', '4,500', '8,200', '4,500'],
      ['From Personnel: 15:25:30:20% of $P=1{,}200$', '180.00', '300.00', '360.00', '240.00'],
      ['From Administration: 10:30:40:15% of $A=2{,}377.89$', '237.79', '713.37', '951.16',
       '356.68'],
      ['From Maintenance: 15:30:40:5% of $M=2{,}178.89$', '326.83', '653.67', '871.56', '108.94'],
      ['**Overheads to production centres**', '**6,744.62**', '**6,167.04**', '**10,382.72**',
       '**5,205.62**'],
    ]}},
    {'note': 'Rounded to the nearest ₵\'000, this gives 6,745 / 6,167 / 10,383 / 5,206 — matching '
             'continuous allotment\'s 6,745/6,167/10,383 exactly, with Polishing landing one unit '
             'away (5,206 here against 5,205 there). This is pure rounding noise from carrying '
             '$A$ and $M$ to only 2 decimal places rather than their exact repeating-decimal '
             'values ($A=473{,}200/199$, $M=433{,}600/199$ precisely) — not a sign either method '
             'was done incorrectly, exactly the same kind of small reconciling gap already '
             'flagged for Illustration 8.5\'s rounded unit costs.'},
    {'note': 'Continuous allotment and simultaneous equations reach, to within this rounding '
             'noise, the **same** final answer (6,745/6,167/10,383/≈5,205-6) — a useful cross-'
             'check, since they arrive at it by completely different routes. Elimination gives a '
             'slightly different answer (6,738/6,165/10,380/5,217) because it forces every '
             'service centre fully closed '
             'after one pass, an approximation the other two methods do not make. In an exam, '
             'use whichever method the question asks for — do not mix figures from different '
             'methods in one answer.'},
    {'p': 'The rest of this chapter (overhead absorption rates, over/under absorption) uses the '
          '**elimination method**\'s production-centre totals — ₵6,738,000 (Grinding), '
          '₵6,165,000 (Blending), ₵10,380,000 (Firing), ₵5,217,000 (Polishing).'},
  ]},

  {'n': '5.5', 't': 'Overhead absorption — the six bases', 'b': [
    {'def': {'t': 'Overhead absorption', 'd': 'the process of assigning overhead costs to the '
                  'products or services produced — by first calculating an overhead absorption '
                  'rate (OAR), then applying that rate to determine the overhead absorbed by '
                  'each cost unit.'}},
    {'fbox': {'h': 'Overhead absorption rate (general form)', 'rows': [
      {'lb': 'OAR', 'tex': 'OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted activity '
        'level}}'},
    ]}},
    {'p': 'Six factors are commonly used as "activity level" — each suited to a different kind '
          'of production process:'},
    {'table': {'align': 'lll', 'head': ['Basis', 'Formula', 'Best suited where…'], 'rows': [
      ['**Direct labour hours**', '$OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted '
       'DLH}}$', 'production is labour-intensive and wage rates are stable.'],
      ['**Machine hours**', '$OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted machine '
       'hours}}$', 'production is highly mechanised, so labour hours would be inappropriate.'],
      ['**Units of production**', '$OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted '
       'production units}}$', 'output is uniform in mass quantities — inappropriate for '
       'non-uniform units.'],
      ['**Direct material cost %**', '$OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted '
       'DM cost}} \\times 100$', 'material prices are stable and uniform.'],
      ['**Direct labour cost %**', '$OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted '
       'DL cost}} \\times 100$', 'labour is intensive and wage rates are stable and uniform.'],
      ['**Prime cost %**', '$OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted prime '
       'cost}} \\times 100$', 'rates and prices are relatively stable overall.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 5.2 continued — OAR by direct labour hours '
      'and by machine hours', 'open': True, 'q': [
      {'p': 'Using the elimination-method totals: Blending ₵6,165,000 (1,050 budgeted DLH), '
            'Polishing ₵5,217,000 (450 budgeted DLH); Grinding ₵6,738,000 (620 budgeted machine '
            'hours), Firing ₵10,380,000 (520 budgeted machine hours). Find each OAR.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['', 'Blending', 'Polishing'], 'rows': [
        ['Budgeted overhead', '₵6,165,000', '₵5,217,000'],
        ['Budgeted DLH', '1,050', '450'],
        ['**OAR**', '**₵5,871.43 per DLH**', '**₵11,593.33 per DLH**'],
      ]}},
      {'table': {'align': 'lrr', 'head': ['', 'Grinding', 'Firing'], 'rows': [
        ['Budgeted overhead', '₵6,738,000', '₵10,380,000'],
        ['Budgeted machine hours', '620', '520'],
        ['**OAR**', '**₵10,867.74 per MH**', '**₵19,961.54 per MH**'],
      ]}}]}},

    {'eg': {'tag': 'Study text', 't': 'Illustration 5.3 — direct labour cost % vs total '
      'variable cost %', 'open': True, 'q': [
      {'p': 'Enyo Manufacturing produces Frytol, Brilliant and Pepsodent:'},
      {'table': {'align': 'lrrr', 'head': ['', 'Frytol', 'Brilliant', 'Pepsodent'], 'rows': [
        ['Direct materials', '₵720', '₵1,280', '₵1,800'],
        ['Direct labour, Production dept. (₵60/hr)', '2 hrs', '2.5 hrs', '2 hrs'],
        ['Direct labour, Finishing dept. (₵40/hr)', '2 hrs', '2.5 hrs', '1 hr'],
        ['Variable overhead', '₵80', '₵30', '₵40'],
        ['Planned production', '10,000 units', '20,000 units', '40,000 units'],
      ]}},
      {'p': 'Fixed overhead for the year is budgeted at ₵6,000,000. Find the OAR under (i) '
            'direct labour cost percentage and (ii) percentage of total variable cost.'}],
      'a': [
      {'p': 'Budgeted DLH — Production dept.: $2(10{,}000)+2.5(20{,}000)+2(40{,}000) = '
            '150{,}000$; Finishing dept.: $2(10{,}000)+2.5(20{,}000)+1(40{,}000) = 110{,}000$.'},
      {'p': 'Budgeted direct labour cost $= 150{,}000(60) + 110{,}000(40) = 9{,}000{,}000 + '
            '4{,}400{,}000 = ₵13{,}400{,}000$.'},
      {'p': 'Budgeted material cost $= 720(10{,}000)+1{,}280(20{,}000)+1{,}800(40{,}000) = '
            '₵104{,}800{,}000$. Budgeted variable overhead $= 80(10{,}000)+30(20{,}000)+'
            '40(40{,}000) = ₵3{,}000{,}000$. Budgeted total variable cost $= 104{,}800{,}000 + '
            '13{,}400{,}000 + 3{,}000{,}000 = ₵121{,}200{,}000$.'},
      {'tex': '\\text{(i) OAR} = \\dfrac{6{,}000{,}000}{13{,}400{,}000} \\times 100 \\approx '
              '44.78\\% \\text{ of direct labour cost}'},
      {'tex': '\\text{(ii) OAR} = \\dfrac{6{,}000{,}000}{121{,}200{,}000} \\times 100 \\approx '
              '4.95\\% \\text{ of total variable cost}'}]}},
  ]},

  {'n': '5.6', 't': 'Predetermined rates, and blanket versus departmental rates', 'b': [
    {'h4': 'Why predetermined (budgeted) rates are used'},
    {'ol': [
      'actual overheads are not known until **after** a period ends — without budgeted figures, '
      'product cost cannot be determined promptly; recalculating actual rates as often as '
      'possible would be cumbersome and inconvenient; and',
      'actual overheads are heavily influenced by general price levels, and actual activity '
      'levels fluctuate widely — combined, these would cause large swings in the absorption '
      'rate if it were based on actual figures. Using budgeted overhead and budgeted activity '
      '(which reflect *standards*) reduces the effect of such fluctuations.',
    ]},
    {'h4': 'Blanket versus departmental (cost-centre) rates'},
    {'def': {'t': 'Blanket (factory-wide) overhead recovery rate', 'd': 'a single overhead '
                  'recovery rate applied across the **whole factory**, rather than a separate '
                  'rate per production cost centre.'}},
    {'warn': 'Blanket rates are usually inappropriate: (i) a factory consists of different '
             'production cost centres, and products may consume each centre\'s overheads in '
             'different proportions; (ii) different activity bases drive cost for different '
             'products in different proportions. A single, factory-wide rate hides these '
             'differences and distorts individual product costs.'},
  ]},

  {'n': '5.7', 't': 'Over-absorbed and under-absorbed overhead', 'b': [
    {'tex': '\\text{Overhead absorbed} = \\text{OAR} \\times \\text{Actual quantity of activity '
            'base}'},
    {'p': 'Because the OAR is based on *budgeted* figures while absorption is applied to '
          '*actual* activity, the overhead absorbed rarely equals the overhead actually '
          'incurred — creating **over-absorption** (absorbed exceeds incurred) or **under-'
          'absorption** (incurred exceeds absorbed).'},
    {'h4': 'Treatment of over/under absorption'},
    {'table': {'align': 'll', 'head': ['Treatment', 'Drawback'], 'rows': [
      ['Adjust the under/over recovery into the cost of units produced during the period.',
       'Not usually worthwhile — this historical information is of little use to management.'],
      ['Carry the under/over recovery forward to future accounting periods.', 'Distorts future '
       'performance figures.'],
      ['**Write it off to the Profit and Loss account as a period cost.**', '**This is the most '
       'preferred treatment.**'],
    ]}},
    {'note': 'The treatment of overheads generally can follow either **absorption costing** '
             '(both fixed and variable overhead charged to products) or **marginal costing** '
             '(only variable overhead absorbed into products; fixed overhead treated as a period '
             'cost, charged straight to the P&L account).'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 5.4 — calculating over/under absorption',
      'open': True, 'q': [
      {'p': 'Agape Co. Ltd has two production departments (Machining, Assembling) and one '
            'service department (Maintenance):'},
      {'table': {'align': 'lrrr', 'head': ['₵\'000', 'Machining', 'Assembling', 'Maintenance'],
        'rows': [
        ['Indirect labour', '200', '250', '120'], ['Indirect materials', '420', '450', '500'],
        ['Materials handling', '—', '—', '80'], ['Housekeeping', '50', '70', '100'],
        ['Air conditioning', '30', '30', '50'], ['Rent & rates', '160', '120', '150'],
        ['Supervision', '240', '180', '200'],
      ]}},
      {'p': 'Maintenance is re-apportioned to the two production centres in proportion to their '
            'total expenses. Budgeted overhead: Machining ₵2,000,000 (500,000 planned machine '
            'hours); Assembling ₵1,200,000 (400,000 planned direct labour hours). Actual: '
            '300,000 machine hours worked in Machining, 600,000 direct labour hours worked in '
            'Assembling. Find the OAR for each department and the over/under absorption for the '
            'period.'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['₵\'000', 'Machining', 'Assembling', 'Maintenance'],
        'rows': [
        ['Subtotal (allocated)', '1,100', '1,100', '1,200'],
        ['Re-apportion Maintenance (50:50, by relative expense)', '600', '600', '(1,200)'],
        ['**Overhead incurred**', '**1,700**', '**1,700**', 'Nil'],
      ]}},
      {'table': {'align': 'lrr', 'head': ['', 'Machining', 'Assembling'], 'rows': [
        ['OAR', '₵4/machine hour', '₵3/DLH'],
        ['Actual activity', '300,000 machine hrs', '600,000 DLH'],
        ['Overhead absorbed ($OAR \\times$ actual)', '₵1,200,000', '₵1,800,000'],
        ['Overhead incurred', '₵1,700,000', '₵1,700,000'],
        ['**Result**', '**₵500,000 under-absorbed**', '**₵100,000 over-absorbed**'],
      ]}}]}},
  ]},

  {'n': '5.8', 't': 'Activity-Based Costing (ABC)', 'b': [
    {'p': 'Conventional overhead absorption uses a single base (units of production, labour '
          'hours, etc.) for a whole cost centre — adequate for a small/medium firm with simple '
          'operations. In a large, highly automated firm, a single base is unsuitable, because '
          'different *activities* drive indirect cost in different ways. **Activity-Based '
          'Costing** exists for exactly this situation.'},
    {'def': {'t': 'Activity-Based Costing (ABC)', 'd': 'a costing approach that traces the cost '
                  'of resources used to the *activities* that cause them to be incurred, and '
                  'then absorbs overhead into products or services based on each product\'s use '
                  'of those activities.'}},
    {'def': {'t': 'Cost driver (CIMA)', 'd': 'any factor that causes a change in the cost of an '
                  'activity.'}},
    {'p': 'Examples of cost drivers: the number of materials handling operations or issues; the '
          'number of machine set-ups; the number of machine hours; the number of inspection '
          'orders.'},
    {'h4': 'Stages in ABC'},
    {'steps': [
      'Identify and classify activities.',
      'Select a cost-driver base for each activity (e.g. number of machine set-ups).',
      'Assign cost to each activity/cost pool.',
      'Ascertain the activity cost per unit of cost driver: $\\text{Cost driver rate} = '
      '\\dfrac{\\text{Activity cost for the cost pool}}{\\text{Quantity of cost driver '
      'available}}$.',
      'Charge overhead to each product by multiplying its own consumption of each cost driver '
      'by that driver\'s rate.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Quick illustration — overhead rate per unit via two cost '
      'drivers', 'open': True, 'q': [
      {'p': '100 units of Product L are to be manufactured. 20 machine set-ups are needed at '
            '₦40 each, and 10 materials issues at ₦20 each. Find the overhead rate per unit of '
            'Product L.'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['', 'Cost (₦)'], 'rows': [
        ['Machine set-up (20 × ₦40)', '800'], ['Materials handling (10 × ₦20)', '200'],
        ['**Total overhead**', '**1,000**'],
      ]}},
      {'tex': '\\text{Overhead rate per unit} = \\dfrac{₦1{,}000}{100\\text{ units}} = ₦10'}]}},
    {'eg': {'tag': 'Study text — Illustrations 5.5 and 5.6',
      't': 'MMT Ltd — determining overhead absorption through activity-based costing',
      'open': True, 'q': [
      {'note': 'The study text prints this illustration **twice**, as Illustration 5.5 and again, '
               'word for word, as Illustration 5.6. Only the second carries a solution. It is '
               'shown once here.'},
      {'p': 'MMT manufactures two products. The company provides the following details relating '
            'to the 2015 financial year.'},
      {'p': '**1.  Units produced:** Product AB — 150,000 units; Product CD — 200,000 units.'},
      {'p': '**2.  Activity cost pools and total cost drivers:**'},
      {'stmt': {'t': 'Activity cost pools', 'rows': [
        ['Activity', 'Activity cost pool (₦)', 'Total cost driver quantity', '@hd'],
        ['Machine set-up', 300000, '60 set-ups'],
        ['Materials issued', 200000, '90 requisitions'],
        ['Quality control', 100000, '40 inspections'],
      ]}},
      {'p': '**3.  Cost drivers consumed by each product:**'},
      {'stmt': {'t': 'Cost driver usage by product', 'rows': [
        ['Activity', 'Product AB', 'Product CD', '@hd'],
        ['Machine set-up', 10, 10],
        ['Materials issued', 20, 10],
        ['Quality control', 10, 5],
      ]}},
      {'p': '**Required:** determine the overhead absorbed by each product through activity-based '
            'costing.'}],
      'a': [
      {'h4': 'Step 1 — the cost driver rate for each activity'},
      {'tex': '\\text{Cost driver rate} = \\frac{\\text{Activity cost for each cost pool}}'
              '{\\text{Quantity of cost driver available}}'},
      {'stmt': {'t': 'Cost driver rates', 'rows': [
        ['Activity', 'Cost pool (₦)', '÷ drivers', 'Rate per driver (₦)', '@hd'],
        ['Machine set-up', 300000, '60 set-ups', '5,000 per set-up'],
        ['Materials issued', 200000, '90 requisitions', '2,222.22 per requisition'],
        ['Quality control', 100000, '40 inspections', '2,500 per inspection'],
      ]}},
      {'warn': 'The study text\'s own solution divides the ₦200,000 materials-issued pool by '
               '**80** requisitions, not the **90** its question states, giving ₦2,500 per '
               'requisition instead of ₦2,222.22. The rates above use the figure the question '
               'actually gives (90). The table below shows both, because the book\'s printed '
               'answers (₦125,000 and ₦87,500) follow from its 80.',
       'lbl': 'An inconsistency in the study text'},
      {'h4': 'Step 2 — charge each product with the drivers it consumed'},
      {'stmt': {'t': 'Overhead charged, on the question\'s stated 90 requisitions', 'rows': [
        ['', 'Product AB (₦)', 'Product CD (₦)', '@hd'],
        ['Machine set-up:  ₦5,000 × 10;  ₦5,000 × 10', 50000, 50000],
        ['Materials issued:  ₦2,222.22 × 20;  ₦2,222.22 × 10', 44444, 22222],
        ['Quality control:  ₦2,500 × 10;  ₦2,500 × 5', 25000, 12500],
        ['**Total overhead charged**', 119444, 84722, '@tt'],
      ]}},
      {'p': 'For comparison, the study text\'s own printed answer, which uses ₦2,500 per '
            'requisition:'},
      {'stmt': {'t': 'The study text\'s answer (80 requisitions assumed)', 'rows': [
        ['', 'Product AB (₦)', 'Product CD (₦)', '@hd'],
        ['Machine set-up:  ₦5,000 × 10', 50000, 50000],
        ['Materials issued:  ₦2,500 × 20;  ₦2,500 × 10', 50000, 25000],
        ['Quality control:  ₦2,500 × 10;  ₦2,500 × 5', 25000, 12500],
        ['**Total overhead absorbed**', 125000, 87500, '@tt'],
      ]}},
      {'key': 'Notice what ABC has and has not done here. The two products between them consume '
              'only 20 of the 60 set-ups, 30 of the 90 requisitions and 15 of the 40 '
              'inspections, so **most of the ₦600,000 overhead pool is not charged to either '
              'product** — it belongs to other products the question does not describe. That is '
              'ABC working correctly: a product is charged for the activities it actually '
              'causes, and nothing more. Under a traditional blanket rate, AB and CD would each '
              'have absorbed a share of the whole ₦600,000 in proportion to their volume, which '
              'is precisely the distortion ABC exists to remove.'},
      {'note': 'Per unit, product AB absorbs $₦119{,}444 \\div 150{,}000 = ₦0.80$ and product '
               'CD $₦84{,}722 \\div 200{,}000 = ₦0.42$ — AB costs nearly twice as much per '
               'unit to support, even though it is the smaller-volume product, because it '
               'consumes twice as many requisitions and twice as many inspections. A '
               'volume-based blanket rate would have reported the opposite.'}]}},
  ]},

  {'n': '5.9', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§5.1–5.2 Overheads** — indirect materials + indirect labour + indirect expenses; '
      'classified by function (production/admin/marketing-selling-distribution/R&D), element, '
      'or behaviour.',
      '**§5.3 Allocation vs apportionment** — allocation is direct, no sharing; apportionment '
      'shares a cost across several centres on a fair basis (5 named bases matched to overhead '
      'type).',
      '**§5.4 Reciprocal service re-apportionment** — 3 methods (elimination, continuous '
      'allotment, simultaneous equations); continuous allotment and simultaneous equations '
      'converge exactly; elimination is a close approximation that needs ratio re-normalisation '
      'once a reciprocal partner is already closed.',
      '**§5.5 Absorption, 6 bases** — DLH and machine-hour bases give a rate *per hour*; '
      'material-cost%, labour-cost% and prime-cost% bases give a rate as a *percentage*; each '
      'suited to a different production style (labour-intensive, mechanised, uniform-unit, '
      'stable-price).',
      '**§5.6 Predetermined & blanket vs departmental** — budgeted rates avoid both the delay of '
      'waiting for actual figures and the distortion of actual-cost/actual-activity swings; '
      'blanket (factory-wide) rates hide different centres\' different overhead intensity and '
      'different activity-base mixes.',
      '**§5.7 Over/under absorption** — absorbed = OAR × actual activity; the preferred '
      'treatment of any gap is writing it off to the P&L as a period cost.',
      '**§5.8 ABC** — traces cost to activities via cost drivers, not a single blanket base; '
      '5-step process; cost driver rate = cost pool ÷ total driver quantity.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'Overhead formulas (recap)', 'rows': [
      {'lb': 'OAR (general)', 'tex': 'OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted '
        'activity level}}'},
      {'lb': 'OAR, cost-percentage bases', 'tex': 'OAR = \\dfrac{\\text{Budgeted overhead}}'
        '{\\text{Budgeted DM/DL/prime cost}} \\times 100'},
      {'lb': 'Overhead absorbed', 'tex': '\\text{OAR} \\times \\text{Actual activity}'},
      {'lb': 'Over/under absorption', 'tex': '\\text{Overhead absorbed} - \\text{Overhead '
        'incurred}', 'nt': 'Positive = over-absorbed; negative = under-absorbed.'},
      {'lb': 'Cost driver rate (ABC)', 'tex': '\\dfrac{\\text{Activity cost for the pool}}'
        '{\\text{Quantity of cost driver available}}'},
    ]}},
  ]},

  {'n': '5.10', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Overheads are the aggregate of (A) Indirect materials, indirect labour and indirect '
        'expenses  (B) Expenses incurred over the normal expense heads  (C) Expenses incurred by '
        'the owners of the business  (D) All uncontrollable expenses  (E) All unauthorised '
        'expenses',
        'Distinguish between overhead allocation and overhead apportionment. (A) Allocation is '
        'used in government whilst apportionment is used in the private sector  (B) Allocation '
        'is assigned direct to cost centres whilst apportionment is shared to a number of cost '
        'centres  (C) Allocation is made scientifically whilst apportionment is done arbitrarily '
        '(D) Allocation benefits only managers whilst apportionment benefits junior staff  '
        '(E) Both terms mean the same thing',
        'What is the usual basis of apportioning factory rent? (A) Number of employees  '
        '(B) Number of machines  (C) Floor space occupied  (D) Kilowatt of energy used  '
        '(E) Number of pillars',
        'What distinguishes a profit centre from a cost centre? (A) Direct Cost  '
        '(B) Indirect Cost  (C) Profit  (D) Loss  (E) Revenue',
        'What does OAR stand for in overheads accounting? (A) Organisational Accounting Returns  '
        '(B) Overheads Accounting Rate  (C) Overheads Accounting Returns  (D) Overheads '
        'Absorption Rate  (E) Organisational Absorption Rate',
        'Where the actual overheads for a period exceed the predetermined overheads, this is a '
        'case of …………………………..',
        'A system of continuously reallocating each service cost centre overhead until the '
        'amounts become insignificant is known as ……………….',
        'Overheads covering the cost of securing orders, publicising and presenting a company\'s '
        'products in proper forms at acceptable prices and delivering the goods to customers are '
        'generally known as …………………',
        'Where the production process is highly mechanised, making the use of labour hours '
        'inappropriate for overhead absorption, what alternative basis may be used?',
        'Which is the best way to treat over- and under-absorbed overheads for a period?',
      ]}],
      'a': [
      {'ol': [
        '**A — indirect materials, indirect labour and indirect expenses.**',
        '**B** — allocation goes direct to a cost centre; apportionment is shared across several.',
        '**C — floor space occupied.**',
        '**E — revenue** (a profit centre both incurs cost and generates revenue).',
        '**D — Overheads Absorption Rate.**',
        '**Under-absorption** (actual overhead exceeds what was absorbed).',
        '**Continuous allotment.**',
        '**Marketing, selling and distribution overheads.**',
        '**Machine hours.**',
        '**Write it off to the Profit and Loss Account.**',
      ]}]}},
  ]},

  {'n': '5.11', 't': 'Chapter summary', 'b': [
    {'p': 'This chapter has discussed accounting for overheads in three sections.'},
    {'ol': [
      'The **first section** addressed the introductory issues in overheads — explaining the '
      'meaning of overheads, the classification of overheads and the treatment of overheads.',
      'The **second section** discussed the processes of overhead **allocation**, overhead '
      '**apportionment** and overhead **absorption**.',
      'The **final section** explained the concept of overhead absorption — the six methods that '
      'can be used to absorb overheads, the reasons for preferring **predetermined** absorption '
      'rates to actual rates, and the treatment of overhead **under-absorbed** or '
      '**over-absorbed**.',
    ]},
    {'key': 'Overheads are a very important concept in cost accounting and it is important to '
            'understand them thoroughly, because overhead concepts recur in every subsequent '
            'topic — job and contract costing (Chapter 7), process costing (Chapter 8), '
            'marginal versus absorption costing (Chapter 9), budgeting (Chapter 12) and the '
            'fixed overhead variances of standard costing (Chapter 13) all rest on this '
            'chapter.'},
  ]},

  {'n': '5.12', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with nine examination-type questions, drawn from '
          'past ICAG, CIMA, CACA and ACCA papers. All are reproduced below with full answers.'},

    {'eg': {'tag': 'Exam type — Q5.1 (20 marks) — ICAG, May 2000',
      't': 'Absorbed fixed overhead, absorption versus marginal profit, and the reconciliation',
      'q': [
      {'p': 'The following information is available for a firm producing and selling a single '
            'product. Budgeted costs at normal activity:'},
      {'stmt': {'t': 'Budgeted costs at normal activity', 'rows': [
        ['', '¢000', '@hd'],
        ['Direct material and labour', 264000],
        ['Variable production overhead', 48000],
        ['Fixed production overhead', 144000],
        ['Variable selling and administration overhead', 24000],
        ['Fixed selling and administration overhead', 96000],
      ]}},
      {'p': 'The overhead absorption rates are based upon **normal activity of 240,000 units** '
            'per period. During the period just ended **260,000 units** were produced and '
            '**230,000 units** were sold at **¢3,000 per unit**. At the beginning of the period '
            '**40,000 units** were in stock, valued at the budgeted costs shown above. Actual '
            'costs incurred were as per the budget.'},
      {'p': '**Required:** (a) calculate the fixed production overhead absorbed during the '
            'period and the extent of any over- or under-absorption, using absorption costing; '
            '(b) calculate the profit for the period using absorption costing and marginal '
            'costing respectively; (c) reconcile the two profit figures; (d) state the '
            'situations in which the two profits would be the same.'}],
      'a': [
      {'h4': 'Step 1 — unit costs from the budget'},
      {'p': 'Every budgeted cost is divided by the normal activity of 240,000 units:'},
      {'stmt': {'t': 'Budgeted cost per unit', 'rows': [
        ['', 'Budget ¢000', '÷ 240,000 units', '@hd'],
        ['Direct material and labour', 264000, '¢1,100'],
        ['Variable production overhead', 48000, '¢200'],
        ['**Marginal (variable) production cost**', 312000, '**¢1,300**', '@t'],
        ['Fixed production overhead', 144000, '¢600'],
        ['**Full (absorption) production cost**', 456000, '**¢1,900**', '@t'],
        '@gap',
        ['Variable selling and administration overhead', 24000, '¢100'],
        ['Fixed selling and administration overhead', 96000, '¢400'],
      ]}},
      {'h4': '(a)  Fixed production overhead absorbed, and the over/under-absorption'},
      {'stmt': {'t': 'Fixed production overhead', 'rows': [
        ['Absorbed:  260,000 units produced × ¢600 per unit', '', '¢156,000,000'],
        ['Incurred (actual = budget)', '', '¢144,000,000'],
        ['**Over-absorbed**', '', '**¢12,000,000**', '@tt'],
      ]}},
      {'note': 'Fixed overhead is absorbed on **production**, not on sales — 260,000 units were '
               'made, so 260,000 units\' worth of fixed overhead went into the cost of '
               'production. Because output exceeded the 240,000 units on which the rate was '
               'set, more was absorbed than was spent, and the excess is credited to the profit '
               'and loss account.'},
      {'h4': '(b)  Profit under absorption costing'},
      {'stmt': {'t': 'Absorption costing — profit statement for the period (¢)', 'rows': [
        ['Sales:  230,000 units × ¢3,000', '', 690000000],
        ['Less cost of sales:  230,000 units × ¢1,900 full production cost', '', 437000000],
        ['**Gross profit**', '', 253000000, '@t'],
        ['Add: fixed production overhead over-absorbed', '', 12000000],
        ['', '', 265000000, '@t'],
        ['Less: variable selling and administration (230,000 × ¢100)', 23000000, ''],
        ['          fixed selling and administration', 96000000, 119000000],
        ['**Profit — absorption costing**', '', 146000000, '@tt'],
      ]}},
      {'h4': '(b)  Profit under marginal costing'},
      {'stmt': {'t': 'Marginal costing — profit statement for the period (¢)', 'rows': [
        ['Sales:  230,000 units × ¢3,000', '', 690000000],
        ['Less variable cost of sales:  230,000 × ¢1,300', 299000000, ''],
        ['          variable selling and administration:  230,000 × ¢100', 23000000, 322000000],
        ['**Contribution**', '', 368000000, '@t'],
        ['Less: fixed production overhead (actual)', 144000000, ''],
        ['          fixed selling and administration', 96000000, 240000000],
        ['**Profit — marginal costing**', '', 128000000, '@tt'],
      ]}},
      {'h4': '(c)  Reconciliation of the two profits'},
      {'stmt': {'t': 'Reconciliation (¢)', 'rows': [
        ['Opening inventory (units)', '', 40000],
        ['Add: production', '', 260000],
        ['Less: sales', '', -230000],
        ['**Closing inventory (units)**', '', 70000, '@t'],
        ['**Increase in inventory during the period (units)**', '', 30000, '@t'],
        '@gap',
        ['Fixed production overhead per unit', '', '¢600'],
        ['**Fixed overhead carried forward in the inventory increase: 30,000 × ¢600**', '',
         18000000, '@t'],
        '@gap',
        ['Profit — marginal costing', '', 128000000],
        ['Add: fixed production overhead carried forward in the increase in inventory', '',
         18000000],
        ['**Profit — absorption costing**', '', 146000000, '@tt'],
      ]}},
      {'key': 'The whole difference between the two systems is **where fixed production overhead '
              'sits**. Under marginal costing it is written off in full in the period it is '
              'incurred. Under absorption costing it is attached to units, so when inventory '
              'rises, ¢18 million of this period\'s fixed overhead is carried forward in the '
              'extra 30,000 units and is **not** charged against this period\'s profit — which '
              'is exactly why absorption profit is ¢18 million higher. If inventory had fallen, '
              'the effect would reverse.'},
      {'h4': '(d)  When the two profits are the same'},
      {'ol': [
        'When **production equals sales**, so there is **no change in inventory** over the '
        'period — nothing is carried forward or released, and the same fixed overhead is charged '
        'under both systems.',
        'When there is **no opening and no closing inventory** at all (a special case of the '
        'above).',
        'When fixed production overhead per unit is the **same** in opening and closing '
        'inventory **and** inventory volume is unchanged — i.e. where the absorption rate has '
        'not altered between periods.',
        'Where the business carries **no fixed production overhead** at all, so there is nothing '
        'to attach to inventory.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q5.2 (25 marks) — ICAG, May 1997',
      't': 'Atta Kwesi Manufacturing — a blanket rate versus departmental rates, and Job FX18',
      'q': [
      {'p': 'Atta Kwesi Manufacturing Company has three departments X, Y and Z. The company uses '
            'a **single production overhead rate**, expressed as a percentage of direct wages. A '
            'change of policy in favour of **departmental absorption rates** is contemplated, on '
            'the grounds that these can be more precise.'},
      {'stmt': {'t': 'Budgeted figures', 'rows': [
        ['', 'Direct wages ¢000', 'Direct labour hours \'000', 'Machine hours \'000',
         'Production overheads ¢000', '@hd'],
        ['Dept. X', 250, 100, 400, 1200],
        ['Dept. Y', 1000, 500, 100, 300],
        ['Dept. Z', 250, 250, '—', 750],
        ['**Total**', 1500, 850, 500, 2250, '@tt'],
      ]}},
      {'stmt': {'t': 'Actual figures', 'rows': [
        ['', 'Direct wages ¢000', 'Direct labour hours \'000', 'Machine hours \'000',
         'Production overheads ¢000', '@hd'],
        ['Dept. X', 300, 120, 450, 1300],
        ['Dept. Y', 800, 450, 140, 280],
        ['Dept. Z', 300, 300, '—', '—'],
        ['**Total**', 1400, 870, 590, 1580, '@tt'],
      ]}},
      {'p': 'Job No. **FX18** has just been completed. The actual information on this job is:'},
      {'stmt': {'t': 'Job FX18', 'rows': [
        ['', 'Direct materials ¢', 'Direct wages ¢', 'Direct labour hours', 'Machine hours',
         '@hd'],
        ['Dept. X', 1200, 1000, 200, 400],
        ['Dept. Y', 600, 600, 400, 100],
        ['Dept. Z', 100, 100, 100, '—'],
        ['**Total**', 1900, 1700, 700, 500, '@tt'],
      ]}},
      {'p': 'The pricing policy of the company is to make a **gross mark-up of 33⅓%** on '
            'completion of jobs, which is expected to cover other business expenses plus net '
            'profit.'},
      {'p': '**Required:** (a) determine the overhead absorption rate which has been in use; '
            '(b) determine the production overhead to be absorbed by Job FX18 using that rate, '
            'and the price of Job FX18; (c) considering the new policy, determine the relevant '
            'departmental absorption rates, giving reasons for each rate chosen; (d) with the '
            'new rates, determine the new departmental overheads and total production overhead '
            'to be absorbed by Job FX18, and the price of the job on this new information.'},
      {'note': 'The actual production overhead for Department Z is printed as a blank. The '
               'printed actual total of ¢1,580 thousand equals ¢1,300 + ¢280, so the blank is '
               'consistent with nil. Nothing in the required parts depends on the actual '
               'overheads, which are given for context only — all the rates asked for are '
               '**predetermined**, and so are built from the **budgeted** figures.'}],
      'a': [
      {'h4': '(a)  The overhead absorption rate in use'},
      {'p': 'A single (blanket) rate expressed as a percentage of direct wages:'},
      {'tex': '\\text{Blanket rate} = \\frac{\\text{Budgeted production overheads}}'
              '{\\text{Budgeted direct wages}} = \\frac{2{,}250}{1{,}500} \\times 100 '
              '= 150\\% \\text{ of direct wages}'},
      {'h4': '(b)  Overhead absorbed by Job FX18, and its price'},
      {'stmt': {'t': 'Job FX18 under the blanket rate (¢)', 'rows': [
        ['Direct materials  (1,200 + 600 + 100)', '', 1900],
        ['Direct wages  (1,000 + 600 + 100)', '', 1700],
        ['**Prime cost**', '', 3600, '@t'],
        ['Production overhead absorbed:  150% × ¢1,700', '', 2550],
        ['**Total production cost**', '', 6150, '@t'],
        ['Gross mark-up at 33⅓% of cost', '', 2050],
        ['**Price of Job FX18**', '', 8200, '@tt'],
      ]}},
      {'h4': '(c)  Departmental absorption rates, and the reasons for each'},
      {'p': 'The right basis for each department is the one that best measures what actually '
            'causes overhead to be incurred there. Compare each department\'s machine hours '
            'with its labour hours:'},
      {'stmt': {'t': 'Choosing a basis', 'rows': [
        ['', 'Direct labour hrs (\'000)', 'Machine hrs (\'000)', 'Character of the department',
         '@hd'],
        ['Dept. X', 100, 400, '**Machine-intensive** — 4 machine hours per labour hour'],
        ['Dept. Y', 500, 100, '**Labour-intensive** — 5 labour hours per machine hour'],
        ['Dept. Z', 250, '—', '**Labour only** — no machinery at all'],
      ]}},
      {'stmt': {'t': 'Departmental absorption rates', 'rows': [
        ['Department', 'Budgeted overhead ¢000', 'Basis', 'Rate', '@hd'],
        ['X', 1200, '400,000 machine hours', '**¢3.00 per machine hour**'],
        ['Y', 300, '500,000 direct labour hours', '**¢0.60 per direct labour hour**'],
        ['Z', 750, '250,000 direct labour hours', '**¢3.00 per direct labour hour**'],
      ]}},
      {'ul': [
        '**Dept. X — machine hour rate.** Overhead here is overwhelmingly machine-driven '
        '(depreciation, power, maintenance, machine insurance), and the department runs four '
        'machine hours for every labour hour, so machine time is what consumes the overhead.',
        '**Dept. Y — direct labour hour rate.** The department is labour-intensive, with five '
        'labour hours per machine hour, so overhead is incurred broadly in proportion to the '
        'time people spend there.',
        '**Dept. Z — direct labour hour rate.** There are no machine hours at all, so machine '
        'hours are not available as a basis. (A percentage of direct wages would give the same '
        'answer here — 300% of ¢250,000 — because wages and hours happen to stand in the ratio '
        '¢1 per hour; the labour hour rate is preferable in principle because it is unaffected '
        'by differences in wage rates between workers.)',
      ]},
      {'h4': '(d)  Job FX18 under the departmental rates'},
      {'stmt': {'t': 'Overhead absorbed by Job FX18 (¢)', 'rows': [
        ['Dept. X:  400 machine hours × ¢3.00', '', 1200],
        ['Dept. Y:  400 direct labour hours × ¢0.60', '', 240],
        ['Dept. Z:  100 direct labour hours × ¢3.00', '', 300],
        ['**Total production overhead absorbed**', '', 1740, '@tt'],
      ]}},
      {'stmt': {'t': 'Price of Job FX18 under the new rates (¢)', 'rows': [
        ['Direct materials', '', 1900],
        ['Direct wages', '', 1700],
        ['**Prime cost**', '', 3600, '@t'],
        ['Production overhead absorbed', '', 1740],
        ['**Total production cost**', '', 5340, '@t'],
        ['Gross mark-up at 33⅓% of cost', '', 1780],
        ['**Price of Job FX18**', '', 7120, '@tt'],
      ]}},
      {'key': 'The same job, the same costs, the same mark-up policy — and a price **¢1,080 '
              'lower** (¢7,120 against ¢8,200), a difference of over 13%. The blanket rate '
              'charged Job FX18 for overhead in proportion to its wages bill, and the job\'s '
              'wages are concentrated in Department Y, which has low overhead and absorbs it '
              'cheaply. The blanket rate therefore **over-costed** this job — and, necessarily, '
              'under-costed some other job. On the blanket rate Atta Kwesi may well have lost '
              'tenders it could profitably have won. That is the entire argument for '
              'departmental rates.'}]}},

    {'eg': {'tag': 'Exam type — Q5.3 (24 marks) — ICAG, January 1996',
      't': 'Moulding and Finishing — percentage-of-prime-cost rates under two treatments of '
           'machine preparation time',
      'q': [
      {'p': 'A manufacturing company producing in batches is preparing a budget for the next '
            'financial period. There are two production departments — **Moulding** and '
            '**Finishing**. The following information for the coming year has been compiled:'},
      {'stmt': {'t': 'Budget for the coming year', 'rows': [
        ['', 'Moulding (¢\'000)', 'Finishing (¢\'000)', '@hd'],
        ['Direct materials', 640000, 120000],
        ['Direct labour  *(56,000 hours;  14,000 hours)*', 224000, 44800],
        ['Overhead (apportioned)', 313600, 62720],
        ['**Total**', 1177600, 227520, '@tt'],
      ]}},
      {'p': 'The following forecast has been made:'},
      {'ol': [
        'In the Moulding department **90%** of the labour time will be spent in actual '
        'production and **10%** adjusting machines before actual production; in the Finishing '
        'department **80%** will be actual production and **20%** preparing machines.',
        '**2,000 batches** of work will be produced. Work passes through both stages before '
        'completion. The labour employed in preparing machines could be treated either '
        '**(i) as part of direct labour cost**, or **(ii) as an addition to the overhead** '
        'apportioned to each department.',
      ]},
      {'p': '**Required:** **(a)** calculate for each department the overhead absorption rates '
            'on a **percentage of prime cost** basis, under each of the two treatments (to the '
            'nearest whole number) *(12 marks)*. **(b)** calculate the total production cost of '
            'each of the three batches below, on each of the two sets of rates *(12 marks)*.'},
      {'stmt': {'t': 'The three batches', 'rows': [
        ['Batch No.', 'Direct labour hrs — Moulding', 'Direct labour hrs — Finishing',
         'Materials (kg) — Moulding', 'Materials (kg) — Finishing', 'Price per kilo (¢)', '@hd'],
        ['C061', 35, 22, 250, 101, 800],
        ['L024', 38, 29, 411, 139, 690],
        ['M115', 19, 12, 89, 26, 1100],
      ]}},
      {'note': 'The study text prints the labour-hour figures on the direct **materials** line; '
               'they are the departments\' direct **labour** hours, which is the only reading '
               'under which the direct labour cost and the batch data are consistent.'}],
      'a': [
      {'h4': 'Working — the direct labour rate per hour'},
      {'stmt': {'t': 'Direct labour rate per hour', 'rows': [
        ['Moulding:  ¢224,000,000 ÷ 56,000 hours', '', '¢4,000 per hour'],
        ['Finishing:  ¢44,800,000 ÷ 14,000 hours', '', '¢3,200 per hour'],
      ]}},
      {'h4': '(a)(i)  Rates with machine-preparation time treated as **direct labour cost**'},
      {'p': 'All the labour is direct, so prime cost and overhead are exactly as budgeted:'},
      {'stmt': {'t': 'Overhead as a percentage of prime cost — treatment (i)  (¢\'000)', 'rows': [
        ['', 'Moulding', 'Finishing', '@hd'],
        ['Direct materials', 640000, 120000],
        ['Direct labour (all of it)', 224000, 44800],
        ['**Prime cost**', 864000, 164800, '@t'],
        ['Overhead', 313600, 62720],
        ['**Overhead as % of prime cost**', '36.3%  →  **36%**', '38.1%  →  **38%**', '@tt'],
      ]}},
      {'h4': '(a)(ii)  Rates with machine-preparation time treated as **overhead**'},
      {'p': 'The preparation portion of the wage bill moves out of direct labour and into '
            'overhead — prime cost falls and overhead rises, so the percentage rises twice over:'},
      {'stmt': {'t': 'Overhead as a percentage of prime cost — treatment (ii)  (¢\'000)',
        'rows': [
        ['', 'Moulding', 'Finishing', '@hd'],
        ['Direct materials', 640000, 120000],
        ['Direct labour — productive only (90% × 224,000;  80% × 44,800)', 201600, 35840],
        ['**Prime cost**', 841600, 155840, '@t'],
        ['Overhead as apportioned', 313600, 62720],
        ['Add: preparation labour (10% × 224,000;  20% × 44,800)', 22400, 8960],
        ['**Total overhead**', 336000, 71680, '@t'],
        ['**Overhead as % of prime cost**', '39.9%  →  **40%**', '46.0%  →  **46%**', '@tt'],
      ]}},
      {'h4': '(b)  Total production cost of the three batches'},
      {'p': 'Materials are the same under either treatment. Direct labour is the full hours in '
            'treatment (i), and only the productive 90%/80% of the hours in treatment (ii).'},
      {'stmt': {'t': 'Batch C061  (materials at ¢800 per kilo)', 'rows': [
        ['', 'Treatment (i) — ¢', 'Treatment (ii) — ¢', '@hd'],
        ['**Moulding**', '', '', '@hd'],
        ['Direct materials  250 kg × ¢800', 200000, 200000],
        ['Direct labour  35 hrs × ¢4,000;  31.5 hrs × ¢4,000', 140000, 126000],
        ['Prime cost', 340000, 326000],
        ['Overhead  36% × 340,000;  40% × 326,000', 122400, 130400],
        ['**Moulding cost**', 462400, 456400, '@t'],
        '@gap',
        ['**Finishing**', '', '', '@hd'],
        ['Direct materials  101 kg × ¢800', 80800, 80800],
        ['Direct labour  22 hrs × ¢3,200;  17.6 hrs × ¢3,200', 70400, 56320],
        ['Prime cost', 151200, 137120],
        ['Overhead  38% × 151,200;  46% × 137,120', 57456, 63075],
        ['**Finishing cost**', 208656, 200195, '@t'],
        '@gap',
        ['**Total production cost — Batch C061**', 671056, 656595, '@tt'],
      ]}},
      {'stmt': {'t': 'Batch L024  (materials at ¢690 per kilo)', 'rows': [
        ['', 'Treatment (i) — ¢', 'Treatment (ii) — ¢', '@hd'],
        ['Moulding materials  411 kg × ¢690', 283590, 283590],
        ['Moulding labour  38 hrs;  34.2 hrs', 152000, 136800],
        ['Moulding prime cost', 435590, 420390],
        ['Moulding overhead  36%;  40%', 156812, 168156],
        '@gap',
        ['Finishing materials  139 kg × ¢690', 95910, 95910],
        ['Finishing labour  29 hrs;  23.2 hrs', 92800, 74240],
        ['Finishing prime cost', 188710, 170150],
        ['Finishing overhead  38%;  46%', 71710, 78269],
        '@gap',
        ['**Total production cost — Batch L024**', 852822, 836965, '@tt'],
      ]}},
      {'stmt': {'t': 'Batch M115  (materials at ¢1,100 per kilo)', 'rows': [
        ['', 'Treatment (i) — ¢', 'Treatment (ii) — ¢', '@hd'],
        ['Moulding materials  89 kg × ¢1,100', 97900, 97900],
        ['Moulding labour  19 hrs;  17.1 hrs', 76000, 68400],
        ['Moulding prime cost', 173900, 166300],
        ['Moulding overhead  36%;  40%', 62604, 66520],
        '@gap',
        ['Finishing materials  26 kg × ¢1,100', 28600, 28600],
        ['Finishing labour  12 hrs;  9.6 hrs', 38400, 30720],
        ['Finishing prime cost', 67000, 59320],
        ['Finishing overhead  38%;  46%', 25460, 27287],
        '@gap',
        ['**Total production cost — Batch M115**', 328964, 319427, '@tt'],
      ]}},
      {'key': 'Every batch comes out **cheaper** under treatment (ii), even though the factory '
              'spends exactly the same money either way. The reason is the absorption base: '
              'moving preparation labour out of prime cost shrinks the base these batches are '
              'charged on, and although the percentage rate rises to compensate at the level of '
              'the whole department, it does not compensate exactly for any **individual** '
              'batch. Total cost across all 2,000 batches is unchanged — what changes is how it '
              'is spread between them. This is the general lesson of absorption: the choice of '
              'base is a choice about **who bears the overhead**, not about how much there is.'}]}},

    {'eg': {'tag': 'Exam type — Q5.4 (28 marks) — ICAG, January 1988',
      't': 'Larson Co. Ltd — full overhead apportionment, service-department reapportionment, '
           'and the pricing of two jobs',
      'q': [
      {'p': 'Larson Co. Ltd, a jobbing engineering firm, has in its single factory three '
            'production departments (**moulding, assembly and finishing**) supported by two '
            'service departments (**boiler and maintenance**). The company\'s production costs '
            'for the past month are:'},
      {'stmt': {'t': 'Production costs for the month (¢)', 'rows': [
        ['**Prime cost**', '', '', '@hd'],
        ['Direct materials', 360000, ''],
        ['Direct wages', 300000, 660000],
        '@gap',
        ['**Indirect materials**', '', '', '@hd'],
        ['Moulding', 11240, ''],
        ['Assembly', 17890, ''],
        ['Finishing', 6390, ''],
        ['Boiler', 11000, ''],
        ['Maintenance', 5000, 51520],
        '@gap',
        ['**Supervision and indirect wages**', '', '', '@hd'],
        ['Moulding', 13000, ''],
        ['Assembly', 16800, ''],
        ['Finishing', 13600, ''],
        ['Boiler', 12420, ''],
        ['Maintenance', 10380, 66200],
        '@gap',
        ['**General production overheads**', '', '', '@hd'],
        ['Factory rent and rates', 25200, ''],
        ['Insurance — machinery', 9900, ''],
        ['Insurance — building', 7700, ''],
        ['Depreciation — machinery', 18000, ''],
        ['Depreciation — building', 7280, ''],
        ['Administrative costs of wages department', 16800, 84880],
        '@gap',
        ['**Total factory cost**', '', 862600, '@tt'],
      ]}},
      {'warn': 'The study text prints the supervision and indirect wages subtotal as "6,200" and '
               'the total factory cost as ¢882,600. The five departmental figures sum to '
               '**¢66,200**, and the total factory cost is therefore **¢862,600**. The '
               'corrected figures are used above and are confirmed below: the overheads to be '
               'apportioned come to exactly $51{,}520 + 66{,}200 + 84{,}880 = ¢202{,}600$, which '
               'is what the departmental analysis totals.',
       'lbl': 'Source arithmetic corrected'},
      {'p': 'Further information is available:'},
      {'stmt': {'t': 'Departmental data', 'rows': [
        ['', 'Moulding', 'Assembly', 'Finishing', 'Boiler', 'Maintenance', '@hd'],
        ['Area (square metres)', 600, 400, 200, 100, 100],
        ['Direct labour (hours)', 15000, 15000, 10000, '—', '—'],
        ['Direct labour cost (¢)', 45000, 30000, 25000, '—', '—'],
        ['Machine hours', 20000, 30000, 40000, '—', '—'],
        ['Net book value of plant (¢)', 30000, 60000, 90000, 120000, 'nil'],
        ['Number of employees', 75, 75, 50, 15, 25],
        ['Machine maintenance hours', 156, 312, 468, 104, '—'],
      ]}},
      {'ul': [
        'The factory manager estimates that **10% of total maintenance costs relates to the '
        'boiler** and the balance to the three production departments (the maintenance '
        'department uses none of the power produced by the boiler).',
        'The most important factor in determining the requirement for maintenance is total '
        'machine hours; all machines in the factory can be taken to be of approximately equal '
        'value.',
        'The company sets its selling prices as: **(1)** cost of production, plus **(2)** 25% '
        'uplift to cover normal administrative and selling cost, plus **(3)** a profit margin of '
        '**10% of the final selling price**.',
        'It is the policy of the company to **absorb overhead on the basis of direct labour '
        'hours**.',
      ]},
      {'p': 'Two jobs, X and Y, are currently being priced:'},
      {'stmt': {'t': 'Jobs X and Y', 'rows': [
        ['', 'Job X', 'Job Y', '@hd'],
        ['Direct materials', '¢483.00', '¢361.00'],
        '@gap',
        ['**Direct labour**', '', '', '@hd'],
        ['Moulding', '10 hrs — ¢30.00', '15 hrs — ¢45.00'],
        ['Assembly', '20 hrs — ¢40.00', '2 hrs — ¢4.00'],
        ['Finishing', '8 hrs — ¢20.00', '12 hrs — ¢30.00'],
        '@gap',
        ['**Machine hours**', '', '', '@hd'],
        ['Moulding', '5 hrs', '8 hrs'],
        ['Assembly', '7 hrs', '1 hr'],
        ['Finishing', '1 hr', '5 hrs'],
      ]}},
      {'p': '**Required:** (a) calculate overhead absorption rates for the three production '
            'departments *(20 marks)*; (b) calculate the prices to be charged for jobs X and Y, '
            'to 2 decimal places *(8 marks)*.'},
      {'note': 'In the study text the job table\'s row labels sit one line above their figures, '
               'so the hours appear against the wrong departments. The alignment above is '
               'confirmed by the implied wage rates, which match the departmental data exactly: '
               'Moulding ¢30 ÷ 10 hrs = ¢3.00/hr (and ¢45,000 ÷ 15,000 hrs = ¢3.00); Assembly '
               '¢40 ÷ 20 = ¢2.00 (¢30,000 ÷ 15,000 = ¢2.00); Finishing ¢20 ÷ 8 = ¢2.50 '
               '(¢25,000 ÷ 10,000 = ¢2.50).'}],
      'a': [
      {'h4': 'Step 1 — allocate and apportion the overheads'},
      {'p': 'Indirect materials and supervision are **allocated** — each is already identified '
            'with one department. The six general production overheads must be **apportioned** '
            'on a sensible basis:'},
      {'stmt': {'t': 'Bases of apportionment', 'rows': [
        ['Overhead', 'Amount (¢)', 'Basis', 'Why', '@hd'],
        ['Factory rent and rates', 25200, 'Area', 'Space occupied drives the cost of the '
         'premises'],
        ['Insurance — building', 7700, 'Area', 'The premium follows the building, and so the '
         'space occupied'],
        ['Depreciation — building', 7280, 'Area', 'As above'],
        ['Insurance — machinery', 9900, 'Net book value of plant', 'The premium follows the '
         'value of the plant insured'],
        ['Depreciation — machinery', 18000, 'Net book value of plant', 'Depreciation is a '
         'function of the plant\'s cost'],
        ['Administrative costs of wages dept.', 16800, 'Number of employees', 'The wages '
         'department\'s work is driven by the number of people on the payroll'],
      ]}},
      {'stmt': {'t': 'Overhead analysis sheet (¢)', 'rows': [
        ['', 'Basis', 'Moulding', 'Assembly', 'Finishing', 'Boiler', 'Maintenance', 'Total',
         '@hd'],
        ['Indirect materials', 'Allocated', 11240, 17890, 6390, 11000, 5000, 51520],
        ['Supervision and indirect wages', 'Allocated', 13000, 16800, 13600, 12420, 10380, 66200],
        ['Rent, rates, building insurance and depreciation (¢40,180)', 'Area 6:4:2:1:1',
         17220, 11480, 5740, 2870, 2870, 40180],
        ['Machinery insurance and depreciation (¢27,900)', 'NBV of plant',
         2790, 5580, 8370, 11160, 0, 27900],
        ['Wages department administration', 'Employees 75:75:50:15:25',
         5250, 5250, 3500, 1050, 1750, 16800],
        ['**Total before reapportionment**', '', 49500, 57000, 37600, 38500, 20000, 202600,
         '@tt'],
      ]}},
      {'h4': 'Step 2 — reapportion the service departments'},
      {'p': '**Maintenance** is reapportioned on **machine maintenance hours** (156 : 312 : 468 '
            ': 104, total 1,040). This basis reproduces the factory manager\'s own estimate '
            'exactly — the boiler\'s 104 hours are $104 \\div 1{,}040 = 10\\%$ of the total, '
            'which is the 10% he states — so it is clearly the basis intended.'},
      {'p': '**Boiler** is then reapportioned to the three **production departments only**, '
            'since the question states the maintenance department uses none of the power the '
            'boiler produces. The boiler supplies heat and power to the floor space it serves, '
            'so **area** (600 : 400 : 200) is used.'},
      {'stmt': {'t': 'Reapportionment of service departments (¢)', 'rows': [
        ['', 'Moulding', 'Assembly', 'Finishing', 'Boiler', 'Maintenance', 'Total', '@hd'],
        ['Total before reapportionment', 49500, 57000, 37600, 38500, 20000, 202600],
        ['Maintenance on machine maintenance hours 156:312:468:104',
         3000, 6000, 9000, 2000, -20000, 0],
        ['', 52500, 63000, 46600, 40500, 0, 202600],
        ['Boiler on area 6:4:2 (production departments only)',
         20250, 13500, 6750, -40500, 0, 0],
        ['**Total production department overhead**', 72750, 76500, 53350, 0, 0, 202600, '@tt'],
      ]}},
      {'h4': '(a)  Overhead absorption rates'},
      {'p': 'Company policy is to absorb on **direct labour hours**:'},
      {'stmt': {'t': 'Overhead absorption rates', 'rows': [
        ['Department', 'Overhead (¢)', 'Direct labour hours', 'Rate per direct labour hour',
         '@hd'],
        ['Moulding', 72750, 15000, '**¢4.85**'],
        ['Assembly', 76500, 15000, '**¢5.10**'],
        ['Finishing', 53350, 10000, '**¢5.335**'],
      ]}},
      {'h4': '(b)  Prices for jobs X and Y'},
      {'stmt': {'t': 'Job X (¢)', 'rows': [
        ['Direct materials', '', 483.00],
        ['Direct labour  (30.00 + 40.00 + 20.00)', '', 90.00],
        ['**Prime cost**', '', 573.00, '@t'],
        ['Overhead — Moulding  10 hrs × ¢4.85', 48.50, ''],
        ['Overhead — Assembly  20 hrs × ¢5.10', 102.00, ''],
        ['Overhead — Finishing  8 hrs × ¢5.335', 42.68, 193.18],
        ['**Cost of production**', '', 766.18, '@t'],
        ['Add: 25% uplift for administrative and selling cost', '', 191.55],
        ['**Cost plus uplift**', '', 957.73, '@t'],
        ['Add: profit margin of 10% of the final selling price  (957.73 ÷ 0.9 − 957.73)', '',
         106.41],
        ['**Selling price of Job X**', '', 1064.14, '@tt'],
      ]}},
      {'stmt': {'t': 'Job Y (¢)', 'rows': [
        ['Direct materials', '', 361.00],
        ['Direct labour  (45.00 + 4.00 + 30.00)', '', 79.00],
        ['**Prime cost**', '', 440.00, '@t'],
        ['Overhead — Moulding  15 hrs × ¢4.85', 72.75, ''],
        ['Overhead — Assembly  2 hrs × ¢5.10', 10.20, ''],
        ['Overhead — Finishing  12 hrs × ¢5.335', 64.02, 146.97],
        ['**Cost of production**', '', 586.97, '@t'],
        ['Add: 25% uplift for administrative and selling cost', '', 146.74],
        ['**Cost plus uplift**', '', 733.71, '@t'],
        ['Add: profit margin of 10% of the final selling price  (733.71 ÷ 0.9 − 733.71)', '',
         81.52],
        ['**Selling price of Job Y**', '', 815.23, '@tt'],
      ]}},
      {'warn': 'The profit margin is **10% of the final selling price**, not 10% of cost. So the '
               'cost-plus-uplift figure represents 90% of the price, and the price is found by '
               'dividing by 0.9 — **not** by multiplying by 1.1. On Job X, multiplying by 1.1 '
               'would give ¢1,053.50 instead of ¢1,064.14, and the margin actually earned would '
               'be 9.09% of the price rather than the 10% intended. Watch the words **"on '
               'cost"** versus **"of selling price"** in every pricing question.'},
      {'note': 'The machine hours given for the two jobs are not used, because company policy is '
               'to absorb on direct labour hours. They are there to be discarded — recognising '
               'which data a question does **not** need is part of what is being tested. The '
               '¢300,000 direct wages in the cost summary are likewise inconsistent with the '
               '¢100,000 that the departmental analysis totals; neither figure is needed for the '
               'overhead rates, which depend only on hours.'}]}},

    {'eg': {'tag': 'Exam type — Q5.5 (20 marks) — CIMA Cost Accounting 1, November 1979',
      't': 'Why predetermined rates are preferred, and whether a lower rate means a more '
           'efficient factory',
      'q': [
      {'p': '**(a)** Explain why predetermined overhead absorption rates are preferred to '
            'overhead absorption rates calculated from factual information after the end of a '
            'financial period.'},
      {'p': '**(b)** The production overhead absorption rates of factories X and Y are '
            'calculated using similar methods. However, the rate used by X is **lower** than '
            'that used by factory Y. Both factories produce the same type of product. Discuss '
            'whether or not this can be taken to be a sign that factory X is more efficient than '
            'factory Y.'}],
      'a': [
      {'h4': '(a)  Why predetermined rates are preferred'},
      {'ol': [
        '**Costs are needed before the period ends.** Quotations, tenders and selling prices '
        'must be prepared when the customer asks, not months later. An actual rate cannot be '
        'computed until the period has closed, by which time the job has been quoted, made and '
        'delivered.',
        '**Invoicing and job costing cannot wait.** A job completed in the first week of the '
        'year would have to remain uncosted until the year end if actual rates were used.',
        '**Actual rates fluctuate with volume.** Fixed overhead divided by the actual activity '
        'of a slack month gives a high rate, and of a busy month a low one, so identical jobs '
        'would be costed differently depending only on when they happened to be made. A '
        'predetermined rate based on **normal activity** removes this distortion.',
        '**Actual rates fluctuate with seasonal expenditure.** Heating in winter, holiday pay in '
        'summer and an annual maintenance shutdown would all distort the rate of the month in '
        'which they fall. A predetermined annual rate spreads them evenly.',
        '**They permit control.** Comparing overhead absorbed with overhead incurred produces '
        'the under- or over-absorption, which is itself a control signal, and it can be analysed '
        'into expenditure and volume causes. With actual rates there is nothing to compare and '
        'no variance can arise.',
        '**They allow budgeting and planning.** Budgets, standard costs and the whole machinery '
        'of Chapters 12 and 13 presuppose a rate fixed in advance.',
        '**They smooth and simplify the accounting**, avoiding monthly recalculation of rates '
        'and giving consistent inventory valuations through the year.',
      ]},
      {'h4': '(b)  Does X\'s lower rate mean X is more efficient?'},
      {'p': '**No — not without a great deal more information.** A lower overhead absorption '
            'rate shows only that the ratio of budgeted overhead to the budgeted absorption base '
            'is lower. Both the numerator and the denominator can differ for reasons that have '
            'nothing to do with efficiency.'},
      {'p': '**Reasons for a lower rate that are unconnected with efficiency:**'},
      {'ol': [
        '**A different absorption base, or a different level of it.** If X budgeted a higher '
        'activity level than Y, the same overhead spread over more hours gives a lower rate — X '
        'is merely busier, or more optimistic.',
        '**A different degree of mechanisation.** A labour-intensive factory has low overhead '
        'and high direct labour cost; a highly automated one has high overhead (depreciation, '
        'power, maintenance) and low labour cost. If X is labour-intensive, its rate per labour '
        'hour will be lower while its **total** cost per unit may well be higher.',
        '**Different cost classification.** If X treats some costs as direct that Y treats as '
        'indirect, X\'s overhead pool is smaller for that reason alone.',
        '**Different ages of plant.** Y\'s newer plant carries more depreciation, raising its '
        'overhead even though the plant may be more productive.',
        '**Different locations and circumstances** — rent, rates, wage rates and energy costs '
        'differ geographically.',
        '**Different accounting policies** — depreciation methods and lives, and the treatment '
        'of service departments.',
      ]},
      {'p': '**What would actually be needed to judge efficiency:**'},
      {'ul': [
        'the **total cost per unit** of comparable output in each factory, not the overhead rate '
        'alone;',
        'each factory\'s overhead **expenditure against its own budget** — that is a measure of '
        'control, whereas the rate is not;',
        'physical measures: output per labour hour, machine utilisation, scrap and rework rates, '
        'idle time;',
        'the **under- or over-absorption** in each factory and its causes.',
      ]},
      {'key': 'A rate is a **ratio**, and a ratio can fall because the numerator fell *or* '
              'because the denominator rose. Factory X might have a lower rate precisely because '
              'it is **less** efficient — if its labour is slow, it books more labour hours, and '
              'the same overhead divided by more hours gives a lower rate per hour. The rate '
              'would fall while the cost per unit rose.'}]}},

    {'eg': {'tag': 'Exam type — Q5.6 (20 marks)',
      't': 'Allocation, apportionment and absorption distinguished; causes of under/over '
           'absorption',
      'q': [
      {'p': '**(a)** Explain the differences between the following terms as used in cost '
            'accounting: (i) allocation of overheads; (ii) apportionment of overheads; '
            '(iii) absorption of overheads *(12 marks)*.'},
      {'p': '**(b)** Explain the reasons for overhead under-absorbed and overhead over-absorbed '
            '*(8 marks)*.'}],
      'a': [
      {'h4': '(a)  The three terms'},
      {'table': {'align': 'llll', 'head': ['', 'Allocation', 'Apportionment', 'Absorption'],
        'rows': [
        ['**What it means**', 'Charging a **whole** item of overhead to **one** cost centre, '
         'because the whole of it was incurred by that centre.',
         'Sharing an item of overhead **between several** cost centres on an equitable basis, '
         'because it was incurred by all of them jointly.',
         'Charging the overhead accumulated in a production cost centre **out to the cost '
         'units** that pass through it, by means of an absorption rate.'],
        ['**When used**', 'When the cost is **wholly identifiable** with one cost centre.',
         'When the cost is **shared** and cannot be identified with one centre.',
         'After allocation and apportionment are complete and all overhead sits in production '
         'cost centres.'],
        ['**Direction**', 'Overhead → one cost centre', 'Overhead → several cost centres',
         'Cost centre → cost units'],
        ['**Example**', 'The salary of the moulding department\'s own supervisor, charged '
         'wholly to moulding.',
         'Factory rent, shared between all departments on floor area.',
         'A job spending 10 hours in moulding is charged 10 × the moulding hourly overhead '
         'rate.'],
        ['**Basis required?**', 'No — the whole amount goes to one place.',
         'Yes — an equitable basis (area, employees, net book value, machine hours…).',
         'Yes — an absorption base (labour hours, machine hours, % of wages…).'],
      ]}},
      {'note': 'The sequence is always the same and is worth memorising as a sentence: '
               '**allocate what you can, apportion what you cannot, reapportion the service '
               'departments, then absorb into units.** Allocation and apportionment both move '
               'cost *between cost centres*; only absorption moves cost *onto the product*.'},
      {'h4': '(b)  Reasons for under- and over-absorption'},
      {'p': 'Overhead is absorbed at a **predetermined** rate — budgeted overhead divided by '
            'budgeted activity — and applied to **actual** activity. A difference from actual '
            'overhead incurred is therefore almost inevitable, and it has exactly two sources:'},
      {'fbox': {'h': 'The two causes', 'rows': [
        {'lb': 'Expenditure difference',
         'tex': '\\text{Budgeted overhead} - \\text{Actual overhead incurred}',
         'nt': 'Actual spending differed from what was budgeted — price rises, unexpected '
               'repairs, savings made, a change in the cost structure.'},
        {'lb': 'Volume difference',
         'tex': '(\\text{Actual activity} - \\text{Budgeted activity}) \\times '
                '\\text{Absorption rate}',
         'nt': 'Actual activity differed from the level on which the rate was built — more or '
               'fewer hours worked or units made than budgeted.'},
      ]}},
      {'p': '**Overhead is UNDER-absorbed when:**'},
      {'ol': [
        '**actual overhead exceeds budgeted overhead** — unforeseen expenditure, price '
        'increases, emergency repairs, higher insurance or energy costs; and/or',
        '**actual activity falls below budgeted activity** — a strike, machine breakdown, '
        'material shortage, power failure, a fall in demand, or an over-optimistic budget — so '
        'fewer hours or units are available to carry the overhead.',
      ]},
      {'p': '**Overhead is OVER-absorbed when:**'},
      {'ol': [
        '**actual overhead falls below budgeted overhead** — economies achieved, a budgeted cost '
        'not in fact incurred, or an over-cautious budget; and/or',
        '**actual activity exceeds budgeted activity** — higher demand, improved efficiency, '
        'extra shifts or overtime, or a conservative activity budget.',
      ]},
      {'p': 'A third, more fundamental cause cuts across both: **an inappropriate absorption '
            'base or an inaccurate budget**. If the base chosen does not reflect what actually '
            'drives overhead in the department, the rate will systematically mis-absorb however '
            'accurately it was computed.'},
      {'key': 'The treatment: whatever the cause, the balance left on the Production Overhead '
              'Control Account is written off to the costing profit and loss account — '
              '**debited** if under-absorbed (profit falls) and **credited** if over-absorbed '
              '(profit rises). It is **not** carried forward and **not** adjusted into inventory '
              'value, because inventory is valued at the predetermined rate.'}]}},

    {'eg': {'tag': 'Exam type — Q5.7 (20 marks) — CACA Management Accounting, June 1981',
      't': 'A single factory-wide rate or separate cost-centre rates; and three methods of '
           'overhead recovery',
      'q': [
      {'p': 'Specify and explain the factors to be considered in determining whether to utilise a '
            'single factory-wide recovery rate for all production overheads, or a separate rate '
            'for each cost centre, production or service department *(12 marks)*.'},
      {'p': '**(a)** Describe **three** methods of determining overhead recovery rates and '
            'specify the circumstances under which each method is superior to the others '
            '*(8 marks)*.'}],
      'a': [
      {'h4': 'Factors in choosing between a blanket rate and departmental rates'},
      {'ol': [
        '**How similar the departments are.** If every department has much the same overhead '
        'per hour and products pass through them in much the same proportions, a single rate '
        'gives almost the same answer as departmental rates and is not worth the extra work. '
        'The greater the variation between departments, the stronger the case for separate '
        'rates (see Q5.2 above, where the two methods differ by 13% on one job).',
        '**How uniform the product range is.** If all products pass through all departments in '
        'the same sequence and proportion, a blanket rate will not distort. If some products '
        'skip departments, or spend much longer in the expensive ones, a blanket rate '
        'systematically over-costs some products and under-costs others.',
        '**The degree of mechanisation, and whether it varies.** A factory with one '
        'machine-intensive and one labour-intensive department cannot absorb both sensibly on '
        'the same base.',
        '**The cost and complexity of operating the system.** Departmental rates need a full '
        'overhead analysis sheet, apportionment bases, reapportionment of service departments, '
        'and separate records of hours by department. The benefit must exceed this cost '
        '(§1.2.12).',
        '**The use to which the cost will be put.** If costs drive pricing of individual jobs, '
        'or decisions to accept or refuse work, accuracy matters and departmental rates are '
        'worth their cost. If they are used only to value total inventory, a blanket rate may '
        'suffice.',
        '**The materiality of overhead** in the total cost. Where overhead is a small fraction '
        'of total cost, even a crude rate cannot distort much; where it dominates, precision '
        'matters.',
        '**The need for cost control and responsibility accounting.** Departmental rates require '
        'overhead to be analysed by cost centre, which is itself the basis for holding each '
        'manager responsible for their own overhead — a blanket rate provides no such analysis.',
        '**The information available.** Departmental rates are impossible without records of '
        'hours by department and a defensible basis for apportioning shared costs.',
      ]},
      {'h4': '(a)  Three methods of determining overhead recovery rates'},
      {'table': {'align': 'lll', 'head': ['Method', 'Formula', 'When it is superior'], 'rows': [
        ['**Direct labour hour rate**',
         '$\\dfrac{\\text{Overhead}}{\\text{Direct labour hours}}$',
         'In **labour-intensive** departments, where overhead is incurred broadly in proportion '
         'to the time people spend working. It is superior to a wages-percentage method because '
         'it is unaffected by differences in wage rates between workers of different grades '
         'doing the same job for the same time.'],
        ['**Machine hour rate**',
         '$\\dfrac{\\text{Overhead}}{\\text{Machine hours}}$',
         'In **machine-intensive** departments, where most of the overhead (depreciation, power, '
         'maintenance, machine insurance, space for the machine) is caused by running machines '
         'rather than by employing people. Superior wherever machine time, not labour time, '
         'drives the cost.'],
        ['**Percentage of direct wages**',
         '$\\dfrac{\\text{Overhead}}{\\text{Direct wages}} \\times 100$',
         'Where hours are **not recorded** and only wage values are available, and where wage '
         'rates within the department are reasonably uniform so that cost is a fair proxy for '
         'time. Simple and cheap, but distorted whenever two workers on different rates spend '
         'the same time on a job.'],
      ]}},
      {'note': 'The other three methods the chapter covers, for completeness: **percentage of '
               'direct material cost** (only defensible where material cost and overhead move '
               'together, which is rare); **percentage of prime cost** (a compromise inheriting '
               'the weaknesses of both the material and wages bases); and the **unit (cost '
               'unit) rate** — overhead ÷ units produced — which is superior only where the '
               'output is a **single homogeneous product**, when it is both the simplest and the '
               'most accurate method available.'}]}},

    {'eg': {'tag': 'Exam type — Q5.8 (20 marks) — ACCA Costing',
      't': 'Procedures for setting predetermined rates, and the purpose of calculating them',
      'q': [
      {'p': '**(a)** Outline the procedures and information required in order to determine a set '
            'of predetermined production overhead absorption rates for a company manufacturing a '
            'range of different products in a factory containing a number of production '
            'departments and several service departments.'},
      {'p': '**(b)** Critically examine the purpose of calculating overhead absorption rates.'}],
      'a': [
      {'h4': '(a)  The procedure, step by step'},
      {'steps': [
        '**Define the cost centres.** Divide the factory into production cost centres and '
        'service cost centres, each with a manager responsible for it.',
        '**Budget the overhead expenditure** for the coming period, item by item, for the '
        'factory as a whole and for each cost centre — using past costs adjusted for known price '
        'changes, planned activity and planned changes in method.',
        '**Allocate** every overhead that is wholly identifiable with one cost centre directly '
        'to it.',
        '**Apportion** the remaining shared overheads to all cost centres on equitable bases '
        '(area, number of employees, net book value of plant, metered usage, and so on), chosen '
        'so that each basis reflects what actually causes the cost.',
        '**Reapportion the service cost centre totals** to the production cost centres, on bases '
        'measuring the service each receives — and where service departments serve each other, '
        'by the repeated distribution, simultaneous equation or elimination method (§5.4).',
        '**Budget the activity level** of each production cost centre — direct labour hours, '
        'machine hours, units or direct wages — at the **normal** level of activity rather than '
        'at full capacity.',
        '**Select the absorption base** for each production cost centre, matched to whether it '
        'is labour- or machine-intensive, and to the records actually available.',
        '**Compute the rate** for each production cost centre: budgeted overhead after '
        'reapportionment ÷ budgeted activity for that centre.',
        '**Review and approve** the rates, and build in a procedure for monitoring the resulting '
        'under- or over-absorption during the period, and for revising the rates if conditions '
        'change materially.',
      ]},
      {'h4': '(a)  Information required'},
      {'ul': [
        'historical overhead costs, analysed by type and by department, as a starting point;',
        'the production budget and sales budget for the coming period;',
        'expected price changes — wage awards, rents, energy, insurance premiums;',
        'the budgeted activity of each cost centre in the chosen base (hours, units, wages);',
        'physical data for the apportionment bases — floor area, number of employees, net book '
        'value and location of plant, metered consumption, machine maintenance hours;',
        'the pattern of service provided by each service department to each other department;',
        'planned changes in product mix, methods, plant or staffing.',
      ]},
      {'h4': '(b)  The purpose of calculating overhead absorption rates — critically examined'},
      {'p': '**The purposes claimed for them:**'},
      {'ol': [
        '**Inventory valuation and profit measurement.** IAS 2 requires inventory to include an '
        'appropriate share of production overhead, so an absorption rate is **unavoidable** for '
        'external reporting.',
        '**Product costing and pricing.** A full cost per unit is needed to set a cost-plus '
        'price and to judge whether current prices cover total cost in the long run.',
        '**Timely job costing**, so that jobs can be costed and invoiced as they are completed '
        'rather than at the year end.',
        '**Cost control**, through the under/over-absorption figure and its analysis into '
        'expenditure and volume causes.',
        '**Decision making and planning** — budgeting, tendering, and assessing the relative '
        'profitability of products.',
      ]},
      {'p': '**The criticisms:**'},
      {'ol': [
        '**The resulting unit cost is arbitrary.** It depends entirely on the apportionment '
        'bases and the absorption base chosen; a different, equally defensible, set of bases '
        'gives a different "cost" for the same product. There is no single true full cost.',
        '**It is of limited use for decisions.** Most short-run decisions — accept or reject a '
        'special order, make or buy, drop a product — turn on **relevant** costs, which are '
        'usually marginal. Fixed overhead absorbed into a unit cost is not avoided by declining '
        'the order, so a decision made on absorbed cost can be simply wrong (Chapter 9).',
        '**It can mislead on profitability.** A product carrying a large apportioned share of '
        'fixed overhead may appear to make a loss and be discontinued — after which the same '
        'fixed overhead is reapportioned onto the remaining products, which then appear less '
        'profitable in turn.',
        '**Absorption on volume-based rates distorts a modern cost structure.** Where overhead '
        'is driven by set-ups, inspections and material handling rather than by volume, '
        'absorbing on labour or machine hours over-costs high-volume products and under-costs '
        'low-volume ones — which is the case for activity-based costing (§5.8).',
        '**It encourages overproduction.** Because absorption costing attaches fixed overhead to '
        'inventory, producing more than can be sold increases reported profit (see Q5.1 above), '
        'which is a perverse incentive.',
        '**It is costly to operate**, and the under/over-absorption it generates needs '
        'explaining to managers who did not cause it.',
      ]},
      {'key': 'A balanced conclusion: absorption rates are **indispensable for inventory '
              'valuation and long-run pricing**, and are required by accounting standards — but '
              'they are a **poor guide to short-run decisions**, which need marginal and '
              'relevant costs, and in a modern overhead-heavy factory they may need refining by '
              'activity-based costing before the resulting product costs can be trusted.'}]}},

    {'eg': {'tag': 'Exam type — Q5.9 (12½ marks)',
      't': 'XYZ Ltd — blanket versus cost-centre rates, and an under-absorption',
      'q': [
      {'p': '**(a)** Distinguish between a **blanket rate** and a **cost centre (multiple) '
            'rate** used for absorbing overheads.'},
      {'p': '**(b)** The following data were provided by XYZ Ltd:'},
      {'stmt': {'t': 'XYZ Ltd — data', 'rows': [
        ['Budgeted labour hours', '', 8500],
        ['Budgeted overheads', '', 'N148,750'],
        ['Actual labour hours', '', 7928],
        ['Actual overheads', '', 'N146,200'],
      ]}},
      {'p': '**Required:** (i) what is the labour hour overhead absorption rate? (ii) what is '
            'the amount of overhead under- or over-absorbed, if any? (iii) produce the overhead '
            'control account for the transactions above; (iv) give the major reason for the '
            'under/over-absorption in (ii).'}],
      'a': [
      {'h4': '(a)  Blanket rate versus cost centre (multiple) rate'},
      {'table': {'align': 'lll', 'head': ['', 'Blanket (single, factory-wide) rate',
        'Cost centre (multiple / departmental) rate'], 'rows': [
        ['**Definition**', 'A **single** overhead absorption rate computed for the factory as a '
         'whole and applied to every product, whichever departments it passes through.',
         'A **separate** rate computed for **each** production cost centre, each product being '
         'charged the rate of every department it actually passes through.'],
        ['**Computation**', 'Total factory overhead ÷ total factory activity.',
         'Each department\'s overhead (after reapportionment of service departments) ÷ that '
         'department\'s own activity.'],
        ['**Accuracy**', 'Crude. Acceptable only where all products pass through all departments '
         'in much the same proportions, and departments have similar overhead per hour.',
         'Much more accurate, because it reflects where the product actually spent its time and '
         'what that department\'s overhead really costs per hour.'],
        ['**Administrative cost**', 'Low — no overhead analysis sheet, no apportionment, no '
         'reapportionment.',
         'High — needs a full analysis sheet, apportionment bases, reapportionment, and hours '
         'recorded by department.'],
        ['**Suitable for**', 'Small factories, single-product businesses, or where overhead is '
         'immaterial.',
         'Multi-department factories making a varied product range, especially where '
         'mechanisation differs between departments.'],
      ]}},
      {'h4': '(b)(i)  Labour hour overhead absorption rate'},
      {'tex': '\\text{OAR} = \\frac{\\text{Budgeted overheads}}'
              '{\\text{Budgeted labour hours}} = \\frac{N148{,}750}{8{,}500} '
              '= N17.50 \\text{ per labour hour}'},
      {'h4': '(b)(ii)  Overhead under- or over-absorbed'},
      {'stmt': {'t': 'Under/over absorption', 'rows': [
        ['Overhead absorbed:  7,928 actual labour hours × N17.50', '', 138740],
        ['Actual overhead incurred', '', 146200],
        ['**Overhead UNDER-absorbed**', '', 7460, '@tt'],
      ]}},
      {'h4': '(b)(iii)  Overhead Control Account'},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Bank / creditors — actual overhead incurred', 146200], ['', 146200, '@tot']],
        'cr': [['Work-in-progress — overhead absorbed (7,928 × N17.50)', 138740],
               ['Costing Profit and Loss — under-absorbed overhead', 7460],
               ['', 146200, '@tot']]}},
      {'h4': '(b)(iv)  The major reason for the under-absorption'},
      {'p': 'The under-absorption is caused almost entirely by a **shortfall in activity**: only '
            '7,928 labour hours were worked against the 8,500 budgeted, so 572 hours\' worth of '
            'overhead was never charged to production. Analysing the N7,460 into its two causes '
            'makes this plain:'},
      {'stmt': {'t': 'Analysis of the N7,460 under-absorption', 'rows': [
        ['**Volume cause:** (7,928 − 8,500 hours) × N17.50', '', -10010],
        ['**Expenditure cause:** budgeted overhead N148,750 − actual N146,200', '', 2550],
        ['**Net under-absorption**', '', -7460, '@tt'],
      ]}},
      {'p': 'So the business actually **spent N2,550 less** than it budgeted — expenditure '
            'control was good — but it **worked 572 fewer hours** than planned, which alone '
            'caused N10,010 of under-absorption. The major reason is therefore **a fall in '
            'activity below the budgeted level**, which might be due to lower demand, machine '
            'breakdowns, labour shortages, absenteeism, material shortages, or an '
            'over-optimistic activity budget.'},
      {'key': 'Note the direction convention. A **debit** balance remaining on the overhead '
              'control account is **under-absorption** — more was spent than was charged out — '
              'and it is written off as an extra expense, reducing profit. Here the account is '
              'balanced by a **credit** of N7,460 to close it, with the matching **debit** going '
              'to the costing profit and loss account.'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Overhead absorption rate (general)', 'tex': 'OAR = \\dfrac{\\text{Budgeted overhead}}'
   '{\\text{Budgeted activity level}}'},
  {'lb': 'OAR — direct labour hour basis', 'tex': 'OAR = \\dfrac{\\text{Budgeted overhead}}'
   '{\\text{Budgeted DLH}}'},
  {'lb': 'OAR — machine hour basis', 'tex': 'OAR = \\dfrac{\\text{Budgeted overhead}}'
   '{\\text{Budgeted machine hours}}'},
  {'lb': 'OAR — cost-percentage bases (DM/DL/prime cost)',
   'tex': 'OAR = \\dfrac{\\text{Budgeted overhead}}{\\text{Budgeted DM, DL or prime cost}} '
   '\\times 100'},
  {'lb': 'Overhead absorbed', 'tex': '\\text{OAR} \\times \\text{Actual quantity of activity '
   'base}'},
  {'lb': 'Cost driver rate (ABC)', 'tex': '\\dfrac{\\text{Activity cost for the pool}}'
   '{\\text{Quantity of cost driver available}}'},
 ],
 'focus':
   'Overheads is usually the single most heavily weighted chapter in the paper, spanning at '
   'least one full Section B question most diets. Master the full allocation → apportionment → '
   'absorption sequence as one pipeline, not three separate topics. For reciprocal service '
   'centres, be able to name which of the three methods a question is asking for and apply only '
   'that one — do not blend figures across methods. Over/under absorption questions almost '
   'always want the write-off-to-P&L treatment named explicitly as "preferred," with a reason.',
 'errors': [
   'Absorbing overhead using the *budgeted* activity level instead of the *actual* activity '
   'level — absorption always uses actual activity against the predetermined (budgeted-derived) '
   'rate.',
   'Forgetting to re-normalise a service centre\'s remaining percentage shares once one of its '
   'reciprocal partners has already been closed out under the elimination method.',
   'Mixing up over-absorption (absorbed > incurred, a credit/favourable position) with under-'
   'absorption (incurred > absorbed).',
   'Using a blanket, factory-wide rate when the question\'s own data shows different cost '
   'centres with clearly different overhead-to-activity ratios — this is exactly the scenario '
   'departmental rates exist to fix.',
   'In ABC, dividing the cost pool by one product\'s driver usage instead of the *total* driver '
   'quantity across all products when finding the cost driver rate.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The assignment of an overhead cost directly to one cost centre, with no sharing, is '
         'called',
    'o': ['apportionment', 'absorption', 'allocation', 'activity-based costing',
          'a blanket rate'],
    'a': 2,
    'w': 'Allocation is direct assignment with no sharing; apportionment shares a cost across '
         'several centres; absorption is the final step, charging overhead into cost units.',
    'src': 'Chapter 5.3', 'sec': '5.3'},
   {'q': 'A cost centre\'s overhead is budgeted at ₵2,400,000 and budgeted machine hours are '
         '480. The overhead absorption rate is',
    'o': ['₵500 per machine hour', '₵5,000 per machine hour', '₵50 per machine hour',
          '₵200 per machine hour', '₵4,800 per machine hour'],
    'a': 1,
    'w': 'OAR = budgeted overhead ÷ budgeted machine hours = 2,400,000 / 480 = ₵5,000/machine '
         'hour.',
    'calc': 'OAR = \\dfrac{2{,}400{,}000}{480} = 5{,}000',
    'src': 'Chapter 5.5', 'sec': '5.5'},
   {'q': 'A department\'s OAR is ₵4 per direct labour hour, and actual direct labour hours '
         'worked during the period were 50,000 against overhead actually incurred of ₵215,000. '
         'The overhead is',
    'o': ['under-absorbed by ₵15,000', 'over-absorbed by ₵15,000', 'exactly absorbed',
          'under-absorbed by ₵200,000', 'over-absorbed by ₵35,000'],
    'a': 0,
    'w': 'Overhead absorbed = 4 × 50,000 = ₵200,000. Incurred ₵215,000 exceeds absorbed by '
         '₵15,000 — under-absorbed.',
    'calc': '(4 \\times 50{,}000) - 215{,}000 = -15{,}000',
    'src': 'Chapter 5.7', 'sec': '5.7'},
   {'q': 'The preferred treatment of overhead under- or over-absorption at the end of a period '
         'is to',
    'o': ['carry it forward to future periods', 'adjust it into the cost of units produced '
          'during the period', 'write it off to the Profit and Loss Account as a period cost',
          'ignore it entirely', 'split it equally between all cost centres'],
    'a': 2,
    'w': 'Writing the balance off to the P&L account as a period cost is explicitly stated as '
         'the most preferred treatment — the other two named alternatives both have real '
         'drawbacks (limited management usefulness, or distorted future performance figures).',
    'src': 'Chapter 5.7', 'sec': '5.7'},
   {'q': 'A single overhead recovery rate applied across an entire factory, rather than '
         'separately for each production cost centre, is called a',
    'o': ['departmental rate', 'blanket rate', 'predetermined rate', 'activity-based rate',
          'marginal rate'],
    'a': 1,
    'w': 'This is the definition of a blanket (factory-wide) overhead recovery rate — generally '
         'not recommended, since different centres consume overhead and drive cost differently.',
    'src': 'Chapter 5.6', 'sec': '5.6'},
   {'q': 'Which method of re-apportioning reciprocal service-centre overheads treats each '
         'centre\'s total overhead as an unknown, solved via a system of equations?',
    'o': ['Elimination method', 'Continuous allotment method', 'Simultaneous equations method',
          'Blanket rate method', 'Activity-based costing'],
    'a': 2,
    'w': 'The simultaneous equations method expresses each reciprocal service centre\'s total '
         'overhead algebraically and solves the resulting equations.',
    'src': 'Chapter 5.4', 'sec': '5.4'},
   {'q': 'In Activity-Based Costing, a "cost driver" is best described as',
    'o': ['the person responsible for approving overhead budgets',
          'any factor that causes a change in the cost of an activity',
          'the total overhead of the whole factory',
          'a synonym for a blanket absorption rate',
          'the department that incurs the least overhead'],
    'a': 1,
    'w': 'CIMA\'s own definition: a cost driver is any factor causing a change in the cost of an '
         'activity — e.g. the number of machine set-ups or material requisitions.',
    'src': 'Chapter 5.8', 'sec': '5.8'},
   {'q': 'Overhead of ₵180,000 is pooled for a "quality control" activity with 60 total '
         'inspections across all products. The cost driver rate is',
    'o': ['₵3,000 per inspection', '₵300 per inspection', '₵1,800 per inspection',
          '₵30,000 per inspection', '₵10,800,000 per inspection'],
    'a': 0,
    'w': 'Cost driver rate = activity cost for the pool ÷ total driver quantity = 180,000 / 60 '
         '= ₵3,000 per inspection.',
    'calc': '\\dfrac{180{,}000}{60} = 3{,}000',
    'src': 'Chapter 5.8', 'sec': '5.8'},
   {'q': 'Budgeted overheads are preferred to actual overheads for setting an absorption rate '
         'mainly because',
    'o': ['actual overheads are always lower', 'actual figures are illegal to use in cost '
          'accounting', 'actual overheads are not known until after the period ends, and actual '
          'activity/price fluctuations would cause large swings in the rate',
          'budgeted figures never need revising', 'HMRC requires budgeted figures only'],
    'a': 2,
    'w': 'Two reasons: actual figures are only available after the period ends (delaying product '
         'costing), and using actual overhead/activity would introduce large fluctuations driven '
         'by price levels and activity swings — budgeted figures reflect stable standards '
         'instead.',
    'src': 'Chapter 5.6', 'sec': '5.6'},
   {'q': 'Overhead is absorbed into a job using an OAR based on direct material cost. This basis '
         'is most appropriate when',
    'o': ['material prices are stable and uniform', 'the factory is highly automated',
          'labour is the dominant cost driver', 'output units are highly non-uniform',
          'the business has no service cost centres'],
    'a': 0,
    'w': 'The direct-material-cost-percentage basis only gives good results when material '
         'prices are stable and uniform; where prices vary a lot, this basis distorts the '
         'absorption rate.',
    'src': 'Chapter 5.5', 'sec': '5.5'},
  ],
  'theory': [
   {'q': 'Explain the differences between the following terms as used in cost accounting: '
         '(i) Allocation of overheads, (ii) Apportionment of overheads, (iii) Absorption of '
         'overheads.',
    'marks': 12,
    'a': [
      {'p': '**(i) Allocation** — assigning an overhead cost that is specifically and wholly '
            'incurred for one cost centre, directly to that centre, with no sharing.'},
      {'p': '**(ii) Apportionment** — sharing an overhead cost incurred for a number of cost '
            'centres (or the whole factory) among the centres that benefit from it, using a fair '
            'and equitable basis such as floor space, headcount or plant value.'},
      {'p': '**(iii) Absorption** — the final step: charging the overhead now sitting in each '
            'production cost centre onto the actual cost units passing through it, using an '
            'overhead absorption rate (OAR) applied to the actual quantity of the chosen '
            'activity base.'},
    ], 'src': 'Chapter 5.3', 'sec': '5.3'},
   {'q': 'Explain the reasons for overhead under-absorption and overhead over-absorption.',
    'marks': 8,
    'a': [
      {'p': 'Both arise from the same root cause: the OAR is set using **budgeted** overhead and '
            '**budgeted** activity, but overhead is absorbed against **actual** activity, while '
            'the overhead actually **incurred** is a separate, independently-varying figure.'},
      {'p': '**Under-absorption** results when actual overhead incurred exceeds overhead '
            'absorbed — e.g. actual activity fell short of budget (so less overhead was '
            'absorbed than planned), or actual overhead expenditure ran above budget.'},
      {'p': '**Over-absorption** results when overhead absorbed exceeds overhead incurred — '
            'e.g. actual activity ran above budget (absorbing more than planned), or actual '
            'overhead expenditure came in below budget.'},
    ], 'src': 'Chapter 5.7', 'sec': '5.7'},
  ]},
}
