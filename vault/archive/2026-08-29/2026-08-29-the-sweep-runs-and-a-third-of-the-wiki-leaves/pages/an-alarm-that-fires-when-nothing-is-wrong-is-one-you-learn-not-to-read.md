---
title: "An alarm that fires when nothing is wrong is one you learn not to read"
type: lesson
status: archived
authority: false-alarm-cost
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, vault, agents]
---

# The instance, 2026-08-20

**The one-writer note had been firing about fifty times per ingest into the librarian's own
context** — the one agent for which the note is not a warning at all, since writing `wiki/` is its
job.

**Verified as pre-existing rather than assumed**: the branch is unchanged in its history, so this
was not something the session had just introduced and then found. That distinction is what makes it
a measurement and not a self-report.

**The message had been written for two audiences at once** — *if you are the librarian, this is your
job: proceed* — which is what a hook does when it cannot tell who is writing. That it cannot is
already on the record: **a `PreToolUse` payload does not say who**
([[parallel-librarians-break-the-one-writer-property]], [[session-hooks]]).

# What it costs, and why it is not merely noise

**A reader who meets a warning fifty times, correctly ignoring it every time, has been trained.**
The training generalises: the next warning from the same channel is skimmed, and the one after that
is not read. So a false alarm does not cost attention once — it spends the credibility of the
channel, and it spends it against every future message in that channel.

**The repair is the channel, never the scope.** Speaking once per session leaves the guard covering
exactly what it covered ([[the-one-writer-note-speaks-once-per-session]]); narrowing what it watches
would have reversed a direction the owner had already chosen
([[the-hook-was-stricter-than-the-rule-it-enforced]]).

# Where this store has met the same shape

**A staleness check that fired on every fresh clone**, deterministically, because git writes the
working tree in index order ([[session-hooks]]). **A density advisory printed on every run**, which
buried the one advisory that was about that run
([[the-tag-density-advisories-move-behind-lint]]). Same failure, three channels: the alarm is
correct about its condition and wrong about when it is worth saying.
