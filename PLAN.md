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

**Phase: 3 COMPLETE — all four ATSWA III subjects done. Cost Accounting (15/15).
Auditing (12/12). Taxation (25/25). Management (10/10).** Next: the Skills project at
`../SKIILLS/`, same standard, same method.** Reconnaissance done earlier this session:
`Taxation_2026_Study_Text.pdf` extracted (5th edition — reflects the brand-new Nigeria
Tax Act 2025 / Nigeria Tax Administration Act 2025 reform, effective the September 2026
diet, replacing the older CITA/PITA/VAT-Act framework), confirmed **25 chapters** from
its own TOC: (1) Introduction to Taxation; (2) Administration of Taxation; (3) Basic
Ethical Issues in Taxation; (4) Returns, Assessments and Collection Procedures; (5)
Objections and Appeal Procedures; (6) Tax Clearance Certificate; (7) Value Added Tax;
(8) Stamp Duties; (9) Withholding Tax; (10) Customs and Excise Duties; (11) Surcharge on
Fossil Fuel Products; (12) Taxation of Employment Income; (13) Computation of Personal
Income Tax; (14) Taxation of Investment Income; (15) Taxation of Sole Traders/Self-
Employed Individuals; (16) Capital Allowances; (17) Taxation in Partnerships; (18)
Settlement, Trusts and Estates; (19) Loss Relief; (20) Ascertainment of Assessable
Profit; (21) Computation of Companies Income Tax; (22) Taxation of Specialised
Businesses (the largest chapter by far — ~4,900 raw-text lines covering 18 distinct
specialised-business sub-topics); (23) Federal Development Levy; (24) Chargeable Gains;
(25) Application of IT in Taxation. `SUBJECTS` in `tools/build_content.py` updated to
add `'tax': ('TAX', 25)`, `content/tax/meta.py` and `src/subjects.js`'s TAX entry added.
Chapter 22 (Taxation of Specialised Businesses) — by far the largest chapter in the
subject, covering all 18 specialised-business sub-topics with the digital-economy/e-
commerce section deliberately compressed from source (see PROGRESS.md for the full
rationale). Chapter 23 (Federal Development Levy) — confirmed the FDL replaced TET/
Police Trust Fund/NITDA/NASENI levies (resolving ch19's flagged ambiguity), and flagged a
genuine source inconsistency in Illustration 23.3. Chapter 24 (Chargeable Gains) — the
NTA 2025's repeal of the old standalone CGT Act, full computation/exemption framework,
all 5 numeric illustrations verified clean. Chapter 25 (Application of IT in Taxation) —
the FINAL chapter, purely descriptive (TaxPro Max, Rev360, SEP/digital-tax framework),
completing the subject. **Rebuilt and re-verified the full site via a fresh headless
jsdom smoke test** — all 25 chapters confirmed live and rendering real content, zero JS
errors.

**Management started this session: chapter 1 of 10 done (10%).** Reconnaissance done:
`2025_MAN.pdf` extracted (17,937 lines), confirmed **10 chapters** from its own Contents
Summary and detailed TOC: (1) Nature of Business (3 lettered sub-sections: A Introduction
to Business, B Business Environment, C CSR/Business Ethics/Corporate Governance); (2)
Management Theories and Thoughts; (3) Management Process; (4) Organic Business
Functions; (5) Managing of Work Relationships; (6) Business Process Re-engineering; (7)
Organisational Effectiveness; (8) Office Practice and Procedure, Health and Safety; (9)
Contemporary Management Issues; (10) Entrepreneurship. A structurally distinct subject —
almost entirely qualitative/conceptual (no numeric computation), several chapters split
into lettered Sections each with their OWN embedded, answer-keyed MCQ/short-answer
review questions this project can draw on directly. `SUBJECTS` in
`tools/build_content.py` updated to add `'man': ('MAN', 10)`, `content/man/meta.py` and
`src/subjects.js`'s MAN entry added (once ch1 validated, per this project's established
convention). Chapters 1 (Nature of Business), 2 (Management Theories and Thoughts — full
historical evolution of management thought), 3 (Management Process — 6 sub-sections:
planning/decision-making/organising/coordination/controlling/strategic management), 4
(Organic Business Functions — the LARGEST chapter, 4 sub-sections: HR/production/
marketing/finance-accounting), 5 (Managing of Work Relationships — 8 sub-sections:
motivation/leadership/groups/conflict/attitude/communication/emotional intelligence/
change), and 6 (Business Process Re-engineering) done, full-fidelity, clean build. Full
site rebuilt and verified after every chapter.

