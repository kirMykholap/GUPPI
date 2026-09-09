---
title: "A schema per type would say what a record asserts and what expires it"
type: proposal
status: current
authority: per-type-assertion-schema
basis: human
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", "CLAUDE.md"]
decided_by: [[the-wide-half-of-the-per-type-schema-is-a-conversation-not-a-task]]
tags: [vault, retrieval]
---

# The defect it answers: two records mis-filed, found 2026-08-16

- **[[lint-waits-for-an-open-sprint]]** is typed `decision` while its title asserts a **state** —
  "has never run".
- **[[app-restart-required]]** is typed `entity` while its `authority: restart-to-see-changes` is
  an **obligation**.

Both are the same defect, and neither is a mistake by whoever filed them: **nothing in the schema
says what a record of each type asserts, and what expires it.** The vault's `CLAUDE.md` carries one
page schema for every type — the same frontmatter, the same fields — plus four sentences about
choosing a category. `vault-check.sh` rule 4 checks that the folder and `type:` agree, which is a
check on where the file sits and not on what it claims.

**Nothing here is decided.** The owner named the fix; nobody has written one.

## What it would be

A schema, or a template, per type — saying at least:

| | what a record of this type asserts | what expires it |
|---|---|---|
| `decision` | a choice, with a date and a rejected alternative | the choice being reversed |
| `entity` | what a thing is and what it is like | the thing changing or going out of service |
| `concept` | a mechanism and its consequences | the mechanism being replaced |
| `lesson` | a failure class and what it cost | nothing — a lesson is testimony about a date |
| `proposal` | what we would build and what it would take | being built, or refused |

The rows above are the shape, not the content: filling them in is the work, and the title rule
already decided one of the fields ([[the-titles-form-follows-the-records-type]] — an entity is a
noun phrase, a decision states its claim).

## The trap to design around, named by the owner

**A template that nothing tests becomes the next stale `CLAUDE.md.`** This store has four recorded
instances of a claim living only in a rule file and going stale with nothing noticing
([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]), and a per-type template is exactly
that shape of artefact.

**So each template must be a real page that the selftest runs through `vault-check.sh`** — a
fixture, not a description. That is affordable: the selftest already plants pages and asserts what
the check says about them, and the cost of adding a rule over every page is known
([[a-rule-over-every-page-makes-every-test-fragile]], [[vault-scripts]]).

## What is open

- **Whether the two mis-filed records above are then re-typed**, which is supersession and the
  owner's ([[the-audits-findings-are-owed-to-the-owner]]).
- **Whether `rules` is one of the types this schema covers** — it is decided and unbuilt
  ([[rules-becomes-a-type-of-its-own]]), and designing the schema before the type exists means
  designing it twice or once too early.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

## Half of it was settled on 2026-08-16, field by field rather than type by type

The second session of that day worked the same problem from the field end instead of the type end,
and the results are decisions rather than proposals:

- **the admission test** a field has to pass —
  [[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]];
- **the core, and `updated` joining it** —
  [[the-frontmatter-core-is-fixed-and-updated-joins-it]], which also lists the three checks the
  schema now owes and the per-type additions (`decided`, `supersedes` and its unchecked symmetry);
- **`rules` gets `governs:` and optional `asserts:`**, and carries no `authority:`
  ([[rules-becomes-a-type-of-its-own]]);
- **`entities` gains the application**, sequenced behind the detector that would keep it honest
  ([[entities-describe-the-application-once-the-detector-exists]]).

**What is still missing is exactly what this page asked for**: the *what a record of this type
asserts / what expires it* table, filled in, as a real page the selftest runs through
`vault-check.sh`. A field list is not that table, and the owner's trap — a template nothing tests
becomes the next stale `CLAUDE.md` — is unaddressed.

**One open question of this page is now answered and a new defect belongs on the list.** `rules` is
a **sixth folder**, so the schema has to cover it; and `proposals` cannot express *built* against
*refused*, which is recorded and deliberately not fixed
([[the-proposal-status-cannot-tell-built-from-refused]]).

# The field half was built on 2026-08-19; the wide half is what this proposal still carries

**Built:** each `wiki/` folder carries a `_schema.yaml` naming the frontmatter keys a page there must
and may hold, and `vault-check.sh` reads it rather than carrying a list
([[the-per-folder-frontmatter-schema]], [[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]).
That closes the *what fields* half, and it closes it as a gate rather than as a template.

**Not built, and it is the half this page was written for:** **what a record of each type asserts, and
what expires it.** Both defects named at the top — a `decision` whose title asserts a state, an
`entity` whose `authority:` is an obligation — are still unaddressed by anything mechanical, because
neither is a question about which keys are present.

**The owner ruled on the sequencing rather than on the design**: the wide half is a conversation about
each type, not a task ([[the-wide-half-of-the-per-type-schema-is-a-conversation-not-a-task]]). **This
proposal stays `current`**, because what it designs is unbuilt — the field half arriving does not
retire it ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
