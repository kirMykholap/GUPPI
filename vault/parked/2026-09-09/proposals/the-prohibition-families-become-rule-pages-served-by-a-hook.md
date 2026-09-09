---
title: "The prohibition families become rule pages served by a hook, and the sweep that empties `wiki/decisions/`"
type: proposal
status: current
authority: prohibition-family-rule
basis: human
sprint: S3
created: 2026-08-30
decided_by: [[a-prohibition-family-becomes-one-rule-page-served-by-a-hook]]
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/authority.md", "docs/vault-cleanup-families.md", "scripts/vault-authority.sh"]
tags: [vault, harness, process]
---

# Decisions

**One line per decision this proposal must close before it can be implemented.** A ticked box records
that the owner has **ratified** the answer, never that it is built; an unanswered line carries no link
at all.

- [x] [[a-prohibition-family-becomes-one-rule-page-served-by-a-hook]] — the mechanism itself, and it
  is this proposal's cause.
- [x] [[the-cleanup-suspends-the-rules-that-would-refuse-it]] — the four rules that would refuse the
  sweep are lifted.
- [x] [[authority-uniqueness-becomes-a-per-type-question]] — a rule and the decision behind it may
  share a slug, which is what lets a family rule inherit one.
- [x] [[the-rule-about-rules-is-served-by-the-hook-and-not-rendered-into-claude-md]] — the
  conditional-delivery gate is satisfied by this decision, and it is written before any rule page.
- [x] [[the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages]] — the ordering that keeps
  the gate green while the pages land.
- [x] [[proposals-and-lessons-are-not-touched-by-the-cleanup]] — the scope, so the sweep does not walk
  two folders the owner took out.
- [x] [[the-retro-list-is-worked-by-the-session-with-items-carved-out-for-the-owner]] — how the 99
  verdicts reach him: the session works the list and carves out what only he can answer.
- [x] [[the-cleanup-verdict-names-which-delivery-a-family-gets]] — the verdict names a delivery,
  the session sets them, and he ratifies the block. **This closes the unticked line below it**, which
  said the verdicts were none of them given: 53 were set and ratified on 2026-08-31 as
  `docs/vault-cleanup-verdicts.md`.
- [x] [[only-the-vault-facing-families-are-built-and-the-harness-facing-kind-waits]] — only the first kind is
  built; the harness-facing families are a discussion of their own.
- [x] [[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]] — the hook resolves
  nothing, and `authority.md` never becomes a runtime dependency.
- [x] [[the-family-rules-are-drafted-by-a-generator-inside-the-librarians-dispatch]] — a generator
  drafts the pages and it runs inside the librarian's dispatch, because both orders redden the gate.
- [x] [[the-slug-converges-by-hand-along-the-chain-of-types]] — the delivery's coverage comes from a
  manual convergence rather than from anything the hook does.
- [ ] **Which of the 53 families becomes a rule, and which are dead.** Ninety-nine verdicts in
  `docs/vault-cleanup-families.md`, none of them given. *(Answered 2026-08-31 by the first line above;
  the wording is left as written because the count and the two-valued framing are both part of what
  changed.)*
- [ ] **Whether the concept/entity taxonomy replaces the noun-and-mechanism folder test or stands
  beside it.** The sweep of 187 pages walks by whichever answer he gives, and both are live
  ([[concepts-are-non-functional-requirements-and-entities-are-functional]]).
- [ ] **Whether the one-line register exception reaches fifty-three lines**, or whether the librarian
  writes all of them ([[the-session-writes-one-authority-row-and-the-one-writer-clause-stands]]).

# What would be built

**Fifty-three pages in `wiki/rules/`, one per prohibition family, each carrying the family's
`authority:` slug under `render: authority`, no `governs:` and no marked slice.** Each holds one
clause per member of its family — the member's title, which rule 10 has already made a complete claim
— plus a link to the decision that clause came from
([[a-family-rules-clauses-are-drafted-from-titles-because-a-title-names-its-claim]]).

**Fifty-three rows in `authority.md`, written in the same pass**, or the gate is red between the two
acts and the party permitted to close it cannot be dispatched
([[the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages]]).

**A sweep that moves the discharged decisions into `archive/`**, each keeping its slug and its row.

**The rule about rules**, born with the families: a page under `render: authority` describing the
mechanism itself, delivered by the same hook on a read or write inside `wiki/rules/` and rendered into
no file ([[the-rule-about-rules-is-served-by-the-hook-and-not-rendered-into-claude-md]]).

# What it stands on, and none of it exists yet

