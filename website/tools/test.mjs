/* Headless UI regressions. npm install --no-save jsdom, or set JSDOM to an
 * existing node_modules/jsdom directory. No runtime site dependencies. */
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const { JSDOM, VirtualConsole } = await import(process.env.JSDOM
  ? pathToFileURL(join(process.env.JSDOM, 'lib/api.js')).href : 'jsdom');
const errors = [], scrolled = [];
const virtualConsole = new VirtualConsole();
virtualConsole.on('jsdomError', error => errors.push(error.message));
const dom = new JSDOM(readFileSync(join(root, 'index.html'), 'utf8'), {
  url: 'https://atswa3.test/#/', runScripts: 'dangerously', pretendToBeVisual: true,
  virtualConsole,
  beforeParse(w) {
    w.scrollTo = () => {};
    w.HTMLElement.prototype.scrollIntoView = function () { scrolled.push(this.id); };
    w.MathMLElement = function () {};
    w.localStorage.setItem('atswa2:prog', JSON.stringify({
      'CA/1': { read: 123 }, 'FA/1': { read: 456 },
    }));
    const append = w.Node.prototype.appendChild;
    w.Node.prototype.appendChild = function (node) {
      const src = node?.tagName === 'SCRIPT' ? node.getAttribute('src') : null;
      if (src?.startsWith('data/')) {
        const path = join(root, src);
        if (existsSync(path)) w.eval(readFileSync(path, 'utf8'));
        else node.onerror?.();
        return node;
      }
      return append.call(this, node);
    };
  },
});
const w = dom.window, A = w.ATSWA, doc = w.document;
const tick = (ms = 0) => new Promise(resolve => setTimeout(resolve, ms));
let passed = 0, failed = 0;
async function test(name, fn) {
  try { await fn(); passed++; console.log('ok  ' + name); }
  catch (error) { failed++; console.error('FAIL ' + name + ': ' + error.stack); }
}
function view(route) {
  w.history.replaceState(null, '', route);
  A.quizClear(); A.render(); A.tabs();
  return doc.getElementById('view');
}
function has(element, text) { assert.ok(element.textContent.includes(text), 'Missing ' + text); }
await tick();

await test('home identifies Part III, all four subjects and current inventory', () => {
  const page = view('#/');
  for (const subject of ['Cost Accounting', 'Principles of Auditing', 'Taxation', 'Management']) has(page, subject);
  has(page, '60'); has(page, '3,360'); has(page, '62');
  assert.equal(doc.querySelectorAll('title').length, 1);
  assert.ok(!page.textContent.includes('undefined'));
});

await test('Part III preserves its legacy progress and isolates Part II', () => {
  assert.equal(A.PK, 'atswa3:');
  assert.equal(A.prog()['CA/1'].read, 123);
  assert.equal(A.prog()['FA/1'], undefined);
  assert.equal(JSON.parse(w.localStorage.getItem('atswa2:prog'))['FA/1'].read, 456);
});

await test('every authored chapter renders its actual section targets', () => {
  for (const [code, count] of Object.entries({ AUD: 12, CA: 15, TAX: 25, MAN: 10 })) {
    const subject = view('#/s/' + code);
    assert.equal(subject.querySelectorAll('.chrow').length, count);
    for (let n = 1; n <= count; n++) {
      const page = view('#/s/' + code + '/' + n);
      const chapter = A.DATA[code].chapters.find(ch => ch.n === n);
      for (const section of chapter.secs) {
        assert.ok(doc.getElementById('sec-' + String(section.n).replaceAll('.', '-')), `${code}/${n}/${section.n}`);
        for (const block of section.b) {
          if ((block.h3 || block.h4) && block.id) assert.ok(doc.getElementById(block.id), block.id);
        }
      }
      assert.ok(page.querySelector('h1'));
    }
  }
});

