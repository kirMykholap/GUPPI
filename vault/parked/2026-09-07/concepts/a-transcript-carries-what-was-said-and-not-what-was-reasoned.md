---
title: "A transcript carries what was said and never what was reasoned, and a user-role block is not always the owner"
type: concept
status: current
authority: transcript-contents
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", "scripts/session-dialogue.py"]
tags: [harness, retrieval, external]
---

# What the harness transcript holds, measured 2026-08-24

**`thinking` blocks are present with empty content.** Only an encrypted signature survives. So a
transcript answers *what was said* and can never answer *why it was said* — which bounds every
ritual built on it ([[the-session-dialogue-extract]]).

**A subagent's turns are not there.** Every `user` and `assistant` record in the measured session
carried `isSidechain: false`, **including across a `/pre-task` dispatch**. What a dispatched agent
said reaches the record only through what the caller relays
([[a-librarian-answer-that-stops-at-the-agent-boundary-is-not-an-answer-the-owner-has]]).

**`AskUserQuestion` answers are there, and this is the half a prompt hook cannot see.** Verified on
the session of 2026-08-22: **11 questions asked, 11 answers recovered**, each with the option label
taken and the free text where "Other" was chosen. In that session **8 of 10 rulings arrived through
a menu** ([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

# `origin.kind` is what separates the owner from the harness

**A user-role text block is not necessarily the owner.**

| what `origin` says | who it is |
|---|---|
| `{"kind": "human"}` | a turn he typed |
| `{"kind": "task-notification"}` | the harness reporting a background job |
| absent, `isMeta` true | the body of a skill the session invoked |
| absent, `isMeta` false | an interrupt marker — **which is his: he pressed stop** |

**Reading a user-role block as his word is how a task notification becomes a quotation.** It
happened on the first real use of the extract, and it is the class the ratification apparatus exists
against ([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]],
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

# What the store is, as a quantity

**37 files, 255 MB**, for this project alone. **Dialogue is 2–4% of a transcript** — median 130 KB
across the 37, largest 221 KB, 5.8 MB in total — which is what makes reading it once per session
affordable ([[the-floor-under-a-session-is-read-because-the-record-already-existed]]).
