/* -- past papers, search, formulas, progress, boot --------------------- */
(function () {
  var A = ATSWA, V = A.VIEWS;

  function withExams(cb) {
    var request = location.hash;
    A.loading('Past papers');
    A.need('EXAMS', 'exams', function (ex) {
      if (location.hash !== request) return;
      if (!ex) return A.h('<div class="wrap"><p style="padding:60px 0">Could not load the past ' +
        'papers. Serve this folder over http:// rather than opening the file directly.</p></div>');
      cb(ex);
    });
  }
  function findPaper(ex, diet, code) {
    for (var i = 0; i < ex.papers.length; i++)
      if (ex.papers[i].diet === diet && ex.papers[i].subject === code) return ex.papers[i];
    return null;
  }
  /* the "Chapter N" tag on a past question: a plain badge where there is no
     confident section match, a link straight to the passage it was worked
     from where there is */
  function chBadge(subj, q) {
    if (!q.ch) return '';
    if (q.sec) return '<a class="ch" href="#/s/' + subj + '/' + q.ch + '?sec=' +
      String(q.sec).replace(/\./g, '-') + '">Chapter ' + q.ch + ' &rarr;</a>';
    return '<a class="ch" href="#/s/' + subj + '/' + q.ch + '">Chapter ' + q.ch + '</a>';
  }

  /* ---- index -------------------------------------------------------- */
  V.exams = function () {
    withExams(function (ex) {
      var only = A.subOf(route_q('s')) ? route_q('s') : '';
      var diets = {};
      ex.papers.forEach(function (p) { (diets[p.diet] = diets[p.diet] || []).push(p); });
      var order = Object.keys(diets).sort().reverse();
      var years = order.map(function (d) { return d.slice(0, 4); }).filter(function (y, i, all) { return all.indexOf(y) === i; });
      var year = years.indexOf(route_q('y')) >= 0 ? route_q('y') : '';
      var shown = 0;
      var body = order.map(function (d) {
        if (year && d.slice(0, 4) !== year) return '';
        var ps = diets[d].filter(function (p) { return !only || p.subject === only; });
        if (!ps.length) return '';
        shown += ps.length;
        return '<h3 style="font-size:20px;margin:34px 0 12px;letter-spacing:-.02em">' +
          A.esc(ps[0].name) + '</h3><div class="dietgrid' + (only ? ' single' : '') + '">' +
          ps.map(function (p) {
            var s = A.subOf(p.subject);
            return '<a class="dietcard" href="#/exams/' + p.diet + '/' + p.subject + '" ' +
              'data-sub="' + p.subject + '">' +
              '<div class="d">' + p.subject + '</div><h3>' + A.esc(s ? s.name : p.subject) + '</h3>' +
              '<div class="m"><span>' + p.mcq.length + ' MCQ</span><span>' + p.saq.length +
              ' short</span><span>' + p.secb.length + ' essay</span></div></a>';
          }).join('') + '</div>';
      }).join('');
      var oldest = diets[order[order.length - 1]][0].name;
      var newest = diets[order[0]][0].name;
      function filterHref(code) {
        var params = [];
        if (code) params.push('s=' + code);
        if (year) params.push('y=' + year);
        return '#/exams' + (params.length ? '?' + params.join('&') : '');
      }
      var filters = [{ code: '', name: 'All subjects' }].concat(SUBJECTS).map(function (s) {
        return '<a class="filter-chip" href="' + filterHref(s.code) + '"' +
          (only === s.code ? ' aria-current="true"' : '') + ' title="' + A.esc(s.name) + '">' +
          (s.code || s.name) + '</a>';
      }).join('');
      A.h('<div class="wrap"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="#/">Study desk</a>' +
        '<span>/</span><span>Past papers</span></nav><section class="shead" style="border:none">' +
        '<div class="code">The past-paper library &middot; ' + order.length + ' diets &middot; ' + ex.papers.length + ' papers</div>' +
        '<h1>Turn what you know into practice.</h1>' +
        '<p>Every downloaded ATSWA Part III paper from ' + A.esc(oldest) + ' to ' + A.esc(newest) +
        ', exactly as sat, with the examiners&rsquo; own solutions and reports. Read one ' +
        'through, or sit it against the clock.</p>' +
        '</section><div class="paper-filters" aria-label="Filter papers">' + filters +
        '<label class="paper-year" for="paper-year">Exam year <select id="paper-year"><option value="">All years</option>' +
        years.map(function (y) { return '<option' + (year === y ? ' selected' : '') + '>' + y + '</option>'; }).join('') +
        '</select></label></div><div class="paper-count" role="status">' + shown + ' paper' + (shown === 1 ? '' : 's') +
        (only ? ' &middot; ' + A.esc(A.subOf(only).name) : ' &middot; All four subjects') +
        (year ? ' &middot; ' + year : ' &middot; 2019–2026') + '</div>' +
        (body || '<p class="empty-state">No papers match these filters.</p>') + '<div style="height:40px"></div></div>');
      A.el('paper-year').addEventListener('change', function (e) {
        var params = [];
        if (only) params.push('s=' + only);
        if (e.target.value) params.push('y=' + e.target.value);
        A.go('#/exams' + (params.length ? '?' + params.join('&') : ''));
      });
    });
  };
  function route_q(k) {
    var raw = location.hash, i = raw.indexOf('?');
    if (i < 0) return '';
    var out = '';
    raw.slice(i + 1).split('&').forEach(function (kv) {
      var p = kv.split('='); if (decodeURIComponent(p[0]) === k) out = decodeURIComponent(p[1] || '');
    });
    return out;
  }

  function sectionExtras(workings, examiner, figures) {
    return A.sourceFigures(figures) + (workings && workings.length ? '<details class="bq"><summary>Official workings</summary><div class="pre">' + A.esc(workings.join('\n')) + '</div></details>' : '') +
      (examiner && examiner.length ? '<details class="exm"><summary>Examiner’s report</summary><p>' + A.esc(examiner.join(' ')) + '</p></details>' : '');
  }

  /* ---- one paper, read through ------------------------------------- */
  V.paper = function (diet, code) {
    withExams(function (ex) {
      var p = findPaper(ex, diet, code);
      if (!p) return V.exams();
      var s = A.subOf(code);

      var mcq = p.mcq.map(function (q) {
        var ans = p.key[q.n];
        var flag = ex.flags[diet + '/' + code + '/mcq/' + q.n];
        return '<div class="bq" id="q-mcq-' + q.n + '"><div class="h"><span class="n">' + q.n + '</span>' +
          A.sourceLink(p, q.sourcePage) + chBadge(code, q) + '</div>' +
          '<div class="body">' + A.preBlock(q.pre) + A.stemHTML(q) +
          '<div style="margin-top:10px">' + q.options.map(function (o, k) {
            var info = A.keyInfo(q.studyKey || ans);
            var on = !info.bonus && info.accepted.indexOf(k) >= 0;
            var printed = q.studyKey && A.keyInfo(ans).accepted.indexOf(k) >= 0 && !on;
            return '<div style="display:flex;gap:10px;padding:4px 0' +
              (on ? ';color:var(--ok);font-weight:600' : '') + '">' +
              '<span class="mono" style="width:1.4em;flex:none">' + 'ABCDE'[k] + '</span>' +
              '<span style="flex:1">' + A.optText(o) + '</span>' +
              (on ? '<span class="mono" style="font-size:10px;letter-spacing:.1em">' +
                (q.studyKey ? 'REVIEWED' : 'ANSWER') + '</span>' : printed ?
                '<span class="printed-key-label">PRINTED KEY</span>' : '') +
              '</div>';
          }).join('') + '</div>' +
          A.flagHTML(flag) + A.sourceFigures(q.sourceFigures) +
          '</div></div>';
      }).join('');

      var saq = p.saq.map(function (q) {
        var badge = chBadge(code, q);
        return '<div class="saqrow" id="q-saq-' + q.n + '"><span class="n">' + q.n + '</span><div class="b">' +
          A.preBlock(q.pre) +
          '<div>' + R.inl(q.body.join(' ')) + '</div>' +
          (q.studyAns ? '<div class="ans"><div class="lbl">Reviewed study answer</div>' +
            R.inl(q.studyAns.join(' ')) + '</div><details class="printed-answer"><summary>Printed official answer</summary><p>' +
            R.inl(q.ans.join(' ')) + '</p></details>' :
            q.ans ? '<div class="ans"><div class="lbl">Official answer</div>' + R.inl(q.ans.join(' ')) + '</div>' : '') +
          '<div class="question-links">' + A.sourceLink(p, q.sourcePage) + badge + '</div>' +
          A.flagHTML(ex.flags[diet + '/' + code + '/saq/' + q.n]) + A.sourceFigures(q.sourceFigures) +
          '</div></div>';
      }).join('');

      var secb = p.secb.map(function (b) {
        return '<div class="bq" id="q-secb-' + b.n + '"><div class="h"><span class="n">Question ' + b.n + '</span>' +
          A.sourceLink(p, b.sourcePage) + chBadge(code, b) + '</div>' + A.flagHTML(ex.flags[diet + '/' + code + '/secb/' + b.n]) +
          (b.q && b.q.length ? '<div class="body"><div class="pre">' +
            A.esc(b.q.join('\n')) + '</div>' + A.relatedReadings(b, code) + '</div>' : '') +
          '<button class="reveal" data-reveal="sol' + p.diet + code + b.n + '">' +
          'Show the official solution</button>' +
          '<div class="sol hid" id="sol' + p.diet + code + b.n + '">' +
          A.sourceLink(p, b.solutionPage, 'View original solution') +
          (b.note ? R.blocks(b.note) : '') + A.sourceFigures(b.sourceFigures) +
          '<div class="pre">' + A.esc(b.solution.join('\n')) + '</div>' +
          (b.examiner && b.examiner.length
            ? '<div class="exm"><div class="lbl">Examiner&rsquo;s report</div>' +
              A.esc(b.examiner.join(' ')) + '</div>' : '') +
          '</div></div>';
      }).join('');

      A.h('<div class="wrap"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="#/">Study desk</a>' +
        '<span>/</span><a href="#/exams?s=' + code + '">Past papers</a><span>/</span><span>' +
        A.esc(p.name) + '</span></nav><section class="paperhead">' +
        '<div class="code">' + A.esc(p.name) + ' &middot; ' + code + '</div>' +
        '<h1 style="font-size:clamp(28px,4.4vw,42px);letter-spacing:-.032em;margin-top:8px">' +
        A.esc(s ? s.name : code) + '</h1>' +
        '<div class="sbar"><a class="btn pri" href="#/exams/' + diet + '/' + code + '/sit">' +
        'Sit this paper &middot; 3 hours</a>' +
        '<a class="btn" href="#/exams">All papers</a>' +
        (p.source ? '<a class="btn" href="' + A.esc(p.source.src) + '#page=' + p.source.startPage +
        '" target="_blank" rel="noopener">Open original PDF &nearr;</a>' : '') +
        '<button class="btn" data-revealall="1">Reveal every solution</button></div>' +
        '<nav class="paper-jumps" aria-label="Paper sections"><a href="#/exams/' + diet + '/' + code +
        '?q=mcq-1">Multiple choice</a><a href="#/exams/' + diet + '/' + code +
        '?q=saq-1">Short answers</a><a href="#/exams/' + diet + '/' + code + '?q=secb-1">Section B</a></nav>' +
        '</section>' +
        '<div class="secmark"><h2>Section A, Part I</h2><span class="mk">Multiple choice ' +
        '&middot; 30 marks</span></div>' + mcq + sectionExtras(p.mcqWorkings, p.mcqExaminer, p.mcqFigures) +
        '<div class="secmark"><h2>Section A, Part II</h2><span class="mk">Short answer ' +
        '&middot; 20 marks</span></div><div style="margin-bottom:30px">' + saq + '</div>' + sectionExtras(p.saqWorkings, p.saqExaminer, p.saqFigures) +
        '<div class="secmark"><h2>Section B</h2><span class="mk">Answer any four ' +
        '&middot; 50 marks</span></div>' + secb +
        (p.referenceTables && p.referenceTables.length ?
          '<section class="paper-references" id="paper-reference-tables"><div class="secmark">' +
          '<h2>Reference tables supplied in the exam</h2></div><p>Historical rates and allowances, exactly as supplied ' +
        'with this paper. Use these for the original period; the <a href="#/s/TAX">2026 Taxation notes</a> ' +
          'and <a href="guides/tax-transition.html">old papers/current rules guide</a> explain the current framework.</p><div class="pre">' + A.esc(p.referenceTables.join('\n')) + '</div></section>' : '') +
        '<div style="height:60px"></div></div>');
      var question = route_q('q');
      if (/^(mcq|saq|secb)-\d+$/.test(question)) {
        var target = A.el('q-' + question);
        if (target) {
          var questionRoute = location.hash;
          (document.fonts ? document.fonts.ready : Promise.resolve()).then(function () {
            requestAnimationFrame(function () { requestAnimationFrame(function () {
              if (!target.isConnected || location.hash !== questionRoute) return;
              A.scrollInto(target);
              target.classList.add('question-landed');
            }); });
          });
        }
      }
    });
  };

  /* ---- sit the paper ------------------------------------------------- */
  V.sit = function (diet, code) {
    withExams(function (ex) {
      var p = findPaper(ex, diet, code);
      if (!p) return V.exams();
      var s = A.subOf(code);
      var mcq = p.mcq.map(function (q) {
        var ans = p.key[q.n];
        return {
          q: q.stem, o: q.options, a: A.keyInfo(q.studyKey || ans).a,
          accepted: A.keyInfo(q.studyKey || ans).accepted, bonus: A.keyInfo(q.studyKey || ans).bonus,
          studyCorrection: !!q.studyKey, printedKey: q.studyKey ? ans : '', pre: q.pre || [], past: true,
          src: p.name + ' &middot; Q' + q.n, ch: q.ch, sec: q.sec,
          w: ex.notes[diet + '/' + code + '/mcq/' + q.n] || '',
          flag: ex.flags[diet + '/' + code + '/mcq/' + q.n] || '', sourceFigures: q.sourceFigures || [],
          original: A.sourceLink(p, q.sourcePage, 'Open the original question')
        };
      });
      var theory = p.saq.filter(function (q) { return q.ans; }).map(function (q) {
        return { q: q.body.join(' '), marks: 1, short: true, pre: q.pre || [],
                 a: [{ p: '**' + (q.studyAns || q.ans).join(' ') + '**' }],
                 src: p.name + ' &middot; Short answer ' + q.n, ch: q.ch, sec: q.sec,
                 flag: ex.flags[diet + '/' + code + '/saq/' + q.n] || '', sourceFigures: q.sourceFigures || [],
                 original: A.sourceLink(p, q.sourcePage, 'Open the original question') };
      }).concat(p.secb.map(function (b) {
        return { q: 'Question ' + b.n + ' — see the paper for the full text.',
                 marks: 12.5, pre: b.q || [],
                 a: [{ pre: b.solution.join('\n') }].concat(
                    b.examiner && b.examiner.length
                      ? [{ note: b.examiner.join(' '), lbl: "Examiner's report" }] : []),
                 src: p.name + ' &middot; Section B, Q' + b.n, ch: b.ch, sec: b.sec, readings: b.readings || [],
                 flag: ex.flags[diet + '/' + code + '/secb/' + b.n] || '', sourceFigures: b.sourceFigures || [],
                 original: A.sourceLink(p, b.sourcePage, 'Open the original question') };
      }));
      var kkey = A.PK + 'sit:' + diet + '/' + code + ':start';
      var started = A.get(kkey, 0);
      var previous = A.get(A.PK + 'quiz:sit:' + diet + '/' + code, null);
      if (previous && previous.phase === 'results') {
        A.set(A.PK + 'quiz:sit:' + diet + '/' + code, null);
        theory.forEach(function (_, i) { A.set(A.PK + 'wr:sit:' + diet + '/' + code + ':' + i, ''); });
        started = 0;
      }
      if (!started) { started = Date.now(); A.set(kkey, started); }
      A.quizStart({
        key: 'sit:' + diet + '/' + code,
        title: A.esc(p.name) + ' &middot; ' + (s ? s.name : code),
        back: '#/exams/' + diet + '/' + code,
        code: code,
        mcq: mcq, theory: theory,
        exam: true, deadline: started + 3 * 60 * 60 * 1000,
        referenceTables: p.referenceTables || []
      });
    });
  };

  /* ---- formula index ------------------------------------------------- */
  V.formulas = function () {
    var request = location.hash;
    var want = SUBJECTS.filter(function (s) { return s.formulas !== false; });
    A.loading('Formulas');
    var got = 0, all = {};
    want.forEach(function (s) {
      A.need(s.code, s.file, function (d) {
        all[s.code] = d; got++;
        if (got === want.length) show();
      });
    });
    function show() {
      if (location.hash !== request) return;
      var body = want.map(function (s) {
        var d = all[s.code];
        if (!d) return '';
        var chunks = d.chapters.filter(function (c) { return c.formulas && c.formulas.length; })
          .map(function (c) {
            return '<h3 style="font-size:18px;margin:26px 0 10px;letter-spacing:-.02em">' +
              '<a href="#/s/' + s.code + '/' + c.n + '">' + c.n + '. ' + A.esc(c.t) + '</a></h3>' +
              R.block({ fbox: { h: '', rows: c.formulas } });
          }).join('');
        if (!chunks) return '';
        return '<section data-sub="' + s.code + '" style="margin-bottom:44px">' +
          '<div class="secmark"><h2>' + A.esc(s.name) + '</h2>' +
          '<span class="mk">' + s.code + '</span></div>' + chunks + '</section>';
      }).join('');
      A.h('<div class="wrap"><section class="shead" style="border:none">' +
        '<div class="code">Reference</div><h1>Every formula, in one place</h1>' +
        '<p>Pulled from the chapters, in chapter order. Each heading links back to where the ' +
        'formula is derived and used.</p></section>' + (body ||
        '<p style="padding:40px 0;color:var(--ink3)">No formulas recorded yet.</p>') +
        '<div style="height:60px"></div></div>');
    }
  };

  /* ---- progress ------------------------------------------------------ */
  V.progress = function () {
    var p = A.prog();
    var cards = SUBJECTS.map(function (s) {
      var st = A.subStats(s.code);
      var heat = [];
      for (var i = 1; i <= s.n; i++) {
        var r = p[s.code + '/' + i] || {};
        var v = 0;
        if (r.read) v = 1;
        if (r.quiz) v = r.best >= 0.8 ? 4 : r.best >= 0.6 ? 3 : 2;
        var status = r.quiz ? Math.round((r.best || 0) * 100) + '% best quiz score' : (r.read ? 'Read' : 'Not read yet');
        heat.push('<a class="heat-cell" data-v="' + v + '" href="#/s/' + s.code + '/' + i +
          '" title="Chapter ' + i + ' · ' + status + '" aria-label="' + s.code + ' chapter ' + i +
          ', ' + status + '">' + ('0' + i).slice(-2) + '</a>');
      }
      return '<div class="pcard" data-sub="' + s.code + '">' +
        '<div class="s">' + s.code + '</div><h3>' + A.esc(s.name) + '</h3>' +
        '<div class="heat">' + heat.join('') + '</div>' +
        '<div style="margin-top:14px;display:flex;gap:18px;font-family:var(--mono);' +
        'font-size:11px;color:var(--ink3)">' +
        '<span><b style="color:var(--ink)">' + st.read + '</b>/' + st.n + ' read</span>' +
        '<span><b style="color:var(--ink)">' + st.done + '</b> quizzed</span>' +
        (st.done ? '<span><b style="color:var(--ink)">' + st.avg + '%</b> avg</span>' : '') +
        '</div>' +
        '<div style="margin-top:14px"><a class="btn sm" href="#/s/' + s.code + '">Open</a></div>' +
        '</div>';
    }).join('');
    A.h('<div class="wrap"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="#/">Study desk</a>' +
      '<span>/</span><span>Progress</span></nav><section class="shead" style="border:none">' +
      '<div class="code">Progress</div><h1>Where you are</h1>' +
      '<p>Kept in this browser only. Reading a chapter marks it; taking its quiz records your ' +
      'best score. Select a chapter below to get back to it.</p></section>' +
      '<div class="progress-legend"><span><i data-v="0"></i>Not read</span>' +
      '<span><i data-v="1"></i>Read</span><span><i data-v="2"></i>Quiz under 60%</span>' +
      '<span><i data-v="3"></i>60–79%</span><span><i data-v="4"></i>80% and up</span></div>' +
      '<div class="pgrid">' + cards + '</div>' +
      '<div style="margin-bottom:70px"><button class="btn" id="wipe">Clear all progress</button></div>' +
      '</div>');
    var w = A.el('wipe');
    if (w) w.addEventListener('click', function () {
      if (w.dataset.armed) {
        A.resetProgress();
        V.progress();
      } else { w.dataset.armed = '1'; w.textContent = 'Click again to erase everything'; }
    });
  };

  /* ---- search --------------------------------------------------------- */
  var IDX = null, building = false, indexWaiters = [];
  function buildIndex(done) {
    if (IDX) return done(IDX);
    indexWaiters.push(done);
    if (building) return;
    building = true;
    var got = 0, index = [];
    SUBJECTS.forEach(function (s) {
      A.need(s.code, s.file, function (d) {
        if (d) d.chapters.forEach(function (c) {
          index.push({ t: c.n + '. ' + c.t, c: c.brief || '', w: s.code + ' chapter',
                     u: '#/s/' + s.code + '/' + c.n,
                     x: (c.t + ' ' + (c.brief || '') + ' ' +
                         (c.outcomes || []).join(' ')).toLowerCase() });
          (c.secs || []).forEach(function (sec) {
            index.push({ t: sec.t, c: R.text(sec.b).slice(0, 220),
                       w: s.code + ' ' + sec.n,
                       u: '#/s/' + s.code + '/' + c.n + '?sec=' + String(sec.n).replace(/\./g, '-'),
                       x: (sec.t + ' ' + R.text(sec.b)).toLowerCase() });
          });
        });
        if (++got === SUBJECTS.length) {
          IDX = index; building = false;
          indexWaiters.splice(0).forEach(function (callback) { callback(IDX); });
        }
      });
    });
  }
  function runSearch(qs) {
    var out = A.el('srch-o');
    var q = qs.trim().toLowerCase();
    if (q.length < 2) { out.innerHTML = '<div class="empty">Type at least two letters.</div>'; return; }
    buildIndex(function (idx) {
      if (!A.el('srch').classList.contains('on') || A.el('srch-i').value.trim().toLowerCase() !== q) return;
      var terms = q.split(/\s+/);
      var hits = [];
      idx.forEach(function (r) {
        var sc = 0;
        terms.forEach(function (t) {
          var i = r.x.indexOf(t);
          if (i < 0) { sc = -1e9; return; }
          sc += 12 - Math.min(10, i / 60);
          if (r.t.toLowerCase().indexOf(t) >= 0) sc += 24;
        });
        if (sc > 0) hits.push({ r: r, s: sc });
      });
      hits.sort(function (a, b) { return b.s - a.s; });
      if (!hits.length) { out.innerHTML = '<div class="empty">Nothing found.</div>'; return; }
      out.innerHTML = hits.slice(0, 40).map(function (x, i) {
        return '<a class="hit' + (i === 0 ? ' on' : '') + '" href="' + x.r.u + '">' +
          '<span class="w">' + A.esc(x.r.w) + '</span>' +
          '<div class="t">' + hl(x.r.t, terms) + '</div>' +
          '<div class="c">' + hl(x.r.c, terms) + '</div></a>';
      }).join('');
    });
  }
  function hl(s, terms) {
    var pattern = terms.filter(Boolean).map(function (t) { return t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|');
    return String(s).split(new RegExp('(' + pattern + ')', 'ig')).map(function (part, i) {
      return i % 2 ? '<mark>' + A.esc(part) + '</mark>' : A.esc(part);
    }).join('');
  }
  function openSearch() {
    A.el('srch').classList.add('on');
    document.body.classList.add('search-open');
    var i = A.el('srch-i'); i.value = ''; i.focus();
    A.el('srch-o').innerHTML = '<div class="empty">Search every chapter and section.</div>';
    buildIndex(function () {});
  }

  /* ---- boot ----------------------------------------------------------- */
  function theme() {
    var t = A.get(A.PK + 'theme', null);
    if (t) document.documentElement.setAttribute('data-theme', t);
  }
  function toggleTheme() {
    var cur = document.documentElement.getAttribute('data-theme');
    var dark = window.matchMedia && window.matchMedia('(prefers-color-scheme:dark)').matches;
    var next = cur ? (cur === 'dark' ? 'light' : 'dark') : (dark ? 'light' : 'dark');
    document.documentElement.setAttribute('data-theme', next);
    A.set(A.PK + 'theme', next);
  }

  function foot() {
    A.el('foot').innerHTML = '<div class="footer-top"><div class="footer-brand">ATSWA Part III' +
      '<span>A little closer, every day.</span></div><a href="#/about">About this project &nearr;</a></div>' +
      '<p>Written from the ATSWA Part&nbsp;III study texts (2025; Taxation 2026, fifth ' +
      'edition) and the INSIGHT past-question packs, March 2019 to March 2026. The chapter notes ' +
      'are a study aid, not a substitute for the study text; check anything that matters against ' +
      'it and against your tutor.</p>' +
      '<p style="margin-top:10px;font-size:12px;color:var(--ink3)">Keys: <b>A</b>&ndash;<b>E</b> ' +
      'answer &middot; <b>S</b> show answer &middot; <b>J</b> jump &middot; <b>/</b> search ' +
      '&middot; <b>Esc</b> close</p>';
  }

  function boot() {
    theme(); foot();
    A.el('btn-theme').addEventListener('click', toggleTheme);
    A.el('btn-search').addEventListener('click', openSearch);
    A.el('search-close').addEventListener('click', A.closeSearch);
    document.querySelector('.skip-link').addEventListener('click', function (e) {
      e.preventDefault(); A.el('view').focus(); A.el('view').scrollIntoView({ block: 'start' });
    });
    A.el('btn-menu').addEventListener('click', A.toggleMobileNav);
    A.el('sheet-x').addEventListener('click', A.closeSheet);
    A.el('veil').addEventListener('click', A.closeSheet);
    A.el('srch').addEventListener('click', function (e) {
      if (e.target.id === 'srch') A.closeSearch();
    });
    A.el('srch-i').addEventListener('input', function (e) { runSearch(e.target.value); });
    A.el('srch-o').addEventListener('click', function (e) {
      if (e.target.closest('.hit')) A.closeSearch();
    });
    A.el('srch-i').addEventListener('keydown', function (e) {
      var hits = [].slice.call(document.querySelectorAll('.srch .hit'));
      var cur = hits.findIndex(function (x) { return x.classList.contains('on'); });
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (!hits.length) return;
        var ni = Math.max(0, Math.min(hits.length - 1, cur + (e.key === 'ArrowDown' ? 1 : -1)));
        hits.forEach(function (x) { x.classList.remove('on'); });
        hits[ni].classList.add('on'); hits[ni].scrollIntoView({ block: 'nearest' });
      }
      if (e.key === 'Enter' && hits[cur < 0 ? 0 : cur]) {
        e.preventDefault();
        location.hash = hits[cur < 0 ? 0 : cur].getAttribute('href');
        A.closeSearch();
      }
    });
    document.addEventListener('keydown', function (e) {
      if (A.el('srch').classList.contains('on') && e.key === 'Tab') {
        var focusable = [A.el('srch-i'), A.el('search-close')].concat([].slice.call(document.querySelectorAll('.srch a.hit')));
        var first = focusable[0], last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
      if (/^(INPUT|TEXTAREA)$/.test(e.target.tagName)) {
        if (e.key === 'Escape') A.closeSearch();
        return;
      }
      if (e.key === '/' && !e.metaKey && !e.ctrlKey) { e.preventDefault(); openSearch(); }
      if (e.key === 'Escape') { A.closeSearch(); A.closeSheet(); A.closeMobileNav(); }
    });
    document.addEventListener('click', function (e) {
      var mn = A.el('mobilenav');
      if (mn && mn.classList.contains('on') &&
          !e.target.closest('#mobilenav') && !e.target.closest('#btn-menu')) {
        A.closeMobileNav();
      }
    });
    document.addEventListener('click', function (e) {
      var t = e.target.closest && e.target.closest('[data-revealall]');
      if (!t) return;
      [].slice.call(document.querySelectorAll('.sol.hid, .az.hid')).forEach(function (x) {
        x.classList.remove('hid');
      });
      [].slice.call(document.querySelectorAll('.reveal')).forEach(function (x) { x.remove(); });
      t.remove();
    });
    window.addEventListener('hashchange', function () {
      /* A bare "#sec-2-6" hash is an in-page jump — the "In this chapter"
         sidebar links on the chapter reader use exactly this — not a route.
         Re-rendering on it would tear down the very page it is meant to
         scroll within (parseHash sees no "/s/..." prefix and falls back to
         the home view), so it gets a plain native-style scroll and nothing
         else. Every real route change still re-renders as before. */
      if (/^#sec-[\w-]+$/.test(location.hash)) {
        var el = document.getElementById(location.hash.slice(1));
        if (el) A.scrollInto(el);
        return;
      }
      ATSWA.quizClear();
      A.render(); A.tabs();
      var m = location.hash.match(/#sec-[\w-]+$/);
      if (m) {
        setTimeout(function () {
          var t = document.getElementById(m[0].slice(1));
          if (t) A.scrollInto(t);
        }, 60);
      }
    });
    A.render(); A.tabs();
  }

  if (document.readyState === 'loading')
    document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