await test('all 60 paper reading views contain all 56 questions and solutions', () => {
  view('#/exams');
  assert.equal(doc.querySelectorAll('.dietcard').length, 60);
  for (const paper of A.DATA.EXAMS.papers) {
    const page = view(`#/exams/${paper.diet}/${paper.subject}`);
    assert.equal(page.querySelectorAll('.bq > .h').length, 36, paper.diet + '/' + paper.subject);
    assert.equal(page.querySelectorAll('.saqrow').length, 20);
    assert.equal(page.querySelectorAll('.sol').length, 6);
    assert.ok(!page.textContent.includes('undefined'));
    assert.ok(!page.textContent.includes('Part II paper'));
  }
});

await test('question flags render for MCQ, short answers and essays', () => {
  const page = view('#/exams/2019-03/TAX');
  has(page, '50,000'); has(page, 'Nigeria Revenue Service');
  assert.ok(page.querySelector('.saqrow .flagbox'));
  assert.ok(page.querySelector('.bq > .flagbox'));
  assert.ok(page.querySelector('.flagbox a[href^="https://nass.gov.ng/"]'));
});

await test('visual source recoveries and original workings are available', () => {
  let page = view('#/exams/2024-09/MAN');
  assert.ok(page.querySelector('img[src="assets/source-figures/2024-09-p83.png"]'));
  page = view('#/exams/2021-09/CA');
  has(page, '102.4%'); has(page, '93.75%');
  assert.ok(page.querySelector('img[src="assets/source-figures/2021-09-p51.png"]'));
  page = view('#/exams/2019-03/TAX'); has(page, 'Worldwide Income');
  assert.ok(page.querySelector('details.exm'));
});

await test('source defects and all accepted MCQ answers remain visible', () => {
  let page = view('#/exams/2020-03/MAN'); has(page, 'source prints question 16'); has(page, 'F–J');
  page = view('#/exams/2024-03/TAX'); has(page, 'only four options');
  page = view('#/exams/2023-03/TAX'); has(page, 'A or E'); has(page, 'E or B');
  page = view('#/exams/2023-03/AUD'); has(page, 'bonus mark');
});

await test('every timed paper receives 30 MCQ and 26 written questions', () => {
  const start = A.quizStart;
  let config;
  A.quizStart = value => { config = value; };
  try {
    for (const paper of A.DATA.EXAMS.papers) {
      view(`#/exams/${paper.diet}/${paper.subject}/sit`);
      assert.equal(config.mcq.length, 30);
      assert.equal(config.theory.length, 26);
      assert.ok(config.exam);
      assert.ok(config.mcq.every(q => q.bonus || q.accepted.length));
      if (paper.subject === 'TAX') assert.ok(config.theory.some(q => q.flag));
    }
  } finally { A.quizStart = start; }
});

await test('practice scoring accepts a second official answer and awards an unanswered bonus', () => {
  A.quizStart({ key: 'regression-key', title: 'Key regression', back: '#/exams',
    mcq: [
      { q: 'Dual answer', o: ['A', 'B', 'C', 'D', 'E'], ...A.keyInfo('A/E') },
      { q: 'Bonus', o: ['A', 'B', 'C', 'D', 'E'], ...A.keyInfo('BONUS') },
    ], theory: [] });
  doc.querySelector('[data-pick="4"]').click();
  has(doc.getElementById('view'), 'Why that is right');
  doc.querySelector('[data-jump]').click();
  doc.querySelector('[data-phase="results"]').click();
  has(doc.getElementById('view'), '2 of 2');
  has(doc.getElementById('view'), '100%');
});

await test('chapter practice includes past questions, their flags and section citations', () => {
  for (const code of ['AUD', 'CA', 'TAX', 'MAN']) {
    let past = 0;
    for (const chapter of A.DATA[code].chapters) {
      const questions = A.chapterQuestions(code, chapter.n, chapter, A.DATA.EXAMS);
      past += questions.mcq.filter(q => q.past).length;
      assert.ok(questions.mcq.every(q => q.bonus || q.a >= 0));
    }
    assert.ok(past > 300, code + ': past questions missing');
  }
});

