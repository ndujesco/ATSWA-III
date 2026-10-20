CH = {
 'n': 6,
 't': 'Audit Evidence and Verification Procedures',
 'brief': 'What audit evidence actually is, how the auditor obtains it (financial statement '
          'assertions, the eight audit procedures, external confirmation, the work of an '
          'expert, management representations), and how it is applied to verify assets and '
          'liabilities on the Statement of Financial Position — closing with the firm-level '
          'safeguards of quality control and peer review.',
 'outcomes': [
   'Describe the sources and relative merits of different types of evidence available',
   'Describe what is sufficiently appropriate audit evidence',
   'Describe the financial statement assertions commonly reported on',
   'Explain how the auditor uses assertions in obtaining audit evidence',
   'Outline the audit procedures for obtaining audit evidence',
   'Outline examples of situations where external confirmation may be used',
   'Describe how the auditor should design external confirmation requests',
   'Distinguish between positive and negative confirmation',
   'Explain how the auditor should deal with responses from external confirmations',
   'Explain the importance of management representation as audit evidence',
 ],
 'secs': [
  {'n': '6.1', 't': 'Nature and scope of audit evidence', 'b': [
    {'key': 'The auditor should obtain **sufficient and appropriate** audit evidence to be able '
            'to draw reasonable conclusions on which to base the audit opinion — sufficiency '
            'and appropriateness are two genuinely separate qualities, covered in detail below.'},
    {'def': {'t': 'Audit evidence', 'd': 'all the information used by the auditor in arriving at '
                  'the conclusions on which the audit opinion is based — including information '
                  'in the accounting records underlying the financial statements, and other '
                  'information.'}},
    {'key': 'Auditors are **not** expected to address all information that may exist — '
            'conclusions are ordinarily reached using sampling and other selection approaches, '
            'and the auditor ordinarily relies on evidence that is **persuasive rather than '
            'conclusive**. To obtain reasonable assurance, however, the auditor is never '
            'satisfied with evidence that is less than persuasive — professional judgment and '
            'scepticism determine the sufficiency and appropriateness needed.'},

    {'h4': '§6.1.2 Types of audit evidence'},
    {'table': {'align': 'll', 'head': ['Type', 'What it covers'], 'rows': [
      ['**Accounting records**', 'Records of initial entries and supporting records — cheques, '
       'electronic fund transfer records, invoices, contracts, the general and subsidiary '
       'ledgers, journal entries and other unrecorded adjustments, worksheets and spreadsheets '
       'supporting cost allocations/computations/reconciliations/disclosures — potentially part '
       'of integrated systems sharing data across reporting, operations and compliance.'],
      ['**Financial statements prepared by management**', 'Management is responsible for '
       'preparing them from the accounting records. The auditor obtains some evidence by '
       'testing the records (analysis, review, re-performance, reconciliation), potentially '
       'establishing internal consistency — but accounting records **alone** never provide '
       'sufficient evidence for an opinion; other evidence is always needed.'],
      ['**Other audit evidence**', 'Minutes of meetings; third-party confirmations; analysts\' '
       'reports; information from inquiry, observation and inspection; and other information '
       'developed by, or available to, the auditor permitting conclusions through valid '
       'reasoning.'],
    ]}},

    {'h4': '§6.1.3 Sufficient and appropriate audit evidence'},
    {'def': {'t': 'Sufficiency', 'd': 'the measure of the QUANTITY of audit evidence.'}},
    {'def': {'t': 'Appropriateness', 'd': 'the measure of the QUALITY of audit evidence — its '
                  'relevance and reliability in supporting, or detecting misstatements in, '
                  'transaction classes, account balances, disclosures and related '
                  'assertions.'}},
    {'key': 'Quantity needed is affected by the **risk of misstatement** (higher risk needs '
            'more evidence) and by **quality** (higher quality needs less) — sufficiency and '
            'appropriateness are therefore interrelated. But **merely obtaining more evidence '
            'cannot compensate for poor quality** — quantity is not a substitute for quality.'},
    {'p': 'A given set of procedures may be relevant to some assertions but not others — e.g. '
          'inspecting post-period-end receivable collection records may evidence existence and '
          'valuation, but not period-end cut-off appropriateness. Conversely, the auditor often '
          'obtains evidence from different sources/natures relevant to the **same** assertion — '
          'e.g. combining receivables ageing analysis with subsequent collection evidence for '
          'the valuation of the doubtful debts allowance.'},
    {'warn': 'Obtaining evidence for one assertion (e.g. physical existence of inventory) is '
             '**never a substitute** for obtaining evidence for another assertion (e.g. the '
             'valuation of that same inventory) — existence and valuation are independent '
             'questions requiring independent evidence.'},
    {'p': 'General reliability rules (subject to important exceptions):'},
    {'ol': [
      'evidence is more reliable when obtained from independent sources outside the entity;',
      'internally generated evidence is more reliable when related controls are effective;',
      'evidence obtained directly by the auditor (e.g. observing a control) is more reliable '
      'than evidence obtained indirectly or by inference (e.g. inquiring about a control);',
      'evidence is more reliable in documentary form than oral (a contemporaneous written '
      'meeting record beats a later oral account of what was discussed); and',
      'original documents are more reliable than photocopies or facsimiles.',
    ]},
    {'note': 'An audit rarely involves authenticating documentation, and the auditor is neither '
             'trained as, nor expected to be, an expert authenticator — but must still consider '
             'the reliability of photocopies, facsimiles, filmed, digitised or other electronic '
             'documents, including the controls over their preparation and maintenance.'},
    {'p': 'Where the auditor uses information the entity itself produced, they must obtain '
          'evidence of its **accuracy and completeness** — e.g. auditing revenue via standard '
          'prices applied to sales volume records requires considering both price-data accuracy '
          'and sales-volume-data completeness/accuracy. This may be tested concurrently with the '
          'audit procedure itself, via testing controls over the information\'s production, or, '
          'where needed, additional procedures such as CAATs recalculation.'},
    {'key': 'The auditor ordinarily obtains **more assurance** from consistent evidence obtained '
            'from different sources/natures than from any single item considered alone — and '
            'obtaining evidence from different sources may itself reveal that one particular '
            'item is unreliable. Where evidence from different sources is **inconsistent**, the '
            'auditor determines what additional procedures are needed to resolve the '
            'inconsistency.'},
    {'p': 'The auditor weighs the cost of obtaining evidence against the usefulness of the '
          'information obtained — but difficulty or expense alone is **never** a valid basis for '
          'omitting a procedure for which there is no alternative.'},
  ]},

  {'n': '6.2', 't': 'Obtaining audit evidence', 'b': [
    {'h4': 'The use of assertions in obtaining audit evidence'},
    {'p': 'In representing that the financial statements give a true and fair view, management '
          'implicitly or explicitly makes **assertions** about the recognition, measurement, '
          'presentation and disclosure of the financial statements\' elements. The auditor uses '
          'assertions, in sufficient detail, as the basis for assessing risks of material '
          'misstatement and designing/performing further audit procedures responsive to those '
          'risks.'},
    {'p': 'Assertions fall into three categories:'},
    {'table': {'align': 'll', 'head': ['Category', 'Assertions within it'], 'rows': [
      ['**Classes of transactions and events** (for the period)', '**Occurrence** — recorded '
       'transactions/events have occurred and pertain to the entity; **accuracy** — amounts and '
       'data have been recorded appropriately; **cut-off** — transactions/events are recorded '
       'in the correct accounting period; **classification** — transactions/events are recorded '
       'in the proper accounts.'],
      ['**Account balances** (at period end)', '**Existence** — assets, liabilities and equity '
       'interests exist; **rights and obligations** — the entity holds/controls the rights to '
       'assets, and liabilities are the entity\'s obligations; **completeness** — all balances '
       'that should have been recorded have been; **valuation and allocation** — balances are '
       'included at appropriate amounts, with valuation/allocation adjustments appropriately '
       'recorded.'],
      ['**Presentation and disclosure**', '**Occurrence and rights and obligations** — '
       'disclosed events/transactions have occurred and pertain to the entity; **completeness** '
       '— all disclosures that should have been included have been; **classification and '
       'understandability** — information is appropriately presented/described, disclosures '
       'clearly expressed; **accuracy and valuation** — information is disclosed fairly and at '
       'appropriate amounts.'],
    ]}},
    {'note': 'The auditor may use these exact assertions or express them differently, provided '
             'every aspect above is covered — e.g. combining "transactions and events" with '
             '"account balance" assertions, or folding cut-off into occurrence/completeness.'},

    {'h4': 'The use of audit procedures for obtaining audit evidence'},
    {'p': 'The auditor performs audit procedures to:'},
    {'ol': [
      'obtain an understanding of the entity and its environment, including internal control, '
      'to assess risks of material misstatement at the financial statement and assertion '
      'levels — called **"risk assessment procedures"**;',
      'test the operating effectiveness of controls in preventing, or detecting and '
      'correcting, material misstatements — called **"tests of controls"**; and',
      'detect material misstatements at the assertion level — called **"substantive '
      'procedures"** (tests of detail plus substantive analytical procedures).',
    ]},
    {'key': 'The auditor **always** performs risk assessment procedures — but these **alone** '
            'never provide sufficient appropriate evidence for the opinion; they must be '
            'supplemented by further procedures (tests of controls where relevant, and always '
            'substantive procedures).'},
    {'p': 'Tests of controls are necessary in **two circumstances**: (1) where the risk '
          'assessment expects controls to operate effectively, the auditor must test them to '
          'support that assessment; and (2) where substantive procedures alone cannot provide '
          'sufficient appropriate evidence, tests of controls are required regardless.'},
    {'warn': 'Because the auditor\'s risk assessment is judgmental and may not identify every '
             'risk, and because internal control has inherent limitations (management override, '
             'human error, systems changes), **substantive procedures for material classes of '
             'transactions, account balances and disclosures are always required** — no amount '
             'of favourable control testing ever eliminates the need for substantive work.'},
  ]},

  {'n': '6.3', 't': 'Sources of audit evidence: the eight audit procedures', 'b': [
    {'p': 'The auditor uses one or more of these procedures to obtain evidence — each may serve '
          'as a risk assessment procedure, test of control, or substantive procedure, depending '
          'on the context of its use:'},
    {'table': {'align': 'll', 'head': ['Procedure', 'What it involves'], 'rows': [
      ['**Inspection of records/documents**', 'Examining internal or external records/documents '
       'in paper, electronic or other media — reliability varies by nature/source, and (for '
       'internal documents) the effectiveness of the controls over their production. Documents '
       'are **least reliable** if created and held by the entity (e.g. invoices); **more '
       'reliable** if created by third parties and held by the entity (e.g. a supplier\'s '
       'statement); **most reliable** if created by third parties and held by the auditor (e.g. '
       'debtor circularisation responses).'],
      ['**Physical inspection of tangible assets**', 'Physical examination of assets — reliable '
       'for **existence**, but not necessarily for rights/obligations or valuation. Individual '
       'inventory item inspection ordinarily accompanies observation of the inventory count.'],
      ['**Observation**', 'Watching a process or procedure being performed by others (e.g. '
       'inventory counting, control activities) — evidences the performance of a process, but '
       'limited to the specific point in time observed, and by the fact that being observed may '
       'itself change how the process is performed.'],
      ['**Inquiry**', 'Seeking information from knowledgeable persons, inside or outside the '
       'entity — ranging from formal written to informal oral. Used extensively and often '
       'complements other procedures, but **alone is never sufficient** to address a material '
       'misstatement risk, nor to test control operating effectiveness.'],
      ['**Confirmation**', 'A specific type of inquiry — obtaining a representation of '
       'information or an existing condition directly from a third party (e.g. confirming '
       'receivables by communicating with debtors). Used for balances and their components, and '
       'also for confirming the absence of certain conditions (e.g. a "side agreement" '
       'affecting revenue recognition).'],
      ['**Recalculation**', 'Checking the mathematical accuracy of documents/records — can be '
       'performed via CAATs (e.g. checking a file\'s summarisation accuracy electronically).'],
      ['**Re-performance**', 'The auditor\'s own independent execution of procedures or '
       'controls originally performed as part of the entity\'s internal control (manually or '
       'via CAATs) — e.g. re-performing the ageing of accounts receivable.'],
      ['**Analytical procedures**', 'Evaluating financial information via plausible '
       'relationships among financial and non-financial data — including investigating '
       'fluctuations/relationships inconsistent with other information or deviating '
       'significantly from predictions (e.g. comparing monthly payroll costs against wage '
       'rises/starters/leavers/seasonality; sales vs. expenses month-on-month and against prior '
       'years; ageing inventory/debtors and debtor days/inventory turnover). Widely used, but '
       'limited by the predictability of relationships, data availability/relevance/'
       'comparability, and the auditor\'s own knowledge of the business.'],
    ]}},
    {'note': 'Where accounting data exists only electronically (electronic commerce, image '
             'processing systems that scan and discard source documents), the auditor may need '
             '**Computer Assisted Audit Techniques (CAATs)** to carry out these procedures, and '
             'must consider the entity\'s data retention policy to ensure needed information '
             'remains available when required.'},
  ]},

  {'n': '6.4', 't': 'Reliability of third-party evidence: external confirmation', 'b': [
    {'p': 'The auditor determines whether external confirmation is necessary to obtain '
          'sufficient appropriate evidence, considering the assessed risk of material '
          'misstatement and how evidence from other planned procedures will reduce that risk to '
          'an acceptably low level.'},
    {'def': {'t': 'External confirmation', 'd': 'the process of obtaining and evaluating audit '
                  'evidence through a representation of information or an existing condition, '
                  'directly from a third party, in response to a request about a particular item '
                  'affecting the financial statement assertions or disclosures.'}},
    {'p': 'Situations where external confirmations may be used:'},
    {'ul': [
      'bank balances and other information from bankers;',
      'accounts receivable balances;',
      'inventories held by third parties at bonded warehouses for processing or on '
      'consignment;',
      'property title deeds held by lawyers/financiers for safe custody or as security;',
      'investments purchased from stockbrokers but not delivered at the reporting date;',
      'loans from lenders; and',
      'accounts payable balances.',
    ]},
    {'key': 'Reliability depends on the auditor applying appropriate procedures across three '
            'stages: **designing** the request, **performing** the confirmation procedures, and '
            '**evaluating** the results — plus factors like the control exercised over requests/'
            'responses, respondent characteristics, and any restrictions in the response or '
            'imposed by management.'},

    {'h4': '§6.4.2 Designing the request'},
    {'p': 'Requests should be tailored to the specific audit objective, considering the '
          'assertions addressed and factors affecting reliability — the request\'s form, prior '
          'experience, the information\'s nature, and the intended respondent all directly '
          'affect the reliability of the resulting evidence.'},

    {'h4': '§6.4.3 Positive vs. negative confirmations'},
    {'table': {'align': 'll', 'head': ['Positive confirmation', 'Negative confirmation'], 'rows': [
      ['Asks the respondent to reply **in every case** — either confirming agreement or filling '
       'in requested information. Ordinarily provides reliable evidence, but risks a respondent '
       'replying without actually verifying the information (undetectable by the auditor). A '
       '"blank" variant (omitting the stated amount, asking the respondent to fill it in) '
       'reduces this risk but tends to lower response rates.',
       'Asks the respondent to reply **only if they disagree**. No response gives no explicit '
       'evidence that the request was even received and verified — so it ordinarily provides '
       '**less reliable** evidence than positive confirmation, and the auditor should consider '
       'supplementing it with other substantive procedures.'],
    ]}},
    {'p': 'Negative confirmation may reduce risk to an acceptable level when: the assessed risk '
          'of material misstatement is lower; a large number of small balances is involved; a '
          'substantial number of errors is not expected; and the auditor has no reason to '
          'believe respondents will disregard the requests. A **combination** may be used — '
          'e.g. positive requests for a small number of large balances, negative requests for a '
          'large number of small balances.'},

    {'h4': '§6.4.4 Management requests to withhold confirmation'},
    {'p': 'If management asks the auditor not to seek confirmation on a matter, the auditor must '
          'consider whether valid grounds exist and obtain evidence supporting that validity. If '
          'the auditor agrees, alternative procedures must be applied instead. If the auditor '
          '**disagrees** and is prevented from confirming anyway, this is a **scope '
          'limitation**, with possible impact on the auditor\'s report.'},
    {'key': 'Applying professional scepticism here means considering whether the request has '
            'any implications for management\'s **integrity** — whether it may indicate the '
            'possible existence of fraud or error, and whether the proposed alternative '
            'procedures can genuinely provide sufficient appropriate evidence in its place.'},

    {'h4': '§6.4.5-6.4.11 Process integrity, non-response and evaluation'},
    {'p': 'Reliability is affected by the respondent\'s competence, independence, authority to '
          'respond, knowledge and objectivity — the auditor tries to direct requests to an '
          'appropriately knowledgeable, authorised individual. The auditor maintains **control** '
          'over the whole process (selecting recipients, preparing/sending requests, receiving '
          'responses) to minimise the risk of interception or alteration — ensuring the auditor '
          'sends the requests, they are properly addressed, and replies come directly back to '
          'the auditor.'},
    {'p': 'Where **no response** is received to a positive request, the auditor performs '
          '**alternative procedures** providing evidence for the same assertions — e.g. for '
          'receivables: examining subsequent cash receipts, shipping documentation for '
          'existence, and sales near period-end for cut-off; for payables: subsequent cash '
          'disbursements, third-party correspondence, and goods-received notes.'},
    {'p': 'The auditor also considers the **authenticity** of responses received (e.g. verifying '
          'a response by telephone call, requesting the original be mailed directly, validating '
          'electronic responses), documents oral confirmations in the working papers, and, for '
          'significant oral information, requests written confirmation directly.'},
    {'p': 'Where confirmation and alternative procedures together have not provided sufficient '
          'appropriate evidence, additional procedures are performed — considering the '
          'reliability of what was obtained, the nature and implications of any **exceptions** '
          '(which may indicate a misstatement requiring further investigation), and the '
          'evidence from other procedures. The overall results are finally evaluated together '
          'with all other audit evidence obtained for that assertion.'},
    {'note': 'The auditor may confirm balances at a date **prior to** the reporting date (e.g. '
             'where the audit must complete shortly after period end) — but must then obtain '
             'sufficient evidence that transactions in the intervening period have not been '
             'materially misstated, considering the need for further evidence covering the '
             'remainder of the period.'},
  ]},

  {'n': '6.5', 't': 'Specific examples of third-party confirmations', 'b': [
    {'p': 'The most commonly used external verification procedures are debtors circularisation, '
          'bank confirmations, and confirmation of pending legal matters.'},

    {'h4': '§6.5.1 Debtors circularisation'},
    {'def': {'t': 'Debtors circularisation', 'd': 'a verification procedure where trade debtors '
                  'are contacted directly to confirm their balances — the normal means of '
                  'checking whether debtors really owe the amount stated in the client\'s sales '
                  'ledger.'}},
    {'key': 'Circularisation is essentially an act of the **client**, who alone can authorise '
            'third parties to divulge information to the auditor. If the client refuses to '
            'co-operate, the auditors must consider whether to **qualify their report**, since '
            'they may be unable to satisfy themselves by other means of the validity/accuracy '
            'of debtor balances.'},
    {'p': 'Ideally circularisation happens immediately after year end, to cover the actual '
          'year-end balances. Where timing constraints prevent this, prior year-end '
          'circularisation may be appropriate — recommended to be no more than **two months** '
          'before year end, especially where internal controls are strong enough for the '
          'auditor to gain reasonable assurance from reconciling the intervening period\'s '
          'movements.'},
    {'table': {'align': 'll', 'head': ['Positive circularisation', 'Negative circularisation'],
      'rows': [
      ['Requires confirmation of the outstanding balance **in every case**. Appropriate where: '
       'the auditor is not satisfied with sales/debtor control systems; other verification work '
       'showed unsatisfactory results. Its usefulness depends heavily on the auditor\'s '
       'tenacity in following up non-replies (telephone, personal calls).',
       'Requires a reply only if the debtor disputes the balance. Simpler, needs no follow-up, '
       'but appropriate only where: the auditor already trusts the internal control governing '
       'sales/debtors; other verification already showed satisfactory results; and it is used '
       'with a large, carefully selected sample (otherwise many requests are simply discarded, '
       'negating the test\'s value).'],
    ]}},
    {'p': 'Sample selection requires scrutinising accounts individually to include special '
          'cases, such as: accounts with credit balances; accounts written off as bad, or under '
          'specific loss provision; active accounts with nil balances; accounts unpaid beyond '
          'the normal period; accounts habitually exceeding credit limits; accounts with '
          'balances materially smaller at the reporting date than usual (possibly artificially '
          'reduced to escape attention); accounts of debtors connected to the client or its '
          'officers; accounts with unusually favourable trade terms; and accounts in arrears '
          'that do not appear to be followed up by normal credit control.'},
    {'p': 'For **positive** circularisation, non-respondents must be followed up by all '
          'practical means — a second request after 2-3 weeks, then telephone (with client '
          'permission) if needed. Where follow-up is limited, alternative procedures include: '
          'checking post-date cash receipts and valid purchase orders; examining the account for '
          'specific invoices and confirming their validity; obtaining explanations for unpaid '
          'invoices when later ones have been paid; checking if the balance is growing (and '
          'why); and testing controls over credit notes and bad debt write-offs.'},
    {'p': 'Where circularisation is carried out **before** year end, additional procedures '
          'apply: reviewing/reconciling debtor control account entries for the intervening '
          'period; reconciling sales journal/invoice/dispatch note entries to the control '
          'account; checking credit entries for returns/allowances; sampling cash receipts for '
          'correct control account crediting; reviewing balances at both the circularisation '
          'and year-end dates and investigating unexpected movements (possibly sending further '
          'year-end requests to material debtors); analytical review comparing debtor ratios at '
          'both dates; and year-end cut-off tests in addition to those at the confirmation '
          'date.'},
    {'key': 'All circularisation results must be properly recorded and evaluated — every '
            'disagreement and non-reply followed up, with its effect on total debtors assessed. '
            'Differences that are merely invoices or cash in transit generally need no '
            'adjustment, but disputed amounts and genuine client errors might.'},

    {'h4': '§6.5.2 Bank confirmations'},
    {'p': 'Auditors rely heavily on bank confirmation for the completeness, existence, rights, '
          'obligations and valuation of bank balances. A standard bank confirmation letter '
          'requests:'},
    {'ol': [
      'balances on all current, deposit and term accounts, noting any restrictions (blocked '
      'funds, compensating balances) — including a description of any account with no balance '
      'that operated during the year;',
      'the name and closure date of any accounts closed during the year;',
      'balances on advance/loan/overdraft accounts, with terms, interest, and any collateral/'
      'guarantees held;',
      'liability for notes/bills discounted or deposited for collection;',
      'guarantees given on the client\'s behalf, or given by the client for third parties;',
      'a list of share certificates/securities deposited, and any lien/pledge/restriction on '
      'them;',
      'interest/charges to be paid, and interest due, not yet included in the stated balances;',
      'details of any other operations or matters in progress not otherwise covered; and',
      'a list of officers authorised to sign cheques, and how their signatures must be '
      'combined.',
    ]},
    {'note': 'Matters excluded from the **standard** bank letter, requiring a supplementary '
             'request where needed: copies of bank statements; copies of paying-in slips for '
             'specific lodgements; the make-up of those lodgements; lists of securities/title '
             'documents lodged with the bank (usually only relevant between banking '
             'organisations); interest paid to/by third parties and their names; insurance-'
             'related receipts; returned paid cheques; stopped cheques (not normally needed, '
             'since they clear through the banking system within the audit period anyway); '
             'third-party securities including director guarantees (requiring specific third-'
             'party authority); and outstanding forward foreign exchange contract details.'},

    {'h4': '§6.5.3 Legal confirmation of pending legal matters'},
    {'p': 'Confirmation from a client\'s legal advisers is often required for contingent '
          'liabilities from outstanding legal matters — pending lawsuits present problems of '
          'both **ascertainment** (does the claim exist) and **appraisal** (what might it '
          'cost).'},
    {'p': 'Relevant audit procedures for verifying such claims exist (though not necessarily '
          'their likely amount):'},
    {'ol': [
      'reviewing the claims-recording system and how claims reach management\'s attention;',
      'discussing solicitor-instruction arrangements with the responsible official (e.g. head '
      'of legal, or the company secretary);',
      'examining board/committee minutes for references to possible claims;',
      'examining solicitors\' bills and correspondence;',
      'obtaining a list of matters referred to solicitors, with liability estimates, from the '
      'appropriate director/official; and',
      'obtaining written assurance that the director/official is not aware of any referred '
      'matters beyond those disclosed.',
    ]},
    {'key': 'The normal, proper source of confirmation for legal matters is the company\'s '
            '**own legal advisers** — requests should stay within the solicitor-client '
            'relationship, with the client asking that a copy of the reply go directly to the '
            'auditor. If the enquiries turn up nothing unexpected, the auditor would not '
            'normally qualify the report merely for lack of independent corroboration of the '
            'list\'s completeness. But if the auditor remains unable to obtain all the '
            'information required, **the report must be qualified**.'},

    {'h4': '§6.5.4 Summary: assets/liabilities and their confirming third party'},
    {'table': {'align': 'll', 'head': ['Asset/Liability', 'Confirming third party'], 'rows': [
      ['Bank balance, security, bank loans, contingent liabilities, accrued interest', 'Bank'],
      ['Debtors and creditors balances', 'Individual debtors and creditors'],
      ['Staff loans, advances, mortgages, accrued interest', 'Individual staff members / '
       'financial houses'],
      ['Assets held abroad, goods on consignment/sale-or-return, liabilities repayable abroad',
       'Overseas agents, associate firms, agents, consignees, sale-or-return holders'],
      ['Investments in subsidiary companies', 'Auditors of the subsidiaries'],
      ['Goods held in bond or warehouse', 'Harbour board, warehouse company'],
      ['Leased premises', 'Landlord'],
      ['Pending litigation, possible damages/costs/legal fees outstanding', 'Solicitors'],
    ]}},
  ]},

  {'n': '6.6', 't': 'The reliability of audit evidence — a consolidated view', 'b': [
    {'p': 'Reliability is influenced by source (internal or external) and nature (visual, '
          'documentary or oral). Useful generalisations:'},
    {'ol': [
      'evidence from external sources (e.g. third-party confirmation) is more reliable than '
      'that from the entity\'s own records;',
      'evidence from the entity\'s records is more reliable when the related accounting/'
      'internal control system operates effectively;',
      'evidence obtained directly by the auditor is more reliable than evidence obtained by or '
      'from the entity;',
      'documentary/written evidence is more reliable than oral; and',
      'original documents are more reliable than photocopies, telexes or facsimiles.',
    ]},
    {'key': 'Consistency across sources has a **corroborating effect**, making evidence more '
            'persuasive; where evidence is inconsistent, the auditor must determine what '
            'additional procedures are needed to resolve it. The cost-benefit relationship of '
            'obtaining evidence matters, but difficulty/expense alone never justifies omitting a '
            'necessary procedure — the same principle stated in §6.1, restated here as a general '
            'takeaway.'},
  ]},

  {'n': '6.7', 't': 'Using the work of an expert', 'b': [
    {'def': {'t': 'Expert', 'd': 'a person or firm possessing special skill, knowledge and '
                  'experience in a particular field other than accounting and auditing.'}},
    {'key': 'The auditor\'s education and experience make them knowledgeable about business '
            'matters generally, but they are **not expected** to have the expertise of a person '
            'trained in another profession (e.g. an actuary or engineer). When using an '
            'expert\'s work, the auditor must still obtain sufficient appropriate evidence that '
            'the work is adequate for the audit\'s purposes — using an expert does not transfer '
            'responsibility for the opinion.'},
    {'p': 'An expert may be engaged by the entity, engaged by the auditor, employed by the '
          'entity, or employed by the auditor. Where the auditor uses the work of their own '
          'employee-expert, that work is used in the employee\'s capacity **as an expert**, not '
          'as an ordinary audit assistant — so the auditor applies the relevant procedures to '
          'their work/findings, but does not ordinarily need to re-evaluate their skill/'
          'competence for each engagement (unlike an outside expert).'},

    {'h4': '§6.7.1 Determining the need for an expert'},
    {'p': 'Examples where an expert\'s report/opinion/valuation/statement may be needed:'},
    {'ul': [
      'valuations of certain assets (land/buildings, plant/machinery, art, precious stones);',
      'determining quantities or physical condition of assets (stored minerals, underground '
      'reserves, remaining plant life);',
      'determining amounts using specialised techniques (e.g. actuarial valuation);',
      'measuring work completed/to be completed on contracts in progress; and',
      'legal opinions interpreting agreements, statutes and regulations.',
    ]},
    {'p': 'Relevant considerations: the engagement team\'s own knowledge/experience of the '
          'matter; the risk of material misstatement based on the matter\'s nature/complexity/'
          'materiality; and the quantity/quality of other evidence expected to be available.'},

    {'h4': '§6.7.2 Competence and objectivity of the expert'},
    {'p': 'The auditor evaluates the expert\'s **professional competence** — considering '
          'professional certification/licensing/membership, and experience/reputation in the '
          'relevant field — and separately evaluates their **objectivity**.'},
    {'warn': 'The risk of impaired objectivity **increases** where the expert is: employed by '
             'the entity; or otherwise related to the entity (e.g. financially dependent on it, '
             'or holding an investment in it). If concerned about competence or objectivity, the '
             'auditor discusses reservations with management, considers whether sufficient '
             'appropriate evidence can still be obtained, and may need additional procedures or '
             'a different expert entirely.'},

    {'h4': '§6.7.3 Scope of the expert\'s work'},
    {'p': 'The auditor obtains evidence that the scope of the expert\'s work is adequate — often '
          'via reviewing written instructions from the entity to the expert, covering: the '
          'objectives/scope of the work; the matters the expert\'s report is expected to cover; '
          'the auditor\'s intended use of the work (including possible disclosure of the '
          'expert\'s identity/involvement to third parties); the expert\'s access to records/'
          'files; clarification of the expert\'s relationship with the entity; confidentiality; '
          'and the assumptions/methods to be used and their consistency with prior periods. '
          'Where these are not clearly set out, the auditor may communicate with the expert '
          'directly.'},

    {'h4': '§6.7.4 Evaluating the expert\'s work'},
    {'p': 'The auditor evaluates whether the substance of the expert\'s findings is properly '
          'reflected in, or supports, the financial statements — considering the source data '
          'used, the assumptions/methods used and their consistency with prior periods, and the '
          'results in light of the auditor\'s own business knowledge and other audit evidence.'},
    {'key': 'The **appropriateness and reasonableness of assumptions and methods** are the '
            '**expert\'s** own responsibility — the auditor typically lacks the expertise to '
            'challenge them directly, but must still understand them and consider whether they '
            'seem appropriate and reasonable given the auditor\'s own knowledge and other '
            'evidence. Where the expert\'s results are insufficient, or inconsistent with other '
            'evidence, the auditor resolves the matter — via discussion, additional procedures, '
            'possibly engaging another expert, or modifying the auditor\'s report.'},

    {'h4': '§6.7.5 Reference to an expert in the auditor\'s report'},
    {'warn': 'When issuing an **unmodified** report, the auditor should **not** refer to an '
             'expert\'s work — such a reference might be misunderstood as a qualification, or a '
             'division of responsibility, neither of which is intended. If the auditor\'s report '
             'is **modified** as a result of an expert\'s work, it may be appropriate to '
             'describe the expert\'s involvement (identity and extent) in explaining the '
             'modification — but only with the expert\'s **permission**; if refused and the '
             'auditor still believes reference is necessary, legal advice may be needed.'},
  ]},

  {'n': '6.8', 't': 'Management representation', 'b': [
    {'key': 'The auditor should obtain evidence that management acknowledges its responsibility '
            'for the fair presentation of the financial statements, and has approved them — via '
            'minutes of governance meetings, a written representation, or a signed copy of the '
            'financial statements.'},
    {'p': 'Written representations should be obtained on matters **material** to the financial '
          'statements when other sufficient appropriate evidence cannot reasonably be expected '
          'to exist — reducing the possibility of misunderstanding, since oral representations '
          'confirmed in writing are less ambiguous. Requests may be limited to matters material '
          'individually or collectively; the auditor may need to inform management of their '
          'understanding of materiality for this purpose.'},
    {'p': 'The auditor should obtain written representation that management: (a) acknowledges '
          'responsibility for designing and implementing internal control to prevent and detect '
          'error; and (b) believes the effects of uncorrected misstatements aggregated by the '
          'auditor are immaterial, individually and in aggregate — with a summary of such items '
          'attached.'},
    {'p': 'Where management representations relate to material matters, the auditor should: '
          'seek corroborative evidence from inside or outside the entity; evaluate whether the '
          'representations seem reasonable and consistent with other evidence obtained; and '
          'consider whether the individuals making them can reasonably be expected to be well '
          'informed.'},
    {'warn': 'Management representations are **never a substitute** for other audit evidence '
             'the auditor could reasonably expect to be available — e.g. a management '
             'representation about an asset\'s cost is not a substitute for the cost evidence the '
             'auditor would ordinarily expect to obtain independently. If the auditor cannot '
             'obtain sufficient appropriate evidence on a matter with a material effect (or '
             'potential material effect), that is a **scope limitation**, even if management has '
             'made a representation on the matter.'},
    {'p': 'Some matters genuinely cannot be evidenced any other way — e.g. management\'s '
          'intention to hold an investment long-term, or to call up a debt before month-end '
          'balancing and re-grant the facility. In such cases, a written representation is the '
          'appropriate evidence. If a representation is **contradicted** by other evidence, the '
          'auditor investigates and, where necessary, reconsiders the reliability of other '
          'representations made.'},

    {'h4': 'Documentation and form'},
    {'p': 'Working papers ordinarily include a summary of oral discussions, or written '
          'representations. A **written** representation is ordinarily more reliable than an '
          'oral one, and can take the form of: a representation letter from management; a '
          'letter from the auditor outlining their understanding of management\'s '
          'representations, acknowledged/confirmed by management; or relevant board minutes/a '
          'signed copy of the financial statements.'},
    {'p': 'A management representation letter should be addressed to the auditor, contain the '
          'specified information, and be appropriately dated and signed — ordinarily dated the '
          'same date as the auditor\'s report (though a separate letter on specific matters may '
          'be obtained during the audit, or after the report date, e.g. at a public offering). '
          'It is ordinarily signed by those with primary responsibility for the entity and its '
          'financial aspects (ordinarily the CEO and CFO), based on the best of their knowledge '
          'and belief. Separate representation letters may be sought from other individuals '
          'where appropriate (e.g. confirming the completeness of minute-keeping from the '
          'person responsible for it).'},
    {'h4': 'Contents typically confirmed in a management representation letter'},
    {'p': 'A specimen letter (illustrative, not a fixed standard — content varies by entity and '
          'period) would ordinarily confirm, to the best of management\'s knowledge and belief:'},
    {'ol': [
      'no irregularities involving management or employees with a significant internal control '
      'role, or with a material effect on the financial statements;',
      'all books of account, supporting documentation and meeting minutes have been made '
      'available;',
      'completeness of information provided on the identification of related parties;',
      'the financial statements are free of material misstatement, including omissions;',
      'compliance with contractual agreements and regulatory requirements whose breach could '
      'have a material effect;',
      'proper recording/disclosure of related-party balances/transactions, sale/purchase '
      'commitment losses, asset buy-back agreements, and pledged collateral;',
      'no undisclosed plans that would materially alter asset/liability carrying values or '
      'classification;',
      'no undisclosed plans that would cause excess/obsolete inventory, and no inventory '
      'stated above net realisable value;',
      'satisfactory title to all assets, with no undisclosed liens/encumbrances;',
      'all liabilities (actual and contingent) recorded/disclosed as appropriate, with '
      'guarantees given to third parties disclosed;',
      'no undisclosed post-period-end events requiring adjustment or disclosure;',
      'confirmation of settled litigation amounts, and no other expected claims;',
      'no undisclosed compensating balance arrangements or other credit lines; and',
      'proper recording/disclosure of capital stock repurchase options/agreements and reserved '
      'shares.',
    ]},

    {'h4': 'Action if management refuses to provide representations'},
    {'warn': 'If management refuses to provide a representation the auditor considers '
             'necessary, the auditor should discuss it with management. The refusal itself '
             'constitutes a **scope limitation**, and the auditor should express a **modified '
             'opinion**. The auditor should also re-evaluate reliance placed on any other '
             'management representations made during the audit, and consider whether the '
             'refusal has additional implications for the report.'},
  ]},

  {'n': '6.9', 't': 'Verification of assets and liabilities', 'b': [
    {'key': 'The auditor has a duty to verify all assets and liabilities appearing in the '
            'Statement of Financial Position, **and** to ensure there are no other assets or '
            'liabilities that ought to appear but do not.'},
    {'h4': '§6.9.1 Verification of assets: CAVEBOP and VEBOP'},
    {'p': 'In verifying assets, the auditor seeks to establish six things, remembered by the '
          'mnemonic **CAVEBOP**:'},
    {'ol': [
      '**C**ost;',
      '**A**uthorization;',
      '**V**alue;',
      '**E**xistence;',
      '**B**eneficial **O**wnership; and',
      '**P**resentation in the accounts.',
    ]},
    {'key': 'Cost and authorisation are ordinarily verified **once**, in the year of '
            'acquisition. For assets already on the books from prior years, the auditor '
            'therefore only needs the remaining four aspects — remembered as **VEBOP** '
            '(Valuation, Existence, Beneficial ownership, Presentation/disclosure). Assets '
            'acquired **during** the current year still need the full CAVEBOP treatment.'},

    {'h4': '§6.9.2 Verification of trade debtors and creditors'},
    {'key': 'Independent, externally derived confirmation minimises the risk of **collusion** '
            'between third parties and the company\'s own staff aimed at deceiving the '
            'auditor — as a general rule, independent documentary evidence is superior to '
            'documentary evidence compiled by company staff, regardless of their seniority.'},
    {'p': 'Circularising a carefully selected sample of debtors/creditors serves to: ensure the '
          'accuracy of sales/purchase ledger book entries and resulting balances; ensure proper '
          'functioning of the credit control system; identify disputed accounts; and ensure '
          'records are fully up to date. Where suppliers are circularised, the confirmations '
          'received support both the creditors\' ledger balances and the monthly statements '
          'most suppliers send their customers anyway.'},
    {'note': 'It is essential that replies be sent **directly to the auditor at their own '
             'office** — otherwise there is a risk of tampering or suppression by client '
             'staff.'},

    {'h4': '§6.9.3 Verification of inventory and work in progress'},
    {'key': 'Management is responsible for ensuring reported stock figures represent stock '
            'physically in existence and include everything the entity owns; the auditor\'s '
            'duty is to obtain evidence of **ownership, existence and condition** at year end.'},
    {'p': 'Inventory receives particular audit attention because: it usually forms one of the '
          'largest Statement of Financial Position items (so a small error can be material); '
          'closing inventory directly affects cost of sales and hence profit/loss; it can be '
          'manipulated to hit a targeted profit figure; different valuation bases may be used; '
          'and there can be genuine valuation/existence/development-stage problems for '
          'specialised inventory (livestock, production-in-process, etc.).'},
    {'p': 'Objectives of inventory taking: verify condition; verify existence; establish title; '
          'determine cut-off accuracy; ascertain internal control effectiveness over inventory; '
          'provide a basis for checking inventory record correctness; ensure adequate provision '
          'for slow-moving/obsolete inventory; provide a quantity basis for valuation; and '
          'determine valuation accuracy.'},

    {'h4': '§6.9.4 Liability verification'},
    {'p': 'A Statement of Financial Position groups liabilities under headings such as equity, '
          'reserves, creditors due after more than one year, provisions for liabilities/charges, '
          'creditors due within one year, and contingent liabilities. The auditor\'s duty: '
          'verify the existence of stated liabilities; verify the correctness of their money '
          'amounts; verify the appropriateness of their description and the adequacy of '
          'disclosure; and verify that **all** existing liabilities are actually included.'},
    {'p': 'General verification principles (applied per the specific circumstances):'},
    {'ol': [
      '**Schedule** — request or prepare a schedule for each liability/class;',
      '**Cut-off** — e.g. a trade creditor should not be included unless the goods were '
      'acquired before year end;',
      '**Reasonableness** — of the liability itself;',
      '**Internal control** — determine, evaluate and test relevant procedures;',
      '**Previous-date clearance** — have prior-period liabilities all been cleared?',
      '**Authority** — for all liabilities;',
      '**Description** — adequacy of each liability\'s description in the accounts;',
      '**Documents** — examine relevant invoices, correspondence, debenture deeds, etc.;',
      '**Vouching** — the creation of each liability (e.g. receipt of a loan);',
      '**Accounting policies** — appropriate and consistently applied;',
      '**Disclosure** — everything needed for a true and fair view;',
      '**External verification** — direct confirmation with creditors, where possible;',
      '**Materiality** — a factor in every accounting/auditing decision;',
      '**Post-reporting-date events** — particularly important for liabilities;',
      '**Accounting standards** — liabilities accounted for per the relevant standards; and',
      '**Risk** — assess the risk of misstatement.',
    ]},

    {'h4': '§6.9.5 Verification of non-current assets'},
    {'p': 'Verification often begins with the **asset register**, which facilitates identifying '
          'assets during a physical check and forms an important part of internal control. It '
          'must be agreed to the financial records, and the auditor enquires about the extent/'
          'frequency of company officials\' own reconciliation checks between records, register '
          'and physical assets.'},
    {'p': 'An asset register normally records, per asset: supplier\'s name; purchase date; '
          'original cost; estimated useful life; estimated residual value; a summary of repair '
          'expenditure to date; estimated replacement cost (updated annually); and eventual '
          'disposal details.'},

    {'h4': '§6.9.6 Verification of intangible assets'},
    {'key': 'All intangibles have a finite economic life and should therefore be **amortised**.'},
    {'table': {'align': 'll', 'head': ['Intangible', 'Key verification points'], 'rows': [
      ['**Goodwill**', 'Arises on purchase of a business — examine the contract and allocation '
       'of purchase price to assets; normally remains in the accounts at cost.'],
      ['**Patents**', 'Examine the patent and its assignment (a patent can only be granted to '
       'an individual, e.g. an employee, who assigns it to the company); check payment of '
       'renewal fees and accounting for receivable royalties.'],
      ['**Trademarks**', 'Examine the patent office certificate; the assignment, if purchased; '
       'the reasonableness of capitalised design costs; and payment of renewal fees.'],
      ['**Copyrights**', 'Examine the document of title and assignment (if purchased); note '
       'that its life is the author\'s life plus 50 years.'],
    ]}},

    {'h4': '§6.9.7 Physical examination'},
    {'p': 'Physical inspection ascertains the existence of assets and liabilities, supporting '
          'the auditor\'s conclusion on the fairness of related financial statement '
          'assertions — using professional judgment to determine sufficient evidence, '
          'considering the item\'s nature, the materiality of possible errors, the item\'s '
          'relative risk, and the quality/quantity of evidence available cost-effectively.'},
  ]},

  {'n': '6.10', 't': 'Quality control', 'b': [
    {'key': 'Per the International Standard on Quality Control (ISQC), the audit firm '
            'establishes a system of quality control giving **reasonable assurance** that the '
            'firm and its personnel comply with professional standards and legal/regulatory '
            'requirements, and that the firm\'s reports are appropriate to the circumstances. '
            'The objectives are the same for every firm, but the exact nature/extent of '
            'procedures depends on the firm\'s size, practice, staff numbers and organisation.'},
    {'p': 'Procedures for controlling an audit plan: allocate work to staff, specifying '
          'completion timing for each aspect; and brief staff fully, determining the required '
          'performance standard and flagging possible problems.'},
    {'p': 'Audit risk areas demanding special attention:'},
    {'ol': [
      'precise instructions that staff bring problems encountered, and anything putting them '
      'upon enquiry, to the team leader\'s attention;',
      'thorough, meticulous completion of working papers recording all actions taken;',
      'review of the work and working papers by a more senior partner, adding their own '
      'comments/observations/instructions alongside what staff recorded.',
    ]},
    {'note': 'A completion checklist is commonly used — each staff member ticks off completed '
             'sections, followed by a final review by a partner (not necessarily on that '
             'assignment) exercising overall quality control.'},
    {'h4': 'Features of audit quality control'},
    {'table': {'align': 'll', 'head': ['Feature', 'What it involves'], 'rows': [
      ['**Hierarchy of control**', 'Communication flows (either way) through: partner → '
       'manager → audit senior → senior audit trainee → junior audit trainee. Ultimate '
       'responsibility for quality control rests with the relevant reporting **partner**.'],
      ['**Audit planning**', 'Scheduling audits (often clustered around common financial '
       'year-ends) to make maximum use of limited staff at minimum time/money cost, without '
       'compromising efficiency or quality.'],
      ['**Audit staff**', 'Wherever possible, the team should include experienced staff already '
       'familiar with that specific audit; new staff receive adequate training.'],
      ['**Communication with client/third parties**', 'Along three lines: the client\'s '
       'accounts department head (readiness to receive the team); the internal audit '
       'department (possible help/co-operation); and top management, year-round, for first-'
       'hand information on structural changes and legal matters without delay.'],
      ['**Timing**', 'Breaking the audit into work that can be done before, during and after '
       'the financial year-end, balancing promptness against audit cost.'],
      ['**Field work**', 'Proper execution of the audit plan, with adequate assessment and '
       'thorough evaluation of existing internal control/accounting systems to determine '
       'scope.'],
      ['**Reviews and consultation**', 'Before finalising the report, the reporting partner '
       'thoroughly reviews all field work — recordings, documents and evidence — alongside the '
       'letter of engagement and the audit completion checklist.'],
      ['**The audit report**', 'Should reflect the sum total of work and evidence gathered, '
       'worded to leave no doubt as to its meaning/implications, and state compliance (or '
       'otherwise) with regulatory requirements, accounting principles and auditing '
       'standards.'],
    ]}},
  ]},

  {'n': '6.11', 't': 'Peer review', 'b': [
    {'p': 'To mitigate litigation and losses arising from negligence, firms have taken measures '
          'to improve work quality — one of which is peer review.'},
    {'def': {'t': 'Peer review', 'd': 'a process where firms agree to set up mechanisms to '
                  'review each other\'s processes, identifying practice weaknesses that could be '
                  'addressed to improve quality standards. It involves a review of one audit '
                  'firm\'s systems, procedures and strategies by another audit firm of comparable '
                  'size, reputation and standard.'}},
    {'warn': 'Peer review is **not common in Nigeria** — it is a new approach, limited by: '
             'potentially prohibitive cost; the legality/confidentiality of allowing others '
             'through a client\'s file being unprotected; and the inevitable exposure of one '
             'firm\'s procedures/standards to a competing firm.'},
    {'p': 'The reviewer is expected to report on: acceptance and retention of clients; means of '
          'engaging, training, allocating and motivating staff; independence, integrity and '
          'competence; and the conduct of individual audit and other engagements.'},
  ]},

  {'n': '6.12', 't': 'Chapter summary', 'b': [
    {'ol': [
      'The financial statement assertions are existence, rights and obligations, occurrence, '
      'completeness, valuation, measurement, presentation and disclosure.',
      'Auditors are required to obtain sufficient appropriate audit evidence on which to base '
      'audit opinions.',
      'Substantive tests may be incorporated with other procedures like tests of control to '
      'obtain the required audit evidence.',
      'Documentary evidence is least reliable if created and held by the entity, most reliable '
      'if created and held by third parties.',
      'Among the key techniques used to obtain audit evidence are inspection, observation, '
      'enquiry, confirmation, computation, re-performance and analytical procedures.',
      'Examples of third-party confirmations include debtors and creditors circularisation, '
      'and requesting bank references through a bank letter.',
      'Management representations are also sought to provide evidence in key areas where other '
      'sources may be less reliable, normally in the form of a management representation '
      'letter.',
    ]},
  ]},

  {'n': '6.13', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'p': 'The study text closes the chapter with 10 questions — 5 multiple-choice and 5 '
          'short-answer — reproduced below in full with the official answers, each explained. The '
          'Auditing study text sets **no examination-type questions**; this bank is the whole of '
          'its end-of-chapter material.'
},
    {'eg': {'tag': 'Study text', 't': 'The questions, with the official answers', 'open': True, 'q': [
      {'ol': [
        'The examination of the documentary evidence in support of the transactions of an '
        'organisation is known as (A) Verification; (B) Observation; (C) Vouching; (D) Physical '
        'inspection; (E) Analytical review.',
        'The **positive** method of circularising debtors can be used in the following situations '
        '**EXCEPT**: (A) Where there are numerous small accounts to be circularised; (B) Where '
        'there is a need to confirm the existence and amount of the debt; (C) Where the condition '
        'of the internal control system is not satisfactory; (D) Where the condition of the '
        'internal control system is satisfactory; (E) Where the amount of the debt is material.',
        '"Auditors should plan the audit work so as to perform the audit in an effective manner." '
        '(A) The statement is true; (B) The statement is not true; (C) Writing audit planning is '
        'enough; (D) Writing a management report will suffice; (E) Auditors’ prior year knowledge '
        'will suffice.',
        'The following assertions about audit evidence are correct **EXCEPT**: (A) Evidence is '
        'more reliable when it is obtained from sources outside the entity; (B) All evidence is '
        'acceptable; (C) Evidence provided by original documents is more reliable; (D) The '
        'reliability of audit evidence is influenced by its source; (E) Internally generated '
        'evidence is reliable when control is effective.',
        'Situations where external confirmations may be used include all but one of the '
        'following: (A) Account receivable balances; (B) Bank balances and other information from '
        'bankers; (C) Account payable balances; (D) Property agreed in the prior year audit; (E) '
        'Inventories held by third parties at a bonded warehouse for processing.',
        'Information obtained by the auditor which enables him to arrive at the conclusions '
        'necessary for his opinion on financial statements is called ………',
        'Written requests by a client to its debtors or creditors for confirmation of their '
        'outstanding balances as at a given date is called ………',
        'When planning to use the work of an expert, the auditor should evaluate the ……… and ……… '
        'of the expert.',
        'The representations by management, explicit or otherwise, that are embodied in the '
        'financial statements are called ………',
        'State any **TWO** methods of obtaining audit evidence.',
      ]}],
      'a': [
      {'ol': [
        '**C** — vouching. Note the distinction the examiner is testing: **vouching** is the '
        'examination of documentary evidence supporting **transactions**; **verification** is the '
        'confirmation of the existence, ownership, valuation and presentation of **assets and '
        'liabilities** at the reporting date.',
        '**A** — numerous small accounts. The positive method asks every debtor to reply whether '
        'they agree or not, and is therefore reserved for **material balances, suspect balances '
        'and weak control environments**. Where there are many small accounts the **negative** '
        'method — reply only if you disagree — is used instead.',
        '**A** — the statement is true, and is a direct restatement of the requirement in the '
        'planning standard.',
        '**B** — "all evidence is acceptable" is plainly false. Evidence must be both '
        '**sufficient** (enough of it) and **appropriate** (relevant and reliable), and its '
        'reliability varies with its source and nature — which is exactly what the other four '
        'options describe.',
        '**D** — property agreed in the prior year audit. External confirmation is a technique '
        'for obtaining evidence **from a third party about a current balance or condition**; '
        'property already verified last year is confirmed by inspecting title deeds and the asset '
        'register, not by circularisation.',
        '**Audit evidence.**',
        '**Circularisation** (external confirmation).',
        '**Any two of:** professional competence; independence; experience; reputation — the two '
        'most often cited being **competence** and **objectivity/independence**.',
        '**Assertions** — existence, rights and obligations, occurrence, completeness, valuation, '
        'measurement, and presentation and disclosure.',
        '**Any two of:** physical inspection; observation (e.g. of inventory taking); enquiry '
        '(communicating with a third party or with management); confirmation; computation / '
        're-performance; analytical procedures; inspection of records or documents.',
      ]}]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'This chapter is the practical heart of the whole subject — the eight audit procedures '
   '(inspection, physical inspection, observation, inquiry, confirmation, recalculation, '
   're-performance, analytical procedures) and the assertion categories (transactions/events, '
   'account balances, presentation/disclosure) are both directly examinable lists worth '
   'memorising verbatim. The reliability hierarchy for documentary evidence (least reliable: '
   'created and held by the entity; most reliable: created by third parties and held by the '
   'auditor) recurs constantly across MCQs. Also know: positive vs. negative confirmation and '
   'when each is appropriate; the CAVEBOP/VEBOP mnemonic for asset verification (and why cost/'
   'authorization drop out after the acquisition year); and that management representations '
   'can NEVER substitute for other reasonably-available evidence.',
 'errors': [
   'Treating "sufficient" and "appropriate" as synonyms — sufficiency is QUANTITY, '
   'appropriateness is QUALITY (relevance + reliability), and more quantity never compensates '
   'for poor quality.',
   'Assuming risk assessment procedures alone can support the audit opinion — they never do by '
   'themselves; they must always be supplemented by tests of controls (where relevant) and '
   'substantive procedures, which are ALWAYS required regardless of how favourable the control '
   'assessment is.',
   'Using positive confirmation for a large number of small, low-risk balances where a strong '
   'control environment already exists — that is precisely the negative-confirmation use case; '
   'the two methods are not interchangeable defaults.',
   'Believing verification of one assertion (e.g. existence) satisfies another (e.g. '
   'valuation) for the same asset — each assertion requires its own independent evidence.',
   'Forgetting that cost and authorization (the "CA" in CAVEBOP) apply only in the year of '
   'acquisition — for assets already on the books, only VEBOP (valuation, existence, '
   'beneficial ownership, presentation) needs re-verifying each year.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The examination of the documentary evidence in support of the transactions of an '
         'organization is known as',
    'o': ['Verification', 'Observation', 'Vouching', 'Physical inspection', 'Analytical '
          'review'],
    'a': 2,
    'w': 'Vouching is precisely the examination of documentary evidence supporting recorded '
    'transactions — distinct from verification, which covers the broader existence/ownership/'
    'valuation of assets and liabilities generally.',
    'src': 'Chapter 6.3', 'sec': '6.3'},
   {'q': 'The positive method of circularizing debtors can be used in the following situations '
         'EXCEPT:',
    'o': ['Where there are numerous small accounts to be circularized', 'Where there is need to '
          'confirm the existence and amount of the debt', 'Where the condition of the internal '
          'control system is not satisfactory', 'Where the condition of the internal control '
          'system is satisfactory', 'Where the amount of the debt is material'],
    'a': 0,
    'w': 'Numerous small accounts is precisely the scenario the NEGATIVE method suits — positive '
    'circularisation is reserved for material balances, weak controls, or a specific need to '
    'confirm existence/amount, not for large volumes of small, low-materiality balances.',
    'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': '"Auditors should plan the audit work so as to perform the audit in an effective '
         'manner" — is this statement true?',
    'o': ['The statement is true', 'The statement is not true', 'Writing audit planning is '
          'enough', 'Writing management report will suffice', 'Auditors\' prior year knowledge '
          'will suffice'],
    'a': 0,
    'w': 'This is the chapter\'s own opening principle on planning (also established in Chapter '
    '5) — planning exists specifically to enable the engagement to be performed effectively and '
    'efficiently.',
    'src': 'Chapter 6.1', 'sec': '6.1'},
   {'q': 'The following assertions about audit evidence are correct EXCEPT:',
    'o': ['Evidence is more reliable when it is obtained from sources outside the entity', 'All '
          'evidence is acceptable', 'Evidence provided by original documents is more reliable',
          'Reliability of audit evidence is influenced by its source', 'Internally generated '
          'evidence is reliable when control is effective'],
    'a': 1,
    'w': '"All evidence is acceptable" directly contradicts the whole chapter\'s reliability '
    'framework — evidence varies enormously in reliability by source, nature and the '
    'circumstances under which it was obtained; it is never uniformly "acceptable."',
    'src': 'Chapter 6.1', 'sec': '6.1'},
   {'q': 'Situations where external confirmations may be used include all BUT ONE of the '
         'following:',
    'o': ['Accounts receivable balances', 'Bank balances and other information from bankers',
          'Accounts payable balances', 'Property agreed in prior year audit', 'Inventories held '
          'by third parties at bonded warehouse for processing'],
    'a': 3,
    'w': 'A property balance already agreed in a PRIOR year\'s audit is not a current-period '
    'item requiring fresh external confirmation — the other four are all live examples the '
    'chapter lists of situations where external confirmation is actively used.',
    'src': 'Chapter 6.4', 'sec': '6.4'},
  ],
  'theory': [
   {'q': 'Distinguish between positive and negative external confirmation requests, and state '
         'the circumstances in which negative confirmation may be used.',
    'marks': 6,
    'a': [
      {'p': 'A **positive** confirmation request asks the respondent to reply in every case — '
            'either confirming agreement or filling in the requested information. It ordinarily '
            'provides more reliable evidence, but carries the risk that a respondent replies '
            'without actually verifying the information.'},
      {'p': 'A **negative** confirmation request asks the respondent to reply only if they '
            'disagree with the stated information. It provides less reliable evidence, since no '
            'response gives no explicit evidence the request was even received and checked.'},
      {'p': 'Negative confirmation may be used to reduce risk to an acceptable level when: the '
            'assessed risk of material misstatement is lower; a large number of small balances '
            'is involved; a substantial number of errors is not expected; and the auditor has '
            'no reason to believe respondents will disregard the requests.'},
    ], 'src': 'Chapter 6.4', 'sec': '6.4'},
   {'q': 'Using the CAVEBOP mnemonic, state the six matters an auditor seeks to establish when '
         'verifying an asset, and explain why only four of them (VEBOP) apply in years after '
         'acquisition.',
    'marks': 6,
    'a': [
      {'ol': [
        'Cost',
        'Authorization',
        'Value',
        'Existence',
        'Beneficial ownership',
        'Presentation in the accounts',
      ]},
      {'p': 'Cost and authorization relate to the asset\'s **acquisition**, and are therefore '
            'ordinarily verified once, in the year the asset was acquired. In subsequent years, '
            'only the remaining four aspects — valuation, existence, beneficial ownership and '
            'presentation/disclosure (VEBOP) — need re-verifying, since cost and authorization '
            'do not change year to year for an asset already on the books.'},
    ], 'src': 'Chapter 6.9', 'sec': '6.9'},
  ]},
}
