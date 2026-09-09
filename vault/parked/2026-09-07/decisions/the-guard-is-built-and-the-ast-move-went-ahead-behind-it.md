---
title: "The guard is built, and the AST rule's move went ahead behind it"
type: decision
status: current
authority: ast-move-blocker
binding: prohibition
basis: code
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/hooks/ask-the-vault.ps1", ".claude/rules/ast-boundaries.md", "CLAUDE.md"]
tags: [harness, agents, testing]
supersedes: [[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]]
---

# The deferral is discharged, 2026-08-19 into 2026-08-20

**The guard was built** — a branch in `.claude/hooks/ask-the-vault.ps1` that reads `.claude/rules/`,
matches `paths:` against the payload and injects the rule body
([[the-guard-branch-lives-inside-a-hook-that-already-runs]]). **Then the AST boundary rule
moved**, in the order that fails safely rather than the order that is convenient
([[order-a-split-change-against-its-failure-not-for-convenience]]).

**What the page this replaces claimed** — *the guard is not built, and the AST rule's move now waits
on it* — is false in its title and in its *what not doing it costs* section. It is retired rather
than corrected, because the claim changed and not only the wording
([[a-title-corrected-in-place-is-not-a-supersession]]).

## What was measured on the real tree, not in a sandbox

| Reading | Value |
|---|---|
| `CLAUDE.md` | went 145 lines to 139, and the regions it carries went from nine to eight |
| `.claude/rules/ast-boundaries.md` | generated from the page's slice, with `paths:` copied verbatim |
| `bash scripts/vault-check.sh` | exit 0, 21 advisories, 0 notes |
| the glob, re-measured before the move | `tests/unit/*boundar*.py` matches 8 files and contains all three importers of `_ast_boundary` |

**Delivery, measured through the hook on the live repository**: an Edit on
`tests/unit/test_network_boundary.py` delivers the rule, so does one on
`tests/unit/_ast_boundary.py`, and `tests/unit/test_dedupe.py` and `src/jobhunt/web/app.py` are both
silent.

**The region was dropped by its marker pair, never by a line number.** A region moves whenever
anything above it is edited, and a hard-coded range is a silent off-by-one that takes a neighbour's
text. Dry-run first: exactly the pair, its text and its separator.

## What the ground was, and it is unchanged

**The move is a rehearsal with one subject and is not about the context it saves**
([[the-ast-rule-moves-to-prove-the-mechanism]]). The rejected alternative — leaving the rule in
`CLAUDE.md` — is named on that page, and the gate that demanded it named the alternative in advance
for the whole class ([[a-rule-moving-to-conditional-delivery-needs-its-page-first]]).

**The price is a rule that does not arrive**, and it is paid knowingly: that is precisely why the
guard came first, and why the move was taken on one rule rather than on a batch
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).

## What it costs now, replacing the retired page's cost section

- **The rule no longer reaches every session unconditionally.** It reaches a session that reads a
  matching file, and a session that edits one after a `/compact`
  ([[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]).
- **The advisory reads `a region or whole generation covers 2 of 15`**, and the numerator moved by a
  rewording rather than by any file gaining a region
  ([[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]]).
- **`.claude/rules/_probe-paths.md` still stands in the denominator** and is blocked from deletion by
  the citations pointing at it ([[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]]).
