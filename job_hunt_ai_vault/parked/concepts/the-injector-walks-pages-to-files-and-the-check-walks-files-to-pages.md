---
title: "The injector walks pages to files and the check walks files to pages, and neither sees what the other sees"
type: concept
status: current
authority: injector-check-directions
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# Two directions, and the mechanism needs both

| | Direction | What it opens | What it is blind to |
|---|---|---|---|
| `scripts/vault-inject.sh` | **pages → files** | for each current rule page, **only** the one destination its `governs:` names | any file no `governs:` names, and any region in it |
| `scripts/vault-check.sh`, rule 11 | **files → pages** | both `CLAUDE.md`s and every markdown under `.claude/`, swept | a rule that has no region anywhere at all |

**The injector never opens a file no `governs:` names.** `for page in "$VAULT"/wiki/rules/*.md` then
one destination per page — so a region in a file outside that set is invisible to it, forever.

**The check never notices a rule with no region.** It sweeps files and asks of each region whether it
is well formed, has a page behind it, and sits at the right address. A rule page nobody has marked up
anywhere produces no region, so there is nothing for the sweep to find. That absence is caught from the
other end — the injector opens the destination, finds no region, and rule 12 reports it.

## Why the split is not an accident of implementation

**Content belongs to the writer and address belongs to the sweep.** Asking the injector about an
address it cannot reach would mean giving it a second copy of the swept governed set, and a copied list
drifts where a sweep cannot ([[a-copied-list-drifts-and-a-sweep-cannot]]). Asking the check about
content would mean a second implementation of the comparison, which is exactly what rule 12 refuses by
running the injector instead ([[a-check-asks-by-running-the-writer-it-checks]]).

So the two blindnesses are **complementary by construction**, and that is checkable rather than
believed: every failure mode of the mechanism is named by one of them, and the one case that fell
between them was the reason the fifth verdict exists
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

## The consequence a reader needs

**A green gate means the two agree about what they can each see.** It does not mean every rule is
rendered somewhere useful: twelve of thirteen governed files carry no region and the run is green with
an advisory ([[a-governed-file-with-no-region-is-an-advisory]]).

**And it means one of the two must change when the mechanism widens.** A page outside `wiki/rules/`
carrying `governs:` is invisible to both — the injector's glob and every `governs:` branch of the check
exclude it ([[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]]).