**SESSION CHECKPOINT REACHED**: Management now stands at exactly 6/10 chapters (60%) —
the threshold the user explicitly instructed this session to stop at. Transcription
pauses here rather than continuing to subject completion (unlike the full-completion
CA/AUD/TAX runs earlier this session). **ch7 (Organisational Effectiveness, the
shortest chapter — 135 lines) is next whenever work resumes**, followed by ch8 (Office
Practice/Health and Safety), ch9 (Contemporary Management Issues), and ch10
(Entrepreneurship — the FINAL chapter). Completing these 4 would finish Management,
leaving only the Skills project's Phase 3 outstanding before Phase 4 (past-question
linking) becomes possible for either project, per the standing cross-project
sequencing rule.

**Still outstanding** (deferred until Phase 4, which cannot start until every subject in
both this project and Skills finishes Phase 3): `git init`, the rest of `tools/`
(`aim.py`, `aim_sec.py`, `corrections.py`, `extract_papers.py`, `build_exams.py`,
`outline.py`, `common.py`, `final_revision.py`, `audit_*.py`, `expansions.py`),
`tools/test.mjs`, `website/README.md`, and all of Phase 2 for Skills, which has not
started Phase 3 at all yet. See `PROGRESS.md`'s latest entries for full chapter-by-
chapter detail, and for how to view the site locally right now.

Done (2026-09-25, session 1):
- Downloaded 15 of the last-20 target INSIGHT diets. See `../DOWNLOADS_LOG.md`
  for the exact 5 that are currently unrecoverable and why.
- Reorganised `materials/` into `study-texts/` + `past-questions/`, matching
  `ATSWA II/materials/`'s own layout.
- Confirmed the 4-subject list directly from a real INSIGHT pack's table of
  contents (§A.1 below), not assumed from memory.
- Read `ATSWA II/website/README.md` in full and `ATSWA II/website/RESUME.md`
  in full (all 1098 lines, both halves read directly, not sampled) to
  reverse-engineer the methodology in Part B below.
- Checked `ATSWA II` for hidden files beyond `.git`/`.DS_Store`: only
  `website/.gitignore` (excludes `node_modules/`) and the `node_modules/`
  tree itself. Nothing else hidden, nothing missed.
- Located `ATSWA II`'s own Claude Code session transcripts (5 top-level
  sessions, 2026-09-04 → 2026-09-25, ~120MB combined, plus per-session
  subagent transcripts) at `~/.claude/projects/-Users-ndujekwuugochukwu-
  Desktop-ATSWA-II/`. **Deliberately not read in full** — `RESUME.md` is
  itself the distilled, narrative record of exactly these sessions, written
  session-by-session as they happened, and re-deriving the same information
  from ~120MB of raw transcript would be redundant with what's already in
  Part B/C below. If a future session needs a specific decision's *exact*
  original wording (not just its distilled outcome), the transcripts are
  there to grep, by date, against a RESUME.md entry's own date heading.
- Explained the "Pilot Questions and Answers" section the user asked about —
  Part A, §A.4 (this is a Skills/Professional-level resource; not directly
  relevant to ATSWA III, cross-referenced here for completeness).

**Next action, when the user next says "continue":**
1. Re-read this document in full, then `PROGRESS.md` (once it has entries).
2. Resume at the first unchecked box in **Part D**.
3. If mid-session context was lost, this file + `PROGRESS.md` are the full
   state — nothing else needs reconstructing from memory.