**Ninety-nine verdicts the owner writes into `docs/vault-cleanup-families.md`** — 53 for the
prohibition families and 46 for the concept/entity groups. The file is generated, its verdict columns
are empty, and **nothing downstream can start without them**. That is why the sweep moved to the next
session rather than being attempted on 2026-08-30.

**A delivery for `render: authority`.** `.claude/hooks/serve-the-rule.ps1` has no `authority:` matching
branch, and its path silence excludes every file under `wiki/` — so the rules this proposal writes
would be served to nobody as the hook stands
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).

**A decision page before any rule moves to conditional delivery**, which the gate on that transition
demands with a rejected alternative named
([[a-rule-moving-to-conditional-delivery-needs-its-page-first]],
[[the-conditional-delivery-gate-covers-any-departure-from-unconditional-delivery]]). The rule about
rules is the page that has to be written first, not after.

# What it would take

**One pass over 320 titles and their slugs — about 72 KB, eighteen thousand tokens, no page opened.**
That is the drafting half and it is cheap.

**The judgement half is the 99 verdicts and it is not the librarian's.** A family may become one rule,
several, or none; a dead family is a finding the pass is designed to surface.

**The estimate the owner's design was priced on, and it is an upper bound**: `rules/` goes 17 → up to
70 pages, `decisions/` goes 321 → about ten, and the corpus loses roughly 250 pages. It assumes every
one of the 53 families produces a rule, which the dead-family verdict is precisely what does not
assume.

# What is open

**Whether a family is the right unit of judgement.** The measurement says a grouping exists and costs
one pass to read; it does not say the grouping is correct.

**What happens to `binding: deferral`.** Thirty-six pages stay in `wiki/decisions/` and are worked in
their own session ([[a-decisions-archival-condition-is-read-off-its-binding]]). None of them is named
in any live `decided_by:`, and nothing records what a deferral's term is, so no existing route retires
one.

**Whether `/pre-task` phase 1 survives an empty `decisions/`, and whether the catalogue goes with
it.** The owner raised it and nothing decides it.

# What it obliges

**The eleven rules that render into the repository's `CLAUDE.md` stay rendered.** They have to be
known before any write happens, and a delivery triggered by touching a file arrives too late for them.

**Every clause keeps a link to its decision**, and the decision keeps its slug and its `authority.md`
row in `archive/`, so the ground under a clause stays reachable after the sweep
([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]).

**Nothing here may move the one-writer clause.** The 53 rows are the librarian's to write; the
exception granted on 2026-08-30 was for one line and is not a licence for fifty-three
([[the-session-writes-one-authority-row-and-the-one-writer-clause-stands]]).

# Half of this was built on 2026-08-31, and the scope above is what changed

**This page stays `current` and is not implemented.** What it describes as one build is two, and only
the first ran.

**What the page says, and what happened.** It sizes the work at **53 rule pages**, `rules/` going from
17 to "up to 70" and `decisions/` falling to "about ten". **Nineteen pages were written; `wiki/rules/`
stands at 36 and `wiki/decisions/` at 211.** Those sentences are left as written and are false as
estimates of the whole, because the whole is no longer one act
([[only-the-vault-facing-families-are-built-and-the-harness-facing-kind-waits]]).

**The split the page does not contain.** A **vault-facing** family becomes a `render: authority` page
whose clauses a script assembles from titles; a **harness-facing** family needs `governs:` and a written
region, which is prose. Eighteen of the families are the first kind and **35 are the second**, holding
164 prohibitions that stay exactly where they are.

**The measured result of the half that ran.** `wiki/` 630 → **520**; `decisions/` 340 → **211**;
`rules/` 17 → **36**; `binding: prohibition` 295 → **166**; `bash scripts/vault-catalogue.sh | wc -c`
139,210 → **112,690**, which is 44 % off the 201,927 the catalogue stood at before the cleanup began.
**Both halves of the promise moved for the first time** — the tokens and the pages
([[the-purpose-of-archiving-is-a-cheaper-working-wiki-and-archive-is-a-warehouse]]).

**And two things this page opened are now decided elsewhere.** The verdicts are three-valued and set by
the session; and *"whether `/pre-task` phase 1 survives an empty `decisions/`"* is ruled a `vault-ask`
topic rather than cleanup work ([[pre-task-reads-too-much-and-the-rework-belongs-to-vault-ask]]).

**What still stands unbuilt, which is what keeps this page in `wiki/proposals/`:** the 35 harness-facing
families, their 164 prohibitions, and the shape of a second-kind family rule — which lands on
[[what-travels-from-a-rule-page-is-a-marked-slice]], a rule that is narrowed for the first kind and
unnarrowed for this one.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, and extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
