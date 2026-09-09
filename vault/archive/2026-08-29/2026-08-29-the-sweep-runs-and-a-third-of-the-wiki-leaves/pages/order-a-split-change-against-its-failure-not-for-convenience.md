---
title: "Order a change whose halves land separately against its failure, not for convenience"
type: lesson
status: archived
authority: two-party-change-ordering
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check.sh", "CLAUDE.md"]
tags: [harness, process, vault]
---

# The instance

**The AST rule's move has two halves in two hands**: the librarian rewrites the page's `governs:`,
and the session removes the region from `CLAUDE.md` and generates the destination. **They cannot be
simultaneous**, so one of the intermediate windows is going to exist.

| order | the window it leaves | the gate's verdict in it |
|---|---|---|
| **librarian first** | the page points at `.claude/rules/` while the region is still in `CLAUDE.md` | **red** — rule 11's address verdict fires on the leftover |
| region first | the region is gone and the page has not moved | **advisory** — a governed file with no region |

**Librarian first was chosen**, and the reason is the failure rather than the convenience: **if the
write of the second half fails, the reverse order leaves the rule silently missing from
`CLAUDE.md`** ([[a-governed-file-with-no-region-is-an-advisory]],
[[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

# The rule

**Choose the ordering whose failure state is loud.** Both orders are correct when both halves land.
What separates them is what the tree says when only one does — and that is the state a reader will
actually be in, because a change that never fails needs no ordering at all.

**An advisory is not loud.** It is a line in a run that already prints twenty of them, and the whole
design of the advisory verdict assumes the reader is not being told about an emergency
([[an-advisory-prints-one-line-and-sorts-what-it-names]]). A red gate cannot be walked past.

# Two details that belong to the same discipline

**The region was dropped by its marker pair, never by a line number.** A region moves whenever
anything above it is edited, and a hard-coded range is a silent off-by-one that takes a neighbour's
text ([[a-region-is-a-paired-comment-named-for-a-rule]]).

**Dry-run first.** The removal was previewed and counted before it was performed: exactly the pair,
its text and its separator ([[the-injector-writes-the-separator-inside-the-region]]).

# A commit is split where each half stays independently verified — 2026-08-22

**The third commit of that session is about 1200 insertions across 30 files, and it is not split.**
`scripts/vault-check-selftest.sh` carries cases for the strike, for both new verdicts and for the
sandbox repair, so **any cut leaves a mechanism arriving in one commit and its test in another**.

**That is the criterion this page argues for, applied to size rather than to order:** the boundary is
where each half is still independently verified, and a large commit whose halves are not is one
commit ([[a-case-that-passes-before-the-change-tests-nothing]]).

**The rejected cut is the tempting one** — mechanism first, tests after — which produces a commit
that is green because nothing tests it yet, and a second commit that is the only real verification of
the first ([[reverting-the-code-tells-you-whether-a-test-tests-anything]]).
