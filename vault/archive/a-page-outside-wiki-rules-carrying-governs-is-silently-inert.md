---
title: "A page outside `wiki/rules/` carrying `governs:` is silently inert — neither rendered nor refused"
type: concept
status: deprecated
authority: governs-outside-rules
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
superseded_by: [[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]
tags: [harness, record-schema, vault]
---

# Measured on the code, not inferred from the schema

**`scripts/vault-inject.sh` globs one folder**: `for page in "$VAULT"/wiki/rules/*.md`. A page anywhere
else is never opened, so its `governs:` renders nothing.

**And every `governs:` branch in `scripts/vault-check.sh` is gated on `folder == "rules"`.** The
frontmatter pass collects the field, but the verdicts that require it, forbid `authority:` beside it, and
join it against a region's file all apply inside that folder only.

**So the field is neither rendered nor refused outside it.** Write `governs: CLAUDE.md` on a concept page
and the gate stays green, the injector stays silent, and the author has every reason to believe the text
is being delivered.

## Why this is the shape that matters here

**It is a green that examined nothing** — the failure this project has recorded more often than any
other, and the one every one of its checks was written against
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

It is also the *inverse* of a defect the same mechanism already carries and already answers: a marker
with a typo would be invisible rather than wrong, so the detector was widened
([[a-marker-is-detected-loosely-and-judged-strictly]]). Here the field is legal, spelled correctly, and
does nothing. **Nothing distinguishes it from a field that works.**

## What has to happen, whichever way the decision goes

**The silence must become either a rendering or a refusal.** Those are the only two states that leave a
reader able to tell what happened:

| If the field is widened | If it is not |
|---|---|
| the injector globs `wiki/*/*.md` and the check's branches drop the folder gate ([[governs-becomes-a-property-of-any-page]]) | a verdict: `governs:` on a page outside `rules/` is red |

**The owner has decided to widen it, and it is not built** — so the inert state is what stands today.
The pair to this from the other side is a `<!-- text -->` slice on a page with no `governs:` at all,
which is also unremarked and is the second verdict the mechanism change owes
([[the-marker-carries-a-type-and-governs-is-read-as-a-field]]).
