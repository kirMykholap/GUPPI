---
title: "Field-driven injection: `governs:` read as a field, `[type]:` in the marker, and the verdicts that come with them"
type: proposal
status: deprecated
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
superseded_by: [[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]
tags: [harness, record-schema, vault]
---

# Designed 2026-08-17, agreed in full, and not built

The owner's two decisions are [[governs-becomes-a-property-of-any-page]] and
[[the-marker-carries-the-records-type]]. This is what building them takes.

## What it would take

| Part | The change |
|---|---|
| `scripts/vault-inject.sh` | glob `wiki/*/*.md` instead of `wiki/rules/*.md`, and take the destination from the `governs:` field rather than from the folder |
| `scripts/vault-check.sh` | accept `<!-- [type]: slug -->` where `[type]` is validated against the **closed six-type set**, and resolve the region to `wiki/<plural of type>/<slug>.md` |
| a new verdict | **red** — a marker whose type disagrees with its page's `type:` |
| a new verdict | **red** — a `<!-- text -->` slice on a page carrying no `governs:` (a page that marks text nothing delivers) |
| the drop of a gate | every `governs:` branch of the check currently reads `folder == "rules"` ([[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]]) |
| `scripts/vault-check-selftest.sh` | a case per verdict, and the sandbox's destination-materialisation follows the wider glob ([[a-fixture-must-materialise-what-the-subject-reads]]) |
| the existing regions | nine markers say `rule:` and have to be rewritten — a rewriter with a detector, not a substitution ([[a-rewriter-must-be-paired-with-a-detector]]) |

**The type in the marker removes a lookup rather than adding a copy**, which is the design's own argument
for itself ([[a-marker-with-its-type-is-a-complete-address]]).

## What is open

- **Whether the type word is the singular or the folder name.** `<!-- entity: x -->` against
  `wiki/entities/x.md` needs a pluralisation the check does not currently do anywhere; `<!-- entities: x -->`
  avoids it and reads worse. Nobody has decided.
- **Whether a non-rule record may render at all** was decided yes for a *sourced factual record*
  ([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]) — but the definition of
  *retrospective* is a **definition rather than an imperative**, and whether that shape may render is still
  the owner's call ([[the-end-of-a-session-is-a-retrospective]]).
- **The selftest cost.** Every new verdict is a case, and a case costs 4.9 s of check
  ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

## What not building it costs

**Three records have nowhere to live**: the project description, the definition of *retrospective*, and the
map ([[the-map-in-claude-md-and-its-admission-test]]). Each of them therefore stands as hand-written prose
in the one file this project has recorded going stale eight times
([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

**And the inert `governs:` stays inert** — neither rendered nor refused, which is a green that examined
nothing.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

# Built at `e83ce28`, and retired on 2026-08-18 by the owner

**Everything in the table above is built**, except where this page was wrong about it. The check
first ran that nothing on it lives only here
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]); where each part went:

| What it designed | Where it lives now |
|---|---|
| the wider glob and the field-driven destination | [[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]] |
| the type in the marker, and the address it completes | [[a-marker-with-its-type-is-a-complete-address]], [[the-marker-carries-the-records-type]] |
| the verdict for a slice with no `governs:` | [[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]] |
| the verdict for a marker whose type disagrees with its page | **dropped as unreachable, and replaced** ([[the-unreachable-verdict-is-dropped-and-replaced]]) |
| the drop of the `folder == "rules"` gate | **one branch of three**, not the gate ([[the-governs-branch-widens-and-the-others-stay-rules-only]]) |
| whether the type word is singular or the folder name | **closed: the singular** ([[the-marker-carries-the-records-type]]) |
| whether a definition may render | **closed: yes** ([[a-definition-may-render-into-the-repository-claude-md]]) |

**This page was wrong three times and each is recorded rather than corrected here.** It priced the
singular as needing a pluralisation the check does not do — it does, in one place; it charged the
singular for a rewrite it does not owe, since all nine live markers were already in the target
form; and it counted three gate branches with three different correct fates as one. Executing its
build table literally would have reddened the check. All three were caught at `/pre-task` and none
by reading the page ([[a-proposal-misprices-by-overcharging-one-row-and-undercharging-another]],
[[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

**Two of the three records it said had nowhere to live still have nowhere to live**: the project
description and the definition of *retrospective*. The map is built
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]); the other two are on
[[what-the-harness-build-waits-on]].
