---
title: "Marked regions, their verdicts, and the layers over the prose that stays outside them"
type: proposal
status: current
authority: unregioned-prose-layers
basis: human
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "scripts/vault-check.sh"]
decided_by: [[what-the-harness-build-waits-on]]
tags: [harness, testing]
---

# The form, designed 2026-08-16, and no file carries one

**A paired HTML comment named for the rule's slug, alone on its line at column zero, no nesting and
no overlap.** The file owns the skeleton; the pages own the text
([[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]).

**A marker inside a fenced block does not count.** The check's existing fence-stripping pass is
reused for this, and **its two recorded scars are exactly this error**: prose inside a `<script>`
block satisfying an id search for a slice and a half, and a fenced example link read as a real one
([[an-example-inside-a-code-block-satisfies-a-search]], [[vault-scripts]]).

## Four verdicts

| the situation | the verdict |
|---|---|
| a region with no page behind it | **red** |
| a `render: region` rule with no region to render into | **red** |
| two rules rendering into one region | **red** |
| text outside every region | **allowed, and unchecked** |

**The fourth is the real hole**, and it is where every recorded staleness has lived: an assertion in
hand-written prose that no page carries ([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

## Three layers over the prose outside regions

1. **The regions themselves**, as far as the markup has got.
2. **A grep for imperative words outside them**, as a cheap approximation. This is the check the
  vault already proposed ([[claude-md-may-point-and-may-not-assert]]), and it was measured:
  **103 hits across ten files** — a list one can work through rather than a fog.
3. **The semantic pass of `/vault-lint`, once per sprint** ([[lint-waits-for-an-open-sprint]]).

**Plus a coverage number per file in the gate's output**, which turns an invisible hole into a
number that shrinks as markup proceeds — the same move that made the ingest's completeness
mechanical rather than a claim ([[ingest-is-units-and-verdicts]]).

## What is open

- **Which files may be exempt from *a `render: region` rule with no region is red*.** One of the
  three items blocking construction ([[what-the-harness-build-waits-on]]).
- **Which regions exist in which files.** The markup is gradual and starts with
  `.claude/skills/ingest/SKILL.md` and the repository's `CLAUDE.md` — both already carry a recorded
  divergence ([[no-rule-reads-a-harness-file]]). Marking everything up front costs the same as
  reading the corpus by eye, which this project has already refused.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

## The measured case for this design, 2026-08-17

**The handoff mapping had been copied into six files, and the copies were found only because they
happened to share a distinctive string.** Dropping the section numbers forced a sweep, and
`section 7` turned up in `.claude/skills/ingest/SKILL.md`, `.claude/skills/handoff/SKILL.md`,
`.claude/skills/vault-ask/SKILL.md`, `.claude/agents/vault-librarian/AGENT.md`, the repository's own
`CLAUDE.md`, and the handoff template itself.

**None of them was wrong when written.** They drifted because the thing they copied changed under
them — which is the failure this design exists to make impossible.

**The load-bearing detail is how they were found: by grepping for a number.** A renamed heading
would not have been findable that way, and neither would a reworded rule. Six copies, no detector,
and one lucky string is the strongest evidence this proposal has
([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]], [[no-rule-reads-a-harness-file]]).

# Built on 2026-08-17, and the verdict table above is wrong in two rows

**Everything above is the design as it stood on 2026-08-16 and is kept verbatim.** The mechanism
now exists — rule 11, rule 12 and `scripts/vault-inject.sh` — and two of the four verdicts as
written cannot be evaluated against anything.

**The defect: rows two and three name `render: region`, a field that was never introduced**
([[render-was-not-introduced]]). Only the region mode is built, so a mode field would have one
legal value and no writer. Anyone reading the table above as a specification builds something
uncheckable.

## The verdicts as built

| the situation | the verdict |
|---|---|
| a region whose `wiki/rules/<slug>.md` does not exist | **red** |
| a **current rule page** with no `<!-- text -->` slice | **red** |
| one slug marking two regions in one file | **red** |
| two current rules carrying the same `governs:` | **red**, caught in the frontmatter pass |
| a **governed file** carrying no region at all | **advisory**, one line — [[a-governed-file-with-no-region-is-an-advisory]] |
| text outside every region | **allowed, and unchecked** |

The predicate moved from *a rule with no region* to *a region with no rule*, plus a uniqueness
check on `governs:`. That is the same intent read from the side that can actually be evaluated: the
tree is swept for regions and the frontmatter is already in hand, while "a rule that ought to have a
region somewhere" needs the fifth verdict to be answerable at all
([[a-region-is-checked-against-its-rules-governs]]).

**The fourth row still stands as written, and is still the real hole**: text outside every region
is allowed and unchecked, and `0 of 13` governed files carry a region, so today that is all of it.

## What else changed under the design

- **The governed set is swept, not listed**, and `settings.json` and the `.ps1` hooks are outside
  it by a property rather than by an exemption
  ([[the-governed-set-is-swept-and-markdown-by-property]]).
- **What travels is a marked slice of the page, not its body**
  ([[what-travels-from-a-rule-page-is-a-marked-slice]]).
- **The coverage number per file** that this page asked for exists, as one advisory line over a
  swept denominator ([[an-advisory-prints-one-line-and-sorts-what-it-names]],
  [[a-denominator-is-walked-off-the-input-list]]).
- The three layers over the prose outside regions are unchanged, and layer 2 — the imperative-word
  grep, measured at 103 hits across ten files — is still unbuilt.

**This page stays `current`** because its subject is not finished: no file is marked up, the
`whole` mode does not exist, and the fifth verdict is not written. **It needs rewriting rather than
retiring**, and this section is the correction rather than the rewrite.

## The uniqueness row of the verdicts-as-built table is contested, 2026-08-17

*"two current rules carrying the same `governs:` → red, caught in the frontmatter pass"* fires the
moment a second rule of the repository's `CLAUDE.md` becomes a page — which happened on the day
after that row was written. The injector renders four rules into that one file and reports no
problem; the check refuses the same corpus. Marked as a contradiction on
[[a-deprecated-rule-does-not-render]] and [[rules-becomes-a-type-of-its-own]], where the
measurement is, and not resolved here.

> [!NOTE] RESOLVED BY THE OWNER, 2026-08-17
> **The uniqueness went out of the check, and the migration stands.** At `e478c19` the owner removed
> `governs:` uniqueness from `scripts/vault-check.sh`, on the first day it met a real tree: it was
> stricter than the schema it guarded, which says a rule names the one destination *its own* text
> goes to and says nothing about a destination taking one rule. What it appeared to protect is held
> by verdicts that read the tree instead — one slug marking two regions in one file, and a region
> sitting in a file its rule does not govern — and its selftest case **flipped rather than
> disappearing**: two rules on one file with two regions is now asserted green. The gate no longer
> prints that line. The block above is left standing as the record of the alarm that produced the
> decision, which is the point of marking rather than choosing
> ([[ask-before-weakening-or-working-around-a-rule]]).

# Weighed for retirement on 2026-08-17 and kept `current`, with the reason

**The verdicts-as-built table above has lost a row.** *"Two current rules carrying the same `governs:`
→ red"* is gone from `scripts/vault-check.sh`: the owner removed it at `e478c19` because it was
stricter than the schema it guarded, and the resolution block above records that. **The remaining
verdicts gained one** — a region is now checked against its rule's `governs:`, and it lands in rule 11
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

**Two of the three reasons this page gave for staying `current` have gone.** It said: *no file is
marked up, the `whole` mode does not exist, and the fifth verdict is not written.* The first file is
marked up — nine regions in the repository's `CLAUDE.md`
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]) — and the fifth verdict exists.

