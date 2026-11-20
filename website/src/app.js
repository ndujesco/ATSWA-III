/* -- ATSWA Part III study app -----------------------------------------
   Hash routing, lazy per-subject data, a quiz engine shared by chapter
   quizzes and exam mode, full-text search, and progress in localStorage. */
var ATSWA = (function () {

  /* ---- storage, with an in-memory fallback when it is blocked ------- */
  var mem = {};
  var LS = (function () {
    try { var k = '__t'; localStorage.setItem(k, '1'); localStorage.removeItem(k); return localStorage; }
    catch (e) { return null; }
  })();
  function get(k, d) {
    try { var v = LS ? LS.getItem(k) : mem[k]; return v == null ? d : JSON.parse(v); }
    catch (e) { return d; }
  }
  function set(k, v) {
    try { var s = JSON.stringify(v); if (LS) LS.setItem(k, s); else mem[k] = s; } catch (e) {}
  }
  var PK = 'atswa3:';
  if (LS && !get(PK + 'legacy-migrated', false)) {
    if (LS.getItem(PK + 'prog') === null) {
      var legacy = get('atswa2:prog', {}), migrated = {};
      Object.keys(legacy).forEach(function (key) {
        if (/^(CA|AUD|TAX|MAN)\//.test(key)) migrated[key] = legacy[key];
      });
      if (Object.keys(migrated).length) set(PK + 'prog', migrated);
    }
    Object.keys(LS).forEach(function (key) {
      if (/^atswa2:(?:(?:quiz:|wr:)?(?:CA|AUD|TAX|MAN)\/|(?:quiz:|wr:)?sit:[^/]+\/(?:CA|AUD|TAX|MAN)(?:[:/]|$)|theme$)/.test(key)) {
        var next = PK + key.slice('atswa2:'.length);
        if (LS.getItem(next) === null) LS.setItem(next, LS.getItem(key));
      }
    });
    set(PK + 'legacy-migrated', true);
  }

  /* ---- data registry ----------------------------------------------- */
  var DATA = {}, PEND = {};
  function put(key, obj) {
    DATA[key] = obj;
    if (PEND[key]) { PEND[key].forEach(function (f) { f(obj); }); delete PEND[key]; }
  }
  function need(key, file, cb) {
    if (DATA[key]) return cb(DATA[key]);
    if (PEND[key]) { PEND[key].push(cb); return; }
    PEND[key] = [cb];
    var s = document.createElement('script');
    s.src = 'data/' + file + '.js';
    s.onerror = function () {
      var w = PEND[key] || []; delete PEND[key];
      w.forEach(function (f) { f(null); });
    };
    document.head.appendChild(s);
  }

  /* ---- helpers ------------------------------------------------------ */
  var esc = function (s) { return R.esc(s); };
  function el(id) { return document.getElementById(id); }
  function h(html) { el('view').innerHTML = html; }
  function subOf(code) {
    for (var i = 0; i < SUBJECTS.length; i++) if (SUBJECTS[i].code === code) return SUBJECTS[i];
    return null;
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fmtClock(ms) {
    if (ms < 0) ms = 0;
    var s = Math.floor(ms / 1000);
    return pad(Math.floor(s / 3600)) + ':' + pad(Math.floor(s / 60) % 60) + ':' + pad(s % 60);
  }
  function pct(a, b) { return b ? Math.round(a / b * 100) : 0; }
  function scrollInto(target) {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion:reduce)').matches;
    target.scrollIntoView({ block: 'start', behavior: reduce ? 'auto' : 'smooth' });
  }
  function relatedReadings(q, code) {
    var refs = (q.readings || []).filter(function (r) { return r.ch !== q.ch || r.sec !== q.sec; });
    return refs.length ? '<div class="question-links reading-links"><span>Related reading</span>' + refs.map(function (r) {
      return '<a href="#/s/' + code + '/' + r.ch + '?sec=' + String(r.sec).replace(/\./g, '-') +
        '">Ch ' + r.ch + ' · §' + esc(r.sec) + '</a>';
    }).join('') + '</div>' : '';
  }
  function questionReference(q, chapter) {
    if (q.ch === chapter) return { ch: q.ch, sec: q.sec };
    return (q.readings || []).find(function (ref) { return ref.ch === chapter; });
  }
  function icon(name) {
    var paths = {
      arrow: '<path d="M5 12h14m-6-6 6 6-6 6"/>',
      book: '<path d="M12 5v15m0-15C8 2 4 3 2 4v14c4-1 7 0 10 2 3-2 6-3 10-2V4c-2-1-6-2-10 1Z"/>',
      papers: '<path d="M8 3h10l3 3v15H8zM18 3v4h3M4 7H3v14m9-10h5m-5 4h5"/>',
      spark: '<path d="m12 3 2.5 6.5L21 12l-6.5 2.5L12 21l-2.5-6.5L3 12l6.5-2.5Z"/>',
      chart: '<path d="M4 3v17h17M8 15v-4m5 4V7m5 8v-6"/>',
      calculator: '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 10h1m6 0h1M8 14h1m6 0h1M8 18h1m6 0h1"/>',
      shield: '<path d="M12 2 3 6v6c0 5 9 10 9 10s9-5 9-10V6zM8 12l3 3 5-6"/>',
      receipt: '<path d="M5 3h14v18l-3-2-4 2-4-2-3 2ZM8 7h8m-8 4h8m-8 4h4"/>',
      people: '<circle cx="9" cy="7" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 4a3 3 0 0 1 0 6m3 11v-3a6 6 0 0 0-3-5"/>',
      search: '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
      check: '<path d="m5 12 4 4L19 6"/>'
    };
    return '<svg class="ui-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      (paths[name] || paths.book) + '</svg>';
  }
  function optText(o) {
    if (typeof o === 'string') return R.inl(o);
    if (o && o.pre) return '<div class="pre">' + esc(o.pre.join('\n')) + '</div>';
    return R.inl(o && o.t);
  }
  function optPlain(o) {
    if (typeof o === 'string') return o;
    if (o && o.pre) return o.pre.join(' ');
    return (o && o.t) || '';
  }
  function stemHTML(q) {
    var s = q.stem !== undefined ? q.stem : q.q;
    var out = typeof s === 'string' ? R.inl(s) : R.inl(s && s.t);
    if (s && s.pre) {
      if (s.t && s.pre[0] && String(s.t).trim().replace(/\s+/g, ' ') === String(s.pre[0]).trim().replace(/\s+/g, ' ')) out = '';
      out += '<div class="pre">' + esc(s.pre.join('\n')) + '</div>';
    }
    return out;
  }
  function preBlock(pre, label) {
    if (!pre || !pre.length) return '';
    return '<div class="qpre"><div class="lbl">' + (label || 'Shared data') + '</div>' +
           '<div class="pre">' + esc(pre.join('\n')) + '</div></div>';
  }
  function sourceLink(paper, page, label) {
    if (!paper || !paper.source) return '';
    var source = paper.source, number = page || source.startPage;
    return '<a class="source-link" href="' + esc(source.src) + '#page=' + number +
      '" target="_blank" rel="noopener">' + esc(label || (page ? 'Source p. ' + page : 'Original PDF')) +
      ' <span aria-hidden="true">↗</span></a>';
  }

  /* ---- progress ----------------------------------------------------- */
  function prog() { return get(PK + 'prog', {}); }
  function resetProgress() {
    if (LS) {
      Object.keys(LS).forEach(function (key) {
        if (key.indexOf(PK) === 0 && key !== PK + 'theme') LS.removeItem(key);
      });
    } else {
      Object.keys(mem).forEach(function (key) {
        if (key.indexOf(PK) === 0 && key !== PK + 'theme') delete mem[key];
      });
    }
    set(PK + 'legacy-migrated', true);
    set(PK + 'prog', {});
  }
  function markRead(code, n) {
    var p = prog(), k = code + '/' + n;
    p[k] = p[k] || {};
    if (!p[k].read) { p[k].read = Date.now(); set(PK + 'prog', p); }
  }
  function saveScore(code, n, right, total) {
    var p = prog(), k = code + '/' + n;
    p[k] = p[k] || {};
    var best = p[k].best || 0;
    p[k].quiz = { r: right, t: total, at: Date.now() };
    p[k].best = Math.max(best, total ? right / total : 0);
    set(PK + 'prog', p);
  }
  function subStats(code) {
    var p = prog(), s = subOf(code), read = 0, done = 0, sum = 0;
    for (var i = 1; i <= s.n; i++) {
      var r = p[code + '/' + i];
      if (r && r.read) read++;
      if (r && r.quiz) { done++; sum += r.best || 0; }
    }
    return { read: read, done: done, avg: done ? Math.round(sum / done * 100) : 0, n: s.n };
  }
  function studyTarget(code) {
    var saved = get(PK + 'resume', null), s = saved && subOf(saved.code);
    if (s && (!code || code === s.code) && Number.isInteger(saved.n) && saved.n >= 1 && saved.n <= s.n) {
      return { subject: s, n: saved.n, sec: saved.sec || '', title: saved.title || '', resume: true };
    }
    var p = prog(), subjects = code ? [subOf(code)] : SUBJECTS;
    for (var i = 0; i < subjects.length; i++) {
      for (var n = 1; n <= subjects[i].n; n++) {
        if (!(p[subjects[i].code + '/' + n] || {}).read) return { subject: subjects[i], n: n, sec: '' };
      }
    }
    return { subject: subjects[0], n: 1, sec: '' };
  }
  function targetHref(target) {
    return '#/s/' + target.subject.code + '/' + target.n +
      (target.sec ? '?sec=' + encodeURIComponent(target.sec) : '');
  }

  /* ---- routing ------------------------------------------------------ */
  var route = { parts: [], q: {} };
  function go(hash) { location.hash = hash; }
  function parseHash() {
    var raw = location.hash.replace(/^#\/?/, '');
    var qi = raw.indexOf('?'), q = {};
    if (qi >= 0) {
      raw.slice(qi + 1).split('&').forEach(function (kv) {
        var p = kv.split('='); q[decodeURIComponent(p[0])] = decodeURIComponent(p[1] || '');
      });
      raw = raw.slice(0, qi);
    }
    return { parts: raw.split('/').filter(Boolean).map(decodeURIComponent), q: q };
  }

  var VIEWS = {};

  function render() {
    route = parseHash();
    var p = route.parts;
    closeSheet(); closeSearch(); closeMobileNav();
    window.removeEventListener('scroll', spyToc._h || function () {});
    document.body.removeAttribute('data-sub');
    document.body.classList.toggle('is-reader', p[0] === 's' && !!p[2] && !p[3]);
    if (!route.q.sec) window.scrollTo(0, 0);
    if (!p.length) return VIEWS.home();
    if (p[0] === 's' && p[1]) {
      document.body.setAttribute('data-sub', p[1]);
      if (!p[2]) return VIEWS.subject(p[1]);
      if (p[3] === 'quiz') return VIEWS.quiz(p[1], +p[2]);
      return VIEWS.chapter(p[1], +p[2]);
    }
    if (p[0] === 'exams') {
      if (!p[1]) return VIEWS.exams();
      if (p[3] === 'sit') { document.body.setAttribute('data-sub', p[2]); return VIEWS.sit(p[1], p[2]); }
      document.body.setAttribute('data-sub', p[2]);
      return VIEWS.paper(p[1], p[2]);
    }
    if (p[0] === 'revision') {
      if (!p[1]) return VIEWS.revision();
      document.body.setAttribute('data-sub', p[1]);
      if (!p[2]) return VIEWS.revisionSub(p[1]);
      return VIEWS.revisionList(p[1], p[2]);
    }
    if (p[0] === 'formulas') return VIEWS.formulas();
    if (p[0] === 'progress') return VIEWS.progress();
    if (p[0] === 'about') return VIEWS.about();
    return VIEWS.home();
  }

  function tabs() {
    var p = route.parts;
    var cur = p[0] === 's' ? p[1] : p[0];
    var out = ['<a class="desk-tab" href="#/"' + (!p.length ? ' aria-current="page"' : '') + '>Study desk</a>'];
    out = out.concat(SUBJECTS.map(function (s) {
      return '<a href="#/s/' + s.code + '"' + (cur === s.code ? ' aria-current="page"' : '') +
             ' title="' + esc(s.name) + '" aria-label="' + esc(s.name) + '">' +
             '<span class="tab-code">' + s.code + '</span><span class="tab-name">' + esc(s.name) + '</span></a>';
    }));
    out.push('<a href="#/exams"' + (p[0] === 'exams' ? ' aria-current="page"' : '') + '>Past papers</a>');
    out.push('<a href="#/revision"' + (p[0] === 'revision' ? ' aria-current="page"' : '') + '>Revision</a>');
    out.push('<a href="#/formulas"' + (p[0] === 'formulas' ? ' aria-current="page"' : '') + '>Formulas</a>');
    out.push('<a href="#/progress"' + (p[0] === 'progress' ? ' aria-current="page"' : '') + '>Progress</a>');
    el('tabs').innerHTML = out.join('');
    var mn = el('mobilenav');
    if (mn) mn.innerHTML = out.join('');
  }

  function loading(msg) {
    h('<div class="wrap"><div style="padding:70px 0;text-align:center;color:var(--ink3)">' +
      '<div class="eyebrow">' + esc(msg || 'Loading') + '</div></div></div>');
  }

  /* =================================================================== */
  /*  home                                                               */
  /* =================================================================== */
  VIEWS.home = function () {
    var totalCh = SUBJECTS.reduce(function (a, s) { return a + s.n; }, 0);
    var read = 0, quizzed = 0, target = studyTarget(), s = target.subject;
    var href = targetHref(target);
    var cards = SUBJECTS.map(function (s) {
      var st = subStats(s.code);
      read += st.read; quizzed += st.done;
      return '<a class="subcard" href="#/s/' + s.code + '" data-sub="' + s.code + '">' +
        '<div class="r1"><span class="subject-icon">' + icon(s.icon) + '</span>' +
        '<span class="code">' + s.code + '</span><span class="cnt">' + s.n + ' chapters</span></div>' +
        '<h2>' + esc(s.name) + '</h2>' +
        '<p class="sub">' + esc(s.summary || s.blurb) + '</p>' +
        '<div class="card-progress"><span>' + st.read + ' of ' + st.n + ' chapters read</span>' +
        '<span>' + pct(st.read, st.n) + '%</span></div>' +
        '<div class="bar" role="progressbar" aria-label="' + esc(s.name) + ' chapters read" ' +
        'aria-valuenow="' + st.read + '" aria-valuemin="0" aria-valuemax="' + st.n + '">' +
        '<i style="width:' + pct(st.read, st.n) + '%"></i></div>' +
        '<div class="foot"><span>' + (st.read ? 'Continue exploring' : 'Explore chapters') + '</span>' +
        icon('arrow') + '</div></a>';
    }).join('');
    function tool(url, name, description, glyph) {
      return '<a class="study-tool" href="' + url + '"><span class="tool-icon">' + icon(glyph) +
        '</span><span class="tool-copy"><h3>' + name + '</h3><p>' + description +
        '</p></span>' + icon('arrow') + '</a>';
    }
    h('<div class="wrap study-home">' +
      '<section class="hero"><div class="hero-copy"><div class="eyebrow"><i class="live-dot"></i>' +
      'The great lock-in &nbsp;/&nbsp; ATSWA Part III</div>' +
      '<h1>One chapter<br><em>closer.</em></h1>' +
      '<p class="lede">Your space to understand the material, work the questions, and build ' +
      'your confidence. All four subjects, one chapter at a time.</p>' +
      '<div class="hero-actions"><a id="continue-study" class="btn pri" href="' + href + '">' +
      (target.resume ? 'Continue studying' : 'Start studying') + icon('arrow') + '</a>' +
      '<a class="hero-secondary" href="#/exams">Explore past papers <span>&nearr;</span></a></div></div>' +
      '<aside class="session-card" data-sub="' + s.code + '"><div class="session-top">' +
      '<span class="eyebrow">' + (target.resume ? 'Pick up where you left off' : 'Your next session') +
      '</span>' + icon('book') + '</div><div class="session-subject">' + esc(s.name) + '</div>' +
      '<div class="session-chapter">CHAPTER ' + pad(target.n) + ' <span>/ ' + pad(s.n) + '</span></div>' +
      '<h2 id="resume-title" data-chapter="' + s.code + '/' + target.n + '">' +
      esc(target.title || 'Chapter ' + target.n) + '</h2>' +
      '<p>' + (target.resume ? (target.sec ? 'Your place in the chapter is saved. Settle back in.' :
      'A little progress today goes a long way.') : 'Start with the notes. Put it into practice with the chapter quiz.') +
      '</p><a class="session-link" href="' + href + '">' +
      (target.resume ? 'Return to chapter' : 'Open chapter') + icon('arrow') + '</a></aside></section>' +
      '<div class="tally"><div><b>04</b><span>subjects to master</span></div>' +
      '<div><b>' + totalCh + '</b><span>chapters to explore</span></div>' +
      '<div><b>60</b><span>past papers</span></div><div><b>3,360</b><span>past questions</span></div></div>' +
      '<section class="subjects-section" aria-labelledby="subjects-title"><div class="section-heading">' +
      '<div><div class="eyebrow">The syllabus</div><h2 id="subjects-title">Four subjects. One goal.</h2></div>' +
      '<a class="text-link" href="#/progress">Your progress ' + icon('arrow') + '</a></div>' +
      '<div class="subs">' + cards + '</div></section>' +
      '<section class="study-bottom"><div><div class="section-heading"><div><div class="eyebrow">Make it stick</div>' +
      '<h2>A little practice. A lot of progress.</h2></div></div><div class="study-tools">' +
      tool('#/exams', 'The past-paper library', '15 diets. Official solutions. Practice at your pace or against the clock.', 'papers') +
      tool('#/revision', 'Final revision', 'See what comes up often, grouped by topic and question type.', 'spark') +
      tool('#/formulas', 'Your formula reference', 'Every chapter’s formulas, gathered in one place.', 'calculator') +
      '</div></div><aside class="overview-card"><div class="overview-top"><span class="eyebrow">Your progress</span>' +
      icon('chart') + '</div><div class="progress-ring" style="--progress:' + pct(read, totalCh) +
      '%" role="img" aria-label="' + read + ' of ' + totalCh + ' chapters read"><div><b>' + pct(read, totalCh) +
      '%</b><span>of the syllabus</span></div></div><h3>' +
      (read ? 'Keep showing up.' : 'Every chapter counts.') + '</h3><p><b>' + read + '</b> of ' + totalCh +
      ' chapters read <span>&middot;</span> <b>' + quizzed + '</b> quizzed</p>' +
      '<a class="text-link" href="#/progress">See your breakdown ' + icon('arrow') + '</a>' +
      '<span class="local-note">Saved on this browser, just for you.</span></aside></section>' +
      (GUIDES.length ? (
      '<section class="ghead"><h2>Study guides</h2><p>One topic, everything about it, in one ' +
      'page — with worked examples, chapter links and the relevant past questions.</p>' +
      '</section>' +
      '<div class="subs">' + GUIDES.map(function (g) {
        return '<a class="subcard" href="' + g.href + '">' +
          '<div class="r1"><span class="code">' + esc(g.tag) + '</span></div>' +
          '<h2>' + esc(g.title) + '</h2>' +
          '<div class="sub">' + esc(g.blurb) + '</div></a>';
      }).join('') + '</div>') : '') +
      '</div>');
    need(s.code, s.file, function (d) {
      var title = el('resume-title');
      if (!d || !title || title.dataset.chapter !== s.code + '/' + target.n) return;
      var chapter = d.chapters.find(function (c) { return c.n === target.n; });
      if (chapter) title.textContent = chapter.t;
    });
  };

  VIEWS.about = function () {
    h('<div class="wrap"><div class="col" style="padding:44px 0 70px">' +
      '<h1 style="font-size:34px;letter-spacing:-.03em">About this site</h1>' +
      '<p style="margin-top:16px;color:var(--ink2)">Built from the 2025 ATSWA Part III ' +
      'study texts and the 2026 Taxation text, alongside 15 INSIGHT packs from March 2019 ' +
      'to March 2026. All four subjects have chapter notes, past papers and official solutions.</p>' +
      '<p style="color:var(--ink2)">Past-paper answers retain the law and rates used in their ' +
      'original periods. Question-level notes identify changed provisions and printed defects. ' +
      'Taxation notes follow the 2026 syllabus; the NTA tax changes commenced in January 2026, ' +
      'which is distinct from their September 2026 exam-syllabus adoption. ' +
      '<a href="https://nass.gov.ng/documents/download/11249">Nigeria Tax Act 2025</a> · ' +
      '<a href="https://nass.gov.ng/documents/download/11250">Tax Administration Act 2025</a>.</p>' +
      '<p style="color:var(--ink2)">Nothing here replaces the study text or your tutor. Where a ' +
      'printed paper is defective, this site says so rather than quietly picking a side.</p>' +
      '</div></div>');
  };

  /* =================================================================== */
  /*  subject                                                            */
  /* =================================================================== */
  VIEWS.subject = function (code) {
    var s = subOf(code);
    if (!s) return VIEWS.home();
    var request = route;
    loading(s.name);
    need(code, s.file, function (d) {
      if (route !== request) return;
      if (!d) return h('<div class="wrap"><p style="padding:60px 0">Could not load ' +
        esc(s.name) + '. Serve this folder over http:// rather than opening the file directly.</p></div>');
      var p = prog();
      var rows = d.chapters.map(function (c) {
        var r = p[code + '/' + c.n] || {};
        var mark = r.quiz ? '<span class="pill on">' + Math.round((r.best || 0) * 100) + '%</span>'
                          : (r.read ? '<span class="pill">read</span>' : '');
        return '<a class="chrow" href="#/s/' + code + '/' + c.n + '" data-chapter-search="' +
          esc((c.n + ' ' + c.t + ' ' + (c.brief || '')).toLowerCase()) + '">' +
          '<span class="n">' + pad(c.n) + '</span>' +
          '<span class="body"><span class="t">' + esc(c.t) + '</span>' +
          '<span class="d">' + esc(c.brief || '') + '</span></span>' +
          '<span class="meta">' + mark +
          '<span class="dot' + (r.read ? ' on' : '') + '"></span></span></a>';
      }).join('');
      var st = subStats(code), target = studyTarget(code);
      h('<div class="wrap subject-page"><nav class="breadcrumbs" aria-label="Breadcrumb">' +
        '<a href="#/">Study desk</a><span>/</span><span>' + esc(s.name) + '</span></nav>' +
        '<section class="shead subject-head"><div class="subject-intro">' +
        '<div class="code">' + code + ' &middot; Part III</div>' +
        '<h1>' + esc(s.name) + '</h1>' +
        '<p>' + esc(s.blurb) + '</p>' +
        '<div class="sbar">' +
        '<a class="btn pri" href="' + targetHref(target) + '">' +
        (target.resume ? 'Continue chapter ' + target.n : 'Start chapter ' + target.n) + icon('arrow') + '</a>' +
        '<a class="btn" href="#/exams?s=' + code + '">Past papers</a>' +
        '<a class="btn" href="#/revision/' + code + '">Revision</a>' +
        '</div>' + (d.intro ? '<details class="subject-context"><summary>About these study notes</summary><p>' +
        esc(d.intro) + '</p></details>' : '') + '</div><div class="subject-stat">' + icon(s.icon) +
        '<b>' + st.read + '<span> / ' + st.n + '</span></b><span>chapters read</span>' +
        '<div class="bar"><i style="width:' + pct(st.read, st.n) + '%"></i></div>' +
        '<small>' + st.done + ' chapter quizzes taken</small></div></section>' +
        '<div class="chapter-toolbar"><h2>Chapters <span>' + d.chapters.length + '</span></h2>' +
        '<label class="chapter-search">' + icon('search') +
        '<input id="chapter-filter" type="search" placeholder="Find a chapter…" aria-label="Find a chapter"></label></div>' +
        '<div class="chlist">' + rows + '</div><p id="chapter-empty" class="empty-state hide">' +
        'No chapters match. Try another word or a chapter number.</p></div>');
      el('chapter-filter').addEventListener('input', function (e) {
        var words = e.target.value.trim().toLowerCase().split(/\s+/), count = 0;
        document.querySelectorAll('[data-chapter-search]').forEach(function (row) {
          var match = words.every(function (word) { return row.dataset.chapterSearch.indexOf(word) >= 0; });
          row.classList.toggle('hide', !match);
          if (match) count++;
        });
        el('chapter-empty').classList.toggle('hide', count > 0);
      });
    });
  };

  /* Past questions this chapter's material has actually been examined
     with, gathered lazily (the exam bank is a separate, larger file) and
     dropped into the #pq-panel placeholder once it loads. Each row goes to
     the full past paper, official solution and all — the reverse direction
     of the "Source" links on a past question, which land back here. */
  function stemText(q) {
    var s = q.stem !== undefined ? q.stem : q.q;
    return (typeof s === 'string' ? s : (s && s.t) || '').replace(/\*\*/g, '');
  }
  function fillPqPanel(code, n, c) {
    need('EXAMS', 'exams', function (ex) {
      if (route.parts[0] !== 's' || route.parts[1] !== code || +route.parts[2] !== n || route.parts[3]) return;
      updateQuizCta(code, n, c, ex);
      var box = el('pq-panel');
      if (!box || !ex) return;
      /* diet (e.g. "2026-03") -> { name, rows: [...] }; 24 diets deep now,
         so grouped by diet and collapsed by default rather than one long
         flat list — the group header carries the year, so each row no
         longer needs to repeat it. */
      var groups = {};
      function add(diet, name, row) {
        var g = groups[diet] || (groups[diet] = { name: name, rows: [] });
        g.rows.push(row);
      }
      ex.papers.forEach(function (p) {
        if (p.subject !== code) return;
        p.mcq.forEach(function (q) {
          if (q.ch === n && p.key[q.n]) add(p.diet, p.name, { kind: 'MCQ', label: 'Q' + q.n,
            txt: stemText(q), href: '#/exams/' + p.diet + '/' + code + '?q=mcq-' + q.n });
        });
        p.saq.forEach(function (q) {
          if (q.ch === n && q.ans) add(p.diet, p.name, { kind: 'Short answer', label: 'Q' + q.n,
            txt: q.body.join(' '), href: '#/exams/' + p.diet + '/' + code + '?q=saq-' + q.n });
        });
        p.secb.forEach(function (b) {
          if (questionReference(b, n) && b.solution && b.solution.length) add(p.diet, p.name, {
            kind: 'Section B', label: 'Q' + b.n,
            txt: (b.q && b.q[0]) || 'See the full question in the paper.',
            href: '#/exams/' + p.diet + '/' + code + '?q=secb-' + b.n });
        });
      });
      var diets = Object.keys(groups).sort().reverse();
      var total = diets.reduce(function (a, d) { return a + groups[d].rows.length; }, 0);
      if (!total) return;
      var body = diets.map(function (d) {
        var g = groups[d];
        return '<details class="pqgroup"><summary>' + esc(g.name) +
          '<span class="n">' + g.rows.length + ' question' +
          (g.rows.length === 1 ? '' : 's') + '</span></summary>' +
          '<div class="pqlist">' + g.rows.map(function (r) {
            return '<a class="pqrow" href="' + r.href + '">' +
              '<span class="tag">' + esc(r.kind) + ' ' + esc(r.label) + '</span>' +
              '<span class="tx">' + esc(r.txt.slice(0, 130)) + (r.txt.length > 130 ? '…' : '') +
              '</span></a>';
          }).join('') + '</div></details>';
      }).join('');
      box.innerHTML = '<section class="sec"><h2><span class="sn">&#9679;</span>' +
        '<span>Examined before</span></h2>' +
        '<p>This chapter’s material has come up ' + total + ' time' +
        (total === 1 ? '' : 's') + ' across ' + diets.length + ' diet' +
        (diets.length === 1 ? '' : 's') + ' of past papers. Attempt them, with the official ' +
        'answer, in the <a href="#/s/' + code + '/' + n + '/quiz">chapter quiz</a> — or open a ' +
        'diet below to see the paper itself.</p>' + body + '</section>';
    });
  }

  /* The "Take the chapter quiz · N" button is first painted with only the
     authored count, because that is all that is known synchronously — the
     quiz itself also folds in every past question matched to this chapter
     (see quiz.js chapterQuestions), which can only be counted once the exam
     bank has loaded. Reconcile the two once it has, rather than leave the
     button quietly promising fewer questions than the quiz actually has. */
  function updateQuizCta(code, n, c, ex) {
    var btn = el('quiz-cta'), span = el('quiz-cta-n');
    if (!btn || !span || !ex || !ATSWA.chapterQuestions) return;
    var built = ATSWA.chapterQuestions(code, n, c, ex);
    var total = built.mcq.length + built.theory.length;
    if (!total) { btn.style.display = 'none'; return; }
    span.textContent = total;
    btn.style.display = '';
  }

  /* =================================================================== */
  /*  chapter reader                                                     */
  /* =================================================================== */
  VIEWS.chapter = function (code, n) {
    var s = subOf(code);
    if (!s) return VIEWS.home();
    var request = route;
    loading(s.name);
    need(code, s.file, function (d) {
      if (route !== request) return;
      if (!d) return VIEWS.subject(code);
      var c = null;
      for (var i = 0; i < d.chapters.length; i++) if (d.chapters[i].n === n) c = d.chapters[i];
      if (!c) return VIEWS.subject(code);
      markRead(code, n);
      set(PK + 'resume', { code: code, n: n, title: c.t, sec: route.q.sec || '', at: Date.now() });

      var toc = (c.secs || []).map(function (sec) {
        return '<a href="#/s/' + code + '/' + n + '?sec=' + esc(sec.n).replace(/\./g, '-') +
          '"><span>' + esc(sec.sourceN === undefined ? sec.n : sec.sourceN) + '</span>' + esc(sec.t) + '</a>';
      }).join('');
      var secs = (c.secs || []).map(function (sec) {
        return '<section class="sec" id="sec-' + esc(sec.n).replace(/\./g, '-') + '">' +
          '<h2><span class="sn">' + esc(sec.sourceN === undefined ? sec.n : sec.sourceN) + '</span><span>' + esc(sec.t) + '</span></h2>' +
          R.blocks(sec.b) + '</section>';
      }).join('');
      var fbox = c.formulas && c.formulas.length
        ? R.block({ fbox: { h: 'Formulas in this chapter', rows: c.formulas } }) : '';
      var focus = '';
      if (c.focus || (c.errors && c.errors.length)) {
        focus = '<section class="sec"><h2><span class="sn">&#9679;</span><span>In the exam</span></h2>' +
          (c.focus ? '<p>' + R.inl(c.focus) + '</p>' : '') +
          (c.errors && c.errors.length
            ? R.block({ warn: c.errors.map(function (e) { return { p: e }; }),
                        lbl: 'Marks are lost here' }) : '') +
          '</section>';
      }
      var prev = null, next = null;
      d.chapters.forEach(function (x) {
        if (x.n === n - 1) prev = x; if (x.n === n + 1) next = x;
      });
      var nq = ((c.quiz && c.quiz.mcq) || []).length + ((c.quiz && c.quiz.theory) || []).length;
      var pqBox = '<div id="pq-panel"></div>';
      var glossary = c.abbreviations && c.abbreviations.length ?
        '<details class="chapter-glossary"><summary>Terms and abbreviations <span>' + c.abbreviations.length +
        '</span></summary><dl>' + c.abbreviations.map(function (term) {
          return '<div><dt>' + esc(term.term) + '</dt><dd>' + esc(term.meaning) + '</dd></div>';
        }).join('') + '</dl></details>' : '';

      h('<div class="wrap"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="#/">Study desk</a>' +
        '<span>/</span><a href="#/s/' + code + '">' + esc(s.name) + '</a><span>/</span>' +
        '<span>Chapter ' + n + '</span></nav><div class="rlayout"><article class="reader-main">' +
        '<header class="chead"><div class="kicker">' + code + ' &middot; Chapter ' + n +
        ' of ' + s.n + '</div><h1>' + esc(c.t) + '</h1>' +
        (c.brief ? '<p class="brief">' + R.inl(c.brief) + '</p>' : '') + '</header>' +
        '<details class="reader-index"><summary>In this chapter <span>' +
        (c.secs || []).length + ' sections</span></summary><nav aria-label="Chapter sections">' + toc + '</nav></details>' +
        (c.outcomes && c.outcomes.length
          ? '<div class="lo"><h4>By the end of this chapter you can</h4><ul>' +
            c.outcomes.map(function (o) { return '<li>' + R.inl(o) + '</li>'; }).join('') +
            '</ul></div>' : '') +
        glossary + secs + fbox + focus + pqBox +
        '<div class="cfoot">' +
        '<a id="quiz-cta" class="btn pri" href="#/s/' + code + '/' + n + '/quiz"' +
        (nq ? '' : ' style="display:none"') + '>Take the chapter quiz' +
        ' &middot; <span id="quiz-cta-n">' + nq + '</span></a>' +
        '<a class="btn" href="#/s/' + code + '">All chapters</a>' +
        '</div>' +
        '<div class="cnav">' +
        (prev ? '<a href="#/s/' + code + '/' + prev.n + '"><span class="l">Previous</span>' +
                '<span class="t">' + esc(prev.t) + '</span></a>' : '<span style="flex:1"></span>') +
        (next ? '<a class="nx" href="#/s/' + code + '/' + next.n + '"><span class="l">Next</span>' +
                '<span class="t">' + esc(next.t) + '</span></a>' : '<span style="flex:1"></span>') +
        '</div>' +
        '</article><aside class="rtoc"><a class="reader-back" href="#/s/' + code + '">&larr; All chapters</a>' +
        '<h4>In this chapter</h4><div class="reading-meter" aria-hidden="true"><i id="reading-meter"></i></div>' +
        toc + '</aside></div></div>');
      spyToc(code, n, c.t);
      scrollToAnchor();
      fillPqPanel(code, n, c);
    });
  };

  /* A past-question citation links to "#/s/FA/2?sec=2-6" — the chapter route
     already carries the reader there; this lands them on the exact section
     the question was worked from, with a brief highlight so it is easy to
     find on the page rather than merely scrolled past. */
  function scrollToAnchor() {
    var sec = route.q.sec;
    if (!sec) { window.scrollTo(0, 0); return; }
    var el = document.getElementById('sec-' + sec);
    if (!el) { window.scrollTo(0, 0); return; }
    var request = route;
    window.scrollTo(0, 0);
    var fonts = document.fonts ? document.fonts.ready : Promise.resolve();
    fonts.then(function () {
      requestAnimationFrame(function () { requestAnimationFrame(function () {
        if (route !== request || !el.isConnected) return;
        scrollInto(el);
        el.classList.add('landed');
        set(PK + 'resume', { code: route.parts[1], n: +route.parts[2],
          title: document.querySelector('.chead h1').textContent, sec: sec, at: Date.now() });
        if (spyToc._h) spyToc._h();
        setTimeout(function () { el.classList.remove('landed'); }, 2600);
      }); });
    });
  }
  function spyToc(code, n, title) {
    var links = [].slice.call(document.querySelectorAll('.rtoc a'));
    var secs = [].slice.call(document.querySelectorAll('.sec[id]'));
    if (!links.length) return;
    var previous = '';
    var onScroll = function (event) {
      var y = window.scrollY + 120, cur = secs[0];
      secs.forEach(function (s) { if (s.offsetTop <= y) cur = s; });
      links.forEach(function (a) {
        a.classList.toggle('here', cur && a.getAttribute('href').split('?sec=')[1] === cur.id.replace(/^sec-/, ''));
      });
      var meter = el('reading-meter'), main = document.querySelector('.reader-main');
      if (meter && main) {
        var distance = main.offsetHeight - window.innerHeight + main.offsetTop;
        meter.style.width = Math.min(100, Math.max(0, distance > 0 ? window.scrollY / distance * 100 : 0)) + '%';
      }
      if (event && cur && cur.id !== previous) {
        previous = cur.id;
        set(PK + 'resume', { code: code, n: n, title: title,
          sec: window.scrollY > 0 ? cur.id.replace(/^sec-/, '') : '', at: Date.now() });
      }
    };
    window.removeEventListener('scroll', spyToc._h || function () {});
    spyToc._h = onScroll;
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  return { put: put, need: need, go: go, render: render, tabs: tabs,
           VIEWS: VIEWS, get: get, set: set, PK: PK, prog: prog,
           saveScore: saveScore, subOf: subOf, esc: esc, el: el, h: h,
           fmtClock: fmtClock, pct: pct, optText: optText, optPlain: optPlain,
           stemHTML: stemHTML, preBlock: preBlock, loading: loading,
           closeSheet: function () { closeSheet(); },
           toggleMobileNav: toggleMobileNav, closeMobileNav: closeMobileNav, DATA: DATA,
           subStats: subStats, icon: icon, studyTarget: studyTarget, targetHref: targetHref,
           closeSearch: closeSearch, scrollInto: scrollInto, resetProgress: resetProgress,
           sourceLink: sourceLink, relatedReadings: relatedReadings, questionReference: questionReference };

  function closeSheet() {
    el('sheet').classList.remove('on'); el('veil').classList.remove('on');
  }
  function closeSearch() {
    var search = el('srch');
    if (search.classList.contains('on')) {
      search.classList.remove('on');
      document.body.classList.remove('search-open');
      el('btn-search').focus({ preventScroll: true });
    }
  }
  function closeMobileNav() {
    var mn = el('mobilenav'), btn = el('btn-menu');
    if (mn) mn.classList.remove('on');
    if (btn) btn.setAttribute('aria-expanded', 'false');
  }
  function toggleMobileNav() {
    var mn = el('mobilenav'), btn = el('btn-menu');
    if (!mn || !btn) return;
    var open = mn.classList.toggle('on');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
})();
