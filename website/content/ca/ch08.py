CH = {
 'n': 8,
 't': 'Continuous Operation Costing: Process Costing and Joint Products',
 'brief': 'The costing method for continuous, repetitive production rather than discrete '
          'orders: process costing\'s principles and how it differs from order costing, the '
          'treatment of normal and abnormal process losses/gains, the equivalent-units concept '
          'that lets part-finished work-in-progress share fairly in a period\'s cost, the full '
          'cost-of-production report under both weighted-average and FIFO inventory valuation, '
          'joint products and by-products, the three methods of apportioning joint cost, and '
          'service (operation) costing as the non-specific-order method for service industries.',
 'outcomes': [
   'Explain the meaning and importance of process costing',
   'Explain the areas where process costing is applied',
   'Determine equivalent units and explain their meaning',
   'Treat process losses and wastages',
   'Describe the valuation process in process costing',
   'Determine completed product cost',
   'Explain joint costs and joint products',
   'Understand the various methods of apportioning joint costs to joint products',
   'Explain the accounting treatment of by-products',
   'Determine the total cost of producing joint products',
 ],
 'secs': [
  {'n': '8.1', 't': 'Process costing — principles, application and distinction from order '
   'costing', 'b': [
    {'p': 'Continuous operation costing applies wherever production is **repetitive**, rather '
          'than made to a customer\'s own specification. In manufacturing it takes two forms — '
          '**process costing** and **output/operation costing**; in service organisations, the '
          'equivalent is called **operating (service) costing** (§8.7).'},
    {'def': {'t': 'Process costing', 'd': 'a method used where production follows a series of '
                  'sequential processes, ascertaining the cost of a product or service at each '
                  'stage. It applies where continuous mass production is possible.'}},
    {'key': 'Because output is continuous and uniform, it is neither possible nor necessary to '
            'tie a particular unit of output to a particular moment of manufacture — the cost '
            'of any one unit is taken as the **average cost of manufacture over the period**. '
            'This average is complicated by two things every process-costing question must '
            'handle: apportioning cost between completed output and unfinished production at '
            'period end, and accounting for wastage.'},
    {'p': 'Industries using process costing: food processing, paper milling, chemicals and '
          'drugs, oil refining, soap making, textiles, box-making, paint and ink, brewing, '
          'flour milling, bottling/canning, biscuits, meat products, sugar making — arguably '
          '**the most widely used cost accounting system in the world**.'},
    {'p': 'Common features across most process costing systems:'},
    {'ol': [
      'expenditure for each cost centre is collected, and at period end the cost of completed '
      'units transfers to an inventory account or to the next process cost centre;',
      'accurate records of units produced and part-produced (and their cost) are essential;',
      'the cost unit chosen should be relevant to the organisation;',
      'the output of one process becomes the raw material **input** of the next — so a process '
      'cost centre\'s cost includes the transferred-in cost from the previous process, plus its '
      'own materials, labour and overhead; and',
      'wastage (scrap, chemical reaction, evaporation) is unavoidable, but should be minimised '
      'by good operating practice.',
    ]},
    {'note': 'Either the main product or a by-product may need further processing before it can '
             'be sold.'},

    {'h4': 'Process costing versus order costing'},
    {'p': 'These are two extreme systems of product costing. Both, fundamentally, are an '
          '**averaging process**: unit cost = accumulated cost ÷ production level. The real '
          'difference is the **size of the denominator**.'},
    {'table': {'align': 'll', 'head': ['', 'Order costing', 'Process costing'], 'rows': [
      ['Denominator (activity level)', 'Small — one bridge, one hundred copies of a book',
       'Large — thousands of litres, thousands of bags'],
      ['Typical industries', 'Construction, printing, furniture-making, aircraft, machinery, '
       'shoe-making — tailor-made/unique goods', 'Chemicals, oil, textiles, plastics, paints, '
       'flour milling, canneries, rubber, food processing, glass-making, mining, cement, meat '
       'processing — mass production of identical units passing through uniform steps'],
    ]}},

    {'h4': 'Production stages'},
    {'p': 'Output of one process automatically becomes the input of the next. An intermediate '
          'product is progressively processed — further material, labour and overhead added at '
          'each stage — until finished goods emerge and move to the warehouse. At **each** '
          'process, unit cost = total output cost ÷ total units produced at that stage: Process '
          'A → Process B → Process C → … → Finished Goods.'},
  ]},

  {'n': '8.2', 't': 'Process losses, wastages, and gains', 'b': [
    {'p': 'In many industries, process output is less than the material input — a **process '
          'loss (wastage)**, from evaporation, scrap, shrinkage, unavoidable handling, breakage, '
          'etc.'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning and treatment'], 'rows': [
      ['**Normal process loss**', 'Unavoidable, arising from the nature of the process itself, '
       'under efficient operating conditions — so it can be estimated with reasonable accuracy. '
       'It is logical and equitable to fold its cost **into the cost of good production**, '
       'since achieving good units necessarily entails this loss.'],
      ['**Abnormal process loss**', 'Loss **above** the normal, expected level — unpredictable, '
       'from causes like plant breakdown, inefficient working or defective materials. Charged '
       '**to the Profit and Loss Account**, not to good production: the Process Account is '
       'credited, the Abnormal Loss Account is debited, then closed to P&L.'],
      ['**Abnormal gain**', 'Where actual loss is **less** than the normal (estimated) loss. The '
       'Abnormal Gain Account is credited, the Process Account debited; the Abnormal Gain '
       'Account is closed to the **credit** of P&L.'],
    ]}},
    {'key': 'Abnormal loss/gain is always **actual loss vs. normal (estimated) loss** — never '
            'actual vs. actual, and never confused with the physical difference between input '
            'and expected output.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.1 — accounting for process wastage',
      'open': True, 'q': [
      {'p': 'TMR produces 100 units of output from 120 units of input material costing N27,000, '
            'plus conversion cost N13,000. Normal wastage was set in advance at 5% of input. '
            'Wastage can be sold at N50/kg. Find: (a) cost per unit of expected output, '
            '(b) production cost of the output achieved, (c) the cost of abnormal loss/gain.'}],
      'a': [
      {'p': 'Normal wastage $= 5\\% \\times 120 = 6$ units, valued at $6 \\times 50 = N300$.'},
      {'table': {'align': 'lrr', 'head': ['', 'Units (kg)', 'Cost (N)'], 'rows': [
        ['Input (material + conversion)', '120', '40,000'],
        ['Less: normal wastage (5%, at scrap value)', '(6)', '(300)'],
        ['**Expected output**', '**114**', '**39,700**'],
      ]}},
      {'tex': '\\text{(a) Cost per unit of expected output} = \\dfrac{39{,}700}{114} = '
              'N348.25'},
      {'tex': '\\text{(b) Production cost of output achieved} = 100 \\times 348.25 = N34{,}824.6'},
      {'p': '**(c)** Abnormal loss $= 114 - 100 = 14$ units (expected output that failed to '
            'materialise) $= 14 \\times 348.25 = N4{,}875.44$.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.2 — the Process Account and Abnormal '
      'Wastage Account', 'open': True, 'q': [
      {'p': 'Using Illustration 8.1\'s figures, prepare the Process Account and Abnormal Wastage '
            'Account.'}],
      'a': [
      {'table': {'align': 'lrrlrr', 'head': ['Dr.', 'Kg', 'N', 'Cr.', 'Kg', 'N'], 'rows': [
        ['Material', '120', '27,000', 'Good production', '100', '34,825'],
        ['Conversion', '', '13,000', 'Normal wastage', '6', '300'],
        ['', '', '', 'Abnormal wastage', '14', '4,875'],
        ['**Total**', '**120**', '**40,000**', '**Total**', '**120**', '**40,000**'],
      ]}},
      {'table': {'align': 'lrlr', 'head': ['Dr. — Abnormal Wastage Account', 'N', 'Cr.', 'N'],
        'rows': [
        ['Process A/c', '4,875', 'Profit & Loss', '4,875'],
      ]}}]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.3 — cost flowing through three sequential '
      'processes', 'open': True, 'q': [
      {'p': 'A product passes through Processes A, B and C; 1,000 litres were produced in the '
            'period, with no opening or closing WIP:'},
      {'table': {'align': 'lrrr', 'head': ['', 'Process A (N)', 'Process B (N)',
        'Process C (N)'], 'rows': [
        ['Materials', '40,000', '15,000', '5,000'], ['Labour', '20,000', '25,000', '15,000'],
        ['Direct overhead', '5,000', '3,000', '3,000'],
      ]}},
      {'p': 'Indirect overhead of N30,000 for the period is apportioned to the processes on the '
            'basis of wages (A 20,000, B 25,000, C 15,000 — total 60,000). Find the cost of '
            'output transferred to finished goods, and the cost per litre.'}],
      'a': [
      {'p': 'Indirect overhead apportioned: A $= \\tfrac{20{,}000}{60{,}000} \\times 30{,}000 = '
            'N10{,}000$; B $= \\tfrac{25{,}000}{60{,}000} \\times 30{,}000 = N12{,}500$; '
            'C $= \\tfrac{15{,}000}{60{,}000} \\times 30{,}000 = N7{,}500$.'},
      {'table': {'align': 'lrrr', 'head': ['Cost/litre build-up', 'Process A', 'Process B',
        'Process C'], 'rows': [
        ['Transferred in', '—', '75.00', '130.50'],
        ['Materials', '40.00', '15.00', '5.00'],
        ['Labour', '20.00', '25.00', '15.00'],
        ['Direct overhead', '5.00', '3.00', '3.00'],
        ['Indirect overhead', '10.00', '12.50', '7.50'],
        ['**Cost/litre transferred onward**', '**75.00**', '**130.50**', '**161.00**'],
      ]}},
      {'p': 'Total cost of output transferred to finished goods $= 1{,}000 \\times N161 = '
            'N161{,}000$.'},
      {'note': 'Indirect expenses (administrative, selling, distribution — anything that cannot '
               'be directly traced to the process) must be recovered in the selling price too: '
               'the N161/litre found here is **cost**, so the selling price must exceed it for '
               'the business to earn any profit.'}]}},
  ]},

  {'n': '8.3', 't': 'Equivalent units', 'b': [
    {'p': 'At period end, some units are inevitably only part-finished (WIP). Part of the '
          'period\'s cost belongs to these part-finished units as well as the fully completed '
          'ones — the **equivalent units** concept spreads cost equitably between them.'},
    {'def': {'t': 'Equivalent units', 'd': 'the number of fully-completed units that a given '
                  'quantity of partly-completed work represents, given its percentage of '
                  'completion.'}},
    {'tex': '\\text{Total equivalent production} = \\text{Completed units} + (\\%\\text{ '
            'complete} \\times \\text{Partly completed units})'},
    {'tex': '\\text{Cost per unit} = \\dfrac{\\text{Total costs}}{\\text{Total equivalent '
            'production (units)}}'},
    {'key': 'Material, labour and overhead are usually **not** equally complete in the same '
            'WIP — material might be 80% in while labour is only 60% and overhead 50% — so each '
            'cost **element** is normally given its own equivalent-units calculation and its '
            'own cost-per-unit, and the three are added together to price one complete unit.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.4 — equivalent units by cost element',
      'open': True, 'q': [
      {'p': 'Elsemco Shoemakers, January: materials N422,400, labour N395,600, overhead '
            'N225,000 (total N1,043,000). 8,000 units fully completed; 2,000 units WIP, '
            '80% complete on material, 60% on labour, 50% on overhead. Find the value of '
            'completed production and of WIP.'}],
      'a': [
      {'table': {'align': 'lrrrrr', 'head': ['Element', 'WIP equiv. units', 'Fully compl. '
        'units', 'Total equiv. production', 'Total cost (N)', 'Cost/unit (N)'], 'rows': [
        ['Material (80% of 2,000)', '1,600', '8,000', '9,600', '422,400', '44'],
        ['Labour (60% of 2,000)', '1,200', '8,000', '9,200', '395,600', '43'],
        ['Overhead (50% of 2,000)', '1,000', '8,000', '9,000', '225,000', '25'],
        ['**Total**', '', '', '', '**1,043,000**', '**112**'],
      ]}},
      {'tex': '\\text{Value of completed production} = 112 \\times 8{,}000 = N896{,}000'},
      {'tex': '\\text{Value of WIP} = \\text{Total cost} - \\text{Value of completed} = '
              '1{,}043{,}000 - 896{,}000 = N147{,}000'},
      {'p': '**Cross-check** — WIP value from its own equivalent units: material '
            '$1{,}600 \\times 44 = N70{,}400$; labour $1{,}200 \\times 43 = N51{,}600$; overhead '
            '$1{,}000 \\times 25 = N25{,}000$; total $= N147{,}000$ — exactly matches.'},
      {'key': 'The output of one process is the input **material** cost of the next, and — '
              'because it has physically arrived there — is always **100% complete** by that '
              'measure the instant it enters the next process. Any brand-new material the next '
              'process itself adds must be shown as a **separate** cost element, never merged '
              'into the transferred-in cost.'}]}},
  ]},

  {'n': '8.4', 't': 'The cost of production report — weighted average and FIFO', 'b': [
    {'p': 'Building a process cost-of-production report follows five stages: (1) the physical '
          'flow of units (total units to be accounted for, regardless of completion); (2) their '
          'equivalent units, usually split into transferred-in, material and conversion '
          '(labour + overhead) cost elements, since completion can differ between them; (3) '
          'total and *current-period* equivalent units for each element; (4) unit cost, per the '
          'inventory-valuation method assumed (**FIFO** or **Weighted Average Price/WAP**); and '
          '(5) the total cost of units transferred out and of closing WIP, with every cost fully '
          'accounted for.'},
    {'table': {'align': 'll', 'head': ['Method', 'How it treats opening WIP'], 'rows': [
      ['**Weighted Average Price (WAP)**', 'Blends opening WIP\'s cost together with the '
       'current period\'s cost, and spreads the combined total over the combined (opening WIP '
       '+ current-period) equivalent units — it does not distinguish when cost was incurred.'],
      ['**FIFO**', 'Assumes opening WIP is finished and transferred out **first**. Current-'
       'period cost is divided only by **current-period** equivalent units (total equivalent '
       'units *less* the equivalent units already present in opening WIP), so the unit cost '
       'reflects only this period\'s own cost, not a blend with the prior period\'s.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.5 — a full two-process cost of production '
      'report, WAP and FIFO', 'open': True, 'q': [
      {'p': 'Savannah Sugar Co.: Process 1 introduces raw material at the start; Process 2 adds '
            'further material only at the very **end**. Conversion cost accrues uniformly '
            'through both processes. For June:'},
      {'table': {'align': 'lrr', 'head': ['', 'Process 1', 'Process 2'], 'rows': [
        ['Opening WIP (units)', '35,000', '42,000'],
        ['Opening WIP cost — material / transferred-in', 'N210,000', 'N343,000'],
        ['Opening WIP cost — conversion (% complete)', 'N52,500 (2/5)', 'N392,000 (2/3)'],
        ['Units completed in June', '168,000', '154,000'],
        ['Units commenced/transferred in during June', '140,000', '168,000'],
        ['Closing WIP (units, % complete on conversion)', '7,000 (1/2)', '56,000 (3/8)'],
        ['Material introduced in June', 'N770,000', 'N462,000'],
        ['Conversion cost added in June', 'N630,000', 'N2,205,000'],
      ]}},
      {'p': 'Prepare the cost of production report for both processes, using both WAP and FIFO, '
            'showing the cost of finished output and of closing WIP.'}],
      'a': [
      {'h4': 'Process 1 — Weighted Average'},
      {'p': 'Units to account for $= 35{,}000 + 140{,}000 = 175{,}000 = 168{,}000$ completed '
            '$+ 7{,}000$ closing WIP.'},
      {'table': {'align': 'lrr', 'head': ['', 'Material equiv. units', 'Conversion equiv. '
        'units'], 'rows': [
        ['Completed & transferred out', '168,000', '168,000'],
        ['Closing WIP (100% material, ½ conversion)', '7,000', '3,500'],
        ['**Total equivalent units (TEU)**', '**175,000**', '**171,500**'],
      ]}},
      {'table': {'align': 'lrrr', 'head': ['Element', 'Opening WIP cost + Current cost',
        'TEU', 'Cost/unit'], 'rows': [
        ['Material', '210,000 + 770,000 = 980,000', '175,000', 'N5.60'],
        ['Conversion', '52,500 + 630,000 = 682,500', '171,500', 'N3.98'],
        ['**Total**', '**1,662,500**', '', '**N9.58**'],
      ]}},
      {'tex': '\\text{Cost of units completed} = 168{,}000 \\times 9.58 = N1{,}609{,}440'},
      {'p': 'Closing WIP $= (7{,}000\\times1\\times5.60) + (7{,}000\\times0.5\\times3.98) = '
            'N39{,}200 + N13{,}930 = N53{,}130$.'},
      {'note': 'Checking by the shortcut $\\text{Total cost} - \\text{Cost of completed} = '
               '1{,}662{,}500 - 1{,}609{,}440 = N53{,}060$ instead — a N70 gap. The study text '
               'flags this itself as rounding error from carrying unit costs to only 2 decimal '
               'places (5.60 and 3.98 are themselves rounded); it is not a computational mistake '
               'to chase further, and is a useful real-world reminder that the two "equally '
               'valid" ways of finding closing WIP (direct computation vs. the balancing '
               'difference) can disagree slightly once rounding enters the picture.'},
      {'h4': 'Process 1 — FIFO'},
      {'p': 'Current equivalent units (this period\'s own work only) $= $ TEU $-$ opening WIP\'s '
            'own equivalent units: material $175{,}000 - 35{,}000(100\\%) = 140{,}000$; '
            'conversion $171{,}500 - 35{,}000\\times\\tfrac25(14{,}000) = 157{,}500$.'},
      {'table': {'align': 'lrrr', 'head': ['Element', 'Current cost', 'Current equiv. units',
        'Cost/unit'], 'rows': [
        ['Material', '770,000', '140,000', 'N5.50'],
        ['Conversion', '630,000', '157,500', 'N4.00'],
      ]}},
      {'p': 'Closing WIP $= (7{,}000\\times1\\times5.50) + (7{,}000\\times0.5\\times4.00) = '
            'N38{,}500 + N14{,}000 = N52{,}500$.'},
      {'tex': '\\text{Cost of units completed} = \\text{Total cost} - \\text{Closing WIP} = '
              '1{,}662{,}500 - 52{,}500 = N1{,}610{,}000'},
      {'h4': 'Process 2 — Weighted Average'},
      {'p': 'Because Process 2 adds its own material only at the very **end**, no unit still in '
            'WIP (not yet at the end) has received any of it — WIP\'s material equivalent units '
            'are always **0**, however far through conversion it is.'},
      {'p': 'Units to account for $= 42{,}000 + 168{,}000 \\text{ (transferred in)} = 210{,}000 '
            '= 154{,}000$ completed $+ 56{,}000$ closing WIP.'},
      {'table': {'align': 'lrrr', 'head': ['', 'Transferred-in equiv.', 'Material equiv.',
        'Conversion equiv.'], 'rows': [
        ['Completed & transferred out', '154,000', '154,000', '154,000'],
        ['Closing WIP (100% transferred-in, 0% material, ⅜ conversion)', '56,000', '0',
         '21,000'],
        ['**TEU**', '**210,000**', '**154,000**', '**175,000**'],
      ]}},
      {'table': {'align': 'lrrr', 'head': ['Element', 'Opening WIP + Current cost', 'TEU',
        'Cost/unit'], 'rows': [
        ['Transferred in', '343,000 + 1,609,440 = 1,952,440', '210,000', 'N9.2973'],
        ['Material', '0 + 462,000 = 462,000', '154,000', 'N3.0000'],
        ['Conversion', '392,000 + 2,205,000 = 2,597,000', '175,000', 'N14.8400'],
        ['**Total**', '**5,011,440**', '', '**N27.1373**'],
      ]}},
      {'tex': '\\text{Cost of units completed} = 154{,}000 \\times 27.1373 \\approx '
              'N4{,}179{,}144.20'},
      {'p': 'Closing WIP $= (56{,}000\\times9.2973) + 0 + (56{,}000\\times0.375\\times14.84) '
            '\\approx N520{,}648.80 + N311{,}640.00 = N832{,}288.80$ (versus the balancing '
            'figure $5{,}011{,}440 - 4{,}179{,}144.20 = N832{,}295.80$ — again a small, flagged '
            'rounding gap, this time N7, from the 4-decimal-place unit costs).'},
      {'h4': 'Process 2 — FIFO'},
      {'warn': 'The study text\'s own FIFO working for Process 2 uses **N1,609,440** as the '
               'current-period transferred-in cost — but that figure is Process 1\'s **WAP**-'
               'method completed-units value, not Process 1\'s own FIFO value of **N1,610,000** '
               'computed two paragraphs earlier in the very same illustration. This looks like a '
               'genuine authoring inconsistency in the source (reusing the WAP figure where the '
               'FIFO one belongs), not an OCR artefact — both numbers are printed clearly and '
               'repeatedly. It is reproduced below exactly as the source has it, flagged rather '
               'than silently corrected, since changing it would mean re-deriving figures the '
               'source itself never actually shows.'},
      {'table': {'align': 'lrrr', 'head': ['Element', 'Current cost', 'Current equiv. units',
        'Cost/unit'], 'rows': [
        ['Transferred in (as printed in the source — see warning above)', '1,609,440', '168,000',
         'N9.58'],
        ['Material', '462,000', '154,000', 'N3.00'],
        ['Conversion', '2,205,000', '147,000', 'N15.00'],
        ['**Total**', '', '', '**N27.58**'],
      ]}},
      {'p': 'Closing WIP $= (56{,}000\\times9.58) + 0 + (56{,}000\\times0.375\\times15.00) = '
            'N536{,}480 + N315{,}000 = N851{,}480$.'},
      {'tex': '\\text{Cost of units completed} = \\text{Total cost} - \\text{Closing WIP} = '
              '5{,}011{,}440 - 851{,}480 = N4{,}159{,}960'},
      {'note': 'Because this last step subtracts the closing-WIP figure from the **actual total '
               'cost pool** (which does not depend on which transferred-in figure was used '
               'earlier), the final completed-units cost of N4,159,960 still reconciles exactly '
               'with an independent build-up (below) — the flagged inconsistency affects only '
               'the intermediate per-unit-rate display, not the final answer.'},
      {'h4': 'Process 2 FIFO — cross-check by the "opening WIP completion + newly-started-and-'
       'finished" build-up'},
      {'p': 'Opening WIP brought-forward cost: N343,000 + N392,000 = N735,000. Completing it '
            'this period needs its full material share ($42{,}000\\times3.00=N126{,}000$) and '
            'its remaining $\\tfrac13$ of conversion ($42{,}000\\times\\tfrac13\\times15.00='
            'N210{,}000$). Units started **and** completed this period: '
            '$154{,}000-42{,}000=112{,}000$, costed fully at this period\'s own rate '
            '($112{,}000\\times27.58 = N3{,}088{,}960$).'},
      {'tex': '735{,}000 + 126{,}000 + 210{,}000 + 3{,}088{,}960 = N4{,}159{,}960'},
      {'key': 'This matches the shortcut answer exactly — confirming N4,159,960 is right '
              'regardless of the transferred-in-cost inconsistency flagged above.'}]}},
  ]},

  {'n': '8.5', 't': 'Joint products and by-products', 'b': [
    {'def': {'t': 'Joint products', 'd': 'two or more products that result simultaneously from '
                  'processing a **single** raw material — e.g. refining crude oil yields petrol, '
                  'kerosene and gas together.'}},
    {'def': {'t': 'Joint cost', 'd': 'the cost of processing an input up to the point the joint '
                  'products emerge — restricted to the **split-off (separation) point**, after '
                  'which each product may incur its own separate processing cost. Joint cost '
                  'cannot be traced to any one product; it belongs to the whole group.'}},
    {'p': 'In practice, one product is usually identified as the **main/principal product**, '
          'with the rest treated as joint products or **by-products**. A rough classification, '
          'by each product\'s cost/sales value **relative to the main product**:'},
    {'table': {'align': 'll', 'head': ['Relative value', 'Classification'], 'rows': [
      ['10%–15% of main product\'s cost', '**By-product**'],
      ['15%–40% of main product\'s cost', '**Joint product**'],
      ['Above 40% of main product\'s cost', 'Treated as a **main product** in its own right'],
    ]}},
    {'note': 'This is only a guideline, not a fixed law — price changes over time can move a '
             'product between categories (a by-product can become a joint product, or even a '
             'main product, and vice versa).'},

    {'h4': 'Accounting treatment of by-products'},
    {'p': 'A by-product\'s market value, less its own separate processing cost after split-off, '
          'is usually negligible next to the joint products\' or main product\'s total value. '
          'The standard treatment: deduct the by-product\'s **Net Realisable Value (NRV)** from '
          'the total joint cost, then share only the **remaining, net** joint cost among the '
          'main/joint products.'},
    {'def': {'t': 'Net Realisable Value (NRV) — for a by-product', 'd': 'its market value less '
                  'its own separate processing cost after the split-off point.'}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.6 — deducting a by-product\'s NRV before '
      'sharing joint cost', 'open': True, 'q': [
      {'p': 'Wambai Shoemakers: a process yields main products A and B plus by-product C, total '
            'cost N3,000,000. There are 1,000 units of C, needing no further processing, each '
            'sellable at N60 (negligible market cost). A and B share the joint cost equally. '
            'Find A\'s share of the joint cost.'}],
      'a': [
      {'p': 'NRV of C $= 1{,}000 \\times 60 = N60{,}000$ (its market cost is negligible, so '
            'market value $\\approx$ NRV).'},
      {'tex': '\\text{Net Joint Cost} = 3{,}000{,}000 - 60{,}000 = N2{,}940{,}000'},
      {'tex': '\\text{Share of Product A} = \\dfrac{2{,}940{,}000}{2} = N1{,}470{,}000'},
      {'key': 'Deducting a by-product\'s NRV from the joint cost is, in effect, treating the '
              'by-product\'s own share of the joint cost as **equal to its NRV** — no further, '
              'separate allocation step is needed for it.'}]}},
  ]},

  {'n': '8.6', 't': 'Methods of apportioning joint cost', 'b': [
    {'p': 'Three popular ways to share joint cost among joint (or main) products:'},

    {'h4': '(a) Physical units basis'},
    {'p': 'Joint cost is shared in proportion to each product\'s **physical quantity**, provided '
          'all products share a common unit of measurement (kg, litres). Its weakness: it '
          'ignores **value** entirely, even though value is usually the most important factor.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.7 — physical units basis', 'open': True,
      'q': [
      {'p': 'Anadariya Ltd processes three products K (5,000kg), S (3,000kg), T (2,000kg) from '
            'one input, total joint cost N1,000,000 to split-off. Apportion by physical units '
            'and find each unit cost.'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['Product', 'Kg', 'Ratio', 'Share of JC (N)'],
        'rows': [
        ['K', '5,000', '50%', '500,000'], ['S', '3,000', '30%', '300,000'],
        ['T', '2,000', '20%', '200,000'], ['**Total**', '**10,000**', '**100%**',
         '**1,000,000**'],
      ]}},
      {'p': 'Unit cost: K $= 500{,}000/5{,}000 = N100$; S $= 300{,}000/3{,}000 = N100$; T $= '
            '200{,}000/2{,}000 = N100$.'},
      {'key': 'Under the physical units basis, **every product ends up costed at exactly the '
              'same rate per unit** (here, N100/unit for all three) — a direct, numerical '
              'demonstration of why the method is criticised for ignoring value: it cannot, by '
              'construction, ever produce different unit costs for products with different '
              'market values.'}]}},

    {'h4': '(b) Sales value at the point of separation'},
    {'p': 'Joint cost is shared in proportion to each product\'s estimated market value at '
          '**split-off**, before any further processing. Two problems: a product might have '
          'zero value at split-off but real value after modest further processing; and a '
          'product might have a high split-off value but incur heavy selling/distribution cost '
          'afterward, which this method ignores.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.8 — sales value at split-off', 'open': True,
      'q': [
      {'p': 'Same data, but with estimated split-off selling prices K N400/unit, S N440/unit, '
            'T N340/unit. Apportion joint cost by sales value.'}],
      'a': [
      {'table': {'align': 'lrrrr', 'head': ['Product', 'Units', 'SP/unit (N)', 'Sales value (N)',
        'Share of JC (N)'], 'rows': [
        ['K', '5,000', '400', '2,000,000', '500,000'],
        ['S', '3,000', '440', '1,320,000', '330,000'],
        ['T', '2,000', '340', '680,000', '170,000'],
        ['**Total**', '', '', '**4,000,000**', '**1,000,000**'],
      ]}},
      {'p': 'Unit cost: K $= 500{,}000/5{,}000 = N100$; S $= 330{,}000/3{,}000 = N110$; T $= '
            '170{,}000/2{,}000 = N85$ — genuinely different unit costs this time, since value '
            'now drives the split.'}]}},

    {'h4': '(c) Net Realisable Value (NRV) basis'},
    {'p': 'Used when further processing (or heavy marketing/distribution cost) is involved. Net '
          'realisation = sales value **less** the incremental cost of further processing after '
          'split-off and any other selling/distribution cost.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 8.9 — NRV basis', 'open': True, 'q': [
      {'p': 'Same sales values, now assumed to be market prices **after** further processing, '
            'with separate processing/marketing costs K N200,000, S N300,000, T N160,000. '
            'Apportion joint cost by NRV and find unit costs.'}],
      'a': [
      {'table': {'align': 'lrrrrr', 'head': ['Product', 'Sales value (N)', 'Separate '
        'processing cost (N)', 'NRV (N)', 'Share of JC (N)', 'Unit cost (N)'], 'rows': [
        ['K', '2,000,000', '200,000', '1,800,000', '538,922', '108'],
        ['S', '1,320,000', '300,000', '1,020,000', '305,389', '102'],
        ['T', '680,000', '160,000', '520,000', '155,689', '78'],
        ['**Total**', '**4,000,000**', '', '**3,340,000**', '**1,000,000**', ''],
      ]}},
      {'p': 'Each product\'s share of joint cost is proportional to its own NRV over the total '
            'NRV pool, e.g. K $= \\tfrac{1{,}800{,}000}{3{,}340{,}000} \\times 1{,}000{,}000 '
            '\\approx N538{,}922$.'},
      {'key': 'The NRV basis is regarded as the **best** of the three methods, because it is '
              'the only one that accounts for quantity produced, sales value **and** further '
              'processing cost, all together — the physical-units basis ignores value entirely, '
              'and the plain sales-value basis ignores further processing cost.'}]}},

    {'h4': 'Total cost determination using the NRV method'},
    {'p': 'A joint product\'s **total** cost is its share of joint cost **plus** its own further '
          'processing/marketing cost — total cost ÷ units produced gives total cost per unit, '
          'which (unlike the NRV-basis unit cost above) is what should value closing inventory.'},
    {'eg': {'tag': 'Study text', 't': 'Continuing Illustration 8.9 — total unit cost and closing '
      'inventory valuation', 'open': True, 'q': [
      {'p': 'Find each product\'s total cost per unit, and the value of closing inventory of '
            '900 units of K, 500 of S and 400 of T.'}],
      'a': [
      {'table': {'align': 'lrrrr', 'head': ['Product', 'Share of JC (N)', 'Further processing '
        'cost (N)', 'Total cost (N)', 'Total cost/unit (N)'], 'rows': [
        ['K', '538,922', '200,000', '738,922', '147.78'],
        ['S', '305,389', '300,000', '605,389', '201.80'],
        ['T', '155,689', '160,000', '315,689', '157.84'],
      ]}},
      {'table': {'align': 'lrrr', 'head': ['Product', 'Closing units', 'Cost/unit (N)',
        'Value (N)'], 'rows': [
        ['K', '900', '147.78', '133,002'],
        ['S', '500', '201.80', '100,900'],
        ['T', '400', '157.84', '63,136'],
        ['**Total**', '', '', '**297,038**'],
      ]}},
      {'note': 'Profit on a joint product is always total revenue (sales value) less **this** '
               'total cost — the ordinary economic principle of profit applies exactly the same '
               'way in joint-product costing as anywhere else.'}]}},
  ]},

  {'n': '8.7', 't': 'Non-specific order costing: service costing', 'b': [
    {'p': 'Service (operation) costing applies costing principles to services rather than '
          'physical goods — hotels, transport, airlines, schools — and can also apply to a '
          '**service cost centre inside a manufacturing business** (e.g. deciding whether to '
          'run an in-house haulage department or sub-contract it, which needs a reliable '
          'in-house cost figure to compare against). The principle is the same as anywhere '
          'else: classify and aggregate every expense of providing the service, then average '
          'over the total number of service units to find cost per unit.'},
    {'p': 'A transport business\'s cost statement:'},
    {'table': {'align': 'll', 'head': ['Category', 'Items'], 'rows': [
      ['**Fixed (standing) charges**', 'Motor insurance; motor licence; driver\'s remuneration; '
       'general administration — incurred **regardless of distance covered**.'],
      ['**Running costs**', 'Fuel; servicing; lubricants; repairs and maintenance.'],
    ]}},
    {'p': 'A canteen\'s cost statement instead compares **actual vs. budget**, across wages/'
          'salaries (supervisor, cooks, counter helpers), provisions (meat, fish/poultry, '
          'vegetables/fruit, eggs, coffee, miscellaneous), maintenance (crockery/glassware, '
          'insurance, table linen), rent, and deducts income from sales and any company subsidy.'},

    {'h4': 'The cost unit problem'},
    {'p': 'Service costing\'s central difficulty is choosing the right **cost unit** to measure '
          'output — a transport business might measure in kilometres travelled, weight carried, '
          'or a combination of both. Other examples:'},
    {'table': {'align': 'll', 'head': ['Service', 'Cost unit'], 'rows': [
      ['Hotel', 'Occupied room-day'], ['Restaurant', 'Meal served'],
      ['College', 'Full-time equivalent student'], ['Electricity', 'Kilowatt-hour'],
      ['Hospital', 'Patient-day'], ['Transport', 'Miles/kilometres travelled'],
    ]}},

    {'h4': 'Costing professional services'},
    {'p': 'For architects, accountants, tax practitioners, medical doctors and similar '
          'professional offices, services **differ from one client to another** — unlike a '
          'standardised service organisation. This means **job costing**, not standard service '
          'costing, is the appropriate method here — each client engagement is costed as its '
          'own distinct job.'},
  ]},

  {'n': '8.8', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§8.1 Process costing** — continuous/mass production; unit cost is a period average, '
      'not tied to one moment; differs from order costing chiefly in the **size of the '
      'denominator** (small for order costing, large for process costing); one process\'s '
      'output is the next process\'s material input.',
      '**§8.2 Losses/gains** — normal loss (uncontrollable, folded into good production\'s '
      'cost) vs abnormal loss (charged to P&L, Process A/c credited, Abnormal Loss A/c '
      'debited) vs abnormal gain (actual loss less than normal — Abnormal Gain A/c credited, '
      'closed to P&L\'s credit); cost flows process-to-process with indirect overhead '
      'apportioned by an appropriate basis (e.g. wages).',
      '**§8.3 Equivalent units** — completed units + (% complete × part-finished units), '
      'computed **separately per cost element** since material/labour/overhead completion '
      'often differ; transferred-in cost is always 100% complete on arrival.',
      '**§8.4 Cost of production report** — WAP blends opening-WIP and current cost together '
      'over combined equivalent units; FIFO uses only *current-period* cost over *current-'
      'period* equivalent units, assuming opening WIP is finished and out first; both methods\' '
      'closing-WIP figure can be cross-checked two ways (direct computation vs. total-cost-'
      'minus-completed), which can disagree slightly from rounding — not a sign of a mistake.',
      '**§8.5 Joint products/by-products** — one raw material, multiple simultaneous products; '
      'joint cost stops at the split-off point; rough classification by relative value '
      '(<15% by-product, 15–40% joint product, >40% main product); a by-product\'s NRV is '
      'deducted from joint cost before splitting the remainder among the main/joint products.',
      '**§8.6 Joint cost apportionment, 3 methods** — physical units (ignores value entirely, '
      'always gives every product the *same* unit cost); sales value at split-off (ignores '
      'further processing cost); NRV (sales value less further processing cost — the "best" '
      'method, since it is the only one considering quantity, value **and** further cost '
      'together); total unit cost for inventory valuation = share of joint cost + further '
      'processing cost, divided by units.',
      '**§8.7 Service costing** — standardised, continuous services; fixed (standing) vs '
      'variable (running) cost split; the central difficulty is choosing the right cost unit; '
      'professional services (architects, accountants, doctors) use **job** costing instead, '
      'since their service varies client to client.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'Process, equivalent-units and joint-cost formulas (recap)', 'rows': [
      {'lb': 'Total equivalent production', 'tex': '\\text{Completed units} + (\\% \\text{ '
        'complete} \\times \\text{WIP units})'},
      {'lb': 'Cost per equivalent unit', 'tex': '\\dfrac{\\text{Total cost}}{\\text{Total '
        'equivalent production}}'},
      {'lb': 'Value of WIP (by difference)', 'tex': '\\text{Total cost} - \\text{Value of '
        'completed production}'},
      {'lb': 'Net Realisable Value (by-product/joint product)', 'tex': '\\text{Sales value} - '
        '\\text{Separate processing/marketing cost}'},
      {'lb': 'Net joint cost (after a by-product)', 'tex': '\\text{Total joint cost} - '
        '\\text{By-product NRV}'},
      {'lb': 'Total cost per unit of a joint product', 'tex': '\\dfrac{\\text{Share of joint '
        'cost} + \\text{Further processing cost}}{\\text{Units produced}}'},
    ]}},
  ]},

  {'n': '8.9', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'In process costing, what does "Abnormal Loss" mean? (A) Inventory items stolen during '
        'production  (B) Inventory items given out as gifts before full production  '
        '(C) The greater of the present production\'s loss over the previous production  '
        '(D) The greater of the actual process loss over what is deemed normal in the industry  '
        '(E) Losses in production due to abnormal behaviour of workers',
        'Joint products are the name given to two or more (A) The main products arising from '
        'the same process  (B) Dissimilar products manufactured from the same factory  '
        '(C) Complementary products that must be sold together  (D) Raw materials mixed to '
        'manufacture a single item  (E) Products which work alike but are from different '
        'manufacturers',
        'What is scrap? (A) Metal residue of a production process  (B) Residues of little or no '
        'value obtained during production  (C) Failed production items  (D) Cleaning '
        'materials  (E) Packaging materials',
        'Explain "Net Realisable Value" in joint product costing. (A) Sales value less the cost '
        'of further processing before the point of separation  (B) Market value of each of the '
        'joint products  (C) Sales value less the cost of further processing, selling and '
        'distribution after the split-off point  (D) Sales value less cost of production up to '
        'the point of separation  (E) Sales value less commission',
        'Which of these statements is correct as far as process costing is concerned? '
        '(A) Each process\'s output can be sold without further processing  (B) Only the '
        'materials introduced in process 1 are sufficient for the whole production  (C) Each '
        'manufacturing process has a normal gain  (D) Process costing is not significantly '
        'different from contract accounting  (E) The output of one process forms the input of '
        'another process',
        'In process costing, partly completed units are calculated to represent fully completed '
        'units based on the percentage of completion. Such representation is known as ………',
        'Where actual process wastage is less than what is regarded as normal in the industry, '
        'the difference is called …………………...',
        'A product of lesser value incidentally produced during the manufacture of another '
        'product is known as ………………………….',
        'The point during the production process where two or more joint products assume their '
        'own identities is called ………………...',
        'Where is the total credit on the Abnormal Gains Account transferred to at the end of '
        'the accounting period?',
      ]}],
      'a': [
      {'ol': [
        '**D** — the greater of the actual process loss over what is deemed normal in the '
        'industry.',
        '**A — the main products arising from the same process.**',
        '**B — residues of little or no value obtained during production.**',
        '**C** — sales value less the cost of further processing, selling and distribution '
        '**after** the split-off point.',
        '**E — the output of one process forms the input of another process.**',
        '**Equivalent units.**',
        '**Abnormal gain.**',
        '**By-product.**',
        '**Split-off point (separation point).**',
        '**The Profit and Loss Account.**',
      ]}]}},
  ]},

  {'n': '8.10', 't': 'Study text examination-type questions, worked (Q1–Q8)', 'b': [
    {'p': 'The study text closes the chapter with sixteen examination-type questions. They are '
          'reproduced below with full answers, split across two sections for readability — '
          'Q1 to Q8 here, and Q9 to Q16 in §8.11.'},

    {'eg': {'tag': 'Exam type — Q1', 't': 'Process costing as a system of sequential processes',
      'q': [{'p': '"Process Costing is a cost accounting system used to determine the cost of '
                  'production in a series of sequential processes." Discuss this comment, '
                  'giving diagrammatic example(s).'}],
      'a': [
      {'p': 'The comment is accurate but incomplete. Process costing is indeed used where output '
            'passes through a **series of sequential processes**, but its defining feature is '
            'not the sequence — it is that the output is **homogeneous**, so that units cannot '
            'be separately identified and costs must therefore be **averaged** over the units '
            'produced rather than traced to individual orders.'},
      {'def': {'t': 'Process costing', 'd': 'the costing method applied where a product passes '
                    'through two or more distinct processes or operations, the output of one '
                    'process becoming the input of the next, and the cost per unit is found by '
                    'averaging the cost of each process over its output.'}},
      {'h4': 'The sequential flow, diagrammatically'},
      {'pre': 'Raw materials\n     |\n     v\n+-------------+   output    +-------------+'
              '   output    +-------------+   output   +----------------+\n'
              '| PROCESS 1   |------------>| PROCESS 2   |------------>| PROCESS 3   |'
              '----------->| FINISHED GOODS |\n'
              '| materials   |             | + materials |             | + materials |'
              '            +----------------+\n'
              '| + labour    |             | + labour    |             | + labour    |\n'
              '| + overhead  |             | + overhead  |             | + overhead  |\n'
              '+-------------+             +-------------+             +-------------+\n'
              '      |                           |                           |\n'
              '      v                           v                           v\n'
              '  normal loss /              normal loss /              normal loss /\n'
              '  abnormal loss              abnormal loss              abnormal loss\n'
              '  (or abnormal gain)         (or abnormal gain)         (or abnormal gain)'},
      {'p': 'Each process has its **own account**, which is debited with the cost transferred in '
            'from the previous process plus the materials, labour and overhead added in that '
            'process, and credited with the value of normal loss scrap, any abnormal loss, and '
            'the output transferred on. The cost accumulates as the product moves along the '
            'chain, so that each unit of finished output carries the cost of every process it '
            'has been through.'},
      {'h4': 'Features of a process costing system'},
      {'ol': [
        'Production is **continuous** and output is **homogeneous** — one unit cannot be '
        'distinguished from another.',
        'Costs are collected **by process for a period**, not by job, and averaged over output.',
        'The **output of one process becomes the input (transferred-in cost) of the next.**',
        'There is normally **work-in-progress** at the beginning and end of each period, '
        'requiring the use of **equivalent units**.',
        '**Normal losses** are expected and their cost is absorbed by good output; **abnormal '
        'losses and gains** are valued at full cost per unit and taken to the profit and loss '
        'account.',
        'Some processes yield **joint products and by-products**, which require the joint cost '
        'to be apportioned.',
      ]},
      {'h4': 'Industries where it is used'},
      {'ul': [
        'chemicals, paints, pharmaceuticals and fertilisers;',
        'oil refining;', 'food processing, brewing, sugar and flour milling;',
        'cement, steel, paper and textiles;', 'soap and detergent manufacture.',
      ]},
      {'h4': 'How it differs from job costing'},
      {'table': {'align': 'lll', 'head': ['', 'Job (specific order) costing', 'Process costing'],
        'rows': [
        ['**Cost unit**', 'The individual job or batch', 'The process output for the period'],
        ['**Output**', 'Heterogeneous — each job is different', 'Homogeneous — units are '
         'identical'],
        ['**Cost ascertainment**', 'Costs **traced** to each job', 'Costs **averaged** over the '
         'units produced'],
        ['**Work-in-progress**', 'The total of the open job cost cards', 'Converted to '
         '**equivalent units** before averaging'],
        ['**Losses**', 'Usually insignificant and job-specific', 'Expected and formally '
         'accounted for as normal and abnormal'],
        ['**Cost flow**', 'Each job stands alone', 'Cost flows from one process to the next'],
      ]}}]}},

    {'eg': {'tag': 'Exam type — Q2', 't': 'Characteristics of a good process costing system',
      'q': [{'p': 'Briefly discuss the characteristics of a good process costing system.'}],
      'a': [
      {'ol': [
        '**A separate account for every process**, so that the cost of each stage is known and '
        'each process manager can be held responsible for their own stage.',
        '**Clear definition of the physical boundaries** of each process — where one ends and '
        'the next begins — so that costs and output are recorded against the right process.',
        '**Accurate measurement of input and output in physical units** at every process, '
        'including losses, so that the physical units reconcile before any money is allocated.',
        '**Predetermined normal loss percentages**, established from experience and reviewed '
        'regularly, against which actual losses can be measured to produce abnormal losses and '
        'gains.',
        '**Proper treatment of scrap values**, credited to the process account for the normal '
        'loss and to the abnormal loss account for the abnormal element.',
        '**A sound basis for valuing work-in-progress** using **equivalent units**, with the '
        'degree of completion assessed separately for materials, labour and overhead where they '
        'enter the process at different points.',
        '**A consistent and stated inventory flow assumption** — weighted average or FIFO — '
        'applied uniformly from period to period.',
        '**Correct treatment of transferred-in costs**, carried forward as a single 100%-'
        'complete input of the receiving process.',
        '**Identification and separate treatment of joint products and by-products**, with a '
        'defensible basis for apportioning joint cost.',
        '**Timely preparation of a cost of production report** for each process and period, '
        'showing the quantity schedule, equivalent units, cost per equivalent unit and the '
        'allocation of total cost.',
        '**Comparison against standards or budgets**, so that the system controls as well as '
        'records.',
        '**Integration with the financial accounts**, so that the process accounts reconcile '
        'with the general ledger (Chapter 6).',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q3', 't': 'Short notes on four process costing terms',
      'q': [{'p': 'Write short notes on each of the following terms: (a) product flow; '
                  '(b) work-in-progress; (c) equivalent units; (d) transferred-in costs.'}],
      'a': [
      {'h4': '(a)  Product flow'},
      {'p': 'Product flow describes the **route the product takes through the processes**. Three '
            'patterns are recognised:'},
      {'ol': [
        '**Sequential flow** — every unit passes through every process in the same order, one '
        'after another (the pattern in the diagram at Q1 above). The commonest form.',
        '**Parallel flow** — certain parts of the product are worked on simultaneously in '
        'separate processes and brought together later for final processing or assembly.',
        '**Selective flow** — the product moves to different processes depending on the final '
        'product wanted, as in meat processing or oil refining, where one input yields several '
        'products by different routes.',
      ]},
      {'p': 'Identifying the flow correctly matters because it determines which process accounts '
            'are opened and how cost is transferred between them.'},
      {'h4': '(b)  Work-in-progress'},
      {'p': 'Work-in-progress (WIP) is **partly completed output** still within a process at the '
            'beginning or end of a period. It is the central difficulty of process costing: the '
            'period\'s cost must be shared between units **completed** and units only '
            '**partly** completed, and a part-finished unit has not absorbed as much cost as a '
            'finished one. WIP is therefore converted into **equivalent units** before cost per '
            'unit is computed. Its degree of completion must be assessed **separately for each '
            'cost element**, because materials are often added in full at the start of a process '
            'while labour and overhead accrue evenly throughout it.'},
      {'h4': '(c)  Equivalent units'},
      {'def': {'t': 'Equivalent units', 'd': 'the number of **complete** units that the work '
                    'actually done would have produced, had it all been concentrated on finished '
                    'units instead of spread across part-finished ones.'}},
      {'tex': '\\text{Equivalent units} = \\text{Physical units} \\times '
              '\\text{Percentage of completion}'},
      {'p': 'For example, 8,000 units that are 75% complete as to materials represent '
            '$8{,}000 \\times 75\\% = 6{,}000$ equivalent units of material. Converting '
            'everything to equivalent units is what makes it legitimate to divide cost by '
            'output: the denominator then measures **work done**, not merely units touched. '
            'Separate equivalent-unit figures are computed for materials, labour and overhead '
            '(or for materials and conversion cost together) whenever their completion '
            'percentages differ.'},
      {'h4': '(d)  Transferred-in costs'},
      {'p': 'Transferred-in cost is the **cost of the output of the preceding process**, brought '
            'into the receiving process as its opening input. In the second and every subsequent '
            'process it behaves exactly like a material added at the very start of the process, '
            'and so is always **100% complete** for every unit in that process, including units '
            'in closing work-in-progress. It must be shown as a **separate cost element** in the '
            'cost of production report, with its own equivalent units and its own cost per '
            'equivalent unit, because its completion percentage differs from that of the '
            'materials, labour and overhead added within the process itself.'},
      {'warn': 'The commonest error in a multi-process question is to treat closing WIP as '
               'partly complete for transferred-in cost. It never is: a unit cannot be physically '
               'present in Process 2 unless the whole of Process 1 has been done to it.'}]}},

    {'eg': {'tag': 'Exam type — Q4', 't': 'Four distinctions in process costing',
      'q': [{'p': 'Differentiate between the following: (a) actual spoilage and normal spoilage; '
                  '(b) conversion cost and overhead cost; (c) material cost and transferred-in '
                  'cost; (d) WAP and FIFO methods in process costing.'}],
      'a': [
      {'h4': '(a)  Actual spoilage versus normal spoilage'},
      {'table': {'align': 'll', 'head': ['Normal spoilage', 'Actual spoilage'], 'rows': [
        ['The spoilage **expected** to arise under efficient operating conditions, expressed as '
         'a predetermined percentage of input.',
         'The spoilage that **actually** occurred in the period, as counted.'],
        ['**Unavoidable** and inherent in the process — evaporation, trimming, chemical change.',
         'A **fact** observed, which may be more or less than normal.'],
        ['Its cost is **absorbed by the good output**, raising the cost per good unit; its scrap '
         'proceeds are credited to the process account.',
         'Has no accounting treatment of its own — it is split into the normal part and the '
         'excess.'],
        ['Appears in the process account at scrap value only.',
         'The excess over normal is **abnormal spoilage**, valued at full cost per unit and '
         'written off to the costing profit and loss account; a shortfall below normal is an '
         '**abnormal gain**.'],
      ]}},
      {'tex': '\\text{Abnormal loss} = \\text{Actual spoilage} - \\text{Normal spoilage} '
              '\\qquad \\text{(a negative result is an abnormal gain)}'},
      {'h4': '(b)  Conversion cost versus overhead cost'},
      {'table': {'align': 'll', 'head': ['Conversion cost', 'Overhead cost'], 'rows': [
        ['The cost of **converting raw material into finished output**: direct labour **plus** '
         'production overhead.', 'All **indirect** costs: indirect materials, indirect labour '
         'and indirect expenses.'],
        ['$\\text{Conversion cost} = \\text{Direct labour} + \\text{Production overhead}$',
         '$\\text{Overhead} = \\text{Indirect materials} + \\text{Indirect labour} + '
         '\\text{Indirect expenses}$'],
        ['Used in process costing because labour and overhead usually accrue **at the same '
         'rate** through a process, so they can be treated as one element for equivalent-unit '
         'purposes.', 'A classification by **nature** (Chapter 2), used throughout costing, not '
         'only in process costing.'],
        ['**Includes** direct labour, which is not an overhead.',
         '**Excludes** direct labour, and includes non-production overheads too.'],
      ]}},
      {'note': 'So production overhead is **part of** conversion cost, but conversion cost is '
               'not part of overhead. The two overlap; neither contains the other.'},
      {'h4': '(c)  Material cost versus transferred-in cost'},
      {'table': {'align': 'll', 'head': ['Material cost', 'Transferred-in cost'], 'rows': [
        ['The cost of raw materials and components **added within** the process.',
         'The accumulated cost of the output of the **previous** process, brought forward into '
         'this one.'],
        ['May be added at the start, evenly, or at a particular stage — so closing WIP may be '
         'less than 100% complete for it.',
         'Always **100% complete** for every unit physically in the process.'],
        ['Arises in **every** process, including the first.',
         'Arises only in the **second and subsequent** processes.'],
        ['Sourced from the stores ledger on a materials requisition.',
         'Sourced from the preceding process account.'],
      ]}},
      {'h4': '(d)  Weighted average (WAP) versus FIFO'},
      {'table': {'align': 'lll', 'head': ['', 'Weighted average (WAP)', 'FIFO'], 'rows': [
        ['**Treatment of opening WIP**', 'Opening WIP cost is **merged** with the current '
         'period\'s cost and averaged over all output.',
         'Opening WIP is kept **separate** and completed first; only **current** period cost is '
         'averaged.'],
        ['**Equivalent units**', 'Units completed (all of them) + closing WIP equivalent units.',
         'Work **to complete** opening WIP + units started and completed + closing WIP '
         'equivalent units.'],
        ['**Cost per equivalent unit**', '(Opening WIP cost + current cost) ÷ equivalent units.',
         'Current period cost only ÷ equivalent units.'],
        ['**Output valuation**', 'All completed units carry the **same** cost per unit.',
         'Units from opening WIP carry a **different** cost from units started this period.'],
        ['**Simplicity**', 'Simpler, and the usual choice in practice.',
         'More complex, two-tier calculation.'],
        ['**Usefulness for control**', 'Weaker — last period\'s cost is blended into this '
         'period\'s unit cost, so a change in efficiency is partly hidden.',
         'Better — the current cost per unit reflects **this period\'s** performance only, so '
         'it is comparable period to period.'],
      ]}},
      {'note': 'The two give the same answer when there is **no opening work-in-progress**, '
               'because there is then nothing to merge or keep separate. They also converge when '
               'costs per unit are stable between periods.'}]}},

    {'eg': {'tag': 'Exam type — Q5',
      't': 'Cost per kg of good production with a 4% normal wastage',
      'q': [{'p': 'A process has a normal wastage of **4%**, which has a resale value of **N50 '
                  'per kg**. Find the cost per kg of good production, if the material cost is '
                  '**N320,000** and the conversion cost is **N240,000** for producing **500 '
                  'kg**.'}],
      'a': [
      {'h4': 'Step 1 — the physical units'},
      {'stmt': {'t': 'Quantity schedule (kg)', 'rows': [
        ['Input into the process', '', 500],
        ['Less: normal wastage, 4% × 500 kg', '', -20],
        ['**Expected good output**', '', 480, '@tt'],
      ]}},
      {'h4': 'Step 2 — the cost to be spread over good output'},
      {'stmt': {'t': 'Net process cost (N)', 'rows': [
        ['Material cost', '', 320000],
        ['Conversion cost', '', 240000],
        ['**Total process cost**', '', 560000, '@t'],
        ['Less: scrap value of normal wastage, 20 kg × N50', '', -1000],
        ['**Net cost to be absorbed by good output**', '', 559000, '@tt'],
      ]}},
      {'h4': 'Step 3 — cost per kg of good production'},
      {'tex': '\\text{Cost per kg} = \\frac{\\text{Total cost} - '
              '\\text{Scrap value of normal loss}}{\\text{Input} - '
              '\\text{Normal loss units}} = \\frac{560{,}000 - 1{,}000}{500 - 20} '
              '= \\frac{559{,}000}{480} = N1{,}164.58 \\text{ per kg}'},
      {'key': 'Two things make this question work, and both are about the **normal** loss. '
              'First, its units are **excluded from the denominator** — the cost of the wasted '
              'material is deliberately loaded onto the good kilos, because wastage is an '
              'unavoidable cost of producing them. Second, whatever the waste **fetches as '
              'scrap** is **deducted from the numerator**, because that much of the cost has '
              'been recovered. Had the waste been worthless, the cost per kg would have been '
              '$560{,}000 \\div 480 = N1{,}166.67$; had there been no wastage at all, it would '
              'have been $560{,}000 \\div 500 = N1{,}120$.'}]}},

    {'eg': {'tag': 'Exam type — Q6',
      't': 'ABC — a weighted average cost of production report with normal and abnormal spoilage',
      'q': [
      {'p': 'ABC uses process costing for its operations. The following information is given for '
            'the year ended 31 December 2008:'},
      {'stmt': {'t': 'Quantities (units)', 'rows': [
        ['Work-in-process, 1 January 2008', '', 4800],
        ['Units started during the year', '', 19200],
        ['Abnormal spoilage', '', 1392],
        ['Units completed', '', 17280],
        ['Work-in-process, 31 December 2008', '', 3600],
      ]}},
      {'stmt': {'t': 'Stages of completion of work-in-process', 'rows': [
        ['WIP 1 January 2008 — material', '', '100%'],
        ['WIP 1 January 2008 — conversion', '', '80%'],
        ['WIP 31 December 2008 — material', '', '100%'],
        ['WIP 31 December 2008 — conversion', '', '⅔'],
      ]}},
      {'stmt': {'t': 'Costs (N)', 'rows': [
        ['WIP 1 January 2008 — material', 18000, ''],
        ['WIP 1 January 2008 — conversion', 17520, 35520],
        ['Costs incurred during the year — material', 73200, ''],
        ['Costs incurred during the year — conversion', 96480, 169680],
      ]}},
      {'p': '**Required:** using the **weighted average** pricing method, draw up a cost of '
            'production report showing the cost of completed units, abnormal spoilage and the '
            'cost of the inventory (WIP) at 31 December 2008, showing the relevant computations '
            'in detail. **Spoilage is detected at the end of operations.**'}],
      'a': [
      {'h4': 'Step 1 — the quantity schedule, and the hidden normal spoilage'},
      {'p': 'The question does not state the normal spoilage, but the physical units reveal it: '
            'everything that went in must come out somewhere.'},
      {'stmt': {'t': 'Quantity schedule (units)', 'rows': [
        ['**Input**', '', '', '@hd'],
        ['WIP at 1 January', 4800, ''],
        ['Units started during the year', 19200, 24000],
        '@gap',
        ['**Output**', '', '', '@hd'],
        ['Units completed', 17280, ''],
        ['Abnormal spoilage', 1392, ''],
        ['WIP at 31 December', 3600, 22272],
        ['**Normal spoilage (balancing figure)**', '', 1728, '@tt'],
      ]}},
      {'note': 'The 1,728 units of normal spoilage are not given — they are deduced, and the '
               'fact that the cost per equivalent unit comes out at exactly N3.80 and N5.00 '
               'afterwards confirms the deduction. Always complete the **physical** reconciliation '
               'before touching the money; a question that does not appear to balance usually '
               'contains a figure you are expected to derive.'},
      {'h4': 'Step 2 — equivalent units'},
      {'p': 'Spoilage is detected **at the end of operations**, so spoiled units — both normal '
            'and abnormal — have passed through the whole process and are **100% complete** for '
            'both material and conversion. Closing WIP is 100% complete for material and ⅔ '
            'complete for conversion.'},
      {'stmt': {'t': 'Equivalent units — weighted average', 'rows': [
        ['', 'Physical units', 'Material', 'Conversion', '@hd'],
        ['Units completed', 17280, 17280, 17280],
        ['Normal spoilage (100% complete)', 1728, 1728, 1728],
        ['Abnormal spoilage (100% complete)', 1392, 1392, 1392],
        ['Closing WIP (100% material;  ⅔ conversion)', 3600, 3600, 2400],
        ['**Total equivalent units**', 24000, 24000, 22800, '@tt'],
      ]}},
      {'h4': 'Step 3 — cost per equivalent unit'},
      {'stmt': {'t': 'Cost per equivalent unit (N)', 'rows': [
        ['', 'Material', 'Conversion', 'Total', '@hd'],
        ['Cost in opening WIP', 18000, 17520, 35520],
        ['Cost incurred during the year', 73200, 96480, 169680],
        ['**Total cost**', 91200, 114000, 205200, '@t'],
        ['÷ equivalent units', 24000, 22800, ''],
        ['**Cost per equivalent unit**', '**N3.80**', '**N5.00**', '**N8.80**', '@tt'],
      ]}},
      {'h4': 'Step 4 — cost of production report: allocating the N205,200'},
      {'stmt': {'t': 'Cost of production report, year ended 31 December 2008 (N)', 'rows': [
        ['Units completed:  17,280 × N8.80', 152064, ''],
        ['Add: normal spoilage absorbed by completed units:  1,728 × N8.80', 15206, 167270],
        '@gap',
        ['Abnormal spoilage (to costing profit and loss):  1,392 × N8.80', '', 12250],
        '@gap',
        ['Closing WIP — material:  3,600 × N3.80', 13680, ''],
        ['Closing WIP — conversion:  2,400 × N5.00', 12000, 25680],
        '@gap',
        ['**Total cost accounted for**', '', 205200, '@tt'],
      ]}},
      {'stmt': {'t': 'Summary of the required figures', 'rows': [
        ['**Cost of completed units** (including normal spoilage) — 17,280 units', '', 167270],
        ['**Cost per completed unit**  (N167,270 ÷ 17,280)', '', 'N9.68'],
        ['**Cost of abnormal spoilage** — written off to profit and loss', '', 12250],
        ['**Cost of closing work-in-process** — 3,600 units', '', 25680],
      ]}},
      {'key': 'The critical judgement is **who bears the normal spoilage**. Because spoilage is '
              'detected at the **end** of operations, the units in closing WIP have not yet '
              'reached the inspection point, so they cannot have been found spoiled — the normal '
              'spoilage therefore attaches **entirely to the completed units**, lifting their '
              'cost from N8.80 to N9.68 each. Had inspection taken place at the *start* of the '
              'process, closing WIP would have passed it too and would have to bear its share.'}]}},

    {'eg': {'tag': 'Exam type — Q7',
      't': 'BCB Company — two-department production reports under weighted average and FIFO',
      'q': [
      {'p': 'BCB Company has the following data for October:'},
      {'stmt': {'t': 'BCB Company — October data', 'rows': [
        ['', 'Department A', 'Department B', '@hd'],
        ['Beginning inventory in process', '2,000 units', '2,000 units'],
        ['Transferred-in cost', '—', 'N4,600'],
        ['Cost of materials added last month', 'N2,000 (100%)', 'N3,200 (80%)'],
        ['Conversion costs added last month', 'N900 (60%)', 'N800 (40%)'],
        ['Units put in process this month', 30000, 29000],
        ['Cost of materials added this month', 'N30,968', 'N56,580'],
        ['Conversion costs added this month', 'N41,800', 'N29,803'],
        ['Units completed and transferred', 29000, 30000],
        ['Ending inventory in process', '3,000 units', '1,000 units'],
        ['Ending inventory — material content', '90%', '50%'],
        ['Ending inventory — conversion', '50%', '30%'],
      ]}},
      {'p': '**Required:** **(a)** using the **weighted average** costing method, prepare a '
            'production report for October for each department, showing the cost of the ending '
            'work-in-progress and the cost of goods completed and transferred; **(b)** using the '
            '**FIFO** costing method, repeat the requirements of (a).'}],
      'a': [
      {'h4': '(a)  Weighted average — Department A'},
      {'stmt': {'t': 'A1  Quantity schedule and equivalent units — Dept A, weighted average',
        'rows': [
        ['', 'Physical units', 'Material', 'Conversion', '@hd'],
        ['Beginning inventory', 2000, '', ''],
        ['Units put in process', 30000, '', ''],
        ['**To account for**', 32000, '', '', '@t'],
        '@gap',
        ['Completed and transferred', 29000, 29000, 29000],
        ['Ending inventory (90% material; 50% conversion)', 3000, 2700, 1500],
        ['**Accounted for / equivalent units**', 32000, 31700, 30500, '@tt'],
      ]}},
      {'stmt': {'t': 'A2  Cost per equivalent unit — Dept A (N)', 'rows': [
        ['', 'Material', 'Conversion', 'Total', '@hd'],
        ['Cost in beginning inventory', 2000, 900, 2900],
        ['Cost added this month', 30968, 41800, 72768],
        ['**Total cost**', 32968, 42700, 75668, '@t'],
        ['÷ equivalent units', 31700, 30500, ''],
        ['**Cost per equivalent unit**', '**N1.04**', '**N1.40**', '**N2.44**', '@tt'],
      ]}},
      {'stmt': {'t': 'A3  Allocation of cost — Dept A (N)', 'rows': [
        ['Completed and transferred:  29,000 × N2.44', '', 70760],
        ['Ending inventory — material:  2,700 × N1.04', 2808, ''],
        ['Ending inventory — conversion:  1,500 × N1.40', 2100, 4908],
        ['**Total cost accounted for**', '', 75668, '@tt'],
      ]}},
      {'h4': '(a)  Weighted average — Department B'},
      {'p': 'Department B receives the N70,760 transferred out of Department A, for 29,000 '
            'units. Transferred-in cost is **always 100% complete** for every unit in the '
            'department, including those in closing inventory.'},
      {'stmt': {'t': 'B1  Equivalent units — Dept B, weighted average', 'rows': [
        ['', 'Physical units', 'Transferred-in', 'Material', 'Conversion', '@hd'],
        ['Beginning inventory', 2000, '', '', ''],
        ['Transferred in this month', 29000, '', '', ''],
        ['**To account for**', 31000, '', '', '', '@t'],
        '@gap',
        ['Completed and transferred', 30000, 30000, 30000, 30000],
        ['Ending inventory (100% t/in; 50% material; 30% conversion)', 1000, 1000, 500, 300],
        ['**Equivalent units**', 31000, 31000, 30500, 30300, '@tt'],
      ]}},
      {'stmt': {'t': 'B2  Cost per equivalent unit — Dept B (N)', 'rows': [
        ['', 'Transferred-in', 'Material', 'Conversion', 'Total', '@hd'],
        ['Cost in beginning inventory', 4600, 3200, 800, 8600],
        ['Cost added / transferred in this month', 70760, 56580, 29803, 157143],
        ['**Total cost**', 75360, 59780, 30603, 165743, '@t'],
        ['÷ equivalent units', 31000, 30500, 30300, ''],
        ['**Cost per equivalent unit**', '**N2.4310**', '**N1.9600**', '**N1.0100**',
         '**N5.4010**', '@tt'],
      ]}},
      {'stmt': {'t': 'B3  Allocation of cost — Dept B (N)', 'rows': [
        ['Completed and transferred:  30,000 × N5.4010', '', 162029],
        ['Ending inventory — transferred-in:  1,000 × N2.4310', 2431, ''],
        ['Ending inventory — material:  500 × N1.96', 980, ''],
        ['Ending inventory — conversion:  300 × N1.01', 303, 3714],
        ['**Total cost accounted for**', '', 165743, '@tt'],
      ]}},
      {'h4': '(b)  FIFO — Department A'},
      {'p': 'Under FIFO the opening inventory is completed **first** and kept separate. Its '
            'equivalent units are only the work **still to be done** on it: material is already '
            '100% complete, so none; conversion is 60% complete, so the remaining 40%.'},
      {'stmt': {'t': 'A4  Equivalent units — Dept A, FIFO', 'rows': [
        ['', 'Physical units', 'Material', 'Conversion', '@hd'],
        ['To complete beginning inventory (0% material; 40% conversion)', 2000, 0, 800],
        ['Started and completed this month (29,000 − 2,000)', 27000, 27000, 27000],
        ['Ending inventory (90% material; 50% conversion)', 3000, 2700, 1500],
        ['**Equivalent units**', 32000, 29700, 29300, '@tt'],
      ]}},
      {'stmt': {'t': 'A5  Cost per equivalent unit — Dept A, FIFO (current cost only)', 'rows': [
        ['', 'Material', 'Conversion', 'Total', '@hd'],
        ['Cost added this month', 30968, 41800, 72768],
        ['÷ equivalent units', 29700, 29300, ''],
        ['**Cost per equivalent unit**', '**N1.0427**', '**N1.4266**', '**N2.4693**', '@tt'],
      ]}},
      {'stmt': {'t': 'A6  Allocation of cost — Dept A, FIFO (N)', 'rows': [
        ['**Completed and transferred**', '', '', '@hd'],
        ['From beginning inventory — cost brought forward', 2900, ''],
        ['From beginning inventory — conversion to complete:  800 × N1.4266', 1141, 4041],
        ['Started and completed:  27,000 × N2.4693', '', 66672],
        ['**Total transferred out (29,000 units)**', '', 70713, '@t'],
        '@gap',
        ['Ending inventory — material:  2,700 × N1.0427', 2815, ''],
        ['Ending inventory — conversion:  1,500 × N1.4266', 2140, 4955],
        ['**Total cost accounted for**', '', 75668, '@tt'],
      ]}},
      {'h4': '(b)  FIFO — Department B'},
      {'p': 'Department B now receives **N70,713** for 29,000 units, i.e. N2.4384 per unit '
            'transferred in.'},
      {'stmt': {'t': 'B4  Equivalent units — Dept B, FIFO', 'rows': [
        ['', 'Physical units', 'Transferred-in', 'Material', 'Conversion', '@hd'],
        ['To complete beginning inventory (0% t/in; 20% material; 60% conversion)', 2000, 0, 400,
         1200],
        ['Started and completed (30,000 − 2,000)', 28000, 28000, 28000, 28000],
        ['Ending inventory (100% t/in; 50% material; 30% conversion)', 1000, 1000, 500, 300],
        ['**Equivalent units**', 31000, 29000, 28900, 29500, '@tt'],
      ]}},
      {'stmt': {'t': 'B5  Cost per equivalent unit — Dept B, FIFO (N)', 'rows': [
        ['', 'Transferred-in', 'Material', 'Conversion', 'Total', '@hd'],
        ['Cost added / transferred in this month', 70713, 56580, 29803, 157096],
        ['÷ equivalent units', 29000, 28900, 29500, ''],
        ['**Cost per equivalent unit**', '**N2.4384**', '**N1.9578**', '**N1.0103**',
         '**N5.4065**', '@tt'],
      ]}},
      {'stmt': {'t': 'B6  Allocation of cost — Dept B, FIFO (N)', 'rows': [
        ['**Completed and transferred**', '', '', '@hd'],
        ['From beginning inventory — cost brought forward (4,600 + 3,200 + 800)', 8600, ''],
        ['From beginning inventory — material to complete:  400 × N1.9578', 783, ''],
        ['From beginning inventory — conversion to complete:  1,200 × N1.0103', 1212, 10595],
        ['Started and completed:  28,000 × N5.4065', '', 151380],
        ['**Total transferred out (30,000 units)**', '', 161975, '@t'],
        '@gap',
        ['Ending inventory — transferred-in:  1,000 × N2.4384', 2438, ''],
        ['Ending inventory — material:  500 × N1.9578', 979, ''],
        ['Ending inventory — conversion:  300 × N1.0103', 303, 3720],
        ['**Total cost accounted for**', '', 165696, '@tt'],
      ]}},
      {'h4': 'Comparison of the two methods'},
      {'stmt': {'t': 'Weighted average versus FIFO (N)', 'rows': [
        ['', 'Weighted average', 'FIFO', '@hd'],
        ['**Department A** — transferred out', 70760, 70713],
        ['**Department A** — closing inventory', 4908, 4955],
        ['**Department B** — transferred out (finished goods)', 162029, 161975],
        ['**Department B** — closing inventory', 3714, 3720],
      ]}},
      {'key': 'The two methods differ by only a few naira here, because unit costs barely moved '
              'between September and October — opening inventory was already carrying very '
              'nearly this month\'s cost. The difference between WAP and FIFO is only ever '
              'material when **unit costs change sharply** between periods; that is precisely '
              'when FIFO is worth the extra work, because its unit cost reflects **this period '
              'alone** and so reveals the change, whereas the weighted average blends it away.'},
      {'note': 'Figures are rounded to the nearest naira, and unit rates to four decimal places, '
               'so the allocations may differ by a naira or two from an unrounded computation. '
               'In an exam, state the rounding you have used and carry rates to at least four '
               'decimal places before allocating.'}]}},

    {'eg': {'tag': 'Exam type — Q8',
      't': 'Joint product, by-product and main product distinguished',
      'q': [{'p': 'Differentiate clearly between joint-product, by-product and main-product in a '
                  'joint costing system.'}],
      'a': [
      {'table': {'align': 'llll', 'head': ['', 'Main product', 'Joint products', 'By-products'],
        'rows': [
        ['**Definition**', 'The **single** product which is the principal purpose of the '
         'process, where the process is operated primarily to obtain it.',
         '**Two or more** products produced simultaneously from a common process, each of '
         '**significant** sales value, none of which can be produced without the others.',
         'Products arising **incidentally** from a process operated to make something else, '
         'having only **minor** sales value relative to the main or joint products.'],
        ['**Relative value**', 'Dominant.', 'All substantial, and broadly comparable.',
         'Small — the test is one of **relative sales value**, not of physical quantity.'],
        ['**Purpose of the process**', 'The process exists to make it.',
         'The process exists to make them all; none is incidental.',
         'The process does **not** exist to make them; they simply emerge.'],
        ['**Separable at will?**', 'n/a', '**No** — they arise together, in fixed or broadly '
         'fixed proportions, up to the split-off point.',
         '**No** — they arise unavoidably from making the main product.'],
        ['**Accounting treatment**', 'Bears the whole cost of the process.',
         'The **joint cost is apportioned** between them, on physical units, sales value at '
         'split-off, or net realisable value.',
         'Normally **no joint cost is apportioned** to them. Their net proceeds are either '
         'credited to the process account (reducing the cost of the main product) or treated as '
         'other income.'],
        ['**Examples**', 'Refined sugar from a sugar mill.',
         'Petrol, diesel, kerosene and aviation fuel from crude oil; cream and skimmed milk '
         'from whole milk.',
         'Molasses and bagasse from sugar refining; sawdust from timber; glycerine from soap '
         'manufacture.'],
      ]}},
      {'key': 'The **split-off point** is the moment in the process at which the products become '
              'separately identifiable. Before it, the cost is **joint** and can only be '
              'apportioned by convention; after it, every cost is **separable** and is traced '
              'directly to the product that incurred it. That distinction governs the whole '
              'topic — and it is also why apportioned joint cost is **irrelevant** to any '
              'decision about what to do with a product after split-off (Chapter 9).'},
      {'note': 'The classification is not permanent. A by-product whose market price rises '
               'sharply becomes a joint product, and a joint product whose price collapses '
               'becomes a by-product. Review the classification whenever relative values change.'}]}},
  ]},


  {'n': '8.11', 't': 'Study text examination-type questions, worked (Q9–Q16)', 'b': [

    {'eg': {'tag': 'Exam type — Q9',
      't': 'Three methods of apportioning joint cost, and the profit on a joint product',
      'q': [{'p': '**(a)** Discuss briefly the three methods of apportioning joint costs to '
                  'joint products. **(b)** Explain how a profit or loss on a joint product is '
                  'arrived at.'}],
      'a': [
      {'h4': '(a)  Three methods of apportioning joint cost'},
      {'table': {'align': 'lll', 'head': ['Method', 'How it works', 'Comment'], 'rows': [
        ['**1.  Physical units (physical measurement) basis**',
         'The joint cost is shared in proportion to the **quantity** of each product emerging '
         'at split-off — kilos, litres, tonnes, units. Every product then bears the same cost '
         'per physical unit.',
         '**For:** simple, objective, and defensible where products are physically similar. '
         '**Against:** it ignores value entirely, so a cheap bulky product is charged the same '
         'per kilo as a valuable one, which can make the cheap product appear to make a '
         'permanent loss. It is also impossible where the products are measured in different '
         'units (litres of gas and kilos of solid).'],
        ['**2.  Sales value at split-off basis**',
         'The joint cost is shared in proportion to the **sales value of the output of each '
         'product at the split-off point** (quantity produced × selling price at split-off).',
         '**For:** relates cost to the product\'s ability to bear it, so no product is '
         'automatically made to look unprofitable; every product shows the same gross margin '
         'percentage. **Against:** needs a market price **at split-off**, which does not exist '
         'if the product must be processed further before it can be sold.'],
        ['**3.  Net realisable value (net realisation / reverse cost) basis**',
         'Where products need further processing before sale, a notional split-off value is '
         'computed as **final sales value less the separable post-split-off costs**, and the '
         'joint cost is shared in proportion to those net realisable values.',
         '**For:** the only workable value-based method when there is no market at split-off; '
         'it is the method most often required by examiners. **Against:** more computation, and '
         'the answer depends on the estimate of further processing costs.'],
      ]}},
      {'note': 'A fourth method is sometimes met: the **constant gross margin percentage** '
               'method, which apportions joint cost so that every product shows the same gross '
               'margin percentage on final sales. And where products are measured in different '
               'units, a **weighted average (technical estimate) basis** assigns points or '
               'weights to each product to make the physical measures comparable.'},
      {'h4': '(b)  How the profit or loss on a joint product is arrived at'},
      {'steps': [
        'Take the **sales value** of the quantity of that product **actually sold** in the '
        'period.',
        'Compute its **cost of sales**: its **apportioned share of the joint cost**, plus any '
        '**separable (further processing) costs** incurred on it after split-off, adjusted for '
        'opening and closing inventories of that product.',
        'Deduct the cost of sales from the sales value to arrive at the product\'s **gross '
        'profit**.',
        'Deduct any **selling, distribution and administrative costs** attributable to that '
        'product to arrive at its **net profit or loss**.',
      ]},
      {'warn': 'Two cautions that carry marks. **First**, the profit shown for an individual '
               'joint product is only as meaningful as the apportionment method that produced '
               'it — change the method and the product\'s "profit" changes, although the total '
               'profit of the process is unaffected. **Second**, and more important, a reported '
               'loss on a joint product is **never on its own a reason to stop producing it**, '
               'because it cannot be stopped without also stopping the products that are '
               'profitable. The only valid decision is whether to **process it further after '
               'split-off**, and that decision compares the **incremental revenue** from further '
               'processing with the **incremental cost** — the apportioned joint cost is sunk '
               'and irrelevant to it.'}]}},

    {'eg': {'tag': 'Exam type — Q10',
      't': 'By-product accounting, and apportioning N900 of joint cost two ways',
      'q': [
      {'p': '**(a)** Briefly describe the accounting treatment of a by-product.'},
      {'p': '**(b)** A process has two products A and B with a joint cost of **N900**. After the '
            'split-off point, Product A has **1,000 units** with a selling price of **N2 per '
            'unit** and a separate processing cost of **N600**. Product B has **500 units** with '
            'a selling price of **N1 per unit** and a separate processing cost of **N100**. '
            'Calculate the total cost of each product using (a) the physical unit basis and '
            '(b) the net realisation method.'}],
      'a': [
      {'h4': '(a)  Accounting treatment of a by-product'},
      {'p': 'Because a by-product has only minor value, it is **not** normally charged with any '
            'share of the joint cost. Four treatments are met in practice, in ascending order of '
            'refinement:'},
      {'ol': [
        '**Other income.** The net proceeds of the by-product are credited to the profit and '
        'loss account as miscellaneous income, and the main product bears the whole joint cost. '
        'Simplest, but it overstates the cost of the main product.',
        '**Credit to the process account.** The net proceeds are credited to the process from '
        'which the by-product arose, reducing the cost of the main product. This is the usual '
        'treatment.',
        '**Net realisable value credit.** Where the by-product needs further processing or '
        'selling costs, the credit is its sales value **less** those separable costs, so that '
        'only the genuine net recovery reduces the main product\'s cost.',
        '**Reverse (replacement) cost method.** Where the by-product is used internally instead '
        'of being sold, the process is credited with what it would have cost to buy that '
        'material from outside.',
      ]},
      {'p': 'In every case the by-product is also brought into the inventory records at the '
            'value credited, so that unsold by-product is carried as an asset.'},
      {'h4': '(b)(a)  Physical unit basis'},
      {'stmt': {'t': 'Apportionment on physical units', 'rows': [
        ['', 'Product A', 'Product B', 'Total', '@hd'],
        ['Units produced', 1000, 500, 1500],
        ['Proportion', '1,000/1,500', '500/1,500', ''],
        ['**Joint cost apportioned (N900)**', 600, 300, 900, '@t'],
        ['Add: separate processing cost after split-off', 600, 100, 700],
        ['**Total cost of each product**', 1200, 400, 1600, '@tt'],
      ]}},
      {'stmt': {'t': 'Resulting profit — physical unit basis', 'rows': [
        ['', 'Product A', 'Product B', 'Total', '@hd'],
        ['Sales value  (1,000 × N2;  500 × N1)', 2000, 500, 2500],
        ['Total cost', 1200, 400, 1600],
        ['**Profit**', 800, 100, 900, '@tt'],
      ]}},
      {'h4': '(b)(b)  Net realisation method'},
      {'stmt': {'t': 'Apportionment on net realisable value', 'rows': [
        ['', 'Product A', 'Product B', 'Total', '@hd'],
        ['Final sales value  (1,000 × N2;  500 × N1)', 2000, 500, 2500],
        ['Less: separate processing cost after split-off', -600, -100, -700],
        ['**Net realisable value at split-off**', 1400, 400, 1800, '@t'],
        ['Proportion', '1,400/1,800', '400/1,800', ''],
        ['**Joint cost apportioned (N900)**', 700, 200, 900, '@t'],
        ['Add: separate processing cost', 600, 100, 700],
        ['**Total cost of each product**', 1300, 300, 1600, '@tt'],
      ]}},
      {'stmt': {'t': 'Resulting profit — net realisation method', 'rows': [
        ['', 'Product A', 'Product B', 'Total', '@hd'],
        ['Sales value', 2000, 500, 2500],
        ['Total cost', 1300, 300, 1600],
        ['**Profit**', 700, 200, 900, '@tt'],
      ]}},
      {'key': 'Compare the two profit lines. The **total** profit is N900 either way — '
              'apportionment never creates or destroys profit, it only moves it between '
              'products. What changes is the **split**: A earns N800 under physical units and '
              'N700 under net realisation. Note also that under net realisation both products '
              'show exactly the same profit as a percentage of their net realisable value '
              '($700/1{,}400 = 700/1{,}400 = 50\\%$ and $200/400 = 50\\%$), which is the '
              'method\'s great attraction: no product can be made to look like a loser by an '
              'accident of apportionment.'}]}},

    {'eg': {'tag': 'Exam type — Q11',
      't': 'Products X and Y — joint cost apportioned by net realisation',
      'q': [
      {'p': 'A firm manufactures two products, X and Y, from the same material. In Department 1 '
            'the material is split into X and Y. **X requires no further processing**, while **Y '
            'must be processed further in Department 2**. The following costs pertain to '
            'November:'},
      {'stmt': {'t': 'Departmental costs (N)', 'rows': [
        ['Department', 'Direct materials', 'Direct labour', 'Factory overhead', 'Total', '@hd'],
        ['1', 60000, 15000, 10000, 85000],
        ['2', '—', 3000, 12000, 15000],
        ['**Total**', 60000, 18000, 22000, 100000, '@tt'],
      ]}},
      {'stmt': {'t': 'Output and sales', 'rows': [
        ['Product', 'Kilograms sold', 'Kilograms produced', 'Sales for the period', '@hd'],
        ['X', 30000, 45000, 'N60,000'],
        ['Y', 20000, 20000, 'N95,000'],
      ]}},
      {'p': 'There were no finished goods at the beginning of the month. **Required:** using the '
            'net realisation method to apportion the joint cost, calculate the total cost of '
            'producing X and Y during the month. Assume the selling price of X will remain '
            'constant in the immediate future.'}],
      'a': [
      {'h4': 'Step 1 — the selling price per kilogram'},
      {'p': 'Sales value is given for the kilograms **sold**, but joint cost must be apportioned '
            'over the kilograms **produced**, so a price per kilogram is needed first:'},
      {'stmt': {'t': 'Selling price per kilogram', 'rows': [
        ['X:  N60,000 ÷ 30,000 kg sold', '', 'N2.00 per kg'],
        ['Y:  N95,000 ÷ 20,000 kg sold', '', 'N4.75 per kg'],
      ]}},
      {'note': 'This is the step most candidates miss. X **produced** 45,000 kg but **sold** '
               'only 30,000 kg, so 15,000 kg went into closing inventory. The joint cost of the '
               'period relates to everything produced, not only to what was sold — so the sales '
               'value used in the apportionment must be the value of **production**, at the '
               'price per kilogram the sales reveal. This is also why the question tells you the '
               'price of X will remain constant: it entitles you to value the unsold 15,000 kg '
               'at N2.'},
      {'h4': 'Step 2 — net realisable value of each product\'s production'},
      {'stmt': {'t': 'Net realisable value at split-off (N)', 'rows': [
        ['', 'Product X', 'Product Y', 'Total', '@hd'],
        ['Kilograms produced', 45000, 20000, ''],
        ['× selling price per kg', 'N2.00', 'N4.75', ''],
        ['**Sales value of production**', 90000, 95000, 185000, '@t'],
        ['Less: further processing cost in Department 2', 0, -15000, -15000],
        ['**Net realisable value at split-off**', 90000, 80000, 170000, '@tt'],
      ]}},
      {'h4': 'Step 3 — apportion the N85,000 joint cost of Department 1'},
      {'stmt': {'t': 'Total cost of producing X and Y (N)', 'rows': [
        ['', 'Product X', 'Product Y', 'Total', '@hd'],
        ['Proportion of net realisable value', '90,000/170,000', '80,000/170,000', ''],
        ['**Joint cost of Department 1 apportioned (N85,000)**', 45000, 40000, 85000, '@t'],
        ['Add: further processing cost, Department 2', 0, 15000, 15000],
        ['**Total cost of production for the month**', 45000, 55000, 100000, '@tt'],
      ]}},
      {'stmt': {'t': 'Cost per kilogram produced', 'rows': [
        ['X:  N45,000 ÷ 45,000 kg', '', 'N1.00 per kg'],
        ['Y:  N55,000 ÷ 20,000 kg', '', 'N2.75 per kg'],
      ]}},
      {'h4': 'Check — the profit for the month'},
      {'stmt': {'t': 'Profit statement for November (N)', 'rows': [
        ['', 'Product X', 'Product Y', 'Total', '@hd'],
        ['Sales', 60000, 95000, 155000],
        ['Cost of production for the month', 45000, 55000, 100000],
        ['Less: closing inventory  (X: 15,000 kg × N1.00;  Y: nil)', -15000, 0, -15000],
        ['**Cost of sales**', 30000, 55000, 85000, '@t'],
        ['**Gross profit**', 30000, 40000, 70000, '@tt'],
      ]}},
      {'key': 'Notice that the **total** cost apportioned (N100,000) equals the total cost '
              'incurred in both departments — apportionment redistributes, it never changes the '
              'total. And notice the role of closing inventory: of the N100,000 spent, N15,000 '
              'is carried forward in X\'s unsold 15,000 kg, so only N85,000 is charged against '
              'this month\'s sales.'}]}},

    {'eg': {'tag': 'Exam type — Q12',
      't': 'Four refined products — cost of finished units on physical units and sales value',
      'q': [
      {'p': 'A firm operates a process which produces four refined products A, B, C and D. The '
            'joint costs of operating the process in December were:'},
      {'stmt': {'t': 'Joint costs for December (N)', 'rows': [
        ['Raw materials', '', 15000],
        ['Labour', '', 4800],
        ['Overhead', '', 1200],
        ['**Total joint cost**', '', 21000, '@tt'],
      ]}},
      {'stmt': {'t': 'Output, closing finished stock and prices', 'rows': [
        ['Product', 'Output for the period (kg)', 'Finished output at the end (kg)',
         'Price per kg (N)', '@hd'],
        ['A', 14000, 600, 0.20],
        ['B', 12000, 400, 0.45],
        ['C', 8000, 1600, 0.60],
        ['D', 2000, 100, 1.00],
      ]}},
      {'p': 'Work-in-progress at the beginning and end of the period is nil, as was finished '
            'output at the beginning of the month. The price is expected to be maintained '
            'shortly. **Required:** calculate the cost of the finished units using as the basis '
            'of calculation (a) physical units and (b) sales value.'}],
      'a': [
      {'h4': '(a)  Physical units basis'},
      {'tex': '\\text{Joint cost per kg} = \\frac{N21{,}000}{36{,}000 \\text{ kg}} '
              '= N0.58333 \\text{ per kg}'},
      {'stmt': {'t': 'Apportionment and the cost of closing finished stock — physical units',
        'rows': [
        ['Product', 'Output (kg)', 'Joint cost apportioned (N)', 'Finished stock (kg)',
         'Cost of finished stock (N)', '@hd'],
        ['A', 14000, 8166.67, 600, 350.00],
        ['B', 12000, 7000.00, 400, 233.33],
        ['C', 8000, 4666.67, 1600, 933.33],
        ['D', 2000, 1166.66, 100, 58.34],
        ['**Total**', 36000, 21000.00, 2700, 1575.00, '@tt'],
      ]}},
      {'h4': '(b)  Sales value basis'},
      {'stmt': {'t': 'Sales value of production', 'rows': [
        ['Product', 'Output (kg)', 'Price per kg (N)', 'Sales value (N)', '@hd'],
        ['A', 14000, 0.20, 2800],
        ['B', 12000, 0.45, 5400],
        ['C', 8000, 0.60, 4800],
        ['D', 2000, 1.00, 2000],
        ['**Total**', 36000, '', 15000, '@tt'],
      ]}},
      {'stmt': {'t': 'Apportionment and the cost of closing finished stock — sales value',
        'rows': [
        ['Product', 'Sales value (N)', 'Joint cost apportioned (N)', 'Cost per kg (N)',
         'Finished stock (kg)', 'Cost of finished stock (N)', '@hd'],
        ['A', 2800, 3920, 0.28, 600, 168],
        ['B', 5400, 7560, 0.63, 400, 252],
        ['C', 4800, 6720, 0.84, 1600, 1344],
        ['D', 2000, 2800, 1.40, 100, 140],
        ['**Total**', 15000, 21000, '', 2700, 1904, '@tt'],
      ]}},
      {'h4': 'Comparison, and a warning the figures contain'},
      {'stmt': {'t': 'Cost of the finished (closing) units compared (N)', 'rows': [
        ['Product', 'Physical units basis', 'Sales value basis', '@hd'],
        ['A', 350.00, 168],
        ['B', 233.33, 252],
        ['C', 933.33, 1344],
        ['D', 58.34, 140],
        ['**Total closing inventory value**', 1575.00, 1904, '@tt'],
      ]}},
      {'warn': 'Look at the sales-value column of costs per kg against the selling prices: A '
               'costs N0.28 and sells for N0.20; C costs N0.84 and sells for N0.60; every '
               'product costs exactly **140% of its selling price**. That is not an error in the '
               'apportionment — it is a true statement about the business. The joint cost of '
               'N21,000 exceeds the total sales value of N15,000, so the **process as a whole '
               'loses N6,000**, and under the sales-value method every product shares that loss '
               'proportionately. Under the physical-units method the loss is hidden on some '
               'products and exaggerated on others (A costs N0.583 per kg against a N0.20 '
               'price, while D costs N0.583 against a N1.00 price and appears highly '
               'profitable). Neither method rescues the process; the real question the figures '
               'raise is whether it should be run at all.'},
      {'key': 'This is the strongest argument for the sales-value basis: it never makes a '
              'product look profitable or unprofitable merely because of its physical bulk. '
              'Under physical units, D — the most valuable product per kilo — appears to earn a '
              'huge margin and A appears disastrous, which would tempt management into a '
              'decision about A that is impossible anyway, since A cannot be stopped without '
              'stopping D.'}]}},

    {'eg': {'tag': 'Exam type — Q13 (ICAN Foundation, May 1997)',
      't': 'JAY Chemicals — should the export order be accepted?',
      'q': [
      {'p': 'JAY Chemicals Ltd manufactures a range of industrial chemicals. Basic materials are '
            'put through an initial process which produces the ingredients for three products X, '
            'Y and Z. The ingredients for each product then undergo separate further processing '
            'to form the finished products. The budget for the year is:'},
      {'stmt': {'t': 'Budget for the year (N)', 'rows': [
        ['', 'Total', 'X', 'Y', 'Z', '@hd'],
        ['Sales (kilos)', 18000, 6000, 6000, 6000],
        ['Sales value', 540000, 180000, 240000, 120000],
        '@gap',
        ['**Joint cost apportioned**', '', '', '', '', '@hd'],
        ['Materials', 120000, 40000, 60000, 20000],
        ['Labour', 80000, 30000, 40000, 10000],
        ['Overheads', 100000, 30000, 50000, 20000],
        ['**Total joint cost**', 300000, 100000, 150000, 50000, '@t'],
        '@gap',
        ['**Separate further processing cost**', '', '', '', '', '@hd'],
        ['Material', '', 10000, 20000, 10000],
        ['Labour', '', 10000, 10000, 10000],
        ['Overhead', '', 20000, 20000, 20000],
        ['**Total**', '', 40000, 50000, 40000, '@t'],
        '@gap',
        ['**Profit**', 110000, 40000, 40000, 30000, '@tt'],
      ]}},
      {'ul': [
        'The overhead costs are **fixed**, except for the separate processing, where the '
        '**variable portion** is estimated at **N6,000 for X, N12,000 for Y and N3,000 for Z**.',
        'The company can increase its production by **25%** of the present level without '
        'incurring additional fixed costs. Market research has shown that to sell more than the '
        'budgeted quantities **in the present market**, prices would have to be reduced to: '
        '**X N28; Y N35; Z N18**.',
        'Although the products are jointly produced, sales of the products are independent of '
        'each other — an increase in the quantity sold of one product would not affect the sales '
        'of the others.',
        'A customer from a neighbouring country has offered to purchase: **X 1,500 kilos @ N27 '
        'per kilo; Y 500 kilos @ N37 per kilo; Z 1,000 kilos @ N18 per kilo**.',
        'Based on the budget for next year, direct labour will be working at **full capacity**. '
        'To meet the order the direct labour force will have to work **overtime, paid at time '
        'and a half**.',
      ]},
      {'p': '**Required:** evaluate whether the company should accept the order.'},
      {'note': 'The study text prints the overtime rate as "five and a half", which is not a '
               'rate. **Time and a half** is assumed below — the standard reading, and the only '
               'one that makes the question answerable. State the assumption.'}],
      'a': [
      {'h4': 'Step 1 — the principle'},
      {'p': 'This is a **short-run acceptance decision**, so only **relevant costs** matter '
            '(Chapter 9): costs that are **future**, **incremental** and **cash**. Fixed '
            'overhead is explicitly stated not to increase, so it is irrelevant. The apportioned '
            'joint cost is irrelevant **as an apportionment** — but the joint process must '
            'actually be run harder to produce the extra output, so its **variable** elements '
            '(materials and labour) are relevant.'},
      {'h4': 'Step 2 — variable cost per kilo, before overtime'},
      {'stmt': {'t': 'Budgeted variable costs per kilo (6,000 kg of each product)', 'rows': [
        ['', 'X', 'Y', 'Z', '@hd'],
        ['**Joint process (variable elements only)**', '', '', '', '@hd'],
        ['Materials  (40,000; 60,000; 20,000) ÷ 6,000', 6.667, 10.000, 3.333],
        ['Labour  (30,000; 40,000; 10,000) ÷ 6,000', 5.000, 6.667, 1.667],
        '@gap',
        ['**Separate further processing (variable elements only)**', '', '', '', '@hd'],
        ['Material  (10,000; 20,000; 10,000) ÷ 6,000', 1.667, 3.333, 1.667],
        ['Labour  (10,000; 10,000; 10,000) ÷ 6,000', 1.667, 1.667, 1.667],
        ['Variable overhead  (6,000; 12,000; 3,000) ÷ 6,000', 1.000, 2.000, 0.500],
        ['**Total variable cost per kilo**', 16.000, 23.667, 8.833, '@tt'],
      ]}},
      {'h4': 'Step 3 — the overtime premium'},
      {'p': 'Labour is at full capacity, so every extra kilo needs overtime at time and a half — '
            'a **premium of 50%** on the labour element, both in the joint process and in the '
            'further processing:'},
      {'stmt': {'t': 'Overtime premium per kilo (N)', 'rows': [
        ['', 'X', 'Y', 'Z', '@hd'],
        ['Joint process labour per kilo', 5.000, 6.667, 1.667],
        ['Separate processing labour per kilo', 1.667, 1.667, 1.667],
        ['**Total labour per kilo**', 6.667, 8.333, 3.333, '@t'],
        ['**Overtime premium at 50%**', 3.333, 4.167, 1.667, '@tt'],
      ]}},
      {'h4': 'Step 4 — evaluating the order'},
      {'stmt': {'t': 'Incremental profit from the export order (N)', 'rows': [
        ['', 'X', 'Y', 'Z', 'Total', '@hd'],
        ['Quantity offered (kilos)', 1500, 500, 1000, 3000],
        ['Offer price per kilo', 27.000, 37.000, 18.000, ''],
        ['Less: variable cost per kilo', 16.000, 23.667, 8.833, ''],
        ['Less: overtime premium per kilo', 3.333, 4.167, 1.667, ''],
        ['**Contribution per kilo**', 7.667, 9.166, 7.500, '', '@t'],
        ['**Total contribution**', 11500, 4583, 7500, 23583, '@tt'],
      ]}},
      {'h4': 'Step 5 — the alternative use of the spare capacity'},
      {'p': 'The 25% spare capacity could instead be used to sell more **in the present '
            'market** — but only by cutting the price, and the lower price would apply to the '
            'budgeted 6,000 kilos as well as to the extra:'},
      {'stmt': {'t': 'Selling the extra output at home instead (N)', 'rows': [
        ['', 'X (1,500 kg)', 'Y (500 kg)', 'Z (1,000 kg)', '@hd'],
        ['Budgeted price', 30, 40, 20],
        ['Reduced price needed to sell more', 28, 35, 18],
        ['Revenue at the reduced price  (7,500×28; 6,500×35; 7,000×18)', 210000, 227500, 126000],
        ['Less: budgeted revenue at the old price', -180000, -240000, -120000],
        ['**Net change in revenue**', 30000, -12500, 6000, '@t'],
        ['Less: extra variable cost + overtime premium', -28999, -13917, -10500],
        ['**Net benefit (loss) of selling at home**', 1001, -26417, -4500, '@tt'],
      ]}},
      {'h4': 'Conclusion and recommendation'},
      {'stmt': {'t': 'Export order compared with the home-market alternative (N)', 'rows': [
        ['', 'X', 'Y', 'Z', 'Total', '@hd'],
        ['Gain from accepting the export order', 11500, 4583, 7500, 23583],
        ['Gain (loss) from cutting home prices instead', 1001, -26417, -4500, -29916],
        ['**Advantage of the export order**', 10499, 31000, 12000, 53499, '@tt'],
      ]}},
      {'p': '**Recommendation: accept the order.** It increases profit by **N23,583** — none of '
            'the fixed overhead changes, and every product\'s offer price comfortably exceeds '
            'its incremental cost, even after the overtime premium. It is also better than the '
            'only alternative use of the capacity in all three cases, decisively so for Y and Z, '
            'where cutting the home price to shift the extra output would actually destroy '
            'profit.'},
      {'warn': 'Three qualifications a full answer should state. **(1)** The products are '
               '**jointly produced**: running the joint process 25% harder yields 1,500 extra '
               'kilos of **each** product, but the order takes only 500 of Y and 1,000 of Z, so '
               'there would be surplus Y and Z to dispose of. The question\'s statement that '
               'sales are independent is taken as licence to evaluate each product separately, '
               'but in practice the surplus must be sold, stored or dumped, and its disposal '
               'value would need to be brought in. **(2)** Selling abroad at N27 while the home '
               'price is N30 risks the discounted goods finding their way back into the home '
               'market, and may provoke dumping complaints. **(3)** Accepting at these prices '
               'may make it harder to charge full prices to this customer, or to others, in '
               'future.'}]}},

    {'eg': {'tag': 'Exam type — Q14 (ICAN PE I, November)',
      't': 'Okoro Ltd — unit sales prices under two overhead absorption bases',
      'q': [
      {'p': 'Okoro Ltd is deciding the sales price for two products, **wids** and **leads**. '
            'Both are made by the same workforce in the same department. **N30,000 direct '
            'labour hours** are budgeted for the year. Budgeted **fixed costs are N30,000**, and '
            'the department is expected to operate at **full capacity**. Variable costs per unit '
            'are:'},
      {'stmt': {'t': 'Variable cost per unit (N)', 'rows': [
        ['', 'Wids', 'Leads', '@hd'],
        ['Materials', 4, 4],
        ['Labour  (wids 2 hours;  leads 3 hours, at N3 per hour)', 6, 9],
        ['Expenses  (1 machine hour each, at N2 per machine hour)', 2, 2],
        ['**Total variable cost per unit**', 12, 15, '@tt'],
      ]}},
      {'p': 'Expected sales demand is roughly **7,500 wids** and **5,000 leads**. **Required:** '
            'what would the unit sales prices be to give a profit of **20% on full cost** if '
            'overheads are absorbed (a) on a direct labour hour basis, and (b) on a machine hour '
            'basis?'},
      {'warn': 'The variable cost table is mis-typeset in the study text: its three figures for '
               'wids are printed in the order 4, 2, 6 while the underlining shows 6 as the last '
               'addend, and the hour labels sit on the wrong rows. The reading above is the only '
               'one that is internally consistent — it gives a **single labour rate of N3 per '
               'hour for both products** (the question says they are made by the same '
               'workforce), totals of N12 and N15 exactly as printed, and a labour requirement '
               'of $7{,}500 \\times 2 + 5{,}000 \\times 3 = 30{,}000$ hours, which is '
               'precisely the budgeted capacity the question states.',
       'lbl': 'Source data reconstructed — and confirmed'}],
      'a': [
      {'h4': 'Step 1 — the activity levels'},
      {'stmt': {'t': 'Budgeted activity', 'rows': [
        ['', 'Wids', 'Leads', 'Total', '@hd'],
        ['Expected demand (units)', 7500, 5000, ''],
        ['Direct labour hours per unit', 2, 3, ''],
        ['**Total direct labour hours**', 15000, 15000, 30000, '@t'],
        ['Machine hours per unit', 1, 1, ''],
        ['**Total machine hours**', 7500, 5000, 12500, '@t'],
      ]}},
      {'note': 'The direct labour hours come to exactly the 30,000 budgeted, confirming the '
               'statement that the department operates at full capacity — a useful check that '
               'the reconstructed data are right.'},
      {'h4': 'Step 2 — the two absorption rates'},
      {'stmt': {'t': 'Fixed overhead absorption rates', 'rows': [
        ['(a) Direct labour hour basis:  N30,000 ÷ 30,000 hours', '', '**N1.00 per labour '
         'hour**'],
        ['(b) Machine hour basis:  N30,000 ÷ 12,500 hours', '', '**N2.40 per machine hour**'],
      ]}},
      {'h4': '(a)  Prices on a direct labour hour basis'},
      {'stmt': {'t': 'Unit price — overhead absorbed on direct labour hours (N)', 'rows': [
        ['', 'Wids', 'Leads', '@hd'],
        ['Variable cost per unit', 12.00, 15.00],
        ['Fixed overhead absorbed  (2 hrs × N1.00;  3 hrs × N1.00)', 2.00, 3.00],
        ['**Full cost per unit**', 14.00, 18.00, '@t'],
        ['Add: profit at 20% of full cost', 2.80, 3.60],
        ['**Unit sales price**', 16.80, 21.60, '@tt'],
      ]}},
      {'h4': '(b)  Prices on a machine hour basis'},
      {'stmt': {'t': 'Unit price — overhead absorbed on machine hours (N)', 'rows': [
        ['', 'Wids', 'Leads', '@hd'],
        ['Variable cost per unit', 12.00, 15.00],
        ['Fixed overhead absorbed  (1 hr × N2.40;  1 hr × N2.40)', 2.40, 2.40],
        ['**Full cost per unit**', 14.40, 17.40, '@t'],
        ['Add: profit at 20% of full cost', 2.88, 3.48],
        ['**Unit sales price**', 17.28, 20.88, '@tt'],
      ]}},
      {'h4': 'Check — total profit is the same either way'},
      {'stmt': {'t': 'Total profit under each basis (N)', 'rows': [
        ['', 'Labour hour basis', 'Machine hour basis', '@hd'],
        ['Wids:  7,500 × (16.80 − 12.00);  7,500 × (17.28 − 12.00)', 36000, 39600],
        ['Leads: 5,000 × (21.60 − 15.00);  5,000 × (20.88 − 15.00)', 33000, 29400],
        ['**Total contribution**', 69000, 69000, '@t'],
        ['Less: fixed costs', -30000, -30000],
        ['**Profit**', 39000, 39000, '@tt'],
      ]}},
      {'key': 'The same N39,000 profit either way — which is the whole point. Changing the '
              'absorption base cannot change the total profit; it only changes **which product '
              'is asked to earn it**. On a labour hour basis, leads (3 hours each) carry more '
              'overhead and are priced at N21.60; on a machine hour basis, where both products '
              'use one machine hour, leads carry the same overhead as wids and the price falls '
              'to N20.88 while wids rise to N17.28. Which base is right depends entirely on '
              'whether the N30,000 of fixed cost is actually driven by labour time or by machine '
              'time — and that is a question of fact about the department, not of accounting '
              'preference.'}]}},

    {'eg': {'tag': 'Exam type — Q15 (12½ marks)',
      't': 'MMM Ltd — equivalent production, cost per unit, evaluation and the Process I account',
      'q': [
      {'p': '**(a)** Summarise what you understand by **abnormal loss**, and show how it is '
            'treated in process costing.'},
      {'p': '**(b)** The data below relate to Process I for January 2017, as extracted from the '
            'books of MMM Ltd.'},
      {'stmt': {'t': 'Process I — January 2017', 'rows': [
        ['2 January 2017:  Input', '', '40,000 units'],
        ['                      Opening WIP', '', 'Nil'],
        '@gap',
        ['**Process costs (N)**', '', '', '@hd'],
        ['Material', '', 1140000],
        ['Labour', '', 633600],
        ['Overhead', '', 528000],
        '@gap',
        ['**31 January 2017 (units)**', '', '', '@hd'],
        ['Output', '', 32000],
        ['Closing WIP', '', 8000],
        '@gap',
        ['**Degree of completion of closing WIP**', '', '', '@hd'],
        ['Materials', '', '75%'],
        ['Labour', '', '40%'],
        ['Overhead', '', '40%'],
      ]}},
      {'p': '**Required:** determine (i) equivalent production units; (ii) cost per unit of '
            'equivalent production; (iii) the statement of evaluation; (iv) the Process I '
            'account.'}],
      'a': [
      {'h4': '(a)  Abnormal loss and its treatment'},
      {'def': {'t': 'Abnormal loss', 'd': 'the part of a process loss that **exceeds the normal '
                    'loss** — loss that was not expected under efficient operating conditions '
                    'and is therefore avoidable.'}},
      {'tex': '\\text{Abnormal loss} = \\text{Actual loss} - \\text{Normal loss}'},
      {'p': '**Its treatment in process costing:**'},
      {'ol': [
        'It is **valued at the full cost per good unit** of the process — the same rate as good '
        'output — because it consumed exactly the same materials, labour and overhead as a good '
        'unit did.',
        'It is **credited to the process account** (in both units and value) and **debited to an '
        'Abnormal Loss Account**, so that it is removed from the cost of good production.',
        'Any **scrap proceeds** from the abnormally lost units are **credited to the Abnormal '
        'Loss Account**, not to the process account.',
        'The **balance of the Abnormal Loss Account is written off to the costing profit and '
        'loss account** as a period loss.',
        'The effect — and the purpose — is that the cost of good production is **not inflated** '
        'by inefficiency: good units bear only normal loss, while abnormal loss is separately '
        'reported so management can see it and investigate.',
        'The mirror image is the **abnormal gain**, which arises when actual loss is *less* than '
        'normal. It is debited to the process account and credited to an Abnormal Gain Account, '
        'which is then charged with the scrap income foregone and the balance credited to profit '
        'and loss.',
      ]},
      {'h4': '(b)(i)  Equivalent production units'},
      {'stmt': {'t': 'Statement of equivalent production', 'rows': [
        ['', 'Physical units', 'Materials', 'Labour', 'Overhead', '@hd'],
        ['Output completed and transferred', 32000, 32000, 32000, 32000],
        ['Closing WIP  (75% materials;  40% labour;  40% overhead)', 8000, 6000, 3200, 3200],
        ['**Equivalent production units**', 40000, 38000, 35200, 35200, '@tt'],
      ]}},
      {'h4': '(b)(ii)  Cost per unit of equivalent production'},
      {'stmt': {'t': 'Statement of cost per equivalent unit', 'rows': [
        ['', 'Cost (N)', 'Equivalent units', 'Cost per unit (N)', '@hd'],
        ['Materials', 1140000, 38000, 30],
        ['Labour', 633600, 35200, 18],
        ['Overhead', 528000, 35200, 15],
        ['**Total**', 2301600, '', 63, '@tt'],
      ]}},
      {'h4': '(b)(iii)  Statement of evaluation'},
      {'stmt': {'t': 'Statement of evaluation (N)', 'rows': [
        ['**Finished output transferred:  32,000 units × N63**', '', 2016000],
        '@gap',
        ['**Closing work-in-progress**', '', '', '@hd'],
        ['Materials:  6,000 equivalent units × N30', 180000, ''],
        ['Labour:  3,200 equivalent units × N18', 57600, ''],
        ['Overhead:  3,200 equivalent units × N15', 48000, 285600],
        '@gap',
        ['**Total cost accounted for**', '', 2301600, '@tt'],
      ]}},
      {'h4': '(b)(iv)  Process I Account'},
      {'tacc': {'t': 'Process I Account — January 2017', 'drl': 'Dr  (units / N)',
        'crl': 'Cr  (units / N)',
        'dr': [['Material  (40,000 units)', 1140000], ['Labour', 633600], ['Overhead', 528000],
               ['', 2301600, '@tot']],
        'cr': [['Transfer to Process II  (32,000 units)', 2016000],
               ['Closing work-in-progress c/d  (8,000 units)', 285600],
               ['', 2301600, '@tot']]}},
      {'key': 'There is no normal or abnormal loss in this question — 40,000 units in, 40,000 '
              'accounted for — so the whole difficulty is the **equivalent units**. Note that '
              'the three cost elements have three **different** completion percentages and '
              'therefore three different denominators (38,000, 35,200, 35,200): materials are '
              '75% complete while labour and overhead are only 40%. Using one denominator for '
              'all three is the single commonest error in this topic, and it would give a cost '
              'per unit of $2{,}301{,}600 \\div 38{,}000 = N60.57$ instead of the correct '
              'N63.'}]}},

    {'eg': {'tag': 'Exam type — Q16 (12½ marks)',
      't': 'Tamco Limited — two process accounts with an abnormal loss and an abnormal gain',
      'q': [
      {'p': 'Tamco Limited manufactures the product TACO, which passes through two distinct '
            'processes before it is turned out as a finished product.'},
      {'stmt': {'t': 'Input details (N)', 'rows': [
        ['Item', 'Process L', 'Process M', 'Total', '@hd'],
        ['Direct materials', 400000, 158000, 558000],
        ['Direct wages', 200000, 80000, 280000],
        ['Production overhead', 110000, 90000, 200000],
      ]}},
      {'p': '**20,000 units @ N3** were introduced to Process L. The output of Process L passes '
            'to Process M, where finished goods are obtained and forwarded to the warehouse.'},
      {'stmt': {'t': 'Output, normal loss and scrap', 'rows': [
        ['', 'Actual output (units)', 'Normal loss as % of input', 'Total scrap realised (N)',
         '@hd'],
        ['Process L', 18900, '5%', 10000],
        ['Process M', 18000, '5%', 6700],
      ]}},
      {'p': '**Required:** prepare (a) the process accounts; and (b) the process losses and '
            'process gain accounts.'}],
      'a': [
      {'h4': 'Step 1 — Process L: the loss position'},
      {'stmt': {'t': 'Process L — physical units', 'rows': [
        ['Input introduced', '', '20,000 units'],
        ['Normal loss:  5% × 20,000', '', '1,000 units'],
        ['**Expected output**', '', '19,000 units', '@t'],
        ['Actual output', '', '18,900 units'],
        ['**Abnormal loss**  (19,000 − 18,900)', '', '100 units', '@tt'],
      ]}},
      {'stmt': {'t': 'Process L — cost per unit', 'rows': [
        ['Units introduced:  20,000 × N3', '', 60000],
        ['Direct materials', '', 400000],
        ['Direct wages', '', 200000],
        ['Production overhead', '', 110000],
        ['**Total cost of Process L**', '', 770000, '@t'],
        ['Less: scrap value of normal loss', '', -10000],
        ['**Net cost**', '', 760000, '@t'],
        ['÷ expected output (20,000 − 1,000)', '', '19,000 units'],
        ['**Cost per unit**', '', 'N40.00', '@tt'],
      ]}},
      {'note': 'Scrap realises $N10{,}000 \\div 1{,}000 = N10$ **per unit**, which is the rate '
               'used to credit the abnormally lost units with their scrap proceeds below.'},
      {'h4': '(a)  Process L Account'},
      {'tacc': {'t': 'Process L Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Units introduced — 20,000 @ N3', 60000], ['Direct materials', 400000],
               ['Direct wages', 200000], ['Production overhead', 110000],
               ['', 770000, '@tot']],
        'cr': [['Normal loss — 1,000 units @ N10 scrap', 10000],
               ['Abnormal loss — 100 units @ N40', 4000],
               ['Transfer to Process M — 18,900 units @ N40', 756000],
               ['', 770000, '@tot']]}},
      {'h4': 'Step 2 — Process M: the loss position'},
      {'stmt': {'t': 'Process M — physical units', 'rows': [
        ['Input transferred from Process L', '', '18,900 units'],
        ['Normal loss:  5% × 18,900', '', '945 units'],
        ['**Expected output**', '', '17,955 units', '@t'],
        ['Actual output', '', '18,000 units'],
        ['**Abnormal GAIN**  (18,000 − 17,955)', '', '45 units', '@tt'],
      ]}},
      {'stmt': {'t': 'Process M — cost per unit', 'rows': [
        ['Transferred in from Process L — 18,900 units', '', 756000],
        ['Direct materials', '', 158000],
        ['Direct wages', '', 80000],
        ['Production overhead', '', 90000],
        ['**Total cost of Process M**', '', 1084000, '@t'],
        ['Less: scrap value of normal loss', '', -6700],
        ['**Net cost**', '', 1077300, '@t'],
        ['÷ expected output (18,900 − 945)', '', '17,955 units'],
        ['**Cost per unit**', '', 'N60.00', '@tt'],
      ]}},
      {'h4': '(a)  Process M Account'},
      {'tacc': {'t': 'Process M Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Transfer from Process L — 18,900 units', 756000],
               ['Direct materials', 158000], ['Direct wages', 80000],
               ['Production overhead', 90000],
               ['Abnormal gain — 45 units @ N60', 2700], ['', 1086700, '@tot']],
        'cr': [['Normal loss — 945 units @ N7.0899 scrap', 6700],
               ['Finished goods — 18,000 units @ N60', 1080000],
               ['', 1086700, '@tot']]}},
      {'warn': 'An **abnormal gain** is entered on the **debit** side of the process account '
               '(and in the units column), which is the opposite side from an abnormal loss. '
               'The logic: the process produced more good units than it should have, so the '
               'account must be grossed up to carry them at the normal cost per unit. The '
               'corresponding credit goes to the Abnormal Gain Account.'},
      {'h4': '(b)  Abnormal Loss Account (Process L)'},
      {'tacc': {'t': 'Abnormal Loss Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Process L — 100 units @ N40', 4000], ['', 4000, '@tot']],
        'cr': [['Cash / scrap — 100 units @ N10', 1000],
               ['Costing Profit and Loss Account', 3000], ['', 4000, '@tot']]}},
      {'h4': '(b)  Abnormal Gain Account (Process M)'},
      {'tacc': {'t': 'Abnormal Gain Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Normal loss (scrap) account — 45 units @ N7.0899', 319.05],
               ['Costing Profit and Loss Account', 2380.95], ['', 2700.00, '@tot']],
        'cr': [['Process M — 45 units @ N60', 2700.00], ['', 2700.00, '@tot']]}},
      {'h4': '(b)  Normal Loss (Scrap) Account'},
      {'tacc': {'t': 'Normal Loss / Scrap Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Process L — 1,000 units', 10000.00], ['Process M — 945 units', 6700.00],
               ['', 16700.00, '@tot']],
        'cr': [['Abnormal gain — scrap forgone, 45 units @ N7.0899', 319.05],
               ['Cash — scrap actually sold', 16380.95], ['', 16700.00, '@tot']]}},
      {'key': 'Note the scrap adjustment on the abnormal gain, which candidates routinely omit. '
              'Because Process M produced 45 units **more** than expected, it also produced 45 '
              'units **less** scrap than expected — so the scrap income credited to the process '
              'as normal loss was never actually earned. The Abnormal Gain Account is therefore '
              'charged with that forgone scrap (45 × N7.0899 = N319.05), and only the net '
              'N2,380.95 is credited to profit. The mirror of this is the Abnormal Loss Account, '
              'which is **credited** with the scrap the extra lost units did realise.'},
      {'note': 'Both process accounts balance exactly, and the cost per unit comes out at a '
               'round N40 and N60 — the strongest possible confirmation that the normal loss '
               'percentages, scrap values and transfers have all been read correctly from a '
               'question whose data table was printed with its columns out of alignment.'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Total equivalent production', 'tex': '\\text{Completed units} + (\\% \\text{ '
   'complete} \\times \\text{WIP units})'},
  {'lb': 'Cost per equivalent unit', 'tex': '\\dfrac{\\text{Total cost}}{\\text{Total '
   'equivalent production}}'},
  {'lb': 'Value of WIP (balancing figure)', 'tex': '\\text{Total cost} - \\text{Value of '
   'completed production}'},
  {'lb': 'Net Realisable Value', 'tex': '\\text{Sales value} - \\text{Separate processing/'
   'marketing cost}'},
  {'lb': 'Net joint cost, after a by-product', 'tex': '\\text{Total joint cost} - \\text{By-'
   'product NRV}'},
  {'lb': 'Total cost per unit of a joint product', 'tex': '\\dfrac{\\text{Share of joint cost} + '
   '\\text{Further processing cost}}{\\text{Units produced}}'},
 ],
 'focus':
   'Process costing with equivalent units, and joint-cost apportionment, are together one of '
   'the most heavily-weighted topics in the whole syllabus — expect at least one full Section B '
   'question most diets. Master the WAP/FIFO distinction as "does this method blend opening WIP '
   'cost with current cost, or keep them separate?" rather than memorising two unrelated '
   'procedures — every other difference between them follows from that one question. For joint '
   'products, always compute a product\'s *total* cost (share of joint cost plus further '
   'processing) before using it to value inventory — the NRV-basis apportionment figure alone '
   'is not yet a full unit cost.',
 'errors': [
   'Confusing normal loss (folded into good production\'s cost) with abnormal loss (charged '
   'straight to P&L) — this is the single most common error in process-costing questions.',
   'Using total equivalent units instead of *current-period* equivalent units when finding a '
   'FIFO unit cost — FIFO divides only by the units\' worth of work actually done *this* period.',
   'Forgetting that a cost element added only at the *end* of a process (like Process 2\'s '
   'material in Illustration 8.5) has **zero** equivalent units in any closing WIP, however far '
   'advanced that WIP is on conversion.',
   'Treating the physical-units basis of joint-cost apportionment as if it reflects value — by '
   'construction, it gives every joint product exactly the same cost per unit.',
   'Valuing joint-product closing inventory at the NRV-basis apportionment figure alone, without '
   'adding the product\'s own further processing cost to get its *total* cost per unit first.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In process costing, the cost of a *normal* process loss is',
    'o': ['charged directly to the Profit and Loss Account', 'ignored entirely',
          'included as part of the cost of good production', 'carried forward indefinitely as '
          'work-in-progress', 'shared equally between all other processes'],
    'a': 2,
    'w': 'Normal loss is unavoidable and arises under efficient conditions, so its cost is '
         'folded into the cost of good production — unlike abnormal loss, which is charged to '
         'the P&L.',
    'src': 'Chapter 8.2', 'sec': '8.2'},
   {'q': 'A process has an input of 200 units, with normal wastage set at 10% of input. '
         'Expected output is therefore',
    'o': ['200 units', '190 units', '180 units', '20 units', '220 units'],
    'a': 1,
    'w': 'Normal wastage = 10% × 200 = 20 units, so expected output = input − normal wastage = '
         '200 − 20 = 180 units.',
    'calc': '200 - (10\\% \\times 200) = 180',
    'src': 'Chapter 8.2', 'sec': '8.2'},
   {'q': 'Actual output from a process is 95 units, against an expected output (after normal '
         'wastage) of 90 units. This 5-unit difference is',
    'o': ['an abnormal loss', 'an abnormal gain', 'a normal loss', 'a joint product',
          'a by-product'],
    'a': 1,
    'w': 'Where actual output exceeds expected output (i.e. actual loss is less than normal '
         'loss), the difference is an abnormal gain.',
    'src': 'Chapter 8.2', 'sec': '8.2'},
   {'q': 'A period has 6,000 completed units and 1,000 units of closing WIP that are 40% '
         'complete. Total equivalent production is',
    'o': ['6,000 units', '6,400 units', '7,000 units', '400 units', '6,040 units'],
    'a': 1,
    'w': 'Total equivalent production = completed units + (% complete × WIP units) = 6,000 + '
         '(0.4 × 1,000) = 6,400 units.',
    'calc': '6{,}000 + (0.4 \\times 1{,}000) = 6{,}400',
    'src': 'Chapter 8.3', 'sec': '8.3'},
   {'q': 'Compared with the FIFO method, the weighted average method of process costing',
    'o': ['ignores opening work-in-progress entirely',
          'blends opening WIP cost together with current-period cost, over combined equivalent '
          'units', 'can only be used where there is no closing WIP',
          'is identical to FIFO in every respect', 'is used only for joint products'],
    'a': 1,
    'w': 'WAP blends opening WIP\'s cost with the current period\'s cost and spreads the total '
         'over combined equivalent units; FIFO keeps only current-period cost over current-'
         'period equivalent units, treating opening WIP as completed and out first.',
    'src': 'Chapter 8.4', 'sec': '8.4'},
   {'q': 'A cost element is added only at the very end of a process. For a unit of closing WIP '
         'that is 70% complete on conversion but has not yet reached the end of the process, '
         'the equivalent units for that end-of-process cost element are',
    'o': ['70% of the unit', '100% of the unit', '0% of the unit', '30% of the unit',
          'undefined'],
    'a': 2,
    'w': 'If the cost element is added only at the very end, no WIP unit that has not reached '
         'the end has received any of it yet — its equivalent units for that element are 0%, '
         'regardless of how advanced it is on any other element.',
    'src': 'Chapter 8.4', 'sec': '8.4'},
   {'q': 'Under the physical units basis of joint-cost apportionment, different joint products '
         'will end up with',
    'o': ['different unit costs, reflecting their different market values',
          'exactly the same cost per physical unit, regardless of value',
          'zero joint cost apportioned to them', 'costs based only on their selling price',
          'costs based only on further processing cost'],
    'a': 1,
    'w': 'Because physical units basis shares joint cost purely by quantity, every joint product '
         'ends up costed at exactly the same rate per unit — a direct consequence of ignoring '
         'value.',
    'src': 'Chapter 8.6', 'sec': '8.6'},
   {'q': 'The method of apportioning joint cost regarded as the "best," because it accounts for '
         'quantity, sales value and further processing cost together, is the',
    'o': ['physical units basis', 'sales value at split-off basis', 'Net Realisable Value (NRV) '
          'basis', 'blanket rate basis', 'standard costing basis'],
    'a': 2,
    'w': 'The NRV basis is the only one of the three that considers quantity produced, sales '
         'value, and further processing cost all together.',
    'src': 'Chapter 8.6', 'sec': '8.6'},
   {'q': 'A by-product\'s Net Realisable Value is deducted from the total joint cost before the '
         'remaining cost is shared among the main/joint products. This treatment effectively',
    'o': ['charges the by-product nothing at all',
          'assigns the by-product a joint cost equal to its own NRV',
          'assigns the by-product the entire joint cost',
          'converts the by-product into a main product automatically',
          'has no effect on the main products\' costs'],
    'a': 1,
    'w': 'Deducting the by-product\'s NRV from joint cost is, in effect, assigning the by-'
         'product a share of joint cost exactly equal to its own NRV — no further allocation '
         'step is needed for it.',
    'src': 'Chapter 8.5', 'sec': '8.5'},
   {'q': 'For professional-service organisations such as architects\' or accountants\' offices, '
         'where services genuinely differ from one client to the next, the appropriate costing '
         'method is',
    'o': ['standard service (operation) costing', 'process costing', 'job costing',
          'joint-product costing', 'blanket-rate costing'],
    'a': 2,
    'w': 'Since each client engagement differs, job costing — costing each engagement as its '
         'own distinct job — is the appropriate method, not standardised service costing.',
    'src': 'Chapter 8.7', 'sec': '8.7'},
  ],
  'theory': [
   {'q': 'Differentiate between: (a) Actual spoilage and normal spoilage, (b) Conversion cost '
         'and overhead cost, (c) Material cost and transferred-in cost, (d) WAP and FIFO '
         'methods in process costing.',
    'marks': 12,
    'a': [
      {'p': '**(a)** Normal spoilage is the *expected*, unavoidable loss under efficient '
            'operating conditions, estimated in advance. Actual spoilage is what genuinely '
            'occurs in the period — the difference between the two (if actual exceeds normal) '
            'is abnormal loss, or (if normal exceeds actual) abnormal gain.'},
      {'p': '**(b)** Conversion cost is direct labour plus production overhead together — the '
            'cost of turning material into a finished product. Overhead cost is only the '
            'indirect-cost component of that, a narrower category than conversion cost.'},
      {'p': '**(c)** Material cost is the cost of raw material added *within* a given process. '
            'Transferred-in cost is the cost of output *received from a previous process*, '
            'which becomes that process\'s own input material — always 100% complete by '
            'definition, unlike ordinary material which may be only partly added to WIP.'},
      {'p': '**(d)** WAP blends opening WIP cost with current-period cost and divides by '
            'combined equivalent units, giving one blended unit cost. FIFO keeps opening WIP\'s '
            'cost separate, dividing only current-period cost by current-period equivalent '
            'units, and treats opening WIP as completed and transferred out first.'},
    ], 'src': 'Chapter 8.4', 'sec': '8.4'},
   {'q': 'Differentiate clearly between joint product, by-product and main product in a joint '
         'costing system.',
    'marks': 8,
    'a': [
      {'p': 'All three arise from processing the same raw material to a common split-off point. '
            'The **main product** is the one identified as the primary purpose of the process '
            '(e.g. petrol, from refining crude oil) — typically representing more than 40% of '
            'the main product\'s own value by the study text\'s guideline (i.e., it *is* the '
            'reference point). A **joint product** is a genuinely significant co-product, '
            'roughly 15–40% of the main product\'s value, sold as a real product in its own '
            'right. A **by-product** is a minor, incidental output of lesser value (roughly '
            '10–15% or less of the main product\'s value) — its NRV is simply deducted from '
            'joint cost rather than being apportioned a full separate share.'},
    ], 'src': 'Chapter 8.5', 'sec': '8.5'},
  ]},
}
