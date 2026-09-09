---
title: "A hook on `MessageDisplay` cannot speak to the session, measured with a probe that was then deleted"
type: lesson
status: current
authority: message-display-silence
basis: measurement
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", ".claude/hooks/catch-the-feedback.ps1", ".claude/settings.json"]
tags: [harness, agents, process]
---

# The measurement, 2026-08-29

**A probe hook returning `hookSpecificOutput` with `hookEventName: MessageDisplay` and
`additionalContext` fired three times with `final=true`** — confirmed by its own marker file — **and no
context reached the session on any of them.**

**`.claude/hooks/probe-message-display.ps1` existed for that one measurement and was deleted.** It
wrote nothing but its marker, and the reading is what survives it.

**Registering it was step one of S3 item 43**, understood by the session from the plan the owner
approved rather than stated by him separately.

# What it does and does not establish

**It establishes that a reply-silence counter cannot both live on that event and speak from it.** The
feature is therefore two hooks and one number
([[the-reply-silence-counter-is-split-between-the-hook-that-sees-and-the-hook-that-speaks]]).

**It does not distinguish "the event cannot carry context" from "the field is named something else on
this event".** The probe could not tell those apart, and nothing since has. **Say which of the two you
are relying on** before building anything else on it.

**It is a reading about one event.** `PostToolUse` was measured the same day to take a new registration
with no restart, and that reading does not generalise either
([[the-feedback-requirement-is-owned-by-one-hook-and-registered-on-each-event-it-needs]]).

# Why a throwaway probe was the right instrument

**The alternative was reading the documentation and believing it**, which is how the event's *other*
described behaviour turned out wrong here: its description says it fires with each batch of newly
completed lines, and measured, it fires once with the whole message
([[message-display-fires-once-with-the-whole-message]]).

**A hook that writes nothing and is removed the same day costs one registration and one turn**, and it
is the cheapest way this repository has to answer a question about its own platform
([[a-register-of-what-each-hook-writes-when-it-is-probed]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
