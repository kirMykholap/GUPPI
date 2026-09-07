---
title: "Moving a rule into `.claude/rules/` with a `paths:` scope: which rule qualifies, what the move costs, and the measurement it waits on"
type: proposal
status: deprecated
basis: human
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "CLAUDE.md", "scripts/vault-check.sh", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md"]
tags: [harness, agents, process]
superseded_by: [[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]]
---

# Designed 2026-08-18, and not built

**The idea:** a rule that only matters while a particular kind of file is being touched does not
have to reach every session unconditionally. `.claude/rules/` with `paths:` frontmatter delivers it
on a matching read instead ([[claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read]]).

**The decision that any such move is made against comes first**
([[a-rule-moving-to-conditional-delivery-needs-its-page-first]]). This page carries the design.

## The criterion, and the three rules measured against it

> **A path-scoped rule is safe only when the dangerous action requires reading a matching file
> first.**

| Rule                                                           | Verdict           | Measured                                                                                                                                                                                                                                              |
| -------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]] | **moves**         | the dangerous action is editing a boundary test, which requires reading it — `paths: ["tests/unit/*boundar*.py"]`, which covers all three files importing `_ast_boundary` (**corrected 2026-08-18**, see below)                                       |
| [[our-javascript-does-not-choose-which-rows-are-on-screen]]    | **does not move** | our JavaScript is three inline blocks in `src/jobhunt/web/templates/base.html` and nothing of ours is under `static/`, so `static/**/*.js` protects nothing; and writing a *new* js file matches no read. Its own page already warns about this shape |
| [[the-suite-never-runs-against-the-production-database]]       | **does not move** | `uv run pytest` reads no file under `tests/`, so the rule would never load — and the fixture builds and drops schema                                                                                                                                  |

**Two of three fail the criterion**, which is the finding: the pattern is narrower than it looks, and
a blanket migration of the numbered rules would silently unload two of them.

## What the one move takes

- **`governs:` changes** on the rule page, from `CLAUDE.md` to `.claude/rules/ast-boundaries.md`;
- **the new file gets a region**, and **the region leaves `CLAUDE.md` in the same change** — or rule
  11's address verdict fires on the leftover
  ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]);
- **no script change is owed.** Measured 2026-08-18: `.claude/rules/*.md` is already inside rule 11's
  harness sweep by construction, because the governed set is swept by property rather than listed
  ([[the-governed-set-is-swept-and-markdown-by-property]]);
- **the denominator grows**, and is reported as *the twelve unmarked files are unchanged*
  ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

## What is open, and it is the blocker

**Whether a `paths:`-scoped rule fires inside a subagent that reads a matching file is documented
nowhere**, and every task in this project is reviewed by a subagent. **The measurement is the
`InstructionsLoaded` hook**, and it decides what wiring the move needs — not whether the move
happens.

**Also open:** whether `/compact` dropping a scoped rule mid-session is acceptable for a rule of this
weight, given that the loss is invisible in the transcript.

## What not building it costs

**Nothing breaks.** Unconditional delivery is the safe default and it is what stands. What waiting
costs is context — nine rules render into a file every session reads — and the arithmetic on that is
not yet worth the risk of a rule that does not arrive.

