# ATSWA Part III — Master Plan

The single reference document for building this site. It is meant to be
**comprehensive enough that no other document needs consulting** to pick the
project back up cold. Read this file in full at the start of every session
that touches this project, starting with "Where things stand" below.

This project is the sibling of `../../ATSWA II` (already built, chapter-by-
chapter study notes with worked examples, a formula renderer, per-chapter
quizzes, and decades of real past-exam questions cross-linked into every
chapter, deployed as a single dependency-free static site) and is being built
the same way, by the same methodology, reverse-engineered from that project's
own `website/README.md` and `website/RESUME.md` (its 1098-line, session-by-
session build log — read in full while writing this plan). **Copy that
architecture; do not reinvent it.**

There is a separate, independent sibling project for the Skills-level site at
`../SKIILLS/PLAN.md` — same methodology, different subjects, entirely
separate `content/`/`data/`/`tools/` trees, no shared code between the two.
Read that document only if you're working on Skills; it is not a prerequisite
for this one.

---

## Where things stand (read this first, every session)

**Implementation and QA complete; localhost active; Vercel deployment is the
user's responsibility. Updated 2026-11-20.**

**Explicit user correction: work locally and leave publishing to the user.
Do not deploy through Sites, Vercel or any other host without a new explicit
request. The earlier Sites publication was an assistant error, not the
requested release workflow.**

Local site: http://localhost:4000/ — serves website/ directly.
The user's full completion request covers source preservation, all past
questions, exact reading links, current-law notes, revision, UI and release.
The latest user instruction (2026-11-20) is to finish ATSWA III thoroughly and
leave Skills for now. Skills is on hold at 9/119 chapters; no Skills source
files were changed during this audit.

The verified site contains **62 chapters** (CA 15, AUD 12, TAX 25, MAN 10),
**60 papers from 15 diets**, **1,800 MCQ + 1,200 SAQ + 360 essays**. Every one
of the **3,360 questions links to a chapter, section and original PDF page**.
Final Revision preserves all 3,360 source identities. There are 171 additional
passage links for multi-topic essays and 1,434 individually reviewed citation
overrides. Retrieval confidence gates were not reduced.

Original questions, printed answers, workings and available examiner reports
remain visible. All 15 original PDFs are copied and hash-checked; seven source
figure pages and all 15 Taxation rate appendices are preserved. Fixed actual
extraction loss of small standalone numbers, currency glyphs and misspelled
examiner headings. Source defects remain labelled, including irregular 2020
Management numbering, the four-option 2024 Tax question, bonus/dual keys.

The site has **386 question flags**, **7 reviewed MCQ corrections** and
**7 reviewed short-answer corrections**, with printed originals retained.
Current-law notes use the corrected primary 2025 tax Acts, NIIRA 2025 and
IAASB quality-management sources. The standalone Tax transition guide provides
primary links, a worked historical/current comparison and exact question links.
Source-backed chapter supplements and contextual glossaries are additions;
original chapter text was not removed. Literal answer-phrase candidates are
review aids, not proof of an omission. Review evidence and limits are in
website/data/answer-audit-review.json and law-review.json.

The final full rebuild from PDFs passes **13 Python source regressions and
30 jsdom UI regressions**. All four exam-filtered abbreviation audits have
zero unresolved candidates. **38 real Chrome checks** passed across five
viewport widths, plus additional checks for guide filters, exact question
landing, multi-topic readings and timed reference tables. The UI adds a
study desk, reading resumes, chapter finder, responsive contents, paper
filters, accessible search, themes and actionable progress. Timed attempts
retain written work, hide answer hints and reset correctly on a fresh attempt.

The five older target diets were retried on official/legacy paths and Wayback;
none yielded a PDF. The available corpus is complete within the agreed
March 2019–March 2026 scope. This external source gap is documented, not
silently filled or treated as an unfinished extraction task.

Read website/README.md for canonical build commands, RELEASE.md for the
release record, PROGRESS.md for dated history, and ../HANDOVER.md for the
short checkpoint. Historical intermediate counts below/in the log remain
historical. Do not claim independent recomputation of every historic answer
or individual legal adjudication of every question.

## Completion re-audit — 2026-11-20

The previous completion record missed real source material. Restored full
letters/questionnaires/report specimens, original figure/table pages, omitted
modern-costing discussions, product details and 19 worked Management answers.
Restored 61 specific heading references and 70 main-section reference mappings;
62 Taxation/Management sections received source-number/content corrections.
Source-key conflicts are flagged with printed originals retained. After all
changes, 48 individually reviewed citations resolve new ambiguities and old
incorrect targets; the automatic confidence gates are unchanged.

All 62 chapters, 60 papers, 3,360 source identities and their chapter/section/PDF
links pass the final integrity audit. There are 37 original study-text pages
preserving 42 figure/table captions, in addition to seven past-paper figure
recoveries. Final tests pass: 13 Python, 30 jsdom, 38 Chrome, all 62 chapter
layouts at two widths (124 checks), and additional source/guide/timed checks.
The release remains local for the user's manual Vercel deployment.

Review evidence: website/data/source-fidelity-review.json and
website/data/study-figures.json. Heading/caption inventories and targeted body
comparisons support this repair record. They do not prove a word-for-word
certification of every prose line or independent computation of every answer.
The five previously unavailable older diets remain outside the available corpus.

