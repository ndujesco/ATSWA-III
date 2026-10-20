CH = {
 'n': 7,
 't': 'Audit Tests and Sampling Procedures',
 'brief': 'How the auditor actually selects what to test (audit sampling, statistical vs. '
          'non-statistical, sample design/size/selection/evaluation), the substantive testing '
          'programmes for key transaction cycles and Statement of Financial Position items '
          '(including the notoriously difficult verification of inventory), analytical '
          'procedures, and the specialised audit procedures for subsequent events, '
          'contingencies and the going concern basis — closing with quality control at both '
          'the firm and individual-assignment level.',
 'outcomes': [
   'Explain the role sampling techniques play in auditing',
   'Draw audit programmes appropriate for substantive testing for key audit areas',
   'Verify the existence, valuation, ownership, presentation and disclosure of Statement of '
   'Financial Position items',
   'Conduct analytical review procedures',
   'Outline audit procedures relevant to events occurring after the reporting date and '
   'contingencies',
   'Outline the indications for going concern difficulties',
   'Describe the quality control procedures required at assignment level and at the firm '
   'level',
 ],
 'secs': [
  {'n': '7.1', 't': 'Audit sampling', 'b': [
    {'p': 'When designing audit procedures, the auditor determines appropriate means for '
          'selecting items for testing, to gather sufficient appropriate audit evidence.'},
    {'h4': 'Key definitions'},
    {'table': {'align': 'll', 'head': ['Term', 'Definition'], 'rows': [
      ['**Audit sampling**', 'Applying audit procedures to less than 100% of items within a '
       'class of transactions or account balance, such that all sampling units have a chance of '
       'selection — enabling the auditor to form or assist in forming a conclusion about the '
       'whole population. May be statistical or non-statistical.'],
      ['**Error**', 'Control deviations (tests of controls) or misstatements (tests of '
       'details); "total error" means the total deviation rate or total misstatement.'],
      ['**Anomalous error**', 'An error arising from an isolated event that has not recurred '
       'except on specifically identifiable occasions, and is therefore NOT representative of '
       'errors in the population.'],
      ['**Population**', 'The entire set of data from which a sample is selected and about '
       'which the auditor wishes to conclude — may be divided into strata (sub-populations), '
       'each examined separately.'],
      ['**Sampling risk**', 'The risk that the auditor\'s sample-based conclusion differs from '
       'the conclusion reached by testing the entire population.'],
      ['**Non-sampling risk**', 'The risk of an erroneous conclusion for any reason unrelated '
       'to sample size — e.g. relying on persuasive (not conclusive) evidence, using '
       'inappropriate procedures, or misinterpreting evidence and failing to recognise an '
       'error.'],
      ['**Sampling unit**', 'The individual items constituting a population (e.g. cheques on a '
       'deposit list, sales invoices, debtor balances) or a monetary unit.'],
      ['**Statistical sampling**', 'Sampling with BOTH: (i) random item selection; and (ii) use '
       'of probability theory to evaluate results, including measuring sampling risk. Lacking '
       'either characteristic makes it non-statistical sampling.'],
      ['**Stratification**', 'Dividing a population into subpopulations, each a group of '
       'sampling units sharing similar characteristics (often monetary value).'],
      ['**Tolerable error**', 'The maximum error in a population the auditor is willing to '
       'accept.'],
    ]}},
    {'key': 'Sampling risk has **two directions**, with opposite consequences: (i) concluding '
            'controls are more effective (or a material error does not exist) than is actually '
            'true — this affects audit **effectiveness** and is more likely to cause an '
            'inappropriate opinion; and (ii) concluding controls are less effective (or a '
            'material error exists) than is actually true — this affects audit **efficiency**, '
            'usually triggering unnecessary additional work. The mathematical complements of '
            'these risks are called **confidence levels**.'},

    {'h4': '§7.1.2 Selecting items for testing'},
    {'p': 'Three means are available: selecting all items (100% examination), selecting '
          'specific items, and audit sampling. The choice (or combination) depends on the risk '
          'of material misstatement for the assertion tested and audit efficiency — but the '
          'auditor must always be satisfied the method is effective in providing sufficient '
          'appropriate evidence.'},
    {'table': {'align': 'll', 'head': ['Approach', 'When appropriate'], 'rows': [
      ['**Selecting all items**', 'Rare for tests of controls, more common for tests of '
       'details — e.g. a small number of large-value items, significant risk with no other '
       'sufficient means, or where automated/repetitive processing makes 100% examination '
       'cost-effective via CAATs.'],
      ['**Selecting specific items**', 'Based on the auditor\'s understanding of the entity, '
       'risk assessment, and population characteristics — e.g. high-value/key items, items '
       'over a certain amount, items chosen to obtain information, or items to test specific '
       'control activities. Subject to non-sampling risk. **Does NOT constitute audit '
       'sampling** — results cannot be projected to the whole population, so the auditor still '
       'considers whether the untested remainder needs its own evidence if material.'],
      ['**Audit sampling**', 'Applying either statistical or non-statistical sampling to a '
       'class of transactions or account balance, where results CAN be projected to the whole '
       'population.'],
    ]}},
    {'key': 'For any sample to be **representative**, every item in the population must have '
            'an opportunity of being selected.'},

    {'h4': 'Statistical vs. non-statistical sampling'},
    {'p': 'The choice is a matter of judgment about the most efficient means of obtaining '
          'sufficient appropriate evidence — e.g. for tests of controls, analysing the '
          '**nature and cause** of errors is often more important than a statistical count of '
          'their presence/absence, favouring non-statistical sampling in that case.'},
    {'key': 'Sample size is **not** a valid criterion for distinguishing statistical from '
            'non-statistical sampling — an approach can use elements of statistical technique '
            '(e.g. computer-generated random numbers) without meeting the full definition. Only '
            'where the approach genuinely has statistical sampling\'s characteristics are '
            'statistical measurements of sampling risk actually valid.'},
    {'p': 'Conditions favouring statistical sampling:'},
    {'ol': [
      'the population must be **sufficiently large** (minimising the potential margin of '
      'error);',
      'the system producing the records must be **sufficiently reliable** — without a system '
      'worthy of the name, it is dangerous to treat any recorded transaction as representative, '
      'and a vouching audit of nearly all transactions may be the only alternative;',
      'all items within the population must be **homogeneous** — falling within the same '
      'materiality band, recorded the same way, and subject to the same internal checks/'
      'controls; and',
      'all items must be **identifiable and accessible**, so each stands an equal chance of '
      'selection.',
    ]},
    {'table': {'align': 'll', 'head': ['Advantages of statistical sampling', 'Disadvantages of '
      'statistical sampling'], 'rows': [
      ['States a definite confidence level, within a stated precision limit, that the whole '
       'population conforms to the sample result.', 'Auditing has never been a mathematical '
       'discipline — developed intuition has historically been more valuable than mathematical '
       'knowledge.'],
      ['Sample size is objectively determined given the accepted degree of risk.',
       'Mathematically valid schemes take a long time, during which a good deal of '
       'representative random sampling could otherwise have been conducted.'],
      ['Fixing precision/confidence levels compels the auditor to clarify audit objectives.',
       'Results in sample sizes much smaller than traditional practice — validity then depends '
       'on rigid adherence to statistical tenets and every team member\'s technical grasp of '
       'them.'],
      ['Results can be expressed in precise mathematical terms.', 'Many pre-implementation '
       'decisions are inherently subjective, making some auditors suspicious of the technique\'s '
       'validity (or how a court might view conclusions reached this way).'],
      ['Bias in selecting sample units is largely eliminated.', 'Often needs back-up testing '
       'within the population anyway — large items, non-routine items, sensitive items.'],
    ]}},

    {'h4': 'Judgmental (non-statistical) sampling'},
    {'def': {'t': 'Judgmental sampling', 'd': 'selecting a sample of appropriate size based on '
                  'the auditor\'s judgment of what is desirable.'}},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['In use for many years — lends itself to easy application through experience.',
       'Unscientific.'],
      ['No special statistical knowledge required.', 'Wasteful — sample sizes are usually too '
       'large.'],
      ['No time wasted on mathematics.', 'No quantitative results obtained.'],
      ['The auditor can apply judgment — "the sixth sense."', 'Personal bias in selection is '
       'unavoidable, and there is no real logic to sample size/selection.'],
      ['—', 'Selection can be imbalanced to suit the auditor\'s convenience — e.g. items near '
       'year end for cut-off — and conclusions from it are usually vague.'],
    ]}},

    {'h4': '§7.1.4 Designing the sample'},
    {'p': 'The auditor considers the audit procedure\'s objectives and the population\'s '
          'attributes: (a) the specific objectives and best combination of procedures to '
          'achieve them, clarifying what constitutes an error and what population to sample; '
          '(b) what conditions constitute an error, by reference to the procedure\'s objective — '
          'e.g. in testing receivables existence via confirmation, a customer payment made '
          'before but received shortly after the confirmation date is **not** an error, and a '
          'mis-posting between customer accounts that does not affect the total receivables '
          'balance is not an error **for this specific procedure**, even though it may matter '
          'elsewhere (e.g. fraud assessment); and (c) an expected error rate (tests of '
          'controls) or expected error amount (tests of details) — if the expected error rate '
          'is unacceptably high, tests of controls are normally not performed at all; if the '
          'expected amount of error is high in tests of details, 100% examination or a large '
          'sample may be appropriate.'},

    {'h4': '§7.1.5 Population'},
    {'p': 'The population must be: (a) **appropriate to the objective**, including the '
          'direction of testing — e.g. testing for accounts payable overstatement uses the '
          'payables listing itself, but testing for **understatement** requires a different '
          'population entirely (subsequent disbursements, unpaid invoices, suppliers\' '
          'statements, unmatched receiving reports); and (b) **complete** — e.g. conclusions '
          'about all vouchers require confidence that all vouchers were actually filed.'},

    {'h4': '§7.1.6 Value weighted selection'},
    {'p': 'Often efficient for tests of details (particularly overstatement testing): defining '
          'the sampling unit as individual **monetary units** making up a balance, then '
          'examining whichever items contain the selected monetary units. This directs audit '
          'effort toward larger-value items (which have a greater chance of selection) and can '
          'result in smaller sample sizes overall.'},

    {'h4': '§7.1.7 Sample size'},
    {'key': 'Sample size is affected by the sampling risk the auditor is willing to accept — '
            'the **lower** the acceptable risk, the **greater** the sample size needed. It can '
            'be determined via a statistically-based formula, or through professional '
            'judgment objectively applied.'},

    {'h4': '§7.1.8 Selecting the sample — five methods'},
    {'table': {'align': 'll', 'head': ['Method', 'How it works'], 'rows': [
      ['**Random sampling**', 'Ensures all items have an equal chance of selection, e.g. via '
       'random number tables.'],
      ['**Systematic sampling**', 'A constant interval between selections, with a random start '
       '— the auditor must ensure the interval does not coincide with a pattern in the '
       'population.'],
      ['**Haphazard sampling**', 'An acceptable alternative to random selection, provided the '
       'auditor is satisfied the sample is not unrepresentative — care is needed to avoid bias '
       'toward easily located items.'],
      ['**Stratified sampling**', 'Divides the population into layers/strata, each tested '
       'separately (by random or interval methods) — appropriate where values vary widely; '
       'each stratum\'s relative materiality determines its own required confidence level and '
       'precision range.'],
      ['**Cluster sampling**', 'Suitable where data is grouped so that selecting a cluster is '
       'itself a sensible test — each cluster is numbered, one selected randomly, then tested '
       'fully or by further random/interval sampling. Most precise when each cluster is as '
       'varied internally, and as similar to other clusters, as possible. Useful when the '
       'population is too dispersed for other selection forms.'],
    ]}},

    {'h4': '§7.1.9-7.1.12 Performing, evaluating and concluding'},
    {'p': 'If a selected item is unsuitable for the designed procedure (e.g. a voided cheque '
          'selected to test payment authorisation), an appropriately chosen **replacement** is '
          'examined instead — provided the original item genuinely does not constitute an '
          'error. Where suitable alternative procedures **cannot** be performed on a selected '
          'item (e.g. lost documentation), the auditor ordinarily treats that item as an '
          'error.'},
    {'p': 'For **tests of controls**, the auditor considers the direct effect of identified '
          'errors on the financial statements, and the effect on control effectiveness/audit '
          'approach (e.g. where an error results from management override). An **anomalous '
          'error** requires a high degree of certainty (via additional procedures) that it is '
          'genuinely non-representative — e.g. an error traced to a single day\'s computer '
          'breakdown, or an incorrect formula confirmed to be used at only one branch.'},
    {'p': 'For **tests of details**, the auditor **projects** monetary errors found in the '
          'sample to the whole population, comparing the projected total against **tolerable '
          'error** (itself an amount ≤ the materiality used for that class of transactions/'
          'balance).'},
    {'key': 'If total projected error plus anomalous error is close to, but below, tolerable '
            'error, the auditor considers the persuasiveness of results in light of other '
            'procedures, recognising that a **different sample** might have produced a '
            'different estimate that exceeds tolerable error — additional evidence reduces this '
            'risk.'},
    {'p': 'If the evaluation indicates the population assessment needs revision, the auditor '
          'may: (a) request management investigate and adjust; (b) modify the nature/timing/'
          'extent of further procedures (e.g. extend the sample, test an alternative control, '
          'modify substantive procedures); and/or (c) consider the effect on the audit '
          'report.'},
    {'p': 'The steps of audit sampling, summarised: define the audit objective; define the '
          'population (must be complete); define the sample size; select items using the '
          'appropriate technique; test the selected items; and evaluate results — analysing '
          'errors against expected rates, estimating total population error, and ensuring the '
          'final conclusion is valid and clearly documented in the current file.'},
  ]},

  {'n': '7.2', 't': 'Substantive testing procedures', 'b': [
    {'key': 'Substantive procedures detect material misstatement at the **assertion level**, '
            'and are performed **irrespective of** the assessed risk — the auditor always '
            'designs and performs substantive procedures for each **material** class of '
            'transactions, account balance and disclosure. Where a **significant risk** has '
            'been identified, the auditor performs substantive procedures specifically '
            'responsive to that risk.'},
    {'p': 'Substantive procedures related to the financial statement closing process always '
          'include: (a) agreeing the financial statements to the underlying accounting '
          'records; and (b) examining material journal entries and other adjustments made '
          'while preparing the financial statements.'},
    {'h4': '§7.2.1 Nature of substantive procedures'},
    {'p': 'Substantive analytical procedures suit large, predictable transaction volumes; '
          'tests of details generally suit assertions about account balances (existence, '
          'valuation). Designing substantive analytical procedures involves considering: their '
          'suitability given the assertions; the reliability of the underlying data; whether '
          'the expectation is sufficiently precise; and what amount of difference from '
          'expectation is acceptable.'},

    {'h4': '§7.2.2 Substantive testing programmes for key audit areas'},
    {'p': 'Illustrative audit programmes for three key transaction cycles:'},
    {'table': {'align': 'll', 'head': ['Cycle', 'Objectives and key programme steps'], 'rows': [
      ['**Sales and receipts**', 'Objectives: confirm reliability/accuracy/completeness of the '
       'accounting; confirm all goods supplied were duly invoiced and recorded. Key steps: '
       'test the numerical sequence of dispatch notes and sales invoices; trace a sample from '
       'dispatch notes through to sales invoice, sales day book, inventory records and proof of '
       'delivery; check invoices against customer orders, credit procedures, price lists, '
       'calculations and postings; for receipts, trace to the cash book, paying-in slip and '
       'bank statement; cast/cross-cast the sales day book and control account; vouch a sample '
       'of credit notes against correspondence, authorisation and inventory records; confirm '
       'discounts match the client\'s trade terms; and scrutinise both books for large/unusual '
       'items throughout the year.'],
      ['**Purchases and payments**', 'Objectives: confirm reliability/accuracy/completeness of '
       'the accounting; confirm all incurred liabilities are recorded and represent goods/'
       'services actually received. Key steps: test the numerical sequence of goods-received '
       'notes and purchase invoices; verify authorisation, cash discounts, price agreement, '
       'delivery-note matching, and additions/calculations (including VAT) on a sample of '
       'invoices; check allocation to inventory/WIP records; cast/cross-cast the purchase day '
       'book and petty cash book; select miscellaneous cash-book payments and verify '
       'authorisation/allocation/vouching; and scrutinise the books for large/unusual items.'],
      ['**Payroll**', 'Objectives: ensure pay levels are in order; check accuracy/validity of '
       'deductions; confirm proper payments; test net-pay reasonableness; confirm reliability/'
       'accuracy/completeness of accounting entries; ensure correct PAYE/social security '
       'treatment. Key steps: select a sample of employees and check gross pay against hourly/'
       'piece-work/overtime rate lists, salary lists and employment contracts; check hours '
       'worked against time records for hourly staff, and output returns for piece workers; '
       'check PAYE/NSITF deduction additions and cross-cast to net pay; inspect receipts for '
       'cash payments; trace gross wages to income tax deduction and holiday pay records; trace '
       'a sample of net wages to the cash book; check wage-summary casts and postings to the '
       'nominal ledger; review payroll cost trends for unusual variation; trace joiners/leavers '
       'to ensure correct-period payments; and, for significant cash payments, consider '
       'attending to observe the pay-out.'],
    ]}},
  ]},

  {'n': '7.3', 't': 'Verification of Statement of Financial Position items', 'b': [
    {'def': {'t': 'Verification', 'd': 'the process by which auditors seek confirmation of the '
                  'existence, ownership, cost/valuation and appropriate presentation/disclosure '
                  'of assets and liabilities — relying heavily on vouching work having been '
                  'properly executed.'}},
    {'p': 'Specific verification objectives, in summary:'},
    {'table': {'align': 'll', 'head': ['Objective', 'What the auditor establishes'], 'rows': [
      ['**Cost**', 'What the client actually paid, supported by supplier invoices/receipts, '
       'traced to the bank statement/cash book.'],
      ['**Authorization**', 'That acquisition passed through the company\'s proper approval '
       'procedures, evidenced by documents.'],
      ['**Valuation**', 'That assets appear at fair value (which may differ from original '
       'cost) and liabilities at the amount likely to be needed for settlement — including '
       'correct determination of depreciation or other value falls on an acceptable basis.'],
      ['**Existence**', 'Via physical verification wherever practicable, ideally on a random '
       'selection basis if 100% inspection is impractical.'],
      ['**Beneficial ownership**', 'That the client genuinely owns the asset / owes the '
       'liability — sometimes via documents like leases/deeds, sometimes only via '
       'corroborative evidence or outside representations.'],
      ['**Presentation/disclosure**', 'That items are appropriately presented, with full '
       'disclosure.'],
    ]}},
    {'note': 'Verification procedures draw on the same techniques covered in Chapter 6: '
             'observation, inspection, enquiry and confirmation, computation, and analytical '
             'review.'},

    {'h4': 'Verification objectives and programmes for key assets/liabilities'},
    {'table': {'align': 'll', 'head': ['Item', 'Objectives and key programme steps'], 'rows': [
      ['**Non-current assets**', 'Objectives: ownership confirmed; self-constructed assets '
       'properly capitalised; cost/valuation correctly stated with consistent depreciation; '
       'physical existence verified; proper classification/presentation. Steps: obtain a '
       'summary reconciling to the prior year\'s Statement of Financial Position; test '
       'additions against suppliers\' invoices/architects\' certificates and capital '
       'expenditure authorisations; test disposal proceeds and disposal authority; verify '
       'original cost/depreciation elimination on disposal, and profit/loss calculations; '
       'inspect title deeds/leases; verify any revaluation\'s basis and the valuer\'s '
       'independence/qualifications; physically inspect samples; check depreciation rates are '
       'board-approved and reasonable; reconcile the asset register to the accounts; and verify '
       'adequate insurance cover.'],
      ['**Investments**', 'Objectives: documentary ownership evidence exists; period changes '
       'were bona fide transactions; the valuation basis is appropriate and consistently '
       'applied; amounts are properly classified/described. Steps: analyse investments and '
       'test clerical accuracy; obtain third-party confirmation or physically inspect '
       'securities; test interest/dividend income; check acquisitions/redemptions and capital '
       'distributions/bonus/rights issues; verify quoted prices at the reporting date; assess '
       'unlisted investment valuation; and confirm current-vs-long-term classification.'],
      ['**Debtors**', 'Objectives: confirm accuracy/collectability of the balance; confirm the '
       'doubtful debts provision is adequate. Steps: examine material ledger accounts and cast '
       'the balance list, tracing to the control account; select balances for direct '
       'confirmation via circularisation and investigate discrepancies; where no '
       'circularisation, check post-date payments; examine credit balances (ensuring proper '
       'authorisation and separate disclosure under creditors); verify the doubtful debts/'
       'discount provisions are reasonable; review credit control compliance; verify bad-debt '
       'write-off authorisation and prior recovery efforts; and examine post-year-end credit '
       'notes for genuine sales.'],
      ['**Cash at bank and in hand**', 'Objectives: confirm existence/accuracy of year-end '
       'balances; confirm proper classification/description. Bank steps: obtain and compare '
       'the year-end bank reconciliation against the cash book/bank statements; trace '
       'outstanding cheques/lodgements to subsequent clearance; scrutinise for dishonoured '
       'cheques; obtain a direct bank confirmation certificate; check overdraft security '
       'against facility agreements. Cash steps: count cash in the cashier\'s presence and '
       'reconcile; verify last-day receipts were banked or included in the cash balance; '
       'examine pre-/post-year-end cash counts and petty cash replenishment entries.'],
      ['**Trade creditors**', 'Objectives: confirm all existing/incurred creditors are '
       'recorded at the correct amount and represent genuine claims; confirm consistent, '
       'properly described/classified presentation. Steps: test extraction of the purchase '
       'ledger and reconcile against supplier statements (or circularise where unavailable); '
       'cast the balance list and trace to the control account; separate and reclassify debit '
       'balances under debtors; review goods-received-not-invoiced provisioning against '
       'delivery/goods-received notes; review major suppliers\' terms for reservation of '
       'title; reconcile inter-company/inter-branch balances; and check classification/'
       'disclosure.'],
    ]}},
  ]},

  {'n': '7.4', 't': 'Verification of inventories', 'b': [
    {'key': 'Inventory has always been the asset posing the **greatest verification '
            'difficulties**, because: it is almost always **material**, especially for '
            'manufacturers; misstatement has a **direct, one-to-one effect** on reported profit '
            '(an inventory overstatement equally overstates profit); it is the **only** '
            'published-accounts item not itself arising from the double-entry process — its '
            'figure depends largely on physical inventory-taking, making it the item most '
            'susceptible to manipulation; for a manufacturer, it is not really one asset at all '
            'but several (raw materials, WIP, finished goods, etc.), each with its own '
            'difficulties; verification sometimes needs highly technical expertise beyond the '
            'auditor\'s own; items require categorisation (sound, defective, slow-moving, '
            'obsolete, scrap) that materially affects value, yet the auditor often lacks the '
            'competence to question that categorisation; inventory may be held across multiple '
            'locations needing **simultaneous** counting to avoid omission or double-counting '
            'from goods moving between sites; a moving production line or construction site '
            'complicates counting further, since work is unlikely to be halted specially for '
            'it; and some items pose basic identification/measurement problems (e.g. measuring '
            'a large volume of liquid — by volume or weight?).'},
    {'p': 'Objectives of inventory verification: confirm all inventory/WIP belonging to the '
          'client has been brought into the accounts; confirm third-party inventory in the '
          'client\'s possession is separately identified and excluded; confirm obsolete/'
          'damaged/slow-moving inventory is separately identified and stated at realisable '
          'value; confirm the value stated is correctly calculated on a basis consistent with '
          'prior years; and confirm adequate security arrangements exist.'},

    {'h4': 'Audit programme for inventory quantity'},
    {'p': 'Before the count: review the client\'s own counting instructions for adequacy, and '
          'note any weaknesses to raise with the audit manager. During the count: attend to '
          'observe, ensuring slow-moving/obsolete/damaged inventory is segregated, all '
          'locations are covered, third-party inventory is segregated, and inventory sheets '
          'are properly accounted for/dated/signed. After the count: complete the standard '
          'inventory-taking report; obtain details of the last goods inward/outward notes for '
          'cut-off testing; ensure all rough sheets are processed into the final sheets; check '
          'quantities tested at observation against final sheets; test extensions/additions; '
          'reconcile final sheets to the inventory summary and to any perpetual inventory '
          'records (bin cards, stores ledgers), investigating discrepancies; and reconcile the '
          'final accounts figure with perpetual/management-account totals, scheduling reasons '
          'for any divergence.'},
    {'p': 'For inventory held by **third parties**, obtain direct certificates identifying the '
          'stock\'s nature/quantity/purpose, confirming good condition and freedom from lien/'
          'charge, and any necessary deductions for slow-moving/damaged/obsolete stock.'},

    {'h4': 'Audit programmes for valuation'},
    {'table': {'align': 'll', 'head': ['Aspect', 'Key programme steps'], 'rows': [
      ['**Inventory valuation (general)**', 'Test final-sheet prices to purchase invoices; '
       'scrutinise bin cards/records for apparently obsolete stock; review slow-moving/'
       'obsolete items with the storekeeper and responsible officials; assess the appropriate '
       'value reduction given prior-year valuation and near-term sale prospects; and schedule '
       'the details for the manager\'s attention.'],
      ['**Work in progress (WIP)**', 'Test the reliability of the costing system (adequate '
       'stores-issue/labour-usage controls, reasonable overhead allocation confirmed against '
       'the actual — or normal, if below-capacity — rate, and a WIP valuation method '
       'consistent with prior years); compare selected WIP items\' cost-plus-completion '
       'estimate against selling price, providing for anticipated losses; and, for long-term '
       'contracts, confirm the WIP calculation basis is permissible under the relevant '
       'accounting standard.'],
      ['**Overall inventory schedule**', 'Prepare a schedule summarising inventory/WIP by '
       'category with prior-year comparatives, reconciled to the Statement of Financial '
       'Position and final inventory sheets, stating the valuation basis and evidence '
       'obtained; state the proportion of value covered by observation/testing; compare key '
       'ratios (inventory/WIP to sales, raw material/WIP/finished goods to cost of sales) '
       'against the prior period, scheduling reasons for significant changes; and review the '
       'valuation on a current cost basis, discussing any material difference with directors.'],
    ]}},

    {'h4': 'Attendance at inventory taking'},
    {'key': 'It remains **management\'s** responsibility to ensure reported inventory figures '
            'represent inventory physically in existence and complete — this responsibility is '
            '**not reduced** merely because the auditor attends the physical count. It is the '
            '**auditor\'s** responsibility to obtain evidence enabling conclusions about the '
            'validity of the quantities underlying the reported figure — principally through '
            'test counts made by the auditor themselves, and reviewing the entity\'s inventory '
            'records/control systems to decide how much to rely on attendance.'},
    {'p': 'Where inventory is material and the auditor is relying on management\'s count as '
          'existence evidence, the auditor should **attend** the count — attendance is normally '
          'the best way of evidencing the proper functioning of management\'s counting '
          'procedures, and hence the existence/condition of inventory. WIP existence evidence '
          'often also comes from the count, though where WIP\'s nature makes counting '
          'impracticable, inspection still helps plan procedures and assess completion stage, '
          'even absent a formal count to attend.'},
    {'h4': 'Types of inventory taking'},
    {'p': 'Physical verification may be a full count (or measurement) of everything at year '
          'end or a nearby date, a partial count statistically extrapolated, or continuous '
          'inventory-checking throughout the year (some businesses use continuous methods for '
          'some items and a full count for others). Evidence is most effective when the count '
          'happens **at** the year end; counts before/after are acceptable provided '
          'intervening movements can be examined/substantiated — the greater the interval, the '
          'greater the difficulty in substantiating the year-end figure (lessened by strong '
          'internal control and satisfactory records).'},
    {'key': 'Where **continuous** inventory-checking is used, the auditor tests to confirm '
            'management: maintains adequate, up-to-date records; has satisfactory counting/'
            'test-counting procedures covering all inventory at least once a year; and '
            'investigates/corrects material differences between book records and physical '
            'counts.'},
    {'h4': 'Inventory-taking procedures: before, during and after'},
    {'p': '**Before**: review prior-year working papers and discuss inventory changes with '
          'management; discuss counting arrangements/instructions; understand the nature/'
          'volume of inventory and high-value items; consider location implications for '
          'control; review internal/accounting systems for difficulty areas (e.g. cut-off); '
          'consider internal audit involvement; ensure representative coverage of locations/'
          'inventories/procedures, with particular attention to high-value items; arrange '
          'third-party confirmation (or attendance at their premises, if their holding is '
          'material or they seem unreliable); and establish whether expert help is needed for '
          'specialised inventory. The auditor evaluates the adequacy of the client\'s own '
          'written instructions, seeking improvements where inadequate.'},
    {'p': '**During**: ascertain whether client staff follow instructions properly, making own '
          'test counts and immediately raising unsatisfactory results with supervising '
          'management (possibly requesting a recount); select items both from count records '
          'and physical inventory, checking one against the other (particular attention to '
          'high-value items); include working-paper evidence (rough sheet copies, sheet-'
          'sequence details) for subsequent testing; determine whether procedures for '
          'identifying damaged/obsolete/slow-moving stock operate properly, gathering '
          'condition/age/usage/completion-stage information; assess cut-off procedure adequacy; '
          'and conclude whether the count is reliable enough as an existence basis, forming an '
          'overall impression of inventory levels/values for later reasonableness judgment.'},
    {'p': '**After**: follow up the matters recorded during the count (using rough-sheet '
          'copies/test-count details to check the final sheets are accurate/complete); check '
          'third-party replies, follow up queries, and notify senior management of serious '
          'problems encountered.'},
  ]},

  {'n': '7.5', 't': 'Analytical procedures', 'b': [
    {'def': {'t': 'Analytical procedures', 'd': 'evaluations of financial information through a '
                  'study of plausible relationships among financial and non-financial data — '
                  'including investigating fluctuations/relationships inconsistent with other '
                  'information, or deviating significantly from predicted amounts.'}},
    {'p': 'Analytical procedures compare the entity\'s financial information against: '
          'comparable prior-period information; anticipated results (budgets, forecasts, or an '
          'auditor estimate like depreciation); and similar-industry information. They also '
          'consider relationships among financial elements expected to follow a predictable '
          'pattern (e.g. gross margin %), and between financial and relevant non-financial '
          'information (e.g. payroll cost to headcount).'},
    {'p': 'Analytical procedures are used for three purposes: as **risk assessment '
          'procedures**, to understand the entity/environment; as **substantive procedures**, '
          'where more effective/efficient than tests of details; and as an **overall review** '
          'at the end of the audit.'},

    {'h4': '§7.5.2 As risk assessment procedures'},
    {'p': 'Applied using both financial and non-financial information (e.g. sales vs. selling '
          'floor space, or vs. volume sold) — may reveal aspects of the entity the auditor was '
          'previously unaware of, helping determine the nature/timing/extent of further '
          'procedures.'},

    {'h4': '§7.5.3-7.5.7 As substantive procedures'},
    {'p': 'The choice between tests of details and substantive analytical procedures (or a '
          'combination) rests on judgment about relative effectiveness/efficiency. The auditor '
          'ordinarily enquires about the availability/reliability of information needed, and '
          'may use entity-prepared analytical data if satisfied it is properly prepared. '
          'Designing them requires considering:'},
    {'table': {'align': 'll', 'head': ['Factor', 'What it involves'], 'rows': [
      ['**Suitability given the assertions**', 'Generally more applicable to large, '
       'predictable transaction volumes; relies on data relationships continuing absent known '
       'contrary conditions. Depends on the risk assessment (e.g. weak sales-order controls '
       'push toward tests of details for receivables) and whether tests of details are also '
       'applied to the same assertion (e.g. combining receivables ageing analysis with '
       'subsequent-receipts testing).'],
      ['**Reliability of the data**', 'Influenced by source (more reliable if independent/'
       'external), comparability (broad industry data may need supplementing for a specialised '
       'producer), nature/relevance (whether budgets are set as expected results vs. '
       'aspirational goals), and controls over the data\'s preparation.'],
      ['**Precision of the expectation**', 'Depends on prediction accuracy (gross margin '
       'comparisons are ordinarily more consistent than discretionary expenses like R&D or '
       'advertising), the degree of disaggregation possible (more effective applied to '
       'individual operating sections than the whole entity), and the availability of both '
       'financial and non-financial information.'],
      ['**Acceptable difference from expectation**', 'Driven primarily by materiality and the '
       'desired assurance level — considering whether a combination of individually-acceptable '
       'differences could aggregate unacceptably. The higher the risk of material misstatement, '
       'the smaller the acceptable difference before investigation is required.'],
    ]}},

    {'h4': '§7.5.8-7.5.9 Overall review and investigating unusual items'},
    {'p': 'Analytical procedures are applied at/near the audit\'s end, forming an overall '
          'conclusion on whether the financial statements as a whole are consistent with the '
          'auditor\'s understanding — corroborating conclusions from individual components, and '
          'potentially revealing a previously unrecognised risk requiring re-evaluation of '
          'planned procedures.'},
    {'key': 'When significant fluctuations or unexpected relationships are found, the auditor '
            '**investigates** — beginning with management enquiries, then corroborating the '
            'response against the auditor\'s own understanding/other evidence, and applying '
            'other procedures where management cannot provide an adequate explanation.'},

    {'h4': '§7.5.10 Public sector perspective'},
    {'p': 'Traditional business-entity relationships may not hold in government/public-sector '
          'audits — e.g. little direct revenue-expenditure relationship, or no relationship '
          'between asset expenditure and reported asset amounts where acquisition costs are '
          'not capitalised; industry comparative data may not exist. Other relationships '
          '(e.g. cost per kilometre of road construction, vehicles acquired vs. retired) may '
          'still be relevant — referring to private-sector data where appropriate, or building '
          'an in-house reference database.'},

    {'h4': '§7.5.11 The practice of analytical procedures'},
    {'p': 'Items commonly subjected to analytical procedures: creditors and purchases; '
          'inventories and cost of sales; fixed assets, depreciation, repairs and maintenance; '
          'loans and interest; investments and investment income; debtors and bad debt '
          'expense; and debtors and sales.'},
    {'p': 'Ratios commonly computed: gross profit margin; net profit margin; return on capital '
          'employed; current ratio; quick (acid test) ratio; debtors turnover period; '
          'creditors payment period; rate of inventory turnover; gearing ratio; price/earnings '
          'ratio; dividend per share; earnings per share; earnings yield; and return on net '
          'assets — plus any other ratio the client\'s specific circumstances call for (e.g. '
          'revenue per passenger-mile for an airline).'},

    {'h4': '§7.5.12 Other areas examined'},
    {'p': 'Changes in products/customers/distribution/returns; the effect of inflation, '
          'industrial disputes, production-technology changes and activity levels on wages; '
          'explanations for major standard-costing variances (particularly overhead over/under-'
          'absorption, given its inventory-valuation effect); production/sales trends and their '
          'effect on obsolete-inventory provisions; changes in labour/overhead content of '
          'production costs; comparisons of rent, rates, interest and vehicle-running expenses '
          'against agreements/prior-year figures/known variations; review of the Statement of '
          'Profit or Loss and OCI for possible omissions; and variations from industry/local '
          'trends or known trading disturbances (strikes, depot closures, supplier failures).'},
  ]},

  {'n': '7.6', 't': 'Auditing procedures for subsequent events', 'b': [
    {'def': {'t': 'Subsequent event', 'd': 'an event (favourable or unfavourable) occurring '
                  'between the reporting date and the date the financial statements are '
                  'approved by the board of directors.'}},
    {'table': {'align': 'll', 'head': ['Category', 'Definition and examples'], 'rows': [
      ['**Adjusting events**', 'Provide additional evidence of conditions existing at the '
       'reporting date, requiring changes to amounts in the financial statements. Examples: '
       'subsequent determination of purchase price/sale proceeds for assets bought/sold before '
       'year end; a valuation evidencing permanent property value diminution; evidence of '
       'permanent diminution in an unlisted long-term investment; post-date sale proceeds/'
       'evidence about inventory net realisable value; renegotiation of debtor amounts or '
       'debtor insolvency; subsidiary/associate dividend declarations relating to prior '
       'periods; new taxation rate information; insurance claims settled that were in '
       'negotiation at the reporting date; and discovery of errors/fraud showing the financial '
       'statements were incorrect.'],
      ['**Non-adjusting events**', 'Arise after the reporting date, concerning conditions that '
       'did NOT exist at that time — so they do NOT change amounts, but may need disclosure by '
       'way of notes if material enough to affect whether the statements mislead. Examples: '
       'mergers/acquisitions; reconstructions; share/debenture issues; major asset purchases/'
       'sales/losses; opening or closing significant trading activities (if unanticipated); '
       'property/investment value declines confirmed to have occurred after year end; foreign '
       'exchange rate changes; government actions (e.g. nationalisation); strikes/labour '
       'disputes; and pension benefit augmentation.'],
    ]}},
    {'p': 'For each disclosed subsequent event, the notes should state: its nature, and an '
          'estimate of its financial effect (or a statement that estimation is impracticable).'},

    {'h4': 'Auditing procedures'},
    {'p': 'Procedures to identify subsequent events are performed as near as practicable to the '
          'audit report date: enquiring about management\'s own procedures for identifying such '
          'events; reading post-period-end minutes of member/board/audit-committee meetings; '
          'enquiring about matters discussed where minutes are not yet available; reading '
          'interim financial statements, cash flow forecasts and related management reports; '
          'and enquiring directly of management about relevant occurrences.'},
    {'p': 'Specific enquiries might cover: the status of subjective-judgment or preliminary-'
          'data items (e.g. ongoing litigation); new commitments/borrowings/guarantees; asset '
          'sales occurred or planned; new share/debenture issues or merger/liquidation plans; '
          'asset destruction (e.g. fire, flood); developments in risk areas/contingencies; and '
          'events calling into question accounting policies used, including the going concern '
          'presumption.'},

    {'h4': 'Events discovered after the audit report but before the financial statements are '
      'issued'},
    {'key': 'The auditor has **no obligation** to actively enquire about the financial '
            'statements after the audit report date — but management would reasonably be '
            'expected to inform the auditor of material subsequent events discovered before the '
            'statements are actually issued.'},
    {'p': 'If the auditor becomes aware of such an event, they establish whether amendment is '
          'needed, discuss with management, and consider the report\'s implications. Where '
          'management **amends** the statements, the auditor performs necessary additional '
          'procedures, issues a new report dated no earlier than the amended statements\' '
          'approval, and extends procedures to that new date. Where management **does not '
          'amend**, and the report has not yet been released, the auditor issues a **qualified '
          'report**; if the report has already been released, the auditor requests management '
          'not issue the statements — and if they are issued anyway, must act to prevent '
          'reliance on the auditor\'s report (possibly seeking legal advice).'},

    {'h4': 'Events discovered after the financial statements have been issued'},
    {'p': 'If, before the statements are laid before members, the auditor learns of an event '
          'that existed at the report date and would have changed the report had it been known, '
          'the same establish/discuss/consider-implications process applies. Where management '
          '**amends**: the auditor performs necessary procedures, considers stock-exchange '
          'publicity requirements and regulatory communication, reviews management\'s steps to '
          'inform prior recipients, and issues a **new report** — referencing the reason for '
          'amendment (in an explanatory paragraph or the report itself), referencing the '
          'earlier report, and dating the new report no earlier than the amended statements\' '
          'approval. Where management **does not** take these steps and does not amend when '
          'the auditor believes they should, the auditor notifies management that action will '
          'be taken to prevent future reliance on the report, and may need legal advice.'},
  ]},

  {'n': '7.7', 't': 'Audit procedures for contingencies', 'b': [
    {'def': {'t': 'Contingency', 'd': 'a condition existing at the reporting date, whose '
                  'outcome will be confirmed only by the occurrence or non-occurrence of one or '
                  'more uncertain future events. Uncertainties inherent to ordinary accounting '
                  'estimates (asset lives, bad debt amounts, inventory NRV, long-term contract '
                  'outcomes, property/foreign currency valuation) do NOT fall within this '
                  'definition.'}},
    {'key': 'A **material contingent loss** should be **accrued** where it is probable a '
            'future event will confirm a loss estimable with reasonable accuracy at approval '
            'date. A material contingent loss **not** accrued should be **disclosed**, unless '
            'the possibility of loss is remote. **Contingent gains should never be accrued** — '
            'a material contingent gain is only disclosed if realisation is probable, and once '
            'realisation becomes reasonably certain, it stops being a contingency and accrual '
            'becomes appropriate.'},
    {'p': 'Required disclosures for an unaccounted material contingency: its nature; the '
          'uncertainties affecting its ultimate outcome; and a prudent estimate of the '
          'financial effect (or a statement that estimation is impracticable) — for a '
          'contingent loss, the disclosed amount is reduced by any amount already accrued and '
          'any component whose loss possibility is remote (only the **net** amount need be '
          'disclosed), before taking account of taxation, with the taxation implications '
          'explained where needed for proper understanding.'},
    {'p': 'Auditing procedures for contingencies: reviewing the claims-recording system and how '
          'claims reach management/board attention; arrangements for instructing solicitors; '
          'examining board/committee minutes for claim references; examining solicitors\' bills '
          'and correspondence (requesting confirmation of unbilled charges); obtaining a list '
          'of matters referred to solicitors with liability estimates; obtaining written '
          'assurance no other matters exist beyond those disclosed; considering contingencies '
          'from the prior year still applicable; and considering the nature of the client\'s '
          'business for likely contingency types (e.g. warranty claims).'},
  ]},

  {'n': '7.8', 't': 'Audit procedures for the going concern basis', 'b': [
    {'key': 'Financial statements are normally prepared assuming the entity is a **going '
            'concern**, unless stated otherwise. The auditor assesses whether this basis is '
            'appropriate, considers directors\' written assertion on the matter, considers the '
            'adequacy of related disclosures, and factors both into their report.'},
    {'h4': '§7.8.1 Is the client a going concern? Danger symptoms'},
    {'p': 'Checklists of danger symptoms typically include: loan repayments falling due soon '
          'with refinancing not readily available; high/rising gearing; heavy/increasing '
          'reliance on short-term finance (trade credit, overdrafts); inability to take '
          'discounts, slowing creditor payment, or suppliers demanding cash terms; deferred '
          'normal purchases reducing inventory dangerously; substantial losses or declining '
          'profitability; capital expenditure switching to leasing; a net current liability '
          'position or declining current ratio; near-exhausted borrowing limits with no sign of '
          'reduced need; slowing debtor collection; rapid growth risking overtrading; '
          'dependence on a limited number of products/customers/suppliers; major capital '
          'project cancellations; and heavy dependence on an overseas holding company for '
          'finance/trade.'},
    {'p': 'Where such features cause concern, the auditor should at minimum: compare the '
          'client\'s cash flow forecast with available facilities for the next 12 months; '
          'obtain written confirmation from any holding company\'s board of its intention to '
          'support the subsidiary; and enquire into (with written evidence) any corrective '
          'steps the client is taking. If unable to be satisfied the client will continue in '
          'business, the auditor considers the going concern basis\'s validity, and the need '
          'for an appropriately worded qualification.'},

    {'h4': '§7.8.2 Audit evidence'},
    {'p': 'The auditor requests an adequate written assertion from the directors on the going '
          'concern basis\'s appropriateness — assessing adequacy by whether it is supported by '
          'an explanation of relevant matters/assumptions, and whether it considers '
          'circumstances over at least **one year** from the approval date. Absent an adequate '
          'assertion, the auditor considers the effect on the report.'},
    {'p': 'To gain sufficient appropriate evidence, the auditor may examine: systems for timely '
          'identification of future risk warnings; budget/forecast information and the '
          'reliability of the systems producing it; whether the underlying key assumptions '
          'seem appropriate; the sensitivity of budgets/forecasts to controllable and '
          'uncontrollable factors; the existence/adequacy/terms of borrowing facilities and '
          'supplier credit; and directors\' plans for resolving any concerns — considering '
          'whether the plans are realistic and likely to be effectively implemented.'},
    {'p': 'The auditor may need to obtain **independent confirmation** of bank facilities and '
          'assess bankers\' own intentions, particularly where: financial resources have a low '
          'margin; borrowing facilities are due for renewal soon; correspondence reveals the '
          'last renewal was difficult or came with new conditions; cash flow is projected to '
          'deteriorate significantly; security asset values are declining; or borrowing '
          'covenants have been (or may be) breached. Where the auditor cannot satisfy '
          'themselves on this despite deciding it necessary, they consider whether the '
          'inability (and its causes) need disclosure in the financial statements and/or '
          'reference in the audit report.'},
    {'p': 'Situations more likely to indicate a significant going concern concern: liabilities '
          'exceeding assets; default on loan terms or potential covenant breaches, plus '
          'significant liquidity/cash flow problems; major post-reporting-date losses/cash flow '
          'problems threatening continued existence; major litigation whose adverse outcome '
          'would imperil the company; denial/reduction of normal supplier credit terms; major '
          'debt repayments requiring refinancing for continued existence; outcome ranges wide '
          'enough that an unfavourable result affects going concern appropriateness; and '
          'fundamental market/technology changes the company cannot adequately adapt to.'},
    {'note': 'The auditor considers information relating to **beyond** one year from the '
             'approval date, when they become aware of it — discussing its relevance with the '
             'directors.'},

    {'h4': '§7.8.3-7.8.4 Assessing disclosures and reporting'},
    {'p': 'If the going concern basis is inappropriate, this affects how every other '
          'fundamental accounting concept is applied. If disclosures relevant to going concern '
          'appropriateness are inadequate, the auditor carefully considers whether the '
          'statements give a true and fair view, and whether a qualified opinion arising from '
          'disagreement over this disclosure is justified.'},
    {'table': {'align': 'll', 'head': ['Scenario', 'Reporting response'], 'rows': [
      ['Significant concern exists, but the auditor does NOT disagree with the going concern '
       'basis being used.', 'Include an **explanatory paragraph** describing the matters giving '
       'rise to concern, referencing the relevant disclosures (typically under a "Fundamental '
       'Uncertainty: going concern" sub-heading) — this alone does NOT justify qualifying the '
       'report, provided the disclosures are adequate for a true and fair view.'],
      ['The auditor DISAGREES with the going concern presumption itself.', 'Issue a **modified '
       'opinion**, providing whatever additional information is considered necessary — even '
       'adequate disclosure of the reasons cannot, by itself, make the statements true and '
       'fair if the presumption is genuinely inappropriate.'],
      ['Significant concern exists, and disclosures are considered INADEQUATE for a true and '
       'fair view.', 'Issue a **modified opinion** arising from disagreement over the '
       'disclosure of these matters.'],
    ]}},
    {'key': 'Where significant going concern concern exists, the auditor does not normally '
            'regard disclosures as adequate unless the financial statements include: a '
            'statement that they are prepared on the going concern basis; a statement of the '
            'pertinent facts; the nature of the concern; details of the matters giving rise to '
            'it; a statement of the directors\' assumptions (clearly distinguished from the '
            'pertinent facts); where practicable, the directors\' resolution plans; and details '
            'of any relevant actions already taken.'},
    {'note': 'In rare cases, directors may prepare financial statements on a basis **other '
             'than** going concern, to give a true and fair view. If the auditor considers this '
             'appropriate and the necessary disclosures are present, they include an '
             'explanatory paragraph describing the basis of preparation and referencing the '
             'relevant notes.'},
  ]},

  {'n': '7.9', 't': 'Quality control for audit work', 'b': [
    {'key': 'Auditors urgently need internal quality control programmes — to improve client '
            'service, improve practice efficiency/profitability, and minimise exposure to '
            'legal liability risk. Every auditor should establish, maintain and **communicate** '
            'appropriate procedures, designed to ensure: staff associated with audit work are '
            '**fit and proper persons**; independence, resource availability and audit '
            'capability are considered before accepting/re-accepting an appointment; all '
            'principals/employees adhere to independence and confidentiality principles; and '
            'appropriate professional consultation and competence levels are maintained.'},
    {'p': 'Quality control operates at **two levels**: the audit firm, and the individual '
          'audit assignment.'},

    {'h4': '§7.9.1 Quality control at the firm level'},
    {'p': 'Firms establish policies/procedures ensuring all audits follow appropriate '
          'standards, communicated to personnel to provide confidence they are understood and '
          'implemented (including any specifically required by the relevant supervisory '
          'body\'s regulations). The nature/extent depends on practice size, geographic '
          'dispersion, organisation and cost-benefit considerations. Policies ordinarily '
          'incorporate:'},
    {'ol': [
      '**Professional requirements** — personnel adhering to independence, integrity, '
      'objectivity, confidentiality and professional behaviour;',
      '**Skills and competence** — personnel attaining and maintaining the required technical '
      'standards and professional competence;',
      '**Acceptance and retention of clients** — evaluating prospective clients and reviewing '
      'existing ones on an ongoing basis, considering independence, ability to serve properly, '
      'and management\'s integrity;',
      '**Assignment** — work assigned to personnel with the required technical training/'
      'proficiency;',
      '**Delegation** — sufficient delegation, supervision and review at every level;',
      '**Consultation** — occurring, when necessary, with appropriately expert persons within '
      'or outside the firm; and',
      '**Monitoring** — the continued adequacy and operational efficiency of the policies '
      'themselves being monitored.',
    ]},

    {'h4': '§7.9.2 Quality control at the individual assignment level'},
    {'p': 'The engagement partner applies the firm\'s policies as appropriate to each '
          'assignment. Delegated work must be **directed, supervised and reviewed** to provide '
          'confidence it is performed competently — with the required extent of each depending '
          'on the assistant\'s professional competence.'},
    {'table': {'align': 'll', 'head': ['Element', 'What it involves'], 'rows': [
      ['**Direction**', 'Informing assistants of their responsibilities and the objectives of '
       'the procedures they perform — communicated via the audit programme, time budgets and '
       'the overall audit plan.'],
      ['**Supervision**', 'Monitoring the audit\'s progress (assistants\' skill adequacy, work '
       'consistency with the plan/programme); becoming informed of and addressing significant '
       'accounting/auditing questions, modifying the plan/programme as needed; and resolving '
       'professional-judgment differences among personnel, considering the appropriate level '
       'of consultation.'],
      ['**Review**', 'Work by each assistant is reviewed by personnel of **at least equal '
       'competence**, checking: adherence to the audit programme; adequate documentation of '
       'work and results; resolution (or proper reflection) of significant audit matters; and '
       'that procedure objectives were achieved and conclusions are consistent with, and '
       'supported by, the work performed. Reviewed on a timely basis: the overall plan and '
       'programme; inherent/control risk assessments and any resulting modifications; '
       'documentation of substantive-procedure evidence and conclusions (including '
       'consultations); and the financial statements, proposed adjustments and proposed '
       'report.'],
    ]}},
    {'note': 'For large, complex audits, the pre-issuance review process may include requesting '
             'personnel **not otherwise involved** in the audit to perform additional '
             'procedures — e.g. reading the annual report, or considering specific areas of '
             'audit judgment.'},
  ]},

  {'n': '7.10', 't': 'Chapter summary', 'b': [
    {'ol': [
      'The sampling process and practices help auditors determine and identify the various '
      'ways of selecting items for testing.',
      'Sampling enables the auditor to gather sufficient appropriate audit evidence from the '
      'population of transactions that occurred during the year.',
      'The effects and differences between statistical and non-statistical sampling '
      'techniques enable the auditor to determine the strategy and choice of elements for '
      'testing.',
      'Errors in the choice of samples can be evaluated with the knowledge gained at this '
      'stage.',
      'Substantive procedures enable the auditor to conduct tests of details of transactions '
      'and relevant analytical procedures.',
      'Analytical procedures ease the comparison of various indicators to establish '
      'expectations.',
      'Audit programmes enable the auditor to establish the procedure for tests of details, '
      'and assign functions easily to assistants — a knowledgeable assistant or accountant '
      'using the audit programme can readily perform audit assignments.',
      'Verification procedures establish the cost, authorisation, valuation, existence, '
      'beneficial ownership and presentation of assets and liabilities.',
      'Entities are evaluated for their survival and continued existence as a going concern — '
      'the auditor uses information even after year end to evaluate this.',
      'Firms set up procedures to strengthen their operations by instilling measures in their '
      'systems to guard against risk and ensure the delivery of desirable quality services.',
    ]},
  ]},

  {'n': '7.11', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'p': 'The study text closes the chapter with 10 questions — 5 multiple-choice and 5 '
          'short-answer — reproduced below in full with the official answers, each explained. The '
          'Auditing study text sets **no examination-type questions**; this bank is the whole of '
          'its end-of-chapter material.'
},
    {'eg': {'tag': 'Study text', 't': 'The questions, with the official answers', 'open': True, 'q': [
      {'ol': [
        'All those tests of transactions and balances, and other procedures such as analytical '
        'review, which seek to obtain audit evidence as to the completeness, accuracy and '
        'validity of all records is known as ……… (A) Substantive test; (B) Compliance test; (C) '
        'Walk-through test; (D) Depth test; (E) Random test.',
        'Those tests which seek to provide audit evidence that internal control procedures are '
        'being applied as prescribed are known as (A) Audit evidence; (B) Substantive tests; (C) '
        'Compliance tests; (D) Procedural tests; (E) Investigating tests.',
        'Which of the following tends to be most predictable for the purpose of analytical '
        'procedures applied as substantive tests? (A) Relationships involving statement of '
        'financial position accounts; (B) Transactions subject to management discretion; (C) '
        'Relationships involving income statement accounts; (D) Data subject to audit testing in '
        'the prior year; (E) Comparison of certificates of balance in the prior year.',
        'An auditor wishes to perform tests of controls on cash disbursement procedures. If the '
        'controls leave no audit trail of documentary evidence, the auditor will most likely test '
        'the procedures by ……… (A) Inquiry and analytical procedures; (B) Confirmation and '
        'observations; (C) Analytical procedures and confirmation; (D) Observation and enquiry; '
        '(E) Comparison and confirmation.',
        'A sample selection method where each item of the population has an equal chance of being '
        'selected is known as ……… (A) Stratified sampling; (B) Multistage sampling; (C) Random '
        'sampling; (D) Discovery sampling; (E) Judgmental sampling.',
        'State **two** stages in statistical sampling as an auditing tool.',
        'The risk that a material misstatement could occur in an account balance or class of '
        'transactions and not be detected by the accounting or internal control system is known '
        'as ………',
        'The risk that the auditor will draw an invalid conclusion from his audit procedures is '
        'called ………',
        'Selecting a sample of appropriate size on the basis of the auditor’s judgment of what is '
        'desirable is called ………',
        'A sampling technique where each item of the population has an equal chance of being '
        'selected is called ………',
      ]}],
      'a': [
      {'ol': [
        '**A** — substantive tests. They test the **figures themselves**; compliance tests (also '
        'called tests of control) test whether the **controls** operated.',
        '**C** — compliance tests (tests of control).',
        '**C** — relationships involving **income statement** accounts. Income statement items '
        'represent transactions over a period and tend to follow stable relationships (gross '
        'margin, wages to hours, commission to sales); statement of financial position items are '
        'balances at a single date and are far more volatile, and items subject to **management '
        'discretion** are by definition unpredictable.',
        '**D** — observation and enquiry. Where a control leaves no document behind — segregation '
        'of duties, for example, or a supervisor’s scrutiny — there is nothing to inspect, so the '
        'auditor must **watch it happening** and **ask** those who operate it.',
        '**C** — random sampling. It is the defining feature of a **statistical** sample, and it '
        'is what permits the result to be projected over the population with a measurable '
        'confidence level.',
        '**Any two of:** planning the sample; selecting the items to be tested; testing the '
        'items; evaluating the results of the test.',
        '**Control risk.**',
        '**Audit risk** *(the study text’s answer)*. More precisely this describes **detection '
        'risk** — the risk that the auditor’s own procedures fail — which is one of the three '
        'components of audit risk.',
        '**Judgment sampling** (non-statistical sampling).',
        '**Random sampling.**',
      ]}]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'This is the longest, most procedurally dense chapter in the subject — resist the '
   'temptation to memorise every audit-programme bullet; the exam tests concepts and '
   'definitions far more than exhaustive checklists. Prioritise: the statistical-sampling '
   'definition (random selection AND probability-theory evaluation — both required); the two '
   'directions of sampling risk and which affects effectiveness vs. efficiency; positive vs. '
   'negative confirmation logic (already met in Chapter 6, reapplied here to debtors); the '
   'CAVEBOP-style verification objectives; why inventory is uniquely hard to verify (the '
   'one-to-one profit effect, and being the only account not arising from double entry); the '
   'adjusting vs. non-adjusting subsequent event distinction; when a contingent loss is '
   'accrued vs. merely disclosed vs. ignored (and the asymmetric treatment of contingent '
   'gains); and the three going-concern reporting outcomes (explanatory paragraph only vs. '
   'two distinct grounds for a modified opinion).',
 'errors': [
   'Treating "random selection" alone as sufficient for statistical sampling — the definition '
   'requires BOTH random selection AND the use of probability theory to evaluate results '
   '(including measuring sampling risk); either alone makes it non-statistical.',
   'Confusing the two directions of sampling risk — concluding things are BETTER than reality '
   '(an effectiveness risk, more likely to cause a wrong opinion) is a different, more '
   'dangerous risk than concluding things are WORSE than reality (an efficiency risk, causing '
   'wasted extra work).',
   'Assuming selecting "specific items" (e.g. all balances over a threshold) counts as audit '
   'sampling — it explicitly does not, and results from it cannot be projected to the whole '
   'population.',
   'Accruing a contingent GAIN the way a contingent loss is accrued — gains are never accrued '
   'while still contingent; only disclosed if probable, and only actually accrued once '
   'realisation is reasonably certain (at which point it is no longer a contingency at all).',
   'Believing inadequate going-concern disclosure can be fixed with only an explanatory '
   'paragraph — an explanatory paragraph is the response when disclosures ARE adequate; '
   'inadequate disclosure requires a modified opinion instead.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'All those tests of transactions and balances and other procedures such as analytical '
         'review which seek to obtain audit evidence as to the completeness, accuracy and '
         'validity of all records is known as',
    'o': ['Substantive test', 'Compliance test', 'Walk-through test', 'Depth test', 'Random '
          'test'],
    'a': 0,
    'w': 'Substantive tests are precisely defined as procedures seeking evidence on the '
    'completeness, accuracy and validity of the accounting records themselves — distinct from '
    'compliance tests, which check whether CONTROL procedures are being followed.',
    'src': 'Chapter 7.2', 'sec': '7.2'},
   {'q': 'Those tests which seek to provide audit evidence that internal control procedures '
         'are being applied as prescribed are known as',
    'o': ['Audit evidence', 'Substantive tests', 'Compliance tests', 'Procedural tests',
          'Investigating tests'],
    'a': 2,
    'w': 'Compliance tests (tests of controls) specifically verify that prescribed control '
    'procedures are actually being applied — the auditing-terminology counterpart to '
    'substantive tests, which verify the records themselves.',
    'src': 'Chapter 7.1', 'sec': '7.1'},
   {'q': 'Which of the following tends to be most predictable for the purpose of analytical '
         'procedures applied as substantive tests?',
    'o': ['Relationship involving statement of financial position accounts', 'Transactions '
          'subject to management discretion', 'Relationship involving income statement '
          'accounts', 'Data subject to audit testing in the prior year', 'Comparison of '
          'certificate of balance in prior year'],
    'a': 2,
    'w': 'Income statement (flow) relationships — such as gross margin percentages — tend to '
    'follow predictable patterns period to period, making them more suitable for analytical '
    'procedures than point-in-time balance sheet accounts or discretionary items.',
    'src': 'Chapter 7.5', 'sec': '7.5'},
   {'q': 'An auditor wishes to perform tests of controls on cash disbursement procedures. If '
         'the controls leave no audit trail of documentary evidence, the auditor most likely '
         'will test the procedures by',
    'o': ['Inquiry and analytical procedures', 'Confirmation and observations', 'Analytical '
          'procedures and confirmation', 'Observation and enquiry', 'Comparison and '
          'confirmation'],
    'a': 3,
    'w': 'With no documentary trail to inspect or vouch, the only remaining ways to test that a '
    'control actually operates are to directly OBSERVE it being performed and to ENQUIRE of '
    'those who perform it.',
    'src': 'Chapter 7.1', 'sec': '7.1'},
   {'q': 'A sample selection method where each item of the population has an equal chance of '
         'being selected is known as',
    'o': ['Stratified sampling', 'Multistage sampling', 'Random sampling', 'Discovery '
          'sampling', 'Judgmental sampling'],
    'a': 2,
    'w': 'Random sampling is defined precisely by this property — every item having an equal '
    'chance of selection, e.g. via random number tables.',
    'src': 'Chapter 7.1', 'sec': '7.1'},
  ],
  'theory': [
   {'q': 'Distinguish between adjusting and non-adjusting subsequent events, giving one '
         'example of each, and state what the financial statement notes should disclose for a '
         'disclosable subsequent event.',
    'marks': 6,
    'a': [
      {'p': '**Adjusting events** provide additional evidence of conditions that existed at '
            'the reporting date, and require the financial statements\' amounts to be '
            'changed — e.g. the subsequent determination of the sale proceeds of an asset sold '
            'before year end.'},
      {'p': '**Non-adjusting events** arise after the reporting date and concern conditions '
            'that did NOT exist at that time — they do not change reported amounts, but may '
            'need note disclosure if material enough to affect whether the statements mislead '
            '— e.g. a merger or acquisition occurring after year end.'},
      {'p': 'For a disclosable event, the notes should state: the nature of the event, and an '
            'estimate of its financial effect (or a statement that such an estimate is not '
            'practicable to make).'},
    ], 'src': 'Chapter 7.6', 'sec': '7.6'},
   {'q': 'Explain the accounting treatment of a material contingent loss and a material '
         'contingent gain, and state why they are NOT treated symmetrically.',
    'marks': 6,
    'a': [
      {'p': 'A material contingent **loss** should be **accrued** if it is probable that a '
            'future event will confirm the loss and it can be estimated with reasonable '
            'accuracy. If not accrued, it should be **disclosed** unless the possibility of '
            'loss is remote.'},
      {'p': 'A material contingent **gain** should **never be accrued** while it remains a '
            'contingency — it should only be **disclosed** if realisation is probable. Once '
            'realisation becomes reasonably certain, the item is no longer treated as a '
            'contingency at all, and accrual becomes appropriate.'},
      {'p': 'The asymmetry reflects accounting prudence: recognising a possible loss early '
            'protects users from overstated profit/assets, while recognising a possible gain '
            'early would risk overstating profit/assets based on an outcome that has not yet '
            'been confirmed.'},
    ], 'src': 'Chapter 7.7', 'sec': '7.7'},
  ]},
}