**One page goes false on the day of the first move**:
[[wiki-rules-holds-the-rules-of-the-repository-claude-md]] says each rule governs that one file, in
its title. A title corrected in place is not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]],
[[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# The glob was wrong, and it was wrong in the direction the criterion exists to prevent — 2026-08-18

**What the row above said until this date:** *"the dangerous action is editing a boundary test,
which requires reading it — **six files**, `paths: ["tests/unit/*boundary*.py"]`"*.

**Six files do match that glob.** But the set this rule exists to protect is the files importing
`_ast_boundary`, and there are **three** — `test_network_boundary.py`,
`test_normalize_boundaries.py`, `test_parser_boundaries.py`. **The glob matches one of the three**:
the two spelled in the plural fall outside a pattern demanding `boundar-y`. Measured with one `ls`
during the `/grill-me` fact-finding, and re-measured at `c521a10`.

**`tests/unit/*boundar*.py` matches eight files** — the seven boundary tests and the `_ast_boundary`
helper itself — and it is what the row now carries, under the rule that `paths:` takes the widest
true pattern ([[paths-lives-on-the-vault-page-and-is-written-widest]]).

**The one migration that passes this page's own safety criterion would have silently failed to load
for two thirds of its subjects** — the exact failure the criterion exists to prevent, reproduced
inside it. The figure had been stated without the plural spelling being considered, and it was
labelled *measured*, which is why nobody re-ran it
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

# What the design gained since, and where it now lives

**The destination is generated whole rather than region-carrying**, and generation, rewriting and
deletion belong to a script — [[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]],
designed in [[generating-a-claude-rules-file-whole-from-its-vault-page]].

**The scope field lives on the vault page and is synced into the destination**
([[paths-lives-on-the-vault-page-and-is-written-widest]]).

**The move's ground is settled and is not the context it saves**
([[the-ast-rule-moves-to-prove-the-mechanism]]); the movability criterion is stated in terms of the
tools' own contracts on [[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]; and the blocker
is laid as a measurement rather than argued ([[the-conditional-delivery-probe]]).

**`.claude/rules/` now exists** and holds the probe file, so the denominator has already moved: the
coverage advisory reads `1 of 14` ([[the-region-coverage-figure-is-dated-where-it-stands]]).

# The criterion's foundation moved under it — 2026-08-19

**The page this design's movability criterion rests on was measured false in one row**, and the row is
the one the criterion uses ([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]). *"Editing an
existing file — yes, by implication"* is wrong: **delivery is triggered by the Read tool, not by touching
a matching path**, and the Edit tool's read gate is session-scoped, so it survives a `/compact` and lets
a post-compaction edit through with no rule in context
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).

**The verdict table above survives, and the reason it survives is worth stating.** The criterion —
*a path-scoped rule is safe only when the dangerous action requires reading a matching file first* —
still separates the AST rule from the JavaScript and test-database rules, because those two fail it for
reasons the correction does not touch: a new file matches no read, and a bare command reads nothing.

**What fails is the AST row's sufficiency, not its verdict.** The rule's dangerous action does require a
read, and the read does deliver — but only until something clears the context, and nothing re-delivers
after that. So **the row now reads *moves, behind a guard*** rather than *moves*.

**What the move now waits on** is [[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]] rather
than the probe, which is answered ([[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]]).

**And one thing this page listed as open is closed and one is not.** *Whether a scoped rule reaches a
subagent* — **it does**, measured, no wiring owed
([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]). *Whether `/compact`
dropping a scoped rule mid-session is acceptable for a rule of this weight* — **it is not**, which is why
there is a guard in front of the move instead of a judgement call behind it.

# Built 2026-08-20 and retired the same day, with three of its own claims struck

**The heading of this page says *"Designed 2026-08-18, and not built"*. It is built.** The AST
boundary rule governs `.claude/rules/ast-boundaries.md`, the file is generated, the region has left
`CLAUDE.md`, and the gate exits 0
([[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]]).

**Three statements on this page were false on the day it retired**, and they are named rather than
edited:

- *"and not built"* — it is;
- *"what is open, and it is the blocker"* — both open questions are answered, one measured and one
  ruled, and what the move waited on last was the guard, which exists
  ([[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]],
  [[the-guard-branch-lives-inside-a-hook-that-already-runs]]);
- *"the new file gets a region"* — **it does not.** The destination is generated whole and carries a
  marker instead, which is a change this page itself recorded further down and never carried back up
  into its own cost list ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]],
  [[the-whole-mode-owns-a-file-end-to-end]]).

| What lived here | Where it lives now |
|---|---|
| the movability criterion, and the verdict table over the rules of `CLAUDE.md` | [[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]], which carries the criterion and the three verdicts |
| the glob correction of 2026-08-18 — `*boundar*` over `*boundary*`, and why the plural spelling matters | re-measured before the move and recorded on [[the-generated-ast-boundaries-rule-file]] |
| what the one move takes, less the region clause | [[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]] |
| the denominator growing, and how it is reported | unchanged: [[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]], with the wording now at [[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]] |
| *one page goes false on the day of the first move* | it did, and it was corrected in place: [[wiki-rules-holds-the-rules-of-the-repository-claude-md]] |

**Its verdict table was reflowed from outside this session** — padded columns and a widened
separator row, **no prose changed**, confirmed with `git diff --ignore-all-space`. That is recorded
so the diff of this retirement is not read as a content edit
([[pages-base-is-not-a-review-item]] covers the other file changed the same way).

**Retired under the policy rather than by a call on this page**
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
