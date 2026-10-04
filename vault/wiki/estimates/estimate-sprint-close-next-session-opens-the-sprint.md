---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: Whether after the close of a sprint the brief puts the opening of the next sprint first, /hi takes no item of sprint.md, the ledger hook refuses every decision line but a defer until a create of a sprint page stands, and the pages written from the ledger of the session that opens it carry its id
method: "pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the librarian's run of the session after the close of a sprint: the brief before it, its frontier.md, the refusals of guppi ledger in its transcript, its ledger and the sprint field of the pages written from that ledger"
origin: raw/2026-10-04/1439/ledger.md#case-628.3
sprint: migration
created: 2026-10-04
tags: [sprint, workflow, ledger]
---

## Criterion

When:
The librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page, and the next session opens with `/hi`; someone reads `vault/wiki/brief.md`, that session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the refusals of `uv run guppi ledger` in its transcript, its ledger, and the pages of its librarian's run.
**＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

Then:
The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
**＋** `/hi` writes that line first under `## Cases` of `frontier.md`, and takes no item of `vault/wiki/sprint.md`.
**＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
**＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
**－** An `estimate` or `lesson` line is not refused for this reason.
**－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

## History

- 2026-10-04 created · [[decision-case-628.3]]
- 2026-10-04 updated: the Criterion replaced whole — the new sprint id goes to the pages written from the ledger that creates the sprint page, as materialize sets it (case 632.5) · [[decision-case-632.5]]
