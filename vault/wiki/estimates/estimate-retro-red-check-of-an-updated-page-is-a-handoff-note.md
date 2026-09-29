---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether Retro reads work.md and writes a red or a refusal on a page or file that a line of its Expected red names as a line of Observations of handoff.md, not as debt, while a red on a page or file no line names is debt unless the Baseline holds it, a session with no work.md leaves it to the agent's judgment, and a red test is never an expected red
method: one reading by hand at the first /retro after the render in a session whose work.md names a check under Expected red, recorded in the estimate line
origin: raw/2026-09-28/0000/ledger.md#case-473.1
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

Then:
The agent reads `raw/<date>/<hi HHMM>/work.md` if it stands.
**＋** A red or a refusal of a check on a page or file that a line of `## Expected red` of `work.md` names with that check is a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md` that names the check and the page or file it waits for.
**－** The red is not debt: the agent does not fix it or revert it into a patch.
**＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
**＋** A red or a refusal on a page or file that no line of `## Expected red` names is debt, even when another line names the same check, unless `## Baseline` of `work.md` holds its line.
**－** In a session with no `work.md`, a red or a refusal of such a check is a line of `## Observations` by the agent's judgment.
**－** A red test is never an expected red, even when `## Expected red` names it: it is fixed or reverted into a patch by the rule for red tests.

## History

- 2026-09-28 created · [[decision-case-473.1]]
- 2026-09-28 updated: the Criterion replaced whole — the red is expected when a line of Expected red of work.md names its check and its page or file, not by the agent's judgment; with no work.md the judgment stands (case 479.3) · [[decision-case-479.3]]
- 2026-09-30 updated: the Criterion replaced whole — the trigger covers the agent's call; an expected red is a line of Observations of handoff.md, not an item of the frontier; the one-read rule of the frontier goes with the frontier (case 531.3) · [[decision-case-531.3]]
