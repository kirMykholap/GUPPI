---
title: "The archive sweep continues past a refused move, and exits non-zero on the list it collected"
type: decision
status: archived
authority: archive-sweep-refusal-handling
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "scripts/vault-archive.sh"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-28

*(the owner selected it, from the session's proposal.)*

**The sweep does not stop at the first refusal.** It collects them, prints them as a list at the
end, and exits non-zero if there was one.

**This closes a clause named open on
[[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]]**, whose own last
paragraph says that what the sweep does when a move is refused is deferred to a session of its own.

# What it changes about a value that had already been decided

**It is the real reason `archived` had to enter every folder's schema before the sweep runs.** A
sweep that stops dead leaves nothing behind; a sweep that continues can leave a page **in `wiki/`**
carrying the mark of a move that did not complete, and an undeclared value would report that as a
schema fault rather than as the half-finished move it is
([[the-gates-frontmatter-pass-reads-wiki-alone-and-archive-is-validated-by-no-schema]]).

**The order the value entered on stands; the ground recorded for it does not**
([[the-archiver-sets-status-archived-and-the-value-enters-the-schema-first]]).

# What it does not change

**`scripts/vault-archive.sh` keeps every refusal it already has** — no page leaves without a live
page naming its slug, and a refused proposal names the decision that refused it. The sweep inherits
them rather than acquiring an opinion of its own ([[vault-archive-sh]],
[[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]]).

**And the script has no sweep mode today.** Measured 2026-08-28: it takes an explicit file list,
lines 38–41 and 117, and its precondition for `kind=pages`, lines 145–161, requires a live page
under `wiki/` naming the slug. Where the archival criterion is *a live page names it in
`decided_by:`*, that precondition is identically true and can never refuse
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).
