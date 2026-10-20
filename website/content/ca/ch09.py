CH = {
 'n': 9,
 't': 'Costing Techniques: Marginal Costing and Decision Making',
 'brief': 'Marginal costing versus absorption costing — their concepts, the fundamental '
          'differences between the income statements each produces, and the marginal-costing '
          'equation (S − V = C, C − FC = P). Contribution as the central decision-making tool. '
          'Relevant cost and relevant revenue, and sunk cost. The four classic short-term '
          'decisions marginal costing supports — make or buy, accept/reject a special order, '
          'pricing, and profit planning — each with fully verified worked illustrations.',
 'outcomes': [
   'Explain the concepts and differences between marginal and absorption costing',
   'Explain the equation, advantages and limitations of marginal costing',
   'Discuss the importance of contribution margin in managerial decision making',
   'Use marginal costing as a technique for short-term tactical planning and decision-making',
   'Make decisions on whether to make or buy a component, accept or reject an order, and '
   'similar short-term choices',
 ],
 'secs': [
  {'n': '9.1', 't': 'Marginal costing versus absorption costing', 'b': [
    {'p': 'Two of the most popular decision-making techniques in accounting are **marginal '
          'costing** and **absorption costing** — both meant for short-term tactical managerial '
          'decisions about the future, which is inherently uncertain, so both must be applied '
          'with care.'},
    {'note': '"Marginal costing" is the term common in the UK and Europe; the US prefers '
             '"direct costing" or "variable costing" — different names for essentially the same '
             'idea.'},
    {'def': {'t': 'Marginal cost', 'd': 'the cost that arises from producing an additional '
                  'increment of output, and does not arise if that increment is not produced — '
                  'the cost of one additional unit of product or service. In the short run, '
                  'marginal cost is synonymous with variable cost (prime cost + variable '
                  'overheads).'}},
    {'key': 'Marginal costing is **not** a costing system in the way process or job costing '
            'are — it is an **approach to presenting** accounting information, for judging '
            'profitability by studying costs according to their nature (fixed vs variable), not '
            'a method of first ascertaining cost. It formalises the ideas behind flexible '
            'budgets, break-even analysis and Cost-Volume-Profit relationships.'},
    {'p': 'Marginal costing treats only costs that vary directly with output as **product '
          'costs** — the opposite of conventional (absorption) costing, which treats *all* '
          'manufacturing cost, fixed or variable, as product cost.'},
    {'def': {'t': 'Absorption costing', 'd': 'the technique used to prepare income statements '
                  'that ascertain the results of operations, by "absorbing" a fair share of '
                  'general (fixed) overhead into every unit produced or serviced, so every '
                  'indirect cost is properly apportioned into total unit cost.'}},

    {'h4': 'The three fundamental differences, in the income statements each produces'},
    {'table': {'align': 'lll', 'head': ['Difference', 'Absorption costing', 'Marginal costing'],
      'rows': [
      ['**Treatment of fixed production overhead**', 'Part of cost of goods sold', 'A **period '
       'cost**, incurred whether or not production happens, and never part of a product\'s own '
       'cost'],
      ['**Cost of closing inventory**', 'Total (fixed + variable) cost per unit × closing units',
       'Only the **variable** cost per unit × closing units — fixed costs are assumed already '
       'covered by contribution'],
      ['**First profit line shown**', 'Gross profit (then net profit)', '**Contribution margin** '
       '(sales less total variable cost) first, then profit'],
    ]}},
    {'warn': 'Except where every unit produced is also sold in the same period, the two methods '
             'will **not** show the same profit at the first reporting stage — because they '
             'value closing inventory differently, differing amounts of fixed cost get carried '
             'forward into the next period under each method.'},
    {'p': 'Absorption costing is what all three forms of business (sole proprietorship, '
          'partnership, company) and government bodies use for end-of-period income statements '
          '— it aids performance evaluation of past results. Marginal costing is relevant only '
          'for **short-term tactical decisions**, focused on the future.'},

    {'h4': 'The marginal costing equation'},
    {'p': 'Marginal costing hinges on **contribution** — a product\'s contribution toward fixed '
          'costs and profit.'},
    {'fbox': {'h': 'The marginal costing equation', 'rows': [
      {'lb': 'Contribution', 'tex': 'S - V = C', 'nt': 'S = Sales, V = Variable costs, '
       'C = Contribution.'},
      {'lb': 'Profit', 'tex': 'C - FC = P', 'nt': 'FC = Fixed costs, P = Profit.'},
      {'lb': 'Sales at break-even point', 'tex': '\\text{BEP Sales} = \\dfrac{\\text{Fixed '
        'Cost} \\times \\text{Sales}}{\\text{Sales} - \\text{Variable costs}}'},
    ]}},
    {'key': 'Given any **three** of Sales, Variable cost, Fixed cost and Profit, the equation '
            'lets you find the fourth — this is why it is described as of "fundamental '
            'importance": most marginal-costing exam questions are really this equation, '
            'rearranged.'},

    {'h4': 'Advantages of marginal costing'},
    {'ol': [
      '**constant in nature** — marginal cost per unit stays the same regardless of production '
      'volume;',
      '**facilitates cost control** — the clean fixed/variable split enables flexible budgeting;',
      '**simplicity of overhead treatment** — no need for fixed-overhead allocation, '
      'apportionment or absorption, removing the whole under-/over-absorption complication;',
      '**basis for pricing and tendering** — gives a clearer, more logical basis for setting '
      'prices, especially when tendering during a slow period;',
      '**aid to profit planning** — presents data showing cost-volume-profit relationships '
      'directly; and',
      '**more realistic inventory valuation** — finished goods/WIP at marginal cost only, '
      'avoiding the arbitrariness of a fixed-overhead allotment.',
    ]},
    {'h4': 'Limitations of marginal costing'},
    {'ol': [
      '**difficulty in analysis** — splitting overheads into fixed and variable components is '
      'genuinely hard in practice;',
      '**lop-sided emphasis** — tends to over-weight the selling function relative to '
      'production, though both matter equally to overall efficiency;',
      '**difficulty in application** — poorly suited to industries needing large WIP inventories;',
      '**limited scope** — hard to apply in capital-intensive industries with very large fixed '
      'costs; and',
      '**inappropriate basis for pricing on its own** — selling price cannot reasonably be set '
      'on contribution alone, without regard to fixed costs at all.',
    ]},

    {'eg': {'tag': 'Study text', 't': 'Illustration 9.1 — comparative income statements',
      'open': True, 'q': [
      {'p': 'Green-Green Ltd, year ended 31 December 2025: sales 1,000 units @ N10; total '
            'manufacturing cost N2,200 (all fixed); variable manufacturing cost 1,100 units @ '
            'N6; closing inventory 100 units; fixed S&A expenses N500; variable S&A expenses '
            'N400. Prepare the income statement under (a) absorption costing and (b) marginal '
            'costing.'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['(a) Absorption costing', 'N'], 'rows': [
        ['Sales (1,000 @ N10)', '10,000'],
        ['Variable manufacturing cost (1,100 @ N6)', '6,600'],
        ['Fixed manufacturing cost', '2,200'],
        ['Less: closing inventory (100 @ N8)', '(800)'],
        ['**Cost of sales**', '**8,000**'],
        ['**Gross margin**', '**2,000**'],
        ['Less: total selling & admin. expenses', '900'],
        ['**Net income**', '**1,100**'],
      ]}},
      {'p': 'Cost per unit of closing inventory (absorption) $= \\dfrac{100}{1{,}100} \\times '
            '8{,}800 = N800$, i.e. $N8$/unit — using **total** manufacturing cost (6,600+2,200).'},
      {'table': {'align': 'lr', 'head': ['(b) Marginal costing', 'N'], 'rows': [
        ['Sales (1,000 @ N10)', '10,000'],
        ['Variable manufacturing cost (1,100 @ N6)', '6,600'],
        ['Less: closing inventory (100 @ N6)', '(600)'],
        ['**Variable cost of sales**', '**6,000**'],
        ['**Variable gross margin**', '**4,000**'],
        ['Less: variable selling & admin. expenses', '400'],
        ['**Contribution margin**', '**3,600**'],
        ['Less: fixed manufacturing cost', '2,200'],
        ['Less: fixed selling & admin. expenses', '500'],
        ['**Net income**', '**900**'],
      ]}},
      {'key': 'The N200 gap between the two net incomes (1,100 vs 900) is exactly the fixed '
              'manufacturing cost **held back in closing inventory** under absorption costing '
              '(N800 vs N600, a N200 difference) — under marginal costing, that N200 is released '
              'immediately as a period charge instead.'}]}},
  ]},

  {'n': '9.2', 't': 'The role of contribution', 'b': [
    {'p': 'Contribution is central to marginal costing precisely because, where a business makes '
          'more than one product, the profit of an *individual* product cannot really be '
          'calculated — that would need apportioning fixed costs to products, which marginal '
          'costing deliberately avoids.'},
    {'def': {'t': 'Contribution', 'd': 'sales less the variable cost of sales — sometimes called '
                  '"gross margin." A pool that every product contributes its share to, out of '
                  'which all fixed costs (of whatever nature) must be met; the difference '
                  'between total contribution and total fixed cost is profit (or loss).'}},
    {'p': 'Contribution is used in: fixing selling prices, finding the break-even point, '
          'choosing a product mix to maximise profit, make-or-buy decisions, accepting/'
          'rejecting special orders, and assessing the profitability of products or departments.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 9.2 — contribution exposes an arbitrary '
      'apportionment problem', 'open': True, 'q': [
      {'p': 'Prudent Engineering has three departments X, Y, Z: variable costs N90,000/'
            'N100,000/N150,000, fixed costs (apportioned by sales) N20,000/N30,000/N50,000, '
            'sales N100,000/N150,000/N250,000 — giving X a loss of N10,000. Management wants to '
            'close X. (a) Assess this on the data given; (b) reassess if specific fixed costs '
            'are actually N5,000 (X), N55,000 (Y), N30,000 (Z), with N10,000 general.'}],
      'a': [
      {'p': '**(a) All fixed cost treated as general (apportioned by sales):**'},
      {'table': {'align': 'lrrrr', 'head': ['', 'X (N)', 'Y (N)', 'Z (N)', 'Total (N)'],
        'rows': [
        ['Sales', '100,000', '150,000', '250,000', '500,000'],
        ['Less: variable cost', '90,000', '100,000', '150,000', '340,000'],
        ['**Contribution**', '**10,000**', '**50,000**', '**100,000**', '**160,000**'],
        ['Less: fixed costs', '', '', '', '100,000'],
        ['**Profit**', '', '', '', '**60,000**'],
      ]}},
      {'key': 'X\'s apparent "loss" was an artefact of arbitrarily apportioning fixed cost by '
              'sales — X actually **contributes N10,000** toward fixed costs. Closing X would '
              'reduce total contribution (and profit) by N10,000, not save anything.'},
      {'p': '**(b) Using each department\'s own specific fixed cost:**'},
      {'table': {'align': 'lrrrr', 'head': ['', 'X (N)', 'Y (N)', 'Z (N)', 'Total (N)'],
        'rows': [
        ['Contribution', '10,000', '50,000', '100,000', '160,000'],
        ['Less: specific fixed costs', '5,000', '55,000', '30,000', '90,000'],
        ['**Net contribution**', '**5,000**', '**(5,000)**', '**70,000**', '**70,000**'],
        ['Less: general fixed costs', '', '', '', '10,000'],
        ['**Profit**', '', '', '', '**60,000**'],
      ]}},
      {'key': 'Same overall profit (N60,000), but a completely different story: once **specific** '
              'fixed costs are properly traced, it is **Department Y**, not X, that loses money '
              '(N5,000) — closing Y (not X) would raise profit by exactly N5,000, matching Y\'s '
              'own loss. This is the core lesson of the illustration: an arbitrary apportionment '
              'basis can make a genuinely profitable department look like the one to cut.'}]}},
  ]},

  {'n': '9.3', 't': 'Relevant cost, relevant revenue and sunk cost', 'b': [
    {'def': {'t': 'Relevant costs/revenues (CIMA)', 'd': 'costs and revenues appropriate to a '
                  'specific management decision — represented by future cash flows whose size '
                  'depends on the decision\'s outcome. Where inventory is used, the relevant '
                  'cost is its *replacement* cost, not its original (sunk) purchase price.'}},
    {'p': 'Three characteristics a cost/revenue must have to be relevant:'},
    {'ul': [
      'it is a **future** cost/revenue;',
      'it is a **differential** cost/revenue — it differs between the alternatives being '
      'compared; and',
      'it involves an actual **cash flow**.',
    ]},
    {'key': 'A direct consequence: **historical (sunk) costs are never relevant** to a decision '
            'being made now, however large they were.'},
    {'p': 'Common relevant-cost items: **notional/imputed costs** (not in financial accounts at '
          'all, since no cash changes hands — e.g. notional interest on internally-generated '
          'funds, notional rent for space already owned — but still useful for decisions); '
          '**opportunity cost** (the value of the best alternative forgone); out-of-pocket cost; '
          'replacement cost; and differential costs above zero.'},
    {'def': {'t': 'Sunk cost (CIMA)', 'd': 'cost that has been irreversibly incurred or '
                  'committed, and so cannot be relevant to a decision — also called an '
                  'irrecoverable cost.'}},
    {'note': 'A past cost is relevant **only if** it still has a replacement/market value, or '
             'can be redirected to an alternative use — otherwise its value in decision-making '
             'is zero.'},
    {'table': {'align': 'll', 'head': ['Cost element', 'Relevant cost rule'], 'rows': [
      ['**Material**', 'If material already in store will be used regardless, its relevant cost '
       'is **NIL**. If it has a replacement/market value or an alternative use, *that* value is '
       'relevant.'],
      ['**Labour**', 'A worker\'s **fixed salary** is irrelevant (it is paid either way) — only '
       'the **opportunity cost** of redirecting a fixed-salary earner\'s time is relevant.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration — finding a minimum price using only '
      'relevant costs', 'open': True, 'q': [
      {'p': 'A special order will use N10,000 of material already in store, with no market '
            'value and no alternative use. Additional material CD must be bought for N30,000. '
            'Factory workers will be paid N50,000 total. The order uses idle plant (written down '
            'value N200,000, depreciation N5,000/month) for one month. Find the minimum price.'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['', 'N'], 'rows': [
        ['Existing material in stores', 'NIL'],
        ['Material CD', '30,000'],
        ['Factory workers\' wages', '50,000'],
        ['Manager\'s salary', 'NIL'],
        ['Plant depreciation', 'NIL'],
        ['**Minimum price**', '**80,000**'],
      ]}},
      {'key': 'Existing stores material is sunk (no market value/alternative use, so NIL); the '
              'manager\'s salary is irrelevant (paid regardless); plant depreciation on **idle** '
              'plant is a sunk cost too, since the plant\'s book value is unaffected by whether '
              'this particular order uses it. Only material CD and the factory wages are genuine '
              'future, differential cash flows.'}]}},
  ]},

  {'n': '9.4', 't': 'Practical applications of marginal costing', 'b': [
    {'h4': 'Make or buy decisions'},
    {'p': 'Arises when a manufacturer must decide whether to make a component in-house or buy '
          'it from an outside supplier. The relevant comparison is the supplier\'s quotation '
          'against the **incremental cost of in-house production** (plus any opportunity cost '
          'of producing in-house).'},
    {'p': 'Qualitative factors to weigh alongside the pure cost comparison: the quality of the '
          'bought-in product; the outside supplier\'s reliability; the effect of future market '
          'prices; management\'s ability to handle current/future capacity; the risk of '
          'revealing trade secrets; and transport/handling problems.'},
    {'table': {'align': 'll', 'head': ['Comparison', 'Decision'], 'rows': [
      ['Supplier\'s quotation **>** total variable cost of making in-house', '**Make** '
       'in-house'],
      ['Total variable cost of making in-house **>** supplier\'s quotation', 'It is prudent to '
       '**buy** from the supplier'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 9.3 — make or buy, differential cost '
      'analysis', 'open': True, 'q': [
      {'p': 'Nagarta Nig. PLC can subcontract a component at N1.80/piece. Subcontracting would '
            'save: material N0.50/unit, labour N0.25/unit, variable overhead N1.00/unit, plus '
            'N2,000/year supervision and N500/year special tools. Units sold: 14,000. Current '
            'standard cost: materials N70,000, labour N28,000, factory overhead N140,000, with '
            'variable overhead at N4/unit and fixed at N6/unit (normal capacity 20,000 units). '
            'Net loss currently N24,000, with selling & admin. N100,000. Advise on subcontracting.'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['', 'Make (N)', 'Difference (N)', 'Buy (N)'],
        'rows': [
        ['Net sales', '350,000', '', '350,000'],
        ['Direct materials', '70,000', '−7,000', '63,000'],
        ['Purchased parts', '—', '+25,200', '25,200'],
        ['Direct labour', '28,000', '−3,500', '24,500'],
        ['Variable overheads', '56,000', '−14,000', '42,000'],
        ['Fixed overheads', '120,000', '−2,500', '117,500'],
        ['**Total manufacturing cost**', '**274,000**', '**−1,800**', '**272,200**'],
        ['Selling & admin.', '100,000', '—', '100,000'],
        ['**Total cost**', '**374,000**', '**−1,800**', '**372,200**'],
        ['**Net loss**', '**(24,000)**', '**−1,800**', '**(22,200)**'],
      ]}},
      {'key': 'With no change in volume or price, revenue is irrelevant — the whole decision '
              'comes down to a **N1,800 cost saving** from subcontracting. Even so, this small '
              'saving may not outweigh the non-quantitative cost of laying off staff — the '
              'differential cost analysis is the *core* of the decision, not necessarily its '
              'final word.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 9.4 — make or buy across several components',
      'open': True, 'q': [
      {'p': 'A.B. Ltd makes W (1,000 units), X (2,000), Y (4,000), Z (3,000). Unit marginal '
            'costs: W N14, X N17, Y N7, Z N12. A subcontractor offers W N12, X N21, Y N10, Z '
            'N14. Directly attributable annual fixed costs: W N1,000, X N5,000, Y N6,000, Z '
            'N8,000 (plus N30,000 committed fixed costs, unaffected either way). Advise.'}],
      'a': [
      {'table': {'align': 'lrrrr', 'head': ['', 'W', 'X', 'Y', 'Z'], 'rows': [
        ['Unit variable cost, making', 'N14', 'N17', 'N7', 'N12'],
        ['Unit variable cost, buying', 'N12', 'N21', 'N10', 'N14'],
        ['Extra variable cost of buying (per unit)', '(2)', '4', '3', '2'],
        ['Annual requirement (units)', '1,000', '2,000', '4,000', '3,000'],
        ['Extra variable cost of buying, total (N)', '(2,000)', '8,000', '12,000', '6,000'],
        ['Fixed cost saved by buying (N)', '1,000', '5,000', '6,000', '8,000'],
        ['**Net effect of buying (N)**', '**(3,000)**', '**3,000**', '**6,000**', '**(2,000)**'],
      ]}},
      {'key': 'A **negative** net-effect figure means buying **saves** money overall (extra '
              'variable cost is more than offset by fixed cost saved, or is itself negative): '
              'buy **W** (saves N3,000, since buying is cheaper per unit even before counting '
              'fixed savings) and buy **Z** (saves N2,000, this time *because of* the fixed-cost '
              'saving, even though its variable cost is higher). Keep making **X** and **Y** — '
              'buying either would cost more overall.'},
      {'p': 'Other considerations: what happens to the spare capacity freed up by buying W and '
            'Z? Is the subcontractor reliable on delivery and quality? Does the company want to '
            'stay flexible by making everything itself? Are the fixed-cost-saving estimates '
            'themselves reliable?'}]}},

    {'h4': 'Acceptance/rejection of a special order'},
    {'p': 'Arises when a customer offers a price below the normal selling price. If the company '
          'has **spare capacity**, and the special price still **covers marginal cost**, '
          'accepting typically adds to profit — since fixed costs are already covered by normal '
          'sales.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 9.5 — accept or reject a special order',
      'open': True, 'q': [
      {'p': 'Shukura Nig. Ltd sells "slimming sticks" at 20k each; current output 400,000 (80% '
            'of capacity — so full capacity is 500,000). Total cost for the period N56,000, of '
            'which N16,000 is fixed (so variable cost = N40,000/400,000 = 10k/unit). A customer '
            'offers 13k/stick for a 100,000-unit order. Advise.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['', 'Present position (N)', 'If order accepted (N)'],
        'rows': [
        ['Sales', '80,000 (400,000 @ 20k)', '13,000 (100,000 @ 13k)'],
        ['Less: marginal cost', '40,000 (400,000 @ 10k)', '10,000 (100,000 @ 10k)'],
        ['Contribution', '40,000', '3,000'],
        ['Less: fixed costs', '16,000', '—'],
        ['**Net profit**', '**24,000**', '**+3,000 extra**'],
      ]}},
      {'key': '**Accept** the order — it adds N3,000 to profit, since 13k still exceeds the '
              '10k marginal cost, and spare capacity (100,000 units) exists to absorb it without '
              'displacing normal-price sales.'},
      {'p': 'Other factors: will this special price prompt other customers to demand the same '
            'discount? Is this the most profitable use of the spare capacity? Could accepting it '
            'crowd out a later order at the true market price? Will fixed costs really stay '
            'constant?'}]}},

    {'h4': 'Marginal costing and pricing decisions'},
    {'p': 'Marginal costing clarifies the relationship between a product\'s own cost and various '
          'candidate selling prices, since contribution is unaffected by how indirect costs are '
          'allocated.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 9.6 — units needed to maintain profit after '
      'a price cut', 'open': True, 'q': [
      {'p': 'M&K Industries: present sales 30,000 units @ N10 (N300,000), variable cost N180,000 '
            '(N6/unit), fixed cost N70,000, profit N50,000. If price is cut 5%, 10% or 15%, how '
            'many units must be sold to hold profit at N50,000?'}],
      'a': [
      {'p': 'To hold profit at N50,000 with fixed cost unchanged at N70,000, total contribution '
            'must stay at N120,000.'},
      {'table': {'align': 'lrrr', 'head': ['Price cut', 'New price', 'New contribution/unit',
        'Units needed'], 'rows': [
        ['5%', 'N9.50', 'N3.50', '120,000 ÷ 3.50 ≈ 34,286'],
        ['10%', 'N9.00', 'N3.00', '120,000 ÷ 3.00 = 40,000'],
        ['15%', 'N8.50', 'N2.50', '120,000 ÷ 2.50 = 48,000'],
      ]}},
      {'p': '**Verification at 10%**: sales $= 40{,}000 \\times 9 = N360{,}000$; variable cost '
            '$= 40{,}000 \\times 6 = N240{,}000$; contribution $= N120{,}000$; less fixed '
            'N70,000 $=$ profit **N50,000** — exactly as required.'}]}},

    {'h4': 'Marginal costing and profit planning'},
    {'p': 'Contribution ratio also drives forward planning — finding the volume, or the price, '
          'needed to hit a target profit.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 9.7 — minimum price for an extra-capacity '
      'order, given rising costs', 'open': True, 'q': [
      {'p': 'A toy manufacturer sells 60,000 pieces (60% of capacity) @ N15, earning N3/piece '
            'profit. Cost composition: DM N4.00, DL N1.00, works overhead N6.00 (50% fixed), '
            'sales overhead N1.00 (25% variable). This year: fixed costs +10%, direct labour '
            'rate +20%, direct material rate +5%, selling price unchanged. An order for a '
            'further 20% of capacity (20,000 units) is offered. Find the minimum price for the '
            'order needed to reach an overall profit of N180,500.'}],
      'a': [
      {'p': 'New variable costs/piece: DM $4.20$ ($4.00 \\times 1.05$); DL $1.20$ ($1.00 \\times '
            '1.20$); variable works overhead unchanged at $3.00$ (only the *fixed* half of works '
            'overhead rises); variable sales overhead unchanged at $0.25$. Total $= N8.65$/piece.'},
      {'table': {'align': 'lr', 'head': ['Marginal costing statement (60,000 pieces)', 'N'],
        'rows': [
        ['Variable cost (60,000 × 8.65)', '519,000'],
        ['Sales value (60,000 × 15)', '900,000'],
        ['**Contribution**', '**381,000**'],
      ]}},
      {'p': 'Fixed works overhead (50% of original N6 × 60,000 $= N180{,}000$) $+10\\% = '
            'N198{,}000$. Fixed sales overhead (75% of original N1 × 60,000 $= N45{,}000$) '
            '$+10\\% = N49{,}500$. Total fixed cost $= N247{,}500$.'},
      {'tex': '\\text{Profit before the order} = 381{,}000 - 247{,}500 = N133{,}500'},
      {'tex': '\\text{Required increase in profit} = 180{,}500 - 133{,}500 = N47{,}000'},
      {'tex': '\\text{Minimum price} = \\dfrac{(20{,}000 \\times 8.65) + 47{,}000}{20{,}000} = '
              '\\dfrac{220{,}000}{20{,}000} = N11\\text{/unit}'}]}},
  ]},

  {'n': '9.5', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§9.1 Marginal vs absorption costing** — marginal costing is a presentation approach, '
      'not a costing system; only variable manufacturing cost is a "product cost" under marginal '
      'costing; 3 income-statement differences (fixed-overhead treatment, closing-inventory '
      'valuation, first profit line shown); $S-V=C$, $C-FC=P$; 6 advantages, 5 limitations.',
      '**§9.2 Contribution** — sales less variable cost of sales; the pool every product feeds '
      'fixed-cost recovery from; exposing an arbitrary fixed-cost apportionment can completely '
      'flip which department/product "looks" unprofitable.',
      '**§9.3 Relevant cost/revenue** — must be future, differential, and a real cash flow; sunk '
      'costs are never relevant; material in store already committed is NIL relevant cost unless '
      'it has a real alternative use/market value; only a fixed-salary worker\'s *opportunity '
      'cost*, not their salary itself, is relevant.',
      '**§9.4 Four practical applications** — make or buy (compare quotation vs variable cost of '
      'making, plus fixed-cost-saved); special order acceptance (accept if price covers marginal '
      'cost and spare capacity exists); pricing (contribution/unit needed for a given profit '
      'target at a new price); profit planning (minimum price for extra volume to hit a named '
      'target profit, allowing for cost inflation).',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Marginal cost** — cost of one additional unit; effectively variable cost in the short '
      'run. **Contribution** — sales less variable cost of sales.',
      '**Relevant cost/revenue** — future, differential, a real cash flow. **Sunk cost** — '
      'irreversibly incurred, never relevant.',
      '**Notional (imputed) cost** — no real cash flow, but useful for decisions (e.g. notional '
      'rent). **Opportunity cost** — the value of the best alternative forgone.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'Marginal costing formulas (recap)', 'rows': [
      {'lb': 'Contribution', 'tex': 'S - V = C'},
      {'lb': 'Profit', 'tex': 'C - FC = P'},
      {'lb': 'Sales at break-even point', 'tex': '\\dfrac{FC \\times S}{S - V}'},
      {'lb': 'Units needed for a target contribution',
       'tex': '\\dfrac{\\text{Required total contribution}}{\\text{Contribution per unit}}'},
    ]}},
  ]},

  {'n': '9.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'What is marginal cost? (A) Cost incurred when increasing profit margin  (B) Total cost '
        'of manufacture  (C) Cost of producing an additional unit  (D) Cost of manufacturing a '
        'new product  (E) Aggregate cost of manufacturing diverse products',
        'What are period costs? (A) Costs incurred during a stated period of production  '
        '(B) Costs incurred during certain periods of the year  (C) Costs which serve to '
        'enhance profitability  (D) Costs of maintaining equipment during a period  (E) Costs '
        'incurred during a period irrespective of production volume',
        'How does marginal costing differ from absorption costing in inventory valuation? '
        '(A) Marginal costing is only concerned with margins  (B) Absorption costing uses LIFO  '
        '(C) Absorption costing recognises slow-moving inventory  (D) Marginal costing uses '
        'total variable costs, writing off fixed assets  (E) Marginal costing uses FIFO',
        'What is contribution? (A) Total sales minus total variable costs  (B) Total sales plus '
        'total variable costs  (C) Total variable costs plus total fixed costs  (D) Total fixed '
        'costs minus profit  (E) Total sales plus total fixed costs',
        'What is a limiting factor? (A) The extent to which the company may manufacture its '
        'products  (B) The factor of production which is in short supply  (C) The limit to '
        'which government may allow the company to manufacture  (D) The factor of production '
        'which is most expensive  (E) The factor of production which is easily obtainable',
        'Under absorption costing, closing inventory includes a portion of the period\'s '
        '…………….',
        'In most decision-making scenarios, marginal costing advises that the relevant cost is '
        'the ……………………………',
        'Under marginal costing, sales minus variable costs equals ……………………………',
        'What is the major cause of differences in profit figures derived from profitability '
        'statements using absorption costing and marginal costing?',
        'Based purely on financial information, a company should manufacture more of the '
        'products giving the highest ……………. towards the absorption of its fixed costs and '
        'ultimately earning profit.',
      ]}],
      'a': [
      {'ol': [
        '**C — cost of producing an additional unit.**',
        '**E** — costs incurred during a period, irrespective of production volume.',
        '**D** — marginal costing uses only total *variable* costs; absorption costing uses '
        'total (fixed + variable) cost.',
        '**A — total sales minus total variable costs.**',
        '**B — the factor of production which is in short supply.**',
        '**Fixed costs.**',
        '**Variable cost (marginal cost).**',
        '**Contribution.**',
        '**The value of closing inventory / the treatment of fixed costs.**',
        '**Contribution.**',
      ]}]}},
  ]},

  {'n': '9.7', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with eight examination-type questions, almost all '
          'of them decision-making problems. All are reproduced below with full answers.'},

    {'eg': {'tag': 'Exam type — Q1',
      't': 'Dala Equipment — make or buy four components under a machine-capacity constraint',
      'q': [
      {'p': 'Dala Equipment Limited manufactures four components, the cost particulars of which '
            'are given below:'},
      {'stmt': {'t': 'Cost per component (N)', 'rows': [
        ['Elements of cost', 'A', 'B', 'C', 'D', '@hd'],
        ['Direct material', 80, 100, 100, 120],
        ['Direct labour', 20, 25, 25, 30],
        ['Variable overhead', 10, 12, 15, 10],
        ['Fixed overhead', 15, 23, 20, 20],
        ['**Total cost**', 125, 160, 160, 180, '@t'],
        '@gap',
        ['Output per machine hour (units)', 4, 2, 3, 3],
      ]}},
      {'p': 'The **key factor is shortage of machine capacity**. The components are used in the '
            'company\'s main product. A supplier has quoted the following prices: **A N115; '
            'B N175; C N135; D N185**.'},
      {'p': '**Required:** advise management whether they should continue to produce all or some '
            'of the components, or buy them from the supplier.'}],
      'a': [
      {'h4': 'Step 1 — the relevant cost of making'},
      {'p': 'Fixed overhead will be incurred whether or not the component is made in-house, so '
            'it is **irrelevant** to the decision. Only the **variable** cost is saved by '
            'buying:'},
      {'stmt': {'t': 'Marginal (variable) cost of making, per unit (N)', 'rows': [
        ['', 'A', 'B', 'C', 'D', '@hd'],
        ['Direct material', 80, 100, 100, 120],
        ['Direct labour', 20, 25, 25, 30],
        ['Variable overhead', 10, 12, 15, 10],
        ['**Marginal cost of making**', 110, 137, 140, 160, '@tt'],
      ]}},
      {'h4': 'Step 2 — the extra cost of buying'},
      {'stmt': {'t': 'Extra cost of buying rather than making, per unit (N)', 'rows': [
        ['', 'A', 'B', 'C', 'D', '@hd'],
        ['Supplier\'s price', 115, 175, 135, 185],
        ['Less: marginal cost of making', 110, 137, 140, 160],
        ['**Extra cost of buying**', 5, 38, -5, 25, '@tt'],
      ]}},
      {'note': 'Component **C is cheaper to buy than to make even before capacity is '
               'considered** — the supplier\'s N135 is N5 below the N140 it costs in variable '
               'cost alone. C should therefore be bought outright, whatever the machine-hour '
               'position.'},
      {'h4': 'Step 3 — rank by the saving per unit of the limiting factor'},
      {'p': 'Machine capacity is short, so the question is not simply which components are '
            'cheaper to make, but which make the **best use of each scarce machine hour**. '
            'Convert output per machine hour into machine hours per unit, then express the '
            'saving from making as a saving **per machine hour**:'},
      {'stmt': {'t': 'Benefit of making, per machine hour', 'rows': [
        ['', 'A', 'B', 'C', 'D', '@hd'],
        ['Output per machine hour (units)', 4, 2, 3, 3],
        ['Machine hours per unit', 0.25, 0.50, '0.333', '0.333'],
        ['Extra cost of buying, per unit (N)', 5, 38, -5, 25],
        ['**Saving from making, per machine hour (N)**', 20, 76, -15, 75, '@t'],
        ['**Ranking**', '3rd', '**1st**', 'do not make', '2nd', '@tt'],
      ]}},
      {'h4': 'Advice to management'},
      {'ol': [
        '**Buy component C** from the supplier in full. It costs N5 per unit *more* to make it '
        'than to buy it, so making it would waste both money and scarce machine time.',
        '**Make component B first.** Every machine hour devoted to B saves **N76** against the '
        'cost of buying — the highest return on the scarce resource.',
        '**Make component D second**, saving N75 per machine hour.',
        '**Make component A last**, saving only N20 per machine hour.',
        '**Buy in whatever cannot be made** once the available machine hours run out, working '
        'down the ranking.',
      ]},
      {'key': 'The trap this question is built around is the ranking of **A against D**. On a '
              'per-unit view, making D saves N25 and making A only N5, so A looks the weaker '
              'candidate — and it is. But if the ranking had been done on per-unit savings '
              'alone it could easily have gone wrong, because a component with a small per-unit '
              'saving may still be the better use of a machine hour if it uses very little '
              'machine time. **When a limiting factor exists, always rank by contribution (or '
              'saving) per unit of the limiting factor, never per unit of product.**'},
      {'note': 'Non-financial factors a complete answer would mention: the reliability and '
               'quality of the supplier; the security of supply for components used in the '
               'company\'s **main** product; whether the quoted prices are guaranteed and for '
               'how long; the effect on the workforce; and the risk of becoming dependent on an '
               'outside supplier who may later raise prices.'}]}},

    {'eg': {'tag': 'Exam type — Q2',
      't': 'Indabawa Mills — should product B be dropped?',
      'q': [
      {'p': 'Three different product lines are sold by Indabawa Mills. **Product A contributes '
            '20% of its revenue** to fixed costs and profits, **product B 10%** and **product C '
            '60%**. The products sell at: A **N8** per unit; B **N2** per unit; C **N3** per '
            'unit.'},
      {'p': 'The company earned a net profit of **N50,000** before income taxes last year by '
            'selling **50,000 units of A, 150,000 units of B and 60,000 units of C**.'},
      {'p': 'The sales manager, Muhammed Ibrahim, believes the profit picture can be improved by '
            '**eliminating product B** and concentrating the sales effort on A and C. He sees an '
            'opportunity to increase sales of A to **70,000 units**, but admits C will probably '
            'sell the same amount next year.'},
      {'p': '**Required:** prepare a projected income statement using Ibrahim\'s assumptions. Do '
            'you agree with him? Explain what would cause the profit to increase or decrease.'}],
      'a': [
      {'h4': 'Step 1 — last year\'s position, and the fixed costs'},
      {'stmt': {'t': 'Last year (N)', 'rows': [
        ['', 'Product A', 'Product B', 'Product C', 'Total', '@hd'],
        ['Units sold', 50000, 150000, 60000, ''],
        ['Selling price per unit', 'N8', 'N2', 'N3', ''],
        ['**Sales revenue**', 400000, 300000, 180000, 880000, '@t'],
        ['P/V ratio (contribution as % of revenue)', '20%', '10%', '60%', ''],
        ['**Contribution**', 80000, 30000, 108000, 218000, '@t'],
        ['Less: fixed costs *(balancing figure)*', '', '', '', 168000],
        ['**Net profit before tax**', '', '', '', 50000, '@tt'],
      ]}},
      {'h4': 'Step 2 — the projected income statement on Ibrahim\'s assumptions'},
      {'stmt': {'t': 'Projected income statement — product B eliminated (N)', 'rows': [
        ['', 'Product A', 'Product C', 'Total', '@hd'],
        ['Units sold', 70000, 60000, ''],
        ['Selling price per unit', 'N8', 'N3', ''],
        ['**Sales revenue**', 560000, 180000, 740000, '@t'],
        ['P/V ratio', '20%', '60%', ''],
        ['**Contribution**', 112000, 108000, 220000, '@t'],
        ['Less: fixed costs (assumed unchanged)', '', '', 168000],
        ['**Projected net profit before tax**', '', '', 52000, '@tt'],
      ]}},
      {'h4': 'Step 3 — what causes the change'},
      {'stmt': {'t': 'Reconciliation of the N2,000 increase (N)', 'rows': [
        ['Contribution gained from the extra 20,000 units of A (20,000 × N8 × 20%)', '', 32000],
        ['Contribution lost by dropping product B entirely', '', -30000],
        ['**Net increase in profit**', '', 2000, '@tt'],
      ]}},
      {'h4': 'Do you agree with Ibrahim?'},
      {'p': '**Only with substantial reservations.** On his own assumptions profit rises by just '
            '**N2,000**, or **4%** — a thin reward for abandoning a product line that generates '
            '**N300,000 of revenue and N30,000 of contribution**. The whole of the gain depends '
            'on two assumptions, either of which could easily be wrong:'},
      {'ol': [
        '**That sales of A really will rise by 20,000 units.** If A reaches only 68,750 units, '
        'the extra contribution is N30,000 and the company is exactly no better off; below that '
        'it is worse off. There is no margin for error at all.',
        '**That fixed costs stay at N168,000.** Dropping B saves nothing in fixed cost on this '
        'analysis. If any fixed cost is **specific to B** and would be avoided, the proposal '
        'improves; if dropping B instead causes fixed costs to be reapportioned over A and C '
        'without falling, nothing is saved.',
      ]},
      {'p': 'Further considerations against the proposal:'},
      {'ul': [
        '**B still makes a positive contribution of N30,000** towards fixed costs. A product '
        'should never be dropped merely because its P/V ratio is low — only if its contribution '
        'is negative, or if the capacity it uses can earn more elsewhere.',
        '**Customers may buy the three products together**, so withdrawing B could cost sales of '
        'A and C as well.',
        '**Idle capacity.** If the resources released by B cannot in fact be redeployed to A, '
        'the company loses B\'s contribution and gains nothing.',
        '**Loss of market presence** and of the option to improve B\'s margin later.',
      ]},
      {'key': 'The better question is not "should we drop B?" but **"can we sell 20,000 more '
              'units of A without dropping B?"** If the extra demand for A is real and capacity '
              'exists, the company could earn N32,000 more while keeping B\'s N30,000 — a '
              'profit of N82,000 rather than N52,000. Ibrahim has bundled two separate decisions '
              'into one, and only one of them is attractive.'}]}},

    {'eg': {'tag': 'Exam type — Q3',
      't': 'Wali and Gwangwazo — should the loss-making product X be discontinued?',
      'q': [
      {'p': 'Management is considering a proposal to discontinue the manufacture of product X '
            'from its range X, Y and Z:'},
      {'stmt': {'t': 'Present position', 'rows': [
        ['', 'X', 'Y', 'Z', '@hd'],
        ['Capacity in actual production', '20%', '40%', '40%'],
        ['Units manufactured', 4000, 10000, 12000],
        '@gap',
        ['**Costs per unit (N)**', '', '', '', '@hd'],
        ['Materials', 25, 20, 40],
        ['Labour', 15, 10, 20],
        ['Fixed overhead', 4, 4, 5],
        ['Variable overhead', 4, 3, 5],
        ['**Total cost**', 48, 37, 70, '@t'],
        ['Profit / (loss) per unit as printed', '(4)', 13, 10],
        ['**Selling price**', 52, 50, 80, '@t'],
      ]}},
      {'p': 'Product X has persistently shown a loss because demand is saturated. Y and Z have '
            'bright prospects, having been accepted as components by a newly established '
            'machine-building complex nearby. The capacity released by discontinuing X is to be '
            '**transferred equally to Y and Z**. The nature of X is such that the transfer would '
            'bring about an increase of **30% for Y** and **50% for Z** in the number of units '
            'manufactured, over those involved in the capacity transferred — without any change '
            'in total fixed costs. Anticipated increases:'},
      {'stmt': {'t': 'Anticipated changes', 'rows': [
        ['', 'Y', 'Z', '@hd'],
        ['Materials', '+5%', '+5%'],
        ['Labour', '+10%', '+10%'],
        ['Selling price', '+10%', '+5%'],
      ]}},
      {'p': '**Required:** (a) prepare a statement of projected profitability; (b) advise '
            'management whether the proposal should be accepted.'},
      {'warn': 'The printed table shows X at a **loss of N4** per unit, but its own figures give '
               '$52 - 48 = $ a **profit** of N4. One of the two numbers must be wrong. The '
               'analysis below uses the printed **selling prices** throughout, because they are '
               'what drive the revised figures for Y and Z, and notes the effect of the '
               'alternative reading on X at the end. The recommendation is the same either way.',
       'lbl': 'An inconsistency in the printed data'}],
      'a': [
      {'h4': 'Step 1 — the present position, restated on contribution'},
      {'stmt': {'t': 'Present profitability (N)', 'rows': [
        ['', 'X', 'Y', 'Z', 'Total', '@hd'],
        ['Units manufactured', 4000, 10000, 12000, ''],
        ['Selling price per unit', 52, 50, 80, ''],
        ['Variable cost per unit (materials + labour + variable overhead)', 44, 33, 65, ''],
        ['**Contribution per unit**', 8, 17, 15, '', '@t'],
        ['**Total contribution**', 32000, 170000, 180000, 382000, '@t'],
        ['Less: fixed overhead (4,000×4; 10,000×4; 12,000×5)', 16000, 40000, 60000, 116000],
        ['**Profit**', 16000, 130000, 120000, 266000, '@tt'],
      ]}},
      {'h4': 'Step 2 — the units after the transfer of capacity'},
      {'p': 'X occupies **20%** of capacity, to be split equally — 10% to Y and 10% to Z. Y\'s '
            'present 40% yields 10,000 units, so 10% yields 2,500; Z\'s 40% yields 12,000 '
            'units, so 10% yields 3,000. The transferred capacity then yields 30% more for Y and '
            '50% more for Z:'},
      {'stmt': {'t': 'Revised output', 'rows': [
        ['', 'Y', 'Z', '@hd'],
        ['Units from the capacity transferred, pro rata (10% of capacity)', 2500, 3000],
        ['Add: increase of 30% for Y;  50% for Z', 750, 1500],
        ['**Additional units**', 3250, 4500, '@t'],
        ['Present units', 10000, 12000],
        ['**Revised units manufactured**', 13250, 16500, '@tt'],
      ]}},
      {'h4': 'Step 3 — the revised unit figures'},
      {'stmt': {'t': 'Revised selling price and variable cost per unit (N)', 'rows': [
        ['', 'Y', 'Z', '@hd'],
        ['Materials  (20 × 1.05;  40 × 1.05)', 21.00, 42.00],
        ['Labour  (10 × 1.10;  20 × 1.10)', 11.00, 22.00],
        ['Variable overhead (unchanged)', 3.00, 5.00],
        ['**Revised variable cost per unit**', 35.00, 69.00, '@t'],
        ['Revised selling price  (50 × 1.10;  80 × 1.05)', 55.00, 84.00],
        ['**Revised contribution per unit**', 20.00, 15.00, '@tt'],
      ]}},
      {'h4': '(a)  Statement of projected profitability'},
      {'stmt': {'t': 'Projected profitability after discontinuing X (N)', 'rows': [
        ['', 'Y', 'Z', 'Total', '@hd'],
        ['Revised units', 13250, 16500, ''],
        ['Contribution per unit', 20.00, 15.00, ''],
        ['**Total contribution**', 265000, 247500, 512500, '@t'],
        ['Less: total fixed overhead (unchanged)', '', '', 116000],
        ['**Projected profit**', '', '', 396500, '@tt'],
      ]}},
      {'h4': '(b)  Advice to management'},
      {'stmt': {'t': 'Comparison (N)', 'rows': [
        ['Projected profit if X is discontinued', '', 396500],
        ['Present profit with all three products', '', 266000],
        ['**Increase in profit**', '', 130500, '@tt'],
      ]}},
      {'p': '**The proposal should be accepted.** Profit rises by **N130,500**, an increase of '
            'nearly 50%. Note carefully *why*: **not** because X makes a loss — on the printed '
            'selling price X actually earns a contribution of **N32,000**, which the company '
            'gives up — but because the capacity X occupies can earn far more when switched to '
            'Y and Z, which between them gain N182,500 of extra contribution (N95,000 from Y and '
            'N67,500 from Z, including the price increases).'},
      {'note': 'If instead X\'s printed loss of N4 per unit is taken as correct (implying a '
               'selling price of N44 and a contribution of nil), the present profit is N234,000 '
               'and the increase from the proposal is N162,500. The recommendation is unchanged '
               'and is, if anything, stronger.'},
      {'warn': 'Two cautions for the answer: the whole gain depends on the assumption that the '
               'extra 3,250 units of Y and 4,500 units of Z **can actually be sold** at the '
               'higher prices, and on fixed costs genuinely remaining at N116,000. Discontinuing '
               'X is also difficult to reverse if demand for it recovers.'},
      {'key': 'The lesson is the one that runs through this whole chapter: **a product should '
              'never be dropped because it shows a loss on a full-cost basis.** It should be '
              'dropped only if its contribution is negative, or — as here — if the scarce '
              'capacity it occupies will earn more elsewhere. The deciding figure is the '
              '**opportunity cost of the capacity**, not the apportioned fixed overhead.'}]}},

    {'eg': {'tag': 'Exam type — Q4',
      't': 'Jigawa Limited — make or buy, with a legislation cost and a sunk-cost argument',
      'q': [
      {'p': 'Management is considering next year\'s production and purchase budgets. One '
            'component, incorporated into another product before sale, has a budgeted '
            'manufacturing cost of:'},
      {'stmt': {'t': 'Budgeted manufacturing cost per unit (N)', 'rows': [
        ['Direct material', '', 14.00],
        ['Direct labour (4 hours at N3)', '', 12.00],
        ['Variable overhead (4 hours at N2)', '', 8.00],
        ['Fixed overhead (4 hours at N5)', '', 20.00],
        ['**Total**', '', 54.00, '@tt'],
      ]}},
      {'p': 'Ball Limited has offered to supply the component at a guaranteed price of **N50 per '
            'unit**.'},
      {'p': '**Required:** **(a)** considering cost criteria only, advise management whether the '
            'component should be purchased from Ball Limited. **(b)** Explain how your advice '
            'would be affected if, as a result of government legislation, continuing to '
            'manufacture would mean additional inspection and testing expenses of **N56,000 per '
            'annum** not included above. **(c)** The production director recently said: "We must '
            'continue to manufacture the component as only one year ago we purchased some '
            'special grinding equipment to be used exclusively for it. The equipment cost '
            'N100,000, it cannot be resold or used elsewhere, and if we cease production we will '
            'have to write off the written-down value of N80,000." Draft a reply.'}],
      'a': [
      {'h4': '(a)  Make or buy on cost criteria'},
      {'p': 'Fixed overhead of N20 per unit is absorbed, not incurred by the decision — it will '
            'continue whether the component is made or bought — so it is **irrelevant**. The '
            'relevant comparison is the **variable** cost of making against the purchase price:'},
      {'stmt': {'t': 'Relevant cost comparison, per unit (N)', 'rows': [
        ['**Cost of making (relevant costs only)**', '', '', '@hd'],
        ['Direct material', 14.00, ''],
        ['Direct labour', 12.00, ''],
        ['Variable overhead', 8.00, 34.00],
        '@gap',
        ['**Cost of buying from Ball Limited**', '', 50.00],
        ['**Extra cost of buying, per unit**', '', 16.00, '@tt'],
      ]}},
      {'p': '**Advice: continue to manufacture the component.** Buying it would cost N16 per '
            'unit more than making it. The N54 full cost is misleading — N20 of it is fixed '
            'overhead that does not disappear if the component is bought in, and would simply be '
            'reabsorbed by the company\'s other products.'},
      {'h4': '(b)  The effect of the N56,000 legislation cost'},
      {'p': 'The N56,000 is a **future, incremental** cost that arises **only if the company '
            'continues to manufacture**, so it is now relevant. It is a fixed amount, so the '
            'advice becomes dependent on **volume**: making saves N16 per unit but costs an '
            'extra N56,000 a year.'},
      {'tex': '\\text{Indifference volume} = \\frac{N56{,}000}{N16} = 3{,}500 '
              '\\text{ units per annum}'},
      {'stmt': {'t': 'The revised advice', 'rows': [
        ['Annual requirement **more than** 3,500 units', '',
         '**Continue to manufacture** — the per-unit saving outweighs the N56,000'],
        ['Annual requirement **exactly** 3,500 units', '',
         'Indifferent on cost grounds — decide on other factors'],
        ['Annual requirement **less than** 3,500 units', '',
         '**Buy from Ball Limited** — the N56,000 is not recovered'],
      ]}},
      {'note': 'Check at, say, 5,000 units: making saves $5{,}000 \\times 16 = N80{,}000$ '
               'against buying, less the N56,000 of inspection cost, a net saving of N24,000 — '
               'so make. At 2,000 units: saving $2{,}000 \\times 16 = N32{,}000$ against a '
               'N56,000 cost, a net extra cost of N24,000 — so buy.'},
      {'h4': '(c)  Reply to the production director'},
      {'p': '**MEMORANDUM** — To: The Production Director. From: The Cost Accountant. '
            'Subject: The grinding equipment and the make-or-buy decision.'},
      {'p': 'Thank you for your note. I am afraid the written-down value of the grinding '
            'equipment is **not a reason to continue manufacturing**, for the following '
            'reasons.'},
      {'ol': [
        'The N100,000 was spent a year ago. It is a **sunk cost** — a past cost that no decision '
        'taken now can alter. Whether we make the component or buy it, that money has gone.',
        'The equipment **cannot be resold or used elsewhere**, so it has **no disposal value and '
        'no opportunity cost**. Keeping it in use therefore costs us nothing and gains us '
        'nothing; it is simply irrelevant to the choice.',
        'The N80,000 written-down value will be **charged against profit either way**. If we '
        'continue, it is charged gradually as depreciation; if we stop, it is charged at once as '
        'a write-off. The **total** charged is the same N80,000 in both cases, so it cannot '
        'favour one option over the other. Only the *timing* differs, and the timing of a '
        'non-cash book entry is not a commercial reason to continue production.',
        'Continuing to manufacture an uneconomic component merely to avoid admitting a past '
        'investment error is the classic **"throwing good money after bad"** fallacy. The '
        'correct question is always: *given where we are now, which future course of action '
        'costs us least?*',
      ]},
      {'p': 'The decision should therefore rest only on **future, incremental cash flows** — the '
            'N34 variable cost of making against Ball Limited\'s N50, together with the N56,000 '
            'of new inspection costs and our expected annual volume. On those figures we should '
            'continue to manufacture provided we need more than 3,500 units a year, and the '
            'grinding equipment has nothing to do with it.'},
      {'p': 'I would, of course, be glad to discuss this with you before the budget meeting.'}]}},

    {'eg': {'tag': 'Exam type — Q5',
      't': 'Koki Limited — make or buy part M-6, with an opportunity cost',
      'q': [
      {'p': 'Koki Limited, which manufactures part M-6 for use in its production cycle, has the '
            'following costs per unit for production of **25,000 units**:'},
      {'stmt': {'t': 'Cost per unit (N)', 'rows': [
        ['Direct materials', '', 5],
        ['Direct labour', '', 20],
        ['Manufacturing overhead', '', 24],
        ['**Total**', '', 49, '@tt'],
      ]}},
      {'p': '**66⅔% of the overhead is fixed.** Sahara Limited has offered to sell 25,000 units '
            'of part M-6 to Koki for **N45 per unit**. If Koki accepts, some of the facilities '
            'presently used to manufacture M-6 could be **rented to a third party at an annual '
            'rent of N65,000**. Additionally, **N6 per unit of the fixed overhead costs applied '
            'to part M-6 would be totally eliminated**.'},
      {'p': '**Required:** **(a)** advise the managing director whether he should accept '
            'Sahara\'s offer. **(b)** State factors other than the relevant costs which would '
            'influence your decision.'}],
      'a': [
      {'h4': 'Step 1 — split the overhead'},
      {'stmt': {'t': 'Analysis of the N24 manufacturing overhead per unit', 'rows': [
        ['Fixed:  66⅔% × N24', '', 'N16'],
        ['Variable:  33⅓% × N24', '', 'N8'],
      ]}},
      {'p': 'Of the N16 of fixed overhead per unit, only **N6** would be eliminated by ceasing '
            'production. The remaining **N10** would continue regardless and is therefore '
            'irrelevant.'},
      {'h4': '(a)  The relevant cost comparison'},
      {'stmt': {'t': 'Make or buy 25,000 units of part M-6 (N)', 'rows': [
        ['', 'Per unit', 'Total (25,000 units)', '@hd'],
        ['**Cost of MAKING — relevant costs**', '', '', '@hd'],
        ['Direct materials', 5, 125000],
        ['Direct labour', 20, 500000],
        ['Variable manufacturing overhead', 8, 200000],
        ['Avoidable fixed overhead', 6, 150000],
        ['**Relevant cost of making**', 39, 975000, '@t'],
        ['Add: opportunity cost — rental income forgone by continuing to make', '', 65000],
        ['**Total relevant cost of making**', '', 1040000, '@t'],
        '@gap',
        ['**Cost of BUYING**', '', '', '@hd'],
        ['Purchase price:  25,000 × N45', 45, 1125000],
        '@gap',
        ['**Extra cost of buying**', '', 85000, '@tt'],
      ]}},
      {'p': '**Advice: reject Sahara\'s offer and continue to manufacture part M-6.** Buying '
            'would cost the company **N85,000 a year more**, even after allowing for the N65,000 '
            'of rental income and the N150,000 of fixed overhead that would be saved.'},
      {'note': 'Note the two refinements that distinguish a good answer. **(1) The opportunity '
               'cost.** The N65,000 rent is not a cost of buying — it is income the company '
               'gives up by **continuing to make**, and so is added to the cost of making. '
               '(Deducting it from the cost of buying gives exactly the same N85,000 answer; '
               'what matters is that it appears once, on the correct side.) **(2) The partial '
               'fixed-cost saving.** Only N6 of the N16 fixed overhead per unit is avoidable; '
               'treating the whole N16 as avoidable would make buying appear N165,000 cheaper '
               'and reverse the decision.'},
      {'h4': '(b)  Other factors influencing the decision'},
      {'ol': [
        '**Quality and reliability** of Sahara\'s product, and whether it meets Koki\'s own '
        'specification.',
        '**Security and continuity of supply** — the risk of late delivery or of Sahara ceasing '
        'to supply, which would halt Koki\'s own production cycle.',
        '**How long the N45 price is guaranteed**, and what happens when the guarantee expires. '
        'A supplier can raise prices once the buyer has dismantled its own capacity.',
        '**Loss of in-house expertise and capacity**, which would be costly and slow to rebuild '
        'if the company later wished to resume production.',
        '**Reliability of the N65,000 rental** — is there an actual tenant, for how long, and '
        'does the lease tie up facilities Koki might need?',
        '**Effect on employees** — redundancies, morale, industrial relations and the cost of '
        'any redundancy payments (which would themselves be a relevant cost).',
        '**Confidentiality** — whether sharing the design with an outside supplier risks losing '
        'a competitive advantage.',
        '**Flexibility** — the ability to vary volume, specification or delivery at short notice '
        'is usually greater in-house.',
        '**Sahara\'s financial stability** and the risk of dependence on a single supplier.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q6',
      't': 'Aminu Motors — make or buy where the released capacity stays idle',
      'q': [
      {'p': 'Aminu Motors Limited specialises in the manufacture of sports cars, making some of '
            'the components it requires and buying others. Alparts Limited offers to supply a '
            'component currently made by Aminu Motors at a price of **N7**. The costs incurred '
            'by Aminu Motors in making the part are:'},
      {'stmt': {'t': 'Cost per unit (N)', 'rows': [
        ['Variable costs', '', 4],
        ['Traceable fixed costs', '', 2],
        ['Allocated fixed costs', '', 3],
        ['**Total**', '', 9, '@tt'],
      ]}},
      {'p': 'Monthly output is **5,000 units**. **Required:** present information to management '
            'on the assumption that the production capacity released as a result of accepting '
            'the offer will remain idle.'}],
      'a': [
      {'h4': 'The key distinction — traceable versus allocated fixed costs'},
      {'table': {'align': 'll', 'head': ['Traceable fixed costs (N2 per unit)',
        'Allocated fixed costs (N3 per unit)'], 'rows': [
        ['Fixed costs incurred **specifically because this component is made** — the supervisor '
         'of that section, the depreciation and insurance of the dedicated machine, its '
         'maintenance contract.',
         'A share of **general factory fixed overhead** apportioned to the component — factory '
         'rent, the works manager\'s salary, general rates.'],
        ['**Avoidable**: they would cease if production of the component ceased.',
         '**Unavoidable**: they continue regardless and would simply be reapportioned to the '
         'company\'s other products.'],
        ['**RELEVANT** to the decision.', '**IRRELEVANT** to the decision.'],
      ]}},
      {'h4': 'Statement of relevant costs for management'},
      {'stmt': {'t': 'Make or buy 5,000 components per month (N)', 'rows': [
        ['', 'Make', 'Buy', '@hd'],
        ['Variable costs:  5,000 × N4', 20000, '—'],
        ['Traceable (avoidable) fixed costs:  5,000 × N2', 10000, '—'],
        ['Purchase price:  5,000 × N7', '—', 35000],
        ['**Relevant cost per month**', 30000, 35000, '@t'],
        '@gap',
        ['*Allocated fixed costs, incurred either way:  5,000 × N3*', 15000, 15000],
        ['**Total cost to the company per month**', 45000, 50000, '@tt'],
      ]}},
      {'stmt': {'t': 'Summary', 'rows': [
        ['Saving from continuing to make, per unit  (N7 − N6)', '', 'N1.00'],
        ['Saving per month  (5,000 units × N1)', '', 'N5,000'],
        ['**Saving per annum**', '', 'N60,000', '@tt'],
      ]}},
      {'p': '**Recommendation: reject Alparts\' offer and continue to make the component.** The '
            'relevant cost of making is **N6** per unit (variable N4 plus traceable fixed N2) '
            'against a purchase price of **N7** — a saving of N1 per unit, N5,000 a month, '
            'N60,000 a year.'},
      {'key': 'The N9 full cost makes the offer look attractive: N7 appears to be a saving of N2 '
              'a unit, N10,000 a month. It is not, because **N3 of that N9 does not go away**. '
              'If the component were bought in, the N15,000 a month of allocated fixed cost '
              'would be reapportioned onto the sports cars themselves, making *them* look N3 '
              'per component dearer — and the company N5,000 a month worse off. Buying on full '
              'cost rather than relevant cost is the single commonest error in make-or-buy '
              'decisions.'},
      {'note': 'The question\'s assumption that the released capacity **remains idle** is what '
               'makes the answer clean. If the capacity could instead be used to make something '
               'else, the contribution from that alternative use would be an **opportunity '
               'cost** of continuing to make the component, and would have to be added to the '
               '"make" column — if it exceeded N5,000 a month, the decision would reverse.'}]}},

    {'eg': {'tag': 'Exam type — Q7',
      't': 'The benefits and pitfalls of marginal costing',
      'q': [
      {'p': '**(a)** What benefits are to be gained from marginal costing? Are there any '
            'pitfalls in the application of marginal costs? Discuss these matters critically.'},
      {'p': '**(b)** Give a brief account of a practical application of marginal costing which '
            'you consider sound from a policy viewpoint.'}],
      'a': [
      {'h4': '(a)  The benefits of marginal costing'},
      {'ol': [
        '**It isolates contribution**, which is the figure that actually changes when volume '
        'changes — so the effect of any change in output, price or mix on profit can be seen '
        'immediately.',
        '**It avoids the arbitrariness of overhead apportionment.** Fixed cost is written off in '
        'full against the period, so no product is made to look profitable or unprofitable by '
        'an apportionment convention.',
        '**Profit moves with sales, not with production.** Under absorption costing, profit can '
        'be increased simply by producing for inventory; under marginal costing it cannot, which '
        'removes a perverse incentive and makes period-to-period comparison meaningful.',
        '**It is the right basis for short-run decisions** — accept or reject a special order, '
        'make or buy, drop a product, choose between products under a limiting factor, set a '
        'minimum price.',
        '**It underpins cost-volume-profit and break-even analysis** (Chapter 10) and the '
        'flexible budget (Chapter 12).',
        '**It is simpler to operate** — no absorption rates, no under/over absorption to '
        'explain, and inventory valuation needs no overhead allocation.',
        '**It assists cost control**, because fixed costs are shown as period costs where '
        'responsibility for them lies, rather than buried in unit costs.',
      ]},
      {'h4': '(a)  The pitfalls — a critical view'},
      {'ol': [
        '**The fixed/variable split is not clean.** Many costs are semi-variable and must be '
        'separated by approximation (the high-low method of §2.1.2a), and some are stepped. The '
        'whole technique rests on a division that is itself an estimate.',
        '**Linearity is assumed.** Variable cost per unit and selling price per unit are taken '
        'as constant, which holds only within the relevant range — bulk discounts, overtime '
        'premiums and price concessions all break it.',
        '**It can encourage under-pricing.** A price that covers marginal cost and makes some '
        'contribution is better than nothing *in the short run and for marginal business*. If '
        'it becomes the normal basis of pricing, total contribution will not cover fixed costs '
        'and the business makes a loss while every individual sale appears "profitable".',
        '**Fixed costs are not ignorable in the long run.** All costs are variable over a long '
        'enough period, and every product must eventually cover its share of them.',
        '**It is not permitted for external reporting.** IAS 2 requires inventory to include '
        'production overhead, so absorption costing must be used for the published accounts and '
        'a reconciliation maintained.',
        '**It understates inventory**, which may matter for loan covenants, insurance and the '
        'reported financial position.',
        '**It is less appropriate where fixed costs dominate.** In a capital-intensive business, '
        'contribution is nearly the whole selling price, and decisions based on it carry very '
        'little information about whether the business is viable.',
        '**It takes no account of the capacity consumed**, unless the limiting-factor technique '
        'is applied as well.',
      ]},
      {'h4': '(b)  A practical application sound from a policy viewpoint'},
      {'p': '**Accepting a special export order at below the normal selling price**, where there '
            'is spare capacity.'},
      {'p': 'Suppose a company with a normal selling price of N100 and a full cost of N85 '
            '(variable N60, fixed N25) is offered an export contract at N70 per unit, using '
            'capacity that would otherwise stand idle. On a full-cost view the order shows a '
            'loss of N15 a unit and would be refused. On a marginal-cost view it earns a '
            '**contribution of N10 a unit**, every naira of which goes towards fixed costs that '
            'are being incurred anyway — so the order increases profit and should be accepted.'},
      {'p': 'This is sound **as a policy** provided four conditions hold, and it is the '
            'conditions that make it sound rather than the arithmetic:'},
      {'ol': [
        'there is genuinely **spare capacity**, so no existing business is displaced (otherwise '
        'the contribution forgone is an opportunity cost);',
        'the special price **will not leak into the normal market** and undermine the N100 '
        'price — hence an *export* order to a separate market;',
        'the order is **marginal and occasional**, not a substitute for normally-priced '
        'business; and',
        '**no additional fixed costs** are incurred to fulfil it.',
      ]},
      {'p': 'Other equally defensible applications: setting a **minimum tender price** when '
            'bidding for work in a slack period; deciding whether to **close a department '
            'temporarily** (comparing the contribution forgone with the fixed costs saved); and '
            'choosing the **best product mix** when a scarce resource limits output, by ranking '
            'on contribution per unit of the limiting factor.'}]}},

    {'eg': {'tag': 'Exam type — Q8 (ICAN Intermediate, November 1999)',
      't': 'Tapgun Industries — marginal and absorption operating statements for two months',
      'q': [
      {'p': 'Tapgun Industries Limited manufactures paints in 4-litre cans. The selling price of '
            'the product is **N280**, with a standard cost of **N180** made up as follows:'},
      {'stmt': {'t': 'Standard cost per can (N)', 'rows': [
        ['Direct materials', '', 100],
        ['Direct labour', '', 20],
        ['Variable overheads', '', 30],
        ['Fixed overhead', '', 30],
        ['**Standard cost**', '', 180, '@tt'],
      ]}},
      {'p': 'In April and May 1999 the company\'s production and sales reports were:'},
      {'stmt': {'t': 'Production and sales (cans)', 'rows': [
        ['', 'April', 'May', '@hd'],
        ['Production', 10000, 10000],
        ['Sales', 8000, 12000],
      ]}},
      {'p': '**Required:** **(a)** prepare the company\'s operating statements for the two '
            'months using (i) the marginal costing technique and (ii) the absorption costing '
            'technique. **(b)** Comment on the results of the two techniques, with particular '
            'reference to the difference in inventory valuation and in operating profit.'}],
      'a': [
      {'h4': 'Working — the unit costs and the fixed overhead'},
      {'stmt': {'t': 'Workings', 'rows': [
        ['Marginal (variable) cost per can  (100 + 20 + 30)', '', 'N150'],
        ['Fixed overhead absorbed per can', '', 'N30'],
        ['Full (absorption) cost per can', '', 'N180'],
        ['Normal activity implied  (production in each month)', '', '10,000 cans'],
        ['**Fixed overhead per month  (10,000 × N30)**', '', 'N300,000'],
        '@gap',
        ['Opening inventory, April', '', 'nil'],
        ['Closing inventory, April  (10,000 − 8,000)', '', '2,000 cans'],
        ['Closing inventory, May  (2,000 + 10,000 − 12,000)', '', 'nil'],
      ]}},
      {'h4': '(a)(i)  Marginal costing operating statements'},
      {'stmt': {'t': 'Operating statement — marginal costing (N)', 'rows': [
        ['', 'April', 'May', '@hd'],
        ['Sales  (8,000 × N280;  12,000 × N280)', 2240000, 3360000],
        '@gap',
        ['Opening inventory at marginal cost  (nil;  2,000 × N150)', 0, 300000],
        ['Variable cost of production  (10,000 × N150)', 1500000, 1500000],
        ['Less: closing inventory at marginal cost  (2,000 × N150;  nil)', -300000, 0],
        ['**Variable cost of sales**', 1200000, 1800000, '@t'],
        ['**Contribution**', 1040000, 1560000, '@t'],
        ['Less: fixed overhead (period cost, written off in full)', 300000, 300000],
        ['**Operating profit — marginal costing**', 740000, 1260000, '@tt'],
      ]}},
      {'h4': '(a)(ii)  Absorption costing operating statements'},
      {'stmt': {'t': 'Operating statement — absorption costing (N)', 'rows': [
        ['', 'April', 'May', '@hd'],
        ['Sales', 2240000, 3360000],
        '@gap',
        ['Opening inventory at full cost  (nil;  2,000 × N180)', 0, 360000],
        ['Full cost of production  (10,000 × N180)', 1800000, 1800000],
        ['Less: closing inventory at full cost  (2,000 × N180;  nil)', -360000, 0],
        ['**Cost of sales**', 1440000, 2160000, '@t'],
        ['**Gross profit**', 800000, 1200000, '@t'],
        ['Under / (over) absorbed fixed overhead  *(production = 10,000 = normal, so nil)*', 0,
         0],
        ['**Operating profit — absorption costing**', 800000, 1200000, '@tt'],
      ]}},
      {'h4': '(b)  Comment on the results'},
      {'stmt': {'t': 'The two techniques compared (N)', 'rows': [
        ['', 'April', 'May', 'Two months', '@hd'],
        ['**Closing inventory — marginal costing (2,000 × N150)**', 300000, 0, ''],
        ['**Closing inventory — absorption costing (2,000 × N180)**', 360000, 0, ''],
        ['Difference in inventory valuation', 60000, 0, ''],
        '@gap',
        ['**Operating profit — marginal costing**', 740000, 1260000, 2000000],
        ['**Operating profit — absorption costing**', 800000, 1200000, 2000000],
        ['Difference in profit', 60000, -60000, 0],
      ]}},
      {'h4': 'Reconciliation'},
      {'stmt': {'t': 'Reconciliation of the two profits (N)', 'rows': [
        ['', 'April', 'May', '@hd'],
        ['Profit — marginal costing', 740000, 1260000],
        ['Add / (less): fixed overhead in the increase / (decrease) in inventory',
         '+60,000', '−60,000'],
        ['   *(2,000 cans × N30 fixed overhead per can)*', '', ''],
        ['**Profit — absorption costing**', 800000, 1200000, '@tt'],
      ]}},
      {'p': '**Inventory valuation.** Marginal costing values the 2,000 cans of April closing '
            'inventory at the variable cost of N150, i.e. **N300,000**; absorption costing adds '
            'the N30 of fixed overhead per can and values them at N180, i.e. **N360,000**. The '
            'difference of **N60,000** is precisely the fixed overhead attached to those 2,000 '
            'cans. Absorption costing therefore reports a higher current asset figure.'},
      {'p': '**Operating profit.** In **April, production (10,000) exceeded sales (8,000)**, so '
            'inventory rose by 2,000 cans and absorption costing **carried N60,000 of April\'s '
            'fixed overhead forward** into inventory instead of charging it against April\'s '
            'sales — hence absorption profit is N60,000 higher. In **May, sales (12,000) '
            'exceeded production (10,000)**, inventory fell to nil, and that same N60,000 was '
            '**released** into May\'s cost of sales — hence absorption profit is N60,000 '
            '*lower* than marginal profit.'},
      {'key': 'Over the **two months together both techniques report exactly N2,000,000**. '
              'Neither method creates or destroys profit; they differ only in **when** fixed '
              'overhead is charged. The rule is worth memorising: when **production exceeds '
              'sales**, absorption profit is higher; when **sales exceed production**, marginal '
              'profit is higher; when they are equal, the two are the same. The difference is '
              'always the change in inventory **units** multiplied by the **fixed overhead per '
              'unit**.'},
      {'warn': 'This is also the strongest practical argument against absorption costing for '
               'internal reporting. In April the company sold 8,000 cans and reported the '
               '**higher** profit; in May it sold 12,000 — half as many again — and reported '
               'the **lower** one. A manager judged on absorption profit is being rewarded for '
               'producing, not for selling.'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'Contribution', 'tex': 'S - V = C', 'nt': 'S = Sales, V = Variable costs.'},
  {'lb': 'Profit', 'tex': 'C - FC = P', 'nt': 'FC = Fixed costs.'},
  {'lb': 'Sales at break-even point', 'tex': '\\dfrac{FC \\times S}{S - V}'},
  {'lb': 'Units needed for a target contribution', 'tex': '\\dfrac{\\text{Required total '
   'contribution}}{\\text{Contribution per unit}}'},
 ],
 'focus':
   'Marginal costing is tested constantly, both as a standalone topic and as the engine behind '
   'CVP analysis (Chapter 10). Learn $S-V=C$, $C-FC=P$ as one interchangeable pair, not two '
   'separate facts — almost every numeric question here is that equation solved for a different '
   'unknown. For decision questions (make-or-buy, special order), the discipline that matters '
   'most is *including only relevant costs* — strip out sunk costs and apportioned fixed costs '
   'that will not actually change before comparing the alternatives.',
 'errors': [
   'Apportioning fixed cost to a "loss-making" department or product and concluding it should '
   'be dropped, without first checking its actual contribution (Illustration 9.2\'s whole point).',
   'Including a sunk cost (money already spent, unaffected by the decision) in a make-or-buy or '
   'special-order comparison.',
   'Valuing closing inventory at total cost per unit under marginal costing — it should be '
   'valued at variable cost per unit only.',
   'Treating a fixed salary as a relevant cost in a decision, rather than only its opportunity '
   'cost if redirected elsewhere.',
   'Accepting a special order below normal price without checking that spare capacity actually '
   'exists — with no spare capacity, the order would displace full-price sales instead.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Sales are N500,000 and variable costs are N320,000. Contribution is',
    'o': ['N820,000', 'N180,000', 'N320,000', 'N500,000', 'N140,000'],
    'a': 1,
    'w': 'Contribution = Sales − Variable costs = 500,000 − 320,000 = N180,000.',
    'calc': '500{,}000 - 320{,}000 = 180{,}000',
    'src': 'Chapter 9.1', 'sec': '9.1'},
   {'q': 'Contribution is N180,000 and fixed costs are N120,000. Profit is',
    'o': ['N300,000', 'N60,000', 'N180,000', 'N120,000', 'N42,000'],
    'a': 1,
    'w': 'Profit = Contribution − Fixed costs = 180,000 − 120,000 = N60,000.',
    'calc': '180{,}000 - 120{,}000 = 60{,}000',
    'src': 'Chapter 9.1', 'sec': '9.1'},
   {'q': 'Under absorption costing, closing inventory is valued at',
    'o': ['variable cost per unit only', 'total (fixed + variable) cost per unit',
          'selling price per unit', 'prime cost per unit only', 'zero — never valued'],
    'a': 1,
    'w': 'Absorption costing includes a share of fixed overhead in every unit\'s cost, so '
         'closing inventory is valued at total cost per unit, not variable cost alone.',
    'src': 'Chapter 9.1', 'sec': '9.1'},
   {'q': 'A company has spare capacity and receives a special order at a price below its normal '
         'selling price, but still above marginal cost per unit. Based purely on this '
         'information, the company should generally',
    'o': ['reject the order automatically', 'accept the order, since it adds to contribution '
          'and profit', 'raise the normal selling price instead',
          'accept only if it equals the normal price', 'shut down production entirely'],
    'a': 1,
    'w': 'With spare capacity and a price above marginal cost, the order adds positive '
         'contribution without displacing existing sales — accepting it increases profit.',
    'src': 'Chapter 9.4', 'sec': '9.4'},
   {'q': 'A cost that has already been irreversibly incurred, and so cannot be relevant to a '
         'current decision, is called a',
    'o': ['relevant cost', 'opportunity cost', 'sunk cost', 'notional cost',
          'differential cost'],
    'a': 2,
    'w': 'A sunk cost is, by definition, irrecoverable and irrelevant to any decision being made '
         'now.',
    'src': 'Chapter 9.3', 'sec': '9.3'},
   {'q': 'Material already sitting in store, with no market value and no alternative use, has a '
         'relevant cost of',
    'o': ['its original purchase price', 'its replacement cost', 'NIL', 'its insured value',
          'double its purchase price'],
    'a': 2,
    'w': 'With no market value or alternative use, the material\'s relevant cost for a new '
         'decision is NIL — its original cost is sunk.',
    'src': 'Chapter 9.3', 'sec': '9.3'},
   {'q': 'In a make-or-buy decision, a component should generally be BOUGHT rather than made '
         'in-house when',
    'o': ['the supplier\'s price exceeds the variable cost of making it',
          'the total variable cost of making it in-house exceeds the supplier\'s quotation',
          'the company has no spare capacity at all', 'fixed costs cannot be avoided either way',
          'the component is used in only one product'],
    'a': 1,
    'w': 'Buying is favoured once the variable cost of making the component exceeds the outside '
         'supplier\'s price (adjusted for any fixed-cost savings from buying).',
    'src': 'Chapter 9.4', 'sec': '9.4'},
   {'q': 'A worker earns a fixed monthly salary regardless of what task they are assigned. In a '
         'short-term decision, the relevant cost associated with using this worker on a new '
         'project is',
    'o': ['their full fixed salary', 'zero, since salary is paid either way',
          'the opportunity cost of what they would otherwise have been doing',
          'double their salary', 'their salary plus a notional profit margin'],
    'a': 2,
    'w': 'A fixed salary is irrelevant on its own (it is paid regardless); what is relevant is '
         'the opportunity cost of diverting that worker\'s time from whatever else they would '
         'otherwise be doing.',
    'src': 'Chapter 9.3', 'sec': '9.3'},
   {'q': 'A firm currently earns a profit of N40,000 with fixed costs of N60,000. If it cuts '
         'price so contribution per unit falls, but wants to hold profit at N40,000, it must',
    'o': ['sell fewer units than before', 'sell the same number of units as before',
          'sell more units than before, to make up total contribution',
          'accept a lower profit automatically', 'increase fixed costs'],
    'a': 2,
    'w': 'With a lower contribution per unit but the same required total contribution '
         '(profit + fixed costs = 100,000), more units must be sold to reach that same total.',
    'src': 'Chapter 9.4', 'sec': '9.4'},
   {'q': 'Which of the following is explicitly listed as a limitation of marginal costing?',
    'o': ['It is difficult to apply in capital-intensive industries with very large fixed costs',
          'It cannot be used for any short-term decision', 'It ignores variable costs entirely',
          'It always overstates profit compared with absorption costing',
          'It cannot be combined with break-even analysis'],
    'a': 0,
    'w': 'Marginal costing has limited scope in capital-intensive industries, where fixed costs '
         'dominate and the fixed/variable distinction matters less for decisions.',
    'src': 'Chapter 9.1', 'sec': '9.1'},
  ],
  'theory': [
   {'q': 'Explain the three fundamental differences between absorption costing and marginal '
         'costing as shown in their respective income statements.',
    'marks': 9,
    'a': [
      {'p': '**(1) Treatment of fixed production overhead** — absorption costing includes it '
            'in cost of goods sold; marginal costing treats it as a period cost, charged in '
            'full regardless of production level.'},
      {'p': '**(2) Valuation of closing inventory** — absorption costing values it at total '
            '(fixed + variable) cost per unit; marginal costing values it at variable cost per '
            'unit only, since fixed costs are assumed already covered by contribution.'},
      {'p': '**(3) The first profit line shown** — absorption costing\'s income statement shows '
            'gross profit first; marginal costing\'s shows contribution margin (sales less '
            'total variable cost) first. Except where production exactly equals sales in the '
            'period, the two methods will show different profit at this first stage.'},
    ], 'src': 'Chapter 9.1', 'sec': '9.1'},
   {'q': 'What benefits are gained from marginal costing? Are there any pitfalls in its '
         'application? Discuss critically.',
    'marks': 12,
    'a': [
      {'p': '**Benefits**: constant cost per unit regardless of volume; facilitates cost '
            'control via flexible budgeting; removes the complications of fixed-overhead '
            'allocation/apportionment/absorption entirely; gives a clearer, more logical basis '
            'for pricing and tendering; aids profit planning by showing cost-volume-profit '
            'relationships directly; and gives a more realistic, uniform valuation of '
            'inventory (at marginal cost, not an arbitrary total-cost figure).'},
      {'p': '**Pitfalls**: splitting overheads into fixed and variable components is genuinely '
            'difficult in practice; the technique can over-emphasise the selling function at '
            'the expense of production efficiency; it is poorly suited to industries with '
            'large WIP inventories, or that are capital-intensive with very large fixed costs; '
            'and selling price cannot reasonably be set on contribution alone without regard '
            'to whether fixed costs are ultimately covered.'},
    ], 'src': 'Chapter 9.1', 'sec': '9.1'},
  ]},
}