**It is kept `current` anyway, and the librarian's reasoning is on the record rather than assumed:**

- **The fourth row is still the real hole and is still open.** *Text outside every region is allowed
  and unchecked* — and region coverage is **`1 of 13`**, so today that is twelve files whole plus two
  blocks of the thirteenth ([[the-repository-claude-md-after-the-rules-left-it]]).
- **Layer 2 lives only here.** The imperative-word grep outside regions, **measured at 103 hits across
  ten files**, is unbuilt and is described on no other page.
- **Retiring it would need a successor that duplicates a concept page** rather than replacing this one:
  the verdicts as built are on [[a-region-is-a-paired-comment-named-for-a-rule]], which is not a
  proposal and does not answer *what did we design and never build*.

**Whether that reading is right is the owner's call, and it is raised in the brief rather than settled
here.** The alternative — retire it as built, and move layer 2 to a proposal of its own — is available
and was not taken, because it would split one design across two pages to make a status field tidier.

## The owner read it and it stays `current`, 2026-08-18

**owner: keep.** Nothing had changed since the last weighing, and the layer-2 measurement is still
on no other page. The verdict is separate from the two proposals retired the same day, and it is
what the retirement policy's test was derived from: **a built proposal retires once nothing on it
lives only there** ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

**The fourth row is still the hole, and it grew a demonstration.** *Text outside every region is
allowed and unchecked* — and on 2026-08-18 the region mechanism's own first use outside
`wiki/rules/` put a rendered claim five lines below the same claim in hand-written prose
([[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]],
[[the-maps-region-replaces-the-prose-it-duplicated]]). Layer 2 is what would have caught it, and
layer 2 is what is unbuilt.

**The `1 of 13` above is dated 2026-08-17 and is not patched here**
([[the-region-coverage-figure-is-dated-where-it-stands]]).

## The agent path in the list above is left as written — noted 2026-08-20

**`.claude/agents/vault-librarian/AGENT.md` moved back to `.claude/agents/vault-librarian.md`**, and
this page is **not** repointed. The list records where a sweep found `section 7` on 2026-08-17 — a
claim about a past reading, not about the tree ([[fidelity-to-a-source-and-fidelity-to-the-tree]],
[[a-path-detector-for-prose-references]]).
