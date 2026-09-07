---
title: "The session slug is written to a file by whoever first needs it, and `/handoff` reads it rather than inventing one"
type: decision
status: current
authority: session-slug-source
binding: deferral
basis: human
sprint: S2
decided: 2026-08-22
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md", "scripts/vault-archive.sh", ".claude/skills/handoff/SKILL.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-22

**Owner selected: the slug is written to a file by whoever first needs it, and `/handoff` reads that
file** instead of naming the session itself.

**Rejected: performing every retirement after `/handoff`**, which splits a strike in two and leaves a
`deprecated` page sitting in `wiki/` for half a session — visible to every reader and to the gate,
claiming an `authority:` it no longer owns.

**It is decided and not built.** Nothing in the tree writes or reads such a file today.

# The hole it closes

**A session folder in `archive/` is named from the journal's own filename**
([[the-archive-gains-a-folder-per-session-inside-the-date]]), **and the journal does not exist until
`/handoff` runs at the end of the session.** So a page retired at any other moment has no legal
folder name to move into, and every retirement that is not the last act of a session meets this
([[archive-is-dated-by-session-and-holds-what-left-the-working-set]]).

**It surfaced while executing a ruling, not while reading it.** The decision that dates the archive
is silent on *when* the retirement happens, and every prior retirement went flat, so nothing had ever
tested the ordering
([[the-archive-script-gains-a-pages-kind-and-a-retired-page-is-dated-by-its-session]]).

# What stood in for it on the day, and why that is not enough

**The slug was fixed at the start of the session and `/handoff` was bound to it by a promise.** The
folder is `2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict` and the journal matches it.

**A promise is not a mechanism.** Nothing compares the session folder holding a retired page against
the journal that names the session, so a `/handoff` that wrote anything else would leave the page
under a folder naming a session that does not exist — **and no check here would say so**
([[knowing-a-rule-is-not-a-mechanism]], [[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

**A file is the repair because it is the only artefact both parties can reach.** The retirement
happens mid-session in one process and `/handoff` runs at the end in another; chat does not survive
between them ([[chat-is-not-a-channel-that-survives-the-session]],
[[the-ritual-records-itself-rather-than-being-detected]]).

*(Compiled from `raw/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md`.)*
