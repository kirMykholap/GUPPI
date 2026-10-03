---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-capture]]"
purpose: "The hook prints one line after the Spec is written: for a plan that names a conserved Spec, the call of /box with its folder and no question; otherwise the fork, asked by AskUserQuestion with /work and /carry, and the skill picked called"
method: uv run pytest tests/test_spec.py -k 'fork or box'; by hand, an ExitPlanMode of a session, and an ExitPlanMode of a session that took a conserved Spec
checked: 2026-09-28
origin: raw/2026-09-16/1034/ledger.md#case-190.5
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
---

## Criterion

When:
`guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

Then:
The stdout of the hook is one JSON object, `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, that holds one line with the session folder and the Spec file `raw/<hi date>/<hi HHMM>/spec.md`.
**＋** For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
**＋** The agent sees this line in the `ExitPlanMode` result.
**＋** When the approved plan names the `spec.md` of a folder under `vault/raw/` that `is_carried_over` of `guppi/materialize.py` judges marked by `carry.md`, the line names that folder and tells the agent to call `.claude/skills/box/SKILL.md` with it, and to ask the person nothing.
**＋** For any other plan the line is the fork. The fork line tells the agent to ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (the Spec conserved for a later session), and to start nothing until the person answers.
**＋** On the answer, the agent calls `.claude/skills/work/SKILL.md` or `.claude/skills/carry/SKILL.md`, the skill of the option picked.
**－** A `PostToolUse` hook blocks nothing: the tool has run.
**－** Without a Spec, nothing, as before.
**－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.
**－** A Case is still ratified by the person's reply in the chat, never by a picker tool, as `vault/wiki/ratification.md` says: the picker is for the end of the session only.
**－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

## Result

2026-09-28, uv run pytest tests/test_spec.py -k fork: 3 passed; by hand, session 2000: the ExitPlanMode result carried the fork line with the session folder and spec.md, the agent asked by AskUserQuestion with /work and /carry and started nothing before the answer, the person picked /work and the agent called the skill work

## History

- 2026-09-16 created · [[decision-case-190.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L36
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the Criterion replaced whole — the fork as additionalContext, read live (case 255) · [[decision-case-255]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0740/ledger.md#L12
- 2026-09-28 updated: the Criterion replaced whole — the fork is asked by AskUserQuestion with /work and /carry, and the skill picked is called (case 479.1) · [[decision-case-479.1]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/2000/ledger.md#L21
- 2026-10-02 updated: the Criterion replaced whole — a plan that names a conserved Spec leads to /box, any other gets the fork (case 591.3) · [[decision-case-591.3]]
- 2026-10-02 updated: the Criterion replaced whole - ratification.md says a Case is ratified by the person's reply (case 595.18) · [[decision-case-595.18]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
