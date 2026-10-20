CH = {
 'n': 10,
 't': 'Cost-Volume-Profit Analysis',
 'brief': 'How total cost, total revenue and profit move together as sales volume changes: '
          'break-even point by the equation and contribution-margin techniques, the Profit/'
          'Volume (P/V) ratio, margin of safety, the break-even chart and P/V graph, and the '
          'assumptions and limitations underlying the whole technique — all built on marginal '
          'costing (Chapter 9).',
 'outcomes': [
   'Explain the meaning and importance of CVP analysis',
   'Explain break-even analysis and compute the Break-Even Point, and the P/V ratio',
   'Explain margin of safety and use a formula to determine it',
   'Present a graphical approach for CVP analysis',
 ],
 'secs': [
  {'n': '10.1', 't': 'Cost-Volume-Profit analysis', 'b': [
    {'def': {'t': 'Cost-Volume-Profit (CVP) analysis', 'd': 'the analysis of how total costs, '
                  'total revenues and total profits relate to sales volume — used to predict the '
                  'effect of changes in cost and sales volume on profit, and to guide decisions '
                  'on starting, expanding or diversifying production.'}},
    {'p': 'Questions CVP analysis answers: what would production cost under different '
          'circumstances? What volume of production is needed? How many units of each product '
          'must be made for a target profit? What is the gap between selling price and '
          'production cost? What is the effect of a percentage change in cost on volume and '
          'profit?'},
    {'p': 'Used well, CVP helps with: the budgeting process (the sales volume needed for profit, '
          'and the budget\'s "safety margin"); pricing and sales-volume decisions; sales-mix '
          'decisions (what proportion of each product to sell); and decisions on cost structure '
          'and production capacity.'},
    {'note': 'CVP analysis is the **broad** concept; its narrower, more specific form is '
             '**break-even analysis**.'},
  ]},

  {'n': '10.2', 't': 'Break-even analysis', 'b': [
    {'def': {'t': 'Break-Even Point (BEP)', 'd': 'the level of production activity at which '
                  'there is neither profit nor loss — total cost equals total revenue.'}},
    {'tex': '\\text{At BEP:} \\quad TC = TR \\quad \\text{i.e.} \\quad TR - TC = 0'},
    {'note': 'After BEP, no *further* fixed cost needs recovering — every additional unit\'s '
             'contribution flows straight to profit, limited only by its variable cost.'},

    {'h4': 'Assumptions of break-even analysis'},
    {'p': 'Break-even and CVP analysis rest on assumptions rarely fully true in practice — a '
          'change in any one of them shifts the break-even point, so results must always be '
          'read with these limitations in mind:'},
    {'ul': [
      'cost variability behaves predictably;',
      'costs can genuinely be split into fixed and variable components;',
      'total fixed costs stay constant across the relevant range;',
      'variable cost per unit is strictly proportional to volume;',
      'selling price does not change as volume changes;',
      'there is only one product, or (with several) the sales mix stays constant;',
      'the general price level does not change;',
      'productivity per worker stays roughly unchanged;',
      'production and sales are synchronised — no inventory build-up;',
      'revenue and cost are compared against a common activity base (e.g. sales value or units '
      'produced); and',
      'plant efficiency can be predicted.',
    ]},

    {'h4': 'Computing the break-even point'},
    {'p': 'Two popular mathematical approaches:'},
    {'table': {'align': 'll', 'head': ['Technique', 'How it works'], 'rows': [
      ['**(i) Equation technique**', 'Sales = Variable expenses + Fixed expenses + Profit '
       '(i.e. $TR = TC + \\text{Profit}$), solved for the unknown — usually the number of units, '
       'with profit set to zero at BEP.'],
      ['**(ii) Contribution margin technique**', 'Unit contribution = unit selling price − unit '
       'variable cost; BEP (units) = Fixed expenses ÷ unit contribution.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Illustration 10.1 — both techniques on the same problem',
      'open': True, 'q': [
      {'p': 'Alhaji Gazali sells toy rockets at a trade fair, buying at N5 each (unsold rockets '
            'returnable), selling at N9 each; booth rent (fixed) N2,000. Find (a) the '
            'break-even quantity, and (b) the quantity needed for a 20% operating margin on '
            'sales.'}],
      'a': [
      {'h4': '(a) Equation technique'},
      {'p': 'Let $A$ = units to break even: $9A = 5A + 2{,}000 + 0$.'},
      {'tex': '4A = 2{,}000 \\implies A = 500\\text{ units}'},
      {'h4': '(a) Contribution margin technique — same answer'},
      {'p': 'Unit contribution $= 9 - 5 = N4$.'},
      {'tex': '\\text{BEP} = \\dfrac{2{,}000}{4} = 500\\text{ units}'},
      {'h4': '(b) 20% operating margin'},
      {'p': 'Let $X$ = units needed: $9X = 5X + 2{,}000 + 0.2(9X)$.'},
      {'tex': '9X - 1.8X - 5X = 2{,}000 \\implies 2.2X = 2{,}000 \\implies X \\approx '
              '909.1 \\approx 910\\text{ units}'}]}},

    {'h4': 'Other CVP formulae'},
    {'fbox': {'h': 'CVP formulae', 'rows': [
      {'lb': 'Break-even point, in money terms', 'tex': '\\text{BEP}_{N} = \\dfrac{\\text{Fixed '
        'Cost}}{\\text{C/S Ratio (P/V Ratio)}}'},
      {'lb': 'C/S (Profit-Volume) ratio', 'tex': '\\dfrac{\\text{Contribution per unit}}'
        '{\\text{Sales price per unit}} \\times 100'},
      {'lb': 'Sales for a target profit, in units', 'tex': '\\dfrac{\\text{Fixed Costs} + '
        '\\text{Target Profit}}{\\text{Contribution per unit}}'},
      {'lb': 'Sales for a target profit, in money terms', 'tex': '\\dfrac{\\text{Fixed Costs} + '
        '\\text{Target Profit}}{\\text{C/S Ratio (P/V Ratio)}}'},
      {'lb': 'Sales for a target AFTER-TAX profit, in units', 'tex': '\\dfrac{\\text{Fixed '
        'Costs} + \\dfrac{\\text{Target after-tax profit}}{1 - \\text{tax rate}}}{\\text{'
        'Contribution per unit}}'},
      {'lb': 'Break-even point, multi-product firm', 'tex': '\\dfrac{\\text{Total Fixed Cost, '
        'all products}}{\\text{Weighted C/S Ratio}}', 'nt': 'Weighted C/S ratio = total '
        'contribution of all products ÷ total sales revenue of all products.'},
    ]}},
    {'warn': 'For a target **after-tax** profit, the tax adjustment divides the after-tax '
             'target **up** to its before-tax equivalent — $\\text{before-tax profit} = '
             '\\text{after-tax profit} / (1-\\text{tax rate})$ — never multiplied by $(1-\\text{'
             'tax rate})$, which would move the number the wrong way. (Illustration 10.2(c) '
             'below applies this correctly even though its own printed working shows the '
             'operation the wrong way round; the numeric answer it reaches only follows from '
             'dividing, not multiplying — a source transcription slip in the formula display, '
             'not in the arithmetic.)'},
    {'note': 'The single-product formulae above apply equally to a firm with a genuinely '
             '**constant** sales mix across several products — only a firm whose mix actually '
             'varies needs the weighted multi-product version.'},

    {'h4': 'The Profit-Volume (P/V) ratio'},
    {'def': {'t': 'Profit-Volume (P/V) ratio / Contribution Margin Ratio (CMR)', 'd': 'the '
                  'relationship between contribution and sales revenue — a measure of a '
                  'product\'s profitability.'}},
    {'fbox': {'h': 'Three equivalent ways to compute the P/V ratio', 'rows': [
      {'lb': '(1) Per unit', 'tex': '\\dfrac{S - V}{S}', 'nt': 'S = unit selling price, '
       'V = unit variable cost.'},
      {'lb': '(2) In total', 'tex': '\\dfrac{TSR - TVC}{TSR}', 'nt': 'TSR = total sales '
       'revenue, TVC = total variable cost.'},
      {'lb': '(3) From fixed cost and profit', 'tex': '\\dfrac{FC + \\text{Profit}}'
       '{\\text{Total Sales}}'},
    ]}},

    {'eg': {'tag': 'Study text', 't': 'Illustration 10.2 — BEP, P/V ratio and margin of safety, '
      'worked through eight related questions', 'open': True, 'q': [
      {'p': 'Time Dey Nigeria Ltd sells a single product at N20/unit. Last year: sales N800,000; '
            'direct materials N120,000; direct wages N160,000; variable production overhead '
            'N80,000; fixed production overhead N100,000; fixed admin. overhead N75,000; fixed '
            'selling & distribution overhead N60,000; net profit before tax N205,000; tax 40%.'}],
      'a': [
      {'p': 'Units sold $= 800{,}000 / 20 = 40{,}000$. Total variable cost $= 120{,}000 + '
            '160{,}000 + 80{,}000 = N360{,}000$, i.e. N9/unit. Contribution/unit $= 20 - 9 = '
            'N11$. Total fixed cost $= 100{,}000 + 75{,}000 + 60{,}000 = N235{,}000$. P/V ratio '
            '$= 11/20 = 0.55$.'},
      {'h4': '(a) Break-even point'},
      {'tex': '\\text{BEP (units)} = \\dfrac{235{,}000}{11} \\approx 21{,}364\\text{ units}'},
      {'tex': '\\text{BEP (N)} = 21{,}364 \\times 20 \\approx N427{,}273'},
      {'h4': '(b) P/V ratio and margin of safety'},
      {'p': 'P/V ratio $= 0.55$, meaning **55 kobo of contribution** is generated per N1 of '
            'sales (contribution, not straight "profit" — once fixed costs are already fully '
            'covered, each further N1 of sales does add 55 kobo of profit, but below that point '
            'it is recovering fixed cost, not yet adding to profit).'},
      {'table': {'align': 'lrr', 'head': ['', 'N', 'Units'], 'rows': [
        ['Sales', '800,000', '40,000'],
        ['Break-even point', '427,273', '21,364'],
        ['**Margin of safety**', '**372,727**', '**18,636**'],
        ['M/S ratio', '47%', '47%'],
      ]}},
      {'key': 'A margin of safety of 47% means sales could fall by **more than 47%** before the '
              'company starts making a loss.'},
      {'h4': '(c) Units for an after-tax target profit of N150,000'},
      {'p': 'Before-tax equivalent of the target $= 150{,}000 / (1-0.4) = N250{,}000$.'},
      {'tex': '\\text{Units} = \\dfrac{235{,}000 + 250{,}000}{11} \\approx 44{,}091\\text{ '
              'units}'},
      {'h4': '(d) Sales value for a 15%-of-revenue net profit before tax'},
      {'p': 'Let $Y$ = required sales. Contribution $= 0.55Y$, and this must cover fixed cost '
            'plus the target profit of $0.15Y$: $0.55Y = 235{,}000 + 0.15Y$.'},
      {'tex': '0.40Y = 235{,}000 \\implies Y = N587{,}500'},
      {'h4': '(e) % volume increase for a profit 20% higher than last year'},
      {'p': 'Target profit before tax $= 1.20 \\times 205{,}000 = N246{,}000$.'},
      {'tex': '\\text{Units} = \\dfrac{235{,}000 + 246{,}000}{11} \\approx 43{,}727\\text{ units}'},
      {'tex': '\\%\\text{ increase} = \\dfrac{43{,}727 - 40{,}000}{40{,}000} \\times 100 '
              '\\approx 9.32\\%'},
      {'h4': '(f) New selling price to hold the same P/V ratio, with variable cost up 12%'},
      {'p': 'New variable cost $= 9 \\times 1.12 = N10.08$. Let RSP = revised selling price: '
            '$0.55 = (\\text{RSP} - 10.08)/\\text{RSP}$.'},
      {'tex': '0.45 \\times \\text{RSP} = 10.08 \\implies \\text{RSP} = N22.40'},
      {'p': 'Check: $(22.40 - 10.08)/22.40 = 12.32/22.40 = 0.55$ — confirmed.'},
      {'h4': '(g) Sales value to maintain the SAME profit (N205,000), price unchanged, variable '
       'cost up 12%'},
      {'p': 'New contribution/unit $= 20 - 10.08 = N9.92$.'},
      {'tex': '\\text{Sales value} = \\dfrac{(235{,}000 + 205{,}000)}{9.92} \\times 20 \\approx '
              'N887{,}097'},
      {'h4': '(h) Revised income statement — 10% salesmen\'s commission, price cut 13%, volume '
       'up 30%'},
      {'p': 'New price $= 20 \\times 0.87 = N17.40$. New volume $= 40{,}000 \\times 1.30 = '
            '52{,}000$ units. Variable cost stays at the **original** N9/unit (this scenario '
            'does not include the 12% variable-cost rise from parts (f)/(g)).'},
      {'table': {'align': 'lr', 'head': ['', 'N'], 'rows': [
        ['Sales (52,000 × 17.40)', '904,800'],
        ['Less: variable cost (52,000 × 9)', '468,000'],
        ['Less: salesmen\'s commission (10% of 904,800)', '90,480'],
        ['**Total contribution**', '**346,320**'],
        ['Less: fixed costs', '235,000'],
        ['**Net profit before tax**', '**111,320**'],
        ['Less: tax (40%)', '44,528'],
        ['**Net profit after tax**', '**66,792**'],
      ]}}]}},
  ]},

  {'n': '10.3', 't': 'CVP graphs', 'b': [
    {'p': 'Alongside the mathematical formulae, businesses often present the same relationships '
          'as a chart, so managers can appraise profitability at a glance without getting '
          '"bogged down" in the report\'s own detail. Two graph types are covered:'},

    {'h4': 'The Break-Even Chart'},
    {'p': 'Costs and revenue sit on the **Y-axis**; output (units) sits on the **X-axis**. The '
          '**total cost line** is fixed cost plus variable cost at each output level; the '
          '**total revenue line** is output × unit selling price. Their intersection is the '
          'break-even point.'},
    {'eg': {'tag': 'Study text', 't': 'Illustration 10.3 — reading a break-even chart', 'open':
      True, 'q': [
      {'p': 'Variable production cost N3/unit, variable selling cost N1/unit (total variable '
            'cost N4/unit), fixed costs N6,000, selling price N6/unit, budgeted output/sales '
            '3,600 units. Find the break-even point and margin of safety, as the chart would '
            'show them.'}],
      'a': [
      {'p': 'Unit contribution $= 6 - 4 = N2$.'},
      {'tex': '\\text{BEP} = \\dfrac{6{,}000}{2} = 3{,}000\\text{ units} = N18{,}000\\text{ '
              'of sales}'},
      {'table': {'align': 'lrr', 'head': ['', 'Revenue (N)', 'Units'], 'rows': [
        ['Budgeted', '21,600', '3,600'],
        ['Break-even point', '18,000', '3,000'],
        ['**Margin of safety**', '**3,600**', '**600**'],
      ]}},
      {'key': 'The chart shows three named regions: a **loss area** (below BEP, where the '
              'total-cost line sits above the total-revenue line), a **profit area** (above '
              'BEP), and the **margin of safety** — the horizontal gap on the chart between the '
              'BEP output and the budgeted output. Sales can fall by up to N3,600 (600 units) '
              'and the firm still just breaks even.'}]}},

    {'h4': 'The Profit-Volume (P/V) Chart'},
    {'p': 'Plots **profit directly** (Y-axis) against **sales revenue** (X-axis), rather than '
          'plotting cost and revenue as two separate lines. To draw it: (i) plot the break-even '
          'sales value on the X-axis, where profit is zero; (ii) plot the loss at zero sales — '
          'this equals the **total fixed cost**, taken as a loss on the Y-axis; (iii) join the '
          'two points with a straight line. Using Illustration 10.3\'s figures, the line runs '
          'from $(0, -6{,}000)$ to $(18{,}000, 0)$; margin of safety reads directly off the '
          'X-axis as the gap between the break-even sales value and the budgeted sales value '
          '(N21,600 − N18,000 = N3,600, or 16.67% of budgeted revenue).'},
  ]},

  {'n': '10.4', 't': 'Limitations of break-even analysis', 'b': [
    {'p': 'The limitations stem directly from its underlying assumptions (§10.2):'},
    {'ol': [
      'assuming fixed cost is constant at **every** activity level is unrealistic — fixed cost '
      'often behaves as a **stepped** cost instead, which the plain break-even model does not '
      'capture;',
      'results are only trustworthy **within** the activity range where costs are genuinely '
      'known accurately;',
      'CVP represents a **short-term** relationship, and is inappropriate for long-term '
      'analysis;',
      'variable cost and sales are assumed **linear**, but bulk discounts, overtime premiums, '
      'learning-curve effects and special-price contracts really make them curve, not a '
      'straight line;',
      'the technique assumes **perfect knowledge** of cost and revenue behaviour, ignoring the '
      'risk and uncertainty that is always genuinely present;',
      'it assumes activity level is the **only** thing driving cost and revenue changes, when '
      'in practice many other factors do too;',
      'individual cost components (material, labour, etc.) do not all react to activity in the '
      'same way, even though the model implicitly treats variable cost as one uniform block;',
      'it unrealistically assumes a **single product** (or a constant mix, or a constant mark-up '
      'on marginal cost) — an oversimplification for a real multi-product business; and',
      'it assumes a **perfect market** in which the firm is a pure price-taker, rarely true in '
      'practice.',
    ]},
  ]},

  {'n': '10.5', 't': 'Worksheet summary — definitions, formulae and structure', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§10.1 CVP** — the broad study of how cost/revenue/profit move with volume; supports '
      'budgeting, pricing, sales-mix and capacity decisions.',
      '**§10.2 Break-even analysis** — BEP is where TC=TR; 11 named assumptions (fixed cost '
      'constant, variable cost strictly proportional, price fixed, single product/constant mix, '
      'no inventory build-up, etc.); 2 computation techniques (equation; contribution margin); '
      'the P/V ratio (3 equivalent formulas) and margin of safety (Sf − Sb, and as a %); the '
      'multi-product BEP needs a *weighted* C/S ratio.',
      '**§10.3 Graphs** — the break-even chart plots cost/revenue vs output, showing loss area/'
      'profit area/margin of safety directly; the P/V chart plots profit itself vs sales '
      'revenue as a single straight line from (0, −Fixed Cost) to (BEP sales, 0).',
      '**§10.4 Limitations** — 9 named weaknesses, all traceable back to the assumptions in '
      '§10.2 not holding perfectly in the real world.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Break-Even Point (BEP)** — where TC = TR, zero profit.',
      '**P/V ratio (Contribution Margin Ratio)** — contribution ÷ sales; measures a product\'s '
      'profitability per unit of revenue.',
      '**Margin of safety** — forecast sales minus break-even sales; how far sales can fall '
      'before a loss starts.',
      '**C/S ratio** — another name for the P/V ratio.',
    ]},
    {'h3': 'B. Formula box'},
    {'fbox': {'h': 'CVP formulas (recap)', 'rows': [
      {'lb': 'BEP, units', 'tex': '\\dfrac{\\text{Fixed Cost}}{\\text{Contribution per unit}}'},
      {'lb': 'BEP, money value', 'tex': '\\dfrac{\\text{Fixed Cost}}{\\text{P/V Ratio}}'},
      {'lb': 'P/V ratio', 'tex': '\\dfrac{\\text{Contribution}}{\\text{Sales}}'},
      {'lb': 'Margin of safety (value)', 'tex': 'S_f - S_b'},
      {'lb': 'Margin of safety (%)', 'tex': '\\dfrac{S_f - S_b}{S_f} \\times 100'},
      {'lb': 'Sales for a target after-tax profit, units', 'tex': '\\dfrac{\\text{Fixed Cost} + '
        '\\dfrac{\\text{Target after-tax profit}}{1-\\text{tax rate}}}{\\text{Contribution per '
        'unit}}'},
    ]}},
  ]},

  {'n': '10.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which one of these is NOT an assumption of break-even analysis? (A) Fixed costs remain '
        'constant  (B) Variable costs vary proportionally with volume  (C) There is no '
        'synchronisation between production and sales  (D) Costs can be resolved into their '
        'fixed and variable components  (E) Selling price does not change as volume changes',
        'What is margin of safety? (A) The amount by which actual or budgeted output/sales may '
        'fall short of the budget without incurring a loss  (B) The amount by which budgeted '
        'output/sales may fall short of the actual without incurring a loss  (C) The point '
        'where actual output/sales agree with the budget  (D) The area immediately preceding '
        'the break-even point  (E) The area where fixed assets are equal to variable costs',
        'What happens in the area before the break-even point? (A) No profit, no loss  '
        '(B) Marginal profit  (C) Huge profit  (D) Loss  (E) No revenue',
        'The point at which total revenues equal total costs is known as ……………………..',
        'The number of units of a product that must be sold to break even is given by the '
        'formula ………….',
        'Break-even point in Naira can be calculated by multiplying the break-even point in '
        'units with ……………………',
      ]}],
      'a': [
      {'ol': [
        '**C** — synchronisation between production and sales (no inventory build-up) **is** '
        'an assumption, so its *absence* is not; every other option lists a real assumption.',
        '**A** — the amount by which actual/budgeted output or sales may fall short of the '
        'budget without incurring a loss.',
        '**D — loss.** Before BEP, total cost still exceeds total revenue.',
        '**Break-even point.**',
        '**Fixed Costs ÷ Contribution per unit.**',
        '**Unit selling price.**',
      ]}]}},
  ]},

  {'n': '10.7', 't': 'Study text examination-type questions, worked', 'b': [
    {'p': 'The study text closes the chapter with ten examination-type questions, numbered 9.1 '
          'to 9.10 in the book (the numbering carries over from the previous chapter). All are '
          'reproduced below with full answers.'},

    {'eg': {'tag': 'Exam type — Q9.1',
      't': 'An electrical goods manufacturer — is direct labour really variable?',
      'q': [
      {'p': 'An electrical goods manufacturing company made a **10% profit on sales of N1 '
            'million** in the last trading year. The composition of its costs was **direct '
            'labour 25%, direct materials 60% and fixed overhead 15%**.'},
      {'p': 'The general manager has drawn attention to the fact that, although sales were just '
            'below forecast, the profit was very much lower than expected. Investigation shows '
            'the significant difference appears to be caused by the **direct labour costs**. The '
            'company uses the marginal cost accounting principle to price its products, and in '
            'all price quotations direct labour was treated as a **variable cost directly '
            'related to volume of output**. However, the review indicates that the direct labour '
            'cost showed **little change when output decreased** for any reason.'},
      {'p': '**Required:** **(a)** state whether you agree that direct labour costs should be '
            'treated as wholly variable with output; **(b)** calculate, using last year\'s '
            'results, the sales volume at break-even point and the margin of safety when direct '
            'labour costs are treated as (i) wholly variable and (ii) fixed.'}],
      'a': [
      {'h4': 'Working — last year\'s cost structure'},
      {'stmt': {'t': 'Last year (N)', 'rows': [
        ['Sales', '', 1000000],
        ['Profit at 10% of sales', '', 100000],
        ['**Total cost**', '', 900000, '@t'],
        '@gap',
        ['Direct materials  (60% of N900,000)', '', 540000],
        ['Direct labour  (25% of N900,000)', '', 225000],
        ['Fixed overhead  (15% of N900,000)', '', 135000],
        ['**Total cost**', '', 900000, '@tt'],
      ]}},
      {'h4': '(a)  Should direct labour be treated as wholly variable?'},
      {'p': '**No — on the evidence here it should not.** The review shows direct labour cost '
            '"showed little change when output decreased", which is the definition of a cost '
            'that is **not** variable. Treating it as variable has three consequences, all of '
            'which explain exactly what the general manager observed:'},
      {'ol': [
        '**The contribution per unit is overstated**, because N225,000 of cost that does not in '
        'fact fall with output has been deducted in arriving at it.',
        '**The break-even point is understated** (see (b) below), so the company believed it was '
        'far safer than it was.',
        '**Prices quoted were too low.** Quotations assumed that labour cost would fall if the '
        'order were not taken; it would not. So each order was quoted on a contribution that did '
        'not exist, and a small shortfall in volume produced a large shortfall in profit.',
      ]},
      {'p': 'Direct labour is genuinely variable only where it is paid by **piecework**, or '
            'where casual or contract labour can be engaged and released with output. Where '
            'workers are on **guaranteed weekly wages**, with notice periods and union '
            'agreements, labour is a **fixed or stepped** cost in the short run, however '
            '"direct" it may be for product-costing purposes.'},
      {'warn': 'Note the distinction being tested. **Direct / indirect** is a classification by '
               '**nature** — can the cost be traced to a cost unit? **Fixed / variable** is a '
               'classification by **behaviour** — does it change with activity? A cost can be '
               'direct **and** fixed, as here. The two classifications are independent, and '
               'assuming "direct therefore variable" is precisely the error that cost this '
               'company its profit.'},
      {'h4': '(b)(i)  Direct labour treated as wholly variable'},
      {'stmt': {'t': 'Break-even and margin of safety — labour variable (N)', 'rows': [
        ['Sales', '', 1000000],
        ['Variable costs:  materials 540,000 + labour 225,000', '', 765000],
        ['**Contribution**', '', 235000, '@t'],
        ['**P/V ratio**  (235,000 ÷ 1,000,000)', '', '23.5%'],
        ['Fixed costs', '', 135000],
        '@gap',
        ['**Break-even sales**  (135,000 ÷ 0.235)', '', 574468, '@t'],
        ['**Margin of safety**  (1,000,000 − 574,468)', '', 425532],
        ['**Margin of safety as % of sales**', '', '42.6%', '@tt'],
      ]}},
      {'h4': '(b)(ii)  Direct labour treated as fixed'},
      {'stmt': {'t': 'Break-even and margin of safety — labour fixed (N)', 'rows': [
        ['Sales', '', 1000000],
        ['Variable costs:  materials only', '', 540000],
        ['**Contribution**', '', 460000, '@t'],
        ['**P/V ratio**  (460,000 ÷ 1,000,000)', '', '46.0%'],
        ['Fixed costs:  overhead 135,000 + labour 225,000', '', 360000],
        '@gap',
        ['**Break-even sales**  (360,000 ÷ 0.46)', '', 782609, '@t'],
        ['**Margin of safety**  (1,000,000 − 782,609)', '', 217391],
        ['**Margin of safety as % of sales**', '', '21.7%', '@tt'],
      ]}},
      {'key': 'Treating labour correctly as fixed **raises the break-even point by N208,141** '
              'and **halves the margin of safety**, from 42.6% to 21.7%. That is the answer to '
              'the general manager\'s question. On the company\'s own (wrong) assumption, '
              'sales could fall 42% before profit disappeared; in reality they could fall only '
              '22%. The business was running far closer to the edge than it believed, and a '
              'small shortfall in sales therefore produced a disproportionate collapse in '
              'profit — which is exactly what **high operating gearing** does.'}]}},

    {'eg': {'tag': 'Exam type — Q9.2',
      't': 'Prudent Nigeria Ltd — deriving fixed cost and P/V ratio from two years\' totals',
      'q': [
      {'p': 'The following figures relate to Prudent Nigeria Ltd, which manufactures a varied '
            'range of products:'},
      {'stmt': {'t': 'Two years\' results (N)', 'rows': [
        ['Year', 'Total sales', 'Total costs', '@hd'],
        [1, 39000, 34800],
        [2, 43000, 37600],
      ]}},
      {'p': 'Assuming stability in prices, with variable costs carefully controlled to reflect '
            'predetermined relationships, and an unvarying figure for fixed costs:'},
      {'p': '**Required:** **(i)** calculate (a) the fixed cost, (b) the profit/volume ratio, '
            '(c) the break-even point, (d) the margin of safety for years 1 and 2. '
            '**(ii)** How might the profit/volume ratio be improved, apart from increasing '
            'prices or reducing costs?'}],
      'a': [
      {'h4': 'Step 1 — the profit for each year, and the P/V ratio'},
      {'p': 'With fixed costs unchanged, every naira of extra contribution falls straight into '
            'profit — so the **change in profit divided by the change in sales** is the P/V '
            'ratio. This is the high-low method of §2.1.2a applied to total figures.'},
      {'stmt': {'t': 'Deriving the P/V ratio (N)', 'rows': [
        ['', 'Year 1', 'Year 2', 'Change', '@hd'],
        ['Total sales', 39000, 43000, 4000],
        ['Total costs', 34800, 37600, 2800],
        ['**Profit**', 4200, 5400, 1200, '@tt'],
      ]}},
      {'tex': '\\text{P/V ratio} = \\frac{\\text{Change in profit}}'
              '{\\text{Change in sales}} = \\frac{1{,}200}{4{,}000} = 30\\%'},
      {'h4': '(i)(a)  The fixed cost'},
      {'p': 'With a P/V ratio of 30%, variable cost is **70% of sales**:'},
      {'stmt': {'t': 'Fixed cost (N)', 'rows': [
        ['', 'Year 1', 'Year 2', '@hd'],
        ['Total cost', 34800, 37600],
        ['Less: variable cost  (70% × 39,000;  70% × 43,000)', 27300, 30100],
        ['**Fixed cost**', 7500, 7500, '@tt'],
      ]}},
      {'note': 'The fixed cost comes out at the same N7,500 from both years, which confirms the '
               'P/V ratio of 30%. Always use the second year as a check — if the two fixed-cost '
               'figures differ, the P/V ratio is wrong or the assumption of stable costs does '
               'not hold.'},
      {'h4': '(i)(b)–(d)  P/V ratio, break-even point and margin of safety'},
      {'stmt': {'t': 'Summary of answers (N)', 'rows': [
        ['**(b) Profit/volume ratio**', '', '30%'],
        ['**(c) Break-even point**  (fixed cost ÷ P/V ratio = 7,500 ÷ 0.30)', '', 25000],
        '@gap',
        ['**(d) Margin of safety — Year 1**  (39,000 − 25,000)', 14000,
         '*35.9% of sales*'],
        ['**       Margin of safety — Year 2**  (43,000 − 25,000)', 18000,
         '*41.9% of sales*'],
      ]}},
      {'h4': '(ii)  Improving the P/V ratio without raising prices or cutting costs'},
      {'p': 'The P/V ratio is contribution ÷ sales, so for a multi-product company it can be '
            'improved by **changing what is sold** rather than what it costs or what it is sold '
            'for:'},
      {'ol': [
        '**Change the sales mix** towards products with a higher individual P/V ratio — the '
        'single most effective lever available to a company selling a "varied range of '
        'products", as this one does.',
        '**Promote and give more sales effort to high-contribution products**, and withdraw '
        'effort from low-contribution ones.',
        '**Introduce new products with a higher P/V ratio**, or redesign existing ones (value '
        'analysis) to use less material and labour without reducing their utility.',
        '**Substitute cheaper materials or methods** of equal quality, which raises contribution '
        'without a price change.',
        '**Improve efficiency and reduce wastage, scrap and rework**, so that less variable cost '
        'is consumed per naira of sales.',
        '**Reduce discounts, allowances and returns**, which raises the *net* price realised '
        'without altering the list price.',
        '**Automate** — substituting machinery for direct labour converts variable cost into '
        'fixed cost and so raises the P/V ratio *(though note it raises the break-even point '
        'too, and with it the risk, as Q9.1 above demonstrates)*.',
      ]}]}},

    {'eg': {'tag': 'Exam type — Q9.3',
      't': 'CVP assumptions, and Yakasai Toys Company\'s break-even and projected income',
      'q': [
      {'p': '**(a)** Cost-volume-profit analysis is a technique available to management to '
            'understand better the inter-relationship of several factors which affect a firm\'s '
            'profit. As with many such techniques, the accountant oversimplifies the real world '
            'by making certain assumptions. **Mention five major assumptions underlying C-V-P '
            'analysis.**'},
      {'p': '**(b)** Yakasai Toys Company\'s tentative budget for product Q for 2004 is:'},
      {'stmt': {'t': 'Budget for product Q, 2004 (N)', 'rows': [
        ['Sales (2,500 units) @ N40', '', 100000],
        '@gap',
        ['**Manufacturing cost of goods sold**', '', '', '@hd'],
        ['Direct labour', 15000, ''],
        ['Direct materials', 14000, ''],
        ['Variable factory overhead', 10000, ''],
        ['Fixed factory overhead', 5000, 44000],
        ['**Gross profit**', '', 56000, '@t'],
        '@gap',
        ['**Selling expenses**', '', '', '@hd'],
        ['Variable', 6000, ''],
        ['Fixed', 10000, ''],
        ['**Administration expenses**', '', '', '@hd'],
        ['Variable', 5000, ''],
        ['Fixed', 10000, 31000],
        ['**Operating income**', '', 25000, '@tt'],
      ]}},
      {'p': '**Required:** (i) how many units of product Q would have to be sold to break even? '
            '(ii) what would the operating income be if projected sales increased by 30%?'}],
      'a': [
      {'h4': '(a)  Major assumptions underlying C-V-P analysis'},
      {'ol': [
        '**All costs can be resolved into fixed and variable elements**, and the split is known '
        'and reliable.',
        '**Cost and revenue behaviour is linear** over the relevant range — variable cost per '
        'unit and selling price per unit are constant, so total cost and total revenue are '
        'straight lines.',
        '**Total fixed cost remains constant** over the whole range of activity considered, and '
        'does not step.',
        '**The sales mix remains constant** where more than one product is sold — otherwise '
        'there is no single P/V ratio.',
        '**Production equals sales**, so there is no change in inventory levels and no fixed '
        'overhead is carried forward or released.',
        '**Volume is the only factor affecting cost and revenue** — efficiency, productivity, '
        'technology, methods and price levels are all unchanged.',
        '**The analysis is valid only within the relevant range** of activity for which the cost '
        'behaviour was established, and only in the short run.',
      ]},
      {'h4': 'Working — the cost structure of product Q'},
      {'stmt': {'t': 'Separating fixed and variable (N)', 'rows': [
        ['**Variable costs**', '', '', '@hd'],
        ['Direct labour', 15000, ''],
        ['Direct materials', 14000, ''],
        ['Variable factory overhead', 10000, ''],
        ['Variable selling expenses', 6000, ''],
        ['Variable administration expenses', 5000, 50000],
        ['**Variable cost per unit  (50,000 ÷ 2,500 units)**', '', 'N20', '@t'],
        '@gap',
        ['**Fixed costs**', '', '', '@hd'],
        ['Fixed factory overhead', 5000, ''],
        ['Fixed selling expenses', 10000, ''],
        ['Fixed administration expenses', 10000, 25000],
        '@gap',
        ['Selling price per unit', '', 'N40'],
        ['**Contribution per unit  (40 − 20)**', '', 'N20', '@t'],
        ['**P/V ratio  (20 ÷ 40)**', '', '50%', '@tt'],
      ]}},
      {'note': 'Note that the budget as presented is in **absorption** form — it computes a '
               'gross profit, which mixes fixed factory overhead into cost of sales. The first '
               'task in any CVP question presented this way is to **re-sort every line into '
               'fixed or variable**, ignoring the manufacturing / selling / administration '
               'classification entirely. Variable selling and administration costs are just as '
               'variable as direct materials.'},
      {'h4': '(b)(i)  Break-even point'},
      {'tex': '\\text{Break-even units} = \\frac{\\text{Fixed costs}}'
              '{\\text{Contribution per unit}} = \\frac{25{,}000}{20} '
              '= 1{,}250 \\text{ units}'},
      {'tex': '\\text{Break-even sales value} = 1{,}250 \\times N40 = N50{,}000 '
              '\\qquad \\left(\\text{or } \\frac{25{,}000}{0.50} = N50{,}000\\right)'},
      {'h4': '(b)(ii)  Operating income if sales increase by 30%'},
      {'stmt': {'t': 'Projected results at 3,250 units (N)', 'rows': [
        ['', 'Budget (2,500 units)', 'Projected (3,250 units)', '@hd'],
        ['Sales @ N40', 100000, 130000],
        ['Less: variable costs @ N20', 50000, 65000],
        ['**Contribution**', 50000, 65000, '@t'],
        ['Less: fixed costs', 25000, 25000],
        ['**Operating income**', 25000, 40000, '@tt'],
      ]}},
      {'key': 'A **30% increase in sales produces a 60% increase in profit** — from N25,000 to '
              'N40,000. That is **operating gearing** at work: fixed costs do not rise with the '
              'extra volume, so the whole of the extra contribution of N15,000 falls into '
              'profit. The same gearing works in reverse: a 30% *fall* in sales would cut '
              'contribution to N35,000 and profit to N10,000, a 60% collapse. Margin of safety '
              'at the budgeted level is $(100{,}000 - 50{,}000) \\div 100{,}000 = 50\\%$, so '
              'the company has reasonable protection.'}]}},

    {'eg': {'tag': 'Exam type — Q9.4',
      't': 'Universal Cloth Manufacturing — break-even and profit across three shift levels',
      'q': [
      {'p': 'Universal Cloth Manufacturing Limited has rented a new factory and intends to '
            'produce a newly developed man-made fibre, "Texlon". It is planned to produce Texlon '
            'in the new mill first on a **single shift**, six months later on a **double '
            'shift**, and three months after that on a **treble shift**. Production, cost and '
            'selling price per unit are:'},
      {'stmt': {'t': 'Shift data', 'rows': [
        ['', 'Single shift', 'Double shift', 'Treble shift', '@hd'],
        ['Production per week (units)', 'up to 1,500', '1,500 – 2,500', '2,501 – 4,000'],
        ['Selling price per unit', 'N5.00', 'N5.00', 'N5.00'],
        ['Variable cost per unit', 'N3.00', 'N3.20', 'N3.50'],
        ['Fixed cost per week', 'N2,000', 'N2,520', 'N3,030'],
      ]}},
      {'p': '**Required:** (i) the break-even units per week of each shift; (ii) the total unit '
            'cost for each shift at break-even and at full capacity; (iii) the profit or loss '
            'for each shift at 50% of the installed (or increased) capacity — single shift 750 '
            'units, double shift 2,000 units, treble shift 3,250 units; (iv) the profit per week '
            'at full capacity for each shift, and the unit variable and fixed cost.'}],
      'a': [
      {'h4': 'Working — contribution per unit at each shift level'},
      {'stmt': {'t': 'Contribution per unit (N)', 'rows': [
        ['', 'Single', 'Double', 'Treble', '@hd'],
        ['Selling price', 5.00, 5.00, 5.00],
        ['Less: variable cost', 3.00, 3.20, 3.50],
        ['**Contribution per unit**', 2.00, 1.80, 1.50, '@tt'],
      ]}},
      {'note': 'Contribution **falls** as shifts are added — N2.00, N1.80, N1.50 — because '
               'night and weekend working carry shift premiums, and fixed cost rises at each '
               'step too. Adding capacity is not free in either direction.'},
      {'h4': '(i)  Break-even units per week'},
      {'stmt': {'t': 'Break-even point', 'rows': [
        ['', 'Single', 'Double', 'Treble', '@hd'],
        ['Fixed cost per week (N)', 2000, 2520, 3030],
        ['÷ contribution per unit (N)', 2.00, 1.80, 1.50],
        ['**Break-even units per week**', 1000, 1400, 2020, '@tt'],
      ]}},
      {'warn': 'Note an important qualification. The double shift operates only between 1,500 '
               'and 2,500 units, and the treble only between 2,501 and 4,000 — yet their '
               'computed break-even points, 1,400 and 2,020 units, lie **below** their own '
               'operating ranges. The figures are arithmetically correct, but they describe a '
               'level of output at which that shift pattern would never actually be run. The '
               'practical meaning is simply that **once a shift level is operating within its '
               'range, it is already past break-even** — which is reassuring, not alarming. A '
               'good answer states this rather than quoting the numbers without comment.'},
      {'h4': '(ii)  Total unit cost at break-even and at full capacity'},
      {'stmt': {'t': 'Total unit cost (N)', 'rows': [
        ['', 'Single', 'Double', 'Treble', '@hd'],
        ['**At break-even**', '', '', '', '@hd'],
        ['Units', 1000, 1400, 2020],
        ['Fixed cost', 2000, 2520, 3030],
        ['Variable cost  (units × variable cost per unit)', 3000, 4480, 7070],
        ['Total cost', 5000, 7000, 10100],
        ['**Total unit cost at break-even**', 5.000, 5.000, 5.000, '@t'],
        '@gap',
        ['**At full capacity**', '', '', '', '@hd'],
        ['Units', 1500, 2500, 4000],
        ['Fixed cost', 2000, 2520, 3030],
        ['Variable cost', 4500, 8000, 14000],
        ['Total cost', 6500, 10520, 17030],
        ['**Total unit cost at full capacity**', 4.333, 4.208, 4.258, '@tt'],
      ]}},
      {'note': 'The unit cost at break-even is **N5.00 in every case** — necessarily so, because '
               'break-even is by definition the point at which total cost equals total revenue, '
               'and revenue is N5 per unit. That identity is a free check on your arithmetic.'},
      {'h4': '(iii)  Profit or loss at 50% of the installed (or increased) capacity'},
      {'stmt': {'t': 'Profit / (loss) per week (N)', 'rows': [
        ['', 'Single (750 units)', 'Double (2,000 units)', 'Treble (3,250 units)', '@hd'],
        ['Contribution  (750×2.00;  2,000×1.80;  3,250×1.50)', 1500, 3600, 4875],
        ['Less: fixed cost per week', 2000, 2520, 3030],
        ['**Profit / (loss) per week**', -500, 1080, 1845, '@tt'],
      ]}},
      {'p': 'The single shift at 750 units makes a **loss of N500 a week**, because 750 units is '
            'below its break-even of 1,000. The double and treble shifts are both comfortably '
            'profitable at the stated levels.'},
      {'h4': '(iv)  Profit at full capacity, and the unit cost split'},
      {'stmt': {'t': 'At full capacity (N)', 'rows': [
        ['', 'Single (1,500)', 'Double (2,500)', 'Treble (4,000)', '@hd'],
        ['Contribution  (1,500×2.00;  2,500×1.80;  4,000×1.50)', 3000, 4500, 6000],
        ['Less: fixed cost per week', 2000, 2520, 3030],
        ['**Profit per week at full capacity**', 1000, 1980, 2970, '@t'],
        '@gap',
        ['**Unit variable cost**', 3.000, 3.200, 3.500],
        ['**Unit fixed cost**  (2,000÷1,500;  2,520÷2,500;  3,030÷4,000)', 1.333, 1.008, 0.758],
        ['**Total unit cost**', 4.333, 4.208, 4.258, '@tt'],
      ]}},
      {'key': 'Read the last three rows across. As shifts are added, **unit variable cost rises** '
              '(N3.00 → N3.20 → N3.50, the shift premium) while **unit fixed cost falls** '
              '(N1.333 → N1.008 → N0.758, the fixed cost spread over more output). The two '
              'pull in opposite directions, and the total unit cost reaches its **minimum at the '
              'double shift** (N4.208) before rising again at the treble shift. Yet weekly '
              '**profit** keeps rising, from N1,000 to N1,980 to N2,970, because the extra '
              'volume more than compensates for the slightly higher unit cost. **The '
              'lowest-unit-cost option is not the most profitable option** — a point worth '
              'making explicitly to the managing director.'}]}},

    {'eg': {'tag': 'Exam type — Q9.5',
      't': 'Break-even point explained, the break-even chart, and the CVP relationship',
      'q': [
      {'p': '**(a)** Explain the term "break-even point". Give an example illustrating your '
            'answer. Mention the types of problem an accountant can expect to solve with the '
            'help of such analysis.'},
      {'p': '**(b)** Draw a break-even chart with a few illustrative figures.'},
      {'p': '**(c)** Explain the cost-volume-profit relationship. How would a change in the '
            'selling price affect it?'}],
      'a': [
      {'h4': '(a)  The break-even point'},
      {'def': {'t': 'Break-even point', 'd': 'the level of activity at which **total revenue '
                    'exactly equals total cost**, so that the business makes neither a profit '
                    'nor a loss. At that point, total contribution is exactly equal to total '
                    'fixed costs.'}},
      {'fbox': {'h': 'Break-even point', 'rows': [
        {'lb': 'In units', 'tex': '\\text{BEP (units)} = \\frac{\\text{Fixed costs}}'
         '{\\text{Contribution per unit}}'},
        {'lb': 'In sales value', 'tex': '\\text{BEP (value)} = \\frac{\\text{Fixed costs}}'
         '{\\text{P/V ratio}}'},
      ]}},
      {'p': '**Example.** A firm sells a product at N50, with a variable cost of N30 per unit '
            'and fixed costs of N120,000 a year. Contribution is N20 per unit, so:'},
      {'stmt': {'t': 'Illustration', 'rows': [
        ['Break-even in units:  120,000 ÷ 20', '', '6,000 units'],
        ['Break-even in sales value:  6,000 × N50', '', 'N300,000'],
        ['P/V ratio:  20 ÷ 50', '', '40%'],
        ['Check:  120,000 ÷ 0.40', '', 'N300,000 ✓'],
      ]}},
      {'p': 'At 6,000 units: revenue N300,000, variable cost N180,000, contribution N120,000, '
            'less fixed costs N120,000 — profit nil. Each unit sold **above** 6,000 adds N20 '
            'straight to profit; each unit below costs N20.'},
      {'h4': '(a)  Problems an accountant can solve with break-even analysis'},
      {'ol': [
        '**What volume must we sell to break even**, or to reach a **target profit**?',
        '**How far can sales fall before we make a loss?** — the margin of safety.',
        '**What happens to profit if volume, price, variable cost or fixed cost changes?** — '
        'sensitivity analysis on each variable in turn.',
        '**Should we accept a special order** at below the normal price?',
        '**Should we change the selling price?** — will the extra volume cover the lower margin?',
        '**Which product mix** maximises profit, and what is the effect of changing it?',
        '**Should we substitute fixed cost for variable cost** — automate, or pay commission '
        'instead of salary? (See Q9.6 below.)',
        '**Should we make or buy**, or close a department temporarily?',
        '**What level of activity** should the budget be set at, and what is the risk if it is '
        'not achieved?',
      ]},
      {'h4': '(b)  The break-even chart'},
      {'p': 'Using the illustrative figures above — selling price N50, variable cost N30, fixed '
            'cost N120,000, capacity 10,000 units:'},
      {'pre': 'N\'000\n'
              ' 500 |                                                        / Total revenue\n'
              '     |                                                   /\n'
              ' 400 |                                              /          _____ Total cost\n'
              '     |                                         /        _____/\n'
              ' 300 |- - - - - - - - - - - - - - - - - - -*=====  PROFIT area\n'
              '     |                               /  ___/|\n'
              ' 200 |                          / ___/      |\n'
              '     |             LOSS    /___/            |\n'
              ' 150 |              area _/                 |              Fixed cost N120,000\n'
              ' 120 |===========/==========================|=====================\n'
              '     |      /                               |\n'
              '     |  /                                   |\n'
              '   0 +---------+---------+---------+--------+---------+-----------> units\n'
              '     0       2,000     4,000     6,000    6,000     8,000   10,000\n'
              '                                      BREAK-EVEN POINT\n'
              '                                      6,000 units / N300,000'},
      {'p': 'The chart has four elements: the **fixed cost line**, horizontal at N120,000; the '
            '**total cost line**, starting at N120,000 and rising by N30 per unit; the **total '
            'revenue line**, starting at the origin and rising by N50 per unit; and the '
            '**break-even point** where the two sloping lines cross. The wedge to the left of '
            'the crossing is the **loss area**; the widening wedge to the right is the **profit '
            'area**; the horizontal distance from break-even to the actual or budgeted sales '
            'level is the **margin of safety**.'},
      {'h4': '(c)  The cost-volume-profit relationship'},
      {'p': 'CVP analysis studies how **profit responds to changes in volume**, given the way '
            'costs behave. Its core identity is:'},
      {'tex': '\\text{Profit} = (\\text{Selling price} - \\text{Variable cost per unit}) '
              '\\times \\text{Units sold} - \\text{Fixed costs}'},
      {'p': 'Because fixed costs do not move with volume, profit changes by the **contribution '
            'per unit** for every extra unit sold — so profit is far more volatile than sales. '
            'The three levers are the contribution per unit, the volume, and the fixed cost.'},
      {'h4': '(c)  The effect of a change in selling price'},
      {'ol': [
        'A **rise in selling price** increases contribution per unit and therefore the **P/V '
        'ratio**; the total revenue line on the chart becomes **steeper**; the **break-even '
        'point falls**; the margin of safety widens; and profit at any given volume rises.',
        'A **fall in selling price** does the reverse: contribution per unit and the P/V ratio '
        'fall, the revenue line flattens, the **break-even point rises**, and more units must be '
        'sold merely to stand still.',
        '**But volume will also change**, in the opposite direction — that is the whole point of '
        'altering a price. The real question is therefore always: **does the change in volume '
        'more than compensate for the change in contribution per unit?**',
      ]},
      {'p': '**Illustration.** On the figures above, cutting the price from N50 to N45 reduces '
            'contribution from N20 to N15 and raises break-even from 6,000 to '
            '$120{,}000 \\div 15 = 8{,}000$ units. To earn the same profit as 8,000 units at '
            'the old price (a profit of N40,000), the company must now sell '
            '$(120{,}000 + 40{,}000) \\div 15 = 10{,}667$ units — a **33% increase in '
            'volume** to absorb a **10% price cut**. That calculation, done before the price is '
            'changed rather than after, is one of the most valuable things CVP analysis '
            'provides.'}]}},

    {'eg': {'tag': 'Exam type — Q9.6 (ICAN Intermediate, November 2000)',
      't': 'Gusau manufacturer — four scenarios on salary versus commission',
      'q': [
      {'p': 'You are the Finance Manager of a manufacturing company based in Gusau. The company '
            'has been incurring trading losses. Your new Managing Director has returned from a '
            'workshop convinced that the Profit/Volume ratio can be used to calculate the effect '
            'of changes in volume or costs on profit. The following details are available:'},
      {'stmt': {'t': 'Operating data (N)', 'rows': [
        ['Selling price per carton of product', '', 1200],
        ['Variable cost per carton', '', 1000],
        ['Variable distribution expenses per carton', '', 50],
        '@gap',
        ['**Annual fixed expenses**', '', '', '@hd'],
        ['Storage', '', 200000],
        ['Wages', '', 100000],
      ]}},
      {'p': '**Required** — consider each case independently: **(i)** the Marketing Director '
            'thinks that by spending **N20,000 monthly on advertising** he can achieve annual '
            'sales of **5,000 cartons** — what will the profit be? **(ii)** The wages are paid '
            'to the Marketing Field Force; they offer to forgo these wages in exchange for a '
            '**N25 commission per carton sold** — if accepted, what would the annual break-even '
            'point be in sales revenue and in unit sales? **(iii)** The target profit is '
            '**N600,000** — how many cartons must be sold to achieve it (ignoring the Marketing '
            'Director\'s proposal) (a) assuming the field force receives their N100,000 '
            'salaries, and (b) assuming they are paid commission? **(iv)** What level of sales '
            'produces the same profit whether the Marketing Department is paid by salary or by '
            'commission?'}],
      'a': [
      {'h4': 'Working — the present cost structure'},
      {'stmt': {'t': 'Present contribution and fixed costs (N)', 'rows': [
        ['Selling price per carton', '', 1200],
        ['Less: variable cost per carton', 1000, ''],
        ['          variable distribution expenses per carton', 50, 1050],
        ['**Contribution per carton**', '', 150, '@t'],
        ['**P/V ratio**  (150 ÷ 1,200)', '', '12.5%'],
        '@gap',
        ['Annual fixed expenses:  storage 200,000 + wages 100,000', '', 300000],
        ['**Present break-even**  (300,000 ÷ 150)', '', '2,000 cartons', '@tt'],
      ]}},
      {'h4': '(i)  The advertising proposal'},
      {'stmt': {'t': 'Profit with N20,000 monthly advertising and sales of 5,000 cartons (N)',
        'rows': [
        ['Contribution:  5,000 cartons × N150', '', 750000],
        ['Less: existing fixed expenses', 300000, ''],
        ['          advertising  (N20,000 × 12 months)', 240000, 540000],
        ['**Profit**', '', 210000, '@tt'],
      ]}},
      {'note': 'The advertising campaign needs $240{,}000 \\div 150 = 1{,}600$ extra cartons '
               'merely to pay for itself. It is worth undertaking only if sales would otherwise '
               'have been below $5{,}000 - 1{,}600 = 3{,}400$ cartons.'},
      {'h4': '(ii)  Break-even under the commission scheme'},
      {'stmt': {'t': 'Break-even with commission replacing salaries (N)', 'rows': [
        ['Contribution per carton (as before)', '', 150],
        ['Less: commission per carton', '', 25],
        ['**Revised contribution per carton**', '', 125, '@t'],
        '@gap',
        ['Fixed expenses:  storage 200,000  (wages of 100,000 now removed)', '', 200000],
        '@gap',
        ['**Break-even in units**  (200,000 ÷ 125)', '', '1,600 cartons', '@t'],
        ['**Break-even in sales revenue**  (1,600 × N1,200)', '', 1920000, '@tt'],
      ]}},
      {'h4': '(iii)  Cartons needed for a target profit of N600,000'},
      {'tex': '\\text{Units for a target profit} = \\frac{\\text{Fixed costs} + '
              '\\text{Target profit}}{\\text{Contribution per unit}}'},
      {'stmt': {'t': 'Target-profit volume', 'rows': [
        ['', '(a) With salaries', '(b) With commission', '@hd'],
        ['Fixed costs (N)', 300000, 200000],
        ['Add: target profit (N)', 600000, 600000],
        ['**Total to be covered (N)**', 900000, 800000, '@t'],
        ['÷ contribution per carton (N)', 150, 125],
        ['**Cartons required**', 6000, 6400, '@tt'],
      ]}},
      {'h4': '(iv)  The level of sales at which the two schemes give the same profit'},
      {'p': 'Let $Q$ be the number of cartons. Profit under each scheme is:'},
      {'tex': '\\text{Salary scheme: } 150Q - 300{,}000 \\qquad\\qquad '
              '\\text{Commission scheme: } 125Q - 200{,}000'},
      {'p': 'Setting them equal:'},
      {'tex': '150Q - 300{,}000 = 125Q - 200{,}000 \\;\\Longrightarrow\\; 25Q = 100{,}000 '
              '\\;\\Longrightarrow\\; Q = 4{,}000 \\text{ cartons}'},
      {'stmt': {'t': 'Check at 4,000 cartons (N)', 'rows': [
        ['', 'Salary scheme', 'Commission scheme', '@hd'],
        ['Contribution  (4,000 × 150;  4,000 × 125)', 600000, 500000],
        ['Less: fixed costs', 300000, 200000],
        ['**Profit**', 300000, 300000, '@tt'],
      ]}},
      {'key': 'The **indifference point is 4,000 cartons**, and the rule either side of it is '
              'the heart of the question. **Below 4,000 cartons the commission scheme is '
              'better**, because the company carries N100,000 less fixed cost and pays the field '
              'force only when they actually sell. **Above 4,000 cartons the salary scheme is '
              'better**, because the N25 a carton given up exceeds the N100,000 saved. Given '
              'that the company has been **making trading losses** and is therefore operating '
              'well below 4,000 cartons, the commission scheme should be accepted — it also '
              'lowers the break-even point from 2,000 to 1,600 cartons, which reduces risk '
              'exactly when the company can least afford it. This is the practical value of the '
              'P/V ratio the Managing Director was told about.'}]}},

    {'eg': {'tag': 'Exam type — Q9.7 (ICAN PE I, May 2001)',
      't': 'ABC Ltd — the effect of a new plant on the P/V ratio, profit and margin of safety',
      'q': [
      {'p': 'ABC Ltd manufactures one product only, which it sells at **N20 per unit**. The '
            'existing plant has a maximum capacity of **20,000 units** per annum, at which level '
            'net profit is **N1.50 per unit** and the **profit/volume ratio is 20%**. A new '
            'plant is to be purchased, having a maximum capacity of **30,000 units** per annum, '
            'but this will increase fixed costs by **N15,000** per annum. Variable costs will be '
            '**reduced by N4 per unit**, and to achieve an increase in sales the selling price '
            'is also to be **reduced by N4 per unit**.'},
      {'p': '**Required:** **(a)** explain what you understand by the terms profit/volume ratio '
            'and margin of safety; **(b)** calculate the revised P/V ratio as a result of the '
            'purchase of the new plant; **(c)** calculate the number of units which would be '
            'required using the new plant to give a **50% increase in profit** compared with '
            'maximum production using the old plant; **(d)** calculate the margin of safety if '
            'the actual level of sales is **25,000 units**, assuming the new plant is '
            'purchased.'}],
      'a': [
      {'h4': '(a)  The two terms'},
      {'def': {'t': 'Profit/volume (P/V) ratio', 'd': 'contribution expressed as a percentage of '
                    'sales value — also called the **contribution to sales ratio**. It measures '
                    'how much of every naira of sales is left after variable costs to cover '
                    'fixed costs and provide profit, and it is therefore the rate at which '
                    'profit changes as sales change.'}},
      {'tex': '\\text{P/V ratio} = \\frac{\\text{Contribution}}{\\text{Sales}} '
              '\\times 100 = \\frac{\\text{Selling price} - \\text{Variable cost}}'
              '{\\text{Selling price}} \\times 100'},
      {'def': {'t': 'Margin of safety', 'd': 'the excess of actual (or budgeted) sales over the '
                    'break-even level of sales. It measures **how far sales can fall before the '
                    'business begins to make a loss**, and is usually expressed in units, in '
                    'sales value, or as a percentage of actual sales.'}},
      {'tex': '\\text{Margin of safety} = \\text{Actual sales} - \\text{Break-even sales} '
              '\\qquad\\qquad \\text{Margin of safety \\%} = '
              '\\frac{\\text{Margin of safety}}{\\text{Actual sales}} \\times 100'},
      {'h4': 'Working — the existing position'},
      {'stmt': {'t': 'Existing plant at 20,000 units (N)', 'rows': [
        ['Selling price per unit', '', 20.00],
        ['Contribution per unit  (P/V ratio 20% × N20)', '', 4.00],
        ['**Variable cost per unit**  (20 − 4)', '', 16.00, '@t'],
        '@gap',
        ['Total contribution  (20,000 × N4)', '', 80000],
        ['Net profit  (20,000 × N1.50)', '', 30000],
        ['**Fixed costs**  (80,000 − 30,000)', '', 50000, '@tt'],
      ]}},
      {'h4': '(b)  The revised P/V ratio with the new plant'},
      {'stmt': {'t': 'New plant — revised figures (N)', 'rows': [
        ['Selling price per unit  (20 − 4)', '', 16.00],
        ['Variable cost per unit  (16 − 4)', '', 12.00],
        ['**Contribution per unit**', '', 4.00, '@t'],
        ['**Revised P/V ratio**  (4 ÷ 16)', '', '**25%**', '@tt'],
        '@gap',
        ['Fixed costs  (50,000 + 15,000)', '', 65000],
      ]}},
      {'note': 'Contribution per unit is **unchanged at N4** — the N4 cut in price is exactly '
               'offset by the N4 saving in variable cost. But the **P/V ratio rises from 20% to '
               '25%**, because the same N4 of contribution is now a larger share of a smaller '
               'selling price. This is a useful reminder that a rising P/V ratio does not by '
               'itself mean the company is better off: here, each unit still earns the same N4, '
               'and fixed costs have gone up by N15,000.'},
      {'h4': '(c)  Units needed for a 50% increase in profit'},
      {'stmt': {'t': 'Target volume with the new plant', 'rows': [
        ['Maximum profit with the old plant  (20,000 × N1.50)', '', 'N30,000'],
        ['Target profit  (N30,000 + 50%)', '', 'N45,000'],
        '@gap',
        ['Fixed costs with the new plant', '', 'N65,000'],
        ['Add: target profit', '', 'N45,000'],
        ['**Total contribution required**', '', 'N110,000', '@t'],
        ['÷ contribution per unit', '', 'N4.00'],
        ['**Units required**', '', '27,500 units', '@tt'],
      ]}},
      {'p': '27,500 units is within the new plant\'s capacity of 30,000, so the target is '
            'attainable — provided the market will absorb 27,500 units at the reduced price of '
            'N16, a 37.5% increase in volume over the 20,000 units sold at N20.'},
      {'h4': '(d)  Margin of safety at 25,000 units with the new plant'},
      {'stmt': {'t': 'Margin of safety', 'rows': [
        ['Break-even units  (65,000 ÷ 4)', '', '16,250 units'],
        ['Actual sales', '', '25,000 units'],
        ['**Margin of safety in units**', '', '8,750 units', '@t'],
        ['**Margin of safety in sales value**  (8,750 × N16)', '', 'N140,000'],
        ['**Margin of safety as % of actual sales**  (8,750 ÷ 25,000)', '', '**35%**', '@tt'],
      ]}},
      {'note': 'Compare with the old plant: break-even was $50{,}000 \\div 4 = 12{,}500$ '
               'units, giving a margin of safety at full capacity of 7,500 units, or **37.5%** '
               'of sales. The new plant therefore operates at a slightly **lower** margin of '
               'safety at 25,000 units, despite the higher P/V ratio — because the extra '
               'N15,000 of fixed cost pushed break-even up by 3,750 units. Profit at 25,000 '
               'units would be $25{,}000 \\times 4 - 65{,}000 = N35{,}000$, against N30,000 '
               'on the old plant.'}]}},

    {'eg': {'tag': 'Exam type — Q9.8', 't': 'Five forms of pricing described',
      'q': [{'p': 'Briefly describe the following forms of pricing: (i) total cost-plus profit '
                  'percentage; (ii) marginal cost-plus contribution percentage; (iii) break-even '
                  'pricing; (iv) negotiated pricing; (v) competitors.'}],
      'a': [
      {'h4': '(i)  Total cost-plus profit percentage'},
      {'p': 'The price is set by adding a predetermined percentage profit to the **full cost** '
            'of the product — direct materials, direct labour, direct expenses and a share of '
            'both production and non-production overhead.'},
      {'tex': '\\text{Price} = \\text{Total cost} \\times '
              '(1 + \\text{profit percentage})'},
      {'p': '**For:** ensures every cost is recovered and a profit earned; simple; defensible to '
            'a customer who can inspect the cost; the normal basis for government and '
            'cost-reimbursement contracts. **Against:** it depends on an arbitrary overhead '
            'apportionment, so the "cost" is not objective; it ignores demand and the '
            'competition; it passes the supplier\'s inefficiency on to the customer; and it is '
            'circular, since the overhead per unit depends on the volume, which depends on the '
            'price.'},
      {'h4': '(ii)  Marginal cost-plus contribution percentage'},
      {'p': 'The price is set by adding a required contribution percentage to the **marginal '
            '(variable) cost** of the product. The resulting price must cover variable cost and '
            'make a contribution towards fixed costs and profit, but does not purport to recover '
            'a share of fixed cost in every unit.'},
      {'tex': '\\text{Price} = \\text{Marginal cost} \\times '
              '(1 + \\text{contribution percentage})'},
      {'p': '**For:** no arbitrary apportionment is involved; it is flexible, so a lower '
            'contribution can be accepted on marginal business, on an export order, or in a '
            'slack period; it is the right basis for short-run and special-order pricing. '
            '**Against:** total contribution must still cover total fixed costs, so if it is '
            'used as the normal basis there is a real risk of under-pricing and of making a loss '
            'while every individual sale appears profitable.'},
      {'h4': '(iii)  Break-even pricing'},
      {'p': 'The price is set at the level which exactly covers total cost at an expected volume '
            '— that is, which yields **no profit and no loss**. Equivalently, having fixed a '
            'price, the volume needed to break even is computed and the price tested against '
            'whether that volume is achievable.'},
      {'p': 'It is used as a **floor** rather than as a normal policy: to establish the minimum '
            'acceptable price below which business should be refused; to break into a new market '
            'or launch a product; to keep a factory occupied through a depression; or to '
            'discourage a competitor from entering. It is not sustainable in the long run, since '
            'no business survives without profit.'},
      {'h4': '(iv)  Negotiated pricing'},
      {'p': 'The price is arrived at by **bargaining between buyer and seller**, rather than '
            'computed from a formula or quoted from a list. It is used for large contracts, '
            'bespoke work, government and defence contracts, and transfers between divisions of '
            'the same group.'},
      {'p': 'Cost information is still essential — it tells the negotiator the floor below which '
            'the business is not worth taking, and the contribution at stake at each possible '
            'price — but the final price depends on bargaining strength, the urgency of the '
            'order on each side, the value of the relationship, and what each party believes '
            'about the other\'s alternatives.'},
      {'h4': '(v)  Competitors (competition-based pricing)'},
      {'p': 'The price is set by reference to **what competitors charge** rather than to the '
            'company\'s own cost — going-rate pricing (matching the market price), price '
            'leadership (following a dominant firm), or sealed-bid tendering (pricing to win '
            'against an unknown rival bid).'},
      {'p': '**For:** essential in a competitive market for a homogeneous product, where no '
            'supplier can charge more than the going rate and none needs to charge less; it '
            'reflects actual market conditions, which cost-plus ignores. **Against:** it takes '
            'no account of the company\'s own cost structure, so the market price may not cover '
            'that company\'s costs at all; and it surrenders the initiative to competitors '
            'whose costs and objectives may be quite different.'},
      {'key': 'In practice no company uses one method alone. **Cost** sets the floor below which '
              'a price should not go; **demand and competition** set the ceiling above which it '
              'cannot go; and the actual price is chosen between the two in the light of the '
              'company\'s objectives — market share, profit, capacity utilisation or long-term '
              'customer relationships.'}]}},

    {'eg': {'tag': 'Exam type — Q9.9 (ICAN PE II, May/June 1995)',
      't': 'Electrical Appliances Ltd — break-even and profit before and after an expansion',
      'q': [
      {'p': 'Electrical Appliances Ltd records and sells video films at **N30 each**. The '
            'results for 1993 and 1994 are summarised below:'},
      {'stmt': {'t': 'Results', 'rows': [
        ['Year', 'Sales (units)', 'Profit (N)', '@hd'],
        [1993, 6800, 23800],
        [1994, 8400, 39400],
      ]}},
      {'p': 'In 1993 and 1994 the company operated at an **average of 80% of the available '
            'capacity**. In 1995 it had budgeted to operate at **100% capacity**. In 1996 it '
            'proposes to acquire additional equipment worth **N150,000**, with an effective life '
            'of **10 years and no residual value**. With the new equipment the company proposes '
            'to operate at **150% of its present capacity**. **Variable costs will decrease by '
            '10%**, and the **selling price will be reduced by 5%** to enable all units produced '
            'to be sold.'},
      {'p': '**Required:** calculate (a) the break-even point of the company for 1995; (b) the '
            'forecast break-even point for 1996; (c) the forecast profit for 1995 and 1996; '
            '(d) the expected rate of return on the additional capital employed in 1996.'}],
      'a': [
      {'h4': 'Step 1 — the present cost structure, from the two years'},
      {'stmt': {'t': 'Deriving contribution and fixed cost', 'rows': [
        ['', '1993', '1994', 'Change', '@hd'],
        ['Units sold', 6800, 8400, 1600],
        ['Profit (N)', 23800, 39400, 15600],
      ]}},
      {'tex': '\\text{Contribution per unit} = \\frac{15{,}600}{1{,}600} = N9.75'},
      {'stmt': {'t': 'Present structure (N)', 'rows': [
        ['Selling price per unit', '', 30.00],
        ['Contribution per unit', '', 9.75],
        ['**Variable cost per unit**', '', 20.25, '@t'],
        ['**P/V ratio**  (9.75 ÷ 30)', '', '32.5%'],
        '@gap',
        ['Contribution, 1993  (6,800 × 9.75)', 66300, ''],
        ['Less: profit, 1993', 23800, ''],
        ['**Fixed costs**', '', 42500, '@t'],
        ['*Check, 1994:*  (8,400 × 9.75) − 42,500', '', '*N39,400 ✓*'],
      ]}},
      {'h4': 'Step 2 — the capacity'},
      {'stmt': {'t': 'Available capacity', 'rows': [
        ['Average units sold in 1993 and 1994  ((6,800 + 8,400) ÷ 2)', '', '7,600 units'],
        ['This represented 80% of available capacity', '', ''],
        ['**100% capacity**  (7,600 ÷ 0.80)', '', '9,500 units', '@tt'],
      ]}},
      {'h4': '(a)  Break-even point for 1995'},
      {'stmt': {'t': '1995 break-even', 'rows': [
        ['Fixed costs (unchanged)', '', 'N42,500'],
        ['÷ contribution per unit', '', 'N9.75'],
        ['**Break-even in units**', '', '4,359 units', '@t'],
        ['**Break-even in sales value**  (4,359 × N30)', '', 'N130,770', '@tt'],
      ]}},
      {'h4': '(b)  Forecast break-even point for 1996'},
      {'stmt': {'t': '1996 — the revised structure (N)', 'rows': [
        ['Selling price  (N30 less 5%)', '', 28.500],
        ['Variable cost per unit  (N20.25 less 10%)', '', 18.225],
        ['**Contribution per unit**', '', 10.275, '@t'],
        ['**P/V ratio**  (10.275 ÷ 28.50)', '', '36.05%'],
        '@gap',
        ['Fixed costs:  existing 42,500', 42500, ''],
        ['Add: depreciation on new equipment  (N150,000 ÷ 10 years)', 15000, 57500],
        '@gap',
        ['**Break-even in units**  (57,500 ÷ 10.275)', '', '5,596 units', '@t'],
        ['**Break-even in sales value**  (5,596 × N28.50)', '', 'N159,486', '@tt'],
      ]}},
      {'h4': '(c)  Forecast profit for 1995 and 1996'},
      {'stmt': {'t': 'Forecast profit (N)', 'rows': [
        ['', '1995  (100% capacity)', '1996  (150% of capacity)', '@hd'],
        ['Units  (9,500;  9,500 × 1.5)', 9500, 14250],
        ['Contribution per unit', 9.750, 10.275],
        ['**Total contribution**', 92625, 146419, '@t'],
        ['Less: fixed costs', 42500, 57500],
        ['**Forecast profit**', 50125, 88919, '@tt'],
      ]}},
      {'h4': '(d)  Expected rate of return on the additional capital employed in 1996'},
      {'stmt': {'t': 'Return on the new investment (N)', 'rows': [
        ['Forecast profit, 1996', '', 88919],
        ['Less: forecast profit, 1995', '', 50125],
        ['**Increase in profit attributable to the investment**', '', 38794, '@t'],
        ['Additional capital employed', '', 150000],
        ['**Expected rate of return**  (38,794 ÷ 150,000)', '', '**25.9%**', '@tt'],
      ]}},
      {'key': 'A 25.9% return on the N150,000 is attractive, and the expansion should be '
              'recommended — but note what it depends on. The selling price is cut by 5% '
              '**specifically to enable all 14,250 units to be sold**, a 50% increase in volume. '
              'If the market will not in fact absorb 14,250 units, the company is left with '
              'N15,000 more fixed cost, a 5% lower price, and a break-even point that has risen '
              'from 4,359 to 5,596 units. The project is sound, but its risk is concentrated '
              'entirely in the sales forecast.'},
      {'note': 'The return calculated here is the simple **accounting rate of return** on the '
               'additional investment. It ignores the timing of the cash flows; Chapter 11\'s '
               'discounted-cash-flow methods would give a more complete appraisal.'}]}},

    {'eg': {'tag': 'Exam type — Q9.10 (12½ marks)',
      't': 'Tom Limited — the principal budget factor and a profit-volume graph',
      'q': [
      {'p': 'Tom Limited manufactures a single product. The unit selling price is fixed at '
            '**N40.00 per unit**. Other data for the 2017 budgeted year are:'},
      {'stmt': {'t': 'Budget data for 2017', 'rows': [
        ['Sales', '', 'N600,000,000'],
        ['Variable cost — production', '', 'N16 per unit'],
        ['Variable cost — others', '', 'N8 per unit'],
        ['Total fixed cost', '', 'N40,000,000'],
      ]}},
      {'p': 'Management is of the view that the budget preparation is realistic, provided all '
            'departments co-operate. **The budget for 2017 is 80% of the 2016 budget because of '
            'the recession in the economy.**'},
      {'p': '**Required:** **(a)(i)** define the principal budget factor; **(a)(ii)** what is '
            'the principal budget factor for 2017? **(b)** produce a profit-volume graph for the '
            '2017 budget year. **(c)** From your graph determine (i) the break-even point; '
            '(ii) the P/V ratio; (iii) the margin of safety; (iv) the profit when sales are '
            'N160,000,000.'}],
      'a': [
      {'h4': '(a)(i)  The principal budget factor'},
      {'def': {'t': 'Principal budget factor', 'd': 'the factor which **limits the activities of '
                    'an organisation** and around which all other budgets are built. Also called '
                    'the **limiting factor**, the **key factor** or the **governing factor**.'}},
      {'p': 'It must be identified **first**, before any budget is prepared, because every other '
            'budget has to be constructed in the light of it. If sales demand is the limiting '
            'factor, the sales budget is prepared first and production, materials, labour and '
            'cash budgets follow from it; if machine capacity is the limiting factor, the '
            'production budget comes first and the sales budget must be cut to match. Preparing '
            'budgets in the wrong order produces a plan the company cannot execute.'},
      {'p': 'Common principal budget factors: **sales demand** (the most usual), raw material '
            'availability, skilled labour availability, machine or plant capacity, factory '
            'space, cash, and management expertise.'},
      {'h4': '(a)(ii)  The principal budget factor for 2017'},
      {'p': '**Sales demand.** The question states that the 2017 budget is only **80% of the '
            '2016 budget because of the recession in the economy** — the company is not '
            'constrained by its ability to make the product, nor by materials, labour or cash, '
            'but by what the market will buy. Nothing in the data suggests a production '
            'constraint, and the budget has been scaled down specifically in response to demand '
            'conditions.'},
      {'h4': 'Working — the figures behind the graph'},
      {'stmt': {'t': '2017 budget analysed (N)', 'rows': [
        ['Sales value', '', 600000000],
        ['÷ selling price per unit', '', 'N40'],
        ['**Budgeted units**', '', '15,000,000 units', '@t'],
        '@gap',
        ['Selling price per unit', '', 40],
        ['Less: variable cost per unit  (16 production + 8 other)', '', 24],
        ['**Contribution per unit**', '', 16, '@t'],
        ['**P/V ratio**  (16 ÷ 40)', '', '**40%**'],
        '@gap',
        ['Total contribution  (15,000,000 × N16)', '', 240000000],
        ['Less: total fixed cost', '', 40000000],
        ['**Budgeted profit**', '', 200000000, '@tt'],
      ]}},
      {'h4': '(b)  Profit-volume graph for 2017'},
      {'p': 'A P/V graph plots **profit (vertical axis) against sales value (horizontal axis)**. '
            'It is a single straight line starting at a **loss equal to the fixed cost** when '
            'sales are nil, and rising at the rate of the **P/V ratio** — here 40 kobo of profit '
            'for every naira of sales. It crosses the horizontal axis at the **break-even '
            'point**.'},
      {'pre': 'Profit\n'
              'N\'m\n'
              ' 200 |                                                            * (600, 200)\n'
              '     |                                                      /\n'
              ' 150 |                                                /\n'
              '     |                                          /\n'
              ' 100 |                                    /\n'
              '     |                              /\n'
              '  50 |                        /\n'
              '     |                  /\n'
              '  24 |- - - - - -*(160, 24)\n'
              '   0 +-----*------+---------+---------+---------+---------+------> Sales N\'m\n'
              '     |   /100     200       300       400       500       600\n'
              ' -40 |* (0, −40)      <------ margin of safety N500m ------>\n'
              '     |\n'
              '  Loss\n'
              '\n'
              '  The line passes through (0, −40) and (600, 200);  slope = P/V ratio = 40%.\n'
              '  It crosses the sales axis at N100m — the break-even point.'},
      {'h4': '(c)  Reading the answers from the graph'},
      {'stmt': {'t': 'Answers (N)', 'rows': [
        ['**(i)  Break-even point**  (fixed cost ÷ P/V ratio = 40,000,000 ÷ 0.40)', '',
         'N100,000,000  *(2,500,000 units)*'],
        ['**(ii) P/V ratio**  (contribution ÷ sales = 16 ÷ 40)', '', '40%'],
        ['**(iii) Margin of safety**  (600,000,000 − 100,000,000)', '',
         'N500,000,000  *(83.3% of budgeted sales)*'],
        ['**(iv) Profit when sales are N160,000,000**  ((40% × 160,000,000) − 40,000,000)', '',
         'N24,000,000'],
      ]}},
      {'key': 'A margin of safety of **83.3%** is exceptionally comfortable — sales could fall by '
              'more than five-sixths before the company made a loss. That is the mark of a '
              'business with **low operating gearing**: fixed costs are only N40 million against '
              'N240 million of contribution. Compare it with the company in Q9.1 above, whose '
              'margin of safety was 21.7%, and the difference in risk is obvious. It also '
              'explains why Tom Limited can absorb an 80%-of-last-year budget without '
              'difficulty, where a highly geared company could not.'}]}},
  ]},

 ],
 'formulas': [
  {'lb': 'BEP, units', 'tex': '\\dfrac{FC}{\\text{Contribution per unit}}'},
  {'lb': 'BEP, money value', 'tex': '\\dfrac{FC}{\\text{P/V Ratio}}'},
  {'lb': 'P/V ratio', 'tex': '\\dfrac{S - V}{S}'},
  {'lb': 'Margin of safety, value', 'tex': 'S_f - S_b'},
  {'lb': 'Margin of safety, %', 'tex': '\\dfrac{S_f - S_b}{S_f} \\times 100'},
  {'lb': 'Sales for a target profit, units', 'tex': '\\dfrac{FC + \\text{Target Profit}}'
   '{\\text{Contribution per unit}}'},
  {'lb': 'Weighted P/V ratio, multi-product', 'tex': '\\dfrac{\\text{Total contribution, all '
   'products}}{\\text{Total sales revenue, all products}}'},
 ],
 'focus':
   'CVP is arguably the most exam-favoured topic in the whole paper, precisely because it '
   'combines cleanly with marginal costing (Chapter 9) into long, multi-part Section B '
   'questions like Illustration 10.2. Learn the P/V ratio\'s three equivalent formulas as one '
   'idea, not three separate ones — whichever inputs a question gives you, one of the three '
   'forms will use them directly. For an after-tax profit target, always convert to the before-'
   'tax equivalent by *dividing* by (1 − tax rate), never multiplying.',
 'errors': [
   'Multiplying an after-tax target profit by (1 − tax rate) instead of dividing by it, when '
   'converting to the before-tax equivalent needed in the standard formula.',
   'Reading "P/V ratio × sales = profit" directly — it actually gives *contribution*, which '
   'only becomes profit once fixed costs are fully covered.',
   'Assuming fixed cost is genuinely constant across the whole chart, rather than recognising '
   'it usually behaves as a stepped cost in reality (Chapter 10.4, limitation 1).',
   'Using the plain single-product BEP formula for a business selling several products in '
   'varying proportions — that needs the *weighted* C/S ratio instead.',
   'Confusing the break-even chart (cost and revenue as two separate lines) with the P/V chart '
   '(profit plotted directly as one line) — they answer the same question but are drawn '
   'completely differently.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A product has a selling price of N15 and a variable cost of N9 per unit. Fixed costs '
         'are N60,000. The break-even point in units is',
    'o': ['4,000 units', '6,667 units', '10,000 units', '15,000 units', '9,000 units'],
    'a': 1,
    'w': 'Unit contribution = 15 − 9 = N6. BEP = 60,000 / 6 = 10,000 units.',
    'calc': '\\dfrac{60{,}000}{15-9} = 10{,}000',
    'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'Forecast sales are N500,000 and break-even sales are N350,000. The margin of safety '
         'ratio is',
    'o': ['30%', '70%', '43%', '150%', '100%'],
    'a': 0,
    'w': 'M/S ratio = (Sf − Sb)/Sf × 100 = (500,000 − 350,000)/500,000 × 100 = 30%.',
    'calc': '\\dfrac{500{,}000-350{,}000}{500{,}000} \\times 100 = 30\\%',
    'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'The P/V ratio of a product is 40%. If sales are N250,000, contribution is',
    'o': ['N100,000', 'N150,000', 'N40,000', 'N625,000', 'N10,000'],
    'a': 0,
    'w': 'Contribution = P/V ratio × Sales = 0.40 × 250,000 = N100,000.',
    'calc': '0.40 \\times 250{,}000 = 100{,}000',
    'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'A company wants an after-tax profit of N120,000, with tax at 25%. The equivalent '
         'before-tax profit target is',
    'o': ['N90,000', 'N160,000', 'N145,000', 'N120,000', 'N30,000'],
    'a': 1,
    'w': 'Before-tax profit = after-tax profit ÷ (1 − tax rate) = 120,000 / 0.75 = N160,000.',
    'calc': '\\dfrac{120{,}000}{1-0.25} = 160{,}000',
    'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'On a Profit-Volume (P/V) chart, the profit line crosses the Y-axis (at zero sales) at '
         'a value equal to',
    'o': ['zero', 'total variable cost', 'negative total fixed cost',
          'total sales revenue', 'the break-even point'],
    'a': 2,
    'w': 'At zero sales there is no contribution to offset fixed cost, so the loss shown equals '
         'the total fixed cost — plotted as a negative value on the profit axis.',
    'src': 'Chapter 10.3', 'sec': '10.3'},
   {'q': 'Which of the following is explicitly listed as a limitation of break-even analysis?',
    'o': ['It assumes fixed costs are always perfectly stepped, never constant',
          'It assumes variable cost and sales behave in a straight line, when real effects like '
          'bulk discounts make them curve', 'It cannot be combined with marginal costing',
          'It only works for single-year budgets', 'It requires knowledge of tax rates'],
    'a': 1,
    'w': 'One of the stated limitations is that the assumed linearity of variable cost and sales '
         'is unrealistic — discounts, overtime premiums and similar effects make them curve '
         'rather than run in a straight line.',
    'src': 'Chapter 10.4', 'sec': '10.4'},
   {'q': 'For a firm selling several products in a genuinely varying sales mix, the correct '
         'break-even point formula uses',
    'o': ['the P/V ratio of its single most profitable product only',
          'a simple average of each product\'s own P/V ratio',
          'a weighted P/V ratio (total contribution of all products ÷ total sales revenue of '
          'all products)', 'the highest-selling-price product\'s fixed costs only',
          'zero — BEP cannot be found for a multi-product firm'],
    'a': 2,
    'w': 'A varying sales mix needs the weighted C/S (P/V) ratio — total contribution across '
         'all products divided by total sales revenue across all products — not any single '
         'product\'s own ratio.',
    'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'Which of these is an assumption underlying CVP/break-even analysis?',
    'o': ['The selling price may change freely as volume changes',
          'Fixed costs vary proportionally with activity',
          'Total fixed costs remain constant throughout the relevant range',
          'Production and sales are never synchronised',
          'The general price level is expected to change constantly'],
    'a': 2,
    'w': 'One of the core assumptions is that total fixed costs stay constant across the '
         'relevant activity range — the other options each contradict a stated assumption.',
    'src': 'Chapter 10.2', 'sec': '10.2'},
  ],
  'theory': [
   {'q': 'Explain the term \'break-even point\'. Give an example illustrating your answer, and '
         'mention the types of problems an accountant can expect to solve with the help of such '
         'analysis.',
    'marks': 10,
    'a': [
      {'p': 'The break-even point is the level of activity at which total cost exactly equals '
            'total revenue, so profit is zero — beyond it, every additional unit\'s contribution '
            'adds directly to profit, since fixed cost is already fully covered.'},
      {'p': '**Example**: a product selling at N9/unit with variable cost N5/unit (contribution '
            'N4) and fixed cost N2,000 breaks even at 2,000/4 = 500 units.'},
      {'p': '**Problems it helps solve**: the sales volume needed to avoid a loss; the safety '
            'margin built into a budget; the units needed for a target profit; the effect of a '
            'price change on required volume; and whether a proposed special order, price cut '
            'or cost increase is worth accepting.'},
    ], 'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'Explain the Cost-Volume-Profit relationship. How would a change in the selling price '
         'affect it?',
    'marks': 8,
    'a': [
      {'p': 'CVP analysis studies how total cost, total revenue and profit move together as '
            'sales volume changes — it is the profit structure of the business, expressed '
            'through the interaction of these three forces.'},
      {'p': 'A **price increase** raises contribution per unit (assuming variable cost is '
            'unchanged), which **lowers** the break-even point (fewer units are needed to cover '
            'fixed costs) and raises the P/V ratio — every unit sold beyond BEP now contributes '
            'more to profit. A **price decrease** has the opposite effect: contribution per '
            'unit falls, the break-even point rises, and more units must be sold just to '
            'maintain the same profit level.'},
    ], 'src': 'Chapter 10.1', 'sec': '10.1'},
  ]},
}
