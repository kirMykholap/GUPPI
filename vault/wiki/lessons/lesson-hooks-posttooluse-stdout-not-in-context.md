---
type: lesson
kind: error
root_cause: "for `PostToolUse` Claude Code writes the exit-0 stdout of a hook to the debug log and adds nothing to the context — only `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart` and `PostModelSwitch` add plain stdout (https://code.claude.com/docs/en/hooks); a `PostToolUse` hook speaks to the agent through a JSON object on stdout, `hookSpecificOutput.hookEventName: PostToolUse` and `additionalContext`, or through stderr on exit 2, shown as a warning; the docstring of `guppi/spec.py` claims \"which the client adds to the agent's context\" with no probe behind it, and the three fork tests check the text of stdout, not the shape the client reads"
status: new
origin: raw/2026-09-20/0527/ledger.md#L2
sprint: migration
created: 2026-09-20
tags: [harness, hooks]
---

## Trigger

the fork line of `guppi spec` — the `PostToolUse ExitPlanMode` hook printing "spec: the Spec is in …, Work Mode or /carry" on stdout with exit 0 — was not in the ExitPlanMode result of sessions 2054 and 2253; the Spec was in place both times, the agent asked the fork from memory of the rule; `estimate-spec-capture-offers-the-fork` stands passed on pytest alone, its Result says the live print is read at the next ExitPlanMode, and no reading took it

## Root cause

for `PostToolUse` Claude Code writes the exit-0 stdout of a hook to the debug log and adds nothing to the context — only `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart` and `PostModelSwitch` add plain stdout (https://code.claude.com/docs/en/hooks); a `PostToolUse` hook speaks to the agent through a JSON object on stdout, `hookSpecificOutput.hookEventName: PostToolUse` and `additionalContext`, or through stderr on exit 2, shown as a warning; the docstring of `guppi/spec.py` claims "which the client adds to the agent's context" with no probe behind it, and the three fork tests check the text of stdout, not the shape the client reads

## History

- 2026-09-20 created · raw/2026-09-20/0527/ledger.md#L2