**Standing instruction from the user:** stop and end the session cleanly
whenever session usage reaches the user's current stated threshold, without
leaving work half-applied — finish the current file/edit, append a
`PROGRESS.md` entry recording exactly what was done and what's next, update
the Part D checklist, and stop. **This threshold was raised from 70% to 88%
mid-session on 2026-09-25** — always use whatever value the user most
recently stated, not this document's own history of it.

---

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

**Confirm these 4 codes before Phase 2 locks them in** — renaming a subject
code later means renaming a `content/<code>/` directory and every reference
to it in `tools/corrections.py` and `src/subjects.js`.

### A.2 Past questions

INSIGHT packs, one PDF per diet, each containing all 4 subjects together
(same convention as `ATSWA II`'s Part II packs — not one file per subject).
Diet cycle: March / September.

**15 of the last-20-diet target downloaded**, March 2019 → March 2026, no
internal gaps. **5 older diets (September 2016, March 2017, September 2017,
March 2018, September 2018) are currently unrecoverable** — dead on ICAN's
own site and the earliest Wayback Machine snapshot on file already shows the
same dead link. Full detail, exact URLs, and the verification method are in
`../DOWNLOADS_LOG.md`. September 2026 was correctly excluded per the user's
instruction (not yet published — March 2026 is the latest real diet).

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
- [ ] *Optional follow-up, not blocking*: retry the Wayback Machine's `cdx`
      API for the 5 missing diets once not rate-limited (see
      `../DOWNLOADS_LOG.md`, "Still outstanding")

### Phase 2 — Scaffolding (first thing once "continue" is said)
- [ ] `git init` this project (mirroring `ATSWA II`'s own repo)
- [ ] Copy `ATSWA II/website/`'s skeleton — `src/`, `tools/`, `build.sh`,
      a `.gitignore` (`node_modules/`) — **adapt, don't blindly copy**:
      `tools/build_content.py`'s `SUBJECTS` dict, `tools/corrections.py`'s
      `CHAPTER_KEYS`, and `src/subjects.js`'s `SUBJECTS` array all need this
      project's own 4 subject codes (§A.1), not `ATSWA II`'s `fa`/`ps`/`qa`/`it`.
- [ ] Create `content/<code>/` for each of the 4 subjects with a stub
      `meta.py` (mirrors `ATSWA II/website/content/it/meta.py`'s pattern —
      read that actual file when this step is reached, it wasn't reproduced
      here to avoid this document going stale if the pattern evolves).
- [ ] Create `website/PROGRESS.md`, first entry: "scaffold created, no
      content yet."
- [ ] Write `tools/test.mjs`'s skeleton now, per B.5, even with almost
      nothing to test.
- [ ] Write `website/README.md` for this project — adapt `ATSWA II`'s own
      as a direct template (deploy instructions, "what is here" table,
      content schema, rebuild commands).

### Phase 3 — Transcription + explanation, all 4 subjects

**2026-10-17 — standing order from the user, overriding the "done" ticks below.**
Every subject in this project, and then every subject in the Skills project, is
to be brought up to the §1A standard above. A chapter previously ticked as
"done" is **not** done if it fails the §1A completeness test — and the CA
re-audit proved that most do, because the end-of-chapter examination-type
questions were never transcribed in any subject and the `tacc`/`stmt` block
types were never used. The order is:

1. **Cost Accounting ch11–15** — the remainder of CA. ✅ **DONE**
2. **Principles of Auditing & Assurance ch1–12** — re-audit all 12. ✅ **DONE**
3. **Taxation ch1–25** — re-audit all 25. ✅ **DONE** (2026-10-17). Every
   chapter renumbered to the study text's own section *and* sub-section scheme —
   the site had been off by one throughout, because it renumbered content from
   `x.1` after correctly lifting the book's `x.0` learning objective and `x.1`
   learning outcomes into the chapter's `outcomes` panel. Collapsed sections
   split back out (worst: ch7's 40 book sections had been squeezed into 21).
   All **25 worked-example sections written for the first time** — 78 questions
   with the book's own suggested solutions, every figure recomputed
   independently. ~45 source defects flagged or corrected.
4. **Management ch1–10** — ✅ **DONE** (2026-10-17). ch7–ch10 written from
   scratch (they did not exist); ch1–ch6 audited. Management is numbered by
   **lettered section** (A.1, B.1, C.1 …) in chapters 1, 3, 4, 5 and 9, and each
   lettered section carries its own summary and review questions — **none of
   which the site had**. All of them are now transcribed with the book's own
   answer keys. **All ten chapters** renumbered to the book's full
   section/sub-section scheme — ch4 to §A.1–§A.17 / §B.1–§B.7 / §C.1–§C.12 /
   §D.1–§D.13 and ch5 to §A.1–§H.4, including the book's own gap at §C.4 of
   ch5, which is reproduced rather than closed. No residual items.
5. **Then the Skills project**, same standard, same method. *(next)*

Record progress against this list in `PROGRESS.md` as each chapter is finished.

Full-fidelity transcription from chapter 1 (per Part C, principle 1's
explicit lesson — no lighter first pass, no rework-later plan):

- [ ] **Principles of Auditing & Assurance** — all chapters
- [x] **Cost Accounting** — all 15 of 15 chapters done (see `PROGRESS.md`). Site rebuilt
      and re-verified via headless jsdom smoke test. **2026-10-09: full ch01-ch15
      fidelity audit against the source PDF for missing examples/info, completed**
      (see `PROGRESS.md`) — 2 previously-dropped worked illustrations restored (ch03,
      ch04), 2 smaller worked asides added (ch02, ch05), 1 drafting artifact cleaned up
      (ch08); ch01, ch06-ch15 confirmed already complete.
      **2026-10-13: chapters 1-10 RE-TRANSCRIBED in full** on the user's complaint that
      they read as a summary rather than a transcription (see `PROGRESS.md` for the full
      account). The 2026-10-09 audit had missed three systemic gaps: (a) the study text's
      end-of-chapter **EXAMINATION TYPE QUESTIONS were not transcribed in any chapter** —
      98 past-exam questions across ch2-ch10, now all reproduced with full worked
      answers; (b) worked illustrations were narrated in **prose** rather than set out as
      accounts — the `tacc` and `stmt` block types were used **zero times** in all 15 CA
      chapters despite the renderer and CSS supporting them from the start, and chapter
      6's Illustration 6.1 (nine incomplete ledger accounts) had been compressed into one
      run-on paragraph, which is what the user called "unintelligible"; (c) three of
      ch4's six illustrations and one of ch5's were missing altogether. Content files grew
      6,676 → 15,705 lines; `data/ca.js` 666 KB → 1,053 KB. **Roughly a dozen genuine
      numerical and typographical errors in the study text were found by recomputing every
      illustration independently, and are flagged on the page rather than silently
      corrected** — including one error that had been carried into the site itself (ch6's
      Illustration 6.1 profit statement did not add up; production overhead is
      over-absorbed by N3,000). One table (ch2's HIMCO power costs) exists in the PDF only
      as a **scanned image** and was recovered by rendering the page with `pdftoppm`.
      **Chapters 11-15 were NOT re-done** — the user asked for 1-10 — and still have gaps
      (a) and (b); they are the obvious next task.
- [x] **Principles of Auditing & Assurance** — all 12 of 12 chapters done (see
      `PROGRESS.md`): (1) Nature, Purpose and Scope of Auditing and Assurance; (2)
      Regulatory Framework of Auditing; (3) Professional Ethics and Public Interest; (4)
      Auditors' Liability; (5) Audit Planning and Documentation; (6) Audit Evidence and
      Verification Procedures; (7) Audit Tests and Sampling Procedures; (8) Internal
      Control System; (9) Public Sector Assurance; (10) IT-Based Audit Assurance; (11)
      Reports on Financial Statements; (12) Audit Completion. Site rebuilt and
      re-verified via headless jsdom smoke test.
- [x] **Taxation** — all 25/25 chapters done (see `PROGRESS.md`). Confirmed 25-chapter
      structure from `Taxation_2026_Study_Text.pdf`'s own TOC (5th edition, NTA/NTAA 2025
      reform) — full chapter list recorded above in "Where things stand." Site rebuilt
      and re-verified via headless jsdom smoke test.
- [ ] **Management** — chapters 1-6 of 10 done (see `PROGRESS.md`). Confirmed 10-chapter
      structure from `2025_MAN.pdf`'s own TOC/Contents Summary — full chapter list
      recorded above in "Where things stand." **Session capped at 6/10 chapters (60%)
      per explicit user instruction — this checkpoint has been reached. ch7
      (Organisational Effectiveness) is next when work resumes.**
- [x] **Taxation** — all chapters
- [ ] **Management** — all chapters

  Each subject, each chapter: full body content (every definition, worked
  illustration, discussion the book has — principle 1), every enumerable
  thing turned into a real list (principles 2 and 8), hard/technical points
  given a plain-language explanation alongside the book's own wording
  (principle 10), the book's own end-of-chapter question bank reproduced
  with official answers where the study text has one. No past-question
  linking yet — that's Phase 4, strictly after this phase is complete for
  **both** ATSWA III and Skills.

  Order among the 4 subjects is not fixed by this plan — pick based on which
  study text is cleanest to extract from, or go in the table order above.
  Record the actual order chosen, and why, in `PROGRESS.md` as it happens.

  Given only 4 subjects here (vs. Skills' 6), this project may finish Phase 3
  materially before Skills does — if so, **wait for Skills to also finish
  Phase 3 before starting Phase 4 on either project**, per the strict
  cross-project ordering rule stated above. Use the wait productively: the
  optional Phase 1 follow-ups (missing diets, study-text edition audit) are
  good uses of that time, or start Phase 2 scaffolding work on the pipeline
  side (adapting `tools/*.py`) that doesn't require content to exist yet —
  but *not* running the pipeline against partial content.

### Phase 4 — Past-question pipeline (only after Phase 3 is fully done for BOTH projects)
- [ ] Adapt and run `extract_papers.py` on `materials/past-questions/`
- [ ] Seed `CHAPTER_KEYS` in `corrections.py` per subject **before** running
      `aim.py`, not after
- [ ] Adapt and run `aim.py` (chapter-level tagging)
- [ ] Adapt and run `aim_sec.py <ALL 4 CODES>` (section-level tagging)
- [ ] Adapt and run `build_exams.py`
- [ ] Spot-check a real, stratified sample per subject before trusting the
      output (Part B.3 — pipeline bugs hide as "bad citations")
- [ ] `final_revision.py` once tagging is trustworthy, plus its UI
      (`src/revision.js`) — don't let the script-without-UI gap `ATSWA II`
      hit happen here

### Phase 5 — Audit & polish
- [ ] `audit_answers.py` pass per subject
- [ ] `audit_abbrevs.py` pass per subject, filtered to exam-tested acronyms
- [ ] Any `guides/*.html` that earn their place (Part B.6)
- [ ] Full regression suite green, full pipeline rebuilt clean, before
      calling this site "done"
- [ ] Retry the 5 missing diets (§A.2) one more time before final release —
      more time may mean a new Wayback snapshot exists, or ICAN may have
      fixed the dead `/documents/` path itself

### Phase 6 — Deploy
- [ ] Same zero-dependency static deploy as `ATSWA II` (its `README.md`
      deploy section is a direct template) — decide hosting when this phase
      is actually reached, not now.

---

## Part E — Open questions for the user

Not blocking Phase 2, but worth a decision before Phase 3 gets far into any
one subject:

- The 5 missing INSIGHT diets (§A.2) — accept the 15-diet corpus as-is, or is
  there another source worth checking (a personal archive, a past student's
  saved copies, ICAN's own office) before treating them as permanently
  unavailable?
- Confirm the 4 subject codes in §A.1 (`aud`/`ca`/`tax`/`man`) before Phase 2
  scaffolding locks them into directory names and code references.
- This project's Taxation study text is a 2026 edition while the other 3 are
  2025 — worth explicitly confirming there isn't a newer 2026 edition for
  Auditing/Cost Accounting/Management too before transcription starts on
  those three (a quick check against the live materials page).
