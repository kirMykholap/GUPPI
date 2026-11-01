---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-approve-spec]]"
purpose: Whether /approve-spec, typed by the person out of Plan Mode after /pre-spec, appends the plan file of the session to its spec.md and gives the agent the line of an approval, and is blocked in Plan Mode, before /pre-spec, while the check of the plan finds a finding, or with no plan file
method: "uv run --project .guppi pytest .guppi/tests/test_spec.py -k typed; by hand, after the librarian's run that applies the create of rule-skill-approve-spec and renders .claude/settings.json and .claude/skills/approve-spec/SKILL.md: in a standalone terminal window, the Claude Code CLI on a copy of the repository, a working session whose plan the CLI withholds and whose check of /pre-spec passes, /approve-spec typed once in Plan Mode and once after Esc and Shift+Tab, then the transcript of that session under ~/.claude/projects/ and its spec.md read against the Criterion"
origin: raw/2026-11-01/1721/ledger.md#case-987.1
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, plugin]
---

## Criterion

When:
In a working session the person types `/approve-spec`, and `uv run --project .guppi guppi spec --typed` of `.guppi/guppi/spec.py` runs on `UserPromptSubmit`.

Then:
Out of Plan Mode, after `/pre-spec`, with a plan file of the session that the check of the plan passes, the hook appends that plan file to `raw/<hi date>/<hi HHMM>/spec.md` under its stamp, once, as `rule-spec-capture` sets it for an approval by `ExitPlanMode`.
**＋** The hook then gives the agent the line it gives after `ExitPlanMode`: the fork between `/work` and `/carry`, or the call of `/box` for a plan that names a conserved Spec.
**＋** The skill `.claude/skills/approve-spec/SKILL.md` tells the agent to follow that line.
**－** While the session is in Plan Mode, the hook blocks the prompt and tells the person to leave Plan Mode with Shift+Tab and type `/approve-spec` again.
**－** Before `/pre-spec`, or while the check of the plan finds a finding, the hook blocks the prompt with the reason that `gate` of `.guppi/guppi/prespec.py` judges at `ExitPlanMode`, by the same function.
**－** With no plan file of the session, or with no `/hi` of the session, the hook blocks the prompt and says why.
**－** A blocked prompt leaves `spec.md` as it stands.
**－** The agent cannot start `/approve-spec` itself.
**－** Any other prompt passes the hook, and nothing is written.

## History

- 2026-11-01 created · [[decision-case-987.1]]
