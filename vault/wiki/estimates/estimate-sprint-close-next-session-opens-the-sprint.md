---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether after the close of a sprint the brief puts the opening of the next sprint first, /hi takes no item of sprint.md, the ledger hook refuses every decision line but a defer until a create of a sprint page stands, and the pages written from the ledger of the session that opens it carry its id
method: "pytest .guppi/tests/test_ledger.py -k sprint and .guppi/tests/test_materialize.py -k sprint; by hand: the step of the Render of rule-brief that writes the first line of the brief's Cases, .claude/skills/hi/SKILL.md and .claude/skills/sprint-open/SKILL.md read against the Criterion"
checked: 2026-10-29
origin: raw/2026-10-04/1439/ledger.md#case-628.3
sprint: migration
created: 2026-10-04
tags: [sprint, workflow, ledger]
---

## Criterion

When:
Someone reads `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and the step of the Render of `rule-brief` that writes the `Cases` of Next session in `vault/wiki/brief.md`, for the session that opens after the librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page.
**＋** Or `.guppi/tests/test_ledger.py` and `.guppi/tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

Then:
The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
**＋** `/hi` starts `/sprint-open` and writes no `frontier.md` before the opening Case is ratified; then `frontier.md` holds that line first under `## Cases`, closed `[x] … · case N` by the opening Case, and no item of `vault/wiki/sprint.md`.
**＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
**＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
**－** An `estimate` or `lesson` line is not refused for this reason.
**－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

## Result

2026-10-29, Retro of session 0327: pytest test_ledger.py -k sprint 8 passed, test_materialize.py -k sprint 2 passed; .claude/agents/librarian-guppi.md line 116 writes first the line "open the next sprint — no sprint is open since the close of <id>"; .claude/skills/hi/SKILL.md line 29 starts /sprint-open first on that line; .claude/skills/sprint-open/SKILL.md step 1 assembles no Frontier before the opening Case; live in install A: frontier.md of raw/2026-10-29/1800 holds that line first, closed "· case kirmykholap-test-1", and no item of sprint.md, and the ledger opens with the create of entity-sprint-kirmykholap-test

## History

- 2026-10-04 created · [[decision-case-628.3]]
- 2026-10-04 updated: the Criterion replaced whole — the new sprint id goes to the pages written from the ledger that creates the sprint page, as materialize sets it (case 632.5) · [[decision-case-632.5]]
- 2026-10-10 updated: the Criterion replaced whole — the opening line reaches frontier.md after the opening Case, closed by it; the method runs in the session of case 769 · [[decision-case-769.5]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L38
- 2026-10-12 updated: the Criterion replaced whole — the When names what the check reads, with no reading of a later session; the method runs in the session of case 779 · [[decision-case-779]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1449/ledger.md#L9
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the pointer of the method stands in a bracket at its end · [[decision-case-823.1]]
- 2026-10-17 updated: the method reads the Renders where they live, with no past moment · [[decision-case-875]]
- 2026-10-29 updated: the Criterion replaced whole — it names no Estimate that the clean version does not hold · [[decision-case-901.1]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/0327/ledger.md#L37
