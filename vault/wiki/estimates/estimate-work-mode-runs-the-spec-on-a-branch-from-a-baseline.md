---
type: estimate
kind: QA
status: passed
target: "[[rule-work-mode]]"
purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks, names that folder under Conserved Spec and deletes its carry.md, and marks an expected red under Expected red
method: "uv run guppi render --check; by hand, a /work the agent calls at the fork, a /work the person types and a /work that /box calls: the branch, work.md, the ticks of the Spec, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line"
checked: 2026-10-04
origin: raw/2026-09-28/1318/ledger.md#case-479.2
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
**＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.

Then:
`uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
**＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
**＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
**＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
**＋** When `work.md` already stands, its `## Baseline` stays as it is.
**＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task.
**＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
**＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
**－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.

## Result

2026-10-04, at the /hi of session 0004: `uv run guppi render --check` exit 0; by hand, the /work the agent called at the fork in session 0317 (transcript 5b311f89) and the /work that /box called in session 1416 (transcript 682b0e2f): in each the skill came with "Run these 2 commands first" in place of the output of `make test` and `make lint`, and the agent ran both itself; 0317 on `migration`: work.md written at 04:58:07, before the first Edit at 04:59:08, with make test exit 0, make lint exit 2 and its 43 finding lines as printed, and an empty `## Expected red`; the code and test boxes ticked in the order of the Spec, lines 116–117 at 05:01:00 after the tests of 611 and lines 490–492 at 05:02:26 after those of 613.1; the task of 613.1, which adds the class `moment` to `make lint`, added one line under `## Expected red` at 05:02:37 naming the check and the pages it waits for; 1416 on `spec/2026-10-03-1341`: work.md written at 14:38:15 with make test exit 0, make lint exit 2 and its 47 finding lines, an empty `## Expected red` and `## Conserved Spec` naming vault/raw/2026-10-03/1341/; that Spec holds no task of code, and its carry.md was deleted at 14:38:26, before the Work readings; the commits of both runs, 783d24e5 and 37c47bd1, bda8f3f4 and a67b0339, touch no file of vault/wiki/, and no read, page, render, sprint or glossary box was ticked; not exercised: a /work the person types — the person's word at this /hi: no one types it —, the branch main, a resume over a work.md that already stands

## History

- 2026-09-28 created · [[decision-case-479.2]]
- 2026-10-02 updated: the Criterion replaced whole — /work runs the Spec of the folder /box gives it (case 591.7) · [[decision-case-591.7]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L6
