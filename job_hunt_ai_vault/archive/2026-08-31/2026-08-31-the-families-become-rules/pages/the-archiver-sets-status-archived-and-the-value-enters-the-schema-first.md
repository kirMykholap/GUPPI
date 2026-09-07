---
title: "The archiver sets `status: archived` mechanically, and the value enters the schema before the sweep runs"
type: decision
status: archived
authority: archived-status-mint
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-archive.sh", "job_hunt_ai_vault/wiki/lessons/_schema.yaml"]
tags: [vault, record-schema, process]
---

# The ruling, 2026-08-26

**The archiver writes `status: archived` on a page it moves, mechanically, and the value is added to
the folder schema first.** *(owner selected it.)*

**The order is the decision and not a detail.** A status outside a folder's `values:` list is
**red**, so a sweep that wrote the mark before the schema declared it would redden every page it
touched — and a red gate locks the librarian out of the work that would clear it
([[the-legal-value-list-lives-in-each-folders-schema]], [[the-librarian-lock-hook]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). This is the same ordering `idea` and
`decided_by:` were given, for the same reason
([[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]]).

# What it is not

**`archived` is not `deprecated`.** A deprecated page was replaced because it went false; an
archived page is simply no longer in the working set, and the corpus already carries the wider
reading of the folder ([[archive-is-dated-by-session-and-holds-what-left-the-working-set]]).

**It is not `implemented` either.** That value is `wiki/proposals/` alone and marks a proposal whose
design was realised ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

# What it obliges, and none of it is done

- **The value in the schema of every folder whose pages the archiver may move**, starting with
  `wiki/lessons/`;
- **The sweep itself**, which does not exist: `scripts/vault-archive.sh` moves named files and
  refuses to move a page no live page cites, and nothing walks a folder applying a criterion
  ([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]]);
- **A reading of what `archived` means for the gate's `deprecated` verdict**, which today obliges a
  page carrying that value to leave `wiki/` on sight and says nothing about any other value.

# Rejected

**Rejected: letting the librarian write the mark page by page.** The whole shape of this mechanism
is that the script does the mechanical work and the agent reads its refusals — the owner's own
ground, given about the measure writer and applying unchanged here
([[a-gauge-is-written-by-a-script-that-runs-the-command]]).

# It landed on 2026-08-28, and the ground recorded above is wrong

**`archived` is declared in all six `wiki/*/_schema.yaml` files**, and the gate's `retired` verdict
now fires on it as well as on `deprecated`, carrying the value it found in its detail field so one
message names whichever mark it met.

**The reason given above — that a sweep writing the mark before the declaration would redden every
page it touched — is false for a page the sweep has already moved.** The gate's frontmatter pass is
`find "$VAULT/wiki"` at `scripts/vault-check.sh:84`, so a page in `archive/` is validated by no
schema and could carry any word
([[the-gates-frontmatter-pass-reads-wiki-alone-and-archive-is-validated-by-no-schema]]).

**The order is right and its real ground arrived the same day.** The sweep continues past a refused
move, so it can leave a page **in `wiki/`** wearing the mark of a move that did not finish — and an
undeclared value would report that as a schema fault rather than as the half-finished move it is
([[the-archive-sweep-continues-past-a-refused-move-and-collects-its-refusals]]).

**The sentence above is left standing rather than edited**, and this section is dated the day the
correction was made ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).
