---
title: "A citation is not a test in a corpus this densely linked"
type: concept
status: current
authority: citation-as-predicate
basis: measurement
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md"]
tags: [vault, retrieval, process]
---

# The property

**"Something cites it" is a property of the corpus, not of the page.** Every page here is written
with wikilinks into its neighbours, so a predicate keyed on being cited selects almost everything
and separates nothing.

# The measurement, over `wiki/decisions/` on 2026-08-28

**329 pages.** Cited by a page outside `decisions/` and outside `archive/`: **316**, which is 96.0
per cent. Cited by anything outside `archive/`: **328**, which is 99.7 per cent. **Cited by nothing:
one** — `a-migrations-warning-is-developer-output-and-stays-in-english`, and it survives only
because its successor is in the archive.

**1,163 of roughly 3,100 citing edges in `wiki/decisions/` run from `decisions/` to `decisions/`**,
more than from lessons, concepts, entities or proposals per folder. The folder mostly cites itself.

# The consequence

**An archival criterion cannot be *cited by something*.** Under either reading above it leaves the
folder essentially where it was, which is the opposite of what archiving is for
([[the-purpose-of-archiving-is-a-cheaper-working-wiki-and-archive-is-a-warehouse]]).

**So the predicate that was taken is directional and narrow** — a live page names the decision in
`decided_by:`, which is a field one page writes about one other page, not a link anyone may drop in
prose ([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

**And it is why the looser variant failed**: *mentioned anywhere by a live proposal or rule* selects
181 of 329, but 120 of its 165 matches rest on prose in a page body
([[a-claim-asserted-from-prose-rather-than-from-the-file]]).

# Where the same reasoning already applies

**`scripts/vault-archive.sh` refuses to release a page no live page names**, matching the slug
anywhere in a live page. That refusal is a floor against losing a page, and it is a different job
from selecting which pages should go — under a `decided_by:` criterion the refusal is identically
true and can never fire ([[vault-archive-sh]],
[[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]).

# The reading held at 320, and the criterion was proposed again and withdrawn — 2026-08-30

**309 of 320 pages in `wiki/decisions/` are mentioned by at least one other live page in `wiki/`**,
tested by `grep -rlF` on the slug and subtracting the page itself. **Eleven are not.** For comparison,
a live `decided_by:` names 47 slugs in the whole corpus.

**So the ratio this page was written on is unchanged at the folder's new size**: a citation criterion
takes the folder, not a selection out of it.

**The owner proposed exactly this criterion that morning** — «любая страница, которая ссылается на
descision дает право архивировать этот descision» — **and withdrew it himself two turns later**:
«Признавать, что страница уносит решение не сильно хочется». What replaced it inside the same
conversation is the family mechanism, where a decision leaves because a **rule carries its clause**
rather than because something mentions it
([[a-prohibition-family-becomes-one-rule-page-served-by-a-hook]]).

**The miss worth recording is that the store had already answered this and nothing surfaced it.** This
page is dated 2026-08-28 with the numbers on it; the session re-derived them on 2026-08-30 and argued
the point out from scratch. **A measurement that already refutes a proposal is only useful if the
proposal's author finds it**, and here the finding happened after the argument rather than before.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
