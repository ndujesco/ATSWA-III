CH = {
 'n': 6,
 't': 'Interlocking and Integrated Accounts',
 'brief': 'The double-entry side of cost accounting: how cost transactions are posted to the '
          'cost ledger under an interlocking system (kept separate from the financial ledger, '
          'reconciled periodically) versus an integrated system (one unified set of accounts); '
          'why costing profit and financial profit differ, and how to reconcile them with a '
          'memorandum reconciliation account; accounts classification and codes; and computer-'
          'assisted costing techniques. Every ledger account in every illustration is written '
          'out in full, in T-account form, and every figure independently re-derived.',
 'outcomes': [
   'Post cost accounting transactions into the appropriate books of account',
   'Apply double-entry principles in cost accounting',
   'Differentiate between "interlocking accounts" and "integrated accounts"',
   'Reconcile the financial accounting profit and the cost accounting profit',
   'Design accounts codes in a summarised and suitable form for effective management of assets',
   'Explain the application of computer-assisted techniques',
 ],
 'secs': [

  # ------------------------------------------------------------------ 6.1
  {'n': '6.1', 't': 'Introduction', 'b': [
    {'def': {'t': 'Bookkeeping', 'd': 'identifying, recording and summarising transactions in '
                  'the appropriate books of account. The balances obtained at the end of an '
                  'accounting period are extracted to the **trial balance**, which is simply a '
                  'list of balances, both debit and credit.'}},
    {'p': 'The system of bookkeeping is **not restricted to financial accounting** — it applies '
          'to cost accounting too. Both financial and cost accounting data must be properly kept '
          'and processed to develop and produce the information management needs for decision '
          'making.'},
    {'p': 'The **size of a business** normally determines how complex its cost records are:'},
    {'ul': [
      '**Small businesses** keep simple records, not linked to the financial accounts.',
      '**Larger businesses** maintain a full set of cost accounts, which provide the detail '
      'behind the totals shown in the financial accounts.',
    ]},
    {'p': 'From that follow the two ways of organising the records, and this chapter explains '
          'both:'},
    {'table': {'align': 'll', 'head': ['System', 'How it works'], 'rows': [
      ['**Interlocking**', 'Cost accounts are kept **independent** of the financial accounts, '
       'so **periodic reconciliation is necessary**.'],
      ['**Integrated (integral)**', 'The cost accounts form part of the formal accounting '
       'system — financial and cost accounting are **combined**, generating a **single profit** '
       'figure, and **no reconciliation is necessary**.'],
    ]}},
    {'key': 'The study text states plainly that the integrated method is **the more '
            'satisfactory** of the two, because it avoids duplication of effort and avoids '
            'reconciliation problems altogether. Interlocking survives mainly where the cost '
            'department and the financial department are genuinely separate functions, or where '
            'the costing system must be free to value inventory on a basis the financial '
            'accounts are not allowed to use.'},
    {'p': 'This chapter therefore focuses on two things: the **double-entry aspect of cost '
          'accounting**, and the **reconciliation** needed between cost accounts and financial '
          'accounts when the two are maintained separately. Reconciliation is required only '
          'where a firm adopts an interlocking system; where the integral system is maintained, '
          'both systems are combined and generate one profit.'},
  ]},

  # ------------------------------------------------------------------ 6.2
  {'n': '6.2', 't': 'Interlocking accounting system and cost ledger', 'b': [
    {'p': 'An interlocking accounting system uses **separate cost accounts**, which are '
          'periodically reconciled with the financial accounts. The cost accountant uses a great '
          'deal of the same financial information available to the financial accountant:'},
    {'ul': [
      'the purchases daybook;', 'the expenses daybook;', 'the payroll;', 'the main journal;',
      'the sales daybook; and the like.',
    ]},
    {'p': 'The **structure** of the interlocking system in any organisation is determined by the '
          'volume of its business transactions. The cost accounting records usually kept include '
          'those of:'},
    {'ul': [
      '**cost elements** (materials, labour, expenses);',
      '**cost centres** — production, marketing, and general administration;',
      '**job costs** — production jobs, repair jobs, capital jobs; and',
      '**inventory** — raw materials, components or spare parts, and finished goods.',
    ]},
    {'h4': 'How the two systems are "interlocked"'},
    {'p': 'The interlocking of the two systems is carried out by the use of two mirror-image '
          'control accounts:'},
    {'ol': [
      '**Cost ledger control account** — kept in the **financial ledger**;',
      '**Financial ledger control account** — kept in the **cost ledger**.',
    ]},
    {'key': 'These two accounts are the hinge of the whole system, and the names are a common '
            'source of confusion because the study text (and the exam) uses several of them '
            'interchangeably. The account sitting **inside the cost ledger** that absorbs every '
            'posting touching something outside costing is called, variously, the **Financial '
            'Ledger Control Account**, the **Cost Ledger Contra Account**, the **General Ledger '
            'Adjustment Account**, or — confusingly — the **Cost Ledger Control Account**. When '
            'a question names any of these, it means the same single account: the one that keeps '
            'the cost ledger self-balancing.'},
  ]},

  # ------------------------------------------------------------------ 6.3
  {'n': '6.3', 't': 'The cost ledger', 'b': [
    {'p': 'In an interlocking cost accounting system, the **cost ledger is the principal '
          'ledger**. Generally, it will contain:'},
    {'ol': [
      '**Control accounts** for stores, work-in-progress, finished goods and overhead. Each '
      'control account is supported by a **subsidiary ledger** providing the detail needed for '
      'accounting control and the preparation of information.',
      '**Accounts for wages, sales and cost of sales**, together with any other account the cost '
      'bookkeeping system needs — e.g. notional charges, suspense accounts.',
      '**Cost Ledger Contra Account** (also called the General Ledger Adjustment Account or the '
      'Cost Ledger Control Account). This account is needed to **maintain the double-entry '
      'principle** within the cost ledger. It contains postings which affect accounts *outside* '
      'the costing system — e.g. debtors, creditors or cash accounts, and other real and '
      'personal account transactions.',
    ]},
    {'note': 'Why the contra account must exist at all: the cost ledger only holds cost '
             'accounts. When raw materials are bought, the debit (Raw Materials Control) sits in '
             'the cost ledger, but the credit belongs to the supplier — a personal account that '
             'lives in the *financial* ledger. The cost ledger would therefore have a debit with '
             'no matching credit. The Cost Ledger Contra Account supplies that missing credit, '
             'so the cost ledger balances on its own and can produce its own trial balance.',
     'lbl': 'Why the contra account exists'},
    {'h4': 'The work-in-progress ledger is the focal point'},
    {'p': 'The focal point of the cost accounting system is the **work-in-progress ledger**. In '
          'an organisation that operates specific-order costing, that ledger contains a '
          '**separate account for each job**. Each job account is debited with:'},
    {'ul': [
      'the cost of **material used**;', 'the **wages allocated**; and',
      'the **production overhead absorbed**.',
    ]},
    {'p': 'When jobs are completed, the cost of completed jobs is transferred to the **Finished '
          'Goods Ledger**. When a job is delivered to the customer, **Cost of Sales** is debited '
          'with the job cost and **Sales** is credited with the selling price. A (costing) '
          'profit and loss statement can then be prepared and analysed **job by job**. The '
          'balances on the control accounts represent the cost value of stores, work-in-progress '
          'and finished goods.'},
    {'note': 'The term **"control" account** implies that a subsidiary ledger is kept behind it. '
             'Entries to control accounts represent **summary postings** — the individual '
             'detail lives in the subsidiary ledger, not in the control account itself.'},
  ]},

  # ------------------------------------------------------------------ 6.4
  {'n': '6.4', 't': 'Cost accounting entries under the interlocking system', 'b': [
    {'p': 'The relevant entries, in the order the study text gives them, running from raw '
          'material purchase through to output achieved:'},
    {'table': {'align': 'lll', 'head': ['#  Transaction', 'Debit', 'Credit'], 'rows': [
      ['**1** Raw material incurred (purchased)', 'Raw Material Control A/c **or** Stores Ledger '
       'Control A/c', 'Cost Ledger Control A/c **or** General Ledger Adjustment A/c **or** Cost '
       'Ledger Contra A/c'],
      ['**2** Materials returned to suppliers', 'Cost Ledger Control A/c **or** General Ledger '
       'Adjustment A/c', 'Raw Materials Control A/c **or** Stores Ledger Control A/c'],
      ['**3** Material issued — direct', 'Work-in-Progress Control A/c (WIP)',
       'Raw Materials Control A/c'],
      ['**3** Material issued — indirect (to factory)', 'Production Overhead Control A/c (POCA)',
       'Raw Materials Control A/c'],
      ['**4** Wages incurred', 'Wages Control A/c (WCA)', 'Cost Ledger Control A/c'],
      ['**5** Wages allocated — direct', 'Work-in-Progress Control A/c', 'Wages Control A/c'],
      ['**5** Wages allocated — indirect (to factory)', 'Production Overhead Control A/c',
       'Wages Control A/c'],
      ['**6** Production overhead absorbed', 'WIP Control A/c',
       'Production Overhead Control A/c'],
      ['**7** Output achieved (jobs completed)', 'Finished Goods A/c', 'WIP Control A/c'],
    ]}},
    {'warn': 'The study text prints entry 5 as "Debit WIP (direct); Debit Production Overhead '
             '(indirect to factory); **Credit Cost Ledger Control Account**." That credit is '
             'wrong. Wages were already brought into the cost ledger by entry 4 (Dr Wages '
             'Control, Cr Cost Ledger Control); entry 5 merely *allocates* that balance out of '
             'the Wages Control Account, so the credit must be to **Wages Control**. Crediting '
             'Cost Ledger Control twice would double-count the wages. The table above shows the '
             'corrected entry, and Illustration 6.1 below confirms it — its own Production Wages '
             'Control Account is credited with N99,000 to WIP and N18,000 to Production '
             'Overhead.', 'lbl': 'Error in the study text, corrected'},
    {'note': 'An **adjustment entry** is always made for the under- or over-absorption of '
             'overhead (see §5.7). Once WIP has been debited with the *absorbed* amount, '
             'whatever balance is left on the Production Overhead Control Account is the '
             'under/over absorption, and it is written off to the costing Profit and Loss '
             'Account — debited there if under-absorbed, credited there if over-absorbed.'},
    {'key': 'A reliable way to read any of these entries: **the cost ledger only ever talks to '
            'the outside world through the Cost Ledger Contra Account.** If a transaction brings '
            'something *into* the cost ledger from outside (purchases, wages paid, overhead '
            'incurred, sales value), the contra account is the credit. If it sends something '
            '*out* (returns to suppliers, sales value transferred, a completed capital job), the '
            'contra account is the debit. Every other entry in the list is an internal transfer '
            'between two cost accounts.'},

    # ---------------------------------------------------------- Illustration 6.1
    {'eg': {'tag': 'Study text — Illustration 6.1 (Adapted from ACCA)',
      't': 'Completing an interlocking cost ledger, the costing profit, and the trial balance',
      'open': True, 'q': [
      {'p': 'Below are **incomplete accounts in the cost ledger** of a manufacturing business '
            'for a period in which final accounts are to be prepared. The missing entries are '
            'labelled (i) to (ix).'},
      {'tacc': {'t': 'Raw Materials Control Account / Stores Ledger Control A/c',
        'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Bal. b/f', 8000], ['Cost ledger contra', 110000], ['', 118000, '@tot']],
        'cr': [['Work-in-Progress', 90000], ['Production overhead  **(i)**', '?'],
               ['Bal. c/d', '?']]}},
      {'tacc': {'t': 'Work-in-Progress Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Bal. b/f', 7000], ['Raw materials control', 90000],
               ['Wages control  **(ii)**', '?'], ['Production OH control  **(iii)**', '?']],
        'cr': [['Finished goods  **(iv)**', '?'], ['Bal. c/d', '?']]}},
      {'tacc': {'t': 'Finished Goods Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Bal. b/f', 30000], ['W.I.P. control  **(iv)**', '?']],
        'cr': [['Cost of sales  **(v)**', '?'], ['Bal. c/d', '?']]}},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Raw materials control  **(i)**', '?'], ['Wages control  **(vi)**', '?'],
               ['Cost ledger contra', 46000]],
        'cr': [['W.I.P. control  **(iii)**', '?']]}},
      {'tacc': {'t': 'Production Wages Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cost ledger contra', 117000]],
        'cr': [['W.I.P. control  **(ii)**', '?'], ['Production overhead  **(vi)**', '?']]}},
      {'tacc': {'t': 'Marketing and Administration Overhead Control Account',
        'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cost ledger contra', 50000]], 'cr': [['Cost of sales  **(vii)**', '?']]}},
      {'tacc': {'t': 'Cost of Sales Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Finished goods control  **(v)**', '?'],
               ['Marketing & admin OH  **(vii)**', '?']],
        'cr': [['Profit & Loss', '?']]}},
      {'tacc': {'t': 'Sales Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Profit & Loss', 300000]], 'cr': [['Cost ledger contra  **(viii)**', '?']]}},
      {'tacc': {'t': 'Cost Ledger Contra Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Sales  **(viii)**', '?'], ['Bal. c/d', '?']],
        'cr': [['Bal. b/f  **(ix)**', '?'], ['Raw materials control', 110000],
               ['Production OH control', 46000], ['Production wages control', 117000],
               ['Marketing & admin OH', 50000]]}},
      {'p': '**You are given the following additional information:**'},
      {'table': {'align': 'lr', 'head': ['(a)  The closing inventory balances are:', 'N'],
        'rows': [
        ['Raw materials control', '18,000'],
        ['Work-in-progress control', '68,000'],
        ['Finished goods control', '45,000'],
      ]}},
      {'ul': [
        '**(b)** The ratio of direct wages incurred to indirect wages is **11 : 2**.',
        '**(c)** Marketing and administration overhead is absorbed by jobs on the basis of '
        '**25% of the cost of goods sold**.',
        '**(d)** Production overhead is absorbed on the basis of **N3.50 per direct labour '
        'hour**. During the period, total direct labour hours worked were **22,000**.',
      ]},
      {'p': '**Required:**'},
      {'ol': [
        'Identify the transactions indicated by the accounting entries numbered (i) to (viii).',
        'Complete the cost accounts for the period.',
        'Compute the cost accounting profit for the period.',
        'Prepare a trial balance as at the end of the period.',
      ]},
      {'warn': 'Four defects in the study text\'s own printing of this question have been '
               'corrected above, each verified against the text\'s own solution. **(1)** The '
               'Production Overhead Control Account is printed with "Cost Ledger Control '
               'N117,000" and the Production Wages Control Account with "Cost Ledger contra '
               'N46,000" — the two figures are **swapped**; the solution uses N46,000 in '
               'production overhead and N117,000 in production wages. **(2)** The Raw Materials '
               'Control Account is printed with "Work-in-progress 9,000"; it is **N90,000** (a '
               'dropped zero — otherwise the account cannot total N118,000). **(3)** In the Cost '
               'Ledger Contra Account the labels are printed one row out of step with the '
               'figures. **(4)** The "Required" says entries "(i) to (vi)" while the solution '
               'identifies **eight** of them, (i) to (viii), and a ninth, (ix), in the workings.',
       'lbl': 'Source errors corrected'},
      ],
      'a': [
      {'h4': '(a)  Identifying the transactions'},
      {'table': {'align': 'll', 'head': ['Entry', 'The transaction it represents'], 'rows': [
        ['**(i)**', 'Issue of **indirect materials** to production'],
        ['**(ii)**', '**Direct wages** allocated'],
        ['**(iii)**', '**Production overhead absorbed**'],
        ['**(iv)**', '**Finished goods produced** during the period, transferred from the WIP '
         'Control Account'],
        ['**(v)**', '**Cost of goods sold** during the period'],
        ['**(vi)**', '**Indirect wages** allocated'],
        ['**(vii)**', '**Marketing and administration overhead absorbed**'],
        ['**(viii)**', '**Value of sales** during the period'],
        ['**(ix)**', '*(from the workings)* **Opening balance of the Cost Ledger Contra '
         'Account**'],
      ]}},

      {'h4': 'Workings — every missing figure, derived'},
      {'p': '**(a) Splitting the production wages (entries ii and vi).** Total production wages '
            'incurred = N117,000 (the debit already shown in the Production Wages Control '
            'Account), and the ratio of direct to indirect wages is 11 : 2, so there are '
            '$11+2=13$ parts in total:'},
      {'tex': '\\text{Direct wages (ii)} \\;=\\; \\frac{11}{13} \\times 117{,}000 '
              '\\;=\\; N99{,}000'},
      {'tex': '\\text{Indirect wages (vi)} \\;=\\; \\frac{2}{13} \\times 117{,}000 '
              '\\;=\\; N18{,}000'},
      {'note': 'Check: $99{,}000 + 18{,}000 = 117{,}000$ ✓ — always add the two parts back to '
               'the total before using them.'},
      {'p': '**(b) Production overhead absorbed (entry iii).** The absorption rate is N3.50 per '
            'direct labour hour and 22,000 hours were worked:'},
      {'tex': '\\text{Production overhead absorbed (iii)} \\;=\\; 22{,}000 \\times 3.50 '
              '\\;=\\; N77{,}000'},
      {'p': '**(c) Indirect materials issued to production (entry i).** The Raw Materials '
            'Control Account must balance, so the indirect issue is whatever is left after the '
            'direct issue and the closing inventory are taken out of the materials available:'},
      {'stmt': {'t': 'Indirect materials issued — by difference', 'rows': [
        ['Total raw materials available (8,000 b/f + 110,000 purchased)', '', 118000],
        ['Less:  Direct materials issued', 90000, ''],
        ['          Closing inventory of raw materials', 18000, 108000],
        ['**Indirect materials issued to production  (i)**', '', 10000, '@tt'],
      ]}},
      {'p': '**(d) Value of finished goods produced (entry iv).** Everything debited to WIP, '
            'less what is still in WIP at the end:'},
      {'tex': '\\text{(iv)} = N(7{,}000 + 90{,}000 + 99{,}000 + 77{,}000 - 68{,}000) '
              '= N205{,}000'},
      {'note': 'In words: opening WIP + direct materials + direct wages + overhead absorbed − '
               'closing WIP. This is the standard "cost of goods manufactured" identity, solved '
               'as a balancing figure on the WIP account.'},
      {'p': '**(e) Cost of goods sold (entry v).** The same identity, one account further on:'},
      {'tex': '\\text{(v)} = N(30{,}000 + 205{,}000 - 45{,}000) = N190{,}000'},
      {'p': '**(f) Marketing and administration overhead absorbed (entry vii)** = 25% of the '
            'cost of goods sold:'},
      {'tex': '\\text{(vii)} = 25\\% \\times N190{,}000 = N47{,}500'},
      {'p': '**(g) Opening balance of the Cost Ledger Contra Account (entry ix).** It is the net '
            'sum of all the opening balances — the contra account is, by construction, the '
            'mirror of everything the cost ledger holds:'},
      {'table': {'align': 'lrlr', 'head': ['', 'Dr (N)', '', 'Cr (N)'], 'rows': [
        ['Raw materials control', '8,000', '', ''],
        ['WIP control', '7,000', '', ''],
        ['Finished goods control', '30,000', 'Cost Ledger Contra', '45,000'],
        ['**Total**', '**45,000**', '', '**45,000**'],
      ]}},

      {'h4': '(b)  The completed accounts'},
      {'tacc': {'t': 'Raw Materials Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Bal. b/f', 8000], ['Cost Ledger Contra', 110000], ['', 118000, '@tot'],
               ['Bal. b/d', 18000]],
        'cr': [['Work-in-progress', 90000], ['Production OH  (i)', 10000], ['Bal. c/d', 18000],
               ['', 118000, '@tot']]}},
      {'tacc': {'t': 'Work-in-Progress Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Bal. b/f', 7000], ['Raw materials control', 90000],
               ['Wages control  (ii)', 99000], ['Production OH control  (iii)', 77000],
               ['', 273000, '@tot'], ['Bal. b/d', 68000]],
        'cr': [['Finished goods  (iv)', 205000], ['Bal. c/d', 68000], ['', 273000, '@tot']]}},
      {'tacc': {'t': 'Finished Goods Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Bal. b/f', 30000], ['W.I.P. control  (iv)', 205000], ['', 235000, '@tot'],
               ['Bal. b/d', 45000]],
        'cr': [['Cost of sales  (v)', 190000], ['Bal. c/d', 45000], ['', 235000, '@tot']]}},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Raw materials control  (i)', 10000], ['Wages control  (vi)', 18000],
               ['Cost Ledger Contra', 46000], ['Profit & Loss (over-absorbed)', 3000],
               ['', 77000, '@tot']],
        'cr': [['W.I.P. control  (iii)', 77000], ['', 77000, '@tot']]}},
      {'note': 'This is the one account most candidates get wrong. Production overhead '
               '**incurred** is $10{,}000 + 18{,}000 + 46{,}000 = N74{,}000$, but N77,000 was '
               '**absorbed** into WIP — so overhead has been **over-absorbed by N3,000**. The '
               'debit of N3,000 shown above is what makes the account balance, and the matching '
               'credit goes to the costing Profit and Loss Account, *increasing* profit. Do not '
               'assume that because the absorbed figure (N77,000) happens to equal the Marketing '
               'and Admin cost ledger entry, or any other figure on the page, there is no '
               'under/over absorption — always total the debits actually incurred.',
       'lbl': 'Over-absorption of N3,000 — where it comes from'},
      {'tacc': {'t': 'Production Wages Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cost Ledger Contra', 117000], ['', 117000, '@tot']],
        'cr': [['W.I.P. control  (ii)', 99000], ['Production overhead  (vi)', 18000],
               ['', 117000, '@tot']]}},
      {'tacc': {'t': 'Marketing and Administration Overhead Account',
        'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cost Ledger Contra', 50000], ['', 50000, '@tot']],
        'cr': [['Cost of sales  (vii)', 47500], ['Profit & Loss (under-absorbed)', 2500],
               ['', 50000, '@tot']]}},
      {'note': 'The mirror image of the production overhead account: N50,000 incurred but only '
               'N47,500 absorbed, so marketing and administration overhead is **under-absorbed '
               'by N2,500**, which is *debited* to the costing Profit and Loss Account, '
               '*reducing* profit.'},
      {'tacc': {'t': 'Cost of Sales Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Finished goods control  (v)', 190000], ['Marketing & admin OH  (vii)', 47500],
               ['', 237500, '@tot']],
        'cr': [['Profit & Loss', 237500], ['', 237500, '@tot']]}},
      {'tacc': {'t': 'Sales Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Profit & Loss', 300000]],
        'cr': [['Cost Ledger Contra  (viii)', 300000]]}},

      {'h4': '(c)  The cost accounting profit'},
      {'tacc': {'t': 'Costing Profit and Loss Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cost of Sales', 237500], ['Marketing & admin OH (under-absorbed)', 2500],
               ['Net profit (to Cost Ledger Contra)', 63000], ['', 303000, '@tot']],
        'cr': [['Sales', 300000], ['Production OH control (over-absorbed)', 3000],
               ['', 303000, '@tot']]}},
      {'p': 'Read as a vertical statement, the same thing:'},
      {'stmt': {'t': 'Costing Profit and Loss Account for the period', 'rows': [
        ['Sales', '', 300000],
        ['Less: Cost of sales', '', -237500],
        ['**Gross profit**', '', 62500, '@t'],
        '@gap',
        ['Add: Production overhead over-absorbed', 3000, ''],
        ['Less: Marketing & administration overhead under-absorbed', -2500, 500],
        ['**Cost accounting profit**', '', 63000, '@tt'],
      ]}},
      {'warn': 'The over-absorbed production overhead of **N3,000 is a credit** in this account '
               '— it is money the jobs were charged but the factory did not actually spend, so '
               'it comes back as profit. Leave it out and the profit falls to N60,000, which is '
               'wrong. The under-absorbed N2,500 goes the other way. Two adjustments, opposite '
               'signs — check each one separately.'},
      {'h4': 'The Cost Ledger Contra Account, completed'},
      {'tacc': {'t': 'Cost Ledger Contra Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Sales  (viii)', 300000], ['Balance c/d', 131000], ['', 431000, '@tot']],
        'cr': [['Balance b/f  (ix)', 45000], ['Raw materials control', 110000],
               ['Production OH control', 46000], ['Production wages control', 117000],
               ['Marketing & admin OH', 50000], ['Profit and Loss', 63000],
               ['', 431000, '@tot'], ['Balance b/d', 131000]]}},
      {'note': 'The study text prints the N63,000 profit on the **debit** side of this account '
               'while including it in the **credit** total. It is a credit: the costing profit '
               'is transferred *out of* the cost ledger to the financial ledger, and the contra '
               'account is the route out. Check the arithmetic either way — debits '
               '$300{,}000 + 131{,}000 = 431{,}000$; credits $45{,}000 + 110{,}000 + 46{,}000 + '
               '117{,}000 + 50{,}000 + 63{,}000 = 431{,}000$.',
       'lbl': 'Another source error, corrected'},

      {'h4': '(d)  Trial balance as at the end of the period'},
      {'stmt': {'t': 'Trial Balance at the end of the period', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Raw materials control', 18000, ''],
        ['Work-in-progress control', 68000, ''],
        ['Finished goods control', 45000, ''],
        ['Cost Ledger Contra', '', 131000],
        ['', 131000, 131000, '@tt'],
      ]}},
      {'key': 'Notice what the trial balance of an interlocking cost ledger always looks like: '
              'the three inventory control balances on the debit side, and the Cost Ledger '
              'Contra Account — equal to their sum — on the credit side. '
              '$18{,}000 + 68{,}000 + 45{,}000 = N131{,}000$. If your contra balance does not '
              'equal the sum of the closing inventories, something earlier in the question has '
              'gone wrong, and this is the fastest place to catch it.'},
      ]}},
  ]},

  # ------------------------------------------------------------------ 6.5
  {'n': '6.5', 't': 'Reconciliation of costing and financial accounting profits', 'b': [
    {'p': 'The profit disclosed by the Costing Profit and Loss Account may differ from that '
          'shown in the financial Profit and Loss Account where an interlocking system is '
          'adopted, and it is then necessary to reconcile them. The difference may be due to '
          'the following reasons, which the study text groups under three headings.'},

    {'h4': '6.5.1  Appropriations of profit not dealt with in the cost accounts'},
    {'ol': [
      '**Corporate tax.**',
      '**Transfers to general reserve** or any other fund of accumulated profits — e.g. a '
      'dividend equalisation reserve.',
      '**Charitable donations**, where no direct benefit is derived from them by the company\'s '
      'employees.',
      '**Dividends paid** on the share capital of the company.',
      '**Additional provisions** for depreciation of buildings, plant, etc., and for bad debts.',
      '**Amounts written off** goodwill, preliminary expenses, underwriting commission, '
      'debenture discounts, expenses of capital issues, etc.',
      '**Appropriations to sinking funds** for the purpose of providing for the repayment of '
      'loans or debentures.',
    ]},
    {'note': 'The unifying idea: these are all **appropriations** — distributions or set-asides '
             '*of* profit, made after the profit has been earned. Cost accounting stops at the '
             'point profit is earned, so none of these ever appear in it.'},

    {'h4': '6.5.2  Financial matters outside the scope of the cost accounts'},
    {'ol': [
      '**Interest received** on bank deposits and investments.',
      '**Rents receivable.** If, however, rents are received from a portion of the business '
      'premises which has been sublet, only the *profit* on the rental is excluded from the cost '
      'records; the proportion which represents recovery of rent paid is deducted from the total '
      'rent to arrive at the **net cost of the premises**, and that net cost *is* included in '
      'the cost records.',
      '**Profits or losses on sales** of investments, buildings and other fixed assets; and '
      'capital expenditure charged specifically to revenue.',
      '**Interest on bank loans, mortgages, debentures** and other borrowed money, if interest '
      'on capital is ignored in the cost records.',
      '**Damages payable** according to law.',
      '**Penalties** payable for late completion of contracts.',
      '**Losses due to scrapping machinery** before the date estimated when depreciation and '
      'obsolescence were provided for.',
    ]},
    {'note': 'The unifying idea here is different: these items are genuine income or expense of '
             'the period, but they have **nothing to do with making the product**. Cost '
             'accounting measures the cost of production, so it leaves them out.'},

    {'h4': '6.5.3  Items whose costing treatment differs from the financial treatment'},
    {'ol': [
      '**Under and over recoveries of overhead** — arising from deliberate omission from the '
      'cost accounts (e.g. selling costs), from approximation in the basis of recovery, or from '
      'fluctuations in output.',
      '**Differences in the valuation of inventory and work-in-progress.** Inventories are '
      'frequently valued in the cost accounts at a figure which includes an appropriate '
      'allotment of overhead — perfectly justifiable from the point of view of ascertaining the '
      'profit on manufacture. It may be thought prudent, when preparing the financial accounts, '
      'to value inventories at **prime cost only**.',
      '**Depreciation.** In the cost accounts it may be charged on the basis of production units '
      'or hours; in the financial accounts it is usually provided for as a charge for the '
      'period, irrespective of the actual level of output.',
      '**Abnormal losses** in production and storage, and **abnormal idle time**. In the '
      'financial accounts these losses are "merged" into the appropriate accounts — the sales '
      'figure is exclusive of finished products wasted, and the debits for materials and wages '
      'are inclusive of any abnormal losses of material or time. In the cost accounts, such '
      'abnormal losses may be ignored as outside the scope of manufacturing costs.',
    ]},
    {'key': 'Group 3 is the one that produces **two-sided** adjustments and therefore most of '
            'the marks. Groups 1 and 2 are items present in one set of books and absent from the '
            'other; group 3 items are present in **both** sets, but measured differently. For a '
            'group 3 item you must work out not only *that* there is a difference but which '
            'direction it pushes profit.'},
    {'h4': 'How inventory differences move profit — the rule to memorise'},
    {'p': 'Profit = Sales − Cost of sales, and Cost of sales = Opening inventory + purchases or '
          'production − Closing inventory. So:'},
    {'table': {'align': 'lll',
      'head': ['If, in the cost accounts…', 'then cost of sales is…', 'so costing profit is…'],
      'rows': [
      ['**opening** inventory is **higher** than in the financial accounts', 'higher', '**lower**'],
      ['**opening** inventory is **lower**', 'lower', '**higher**'],
      ['**closing** inventory is **higher**', 'lower', '**higher**'],
      ['**closing** inventory is **lower**', 'higher', '**lower**'],
    ]}},
    {'note': 'Work each of the six inventory figures (raw materials, WIP and finished goods, '
             'opening and closing) separately through this table. Trying to net them off in your '
             'head is the single commonest source of lost marks in this topic.'},
    {'p': 'The reconciliation of financial accounts and cost accounts is carried out using a '
          '**memorandum reconciliation account**, in order to show why the respective profit '
          'figures of the two accounts are different.'},
    {'def': {'t': 'Memorandum reconciliation account', 'd': 'a statement in T-account form, '
                  'outside the double entry (hence "memorandum"), which starts from one profit '
                  'figure and lists every cause of difference until the other profit figure is '
                  'reached. Both sides must come to the same total.'}},

    # ---------------------------------------------------------- Illustration 6.2
    {'eg': {'tag': 'Study text — Illustration 6.2',
      't': 'NUASA Limited — a memorandum reconciliation account',
      'open': True, 'q': [
      {'p': 'NUASA Limited has **separate financial and cost accounting systems**. Extracts from '
            'both sets of accounts for the year ended 31 December 2021 were as follows.'},
      {'p': '**(a) Financial Accounts**'},
      {'stmt': {'t': 'Financial accounts — extracts', 'rows': [
        ['Inventory valuations:', 'Opening (N)', 'Closing (N)', '@hd'],
        ['Raw materials', 34000, 36000],
        ['Work-in-progress', 7000, 5000],
        ['Finished goods', 16000, 20500],
        '@gap',
        ['', 'N', '', '@hd'],
        ['Debenture interest', 5000, ''],
        ['Interest received', 750, ''],
        ['Discounts allowed', 2000, ''],
        ['Discounts received', 1000, ''],
        ['Net profit (before taxation)', 17500, '', '@b'],
      ]}},
      {'p': '**(b) Cost Accounts**'},
      {'stmt': {'t': 'Cost accounts — inventory valuations', 'rows': [
        ['', 'Opening (N)', 'Closing (N)', '@hd'],
        ['Raw materials', 33000, 34500],
        ['Work-in-progress', 8000, 7000],
        ['Finished goods', 17000, 20000],
      ]}},
      {'p': '**Required:** Reconcile the profit as reported in the financial accounts with the '
            'cost accounts, and calculate the cost accounting profit for the period.'},
      {'warn': 'In the study text the cost-accounts inventory table is printed with its row '
               'labels one line out of step with its figures (the "Raw materials" row has no '
               'figures at all, and the three pairs 33,000/34,500, 8,000/7,000 and '
               '17,000/20,500 sit against the wrong captions). The table above restores the '
               'alignment. The closing finished-goods figure has also been corrected from the '
               'printed 20,500 to **20,000** — the text\'s own reconciliation includes a N500 '
               'finished-goods closing difference, which is only possible if the cost figure is '
               'N20,000 against the financial N20,500.', 'lbl': 'Source table realigned'},
      ],
      'a': [
      {'h4': 'Step 1 — list every cause of difference'},
      {'p': 'Take the items present in one set of books only first. Debenture interest and '
            'discounts allowed are **expenses charged in the financial accounts only** (§6.5.2); '
            'discounts received and interest received are **income credited in the financial '
            'accounts only**.'},
      {'p': 'Then take the six inventory valuations, one at a time, through the rule in §6.5:'},
      {'table': {'align': 'lrrll', 'head': ['Inventory', 'Financial (N)', 'Cost (N)',
        'Difference', 'Effect on **costing** profit'], 'rows': [
        ['Raw materials — opening', '34,000', '33,000', 'cost is 1,000 **lower**',
         'cost of sales lower → profit **higher** by 1,000'],
        ['Raw materials — closing', '36,000', '34,500', 'cost is 1,500 **lower**',
         'cost of sales higher → profit **lower** by 1,500'],
        ['Work-in-progress — opening', '7,000', '8,000', 'cost is 1,000 **higher**',
         'cost of sales higher → profit **lower** by 1,000'],
        ['Work-in-progress — closing', '5,000', '7,000', 'cost is 2,000 **higher**',
         'cost of sales lower → profit **higher** by 2,000'],
        ['Finished goods — opening', '16,000', '17,000', 'cost is 1,000 **higher**',
         'cost of sales higher → profit **lower** by 1,000'],
        ['Finished goods — closing', '20,500', '20,000', 'cost is 500 **lower**',
         'cost of sales higher → profit **lower** by 500'],
      ]}},
      {'h4': 'Step 2 — build the memorandum reconciliation account'},
      {'p': 'The account is laid out as a T-account starting from the **financial** profit on '
            'the debit side. Anything that made costing profit *higher* than financial profit '
            'goes on the **debit** side alongside it; anything that made costing profit *lower* '
            'goes on the **credit** side with the costing profit itself.'},
      {'tacc': {'t': 'Memorandum Reconciliation Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Profit as per financial a/cs', 17500],
               ['Debenture interest', 5000],
               ['Discounts allowed', 2000],
               ['Raw materials — opening (diff.)', 1000],
               ['W.I.P. — closing (diff.)', 2000],
               ['', 27500, '@tot']],
        'cr': [['Profit as per cost a/cs *(balancing figure)*', 21750],
               ['Discounts received', 1000],
               ['Interest received', 750],
               ['Raw materials — closing (diff.)', 1500],
               ['W.I.P. — opening (diff.)', 1000],
               ['Finished goods — opening (diff.)', 1000],
               ['Finished goods — closing (diff.)', 500],
               ['', 27500, '@tot']]}},
      {'h4': 'Step 3 — read off the answer'},
      {'p': 'The debit side totals N27,500 without any contribution from the costing profit. The '
            'credit side\'s known items total $1{,}000 + 750 + 1{,}500 + 1{,}000 + 1{,}000 + '
            '500 = N5{,}750$, so the figure needed to bring that side to N27,500 is:'},
      {'tex': '\\text{Cost accounting profit} = 27{,}500 - 5{,}750 = N21{,}750'},
      {'p': 'Equivalently, in vertical form — which is what most examiners now prefer, and which '
            'is far harder to get the signs wrong in:'},
      {'stmt': {'t': 'Reconciliation statement — financial profit to costing profit', 'rows': [
        ['Net profit as per **financial** accounts', '', 17500],
        '@gap',
        ['Add back: charges made in the financial accounts only', '', '', '@hd'],
        ['Debenture interest', 5000, ''],
        ['Discounts allowed', 2000, ''],
        ['Raw materials opening — valued lower in cost accounts', 1000, ''],
        ['Work-in-progress closing — valued higher in cost accounts', 2000, 10000],
        '@gap',
        ['Deduct: credits in the financial accounts only, and the rest', '', '', '@hd'],
        ['Discounts received', 1000, ''],
        ['Interest received', 750, ''],
        ['Raw materials closing — valued lower in cost accounts', 1500, ''],
        ['Work-in-progress opening — valued higher in cost accounts', 1000, ''],
        ['Finished goods opening — valued higher in cost accounts', 1000, ''],
        ['Finished goods closing — valued lower in cost accounts', 500, -5750],
        ['**Profit as per cost accounts**', '', 21750, '@tt'],
      ]}},
      {'key': 'N21,750 is simultaneously **the difference between the two sides of the account** '
              'and **the cost accounting profit** — those are the same thing, because the '
              'memorandum account is constructed precisely so that the unknown profit is the '
              'balancing figure. $17{,}500 + 10{,}000 - 5{,}750 = 21{,}750$.'},
      {'note': 'The study text prints "W.I.P closing" twice in this account — once on each side. '
               'The credit-side entry is the **W.I.P. opening** difference (financial N7,000 vs '
               'cost N8,000 = N1,000); the debit-side entry is the W.I.P. closing difference '
               '(financial N5,000 vs cost N7,000 = N2,000). Corrected above.',
       'lbl': 'Source label error, corrected'},
      ]}},
  ]},

  # ------------------------------------------------------------------ 6.6
  {'n': '6.6', 't': 'Integrated accounting system', 'b': [
    {'p': 'With this accounting system, the concept of **separate** profit and loss accounts for '
          'financial and cost purposes is discarded, in favour of a **unified set of accounts** '
          'which serves both financial and management purposes. Such a system is referred to as '
          'an **"integrated"** or **"integral"** system.'},
    {'def': {'t': 'Integrated accounts (CIMA Terminology)', 'd': 'a set of accounting records '
                  'that integrates both financial and cost accounts using a common input and '
                  'data for all accounting purposes.'}},
    {'h4': 'The five design principles'},
    {'ol': [
      '**The degree of integration must be determined.** Some undertakings find it satisfactory '
      'merely to integrate up to the stage of **prime cost**, leaving overhead allotment to be '
      'dealt with in memorandum form only.',
      '**The normal classification of expenditure by nature is discarded**, to the extent the '
      'chosen degree of integration requires. In some systems a *single* control account is '
      'opened, into which all expenditure and revenue subject to costing treatment is posted — '
      'operating in the same way as a debtors\' control account, i.e. containing a summary of '
      'transactions posted to the cost ledger in detail. It is, however, more usual for '
      '**separate control accounts** to be opened in the formal records, in the same way as '
      'control accounts were opened within the cost ledger for stores, work-in-progress, '
      'overhead and so on under a separate system.',
      '**Full details of items posted to the control accounts are supplied to the cost '
      'department** at conventional intervals, accompanied by **prelists or registers** of '
      'amounts to ensure completeness.',
      '**The cost department then deals with the information** following the system of costing '
      'in force, with two objectives in mind: *(i)* to provide the necessary costing data; and '
      '*(ii)* to form the basis for journal entries, so that the control accounts can be cleared '
      'to suitable revenue accounts, culminating in a profit and loss account.',
      '**The amount of detail recorded in the ledger itself is usually kept to a minimum**, with '
      'full information regarding each department or process contained in **subsidiary '
      'ledgers** (based, of course, upon exactly the same data). Postings to subsidiary ledgers '
      'are sometimes referred to as **"third entries"**, to emphasise that they are not part of '
      'the double entry of the accounting system.',
    ]},
    {'p': 'Applying these principles facilitates the preparation of **operating statements**, in '
          'whatever form is required, from data which are subject to routine accounting control. '
          'The conventional analysis of expenditure required for statutory purposes and external '
          'reporting can be accommodated by modifying the classification procedures within the '
          'subsidiary ledgers.'},
    {'h4': 'Advantage and problem'},
    {'table': {'align': 'll', 'head': ['The advantage', 'The problem'], 'rows': [
      ['The integrated system **saves administrative effort**, since only one set of accounts is '
       'kept instead of two separate systems of cost and financial accounting. The possible '
       '**confusion arising from having two sets of accounts is eliminated**, as is the need for '
       'reconciliation.',
       'One set of accounts is expected to fulfil **two different purposes**: *(i)* stewardship '
       'of the business and external reporting; and *(ii)* provision of information to aid '
       'management decisions and control of operations. At times these purposes **conflict** — '
       'e.g. the valuation of inventories must conform to International Accounting Standards, '
       'whereas the cost accountant might prefer to value closing inventories at, say, marginal '
       'cost or replacement cost.'],
    ]}},
    {'h4': 'Entries for the integrated system'},
    {'table': {'align': 'lll', 'head': ['#  Transaction', 'Debit', 'Credit'], 'rows': [
      ['**1** Materials purchased', 'Raw Materials / Stores Ledger Control A/c',
       'Bank / Creditors for Materials'],
      ['**2** Materials returned to suppliers', 'Creditors for Materials',
       'Raw Materials Control A/c'],
      ['**3** Materials issued — direct', 'Work-in-Progress Control A/c',
       'Raw Materials Control A/c'],
      ['**3** Materials issued — indirect (factory)', 'Production Overhead Control A/c',
       'Raw Materials Control A/c'],
      ['**4** Wages incurred', 'Wages Control A/c (WCA)', 'Wages Payable A/c'],
      ['**5** Wages allocated — direct', 'Work-in-Progress Control A/c', 'Wages Control A/c'],
      ['**5** Wages allocated — indirect', 'Production Overhead Control A/c', 'Wages Control A/c'],
      ['**6** Production overhead incurred', 'Production Overhead Control A/c (POCA)',
       'Bank / Creditors for Overheads'],
      ['**7** Absorption of overhead', 'WIP Control A/c', 'Production Overhead Control A/c'],
      ['**8** Output achieved', 'Finished Goods A/c', 'Work-in-Progress A/c'],
    ]}},
    {'note': 'Entry 7 again needs the **adjustment for under/over absorption** — the residual '
             'balance on the Production Overhead Control Account goes to the (single) Profit and '
             'Loss Account.'},
    {'warn': 'The study text prints entry 5 as "Debit Work-In-Progress Control Account; Credit '
             'Production Overhead Control Account; Credit Wages Control Account." The middle '
             'line is a misprint for a second **debit** — Production Overhead Control is '
             '*debited* with the indirect wages, not credited. Corrected in the table above.',
     'lbl': 'Source error, corrected'},
    {'key': 'Compare this table against §6.4\'s. The **entries are almost identical** — the '
            'difference is entirely in the credits to the outside world. The interlocking system '
            'routes every external transaction through the **Cost Ledger Control / Contra '
            'Account**, because the cost ledger cannot see real supplier, bank or wages-payable '
            'accounts. The integrated system posts to those **real accounts directly**, because '
            'there is only one ledger and it contains them. Learn one table and the other is a '
            'two-column substitution.'},

    # ---------------------------------------------------------- Illustration 6.3
    {'eg': {'tag': 'Study text — Illustration 6.3',
      't': 'Gwammaja Limited — a complete integrated-accounts month, from control accounts to '
           'the balance sheet',
      'open': True, 'q': [
      {'p': 'Gwammaja Limited manufactures a range of products which are sold through a network '
            'of wholesalers and dealers. A set of **integrated accounts** is kept, and for the '
            'year 2021 the following information is relevant.'},
      {'ul': [
        '**(a)** Production overhead is absorbed into the cost of products on the basis of a '
        'budgeted rate of **80% of direct labour cost**.',
        '**(b)** Finished inventories are valued at **factory cost**.',
      ]},
      {'stmt': {'t': '(c)  Balances', 'rows': [
        ['', '31 March 2021 (N)', '30 April 2021 (N)', '@hd'],
        ['Raw materials inventory', 8600, 7580],
        ['Work-in-progress', 2800, 2375],
        ['Finished goods inventory', 5250, 6045],
        ['Debtors for goods sold', 4600, 5570],
        ['Creditors for raw materials', 3800, 4710],
        ['Fixed assets at net book value', 3000, 3000],
      ]}},
      {'stmt': {'t': '(d)  Bank transactions for April 2021', 'rows': [
        ['Bank balance at 31 March', '', 750],
        ['Receipts from debtors', '', 13780],
        '@gap',
        ['Payments made:', '', '', '@hd'],
        ['Direct labour', 3200, ''],
        ['Creditors for raw materials', 4480, ''],
        ['Production overhead', 2700, ''],
        ['Administration overhead', 350, ''],
        ['Selling & distribution overhead', 1150, ''],
      ]}},
      {'p': '**Required:**'},
      {'ol': [
        'Use the information provided above to write up the following control accounts: '
        '(i) Raw materials inventory; (ii) Work-in-Progress; (iii) Finished Goods; '
        '(iv) Production Overhead.',
        'Prepare the following statements: (i) a Profit and Loss Account for April 2021; '
        '(ii) a Balance Sheet as at 30 April 2021.',
      ]},
      ],
      'a': [
      {'key': 'The whole question is one technique applied six times: **every missing figure is '
              'a balancing figure on a T-account.** Nothing here is given directly — not '
              'purchases, not materials issued, not cost of sales, not even sales. Work the '
              'accounts in the right order and each one hands you the figure the next one needs. '
              'The order is: Creditors → Raw Materials → WIP → Finished Goods → Debtors → Cash.'},

      {'h4': 'Working 1 — Creditors for raw materials, to find purchases'},
      {'tacc': {'t': 'W1  Creditors for Raw Materials', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cash', 4480], ['Balance c/d', 4710], ['', 9190, '@tot']],
        'cr': [['Opening balance', 3800],
               ['Raw material purchases *(balancing figure)*', 5390], ['', 9190, '@tot']]}},
      {'note': 'The study text prints this account\'s totals as **9,199** on both sides. They '
               'are **N9,190** ($4{,}480 + 4{,}710$, and $3{,}800 + 5{,}390$). The purchases '
               'figure of N5,390 that the text then uses is correct, so only the total is '
               'mistyped.', 'lbl': 'Source arithmetic error, corrected'},

      {'h4': 'Working 2 — Production overhead absorbed'},
      {'tex': '\\text{Overhead absorbed} = 80\\% \\times \\text{direct labour cost} '
              '= 0.80 \\times 3{,}200 = N2{,}560'},

      {'h4': '(a)(i)  Raw Materials Inventory Control Account'},
      {'tacc': {'t': 'Raw Materials Inventory', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Opening balance', 8600], ['Creditors (W1) — purchases', 5390],
               ['', 13990, '@tot'], ['Balance b/d', 7580]],
        'cr': [['Work-in-progress *(balancing figure)*', 6410], ['Balance c/d', 7580],
               ['', 13990, '@tot']]}},

      {'h4': '(a)(ii)  Work-in-Progress Control Account'},
      {'tacc': {'t': 'Work-in-Progress', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Opening balance', 2800], ['Raw materials inventory', 6410],
               ['Direct wages', 3200], ['Production OH (W2)', 2560], ['', 14970, '@tot'],
               ['Balance b/d', 2375]],
        'cr': [['Finished goods *(balancing figure)*', 12595], ['Balance c/d', 2375],
               ['', 14970, '@tot']]}},

      {'h4': '(a)(iii)  Finished Goods Control Account'},
      {'tacc': {'t': 'Finished Goods', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Opening balance', 5250], ['Work-in-progress', 12595], ['', 17845, '@tot'],
               ['Balance b/d', 6045]],
        'cr': [['P&L A/c — cost of sales *(balancing figure)*', 11800], ['Balance c/d', 6045],
               ['', 17845, '@tot']]}},

      {'h4': '(a)(iv)  Production Overhead Control Account'},
      {'tacc': {'t': 'Production Overhead', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cash', 2700], ['', 2700, '@tot']],
        'cr': [['Work-in-progress (absorbed)', 2560],
               ['Profit & Loss A/c (under-absorbed)', 140], ['', 2700, '@tot']]}},
      {'note': 'N2,700 was spent; only N2,560 was charged to production. The shortfall of '
               '**N140 is under-absorbed overhead**, written off as an expense in the profit and '
               'loss account.'},

      {'h4': 'Working 3 — Debtors, to find sales'},
      {'tacc': {'t': 'W3  Debtors', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Opening balance', 4600], ['Sales *(balancing figure)*', 14750],
               ['', 19350, '@tot']],
        'cr': [['Cash', 13780], ['Balance c/d', 5570], ['', 19350, '@tot']]}},

      {'h4': 'Working 4 — Cash, to find the closing bank balance'},
      {'tacc': {'t': 'W4  Cash', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Opening balance', 750], ['Debtors', 13780], ['', 14530, '@tot']],
        'cr': [['Creditors for raw materials', 4480], ['Direct labour', 3200],
               ['Production overhead', 2700], ['Administration overhead', 350],
               ['Selling & distribution OH', 1150], ['Balance c/d', 2650],
               ['', 14530, '@tot']]}},

      {'h4': '(b)(i)  Income Statement for April 2021'},
      {'stmt': {'t': 'Gwammaja Limited — Profit and Loss Account for April 2021', 'rows': [
        ['Sales (W3)', '', 14750],
        ['Production cost of sales', '', 11800],
        ['**Gross profit**', '', 2950, '@t'],
        '@gap',
        ['Less:  Administration overhead', 350, ''],
        ['          Selling & distribution overhead', 1150, ''],
        ['          Under-absorbed production overhead', 140, 1640],
        ['**Profit for the month**', '', 1310, '@tt'],
      ]}},

      {'h4': '(b)(ii)  Balance Sheet as at 30 April 2021'},
      {'stmt': {'t': 'Gwammaja Limited — Position Statement as at 30 April 2021', 'rows': [
        ['Fixed assets (net book value)', '', 3000],
        '@gap',
        ['Current assets:', '', '', '@hd'],
        ['Raw materials', 7580, ''],
        ['Work-in-progress', 2375, ''],
        ['Finished goods', 6045, ''],
        ['Debtors', 5570, ''],
        ['Cash (W4)', 2650, 24220],
        ['Less: Current liabilities — creditors for raw materials', 4710, ''],
        ['**Net current assets**', '', 19510, '@t'],
        ['**Total net assets**', '', 22510, '@tt'],
        '@gap',
        ['Financed by:', '', '', '@hd'],
        ['Long-term capital *(balancing figure)*', '', 21200],
        ['Profit for the month', '', 1310],
        ['', '', 22510, '@tt'],
      ]}},
      {'note': 'The study text\'s printed balance sheet omits the N4,710 creditors figure on the '
               '"Less: Current Liabilities" line (leaving only the N19,510 net result), and '
               'prints the capital line as "Long-term capital N21,200 (balancing figure) + '
               '1,310)". Restored above: $24{,}220 - 4{,}710 = N19{,}510$, and '
               '$22{,}510 - 1{,}310 = N21{,}200$.', 'lbl': 'Source presentation errors, fixed'},
      {'key': 'Every "balancing figure" in this question is found the same way: *opening balance '
              '+ known debits − known credits = closing balance*, rearranged to solve for the '
              'one missing entry. That is the real skill being tested — not arithmetic, but '
              'knowing which account to attack first so that each unknown becomes knowable in '
              'turn.'},
      ]}},
  ]},

  # ------------------------------------------------------------------ 6.7
  {'n': '6.7', 't': 'Accounts classification and codes', 'b': [
    {'p': 'In an organisation of any size, the cost and financial data will be so numerous that '
          'details must be **summarised under suitable headings** before management can process '
          'and assimilate them for decision making. For example, many types of indirect material '
          'are used in a factory; in reporting consumption, typical headings under which the '
          'data are summarised would include:'},
    {'ol': [
      'Cleaning materials', 'Lubrication', 'Fuel', 'Protective clothing', 'Stationery',
      'Small tools', 'Packing material', 'Foodstuffs', 'Replacement parts', 'Miscellaneous',
    ]},
    {'p': 'By using such groups, the **number of accounts can be reduced**, and the groups can '
          'then be used for budgeting purposes and the like. To assemble data under these '
          'headings, it is vital to use **code numbers or letters**, and to prepare an '
          '**accounts manual** containing, among other things, a list of all current codes with '
          'explanatory notes on their use.'},
    {'key': 'A good accounts manual is **comprehensive, unambiguous and well indexed**, so that '
            'invoices, requisitions, time-sheets and so on can be coded **quickly and '
            'accurately**. Those three adjectives are the standard exam answer to "what makes a '
            'good accounts manual?"'},
    {'h4': 'Principles of a good code structure'},
    {'p': 'The code structure adopted can be prepared in several ways, but it is important that '
          'it:'},
    {'ol': [
      'follows a **logical sequence**, i.e. all common items are pulled together;',
      'is **flexible** enough to accommodate additions; and',
      'is arranged in a way that **aids memory**.',
    ]},
    {'p': 'If the system is so complex that a code in excess of **6 digits** must be used, then '
          'it is preferable to adopt a **composite code**, suitably structured — like '
          '`024-824-03`.'},
    {'note': 'Why a composite code helps: `02482403` is a single eight-digit string a clerk must '
             'read and retype without transposing a digit. `024-824-03` is three short chunks, '
             'each of which can carry its own meaning (say, division – cost centre – expense '
             'type), so the code is both easier to remember and self-checking: a clerk who knows '
             'the division is 024 will spot `031-824-03` immediately.'},
    {'h4': 'A simple accounts code — fixed asset accounts'},
    {'table': {'align': 'll', 'head': ['Code range', 'Category'], 'rows': [
      ['0000 – 0099', 'Land'],
      ['0100 – 0299', 'Buildings'],
      ['0300 – 0399', 'Machine tools'],
      ['0400 – 0499', 'Containers and tanks'],
      ['0500 – 0599', 'Vehicles'],
      ['0600 – 0699', 'Handling equipment'],
      ['0700 – 0799', 'Heating plant'],
      ['0800 – 0899', 'Tools and patterns'],
      ['0900 – 0999', 'Miscellaneous fixed assets, patents and goodwill'],
    ]}},
    {'p': 'The same coding system may be followed when designing account codes for **current '
          'assets, liabilities, cost centres, expenditure and miscellaneous accounts**.'},
    {'note': 'Notice that the ranges are not all the same width — Buildings gets 200 codes while '
             'Land gets 100. That is the "flexible enough to accommodate additions" principle in '
             'action: you leave more room where you expect more accounts to be opened later.'},
  ]},

  # ------------------------------------------------------------------ 6.8
  {'n': '6.8', 't': 'Computer-assisted costing techniques', 'b': [
    {'p': 'In today\'s dynamic business environment, it is doubtful whether the cost accountant '
          'can be effective without the use of computer techniques. Aside from the **volume of '
          'transactions** and the **speed of processing** required, there is the need for '
          'systems that **simplify decisions** by offering a wide range of options to users of '
          'cost accounting information.'},
    {'h4': '(a)  Transaction processing systems'},
    {'p': 'First among the computer-assisted costing techniques are **transaction processing '
          'systems**. These are systems designed to handle **large volumes of monotonous '
          'transactions** from various points, coordinated by a **central server** which '
          'processes and harmonises such a mass of data. Usually such systems have **set '
          'functions**, and their formats **cannot easily be amended** without the intervention '
          'of data processing experts such as systems analysts and programmers.'},
    {'h4': '(b)  Decision support systems'},
    {'p': 'Secondly, some systems are designed to **support decision making**. They are '
          'generally very **user-friendly and interactive**, offering a variety of tools that '
          'users can employ to perform required tasks more effectively, unlike the mass '
          'data-processing systems.'},
    {'p': 'Decision support systems have the advantages of:'},
    {'ol': [
      '**guiding the manager** through a process of using available data to quickly arrive at '
      'useful decisions. They provide the support but still leave the manager to take the '
      'decisions, because they do **not offer pre-determined solutions**;',
      '**interaction**, which enhances effective problem solving through the wide range of '
      'options provided; and',
      '**not having a structured solution** — the manager must determine the direction of the '
      'decisions to be reached, seeing that the system guides them towards possible solutions '
      'and their implications.',
    ]},
    {'p': 'Decision support systems include:'},
    {'ol': [
      'Spreadsheets', 'Forecasting', 'Regression analysis',
      'Non-linear and linear programming', 'Modelling and simulation', 'Statistical analysis',
      'Financial modelling', 'Sensitivity and risk analysis', 'Activity cost management',
    ]},
    {'h4': '(c)  Application packages, and the spreadsheet in particular'},
    {'p': 'All the systems cited above come with **application packages** which are:'},
    {'ul': [
      '**flexible** — customisable to the user\'s requirements as to transaction types, data '
      'layouts, report formats and frequency; and',
      '**cheap to use** — they do not require the employment of specialists or systems analysts, '
      'who are expensive to maintain.',
    ]},
    {'p': 'Most packages are designed to deal with a single specific application, but by far the '
          'most versatile and widely applied package is the **electronic spreadsheet**, and the '
          'most useful electronic spreadsheet at the disposal of cost accountants is **Microsoft '
          'Excel**. The spreadsheet is capable of storing both alphabetical and numeric data, '
          'which are amenable to easy manipulation through simple commands, arranged in a '
          '**grid of columns and rows**. With the data safely entered in the cells, a change in '
          'a single command is **automatically effected throughout the mass of data** across the '
          'worksheets that are linked together.'},
    {'p': 'Spreadsheets can be used for:'},
    {'ul': [
      'monthly expenditure reports;', 'cash budgets;', 'standard cost records;',
      'profitability reports; among others.',
    ]},
    {'p': 'Data in Microsoft Excel is also capable of being **exported** into packages such as '
          'PowerPoint and others with capabilities for pictorial presentation, thus enhancing '
          'the use of computer systems in decision making.'},
    {'table': {'align': 'lll', 'head': ['', 'Transaction processing system',
      'Decision support system'], 'rows': [
      ['**Purpose**', 'Record and process routine transactions', 'Help a manager choose'],
      ['**Volume**', 'Very high, repetitive', 'Low — one question at a time'],
      ['**Format**', 'Fixed; needs a systems analyst to change', 'Flexible, user-customisable'],
      ['**Output**', 'Processed records, standard reports', 'Options and their implications'],
      ['**Who decides**', 'Nobody — it posts', 'The **manager**; the system only guides'],
    ]}},
  ]},

  # ------------------------------------------------------------------ 6.9
  {'n': '6.9', 't': 'Chapter summary', 'b': [
    {'p': 'In this chapter, efforts were made to explain the **double-entry aspects of cost '
          'accounting**, and the **reconciliation** of the cost accounts with the financial '
          'accounts. It has been made clear that cost accounts and financial accounts may be '
          'organised through either **"interlocking accounts"** or **"integrated accounts"**. We '
          'have also shown how two separate sets of accounts are reconciled with the use of a '
          '**memorandum reconciliation account**. Finally, we have described how **account '
          'codes** should be used to summarise cost and financial data before the data can be '
          'processed and assimilated by management for relevant decisions.'},
    {'p': 'It is clear from this chapter that the double-entry system of bookkeeping is **not '
          'restricted to financial accounting**. The system is also very applicable to cost '
          'accounting and management accounting. It all depends on the type of organisation and '
          'its commitment to proper record keeping, transparency and accountability.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§6.1 Introduction** — bookkeeping applies to cost accounting too; business size drives '
      'record complexity; two systems, interlocking (reconcile) and integrated (no '
      'reconciliation, the more satisfactory method).',
      '**§6.2 Interlocking system** — separate cost accounts periodically reconciled; cost '
      'records cover cost elements, cost centres, job costs and inventory; linked by a **Cost '
      'Ledger Control Account** in the financial ledger and a **Financial Ledger Control '
      'Account** in the cost ledger.',
      '**§6.3 Cost ledger** — the principal ledger; holds control accounts (each with a '
      'subsidiary ledger), wages/sales/cost-of-sales accounts, and the **Cost Ledger Contra '
      'Account** that keeps the cost ledger self-balancing; the **WIP ledger is the focal '
      'point**.',
      '**§6.4 Interlocking entries** — seven numbered entries from raw material incurred to '
      'output achieved, every external transaction routed through the contra account, plus an '
      'adjustment for under/over absorption.',
      '**§6.5 Reconciliation** — three groups of cause (6.5.1 appropriations of profit; 6.5.2 '
      'financial matters outside costing\'s scope; 6.5.3 different costing treatment), '
      'reconciled in a memorandum account that must balance on both sides.',
      '**§6.6 Integrated system** — CIMA definition; five design principles; saves effort and '
      'removes reconciliation, but one set of accounts must serve two conflicting purposes; '
      'eight entries, posting to real accounts instead of a contra account.',
      '**§6.7 Accounts codes** — summarise under headings first; the accounts manual; logical, '
      'flexible, memorable; composite codes beyond 6 digits; range-based fixed-asset example.',
      '**§6.8 Computer-assisted techniques** — transaction processing systems (high volume, '
      'fixed format) vs decision support systems (flexible, guides but does not decide); nine '
      'named DSS tools; the spreadsheet as the most versatile.',
    ]},
    {'h3': 'Every term in this chapter'},
    {'ul': [
      '**Interlocking system** — separate cost and financial ledgers, periodically reconciled.',
      '**Integrated (integral) system** — one unified ledger, no reconciliation needed.',
      '**Cost Ledger Control Account** — the account in the *financial* ledger representing the '
      'cost ledger.',
      '**Financial Ledger Control Account / Cost Ledger Contra Account / General Ledger '
      'Adjustment Account** — three names for the account in the *cost* ledger that holds every '
      'posting affecting the world outside costing, keeping the cost ledger self-balancing.',
      '**Control account** — an account in the main ledger summarising a subsidiary ledger; its '
      'entries are summary postings.',
      '**Subsidiary ledger** — where the detail behind a control account is actually kept.',
      '**Notional charge** — a charge not actually payable, included in the cost accounts to '
      'reflect the normal cost of running the business (e.g. notional rent on owned premises).',
      '**Memorandum reconciliation account** — a statement outside the double entry explaining '
      'the difference between costing and financial profit; must balance on both sides.',
      '**Third entries** — postings to a subsidiary ledger under an integrated system; not part '
      'of the formal double entry.',
      '**Prelists / registers** — listings of amounts sent with control-account detail to the '
      'cost department to prove completeness.',
      '**Composite code** — a code split into meaningful chunks (e.g. `024-824-03`), preferred '
      'once a single code would exceed six digits.',
      '**Transaction processing system** — high-volume, fixed-format routine processing.',
      '**Decision support system (DSS)** — interactive, flexible, unstructured; guides a '
      'manager to a decision without pre-determining it.',
    ]},
  ]},

  # ------------------------------------------- end-of-chapter questions (source)
  {'n': '6.10', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'eg': {'tag': 'Study text', 't': 'The ten questions, with the official answers',
      'open': True, 'q': [
      {'ol': [
        'An interlocking accounting system has — (A) Various ledgers relating to one another; '
        '(B) A separate set of financial ledgers and a separate set of costing ledgers; '
        '(C) Accounting entries locked up in the ledger; (D) Different ledgers for direct '
        'expenses and indirect expenses; (E) A single set of ledgers serving a dual purpose.',
        'A trial balance is — (A) The set of accounting records presented at court cases; '
        '(B) An account prepared to determine a company\'s profitability; (C) A list of account '
        'balances, both debit and credit sides balancing; (D) The balance of the cost ledger '
        'control account; (E) A statement of balances on bank accounts.',
        'What is a notional charge? — (A) A charge on the assets of the company; (B) A '
        'government charge to be paid by the company; (C) Charges introduced to reduce tax '
        'liability; (D) Charges which, though not payable, are meant to reflect the normal costs '
        'of running the business; (E) Expected income which may be recognised in the accounts.',
        'In reconciliation of profits disclosed by interlocking accounts, what are purely '
        'financial matters? — (A) Items involving cash transactions; (B) Balance sheet items; '
        '(C) Matters relating to the banks; (D) Salaries and wages paid to casual workers; '
        '(E) Financial matters outside the scope of production.',
        'What is a control account? — (A) An account in the main ledger summarising the '
        'subsidiary ledger accounts; (B) The account maintained by the Financial Controller; '
        '(C) An account maintained by the Cost Controller; (D) A separate account for monitoring '
        'factory performance; (E) A secret account for monitoring factory performance.',
        'A system where **one** set of accounts is kept for both financial and costing '
        'transactions is known as ………………………',
        '*(The study text prints this question number with no question against it — see the note '
        'below.)*',
        'In the accounts manual, processing of a large mass of data under different account '
        'heads is made possible through the use of ……………….',
        'Raw materials issued to production but yet to reach the finished stage at period end '
        'are to be found in which account?',
        'The conflict between the profit figures arrived at under the financial account and the '
        'cost account ledger is settled by way of a ………………..',
      ]}],
      'a': [
      {'ol': [
        '**B** — a separate set of financial ledgers and a separate set of costing ledgers, '
        'periodically reconciled. (A) is too vague to distinguish any system; (E) describes an '
        '*integrated* system, the opposite answer.',
        '**C** — a list of account balances, both debit and credit sides balancing.',
        '**D** — charges which, though not payable, are meant to reflect the normal costs of '
        'running the business. The classic example is **notional rent** charged on premises the '
        'business owns outright, so that the cost of the product is comparable with that of a '
        'competitor who rents.',
        '**E** — financial matters outside the scope of production (§6.5.2). Note that (A), (B) '
        'and (C) are all true of *some* purely financial items but true of plenty of costing '
        'items too, so none of them defines the category.',
        '**A** — an account in the main ledger summarising the subsidiary ledger accounts.',
        '**Integrated (integral) accounting system.**',
        '*(no question printed)*',
        '**Accounts codes.**',
        '**The Work-in-Progress (Control) Account** — material issued but not yet finished is, '
        'by definition, work in progress.',
        '**A memorandum reconciliation account / statement.**',
      ]},
      {'warn': 'The study text prints **ten** numbered questions but only **nine** answers, and '
               'the two lists are out of step from question 7 onwards. Question 7 is printed as '
               'a bare "…." with no question text; the answer list then gives "Accounts codes" '
               'as answer 7 (which actually answers question 8), "Work in progress account" as '
               'answer 8 (which answers question 9) and "Memorandum Reconciliation Statement" as '
               'answer 9 (which answers question 10). The numbering above has been realigned so '
               'each answer sits against the question it actually answers.',
       'lbl': 'Source numbering error, realigned'},
      ]}},
  ]},

  {'n': '6.11', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with eleven examination-type questions. All eleven '
          'are reproduced below with full solutions — the discursive ones answered from the '
          'chapter, the computational ones worked out account by account.'},

    # ---- Q1
    {'eg': {'tag': 'Exam type — Q1', 't': 'Integrated accounting and its advantages',
      'q': [{'p': 'What do you understand by the term "Integrated Accounting", and what '
                  'advantages does it offer compared to separate systems of cost accounting and '
                  'financial accounting?'}],
      'a': [
      {'h4': 'What it is'},
      {'p': 'Integrated (or integral) accounting is, in CIMA\'s words, **a set of accounting '
            'records that integrates both financial and cost accounts using a common input and '
            'data for all accounting purposes**. The separate costing profit and loss account is '
            'abandoned; a single unified set of accounts serves stewardship and management '
            'purposes together, and the control accounts (stores, WIP, overhead, finished goods) '
            'sit in the one ledger alongside the real accounts for bank, debtors and creditors.'},
      {'h4': 'Advantages over separate systems'},
      {'ol': [
        '**Saves administrative effort** — only one set of accounts is written up instead of '
        'two, so each transaction is recorded once rather than twice.',
        '**Eliminates duplication of data entry** and the cost of the staff needed to do it.',
        '**No reconciliation is necessary** — there is only one profit figure, so the whole '
        'memorandum reconciliation exercise of §6.5 disappears.',
        '**Removes the confusion** that arises from having two sets of records showing different '
        'profits for the same period, which managers outside the accounts department find hard '
        'to interpret.',
        '**One version of the truth** — cost and financial staff work from identical figures, so '
        'disputes about which set is "right" cannot arise.',
        '**Faster reporting**, since management information does not have to wait for a '
        'reconciliation to be completed.',
      ]},
      {'h4': 'The offsetting disadvantage, which a good answer states'},
      {'p': 'One set of accounts must fulfil **two different purposes** — stewardship and '
            'external reporting on one hand, and management decision-making and operational '
            'control on the other — and these can conflict. Inventory, for instance, must be '
            'valued to meet International Accounting Standards for the external accounts, '
            'whereas the cost accountant might prefer a marginal-cost or replacement-cost '
            'valuation for decision-making.'}]}},

    # ---- Q2
    {'eg': {'tag': 'Exam type — Q2', 't': 'Principles to observe in codifying accounts',
      'q': [{'p': 'The growth in the volume of data handled and current technological advances '
                  'in data processing equipment continue to emphasise the need for a '
                  'satisfactory system of codification of accounts. In determining such a code, '
                  'what principles should be observed?'}],
      'a': [
      {'ol': [
        '**Logical sequence** — the code must group all common items together, so that related '
        'accounts fall in adjacent ranges and a reader can tell what an account is from its '
        'number alone.',
        '**Flexibility** — enough unused numbers must be left within each range to accommodate '
        'additions, so a new account can be opened without disturbing the structure (note how '
        'the study text\'s own example gives Buildings 200 codes but Land only 100).',
        '**Memorability** — the arrangement should aid memory, since clerks code invoices, '
        'requisitions and time-sheets at speed.',
        '**Uniqueness** — one code per account and one account per code, with no ambiguity about '
        'which to use.',
        '**Brevity, with a composite structure beyond six digits** — where a code would need '
        'more than six digits, split it into meaningful chunks such as `024-824-03` rather than '
        'running one long number.',
        '**Supported by an accounts manual** which is comprehensive, unambiguous and well '
        'indexed, listing every current code with explanatory notes on its use.',
        '**Comprehensiveness** — the structure must cover fixed assets, current assets, '
        'liabilities, cost centres, expenditure and miscellaneous accounts on the same pattern, '
        'not just one family of accounts.',
      ]}]}},

    # ---- Q3
    {'eg': {'tag': 'Exam type — Q3', 't': 'Uniform costing — overhead aspects',
      'q': [{'p': 'You have been appointed as adviser to a trade association of toy '
                  'manufacturers and are asked to prepare a report on implementing uniform '
                  'costing systems. List **two** aspects of overhead costing to be examined and '
                  'explain how uniformity may be achieved in respect of each.'}],
      'a': [
      {'note': 'Uniform costing — a common costing system adopted by several firms in the same '
               'industry so their costs are comparable — is treated in the Cost Reduction and '
               'Control material rather than here. This answer uses the overhead framework of '
               'Chapter 5 to answer the question as set.'},
      {'h4': 'Aspect 1 — the basis of apportioning overhead to cost centres'},
      {'p': 'Member firms will otherwise apportion rent on floor area, power on machine '
            'horsepower, canteen cost on head count and so on, each in its own way, so two firms '
            'with identical total overhead can report quite different departmental costs. '
            '**Uniformity is achieved** by the association agreeing and publishing a standard '
            'schedule of apportionment bases — one prescribed basis for each class of overhead — '
            'together with a standard list of cost centres, so every member apportions the same '
            'cost to the same place in the same way.'},
      {'h4': 'Aspect 2 — the overhead absorption rate: its basis and the activity level used'},
      {'p': 'One firm may absorb on direct labour hours, another on machine hours, another as a '
            'percentage of direct wages; and one may use budgeted capacity while another uses '
            'normal or actual capacity, which changes the rate even when the basis is the same. '
            '**Uniformity is achieved** by prescribing both the absorption basis for each type '
            'of production department (e.g. machine hours in machine-intensive departments, '
            'labour hours in labour-intensive ones) and the activity level on which the '
            'predetermined rate is to be computed, plus a common treatment of the resulting '
            'under- or over-absorption.'},
      {'h4': 'Other aspects a fuller report would add'},
      {'ul': [
        'a common classification of costs as **direct or indirect**, and as production, '
        'administration, or selling and distribution overhead;',
        'a common treatment of **depreciation** — same method, same lives, same basis of charge;',
        'a common policy on **notional charges** (notional rent, interest on capital), which '
        'otherwise make one firm\'s costs look structurally higher than another\'s.',
      ]}]}},

    # ---- Q4
    {'eg': {'tag': 'Exam type — Q4', 't': 'Explaining the balances on a jobbing manufacturer\'s '
                                          'cost ledger trial balance',
      'q': [
      {'p': 'The following trial balance results from entries in the cost ledger of a jobbing '
            'manufacturer:'},
      {'stmt': {'t': 'Cost ledger trial balance', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['(a)  Cost Ledger Contra Account', '', 11590],
        ['(b)  Stores Ledger Account', 3790, ''],
        ['(c)  Work-in-Progress Account', 5430, ''],
        ['(d)  Finished Goods Account', 2350, ''],
        ['(e)  Factory Overhead Account', 50, ''],
        ['(f)  Administration Cost Account', '', 30],
        ['', 11620, 11620, '@tt'],
      ]}},
      {'p': '**Required:** Explain what each balance represents and the transaction(s) out of '
            'which it has arisen.'}],
      'a': [
      {'table': {'align': 'll', 'head': ['Balance', 'What it represents, and how it arose'],
        'rows': [
        ['**(a) Cost Ledger Contra N11,590 Cr**', 'The mirror of everything the cost ledger '
         'holds — it exists solely to complete the double entry for transactions whose other '
         'side lies outside the cost ledger (purchases from suppliers, wages paid, overheads '
         'incurred, sales value, profit transferred out). Its balance must always equal the net '
         'total of all the other balances: $3{,}790 + 5{,}430 + 2{,}350 + 50 - 30 = '
         '**N11{,}590**$ ✓'],
        ['**(b) Stores Ledger N3,790 Dr**', 'The **cost value of raw materials, components and '
         'spare parts physically still in store** at the period end. It arises as purchases '
         'received into store (debits) less materials issued to jobs and to the factory '
         '(credits) and any returns to suppliers.'],
        ['**(c) Work-in-Progress N5,430 Dr**', 'The **cost of jobs started but not yet '
         'completed** — the accumulated direct materials, direct wages and absorbed production '
         'overhead on those jobs. It arises as those three debits less the cost of jobs '
         'completed and transferred to finished goods.'],
        ['**(d) Finished Goods N2,350 Dr**', 'The **cost of completed jobs not yet delivered to '
         'customers**. It arises as transfers in from work-in-progress less the cost of jobs '
         'delivered, transferred to cost of sales.'],
        ['**(e) Factory Overhead N50 Dr**', 'A debit balance on an overhead account is '
         '**under-absorbed factory overhead** — overhead actually incurred (indirect materials, '
         'indirect wages and other factory expenses) exceeded the amount absorbed into jobs by '
         'N50. It awaits write-off as a debit to the costing profit and loss account.'],
        ['**(f) Administration Cost N30 Cr**', 'A credit balance is the opposite: '
         '**over-absorbed administration cost** — jobs were charged N30 more administration '
         'overhead than was actually incurred. It will be credited to the costing profit and '
         'loss account.'],
      ]}},
      {'key': 'Two rules worth taking away from this question. First, on any overhead account a '
              '**debit balance means under-absorbed** and a **credit balance means '
              'over-absorbed** — the debits are what you spent, the credits are what you '
              'charged. Second, the **contra account always equals the net of everything else**; '
              'that identity is the quickest check on a cost-ledger answer.'}]}},

    # ---- Q5
    {'eg': {'tag': 'Exam type — Q5 (ICAN, May 1995 adapted)',
      't': 'Easy Going Limited — a month in an interlocking cost ledger',
      'q': [
      {'p': 'The following trial balance was extracted from the books of Easy Going Limited on '
            '1 January 2010:'},
      {'stmt': {'t': 'Opening trial balance, 1 January 2010', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Raw materials', 18000, ''],
        ['Work-in-progress', 27000, ''],
        ['Finished goods', 9000, ''],
        ['General ledger control a/c', '', 54000],
        ['', 54000, 54000, '@tt'],
      ]}},
      {'p': 'The company keeps **separate** cost accounting records. Transactions for January '
            '2010 are given below:'},
      {'stmt': {'t': 'Transactions for January 2010', 'rows': [
        ['Raw materials purchased', '', 59000],
        ['Direct wages', '', 40000],
        ['Indirect wages', '', 7200],
        ['Administration salaries', '', 6800],
        ['Selling and distribution expenses', '', 4400],
        ['Administration expenses', '', 7500],
        ['Production expenses', '', 4000],
        ['Stores issued —  Production', '', 33100],
        ['Stores issued —  Factory maintenance', '', 2070],
        ['Stores issued —  Administration', '', 1000],
        ['Production overhead absorbed', '', 14000],
        ['Administration overhead absorbed by finished goods', '', 15000],
        ['Selling and distribution overhead absorbed by sales', '', 11000],
        ['Factory cost of finished goods', '', 78000],
        ['Cost of finished goods sold', '', 80000],
        ['Sales', '', 120000],
      ]}},
      {'p': '**Required:** Record the transactions for the month and prepare a Costing Profit '
            'and Loss Account and a Trial Balance as at the end of the month.'},
      {'warn': 'This question is **mis-typeset in the study text**: the sixteen captions and the '
               'sixteen figures are printed in two columns that have come apart, so no figure '
               'sits beside its own caption, and one caption ("Production overhead absorbed") is '
               'printed twice. The layout above restores the one-to-one, in-order pairing, and '
               'reads the duplicated caption as **"Administration overhead absorbed by finished '
               'goods"** — the item the rest of the question plainly needs. Two independent '
               'checks support the reconstruction: administration overhead *incurred* then comes '
               'to $6{,}800 + 7{,}500 + 1{,}000 = N15{,}300$ against N15,000 absorbed (a '
               'plausible N300 under-absorption), and production overhead incurred comes to '
               '$7{,}200 + 4{,}000 + 2{,}070 = N13{,}270$ against N14,000 absorbed. Treat the '
               'figures as a well-supported reconstruction rather than as certainly what the '
               '1995 paper printed, and work the **method**, which is what the examiner is '
               'testing.', 'lbl': 'Source data mis-typeset — reconstruction'}],
      'a': [
      {'h4': 'The ledger accounts'},
      {'tacc': {'t': 'Stores Ledger (Raw Materials) Control Account',
        'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 18000], ['General ledger control (purchases)', 59000],
               ['', 77000, '@tot'], ['Balance b/d', 40830]],
        'cr': [['Work-in-progress (production)', 33100],
               ['Production overhead (factory maintenance)', 2070],
               ['Administration overhead', 1000], ['Balance c/d', 40830],
               ['', 77000, '@tot']]}},
      {'tacc': {'t': 'Wages Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['General ledger control', 47200], ['', 47200, '@tot']],
        'cr': [['Work-in-progress (direct)', 40000],
               ['Production overhead (indirect)', 7200], ['', 47200, '@tot']]}},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Stores (factory maintenance)', 2070], ['Wages control (indirect)', 7200],
               ['General ledger control (production expenses)', 4000],
               ['Costing P&L (over-absorbed)', 730], ['', 14000, '@tot']],
        'cr': [['Work-in-progress (absorbed)', 14000], ['', 14000, '@tot']]}},
      {'tacc': {'t': 'Administration Overhead Control Account', 'drl': 'Dr  (N)',
        'crl': 'Cr  (N)',
        'dr': [['General ledger control (salaries)', 6800],
               ['General ledger control (expenses)', 7500], ['Stores', 1000],
               ['', 15300, '@tot']],
        'cr': [['Finished goods (absorbed)', 15000],
               ['Costing P&L (under-absorbed)', 300], ['', 15300, '@tot']]}},
      {'tacc': {'t': 'Selling & Distribution Overhead Control Account', 'drl': 'Dr  (N)',
        'crl': 'Cr  (N)',
        'dr': [['General ledger control', 4400], ['Costing P&L (over-absorbed)', 6600],
               ['', 11000, '@tot']],
        'cr': [['Cost of sales (absorbed)', 11000], ['', 11000, '@tot']]}},
      {'tacc': {'t': 'Work-in-Progress Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 27000], ['Stores ledger control', 33100],
               ['Wages control (direct)', 40000], ['Production overhead absorbed', 14000],
               ['', 114100, '@tot'], ['Balance b/d', 36100]],
        'cr': [['Finished goods (factory cost)', 78000], ['Balance c/d', 36100],
               ['', 114100, '@tot']]}},
      {'tacc': {'t': 'Finished Goods Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 9000], ['Work-in-progress', 78000],
               ['Administration overhead absorbed', 15000], ['', 102000, '@tot'],
               ['Balance b/d', 22000]],
        'cr': [['Cost of sales', 80000], ['Balance c/d', 22000], ['', 102000, '@tot']]}},
      {'tacc': {'t': 'Cost of Sales Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Finished goods control', 80000],
               ['Selling & distribution OH absorbed', 11000], ['', 91000, '@tot']],
        'cr': [['Costing Profit and Loss', 91000], ['', 91000, '@tot']]}},
      {'tacc': {'t': 'Sales Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Costing Profit and Loss', 120000]],
        'cr': [['General ledger control', 120000]]}},
      {'h4': 'Costing Profit and Loss Account'},
      {'stmt': {'t': 'Costing Profit and Loss Account for January 2010', 'rows': [
        ['Sales', '', 120000],
        ['Less: Cost of sales (80,000 + 11,000 S&D absorbed)', '', 91000],
        ['**Profit before overhead adjustments**', '', 29000, '@t'],
        '@gap',
        ['Add:  Production overhead over-absorbed', 730, ''],
        ['          Selling & distribution overhead over-absorbed', 6600, 7330],
        ['Less: Administration overhead under-absorbed', '', -300],
        ['**Costing net profit**', '', 36030, '@tt'],
      ]}},
      {'h4': 'Closing trial balance'},
      {'stmt': {'t': 'Trial balance as at 31 January 2010', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Raw materials (stores ledger) control', 40830, ''],
        ['Work-in-progress control', 36100, ''],
        ['Finished goods control', 22000, ''],
        ['General ledger control a/c', '', 98930],
        ['', 98930, 98930, '@tt'],
      ]}},
      {'note': 'Proof of the contra balance, the same check as in Illustration 6.1: opening '
               'N54,000 + purchases 59,000 + wages 47,200 + production expenses 4,000 + admin '
               'salaries 6,800 + admin expenses 7,500 + S&D expenses 4,400 + profit 36,030 '
               '− sales 120,000 = **N98,930**, and $40{,}830 + 36{,}100 + 22{,}000 = N98{,}930$ '
               '✓'}]}},

    # ---- Q6
    {'eg': {'tag': 'Exam type — Q6', 't': 'Gwammaja PLC — reconciling cost and financial profit',
      'q': [
      {'p': '**(a)** Explain how the results shown by the Cost Accounts and those shown by the '
            'Financial Accounts may be reconciled.'},
      {'p': '**(b)** According to the Cost Accounts of Gwammaja PLC, profit for the year was '
            '**N48,390**. The Financial Accounts disclosed the following position.'},
      {'tacc': {'t': 'Manufacturing Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Raw materials opening inventory', 1900], ['Purchases (less returns)', 54900],
               ['', 56800, '@tot'], ['Less closing inventory', -1800],
               ['Raw materials consumed', 55000], ['Direct labour', 35500],
               ['Factory overhead', 21400], ['', 111900, '@tot'],
               ['WIP: opening 8,400 less closing 8,900', -500], ['', 111400, '@tot']],
        'cr': [['Transfer to finished inventory account', 111400], ['', 111400, '@tot']]}},
      {'tacc': {'t': 'Finished Inventory Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Opening inventory', 11600], ['Transfer from manufacturing a/c', 111400],
               ['', 123000, '@tot']],
        'cr': [['Cost of sales transferred to trading a/c', 110700],
               ['Closing inventory', 12300], ['', 123000, '@tot']]}},
      {'tacc': {'t': 'Trading Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Factory cost of sales from inventory a/c', 110700],
               ['Gross profit c/d', 73800], ['', 184500, '@tot']],
        'cr': [['Sales', 184500], ['', 184500, '@tot']]}},
      {'tacc': {'t': 'Profit and Loss Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Administration expenses', 15600], ['Distribution expenses', 10182],
               ['Discounts allowed', 1511], ['Debenture interest', 850], ['Fines', 500],
               ['Losses of a non-trading nature', 350], ['Net profit', 46944],
               ['', 75937, '@tot']],
        'cr': [['Gross profit b/d', 73800], ['Discount received', 1800],
               ['Bank interest received', 37], ['Dividend received', 300],
               ['', 75937, '@tot']]}},
      {'p': 'Inventory valuations in the **Cost Accounts** were as follows:'},
      {'stmt': {'t': 'Cost account inventory valuations', 'rows': [
        ['', 'Opening (N)', 'Closing (N)', '@hd'],
        ['Raw materials', 1969, 1850],
        ['Work-in-progress', 8280, 8730],
        ['Finished inventory', 11396, 12810],
      ]}},
      {'p': 'Depreciation amounting to **N6,146** was charged in the cost accounts, whereas '
            'factory overhead in the financial accounts included **N5,873** for this expense. '
            'The profit shown in the cost accounts has been arrived at **before** charging the '
            'notional rent of N1,500. You are required to present a logical statement to '
            'reconcile the two profit figures.'},
      {'warn': 'The study text prints the financial net profit as **N46,950** and the profit and '
               'loss account totals as N76,943 (debit) and N75,943 (credit). None of the three '
               'is right. The credits total $73{,}800 + 1{,}800 + 37 + 300 = '
               '**N75{,}937**$ and the listed expenses total $15{,}600 + 10{,}182 + 1{,}511 + '
               '850 + 500 + 350 = N28{,}993$, so net profit is $75{,}937 - 28{,}993 = '
               '**N46,944**$ — six naira below the printed figure. The account above uses the '
               'corrected figures, and the reconciliation below arrives at exactly N46,944 '
               'independently, which confirms them.', 'lbl': 'Source arithmetic error, corrected'}],
      'a': [
      {'h4': '(a)  How the two results are reconciled'},
      {'p': 'Where an interlocking system is used the two profits are reconciled in a '
            '**memorandum reconciliation account** or a vertical reconciliation statement. One '
            'profit figure is taken as the starting point and every cause of difference is added '
            'or deducted until the other is reached. The causes fall into the three groups of '
            '§6.5: appropriations of profit dealt with only in the financial accounts; purely '
            'financial matters outside the scope of the cost accounts; and items given a '
            '**different treatment** in the two sets of books — over/under absorbed overhead, '
            'different inventory and WIP valuations, a different depreciation basis, abnormal '
            'losses, and notional charges made only in the cost accounts.'},
      {'h4': '(b)  Working — classifying every difference'},
      {'table': {'align': 'lrrl', 'head': ['Inventory', 'Financial (N)', 'Cost (N)',
        'Effect of moving from **cost** profit to **financial** profit'], 'rows': [
        ['Raw materials — opening', '1,900', '1,969', 'cost charged 69 more → **add 69**'],
        ['Raw materials — closing', '1,800', '1,850', 'cost credited 50 more → **deduct 50**'],
        ['Work-in-progress — opening', '8,400', '8,280', 'cost charged 120 less → '
         '**deduct 120**'],
        ['Work-in-progress — closing', '8,900', '8,730', 'cost credited 170 less → **add 170**'],
        ['Finished inventory — opening', '11,600', '11,396', 'cost charged 204 less → '
         '**deduct 204**'],
        ['Finished inventory — closing', '12,300', '12,810', 'cost credited 510 more → '
         '**deduct 510**'],
      ]}},
      {'p': 'Depreciation: the cost accounts charged N6,146 against the financial accounts\' '
            'N5,873, i.e. **N273 more**, so costing profit is N273 lower and N273 must be added '
            'back.'},
      {'h4': '(b)  Reconciliation statement'},
      {'stmt': {'t': 'Gwammaja PLC — reconciliation of costing profit with financial profit',
        'rows': [
        ['Profit as per **cost accounts**', '', 48390],
        '@gap',
        ['Add:  income credited in the financial accounts only —', '', '', '@hd'],
        ['Discount received', 1800, ''],
        ['Bank interest received', 37, ''],
        ['Dividend received', 300, ''],
        ['Raw materials opening — overvalued in cost accounts', 69, ''],
        ['Work-in-progress closing — undervalued in cost accounts', 170, ''],
        ['Depreciation overcharged in cost accounts (6,146 − 5,873)', 273, 2649],
        '@gap',
        ['Less: expenses charged in the financial accounts only —', '', '', '@hd'],
        ['Discounts allowed', 1511, ''],
        ['Debenture interest', 850, ''],
        ['Fines', 500, ''],
        ['Losses of a non-trading nature', 350, ''],
        ['Raw materials closing — overvalued in cost accounts', 50, ''],
        ['Work-in-progress opening — undervalued in cost accounts', 120, ''],
        ['Finished inventory opening — undervalued in cost accounts', 204, ''],
        ['Finished inventory closing — overvalued in cost accounts', 510, -4095],
        ['**Profit as per financial accounts**', '', 46944, '@tt'],
      ]}},
      {'note': '$48{,}390 + 2{,}649 - 4{,}095 = N46{,}944$ — which is exactly the net profit '
               'recomputed from the financial profit and loss account above. Two independent '
               'routes to the same figure is the strongest confirmation available that both the '
               'classification and the arithmetic are right.'},
      {'key': '**The notional rent of N1,500 requires no adjustment here.** A notional charge '
              'appears in the cost accounts only, so it would normally have to be added back '
              'when moving to financial profit — but the question states the costing profit was '
              'arrived at *before* charging it, so it has not been charged at all and there is '
              'nothing to reverse. Had the question said "after charging", N1,500 would be '
              'added. This is exactly the trap the examiner built into the question: read the '
              'word **before** or **after** carefully.'}]}},

    # ---- Q7
    {'eg': {'tag': 'Exam type — Q7 (ACCA, Costing, adapted)',
      't': 'Indabawa Limited — a full interlocking cost ledger, including a capital job',
      'q': [
      {'p': 'Indabawa Limited, a company engaged in the manufacture of specialised marine '
            'engines, operates a historic job cost accounting system which is **not** integrated '
            'with the financial accounts. At the beginning of May 2021, the opening balances in '
            'the cost ledger were:'},
      {'stmt': {'t': 'Opening balances, 1 May 2021', 'rows': [
        ['Stores Ledger Control Account', '', 85400],
        ['Work-in-Progress Control Account', '', 167350],
        ['Finished Goods Control Account', '', 49250],
        ['Cost Ledger Control Account', '', 302000],
      ]}},
      {'p': 'During the month, the following transactions took place:'},
      {'stmt': {'t': 'Transactions for May 2021', 'rows': [
        ['Materials:  Purchases', '', 42700],
        ['                   Issues — to production', '', 63400],
        ['                   Issues — to general maintenance', '', 1450],
        ['                   Issues — to the construction of manufacturing equipment', '', 7650],
        ['Factory wages:  Total gross wages paid', '', 124000],
      ]}},
      {'ul': [
        '**N12,500** of the above gross wages were incurred on the construction of manufacturing '
        'equipment, **N35,750** were indirect wages, and the balance was direct.',
        '**Production overheads:** actual amount incurred, excluding items shown above, was '
        '**N152,350**; **N30,000** was absorbed by the manufacturing equipment under '
        'construction, and under-absorbed overheads written off at the end of the month amounted '
        'to **N7,550**.',
        '**Royalty payments:** one of the engines produced is manufactured under licence. '
        '**N2,150** will be paid to the inventor for the month\'s production of that particular '
        'engine.',
        '**Selling overheads** N22,000; **Sales** N410,000.',
        'The company\'s **gross profit margin is 25% on factory cost**.',
        'At the end of May, the inventory of work-in-progress had **increased by N12,000**. The '
        'manufacturing equipment under construction was completed within the month and '
        'transferred out of the cost ledger at the end of the month.',
      ]},
      {'p': '**Required:** Prepare the relevant control accounts, costing profit and loss '
            'account, and any other accounts you consider necessary to record the above '
            'transactions in the cost ledger for May 2021.'},
      {'warn': 'The study text prints the wages spent on the capital job as **N125,000**, which '
               'is more than the N124,000 of total gross wages — impossible. It is **N12,500**; '
               'with that figure the whole question closes exactly (the Cost Ledger Control '
               'balance at the month end equals the sum of the three closing inventory '
               'balances), which it cannot do on any other reading. The materials section is '
               'also printed with its captions out of step with its figures — the N63,400 '
               'issue has no caption at all; it is the issue **to production**.',
       'lbl': 'Source errors corrected'}],
      'a': [
      {'h4': 'Step 1 — split the wages and the overhead before touching any account'},
      {'stmt': {'t': 'Analysis of the N124,000 gross wages', 'rows': [
        ['Capital job — construction of manufacturing equipment', '', 12500],
        ['Indirect wages', '', 35750],
        ['Direct wages *(balance)*', '', 75750],
        ['', '', 124000, '@tt'],
      ]}},
      {'stmt': {'t': 'Analysis of production overhead', 'rows': [
        ['Incurred:  indirect materials (general maintenance)', 1450, ''],
        ['                 indirect wages', 35750, ''],
        ['                 other production overhead', 152350, 189550],
        '@gap',
        ['Absorbed by the capital job', 30000, ''],
        ['Under-absorbed, written off to costing P&L', 7550, ''],
        ['Absorbed by production (WIP) *(balance)*', 152000, 189550],
      ]}},
      {'h4': 'Step 2 — the two figures the narrative hides'},
      {'p': 'Gross profit is 25% **on factory cost**, so sales are 125% of the factory cost of '
            'goods sold:'},
      {'tex': '\\text{Factory cost of sales} = \\frac{410{,}000}{1.25} = N328{,}000'},
      {'p': 'And closing WIP is the opening balance plus the stated increase:'},
      {'tex': '\\text{Closing WIP} = 167{,}350 + 12{,}000 = N179{,}350'},
      {'h4': 'Step 3 — the control accounts'},
      {'tacc': {'t': 'Stores Ledger Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 85400], ['Cost ledger control (purchases)', 42700],
               ['', 128100, '@tot'], ['Balance b/d', 55600]],
        'cr': [['Work-in-progress (production)', 63400],
               ['Production overhead (maintenance)', 1450],
               ['Capital job — manufacturing equipment', 7650], ['Balance c/d', 55600],
               ['', 128100, '@tot']]}},
      {'tacc': {'t': 'Wages Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cost ledger control', 124000], ['', 124000, '@tot']],
        'cr': [['Work-in-progress (direct)', 75750],
               ['Production overhead (indirect)', 35750],
               ['Capital job — manufacturing equipment', 12500], ['', 124000, '@tot']]}},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Stores ledger control', 1450], ['Wages control', 35750],
               ['Cost ledger control (other overheads)', 152350], ['', 189550, '@tot']],
        'cr': [['Work-in-progress (absorbed)', 152000],
               ['Capital job — manufacturing equipment', 30000],
               ['Costing P&L (under-absorbed)', 7550], ['', 189550, '@tot']]}},
      {'tacc': {'t': 'Work-in-Progress Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 167350], ['Stores ledger control', 63400],
               ['Wages control (direct)', 75750], ['Production overhead absorbed', 152000],
               ['Cost ledger control (royalty)', 2150], ['', 460650, '@tot'],
               ['Balance b/d', 179350]],
        'cr': [['Finished goods *(balancing figure)*', 281300], ['Balance c/d', 179350],
               ['', 460650, '@tot']]}},
      {'tacc': {'t': 'Finished Goods Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 49250], ['Work-in-progress', 281300], ['', 330550, '@tot'],
               ['Balance b/d', 2550]],
        'cr': [['Cost of sales', 328000], ['Balance c/d *(balancing figure)*', 2550],
               ['', 330550, '@tot']]}},
      {'tacc': {'t': 'Capital Job — Manufacturing Equipment Under Construction',
        'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Stores ledger control', 7650], ['Wages control', 12500],
               ['Production overhead absorbed', 30000], ['', 50150, '@tot']],
        'cr': [['Cost ledger control (completed, transferred out)', 50150],
               ['', 50150, '@tot']]}},
      {'note': 'The capital job is the part of this question that separates good answers from '
               'average ones. The equipment is being built **by the company for itself**, so its '
               'cost is collected exactly like any other job — materials, wages and absorbed '
               'overhead — but on completion it does **not** go to finished goods, because it is '
               'not for sale. It leaves the cost ledger altogether, through the Cost Ledger '
               'Control Account, to be capitalised as a fixed asset in the financial ledger.',
       'lbl': 'Why the capital job leaves the cost ledger'},
      {'h4': 'Step 4 — the costing profit and loss account'},
      {'stmt': {'t': 'Costing Profit and Loss Account for May 2021', 'rows': [
        ['Sales', '', 410000],
        ['Less: factory cost of sales', '', 328000],
        ['**Gross profit** (25% of factory cost)', '', 82000, '@t'],
        '@gap',
        ['Less: under-absorbed production overhead', 7550, ''],
        ['          selling overheads', 22000, 29550],
        ['**Net profit for the month**', '', 52450, '@tt'],
      ]}},
      {'h4': 'Step 5 — the Cost Ledger Control Account, and the proof'},
      {'tacc': {'t': 'Cost Ledger Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Sales', 410000], ['Manufacturing equipment transferred out', 50150],
               ['Balance c/d', 237500], ['', 697650, '@tot']],
        'cr': [['Balance b/f', 302000], ['Stores ledger control (purchases)', 42700],
               ['Wages control', 124000], ['Production overhead control', 152350],
               ['Work-in-progress (royalty)', 2150], ['Selling overheads', 22000],
               ['Costing P&L (net profit)', 52450], ['', 697650, '@tot'],
               ['Balance b/d', 237500]]}},
      {'stmt': {'t': 'Trial balance at 31 May 2021', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Stores ledger control', 55600, ''],
        ['Work-in-progress control', 179350, ''],
        ['Finished goods control', 2550, ''],
        ['Cost ledger control', '', 237500],
        ['', 237500, 237500, '@tt'],
      ]}},
      {'key': 'The trial balance closing cleanly at N237,500 on both sides is the proof that '
              'every one of the fifteen postings above is right — and it is also the proof that '
              'the capital-job wages figure must be N12,500 and not the N125,000 the book '
              'prints, because no other figure makes the ledger close.'}]}},

    # ---- Q6.8
    {'eg': {'tag': 'Exam type — Q6.8',
      't': 'Chiroki and Ibro Nig. Ltd — working back from financial profit to costing profit',
      'q': [
      {'p': 'Chiroki and Ibro Nig. Ltd maintained separate cost and financial accounts, and the '
            'costing profit for 2020 differed from that revealed in the financial accounts, '
            'which was shown as **N50,000**.'},
      {'p': '**(i)** The following information is available:'},
      {'stmt': {'t': 'Inventory valuations', 'rows': [
        ['', 'Cost accounts (N)', 'Financial accounts (N)', '@hd'],
        ['Opening inventory of raw materials', 5000, 5500],
        ['Closing inventory of raw materials', 4000, 5300],
        ['Opening inventory of finished goods', 12000, 15000],
        ['Closing inventory of finished goods', 14000, 16000],
      ]}},
      {'ul': [
        '**(ii)** The company received a dividend of **N1,000**.',
        '**(iii)** A machine with a net book value of **N10,000** was sold during the year for '
        '**N8,000**.',
        '**(iv)** The company charged **10% interest on its opening capital employed of '
        'N80,000** to its process costs.',
      ]},
      {'p': '**Required:** (i) Determine the profit figure shown in the cost accounts. '
            '(ii) Explain the advantages a business might obtain from the integration of cost '
            'and financial accounting data.'}],
      'a': [
      {'h4': '(i)  Working — classify each item first'},
      {'ol': [
        '**Dividend received N1,000** — income in the financial accounts only (§6.5.2), so it '
        'inflates financial profit relative to costing profit: **deduct**.',
        '**Loss on sale of the machine** — sold for N8,000 against a net book value of N10,000, '
        'so a **loss of N2,000**, charged in the financial accounts only: **add back**.',
        '**Notional interest on capital** — $10\\% \\times 80{,}000 = **N8{,}000**$, charged to '
        'process costs in the cost accounts only. It depresses costing profit, so: **deduct**.',
        '**Raw materials opening** — cost N5,000 vs financial N5,500: cost charged N500 less, so '
        'costing profit is N500 higher: **add**.',
        '**Raw materials closing** — cost N4,000 vs financial N5,300: cost credited N1,300 less, '
        'so costing profit is N1,300 lower: **deduct**.',
        '**Finished goods opening** — cost N12,000 vs financial N15,000: cost charged N3,000 '
        'less, so costing profit is N3,000 higher: **add**.',
        '**Finished goods closing** — cost N14,000 vs financial N16,000: cost credited N2,000 '
        'less, so costing profit is N2,000 lower: **deduct**.',
      ]},
      {'stmt': {'t': 'Reconciliation — financial profit to costing profit', 'rows': [
        ['Profit as per **financial** accounts', '', 50000],
        '@gap',
        ['Add:  loss on sale of machine (10,000 − 8,000), financial books only', 2000, ''],
        ['          raw materials opening — undervalued in cost accounts', 500, ''],
        ['          finished goods opening — undervalued in cost accounts', 3000, 5500],
        '@gap',
        ['Less: dividend received, financial books only', 1000, ''],
        ['          notional interest on capital (10% × 80,000), cost books only', 8000, ''],
        ['          raw materials closing — undervalued in cost accounts', 1300, ''],
        ['          finished goods closing — undervalued in cost accounts', 2000, -12300],
        ['**Profit as per cost accounts**', '', 43200, '@tt'],
      ]}},
      {'tex': '50{,}000 + 5{,}500 - 12{,}300 = N43{,}200'},
      {'note': 'Watch the **direction of travel**. Here you are going *from* financial profit '
               '*to* costing profit, which is the reverse of Illustration 6.2 and of Q6 above, '
               'so every sign flips. The safest habit: write at the top of your working which '
               'profit you are starting from, then ask of each item "does this make the '
               'destination figure bigger or smaller?" rather than trying to remember a rule.'},
      {'h4': '(ii)  Advantages of integrating cost and financial accounting data'},
      {'ol': [
        '**Only one set of records** is maintained, saving the clerical labour and the staff '
        'cost of writing up two.',
        '**No reconciliation is needed** — this entire exercise disappears, along with the time '
        'and the risk of error in it.',
        '**A single profit figure**, so management and shareholders are never shown two '
        'different answers to the same question.',
        '**Consistent data** — cost and financial information come from the same source entry, '
        'so they cannot drift apart.',
        '**Faster management reporting**, because information does not wait on a '
        'reconciliation.',
        '**Lower risk of error and fraud**, since there is one control framework rather than two '
        'partially-overlapping ones.',
        '**Easier audit**, as the auditor traces one trail rather than two.',
      ]}]}},

    # ---- Q6.9
    {'eg': {'tag': 'Exam type — Q6.9 (12½ marks)',
      't': 'Tamsat Limited — an integrated ledger for the period',
      'q': [
      {'p': 'You are provided with the extracted operational data of Tamsat Limited.'},
      {'stmt': {'t': 'Opening trial balance as at 1 January 2022', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Work-in-progress', 25000, ''],
        ['Stores ledger control a/c', 10000, ''],
        ['Finished goods control a/c', 20000, ''],
        ['Fixed assets (non-current assets)', 80000, ''],
        ['Creditors for material', '', 30000],
        ['Provision for depreciation on fixed assets', '', 10000],
      ]}},
      {'stmt': {'t': 'Transactions for the period ended 31 January', 'rows': [
        ['Materials purchased', '', 70000],
        ['Normal loss on materials', '', 3000],
        ['Direct materials issued', '', 50000],
        ['Indirect materials issued to factory', '', 6000],
        ['Wages allocated as direct to factory', 35000, ''],
        ['Wages allocated as indirect to factory', 10000, ''],
        ['Total wages incurred', '', 45000],
        ['Production overhead incurred', '', 12000],
        ['Production overhead absorbed', '', 24000],
        ['Output for the period', '', 100000],
      ]}},
      {'p': '**Required:** (a) Using integrated accounts, produce the following ledgers: '
            '(i) stores ledger; (ii) wages control account; (iii) production overhead control '
            'account; (iv) work-in-progress control account; and (v) finished goods account. '
            '(b) Prepare the closing trial balance.'},
      {'warn': 'Two defects in the printed question. **(1)** The transaction list\'s captions '
               'and figures are out of step: the line "Wages allocated as indirect to factory" '
               'is printed **twice** (the first should read "as **direct**"), and the figures '
               'N35,000 and N10,000 shown against "Total wages incurred" and "Production '
               'overhead incurred" are in fact the two wage allocations — confirmed by '
               '$35{,}000 + 10{,}000 = N45{,}000$, the total wages figure. Everything below '
               'shifts up one line accordingly. **(2)** The opening trial balance does not '
               'balance: debits total N135,000 and credits only N40,000. A **capital (owner\'s '
               'equity) balance of N95,000** is missing from the printed credit column and has '
               'been restored below.', 'lbl': 'Source errors corrected'}],
      'a': [
      {'h4': 'Assumptions stated before starting'},
      {'ul': [
        'The question gives **no cash payments**, so the purchases, wages and overheads are all '
        'taken as still owing at the period end (creditors, wages payable, creditors for '
        'overhead).',
        '**Normal loss on materials** is written off as a period charge. (An equally defensible '
        'treatment is to debit it to production overhead, where it would then be absorbed into '
        'the cost of good output; the figures below note the effect.)',
        'No sales are given, so the finished goods produced simply accumulate; there is no '
        'trading result for the period, only the losses below.',
      ]},
      {'h4': '(a)(i)  Stores Ledger Control Account'},
      {'tacc': {'t': 'Stores Ledger Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 10000], ['Creditors for material (purchases)', 70000],
               ['', 80000, '@tot'], ['Balance b/d', 21000]],
        'cr': [['Work-in-progress (direct materials)', 50000],
               ['Production overhead (indirect materials)', 6000],
               ['Profit & Loss (normal loss)', 3000], ['Balance c/d', 21000],
               ['', 80000, '@tot']]}},
      {'h4': '(a)(ii)  Wages Control Account'},
      {'tacc': {'t': 'Wages Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Wages payable / bank', 45000], ['', 45000, '@tot']],
        'cr': [['Work-in-progress (direct)', 35000],
               ['Production overhead (indirect)', 10000], ['', 45000, '@tot']]}},
      {'h4': '(a)(iii)  Production Overhead Control Account'},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Stores ledger control (indirect materials)', 6000],
               ['Wages control (indirect wages)', 10000],
               ['Creditors (overhead incurred)', 12000], ['', 28000, '@tot']],
        'cr': [['Work-in-progress (absorbed)', 24000],
               ['Profit & Loss (under-absorbed)', 4000], ['', 28000, '@tot']]}},
      {'note': 'Overhead incurred $6{,}000 + 10{,}000 + 12{,}000 = N28{,}000$ against N24,000 '
               'absorbed → **N4,000 under-absorbed**, written off. Had the N3,000 normal loss '
               'been charged here instead, incurred would be N31,000 and the under-absorption '
               'N7,000 — the final loss for the period is the same either way, only its '
               'description changes.'},
      {'h4': '(a)(iv)  Work-in-Progress Control Account'},
      {'tacc': {'t': 'Work-in-Progress Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 25000], ['Stores ledger control', 50000],
               ['Wages control (direct)', 35000], ['Production overhead absorbed', 24000],
               ['', 134000, '@tot'], ['Balance b/d', 34000]],
        'cr': [['Finished goods (output for the period)', 100000],
               ['Balance c/d *(balancing figure)*', 34000], ['', 134000, '@tot']]}},
      {'h4': '(a)(v)  Finished Goods Control Account'},
      {'tacc': {'t': 'Finished Goods Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 20000], ['Work-in-progress (output)', 100000],
               ['', 120000, '@tot'], ['Balance b/d', 120000]],
        'cr': [['Balance c/d', 120000], ['', 120000, '@tot']]}},
      {'h4': '(b)  Closing trial balance'},
      {'stmt': {'t': 'Tamsat Limited — trial balance as at 31 January 2022', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Stores ledger control', 21000, ''],
        ['Work-in-progress control', 34000, ''],
        ['Finished goods control', 120000, ''],
        ['Fixed assets (non-current assets)', 80000, ''],
        ['Profit & Loss — normal loss 3,000 + under-absorbed overhead 4,000', 7000, ''],
        ['Creditors for material (30,000 + 70,000)', '', 100000],
        ['Wages payable', '', 45000],
        ['Creditors for production overhead', '', 12000],
        ['Provision for depreciation on fixed assets', '', 10000],
        ['Capital', '', 95000],
        ['', 262000, 262000, '@tt'],
      ]}},
      {'key': 'That the trial balance closes at N262,000 both sides is itself the evidence for '
              'the N95,000 capital figure restored in the question — the printed opening trial '
              'balance is N95,000 light, and supplying it is the only way the closing balance '
              'can be struck at all. Note too what makes this an **integrated** ledger: there is '
              'no Cost Ledger Contra Account anywhere. Creditors, wages payable and fixed assets '
              'sit in the same ledger as work-in-progress.'}]}},

    # ---- Q6.10
    {'eg': {'tag': 'Exam type — Q6.10 (12½ marks)',
      't': 'Wusu — a full interlocking ledger for April 2021',
      'q': [
      {'p': 'The trial balance of Wusu on 31 March 2021 is provided below.'},
      {'stmt': {'t': 'Trial balance, 31 March 2021', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Stores ledger control account', 20000, ''],
        ['Work-in-progress control account', 30000, ''],
        ['Finished goods control account', 10000, ''],
        ['Cost ledger contra / general ledger adjustment account', '', 60000],
        ['', 60000, 60000, '@tt'],
      ]}},
      {'p': 'The extracted details for April 2021 transactions are:'},
      {'stmt': {'t': 'Transactions for April 2021', 'rows': [
        ['Purchase of stores', '', 70000],
        ['Returned to suppliers', '', 15000],
        ['Normal loss in stores', '', 1000],
        ['Direct materials issued to production', '', 50000],
        ['Stores issued to maintenance', '', 5000],
        ['Wages allocated as direct', 25000, ''],
        ['Indirect factory wages', 8000, ''],
        ['Total wages incurred', '', 33000],
        ['Production overhead incurred', '', 9000],
        ['Production overhead recovered', '', 22000],
        ['Output for the period', '', 120000],
      ]}},
      {'p': '**Required:** Prepare the following ledgers: (i) cost ledger contra account; '
            '(ii) stores/raw materials ledger control account; (iii) wages control account; '
            '(iv) production overhead control account; (v) work-in-progress control account; '
            '(vi) finished goods account; (vii) closing trial balance at 30 April 2021.'},
      {'warn': 'As in Q6.9, the printed transaction list has its captions and figures out of '
               'step from the wages line onwards. The restoration above is confirmed twice over: '
               '$25{,}000 + 8{,}000 = N33{,}000$, the stated total wages; and production '
               'overhead then comes to $5{,}000 + 8{,}000 + 9{,}000 = N22{,}000$ incurred '
               'against N22,000 recovered — an exact match, which is almost certainly what the '
               'question intended.', 'lbl': 'Source data realigned'}],
      'a': [
      {'h4': '(ii)  Stores / Raw Materials Ledger Control Account'},
      {'tacc': {'t': 'Stores Ledger Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 20000], ['Cost ledger contra (purchases)', 70000],
               ['', 90000, '@tot'], ['Balance b/d', 19000]],
        'cr': [['Cost ledger contra (returns to suppliers)', 15000],
               ['Costing P&L (normal loss)', 1000],
               ['Work-in-progress (direct materials)', 50000],
               ['Production overhead (maintenance)', 5000], ['Balance c/d', 19000],
               ['', 90000, '@tot']]}},
      {'h4': '(iii)  Wages Control Account'},
      {'tacc': {'t': 'Wages Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Cost ledger contra', 33000], ['', 33000, '@tot']],
        'cr': [['Work-in-progress (direct)', 25000],
               ['Production overhead (indirect factory wages)', 8000], ['', 33000, '@tot']]}},
      {'h4': '(iv)  Production Overhead Control Account'},
      {'tacc': {'t': 'Production Overhead Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Stores ledger control (maintenance)', 5000],
               ['Wages control (indirect)', 8000],
               ['Cost ledger contra (overhead incurred)', 9000], ['', 22000, '@tot']],
        'cr': [['Work-in-progress (recovered)', 22000], ['', 22000, '@tot']]}},
      {'note': 'Incurred N22,000, recovered N22,000 — **neither under- nor over-absorbed**, so '
               'nothing goes to the profit and loss account from this account. That exact match '
               'is unusual in practice and is the strongest evidence that the realignment of the '
               'printed data above is the reading the examiner intended.'},
      {'h4': '(v)  Work-in-Progress Control Account'},
      {'tacc': {'t': 'Work-in-Progress Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 30000], ['Stores ledger control', 50000],
               ['Wages control (direct)', 25000], ['Production overhead recovered', 22000],
               ['', 127000, '@tot'], ['Balance b/d', 7000]],
        'cr': [['Finished goods (output for the period)', 120000],
               ['Balance c/d *(balancing figure)*', 7000], ['', 127000, '@tot']]}},
      {'h4': '(vi)  Finished Goods Control Account'},
      {'tacc': {'t': 'Finished Goods Control Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Balance b/f', 10000], ['Work-in-progress (output)', 120000],
               ['', 130000, '@tot'], ['Balance b/d', 130000]],
        'cr': [['Balance c/d', 130000], ['', 130000, '@tot']]}},
      {'h4': '(i)  Cost Ledger Contra (General Ledger Adjustment) Account'},
      {'tacc': {'t': 'Cost Ledger Contra Account', 'drl': 'Dr  (N)', 'crl': 'Cr  (N)',
        'dr': [['Stores ledger control (returns to suppliers)', 15000],
               ['Costing P&L (normal loss written off)', 1000], ['Balance c/d', 156000],
               ['', 172000, '@tot']],
        'cr': [['Balance b/f', 60000], ['Stores ledger control (purchases)', 70000],
               ['Wages control', 33000], ['Production overhead control', 9000],
               ['', 172000, '@tot'], ['Balance b/d', 156000]]}},
      {'h4': '(vii)  Closing trial balance'},
      {'stmt': {'t': 'Wusu — trial balance as at 30 April 2021', 'rows': [
        ['', 'Dr (N)', 'Cr (N)', '@hd'],
        ['Stores ledger control', 19000, ''],
        ['Work-in-progress control', 7000, ''],
        ['Finished goods control', 130000, ''],
        ['Cost ledger contra account', '', 156000],
        ['', 156000, 156000, '@tt'],
      ]}},
      {'key': 'The same identity as always: $19{,}000 + 7{,}000 + 130{,}000 = N156{,}000$. No '
              'sales were given, so there is no trading profit — only the N1,000 normal loss, '
              'which is why it is the single item routed through the costing profit and loss '
              'account and out to the contra.'}]}},

    # ---- Q6.11
    {'eg': {'tag': 'Exam type — Q6.11', 't': 'Dambat Limited — why profits differ, and a short '
                                             'reconciliation',
      'q': [
      {'p': '**(a)** Dambat Limited is a medium-size firm that has been in existence for the '
            'past five years. The firm uses an interlocking system in its Cost Accounting '
            'Department. It has been observed that the profit disclosed in the costing '
            'department\'s books differs from the profit disclosed in the financial reports '
            'generated in the Financial Accounting Department.'},
      {'ol': [
        'Why are profits disclosed in the cost accounting department different from those of the '
        'financial accounting department?',
        'List **four** items that are recorded in the financial books only.',
        'List **two** items that are considered in the cost accounting books only.',
      ]},
      {'p': '**(b)** Given below are extracted data from both financial and costing books:'},
      {'stmt': {'t': 'Extracted data', 'rows': [
        ['Financial books:', '', '', '@hd'],
        ['Opening inventory of raw materials', '', 6000],
        ['Closing inventory of raw materials', '', 7000],
        '@gap',
        ['Costing books:', '', '', '@hd'],
        ['Opening inventory of raw materials', '', 5000],
        ['Closing inventory of raw materials', '', 12000],
        '@gap',
        ['Other details:', '', '', '@hd'],
        ['Interest received on investment', '', 2000],
        ['Profit on sale of fixed asset (non-current asset)', '', 1000],
        ['Profit disclosed in financial books', '', 77000],
        ['Profit disclosed in costing books', '', 80000],
      ]}},
      {'p': '**Required:** Reconcile the differences in the profits disclosed in both books.'}],
      'a': [
      {'h4': '(a)(i)  Why the two profits differ'},
      {'p': 'Under an interlocking system the two sets of books are kept independently, for '
            'different purposes and on different conventions, so the same period\'s trading can '
            'produce two different profits. The causes fall into the three groups of §6.5:'},
      {'ol': [
        '**Appropriations of profit** recorded only in the financial accounts — tax, dividends, '
        'transfers to reserves, amounts written off goodwill and preliminary expenses.',
        '**Purely financial matters** outside the scope of cost accounting — interest and rent '
        'received, profits and losses on disposals of fixed assets or investments, fines, '
        'damages, debenture interest.',
        '**Different treatment of the same item** in the two sets of books — over- and '
        'under-absorbed overhead, different inventory and work-in-progress valuation bases, a '
        'different depreciation basis, abnormal losses, and notional charges (notional rent, '
        'interest on capital) that appear in the cost books alone.',
      ]},
      {'h4': '(a)(ii)  Four items recorded in the financial books only'},
      {'ol': [
        '**Interest received** on bank deposits and investments.',
        '**Dividends paid** on share capital, and **corporate tax** — appropriations of profit.',
        '**Profit or loss on the sale** of fixed assets or investments.',
        '**Fines, penalties and damages** payable at law, and **debenture interest**.',
      ]},
      {'h4': '(a)(iii)  Two items considered in the cost books only'},
      {'ol': [
        '**Notional charges** — notional rent on premises the business owns outright, and '
        'notional interest charged on capital employed, included so the product cost reflects '
        'the full normal cost of operating.',
        '**Absorbed (rather than actual) overhead**, charged to jobs at a predetermined rate — '
        'the financial accounts only ever record the actual expenditure.',
      ]},
      {'h4': '(b)  The reconciliation'},
      {'p': 'First classify the two inventory differences, using the rule from §6.5:'},
      {'table': {'align': 'lrrl', 'head': ['Raw materials', 'Financial (N)', 'Costing (N)',
        'Effect on **costing** profit'], 'rows': [
        ['Opening inventory', '6,000', '5,000', 'cost charged 1,000 less → costing profit '
         '**1,000 higher**'],
        ['Closing inventory', '7,000', '12,000', 'cost credited 5,000 more → costing profit '
         '**5,000 higher**'],
      ]}},
      {'stmt': {'t': 'Dambat Limited — reconciliation of costing and financial profits', 'rows': [
        ['Profit as per **costing** books', '', 80000],
        '@gap',
        ['Add: items credited in the financial books only —', '', '', '@hd'],
        ['Interest received on investment', 2000, ''],
        ['Profit on sale of fixed asset', 1000, 3000],
        '@gap',
        ['Less: inventory valuation differences —', '', '', '@hd'],
        ['Opening raw materials undervalued in the costing books (6,000 − 5,000)', 1000, ''],
        ['Closing raw materials overvalued in the costing books (12,000 − 7,000)', 5000, -6000],
        ['**Profit as per financial books**', '', 77000, '@tt'],
      ]}},
      {'tex': '80{,}000 + 3{,}000 - 6{,}000 = N77{,}000 \\;\\checkmark'},
      {'note': 'The reconciliation closes exactly on the N77,000 the question gives for the '
               'financial books, which confirms that all four adjustments have been classified '
               'and signed correctly. When a question supplies **both** profit figures, as this '
               'one does, always finish by checking that your statement actually lands on the '
               'given figure — it converts a guess into a proof.'}]}},
  ]},
 ],

 'formulas': [
   {'lb': 'Splitting a wages total on a direct : indirect ratio',
    'tex': '\\text{Direct wages} = \\frac{d}{d+i} \\times \\text{total wages}, \\qquad '
           '\\text{Indirect wages} = \\frac{i}{d+i} \\times \\text{total wages}',
    'nt': 'Illustration 6.1: an 11 : 2 ratio on N117,000 gives N99,000 direct and N18,000 '
          'indirect. Always add the two parts back to the total as a check.'},
   {'lb': 'Production overhead absorbed',
    'tex': '\\text{Overhead absorbed} = \\text{absorption rate} \\times \\text{actual activity}',
    'nt': 'N3.50 per direct labour hour × 22,000 hours = N77,000 (Illustration 6.1); 80% of '
          'direct labour cost × N3,200 = N2,560 (Illustration 6.3).'},
   {'lb': 'Under- or over-absorbed overhead',
    'tex': '\\text{Under/(over) absorbed} = \\text{overhead incurred} - '
           '\\text{overhead absorbed}',
    'nt': 'A **positive** result is under-absorption — debited to the costing P&L (an extra '
          'expense). A **negative** result is over-absorption — credited to it. On the control '
          'account itself: a debit balance is under-absorbed, a credit balance over-absorbed.'},
   {'lb': 'Cost of goods manufactured (the WIP identity)',
    'tex': '\\text{Finished goods produced} = \\text{opening WIP} + \\text{direct materials} '
           '+ \\text{direct wages} + \\text{overhead absorbed} - \\text{closing WIP}',
    'nt': 'Illustration 6.1: $7{,}000 + 90{,}000 + 99{,}000 + 77{,}000 - 68{,}000 = N205{,}000$.'},
   {'lb': 'Cost of goods sold (the finished goods identity)',
    'tex': '\\text{Cost of goods sold} = \\text{opening finished goods} + '
           '\\text{goods produced} - \\text{closing finished goods}',
    'nt': 'Illustration 6.1: $30{,}000 + 205{,}000 - 45{,}000 = N190{,}000$.'},
   {'lb': 'The interlocking cost ledger\'s trial-balance identity',
    'tex': '\\text{Cost Ledger Contra balance} = \\text{closing stores} + \\text{closing WIP} '
           '+ \\text{closing finished goods}',
    'nt': 'The fastest single check on any interlocking-ledger answer. Illustration 6.1: '
          '$18{,}000 + 68{,}000 + 45{,}000 = N131{,}000$.'},
   {'lb': 'Sales from a margin stated on cost',
    'tex': '\\text{Factory cost of sales} = \\frac{\\text{Sales}}{1 + \\text{margin on cost}}',
    'nt': 'Exam Q7: a 25% margin *on factory cost* means sales are 125% of cost, so '
          '$410{,}000 \\div 1.25 = N328{,}000$. Note this is **not** the same as a 25% margin '
          'on sales, which would give $410{,}000 \\times 0.75 = N307{,}500$.'},
 ],

 'focus':
   'Two things carry the marks in this chapter, and they are different in kind. The first is '
   'knowing the **debit/credit pair** for every transaction cold — and in particular knowing '
   'that an interlocking system routes everything external through the Cost Ledger Contra '
   'Account while an integrated system posts to real accounts directly, which is the only real '
   'difference between the two entry tables. The second is the **reconciliation**, where most '
   'marks go to correctly *classifying* why an item causes a difference (appropriation / purely '
   'financial / different treatment) and getting the direction right, not to the final number. '
   'In computational questions, almost every figure you need is a balancing figure on a '
   'T-account, so work the accounts in a sensible order and finish by checking the contra '
   'balance against the sum of the closing inventories — if those two do not agree, something '
   'is wrong and you still have time to find it.',

 'errors': [
   'Crediting the Raw Materials Control Account instead of the Cost Ledger Control Account when '
   'recording a materials *purchase* under the interlocking system — the double entry runs '
   'through the contra account, not straight into a real supplier account.',
   'Assuming overhead has been fully absorbed because the absorbed figure happens to match some '
   'other number on the page. Always add up the overhead actually **incurred** (indirect '
   'materials + indirect wages + other overhead) and compare. In Illustration 6.1, N77,000 was '
   'absorbed against N74,000 incurred — a N3,000 **over**-absorption which, if missed, '
   'understates the costing profit by exactly that amount.',
   'Getting the sign wrong on an under/over absorption in the profit and loss account. '
   'Under-absorbed = extra expense = **debit**, reducing profit. Over-absorbed = **credit**, '
   'increasing profit. Illustration 6.1 contains one of each, moving profit in opposite '
   'directions.',
   'Netting the six inventory valuation differences off in your head during a reconciliation. '
   'Take raw materials, WIP and finished goods, opening and closing, one at a time through the '
   '"higher opening → lower profit, higher closing → higher profit" rule.',
   'Losing track of which profit you are reconciling **from**. Moving financial → costing and '
   'costing → financial reverse every sign; write the direction at the head of the working '
   'before starting.',
   'Treating dividends received, interest received, profit or loss on asset disposals, fines or '
   'debenture interest as if they belong in cost accounts — these are always purely financial '
   'matters, outside the scope of production.',
   'Forgetting that a memorandum reconciliation account must balance to the same total on '
   '**both** sides. If it does not, an item has been misclassified, omitted, or put on the '
   'wrong side.',
   'Reading "25% gross profit margin **on factory cost**" as a margin on sales. On cost means '
   'sales = 125% of cost, so divide by 1.25; on sales would mean multiply by 0.75. The two give '
   'answers N20,500 apart in Exam Q7.',
   'Sending a self-constructed capital job (Exam Q7\'s manufacturing equipment) to finished '
   'goods. It is not for sale; it leaves the cost ledger through the Cost Ledger Control '
   'Account to be capitalised in the financial ledger.',
   'Adding back a notional charge that the question says has **not** been charged. Exam Q6 '
   'states the costing profit was struck *before* the N1,500 notional rent — so there is '
   'nothing to reverse.',
 ],

 'quiz': {
  'mcq': [
   {'q': 'Under an interlocking cost accounting system, a purchase of raw materials is recorded '
         'by debiting the Raw Materials Control Account and crediting the',
    'o': ['Creditors Account directly', 'Cost Ledger Control Account', 'Sales Account',
          'Work-in-Progress Control Account', 'Finished Goods Account'],
    'a': 1,
    'w': 'Under interlocking accounts, every posting that touches something outside the cost '
         'ledger (like a supplier) routes through the Cost Ledger Control / Contra Account, not '
         'directly to a real external account. That is the single difference between the '
         'interlocking and integrated entry tables.',
    'src': 'Chapter 6.4', 'sec': '6.4'},
   {'q': 'A Production Overhead Control Account shows total debits of N74,000 and has been '
         'credited with N77,000 absorbed into work-in-progress. The N3,000 difference is',
    'o': ['under-absorbed overhead, debited to the costing profit and loss account',
          'over-absorbed overhead, credited to the costing profit and loss account',
          'a posting error that must be corrected',
          'the closing balance of work-in-progress',
          'indirect materials not yet issued'],
    'a': 1,
    'w': 'More was absorbed into jobs (N77,000) than was actually incurred (N74,000), so '
         'overhead is **over**-absorbed by N3,000. It is credited to the costing P&L, '
         'increasing profit — this is exactly the adjustment in Illustration 6.1.',
    'src': 'Chapter 6.4', 'sec': '6.4'},
   {'q': 'In an interlocking cost ledger, the closing balances are: stores N18,000, '
         'work-in-progress N68,000 and finished goods N45,000. The Cost Ledger Contra Account '
         'balance must be',
    'o': ['N45,000 credit', 'N86,000 debit', 'N131,000 credit', 'N131,000 debit',
          'indeterminate without the profit figure'],
    'a': 2,
    'w': 'The contra account is the mirror of everything the cost ledger holds, so its credit '
         'balance always equals the sum of the closing inventory control balances: '
         'N18,000 + N68,000 + N45,000 = N131,000. This identity is the fastest check on any '
         'answer to this style of question.',
    'src': 'Chapter 6.4', 'sec': '6.4'},
   {'q': 'Which of the following would appear in the financial accounts but never in the cost '
         'accounts?',
    'o': ['Direct materials issued to production', 'Dividends paid on share capital',
          'Production overhead absorbed', 'Direct labour cost', 'Work-in-progress'],
    'a': 1,
    'w': 'Dividends paid on share capital are an appropriation of profit, dealt with only in the '
         'financial accounts (§6.5.1), never in the cost accounts.',
    'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': 'Closing inventory is valued at N12,000 in the cost accounts and N7,000 in the '
         'financial accounts. Compared with the financial accounts, the costing profit is',
    'o': ['N5,000 lower', 'N5,000 higher', 'the same', 'N19,000 higher', 'N12,000 higher'],
    'a': 1,
    'w': 'A higher closing inventory means a lower cost of sales, and a lower cost of sales '
         'means a higher profit — so the cost accounts show N5,000 more profit on this item. '
         'Moving from costing profit to financial profit you would therefore deduct N5,000 '
         '(Exam Q6.11).',
    'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': 'A memorandum reconciliation account is used to',
    'o': ['record every transaction of the business', 'replace the trial balance',
          'explain the difference between costing profit and financial profit',
          'calculate the overhead absorption rate', 'record fixed asset purchases only'],
    'a': 2,
    'w': 'The memorandum reconciliation account exists purely to show, item by item, why '
         'costing profit and financial profit differ — "memorandum" meaning it sits outside the '
         'formal double entry.',
    'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': 'Under an integrated accounting system, the number of separate profit and loss '
         'accounts prepared is',
    'o': ['two — one for cost, one for financial purposes', 'three',
          'one, serving both purposes', 'zero — no profit and loss account is prepared', 'four'],
    'a': 2,
    'w': 'The defining feature of an integrated system is that separate costing and financial '
         'P&L accounts are discarded in favour of one unified account — which is why no '
         'reconciliation is ever needed.',
    'src': 'Chapter 6.6', 'sec': '6.6'},
   {'q': 'A charge that is not actually payable, but is included in cost accounts to reflect the '
         'normal cost of running the business, is called a',
    'o': ['sunk cost', 'notional charge', 'opportunity cost', 'committed cost',
          'discretionary cost'],
    'a': 1,
    'w': 'This is the definition of a notional charge — e.g. notional rent on premises the '
         'business owns outright, or notional interest on capital employed, so that the product '
         'cost is comparable with a competitor who rents or borrows.',
    'src': 'Chapter 6.3', 'sec': '6.3'},
   {'q': 'Postings made to a subsidiary ledger under an integrated accounting system, which are '
         'not part of the formal double entry, are known as',
    'o': ['contra entries', 'third entries', 'memorandum entries', 'suspense entries',
          'prelist entries'],
    'a': 1,
    'w': 'The study text calls them **third entries**, precisely to emphasise that they sit '
         'outside the two-sided double entry of the formal records.',
    'src': 'Chapter 6.6', 'sec': '6.6'},
   {'q': 'Where a single account code would need more than 6 digits, the accounts manual should '
         'instead use',
    'o': ['a purely alphabetic code', 'a composite code, suitably structured',
          'no code at all — free text descriptions', 'a randomly generated code',
          'the supplier\'s own invoice number as the code'],
    'a': 1,
    'w': 'A composite code such as 024-824-03 is preferred once a plain single code would exceed '
         'six digits — each chunk can carry its own meaning, which makes the code easier to '
         'remember and partly self-checking.',
    'src': 'Chapter 6.7', 'sec': '6.7'},
   {'q': 'A computerised system that guides a manager toward a decision using available data, '
         'but does not itself offer a pre-determined solution, is best described as a',
    'o': ['transaction processing system', 'decision support system', 'payroll system',
          'general ledger posting system', 'fixed asset register'],
    'a': 1,
    'w': 'A decision support system is deliberately interactive and unstructured — it guides, '
         'the manager still decides — unlike a transaction processing system, built for '
         'fixed-format, high-volume routine postings.',
    'src': 'Chapter 6.8', 'sec': '6.8'},
   {'q': 'In the cost ledger, the account that acts as the focal point of a specific-order '
         'costing system, holding a separate account per job, is the',
    'o': ['Sales Account', 'Cost Ledger Contra Account', 'Work-in-Progress ledger',
          'Finished Goods Control Account', 'Marketing and Admin Overhead Account'],
    'a': 2,
    'w': 'The study text names the WIP ledger explicitly as the focal point of the cost '
         'accounting system under specific-order costing, with a separate account for each job, '
         'each debited with materials, wages and absorbed overhead.',
    'src': 'Chapter 6.3', 'sec': '6.3'},
   {'q': 'Sales are N410,000 and the gross profit margin is 25% on factory cost. The factory '
         'cost of sales is',
    'o': ['N307,500', 'N328,000', 'N512,500', 'N102,500', 'N385,000'],
    'a': 1,
    'w': 'A margin stated **on cost** means sales are 125% of factory cost, so the cost is '
         '410,000 ÷ 1.25 = N328,000. (N307,500 is the trap — that is what you get by treating '
         'it as a 25% margin on *sales*.)',
    'src': 'Chapter 6.11', 'sec': '6.11'},
   {'q': 'A company builds a machine for its own use. On completion, the accumulated cost of the '
         'job in an interlocking cost ledger is',
    'o': ['transferred to the Finished Goods Control Account',
          'transferred out of the cost ledger via the Cost Ledger Control Account',
          'written off to the costing profit and loss account',
          'left permanently in work-in-progress',
          'credited to the Production Overhead Control Account'],
    'a': 1,
    'w': 'The machine is not for sale, so it never becomes finished goods. Its cost leaves the '
         'cost ledger through the Cost Ledger Control Account and is capitalised as a fixed '
         'asset in the financial ledger (Exam Q7, N50,150).',
    'src': 'Chapter 6.11', 'sec': '6.11'},
  ],
  'theory': [
   {'q': 'Explain how the results shown by the Cost Accounts and those shown by the Financial '
         'Accounts may be reconciled.',
    'marks': 8,
    'a': [
      {'p': 'Where interlocking accounts are used, the two profit figures can differ for three '
            'broad reasons: (i) **appropriations of profit** recorded only in the financial '
            'accounts (tax, dividends, transfers to reserves, charitable donations, additional '
            'provisions, amounts written off goodwill and preliminary expenses, sinking-fund '
            'appropriations); (ii) **purely financial matters** outside the scope of cost '
            'accounts (interest and rent received, profits or losses on disposals of fixed '
            'assets and investments, interest on borrowed money, damages, penalties, losses on '
            'premature scrapping); and (iii) items where the **costing treatment itself '
            'differs** from the financial treatment — over- and under-absorbed overhead, '
            'different inventory and WIP valuation bases, a different depreciation basis, and '
            'abnormal losses excluded from the cost accounts.'},
      {'p': 'The reconciliation is carried out using a **memorandum reconciliation account** — '
            'a T-account outside the double entry. One profit figure is entered as the starting '
            'point and every item causing a difference is added on one side or the other until '
            'the second profit figure emerges as the balancing figure, with both sides brought '
            'to the same total. It may equally be presented as a vertical statement: start from '
            'one profit, add every item that made the destination figure larger, deduct every '
            'item that made it smaller, and arrive at the other profit.'},
    ], 'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': 'What do you understand by the term "Integrated Accounting," and what advantages does '
         'it offer compared with separate systems of cost and financial accounting?',
    'marks': 10,
    'a': [
      {'p': 'Integrated accounts, per CIMA, are **a set of accounting records that integrates '
            'both financial and cost accounts using a common input and data for all accounting '
            'purposes** — a single unified ledger rather than two parallel systems requiring '
            'periodic reconciliation. The separate costing profit and loss account is abandoned, '
            'and control accounts for stores, WIP, overhead and finished goods sit in the same '
            'ledger as bank, debtors and creditors.'},
      {'p': '**Advantages**: it saves administrative effort, since only one set of accounts is '
            'kept instead of two; it eliminates duplicated data entry and the staff cost of it; '
            'it removes the need for periodic reconciliation altogether; it eliminates the '
            'confusion of two different profit figures for the same period; it gives cost and '
            'financial staff one version of the truth; and it speeds up management reporting, '
            'which no longer waits on a reconciliation.'},
      {'p': '**The offsetting drawback**: one set of accounts must serve two purposes that can '
            'conflict — external stewardship reporting, which must follow accounting standards, '
            'and internal management decision support, where the cost accountant might prefer, '
            'for instance, a marginal-cost or replacement-cost inventory valuation.'},
    ], 'src': 'Chapter 6.6', 'sec': '6.6'},
   {'q': 'State the principles that should be observed in determining a satisfactory system of '
         'codification of accounts, and explain why an accounts manual is needed.',
    'marks': 10,
    'a': [
      {'p': '**Principles of a good code structure**: it should follow a **logical sequence**, '
            'pulling all common items together so related accounts fall in adjacent ranges; it '
            'should be **flexible** enough to accommodate additions, leaving spare numbers '
            'within each range; it should be arranged in a way that **aids memory**, since '
            'clerks code documents at speed; each code should be **unique** to one account; and '
            'where a code would need more than **six digits**, a **composite code** such as '
            '`024-824-03` should be used instead of one long unbroken number.'},
      {'p': '**Why an accounts manual is needed**: the codes are useless unless everyone uses '
            'the same one for the same thing. The manual lists all current codes with '
            'explanatory notes on their use, so that invoices, requisitions and time-sheets can '
            'be coded **quickly and accurately**. A good manual is **comprehensive, unambiguous '
            'and well indexed**.'},
      {'p': 'The purpose behind all of it: in an organisation of any size the volume of cost and '
            'financial data is too great to assimilate, so data must be summarised under '
            'suitable headings — e.g. indirect materials grouped as cleaning materials, '
            'lubrication, fuel, protective clothing, stationery, small tools, packing material, '
            'foodstuffs, replacement parts and miscellaneous — which reduces the number of '
            'accounts and provides ready-made groupings for budgeting.'},
    ], 'src': 'Chapter 6.7', 'sec': '6.7'},
   {'q': 'Distinguish between a transaction processing system and a decision support system, '
         'and state the advantages of decision support systems to the cost accountant.',
    'marks': 8,
    'a': [
      {'p': '**Transaction processing systems** are designed to handle large volumes of '
            'monotonous transactions arriving from various points, coordinated by a central '
            'server that processes and harmonises the mass of data. They have **set functions**, '
            'and their formats cannot easily be amended without the intervention of data '
            'processing experts such as systems analysts and programmers.'},
      {'p': '**Decision support systems** are designed to support decision making. They are '
            'user-friendly and interactive, offering a variety of tools users can employ to '
            'perform tasks more effectively. Their advantages are that they **guide the '
            'manager** through using available data to reach useful decisions quickly while '
            'still leaving the decision to the manager (they offer no pre-determined solution); '
            'their **interactivity** enhances problem solving through the wide range of options '
            'provided; and they deliberately have **no structured solution**, so the manager '
            'determines the direction while the system shows possible solutions and their '
            'implications.'},
      {'p': 'Examples include spreadsheets, forecasting, regression analysis, linear and '
            'non-linear programming, modelling and simulation, statistical analysis, financial '
            'modelling, sensitivity and risk analysis, and activity cost management. The '
            '**electronic spreadsheet** (Microsoft Excel) is by far the most versatile and '
            'widely applied, used for monthly expenditure reports, cash budgets, standard cost '
            'records and profitability reports, and exportable into presentation packages.'},
    ], 'src': 'Chapter 6.8', 'sec': '6.8'},
  ]},
}
