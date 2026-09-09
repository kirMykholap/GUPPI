---
title: "A detector for paths written in prose, whose noise is bounded and has names"
type: proposal
status: refused
authority: prose-path-detector
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check.sh", "archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md"]
decided_by: [[the-prose-path-detector-is-refused-on-its-own-measurement]]
tags: [vault, harness, retrieval]
---

# Prototyped and measured 2026-08-19 at `6bb9a12`, and not built

**The hole it closes:** rule 5 of the gate reads `sources:` and nothing reads a path written in a
sentence, so a prose citation can point at a file that no longer exists and nothing says so
([[a-rewriter-must-be-paired-with-a-detector]]). That is the half every `raw/` migration is blocked
on ([[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]]).

# What it does, and what it measured

**Over the bodies of `wiki/` — frontmatter is rule 11's territory already — every backtick span
shaped like a path was tested for existence.**

**Naively: 299 resolve, 168 do not, across 81 pages.** After two mechanical exclusions and one
correction, **the residual is 65 across 41 pages**:

| What was taken out | How many | Why |
|---|---|---|
| a glob is not a path | 25 | `probe/*.md` and its friends name a set, not a file |
| `N/M` is a score, not a path | 6 | `24/96` and `119/1` are this store's own suite readings |
| a path in a `wiki/` body is written from the VAULT root | 97 | they resolve the moment the second base is tried |

**The third is the single biggest source of false positives and it is a base, not a heuristic.** A
detector that tries one root reports a third of the corpus.

# What the residual actually is, read rather than counted

Roughly 24 illustrations and placeholders (`folder/slug`, `wiki/rules/some-slug.md`,
`scripts/do.sh`, `archive/sprints/sprint-N/`); 8 web routes (`/collection/panel`), which are URLs
and not files; 11 module paths written short (`ingest/upsert.py` for
`src/jobhunt/ingest/upsert.py`); 6 paths one session deleted; and a handful that are genuinely dead.

# So it is an advisory and can never be red

**A page recording history is *supposed* to name a path that no longer exists**
([[fidelity-to-a-source-and-fidelity-to-the-tree]]). Reddening on that would make the store choose
between being accurate about the past and passing its own gate.

**And a red verdict here would fire on illustrations**, which are the largest class in the residual
and are the one class no rule can distinguish from a citation — the same reason `sed` cannot tell an
address from a quotation ([[sed-cannot-tell-an-address-from-a-quotation]]).

# What is open

- **Whether the exclusions are hard-coded or derived.** A glob and a score are shapes; the vault-root
  base is a fact about how this corpus writes. All three are stable, and none has been argued as a
  rule rather than as a filter that worked once.
- **Where the advisory prints and how it names what it found.** One line with sorted names is the
  house style ([[an-advisory-prints-one-line-and-sorts-what-it-names]]), and 41 pages is past what
  one line carries.
- **Whether it runs in the gate at all**, or only inside the migration script that needs it.

# What not building it costs

**The prose half of every path migration stays an eye pass**, accepted by the owner for now
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]]). And a dangling prose
reference survives indefinitely: the 2026-08-16 agent-file move left one that was still pointing at
nothing three days later, found by this prototype and by nothing else.

Retired with `superseded_by:` the day it is built or refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

**That sentence is struck — 2026-08-26, and it is false twice over.** A refused proposal takes
`status: refused` and carries **no** `superseded_by:` — a refusal is a cause, and `superseded_by:`
is a relation between two pages asserting one claim differently
([[a-refused-proposal-is-archived-and-takes-status-refused]]). An implemented one carries neither
that field nor a successor ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).
**And the page it cites is itself retired**, so the citation reaches `archive/` rather than a live
rule ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]). Struck here rather than
left to be read in `archive/`, which no check, no injector and no `/pre-task` ever opens.

# Still unbuilt on 2026-08-20, and the rewriter it complements now exists

**`scripts/vault-archive.sh` shipped and it deliberately touches only lines beginning `sources:`**
([[a-path-is-never-a-pattern]], [[vault-archive-sh]]). **So the residual this page exists for is now
produced by a tool rather than only by history**: after the probe archive, thirteen prose mentions of
`probe/RUNBOOK` remain and are correct as written — a page recording history is supposed to name a
path that no longer exists.

