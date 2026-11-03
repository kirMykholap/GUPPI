---
type: estimate
kind: QA
status: passed
target: "[[rule-cleanup]]"
purpose: guppi cleanup moves an archived page into the archive of the session of the run and a restored one back, and unlinks its slug from the live lists without rebuilding a section
method: pytest .guppi/tests/test_cleanup.py, plus by hand on the cleanup of a later librarian's run
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi cleanup` runs over the live pages of `vault/wiki/` and the pages under the archive.

Then:
A live page with `status: archived` moves under the same file name to `vault/archive/<sprint>/<date>/<HHMM>/<category>/`. The date is the day of the run, and the session is the latest session folder of `vault/raw/<date>/`, else the latest of the nearest date back. With no session folder at all, the page goes into the category folder under the date, with no session level.
**＋** The moved page gets the History line "- <date> archived · cleanup", and a page moved back gets "- <date> restored · cleanup". Each History line that cleanup writes also goes to `log.md` with the page's category and slug in front, such as "- <date> <category>/<slug> archived · cleanup".
**＋** Its slug leaves the `children` of live pages and the `estimates` of entities and rules, the field only, and that page gets the History line "- <date> child <slug> archived · cleanup" or "- <date> estimate <slug> archived · cleanup". No section is rebuilt, and an Insight's `children` keep the slug.
**＋** Wikilinks in page bodies stay, and a page with any other status stays.
**＋** A page under the archive, at any depth, whose status is no longer `archived` moves back to its category folder under `vault/wiki/`.
**＋** A live page whose `parent` or `target` is archived is reported on stderr and left.
**＋** A rerun moves nothing and exits 0. A file that cannot move, or a name already taken in the archive, is a line on stderr and exit 1, and the other pages still move.
**＋** Live, a run with nothing to move exits 0 and leaves `git diff` empty.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
