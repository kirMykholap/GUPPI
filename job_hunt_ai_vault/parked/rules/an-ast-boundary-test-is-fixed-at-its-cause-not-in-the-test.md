---
title: "An AST boundary test that fails is fixed at its cause, never in the test"
type: rule
status: current
governs: .claude/rules/ast-boundaries.md
render: whole
paths:
  - "tests/unit/*boundar*.py"
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "[[architectural-boundaries]]", "[[claude-md-is-a-map-and-four-rules]]"]
decided_by: [[claude-md-is-a-map-and-four-rules]]
tags: [harness, testing, architecture]
---

# What travels

<!-- text -->
**AST tests guard the architectural boundaries. If one fails, fix the cause, never the test.**
Which boundaries there are, and why each exists, is a question for the vault.
<!-- /text -->

**That is rule 2 of the repository's `CLAUDE.md`, to the word** — the second item of a numbered
list, dedented and nothing else, because a marker stands alone at column zero and an ordinal
shipped inside a rule page would drift as the rules around it move. Verified the way the rest of
this migration was: the lines were cut out of the file by line number, the ordinal and the list
indent stripped mechanically, and the result diffed byte for byte against the slice above rather
than read against it.

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it cannot wait for a question

**By the time you would think to ask, the test is already edited.** That is this rule's line in the
table that chose the four ([[claude-md-is-a-map-and-four-rules]]), and it is the whole of the
argument: a red boundary test is read as an obstacle in the same minute it is read at all, and the
cheapest thing in the tree to change is the assertion that objected.

# Why no test can hold it, although it is a rule about tests

**This is the one of the four that reads as though a test already holds it, and that reading is
wrong.** Record the distinction here, because it is the argument that admitted this page and
somebody will ask.

**The tests hold the boundaries.** Web routes touch no database, one Jinja environment with
`auto_reload` off, only `ingest/upsert.py` writes `Vacancy` fields, and the rest
([[architectural-boundaries]]). Each of those is a statement about the source tree, and each is
decided by reading the tree.

**No test holds *fix the cause rather than the test*.** That sentence is addressed to whoever is
about to edit the test, and that party is the one thing a test cannot constrain — a test that has
been edited passes. The guard and the guarded would be the same file, and the result is a green
suite over a boundary nobody holds any more: the shape this project has met most often, a check
that passes having examined nothing ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[a-test-green-under-any-implementation]]).

So the folder's admission test — *a paragraph becomes a rule page if it is imperative and not
enforced by a test, and where a test holds the rule, the test is the rule*
([[rules-becomes-a-type-of-its-own]]) — is passed rather than failed here, but only when it is read
exactly. Read quickly, the AST tests look like the enforcement; read exactly, they enforce the
other sentence. **The rule and the thing the rule protects are one word apart and are not the same
object.**

The delivery matters for the same reason. The boundary page has carried *"If one of them fails, fix
the cause, never the test"* since it was written, and a page is found by searching; this text has to
arrive **before** the work, which is the property the injector preserves and the reason the rule is
rendered instead of cited ([[a-region-is-a-paired-comment-named-for-a-rule]]).

# What the vault holds and this rule deliberately does not

Which boundaries exist, why each exists, and — the part that matters most when one goes red —
**what each of them does not catch**: a computed field name, raw SQL text, a write from another
process ([[architectural-boundaries]]). A boundary described more strongly than it is implemented is
worse than no boundary at all ([[a-boundary-stronger-in-prose-than-in-code]]), so a failing test
sends its reader to that page and not to this one.

**The rule's text names no count on purpose.** The number of these tests has drifted in prose more
than once, and when it did, the corpus was right where the rule file was wrong
([[a-stated-count-drifts-from-the-list-it-heads]]). A rendered rule carrying a number would put that
drift back into a file nothing greps.

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment named for this
page's slug, in a file on its way to being a dispatch table
([[the-repository-claude-md-becomes-a-dispatch-table]]).

