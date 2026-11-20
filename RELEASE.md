# ATSWA III — local build and manual deployment

**Development stays local. The user deploys through Vercel.**
Do not publish or synchronize this project to a hosting service unless the
user explicitly asks for that action.

Local site: http://localhost:4000/

The existing Python server serves ATSWA III/website directly. HTTP checks
confirmed the home page, chapter data, exams, revision and Tax guide return
200 and exactly match the current local files. Leave the server running.

The completed build contains 62 chapters, 60 papers from 15 diets and all
3,360 questions with chapter, section and original PDF-page links. UI,
practice, timed exams, revision and the Tax transition guide are local files.
The full PDF rebuild and integrity audit pass, with 7 Python tests, 29 jsdom
UI tests, 38 real Chrome checks and additional guide/table/reading checks.

For manual deployment, website/ contains the complete static site: index.html,
data/, assets/ and guides/. No application server or runtime packages are
needed on the host. The optional dist/ can be rebuilt from ATSWA III with
`python3 website/tools/package_site.py`; its release.json records inventory
and runtime file hashes. The user chooses when to deploy to Vercel.

The earlier assistant-created Sites deployment was not the requested workflow.
Its recovery records were moved out of the active project configuration to
website/.cache/unrequested-sites-publication/. The extra hosted copy remains
owner-private; it has not been removed. The source snapshot/archive under
../.sites/ are retained as recovery artifacts, not as an active deploy target.

Five older target diets remain externally unavailable after retries; evidence
is in website/data/source-availability.json and ../DOWNLOADS_LOG.md.


## Local release refreshed — 2026-11-20

The source-fidelity audit restored missing letters, forms, reports, figures,
modern-costing discussions, product details and worked review answers. Current
inventory: 62 chapters, 60 papers, all 3,360 linked questions, 1,434 reviewed
citations and 386 labelled flags. An additional 37 original study-text pages
preserve 42 figure/table captions.

The source-to-site pipeline and integrity audit pass, with 13 Python source
tests, 30 jsdom tests, 38 Chrome checks, 124 chapter-layout checks and extra
guide/source-restoration checks. Runtime dist/ contains current inventory and
file hashes. The site remains at localhost:4000; the user handles Vercel.
No hosting or Git publication occurred. Skills is on hold under the latest
instruction. Review method and limits are recorded in PROGRESS.md and
website/data/source-fidelity-review.json.
