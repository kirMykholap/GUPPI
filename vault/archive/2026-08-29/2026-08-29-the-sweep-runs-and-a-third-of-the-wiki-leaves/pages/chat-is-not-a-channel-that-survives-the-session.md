---
title: "Chat is not a channel that survives the session, and saying it out loud feels like filing it"
type: lesson
status: archived
authority: chat-durability
basis: human
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md"]
tags: [process, vault, agents]
---

# The incident

**A vault miss was found and not written into `vault-feedback.md` in the turn it appeared.** It was
reported to the owner in chat, and filed hours later at the retrospective — marked late in the file
itself, which is the only reason it is recoverable at all.

**Why it looked unnecessary at the time: it had just been said out loud.** The finding had an
audience, the owner had answered, and the transaction felt complete. That feeling is the whole
failure — the rule requiring the line in the same turn exists for exactly it
([[write-the-miss-into-vault-feedback-before-the-turn-ends]],
[[feedback-is-recorded-in-the-turn-it-is-noticed]]).

# What chat actually is, as a store

**It is a buffer with no reader after the session ends.** Nothing in this repository looks inside a
transcript: `/handoff` drains a file, `/ingest` reads a journal, and the librarian greps the vault.
A finding that lives only in chat is not slow to retrieve — it is unretrievable
([[the-closing-ritual-produces-what-the-journal-cannot-hold]]).

**And the reconstruction is worse than the recording.** By the retrospective the question, the grep
that failed and the page that should have carried it are gone, so what gets filed is a summary of a
feeling about a finding ([[journal-vault-brief-each-artefact-has-one-owner]]).

# The rule this produces, which is not new

**One line, in the turn, before anything else.** Recording is not arguing; whether the corpus
changes is the owner's call afterwards. **A rule whose cost is one line and which was still skipped
was skipped for a reason that will recur** — and the reason is that the alternative channel felt
warm ([[knowing-a-rule-is-not-a-mechanism]]).
