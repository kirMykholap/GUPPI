---
title: "A declaration that silences a check must expire or be re-derived, because what it silences is what would have found it wrong"
type: concept
status: current
authority: silencing-declaration
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "job_hunt_ai_vault/CLAUDE.md"]
tags: [record-schema, harness, vault]
---

# The mechanism

**A field that answers a verdict does not answer it once. It answers it forever, on every run, on a
page nobody re-reads.** The verdict is the instrument that would notice the page drifting; the
declaration switches that instrument off for that page; so the one thing that could catch the
declaration going stale is the thing the declaration disables. **The check cannot catch it by
construction**, and no amount of tightening the check changes that.

This is the mechanism behind the withdrawal of `quantity:`
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), and it is **stronger than the
tidiness argument made at the time** — which was that a corpus with an escape hatch is untidy and
that the hatch outlives the rule it softens
([[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]]). The tidiness
argument is about the store's shape. This one is about the store being wrong and saying nothing.

# The measurement, taken while the field was being removed

**Two of the twenty-four `quantity:` declarations were already false while they stood**, and both
were found only because a human-scale reader was retitling their pages by hand.

| page | what the declaration said | what the body did |
|---|---|---|
| [[fidelity-to-a-source-and-fidelity-to-the-tree]] | *"a third would make the page wrong rather than stale"* | a section headed *"A third kind, proved on 2026-08-17: fidelity of a move"* had been added to that very page while the declaration sat in its frontmatter — the title read *two different properties* over a body describing three |
| [[journal-vault-brief-each-artefact-has-one-owner]] | *"the artefacts counted are named in the title itself"* | the page names a fourth artefact with a fourth owner in its own body |

**Neither was found by anything mechanical, and neither could have been.** That is not a gap in
rule 10; it is the property of the shape.

# The general rule this leaves

**A declaration that silences a check must expire or be re-derived.** Three forms satisfy it, and any
of them is better than the fourth:

- **no declaration at all** — the rule is unconditional and a flagged page is repaired. This is what
  the vault chose ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]);
- **a declaration with an expiry** — it silences the verdict until a date, after which the page
  reddens and someone re-reads it;
- **a declaration that is re-derived** — the check recomputes the exemption's premise rather than
  trusting a stored answer, which is what an exemption *inside* a predicate does. Rule 10's exempt
  words are of this kind: `one` and `first` were measured across every title using them, not declared
  ([[ordinals-count-and-first-does-not]]);
- **a permanent, stored, per-page declaration** — the shape this page is against.

# What it costs to remove one, and why that is not an argument for keeping it

**Withdrawing the hatch converted a false positive from a line of frontmatter into a rewrite of
correct prose.** That is a real price and it is why rule 10's word list is short and why every word in
it is a promise ([[ordinals-count-and-first-does-not]]). The price is paid **once, by whoever writes
the page, in front of a reader**. The declaration's price is paid **silently, forever, by a reader
who trusts a title**.

# Where else this shape is admitted

**Any `skip:` verdict, any waiver, any per-item suppression is the same shape.** The store already
carries one on purpose — the `skip:<reason>` verdict of an ingest sidecar — and it survives scrutiny
for a reason worth naming: it is **not stored against a live page**. A sidecar is written once,
against an immutable source in `raw/`, and the source cannot drift under it
([[raw-holds-testimony-and-artefacts-are-frozen]]). A declaration on a live page has no such
guarantee, and that is the whole difference.
