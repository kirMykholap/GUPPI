---
title: "A stated count drifts from the list it heads, and nothing checks the number against the list"
type: lesson
status: archived
authority: count-drift
basis: measurement
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", "scripts/vault-check-selftest.sh", "scripts/hook-selftest.ps1"]
tags: [vault, testing, process]
---

# One failure shape, fifteen instances, all in prose a script could reach

*(This heading read "six instances" until 2026-08-15, when the first `/vault-lint` measured six
more, and "twelve" until the audit's own arithmetic supplied the thirteenth the same day, and
"thirteen" until 2026-08-16 and 2026-08-17 added one each. It is the
one count on this page that is meant to grow, and it is re-derived from the tables below rather
than carried.)*

A document says *"five AST tests"* and then lists seven. The list is edited; the number is not.
Nothing anywhere compares them, so the sentence stays wrong until a human happens to count.

*(The title read "A stated count drifts from the list it heads, and nothing checks the two against
each other" until 2026-08-18, and the sentence above names what it was counting: the stated number,
and the list beneath it. **They were never a count of the world** — a stated count heads exactly one
list, so a third member cannot arrive and make this page stale; it would make the page wrong
instead. That reasoning stood in a `quantity:` line until the field was rejected and the rule made
unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), so an argument that a number
is not a count is no longer a way to keep one in a title. The title now names the number and the
list instead of counting them ([[a-title-names-what-is-counted-instead-of-counting-it]]), and that
is a correction in place rather than a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

**Three instances were found on 2026-08-14 alone**, which is what turned a set of corrections into
a rule:

| Where | Said | Was |
|---|---|---|
| the repository's `CLAUDE.md` | five AST boundary tests | **seven** — `test_parser_boundaries.py` and `test_normalize_boundaries.py` were missing from the table |
| [[test-suite-wall-clock]] | "the six hours that slice took" | **eight to ten hours** everywhere else, and "six" appears in neither of that page's own sources |
| `log.md` | "four pairs of pages" | **three**, listed immediately below it |

**Three more were measured while this was being written down**, and they are worse because all
three are inside the store that was diagnosing the disease:

| Where | Said | Measured 2026-08-14 |
|---|---|---|
| [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]] | 53 selftest cases | `bash scripts/vault-check-selftest.sh` → **caught 55, missed 0** |
| [[vault-scripts]] | 54 selftest cases, and 25 hook cases | **55**, and `scripts/hook-selftest.ps1` → **caught 29, missed 0** |
| [[session-hooks]] / `log.md` | 29 hook cases / 31 hook cases | **29** |

Three numbers for one script, held simultaneously in one knowledge base, is the clearest statement
of the shape available: **the count is copied, the thing counted is not.**

**Six more on 2026-08-15**, all found by the first `/vault-lint` sweeping the corpus for stated
counts and measuring each against what it heads:

| Where | Said | Measured 2026-08-15 |
|---|---|---|
| [[a-sprint-closes-on-its-goal]], and three pages citing it | 31 pages cite `raw/handoffs/…` in `sources:` | **95 of 111** — the 2026-08-13 reading carried across two ingests, on the page whose whole argument is the number |
| [[batch-lifecycle]] | "the **five** AST boundaries" | **seven** — the corpus's own opening example of this failure, uncorrected inside the corpus that diagnosed it |
| [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]] | 55 selftest cases | **61 of 61, 0 missed** — third value on one line in two days |
| [[the-catalogue-is-generated-not-maintained]] | "selftest **case 58**" | the case is the **50th of 61** now; an ordinal renumbers itself, so the case is named instead |
| [[session-hooks]] | "bash, like the **four** scripts" | **five**, since `vault-catalogue.sh` |
| [[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]] | `docs/HANDOFF.md` "is **now** a 27-line pointer" | **29** — 27 was true at `d30b317`, and `ea11cdc` added two lines |

Two things the sweep says that the first six did not. **The commit-stamped numbers survived and the
present-tense ones did not**: every figure written as "*N* at `<commit>`" was still right, and every
figure written as "it is now *N*" had moved. That is the discipline below, working. And **the drift
is not random in direction** — five of the six understate, because a corpus grows and a copied
number does not, so the argument a stale count supports is usually *stronger* than the page claims,
not weaker. That makes the failure quiet: nothing built on the number breaks, it merely stops being
evidence.

