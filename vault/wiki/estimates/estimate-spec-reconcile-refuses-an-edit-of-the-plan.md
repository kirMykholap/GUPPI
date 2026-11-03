---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-reconcile]]"
purpose: An edit of the plan file or its store is refused, the one Write that creates the plan with its title line excepted, and so is an edit of a file of a built Case under cases/ by any agent but case-guppi, and any edit of case-guppi outside cases/; an edit of case-guppi under cases/ is written by the hook itself and the call stopped
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k guard; by hand at the Work readings of the session that changes the guard, one probe Write of the main agent under cases/, refused and in the event log
checked: 2026-10-28
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
An agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run --project .guppi guppi ratified --guard` on `PreToolUse` reads the path, the content, the agent type and the `agent_id` of the call from the hook input.

Then:
The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
**＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
**＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way, and so is one of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, when the hook input does not name `case-guppi` as the agent type; the reason names the file and says that `case-guppi` alone writes it.
**＋** An `Edit`, `Write` or `MultiEdit` whose hook input names `case-guppi` on a file outside such a `cases/` folder is refused the same way.
**＋** A call whose hook input names `case-guppi` on a file under such a folder, which `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` neither refuses nor lets run on an error of the guard, is written by the hook itself: the content of a `Write`, or each `old_string` of an `Edit` or a `MultiEdit` replaced by its `new_string`, in order, once, or at each match with `replace_all`.
**＋** After that write the hook exits 2 with one line on stderr that names the file, says that the hook wrote it and tells the agent not to make the call again, so the call does not run.
**＋** A file under that folder is judged by `is_case_file` of `.guppi/guppi/casecheck.py`, which the check of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by `is_plan_file` of `.guppi/guppi/ledger.py`, which `plan_path` uses too.
**＋** A refusal writes one line `ratified refused` to the day's event log, the write of the hook one line `ratified wrote`, and neither writes a `tool` line, so `plan_path` of `.guppi/guppi/ledger.py` still names the plan file.
**－** An `Edit` or `MultiEdit` of `case-guppi` whose old string is missing from the file, is found more than once without `replace_all`, or names a file that does not exist leaves the file as it stands: exit 2 with that reason, and nothing of a `MultiEdit` is written.
**－** An error of the hook while it writes the file of `case-guppi` lets the call run: exit 0 with one line on stderr.
**－** An edit of a file outside `.claude/plans/` and outside such a `cases/` folder by any agent but `case-guppi` is not judged by this hook.
**－** A payload the hook cannot read: exit 0 with one line on stderr.
**－** No `PostToolUse` hook compares an edit of the plan.

## Result

2026-10-28, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
