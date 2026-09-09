---
title: "The lessons cycle is the owner's own, and a lesson leaves `lessons/` when a page outside `lessons/` cites it"
type: decision
status: archived
authority: lessons-cycle
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/lessons-queue.py", "scripts/vault-archive.sh"]
tags: [vault, process, retrieval]
---

# The cycle, in his own description — 2026-08-26

> **owner:** «главная цель сборщика уроков - обработать уроки так, чтобы они были связаны
> какой-либо страницей(proposal - если новая, любая другая страница если она уже существует) и
> передать это библиотекарю.»

**Sessions write lessons; `/ingest` files them into `wiki/lessons/`; the collector reads them and
prepares a *proposal* rather than a rule; the librarian decides whether to write a new page or to
attach the lesson by citing it from an existing one; and the archiver then walks mechanically and
moves out what has a route back.**

**Nothing is deleted.** The lesson stays reachable through the page that cites it — which is why the
citation, and not the removal, is the unit of work
([[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]],
[[lessons-become-a-queue-drained-into-proposals]]).

# The archiver's criterion for a lessons page

**Move a lesson that any page cites, except another lesson.** *(owner selected it, 2026-08-26.)*

**A lesson-to-lesson citation is not a route back**: once both move, both are unreachable from the
live corpus, and the pair has left the store rather than been filed in it.

**Recorded with its subject, after he corrected a version of this line that had lost it.** The line
first went down as *"any page except a lesson"*, which is a statement about **which pages may be
archived at all** — a rule he never gave. What he said is a statement about **what counts as a
citation to a lesson**. The correction was caught at the ratification step, which is the step that
exists for exactly this ([[a-quote-written-for-the-librarian-carries-its-context]],
[[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]]).

# What the criterion would do today, measured

**157 lesson pages on 2026-08-26. One is cited by nothing live at all; 12 are cited only by other
lessons; 144 are cited by something outside `lessons/`.** So the first sweep would move **144** and
leave **13**.

**The queue reads 104 and is a different number** — `scripts/lessons-queue.py` counts only `rules/`
and `proposals/` as citers and does not see `decisions/`
([[the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach]]).

# Rejected, and what it obliges

**Rejected: deleting a drained lesson.** Nothing is deleted here, and a lesson that has been acted
on is exactly the page a reader six months later needs to find behind the rule
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**It obliges an archiver that does not exist.** `scripts/vault-archive.sh` moves named files and
refuses to move a page no live page cites; **the sweep over `lessons/` applying this criterion is
unbuilt**, and so are the sweep that finds `deprecated`/`superseded_by:` pages and checks their
successor is live, and the mechanical `status: archived` write
([[the-archiver-sets-status-archived-and-the-value-enters-the-schema-first]]). All three are S3 work
by the rulings of the same day.

# The criterion was put to him again on 2026-08-28 and stands unchanged

*(the owner selected it.)* **A lesson leaves when any page outside `lessons/` cites it — not only a
proposal.** His own earlier description of the cycle *through* a proposal was a particular case
rather than a narrowing of the rule, and he said so when the narrower reading was offered.

**And the part of the cycle he named as the point of it** is the separate agent that works the
lessons and prepares a proposal from them, which is still unbuilt for a second session
([[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]).

**The sweep that would apply this criterion is still not written**, and it now has a decided failure
mode ([[the-archive-sweep-that-walks-each-folder-and-collects-its-refusals]],
[[the-archive-sweep-continues-past-a-refused-move-and-collects-its-refusals]]).
