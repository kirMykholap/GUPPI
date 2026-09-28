---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-capture]]"
purpose: "The hook prints the fork after the Spec is written: the agent asks by AskUserQuestion with the options /work and /carry, and calls the skill picked"
method: "uv run pytest tests/test_spec.py -k fork; by hand, the first ExitPlanMode of a session after the render: the fork asked by AskUserQuestion with /work and /carry, and the skill picked called"
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
The stdout of the hook is one JSON object, `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, that holds the fork line with the session folder and the Spec file.
**＋** For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
**＋** The agent sees this line in the `ExitPlanMode` result.
**＋** The fork line tells the agent to ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (the Spec conserved for a later session), and to start nothing until the person answers.
**＋** On the answer, the agent calls `.claude/skills/work/SKILL.md` or `.claude/skills/carry/SKILL.md`, the skill of the option picked.
**－** A `PostToolUse` hook blocks nothing: the tool has run.
**－** Without a Spec, nothing, as before.
**－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.
**－** A Case is still ratified by the person's reply in the chat, never by a picker tool, as `vault/wiki/case-schema.md` says: the picker is for the end of the session only.
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