await test('real citations land and highlight numeric and lettered sections', async () => {
  for (const code of ['AUD', 'CA', 'TAX', 'MAN']) {
    const paper = A.DATA.EXAMS.papers.find(p => p.subject === code && p.mcq.some(q => q.sec));
    const question = paper.mcq.find(q => q.sec && (code !== 'MAN' || /^[A-Z]/.test(q.sec)));
    assert.ok(question);
    view(`#/exams/${paper.diet}/${code}`);
    const href = `#/s/${code}/${question.ch}?sec=${question.sec.replaceAll('.', '-')}`;
    const link = doc.querySelector(`a[href="${href}"]`);
    assert.ok(link);
    link.click(); await tick(80);
    const id = 'sec-' + question.sec.replaceAll('.', '-');
    assert.ok(doc.getElementById(id).classList.contains('landed'));
    assert.ok(scrolled.includes(id));
  }
});

await test('in-chapter TOC jumps retain the chapter and a stale citation is safe', async () => {
  view('#/s/MAN/1');
  const title = doc.querySelector('h1').textContent;
  w.location.hash = '#sec-A-1';
  w.dispatchEvent(new w.Event('hashchange')); await tick();
  assert.equal(doc.querySelector('h1').textContent, title);
  view('#/s/MAN/1?sec=missing');
  assert.equal(doc.querySelector('h1').textContent, title);
});

await test('final revision renders every subject and question type with source links and notes', () => {
  view('#/revision'); has(doc.getElementById('view'), '15 diets');
  for (const code of ['AUD', 'CA', 'TAX', 'MAN']) {
    for (const kind of ['mcq', 'saq', 'essay']) {
      const page = view(`#/revision/${code}/${kind}`);
      assert.ok(page.querySelector('[data-years]'), code + '/' + kind);
      assert.ok(page.querySelector('a[href^="#/exams/"]'), 'Original diet link missing');
      const sourceKind = kind === 'essay' ? 'secb' : kind;
      assert.ok([...page.querySelectorAll('a[href^="#/exams/"]')].every(link =>
        link.getAttribute('href').includes('?q=' + sourceKind + '-')), 'Exact original question missing');
      assert.ok(!page.textContent.includes('undefined'));
      if (code === 'TAX') assert.ok(page.querySelector('.flagbox'));
    }
  }
  const page = view('#/revision/TAX/mcq');
  doc.getElementById('revYearFrom').value = '2026';
  doc.getElementById('revYearTo').value = '2026';
  doc.getElementById('revYearTo').dispatchEvent(new w.Event('change'));
  assert.ok(page.querySelectorAll('[data-years]:not(.hid)').length > 0);
  assert.ok(page.querySelectorAll('[data-years].hid').length > 0);
});

await test('study desk resumes the last chapter at its saved section', () => {
  view('#/s/CA/3?sec=3-2');
  const resume = A.get(A.PK + 'resume');
  assert.equal(resume.code, 'CA'); assert.equal(resume.n, 3); assert.equal(resume.sec, '3-2');
  view('#/');
  assert.equal(doc.getElementById('continue-study').getAttribute('href'), '#/s/CA/3?sec=3-2');
  has(doc.querySelector('.session-card'), A.DATA.CA.chapters[2].t);
  assert.ok(doc.querySelector('.mark').textContent.includes('Part III'));
});

await test('chapter finder filters, shows an empty state, and restores all chapters', () => {
  view('#/s/TAX');
  const input = doc.getElementById('chapter-filter');
  input.value = 'capital allowances'; input.dispatchEvent(new w.Event('input'));
  const matches = doc.querySelectorAll('.chrow:not(.hide)');
  assert.ok(matches.length > 0 && matches.length < 25);
  assert.ok([...matches].some(row => row.textContent.includes('Capital Allowances')));
  input.value = 'zzzz-no-such-chapter'; input.dispatchEvent(new w.Event('input'));
  assert.equal(doc.querySelectorAll('.chrow:not(.hide)').length, 0);
  assert.ok(!doc.getElementById('chapter-empty').classList.contains('hide'));
  input.value = ''; input.dispatchEvent(new w.Event('input'));
  assert.equal(doc.querySelectorAll('.chrow:not(.hide)').length, 25);
});

