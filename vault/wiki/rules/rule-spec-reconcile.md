---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again
status: built
enforcement: hook
implementation_ref: [guppi/ratified.py, guppi/ledger.py, guppi/casecheck.py, tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-reconcile-refuses-an-edit-of-the-plan]]", "[[estimate-spec-reconcile-refuses-a-case-file-another-agent-holds]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session]
core: true
---

## Purpose

Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again. The hooks alone write the Cases into the plan (since case 441): the `Stop` hook of `rule-spec-write` writes the text of the file of `case-guppi` that `rule-case-check` stored, and a Case changes only through its `case-guppi` and a new ratification. The agent writes only the title line that creates the plan, and a hook refuses any other edit of it, and any edit of the file of a built Case that the person is sent, before it lands, unless `case-guppi` makes it and no other agent holds the number of that Case (cases 453, 645.3, 650.1); the comparison with a ratified copy that stood here is gone (from case 387.3 to case 445.1).

## How it works

`uv run guppi ratified --guard` on `PreToolUse` of `Edit`, `Write` and `MultiEdit`. A plan file is a `.md` file under `.claude/plans/`, judged by one function of `guppi/ledger.py` that `plan_path` also uses; the store `<plan>.checked.json` of `rule-case-check` lies beside it. The hook refuses every `Edit` and `MultiEdit` of a plan file or a store, every `Write` of a store, every `Write` of a plan file that exists, and every `Edit`, `Write` and `MultiEdit` of a file under the `cases/` folder of a session folder under `vault/raw/` whose hook input does not name `case-guppi` as the agent type — the file of a built Case that `case-guppi` writes and the `SubagentStop` hook of `rule-case-check` checks, judged by one function of `guppi/casecheck.py` that the check uses too (cases 453, 645.3) — and every `Edit`, `Write` and `MultiEdit` that names `case-guppi` on a file outside such a folder, or on the file `case-<N>.md` of a Case when the store holds Case N, or a sub-case of it, under its number alone from another `agent_id` (case 650.1): exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run. The exceptions are an `Edit`, `Write` or `MultiEdit` of `case-guppi` under `cases/` on a file `case-<N>.md` when the store holds neither Case N nor a sub-case of it under its number alone from another `agent_id` — when the store holds no entry under N, N the number of the file `case-<N>.md`, the call writes its `agent_id` there, so the number is held before the agent stops, and a refusal names a free number counted as the check of `rule-case-check` counts one, by the functions of `guppi/casecheck.py` the check runs (case 650.1) —, and a `Write` of a plan file that does not exist whose content, trimmed, is one line that opens with `# ` — the title line the agent writes before the first dispatch of `case-guppi`; the hooks find the plan by that write in the event log, so no hook can create it. A refusal writes one line to the day's event log; a refused call has no `PostToolUse`, so it leaves no `tool` line and does not move `plan_path`. The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and so does this hook for the entry that holds a number, and the old path of `rule-case-check` writes a file of `cases/` the same way until the writer is live; this hook does not judge them; a write through a shell is not judged here (case 453). A payload the hook cannot read: exit 0 with one line on stderr; it never raises (until case 445.1 the rule was a comparison: `guppi ratified --edit` on `PostToolUse` compared an edited plan with a ratified copy `<plan>.ratified.md` and marked a changed Case in `<plan>.waiting.json` for its showing; the copy, the marks and that hook are gone).

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
- 2026-09-27 updated: the guard also refuses the agent's edit of a file under the cases/ folder of a session folder, judged by one function of guppi/casecheck.py (case 453) · [[decision-case-453]]
- 2026-09-27 status: draft → built · cascade
- 2026-10-05 updated: the guard lets case-guppi alone write under cases/, and refuses case-guppi anywhere else (case 645.3) · [[decision-case-645.3]]
- 2026-10-05 status: built → draft · cascade
- 2026-10-05 estimate estimate-spec-reconcile-refuses-a-case-file-another-agent-holds added · [[decision-case-650.1]]
- 2026-10-05 updated: the first write of case-guppi on the file of a Case holds its number in the store, and a write of another case-guppi on that file is refused with a free number (case 650.1) · [[decision-case-650.1]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the history of the guard stands in the brackets of its pointers · [[decision-case-809]]
