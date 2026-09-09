---
title: "A rule page carries a family slug and the decision that caused it"
type: rule
status: current
authority: rule-about-rules-delivery
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: [".claude/hooks/serve-the-rule.ps1", "docs/vault-cleanup-verdicts.md", "authority.md"]
decided_by: [[the-rule-about-rules-is-served-by-the-hook-and-not-rendered-into-claude-md]]
tags: [vault, harness, record-schema]
---

# A rule page carries a family slug and the decision that caused it

How a page in `wiki/rules/` is written: what slug it takes, where the slug comes from, what a clause is, and what it links back to. Answers "I am about to write or extend a rule — what shape is it".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. It is the one rule about this folder that a reader gets by walking into the folder rather than by remembering it, which is the whole reason it was not rendered into the vault's `CLAUDE.md` — that file is 25,020 bytes and every dispatched agent pays for it, for a rule that concerns one folder ([[the-rule-about-rules-is-served-by-the-hook-and-not-rendered-into-claude-md]]).

# The rule text

**A rule page in `wiki/rules/` takes its `authority:` slug from the decision that caused it, and one
slug is carried by one rule page.** When a decision with `binding: prohibition` and
`target_kind: rule` is ratified, the librarian assigns it an `authority:` and then looks the slug up:
**if a rule already carries it, that rule is extended with the decision's `# The rule text` clause; if
none does, a rule page is created and inherits the slug.** Each clause names the decision it came
from. A rule delivered by lookup carries `authority:` and no `governs:`; a rule delivered by
injection carries `governs:` and no slug.

**A rule compiled from a whole family takes the slug a live page will still be carrying.** The
paragraph above describes one decision arriving; a family rule is compiled from many at once, and
the decisions it discharges all leave for `archive/`. So where a `concepts/` or `entities/` page of
the same family already carries a slug, the rule takes **that** one and the two share it from the day
it is written — which is legal because rule 3 of the gate compares slugs within a type, and is the
point rather than a loophole, because the shared slug is the address the lookup matches on. Where no
live page of the family carries one, the causing decision's slug stands and the rule is served by
nothing until the convergence is done. Owner, **2026-08-31**, refusing the alternative of teaching the
hook to resolve a slug through `authority.md`: that register is an instrument of the cleanup and a
runtime reading it would outlive the cleanup as a dependency nobody asked for
([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]]).

*Date corrected at the ingest of 2026-08-31.* This clause read **2026-08-30** when the page was written
earlier the same day. The ruling and its quotation — «Я считаю, что хук не должен искать ничего кроме
конкретного Authority» — are in the journal of **2026-08-31** and in no journal before it; both
2026-08-30 handoffs were searched and neither carries it. **An attribution to the owner carrying the
wrong day is the failure this store guards hardest**, so the wrong date is named here rather than
quietly overwritten ([[what-the-owner-said-and-what-was-put-in-his-mouth]]).

**`decided_by:` names a decision and is not obliged to name the page the slug came from.** It is
required in this folder, is exactly one `[[wikilink]]`, and must resolve to a page whose `type:` is
`decision`. On a family rule it names one member of the family; on a rule caused by a single decision
it names that decision, and the two coincide.

# What this obliges when a rule is next written

- Look the slug up first — `bash scripts/vault-authority.sh --near <slug>` — and extend the rule that
  already carries it rather than opening a second page on the same question.
- Under `render: authority` there is no `governs:`, no `paths:` and no `<!-- text -->` slice: nothing
  travels, so there is nothing to mark. The gate reads `render:` before it asks for a destination.
- A clause is a claim with the decision it came from beside it. In the family rules of 2026-08-31
  that claim is the decision's own title, because only two of the 295 prohibitions the cleanup
  surveyed carried a written `# The rule text` section of their own — and titles in this store are
  sentences precisely because the no-quantity rule made every one of them state its claim
  ([[a-family-rules-clauses-are-drafted-from-titles-because-a-title-names-its-claim]]).

# Which of the two paragraphs governs, decided at the ingest — 2026-08-31

**The rule text above states two answers and chose neither, and that was carried as a deferral.** The
first paragraph says a rule takes the slug of the decision that caused it; the second says a family
rule takes the slug a live page will still be carrying. **A reader met both and no verdict**, which is
worse than two pages, because no `CONTRADICTION` block is legal for two paragraphs of one page.

**The second governs and the first is its special case.** A rule page takes **the slug that a live page
of its family will still be carrying after the decisions leave** — and where exactly one decision
arrives and nothing else of that family exists yet, that page is the decision, which is how the first
paragraph reads today. The two are one rule stated at two widths, not two rules.

**The test, which is what a writer applies:** after the pages this rule discharges have moved, will any
live page under `wiki/` carry this slug? If yes, take that one. If no, take the causing decision's and
accept that the rule is served by nothing until the convergence reaches it
([[the-convergence-pass-over-the-live-non-decision-pages]]).

**`decided_by:` is unaffected and still names a decision**, which need not be the page the slug came
from — the paragraph below the rule text already says so, and it is what keeps the reasoning reachable
after the sweep.

# Why this page exists before the rules it describes

**The order is a gate rather than advice.** [[a-rule-moving-to-conditional-delivery-needs-its-page-first]],
widened by [[the-conditional-delivery-gate-covers-any-departure-from-unconditional-delivery]], demands
a dated decision with a rejected alternative before a rule stops arriving unconditionally. The
decision behind this page is that dated decision, and it declares this filename in its `target:`, so
the handshake rule 17 of the gate checks is what ties the two together.

**The delivery is live and its coverage is not.** The hook's `authority:` half was written on
2026-08-31 and matches exactly, resolving nothing. On the day the family rules landed, fourteen of
the nineteen shared their slug with a live `concepts/` or `entities/` page and five did not — this
page among them. A rule always matches a read of itself, which is worth nothing: the coverage that
counts is a *different* live page carrying the slug, and it grows only as the convergence is done by
hand ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).
