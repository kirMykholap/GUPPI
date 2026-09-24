---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from entering the Spec in other words than the ones the person signed
status: built
enforcement: hook
implementation_ref: [guppi/ratified.py, tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-write-copies-the-ratified-case]]"]
deferred_by: ["[[decision-case-412]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.2
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session]
---

## Purpose

Prevents a ratified Case from entering the Spec in other words than the ones the person signed. Until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two. Now `given`, `when`, `then` and `tasks` are English in the chat, and a hook copies them.

## How it works

`uv run guppi ratified` on `Stop`. After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, it reads the session's transcript, finds the last earlier reply that shows `## Case N —` whole, and writes that Case into the plan file named by `gate.plan_path` and into the ratified copy `<plan>.ratified.md` beside it, outside the repository: the heading, `context`, `problem`, `given`, `when` and `then` as they stand, a block tagged `then` built from the sub-points of `tasks`, and a block tagged `tasks` of the task lines without their sub-points; the section of Case N is replaced when it stands, appended otherwise. A last showing that is a `DIFF` block writes nothing. No plan file, no showing, or a sub-point it cannot read — a value holding a backtick whose outer span is not padded by one space on each side among them (case 402): exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0. A defer-only Case is the agent's, under `## Deferred`.

## History

- 2026-09-24 created · [[decision-case-387.2]]
- 2026-09-24 estimate estimate-spec-write-copies-the-ratified-case added · [[decision-case-387.2]]
- 2026-09-24 deferred · [[decision-case-394]]
- 2026-09-24 status: draft → built · cascade
- 2026-09-25 defer by decision-case-394 superseded · [[decision-case-402]]
- 2026-09-25 updated: a value holding a backtick is refused unless its outer span is padded by one space on each side (case 402, supersedes 394) · [[decision-case-402]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 status: draft → built · cascade
