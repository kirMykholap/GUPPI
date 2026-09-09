---
title: "The reply-silence counter is split between the hook that sees and the hook that speaks"
type: concept
status: current
authority: reply-silence-mechanism
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", ".claude/hooks/catch-the-feedback.ps1", ".claude/hooks/remind-the-feedback.ps1"]
tags: [harness, process, vault]
---

# Why it could not be one hook

**The event that can see a session's replies cannot speak to the session.** `MessageDisplay` receives
the assistant's own message and has no way to return context to it, which was measured with a throwaway
probe rather than assumed ([[a-hook-on-message-display-cannot-speak-to-the-session]]).

**And the event that can speak cannot see.** `UserPromptSubmit` fires on the owner's turn and knows
nothing about how many replies went by in between.

**So the feature is two hooks and one number**, and the split is forced by the platform rather than
chosen for tidiness.

| | counts | speaks |
|---|---|---|
| `catch-the-feedback.ps1` on `MessageDisplay` | yes — replies with no `VAULT-FEEDBACK` block | never |
| `remind-the-feedback.ps1` on `UserPromptSubmit` | no | yes, past the threshold |

# The state discipline that makes it safe

**Each hook writes only its own file.** The catcher owns the count; the reminder tracks, in its **own**
state, the count it last spoke about.

**The reminder never resets the catcher's file**, which is what keeps the two independent: a reset from
the reading side is a write into somebody else's state, and it would lose every increment that landed
between the read and the reset ([[the-feedback-catcher-hook]], [[the-feedback-reminder-hook]]).

**The same discipline was already there in the older half** — the prompt counter reads the write time
of `.superpowers/sdd/vault-feedback.md`, shared state neither hook had to be taught about.

# What each threshold is

**They are different numbers because they count different things at different rates** — a session
produces several replies per prompt, so one threshold would mean two waiting times
([[the-reply-silence-threshold-is-its-own-and-the-prompt-threshold-is-unchanged]]).

**Neither is written into a page as a live figure.** They are in the hooks, and a reader who needs the
current value reads the hook ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
