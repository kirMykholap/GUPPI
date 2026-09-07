---
title: "A harness change is recorded the moment it is decided, and cut out at ingest on a section boundary"
type: decision
status: current
authority: harness-change-capture
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", ".superpowers/sdd/vault-feedback.md"]
tags: [harness, process]
---

# Decided 2026-08-16: capture at the moment, never classify afterwards

**A change to the harness is written down in the turn it is decided**, as a marked line in
[[vault-feedback-file]], and `/ingest` **cuts it out on a section boundary** rather than reading
prose for it. The handoff carries a section of its own for it
([[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]]).

This is the same shape the project already chose for vault feedback
([[feedback-is-recorded-in-the-turn-it-is-noticed]]), applied to a second kind of observation and
for a second reason.

## Rejected: an agent classifying prose as harness-related at ingest

**A classifier detects presence and cannot detect absence.** If it misses a rule, nothing anywhere
says how many it missed — the error is unbounded and silent, which is this project's signature
failure mode and the one the whole harness build exists to remove. A section boundary has the
opposite property: the section is either there or it is not, and
[[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]] makes the section set checkable.

Cutting on a marker inside prose was rejected for the same reason: it re-admits the classifier
through the back door.

## What it obliges

- **The session, not the librarian, writes the line** — the party that noticed, in the moment.
  Recording is not arguing, and it costs a line ([[feedback-is-recorded-in-the-turn-it-is-noticed]]).
- **The channel's failure mode is silence.** Nothing checks that the section was written to, and a
  session that never opens it produces a `Harness` section reading "none" that is indistinguishable
  from a session that changed nothing ([[vault-feedback-file]]).