await test('paper filters combine subject and year and preserve the selected year', async () => {
  view('#/exams?s=CA&y=2025');
  assert.equal(doc.querySelectorAll('.dietcard').length, 2);
  assert.ok([...doc.querySelectorAll('.dietcard')].every(card => /2025-\d\d\/CA$/.test(card.getAttribute('href'))));
  assert.ok([...doc.querySelectorAll('a.filter-chip')].some(link => link.getAttribute('href') === '#/exams?s=TAX&y=2025'));
  doc.getElementById('paper-year').value = '2026';
  doc.getElementById('paper-year').dispatchEvent(new w.Event('change'));
  await tick(40);
  assert.equal(doc.querySelectorAll('.dietcard').length, 1);
  has(doc.querySelector('.paper-count'), 'Cost Accounting');
});

await test('search opens the exact section and returns keyboard focus when dismissed', async () => {
  view('#/');
  doc.getElementById('btn-search').click();
  const input = doc.getElementById('srch-i');
  assert.equal(doc.activeElement, input);
  input.value = 'capital allowance'; input.dispatchEvent(new w.Event('input'));
  const hit = doc.querySelector('.srch .hit[href*="?sec="]');
  assert.ok(hit, 'No section results');
  const href = hit.getAttribute('href'), section = href.split('?sec=')[1];
  assert.ok(!href.includes('#sec-'));
  hit.click(); await tick(80);
  assert.ok(doc.getElementById('sec-' + section));
  assert.ok(!doc.getElementById('srch').classList.contains('on'));
  doc.getElementById('btn-search').click();
  input.dispatchEvent(new w.KeyboardEvent('keydown', {key:'Escape', bubbles:true}));
  assert.equal(doc.activeElement, doc.getElementById('btn-search'));
  assert.ok(!doc.body.classList.contains('search-open'));
});

await test('chapter references open the exact past-paper question', async () => {
  view('#/s/CA/1');
  const link = doc.querySelector('.pqrow[href*="?q="]');
  assert.ok(link);
  const question = link.getAttribute('href').split('?q=')[1];
  link.click(); await tick(60);
  const target = doc.getElementById('q-' + question);
  assert.ok(target && target.classList.contains('question-landed'));
  assert.ok(scrolled.includes(target.id));
});

await test('mobile chapter contents use reloadable section routes', () => {
  view('#/s/MAN/1');
  const link = doc.querySelector('.reader-index a');
  assert.ok(link.getAttribute('href').startsWith('#/s/MAN/1?sec='));
  const target = 'sec-' + link.getAttribute('href').split('?sec=')[1];
  assert.ok(doc.getElementById(target));
});

await test('progress chapters are actionable and clearing progress stays cleared', async () => {
  view('#/progress');
  assert.equal(doc.querySelectorAll('a.heat-cell').length, 62);
  doc.querySelector('a.heat-cell').click(); await tick(50);
  assert.ok(doc.querySelector('.chead'));
  A.set(A.PK + 'theme', 'dark');
  view('#/progress');
  doc.getElementById('wipe').click();
  assert.ok(Object.keys(A.prog()).length > 0, 'First click cleared progress');
  doc.getElementById('wipe').click();
  assert.equal(Object.keys(A.prog()).length, 0);
  assert.equal(A.get(A.PK + 'resume', null), null);
  assert.equal(A.get(A.PK + 'legacy-migrated'), true);
  assert.equal(A.get(A.PK + 'theme'), 'dark');
  assert.ok(w.localStorage.getItem('atswa2:prog'), 'Part II progress changed');
});

