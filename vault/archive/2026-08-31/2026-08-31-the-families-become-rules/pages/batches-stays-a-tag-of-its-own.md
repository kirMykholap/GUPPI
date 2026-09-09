---
title: "`batches` stays a tag of its own: the merge into `collection` was proposed and refused the same day"
type: decision
status: archived
authority: batches-tag
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", "tags.md"]
tags: [retrieval, vault]
---

# Proposed in the morning, refused by the owner the same day

The merge was a candidate **only under the frame that was replaced the same session.** Under the
old frame the measure was the dictionary's size, and `batches` "selects nothing new" because it is
a strict subset of `collection` — verified at `94483b1`: all five of its pages carry both. Under
the rule adopted that day the measure is whether a tag narrows **inside a folder** against ten
([[the-folder-is-the-first-narrowing]]), and `batches` is 3 in `decisions/` and 2 in `concepts/`,
nowhere near it.

**Rejected: merging `batches` into `collection`.** Four reasons, each checkable:

1. **It reverses a recorded split that worked.** `tags.md` records that `collection` was narrowed
   on 2026-08-13 at 17 of 29 pages, and **bookkeeping is the piece that went out to `batches`**.
2. **It was never a candidate by the written rule.** The dictionary's merge rule is *two tags with
   near-identical definitions*, and these two are not — the act of gathering against the run's
   bookkeeping. The subset test that nominated it was invented in chat.
3. **A strict subset is a refinement**, which is exactly the narrowing the new rule is built on:
   `collection` selects 18 pages and `batches` 5 inside them.
4. **It would perform the mechanism that inflated `vault`** — moving `финализатор` and
   `parse_batches` onto a tag that selects 18 pages instead of 5.

## The mechanical cost was also higher than stated

Four of the five pages carry exactly `[batches, collection]`, so removing one tag leaves them with
a single tag and breaks the 2-to-4 rule; each would need a second tag chosen by hand, three of them
in `decisions/`, where two advisories already fire
([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

**What this leaves behind is a lesson rather than a rule.** The proposal was made under one frame
and survived into a session that had replaced it, and nothing prompted the re-check:
[[a-proposal-must-be-rechecked-when-the-frame-changes]].
