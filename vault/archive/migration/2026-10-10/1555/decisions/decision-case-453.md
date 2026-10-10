---
type: decision
case: "453"
status: archived
update: ["[[rule-spec-reconcile]]", "[[estimate-spec-reconcile-refuses-an-edit-of-the-plan]]"]
origin: raw/2026-09-27/1255/ledger.md#case-453
sprint: migration
created: 2026-09-27
tags: [hooks, harness, workflow, session]
---

## Context

Case 452.1 has the `SubagentStop` hook `guppi casecheck --subagent` write each passed answer of `case-guppi` into a file under `raw/<date>/<hi HHMM>/cases/`. The main agent sends that file to the person. No hook stops the main agent from writing or editing that file with `Edit`, `Write` or `MultiEdit`. So the person could read a text that differs from the stored answer, sign it, and then get the stored answer in the Spec. The context of Case 452 named this as not done.
`guppi ratified --guard` of `rule-spec-reconcile` already runs on `PreToolUse` of those tools. It refuses the agent's edit of the plan file and of the store `<plan>.checked.json`, which only hooks write. The person decided that the same guard refuses every edit of any file under the `cases/` folder of a session folder. The guard judges the path by one function of `guppi/casecheck.py`, which the writer of Case 452.1 also uses, as `rule-one-judgment-one-implementation` requires. So this Case is built after 452.1. `.claude/settings.json` and `rule-hook-registry` do not change, because the hook is already registered on these tools. The governed-files hook was not chosen: it matches only the fixed paths that `governs` names.
This Case creates no page, so no vault query was run. In the frame, the line of `estimate-spec-reconcile-refuses-an-edit-of-the-plan` that leaves every file outside `.claude/plans/` unjudged becomes false, so its Criterion is replaced whole. `estimate-case-check-sends-back-a-faulty-case` speaks of the writer of the file, not of an edit by the agent, so it stays. `estimate-governed-files-hook-refuses` speaks of governed paths, so it stays. The sentence of `vault/wiki/case-schema.md` on the hook that refuses an edit of the plan stays true.
Not done: a write through a shell still passes. `guppi bashguard` refuses only a heredoc that writes into a file, so an `echo` redirect in Bash or a `Set-Content` in PowerShell into `cases/` is not refused.

## Problem

The main agent can write or edit the file of a built Case that the person reads and signs. Then the text the person ratified can differ from the stored answer that the Spec hook writes. Which guard refuses that edit, and on which paths?

## Given

`rule-spec-reconcile` — the rule of the guard, its Purpose and `How it works`
**＋** `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — the promise of the guard, whose Criterion this Case replaces whole
**＋** `guppi/ratified.py` — `guard_refusal` and `guard`, the `PreToolUse` hook
**＋** `guppi/casecheck.py` — the one predicate on a path under a `cases/` folder, next to the writer of the file
**＋** `guppi/ledger.py` — the one judgment of a plan file, and `plan_path`
**＋** `tests/test_ratified.py` — the tests of the guard
**＋** `rule-case-check` — its `SubagentStop` hook, which writes the file of a built Case
**＋** `.claude/plans/` — the folder of the plan file and its store
**＋** `vault/raw/<date>/<HHMM>/cases/` — the folder of the files of built Cases

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-453
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
