---
title: "Body sections are declared in every schema and filled only where they are written"
type: decision
status: archived
authority: page-body-sections
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: date-scope-the-decision-fields
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/decisions/_schema.yaml", "wiki/proposals/_schema.yaml", "scripts/vault-check.sh"]
tags: [vault, record-schema, process]
---

# Context

**A page's frontmatter was checked and its body was not.** `scripts/vault-check.sh:292` records that
a wiki page's body is read for exactly one thing — whether it marks a slice to ship. So two decision
pages could answer entirely different questions and both pass.

**The mechanism already had a working precedent.** Rule 8 of the same script enforces that a journal
carries every section of the template it was written from, so a required-section check over page
bodies needs **no new mechanism class** — one helper, two callers.

# The question

**Do body sections become a schema block, in how many folders, and filled for which?**

# How it works after

**The `sections:` block lands in all six `_schema.yaml` files**, so the mechanism is described once
and everywhere.

**The sections themselves are written for `wiki/decisions/`** — five headings, the owner's own, in
this order and with these jobs:

| heading | what it holds |
|---|---|
| `Context` | what the thing is, how it works today, what pages and modules it touches |
| `The question` | the problem, or the fork between options |
| `How it works after` | the condition the decision is discharged by, naming the target |
| `Recommendation` | the session's, with its ground |
| `Ratification` | who decided, in whose words, against what |

**And for `wiki/proposals/`** — one heading, `Decisions`, identical on every proposal because
`scripts/vault-archive.sh` reads that list to decide what a refused proposal takes with it.

**The other four folders carry the block empty**, not filled. That was one of the five forks the
session resolved without asking; the plan said declared-and-empty for all, and the proposals extension
was named to the owner rather than let pass.

**Rule 16 compares the SET, never the sequence, and reads `# ` and not `## `** — 900 first-level
headings against 395 second-level ones across `decisions/`. **The verdict is scoped by a date** and
reddens only a page whose `created:` is on or after it
([[the-decision-lifecycle-fields-are-scoped-by-a-date-rather-than-back-filled]]).

**The fifth section is what the old rule had not got.**
[[every-question-to-the-owner-carries-its-context]] obliged four of these five and no more, which is
why it is superseded rather than amended
([[the-reply-format-becomes-a-rule-and-the-context-rule-is-absorbed-whole]]).

# Recommendation

**Declare the mechanism everywhere and fill it in one place**, so that filling a second folder later
is a list rather than a design.

# Ratification

**The owner said it**, twice. For the shape: «Мы описываем механизм для всех старниц, но сами разделы
прописываем сейчас только для decisions. Будем делать все постепенно, иначе я запутаюсь». For the
case as put: «Case 1 : принимаю в таком виде».

**And he selected the extension to `proposals/`** when the session named it rather than letting it
pass silently: «супер, принимается».

**Built on 2026-08-30**, in the six schemas and in rule 16 of `scripts/vault-check.sh`.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