**The thirteenth is the audit's own**, and it is the most useful of the set. Its report said the
corpus had grown by **+320** pages-and-lines where the tree says **+321** — an arithmetic slip
*inside the audit of numbers drifting from their lists*, made by the agent whose whole task that
day was this failure. Two more of the same day are in `log.md` rather than here, because they are
`lint:` entries about the librarian and not about the corpus: a sidecar reported as 28 `page:` and
10 `skip:` against **27 and 11** measured by `cut -f2 | sort | uniq -c`, and an `archive/` figure
of "31 pages cite `raw/handoffs/…`" that the audit remeasured at **95 of 111** and fixed on four
pages, with the original left standing beside the correction.

**The finding declines to end**, and that is its own evidence: the rule cannot be "be more careful",
because the most careful reader this store has had made the mistake while writing the rule down.

## Why this one is not "be careful"

Every instance sits in **prose a script could reach**. A rule that compares a stated number against
the list or the table immediately following it is mechanical, and this project's own doctrine is
that a rule which fails a build beats an intention a tired session will not re-read
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). **No such rule exists yet**, and
writing one is a `/lint` proposal rather than an ingest's act — but the alternative on display is
six separate corrections in one day. It is now written down as one:
[[a-rule-comparing-a-stated-count-against-its-list]], with the mechanical shape, the false-positive
problem and the cheaper half nobody has argued against.

Until it exists, the cheap discipline is the one used above: **do not carry a count across an
edit — measure it, and write the date and the command beside it.** Every number on this page names
how it was obtained.

## The direction nobody was checking

The five-versus-seven instance has a second lesson inside it. `architectural-boundaries` had
**already recorded** the discrepancy: the corpus was right and the rule file was wrong. This
project checks pages against code routinely — a `basis: code` page may not quote yesterday's run —
and had **never checked the rule file against either**. The traffic was assumed to be one-way.

That asymmetry is now half-closed by [[claude-md-is-a-map-and-four-rules]]: with the counts moved
into the vault there is one place holding them, and `vault-check.sh` rule 15 watches the pointers
that remain. The other half — a rule file that quietly contradicts a page — has no check at all.

## The fourteenth, 2026-08-16, inside the page that heads the sibling failure

| Where | Said | Was |
|---|---|---|
| [[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]] | "**Four** instances are now on record" | **five** rows in the table immediately beneath it, `1–2, 3, 4, 5` |

It was found by a human reading that page for a different purpose, reported through
[[vault-feedback-file]], and it is the shape this page describes in its own words: the list was
edited when instance 5 arrived, the sentence heading it was not. **The count there is now re-derived
from the tables rather than carried**, which is the discipline above.

Two rows were added to that page the same day, so the correct figure moved again while this was
being written — which is the reason the discipline is *do not carry a count across an edit* rather
than *count more carefully*.

## The fifteenth, 2026-08-17: a heading over four items that was about to head nine

| Where | Said | Was about to be |
|---|---|---|
| the repository's `CLAUDE.md` | `## Four rules that cannot wait for a question` | **nine** — five more blocks migrated into `wiki/rules/` the same day |

**The repair was not to write *nine*.** The count came out of the heading altogether, which is the only
repair that holds: the next migration would have made *nine* wrong exactly as *four* was
([[a-rule-leaves-the-numbered-list-and-carries-no-ordinal]],
[[the-repository-claude-md-after-the-rules-left-it]]).

**And the ordinals came out of the rules themselves for the same reason.** A rule shipped into the wiki
carrying *"4."* would drift as the rules ahead of it left the list — so a migrating rule leaves the
numbered list for a block of its own, and ships no ordinal
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).

**This instance is the cleanest of the fifteen**, because the drift was *scheduled*: the session that
would falsify the number was the session that read it. Nothing about it required time to pass.

# A drifted count was copied into a newly written file — 2026-08-22

**The sentence *"five measured runs are on the record"* was already wrong in two files when a third
was written carrying it.** The new file was `.claude/agents/pre-task.md`, written the same day; the
session copied the sentence from the file it was replacing and checked neither against the page that
owns the count.

**A third copy was found on the same day in `.claude/hooks/check-the-plan.ps1`**, which was in no
plan and which no search for the vault page would have reached. It was found by the `pre-task` agent
reading the tree ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

**The repair was not renumbering, and the reason is this page's own.** The owning page states *seven,
plus the run of 2026-08-22* and never states eight, so writing *eight* would have been the writer's
arithmetic rather than the page's claim
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[an-unsourced-number-is-dropped-not-chosen]]). The count came out; the wording became *every
measured run on the record has returned at least one finding*.

**What the incident adds: copying is how a drifted count spreads, and a new file is the worst
carrier.** A stale sentence in an old file is at least dated by the file; the same sentence in a
file written today reads as freshly checked.
