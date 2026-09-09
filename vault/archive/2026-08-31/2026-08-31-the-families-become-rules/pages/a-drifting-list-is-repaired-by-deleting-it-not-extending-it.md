---
title: "A copy that keeps drifting is repaired by deleting it, not by adding the missing row"
type: decision
status: archived
authority: drifting-copy-repair
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "CLAUDE.md", "index.md"]
tags: [harness, vault, process]
---

# Two stale copies were found on 2026-08-17 and both were deliberately left stale

- **The repository's `CLAUDE.md` lists the vault tooling** as *"`vault-check.sh`, `vault-units.sh`,
  `vault-coverage.sh` and their self-tests"*. It was already missing `vault-catalogue.sh` before
  this session and is now missing `vault-inject.sh` as well — **two scripts behind**.
- **`index.md` still carries a five-row categories table**, while `wiki/rules/` exists, rule 1 of
  `vault-check.sh` requires it, the vault's `CLAUDE.md` names it and `vault-catalogue.sh` emits a
  section for it ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]).

**Neither was patched, on purpose.** S2's criterion 4 turns the repository's `CLAUDE.md` into
pointers ([[the-repository-claude-md-becomes-a-dispatch-table]]) and criterion 3 removes
`index.md`'s copies of what `CLAUDE.md` and `sprint.md` own
([[the-index-reads-and-the-schema-writes]]). Adding the missing row to a list that is scheduled for
deletion buys one correct reading and leaves the mechanism that produced the error intact.

# The rule

**When a copy has drifted twice, the repair is removing the copy, not correcting it.** Correcting
it is cheaper today and costs the same again at the next change, forever. Removing it costs once.

The discipline this needs is the uncomfortable half: **the stale copy stands, visibly wrong, until
the criterion that deletes it is done.** That is only acceptable because the staleness is written
down here and raised in the brief. An undocumented stale copy is a different thing entirely, and it
is what every recorded harness divergence in this project has been ([[no-rule-reads-a-harness-file]]).

## What the librarian did with `index.md` at the ingest of 2026-08-17

**No sixth row was added.** The categories table was left at five, and a dated note under it names
the sixth folder, names the page that holds the set, and says why the table was not extended. The
table itself is untouched and still awaits criterion 3.

**The tension is real and is reported rather than resolved**: the librarian's standing instruction
is to update `index.md` when a category changes, and a category did change. The note is the
smallest thing that keeps `index.md` from stating something false while leaving the criterion its
work. If the owner would rather have the row, it is one line.

## The related shape

The same argument, one level down, is why the governed set is swept instead of listed
([[the-governed-set-is-swept-and-markdown-by-property]]) and why a copied list cannot be kept in
step by discipline ([[a-copied-list-drifts-and-a-sweep-cannot]]). The vault-discovery block now
stands in **four** identical copies — `vault-check.sh`, `vault-catalogue.sh`, `vault-inject.sh` and
`.claude/hooks/vault-path.ps1` — each carrying a comment saying it is deliberately identical to the
others. That was the right call at two and is worth re-reading at four; the alternative is one
sourced fragment the shell scripts share, which the PowerShell hook still could not use
([[the-vault-directory]]).

## The owner took the exit above on 2026-08-17, and the row was added

**He asked for the sixth row, and `index.md` now names six folders.** The sentence this page ends
its `index.md` section with — *"If the owner would rather have the row, it is one line"* — was an
offer, and it was taken the same day, in the session that wrote the vault's first rule page
([[the-owner-decides-how-a-slice-is-executed]]). The dated note that explained the five-row table
was **kept whole** and stands under the reversal, so `index.md` carries both the row and the record
of why it was withheld.

**The rule of this page is not reversed and is not superseded.** What was overridden is its
*application* to one row of one table, by the only person who can override it. The claim itself
stands unchanged: when a copy has drifted twice, the repair is removing the copy. So does the
argument for it — correcting a copy buys one correct reading and leaves the mechanism intact.

**The copy is still scheduled for removal.** S2's criterion 3 deletes that table
([[the-index-reads-and-the-schema-writes]]), and the row changes nothing about what the criterion
asks for; it buys the correct reading in the meantime and its cost is exactly the one named above,
paid once. If the table is corrected a *second* time before the criterion lands, that is the signal
this page was written about.

**The other stale copy of that day was not touched.** The repository's `CLAUDE.md` still lists the
vault tooling two scripts behind, and it stays where S2's criterion 4 finds it
([[the-repository-claude-md-becomes-a-dispatch-table]]).

## Applied without argument on 2026-08-17: `## Where things are` was deleted

**The owner deleted the block rather than correcting it**, which is the first time this rule was applied
to something that had drifted four ways at once
([[where-things-are-is-deleted-now-and-generated-later]]).

**The alternative that this rule exists to refuse was on the table and named**: correcting the block. It
was refused, and the generator that will fill the gap is deferred with the cost stated
([[a-generator-fills-a-marked-region-from-the-tree]]).

**One copy in that file was deliberately left wrong instead of either corrected or deleted**, and it is
worth noting as the edge of this rule: `## Commands` says `vault-check.sh` takes `~2 s` where the measured
figure is `4.9 s`. Deleting a command list nobody has replaced would leave a session with no commands, so
it stands, wrong, on the record ([[the-command-list-moves-into-a-makefile]],
[[the-repository-claude-md-after-the-rules-left-it]]).

## The same list drifted a third time on 2026-08-21, and its own margin had already said so twice

**`empty_vault` in `scripts/vault-check-selftest.sh` kept the vault's register list by hand**, and
it went stale when `authority.md` joined rule 1's existence check. **The fixture's own comments
record the first two drifts, and both times state the repair this page rules for — derive the set,
never list it — and both times the list was extended instead.**

**It is now a sweep of the vault's top-level markdown off the pristine tree.**

**The instructive part is not the drift; it is that the file argued against itself twice in its own
margin and lost both times.** A repair written as a comment beside the thing it repairs is a note,
not a mechanism ([[knowing-a-rule-is-not-a-mechanism]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
