---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-box]]"
purpose: Whether guppi box --check refuses a conserved Spec whose folder lacks carry.md or its branch, a run from main, a session that ratified a Case of its own, a page of the Spec changed by a later Case, and a page the Spec creates that now stands — and passes any other
method: uv run pytest tests/test_box.py
origin: raw/2026-10-02/1202/ledger.md#case-593.3
sprint: migration
created: 2026-10-02
tags: [session, workflow, git, harness]
---

## Criterion

When:
Someone runs `uv run guppi box --check <folder> --session <id>`, where `<folder>` is a folder `vault/raw/<date>/<HHMM>/` and `<id>` is the session id of a `hi` line.

Then:
It prints one line for each reason the Spec cannot run now, and exits 1 when it prints any; with no reason it prints nothing and exits 0.
**＋** A folder that `is_carried_over` of `guppi/materialize.py` does not judge marked is one reason, and so is a folder for which no branch `spec/<date>-<HHMM>` exists.
**＋** A current branch `main` is one reason: the shared branch is never `main`.
**＋** A decision line other than a `defer` in the ledger of the session's folder is one reason, naming its Case.
**＋** A live page named by an `update`, `delete` or `defer` item of the folder's `spec.md` is one reason when a line of its History names the Decision page of a Case whose number, in its whole part, is higher than that of every Case of that Spec; the line names the page and that Decision page.
**＋** A slug that a `create` item of that Spec names and a live page carries is one reason, naming the slug.
**－** The check writes nothing, switches no branch, and opens no page beyond those the Spec names.

## History

- 2026-10-02 created · [[decision-case-593.3]]
