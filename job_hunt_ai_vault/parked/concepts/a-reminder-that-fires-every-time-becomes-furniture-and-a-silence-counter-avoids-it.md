---
title: "A reminder that fires every time becomes furniture, and a silence counter is what avoids it"
type: concept
status: current
authority: reminder-fatigue
basis: code
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", ".claude/hooks/remind-the-feedback.ps1", ".claude/hooks/remind-the-smoke.ps1"]
tags: [harness, process, vault]
---

# The mechanism

**`remind-the-feedback.ps1` reads the write time of `.superpowers/sdd/vault-feedback.md`**, which
`catch-the-feedback.ps1` already touches whenever a block is filed, and keeps a counter of
consecutive prompts in which that time did not move. **It speaks on the third quiet prompt, then
resets.**

**Nothing had to be coordinated between the two hooks.** The file's mtime is the shared state, and
the catcher was already writing it for its own reasons.

**It is the first hook in this repository that decides whether to speak.** Every other one either
always speaks or always refuses ([[session-hooks]], [[the-feedback-reminder-hook]]).

# Why a counter rather than a louder reminder

**Two defences against the feedback channel going quiet already existed, both firing once per
invocation, and neither stopped anything.** The rendered rule
[[every-turn-of-a-retro-files-a-feedback-block]] is addressed to `/retro`; the demand at the head of
`remind-the-smoke.ps1` fires once at a retro's start. **Checked against the incident of 2026-08-28:
neither could have fired**, because the conversation that lost eleven owner rulings was neither a
retro nor a tool run ([[divergence-the-retro-filed-no-feedback-block-while-it-ran]]).

**A reminder that fires unconditionally stops being read**, which is the standing argument against
always-on advisories here and is not new
([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

# What the counter buys that neither of the others could

**It makes the channel measurable for the first time.** How often the hook spoke in a session is a
reading, and **zero means the channel worked** — the first instrument here whose silence is the
result rather than the absence of one.

# What it does not cover

**A session that goes quiet in its own replies.** The counter advances on the owner's prompts, so a
session filing nothing while he says nothing is invisible to it. `MessageDisplay` is registered and
fires on every assistant reply, and that is where the covering counter would live
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]],
[[the-feedback-reminder-fires-on-the-owners-prompt-and-speaks-when-the-channel-is-quiet]]).
