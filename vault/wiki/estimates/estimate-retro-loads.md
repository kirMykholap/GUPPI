---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Context

A Retro that starts by reading files spends the context it exists to save; one that edits new scope hides a decision.

## Criterion

After a live /retro: the first turn's context holds the output of make test, make
style and today's ledger with no read-tool call; event_log.md carries a retro line;
the first message is the frontier in three blocks — ratified by Case, done and not
done against the Spec, noticed — with no read call; every item raised by either side
ends as a lesson line, an estimate line, a short defer with its Case under ## Deferred in
spec.md, or a handoff note; no decision line other than defer is written in Retro;
every Estimate whose work is finished has its reading line; a red test ends as a fix
that traces to today's ledger or as a patch in raw/ with a short defer, with a
lesson[error] either way; every edit made in Retro traces to a line of today's ledger;
the closing reply lists the ratifications, the done and the not done; the commit
precedes the /handoff call.

### case 73.6

When:
`/retro` writes a short defer.

Then:
It is appended under `## Deferred` of `raw/<hi date>/<hi HHMM>/spec.md`; the unticked
`tasks` Retro counts are that file's.

### case 109.1

When:
The person invokes `/retro`.

Then:
The Render: `Ledger of today: !`cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null``; the text "a line of today's ledger" becomes "a line of this session's ledger".
**＋** The revert patch goes to `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session folder.
**＋** `estimate-retro-loads` gets a `### case 109.1` block, `pending`.

### case 126

When:
The person invokes `/retro`.

Then:
The Render of `rule-retro`: the line `Ledger of today: !`cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`` → `Ledger: !`uv run guppi tail`` — the unmaterialized lines, this session's in its folder; the phrase "the ledger lines of today grouped by Case" → "the lines of the Tail above grouped by Case, this session's folder first".
**＋** `estimate-retro-loads` gets a `### case 126` block, `pending`; read at the first `/retro` after the render — the next session's, since the skill is rendered by the librarian after this session's Retro: the skill loaded, `Ledger:` carries the lines of the session's folder, no substitution failed.
**－** `{supersedes:case 118}`: `decision-case-118` is superseded, `rule-retro` loses `deferred_by`.

### case 169.3

When:
The person types `/retro`, or the agent calls the skill `retro`.

Then:
The typed `/retro` passes through `guppi gate` on `UserPromptSubmit`, the agent's call through `guppi gate` on `PreToolUse Skill`; both check the Spec against the ledger, both leave the mark `retro`; a refused typed prompt is not expanded.
**＋** The frontmatter of `SKILL.md` without `disable-model-invocation`: the agent calls `/retro` when the tasks of the Spec are ticked.
**－** Retro still stops at the lessons and the readings; `/handoff` behind the gate of the tree and of 122.

## Method

one reading by hand at the first /retro, recorded in the estimate line

## Result

block 169.3, live 2026-09-15 session S: /retro typed by the person at 20:31:22 and called by the agent through the Skill tool at 21:12:53; the event log carries two marks retro, both after the gate's check of the Spec against the ledger, all then items with their lines; neither prompt refused

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L86
- 2026-09-11 updated: the frontier, the four outcomes, the readings and the red-test paths added; pending until the next live /retro · [[decision-case-56]]
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L106
- 2026-09-12 criterion: case 73.6 added · [[decision-case-73.6]]
- 2026-09-13 criterion: case 109.1 added · [[decision-case-109.1]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/0747/ledger.md#L50
- 2026-09-14 criterion: case 126 added · [[decision-case-126]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/1029/ledger.md#L41
- 2026-09-14 status: failed → passed · raw/2026-09-14/1229/ledger.md#L30
- 2026-09-14 criterion: case 150 added · [[decision-case-150]]
- 2026-09-15 status: pending → failed · raw/2026-09-15/1110/ledger.md#L26
- 2026-09-15 criterion: case 169.3 added · [[decision-case-169.3]]
- 2026-09-15 criterion: case 150 removed · [[decision-case-169.3]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L14