**The page and its region belong in one change, and this page arrived first.** The librarian writes
`wiki/`; marking the region and running the injector are the session's, in the same commit. Until
then rule 12 reports this rule as governing a file that carries no region for it. If the rule is
ever replaced, the successor renders and this page does not
([[a-deprecated-rule-does-not-render]]).

> [!CAUTION] CONTRADICTION
> **The gate is red on a second line, and that one is not about the missing region.** This page is
> one of several current rules governing `CLAUDE.md`, and `governs:` is required to be unique across
> current rules, so `vault-check.sh` prints *two current rules govern the same destination:
> `CLAUDE.md`*. The injector renders them all into that file without complaint — measured.
> Unresolved, and not the librarian's to choose:
> [[a-deprecated-rule-does-not-render]] carries the measurement, [[rules-becomes-a-type-of-its-own]]
> carries the migration it collides with.

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

# The instruction and the mechanism are different pages

[[architectural-boundaries]] answers `authority: boundary-tests`. This page carries only the
instruction, and carries `governs:` in place of an `authority:`, so the pair does not read as two
answers to one question ([[rules-becomes-a-type-of-its-own]]).

# Where it renders, corrected — 2026-08-20

**The section *Where it renders* above went false on this date and is left standing rather than
rewritten.** It read *"`governs: CLAUDE.md` — a path from the repository root … The text lands in a
paired comment named for this page's slug"*, and *"the page and its region belong in one change,
and this page arrived first"*, until 2026-08-20. Both were true of this rule from 2026-08-17, when
it was first rendered, and both stopped being true when it moved to conditional delivery
([[the-ast-rule-moves-to-prove-the-mechanism]],
[[a-rule-moving-to-conditional-delivery-needs-its-page-first]]). The paragraph is the record of how
this rule was delivered while it was unconditional, and the argument above it — **why** this text
renders instead of being cited — is untouched by **where** it renders.

**What is true now.** `governs: .claude/rules/ast-boundaries.md`, still a path from the repository
root and still resolved against nothing else ([[governs-is-a-path-from-the-repository-root]]), with
`render: whole` and a `paths:` scope of `tests/unit/*boundar*.py`, which lives in this page's
frontmatter and is synced into the generated file verbatim
([[paths-lives-on-the-vault-page-and-is-written-widest]]).

**There is no region and no paired comment, because the destination has no life of its own.** The
file is generated whole by `scripts/vault-inject.sh` — frontmatter carrying this page's `paths:`,
the marker, the slice, and nothing else. A region exists to protect an insert into a file that has
other content around it; here the script owns the bytes end to end
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]],
[[a-region-is-a-paired-comment-named-for-a-rule]]).

**The marker is the whole of that ownership, and it does two jobs in one reading.**
`<!-- vault-inject: generated from rule: <this page's slug> - do not edit -->` sits between the
frontmatter and the text: it is the human's warning not to hand-edit, and it is the script's
permission to delete the file. A file in that directory **without** it is somebody's own rule and is
never touched, whatever the vault knows about it. It is an HTML comment because a comment is
stripped before the model reads the file, so the banner costs no context
([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]).

**A hand edit to the generated file is red.** The gate asks its question by running the injector, so
any difference between the file and this page comes back as a failure naming both — *does not carry
what this page says* — rather than as something the next run silently overwrites
([[a-check-asks-by-running-the-writer-it-checks]]). That is the owner's ruling of 2026-08-19 and it
answers *red, or advisory*, which the design left open
([[generating-a-claude-rules-file-whole-from-its-vault-page]]).

**And retirement now deletes rather than overwrites.** A deprecated rule does not render
([[a-deprecated-rule-does-not-render]]); under a region that meant the successor's text replaced
this one's in place, and under `whole` it means the file this page owns is removed — by its marker,
which is why the marker is the only fact the deleting branch may read.

**What did not change is the slice.** It is the same bytes it was before the move; what changed is
that it now arrives when a matching file is read rather than in every session, and that after a
`/compact` it arrives because something runs again
([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]],
[[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).
