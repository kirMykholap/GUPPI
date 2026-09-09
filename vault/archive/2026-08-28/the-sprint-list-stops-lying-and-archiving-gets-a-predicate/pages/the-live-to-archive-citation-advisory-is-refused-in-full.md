---
title: "The live-to-archive citation advisory is refused in full, and a live page citing an archived one is legal"
type: decision
status: deprecated
authority: archive-citation-advisory
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
superseded_by: [[the-gate-advisory-on-a-live-link-into-a-deprecated-page-is-ordered-built]]
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-26

> **owner:** «я вообще не вижу смысла добавлять такое в гейт. Если живая страница ссылается на
> архивную - окей, это легальное поведение. Ничего не строим дополнительно»

**Refused in full.** The lessons collector's Proposal 2 — an advisory naming every live-to-archive
citation edge — is not built, and neither is the narrower variant the session offered as a
candidate: *cites a superseded page without naming its successor.*

**The proposal is filed as refused rather than dropped**
([[a-reference-graph-sweep-over-live-to-archive-citations]],
[[a-refused-proposal-is-archived-and-takes-status-refused]]).

# The measurement the refusal was taken against

**313 citation edges run from live `wiki/` pages into `archive/`**, across **199 of 653** live
pages, naming **38 of the 50** archived slugs, and the gate exits 0 on every one. Measured by the
collector at `9950dbd`.

**All 313 point at a page carrying `status: deprecated`.** `archive/` holds 50 pages: 38
`deprecated` and 12 with no status, the latter being journals nothing cites by slug. **So *cited
page is in `archive/`* and *cited page is deprecated* give the identical answer today** — the
distinction the session spent a round building has zero cases, and would acquire any only once the
lessons sweep runs.

# What the refusal leaves standing, and what it overturns

**It leaves standing that a live page can argue from a deprecated one and nothing catches it**
([[a-live-page-can-argue-from-a-deprecated-one]]). That page describes a real hole; this ruling says
the hole is not worth an instrument.

**It follows from the wider reading of `archive/` he gave the same day**: the folder is where
inactive pages go, not only pages that were replaced, so a citation into it is not evidence of
anything ([[archive-is-dated-by-session-and-holds-what-left-the-working-set]]).

# Rejected alternatives, both his

**Rejected: the full advisory** — one line per edge under `--lint`. **Rejected: the narrow variant**
scoped to a superseded page whose successor is not named. He refused the class, not a size of it:
«Ничего не строим дополнительно».

# Overturned 2026-08-28

**The owner reversed the refusal.** The gate gains an advisory keyed on the target's `status:` — a
live page links a slug whose page is `deprecated` — printing a line and never a red
([[the-gate-advisory-on-a-live-link-into-a-deprecated-page-is-ordered-built]]).

**What survives the reversal is the sentence in this page's title**: a live page citing a deprecated
one is still legal. The advisory names it; nothing forbids it.

**What the reversal was taken against is a wider measurement than the one above.** 313 edges was a
reading of 2026-08-26 over `archive/` targets; over the whole of `wiki/` on 2026-08-28 it is 424 link
occurrences across 210 live pages naming 42 deprecated slugs, of which about 197 occurrences lean on
the target as if it were live.
