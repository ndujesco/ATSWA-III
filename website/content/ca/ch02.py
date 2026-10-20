CH = {
 'n': 2,
 't': 'Cost Classification, Segregation and Codification',
 'brief': 'The many ways a single cost can be classified — by element, nature, function, '
          'behaviour, relevance to decisions, and controllability — the problems with the '
          'conventional fixed/variable split and the real patterns cost behaviour takes, cost '
          'centres versus cost units versus profit centres, and how classified costs are turned '
          'into codes for a working cost-accounting system.',
 'outcomes': [
   'Define the classification of cost',
   'Know the methods of cost classification',
   'Explain the various patterns of cost behaviour',
   'Explain the meaning of cost segregation',
   'Explain the meaning of cost estimation',
   'Analyse the effect of changing activity levels on unit costs',
   'Explain cost codification',
 ],
 'secs': [
  {'n': '2.1', 't': 'Introduction', 'b': [
    {'p': 'Cost accounting is concerned with **controlling** operations, products or services. '
          'Cost control is possible only once cost classification has been introduced into '
          'business activities.'},
    {'def': {'t': 'Cost classification (CIMA Terminology)', 'd': 'the arrangement of cost into '
                  'logical groups concerning their nature (fixed, variable, value adding), '
                  'function (production, selling) or use in the business of the entity.'}},
    {'p': 'This chapter is in three parts, following the study text\'s own structure: '
          '**classification** of cost (§2.1.1), **segregation** of cost (§2.1.2 to §2.1.5), and '
          '**codification** of cost (§2.3), with cost centres and cost units (§2.2) between '
          'them.'},
    {'key': 'The point of classifying a cost is never classification for its own sake — it is '
            'that a *different* question needs a *different* grouping. "What did this product '
            'cost?" needs the element and nature split. "Which department overspent?" needs the '
            'functional split. "Should we accept this order?" needs the relevant/irrelevant '
            'split. "Whose fault is this overspend?" needs the controllable/uncontrollable '
            'split. The same naira of expenditure sits in all of these at once.'},
  ]},

  {'n': '2.1.1', 't': 'Classification of cost', 'b': [
    {'def': {'t': 'Classification', 'd': 'the practice of grouping costs according to their '
                  'common characteristics — the same cost may be classified in several different '
                  'ways, for different purposes.'}},

    {'h4': '(a) Classification according to elements of cost'},
    {'p': 'Cost can be classified according to the three basic elements of cost: **material**, '
          '**labour** and **expenses**.'},
    {'table': {'align': 'lll', 'head': ['Element', 'Definition', 'Typical examples'], 'rows': [
      ['**(i) Material costs**', 'Costs of materials and commodities **other than fixed '
       'assets**, introduced into a product or consumed in the operations of an organisation. '
       'Alternatively, the costs of material input into the production of goods and services.',
       'Raw materials; component parts; work in progress; primary packing materials; lubricating '
       'oil; consumable tools; cleaning materials; stationery.'],
      ['**(ii) Labour costs**', 'The costs of employee remuneration — payments made to and on '
       'behalf of employees for offering services in the production or service function.',
       'Wages; salaries; and employer-borne costs paid on employees\' behalf.'],
      ['**(iii) Expenses**', 'Costs other than material costs and labour costs.',
       'Cost of hiring special equipment and maintaining it; royalty payments; copyright and '
       'patent payments; cost of utilities such as electricity and water; rent.'],
    ]}},
    {'note': 'Note the exclusion built into the definition of material cost: **fixed assets are '
             'not materials.** A machine bought for the factory is capital expenditure; the '
             'lubricating oil that keeps it running is a material cost. This single word is the '
             'basis of a recurring examination multiple-choice question (see Q4 in §2.6).'},

    {'h4': '(b) Classification according to nature — direct and indirect costs'},
    {'p': 'This is an important method of cost classification. Costs can be classified as '
          '**direct** or **indirect** based on their nature, i.e. on whether they can be '
          'identified with units, jobs, processes or cost centres.'},
    {'def': {'t': 'Direct costs', 'd': 'costs that can be directly identified and charged to a '
                  'cost unit **without apportionment**. They are made up of direct material '
                  'cost, direct labour cost and direct expenses.'}},
    {'table': {'align': 'lll', 'head': ['Direct cost', 'Definition', 'Typical examples'], 'rows': [
      ['**(i) Direct material costs**', 'Costs of material that can be **physically identified** '
       'with a specific cost unit — materials entering into and becoming constituent elements of '
       'a product or saleable service. Conveniently **allocated** to cost units.',
       'Materials specifically purchased for a particular job order or process; materials '
       'requisitioned from store for a particular production order; work-in-progress and '
       'component parts; primary packing materials (cartons, wrapping materials).'],
      ['**(ii) Direct labour (wages) costs**', 'Costs of employees\' efforts and skills applied '
       '**directly** to a product or saleable service; allocated directly to cost units.',
       'Wages of production operatives transforming raw materials into finished goods; wages of '
       'waiters who serve meals at restaurants; wages of sales assistants in supermarkets.'],
      ['**(iii) Direct expenses**', 'Costs other than material and labour cost which can be '
       'identified with, and charged or allocated to, a cost unit — i.e. costs incurred for a '
       'specific product or saleable service.',
       'Cost of hiring a piece of special equipment for a particular production order; '
       'maintenance cost of that hired equipment; royalty payments; travelling expenses to '
       'contract sites.'],
    ]}},
    {'note': 'Some materials which could qualify as **direct** materials may be treated as '
             '**indirect** materials for reasons of **materiality and convenience**. The glue '
             'in a chair is physically part of the finished chair, but no one meters glue per '
             'chair; it costs more to track than the information is worth, so it is swept into '
             'production overhead instead.'},
    {'fbox': {'h': 'Prime cost', 'rows': [
      {'lb': 'Prime cost', 'tex': '\\text{Prime cost} = \\text{Direct material} + '
       '\\text{Direct labour} + \\text{Direct expenses}',
       'nt': 'The aggregate of direct materials, direct labour and direct expenses.'},
    ]}},
    {'def': {'t': 'Indirect costs (overheads)', 'd': 'all costs that **cannot** be identified '
                  'with and allocated to a cost unit, but which have to be **apportioned** to a '
                  'number of cost centres and further **absorbed** by cost units.'}},
    {'table': {'align': 'lll', 'head': ['Indirect cost', 'Definition', 'Typical examples'],
      'rows': [
      ['**(i) Indirect material costs**', 'Costs of material items that cannot be identified '
       'with any particular product, because they are used for the benefit of **all** products '
       'instead of a specific one. Apportioned and absorbed, never allocated.',
       'Materials required for operating and maintaining plant and equipment — lubricating oil, '
       'consumable tools; stationery; cleaning materials — soap and detergents, rugs and '
       'dusters, brooms and brushes.'],
      ['**(ii) Indirect labour costs**', 'Wages of employees who do not work on a specific '
       'product itself, though they assist in the manufacturing process. Apportioned to cost '
       'centres and then related to cost units through absorption.',
       'Salaries of factory supervisors; wages of store department employees; wages of '
       'cleaners.'],
      ['**(iii) Indirect expenses**', 'Expenses incurred in general and not for the production '
       'of a specific cost unit.',
       '**Selling and distribution** — advertising, sales promotion. **Administrative** — '
       'stationery, audit and consultancy fees, secretarial charges. **Production** — rent, '
       'insurance, electricity.'],
    ]}},
    {'key': 'Three verbs do all the work in this topic, and the exam tests whether you use them '
            'precisely. **Allocate** — charge a whole cost to one cost centre or cost unit, '
            'because it belongs wholly to it (direct costs, and overheads attributable to one '
            'centre). **Apportion** — split a shared cost between several cost centres on some '
            'fair basis. **Absorb** — charge the overhead accumulated in a cost centre out to '
            'the cost units that passed through it. Direct costs are allocated; indirect costs '
            'are apportioned, then absorbed. Chapter 5 is this sentence in detail.'},
    {'p': 'When classification according to **element** and **nature** is combined, a cost '
          'build-up (cost card) appears as follows:'},
    {'stmt': {'t': 'Cost card — elements combined with nature', 'rows': [
      ['Direct material cost', 'xx'],
      ['Direct labour cost', 'xx'],
      ['Direct expenses', 'xx'],
      ['**Prime cost**', 'xxx', '@t'],
      ['Indirect material cost', 'xx'],
      ['Indirect labour cost', 'xx'],
      ['Indirect expenses', 'xx'],
      ['**Overhead cost**', 'xxx', '@t'],
      ['**Total cost**', 'xxx', '@tt'],
    ]}},

    {'h4': '(c) Classification according to function'},
    {'p': 'All overhead cost can be classified by the function it serves:'},
    {'table': {'align': 'll', 'head': ['Function', 'What it covers'], 'rows': [
      ['**Production (factory/works/manufacturing) overheads**', 'The indirect costs of '
       'manufacturing a cost unit — indirect materials consumed in the factory, indirect '
       'factory wages, and other indirect expenses connected with production.'],
      ['**Selling overheads**', 'Marketing costs incurred in securing orders, e.g. sales '
       'promotion cost.'],
      ['**Marketing overheads**', 'Costs of publicising and presenting products to customers in '
       'attractive form at an acceptable price — comprising selling costs, distribution costs '
       'and other related costs (research work, securing orders and delivering goods, and after-'
       'sales service).'],
      ['**Distribution overheads**', 'Costs of making finished goods ready for dispatch and '
       'delivery to customers, e.g. carriage outwards.'],
      ['**Administrative overheads**', 'Costs of formulating policy and directing/controlling '
       'operations that are not directly related to production, selling, distribution or '
       'research and development.'],
      ['**Research and development overheads**', 'Costs of seeking new ideas, alternative '
       'materials, improved production methods, improved products, and designing innovative '
       'ideas.'],
    ]}},
    {'p': 'When classification according to elements of cost, **nature** and **function** are '
          'all combined, the revised cost build-up / cost card appears as follows:'},
    {'stmt': {'t': 'Cost card — elements, nature and function combined', 'rows': [
      ['Direct material cost', 'xxx', ''],
      ['Direct labour cost', 'xxx', ''],
      ['Direct expenses', 'xxx', ''],
      ['**Prime cost**', 'xxx', '', '@t'],
      ['Indirect production material cost', 'xxx', ''],
      ['Indirect production labour cost', 'xxx', ''],
      ['Indirect production expenses', 'xxx', ''],
      ['**Production overheads**', 'xxx', '', '@t'],
      ['**Production cost**', '', 'xxx', '@b'],
      '@gap',
      ['Selling overheads', 'xxx', ''],
      ['Distribution overheads', 'xxx', ''],
      ['Administrative overheads', 'xxx', 'xxx'],
      ['**Total cost**', '', 'xxx', '@t'],
      ['Profit margin', '', 'xxx'],
      ['**Selling price**', '', 'xxx', '@tt'],
    ]}},
    {'key': 'This single card is the skeleton of the whole subject, and it is worth being able '
            'to draw it from memory. Read it downwards and you can see exactly where every later '
            'chapter plugs in: Chapter 3 fills in direct **materials**, Chapter 4 direct '
            '**labour**, Chapter 5 the **overhead** lines (and how they get there — allocation, '
            'apportionment, absorption), Chapters 7 to 10 are four different **methods** of '
            'accumulating the top half for different kinds of business, and Chapter 11 asks what '
            'happens to the **profit margin** at the bottom when volume changes.'},
    {'note': 'Watch the two intermediate subtotals, which examiners use to catch people out. '
             '**Production cost** stops after production overheads — selling, distribution and '
             'administrative overheads come *below* it, so they are **not** in the figure used to '
             'value closing inventory. **Total cost** includes them. Mixing the two up '
             'misvalues inventory and misstates profit.'},

    {'h4': '(d) Classification according to behaviour'},
    {'p': 'Costs may or may not change in sympathy with activity. Four behaviour classes:'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning'], 'rows': [
      ['**Fixed cost**', 'Does not vary with changes in activity level — it changes instead with '
       'the passage of time (e.g. rent and rates, the managing director\'s salary). Sometimes '
       'called a **period cost**.'],
      ['**Variable cost**', 'Varies in *direct proportion* with changes in activity level (e.g. '
       'raw materials cost, direct wages, direct expenses such as royalties).'],
      ['**Semi-fixed/semi-variable (mixed) cost**', 'Contains both fixed and variable elements — '
       'over a given range of activity the cost stays constant, but beyond that range it varies '
       'in direct proportion with activity (e.g. electricity, water, telephone).'],
      ['**Stepped fixed cost**', 'Fixed over a given range of activity, but changes discretely '
       '(in a jump) for ranges of activity beyond the given range.'],
    ]}},

    {'h4': '(e) Classification as product costs or period costs'},
    {'def': {'t': 'Product costs', 'd': 'costs identified with goods produced or purchased for '
                  'resale — also called production/manufacturing costs. Used to value inventory '
                  'and work in progress. Examples: raw materials cost, production wages, '
                  'production overheads (electricity, plant depreciation, factory rent).'}},
    {'ul': [
      '**Expired product costs** — the portion of product cost relating to products that have '
      'already realised revenue, and have no future revenue-generating potential.',
      '**Unexpired product costs** — costs of resources acquired that are expected to contribute '
      'to *future* revenue (e.g. the cost of materials not yet sold). Once the inventory is sold '
      'and revenue realised, the cost is said to have "expired" and is recorded in the profit '
      'and loss account.',
    ]},
    {'def': {'t': 'Period costs', 'd': 'costs incurred and charged against profit for a period, '
                  'not included in inventory valuation — usually non-manufacturing costs, e.g. '
                  'selling/distribution overheads and administrative overheads. Charged in full '
                  'to the profit and loss account for the relevant period.'}},
    {'key': 'Product costs can themselves be analysed as expired or unexpired; period costs are '
            'never part of inventory valuation in the first place — the two classifications '
            'answer different questions (what a cost *is*, versus *when* it hits the P&L).'},

    {'h4': '(f) Classification as controllable and uncontrollable costs/revenue'},
    {'def': {'t': 'Controllable cost/revenue', 'd': 'cost/revenue reasonably amenable to '
                  'regulation by a given responsibility-centre manager — its incidence is '
                  'influenced by that manager\'s actions or inactions (e.g. raw materials '
                  'purchased in bulk; variable costs generally are prone to control).'}},
    {'def': {'t': 'Uncontrollable cost', 'd': 'cost that cannot be influenced by the actions of a '
                  'specified responsibility-centre manager (e.g. factory rent, managers\' '
                  'salaries).'}},
    {'note': 'All costs/revenues are controllable **at some level of management** — but lower '
             'down the hierarchy, some become uncontrollable at that manager\'s level. Control '
             'reports must always classify a cost as controllable or not **relative to the '
             'manager receiving the report**.'},

    {'h4': '(g) Classification as relevant/irrelevant costs'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning / examples'], 'rows': [
      ['**Relevant costs/revenue**', 'Future costs/revenues that *can* be altered by a given '
       'decision — future/predetermined costs, opportunity costs, avoidable costs, incremental '
       'costs.'],
      ['**Irrelevant costs/revenue**', 'Costs/revenues that will *not* be affected by a given '
       'decision, whatever is decided — past costs, sunk costs, unavoidable costs, fixed costs '
       '(except any incremental fixed cost element).'],
    ]}},

    {'h4': '(h) Other classifications of cost'},
    {'p': 'A large glossary of further cost terms, each defined precisely:'},
    {'table': {'align': 'll', 'head': ['Term', 'Meaning'], 'rows': [
      ['**Avoidable costs**', 'Costs that may be saved by adopting a given alternative option.'],
      ['**Non-avoidable (unavoidable) costs**', 'Costs that cannot be saved or eliminated by '
       'adopting a given alternative line of action.'],
      ['**Normal costs**', 'Costs planned for and expected at a given activity level under '
       'specified conditions, e.g. normal scrap, normal loss of materials, expected idle time.'],
      ['**Abnormal costs**', 'Costs not planned for and not expected at a given activity level '
       'under normal conditions, e.g. excessive scrap, abnormal idle-time pay.'],
      ['**Sunk costs**', 'Costs of resources already acquired — created by past decisions and '
       'unalterable by any future decision, e.g. the written-down value of a plant already '
       'bought.'],
      ['**Opportunity costs**', 'The value of the benefit forgone or sacrificed in favour of an '
       'alternative course of action.'],
      ['**Incremental (differential) costs/revenue**', 'Additional costs or revenues arising from '
       'producing or selling a *group* of additional units.'],
      ['**Marginal costs/revenues**', 'Additional cost or revenue arising from producing *one* '
       'additional unit of output or service.'],
      ['**Future costs**', 'Estimated costs reasonably expected to be incurred in the future.'],
      ['**Replacement costs**', 'The estimated cost at which an identical item can currently be '
       'acquired or produced.'],
      ['**Conversion costs**', 'The cost of transforming raw materials into finished goods, or of '
       'converting materials from one production stage to the next — total production cost less '
       'the cost of bought-in materials.'],
      ['**Attributable costs**', 'Costs that can be directly associated with a particular '
       'project, programme or cost centre.'],
      ['**Discretionary costs**', 'Non-essential costs — a business unit can survive without '
       'them.'],
      ['**Development costs**', 'Costs of research (exploration) into improving the production '
       'of goods and services.'],
      ['**Pre-production costs**', 'The part of development costs relating to a trial production '
       'run, as a preliminary step before formal production.'],
      ['**Committed costs**', 'Costs expected to be incurred, for which resources have been '
       'earmarked as a result of a contractual agreement or an earlier decision.'],
      ['**Value added**', 'The increase in a product\'s market value from changing its form, '
       'location, etc. — total market value less the cost of bought-in materials and services.'],
      ['**Pre-determined costs**', 'Costs estimated and computed *in advance* of the production '
       'process, based on the specification of every factor affecting cost.'],
      ['**Standard costs**', 'Costs estimated and expected to be incurred per unit of activity, '
       'under efficient production conditions.'],
      ['**Budgeted costs**', 'Costs estimated and planned for a given activity level, function or '
       'segment, within a specified time horizon.'],
      ['**Actual costs**', 'The costs actually incurred in production — historical, past costs, '
       'never estimates.'],
    ]}},
  ]},

  {'n': '2.1.2', 't': 'Cost segregation', 'b': [
    {'p': 'This part of the chapter covers the different **behavioural patterns of cost**. After '
          'completing it you should be able to:'},
    {'ol': [
      'explain the problems associated with the conventional methods of cost classification;',
      'explain the different cost patterns; and',
      'explain the factors that influence cost behaviour.',
    ]},
    {'def': {'t': 'Cost segregation', 'd': 'the separation of a mixed (semi-variable) cost into '
                  'its fixed component and its variable component, so that each can be treated '
                  'according to the way it actually behaves.'}},
    {'def': {'t': 'Cost estimation', 'd': 'the use of a cost function derived from past data to '
                  'predict what a cost will be at some future activity level.'}},
    {'key': 'Segregation and estimation are two halves of one exercise. You **segregate** a '
            'past mixed cost into $a$ (fixed) and $b$ (variable per unit) to obtain the cost '
            'function $y = a + bx$; you then **estimate** a future cost by substituting the '
            'planned activity level into that function. §2.1.2a below works this through '
            'numerically.'},
  ]},

  {'n': '2.1.2a', 't': 'Segregating a semi-variable cost — the high-low method', 'b': [
    {'warn': 'The study text names cost segregation in this chapter\'s own title and objectives, '
             'and sets an examination question on it (Q11 below), but never actually shows the '
             'method — it says only that "some methods could be applied to separate fixed and '
             'variable costs: statistical methods, non-statistical methods (judgement)". This '
             'section fills that gap with the **high-low method**, which is the technique the '
             'examiner\'s own question requires and which is standard, uncontroversial ATSWA '
             'material. It is also used again in Chapter 11 (cost-volume-profit analysis) and '
             'Chapter 13 (standard costing).',
     'lbl': 'Filling a gap in the study text'},
    {'p': 'A semi-variable cost has the form:'},
    {'tex': 'y = a + bx'},
    {'p': 'where $y$ is total cost, $a$ is the fixed element, $b$ is the variable cost per unit '
          'of activity and $x$ is the activity level. Two unknowns ($a$ and $b$) need two '
          'equations, so the method takes **two observations** — the highest and lowest '
          '*activity* levels — and solves them simultaneously.'},
    {'steps': [
      'Identify the period with the **highest activity** and the period with the **lowest '
      'activity**. Choose on *activity*, not on cost — they usually coincide, but where they do '
      'not, activity is what drives the cost, so activity decides.',
      'Find the **difference in cost** and the **difference in activity** between those two '
      'periods only. Every naira of that cost difference must be variable, because the fixed '
      'element is identical in both periods and cancels out.',
      'Divide: variable cost per unit $b = \\dfrac{\\text{change in cost}}'
      '{\\text{change in activity}}$.',
      'Substitute $b$ back into **either** observation to find the fixed cost: '
      '$a = y - bx$. Do it for both observations as a check — they must give the same $a$.',
      'State the cost function $y = a + bx$, then substitute the required future activity level '
      'to **estimate** the cost.',
    ]},
    {'fbox': {'h': 'High-low method', 'rows': [
      {'lb': 'Variable cost per unit',
       'tex': 'b = \\frac{\\text{Cost at highest activity} - \\text{Cost at lowest activity}}'
              '{\\text{Highest activity} - \\text{Lowest activity}}'},
      {'lb': 'Fixed cost', 'tex': 'a = \\text{Total cost at any level} - '
             '(b \\times \\text{that activity level})'},
      {'lb': 'Estimated cost at activity $x$', 'tex': 'y = a + bx'},
    ]}},
    {'note': 'The high-low method uses only **two** of the available observations and ignores '
             'the rest, so a single freak month at the top or bottom of the range distorts the '
             'whole answer. That is its one real weakness, and the reason the statistical '
             'alternative — **least-squares regression**, which uses every observation — is '
             'preferred where the data warrant it. The examiner at this level almost always '
             'wants high-low, because it can be done without a calculator.'},
  ]},

  {'n': '2.1.3', 't': 'Problems associated with the conventional classification of cost '
                      'according to behaviour', 'b': [
    {'ol': [
      'assuming **cost linearity** for variable cost per unit is not always practical — a '
      'variable cost may just as well be curvilinear (non-linear) as linear;',
      'a cost\'s behaviour should be established by **analysing that specific cost**, not by an '
      'overall simplistic assumption;',
      'fixed cost can itself change as activity levels change, and some costs (e.g. '
      'depreciation) could be classified as fixed *or* variable depending on the organisation.',
    ]},
    {'key': 'Because fixed cost is not really a single homogeneous thing, it is better to '
            'sub-divide it into four categories: **time-related** fixed cost (rent, rates — '
            'changes with the passage of time, not activity); **volume-related** fixed cost '
            '(behaves like a step cost, e.g. the cost of a plant); **policy-related (programmed)** '
            'fixed cost (advertising, R&D — set by management decision, not by volume); and '
            '**joint** fixed cost.'},
    {'p': 'Some cost items genuinely mix fixed and variable elements, and must be separated using '
          'either **statistical methods** or **non-statistical methods (judgement)**. Cost '
          'patterns are not always regular either — a variable cost might be linear only between '
          '90%–115% of normal activity, and curvilinear beyond that; different variable costs '
          'also react to *different* activity measures (direct wages may vary with the number of '
          'direct workers engaged, distribution costs with the number of deliveries made) — the '
          'simplistic assumption that every variable cost varies with the *same* activity measure '
          'is misleading. In short: the conventional fixed/variable split, defined by one factor '
          '(production volume), is at best a crude approximation of reality.'},

  ]},

  {'n': '2.1.4', 't': 'Typical cost patterns', 'b': [
    {'p': 'Six cost-behaviour shapes turn up repeatedly, each with its own graph and its own cost '
          'function:'},
    {'table': {'align': 'lll', 'head': ['Pattern', 'Cost function', 'Examples / implication'],
      'rows': [
      ['**Linear variable cost**', '$y = bx$ ($b$ = variable cost per unit, the slope)',
       'Direct materials cost; royalties per unit of production; power usage (excluding any '
       'fixed element). A perfectly linear variable cost across *every* activity level is '
       'unlikely — more realistically it is linear only over the *relevant range*.'],
      ['**Curvilinear (convex) variable cost**', '—', 'An extra unit of activity causes a '
       '*less-than-proportionate* increase in cost — economies of scale are operating.'],
      ['**Curvilinear (concave) variable cost**', '$y = bx + cx^2 + \\dots + px^n$ ($b,c,p$ '
       'constants; $x$ = activity level)', 'An extra unit of activity causes a '
       '*more-than-proportionate* increase in cost — diminishing returns are operating. This '
       'family of functions is called a "polynomial" cost function.'],
      ['**Fixed cost**', '$y = a$', 'Rates, rent, time-based depreciation, salaries — constant '
       'regardless of activity level (within the normal activity range).'],
      ['**Linear semi-variable cost**', '$y = a + bx$', 'Electricity; telephone charges; computer '
       'bureau costs; some piecework wage schemes with a guaranteed minimum payment.'],
      ['**Curvilinear semi-variable cost**', '$y = a + bx + cx^2 + \\dots + px^n$', 'Same family '
       'of costs as above, but where the variable portion itself behaves non-linearly.'],
      ['**Stepped cost**', '—', 'Supervisory salaries; bought-in materials where bulk discounts '
       'apply — constant over a range, then jumps to a new constant level.'],
    ]}},
    {'fbox': {'h': 'Cost-behaviour functions', 'rows': [
      {'lb': 'Linear variable cost', 'tex': 'y = bx'},
      {'lb': 'Polynomial (curvilinear) cost', 'tex': 'y = bx + cx^2 + \\dots + px^n'},
      {'lb': 'Fixed cost', 'tex': 'y = a'},
      {'lb': 'Linear semi-variable cost', 'tex': 'y = a + bx'},
      {'lb': 'Curvilinear semi-variable cost', 'tex': 'y = a + bx + cx^2 + \\dots + px^n'},
    ]}},

  ]},

  {'n': '2.1.4a', 't': 'Factors influencing cost behaviour', 'b': [
    {'ul': [
      '**Activity level** — sales volume, production volume, hours of work, number of invoices '
      'processed, etc.;',
      '**Time** — the passage of time itself; and',
      '**Non-volume factors** — technology, methods of production, levels of efficiency, price '
      'levels.',
    ]},

  ]},

  {'n': '2.1.5', 't': 'Analysis of the effect of changing activity levels on costs', 'b': [
    {'p': '"Level of activity" is sometimes described by alternative terms depending on the '
          'business — throughput, output, volume, capacity. Unit costs do **not** stay the same '
          'across different activity levels, since this is the very basis on which costs are '
          'classified fixed/variable in the first place — care is needed in monitoring cost '
          'behaviour at each level.'},
    {'warn': 'A fixed cost stays fixed only up to a certain level of activity, then changes — '
             'factory rent is fixed up to the factory\'s maximum capacity, but any output beyond '
             'that may need an additional factory (and hence more fixed cost). Even variable '
             'costs are not immune: unit material cost may fall at high volumes because of '
             'quantity discounts. Treat every "fixed" or "variable" label as valid only within a '
             'relevant range, not universally.'},
  ]},

  {'n': '2.2', 't': 'Cost centre and cost unit', 'b': [
    {'def': {'t': 'Cost centre (CIMA)', 'd': 'a production or service location, function, '
                  'activity or item of equipment for which costs are accumulated.'}},
    {'p': 'More broadly: a location, a person, an item of equipment, or a group of these, to '
          'which costs are incurred and then related to cost units — e.g. the factory, the '
          'canteen, the maintenance section, the foreman, the managing director, the plant, the '
          'pool of computers. Cost centres are broadly:'},
    {'ul': ['**Production cost centres**', '**Service cost centres**']},
    {'key': 'The manager of any cost centre is accountable for the outcome achieved within it — '
            'each centre is evaluated on the performance it achieves.'},
    {'def': {'t': 'Cost unit (CIMA)', 'd': 'a unit of product or service in relation to which '
                  'costs are ascertained.'}},
    {'p': 'A cost unit is a *quantitative* unit of product or service to which costs are '
          'ascertained — a selection of common cost units by industry:'},
    {'table': {'align': 'll', 'head': ['Industry', 'Cost unit'], 'rows': [
      ['Brewing', 'Barrel'], ['Coal mining', 'Tunnel/ton'],
      ['Electricity', 'Kilowatt hour (kW/hr)'], ['Oil', 'Barrel/tonne, litre'],
      ['Education', 'Course, enrolled student'], ['Paper', 'Ream'],
      ['Hospitals', 'Bed-day'], ['Telephone', 'Calls made, number of extensions'],
    ]}},
    {'def': {'t': 'Profit centre', 'd': 'a centre which not only incurs cost, but also generates '
                  'income — unlike a plain cost centre, which only incurs cost.'}},
  ]},

  {'n': '2.3', 't': 'Codification', 'b': [
    {'p': 'Classifying and controlling cost is not complete until codes are applied to classified '
          'cost items, for simplicity.'},
    {'def': {'t': 'Code', 'd': 'a brief, accurate reference designed to assist the classification '
                  'of items, by facilitating entry, collation and analysis.'}},
    {'h4': 'Characteristics of a well-designed coding system'},
    {'ul': [
      'simple for the organisation to operate;',
      'flexible in nature;',
      'easy to remember;',
      'a **fixed coding length** for every item, e.g. a 6-digit code such as 000000;',
      'concise in nature.',
    ]},
    {'h4': 'Methods of codification'},
    {'table': {'align': 'll', 'head': ['Method', 'How it works'], 'rows': [
      ['**Mnemonic method**', 'Applies memorable symbols to classified items, e.g. `FAU` for '
       'Factory Unit, `ADM` for Administration, `DMA` for Direct Material, `DLA` for Direct '
       'Labour.'],
      ['**Decimal method**', 'A whole number identifies a master group, and a decimal identifies '
       'the primary/secondary groups within it — e.g. 1 Direct Materials, 2 Direct Labour, '
       '3 Direct Expenses, 4 Factory Overheads (4.1 Indirect material in the factory, 4.2 '
       'Consumable stores), 5 Indirect Labour (5.1 Factory labour, 5.2 Factory cleaners).'],
      ['**Numerical method**', 'Applies fixed-length digit strings to classified items, each '
       'digit position (or block of digits) standing for one dimension of the item.'],
    ]}},
    {'p': 'Worked example of the numerical method: suppose an 8-digit code is designed for types '
          'of wood, laid out as `T LLL WW TT` (1 digit for wood type, 3 for length, 2 for width, '
          '2 for thickness):'},
    {'table': {'align': 'llll', 'head': ['Type of wood', 'Length', 'Width', 'Thickness'],
      'rows': [['0', '000', '00', '00']]}},
    {'eg': {'tag': 'Study text', 't': 'Coding Iroko and Mahogany wood', 'open': True, 'q': [
      {'p': 'Iroko wood measuring 12 feet in length, 2 inches in width and 1 inch in thickness is '
            'to be coded, followed by Mahogany wood of the identical dimensions.'},
    ], 'a': [
      {'p': 'Iroko wood, 12 feet by 2 inches by 1 inch → **Code 1 1 4 4 0 4 0 4** (wood type digit '
            '"1" for Iroko, followed by the length/width/thickness digits).'},
      {'p': 'Mahogany wood, the same dimensions (12 feet by 2 inches by 1 inch) → **Code 2 1 4 4 '
            '0 4 0 4** (only the leading wood-type digit changes, to "2" for Mahogany).'},
      {'p': 'Only the code itself needs to be disclosed to staff handling the materials — the '
            'underlying names and actual dimensions of the wood can be kept confidential.'},
    ]}},
    {'note': 'Coding is not limited to material *types* — it can equally be designed for '
             'material cost, labour cost and overhead, using the same three methods.'},
  ]},

  {'n': '2.4', 't': 'Chapter summary', 'b': [
    {'p': 'Chapter 2 has been discussed in three parts. Part 1 focused on the **classification '
          'of cost**; part 2 explained **cost segregation**; and part 3 dealt with **cost '
          'codification**.'},
    {'p': 'In conclusion, this chapter has given a firm foundation of the various concepts and '
          'principles in cost accounting, to aid the comprehension of the chapters ahead.'},
    {'key': 'If you remember only three things from this chapter: (1) the **same naira** of '
            'expenditure is classified several different ways at once, and which classification '
            'matters depends on the question being asked; (2) **fixed and variable are only true '
            'within a relevant range** — the conventional split is a crude approximation; and '
            '(3) a mixed cost can be **segregated** into $a + bx$ by the high-low method, and '
            'the resulting function then **estimates** future cost.'},
  ]},

  {'n': '2.5', 't': 'Worksheet summary — definitions and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§2.1 Classification** — 8 ways to classify the same cost: by element (materials/'
      'labour/expenses), by nature (direct/indirect → prime cost/overhead), by function '
      '(production/selling/marketing/distribution/administrative/R&D overheads), by behaviour '
      '(fixed/variable/semi-variable/stepped), as product vs period cost (+ expired/unexpired), '
      'as controllable/uncontrollable (relative to a management level), as relevant/irrelevant '
      'to a decision, plus a long glossary of named cost types (avoidable, sunk, opportunity, '
      'incremental, marginal, conversion, standard, budgeted, actual, etc.).',
      '**§2.2 Segregation and behaviour** — the conventional fixed/variable split is a crude '
      'approximation (3 named problems); fixed cost itself splits 4 ways (time-related, '
      'volume-related, policy-related/programmed, joint); 7 named cost-behaviour patterns with '
      'their functions ($y=bx$, $y=a$, $y=a+bx$, stepped, and their curvilinear/polynomial '
      'forms); 3 factors driving behaviour (activity level, time, non-volume factors); a fixed '
      'cost is only fixed within a relevant range.',
      '**§2.3 Cost centre/unit/profit centre** — a cost centre accumulates cost (production or '
      'service); a cost unit is the quantitative unit costs attach to (with named cost units by '
      'industry); a profit centre both incurs cost **and** generates income.',
      '**§2.4 Codification** — codes make classified cost simple to enter/collate/analyse; 5 '
      'characteristics of a good code; 3 codification methods (mnemonic, decimal, numerical).',
    ]},
    {'h3': 'B. Cost-behaviour formula box'},
    {'fbox': {'h': 'Cost-behaviour functions (recap)', 'rows': [
      {'lb': 'Linear variable cost', 'tex': 'y = bx'},
      {'lb': 'Fixed cost', 'tex': 'y = a'},
      {'lb': 'Linear semi-variable cost', 'tex': 'y = a + bx'},
      {'lb': 'Polynomial (curvilinear) cost', 'tex': 'y = bx + cx^2 + \\dots + px^n'},
    ]}},
  ]},

  {'n': '2.6', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Cost accounting involves (A) Drawing up the balance sheet  (B) Writing off costs  '
        '(C) Ascertaining of cost  (D) Preparation of statement of value added  (E) Annual audit '
        'of financial statements',
        'Cost accounting is an integral part of (A) Financial accounting  (B) Forensic '
        'accounting  (C) Treasury accounting  (D) Historical accounting  (E) Management '
        'accounting',
        'Which of the following is NOT an objective of cost accounting? (A) Provision of '
        'information to aid control  (B) Ascertainment of cost in order to facilitate pricing  '
        '(C) Provision of information for decision making  (D) Investigation of fraud  '
        '(E) Provision of assistance in planning',
        'Material costs do NOT include the cost of (A) Fixed assets  (B) Raw materials  '
        '(C) Work in progress  (D) Packing materials  (E) Cleaning materials',
        'Which one of the following is a direct expense? (A) Cost of hiring a special equipment '
        'for a particular production order  (B) Advertising expenses  (C) Electricity expenses  '
        '(D) Insurance premiums  ~(printed in the study text as option E — see the note with the '
        'answers)~',
        'Classifying costs by elements includes materials, labour and …………………..',
        'The addition of all direct costs is known as ………………………………..',
        'Costs which are fixed for a given range of activity level but which change discretely '
        'for ranges of activity levels beyond the given ranges are called ………….',
        'Costs which may be saved by the adoption of a given alternative option are known as '
        '……………………',
        'Costs which vary in direct proportion with changes in activity levels are called '
        '……………………',
      ]}],
      'a': [
      {'ol': [
        '**C — ascertaining of cost.** *(The study text\'s own answer key says "A — drawing up '
        'the balance sheet", which is plainly wrong: drawing up the balance sheet is financial '
        'accounting. See the note below.)*',
        '**E — management accounting.**',
        '**D — investigation of fraud** is not one of the six objectives listed in §1.2.3.',
        '**A — fixed assets.** Material costs are, by definition, the costs of materials and '
        'commodities **other than fixed assets** (§2.1.1a).',
        '**A — the cost of hiring special equipment for a particular production order.** It is '
        'incurred for one specific production order, so it can be identified with and charged '
        'directly to that cost unit. Advertising, electricity and insurance are all general '
        'indirect expenses. *(The study text\'s answer key says "B — advertising expenses", '
        'which is wrong — advertising is a selling overhead, the textbook example of an '
        '**indirect** expense.)*',
        '**Expenses.** The three elements are material, labour and expenses.',
        '**Prime cost.**',
        '**Stepped fixed costs.**',
        '**Avoidable costs.**',
        '**Variable costs.**',
      ]},
      {'warn': 'Two of the study text\'s own printed answers to this question set are wrong. '
               'Its key gives **1 = A** and **5 = B**; the correct answers are **1 = C** and '
               '**5 = A**, for the reasons given above. Question 5 is also printed with only '
               'four options lettered **A, B, C and E** — option D is missing from the book '
               'altogether; the fourth option has been relettered D above so the question can be '
               'attempted normally.',
       'lbl': 'Errors in the study text\'s answer key'},
      ]}},
  ]},

  {'n': '2.7', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with eleven examination-type questions. All are '
          'reproduced below with full answers. Note that **questions 6 and 7 are identical** in '
          'the book — the same question is printed twice, once unattributed and once credited to '
          'CACA Level I Costing, June 1989 — so they are answered once here.'},

    {'eg': {'tag': 'Exam type — Q1 (16 marks)',
      't': 'Six principal items of information obtainable from a costing system',
      'q': [{'p': 'You have been appointed to the newly created position of Cost Accountant in a '
                  'small manufacturing company. Having installed a costing system successfully, '
                  'the Managing Director would like a detailed explanation of the kind of '
                  'information the newly installed system would provide. Write a report to the '
                  'Managing Director setting out **six** principal items of information '
                  'obtainable from a costing system.'}],
      'a': [
      {'p': '**REPORT**  —  To: The Managing Director.  From: The Cost Accountant.  '
            'Subject: Information obtainable from the newly installed costing system.'},
      {'p': 'The following six classes of information are produced by the system and are '
            'available to management on a routine basis.'},
      {'ol': [
        '**Statements of material, direct labour and machine utilisation**, showing both trends '
        'and values — so that the use of each major resource can be monitored period by period.',
        '**The cost of products and services**, broken down into material cost, labour cost and '
        'other expenses, and shown in comparison with estimates — the basis for pricing and for '
        'checking whether estimates are reliable.',
        '**Cost control statements for each section and department**, showing actual results '
        'compared with budget, so that responsibility for any overspend can be located.',
        '**Periodic inventory valuation reports** — the value of raw materials, work-in-progress '
        'and finished goods held, needed both for control and for the financial accounts.',
        '**Scrap and rectification cost reports**, quantifying what defective work is costing '
        'the company and where it arises.',
        '**Budgets for planning and control purposes**, including cash budgets for monitoring '
        'liquidity.',
      ]},
      {'note': 'This is Chapter 1 §1.3.4 reproduced as a report. In the exam, the marks for a '
               '"write a report" question are split between **content** (the six items) and '
               '**form** — use a proper report heading (to, from, subject, date), number the '
               'points, and close with a short recommendation or offer to discuss.'}]}},

    {'eg': {'tag': 'Exam type — Q2 (8 marks)',
      't': 'Problems inherent in installing a costing system',
      'q': [{'p': '"Installation of a costing system is a major move in a business." Discuss the '
                  'inherent problems associated with installing a costing system.'}],
      'a': [
      {'p': 'Installing a costing system is a substantial undertaking requiring detailed '
            'discussion with management and staff and careful analysis of procedures and '
            'records. The problems that arise are of two kinds.'},
      {'h4': 'General factors that shape the problem'},
      {'ol': [
        '**Size of the organisation** — a system adequate for a small workshop collapses under '
        'the transaction volume of a large factory, and one designed for a large factory is '
        'uneconomic for a small one.',
        '**Type of product or service** — a jobbing manufacturer, a continuous-process plant and '
        'a service provider each need a fundamentally different costing method.',
        '**The production process** and **the methods of manufacture** — these determine whether '
        'costs can be collected by job, by batch, by process or by operation.',
        '**Availability of staff** — a system no one is competent to operate will not work, '
        'however well designed.',
      ]},
      {'h4': 'Specific problems met in practice'},
      {'ol': [
        '**Definition of responsibility** — deciding who is accountable for which costs, which '
        'often exposes gaps and overlaps in the existing management structure.',
        '**Definition or designation of cost centres** — drawing the boundaries so that costs '
        'can be meaningfully accumulated and controlled.',
        '**Compilation of a comprehensive cost system** covering every element without leaving '
        'costs uncollected.',
        '**Labour hours worked** — obtaining accurate, timely time records from the shop floor.',
        '**Machine utilisation time** — measuring running and idle time reliably.',
        '**Scrap treatment** and **rectification cost** — deciding how defective output and the '
        'cost of putting it right are to be recorded and charged.',
        '**The difficulty of accurate classification of cost** — in particular the direct/'
        'indirect and fixed/variable boundaries, which are rarely as clean in practice as in a '
        'textbook.',
      ]},
      {'key': 'Underlying all of these is a **human** problem the examiner rewards you for '
              'naming: a costing system makes performance visible, so staff may resist it, '
              'suspect it, or supply poor data to it. That is why §1.2.9 puts "co-operation and '
              'co-ordination among all staff members" first among the conditions for success, '
              'and why §1.2.10 ends with training and "implement the system with full '
              'publicity".'}]}},

    {'eg': {'tag': 'Exam type — Q3 (10 marks)',
      't': 'Problems from introducing a system of cost control',
      'q': [{'p': 'Outline the possible problems which may be encountered as a result of the '
                  'introduction of a system of cost control into an organisation.'}],
      'a': [
      {'ol': [
        '**Staff resistance and low morale** — cost control makes individual and departmental '
        'performance visible, and employees may perceive it as surveillance or as a prelude to '
        'redundancies.',
        '**Poor-quality source data** — the system depends on shop-floor returns (time sheets, '
        'material requisitions, scrap notes). Where staff complete these carelessly or '
        'defensively, every subsequent analysis is unreliable.',
        '**Cost of the system itself** — additional staff, forms, software and management time. '
        'If the information generated does not outweigh the cost of generating it, the system '
        'fails its own cost-benefit test (§1.2.12).',
        '**Complexity** — a system too complex for the managers who must operate it will not be '
        'used, or will be used wrongly.',
        '**Dysfunctional behaviour** — managers judged on a single cost measure may cut costs in '
        'ways that damage the business (deferring maintenance, buying cheaper and worse '
        'material, suppressing scrap reports).',
        '**Disputes over controllability** — managers held responsible for costs they cannot '
        'influence (apportioned head-office overhead, for instance) will reject the reports '
        'altogether; see §2.1.1f.',
        '**Delay** — reports produced too late to act on lose their relevance entirely '
        '(§1.2.12).',
        '**Difficulty in setting realistic standards and budgets** against which actual '
        'performance is compared — standards that are too tight demotivate, and standards that '
        'are too loose conceal inefficiency.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q4 (8 marks)',
      't': 'Differences between financial and cost accounting',
      'q': [{'p': 'Enumerate the differences, if any, between financial and cost accounting.'}],
      'a': [
      {'table': {'align': 'lll',
        'head': ['Factor', 'Cost accounting', 'Financial accounting'], 'rows': [
        ['**Nature of costs / revenue**', 'Predetermined estimates, standards and budgets',
         'Historical and past costs / revenue'],
        ['**Users of information**', 'Management of the business enterprise',
         'Management as well as external stakeholders — shareholders, creditors, debtors, tax '
         'authorities, investors'],
        ['**Objectives**', 'Provide information to aid planning, decision making and control',
         'Satisfy the stewardship function of management, i.e. account for the use of resources '
         'entrusted to management'],
        ['**Conformity to concepts and standards**', 'No need to comply with standards and '
         'concepts', 'Absolute need to comply meticulously with accounting concepts and '
         'standards'],
        ['**Scope and form of presentation**', 'Determined by management on the basis of '
         'relevance and cost-benefit considerations',
         'Determined by concepts, standards and legal provisions'],
        ['**Precision of information**', 'Approximations are permitted, due to uncertainties in '
         'making estimates, but must be sufficiently precise and accurate',
         'Information must be more precise; there is usually an audit by independent external '
         'auditors to confirm its reliability'],
      ]}},
      {'p': 'Two further differences worth adding for the extra marks:'},
      {'ul': [
        '**Frequency** — cost accounting reports as often as management needs them (daily, '
        'weekly, monthly); financial accounting reports at fixed statutory intervals, normally '
        'annually.',
        '**Level of detail** — cost accounting reports by job, product, process and cost centre; '
        'financial accounting reports on the entity as a whole.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q5 (10 marks)',
      't': 'Report: why the cost accounting staff should be retained',
      'q': [{'p': 'The Managing Director of a manufacturing concern once said: "Since the main '
                  'object of our firm is to know the annual profit, there is no need retaining '
                  'the cost accounting staff; let us pay them off and retain only the financial '
                  'accounting staff in order to reduce the administrative costs." **Required:** '
                  'Write a report to the Managing Director to convince him of the need to retain '
                  'the cost accounting staff.'}],
      'a': [
      {'p': '**REPORT**  —  To: The Managing Director.  From: The Cost Accountant.  '
            'Subject: The case for retaining the cost accounting function.'},
      {'h4': '1.  The premise of the proposal is too narrow'},
      {'p': 'Knowing the annual profit tells us *that* we made money; it does not tell us *how*, '
            '*where*, or *whether we could have made more*. The annual profit figure is the '
            '**result** of decisions that cost accounting exists to inform in the first place.'},
      {'h4': '2.  Financial accounting alone cannot fill the gap'},
      {'p': 'Financial accounting suffers five well-recognised weaknesses:'},
      {'ol': [
        'it gives **no information about individual jobs, products or processes**, so we could '
        'not tell a profitable product line from a loss-making one;',
        'it is **historical** — information is not available until the accounting period ends, '
        'by which time any damage is months old;',
        'it does **not classify costs** into direct and indirect, controllable and '
        'non-controllable, normal and abnormal, or variable and fixed — the very classifications '
        'every operating decision needs;',
        'it keeps **no detailed records of inventory movement**, which inhibits efficient '
        'inventory control; and',
        'it generally involves **no budget plan**, so there is nothing to compare actual '
        'performance against.',
      ]},
      {'h4': '3.  What we would lose'},
      {'ol': [
        '**Pricing** would become guesswork, since we would not know the cost of a unit.',
        '**Planning** would lose its basis — no budgets, no capital-expenditure evaluation, no '
        'cash-flow projection.',
        '**Control** would disappear — no variance reports, so overspends would surface only in '
        'next year\'s accounts.',
        '**Decision making** — make-or-buy, accept-or-reject a special order, continue or '
        'discontinue a product line — would have no cost basis.',
        '**Inventory control and scrap control** would weaken, with direct cash consequences.',
      ]},
      {'h4': '4.  The saving is illusory'},
      {'p': 'The administrative saving from paying off the cost accounting staff is a known, '
            'one-off, modest figure. The cost of mispricing a single major contract, of carrying '
            'excessive inventory for a year, or of continuing a loss-making product line '
            'unnoticed, is unknown and open-ended — and we would, by construction, have no means '
            'of detecting any of them.'},
      {'h4': '5.  Recommendation'},
      {'p': 'Retain the cost accounting function. If the objective is to reduce administrative '
            'cost, I would instead recommend reviewing the costing system for simplification, '
            'and considering an **integrated** accounting system (Chapter 6), which keeps one '
            'set of records instead of two and so removes duplicated effort without losing any '
            'management information.'}]}},

    {'eg': {'tag': 'Exam type — Q6 and Q7 (11 marks) — CACA Level I Costing, June 1989',
      't': 'Three methods of cost classification and the usefulness of each',
      'q': [{'p': 'Describe **three** different methods of cost classification and explain the '
                  'usefulness of each method.'},
            {'note': 'The study text prints this question twice, as Q6 and Q7 — identical '
                     'wording, with only Q7 carrying the CACA attribution. It is answered once '
                     'here.'}],
      'a': [
      {'h4': 'Method 1 — classification by **element** (material, labour, expenses)'},
      {'p': '**What it is:** every cost is assigned to one of the three basic inputs — material, '
            'labour, or expenses (everything else).'},
      {'p': '**Usefulness:** it is the basis of the cost card and therefore of all product '
            'costing; it allows each input to be controlled by the manager responsible for it '
            '(the storekeeper for materials, the personnel function for labour); and it makes '
            'inter-period and inter-firm comparison possible, since the same three headings '
            'apply to any manufacturer.'},
      {'h4': 'Method 2 — classification by **nature** (direct and indirect)'},
      {'p': '**What it is:** costs that can be identified with and charged to a cost unit '
            'without apportionment are **direct**; those that must be apportioned to cost '
            'centres and absorbed into cost units are **indirect** (overhead).'},
      {'p': '**Usefulness:** it determines how each cost reaches the product — allocation versus '
            'apportionment and absorption; it gives the two key subtotals, **prime cost** and '
            '**overhead**; and it is the foundation of absorption costing and of the whole of '
            'Chapter 5.'},
      {'h4': 'Method 3 — classification by **behaviour** (fixed, variable, semi-variable, '
             'stepped)'},
      {'p': '**What it is:** costs are grouped by how they respond to a change in the level of '
            'activity.'},
      {'p': '**Usefulness:** it is indispensable for **planning and decision making** — '
            'budgeting at different activity levels (flexible budgets), cost-volume-profit and '
            'break-even analysis (Chapter 11), marginal costing, and any short-run decision such '
            'as accepting a special order, because only the variable element changes.'},
      {'note': 'Three other classifications would earn equal credit if described as fully: by '
               '**function** (production / selling / distribution / administration / R&D — '
               'useful for departmental responsibility and for separating product cost from '
               'period cost); as **product or period** cost (useful for inventory valuation and '
               'profit measurement); and as **relevant or irrelevant** (useful for decision '
               'making, since only future costs that change with the decision matter).'}]}},

    {'eg': {'tag': 'Exam type — Q8 (17 marks) — CACA Level I Costing, June 1987',
      't': 'Period, product, variable and opportunity costs, with two examples of each',
      'q': [{'p': 'The following are some of the cost classifications used in any costing '
                  'system: (i) Period costs; (ii) Product costs; (iii) Variable costs; '
                  '(iv) Opportunity costs. **Required:** Citing two examples in each case, '
                  'explain each of these classified costs.'}],
      'a': [
      {'table': {'align': 'lll', 'head': ['Classification', 'Explanation', 'Two examples'],
        'rows': [
        ['**(i) Period costs**', 'Costs incurred and charged against the profit of a period, '
         'and **not** included in the cost used for inventory valuation. They are usually '
         'non-manufacturing costs, and are charged in full to the profit and loss account of the '
         'period in which they are incurred, whether or not any output was sold.',
         '1. Selling and distribution overheads (e.g. advertising).  2. Administrative overheads '
         '(e.g. the managing director\'s salary).'],
        ['**(ii) Product costs**', 'Costs identified with goods produced or purchased for '
         'resale — also called production or manufacturing costs. They are the costs used for '
         'the valuation of inventory and work-in-progress, and are charged against profit only '
         'when the goods are sold.',
         '1. The cost of raw materials.  2. Production wages. *(Production overheads such as '
         'factory rent and plant depreciation are also product costs.)*'],
        ['**(iii) Variable costs**', 'Costs which vary in direct proportion with changes in the '
         'level of activity — if activity doubles, total variable cost doubles, while variable '
         'cost **per unit** stays constant.',
         '1. Direct material cost.  2. Royalties payable per unit produced. *(Direct wages paid '
         'on a piecework basis are a third.)*'],
        ['**(iv) Opportunity costs**', 'The value of the benefit forgone or sacrificed in '
         'favour of an alternative course of action. It is not an outlay recorded in the books — '
         'it is a benefit given up — but it is a **relevant** cost for decision making.',
         '1. The rent forgone by using an owned building for production rather than letting it. '
         '2. The contribution lost on normal production displaced in order to fulfil a special '
         'order.'],
      ]}},
      {'key': 'Note the trap built into (i) and (ii): period and product costs are **not** the '
              'same split as fixed and variable. Factory rent is a *fixed* cost but a *product* '
              'cost (it is absorbed into inventory under absorption costing); a sales commission '
              'is a *variable* cost but a *period* cost. The product/period split asks "does '
              'this cost attach to the goods?"; the fixed/variable split asks "does this cost '
              'change with volume?" They are independent questions.'}]}},

    {'eg': {'tag': 'Exam type — Q9 (22 marks) — ICSA Management Accounting, December 1984',
      't': 'Cost may be classified in a variety of ways according to their nature and the '
           'information needs of management',
      'q': [{'p': '"Cost may be classified in a variety of ways according to their nature and '
                  'the information needs of management." With relevant illustrative examples, '
                  'provide a detailed explanation of the above statement.'}],
      'a': [
      {'p': 'The statement makes two linked points: that a single cost can be classified in '
            'several different ways at the same time, and that **which classification is used '
            'depends on what management needs to know.** Each classification below is matched '
            'with the management question it answers.'},
      {'table': {'align': 'lll',
        'head': ['Classification', 'The management question it answers', 'Illustration'],
        'rows': [
        ['**By element** — material, labour, expenses', 'What kind of resource is being '
         'consumed, and who should control it?',
         'A furniture maker separates timber (material) from carpenters\' wages (labour) from '
         'the rent of the workshop (expense).'],
        ['**By nature** — direct and indirect', 'How does this cost reach the product — directly, '
         'or through apportionment and absorption?',
         'The timber in a chair is a direct material; the glue and the supervisor\'s salary are '
         'indirect, and must be absorbed into the chair through an overhead rate.'],
        ['**By function** — production, selling, distribution, administration, R&D',
         'Which department incurred it, and is it a product cost or a period cost?',
         'Factory power is a production overhead and goes into inventory value; the sales '
         'director\'s car is a selling overhead and does not.'],
        ['**By behaviour** — fixed, variable, semi-variable, stepped',
         'What will happen to this cost if volume changes?',
         'If output rises 20%, timber cost rises 20% but factory rent does not move at all — '
         'until a second workshop is needed, when it steps up.'],
        ['**As product or period cost**', 'Does this cost sit in closing inventory, or is it '
         'written off this period?',
         'Unsold chairs carry their material, labour and production overhead into next year; the '
         'advertising that failed to sell them does not.'],
        ['**As controllable or uncontrollable**', 'Whom can I hold responsible for this '
         'overspend?', 'The foreman controls material usage and overtime; he does not control '
         'the factory rent apportioned to his department, so his report should separate the '
         'two.'],
        ['**As relevant or irrelevant**', 'Does this cost matter to the decision I am about to '
         'take?', 'In deciding whether to replace a machine, its written-down value is a **sunk** '
         'cost and irrelevant; the disposal proceeds and the running costs of the new machine '
         'are relevant.'],
        ['**As normal or abnormal**', 'Is this loss an expected part of the process, or a '
         'failure to be investigated?', 'A 2% evaporation loss in a chemical process is normal '
         'and absorbed into the cost of good output; a spillage of a whole batch is abnormal and '
         'written off separately.'],
      ]}},
      {'p': 'In conclusion, no one classification is "correct". Classification is a tool: the '
            'cost accountant selects the grouping that answers the question in front of '
            'management, and the same expenditure will appear in several groupings at once.'}]}},

    {'eg': {'tag': 'Exam type — Q10',
      't': 'Making good the deficiencies of a cost system that lacks cost control',
      'q': [{'p': 'An existing cost system lacks the essential aspects of cost control. List the '
                  'main matters to be introduced to make good the system\'s deficiencies.'}],
      'a': [
      {'ol': [
        '**A budgetary control system** — budgets prepared for each responsibility centre, '
        'against which actual results are compared period by period.',
        '**Standard costs** for material, labour and overhead per unit, with **variance '
        'analysis** to isolate the cause of each difference between standard and actual '
        '(Chapter 13).',
        '**Clearly designated cost centres**, each with a named manager accountable for its '
        'results.',
        '**Separation of controllable from uncontrollable costs** in every report, so that a '
        'manager is measured only on what they can influence.',
        '**A proper system of stores and inventory control** — bin cards, stores ledger, '
        'reorder levels, and periodic or continuous stocktaking (Chapter 3).',
        '**Adequate payroll and time-recording procedures** — clock cards, job cards, idle-time '
        'analysis (Chapter 4).',
        '**A sound basis for collecting and absorbing overhead**, with under/over absorption '
        'identified and reported (Chapter 5).',
        '**Scrap, waste and rectification reporting**, so defective work is quantified rather '
        'than buried in the material cost.',
        '**Standardised pre-printed forms** for material receipts and issues, labour attendance '
        'and hours worked, and wage calculations, to improve the quality of source data.',
        '**Prompt, regular reporting** to the right person — a report that is late, or addressed '
        'to someone who cannot act on it, provides no control at all.',
        '**A feedback mechanism** built into the system, so that variances lead to investigation '
        'and corrective action rather than merely being recorded.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q11', 't': 'HIMCO — segregating and estimating a semi-variable '
                                           'power cost',
      'q': [
      {'p': 'Company HIMCO produces different products through automation. The company incurs a '
            'large amount of overheads in the factory on power alone, which is **semi-variable** '
            'in nature. The details of power costs for the six months ending September 2024 are '
            'as provided below.'},
      {'stmt': {'t': 'HIMCO — power costs, April to September 2024', 'rows': [
        ['Month (2024)', 'Machine hours', 'Power cost (N)', '@hd'],
        ['April', 50000, 400000],
        ['May', 60000, 460000],
        ['June', 40000, 340000],
        ['July', 45000, 370000],
        ['August', 70000, 520000],
        ['September', 75000, 550000],
      ]}},
      {'p': '**Required:**'},
      {'ol': [
        '**(a)(i)** Differentiate between fixed cost and variable cost. '
        '**(ii)** Summarise the meaning of semi-variable cost.',
        '**(b)** Segregate the semi-variable costs into total fixed costs and unit variable '
        'costs.',
        '**(c)** Estimate the power cost for October if the firm plans to use 88 machine hours.',
      ]},
      {'warn': 'The six-month table is printed in the study text as a **scanned image**, not as '
               'text, so it is missing from any text-based copy of the book — it is reproduced '
               'above exactly as it appears on the page. Note also that part (c) asks for '
               '"88 machine hours" while every figure in the table is in tens of thousands of '
               'hours; the intended figure is almost certainly **88,000 machine hours**. Both '
               'readings are answered below.',
       'lbl': 'Source note'}],
      'a': [
      {'h4': '(a)(i)  Fixed cost versus variable cost'},
      {'table': {'align': 'lll', 'head': ['', 'Fixed cost', 'Variable cost'], 'rows': [
        ['**Definition**', 'A cost that does **not** vary with changes in the level of activity',
         'A cost that varies in **direct proportion** with changes in the level of activity'],
        ['**In total**', 'Constant as activity changes', 'Rises and falls with activity'],
        ['**Per unit**', 'Falls as activity rises (the same amount spread over more units)',
         'Constant per unit at every activity level'],
        ['**What it changes with**', 'The passage of **time** — hence "period cost"',
         'The level of **activity** or output'],
        ['**Examples**', 'Rent and rates; the managing director\'s salary; time-based '
         'depreciation', 'Raw materials; direct wages on piecework; royalties per unit'],
        ['**Cost function**', '$y = a$', '$y = bx$'],
      ]}},
      {'note': 'The sentence that earns the mark is the **per-unit reversal**: a fixed cost is '
               'fixed in total but variable per unit, and a variable cost is variable in total '
               'but fixed per unit. Candidates who state only the "in total" half rarely get '
               'full credit. And remember both statements hold only within the **relevant '
               'range** (§2.1.5).'},
      {'h4': '(a)(ii)  Semi-variable cost'},
      {'p': 'A **semi-variable** (semi-fixed, or mixed) cost is one that contains **both a fixed '
            'element and a variable element**. Part of the cost is incurred regardless of '
            'activity, and the rest varies with activity. Its cost function is:'},
      {'tex': 'y = a + bx'},
      {'p': 'where $a$ is the fixed element, $b$ the variable cost per unit of activity and $x$ '
            'the activity level. Power is the classic example: there is a standing charge and a '
            'minimum load whether or not the machines run, plus a usage charge that rises with '
            'machine hours. Electricity, telephone charges, computer bureau costs and piecework '
            'wage schemes with a guaranteed minimum payment all behave this way.'},
      {'h4': '(b)  Segregating the cost — the high-low method'},
      {'p': '**Step 1 — identify the highest and lowest activity levels.** Choose on machine '
            'hours, not on cost:'},
      {'stmt': {'t': 'Step 1 — the two observations', 'rows': [
        ['', 'Machine hours', 'Power cost (N)', '@hd'],
        ['Highest activity — September', 75000, 550000],
        ['Lowest activity — June', 40000, 340000],
        ['**Difference**', 35000, 210000, '@tt'],
      ]}},
      {'p': '**Step 2 — the whole of the cost difference must be variable**, because the fixed '
            'element is the same N$a$ in both months and therefore cancels out in the '
            'subtraction. So:'},
      {'tex': 'b = \\frac{550{,}000 - 340{,}000}{75{,}000 - 40{,}000} '
              '= \\frac{210{,}000}{35{,}000} = N6 \\text{ per machine hour}'},
      {'p': '**Step 3 — substitute $b$ back to find the fixed element.** Using the high point:'},
      {'tex': 'a = 550{,}000 - (6 \\times 75{,}000) = 550{,}000 - 450{,}000 = N100{,}000'},
      {'p': 'Checking with the low point, which must give the same answer:'},
      {'tex': 'a = 340{,}000 - (6 \\times 40{,}000) = 340{,}000 - 240{,}000 = N100{,}000 '
              '\\;\\checkmark'},
      {'stmt': {'t': 'Answer to (b)', 'rows': [
        ['**Total fixed cost per month**', '', 100000, '@b'],
        ['**Variable cost per machine hour**', '', 6, '@b'],
        ['**Cost function**', '', 'y = 100,000 + 6x', '@b'],
      ]}},
      {'h4': 'Verifying the function against every month'},
      {'p': 'The high-low method uses only two of the six observations, so it is always worth '
            'testing the resulting function on the four it ignored:'},
      {'stmt': {'t': 'Predicted versus actual power cost', 'rows': [
        ['Month', 'Hours (x)', '100,000 + 6x', 'Actual (N)', '@hd'],
        ['April', 50000, 400000, 400000],
        ['May', 60000, 460000, 460000],
        ['June *(low point)*', 40000, 340000, 340000],
        ['July', 45000, 370000, 370000],
        ['August', 70000, 520000, 520000],
        ['September *(high point)*', 75000, 550000, 550000],
      ]}},
      {'key': 'Every one of the six months is predicted **exactly**. That tells you the data in '
              'this question were constructed to lie perfectly on a straight line, so high-low '
              'and least-squares regression would give identical answers. With real data they '
              'would not, and the four ignored months would show small residuals — which is '
              'precisely the weakness of the high-low method, and worth a sentence if the '
              'question asks you to comment on your result.'},
      {'h4': '(c)  Estimating October\'s power cost'},
      {'p': 'Taking the intended reading of **88,000 machine hours**:'},
      {'tex': 'y = 100{,}000 + (6 \\times 88{,}000) = 100{,}000 + 528{,}000 = N628{,}000'},
      {'p': 'Taking the question\'s words literally, at **88 machine hours**:'},
      {'tex': 'y = 100{,}000 + (6 \\times 88) = 100{,}000 + 528 = N100{,}528'},
      {'warn': 'Quote the figure the question\'s own data support — **N628,000** — and add one '
               'line stating your assumption that "88 machine hours" means 88,000, consistent '
               'with the table. An examiner marking a mis-typed question gives credit for a '
               'stated assumption and a correct method. Note also that 88,000 hours is '
               '**outside** the 40,000–75,000 range of the observed data, so the estimate '
               'assumes the linear relationship continues to hold beyond the relevant range — '
               'another sentence worth writing.',
       'lbl': 'How to present this in the exam'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Linear variable cost', 'tex': 'y = bx',
   'nt': 'b = variable cost per unit; x = activity level.'},
  {'lb': 'Fixed cost', 'tex': 'y = a', 'nt': 'a = the fixed cost amount, constant with activity.'},
  {'lb': 'Linear semi-variable cost', 'tex': 'y = a + bx',
   'nt': 'a = fixed element; b = variable cost per unit.'},
  {'lb': 'Polynomial (curvilinear) cost', 'tex': 'y = bx + cx^2 + \\dots + px^n',
   'nt': 'A convex curve (b,c,p give diminishing marginal increases) models economies of scale; '
         'a concave curve models diminishing returns.'},
 ],
 'focus':
   'Classification-by-behaviour and the cost-centre/cost-unit/profit-centre trio are the two '
   'most exam-tested ideas here. Learn the four sub-types of fixed cost (time/volume/policy/'
   'joint-related) by name — a stepped cost is regularly set as a distractor against plain fixed '
   'cost. The long glossary in §2.1(h) (avoidable, sunk, opportunity, incremental, marginal, '
   'conversion, committed, discretionary…) is a recurring short-answer source; learn each '
   'definition\'s one distinguishing word rather than the whole sentence.',
 'errors': [
   'Calling a semi-variable cost "fixed" just because part of it does not change with activity.',
   'Treating controllability as an absolute property of a cost rather than relative to a named '
   'management level.',
   'Confusing incremental cost (additional cost from a *group* of extra units) with marginal '
   'cost (additional cost from *one* extra unit).',
   'Assuming every variable cost is linear across the whole range of activity, rather than only '
   'within the relevant range.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'CIMA defines cost classification as the arrangement of cost into logical groups '
         'according to nature, function or',
    'o': ['the auditor\'s judgement', 'use in the business of the entity',
          'the order in which costs are incurred', 'the financial year in which they fall',
          'the currency in which they are denominated'],
    'a': 1,
    'w': 'CIMA\'s definition names three bases: nature (fixed, variable, value-adding), function '
         '(production, selling), or use in the business of the entity.',
    'src': 'Chapter 2.1', 'sec': '2.1'},
   {'q': 'Costs incurred in publicising and presenting products to customers, including research '
         'work, securing and delivering orders, and after-sales service, are classified as',
    'o': ['production overheads', 'marketing overheads', 'administrative overheads',
          'research and development overheads', 'distribution overheads only'],
    'a': 1,
    'w': 'Marketing overheads is the broader category comprising selling costs, distribution '
         'costs and other related costs such as research work and after-sales service.',
    'src': 'Chapter 2.1', 'sec': '2.1'},
   {'q': 'A cost that is fixed for a given range of activity but changes discretely once activity '
         'moves beyond that range is called a',
    'o': ['linear variable cost', 'semi-variable cost', 'stepped (fixed) cost', 'sunk cost',
          'committed cost'],
    'a': 2,
    'w': 'This is the definition of a stepped fixed cost — constant within a range, then jumping '
         'to a new level once the range is exceeded.',
    'src': 'Chapter 2.2', 'sec': '2.2'},
   {'q': 'Which of the following is an example of a time-related, rather than volume-related, '
         'fixed cost?',
    'o': ['The cost of an additional production plant', 'Advertising expenditure', 'Rent',
          'Research and development cost', 'Supervisory salaries that jump at a new shift'],
    'a': 2,
    'w': 'Rent is the textbook example of a time-related fixed cost — it changes with the '
         'passage of time, not with activity volume.',
    'src': 'Chapter 2.2', 'sec': '2.2'},
   {'q': 'The cost of resources already acquired, created by past decisions and unalterable by '
         'any future decision, is known as a',
    'o': ['committed cost', 'sunk cost', 'opportunity cost', 'incremental cost',
          'discretionary cost'],
    'a': 1,
    'w': 'A sunk cost — e.g. the written-down value of a plant already purchased — cannot be '
         'changed by any decision taken now or in the future.',
    'src': 'Chapter 2.1', 'sec': '2.1'},
   {'q': 'A centre which not only incurs cost but also generates income is called a',
    'o': ['cost centre', 'cost unit', 'profit centre', 'production centre', 'service centre'],
    'a': 2,
    'w': 'A profit centre is distinguished from a plain cost centre by also generating income, '
         'not just incurring cost.',
    'src': 'Chapter 2.3', 'sec': '2.3'},
   {'q': 'In a brewing company, the most natural cost unit is the',
    'o': ['kilowatt hour', 'barrel', 'tonne', 'course', 'bed-day'],
    'a': 1,
    'w': 'Brewing\'s standard cost unit is the barrel; kilowatt hour is electricity\'s, and '
         'bed-day is a hospital\'s.',
    'src': 'Chapter 2.3', 'sec': '2.3'},
   {'q': 'A coding method that applies a whole number to a master group and a decimal to primary '
         'and secondary groups within it (e.g. 4 for Factory Overheads, 4.1 for indirect '
         'material in the factory) is the',
    'o': ['mnemonic method', 'decimal method', 'numerical method', 'alphabetic method',
          'symbolic method'],
    'a': 1,
    'w': 'This is the decimal method of codification — mnemonic uses memorable letter symbols '
         '(e.g. DMA for Direct Material), numerical uses fixed-length digit strings.',
    'src': 'Chapter 2.4', 'sec': '2.4'},
   {'q': 'Which of the following is NOT one of the stated characteristics of a well-designed '
         'coding system?',
    'o': ['Simple for the organisation to operate', 'Flexible in nature', 'Easy to remember',
          'A fixed coding length for every item', 'As many digits as possible, for precision'],
    'a': 4,
    'w': 'A good code should be *concise*, not maximally long — the five stated '
         'characteristics are simplicity, flexibility, memorability, a fixed length, and '
         'conciseness.',
    'src': 'Chapter 2.4', 'sec': '2.4'},
   {'q': 'An extra unit of activity causing a more-than-proportionate increase in cost — i.e. '
         'diminishing returns — describes a',
    'o': ['convex variable-cost curve', 'concave variable-cost curve', 'stepped cost',
          'time-related fixed cost', 'linear variable cost'],
    'a': 1,
    'w': 'A concave cost curve means each extra unit costs more than the last (diminishing '
         'returns); a convex curve is the opposite — each extra unit costs less (economies of '
         'scale).',
    'src': 'Chapter 2.2', 'sec': '2.2'},
  ],
  'theory': [
   {'q': 'Describe THREE different methods of cost classification and explain the usefulness of '
         'each.',
    'marks': 11,
    'a': [
      {'p': '**By element** (materials/labour/expenses) — useful because it identifies exactly '
            'what type of resource is being consumed, feeding directly into the basic cost card.'},
      {'p': '**By nature** (direct/indirect) — useful because it separates costs that can be '
            'traced straight to a cost unit (direct, summing to prime cost) from those that must '
            'first be apportioned to cost centres and absorbed (indirect/overhead) — essential '
            'for accurate unit costing and pricing.'},
      {'p': '**By behaviour** (fixed/variable/semi-variable/stepped) — useful for planning, '
            'budgeting and decision making, since it predicts how total cost will move as '
            'activity changes, e.g. for break-even and cost-volume-profit analysis (Chapter 10).'},
    ], 'src': 'Chapter 2.1', 'sec': '2.1'},
   {'q': 'Citing two examples in each case, explain the following cost classifications: '
         '(i) period costs, (ii) product costs, (iii) variable costs, (iv) opportunity costs.',
    'marks': 17,
    'a': [
      {'p': '**(i) Period costs** — charged in full against the profit of the period incurred, '
            'not included in inventory valuation. Examples: administrative overheads (e.g. audit '
            'fees); selling and distribution overheads (e.g. advertising).'},
      {'p': '**(ii) Product costs** — costs identified with goods produced, used to value '
            'inventory and work in progress. Examples: raw materials cost; production wages.'},
      {'p': '**(iii) Variable costs** — vary in direct proportion with activity level. Examples: '
            'direct materials cost; direct wages paid on a piece-rate basis.'},
      {'p': '**(iv) Opportunity costs** — the value of a benefit forgone by choosing one '
            'alternative over another. Examples: the interest income forgone by investing cash '
            'in a project instead of a bank deposit; the rent forgone by using a company\'s own '
            'building for production instead of letting it out.'},
    ], 'src': 'Chapter 2.1', 'sec': '2.1'},
  ]},
}
