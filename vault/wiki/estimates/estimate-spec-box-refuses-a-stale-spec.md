---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-box]]"
purpose: Whether guppi box --check refuses a conserved Spec whose folder lacks carry.md or its branch, a run from main, a session that ratified a Case of its own, a page of the Spec changed by a later Case, and a page the Spec creates that now stands — and passes any other
method: uv run --project .guppi pytest .guppi/tests/test_box.py
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, git, harness]
core: true
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

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