await test('slow subject loads and rapid search typing do not replace the current view', async () => {
  const cold = new JSDOM(readFileSync(join(root, 'index.html'), 'utf8'), {
    url: 'https://atswa3.test/#/', runScripts: 'dangerously', pretendToBeVisual: true,
    virtualConsole,
    beforeParse(win) {
      win.scrollTo = () => {};
      win.HTMLElement.prototype.scrollIntoView = () => {};
      const append = win.Node.prototype.appendChild;
      win.Node.prototype.appendChild = function (node) {
        const src = node?.tagName === 'SCRIPT' ? node.getAttribute('src') : null;
        if (src?.startsWith('data/')) {
          win.setTimeout(() => win.eval(readFileSync(join(root, src), 'utf8')), 60);
          return node;
        }
        return append.call(this, node);
      };
    },
  });
  try {
    await tick();
    const win = cold.window, page = win.document;
    win.history.replaceState(null, '', '#/s/AUD'); win.ATSWA.render();
    win.history.replaceState(null, '', '#/s/TAX'); win.ATSWA.render();
    await tick(150);
    assert.equal(page.querySelector('h1').textContent, 'Taxation');
    assert.equal(page.querySelectorAll('.chrow').length, 25);
    page.getElementById('btn-search').click();
    const input = page.getElementById('srch-i');
    input.value = 'capital'; input.dispatchEvent(new win.Event('input'));
    input.value = 'audit'; input.dispatchEvent(new win.Event('input'));
    await tick(150);
    const hits = page.querySelectorAll('.srch .hit');
    assert.ok(hits.length > 0, 'Search lost its pending callback');
    assert.ok([...hits].every(hit => /audit/i.test(hit.textContent)));
    assert.equal(page.querySelector('h1').textContent, 'Taxation');
  } finally { cold.window.close(); }
});

await test('reviewed keys preserve the printed key and drive practice scoring', () => {
  view('#/exams/2022-03/CA');
  const original = doc.getElementById('q-mcq-19');
  has(original, 'REVIEWED'); has(original, 'PRINTED KEY');
  const paper = A.DATA.EXAMS.papers.find(p => p.diet === '2022-03' && p.subject === 'CA');
  assert.equal(paper.key[19], 'C');
  assert.equal(paper.mcq[18].studyKey, 'A');
  let config; const start = A.quizStart;
  A.quizStart = value => { config = value; };
  try { view('#/exams/2022-03/CA/sit'); } finally { A.quizStart = start; }
  assert.equal(config.mcq[18].accepted.join(','), '0');
  assert.equal(config.mcq[18].printedKey, 'C');
  A.quizStart({key:'reviewed-key-regression',title:'Reviewed key',back:'#/exams',
    mcq:[config.mcq[18]],theory:[]});
  doc.querySelector('[data-pick="0"]').click();
  has(doc.getElementById('view'), 'The source prints C');
  doc.querySelector('[data-phase="results"]').click();
  has(doc.getElementById('view'), '1 of 1');
});

await test('reviewed short answers retain the official source in paper and practice', () => {
  let page = view('#/exams/2024-09/CA');
  const question = doc.getElementById('q-saq-10');
  has(question.querySelector('.ans'), 'Relevant cost');
  has(question.querySelector('.printed-answer'), 'Irrelevant Cost');
  view('#/s/CA/9');
  const chapter = A.DATA.CA.chapters.find(c => c.n === 9);
  const built = A.chapterQuestions('CA',9,chapter,A.DATA.EXAMS);
  const corrected = built.theory.find(q=>q.src.includes('September 2024') && q.src.includes('Short answer 10'));
  assert.ok(corrected);
  assert.ok(JSON.stringify(corrected.a).includes('Relevant cost'));
  assert.ok(corrected.flag.includes('Printed key defect'));
  const bank = A.DATA.EXAMS.papers.find(p=>p.diet==='2024-09'&&p.subject==='CA');
  assert.equal(bank.saq[9].ans.join(' '),'Irrelevant Cost');
});

await test('timed mode provides original tables without leaking answers or correctness', () => {
  view('#/exams/2019-03/TAX/sit');
  doc.querySelector('[data-reference]').click();
  has(doc.getElementById('sheet-b'),'NIGERIAN TAX RATES');
  has(doc.getElementById('sheet-b'),'CAPITAL ALLOWANCES');
  A.closeSheet();
  doc.querySelector('[data-pick="0"]').click();
  assert.equal(doc.querySelectorAll('.flagbox,.why,.ok .mk').length,0);
  doc.dispatchEvent(new w.KeyboardEvent('keydown',{key:'s',bubbles:true}));
  assert.equal(doc.querySelector('[data-look]'),null);
  doc.querySelector('[data-jump]').click();
  assert.equal(doc.querySelectorAll('.answersheet .ok,.answersheet .no').length,0);
  assert.equal(doc.querySelectorAll('[data-shuffle],[data-reset]').length,0);
  A.closeSheet();
  doc.querySelector('[data-phase="theory"]').click();
  assert.ok(doc.getElementById('clk'));
  assert.equal(doc.querySelector('[data-model]'),null);
  assert.equal(doc.querySelector('.flagbox'),null);
});

