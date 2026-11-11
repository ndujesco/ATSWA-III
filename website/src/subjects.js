/* ATSWA Part III subjects. Chapter content lives in data/<file>.js and is
   fetched the first time a subject is opened. Only subjects with real
   authored content should be listed here — aud/tax/man are added once their
   own chapters exist (see ../PLAN.md Part D). */
var SUBJECTS = [
  { code: 'CA', file: 'ca', n: 15, name: 'Cost Accounting', icon: 'calculator',
    summary: 'Make the numbers make sense. Costing, budgets, variances and decisions, with every working laid out.',
    blurb: 'From the three elements of cost through job, batch, contract and process costing to marginal costing, CVP analysis, budgeting, standard costing and cost reduction — the calculation-heavy core of Part III.' },
  { code: 'AUD', file: 'aud', n: 12, name: 'Principles of Auditing & Assurance', icon: 'shield',
    summary: 'Build a sound audit approach, from ethics and planning to evidence, assurance and the final report.',
    blurb: 'What an audit is and why it exists, the CAMA/BOFIA/Insurance Act regulatory framework, ethics, planning, evidence, internal control, public sector assurance, IT-based audit techniques, reporting and audit completion.' },
  { code: 'TAX', file: 'tax', n: 25, name: 'Taxation', icon: 'receipt',
    summary: 'Work through the Nigerian tax system with the 2026 text, worked computations and notes on changed law.',
    blurb: 'The Nigerian tax system under the newly-consolidated Nigeria Tax Act 2025 and Nigeria Tax Administration Act 2025 — administration, VAT, withholding tax, customs and excise, personal and companies income tax, capital allowances, chargeable gains and more.' },
  { code: 'MAN', file: 'man', n: 10, name: 'Management', icon: 'people',
    summary: 'Connect the ideas behind good management: people, organisations, strategy and entrepreneurship.',
    blurb: 'The nature of business and its environment, management theory and process, the organic business functions, managing work relationships, business process re-engineering, organisational effectiveness, office practice, contemporary management issues, and entrepreneurship.' }
];

var GUIDES = [{tag:'TAX · 2026', title:'Old papers, current tax rules',
  blurb:'What changed, how to read the flags, and a worked comparison of personal income tax.',
  href:'guides/tax-transition.html'}];
