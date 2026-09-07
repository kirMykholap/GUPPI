---
title: "A slug shared across types is the graph the `Links:` field would have cached"
type: concept
status: current
authority: cross-type-slug-as-graph
basis: code
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", ".claude/skills/vault-ask/SKILL.md", "scripts/vault-check.sh"]
tags: [retrieval, vault, record-schema]
---

# What one command now returns

```bash
grep -rl "^authority: <slug>" "$VAULT/wiki"
```

**The whole chain of one question, across types** — the proposal that raised it, the decision that
settled it, the concept or entity describing what was built, and the rule that renders or serves it.
One grep, no page opened, no field maintained.

**That is possible because uniqueness became a per-type question on 2026-08-30**
([[authority-uniqueness-becomes-a-per-type-question]]). Two pages of the same type sharing a slug is
still a contradiction and the gate says so; two of different types is legal and is how the chain is
walked.

# It is the answer to a field this store refused

**The `Links:` field was designed to cache exactly this graph and was refused the same day**
([[the-links-field-and-the-script-that-would-fill-it-are-refused]]). Both of its readers already had
the graph more cheaply:

- **the human** — Obsidian builds its graph from the `[[wikilinks]]` in the body, which the owner
  observed in his own vault;
- **an agent** — `grep -o "\[\[[^]]*\]\]" <one file>` gives a page's outgoing links and
  `grep -rl "\[\[<slug>\]\]" wiki` gives its inbound ones, neither loading the page.

**A shared slug adds the third direction those two do not have**: not *what does this page point at*
but *what else answers this question*, which is the relation a link never encoded.

# The cost, and it is why a reading verdict exists

**The gate can no longer see a decision and a concept disagreeing under one slug.** That was rule 3's
whole reach across types, and it was traded for the chain deliberately.

**What looks for it now is the `contradicts` verdict of [[the-decisions-agent]]**, which reads rather
than matches. A reading agent finds disagreements a slug comparison never could — it already found
one pair whose slugs differ — and it misses the ones it does not happen to look at. **That is a
weaker instrument on a wider field, and it is the standing justification for dispatching a reader at
every ingest.**

**Measured on the day the permission landed: zero slugs are shared across types anywhere in `wiki/`**,
so the permission has no subject yet and nothing regressed. The first pages to use it are the ones
written from here on.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
