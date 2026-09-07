---
title: "The reply-silence threshold is its own, and the prompt threshold is left where it was"
type: decision
status: current
authority: reply-silence-threshold
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", ".claude/hooks/remind-the-feedback.ps1", ".claude/hooks/catch-the-feedback.ps1"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-29

**Owner selected: the reply-silence counter fires at five consecutive assistant replies** that carried
no `VAULT-FEEDBACK` block.

**The existing threshold on his own prompts stays where it is, at three.** He asked where the three had
come from before ruling; it is his own, set on 2026-08-28, and the session had not proposed changing it
([[the-feedback-reminder-fires-on-the-owners-prompt-and-speaks-when-the-channel-is-quiet]]).

**Rejected: one threshold governing both counters.** They count different things at different rates — a
session produces several replies per prompt — so one number would mean two different waiting times.

# Why there are two counters at all

**A prompt counter cannot see a session that goes quiet in its own replies**, which is the gap the
reply counter closes. The reminder's own page named that gap when the prompt counter was built
([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).

**And the counting cannot live where the speaking lives.** `MessageDisplay` is the only event that sees
a session's replies and it cannot speak to the session, so the feature is split across two hooks and one
number ([[the-reply-silence-counter-is-split-between-the-hook-that-sees-and-the-hook-that-speaks]],
[[a-hook-on-message-display-cannot-speak-to-the-session]]).

# What it obliges

**`catch-the-feedback.ps1` writes the count and `remind-the-feedback.ps1` reads it.** Each hook writes
only its own file: the reminder tracks the count it last spoke about in its own state rather than
resetting the file the catcher owns.

**Neither number is written into any page's prose as a live figure.** They are in the hooks, and a
reader who needs the current value reads the hook.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
