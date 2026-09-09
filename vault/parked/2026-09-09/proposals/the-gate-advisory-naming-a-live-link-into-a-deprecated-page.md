---
title: "The gate advisory naming a live link into a deprecated page"
type: proposal
status: implemented
authority: deprecated-link-advisory-design
basis: human
sprint: S3
created: 2026-08-28
decided_by: [[the-gate-advisory-on-a-live-link-into-a-deprecated-page-is-ordered-built]]
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "scripts/vault-check.sh", "archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md"]
tags: [vault, harness, retrieval]
---

> [!NOTE] BUILT 2026-08-29, AND ITS KEY CHANGED ON THE WAY
> It lives behind `--lint` and prints one line per dead target
> ([[the-deprecated-link-advisory-prints-one-line-per-dead-target]]). **The phrasing below — keyed on
> the target's `status:` — was not what shipped.** It keys on the literal value `deprecated`, because
> the sweep of the same day put about 240 `status: archived` pages into `archive/` and a
> status-in-general verdict would have grown from 43 lines to hundreds
> ([[the-deprecated-link-advisory-keys-on-the-literal-value-and-not-on-the-targets-status]]). The design
> below is kept as written; `implemented` opens a state rather than naming a place, so this page stays
> in `wiki/` while it is tested for a live page pointing at it.

# What it would be

**A verdict in `scripts/vault-check.sh` keyed on the target's `status:`** — a live page under
`wiki/` links a slug whose page carries `status: deprecated` — **printing an advisory line and never
a red.**

**It classifies nothing about the citation.** A vocabulary-keyed test inverts on the
retirement-policy pages, which discuss deprecation for the opposite reason; what kind of citation it
is, is the reading agent's work
([[the-decisions-agent-reads-only-and-runs-at-every-ingest]]).

# What it would report today

**42 deprecated slugs, 424 link occurrences, 332 distinct page-target pairs, 210 distinct live
pages**, measured over the whole of `wiki/` on 2026-08-28.

**That is more advisory lines than any existing verdict prints**, and the shape of the output is the
first open question: one line per edge is 424 lines, one line per target is 42, one line per page is
210. The house form is one line per name, sorted
([[an-advisory-prints-one-line-and-sorts-what-it-names]],
[[the-filename-advisory-prints-one-name-per-line]]).

# What is open

**The output form**, above.

**Whether it reads `decided_by:` differently from a body link.** A `decided_by:` pointing into
`archive/` is already a decided case — kept as it stands and a lesson candidate — so the advisory
either exempts it or reports it as a distinct kind
([[a-decided-by-target-in-the-archive-is-kept-and-becomes-a-lesson-candidate]]).

**Its cost.** The gate's shared pass over the corpus already dominates its runtime, and this verdict
needs the target page's frontmatter, not just its existence
([[the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to]],
[[a-verdict-reads-every-field-it-needs-in-the-pass-that-already-opened-the-page]]).

# What it does not do

**It does not make the citation illegal.** A live page arguing from a deprecated one stays legal;
the advisory names it so a reader can decide ([[a-live-page-can-argue-from-a-deprecated-one]]).
