---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-box]]"
purpose: Whether guppi box --check refuses a conserved Spec whose folder lacks carry.md or its branch, a run from main, a session that ratified a Case of its own, a page of the Spec changed by a later Case, and a page the Spec creates that now stands — and passes any other
method: uv run --project .guppi pytest .guppi/tests/test_box.py
checked: 2026-10-13
origin: raw/2026-10-02/1202/ledger.md#case-593.3
sprint: migration
created: 2026-10-02
tags: [session, workflow, git, harness]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi box --check <folder> --session <id>`, where `<folder>` is a folder `vault/raw/<date>/<HHMM>/` and `<id>` is the session id of a `hi` line.

Then:
It prints one line for each reason the Spec cannot run now, and exits 1 when it prints any; with no reason it prints nothing and exits 0.
**＋** A folder that `is_carried_over` of `.guppi/guppi/materialize.py` does not judge marked is one reason, and so is a folder for which no branch `spec/<date>-<HHMM>` exists.
**＋** A current branch `main` is one reason: the shared branch is never `main`.
**＋** A decision line other than a `defer` in the ledger of the session's folder is one reason, naming its Case.
**＋** A live page named by an `update`, `delete` or `defer` item of the folder's `spec.md` is one reason when a line of its History names the Decision page of a later Case, read by `.guppi/guppi/caseid.py`: a plain id whose whole part is higher than that of every Case of that Spec with a plain id, when the Spec holds one; an id of a sprint whose number is higher than that of every Case of that Spec of the same sprint; or an id of a sprint of which the Spec holds no Case, on a History line dated on or after the date of the folder. The line names the page and that Decision page.
**＋** A slug that a `create` item of that Spec names and a live page carries is one reason, naming the slug.
**－** The check writes nothing, switches no branch, and opens no page beyond those the Spec names.

## Result

2026-10-13, uv run pytest tests/test_box.py: 14 passed — a later Case of the same sprint, a Case of another sprint dated on or after the folder, a plain id after a Spec of plain ids; a plain id beside a Spec with no plain id is not counted

## History

- 2026-10-02 created · [[decision-case-593.3]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1834/ledger.md#L38
- 2026-10-13 updated: the Criterion replaced whole — a later Case is judged by the sprint and the number of its id, or by the date of its History line for another sprint (case 788.5) · [[decision-case-788.5]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L51
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
