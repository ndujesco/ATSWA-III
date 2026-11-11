# ATSWA Part III — The Great Lock-in

A dependency-free study website for Cost Accounting, Principles of Auditing
& Assurance, Taxation and Management. The completed source corpus is the
15 INSIGHT diets from March 2019 through March 2026.

| Content | Verified inventory |
| --- | ---: |
| Authored chapters (CA / AUD / TAX / MAN) | 15 / 12 / 25 / 10 = 62 |
| Past papers | 60 |
| MCQ / short answers / Section B questions | 1,800 / 1,200 / 360 |
| Questions linked to both chapter and section | 3,360 / 3,360 |
| Questions linked to an original PDF page | 3,360 / 3,360 |
| Additional passages for multi-topic essays | 171 |
| Individually reviewed citation overrides | 1,386 |
| Question-level law/source flags | 384 |
| Reviewed MCQ / short-answer corrections | 7 / 7 |
| Original PDFs / recovered figure pages / tax-table appendices | 15 / 7 / 15 |
| Source questions retained in Final Revision | 3,360 |

The exact build inventory is in `data/audit-report.json`. The five older
target diets (September 2016, March/September 2017, March/September 2018)
remain unavailable after a fresh official-site and archive retry. Evidence
is in `data/source-availability.json`; no substitute questions were invented.
September 2026 is outside this project's agreed source scope.

## Use the site

The study desk offers chapter search, saved reading positions, responsive
contents, formulas, chapter practice, subject/year paper filters, Final
Revision and clickable progress. Every paper supports reading and practice;
timed mode keeps written answers and exposes the original reference tables
without exposing answers. Repeating a completed timed attempt starts a fresh
clock. Exact-question and exact-section links work across these views.

The standalone [Tax transition guide](guides/tax-transition.html) distinguishes
historical answers from the 2025 Acts, links primary sources, includes a
worked comparison, and indexes the flagged Taxation questions by year/topic.
Reader glossaries explain abbreviations in their actual chapter context.
Light/dark themes, keyboard search and layouts from 320px are supported.

Progress, quiz answers and written work stay in this browser under `atswa3:`;
they do not sync between devices. Part II records remain separate. Clearing
Part III progress requires two clicks, preserves the theme and prevents
legacy progress from being imported again.

## Local work and manual deployment

**User instruction: keep development local. The user deploys through Vercel.
Do not publish through Sites, Vercel, or another host unless explicitly asked.**

The updated site is running at <http://localhost:4000/> from this directory.
Keep that server running for the user. To start it if it has stopped:

```sh
python3 -m http.server 4000 --bind 127.0.0.1
```

Open <http://localhost:4000/>. Serve the whole directory: the page loads
`data/*.js`, original PDFs and recovered figures under `assets/` on demand.
No runtime package installation or application server is needed. Web fonts
have system-font fallbacks.

## Edit, rebuild and verify

`index.html` and `data/*.js` are generated. Edit `src/` and
`content/<subject>/chNN.py`; introductions are in `content/<subject>/meta.py`.
The chapter schema and fidelity rules are in `../PLAN.md`.

Rebuild the entire chain from the original PDFs:

```sh
python3 tools/rebuild.py --extract
```

Without source-PDF changes, `python3 tools/rebuild.py` reuses the extracted
bank. Both commands rebuild chapter content, chapter/section retrieval,
source figures, exams, revision and the HTML, then run the integrity audit,
7 Python source regressions and 29 jsdom UI regressions. Extraction and
figure recovery use Poppler's `pdftotext` and `pdftoppm`; Python 3 and Node
are build tools. The UI suite uses jsdom (`npm install --no-save jsdom`).
None is a deployed runtime dependency.

For a UI-only change, `sh build.sh` assembles the page and
`node tools/test.mjs` checks its behavior. Rebuild the full chain after any
content, citation, correction or law-flag change.

The final release passed the full rebuild, all 7 Python and 29 jsdom tests,
38 real Chrome checks across five viewport widths, and additional Chrome
checks for the guide, cross-topic reading links and timed reference tables.
Browser QA helpers/screenshots are local, ignored files under `.cache/`.

## Content integrity

```sh
python3 tools/audit_papers.py
python3 tools/audit_answers.py CA
python3 tools/audit_abbrevs.py CA
python3 tools/review_queue.py CA --sections --limit 30
```

The subject arguments also accept `AUD`, `TAX` and `MAN`. All four
exam-filtered abbreviation audits have zero unresolved candidates. Answer
audits produce literal-phrase candidates for semantic review; absence of an
exact phrase is not proof of a missing explanation. Review decisions and
limits are recorded in `data/answer-audit-review.json`.

The structural audit rejects missing chapter/section/PDF-page links, invalid
targets, count changes, source/revision omissions, broken reading links,
missing figures and changed original-PDF or primary-law hashes. Retrieval
confidence gates remain unchanged. Human decisions are in
`tools/citation_reviews.py`, `citation_review_batches.py` and
`citation_refinements.py`; multi-topic essay passages are in
`tools/essay_readings.py`. Do not fix coverage by weakening the gates.

All original printed keys, answers, workings and available examiner reports
remain visible. Reviewed study answers are explicitly labelled and drive
practice scoring without overwriting the source. Flags cite changed law,
standards or source defects; provenance and review limits are in
`data/law-sources.json`, `data/law-review.json`, `tools/law_flags.py` and
`tools/corrections.py`. This does not claim that every historic computation
has been independently recomputed or every legal question individually
adjudicated.

Known source exceptions remain deliberate: March 2020 Management's irregular
numbering/option labels, March 2024 Taxation MCQ25's four printed options,
two bonus keys and two dual-answer keys. Practice honors the official scoring
exceptions. Recoveries fix extraction loss of small numeric workings and
misread currency glyphs while preserving the original PDFs for comparison.

## Release

From this directory:

```sh
python3 tools/package_site.py
```

This creates only the generated `../dist/`, containing `index.html`, the six
runtime data files, assets, guides and `release.json` with inventory and file
hashes. It excludes tooling, notes, caches and development dependencies.
For the user's manual Vercel deployment, the existing website directory
contains the complete static site: index.html, data/, assets/ and guides/.
The optional dist/ contains just runtime files. Do not deploy on the user's
behalf. See ../RELEASE.md for the local build record and this preference.

See `../PROGRESS.md` for the dated work log and `../../HANDOVER.md` for the
current checkpoint. Skills remains a separate project on hold.
