CH = {
 'n': 7,
 't': 'Costing Methods: Specific Order Costing',
 'brief': 'The four specific-order costing methods — job, batch, contract and service costing — '
          'used wherever output can be identified and tracked through production as a distinct '
          'unit, as opposed to the continuous-flow process costing of Chapter 8. Covers the '
          'overhead-absorption bases used in job costing (with fully verified illustrations), '
          'batch costing\'s set-up-cost economics, the full contract-costing profit-recognition '
          'framework across a contract\'s three life stages, and service (operation) costing.',
 'outcomes': [
   'Appreciate what order costing is and how it differs from process costing',
   'Understand the methods of absorbing overhead by jobs, batches, contracts, services or '
   'products',
   'Appreciate the important features of batch, service and contract costing',
   'Account for the value of a product, service, batch or contract',
   'Account for the total cost of an order, for effective pricing decisions',
 ],
 'secs': [
  {'n': '7.1', 't': 'Order costing — the concept', 'b': [
    {'def': {'t': 'Order (specific-order) costing', 'd': 'a technique used where expenses are '
                  'linked to specific products or services ordered — jobs, batches or contracts '
                  '— that can be identified individually through every stage of production. Job '
                  'costing, contract costing and batch costing are all specific-order costing '
                  'methods.'}},
    {'p': 'Typical users: construction (bridges, roads), building (houses, offices), machine-'
          'tool manufacturing, printing (books, journals, newsletters), general engineering — '
          'anywhere a product is made to a customer\'s own specification — and batches of '
          'similar articles (shoes, bags, shirts). Order costing is a basic procedure that can '
          'be combined with other costing techniques.'},
    {'p': 'Its main purpose is to find the profit or loss on **each individual order** — total '
          'cost per order must be estimated as accurately as possible for the price charged to '
          'yield a reasonable profit. It lets organisations (private or public) distinguish '
          'profitable from unprofitable orders, compare against past estimates to assess '
          'productivity, and price "cost plus" government/other contracts (price = agreed cost '
          '+ agreed target profit).'},
  ]},

  {'n': '7.2', 't': 'Job costing', 'b': [
    {'h4': 'Job order costing procedure'},
    {'p': 'Costing a job, batch or contract means aggregating every cost element behind the '
          'final product — needing solid production-control records. Every job gets its own '
          '**order number**, cited at every stage of production. A very large order should be '
          'split into separate, numbered **batches** (e.g. order 30 → batches 30.1, 30.2, 30.3), '
          'so costing can proceed without waiting for the whole order to finish.'},
    {'p': 'Each order goes into the production-control records, and a **job cost sheet** (job '
          'ledger account) is prepared — recording material used, wages paid, and machine time '
          'taken. Departmental general overhead is apportioned so each job/batch/contract '
          'absorbs its fair share.'},
    {'note': 'The **Job Card** is supplementary to the formal cost book-keeping system — it '
             'exists independently, for up-to-date shop-floor control. In a jobbing concern '
             '(e.g. a motor garage), the job card typically lives on the shop floor, while the '
             'actual costs flow into the cost ledger through the normal source documents '
             '(Material Requisition Note, Wages Analysis Journal, Expenses Analysis Book).'},

    {'h4': 'Overhead absorption methods in job costing'},
    {'p': 'A job\'s direct material, direct wages and direct expenses are totalled, then '
          'overhead is applied by one of the arbitrary bases already met in Chapter 5 §5.5: a '
          'percentage of direct material/labour/prime cost, a cost-unit rate, or a time rate '
          '(machine-hour or direct-labour-hour). Adding production overhead gives **production '
          'cost**; adding a further share of administration/selling/distribution overhead (each '
          'job absorbing its portion, unless treated as a direct P&L charge) gives **total '
          'cost**.'},
    {'key': 'Charging a production cost centre\'s overhead to every unit passing through it is '
            '**absorption** — the exact same concept from Chapter 5, just applied at the level '
            'of one job rather than one whole cost centre.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 7.1 — percentage rate on direct wages',
      'open': True, 'q': [
      {'p': 'Star Modern Shoemakers: annual direct wages N8,000,000, direct materials '
            'N5,000,000, direct expenses N1,500,000, production overhead N2,400,000, 160,000 '
            'units. A job of 500 pairs had direct wages N8,000, direct material N5,000, direct '
            'expenses N1,500. Fixed overhead is apportioned on % of direct wages; admin at 15% '
            'and selling at 10% of production cost. Find production cost, total cost, and cost '
            'per pair.'}],
      'a': [
      {'p': 'Overhead rate $= \\dfrac{2{,}400{,}000}{8{,}000{,}000} \\times 100 = 30\\%$ of '
            'direct wages. Job overhead $= 30\\% \\times 8{,}000 = N2{,}400$.'},
      {'table': {'align': 'lr', 'head': ['', 'N'], 'rows': [
        ['Direct wages', '8,000'], ['Direct material cost', '5,000'],
        ['Direct expenses', '1,500'], ['**Prime cost**', '**14,500**'],
        ['Production overhead', '2,400'], ['**(a) Production cost**', '**16,900**'],
        ['Admin. expenses (15% × 16,900)', '2,535'], ['Selling expenses (10% × 16,900)', '1,690'],
        ['**(b) Total cost**', '**21,125**'],
      ]}},
      {'tex': '\\text{(c) Cost per pair} = \\dfrac{21{,}125}{500} = N42.25'}]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 7.2 — percentage rate on direct material '
      'cost', 'open': True, 'q': [
      {'p': 'Same shoemaker, same job, but fixed overhead is now apportioned on % of direct '
            'material cost instead (overhead rate works out at 80% of direct material). Find '
            'production cost, total cost and cost per pair.'}],
      'a': [
      {'p': 'Job overhead $= 80\\% \\times 5{,}000 = N4{,}000$.'},
      {'table': {'align': 'lr', 'head': ['', 'N'], 'rows': [
        ['Direct wages', '8,000'], ['Direct material cost', '5,000'],
        ['Direct expenses', '1,500'], ['**Prime cost**', '**14,500**'],
        ['Production overhead', '4,000'], ['**(i) Production cost**', '**18,500**'],
        ['Admin. expenses (15% × 18,500)', '2,775'], ['Selling expenses (10% × 18,500)', '1,850'],
        ['**(ii) Total cost**', '**23,125**'],
      ]}},
      {'tex': '\\text{(iii) Cost per pair} = \\dfrac{23{,}125}{500} = N46.25'},
      {'note': 'The two illustrations use the **same job**, but changing only the overhead '
               'basis moves the cost per pair from N42.25 to N46.25 — a direct demonstration of '
               'why choosing the right absorption basis matters, not just getting the arithmetic '
               'right once a basis is chosen.'}]}},
    {'p': 'Choosing between the two: percentage-on-direct-wages suits situations where overhead '
          'is small relative to wages, wages are the major cost component, labour type/pay rates '
          'are similar, and machinery use is low. Percentage-on-direct-material-cost suits jobs '
          'where material cost dominates and overhead tends to move with material cost — also '
          'equitable where only one product type is made, so material cost per unit is uniform.'},
  ]},

  {'n': '7.3', 't': 'Batch costing', 'b': [
    {'def': {'t': 'Batch costing', 'd': 'arises where a customer orders a quantity of identical '
                  'products at once — the job is a number of units of a similar product, all '
                  'covered by a single job number (e.g. a print run of 1,000 copies of a book). '
                  'The batch cost is divided by the total quantity to give a cost per unit.'}},
    {'p': 'Peculiar features of a batch costing system:'},
    {'table': {'align': 'll', 'head': ['Feature', 'What it means'], 'rows': [
      ['**Set-up costs**', 'The cost of setting up production facilities — engineering time, '
       'factory consumables to set up moulds, etc.'],
      ['**Unit cost falls as batch size rises**', 'Because set-up and other fixed costs stay the '
       'same however large the batch is, spreading them over more units lowers the average unit '
       'cost.'],
      ['**Batches of dissimilar products**', 'Sometimes different products are batched together '
       'because a common operation saves set-up time — the shared cost of that joint operation '
       'must then be apportioned on an **equitable** basis.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 7.3 — batch cost and unit cost falling as '
      'batch size rises', 'open': True, 'q': [
      {'p': 'Ayingba Press is asked to quote for 5,000 and 25,000 booklets, on a 10%-of-sales '
            'profit target. Costs per 1,000 copies: paper/materials N30, wages N20, layout '
            '(set-up) N500 flat, fixed overhead N200 flat, variable overhead 12% of wages. '
            'Find the batch cost, unit cost and minimum selling price for each quantity.'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['', '1,000 copies (N)', '5,000 copies (N)',
        '25,000 copies (N)'], 'rows': [
        ['Set-up/layout cost (flat, per batch)', '500', '500', '500'],
        ['Paper (30 per 1,000)', '30', '150', '750'],
        ['Wages (20 per 1,000)', '20', '100', '500'],
        ['Fixed overhead (flat, per batch)', '200', '200', '200'],
        ['Variable overhead (12% of wages)', '2.40', '12', '60'],
        ['**Total batch cost**', '**752.40**', '**962**', '**2,010**'],
        ['Profit margin (10% of selling price)', '83.60', '107', '223'],
        ['**Selling price**', '**836**', '**1,069**', '**2,233**'],
      ]}},
      {'p': 'Since profit margin is 10% of the **selling price** (not of cost), selling price '
            '$= \\text{cost} / 0.9$ — e.g. at 5,000 copies, $962/0.9 \\approx N1{,}069$.'},
      {'tex': '\\text{Unit cost at 5,000 copies} = \\dfrac{962}{5{,}000} = 19.24 \\text{ kobo} '
              '\\quad\\quad \\text{Unit cost at 25,000 copies} = \\dfrac{2{,}010}{25{,}000} = '
              '8.04 \\text{ kobo}'},
      {'key': 'Notice **why** unit cost fell so much: set-up cost (N500) and fixed overhead '
              '(N200) are the **same flat N700** at every batch size — only paper, wages and '
              'variable overhead scale up with quantity. Spreading that fixed N700 over 25,000 '
              'copies instead of 1,000 is most of the unit-cost saving — exactly the general '
              'principle stated above, now seen numerically.'}]}},
  ]},

  {'n': '7.4', 't': 'Contract costing and accounting', 'b': [
    {'p': 'Contract costing is a form of order costing, distinguished by:'},
    {'ul': [
      'jobs of **long-term duration**, often spanning more than one accounting period;',
      'work carried out at the **contractee\'s own premises** (site-based);',
      '**sub-contractors** for specialist work (plumbing, electrical installation); and',
      'an **architect**, engaged by the contractee, who supervises the work and issues a '
      '**valuation certificate** ("work certified"/architect\'s valuation) that payment to the '
      'contractor is based on.',
    ]},
    {'key': 'Ascertaining cost is *not* the hard part of contract costing — a contract account '
            'is simply debited with every expense as it is incurred. The **real problem is '
            'profit**: how much profit (if any) can be recognised on a contract that has '
            'reached an advanced stage but is not yet complete? Taking too much profit too '
            'early risks recognising profit that never materialises if the contract later runs '
            'into trouble — this is a direct application of the **prudence concept**.'},
    {'p': 'Contracts are classified into three stages, each with its own profit-recognition rule:'},

    {'h4': '(a) Early-stage contracts'},
    {'p': 'Not nearing completion at all — expenses debited to the contract account are simply '
          'carried forward as the cost of work-in-progress, exactly as in job costing. **No '
          'profit is recognised yet.**'},

    {'h4': '(b) Fairly advanced-stage contracts'},
    {'p': 'A reliable estimate of cost-to-completion may not yet be available, but some profit '
          'can prudently be recognised on the work done so far.'},
    {'fbox': {'h': 'Profit recognition — fairly advanced stage', 'rows': [
      {'lb': 'Step 1: Notional profit', 'tex': '\\text{Notional profit} = \\text{Value of work '
        'certified} - \\text{Cost of work certified}'},
      {'lb': 'Step 2: Profit taken', 'tex': '\\text{Profit taken} = \\tfrac23 \\times '
        '\\text{Notional profit} \\times \\dfrac{\\text{Cash received}}{\\text{Value of work '
        'certified}}'},
    ]}},
    {'note': '**Cost of work certified is not the same as cost to date** — some cost may have '
             'been incurred on work the architect has not yet certified, so it must be excluded '
             'from the notional-profit calculation. The $\\tfrac23$ fraction in Step 2 is the '
             'study text\'s own stated proportion — in practice (and in an exam), the '
             'proportion to use is whatever the question or examiner specifies, not a fixed '
             'universal rule.'},

    {'h4': '(c) Nearing-completion contracts'},
    {'p': 'A reliable estimate of total cost is now available, so profit is taken with reference '
          'to the contract\'s **total estimated profit over its whole life**, adjusted for any '
          'profit already recognised in earlier periods.'},
    {'fbox': {'h': 'Profit recognition — nearing completion', 'rows': [
      {'lb': 'Step 1: Estimated Total Profit (ETP)', 'tex': '\\text{ETP} = \\text{Total contract '
        'price} - (\\text{Cost to date} + \\text{Cost to complete})'},
      {'lb': 'Step 2: Profit realised to date (lower of two estimates)',
       'tex': '\\min\\!\\left(\\dfrac{\\text{Value of work certified}}{\\text{Estimated total '
              'cost}} \\times \\text{ETP},\\ \\ \\dfrac{\\text{Cost to date}}{\\text{Estimated '
              'total cost}} \\times \\text{ETP}\\right)'},
      {'lb': 'Step 3: Profit taken this period', 'tex': '\\text{Profit realised to date} - '
        '\\text{Profit already recognised in prior periods}'},
    ]}},
    {'warn': 'Where the contract as a whole is **expected to result in a loss**, that entire '
             'foreseeable loss must be written off **immediately**, to the maximum extent '
             'possible — not spread or deferred. This follows directly from the prudence '
             'principle: an unprofitable contract should not have been accepted in the first '
             'place, and the loss must be recognised as soon as it is foreseeable, not only when '
             'the contract finally finishes.'},

    {'h4': 'Valuing a contract in the balance sheet'},
    {'fbox': {'h': 'Contract value receivable', 'rows': [
      {'lb': 'Contract value for balance sheet', 'tex': '(\\text{Total cost incurred to date} + '
        '\\text{Profit taken/realised}) - \\text{Cash received from contractee}'},
    ]}},
    {'p': 'This is simply the value of the asset the contract has created so far, less what has '
          'already been paid for it — the amount the contractor still stands to be paid.'},
  ]},

  {'n': '7.5', 't': 'Service (operation) costing', 'b': [
    {'def': {'t': 'Service costing (operation costing)', 'd': 'a method of cost ascertainment '
                  'for organisations that provide services rather than physical products — e.g. '
                  'transport companies, electricity companies, hotels, hospitals, schools, '
                  'cinemas.'}},
    {'p': 'Characteristics of service costing:'},
    {'ul': [
      'services are **standardised** — a similar service is provided to every customer;',
      'services are provided on an **uninterrupted, regular** basis;',
      'a large amount of capital is tied up in fixed assets (transport vehicles, hotel '
      'buildings, hospital equipment); and',
      'operating cost is part fixed, part variable.',
    ]},
    {'p': 'A transport company\'s operation cost sheet is a representative format:'},
    {'table': {'align': 'llr', 'head': ['', 'Item', ''], 'rows': [
      ['**Fixed costs (standing charges)**', 'Motor park dues; vehicle licensing and insurance; '
       'manager\'s salary; administrative charges; finance charges; drivers\' salaries.',
       'Total ÷ km = cost/km'],
      ['**Variable (running) costs**', 'Depreciation; fuel and oil; spare parts, service and '
       'repairs.', 'Total ÷ km = cost/km'],
    ]}},
    {'p': 'Fixed and variable totals are aggregated to find **cost per vehicle per kilometre**.'},
    {'note': 'The study text\'s current edition adds a substantial discussion of **digital-'
             'economy pricing models** at this point — dynamic pricing (Amazon, Uber surge), '
             'the freemium model (Spotify, LinkedIn), subscription pricing (Netflix, Microsoft '
             '365, Amazon Prime — flat-rate/tiered/usage-based/freemium/per-user/hybrid), price '
             'discrimination, product bundling and psychological pricing, penetration vs '
             'premium pricing by market structure, and the ethical concerns these raise (price '
             'gouging, data-driven personalisation). This material is genuinely present in the '
             'source but is **not** referenced anywhere in this chapter\'s own stated objectives '
             'or its end-of-chapter question bank — it reads as supplementary background on how '
             'costing/pricing concepts show up in a digital business context, not core '
             'examinable technique. Included here for completeness (full fidelity to the '
             'source), condensed accordingly.'},
  ]},

  {'n': '7.6', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§7.1 Order costing** — links expense to a specific, identifiable job/batch/contract; '
      'purpose is to find profit/loss per order and support cost-plus pricing.',
      '**§7.2 Job costing** — every job gets an order number; the Job Card (shop floor) is '
      'supplementary to the cost ledger; overhead absorbed by %-of-wages, %-of-material, '
      '%-of-prime-cost, cost-unit rate or time rate — the *same* job priced two different ways '
      'gives two different costs (Illustrations 7.1/7.2), so choosing the right basis matters.',
      '**§7.3 Batch costing** — one job number for many identical units; set-up costs and other '
      'flat batch costs, spread over more units, drive unit cost down as batch size rises.',
      '**§7.4 Contract costing** — long-term, site-based, may involve sub-contractors and an '
      'architect\'s valuation certificate; the real difficulty is profit recognition, not cost '
      'ascertainment; 3 stages (early: no profit taken; fairly advanced: notional profit × '
      '2/3 × cash-received ratio; nearing completion: ETP-based, lower-of-two-ratios profit '
      'realised, less prior recognition); a foreseeable loss is written off immediately and in '
      'full.',
      '**§7.5 Service costing** — standardised, continuous services with heavy fixed-asset '
      'investment; operation cost sheet splits fixed (standing) and variable (running) costs to '
      'find cost per unit of service (e.g. per km).',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Order costing** — costing a specific, identifiable job/batch/contract. **Job Card** — '
      'shop-floor record, supplementary to the cost ledger.',
      '**Set-up cost** — the flat cost of preparing production facilities for a batch/job.',
      '**Notional profit** — value of work certified less cost of work certified (fairly-'
      'advanced-stage contracts). **Estimated Total Profit (ETP)** — total contract price less '
      'estimated total cost (nearing-completion contracts).',
      '**Work certified** — the architect\'s valuation of work done so far, the basis for '
      'contractor payment.',
      '**Retention money** — a small percentage of the contract sum withheld by the contractee '
      'for a period after completion, as insurance against later-discovered faults.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'Job/batch/contract costing formulas (recap)', 'rows': [
      {'lb': 'Overhead rate, % of direct wages', 'tex': '\\dfrac{\\text{Total overhead}}'
        '{\\text{Total direct wages}} \\times 100'},
      {'lb': 'Overhead rate, % of direct material', 'tex': '\\dfrac{\\text{Total overhead}}'
        '{\\text{Total direct material cost}} \\times 100'},
      {'lb': 'Notional profit', 'tex': '\\text{Value of work certified} - \\text{Cost of work '
        'certified}'},
      {'lb': 'Profit taken, fairly advanced stage', 'tex': '\\tfrac23 \\times \\text{Notional '
        'profit} \\times \\dfrac{\\text{Cash received}}{\\text{Value of work certified}}'},
      {'lb': 'Estimated Total Profit (ETP)', 'tex': '\\text{Total contract price} - '
        '\\text{Estimated total cost}'},
    ]}},
  ]},

  {'n': '7.7', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Distinguish between a Job Card and a Job Cost Card. (A) Job card is kept for employees '
        'whilst Job Cost Card is kept for assets  (B) Job card is kept on the shop floor whilst '
        'Job Cost Card is in the cost office  (C) Job card is for engineering jobs whilst Job '
        'Cost Card is for financial jobs  (D) Job card is for jobs whilst Job Cost Card is for '
        'batches  (E) Job card is given to the customer whilst Job Cost Card is kept by the '
        'company',
        'What are set-up costs? (A) Cost of buying equipment sets  (B) Cost of constructing the '
        'factory  (C) Cost of setting up production facilities for a particular job or '
        'production  (D) Cost of laying ambush for dishonest employees  (E) Cost of assembling '
        'factory operatives in readiness for production',
        'What is mark-up? (A) A percentage of total costs added as profit to determine the '
        'selling price  (B) The distinctive mark on packages to avoid mix-up  (C) The total '
        'selling price of an order  (D) The total cost of executing a job  (E) The amount of '
        'bonus given to those who worked on an order',
        'What is Notional profit on contracts? (A) The total profit of the contractor for the '
        'years  (B) The amount of profit to be paid to the nation\'s coffers  (C) The profit on '
        'the mobilisation fee received on a contract  (D) The amount of profit brought forward '
        'from previous years  (E) The portion of profit to be recognised on an on-going '
        'contract at year end',
        '"Value of work certified" in a contract means (A) Value of materials used in the '
        'contract  (B) Total cost of executing a contract  (C) Total progress payments received '
        'on a contract  (D) The aggregate total value of architect\'s certificates issued so '
        'far  (E) Total value of items sub-contracted on the main contract',
        'How is a job identified among other jobs being carried out simultaneously in the '
        'accounts?',
        'What document gives the value of contract work completed on a progressive basis?',
        'Large jobs, usually of long-term duration extending beyond the company\'s financial '
        'year-end and carried out on the customer\'s premises, are known as ………...',
        'Where a company recognises total provisional profit on a contract almost fully '
        'completed at its year end, what is the name given to the amount added to cost-to-date '
        'to arrive at estimated total cost?',
        'An amount, usually a small percentage of the total contract sum, withheld by the '
        'contractee for almost a year after contract completion as insurance against faults '
        'discovered later, is known as…………..',
      ]}],
      'a': [
      {'ol': [
        '**B** — Job Card is kept on the shop floor; Job Cost Card is kept in the cost office.',
        '**C — cost of setting up production facilities for a particular job or production.**',
        '**A — a percentage of total costs added as profit, to determine the selling price.**',
        '**E — the portion of profit recognised on an on-going contract at year end.**',
        '**D — the aggregate total value of architect\'s certificates issued so far.**',
        '**By its unique Job (Order) Number.**',
        '**The architect\'s certificate.**',
        '**Contracts.**',
        '**Cost to completion (cost to complete).**',
        '**Retention money (retention fee).**',
      ]}]}},
  ]},

  {'n': '7.8', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with eleven examination-type questions — four '
          'discursive, five computational job-costing questions, one article, and one service '
          'costing question. All are reproduced below with full answers. (The book leaves the '
          'last two unnumbered; they are shown here as Q10 and Q11.)'},

    {'eg': {'tag': 'Exam type — Q1', 't': 'Discuss the concept of job order costing',
      'q': [{'p': 'Discuss the concept of Job Order Costing as clearly as possible.'}],
      'a': [
      {'h4': 'What it is'},
      {'p': '**Job order costing** is the method of costing used where production consists of '
            'separately identifiable **jobs**, each carried out to a customer\'s own '
            'specification. Each job is distinct, so costs are collected and ascertained **job '
            'by job** rather than averaged over a period\'s output. It is one of the two '
            'branches of **specific order costing**, the other being contract costing (and '
            'batch costing a variant of it).'},
      {'h4': 'Where it is used'},
      {'ul': [
        'jobbing engineering and machine shops;', 'printing works;',
        'motor-vehicle and plant repair garages;', 'furniture making to order;',
        'shipbuilding repairs, construction of individual items of plant;',
        'professional firms costing an individual client assignment.',
      ]},
      {'h4': 'The essential features'},
      {'ol': [
        'Each job is given a **unique job (order) number**, which is the key under which all its '
        'costs are collected.',
        'A **job cost card** (job cost sheet) is opened for every job in the cost office; all '
        'direct materials, direct wages, direct expenses and absorbed overhead are posted to it '
        'as they are incurred.',
        'Costs are traced from source documents that each quote the job number — **materials '
        'requisitions** for materials, **job cards / time sheets** for labour, and invoices for '
        'direct expenses.',
        'Overhead is **absorbed** into each job using a predetermined rate — per labour hour, '
        'machine hour, or percentage of wages or materials (Chapter 5).',
        'Jobs are usually of **short duration** and carried out **on the company\'s own '
        'premises** — which is what distinguishes a job from a contract.',
        'Work-in-progress at any date is simply the total of the cost cards of jobs not yet '
        'finished.',
        'On completion the job cost card is totalled, and profit is recognised on the '
        'individual job when it is delivered and invoiced.',
      ]},
      {'h4': 'The procedure, from enquiry to invoice'},
      {'steps': [
        'The customer makes an enquiry; the works estimates the materials, labour and expenses '
        'the job will need.',
        'Overhead is added at the predetermined rate, and a profit mark-up applied, to produce '
        'the **quotation** sent to the customer.',
        'On acceptance, a **production order** is raised and a job number allocated; a job cost '
        'card is opened.',
        'Materials are requisitioned and labour booked, each document quoting the job number.',
        'As work proceeds, the cost card is posted with actual materials, wages, direct expenses '
        'and absorbed overhead.',
        'On completion, the card is totalled to give the actual job cost; the job is invoiced, '
        'and actual cost is compared with the original estimate so that the estimating basis can '
        'be improved.',
      ]},
      {'h4': 'Advantages and limitations'},
      {'table': {'align': 'll', 'head': ['Advantages', 'Limitations'], 'rows': [
        ['The **actual cost and profit of each individual job** are known, so loss-making work '
         'can be identified and future quotations improved.',
         'It is **clerically expensive** — every requisition and time booking must carry a job '
         'number, and a card must be kept for each job.'],
        ['It provides a sound basis for **quoting and pricing** similar future work.',
         'It depends entirely on **accurate recording** at source; a mis-booked hour or '
         'requisition costs the wrong job.'],
        ['Actual costs can be **compared with the estimate**, revealing inefficiency and '
         'estimating error.',
         'The job cost includes **absorbed** overhead, so it is only as reliable as the '
         'absorption rate chosen (Chapter 5).'],
        ['Work-in-progress is valued simply and accurately from the open cost cards.',
         'Because each job is unique, there is little scope for **standard costing** or routine '
         'variance analysis.'],
      ]}}]}},

    {'eg': {'tag': 'Exam type — Q2', 't': 'Two methods of absorbing overhead costs by jobs',
      'q': [{'p': 'Briefly explain any **two** methods of absorbing overhead costs by jobs.'}],
      'a': [
      {'h4': 'Method 1 — the direct labour hour rate'},
      {'tex': '\\text{Rate} = \\frac{\\text{Budgeted overhead of the cost centre}}'
              '{\\text{Budgeted direct labour hours}}'},
      {'p': 'Each job is charged with the hours its workers spent in the department, multiplied '
            'by that department\'s rate. It is the most appropriate method in a **labour-'
            'intensive** department, where overhead is incurred broadly in proportion to the '
            'time people spend working. Its advantage over a wages-percentage basis is that it '
            'is unaffected by differences in wage rates — two workers of different grades '
            'spending the same time on the same job absorb the same overhead, which is correct, '
            'because they consume the same amount of supervision, space, heat and light.'},
      {'h4': 'Method 2 — the machine hour rate'},
      {'tex': '\\text{Rate} = \\frac{\\text{Budgeted overhead of the cost centre}}'
              '{\\text{Budgeted machine hours}}'},
      {'p': 'Each job is charged with the machine hours it used in the department. It is the '
            'appropriate method in a **machine-intensive** department, where most of the '
            'overhead — depreciation, power, maintenance, machine insurance and the space the '
            'machine occupies — is caused by running the machine rather than by employing a '
            'person. A job that ties up an expensive machine for eight hours while one operator '
            'watches it should carry more overhead than a job occupying the same operator at a '
            'bench, and only a machine hour rate achieves that.'},
      {'note': 'Two further methods, for completeness: the **percentage of direct wages** '
               '(overhead ÷ direct wages × 100), simple and usable where hours are not recorded; '
               'and the **cost unit rate** (overhead ÷ units produced), appropriate only where a '
               'single homogeneous product is made.'}]}},

    {'eg': {'tag': 'Exam type — Q3', 't': 'Short notes on four topics',
      'q': [{'p': 'Write short notes on each of the following: (i) overhead absorption; '
                  '(ii) cost plus basis of pricing; (iii) transport service costing; '
                  '(iv) batch costing.'}],
      'a': [
      {'h4': '(i)  Overhead absorption'},
      {'p': 'Overhead absorption (also called overhead recovery) is the process of charging the '
            'overhead accumulated in a production cost centre **out to the cost units** that '
            'pass through it. It is the final step after allocation, apportionment and '
            'reapportionment. A **predetermined** absorption rate is computed before the period '
            'begins — budgeted overhead ÷ budgeted activity — and applied to the actual activity '
            'of each job. Because both the overhead and the activity are estimates, the amount '
            'absorbed rarely equals the amount incurred, and the difference is the **under- or '
            'over-absorbed overhead**, written off to the costing profit and loss account. '
            'Common bases are the direct labour hour, the machine hour, a percentage of direct '
            'wages, a percentage of direct materials, a percentage of prime cost, and the cost '
            'unit.'},
      {'h4': '(ii)  Cost plus basis of pricing'},
      {'p': 'Cost plus pricing sets the selling price by calculating the cost of the job and '
            'adding a predetermined margin:'},
      {'tex': '\\text{Selling price} = \\text{Cost} + (\\text{Cost} \\times '
              '\\text{mark-up }\\%)'},
      {'p': 'The "cost" may be total cost, production cost or marginal cost, and the percentage '
            'added differs accordingly. It is used where no market price exists for comparison — '
            'one-off jobs, custom contracts, government contracts, and work for which the '
            'customer agrees to reimburse cost plus a fee. **Advantages:** simple; guarantees '
            'that cost is recovered; useful where the final cost cannot be predicted at the time '
            'of quoting. **Disadvantages:** it ignores demand and what competitors charge; it '
            'passes inefficiency straight on to the customer, so it gives the supplier no '
            'incentive to control cost; and the answer depends on arbitrary overhead '
            'apportionment, so the "cost" it starts from is not a single objective figure.'},
      {'warn': 'Always read whether the margin is a percentage **of cost** (a mark-up) or a '
               'percentage **of selling price** (a margin). A 25% mark-up on a cost of N100 '
               'gives a price of N125; a 25% margin on selling price gives '
               '$100 \\div 0.75 = N133.33$.'},
      {'h4': '(iii)  Transport service costing'},
      {'p': 'Transport service costing is the application of **service (operation) costing** to '
            'a transport undertaking — a bus fleet, a haulage business, or a company\'s own '
            'delivery vehicles. Its distinguishing feature is the use of a **composite cost '
            'unit** that captures both distance and load:'},
      {'ul': [
        '**passenger-kilometre** for passenger transport;',
        '**tonne-kilometre** for goods transport.',
      ]},
      {'p': 'Costs are classified into **standing (fixed) charges** — licences, insurance, road '
            'tax, depreciation on a time basis, drivers\' wages, garage rent, interest — and '
            '**running (variable) charges** — fuel and oil, tyres, repairs and maintenance, and '
            'depreciation on a mileage basis. The cost per composite unit is the total of both, '
            'divided by the total passenger- or tonne-kilometres operated. It is used to set '
            'fares and freight rates, to compare the cost of different vehicles or routes, and '
            'to decide whether to own or hire transport. Question 11 below is a full worked '
            'example.'},
      {'h4': '(iv)  Batch costing'},
      {'p': '**Batch costing** is the form of specific order costing in which a **batch** — a '
            'group of identical units made together as one order — is treated as the cost unit. '
            'Costs are collected for the whole batch exactly as for a job, and the cost per unit '
            'is then found by dividing:'},
      {'tex': '\\text{Cost per unit} = \\frac{\\text{Total cost of the batch}}'
              '{\\text{Number of good units in the batch}}'},
      {'p': 'It is used where identical items are produced in groups rather than singly — '
            'printing, pharmaceuticals, bakeries, clothing, components for assembly, and the '
            'manufacture of spare parts. Its characteristic feature is the **set-up cost**, '
            'which is incurred once per batch whatever the batch size, so the cost **per unit** '
            'falls as the batch grows — the effect worked through numerically in Illustration '
            '7.3 above. Batch costing therefore raises the question of the **economic batch '
            'quantity**, which balances set-up cost against the cost of holding the resulting '
            'inventory, in exactly the way the EOQ balances ordering against carrying cost '
            '(Chapter 3).'}]}},

    {'eg': {'tag': 'Exam type — Q4',
      't': 'Mr Hankaka — costing a job on three different overhead bases',
      'q': [
      {'p': 'Mr Hankaka, a shoe manufacturer, found that his production costs for an accounting '
            'period had been as follows:'},
      {'stmt': {'t': 'Production costs for the period', 'rows': [
        ['Direct wages', '', 800000],
        ['Direct materials', '', 300000],
        ['Direct expenses', '', 100000],
        ['**Prime cost**', '', 1200000, '@t'],
        ['Production overhead', '', 240000],
        ['**Factory cost**', '', 1440000, '@tt'],
        '@gap',
        ['Total shoes manufactured', '', '160,000 units'],
        ['Total machine hours used', '', '10,000 hours'],
        ['Total direct labour hours used', '', '40,000 hours'],
      ]}},
      {'p': 'A job performed had a direct wages cost of **N800**, direct material cost of '
            '**N500** and direct expenses of **N150**.'},
      {'p': '**Required:** **(a)** find the total cost of the job using (i) the direct wages '
            'percentage rate and (ii) the direct material percentage rate. **(b)** If the job '
            'was that of producing **120 units** of shoes, what would be the total cost?'}],
      'a': [
      {'h4': 'Step 1 — the absorption rates'},
      {'stmt': {'t': 'Overhead absorption rates', 'rows': [
        ['Direct wages percentage rate:  N240,000 ÷ N800,000', '', '**30% of direct wages**'],
        ['Direct material percentage rate:  N240,000 ÷ N300,000', '',
         '**80% of direct materials**'],
        ['Cost unit rate:  N240,000 ÷ 160,000 units', '', '**N1.50 per unit**'],
      ]}},
      {'h4': '(a)  Total cost of the job'},
      {'stmt': {'t': 'Job cost under the two bases (N)', 'rows': [
        ['', '(i) Direct wages %', '(ii) Direct material %', '@hd'],
        ['Direct materials', 500, 500],
        ['Direct wages', 800, 800],
        ['Direct expenses', 150, 150],
        ['**Prime cost**', 1450, 1450, '@t'],
        ['Production overhead  (30% × 800;  80% × 500)', 240, 400],
        ['**Total cost of the job**', 1690, 1850, '@tt'],
      ]}},
      {'note': 'The same job, the same work, two answers **N160 apart** — a 9.5% difference on '
               'an identical job. Which is right depends on whether this factory\'s overhead is '
               'actually driven by labour or by materials. For a shoe factory, neither is '
               'convincing: a labour hour or machine hour rate would be better, which is why the '
               'question goes on to part (b).'},
      {'h4': '(b)  If the job produced 120 units of shoes'},
      {'p': 'Where the output is a **single homogeneous product** — as here, shoes — the **cost '
            'unit rate** is both the simplest and the most accurate basis, because every unit '
            'genuinely consumes the same overhead:'},
      {'stmt': {'t': 'Job cost using the cost unit rate (N)', 'rows': [
        ['Direct materials', '', 500],
        ['Direct wages', '', 800],
        ['Direct expenses', '', 150],
        ['**Prime cost**', '', 1450, '@t'],
        ['Production overhead:  120 units × N1.50', '', 180],
        ['**Total cost of the job**', '', 1630, '@tt'],
      ]}},
      {'tex': '\\text{Cost per pair of shoes} = \\frac{1{,}630}{120} = N13.58'},
      {'note': 'A second reading of part (b) is possible — simply applying the **average factory '
               'cost per shoe** of $N1{,}440{,}000 \\div 160{,}000 = N9.00$ to give '
               '$120 \\times N9 = N1{,}080$. That is a valid answer to "what should 120 shoes '
               'cost on average", but it ignores the job\'s own actual direct costs, which the '
               'question supplies. The answer above uses the actual direct costs and absorbs '
               'overhead per unit, which is the more defensible treatment; state whichever '
               'reading you adopt.'}]}},

    {'eg': {'tag': 'Exam type — Q5',
      't': 'Hantsi Limited — Job 707 costed on three overhead bases, with a 45% profit target',
      'q': [
      {'p': 'Hantsi Limited operates a factory consisting of two departments: **Assembly** and '
            '**Galvanizing**. All products pass through both departments. The following '
            'information was given:'},
      {'stmt': {'t': 'Departmental data', 'rows': [
        ['', 'Assembly', 'Galvanizing', '@hd'],
        ['Materials', 'N40,000', 'N12,000'],
        ['Direct wages', 'N20,000', 'N36,000'],
        ['Production overhead', 'N16,000', 'N24,000'],
        ['Direct labour hours', 38000, 24000],
        ['Machine hours', 66000, 38000],
      ]}},
      {'p': 'One of the jobs completed in the factory was **No. 707**:'},
      {'stmt': {'t': 'Job No. 707', 'rows': [
        ['', 'Assembly', 'Galvanizing', '@hd'],
        ['Materials', 'N400', 'N80'],
        ['Direct wages', 'N300', 'N150'],
        ['Direct labour hours', 800, 300],
        ['Machine hours', 700, 800],
      ]}},
      {'p': '**Required:** **(a)** use **three** different methods by which production overhead '
            'could be recovered, and prepare the job cost card for Job No. 707, using **50% of '
            'production overhead** to recover administrative overhead and **25% of production '
            'overhead** to recover selling and distribution overhead. **(b)** Show the total '
            'proceeds on the job if the target profit is **45% of total cost**.'}],
      'a': [
      {'h4': 'Step 1 — three sets of departmental overhead absorption rates'},
      {'stmt': {'t': 'Absorption rates by method', 'rows': [
        ['Method', 'Assembly', 'Galvanizing', '@hd'],
        ['**1. Direct material percentage**  (16,000÷40,000;  24,000÷12,000)', '40%', '200%'],
        ['**2. Direct wages percentage**  (16,000÷20,000;  24,000÷36,000)', '80%', '66⅔%'],
        ['**3. Direct labour hour rate**  (16,000÷38,000;  24,000÷24,000)', 'N0.4211',
         'N1.0000'],
        ['*(4. Machine hour rate, for comparison: 16,000÷66,000; 24,000÷38,000)*', '*N0.2424*',
         '*N0.6316*'],
      ]}},
      {'h4': 'Step 2 — production overhead absorbed by Job 707 under each method'},
      {'stmt': {'t': 'Production overhead absorbed (N)', 'rows': [
        ['Method', 'Assembly', 'Galvanizing', 'Total', '@hd'],
        ['1. Direct material %  (40% × 400;  200% × 80)', 160.00, 160.00, 320.00],
        ['2. Direct wages %  (80% × 300;  66⅔% × 150)', 240.00, 100.00, 340.00],
        ['3. Direct labour hour  (800 × 0.4211;  300 × 1.00)', 336.84, 300.00, 636.84],
      ]}},
      {'h4': '(a)  Job cost card — Job No. 707'},
      {'stmt': {'t': 'Job Cost Card — Job No. 707 (N)', 'rows': [
        ['', 'Method 1', 'Method 2', 'Method 3', '@hd'],
        ['Direct materials  (400 + 80)', 480.00, 480.00, 480.00],
        ['Direct wages  (300 + 150)', 450.00, 450.00, 450.00],
        ['**Prime cost**', 930.00, 930.00, 930.00, '@t'],
        ['Production overhead absorbed', 320.00, 340.00, 636.84],
        ['**Production cost**', 1250.00, 1270.00, 1566.84, '@t'],
        ['Administrative overhead — 50% of production overhead', 160.00, 170.00, 318.42],
        ['Selling and distribution overhead — 25% of production overhead', 80.00, 85.00, 159.21],
        ['**Total cost of Job No. 707**', 1490.00, 1525.00, 2044.47, '@tt'],
      ]}},
      {'h4': '(b)  Total proceeds at a target profit of 45% of total cost'},
      {'stmt': {'t': 'Selling price of Job No. 707 (N)', 'rows': [
        ['', 'Method 1', 'Method 2', 'Method 3', '@hd'],
        ['Total cost', 1490.00, 1525.00, 2044.47],
        ['Add: profit at 45% of total cost', 670.50, 686.25, 920.01],
        ['**Total proceeds on the job**', 2160.50, 2211.25, 2964.48, '@tt'],
      ]}},
      {'key': 'The spread is dramatic: the same job is priced anywhere between N2,160 and N2,964 '
              'depending purely on which overhead base is chosen — a **37% difference**. Method '
              '3 produces much the highest figure because Job 707 is **labour-hour hungry** '
              '(1,100 hours) relative to its small material and wage values, so an hours basis '
              'loads far more overhead onto it than a value basis does. Nothing about the job '
              'changed. This is the clearest possible demonstration that a "job cost" is never a '
              'single objective number — it is a number produced by a chosen convention, and the '
              'convention should be chosen to reflect what actually causes the overhead.'},
      {'note': 'Note the 45% is a mark-up **on cost**, not a margin on selling price, so it is '
               'applied by multiplying the cost by 1.45. The profit as a percentage of the '
               'selling price is $45 \\div 145 = 31.03\\%$.'}]}},

    {'eg': {'tag': 'Exam type — Q6 (BUK, 1993)',
      't': 'Shahada Ltd — Job 807 on a material-percentage and a labour-hour basis',
      'q': [
      {'p': 'Shahada Ltd operates a factory consisting of two departments: **Washing** and '
            '**Cleaning**. All activities pass through both departments:'},
      {'stmt': {'t': 'Departmental data', 'rows': [
        ['', 'Washing', 'Cleaning', '@hd'],
        ['Materials', 'N60,000', 'N25,000'],
        ['Direct wages', 'N30,000', 'N40,000'],
        ['Production overhead', 'N20,000', 'N32,000'],
        ['Direct labour hours', 40000, 25000],
        ['Machine hours', 50000, 43000],
      ]}},
      {'p': 'One of the jobs completed was **Job No. 807**:'},
      {'stmt': {'t': 'Job No. 807', 'rows': [
        ['', 'Washing', 'Cleaning', '@hd'],
        ['Materials', 'N500', 'N120'],
        ['Direct wages', 'N450', 'N200'],
        ['Direct labour hours', 900, 450],
        ['Machine hours', 200, 150],
      ]}},
      {'p': '**Required:** prepare the job cost card for Job No. 807 using (i) the direct '
            'material percentage rate and (ii) the direct labour hour rate of recovering '
            'production overhead. Use **30%** of the production overhead of the job to recover '
            'administrative overhead and **35%** to recover selling and distribution overhead.'}],
      'a': [
      {'h4': 'Step 1 — the absorption rates'},
      {'stmt': {'t': 'Absorption rates', 'rows': [
        ['Method', 'Washing', 'Cleaning', '@hd'],
        ['**(i) Direct material percentage**  (20,000÷60,000;  32,000÷25,000)', '33⅓%', '128%'],
        ['**(ii) Direct labour hour rate**  (20,000÷40,000;  32,000÷25,000)', 'N0.50', 'N1.28'],
      ]}},
      {'h4': 'Step 2 — production overhead absorbed by Job 807'},
      {'stmt': {'t': 'Production overhead absorbed (N)', 'rows': [
        ['Method', 'Washing', 'Cleaning', 'Total', '@hd'],
        ['(i) Direct material %  (33⅓% × 500;  128% × 120)', 166.67, 153.60, 320.27],
        ['(ii) Direct labour hour  (900 × 0.50;  450 × 1.28)', 450.00, 576.00, 1026.00],
      ]}},
      {'h4': 'Job Cost Card — Job No. 807'},
      {'stmt': {'t': 'Job Cost Card — Job No. 807 (N)', 'rows': [
        ['', '(i) Material %', '(ii) Labour hour', '@hd'],
        ['Direct materials  (500 + 120)', 620.00, 620.00],
        ['Direct wages  (450 + 200)', 650.00, 650.00],
        ['**Prime cost**', 1270.00, 1270.00, '@t'],
        ['Production overhead absorbed', 320.27, 1026.00],
        ['**Production cost**', 1590.27, 2296.00, '@t'],
        ['Administrative overhead — 30% of production overhead', 96.08, 307.80],
        ['Selling and distribution overhead — 35% of production overhead', 112.09, 359.10],
        ['**Total cost of Job No. 807**', 1798.44, 2962.90, '@tt'],
      ]}},
      {'key': 'Job 807 uses **1,350 direct labour hours** but only **N620** of materials, so it '
              'is an extremely labour-intensive job. A material-percentage basis therefore '
              'charges it almost nothing for overhead (N320) while a labour-hour basis charges '
              'it over three times as much (N1,026) — and the total cost differs by N1,164, or '
              '65%. Quoting this job on a material-percentage basis would almost certainly lose '
              'money. The lesson is the same as in Q5: **match the absorption base to what '
              'actually consumes the overhead.**'}]}},

    {'eg': {'tag': 'Exam type — Q7 (HUK Poly, 1997)',
      't': 'Ray Soap Manufacturing — Job S.10 on four overhead bases',
      'q': [
      {'p': 'The following figures have been extracted from the books of Ray Soap Manufacturing '
            'Company. All jobs pass through the company\'s two departments:'},
      {'stmt': {'t': 'Departmental data', 'rows': [
        ['', 'Working Department', 'Finishing Department', '@hd'],
        ['Materials used', 'N6,000', 'N500'],
        ['Direct labour cost', 'N3,000', 'N1,500'],
        ['Factory overheads', 'N1,800', 'N1,200'],
        ['Direct labour hours', 12000, 5000],
        ['Machine hours', 10000, 2000],
      ]}},
      {'p': 'The following information relates to **Job S.10**:'},
      {'stmt': {'t': 'Job S.10', 'rows': [
        ['', 'Working Department', 'Finishing Department', '@hd'],
        ['Materials used', 'N20', 'N10'],
        ['Direct labour', 'N65', 'N25'],
        ['Direct labour hours', 265, 70],
        ['Machine hours', 255, 25],
      ]}},
      {'p': '**Required:** **(a)** use **four** methods of absorbing factory overhead to show '
            'the overhead absorbed in each department; **(b)** prepare statements showing the '
            'different cost results for Job S.10 under any **two** of those methods.'}],
      'a': [
      {'h4': '(a)  Four methods of absorbing factory overhead'},
      {'stmt': {'t': 'Absorption rates', 'rows': [
        ['Method', 'Working Dept.', 'Finishing Dept.', '@hd'],
        ['**1. Direct material percentage**  (1,800÷6,000;  1,200÷500)', '30%', '240%'],
        ['**2. Direct labour cost percentage**  (1,800÷3,000;  1,200÷1,500)', '60%', '80%'],
        ['**3. Direct labour hour rate**  (1,800÷12,000;  1,200÷5,000)', 'N0.15', 'N0.24'],
        ['**4. Machine hour rate**  (1,800÷10,000;  1,200÷2,000)', 'N0.18', 'N0.60'],
      ]}},
      {'stmt': {'t': 'Overhead absorbed by Job S.10 (N)', 'rows': [
        ['Method', 'Working Dept.', 'Finishing Dept.', 'Total', '@hd'],
        ['1. Direct material %  (30% × 20;  240% × 10)', 6.00, 24.00, 30.00],
        ['2. Direct labour cost %  (60% × 65;  80% × 25)', 39.00, 20.00, 59.00],
        ['3. Direct labour hour  (265 × 0.15;  70 × 0.24)', 39.75, 16.80, 56.55],
        ['4. Machine hour  (255 × 0.18;  25 × 0.60)', 45.90, 15.00, 60.90],
      ]}},
      {'note': 'A fifth method, the **percentage of prime cost**, would give Working '
               '$1{,}800 \\div (6{,}000+3{,}000) = 20\\%$ and Finishing '
               '$1{,}200 \\div (500+1{,}500) = 60\\%$, absorbing '
               '$20\\% \\times 85 + 60\\% \\times 35 = N38.00$ on Job S.10.'},
      {'h4': '(b)  Cost statements for Job S.10 under two methods'},
      {'stmt': {'t': 'Job S.10 — cost statement (N)', 'rows': [
        ['', 'Direct labour hour basis', 'Machine hour basis', '@hd'],
        ['Direct materials  (20 + 10)', 30.00, 30.00],
        ['Direct labour  (65 + 25)', 90.00, 90.00],
        ['**Prime cost**', 120.00, 120.00, '@t'],
        ['Factory overhead absorbed — Working Department', 39.75, 45.90],
        ['Factory overhead absorbed — Finishing Department', 16.80, 15.00],
        ['**Total factory overhead**', 56.55, 60.90, '@t'],
        ['**Factory cost of Job S.10**', 176.55, 180.90, '@tt'],
      ]}},
      {'key': 'Unlike Q5 and Q6, the four bases here give answers that are reasonably close '
              '(N30 to N60.90 of overhead), because Job S.10 is not lopsided — it consumes '
              'materials, labour and machine time in roughly the proportions the departments do '
              'as a whole. The **direct material percentage** is the outlier at N30, and it is '
              'the least defensible basis: there is no reason why the value of soap ingredients '
              'should govern how much factory overhead a job consumes.'}]}},

    {'eg': {'tag': 'Exam type — Q8', 't': 'Procedures involved in normal service costing',
      'q': [{'p': 'Discuss the procedures involved in normal service costing.'}],
      'a': [
      {'def': {'t': 'Service (operation) costing', 'd': 'the method of costing applied where '
                    'standardised **services** are provided, either to outside customers or by '
                    'one department of an organisation to another, rather than tangible goods '
                    'being produced.'}},
      {'h4': 'The procedures'},
      {'steps': [
        '**Identify the service and the cost centre** providing it — a bus route, a hospital '
        'ward, a canteen, a power house, a hotel, a maintenance department.',
        '**Select an appropriate cost unit.** This is the crucial step, and the unit is usually '
        '**composite**, combining two variables, because a single variable does not describe the '
        'service adequately — passenger-kilometre, tonne-kilometre, patient-day, kilowatt-hour, '
        'bed-night, meal served, student-year.',
        '**Classify the costs** into **standing (fixed) charges** — those incurred whether or '
        'not the service operates: licences, insurance, road tax, rent, supervisory salaries, '
        'time-based depreciation, interest — and **running (variable) charges** — fuel, oil, '
        'tyres, consumables, repairs, mileage-based depreciation. Many undertakings add a third '
        'group, **maintenance charges**.',
        '**Collect the costs** against the service cost centre for the period, using the normal '
        'documents — requisitions, time sheets, invoices, journals.',
        '**Measure the volume of service provided** in the chosen cost unit for the same period '
        '— the kilometres run, the loads carried, the patient-days, the units generated.',
        '**Compute the cost per unit** by dividing total cost by total units, and analyse it '
        'into its standing and running elements per unit.',
        '**Prepare the operating cost statement** — the standard output of service costing — '
        'showing each cost under its heading, the total, the units of service, and the cost per '
        'unit.',
        '**Compare and control** — against budget, against the previous period, and between '
        'comparable vehicles, routes, wards or departments — and act on the differences.',
        '**Use the result** to set fares, charges or transfer prices, and to decide questions '
        'such as own-or-hire, which routes to run, and when to replace a vehicle.',
      ]},
      {'h4': 'Features that distinguish service costing'},
      {'ul': [
        'there is usually **no inventory** and no work-in-progress, because a service cannot be '
        'stored;',
        '**fixed costs are a high proportion** of the total, so the cost per unit is very '
        'sensitive to the level of activity;',
        'the cost unit is often **composite**, and choosing it badly makes the whole exercise '
        'meaningless;',
        'direct **materials** are usually a small proportion of cost, with labour and overhead '
        'dominating.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q9', 't': 'Features of a good batch costing system',
      'q': [{'p': 'Discuss the necessary features of a good batch costing system.'}],
      'a': [
      {'ol': [
        '**A unique batch number** for every batch, under which all its costs are collected, '
        'exactly as a job number works in job costing.',
        '**A batch cost card** opened for each batch, recording direct materials, direct wages, '
        'direct expenses and absorbed overhead, together with the quantity produced and the '
        'quantity rejected.',
        '**Separate identification of set-up costs.** Set-up cost is incurred **once per '
        'batch**, whatever the batch size, and must be distinguished from the costs that vary '
        'with quantity — otherwise the effect of batch size on unit cost cannot be seen.',
        '**Accurate recording of the number of good units produced**, since the cost per unit is '
        'the batch cost divided by good output; rejects must be counted and their treatment '
        '(normal or abnormal loss) decided.',
        '**A sound overhead absorption basis**, with set-up and machine-related overhead '
        'absorbed on a basis that reflects what causes it.',
        '**Determination of an economic batch quantity**, balancing the set-up cost saved by '
        'making larger batches against the extra cost of holding the resulting inventory.',
        '**Comparison of actual batch cost with the estimate**, so that quoting and planning '
        'improve, and so that inefficiency in a particular batch is identified.',
        '**Proper documentation and control of materials and labour** booked to each batch — '
        'requisitions and time records quoting the batch number.',
        '**Prompt reporting** of the completed batch cost and unit cost to management, in time '
        'to influence the next batch.',
        '**Integration with inventory records**, since completed batches move into finished '
        'goods and must be valued consistently.',
      ]},
      {'key': 'The one feature that distinguishes batch costing from job costing is the '
              'treatment of **batch size**. In job costing each job is unique and the question '
              '"how many should we make at once?" does not arise. In batch costing it is the '
              'central question, because set-up cost per unit falls as the batch grows while '
              'inventory holding cost per unit rises — and a good system must produce the '
              'information needed to strike that balance.'}]}},

    {'eg': {'tag': 'Exam type — Q10',
      't': 'Article: "Peculiarities of contract costing and accounting"',
      'q': [{'p': 'Write an article suitable for publication in an Accounting Students\' '
                  'Journal / Newsletter on the topic: **"Peculiarities of contract costing and '
                  'accounting"**.'}],
      'a': [
      {'h4': 'PECULIARITIES OF CONTRACT COSTING AND ACCOUNTING'},
      {'p': 'Contract costing is a form of specific order costing, and in principle a contract '
            'is only a very large job. In practice, however, four characteristics of contract '
            'work force a quite different accounting treatment, and it is those peculiarities '
            'that make the topic worth an article of its own.'},
      {'h4': '1.  The contract is long and straddles the year end'},
      {'p': 'A job is normally begun and finished within an accounting period, so its profit can '
            'simply be recognised when it is delivered. A contract — a road, a bridge, a housing '
            'estate — may run for three or four years. If profit were recognised only on '
            'completion, the contractor would report no profit at all for years and then a vast '
            'profit in one. Contract costing therefore recognises profit **as the work '
            'proceeds**, and the rules for doing so prudently are the heart of the subject.'},
      {'h4': '2.  The work is carried out on the customer\'s site'},
      {'p': 'Because the work is done away from the contractor\'s own premises, almost '
            'everything becomes a **direct** cost of that contract — materials delivered '
            'straight to site, the wages of everyone working there, the hire of plant, site '
            'power and water, the site office, and even the site supervisor\'s salary. Overhead '
            'absorption, which dominates job costing, is a comparatively minor matter in '
            'contract costing: only head-office overhead has to be apportioned between '
            'contracts.'},
      {'h4': '3.  Progress is measured by an outside professional'},
      {'p': 'The contractor does not decide how much work has been done. An independent '
            '**architect or engineer** inspects the site and issues a **certificate** stating '
            'the **value of work certified** to date, and it is on that certificate that '
            'progress payments are made. Contract accounting therefore turns on a set of terms '
            'that have no counterpart in job costing:'},
      {'ul': [
        '**Value of work certified** — the aggregate value of the certificates issued so far;',
        '**Cost of work certified** — cost to date, less the cost of work not yet certified;',
        '**Work not yet certified** — work physically done since the last certificate;',
        '**Progress payments** — the cash actually received, normally the certified value less '
        'the retention;',
        '**Retention money** — a percentage of the certified value (commonly 5% to 10%) withheld '
        'by the customer for a defects-liability period after completion, as insurance against '
        'faults appearing later;',
        '**Notional profit** — value of work certified less the cost of that work: the profit '
        'that *appears* to have been earned so far, and the starting point for deciding how much '
        'may prudently be taken.',
      ]},
      {'h4': '4.  Profit is recognised cautiously, in stages'},
      {'p': 'Because an uncompleted contract may still go wrong, profit is taken by stages '
            'according to how far it has progressed:'},
      {'ol': [
        '**Early stage** (broadly, less than a quarter complete): **no profit** is taken at all, '
        'because the outcome cannot be judged.',
        '**Fairly advanced** (broadly between a quarter and nine-tenths complete): a fraction of '
        'the notional profit is taken, reduced further by the proportion of the certified value '
        'actually received in cash — commonly $\\tfrac23 \\times \\text{notional profit} '
        '\\times \\dfrac{\\text{cash received}}{\\text{value of work certified}}$.',
        '**Nearly complete**: the estimated total profit on the whole contract is computed, and '
        'the proportion relating to work certified is taken.',
        '**Any foreseeable loss** is recognised **in full, immediately** — prudence works in '
        'only one direction.',
      ]},
      {'h4': '5.  Other peculiarities worth knowing'},
      {'ul': [
        '**A separate contract account** is opened for each contract, functioning as that '
        'contract\'s own trading account.',
        '**Plant on site** is charged to the contract and credited back at its written-down '
        'value at the year end, so the contract bears the depreciation of the plant it actually '
        'used.',
        '**Materials on site** at the year end are credited to the contract and carried forward '
        'as an asset.',
        '**Sub-contractors** are common, and their work is a direct cost of the contract.',
        '**Escalation clauses** may allow the contract price itself to be revised for inflation '
        'in material and labour costs.',
        '**Work-in-progress** in the balance sheet is shown as cost to date plus profit taken, '
        'less losses and less progress payments received.',
      ]},
      {'h4': 'Conclusion'},
      {'p': 'Contract costing is where cost accounting meets the problem of **measuring '
            'performance before the work is finished**. Everything peculiar about it — the '
            'architect\'s certificate, retention money, notional profit, the staged recognition '
            'rules — exists to answer one question that job costing never has to ask: *how much '
            'of this job\'s profit have we actually earned yet?* For the student, the practical '
            'advice is to learn the vocabulary precisely, to be ruthless about distinguishing '
            '**cost to date** from **cost of work certified**, and to remember that profits are '
            'taken cautiously while losses are taken in full.'}]}},

    {'eg': {'tag': 'Exam type — Q11 (12 marks)',
      't': 'A bus fleet — cost per passenger-kilometre',
      'q': [
      {'p': 'A transport company runs a fleet of **six buses** between two towns **75 kilometres '
            'apart**. Each bus has a seating capacity of **40 passengers**. The following '
            'details are available for the month of June 2025:'},
      {'stmt': {'t': 'Costs for June 2025 (₦)', 'rows': [
        ['Wages of drivers, conductors and cleaners', '', 360000],
        ['Salaries of office staff', '', 150000],
        ['Fuel and oils', '', 1350000],
        ['Repairs and maintenance', '', 280000],
        ['Vehicle licensing, insurance and other road levies', '', 240000],
        ['Depreciation of buses', '', 390000],
        ['Finance charges (interest on loan)', '', 300000],
      ]}},
      {'p': 'On average the buses are **80% full** during the trips, and they operate on **25 '
            'days** during the month, doing **a round trip each day**.'},
      {'p': '**Required:** compute the cost per passenger-kilometre.'}],
      'a': [
      {'h4': 'Step 1 — the operating cost statement'},
      {'stmt': {'t': 'Operating cost statement for June 2025 (₦)', 'rows': [
        ['**Standing (fixed) charges**', '', '', '@hd'],
        ['Wages of drivers, conductors and cleaners', 360000, ''],
        ['Salaries of office staff', 150000, ''],
        ['Vehicle licensing, insurance and other road levies', 240000, ''],
        ['Depreciation of buses', 390000, ''],
        ['Finance charges (interest on loan)', 300000, 1440000],
        '@gap',
        ['**Running (variable) charges**', '', '', '@hd'],
        ['Fuel and oils', 1350000, ''],
        ['Repairs and maintenance', 280000, 1630000],
        '@gap',
        ['**Total operating cost for the month**', '', 3070000, '@tt'],
      ]}},
      {'h4': 'Step 2 — the volume of service, in the composite cost unit'},
      {'p': 'The cost unit for passenger transport is the **passenger-kilometre** — one '
            'passenger carried one kilometre. Build it up in three steps:'},
      {'stmt': {'t': 'Passenger-kilometres operated in June 2025', 'rows': [
        ['Distance one way', '', '75 km'],
        ['Round trip (×2)', '', '150 km'],
        ['Round trips per bus in the month (1 per day × 25 days)', '', 25],
        ['Kilometres per bus for the month (150 × 25)', '', '3,750 km'],
        ['Number of buses', '', 6],
        ['**Total kilometres run by the fleet**', '', '22,500 km', '@t'],
        '@gap',
        ['Seating capacity per bus', '', '40 passengers'],
        ['Average occupancy', '', '80%'],
        ['**Average passengers carried per bus (40 × 80%)**', '', '32 passengers', '@t'],
        '@gap',
        ['**Total passenger-kilometres (22,500 km × 32 passengers)**', '', '720,000', '@tt'],
      ]}},
      {'h4': 'Step 3 — cost per passenger-kilometre'},
      {'tex': '\\text{Cost per passenger-km} = \\frac{₦3{,}070{,}000}{720{,}000} '
              '= ₦4.26 \\text{ (to the nearest kobo)}'},
      {'stmt': {'t': 'Analysis of the ₦4.26', 'rows': [
        ['Standing charges:  ₦1,440,000 ÷ 720,000', '', '₦2.00 per passenger-km'],
        ['Running charges:  ₦1,630,000 ÷ 720,000', '', '₦2.26 per passenger-km'],
        ['**Total cost per passenger-kilometre**', '', '**₦4.26**', '@tt'],
      ]}},
      {'key': 'Two things decide every service-costing answer, and both are easy to get wrong. '
              'First, the **round trip** — the buses travel 150 km a day, not 75; forgetting the '
              'return journey halves the denominator and doubles the answer. Second, the '
              '**occupancy** — the unit is passenger-kilometres actually carried, so it is 32 '
              'passengers, not the 40 seats available. Using 40 would give ₦3.41 and understate '
              'the true cost by a fifth.'},
      {'note': 'Note how heavily this business depends on load factor. If occupancy rose from '
               '80% to 100%, the passenger-kilometres would become 900,000 and the cost per '
               'passenger-km would fall to **₦3.41** — a 20% reduction — because the ₦1,440,000 '
               'of standing charges would be spread over more passengers while barely changing '
               'in total. That sensitivity of unit cost to activity is the defining economic '
               'feature of service industries.'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Overhead rate, % of direct wages', 'tex': '\\dfrac{\\text{Total overhead}}{\\text{Total '
   'direct wages}} \\times 100'},
  {'lb': 'Overhead rate, % of direct material', 'tex': '\\dfrac{\\text{Total overhead}}'
   '{\\text{Total direct material cost}} \\times 100'},
  {'lb': 'Notional profit (fairly advanced contract)', 'tex': '\\text{Value of work certified} - '
   '\\text{Cost of work certified}'},
  {'lb': 'Profit taken (fairly advanced contract)', 'tex': '\\tfrac23 \\times \\text{Notional '
   'profit} \\times \\dfrac{\\text{Cash received}}{\\text{Value of work certified}}'},
  {'lb': 'Estimated Total Profit (ETP)', 'tex': '\\text{Total contract price} - \\text{Estimated '
   'total cost}'},
  {'lb': 'Contract value for balance sheet', 'tex': '(\\text{Cost to date} + \\text{Profit '
   'taken}) - \\text{Cash received}'},
 ],
 'focus':
   'Contract costing\'s profit-recognition rules are the single most exam-tested part of this '
   'chapter — know all three contract stages and exactly which formula applies at each, since '
   'using the wrong stage\'s formula is the most common error. Job/batch overhead-absorption '
   'questions test whether the *right basis* was chosen for the scenario, not just correct '
   'arithmetic on a given basis (Illustrations 7.1/7.2 show the same job costed two genuinely '
   'different ways). Always separate cost of work *certified* from cost *to date* before '
   'computing notional profit.',
 'errors': [
   'Applying the nearing-completion ETP formula to a contract that is only fairly advanced (or '
   'vice versa) — the two stages use genuinely different formulas, not the same one at '
   'different points.',
   'Using cost to date instead of cost of *work certified* when calculating notional profit — '
   'these differ whenever some incurred cost has not yet been certified by the architect.',
   'Deferring or spreading a foreseeable contract loss instead of writing it off immediately in '
   'full, as prudence requires.',
   'Forgetting to deduct profit already recognised in prior periods when finding the profit to '
   'take in the *current* period on a nearing-completion contract.',
   'Treating the Job Card and the Job Cost Card as the same document — one lives on the shop '
   'floor, the other in the cost office, and they serve different purposes.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A very large order is best handled, for job-costing purposes, by',
    'o': ['refusing the order entirely', 'costing it only once fully complete',
          'dividing it into separately numbered batches (e.g. 30.1, 30.2, 30.3)',
          'ignoring overhead absorption for that order', 'treating it as process costing'],
    'a': 2,
    'w': 'Splitting a very large order into separately numbered batches lets costing proceed '
         'without waiting for the whole order to finish.',
    'src': 'Chapter 7.2', 'sec': '7.2'},
   {'q': 'A company\'s total overhead is ₵1,800,000 and total direct wages are ₵4,500,000. The '
         'overhead absorption rate as a percentage of direct wages is',
    'o': ['25%', '40%', '2.5%', '250%', '4%'],
    'a': 1,
    'w': 'Overhead rate = (1,800,000 / 4,500,000) × 100 = 40%.',
    'calc': '\\dfrac{1{,}800{,}000}{4{,}500{,}000} \\times 100 = 40\\%',
    'src': 'Chapter 7.2', 'sec': '7.2'},
   {'q': 'In batch costing, unit cost tends to fall as batch size increases mainly because',
    'o': ['direct materials become cheaper in bulk automatically',
          'set-up costs and other flat batch costs are spread over more units',
          'labour works faster on larger batches', 'overhead is waived above a certain quantity',
          'quality control is skipped for large batches'],
    'a': 1,
    'w': 'Set-up costs and other costs that stay the same regardless of batch size are divided '
         'by more units as the batch grows, pulling the average unit cost down.',
    'src': 'Chapter 7.3', 'sec': '7.3'},
   {'q': 'A contract\'s value of work certified is ₵900,000 and cost of work certified is '
         '₵750,000. The notional profit is',
    'o': ['₵150,000', '₵900,000', '₵750,000', '₵1,650,000', '₵0'],
    'a': 0,
    'w': 'Notional profit = value of work certified − cost of work certified = 900,000 − '
         '750,000 = ₵150,000.',
    'calc': '900{,}000 - 750{,}000 = 150{,}000',
    'src': 'Chapter 7.4', 'sec': '7.4'},
   {'q': 'A contract has just started and is nowhere near completion. How much profit should be '
         'recognised?',
    'o': ['The full notional profit', 'Two-thirds of the notional profit',
          'None — expenses are simply carried forward as the cost of work-in-progress',
          'The estimated total profit for the whole contract',
          'Half of the estimated total profit'],
    'a': 2,
    'w': 'At the early stage, no profit is recognised — costs are simply carried forward as WIP, '
         'exactly as in ordinary job costing.',
    'src': 'Chapter 7.4', 'sec': '7.4'},
   {'q': 'Where a contract as a whole is expected to result in a loss, that foreseeable loss '
         'should be',
    'o': ['spread evenly over the contract\'s remaining life',
          'ignored until the contract is actually complete',
          'written off immediately and in full, as soon as it is foreseeable',
          'added to the value of work certified', 'deducted from retention money only'],
    'a': 2,
    'w': 'Prudence requires a foreseeable loss to be written off immediately and to the maximum '
         'extent possible, not deferred or spread.',
    'src': 'Chapter 7.4', 'sec': '7.4'},
   {'q': 'The document issued by an architect, valuing the work done on a contract so far and '
         'forming the basis for payment to the contractor, is the',
    'o': ['job cost card', 'retention certificate', 'work certified (architect\'s valuation) '
          'certificate', 'notional profit statement', 'bin card'],
    'a': 2,
    'w': 'The architect\'s valuation certificate ("work certified") is what payment to the '
         'contractor is based on.',
    'src': 'Chapter 7.4', 'sec': '7.4'},
   {'q': 'Service (operation) costing is most associated with organisations that',
    'o': ['manufacture identical products in continuous production runs',
          'provide standardised services on a continuous basis, e.g. transport or hospitals',
          'produce one-off, highly customised physical products only', 'trade purely in raw '
          'materials', 'never invest in fixed assets'],
    'a': 1,
    'w': 'Service costing applies to organisations providing standardised, continuous services '
         '— transport, electricity, hotels, hospitals, schools, cinemas — often with heavy '
         'fixed-asset investment.',
    'src': 'Chapter 7.5', 'sec': '7.5'},
   {'q': 'On a transport company\'s operation cost sheet, driver\'s salaries and vehicle '
         'licensing are classified as',
    'o': ['variable (running) costs', 'fixed costs (standing charges)', 'direct material costs',
          'notional charges only', 'contract costing items'],
    'a': 1,
    'w': 'Driver\'s salaries, vehicle licensing/insurance, park dues and administrative charges '
         'are all standing (fixed) charges; fuel, depreciation and repairs are the variable '
         '(running) costs.',
    'src': 'Chapter 7.5', 'sec': '7.5'},
  ],
  'theory': [
   {'q': 'Write short notes on each of the following: (i) Overhead absorption, (ii) Cost Plus '
         'basis of pricing, (iii) Transport service costing, (iv) Batch costing.',
    'marks': 20,
    'a': [
      {'p': '**(i) Overhead absorption** — the process of charging a production cost centre\'s '
            'overhead to every cost unit passing through it, using a predetermined overhead '
            'absorption rate applied to actual activity.'},
      {'p': '**(ii) Cost Plus pricing** — pricing an order at its agreed cost plus an agreed '
            'target profit margin, commonly used for government and other contracts where a '
            'market price is not readily available.'},
      {'p': '**(iii) Transport service costing** — a form of service costing that aggregates a '
            'vehicle\'s fixed (standing) and variable (running) costs on an operation cost '
            'sheet, to find a cost per unit of service such as cost per kilometre.'},
      {'p': '**(iv) Batch costing** — costing a quantity of identical units produced together '
            'under one job number, with the total batch cost divided by the number of units to '
            'find a cost per unit; unit cost falls as batch size rises, since flat costs (like '
            'set-up cost) are spread over more units.'},
    ], 'src': 'Chapter 7.2', 'sec': '7.2'},
   {'q': 'Discuss the concept of Job Order Costing as clearly as possible.',
    'marks': 10,
    'a': [
      {'p': 'Job order costing is a specific-order costing method used where each unit of '
            'output — a "job" — can be separately identified throughout production, typically '
            'made to a customer\'s own specification (construction, printing, general '
            'engineering). Each job is given its own order number, tracked through a job cost '
            'sheet/ledger account recording its own material, labour and absorbed overhead, '
            'letting the organisation determine the total cost — and hence the profit or loss '
            '— of that specific job individually, rather than averaging cost across continuous, '
            'undifferentiated output the way process costing does.'},
    ], 'src': 'Chapter 7.1', 'sec': '7.1'},
  ]},
}
