---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-reconcile]]"
purpose: An edit of the plan file or its store by the agent is refused, the one Write that creates the plan with its title line excepted
method: uv run pytest tests/test_ratified.py -k guard; by hand, the first refused edit of the plan in a session after the change
checked: 2026-09-24
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow]
---

## Criterion

When:
The agent calls `Edit`, `Write` or `MultiEdit` on a file under `.claude/plans/`, and `uv run guppi ratified --guard` on `PreToolUse` reads the path and the content of the call.

Then:
The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
**＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
**＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way.
**＋** A refusal writes one line of the refusal to the day's event log and no `tool` line, so `plan_path` of `guppi/ledger.py` still names the plan file.
**＋** A plan file is a `.md` file under `.claude/plans/`, judged by one function of `guppi/ledger.py` that `plan_path` uses too.
**－** An edit of a file outside `.claude/plans/` is not judged by this hook.
**－** A payload the hook cannot read: exit 0 with one line on stderr.
**－** No `PostToolUse` hook compares an edit of the plan: `uv run guppi ratified --edit` and the marks `<plan>.waiting.json` are gone.

## Result

2026-09-24, uv run pytest tests/test_ratified.py -k reconcile: 5 passed; live in session 1303: ten edits of the plan file touching only a name or a context (four contexts, six headings) drew no message and no mark; eight edits touching compared parts drew additionalContext naming each Case and part — 391.2 then block and tasks, 392.1 given, then and tasks, 392.2 then block and tasks, 393 then; the next reply showed each marked Case whole, the Stop passed with no refusal and the marks file was gone after it; the exit 2 branch (a marked Case not shown) did not occur and was not read live

## History

- 2026-09-24 created · [[decision-case-387.3]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L21
- 2026-09-27 renamed from `estimate-spec-reconcile-shows-a-changed-case` · [[decision-case-445.1]]
- 2026-09-27 updated: the Criterion replaced whole — the guard refuses the edit instead of comparing it with the ratified copy (case 445.1) · [[decision-case-445.1]]
