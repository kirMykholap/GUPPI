---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-reconcile]]"
purpose: An edit of the plan file or its store is refused, the one Write that creates the plan with its title line excepted, and so is an edit of a file of a built Case under cases/ by any agent but case-guppi, and any edit of case-guppi outside cases/
method: uv run pytest tests/test_ratified.py -k guard; by hand in a later session, one probe Write of the main agent under cases/, refused and in the event log, and one file under cases/ written by case-guppi
checked: 2026-10-05
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow]
---

## Criterion

When:
An agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the content and the agent type of the call from the hook input.

Then:
The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
**＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
**＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way.
**＋** An `Edit`, `Write` or `MultiEdit` of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, is refused the same way when the hook input does not name `case-guppi` as the agent type; the reason names the file and says that `case-guppi` alone writes it.
**＋** An `Edit`, `Write` or `MultiEdit` whose hook input names `case-guppi` on a file outside such a `cases/` folder is refused the same way.
**＋** A file under that folder is judged by `is_case_file` of `guppi/casecheck.py`, which the check of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by `is_plan_file` of `guppi/ledger.py`, which `plan_path` uses too.
**＋** A refusal writes one line of the refusal to the day's event log and no `tool` line, so `plan_path` of `guppi/ledger.py` still names the plan file.
**－** A call whose hook input names `case-guppi` on a file under such a `cases/` folder is let through unless `<plan>.checked.json` holds the number of the file from another agent, as `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` sets it.
**－** An edit of a file outside `.claude/plans/` and outside such a `cases/` folder by any agent but `case-guppi` is not judged by this hook.
**－** A payload the hook cannot read: exit 0 with one line on stderr.
**－** No `PostToolUse` hook compares an edit of the plan.

## Result

2026-10-05, the Work readings of session 1616: uv run pytest -q tests/test_ratified.py -k guard 39 passed, 78 deselected; by hand: a probe Write of the main agent of vault/raw/2026-10-05/1616/cases/probe.md was refused by uv run guppi ratified --guard with the reason naming the file, case-guppi and rule-spec-reconcile, the file not written, and the event log holds "18:13:48 6360af9f ratified refused Write ...\1616\cases\probe.md" and no tool line for it; case-guppi wrote case-660.md, case-661.md, case-662.md, case-663.md, case-664.md and case-668.md under cases/ by Write and Edit with no refusal

## History

- 2026-09-24 created · [[decision-case-387.3]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L21
- 2026-09-27 renamed from `estimate-spec-reconcile-shows-a-changed-case` · [[decision-case-445.1]]
- 2026-09-27 updated: the Criterion replaced whole — the guard refuses the edit instead of comparing it with the ratified copy (case 445.1) · [[decision-case-445.1]]
- 2026-09-27 updated: the Criterion replaced whole — a file under the cases/ folder of a session folder refused like the store (case 453) · [[decision-case-453]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L28
- 2026-10-05 updated: the Criterion replaced whole — case-guppi alone writes under cases/ and is refused anywhere else; the purpose and the method follow (case 645.3) · [[decision-case-645.3]]
- 2026-10-05 updated: the Criterion replaced whole — a call of case-guppi under cases/ passes unless another agent holds the number of the file, the promise of estimate-spec-reconcile-refuses-a-case-file-another-agent-holds (case 650.2) · [[decision-case-650.2]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L40
