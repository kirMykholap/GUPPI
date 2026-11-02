---
type: lesson
kind: error
root_cause: the skill work runs guppi test and guppi check as shell patterns of its preamble and its text expects a failed pattern to come back as an empty line, while Claude Code refuses the whole skill when a shell pattern exits non-zero, so /work cannot load while guppi check finds anything, the usual state of a sprint with a core page in draft
status: archived
insight: "[[insight-harness-skill-refused-when-a-preamble-command-exits-non-zero]]"
origin: raw/2026-11-02/1337/ledger.md#L7
sprint: plugin
created: 2026-11-02
tags: [harness, workflow]
---

## Trigger

in session 1429 of the clone C:\PROJECTS\GUPPI-trial, /box called /work, and Claude Code refused to launch the skill with "Shell command failed for pattern "!`uv run --project .guppi guppi check`"", since guppi check printed the three lint lines of the baseline and exited 1; the agent read .claude/skills/work/SKILL.md and ran Work Mode by its text

## Root cause

the skill work runs guppi test and guppi check as shell patterns of its preamble and its text expects a failed pattern to come back as an empty line, while Claude Code refuses the whole skill when a shell pattern exits non-zero, so /work cannot load while guppi check finds anything, the usual state of a sprint with a core page in draft

## History

- 2026-11-02 created · raw/2026-11-02/1337/ledger.md#L7
- 2026-11-02 updated: clustered under insight-harness-skill-refused-when-a-preamble-command-exits-non-zero (synthesis) · raw/2026-11-02/1337/ledger.md#L7
- 2026-11-02 archived · insight actioned
- 2026-11-02 archived · cleanup
