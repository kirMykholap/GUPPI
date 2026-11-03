---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
purpose: Whether Retro reads work.md and writes a red or a refusal on a page or file that a line of its Expected red names as a line of Observations of handoff.md, not as debt, while a red on a page or file no line names is debt unless the Baseline holds it, a session with no work.md leaves it to the agent's judgment, and a red test is never an expected red
method: one reading by hand at a /retro in a session whose work.md names a check under Expected red, recorded in the estimate line
checked: 2026-10-03
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose Spec updates a page or a governed file, and in Work Mode `uv run --project .guppi guppi check`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

Then:
The agent reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read.
**＋** A red or a refusal of a check on a page or file that a line of `## Expected red` of `work.md` names with that check is a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md` that names the check and the page or file it waits for.
**－** The red is not debt: the agent does not fix it or revert it into a patch.
**＋** The reading of the check that counts is the `uv run --project .guppi guppi check` of the librarian's run, after the page is written and the file rendered.
**＋** A red or a refusal on a page or file that no line of `## Expected red` names is debt, even when another line names the same check, unless `## Baseline` of `work.md` holds its line.
**－** In a session with no `work.md`, a red or a refusal of such a check is a line of `## Observations` by the agent's judgment.
**－** A red test is never an expected red, even when `## Expected red` names it: it is fixed or reverted into a patch by the rule for red tests.

## Result

2026-10-03, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