## Part A — What this project actually is

### A.1 Subjects

Confirmed from the actual table of contents of a downloaded INSIGHT Part III
pack (`materials/past-questions/INSIGHT Part III - 2023-09 September
2023.pdf`, verified via `pdftotext`), not assumed:

| Proposed code | Subject | Study text on hand |
|---|---|---|
| `aud` | Principles of Auditing & Assurance | `materials/study-texts/2025_Aud.pdf` |
| `ca`  | Cost Accounting | `materials/study-texts/2025_CA.pdf` |
| `tax` | Taxation | `materials/study-texts/Taxation_2026_Study_Text.pdf` |
| `man` | Management | `materials/study-texts/2025_MAN.pdf` |

All 4 study texts are already present, 4/4. Taxation is a 2026 edition (newer
than the other three's 2025) — expected, ICAN revises Taxation texts more
often for tax-law currency; not a gap, just note the edition when authoring
so a future check for an even-newer edition knows what it's comparing against.

**Codes confirmed and implemented:** `aud`, `ca`, `tax`, `man`. They match
all content directories, retrieval tools, routes and subject metadata.

### A.2 Past questions

INSIGHT packs, one PDF per diet, each containing all 4 subjects together
(same convention as `ATSWA II`'s Part II packs — not one file per subject).
Diet cycle: March / September.

**15 of the last-20-diet target downloaded**, March 2019 → March 2026, no
internal gaps. **5 older diets (September 2016, March 2017, September 2017,
March 2018, September 2018) are currently unrecoverable** — dead on ICAN's
own site and the earliest Wayback Machine snapshot on file already shows the
same dead link. Full detail, exact URLs, and the verification method are in
`../DOWNLOADS_LOG.md`. September 2026 remains excluded per the user's original source-scope
instruction. The release does not claim that March 2026 is the newest diet
available on the current date.

This gives a smaller past-question corpus than `ATSWA II` started with (15
diets here vs. the 24 `ATSWA II` eventually reached, after a later session
added 19 more beyond its original 5) — not a blocker for Phase 3
(transcription), only relevant once Phase 4 (the past-question pipeline)
starts. Revisit the 5-diet gap then; don't let it block anything now.

### A.3 What "Pilot Questions and Answers" is

(Cross-referenced from the Skills plan, `../SKIILLS/PLAN.md` §A.4, for
completeness — this resource is Skills/Professional-level, not ATSWA-level,
so it does not directly apply here.)

ICAN publishes **specimen questions with official model answers** (two sets
per paper) for papers under its current syllabus revision, because a newly
revised or newly restructured paper has no real past-exam diets yet. It's a
stand-in for past questions until enough real sittings accumulate. The old
ATSWA scheme (Parts I/II/III, including this project) is not under that same
revision — `ATSWA_NEW_SYLLABUS_EFFECTIVE_SEPTEMBER_2026.pdf` (seen on the
materials page) suggests a new ATSWA syllabus takes effect after this
project's own current source material, which is worth being aware of but is
not this project's problem to solve now: build against the current, live
2025/2026 study texts and INSIGHT diets, and treat any post-September-2026
syllabus change as a future revision if and when it actually lands.

---

## Part B — The ATSWA II methodology, in full

This project copies `ATSWA II`'s architecture exactly. Read `ATSWA II/
website/README.md` again before Phase 2 starts (short, authoritative,
possibly updated since this plan was written) — everything below is a
faithful condensation of it plus everything learned from the full
`RESUME.md` session log, not a replacement for reading the original.

### B.1 The pipeline

```
content/<code>/ch*.py           --build_content.py-->  data/<code>.js
materials/past-questions/*.pdf  --extract_papers.py-->  data/papers.json
data/papers.json                --aim.py-->             (chapter-level question tagging)
                                 --aim_sec.py <CODES>-->  (section-level question tagging)
                                 --build_exams.py-->      data/exams.js
data/papers.json + data/*.js    --final_revision.py-->   data/revision.js
src/*.js + src/page.html        --build.sh-->            index.html
```

`tools/extract_papers.py` needs `pdftotext` (poppler) on `PATH` — confirmed
present on this machine (`/opt/homebrew/bin/pdftotext`, v26.08.0). Nothing
else in the pipeline has external dependencies at build time — deliberately,
so the deployed site is just `index.html` + `data/*.js`, no server-side
anything, no build step at deploy time. `python3` (3.14.2 on this machine)
and, for the test suite only, `node`/`npx` + `npm install jsdom --no-save`
(gitignored, never committed) are the only tools needed.

### B.2 Content schema (verbatim from `ATSWA II/website/README.md`)

```python
CH = {
  'n': 9, 't': 'Accounting for Non-Current Assets',
  'brief': '...', 'outcomes': [...],
  'secs': [{'n': '9.1', 't': 'What goes into cost', 'b': [ ...blocks... ]}],
  'formulas': [{'lb': '...', 'tex': '...', 'nt': '...'}],
  'focus': '...', 'errors': [...],
  'quiz': {'mcq': [{'q','o','a','w','calc','src'}], 'theory': [{'q','marks','a','src'}]},
}
```

Block types: `p h3 h4 ul ol steps tex def note key warn pre table eg tacc
stmt fbox`. Inline syntax inside any string value: `$tex$` for maths,
`**bold**`, `*italic*`, `` `mono` ``, `~aside~`, `[label](#/route)` (also
works with any relative path, not just `#/` routes — used for linking to a
standalone guide page, see B.6).

`src/math.js` renders a LaTeX subset to MathML Core natively, no library —
real fractions, radicals, summations with limits, stretchy delimiters,
matrices, aligned blocks, laid out by the browser itself.

`build_content.py` validates as it builds: unknown block types, unbalanced
TeX braces, and out-of-range answer indices fail the build rather than fail
silently on the page. This is the mechanical backstop for principle C.9
below, not the standard itself.

### B.3 Question → chapter/section tagging, and the `PIN` override

Every past question is assigned to a chapter (then a section) by in-subject
IDF/TF-IDF retrieval against the **authored chapter content itself**
(`content/<code>/ch*.py` — title, brief, outcomes, every section's own text,
focus, errors), not raw PDF text — boosted by a curated per-chapter seed
vocabulary in `tools/corrections.py`'s `CHAPTER_KEYS`. The question's own
stem is weighted 3x over its MCQ options / numeric working, since options
often share vocabulary with the *wrong* chapter (e.g. five officer-title
options all pulling toward "officers and their responsibilities" regardless
of what the stem actually asks).

Where retrieval is genuinely ambiguous — two different concepts that
legitimately share dense vocabulary (`ATSWA II` hit this with several
statutory bodies that are each "a Chairman with a tenure") — a manual
override called `PIN` in `tools/corrections.py` forces that specific
question to a specific chapter/section. **`PIN` is the tool for irreducible
ambiguity, not a substitute for fixing a real content gap or a real pipeline
bug.** `ATSWA II`'s own log (RESUME.md, 2026-09-18) found and fixed four
systemic pipeline bugs — a matcher scored against raw PDF instead of authored
content, unweighted MCQ options, a stale-`sec` bug that never cleared on
failure, and a preamble-carry-forward bug in extraction — before reaching for
`PIN` as the residual fix for genuinely hard cases. Read that RESUME.md entry
in full before building the equivalent pipeline here; it's the worked example
of "citation looks wrong" almost always meaning either a pipeline bug or a
content gap, checked in that order, with `PIN` as the last resort.

Below a confidence threshold (`ATSWA II` used `0.12` on the retrieval margin),
**no citation renders at all** rather than risk showing a wrong one — silence
over a wrong link, applied to both the chapter-level and section-level tag.

### B.3a The clickable citation chain — verified against `ATSWA II`'s own code

§B.3 covers how a question is *assigned* to a chapter and section. This covers
how that assignment becomes **a link the reader can click**, which is a
separate mechanism and the one the user specifically asked to have copied.
Every detail below was read out of the working `ATSWA II` implementation on
2026-10-22, not inferred.

**Where `ATSWA II` actually lives.** `/Users/ndujekwuugochukwu/Desktop/ICAN/ATSWA II`
— a **sibling of `GREAT LOCK-IN`, not inside it**. This has already caused one
wasted search (`SKIILLS/PLAN.md` Phase 2 cites it as `ATSWA II/` and a lookup
relative to `GREAT LOCK-IN` finds nothing). From this file the path is
`../../ATSWA II/website/`.

**The chain has four links, and all four must be built or the citation is dead:**

1. **Data** — each question object in `data/exams.js` carries two fields:
   `"ch"` (integer chapter number, or `null`) and `"sec"` (the section number
   as a *string* exactly as the chapter uses it, e.g. `"8.6"`, or `null`).
   They sit directly on the question, alongside `n`/`stem`/`options`, for all
   three question types (`mcq`, `saq`, `secb`).

2. **The link** — `src/exams.js`'s `chBadge(subj, q)` renders the citation:

   ```js
   function chBadge(subj, q) {
     if (!q.ch) return '';                       // no citation at all
     if (q.sec) return '<a class="ch" href="#/s/' + subj + '/' + q.ch + '?sec=' +
       String(q.sec).replace(/\./g, '-') + '">Chapter ' + q.ch + ' &rarr;</a>';
     return '<a class="ch" href="#/s/' + subj + '/' + q.ch + '">Chapter ' + q.ch + '</a>';
   }
   ```

   Note the three-way behaviour, which is the whole design: **a section-level
   link with an arrow** when the section is known, **a bare chapter link** when
   only the chapter is, and **nothing at all** when neither is confident. The
   dots in the section number become dashes in the query string (`8.6` →
   `8-6`).

3. **The target** — `src/app.js` gives every rendered section an id built the
   same way, so the link has something to land on:

   ```js
   '<section class="sec" id="sec-' + esc(sec.n).replace(/\./g, '-') + '">'
   ```

   The right-hand table of contents uses the same ids (`#sec-8-6`), so the
   anchor scheme serves both.

4. **The jump** — `src/app.js`'s `scrollToAnchor()` reads `?sec=` off the
   route, scrolls to `#sec-<sec>`, and adds a `landed` class for 2.6 seconds
   so the reader can *see* where they arrived rather than merely being
   scrolled there:

   ```js
   el.scrollIntoView({ block: 'start', behavior: 'smooth' });
   el.classList.add('landed');
   setTimeout(function () { el.classList.remove('landed'); }, 2600);
   ```

   with one line of CSS in `src/page.html`:
   `.sec.landed{background-color:var(--accent-wash,rgba(31,98,68,.08));}`
   and the badge styled at `.bq .h .ch{…}` / `a.ch:hover{text-decoration:underline;}`.

   It degrades safely: no `?sec=` → scroll to top; a `?sec=` that matches no
   element → scroll to top. A stale citation never throws.

**The benchmark to match.** Measured on `ATSWA II`'s shipped `data/exams.js`:

| | questions | has `ch` | has `sec` |
|---|---:|---:|---:|
| MCQ | 2,859 | 2,418 (84.6%) | 1,953 (68.3%) |
| Short answer | 1,903 | 1,580 (83.0%) | 1,291 (67.8%) |
| Section B | 562 | 462 (82.2%) | 373 (66.4%) |
| **All** | **5,324** | **4,460 (83.8%)** | **3,617 (67.9%)** |

96 papers = 4 subjects × 24 diets (2014-03 to 2026-03). So **~84% chapter
coverage and ~68% section coverage is the standard that was actually
achieved**, with the remainder deliberately left uncited rather than guessed.
Do not treat a lower number here as acceptable without a reason, and do not
inflate it by lowering the confidence gates.

**Two further per-question dictionaries** sit beside `papers` in the same
payload, keyed `"<diet>/<subject>/<kind>/<n>"` (e.g. `"2016-09/FA/mcq/3"`):

- **`notes`** (186 entries in `ATSWA II`) — an added explanation for a
  question whose official solution is a bare answer with no working. TeX is
  allowed and used heavily.
- **`flags`** (`corrections.py`'s `FLAGS`) — a correction where **the printed
  paper or its official key is wrong**. `ATSWA II`'s examples: a key that
  gives "Bonus" for an MCQ when that is not one of the options and appears to
  be a short-answer solution set in the wrong column; a key that claims
  segment reporting features in the *IFRS for SMEs* when the standard
  expressly exempts SMEs from it.

`flags` is the hook for this project's **scheme-change flagging** requirement
(Phase 4 below) — same field, same rendering, a different reason for firing.

### B.4 Tools built mid-project (not from day one)

These need real content to work against — build them once a subject or two
is actually authored and tagged, not before:

- **`tools/audit_answers.py`** — searches for a question's own *correct-
  answer text* (not the stem) across chapter content, far more decisive than
  stem-based matching for finding real content gaps and mislinked citations.
  Needed real iteration in `ATSWA II` to reach useful precision: strip
  stopwords from both sides consistently, restrict to short (2–6 word)
  answers only (long descriptive answers false-positive constantly), and
  exclude "which is NOT/EXCEPT/CANNOT" questions (their correct answer is,
  by construction, the one option *not* actually in the source).
- **`tools/audit_abbrevs.py`** — flags an ALL-CAPS 2–6 letter token used in a
  chapter with no "(ABBR)" spelled out anywhere in that chapter. Very noisy
  unfiltered (roman numerals, quiz-stem "NOT"/"EXCEPT", table headers) —
  narrow to abbreviations that actually appear in a real past-exam question
  stem before chasing any of them; polishing an acronym no exam has ever
  tested isn't a good use of the pass.
- **`tools/final_revision.py`** — clusters every past question by subject +
  type (MCQ/short-answer/essay) + citation, frequency-ranked ("ASKED N×"),
  into a "Final Revision" bank surfaced in the app's own UI (needs matching
  `src/revision.js` view code and `#/revision/...` routes — the script alone
  produces `data/revision.js`, but is invisible until the UI consumes it;
  `ATSWA II` had exactly this gap for a while, script done but nothing
  rendering it, until someone noticed).
- **`tools/expansions.py`** (mentioned in `ATSWA II`'s early "Next, in order"
  list; check whether it still exists / was ever built by the time this is
  needed) — two dicts, `NOTES = {"2026-03/FA/mcq/7": "...expansion..."}` for
  worked MCQ-answer expansions shown in quizzes and exam review, and
  `SECB_NOTES = {"2026-03/FA/1": [blocks]}` for a worked expansion rendered
  above an official Section B solution. `build_exams.py` imports this
  optionally — safe to leave absent until there's an actual expansion worth
  writing.

### B.5 `tools/test.mjs` — the regression suite

A `jsdom`-based headless test suite (`npm install jsdom --no-save`,
gitignored), re-run after **every** content change, not just UI changes.
Write this project's equivalent early in Phase 2, even with almost nothing to
test yet — `ATSWA II` started without it (early sessions verified by hand or
skipped verification, per its own RESUME.md admission) and grew it in later
mid-project, which meant some early regressions went uncaught for a while.
Cheaper to grow the suite alongside content from the start than retrofit it.
`ATSWA II` reached 21–22 passing tests by its later sessions covering:
routing, every subject's chapter count, specific sentences rendering
correctly (regression-proofing a "this is not a bug" judgment call directly
in the suite, not just in a commit message), citation-link scroll-targets,
and UI features as they're added.

### B.6 `website/guides/*.html` — standalone deep-dive pages

For a topic too big or too cross-cutting for one chapter section —
`ATSWA II` built `guides/crf.html`, `guides/ipsas.html`, `guides/
statements.html` for Public Sector Accounting topics that span many chapters
or need a from-scratch, heavily-illustrated treatment. Plain static HTML,
styled to match the site's own light/dark tokens, linked from the relevant
chapter section via the existing `[label](url)` inline syntax (works with
any relative path already — no app-code change needed to add one). Build
these **reactively**, when a topic genuinely earns one — not preemptively for
every subject. A candidate for this project: ATSWA III's Taxation subject
often has cross-cutting computational topics (e.g. a full worked tax-
computation walkthrough) that might outgrow a single chapter section the way
IPSAS did for Public Sector Accounting — watch for this once Taxation
transcription is underway, don't force it in advance.

### B.7 `PROGRESS.md` — this project's own running log

Every `ATSWA II` session appended a dated, narrative entry to its
`RESUME.md`: what was asked, what was found, what was changed, what rebuild
commands were run, what the test suite reported, and — just as importantly —
what was explicitly **not** done and flagged as a gap rather than silently
skipped. `PROGRESS.md` (sibling file to this one) plays that exact role for
this project, starting the moment `website/` exists. Until then, this
document's own "Where things stand" section is the log.

---

## Part C — Working principles

Carried over from `ATSWA II` (confirmed repeatedly, in writing, across its
own session log — these are not inferred, they're the project's own stated
rules):

1. **Full fidelity to the source study-text PDF, not just Q&A closure.**
   Body content, definitions, worked illustrations, "schools of thought"
   style discussion — everything the book itself has. A chapter with a
   correct formula box and a good end-of-chapter quiz but that skipped the
   book's own expository prose is **not done**, even if it looks complete at
   a glance.

   ### 1A. THE GOVERNING RULE — restated by the user on 2026-10-13 and again
   ### on 2026-10-17, after two separate rounds of rework were caused by
   ### ignoring it. Read this before authoring a single line of any chapter.

   > **EVERY SINGLE DETAIL IN THE STUDY TEXTS MUST BE PRESENT ON THE SITE.
   > NOTHING MAY BE OMITTED, CONDENSED, SUMMARISED, PARAPHRASED AWAY, OR
   > REPLACED BY A CROSS-REFERENCE. THE ONLY PERMITTED DEPARTURES FROM THE
   > BOOK ARE *ADDITIONS* — EXPLANATIONS, CLARIFICATIONS, WORKED DETAIL AND
   > CORRECTIONS OF THE BOOK'S OWN ERRORS.**

   What this rules out, concretely — every item below has actually happened
   on this project and had to be undone:

   - **No summarising.** If the book spends four paragraphs on something, the
     site carries the substance of all four. "The gist of it" is not fidelity.
   - **No dropped end-of-chapter material.** Every study text chapter ends with
     a `CHAPTER SUMMARY`, a `MULTIPLE-CHOICE AND SHORT-ANSWER` bank *and* a set
     of `EXAMINATION TYPE QUESTIONS`. **All three must be transcribed**, and the
     exam-type questions must be *worked*, not merely reproduced. (98 of these
     were missing across CA ch2–ch10 before the 2026-10-13 rework; the same gap
     exists in every chapter not yet re-done.)
   - **No dropped illustrations.** Every `Illustration N.N` in the book appears
     on the site, with its question *and* a full solution. Count them in the
     source before declaring a chapter finished.
   - **No cross-references in place of content.** "Covered in full in Chapter 1
     §1.3" is not a transcription. If the book repeats itself, the site repeats
     it too — each chapter must stand alone.
   - **No prose narration of something the book presents as a table, an account
     or a statement.** Ledger accounts become `tacc` blocks; financial
     statements, cost cards, schedules and quantity reconciliations become
     `stmt` blocks; everything else tabular becomes a `table`. A worked example
     narrated as a paragraph is the single defect the user has complained about
     most ("the question is not even tabulated, it is unintelligible").
   - **No silently "fixing" the book's data to make its own answer work.** Where
     the source is wrong, inconsistent or mis-typeset, say so in a `warn` block,
     show the evidence, give the corrected figures, and work the question
     properly. Never alter a question's stated data without flagging it.
   - **No skipping a table because `pdftotext` mangled it.** Several tables in
     these PDFs are **scanned images** and are invisible to text extraction
     altogether (e.g. CA ch2's HIMCO power-cost table). Render the page with
     `pdftoppm -r 140 -png` and read it. Others are text but have their captions
     and figures a row out of step — render the page and realign them.
   - **Every question keeps its citation and its marks.** Each examination-type
     question is tagged with the body, paper and diet the study text credits it
     to (ICAN Nov/Dec 1993, ICAG May 2002, ACCA June 1998, CIMA Nov 1979, CACA
     June 1987, BUK 1993 …) and with its mark allocation, exactly as printed.
     This is not decoration. It is what lets a reader trace any question back to
     its source, it is what the Phase 4 past-question pipeline cites against,
     and it is a second reason nothing may be dropped — a citation that points
     at content the site does not actually carry is worse than no citation. The
     same applies to the book's own illustration numbers (`Illustration 6.1`),
     section numbers and page-level structure: **they are the reference system,
     so they must survive transcription intact.**
   - **Section numbering must match the book's own**, down to sub-sections
     (1.2.1, 1.2.12, 1.3.9 …), so a student can cross-reference the PDF page by
     page. Do not collapse the book's numbered sub-sections into unnumbered
     headings.

   **The completeness test before any chapter is called done:** open the source
   chapter and count — sections and sub-sections, illustrations, tables,
   definitions, numbered lists, the chapter summary, the MCQ/short-answer bank
   and the exam-type questions. Every one of those counts must be matched on the
   site. If a count is lower, the chapter is not done. **Important lesson from `ATSWA II`'s own history**: its
   earliest chapters (FA 1–8, all of early PS/QA) were written as a lighter
   "house-style rewrite" — summarized prose plus originally-authored
   quizzes, not a transcription — and this had to be revisited, subject by
   subject, sometimes chapter by chapter, once the user asked for real
   fidelity ("no information should be lost... thoroughly transcribe it
   all"). **Start this project's chapters at full fidelity from chapter 1 of
   the first subject — do not repeat the two-pass rework `ATSWA II` went
   through.**
2. **"Any list is listed and not stated."** A prose run-on enumeration ("the
   three types are X, which does A; Y, which does B; and Z...") becomes a
   real `ul`/`ol` block. Applies retroactively when found later, not just to
   new content as it's written.
3. When a concept is genuinely missing from the study text but is standard,
   uncontroversial material a past exam's own answer key already uses with
   confidence — **add it**, sourced, flagged as filling a book gap. Not
   fabrication; the concept demonstrably belongs in the syllabus if the
   examiner tests it.
4. When something is missing from **every** source (study text and every
   past answer key available) — flag it, do not invent it.
5. Where a past paper's own printed answer key is internally inconsistent, or
   contradicts another diet's answer to the same underlying question —
   present the majority position as the default and say so explicitly in a
   `note`/`warn` block. Never silently pick a side, never refuse to answer.
6. Rebuild the **full** pipeline after every content change and re-run the
   test suite before considering any change done — not just the one script
   that touches the file just edited. A content edit can shift retrieval
   scores for questions in completely unrelated chapters.
7. Be honest in `PROGRESS.md` about what was **not** verified. "Every single
   question individually checked against the PDF" is not a realistic claim
   at corpus scale — say what sampling method or audit tool was actually
   used instead of overclaiming completeness. `ATSWA II`'s own log models
   this repeatedly and explicitly.

**New for this project** (explicitly requested by the user this session, not
written down as an explicit rule anywhere in `ATSWA II`'s own docs — stated
here for the first time, in writing, as this project's own standing rule):

8. **Everything listable gets listed on the site, even if the study text
   itself never presents it as a list.** Stronger and more general than
   principle 2 — not limited to converting the book's *own* run-on prose. If
   a concept has enumerable parts at all (named sub-types, steps, criteria,
   examples, any fixed set of things) and the book only ever mentions them
   individually, scattered across paragraphs or even across sections, pull
   them together into an explicit list on the site anyway. Where to draw the
   line (two related things mentioned in passing isn't automatically a list)
   is a judgement call for whoever authors that section — same as principle
   2 already required — but the default leans toward listing, not toward
   matching the book's own prose structure.
9. **Formatting must be perfect.** No unbalanced TeX braces, no unclosed
   inline markup, no inconsistent heading levels, no block-type typos.
   `build_content.py`'s validate-as-it-builds behaviour is the mechanical
   backstop, not the standard — the standard is that a finished chapter reads
   as cleanly authored prose and structured data, never as a PDF dump with
   markup sprinkled on top.
10. **The user explicitly asked for "explanation of hard stuff."** Where the
    study text states something technical or easy to misunderstand without
    unpacking it, add a plain-language explanation alongside the book's own
    wording — a `note` or `key` block next to the formal definition, not a
    replacement for it. This is distinct from principle 1 (fidelity to the
    source) — it's an *addition* on top of full fidelity, not a substitute
    for it. Judgement call on what counts as "hard" stays with whoever
    authors the chapter; when in doubt, add the explanation — the cost of an
    unnecessary explanatory aside is much lower than the cost of a genuinely
    hard concept left unexplained.

---

## Part D — Sequencing (the actual plan, session by session)

**Strict ordering, per the user's explicit instruction**: finish
transcription + explanation for **every subject in this project** (and, per
the same instruction, every subject in the Skills project too — see
`../SKIILLS/PLAN.md` Part D) before appending a single past-exam question to
any chapter, in either project. Do not interleave. A half-transcribed
subject with past questions already linked in is exactly the kind of partial
state that caused rework in `ATSWA II` (Part B.3 above) — several "citation
is wrong" bugs there turned out to be "the content isn't there yet" in
disguise. Getting the ordering right the first time avoids repeating that.

### Phase 1 — Reconnaissance & planning ✅ (2026-09-25, session 1)
- [x] Download last-20-diet target (15/20 — see gaps in §A.2)
- [x] Confirm the subject list from a primary source, not assumption
- [x] Read and condense the `ATSWA II` methodology into this document
- [x] State the project's working principles explicitly, including the two
      new ones the user added this session
- [x] *Optional follow-up, completed 2026-11-11*: retry the Wayback Machine's `cdx`
      API for the 5 missing diets once not rate-limited (see
      `../DOWNLOADS_LOG.md`, "Still outstanding")

### Phase 2 — Scaffolding (first thing once "continue" is said)
- [x] `git init` this project (mirroring `ATSWA II`'s own repo)
- [x] Copy `ATSWA II/website/`'s skeleton — `src/`, `tools/`, `build.sh`,
      a `.gitignore` (`node_modules/`) — **adapt, don't blindly copy**:
      `tools/build_content.py`'s `SUBJECTS` dict, `tools/corrections.py`'s
      `CHAPTER_KEYS`, and `src/subjects.js`'s `SUBJECTS` array all need this
      project's own 4 subject codes (§A.1), not `ATSWA II`'s `fa`/`ps`/`qa`/`it`.
- [x] Create `content/<code>/` for each of the 4 subjects with a stub
      `meta.py` (mirrors `ATSWA II/website/content/it/meta.py`'s pattern —
      read that actual file when this step is reached, it wasn't reproduced
      here to avoid this document going stale if the pattern evolves).
- [x] Create `website/PROGRESS.md`, first entry: "scaffold created, no
      content yet."
- [x] Write `tools/test.mjs`'s skeleton now, per B.5, even with almost
      nothing to test.
- [x] Write `website/README.md` for this project — adapt `ATSWA II`'s own
      as a direct template (deploy instructions, "what is here" table,
      content schema, rebuild commands).

### Phase 3 — Transcription + explanation, all 4 subjects ✅

- [x] Cost Accounting — 15/15 chapters, including the full fidelity re-audit.
- [x] Principles of Auditing & Assurance — 12/12 chapters.
- [x] Taxation — 25/25 chapters, 2026 study text and its own section numbers.
- [x] Management — 10/10 chapters, including lettered section numbering.

The 2026-10-17 re-audit and chapter-by-chapter evidence are in PROGRESS.md.
The governing rule in Part C applies to every subsequent change: every source
definition, section, table, illustration, summary and examination question is
retained. Explanations, corrections and source-backed gap supplements are
additions, never replacements. Skills remains on hold; it does not gate this
project's Phase 4.

### Phase 4 — Past-question pipeline ✅ (2026-11-11)

**Gate lifted.** This used to read "only after Phase 3 is fully done for BOTH
projects". Skills is now on hold (see "Where things stand"), so Phase 4 runs
on ATSWA III alone.

#### What the source material actually is — confirmed 2026-10-22

`materials/past-questions/` holds **15 INSIGHT Part III packs**, one per diet,
**2019-03 (March 2019) through 2026-03 (March 2026)**:

    2019-03  2019-09  2020-03  2020-09  2021-03  2021-09  2022-03  2022-09
    2023-03  2023-09  2024-03  2024-09  2025-03  2025-09  2026-03

Each pack holds **four papers in this order**: **Principles of Auditing &
Assurance → Cost Accounting → Taxation → Management**. So the expected yield is
**15 × 4 = 60 papers**.

Each paper has the **same three-part structure as Part II**, which is why
`extract_papers.py` should port rather than be rewritten:

- **Section A: Part I** — 30 multiple-choice questions (30 marks), attempt all
- **Section A: Part II** — 20 short-answer questions (20 marks), attempt all
- **Section B** — 6 questions, **attempt any four** (50 marks)

followed by the official solutions for all three parts. Answer keys print in
the plain numbered form (`1.  B` / `2.  A` …) under
`SECTION A: PART I / MULTIPLE-CHOICE SOLUTIONS`.

**Corrected source finding (2026-11-10): examiner reports are present.**
The extractor preserves them: 59 MCQ reports and 352 essay reports were
identified. Missing-report cases must be checked against the original source;
never invent a report or remove the field because of the old planning guess.

Expected total, if Part III yields the same per-paper counts as Part II:
60 papers × (30 + 20 + 6) = **3,360 questions**.

#### Steps

- [x] **Re-read `../../ATSWA II/website/RESUME.md`** (76 KB, session-by-session)
      — specifically the 2026-09-18 entry on the four systemic pipeline bugs,
      before writing any of this. Part B.3 explains why.
- [x] Adapt and run `extract_papers.py` on all 15 packs → `data/papers.json`.
      Expect per-pack subject splitting on the four title pages, and verify the
      count: 60 papers, 1,800 MCQ, 1,200 SAQ, 360 Section B.
- [x] Verify extraction **before** tagging: every paper has 30 MCQ with 5
      options each, 20 SAQ, 6 Section B, and an answer key of 30 entries.
      A missing or short paper is an extraction bug, not a source gap.
      Confirmed printed exceptions (four options/irregular labels) are preserved
      and tested; all 60 papers have the complete 30/20/6 inventory.
- [x] Seed `CHAPTER_KEYS` in `tools/corrections.py` for all four subjects
      **before** running `aim.py`, not after (Part B.3). `ATSWA II` seeded
      16/23/20/6 chapters for FA/PS/QA/IT; here that is 12 Auditing, 15 Cost
      Accounting, 25 Taxation, 10 Management.
- [x] Adapt and run `aim.py` — chapter-level tagging, scored against our own
      authored `content/<code>/ch*.py`, stem weighted 3× over options.
- [x] Adapt and run `aim_sec.py` for **all four codes** — section-level
      tagging. Keep both gates: `CH_CONF_MIN = 0.10` (don't refine a shaky
      chapter tag) and `MARGIN_MIN = 0.10` (top section must beat the
      runner-up).
- [x] Adapt and run `build_exams.py` → `data/exams.js`, keeping
      `CH_CONF_MIN = 0.12` so a thin chapter match renders **no citation at
      all**. Silence over a wrong link, both levels.
- [x] **Build the full clickable chain of §B.3a** — not just the data. The
      `ch`/`sec` fields are worthless until `chBadge()`, the `id="sec-…"`
      targets, `scrollToAnchor()` and the `.landed` CSS are all in place.
      `src/exams.js` and `src/app.js` here were cloned from `ATSWA II`, so
      check what already exists before writing it: `data/exams.js` now exists and all three question types render source
      links and clickable chapter/section references.
- [x] Spot-check a real, stratified sample per subject before trusting the
      output (Part B.3 — pipeline bugs hide as "bad citations"). Target
      **≥84% chapter and ≥68% section** coverage, the measured `ATSWA II`
      benchmark in §B.3a. Do not reach the number by loosening the gates.
      Final coverage is 100% at both levels, with 1,434 human-reviewed targets
      and 171 secondary essay passage links. Sources and targets are validated.
- [x] **Scheme-change flagging** — see the next sub-section. This is new to
      this project; `ATSWA II` had no equivalent problem at this scale.
- [x] `final_revision.py` once tagging is trustworthy, **plus its UI**
      (`src/revision.js`) — don't let the script-without-UI gap `ATSWA II` hit
      happen here.

#### Scheme-change flagging (new requirement, 2026-10-22)

These papers span **2019 to 2026**, and the law moved underneath them. A
question can be perfectly valid as a historical artefact and **actively wrong
as current law**. Reproducing it silently teaches the wrong answer.

**The rule: where a question, its options, or its official solution states
something that the law or standard no longer supports, flag it on the
question — do not silently reproduce it, and do not quietly "correct" the
printed paper either.** The reader must see both what was set and what is true
now.

**Taxation is the acute case.** `Taxation_2026_Study_Text.pdf` is the 5th
edition and reflects the **Nigeria Tax Act 2025** and **Nigeria Tax
Administration Act 2025**, effective from the **September 2026 diet**, which
displace the **CITA / PITA / VAT Act / Stamp Duties Act** framework that
**every one of the 15 packs was set under**. So essentially the whole Taxation
question bank needs reading against the new Acts. Expect to flag, at minimum:
rate changes, threshold and exemption changes, renamed or merged taxes, the
new **surcharge on fossil fuel products** (study text ch11) having no
counterpart in older papers, and any administrative provision now sitting in
NTAA 2025 rather than its old home.

**The other three subjects need a lighter pass but are not exempt:** Auditing
moved on ISA revisions and on **CAMA 2020** replacing CAMA 1990 (section
numbers in particular — a pre-2020 paper citing s.331 or s.359 is citing a
statute that has been renumbered); Cost Accounting and Management are largely
stable but check anything citing a standard, a statute or a named institution.

**Mechanism: reuse `flags`.** §B.3a documents it — a per-question dictionary
in `data/exams.js` keyed `"<diet>/<subject>/<kind>/<n>"`, already rendered by
the app, already used by `ATSWA II` for "the printed key is wrong". A
scheme-change flag is the same field firing for a different reason. **Do not
invent a second mechanism.** Consider a `kind` discriminator on the flag
("key error" vs "superseded law") only if the UI genuinely needs to style them
differently; decide that when the first fifty are written, not now.

Two things the flag text must do, every time:

1. **Say what the paper says, and why it is no longer right** — naming the
   provision that changed and the Act that changed it. "Superseded" with no
   citation is useless to someone revising.
2. **Say what the answer would be today**, where that is determinable. Where
   it is not — because the new Act has no equivalent provision — say that
   instead, plainly.

The same honesty rule as the chapter transcription applies: this is an
**addition** flagged as such, never a silent edit of the source.

### Phase 5 — Audit & polish ✅ (2026-11-11)
- [x] `audit_answers.py` pass per subject; semantic findings/corrections and
      retained literal-phrase candidates are documented.
- [x] `audit_abbrevs.py` pass per subject, filtered to exam-tested acronyms
- [x] Any `guides/*.html` that earn their place (Part B.6)
- [x] Full regression suite green, full pipeline rebuilt clean, before
      calling this site "done"
- [x] Retry the 5 missing diets (§A.2) one more time before final release —
      more time may mean a new Wayback snapshot exists, or ICAN may have
      fixed the dead `/documents/` path itself. Retry complete: both live paths
      return 591-byte HTML; PDF-filtered Wayback CDX is empty for all five.
      Four archive fetches were rate-limited, the successful one is HTML.
      Evidence: website/data/source-availability.json.

### Phase 6 — Manual Vercel handoff ✅ (2026-11-11)
- [x] Leave the completed static source and optional runtime dist/ ready for
      the user to deploy through Vercel. The user controls publication.
- [x] Keep the updated site available at http://localhost:4000/.
- [x] Verify the local home, chapter data, exams, revision and Tax guide match
      the current files. Do not perform further hosting actions.

---

## Part E — Recorded scope decisions

- Subject codes are implemented consistently as `aud`, `ca`, `tax`, `man`.
- This release uses the four supplied study texts: 2025 Auditing, Cost
  Accounting and Management, and 2026 Taxation. Later editions or the revised
  syllabus are future source updates, not silent replacements of this corpus.
- The five missing older diets have been retried and documented. They can be
  added if authentic PDFs are later recovered; no response from the user is
  needed to finish the available 15-diet corpus.
- Skills remains on hold. September 2026 is outside this release's agreed
  diet range.
- The user deploys through Vercel. Development remains on localhost:4000.
  The accidental Sites publication is historical and is not the active target;
  its recovery metadata is archived under website/.cache/.