await test('an expired written attempt finishes and Try again starts a fresh clock', async () => {
  const key='timer-regression';
  A.set(A.PK+'quiz:'+key,{n:2,i:0,ti:0,ans:{},look:{},phase:'theory'});
  A.set(A.PK+'wr:'+key+':0','Previous written answer');
  A.quizStart({key,title:'Timer regression',back:'#/exams',exam:true,deadline:Date.now()+40,
    mcq:[{q:'Question',o:['A','B'],a:0}],theory:[{q:'Written question',a:[{p:'Model'}]}]});
  assert.ok(doc.getElementById('clk'));
  await tick(1100);
  assert.ok(doc.querySelector('.res'));
  doc.querySelector('[data-again]').click();
  assert.equal(A.get(A.PK+'wr:'+key+':0'),'');
  assert.ok(A.get(A.PK+key+':start')>Date.now()-1000);
  assert.ok(doc.getElementById('clk').textContent.startsWith('02:59') || doc.getElementById('clk').textContent==='03:00:00');
  A.quizClear();
});

await test('original PDF pages and explanatory glossary are accessible', () => {
  const page=view('#/exams/2026-03/TAX');
  assert.equal(page.querySelectorAll('.bq > .h > a.source-link, .saqrow .question-links > a.source-link').length,56);
  const source=page.querySelector('a.source-link[href*=".pdf#page="]');
  assert.ok(source.getAttribute('href').startsWith('assets/papers/2026-03.pdf#page='));
  view('#/s/AUD/10');
  const glossary=doc.querySelector('.chapter-glossary');
  has(glossary,'CAAT');
  has(glossary,'Computer-Assisted Audit Technique');
});

await test('the Tax transition guide is linked from the study desk', () => {
  const page=view('#/');
  assert.ok(page.querySelector('a[href="guides/tax-transition.html"]'));
  const guide=readFileSync(join(root,'guides/tax-transition.html'),'utf8');
  assert.ok(guide.includes('₦665,600') && guide.includes('₦610,800'));
});

await test('multi-topic essays link each passage and appear in secondary chapter practice', () => {
  let page=view('#/exams/2019-03/CA');
  const essay=doc.getElementById('q-secb-3');
  assert.ok(essay.querySelector('a[href="#/s/CA/14?sec=14-4"]'));
  page=view('#/s/CA/14');
  assert.ok(page.querySelector('.pqrow[href="#/exams/2019-03/CA?q=secb-3"]'));
  const chapter=A.DATA.CA.chapters.find(c=>c.n===14);
  const built=A.chapterQuestions('CA',14,chapter,A.DATA.EXAMS);
  const question=built.theory.find(q=>q.src.includes('March 2019') && q.src.endsWith('Question 3'));
  assert.ok(question);
  assert.equal(question.ch,14);
  assert.equal(question.sec,'14.4');
  assert.ok(question.pre.join(' ').includes('Uniform Costing'));
});

await test('source numbers display without breaking citations and printed subheadings can be linked', async () => {
  const page = view('#/s/CA/3');
  assert.equal(page.querySelector('#sec-3-3 > h2 .sn').textContent, '3.5');
  assert.ok(page.querySelector('.reader-index a[href="#/s/CA/3?sec=3-3"]'));
  view('#/s/CA/3?sec=book-3-5-1'); await tick(80);
  has(doc.getElementById('sec-book-3-5-1'), '3.5.1');
  assert.ok(doc.getElementById('sec-book-3-5-1').classList.contains('landed'));
  view('#/s/MAN/3');
  const original = doc.querySelector('img[src="assets/study-figures/man-p160.png"]');
  assert.ok(original && original.alt.includes('Decision Tree'));
  assert.equal(original.closest('a').getAttribute('href'), original.getAttribute('src'));
});

await test('no runtime or data-loading errors occurred', () => assert.deepEqual(errors, []));
dom.window.close();
console.log(`\n${passed} passed, ${failed} failed (jsdom; no visual browser QA).`);
if (failed) process.exitCode = 1;
