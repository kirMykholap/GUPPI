---
title: "Whether a non-rule page may carry `authority:` and render is unruled, and the gate is narrow on purpose so it stays a question"
type: concept
status: deprecated
authority: authority-beside-governs
basis: inference
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh"]
superseded_by: [[authority-beside-governs-is-forbidden-on-any-page]]
tags: [record-schema, harness, vault]
---

# The shape nothing rules on

**`authority:` is forbidden beside `governs:` on a page in `wiki/rules/`.** The reason is
rule-specific: a decision and the rule stating it share a slug, so a rule claiming an `authority:`
would read as a contradiction against the decision it renders
([[rules-becomes-a-type-of-its-own]], [[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

**Since `e83ce28`, a page in any folder may carry `governs:`**
([[governs-becomes-a-property-of-any-page]]). A `concepts/` page that renders *and* owns a question
is now expressible, and **nothing in the schema, the check or this vault says whether it is legal.**

**The `ruleclaim` gate was left rules-only on purpose** rather than widened with the branch beside
it ([[the-governs-branch-widens-and-the-others-stay-rules-only]]). Widening it would have answered
the question by accident from inside a script; leaving it narrow keeps the question askable.

## Why this page exists at all

**Until now the question was neither open nor closed — it was invisible.** No page named it, so it
could not be raised, deferred or decided; the only way to meet it was to write such a page and
notice that nothing objected. That is the same failure class the vault has recorded from the other
side — a field that is legal, spelled correctly, and does nothing, with nothing distinguishing it
from one that works ([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]).

**The first non-rule page to render answered it in the safest direction and said so**: it carries no
`authority:`, deliberately, because claiming one would have settled the question by accident from
the other side ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]).

## The two answers available, and what each costs

| If it is allowed | If it is refused |
|---|---|
| a renderable page can also be the sole answer to a question, and the duplicate-`authority:` check has to tolerate the decision-and-record pair the way it does not for rules | a page must choose between owning a question and delivering text, which splits some records in two and makes the second page exist only to render |

**Neither is obviously right and this page does not pick.** It is `basis: inference` and it is a
question for the owner, which is what a vault page is before it is a settled fact
([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).
