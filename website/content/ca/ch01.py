CH = {
 'n': 1,
 't': 'Introduction to Cost Accounting',
 'brief': 'What cost and cost accounting are, the objectives and functions of cost accounting, '
          'the distinction between cost data and cost information, how cost accounting relates '
          'to (and differs from) financial accounting, the conditions and steps for installing a '
          'cost accounting system, and the scope of cost accounting — its elements of cost, '
          'methods and techniques of costing.',
 'outcomes': [
   'Define cost accounting',
   'State the objectives of cost accounting',
   'Explain the role of the cost accountant',
   'Differentiate between cost data and cost information',
   'Explain the scope of cost accounting',
   'Explain the benefits and drawbacks of cost accounting',
   'Explain the different ways of cost classification',
   'Explain the various patterns of cost behaviour',
 ],
 'secs': [
  {'n': '1.1', 't': 'Introduction', 'b': [
    {'p': 'Business organisations exist to provide goods and services **at a profit**. In order '
          'to earn that profit, organisations must know the cost incurred in producing the goods '
          'and services, so that a desired profit margin can be added to the cost to determine '
          'the selling price.'},
    {'p': 'This chapter explains **what constitutes cost**, the **forms of classifying cost** '
          'and the **different patterns of cost behaviour**. It also explains the **role of the '
          'cost accountant**, as well as the **benefits and drawbacks** of cost accounting.'},
    {'key': 'Everything else in this subject rests on this chapter. The three elements of cost '
            '(§1.3.1), the direct/indirect split, and the prime-cost/overhead build-up are the '
            'vocabulary in which every later chapter — materials, labour, overheads, job and '
            'process costing, budgeting, standard costing — is written. Learn the definitions '
            'here precisely rather than approximately.'},
  ]},

  {'n': '1.2', 't': 'Definition of cost', 'b': [
    {'def': {'t': 'Cost', 'd': 'the amount of expenditure incurred on, or attributable to, a '
                  'specified thing or activity. Mathematically, cost is the product of the '
                  'quantity of a given resource used and the price per unit of the quantity of '
                  'resource.'}},
    {'tex': '\\text{Cost} = \\text{Quantity of resource used} \\times \\text{Price per unit}'},
    {'p': 'Costs are usually ascertained in respect of **cost units** or **cost objectives** '
          '(§1.2.2).'},
    {'note': 'The multiplicative form matters more than it looks. Because cost is *quantity × '
             'price*, any change in a total cost has to come from one of exactly two sources — '
             'a change in how much resource was used, or a change in what it cost per unit. That '
             'is the whole idea behind variance analysis in Chapter 13, where every variance '
             'splits into a **usage** (quantity) part and a **price/rate** part.',
     'lbl': 'Why this formula is worth remembering'},
    {'p': 'Sections 1.2.1 to 1.2.12 below follow the study text\'s own numbering. They move from '
          'the definition of cost accounting, through what it is *for* and who does it, to how a '
          'cost accounting system is actually designed and installed in a real organisation.'},
  ]},

  {'n': '1.2.1', 't': 'Definition of cost accounting', 'b': [
    {'def': {'t': 'Cost accounting (CIMA)', 'd': 'the application of accounting and costing '
                  'principles, methods and techniques in the ascertainment of cost, and the '
                  'analysis of savings and/or excesses as compared with previous experience or '
                  'standard.'}},
    {'p': 'From this definition, cost accounting involves:'},
    {'ul': [
      'the application of costing principles, methods and techniques;',
      'the ascertainment of cost; and',
      'the analysis of savings or overages (excesses).',
    ]},
    {'p': 'A second CIMA definition frames it from the management-accounting side:'},
    {'def': {'t': 'Cost accounting (alternative CIMA definition)', 'd': 'that part of management '
                  'accounting which establishes budgets and standard costs, and actual costs of '
                  'operations, processes, departments or products, and the analysis of variances, '
                  'profitability or the social use of funds.'}},
    {'p': 'The issues to remember about this second definition — cost accounting is:'},
    {'ul': [
      'part of **management accounting**;',
      'concerned with establishing budgets, standard costs, actual costs and variances;',
      'about establishing costs and revenues relating to operations, processes, departments and '
      'products — whether standard or actual;',
      'concerned with the analysis of variances;',
      'concerned with the analysis of profitability of ventures and projects; and',
      'concerned with the analysis of the social use of funds.',
    ]},
    {'p': 'Most simply, cost accounting can be defined as **the ascertainment of cost** — finding '
          'out how much is incurred to produce a given product or unit of service.'},

  ]},

  {'n': '1.2.2', 't': 'Cost objective', 'b': [
    {'def': {'t': 'Cost objective', 'd': 'any activity for which a separate measurement of cost is '
                  'desired — a product, a service, a department or segment of the business, a '
                  'function, a process or activity, or indeed anything for which the cost of '
                  'resources used is to be measured.'}},
    {'key': 'A **cost unit** is always a cost objective, but not every cost objective is a cost '
            'unit — some cost objectives (e.g. "the marketing function" as a whole) are broader '
            'than any single unit of product or service. Where a cost cannot be traced *directly* '
            'to a cost unit, it is first traced to a **cost centre**, for further spreading to '
            'cost units.'},

  ]},

  {'n': '1.2.3', 't': 'The objectives of cost accounting', 'b': [
    {'ol': [
      'to ascertain cost and facilitate pricing;',
      'to provide information to assist planning;',
      'to provide information to facilitate decision making;',
      'to provide information to aid control;',
      'to provide motivation and promote cost consciousness at all levels of the management '
      'hierarchy; and',
      'to provide a formal means of gathering detailed information on operations.',
    ]},
    {'p': 'These objectives are achieved through the processes of **cost ascertainment** and '
          '**cost control**, which form the subject matter of the rest of this study text.'},

  ]},

  {'n': '1.2.4', 't': 'Functions of cost accounting / the role of the cost accountant', 'b': [
    {'p': 'The functions of cost accounting are best understood against the four classic '
          'management functions they support:'},
    {'table': {'align': 'll', 'head': ['Function', 'What the cost accounting system provides'],
      'rows': [
      ['**Pricing**', 'Applies costing principles, methods and techniques to ascertain the cost '
       'of units (products, services or processes) — the basis for pricing decisions.'],
      ['**Planning**', 'Planning is establishing goals and suitable courses of action to achieve '
       'them. The cost system generates information on resource availability (materials, '
       'labour, other facilities), cash-flow pattern within a given time horizon, and expected '
       'returns from alternative projects — enabling management to commit scarce resources and '
       'set good priorities.'],
      ['**Decision making**', 'Decision making is choosing among alternatives to achieve defined '
       'objectives. Cost accounting generates a pool of information — how costs behave, their '
       'composition and nature (fixed or variable, sunk or opportunity, incremental, avoidable '
       'or unavoidable) — supporting choices such as make-or-buy, sell-or-further-process, '
       'continue-or-discontinue a product line, and accept-or-reject a special order.'],
      ['**Control**', 'Control is ensuring that plans are actually achieved, through three '
       'elements: (i) set targets/goals in a budget statement (planning); (ii) measure actual '
       'achievement during the control period and compare with the set goals; (iii) analyse and '
       'investigate any resultant variance and take corrective action.'],
    ]}},

  ]},

  {'n': '1.2.5', 't': 'Difference between cost data and cost information', 'b': [
    {'warn': 'This distinction is a favourite short-answer question — cost **data** is the raw '
             'input; cost **information** is what results once that input has been analysed.'},
    {'def': {'t': 'Cost data', 'd': 'factual information concerning the cost of materials, labour '
                  'and overheads and other cost elements, expected to be incurred or actually '
                  'incurred in a business venture.'}},
    {'p': 'Sources of cost data:'},
    {'ol': [
      'potential suppliers, for the purpose of submitting proposals and bids;',
      'existing suppliers, with which the business has developed a solid basis for financial '
      'control; and',
      'cost models.',
    ]},
    {'def': {'t': 'Cost information', 'd': 'the detailed analysis of costs — the calculation of '
                  'production costs, the quantification of loss and the estimation of work '
                  'efficiency — providing a solid basis for financial control. It is used in '
                  'decision making and in planning future operations, and it assists in '
                  'establishing company performance standards partly from past cost history.'}},
    {'key': 'Cost data are like the **inputs** from which cost information is **generated**.'},

  ]},

  {'n': '1.2.6', 't': 'Advantages (benefits) of cost accounting', 'b': [
    {'ol': [
      'helps identify profitable and unprofitable products and services, so management can make '
      'prudent decisions on adopting a new product or discontinuing a product line;',
      'helps identify efficient and inefficient methods and take corrective measures — areas of '
      'wastage are indicated, idle time is highlighted, and loopholes/system weaknesses are '
      'identified;',
      'generates comparative information on jobs, products and projects over time (temporal '
      'comparison for one cost centre) and across a number of cost centres (cross-sectional '
      'comparison), making effective control possible;',
      'facilitates production control — costing principles keep material, labour and expense '
      'costs at desirable levels, enhancing production planning and scheduling;',
      'facilitates inventory control costing, establishing procedures for the procurement, '
      'storage and issue of inventory items; and',
      'facilitates accurate estimation of the cost of various cost units — essential for pricing.',
    ]},

  ]},

  {'n': '1.2.7', 't': 'Disadvantages (drawbacks) of cost accounting', 'b': [
    {'ol': [
      'analysing cost data itself involves expense and cost;',
      'some costing systems are complex and cumbersome, and thus not well understood by the '
      'managers who need to operate them; and',
      'producing the basic data requires completing many forms; where inaccurate data is '
      'supplied, the foundation of subsequent analysis is weakened.',
    ]},

  ]},

  {'n': '1.2.8', 't': 'Relationship between cost accounting and financial accounting', 'b': [
    {'def': {'t': 'Financial accounting', 'd': 'that part of accounting that records actual '
                  'transactions of an entity in monetary terms, in accordance with established '
                  'concepts, principles, accounting standards and legal requirements, and '
                  'presents as accurate a view as possible of the effects of those transactions '
                  'over a period of time and at the end of that time. It concerns an '
                  'enterprise\'s relationship with creditors, debtors, banks and revenue '
                  'authorities, culminating in periodical financial statements for users outside '
                  'the business.'}},
    {'p': 'Financial accounting has been criticised for these weaknesses, all of which cost '
          'accounting exists to remedy:'},
    {'ol': [
      'no information is given about individual jobs, products or processes;',
      'it is historical — financial information is not available until the end of the '
      'accounting period, so cost data relates to the past;',
      'it does not require costs to be classified into direct/indirect, controllable/'
      'non-controllable, normal/abnormal, variable/fixed, etc.;',
      'detailed records of inventory movement are not kept, which inhibits efficient inventory '
      'control; and',
      'generally, there is no budget plan.',
    ]},
    {'table': {'align': 'llll', 'head': ['Factor', 'Cost accounting', 'Financial accounting'],
      'rows': [
      ['Nature of costs/revenue', 'Predetermined estimates, standards and budgets',
       'Historical and past costs/revenue'],
      ['Users of information', 'Management of the business enterprise',
       'Management and external stakeholders — shareholders, creditors, debtors, tax '
       'authorities, investors, etc.'],
      ['Objectives', 'Provide information to aid planning, decision making and control',
       'Satisfy the stewardship function of management — account for the use of resources '
       'entrusted to management'],
      ['Conformity to concepts/standards', 'No need to comply with standards and concepts',
       'Absolute need to comply meticulously with accounting concepts and standards'],
      ['Scope and form of presentation', 'Determined by management, on relevance and '
       'cost-benefit grounds', 'Determined by concepts, standards and legal provisions'],
      ['Precision of information', 'Approximations permitted (uncertainty in estimates), but '
       'must be sufficiently precise and accurate',
       'Information must be more precise — usually audited by independent external auditors to '
       'confirm reliability'],
    ]}},

  ]},

  {'n': '1.2.9', 't': 'Conditions necessary for an effective cost accounting system', 'b': [
    {'p': 'The purpose of cost accounting is achieved only when an effective system is in place — '
          'one tailor-made to the business\'s own environment: simple, economical and practical. '
          'Conditions for a successful system:'},
    {'ol': [
      'co-operation and co-ordination among all staff members, including management;',
      'a proper system of stores and inventory control;',
      'adequate payroll procedures;',
      'an improved system of data capture — standardised pre-printed forms are recommended for '
      'recording receipts of materials, issue of materials, labour attendance time and hours '
      'worked, and wage calculations;',
      'a sound plan for collecting all indirect costs under suitable headings and absorbing them '
      'into products or service departments on a predetermined basis;',
      'a costing department or section, with the cost accountant\'s responsibilities and duties '
      'clearly defined; and',
      'cost accounts and financial accounts maintained so that their results can be reconciled '
      'easily.',
    ]},

  ]},

  {'n': '1.2.10', 't': 'Steps in installing a cost accounting system', 'b': [
    {'p': 'Installing a cost accounting system is substantial — it needs detailed discussion with '
          'management and staff, and careful analysis of the correct procedures and records. The '
          'generally recommended stages:'},
    {'steps': [
      'Establish the objectives and scope of the proposed system through discussion and '
      'agreement with management.',
      'Analyse the current system — are there cost centres? Is there a coding system? What '
      'accounting records does the existing system maintain?',
      'Study the current system — staff composition (qualification, experience, competence); '
      'the production system and methods (jobbing/engineering, contract, service?); store-'
      'keeping systems; wage systems.',
      'Think through the type and nature of the cost accounting system required — job/batch, '
      'contract, process or service costing? Full absorption, marginal or standard costing? What '
      'method prices store issues? What remuneration methods are desirable? What is the basis of '
      'overhead absorption?',
      'Design the system in collaboration with management and the staff who will operate it.',
      'Prepare an operating manual for all personnel, showing procedures, objectives and codes.',
      'Arrange training and instruction for all staff involved in implementing the system.',
      'Implement the system with full publicity.',
      'Monitor the system closely and report to management periodically.',
      'Build a feedback mechanism into the system.',
    ]},

  ]},

  {'n': '1.2.11', 't': 'Problems inherent in the installation of a cost accounting system', 'b': [
    {'p': 'General factors defining different problems for a given system:'},
    {'ul': [
      'size of the organisation;', 'type of product/service;', 'the production process;',
      'the methods of manufacture; and', 'availability of staff.',
    ]},
    {'p': 'Other specific problems:'},
    {'ul': [
      'definition of responsibility;', 'definition or designation of cost centres;',
      'compilation of a comprehensive cost system;', 'availability of staff;',
      'labour hours worked;', 'machine utilisation time;', 'scrap treatment;',
      'rectification cost; and', 'the difficulty of accurate cost classification.',
    ]},

  ]},

  {'n': '1.2.12', 't': 'Principles of a good cost accounting system', 'b': [
    {'ol': [
      'the system itself must be appropriate to the organisation and its processes or business;',
      'reports, statements and analyses must contain relevant information for their intended '
      'purpose — information is relevant when it has value that helps resolve a problem;',
      'reports must be produced at appropriate intervals, and promptly — a late report loses '
      'relevance;',
      'reports must be addressed to the persons with the capacity to act on their subject matter;',
      'information must be sufficiently accurate to be reliable, or decisions will rest on '
      'invalid foundations;',
      'reports should be simple and understandable — jargon and complex terminology should be '
      'avoided as much as possible; and',
      'the benefits from generating information should outweigh the cost of generating it.',
    ]},
  ]},

  {'n': '1.3', 't': 'Scope of cost accounting', 'b': [
    {'p': 'The "scope" of cost accounting means the ground it covers: what a cost is built out '
          'of, how it is accumulated, what techniques are applied to it, what information the '
          'system alone can produce, where in the organisation it sits, and who uses it. '
          'Sections 1.3.1 to 1.3.9 take those in turn, following the study text\'s own '
          'numbering.'},
  ]},

  {'n': '1.3.1', 't': 'Elements of cost', 'b': [
    {'p': 'There are three elements of cost — **materials**, **labour** and **expenses** — giving '
          'three classes of cost: materials cost, labour cost and expenses. Each element can be '
          'either **direct** or **indirect**.'},
    {'table': {'align': 'lll', 'head': ['Element', 'Meaning', 'Typical examples'], 'rows': [
      ['**Material costs**', 'Costs of materials or commodities (other than fixed assets) '
       'introduced into a product or consumed in operations — the cost of materials input into '
       'goods and services.', 'Raw materials, component parts, work in progress, primary '
       'packing materials, lubricating oil, consumable tools, stationery, cleaning materials.'],
      ['**Labour cost**', 'The cost of employee remuneration — payments made to and on behalf of '
       'employees for offering labour services in the production function.', '—'],
      ['**Expenses**', 'Costs other than material costs and labour costs.', 'Hiring and '
       'maintaining special equipment, royalty payments, copyright/patent payments, utilities '
       '(electricity, water), rent.'],
    ]}},

    {'h4': 'Direct costs'},
    {'def': {'t': 'Direct cost', 'd': 'a cost that can be directly identified and charged to a '
                  'cost unit without apportionment.'}},
    {'p': 'Direct costs comprise direct material cost, direct labour cost and direct expenses:'},
    {'table': {'align': 'lll', 'head': ['Type', 'Meaning', 'Examples'], 'rows': [
      ['**Direct material cost**', 'Cost of material that can be physically identified with a '
       'specific cost unit — materials entering into and becoming a constituent element of a '
       'product or saleable service; allocated directly to cost units.', 'Materials purchased '
       'specifically for a job order or process; materials requisitioned from store for a '
       'particular production order; work-in-progress and component parts; primary packing '
       'materials (cartons, wrapping material).'],
      ['**Direct labour (wages)**', 'Cost of employees\' efforts and skills applied directly to a '
       'product or saleable service; allocated directly to cost units.', 'Wages of production '
       'operatives transforming raw materials into finished goods; wages of waiters serving '
       'meals at a hotel; wages of sales assistants selling goods in a retail shop.'],
      ['**Direct expenses**', 'Costs (other than material and labour cost) that can be identified '
       'with and charged or allocated to a cost unit — incurred for a specific product or '
       'saleable service.', 'Hiring special equipment for a particular production order (and '
       'maintaining it); royalty payments; travelling expenses to a contract site.'],
    ]}},
    {'note': 'Some materials that could qualify as direct materials may be treated as indirect '
             'materials, purely for reasons of materiality and convenience — a low-value item '
             'used across many products is not worth tracking unit by unit.'},
    {'fbox': {'h': 'Prime cost', 'rows': [
      {'lb': 'Prime cost', 'tex': '\\text{Prime cost} = \\text{Direct materials} + '
        '\\text{Direct labour} + \\text{Direct expenses}'},
    ]}},

    {'h4': 'Indirect costs (overheads)'},
    {'def': {'t': 'Indirect cost (overhead)', 'd': 'a cost that cannot be identified with and '
                  'allocated to a cost unit, but must be apportioned to a number of cost centres '
                  'and further absorbed by cost units.'}},
    {'table': {'align': 'lll', 'head': ['Type', 'Meaning', 'Examples'], 'rows': [
      ['**Indirect material cost**', 'Cost of material items that cannot be identified with any '
       'one product, because they benefit all products rather than one specific product — '
       'apportioned and absorbed by cost units, not allocated to them.', 'Materials for '
       'operating/maintaining plant and equipment (lubricating oil, consumable tools); '
       'stationery; cleaning materials (soap and detergents, rugs and dusters, brooms and '
       'brushes).'],
      ['**Indirect labour cost**', 'Wages of employees who do not work on the product itself but '
       'assist the manufacturing process; apportioned to cost centres and assigned to cost units '
       'through absorption, not allocated directly.', 'Salaries of factory supervisors; wages of '
       'store-department employees; wages of cleaners.'],
      ['**Indirect expenses**', 'Expenses incurred in general, not for a specific cost unit.',
       'Selling and distribution (advertising, sales promotion); administrative (stationery, '
       'audit/consultancy fees, secretarial charges); production (rent, insurance, '
       'electricity).'],
    ]}},
    {'fbox': {'h': 'Overhead and cost card build-up', 'rows': [
      {'lb': 'Overhead', 'tex': '\\text{Overhead} = \\text{Indirect materials} + '
        '\\text{Indirect labour} + \\text{Indirect expenses}'},
    ]}},
    {'table': {'align': 'lr', 'head': ['Cost card (elements + nature)', ''], 'rows': [
      ['Direct material cost', 'xx'], ['Direct labour cost', 'xx'], ['Direct expenses', 'xx'],
      ['**Prime cost**', 'xxx'], ['Indirect material cost', 'xx'], ['Indirect labour cost', 'xx'],
      ['Indirect expenses', 'xx'], ['**Overhead cost**', 'xxx'], ['**Total cost**', 'xxx', '@tot'],
    ]}},

  ]},

  {'n': '1.3.2', 't': 'Methods of costing', 'b': [
    {'p': 'The method used to determine the cost of a product or service is dictated by factors '
          'such as the nature of the cost unit, the production process, the mode of cost '
          'accumulation, and the duration of work. The well-established methods:'},
    {'ul': [
      '**Job/batch costing**', '**Contract costing**', '**Process costing**', '**Service costing**',
    ]},
    {'p': 'Each is covered in detail in later chapters.'},

  ]},

  {'n': '1.3.3', 't': 'Techniques of costing', 'b': [
    {'p': 'Independently of which *method* is used, a cost accounting system also applies one of '
          'these *techniques*:'},
    {'ul': ['**Absorption costing**', '**Marginal costing**', '**Standard costing** (itself using '
      'either absorption or marginal costing)']},

  ]},

  {'n': '1.3.4', 't': 'Information exclusively generated from a cost accounting system', 'b': [
    {'ol': [
      'statements of material, direct labour and machine utilisation showing trends and values;',
      'cost of products and services broken down into material cost, labour cost and other '
      'expenses, compared against estimates;',
      'cost control statements for each section/department, showing actual results against '
      'budget;',
      'periodic inventory valuation reports;',
      'scrap and rectification cost reports; and',
      'budgets for planning and control — including cash budgets for monitoring liquidity.',
    ]},

  ]},

  {'n': '1.3.5', 't': 'Cost accounting as part of the management information system', 'b': [
    {'p': 'Management needs information for decision making, planning and control, requiring a '
          'management information system. Cost accounting (and management accounting more '
          'broadly) is an integral part of that system, providing information for:'},
    {'ul': [
      'formulation of policy;', 'planning and controlling the activities of the enterprise;',
      'decision making;', 'disclosure to external stakeholders;', 'disclosure to employees; and',
      'safeguarding the assets of the enterprise.',
    ]},
    {'p': 'In more detail, the cost accounting function is useful in four managerial areas:'},
    {'table': {'align': 'll', 'head': ['Area', 'How cost accounting helps'], 'rows': [
      ['**Policy formulation**', 'Helps decide what products to sell, in what markets to '
       'operate, and at what selling prices.'],
      ['**Planning**', 'Provides data to evaluate capital-expenditure proposals and past '
       'performance to guide future performance; is central to establishing budgetary '
       'procedures/timetables and coordinating short-term plans across the business, including '
       'preparing the master budget.'],
      ['**Control**', 'Produces performance reports comparing actual results with intended '
       'results for each responsibility centre, drawing management attention to trouble spots.'],
      ['**Decision making**', 'The analysis of costs and revenues in cost accounting reports '
       'guides decisions directly.'],
    ]}},

  ]},

  {'n': '1.3.6', 't': 'Organisations other than manufacturing companies where cost accounting can be applied', 'b': [
    {'p': 'Every organisation uses some items of stores or materials — including non-profit '
          'bodies — so cost accounting applies far beyond manufacturing:'},
    {'ul': [
      '**Local authorities** — District, Municipal or Metropolitan Assemblies (e.g. Accra '
      'Metropolitan Authority, Kano Municipal Local Government, Lagos Island Local Education '
      'Authority);',
      '**Health-sector organisations** — hospitals, clinics;',
      '**Educational institutions** — colleges, polytechnics, universities;',
      '**Financial institutions** — banks, insurance companies;',
      '**Transport businesses**;',
      '**Consultancy firms** — accounting/audit firms, economic/management consultancies, legal '
      'chambers;',
      '**Utility companies** — water, electricity;',
      '**Farming ventures**; and',
      '**Trading outlets** — retailing, wholesaling, departmental stores, supermarkets.',
    ]},
    {'p': 'For such organisations, cost accounting can generate: cost per unit of product/'
          'service; cost of running the organisation by section/department; wages cost per unit '
          'and material cost per unit; cost per patient per consulting hour or per bed; '
          'budgetary control statements; cost per full-time-equivalent student; and branch '
          'operating statements.'},

  ]},

  {'n': '1.3.7', 't': 'Value of cost information in the management decision-making process', 'b': [
    {'p': 'Business is dynamic — management must review decisions currently being implemented, '
          'and take fresh decisions for the near and distant future, in line with industry '
          'trends, if the business is to remain competitive. Inflation, for instance, renders '
          'cost structures obsolete as a shift in price indices forces a rework of every cost '
          'element; a change in foreign exchange rates can adversely affect costing for import- '
          'or export-dependent industries. If product cost changes, selling price must follow — '
          'sometimes as often as daily. Without cost information, management cannot respond to '
          'the on-the-spot decisions that dynamic business situations demand.'},

  ]},

  {'n': '1.3.8', 't': 'Impact of information technology on the generation, evaluation and presentation of cost information', 'b': [
    {'p': 'Management cannot afford late information — an untimely piece of information can be '
          'more damaging than none at all. Financial information often comes in arrears, since a '
          'reporting period must expire before complete figures can be compiled; acceptable for '
          'historical purposes, but potentially critical for a business facing stiff competition '
          'or operating under tight conditions, where even a day\'s delay matters.'},
    {'p': 'IT supports businesses with online, real-time reporting to management — with a good '
          'information network, top management can access figures almost as soon as they are '
          'generated at the shop-floor level. Controls can be built directly into the system, '
          'e.g. requiring authorisation before supplying a debtor who has exceeded their credit '
          'limit/period. IT also reduces the time spent generating paperwork and obtaining '
          'physical authorisations, since the system does the groundwork itself and passes '
          'results to management on-line.'},

  ]},

  {'n': '1.3.9', 't': 'Roles required of accounting technicians in collection, analysis and presentation of cost information', 'b': [
    {'p': 'The accounting technician drives the day-to-day detail of information presentation — '
          'laxity here has a profound, adverse effect on the quality and timeliness of the '
          'information management relies on. Specifically, the technician is expected to:'},
    {'ol': [
      'ensure established formats for data compilation are correctly followed at every level;',
      'monitor the regularity of data entry to ensure timeliness — hourly, daily, weekly and '
      'monthly reports as required;',
      'confirm the accuracy of figures supplied, through reasonableness checks or other '
      'independent sources;',
      'raise flags where extraneous or extraordinary figures appear;',
      'prepare summaries of raw data showing results from various perspectives (e.g. sales by '
      'branch, by period, by salesman, by season) to give a total picture;',
      'draw summaries that are simple, straightforward and concise — not too voluminous for a '
      'busy executive, without losing relevance; and',
      'pre-empt questions with explanatory notes on the trends and movements observed.',
    ]},
  ]},

  {'n': '1.4', 't': 'Worksheet summary — definitions and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§1.1 Introduction** — organisations must know cost in order to add a margin and set a '
      'selling price; this chapter covers what cost is, how it is classified, how it behaves, '
      'the cost accountant\'s role, and the benefits and drawbacks of cost accounting.',
      '**§1.2 Definition of cost** — expenditure incurred on or attributable to a specified '
      'thing or activity; cost = quantity of resource used × price per unit; ascertained per '
      'cost unit or cost objective.',
      '**§1.2.1 Definition of cost accounting** — CIMA\'s two definitions (application of '
      'costing principles/methods/techniques to ascertain cost and analyse savings or excesses; '
      'and that part of management accounting establishing budgets, standard costs, actual '
      'costs and variances), plus the simplest form — the ascertainment of cost.',
      '**§1.2.2 Cost objective** — any activity for which a separate measurement of cost is '
      'desired; every cost unit is a cost objective but not every cost objective is a cost '
      'unit; untraceable costs go first to a cost centre.',
      '**§1.2.3 Objectives of cost accounting** — six of them, achieved through cost '
      'ascertainment and cost control.',
      '**§1.2.4 Functions / the role of the cost accountant** — four: pricing, planning, '
      'decision making, and control (control itself having three elements: set targets, measure '
      'and compare, analyse the variance and act).',
      '**§1.2.5 Cost data vs cost information** — data are the raw factual inputs (three named '
      'sources); information is the analysed output.',
      '**§1.2.6–1.2.7 Advantages and drawbacks** — six advantages, three drawbacks.',
      '**§1.2.8 Relationship with financial accounting** — the definition of financial '
      'accounting, its five stated weaknesses, and Fig 1.1\'s six-factor comparison table.',
      '**§1.2.9 Conditions for an effective system** — seven, starting from co-operation and '
      'co-ordination among all staff.',
      '**§1.2.10 Steps in installing a system** — the ten-stage process from establishing '
      'objectives through to building in a feedback mechanism.',
      '**§1.2.11 Problems in installation** — five general factors plus the specific problems.',
      '**§1.2.12 Principles of a good system** — seven, ending with the cost-benefit test.',
      '**§1.3 Scope** — §1.3.1 three elements of cost (materials/labour/expenses), each split '
      'direct/indirect, giving prime cost and overhead; §1.3.2 four costing methods (job/batch, '
      'contract, process, service); §1.3.3 three costing techniques (absorption, marginal, '
      'standard); §1.3.4 the six information outputs only a cost system produces; §1.3.5 cost '
      'accounting within the MIS (policy, planning, control, decision making); §1.3.6 the nine '
      'classes of non-manufacturing organisation that use it; §1.3.7 the value of cost '
      'information (inflation, exchange rates); §1.3.8 IT\'s impact; §1.3.9 the accounting '
      'technician\'s seven specific roles.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Cost** — expenditure incurred on/attributable to a specified thing or activity; '
      'quantity × price per unit.',
      '**Cost accounting** — application of costing principles/methods/techniques to ascertain '
      'cost and analyse variance; part of management accounting.',
      '**Cost objective** — any activity for which a separate cost measurement is desired. '
      '**Cost unit** — a cost objective that is a quantitative unit of product/service (every '
      'cost unit is a cost objective; not every cost objective is a cost unit).',
      '**Cost centre** — where a cost is first traced when it cannot go directly to a cost unit.',
      '**Cost data** — raw factual cost information (the input). **Cost information** — the '
      'analysed output used for decisions.',
      '**Prime cost** — direct materials + direct labour + direct expenses. **Overhead** — '
      'indirect materials + indirect labour + indirect expenses.',
      '**Direct cost** — traced to a cost unit without apportionment. **Indirect cost** — '
      'apportioned to cost centres, then absorbed by cost units.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': 'Cost', 'tex': 'C = q \\times p', 'nt': 'q = quantity of resource used, p = price per '
   'unit of the resource.'},
  {'lb': 'Prime cost', 'tex': '\\text{Prime cost} = \\text{DM} + \\text{DL} + \\text{DE}',
   'nt': 'DM = direct materials, DL = direct labour, DE = direct expenses.'},
  {'lb': 'Overhead', 'tex': '\\text{Overhead} = \\text{IM} + \\text{IL} + \\text{IE}',
   'nt': 'IM = indirect materials, IL = indirect labour, IE = indirect expenses.'},
  {'lb': 'Total cost', 'tex': '\\text{Total cost} = \\text{Prime cost} + \\text{Overhead}'},
 ],
 'focus':
   'Almost every diet asks at least one definition question straight from this chapter — cost '
   'data vs cost information, cost objective vs cost unit, and the cost-accounting-vs-financial-'
   'accounting comparison (Fig 1.1) are the three most examined. The direct/indirect split of '
   'each cost element and the prime-cost/overhead build-up are the numerical foundation for '
   'almost every later chapter\'s costing method — get these exactly right here.',
 'errors': [
   'Treating "cost objective" and "cost unit" as synonyms — every cost unit is a cost objective, '
   'but not every cost objective is a cost unit.',
   'Confusing cost data (raw, factual) with cost information (analysed, decision-ready).',
   'Forgetting that indirect costs are apportioned to cost centres and only then absorbed by '
   'cost units — never allocated directly, unlike direct costs.',
   'Listing "ascertaining fraud" as an objective of cost accounting — investigation of fraud is '
   'not one of the six stated objectives; it is easily confused with control.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Cost accounting is best described, in its simplest form, as',
    'o': ['the preparation of the balance sheet', 'the writing off of costs',
          'the ascertainment of cost', 'the preparation of a statement of value added',
          'the annual audit of financial statements'],
    'a': 2,
    'w': 'Cost accounting can be defined most simply as the ascertainment of cost — finding out '
         'how much is incurred to produce a given product or unit of service.',
    'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'Cost accounting is an integral part of',
    'o': ['financial accounting', 'forensic accounting', 'treasury accounting',
          'historical accounting', 'management accounting'],
    'a': 4,
    'w': 'CIMA\'s second definition frames cost accounting as that part of **management '
         'accounting** which establishes budgets, standard costs, actual costs and the analysis '
         'of variances.',
    'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'Which of the following is NOT one of the objectives of cost accounting?',
    'o': ['provision of information to aid control', 'ascertainment of cost to facilitate pricing',
          'provision of information for decision making', 'investigation of fraud',
          'provision of assistance in planning'],
    'a': 3,
    'w': 'The six stated objectives are ascertaining cost/pricing, assisting planning, '
         'facilitating decision making, aiding control, promoting cost consciousness, and '
         'providing a formal means of gathering operational information — fraud investigation is '
         'not among them.',
    'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'Material costs do NOT include the cost of',
    'o': ['fixed assets', 'raw materials', 'work in progress', 'packing materials',
          'cleaning materials'],
    'a': 0,
    'w': 'Material costs are the costs of materials or commodities **other than fixed assets** '
         'introduced into a product or consumed in operations.',
    'src': 'Chapter 1.3', 'sec': '1.3'},
   {'q': 'The sum of direct material cost, direct labour cost and direct expenses is known as',
    'o': ['overhead', 'total cost', 'prime cost', 'conversion cost', 'marginal cost'],
    'a': 2,
    'w': 'Prime cost = direct materials + direct labour + direct expenses.',
    'src': 'Chapter 1.3', 'sec': '1.3'},
   {'q': 'The wages of a factory supervisor, who does not work directly on any one product but '
         'oversees production generally, are an example of',
    'o': ['direct labour cost', 'indirect labour cost', 'direct expenses', 'prime cost',
          'a period cost only'],
    'a': 1,
    'w': 'Employees who assist the manufacturing process without working on the product itself '
         '(e.g. supervisors) generate indirect labour cost — apportioned to cost centres and '
         'absorbed by cost units, not allocated directly.',
    'src': 'Chapter 1.3', 'sec': '1.3'},
   {'q': 'Which of the following is the correct distinction between cost data and cost '
         'information?',
    'o': ['They are the same thing, just different names',
          'Cost data is analysed output; cost information is the raw input',
          'Cost data is the raw input; cost information is the analysed output',
          'Cost data relates only to labour; cost information relates only to materials',
          'Cost information is always inaccurate, unlike cost data'],
    'a': 2,
    'w': 'Cost data are the raw facts from which cost information — the detailed analysis used '
         'for decisions — is generated.',
    'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'Compared with cost accounting, financial accounting information is best described as',
    'o': ['predetermined estimates, standards and budgets', 'historical and past costs/revenue',
          'approximate and imprecise by design', 'exempt from any legal or standards compliance',
          'intended solely for internal management use'],
    'a': 1,
    'w': 'Per Fig 1.1, cost accounting deals in predetermined estimates/standards/budgets, while '
         'financial accounting deals in historical and past costs/revenue.',
    'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'A cost that cannot be identified with a specific product because it benefits all '
         'products, and so must be apportioned to cost centres before being absorbed by cost '
         'units, is an example of',
    'o': ['a direct cost', 'an indirect cost', 'a sunk cost', 'an opportunity cost',
          'a committed cost'],
    'a': 1,
    'w': 'This is the definition of an indirect cost (overhead) — apportioned, then absorbed, '
         'never allocated directly the way a direct cost is.',
    'src': 'Chapter 1.3', 'sec': '1.3'},
   {'q': 'Which of these is explicitly listed as a role of the accounting technician in '
         'collecting, analysing and presenting cost information?',
    'o': ['Setting the organisation\'s overall pricing strategy unaided',
          'Confirming the accuracy of figures supplied through reasonableness checks',
          'Conducting the external statutory audit', 'Approving all capital expenditure',
          'Negotiating collective bargaining agreements with the labour union'],
    'a': 1,
    'w': 'Confirming accuracy through reasonableness checks (or other independent sources) is '
         'one of the seven roles set out for the accounting technician.',
    'src': 'Chapter 1.3', 'sec': '1.3'},
  ],
  'theory': [
   {'q': 'Distinguish between cost data and cost information, and explain the relationship '
         'between them.',
    'marks': 6,
    'a': [
      {'p': '**Cost data** is factual information concerning the cost of materials, labour, '
            'overheads and other cost elements, expected to be incurred or already incurred in a '
            'business venture. Its sources include potential suppliers (proposals and bids), '
            'existing suppliers, and cost models.'},
      {'p': '**Cost information** is the detailed analysis of costs — the calculation of '
            'production costs, quantification of loss and estimation of work efficiency — used '
            'to make decisions, plan future operations and set performance standards.'},
      {'p': 'The relationship: cost data are the **inputs** from which cost information is '
            '**generated**. Data must be collected and analysed before it becomes usable '
            'information for management.'},
    ], 'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'A Managing Director has said: "Since the main object of our firm is to know the annual '
         'profit, there is no need retaining the cost accounting staff — let us pay them off and '
         'retain only the financial accounting staff, in order to reduce administrative costs." '
         'Write a brief report to the Managing Director explaining why the cost accounting '
         'function should be retained.',
    'marks': 10,
    'a': [
      {'p': 'Financial accounting alone cannot serve the business\'s decision-making needs, for '
            'five reasons: it gives no information about individual jobs, products or processes; '
            'it is historical, so information is not available until the accounting period ends; '
            'it does not classify costs into direct/indirect, controllable/non-controllable, '
            'normal/abnormal or variable/fixed; it keeps no detailed inventory-movement records, '
            'weakening inventory control; and it generally involves no budget plan.'},
      {'p': 'Cost accounting exists precisely to close these gaps: it ascertains the cost of '
            'individual jobs/products (supporting pricing), provides current, forward-looking '
            'information for planning and control (not just year-end historical figures), '
            'classifies costs in the ways decisions actually require, and drives budgetary '
            'control. Losing it would leave management able to see *that* a profit was made, '
            'but not *why*, *where costs could be reduced*, or *how to price competitively* — '
            'the annual profit figure financial accounting produces is the result of decisions '
            'cost accounting exists to inform in the first place.'},
      {'p': 'Recommendation: retain the cost accounting function — the administrative saving from '
            'removing it is very likely to be outweighed by worse pricing, planning and control '
            'decisions taken without it.'},
    ], 'src': 'Chapter 1.2', 'sec': '1.2'},
  ]},
}
