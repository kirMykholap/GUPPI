---
title: "`MessageDisplay` fires once with the whole message, and its own description says otherwise"
type: concept
status: current
authority: message-display-event
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", ".claude/hooks/catch-the-feedback.ps1"]
tags: [harness, testing, external]
---

# Measured, 2026-08-24, on Claude Code 2.1.228

**The event's own description says it fires "with each batch of newly completed lines while an
assistant message streams".** Measured live with a probe hook, a **1,251-character message fired it
once**, with `index` 0, `final` true, and `delta` holding the whole message.

**The divergence is recorded and not resolved.** Two readings are available — the description is
wrong, or this host batches differently — and nothing here decides between them. What is written
down is what was observed, on a named version, with the instrument named
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

# The payload

`session_id`, `transcript_path`, `cwd`, `prompt_id`, `turn_id`, `message_id`, `index`, `final`,
`delta`, `hook_event_name`.

**`message_id` is stable across the fires of one message and is the deduplication key.**

# Registering a hook on it takes effect immediately

**No restart.** That is not true of every part of this harness — agents, skills and hooks reload on
different occasions, and getting it wrong costs a session
([[claude-code-config-loading]]).

# Why the divergence was affordable

**`.claude/hooks/catch-the-feedback.ps1` accumulates by `message_id` and parses at `final`**, so it
is correct whether the event fires once or many times ([[the-feedback-catcher-hook]]). The design
does not depend on which reading is right, which is what made it safe to record the disagreement
instead of chasing it.

# Why this page exists rather than the code alone

**Owner's decision, 2026-08-24: a page with `basis: measurement` records what the event actually
does.** Rejected: relying on the code, which lets a later session read the vendor's description,
conclude the accumulation is pointless, and "fix" what is not broken
([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]).

# The probe that measured it no longer exists

`.claude/hooks/probe-message-display.ps1` was written to read the live payload and deleted the same
hour once it had. **A probe is a measuring instrument and not a component**, and this one left its
reading here rather than in the tree ([[the-conditional-delivery-probe]]).
