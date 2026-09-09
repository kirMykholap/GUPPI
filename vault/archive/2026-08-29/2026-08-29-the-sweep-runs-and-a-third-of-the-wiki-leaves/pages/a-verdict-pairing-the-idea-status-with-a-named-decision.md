---
title: "A verdict pairing `status: idea` with a named decision"
type: proposal
status: archived
authority: idea-decided-by-verdict-design
basis: human
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "wiki/proposals/_schema.yaml"]
decided_by: [[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]]
tags: [record-schema, vault, harness]
---

# What would be built

**A gate verdict relating a proposal's `status:` to whether it carries `decided_by:`.** Both
halves exist already and nothing joins them: `idea` is a legal status in `wiki/proposals/` and
`decided_by:` is a legal key there, optional.

**The pairing the owner ordered built**: a page carrying `status: idea` is a half-thought nobody
ruled on, so it names no deciding decision; a proposal that a decision produced is past that stage
and names it. The verdict says so mechanically instead of leaving it to a reader.

# What is open, and it is the objection the ruling overruled

**Which way the implication runs was never settled.** *An `idea` must carry no `decided_by:`* and
*a proposal carrying `decided_by:` may not be an `idea`* are the same rule read from two ends, but
they redden different pages and produce different messages, and neither was chosen.

**The status would then carry two meanings at once.** `status:` is *maturity* by the ruling of
2026-08-17 ([[an-idea-is-a-proposal-with-an-immature-status]]); this verdict makes it also report
whether anything authorised the page. A fully designed proposal that no decision produced would have
to assert an immaturity it does not have, and a half-thought one produced by a deferral decision
could not be an `idea` at all — and deferral decisions with proposals behind them are the ordinary
case here, not the corner
([[proposals-are-a-folder-not-a-status]]).

**Nothing here resolves that.** The objection is the design's own open question and it is the first
thing the session that builds this has to answer
([[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]]).

# What it would take, in order

1. the `decided_by:` back-fill across `wiki/proposals/`, which `bash scripts/vault-check.sh --lint`
   enumerates today;
2. the verdict in `scripts/vault-check.sh`, with a selftest case in each direction;
3. no schema change at all — both the key and the value are already declared.

**Step 1 before step 2 is not a preference.** Landing the verdict first reddens every page in the
folder and a red gate locks the librarian out of the fill
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

# Consequence of not building it

**A proposal's maturity and its authorisation stay two facts a reader has to join by hand**, and no
page in the folder carries a `status: idea` today — so the value that was minted for this remains
unused ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

# Built 2026-08-24, narrowed, and one claim on this page did not survive the build

**It lives in rule 5c of `scripts/vault-check.sh` and not in a rule of its own**, because 5c had
already resolved the `decided_by:` wikilink and opened the page it names
([[a-verdict-reads-every-field-it-needs-in-the-pass-that-already-opened-the-page]]).

**It is narrowed on the owner's ruling**: a page is red when it carries `status: idea` **and** names
a cause whose `binding:` is not `deferral`
([[the-idea-and-decided-by-verdict-is-built-narrowed-to-a-non-deferral-cause]]). The objection this
page records is therefore answered rather than overruled — a half-thought produced by a deferral
keeps its `idea`.

**Two selftest cases, one each way, each proved able to fail before it was believed**
([[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]]). The fixture plants both
pages and registers both slugs in the authority register, which no other planter in that file has
ever had to do ([[a-fixture-owns-every-end-of-what-it-asserts]]).

**It fires on nothing in this corpus by construction**, since the back-fill sets `idea` exactly where
no decision exists ([[a-proposal-keeps-an-absent-decided-by-rather-than-a-false-idea-mark]]).

## The claim that did not survive

**This page argued that the two readings of the pair redden different pages.** No page could be
built on which they diverge: both fire on the same intersection and differ only in the wording of
the message. **The sentence is left standing above rather than struck**, because it is what the
build was steered by, and the correction is dated here.

## Placement

**It carries `status: implemented` and stays in `wiki/proposals/`**, which is where a page waits
while it is tested for having someone who points at it
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]). The move is a
script's at the lint stage, and that script does not exist
([[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]],
[[divergence-an-implemented-proposal-stays-in-the-proposals-folder-because-nothing-moves-it]]).
