---
title: "The `VAULT-FEEDBACK` requirement is owned by one hook, registered on each event it needs"
type: decision
status: current
authority: feedback-requirement-owner
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", ".claude/hooks/remind-the-feedback.ps1", ".claude/hooks/remind-the-smoke.ps1", ".claude/settings.json"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-29

**Owner selected: `remind-the-feedback.ps1` gains a second registration.** It runs on
`UserPromptSubmit` and on `PostToolUse` with a `Skill` matcher, and the whole `VAULT-FEEDBACK`
requirement lives in that one file. `remind-the-smoke.ps1` loses its half of it and keeps the smoke
half ([[the-feedback-reminder-hook]], [[the-smoke-gate-hooks]]).

**He selected it knowing the vault records that this same file on this same event was built and
withdrawn on his own correction on 2026-08-28**
([[the-feedback-reminder-fires-on-the-owners-prompt-and-speaks-when-the-channel-is-quiet]]). The
record was in front of him; the ruling is his.

**Rejected: the requirement split across two hooks**, which is what it had been — a demand in the
smoke reminder and a demand in the feedback reminder, drifting independently.

# What it obliges

**One file to change when the requirement changes.** That is the whole ground: two copies of one
demand is the shape this project has already paid for twice
([[a-copied-list-drifts-and-a-sweep-cannot]]).

**The ritual branch is not counter-gated.** When a closing skill opens, the hook speaks whatever the
silence counters say. A ritual has to be told the requirement even on a turn the counter would have
kept quiet ([[every-turn-of-a-retro-files-a-feedback-block]]).

**Six of the day's new suite cases cover the ritual half.**

# The registration took effect with no restart, and that is measured for one event only

**A `PostToolUse` entry added to `.claude/settings.json` mid-session was live immediately.** Both
`remind-the-smoke.ps1` and this hook's new ritual branch spoke on the `/retro` that opened the closing
ritual.

**So the plan's stated ground — *unmeasured for this event, so take the strict case* — is now measured
and the strict case was not needed.** It does **not** generalise: every other event stays unmeasured,
and the reading is about `PostToolUse` and nothing else
([[claude-code-config-loading]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