**The standing residual is unmoved and unreported.** Three `wiki/` pages still name
`.claude/agents/vault-librarian.md`, five days after the file moved, and **nothing reports it**
([[a-rewriter-must-be-paired-with-a-detector]]).

**Named by the owner for the session of 2026-08-20 and never started**
([[the-deferrals-of-this-session-go-onto-the-sprint]]).

**One correction to what this page says about the gate.** It calls the `sources:`-path-existence
verdict *rule 5*; it has no number of its own and is emitted inside rule 2's frontmatter pass
([[the-sources-path-verdict-has-no-rule-number-of-its-own]]). The behaviour described is right.

# The case is now a ratio on a live rename, not an anecdote — 2026-08-20

**The owner moved the agent definition back to `.claude/agents/vault-librarian.md` mid-session.** Of
the nine wiki pages naming the moved path, **the gate saw four and was blind to five**:

| where the path was written | how many | what reported it |
|---|---|---|
| in `sources:` | 4 | the frontmatter pass's path-existence verdict ([[the-sources-path-verdict-has-no-rule-number-of-its-own]]) |
| in prose | 5 | nothing |

The five: [[the-mapping-is-documented-at-each-hop-and-copied-nowhere]],
[[claude-code-config-loading]], [[vault-librarian]], [[a-rewriter-must-be-paired-with-a-detector]],
[[marked-regions-and-the-prose-outside-them]].

**44% coverage on a live rename**, against the case this page was written on — *three pages, five
days, nothing reports it*.

## And the judgement half is now demonstrated rather than argued

**At least two of the five must NEVER be repointed.** `claude-code-config-loading` says
*"— not registered"* and `a-rewriter-must-be-paired-with-a-detector` says *"since the move this page
records"*. **Both are claims about where the file was at a time**, and repointing them makes the
sentence assert the opposite of what it meant **while the gate stays green** — the scar
`scripts/vault-archive.sh` documents in its own header
([[fidelity-to-a-source-and-fidelity-to-the-tree]], [[sed-cannot-tell-an-address-from-a-quotation]]).

**All five were judged page by page at the ingest of 2026-08-20 and none was rewritten.** Where the
prose carried a live claim, a **dated correction was appended** instead — the store's standing repair
for a text that went false ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]),
and the one that does not move an address. **That is what this detector would feed: a list to judge,
never a list to rewrite.** It confirms the advisory-only reading above rather than softening it.

**Still unbuilt.** Sprint item 2 was untouched this session; it gained this measurement and nothing
else.

**Read page by page, the split is sharper than *at least two*: four of the five are historical and
one is live.** [[the-mapping-is-documented-at-each-hop-and-copied-nowhere]] and
[[marked-regions-and-the-prose-outside-them]] both name the file as one place a sweep found
`section 7` on 2026-08-17; [[a-rewriter-must-be-paired-with-a-detector]] names it twice, once as
what the 2026-08-16 sweep wrote and once as where the file stood when this page was written;
[[claude-code-config-loading]] names it as *not registered*. **Only the table row on
[[vault-librarian]] asserts where the definition lives today**, and that is the one that got a dated
correction.

**Which is the number this proposal most needs and did not have.** A detector over prose would have
printed five names and **four of them would have been correct as written** — so the advisory's real
output is a judgement queue of one, and its noise floor is the history this corpus is supposed to
keep.

# Refused by the owner on 2026-08-26, on the number above

**`status: refused`, and `decided_by:` names the ruling**
([[the-prose-path-detector-is-refused-on-its-own-measurement]],
[[a-refused-proposal-is-archived-and-takes-status-refused]]).

**The page has not moved to `archive/` yet.** The move, and the removal of `prose-path-detector` from
`authority.md` that must precede it, are S3 lines
([[retiring-a-page-removes-its-slug-from-the-authority-register]],
[[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]]). **The page carries a refused status
inside `wiki/` in the meantime, and that state is named rather than hidden.**

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
