CH = {
 'n': 15,
 't': 'Cost Reduction and Control',
 'brief': 'The final chapter closes the loop on everything a cost accountant does: cost control '
          '(keeping actual cost in line with a target) is not enough on its own, especially in a '
          'recession, so this chapter covers cost reduction and the dedicated toolkit built for '
          'it — value analysis, value engineering, Organisation and Methods, work study, and '
          'cost audit — plus a modern coda on managing cost in cloud computing environments.',
 'outcomes': [
   'Explain the terms "cost reduction" and "cost control"',
   'Differentiate between cost reduction and cost control',
   'Explain value analysis and value engineering',
   'Explain Organisation and Methods (O&M)',
   'Explain work study and differentiate between method study and work measurement',
   'Explain cost audit',
 ],
 'secs': [
  {'n': '15.1', 't': 'Introduction', 'b': [
    {'p': 'Changes in the business environment have compelled organisations to adopt methods '
          'that help keep costs to the barest minimum, so they remain competitive and '
          'profitable. The important consideration is that new technology both lowers cost and '
          'improves quality.'},
  ]},

  {'n': '15.2', 't': 'Cost reduction', 'b': [
    {'p': 'Periods of economic recession are usually characterised by a reduction in demand for '
          'products, and cost control alone is not sufficient to improve demand in such periods. '
          'What a firm needs, to remain in business and compete favourably at such times, is '
          '**cost reduction**.'},
    {'def': {'t': 'Cost reduction programme', 'd': 'the real and permanent savings in unit '
                  'operation cost, achieved by reducing cost without impairing consumer '
                  'satisfaction.'}},
    {'h4': 'Two forms of a cost reduction programme'},
    {'table': {'align': 'll', 'head': ['Form', 'How it works'], 'rows': [
      ['**Crash programme**', 'Not planned — reactive measures such as expenditure cutting, '
       'staff retrenchment, and capital expenditure deferment.'],
      ['**Planned programme**', 'Operations are deliberately planned and monitored to ensure '
       'compliance with the cost reduction goal.'],
    ]}},

  ]},

  {'n': '15.2.1', 't': 'Comparison between cost control and cost reduction', 'b': [
    {'table': {'align': 'll', 'head': ['Cost control', 'Cost reduction'], 'rows': [
      ['Ensures actual costs incurred conform with a **target already set** (using techniques '
       'such as standard costing, budgetary control, and capital expenditure control).',
       'Concerned with a **permanent reduction** in cost, without impairing the quality of '
       'products or the efficiency of operations.'],
    ]}},
    {'key': 'The major reason cost reduction exists as its own discipline: **cost control alone '
            'cannot guarantee a firm\'s survival** in a period of economic recession — it can '
            'only keep spending in line with a target that may itself now be unaffordable, not '
            'find genuinely new, permanent savings.'},

  ]},

  {'n': '15.2.2', 't': 'Where to apply cost reduction', 'b': [
    {'p': 'As a general rule, when a new product is to be designed, a firm should introduce cost '
          'reduction at the **product design stage** — design is also then carried through into '
          'the production process stage. At the design stage, it is important to determine the '
          'appropriate facilities to acquire for production. What cost reduction targets:'},
    {'ol': [
      'the use of cheaper materials that will not impair product specification;',
      'reduction in ordering and holding costs;',
      'reduction in re-order period or lead time;',
      'control of overtime work;',
      'adoption of merit rating for promotion;',
      'adequate utilisation of production capacity; and',
      'elimination of non-value time.',
    ]},
  ]},

  {'n': '15.3', 't': 'Value analysis', 'b': [
    {'def': {'t': 'Value analysis', 'd': 'a systematic, interdisciplinary examination of factors '
                  'affecting the cost of a product or service, in order to devise means of '
                  'achieving its specific purpose most economically, at the required standard of '
                  'quality or reliability.'}},
    {'p': 'Value analysis is an approach to improving the value of a product or process by '
          'understanding its constituent components and their associated costs, then seeking '
          'improvements to those components — either by reducing their cost, or by increasing '
          'the value of the functions they deliver.'},
    {'h4': 'Three key concepts of value analysis'},
    {'ol': [
      '**Value** — the ratio between a function\'s contribution to customer satisfaction and the '
      'cost of that function;',
      '**Function** — the effect produced by a product, or one of its elements, in order to '
      'satisfy customer needs; and',
      '**Need** — something that is necessary or desired by the customer.',
    ]},
    {'p': 'The object analysed can be an existing product/process or a new one. It is usually '
          'accomplished by a team, following a structured work plan, with the main purpose of '
          'improving every component in a product.'},
    {'h4': 'The value analysis process'},
    {'steps': [
      'Orientation/preparation',
      'Information',
      'Analysis',
      'Innovation/creativity',
      'Evaluation',
      'Implementation and monitoring',
    ]},
    {'note': 'Applying value analysis needs only basic techniques such as matrices, Pareto '
             'charts, PERT and Gantt diagrams — most of the process is structured thinking, not '
             'specialised technical tooling.'},
    {'p': 'The producer measures value analysis as the relationship between product worth and '
          'product cost:'},
    {'tex': '\\text{Value} = \\dfrac{\\text{Product worth}}{\\text{Price paid}}'},
    {'key': 'The higher this ratio, the higher the customer\'s satisfaction — value analysis is '
            'ultimately about maximising *worth received per unit of price paid*, not simply '
            'minimising price.'},
    {'h4': 'Advantages of value analysis'},
    {'ul': [
      'A high customer orientation, focusing on the aspects of a product/service that better '
      'satisfy customer needs;',
      'Cost reduction by eliminating functions that supply no specific advantage toward '
      'satisfying customer requirements;',
      'New ideas from the creativity/innovation phase, which may bring radical changes and '
      'competitive advantages the market will notice; and',
      'A new systematic mentality carried forward into the design of future products, or to '
      'systematically improve existing ones.',
    ]},
    {'h4': 'Rules for a successful value analysis exercise'},
    {'ul': [
      'Avoid making generalisations and superficial statements — be precise at every moment;',
      'Collect, determine and examine all costs involved — only when one is genuinely cost-'
      'conscious is it possible to determine the value of the thing being assessed; and',
      'Make use of information from the best possible sources.',
    ]},
  ]},

  {'n': '15.4', 't': 'Value engineering', 'b': [
    {'p': 'Value engineering is an organised approach to providing the necessary functions of a '
          'product or service at the **lowest cost**. From its inception, the concept was seen '
          'as a cost-validation exercise that did not affect product quality.'},
    {'warn': 'That original framing — "does not affect quality" — is now seen as a shortcoming '
             'of the definition itself, since it left no room for genuinely *enhancing* value, '
             'not just holding it constant. The terminology has since been broadened accordingly '
             '(see below), and the chapter presents both formulations deliberately: the '
             'historical starting point, and the fuller definition that replaced it.'},
    {'def': {'t': 'Value engineering (current definition)', 'd': 'an organised approach to the '
                  'identification and elimination of unnecessary cost — formally, a redesign of '
                  'an activity, product or service so that value to the customer is enhanced '
                  'while costs are reduced (or, at least, increased by less than the resulting '
                  'price increase).'}},
    {'def': {'t': 'Unnecessary cost', 'd': 'a cost which does not provide use, life, quality, '
                  'appearance, or customer features, and does not add to customer satisfaction.'}},
    {'h4': 'Tasks involved in value engineering practice'},
    {'ol': [
      'Preparing and administering maintenance programmes;',
      'Forecasting expenditure flows;',
      'Advising on cost limits and preparing budgets;',
      'Advising on cash flow forecasting;',
      'Advising on life cycle costing;',
      'Cost analysis;',
      'Cost-benefit analysis;',
      'Estimating;',
      'Evaluating alternative designs;',
      'Investment appraisal; and',
      'Measuring and describing construction work, but only in terms of cost planning.',
    ]},
    {'key': 'Value **analysis** and value **engineering** are close relatives, not synonyms: '
            'analysis is the *examination* — understanding components and costs to find where '
            'improvement is possible; engineering is the *redesign* that acts on those findings '
            'to eliminate unnecessary cost while protecting or enhancing value.'},
  ]},

  {'n': '15.5', 't': 'Organisation and Methods (O&M)', 'b': [
    {'p': 'Organisation and Methods originated with the pioneers of scientific management — '
          'Taylor and Gilbreth — whose work influenced the early approaches to, and eventual '
          'establishment of, the function.'},
    {'def': {'t': 'Organisation and Methods (O&M)', 'd': 'the systematic examination of '
                  'activities in order to improve the effective use of human and other material '
                  'resources.'}},
    {'p': 'O&M is a specialist function whose primary objective is improving an organisation\'s '
          'efficiency and control — an essential function that should be part of the make-up of '
          'any organisation. O&M and its associated techniques form the basis for:'},
    {'ol': [
      'Business Process Re-engineering; and',
      'Business Process Improvement.',
    ]},
    {'p': 'Because line management typically lacks the time or specialist skill to provide this '
          'service themselves, O&M functions as a **consultative service** to management — staff '
          'and management working daily on a process may not be able to think far beyond it, '
          'and so miss obvious improvement opportunities that a fresh outlook, from O&M '
          'principles, is able to spot.'},
    {'note': 'Until recently, O&M departments existed as a clearly identifiable unit within '
             'organisations. In more recent times the function has commonly been renamed '
             '**Project Management** or **Business Improvement**, and in many organisations '
             'today it has been subsumed into other functions — most often IT.'},
    {'h4': 'The O&M approach — six steps'},
    {'steps': [
      'Select the area/process that requires attention;',
      'Record the current situation;',
      'Examine and analyse the existing situation;',
      'Develop, design and evaluate alternative solutions, and recommend improvement '
      'opportunities;',
      'Implement the chosen solution; and',
      'Monitor and maintain the implemented solution.',
    ]},
    {'key': 'O&M is indispensable precisely because it provides a basis for the approach to '
            '**almost any project**, regardless of the specific process being examined.'},
  ]},

  {'n': '15.6', 't': 'Work study', 'b': [
    {'def': {'t': 'Work study', 'd': 'a system of increasing or maximising the productivity of '
                  'an operating unit by reorganising the work of that unit.'}},
    {'p': 'Work study is sub-divided into two major methods:'},
    {'table': {'align': 'll', 'head': ['Method', 'Definition'], 'rows': [
      ['**Method study**', 'The recording and critical examination of existing methods of doing '
       'work, and comparing them with proposed methods, with a view to arriving at easier '
       'methods that would be more effective and cheaper in the long run.'],
      ['**Work measurement**', 'Seeks to measure the time required for a qualified worker to '
       'complete a specific assignment, at a specified level of performance.'],
    ]}},
    {'key': '§15.6\'s own distinction, stated plainly: **method study asks "what is the best way '
            'to do this work?"**, while **work measurement asks "how long should the best way '
            'take?"** — the two are complementary halves of the same overall work study effort, '
            'not competing techniques.'},
  ]},

  {'n': '15.7', 't': 'Cost audit', 'b': [
    {'p': 'All organisations should strive to ensure their cost structure correctly reflects '
          'operational performance — achievable only where cost audit is carried out as a '
          '**continuous process**. Cost audit assists immensely in the process of cost '
          'reduction.'},
    {'def': {'t': 'Cost Audit (CIMA)', 'd': 'verification of cost records and accounts, and a '
                  'check on adherence to the prescribed cost accounting procedures and their '
                  'continuous relevance.'}},
    {'p': 'Cost audit is a continuous process of auditing current operations, comparing current '
          'audit results with previous audit findings.'},
    {'h4': 'The two forms of cost audit'},
    {'table': {'align': 'll', 'head': ['Form', 'What it ensures'], 'rows': [
      ['**Efficiency (Performance) Audit**', 'That the organisation\'s plans have been carried '
       'out efficiently; that costs incurred are not overstated; and that the organisation\'s '
       'resources are properly utilised.'],
      ['**Propriety Audit**', 'Investigates management plans with respect to financing — its '
       'core aim is to ensure management takes right decisions, and establishes proper control '
       'and monitoring activities.'],
    ]}},

  ]},

  {'n': '15.8', 't': 'Differences between cost audit and financial audit', 'b': [
    {'table': {'align': 'll', 'head': ['Financial Audit', 'Cost Audit'], 'rows': [
      ['May be statutory (compulsory for all PLCs) and, in such instances, must be carried out '
       'by an **external** auditor.', 'Non-statutory, and can be carried out by persons '
       'appointed (internally or externally) by management.'],
      ['Based on specific past records — a "post-mortem" check.', 'Based on current and '
       'continuous operations.'],
      ['Tries to verify **financial** records.', 'Verifies **cost accounting** records.'],
    ]}},

  ]},

  {'n': '15.9', 't': 'Cost audit programme', 'b': [
    {'p': 'A reliable cost audit programme must be designed for the entire organisation, and '
          'kept updated as the organisation\'s activities change. It should cover all three '
          'elements of cost and every other relevant area. For example, the audit programme for '
          '**material transactions** may check:'},
    {'ul': [
      'procedures adopted in selecting suppliers;',
      'reliability of material classification and codification, so that expenditure can be '
      'easily traced;',
      'whether materials are purchased economically;',
      'the control established in the store, and the security established for store items;',
      'the estimate for normal loss, and that abnormal gain receives proper accounting '
      'treatment;',
      'methods adopted for issuing materials from stores to the factory; and',
      'whether there is a quality control unit for testing purchased materials and finished '
      'goods produced.',
    ]},
  ]},

  {'n': '15.10', 't': 'Cost control and cloud systems', 'b': [
    {'p': 'As desirable as moving computing infrastructure to the cloud is, staying within '
          'budget can be a serious challenge — the variables include the amount of storage used, '
          'computing demand, and the application running on each cloud instance. It is important '
          'to know all cloud costs and service requirements, so a good balance is struck between '
          'money spent on cloud infrastructure and the company\'s actual needs.'},
    {'def': {'t': 'Cloud cost management', 'd': 'the process organisations use to keep cloud '
                  'costs under control — whether cloud requirements are left to a single vendor '
                  'or shared across multiple vendors, controlling costs is difficult, and an '
                  'organisation can easily lose track of exactly what services it is consuming '
                  'and whether it is overpaying for them.'}},
    {'p': 'Cloud cost management **tools** help companies control spending by monitoring cloud '
          'use and demand — alerting IT managers about resources that are underutilised, or that '
          'have become unexpectedly expensive.'},
    {'h4': 'Factors that contribute to cloud costs'},
    {'table': {'align': 'll', 'head': ['Factor', 'How it drives cost'], 'rows': [
      ['**Resource usage**', 'The more computing power, storage and bandwidth each cloud '
       'instance uses, the higher the bill — a company that does not monitor resources may be '
       'surprised by unexpectedly high charges.'],
      ['**Instance types**', 'Virtual machines (VMs — software emulating a full operating-system '
       'instance) and containers (prefabricated software packages running a specific '
       'application, several of which can run on one VM) are priced differently; containers are '
       'usually cheaper, though usage fees can erode that gap.'],
      ['**Storage costs**', 'Both the amount of data stored online and the storage type affect '
       'the bill, alongside separate costs for moving data into and out of storage — a data-'
       'intensive business that frequently uploads/downloads can incur substantial charges.'],
      ['**Autoscaling**', 'Automatic scaling of resources up or down on demand can be expensive, '
       'but lets a company handle traffic spikes (e.g. a product going viral) that might '
       'otherwise cripple its servers when performance is needed most.'],
      ['**Geographic location**', 'Different data-centre locations carry different costs; '
       'hosting data far from where it is used can sometimes be cheaper (lower-cost resources/'
       'utilities/infrastructure, or tax incentives), but that saving must be weighed against '
       'increased network latency, slower response times, and security/regulatory concerns.'],
      ['**Support**', 'Contracted or ad hoc support carries an additional cost — support backed '
       'by a service level agreement (SLA), e.g. 99.9% uptime with 24/7 phone support, can be '
       'expensive, but not every cloud instance actually needs that level of guarantee.'],
    ]}},
    {'h4': 'Advantages of cloud cost management'},
    {'ul': [
      '**Cost cutting** — tracking cloud spend lets a business eliminate inefficiencies and '
      'optimise spending, finding (and ideally preventing) waste such as duplicative services '
      'or resources that have outlived their usefulness;',
      '**Cost allocation** — lets a company charge cloud costs back to the departments actually '
      'using the services, giving those departments an incentive to manage their own spending;',
      '**Budgetary control** — helps companies understand what they spend on cloud services and '
      'better set and adhere to a budget, e.g. via chargebacks and showbacks (accounting for '
      'resource consumption without necessarily levying the actual charge);',
      '**Forecasting** — knowing past cloud spend provides a basis for budgeting future '
      'corporate initiatives;',
      '**Visibility** — understanding where and how data and other resources are used, '
      'eliminating duplicative/conflicting databases and securing corporate and customer '
      'information;',
      '**Rightsizing** — detecting an instance created with inappropriate resources (e.g. more '
      'memory/processing cores than the application needs) and suggesting optimisation to save '
      'money.',
    ]},
    {'h4': 'Cloud cost management strategies'},
    {'ol': [
      '**Remove unnecessary instances** — there is no reason to pay for an idle instance, since '
      'the meter generally runs whether it is used or not; identify and turn off what is not '
      'needed.',
      '**Set organisational rules** — internal processes governing who may contract for cloud '
      'services, under what circumstances, and within what spending limits, keep departments '
      'from spinning up unauthorised or wasteful instances.',
      '**Implement autoscaling** — rather than provisioning for maximum load at all times, allow '
      'instances to efficiently accommodate demand surges and dips; autoscaling may be '
      'expensive, but is less costly than paying for more services than are necessary day in and '
      'day out.',
      '**Schedule demand** — not all instances need to run 24/7; shutting down or "sleeping" '
      'instances at night or on weekends, when no one is likely to use them, can save money '
      'without affecting service.',
    ]},
  ]},

  {'n': '15.11', 't': 'Chapter summary', 'b': [
    {'p': 'This chapter, and the whole Cost Accounting study text, close on the theme that cost '
          'management is not a single technique but a **layered discipline**: cost control keeps '
          'actual cost aligned with a pre-set target; cost reduction goes further, finding real, '
          'permanent savings — especially necessary in recession, when a target itself may no '
          'longer be affordable.'},
    {'table': {'align': 'll', 'head': ['Tool', 'What it does'], 'rows': [
      ['**Value analysis**', 'Examines a product/process\'s components and costs to find where '
       'cost can be cut, or value increased, without harming what the customer actually needs.'],
      ['**Value engineering**', 'Acts on those findings — redesigning to eliminate unnecessary '
       'cost while enhancing (or at least protecting) customer value.'],
      ['**Organisation and Methods (O&M)**', 'A consultative, systematic examination of '
       'activities to improve the effective use of human and material resources — the basis for '
       'Business Process Re-engineering/Improvement.'],
      ['**Work study**', 'Method study (finding the *best way* to do work) plus work measurement '
       '(finding *how long* the best way should take).'],
      ['**Cost audit**', 'Continuous verification of cost records and procedures — efficiency/'
       'performance audit plus propriety audit — distinct from financial audit in being '
       'non-statutory, continuous rather than a post-mortem, and focused on cost (not '
       'financial) records.'],
      ['**Cloud cost management**', 'The newest addition to the toolkit — applying the same '
       'underlying discipline (monitor, control, allocate, forecast) to a specifically cloud-'
       'computing cost structure.'],
    ]}},
  ]},

  {'n': '15.12', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'p': 'The study text closes the chapter with eight questions — three multiple-choice and '
          'five short-answer — reproduced below in full with the official answers. The chapter '
          'has **no examination-type questions**; it ends here. (Cost reduction is nonetheless '
          'examined: see Chapter 12\'s examination-type question Q11, ICAG May 1999, which is '
          'worked in §12.20.)'},
    {'eg': {'tag': 'Study text', 't': 'The eight questions, with the official answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following best differentiates cost reduction and cost control? '
        '(A) Cost reduction and cost control are the same; (B) Cost reduction aims to slash '
        'costs whilst cost control aims to increase costs; (C) Cost reduction is a scientific '
        'method of controlling costs whilst cost control is arbitrary; (D) Cost control seeks to '
        'maximise the benefits of every amount spent whilst cost reduction seeks to generally '
        'reduce the cost of products and services; (E) Cost control is used in respect of '
        'products whilst cost reduction is concerned only with services.',
        'Which of the following best describes **Cost Audit**? (A) It is the audit of the cost '
        'of materials; (B) It is the rechecking and confirmation of suppliers\' prices; '
        '(C) It is the process of ascertaining whether every aspect of the business is managed '
        'in the most cost-effective way; (D) It is the independent checking of material costs '
        'from different sources; (E) It is the complete building up of the cost of '
        'manufacturing.',
        'Which of the following best describes **Organisation and Methods**? (A) The total '
        'overhaul of an organisation and its methods of operation in order to improve '
        'profitability; (B) The systematic examination of activities in order to improve the '
        'effective use of human and other natural resources; (C) A complete review of production '
        'processes with a view to improvement; (D) An independent analysis of structures and '
        'policies of an organisation to ensure harmonisation; (E) A periodic review of the '
        'effectiveness of production machinery to ensure their optimum output at all times.',
        'An organised approach to the identification and elimination of unnecessary costs of '
        'running a business is called …………………………..',
        'An approach towards improving the value of a product or process by understanding its '
        'constituent components and the associated costs is known as …………………….',
        'A system of increasing or maximising the productivity of an operating unit by '
        'reorganising the work of that unit is referred to as ……………….',
        'The recording and critical examination of existing methods of doing work, with a view '
        'to coming up with better and more effective methods, is called ………………………..',
        'The measurement of the time required for a qualified worker to complete a specific '
        'assignment is known as …………………………….',
      ]}],
      'a': [
      {'ol': [
        '**D — cost control seeks to maximise the benefits of every amount spent whilst cost '
        'reduction seeks generally to reduce the cost of products and services.** Cost control '
        'keeps costs within a predetermined standard; cost reduction lowers the standard itself '
        '(§15.2.1).',
        '**C — the process of ascertaining whether every aspect of the business is managed in '
        'the most cost-effective way.** Per CIMA, cost audit is the verification of cost records '
        'and accounts and a check on adherence to the prescribed cost accounting procedures and '
        'their continued relevance (§15.7).',
        '**B — the systematic examination of activities in order to improve the effective use of '
        'human and other natural resources.** O&M is the discipline applied to administrative '
        'and clerical work, as work study is to production work (§15.5).',
        '**Cost reduction.**',
        '**Value analysis.**',
        '**Organisation and Methods (O&M).**',
        '**Method study.**',
        '**Work measurement.**',
      ]},
      {'note': 'The study text\'s own answer key gives **4 = Value engineering** and '
               '**5 = Value analysis**. Answer 5 is right, but answer 4 is not: an **organised '
               'approach to the identification and elimination of unnecessary costs of running a '
               'business** is the definition of **cost reduction** itself (§15.2), and in any '
               'case value engineering is applied at the **design** stage of a product rather '
               'than to "the costs of running a business". Question 5\'s wording — improving '
               'the value of an **existing** product or process by examining its components and '
               'their costs — is value analysis, which the key correctly gives. Answers 6, 7 and '
               '8 in the key (work study, method study, work measurement) are shifted by one '
               'against the questions; they have been realigned above.',
       'lbl': 'An error in the study text\'s answer key'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Value (value analysis)', 'tex': '\\dfrac{\\text{Product worth}}{\\text{Price paid}}'},
 ],
 'focus':
   'Like Chapter 14, this chapter is conceptual rather than computational — expect '
   'definition-matching and short-answer questions. The examiner\'s favourite distinction is '
   'cost control vs. cost reduction (target-conformity vs. permanent savings) — know it cold, '
   'since it is also the conceptual thread tying this entire chapter, and this entire study '
   'text, together. The second most-tested pair is value analysis (examining/understanding) '
   'vs. value engineering (redesigning/acting), and the third is method study vs. work '
   'measurement (best way vs. how long the best way takes).',
 'errors': [
   'Treating cost control and cost reduction as synonyms — cost control conforms spending to a '
   'pre-set target; cost reduction finds permanent savings, which is a fundamentally different '
   'and broader goal.',
   'Describing value engineering as "the same thing as value analysis" — analysis examines and '
   'diagnoses; engineering redesigns and acts on what analysis finds.',
   'Confusing method study with work measurement — method study finds the best way to do a '
   'task; work measurement times how long the best way should take. They are the two halves of '
   'work study, not alternatives to each other.',
   'Assuming cost audit is statutory like financial audit — cost audit is explicitly '
   'non-statutory, and can be carried out by persons appointed internally or externally by '
   'management, not necessarily an independent external auditor.',
   'Overlooking that cost reduction is best applied at the **design stage** of a new product, '
   'not only during the production process once the design is already fixed.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Which of the following best differentiates cost reduction and cost control?',
    'o': ['Cost reduction and cost control are the same', 'Cost reduction aims to slash costs '
          'whilst cost control aims to increase costs', 'Cost reduction is a scientific method '
          'of controlling costs whilst cost control is arbitrary', 'Cost control seeks to '
          'maximize the benefits of every amount spent whilst cost reduction seeks to generally '
          'reduce cost of products and services', 'Cost control is used in respect of products '
          'whilst cost reduction is concerned only with services'],
    'a': 3, 'w': 'Cost control ensures actual costs conform to a set target — maximising the '
    'benefit of every amount already budgeted to be spent — while cost reduction seeks a real, '
    'permanent reduction in the cost of products and services themselves.',
    'src': 'Chapter 15.2', 'sec': '15.2'},
   {'q': 'Which of the following best describes Cost Audit?',
    'o': ['It is the audit of the cost of materials', 'It is the rechecking and confirmation of '
          'suppliers\' prices', 'It is the process of ascertaining whether every aspect of the '
          'business is managed in the most cost-effective way', 'It is the independent checking '
          'of material costs from different sources', 'It is the complete building up of cost of '
          'manufacturing'],
    'a': 2, 'w': 'CIMA defines cost audit as verification of cost records and accounts and a '
    'check on adherence to prescribed cost accounting procedures — in substance, an ongoing '
    'check that every aspect of the business is managed in the most cost-effective way.',
    'src': 'Chapter 15.7', 'sec': '15.7'},
   {'q': 'Which of the following best describes Organisation and Methods?',
    'o': ['The total overhaul of an organisation and its methods of operation in order to '
          'improve profitability', 'The systematic examination of activities in order to improve '
          'the effective use of human and other material resources', 'A complete review of '
          'production processes with a view to improvement', 'An independent analysis of '
          'structures and policies of an organisation to ensure harmonisation', 'A periodic '
          'review of the effectiveness of production machinery to ensure their optimum output '
          'at all times'],
    'a': 1, 'w': 'This is the chapter\'s own definition of O&M — the systematic examination of '
    'activities to improve the effective use of human and other material resources.',
    'src': 'Chapter 15.5', 'sec': '15.5'},
   {'q': 'An organised approach to the identification and elimination of unnecessary costs of '
         'running a business is called',
    'o': ['Value analysis', 'Cost audit', 'Value engineering', 'Work study', 'Cost reduction'],
    'a': 2, 'w': 'Value engineering is defined as an organised approach to the identification '
    'and elimination of unnecessary cost.',
    'src': 'Chapter 15.4', 'sec': '15.4'},
   {'q': 'An approach towards improving the value of a product or process by understanding its '
         'constituent components and the associated costs is known as',
    'o': ['Value engineering', 'Cost reduction', 'Value analysis', 'Work measurement', 'Method '
          'study'],
    'a': 2, 'w': 'Value analysis is the systematic, interdisciplinary examination of factors '
    'affecting cost by understanding a product/process\'s constituent components and their '
    'associated costs.',
    'src': 'Chapter 15.3', 'sec': '15.3'},
   {'q': 'The recording and critical examination of existing methods of doing work, with a view '
         'to coming up with better and more effective methods, is called',
    'o': ['Work study', 'Work measurement', 'Method study', 'Value engineering', 'O&M'],
    'a': 2, 'w': 'Method study is defined precisely as the recording and critical examination of '
    'existing methods, compared against proposed methods, to find an easier, more effective and '
    'cheaper method.',
    'src': 'Chapter 15.6', 'sec': '15.6'},
   {'q': 'Which of the following is a genuine difference between financial audit and cost '
         'audit?',
    'o': ['Financial audit is non-statutory while cost audit is always statutory', 'Financial '
          'audit is based on current, continuous operations while cost audit is a post-mortem '
          'check', 'Financial audit may be statutory for PLCs while cost audit is non-statutory',
          'Cost audit must always be carried out by an external auditor', 'There is no genuine '
          'difference — the two terms describe the same process'],
    'a': 2, 'w': 'Financial audit may be statutory (compulsory for PLCs, requiring an external '
    'auditor), while cost audit is non-statutory and can be carried out by persons appointed '
    'internally or externally by management.',
    'src': 'Chapter 15.8', 'sec': '15.8'},
   {'q': 'A "crash programme" form of cost reduction is best described as',
    'o': ['A carefully planned and monitored set of operations', 'An unplanned response, such as '
          'expenditure cutting, staff retrenchment or capital expenditure deferment', 'A '
          'statutory audit procedure', 'A form of value engineering only', 'A method used '
          'exclusively in cloud cost management'],
    'a': 1, 'w': 'A crash programme is explicitly the *unplanned* form of cost reduction — '
    'reactive measures such as expenditure cutting, staff retrenchment and capital expenditure '
    'deferment, as opposed to a planned programme where operations are deliberately planned and '
    'monitored.',
    'src': 'Chapter 15.2', 'sec': '15.2'},
  ],
  'theory': [
   {'q': 'Distinguish between cost control and cost reduction, and explain why cost reduction is '
         'needed even where cost control is already in place.',
    'marks': 6,
    'a': [
      {'p': '**Cost control** ensures that actual costs incurred conform with a target that has '
            'already been set, using techniques such as standard costing, budgetary control and '
            'capital expenditure control.'},
      {'p': '**Cost reduction** is concerned with achieving a **permanent** reduction in cost, '
            'without impairing the quality of products or the efficiency of operations.'},
      {'p': 'Cost reduction is needed alongside cost control because cost control alone cannot '
            'guarantee a firm\'s survival in a period of economic recession: it only keeps '
            'spending aligned with an existing target, but does nothing if that target itself '
            'has become unaffordable as demand falls. Cost reduction finds genuinely new, '
            'permanent savings instead.'},
    ], 'src': 'Chapter 15.2', 'sec': '15.2'},
   {'q': 'Distinguish between value analysis and value engineering, and outline the steps '
         'followed in the value analysis process.',
    'marks': 7,
    'a': [
      {'p': '**Value analysis** is a systematic, interdisciplinary *examination* of the factors '
            'affecting a product or service\'s cost — understanding its components and their '
            'associated costs to find where cost can be reduced, or value increased, without '
            'harming customer satisfaction.'},
      {'p': '**Value engineering** is the organised approach that *acts* on those findings — '
            'redesigning an activity, product or service so that value to the customer is '
            'enhanced while costs are reduced (or increased by less than the resulting price '
            'increase). In short, analysis diagnoses; engineering redesigns.'},
      {'p': 'The value analysis process has six steps: orientation/preparation; information; '
            'analysis; innovation/creativity; evaluation; and implementation and monitoring.'},
    ], 'src': 'Chapter 15.3-15.4', 'sec': '15.3'},
  ]},
}
