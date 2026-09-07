---
title: "A rule differs from a prohibition by having an address, and by nothing else"
type: concept
status: current
authority: rule-versus-prohibition
basis: inference
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/CLAUDE.md", "job_hunt_ai_vault/wiki/rules/_schema.yaml"]
tags: [vault, harness, record-schema]
---

# The question nothing answered

**`wiki/decisions/` holds 283 pages carrying `binding: prohibition` and `wiki/rules/` holds
seventeen.** Both say what may not be done. Asked what separates them, this store had no page — and
the question only surfaced when the owner proposed converting the whole population at once.

# The answer, read off the folder set

**A rule names a destination and a prohibition does not.** That is the entire difference in the
mechanism: `governs:` — or, from 2026-08-30, an `authority:` slug a hook looks up
([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]). Everything else the
two carry is the same shape.

| | a prohibition in `decisions/` | a rule in `wiki/rules/` |
|---|---|---|
| what it says | what may not be done | what may not be done |
| how a reader meets it | by going and looking — `/pre-task`, a grep, a brief | it is put in front of him |
| what it carries | `binding:`, `authority:`, the ground and the rejected alternative | the text that travels, plus a pointer to the decision behind it |
| what it costs to reach | a dispatch that reads a folder | nothing; it arrives |

**So a rule is a prohibition that acquired a delivery.** The folder set already says as much — *a rule
is the only category whose text is written to be rendered somewhere else* — and
[[governs-is-a-property-of-wiki-rules-alone]] says a page that renders **is** a rule by definition.

# Why 282 prohibitions never became rules, and it was not neglect

**There was nowhere to send most of them.** Delivery meant injection into a named file, and a
prohibition about how a page is written has no file to be injected into: the subject is a page in
`wiki/`, not a harness document. Seventeen rules render into eleven files, and eleven of the
seventeen render into one — the repository's `CLAUDE.md`. **That is the complete set of addresses a
rule's text could reach before 2026-08-30.**

**The lookup mode is what supplies an address to the rest**, by making the subject rather than the
destination the key. It is the reason the conversion became thinkable at all
([[a-prohibition-family-becomes-one-rule-page-served-by-a-hook]]).

# What follows, and what this page does not decide

**A prohibition whose subject can be addressed belongs in `wiki/rules/`; one whose subject cannot
stays a decision.** That is the criterion the family sweep applies, and it is a property of the
subject rather than of the prohibition's importance.

**It does not decide whether every family should become a rule.** Some families will be dead, and
finding them is what the review table is for. And it does not decide what happens to the reasoning a
decision carries — the clause travels, the ground stays on the decision in `archive/`
([[a-family-rules-clauses-are-drafted-from-titles-because-a-title-names-its-claim]]).

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, on a question the vault was recorded as unable to answer that day.)*
