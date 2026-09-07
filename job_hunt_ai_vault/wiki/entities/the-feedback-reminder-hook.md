---
title: "`remind-the-feedback.ps1` — the hook that speaks when the feedback channel has gone quiet"
type: entity
status: current
authority: feedback-reminder-hook
basis: code
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", ".claude/hooks/remind-the-feedback.ps1", ".claude/settings.json", "scripts/hook-selftest.ps1"]
tags: [harness, process, vault]
---

# The hook

**Appeared 2026-08-28, twice.** It was built first on `PostToolUse` with a `Skill` matcher, firing
once when `/grill-me` opened; the owner replaced it the same day
([[the-feedback-reminder-fires-on-the-owners-prompt-and-speaks-when-the-channel-is-quiet]]).

| Property | |
|---|---|
| File | `.claude/hooks/remind-the-feedback.ps1` |
| Event | `UserPromptSubmit`, which takes no matcher |
| Disposition | **speaks, and only sometimes** — through `hookSpecificOutput.additionalContext` |
| Reads | the write time of `.superpowers/sdd/vault-feedback.md` |
| Writes | its own silence counter |
| Fires | on the third consecutive quiet prompt, then resets |

**It is the first hook in this repository that decides whether to speak.** Every other one either
always speaks or always refuses ([[session-hooks]]).

**Nothing had to be coordinated with the catcher.** `catch-the-feedback.ps1` already touches that
file whenever it files a block, so the mtime is shared state neither hook had to be taught about
([[the-feedback-catcher-hook]]).

# What is confirmed about its event, and what is not

**Confirmed:** the event name, that it takes no matcher, that it supports
`hookSpecificOutput.additionalContext`, and that it fires on every turn of the owner's.

**Not confirmed:** the name of the field carrying the prompt text, the behaviour on exit 2, and
whether it fires on the first turn. **The hook is built without reading the prompt text**, which is
what makes those three harmless here rather than answered.

# Its cases

**`scripts/hook-selftest.ps1` gained fourteen cases for it**, and the suite read **caught 194,
missed 0 in 55 s** on 2026-08-28, up from 180 at the session's start. The nine cases of the first,
`PostToolUse` version were replaced with the hook they tested.

# What it does not cover

**A session that goes quiet in its own replies.** The counter advances on the owner's prompts
([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).

# It gained a second registration and now owns the requirement whole — 2026-08-29

**The heading above is answered.** The hook is registered on `UserPromptSubmit` **and** on
`PostToolUse` with a `Skill` matcher, and the whole `VAULT-FEEDBACK` requirement lives in this one
file ([[the-feedback-requirement-is-owned-by-one-hook-and-registered-on-each-event-it-needs]]). `remind-the-smoke.ps1` lost its
half of it and keeps the smoke half ([[the-smoke-gate-hooks]]).

**The second registration is the shape the owner withdrew on 2026-08-28 and restored on 2026-08-29**,
knowing the vault records the withdrawal. The ruling is his, and the page recording the first build
stands as written.

**The ritual branch is not counter-gated.** When a closing skill opens, the hook speaks whatever the
counters say — a ritual has to be told the requirement even on a turn the silence counter would have
kept quiet.

**It now reads two counters, not one.** The prompt counter is its own, at a threshold of **three**;
the reply-silence counter is written by `catch-the-feedback.ps1` and read here at a threshold of
**five** ([[the-reply-silence-threshold-is-its-own-and-the-prompt-threshold-is-unchanged]]). The split is
structural: the event that can see the session's replies cannot speak
([[the-reply-silence-counter-is-split-between-the-hook-that-sees-and-the-hook-that-speaks]]).

**Each hook writes only its own file.** The reminder tracks the count it last spoke about in its own
state rather than resetting the file the catcher owns, so neither hook has to know when the other ran.

**The registration took effect immediately, with no restart.** A `PostToolUse` entry added to
`.claude/settings.json` mid-session had both `remind-the-smoke.ps1` and this hook's new ritual branch
speaking on the `/retro` that opened the closing ritual. The plan's stated ground — *unmeasured for
this event, so take the strict case* — is now measured for `PostToolUse` and the strict case was not
needed. It does **not** generalise to other events, which stay unmeasured.

**Six of the day's new suite cases are this hook's ritual half.**

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
