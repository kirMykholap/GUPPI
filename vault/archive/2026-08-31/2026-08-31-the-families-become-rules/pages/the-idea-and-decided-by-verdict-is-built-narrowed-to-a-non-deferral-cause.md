---
title: "The `idea` and `decided_by:` verdict is built narrowed to a cause that is not a deferral"
type: decision
status: archived
authority: idea-decided-by-narrowing
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "wiki/proposals/_schema.yaml", "scripts/vault-check.sh"]
tags: [record-schema, vault, harness]
---

# The ruling, 2026-08-24

> **owner:** «Строим, но сужаем: правило краснеет, только если decided_by: ведёт на решение,
> которое не deferral.»

**A page is red when it carries `status: idea` and names a cause whose `binding:` is not
`deferral`.** The verdict lives in rule 5c of `scripts/vault-check.sh`, which had already resolved
the `decided_by:` wikilink and opened the page it names
([[a-verdict-reads-every-field-it-needs-in-the-pass-that-already-opened-the-page]]).

# What the narrowing is against, and the objection it answers

**Rejected: both unnarrowed readings.** A deferral is a decision here and the corpus holds
twenty-four of them, so a half-thought that was deferred would be forbidden from being an `idea` at
all — which is the objection `wiki/proposals/_schema.yaml` has carried in the session's own words
since `idea` was minted ([[an-idea-is-a-proposal-with-an-immature-status]]).

**Rejected outright: the third reading**, that a proposal which is not an `idea` must carry the
field. [[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]] already forbids it: the
field is optional in `proposals/`.

**So `status:` goes on meaning maturity rather than authorisation**, which is the ruling the
narrowing protects.

# It fires on nothing in this corpus, by construction

**The back-fill sets `status: idea` only where no decision exists**, so an idea page carries no
`decided_by:` and the two halves never meet
([[a-proposal-keeps-an-absent-decided-by-rather-than-a-false-idea-mark]]).

**It is a guard against a page written tomorrow, and that is stated rather than discovered later.**

# One claim the proposal made did not survive the build

**The proposal asserted that the two readings redden different pages.** No page could be built on
which they diverge: both fire on the intersection of `status: idea` and a named cause, and they
differ only in the text of the message. That is recorded on
[[a-verdict-pairing-the-idea-status-with-a-named-decision]] rather than corrected there.
