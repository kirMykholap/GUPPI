---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again
status: draft
enforcement: hook
implementation_ref: [guppi/ratified.py, guppi/ledger.py, tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-reconcile-refuses-an-edit-of-the-plan]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session]
---

## Purpose

Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again. Since case 441 the hooks alone write the Cases into the plan: the `Stop` hook of `rule-spec-write` writes the stored answer of `case-guppi`, and a Case changes only through its `case-guppi` and a new ratification. The agent writes only the title line that creates the plan, and a hook refuses any other edit of it before it lands; the comparison with a ratified copy that stood here from case 387.3 is gone (case 445.1).

## How it works

`uv run guppi ratified --guard` on `PreToolUse` of `Edit`, `Write` and `MultiEdit`. A plan file is a `.md` file under `.claude/plans/`, judged by one function of `guppi/ledger.py` that `plan_path` also uses; the store `<plan>.checked.json` of `rule-case-check` lies beside it. The hook refuses every `Edit` and `MultiEdit` of a plan file or a store, every `Write` of a store, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run. The one exception is a `Write` of a plan file that does not exist whose content, trimmed, is one line that opens with `# ` — the title line the agent writes before the first dispatch of `case-guppi`; the hooks find the plan by that write in the event log, so no hook can create it. A refusal writes one line to the day's event log; a refused call has no `PostToolUse`, so it leaves no `tool` line and does not move `plan_path`. The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and this hook does not judge them. A payload the hook cannot read: exit 0 with one line on stderr; it never raises. Until case 445.1 the rule was a comparison: `guppi ratified --edit` on `PostToolUse` compared an edited plan with a ratified copy `<plan>.ratified.md` and marked a changed Case in `<plan>.waiting.json` for its showing; the copy, the marks and that hook are gone.

## History

- 2026-09-24 created · [[decision-case-387.3]]
- 2026-09-24 estimate estimate-spec-reconcile-shows-a-changed-case added · [[decision-case-387.3]]
- 2026-09-24 status: draft → built · cascade
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 defer by decision-case-412 superseded · [[decision-case-414.1]]
- 2026-09-25 deferred · [[decision-case-416]]
- 2026-09-25 defer by decision-case-416 superseded · [[decision-case-419.2]]
- 2026-09-25 deferred · [[decision-case-423]]
- 2026-09-27 defer by decision-case-423 superseded · [[decision-case-445.1]]
- 2026-09-27 updated: the guard refuses the agent's edits of the plan and its store, the title line that creates the plan excepted; the comparison with the ratified copy goes (case 445.1) · [[decision-case-445.1]]
- 2026-09-27 ref `estimate-spec-reconcile-shows-a-changed-case` → `estimate-spec-reconcile-refuses-an-edit-of-the-plan` · [[decision-case-445.1]]
- 2026-09-27 status: built → draft · cascade
