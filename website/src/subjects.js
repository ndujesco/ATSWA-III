/* ATSWA Part III subjects. Chapter content lives in data/<file>.js and is
   fetched the first time a subject is opened. Only subjects with real
   authored content should be listed here — aud/tax/man are added once their
   own chapters exist (see ../PLAN.md Part D). */
var SUBJECTS = [
  { code: 'CA', file: 'ca', n: 15, name: 'Cost Accounting',
    blurb: 'From the three elements of cost through job, batch, contract and process costing to marginal costing, CVP analysis, budgeting, standard costing and cost reduction — the calculation-heavy core of Part III.' },
  { code: 'AUD', file: 'aud', n: 12, name: 'Principles of Auditing & Assurance',
    blurb: 'What an audit is and why it exists, the CAMA/BOFIA/Insurance Act regulatory framework, ethics, planning, evidence, internal control, public sector assurance, IT-based audit techniques, reporting and audit completion.' },
  { code: 'TAX', file: 'tax', n: 25, name: 'Taxation',
    blurb: 'The Nigerian tax system under the newly-consolidated Nigeria Tax Act 2025 and Nigeria Tax Administration Act 2025 — administration, VAT, withholding tax, customs and excise, personal and companies income tax, capital allowances, chargeable gains and more.' },
  { code: 'MAN', file: 'man', n: 10, name: 'Management',
    blurb: 'The nature of business and its environment, management theory and process, the organic business functions, managing work relationships, business process re-engineering, organisational effectiveness, office practice, contemporary management issues, and entrepreneurship.' }
];

var GUIDES = [];
