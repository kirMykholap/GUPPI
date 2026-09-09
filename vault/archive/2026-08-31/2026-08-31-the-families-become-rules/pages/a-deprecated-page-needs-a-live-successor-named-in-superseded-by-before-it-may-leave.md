---
title: "A `deprecated` page needs a live successor named in `superseded_by:` before it may leave"
type: decision
status: archived
authority: deprecated-move-precondition
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-archive.sh", "scripts/vault-check-selftest.sh"]
tags: [vault, process, testing]
---

# The ruling, 2026-08-29

**Owner selected: the successor check.** A page carrying `status: deprecated` is checked, before it
may move into `archive/`, for a **live page named in its own `superseded_by:`** — not merely for the
archiver's weaker floor of *any* live page naming the slug.

**`refused` and `implemented` proposals are unaffected and need no successor.** A refusal is a cause
and an implemented proposal was never false; neither asserts a claim that something else now asserts
differently ([[a-refused-proposal-is-archived-and-takes-status-refused]],
[[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

**Rejected: the weaker floor**, which the archiver already had for every kind of page and which a
supersession satisfies by accident, because the successor almost always cites the page it replaces.

# Why it is the stronger test

**The floor asks whether the page is reachable. This asks whether the claim was carried forward.** A
deprecated page was retired *because it went false*, so the question worth refusing on is not "can
somebody still find it" but "does the replacement exist and does this page point at it"
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**The link is written in both directions for exactly this reason**, and until today nothing read the
back half. The vault's own schema has required it since the store was built.

# What it caught the day it was built

**A selftest fixture had been violating the supersession rule since 2026-08-22.** The archive
section's fixture planted a `status: deprecated` page carrying no `superseded_by:`, and it passed
because nothing read the field. **The check went red and the fixture was repaired, not the check**
([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]]).

**So the corpus's supersession rule had no instrument behind it until today**, which is the finding
rather than the fixture.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
