---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether after the close of a sprint the brief puts the opening of the next sprint first, /hi takes no item of sprint.md, the ledger hook refuses every decision line but a defer until a create of a sprint page stands, and the pages written from the ledger of the session that opens it carry its id
method: pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the Retro of the session of case 779, .claude/skills/hi/SKILL.md, .claude/skills/sprint-open/SKILL.md and the step of the Render of rule-brief that writes the first line of the brief's Cases read against the Criterion
checked: 2026-10-12
origin: raw/2026-10-04/1439/ledger.md#case-628.3
sprint: migration
created: 2026-10-04
tags: [sprint, workflow, ledger]
---

## Criterion

When:
Someone reads `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and the step of the Render of `rule-brief` that writes the `Cases` of Next session in `vault/wiki/brief.md`, for the session that opens after the librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page.
**＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

Then:
The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
**＋** `/hi` starts `/sprint-open` and writes no `frontier.md` before the opening Case is ratified; then `frontier.md` holds that line first under `## Cases`, closed `[x] … · case N` by the opening Case, and no item of `vault/wiki/sprint.md`, as `estimate-hi-writes-frontier` sets it.
**＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
**＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
**－** An `estimate` or `lesson` line is not refused for this reason.
**－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

## Result

2026-10-12, Retro of session 1449, uv run pytest tests/test_ledger.py tests/test_materialize.py -k sprint: 6 passed (4 of test_ledger on the refusal of decision lines but a defer, a reading or a lesson until a create of an entity-sprint page in the reply or the ledger, 2 of test_materialize on the sprint id of a unit); by hand: .claude/agents/librarian-guppi.md writes the first Cases line `open the next sprint — no sprint is open since the close of <id>`, .claude/skills/hi/SKILL.md starts /sprint-open first and writes the Frontier before the reply that acknowledges the opening Case, that line first and closed by it, no item of sprint.md while it stands, .claude/skills/sprint-open/SKILL.md says the ledger hook refuses each decision line but a defer until the create of entity-sprint-<id>

## History

- 2026-10-04 created · [[decision-case-628.3]]
- 2026-10-04 updated: the Criterion replaced whole — the new sprint id goes to the pages written from the ledger that creates the sprint page, as materialize sets it (case 632.5) · [[decision-case-632.5]]
- 2026-10-10 updated: the Criterion replaced whole — the opening line reaches frontier.md after the opening Case, closed by it; the method runs in the session of case 769 · [[decision-case-769.5]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L38
- 2026-10-12 updated: the Criterion replaced whole — the When names what the check reads, with no reading of a later session; the method runs in the session of case 779 · [[decision-case-779]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1449/ledger.md#L9
