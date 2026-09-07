---
title: "A `vault-feedback.md` line written during an ingest reaches the vault one session late, and that is the order rather than a defect"
type: lesson
status: archived
authority: feedback-lag
basis: code
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/skills/handoff/SKILL.md"]
tags: [vault, process, agents]
---

# The order produces the lag

**`/handoff` empties `.superpowers/sdd/vault-feedback.md` into the journal's `Feedback to the
librarian` section, and `/ingest` runs after it**
([[ingest-runs-after-handoff-at-the-end-of-a-session]]). So anything the ingest itself finds is
written into a file that has already been drained, and it waits for the **next** session's
`/handoff` to carry it.

**This is a property of the cadence, not a leak.** Nothing is lost: the line survives in the file
across the session boundary, and it reaches `log.md` one journal later than the finding that
produced it ([[the-librarian-writes-unattended]]).

**Two of the five feedback lines of 2026-08-20 arrived this way**, from the previous session's
ingest, and the journal says so at the point it lists them.

# Why it is worth a page rather than a shrug

**A reader comparing a `- miss:` line's date with the incident's date will find them a session
apart** and can misread that as a delay in filing. The dates are correct and the gap is structural.

**The previous session's journal documented exactly this about its own inherited line**, which is
how it was recognised the next night rather than rediscovered. That is the thing worth copying: a
structural lag, written down once, stops costing a diagnosis every time it recurs
([[knowing-a-rule-is-not-a-mechanism]] is the other half — knowing it did not make it stop).

**The alternative is not obviously better.** Draining after the ingest would move the lag onto
everything `/handoff` finds, and the ingest is the ritual most likely to notice a corpus defect,
which is the class these lines mostly carry.
