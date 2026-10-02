---
type: decision
case: "444.2"
status: current
update: ["[[rule-spec-write]]", "[[estimate-spec-write-copies-the-ratified-case]]"]
origin: raw/2026-09-26/2300/ledger.md#case-444.2
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow, session]
---

## Context

Several readers in the pipeline decide where a fenced block opens and where it closes, and each one uses its own pattern. `guppi/materialize.py` knows only backtick fences and closes a block on the next line of backticks. `guppi/ratified.py` reads a fenced value under a sub-point and ends it at the first line of three backticks. `guppi/casecheck.py` requires that `ratification` opens and closes with exactly three backticks. `guppi/prespec.py` imports the pattern of `materialize`. `guppi/ledger.py` has a pattern of its own, and it is the only reader that knows tildes. None of them knows the length of a fence. So a sub-point value that holds its own fence, such as a template of questions with a code block in it, is cut at the inner fence. For this reason, a Case ratified earlier in this session moves the template in `.claude/skills/grill-me/SKILL.md` into an indented block. Today the file still holds a fenced block, and this Case does not change what that Case does. The Spec hook writes the `then` and `tasks` blocks with a fixed fence of three backticks, so a value with a fence inside would break the block it is written into. One judgment in several copies is what `rule-one-judgment-one-implementation` forbids.
No rule page describes a fence. `rule-spec-write` describes the blocks it writes but not their fence. The Render of `rule-case-protocol` allows a fenced block under a sub-point and says nothing about a fence inside it. `rule-ledger-write` stays deferred on another question. Only the code of `guppi/ledger.py` changes, and its `How it works` stays true, because a `LEDGER` block is still a fence opened with that tag. Case 445 of this session takes up `rule-spec-reconcile`: a guard replaces the comparison of the plan with a ratified copy, and the Spec hook no longer writes that copy. Neither the guard nor this Case changes the other. The one `create` has a `ref`, so the vault query was not run. The slug `estimate-materialize-judges-a-fence` is free in `wiki/` and in `archive/`.
`guppi/ledger.py` cannot import `guppi/materialize.py` at the top of the module, because `materialize` imports `ledger`. It imports inside the function, as it already does for `parse_line`. The writer depends on the readers: today a fence of four backticks is read as a fence tagged with a backtick. So 444.2 depends on 444.1. Case 445 changes `rule-spec-write` with its own `replace` pairs. Its first pair and the pair of 444.2 stand in one sentence of `How it works`, the one that ends in "appended otherwise". Their anchors do not overlap, so both apply. The other pairs of Case 445 stand in other sentences. The pair of 444.3 and the pairs of Case 445 on `rule-case-protocol` stand in different sentences.
The Criterion of `estimate-spec-write-copies-the-ratified-case` describes the blocks the hook writes, so 444.2 replaces it whole, and Case 445 leaves that Estimate to 444.2. The new Criterion does not mention the ratified copy, because Case 445 removes it. It covers the blocks written into the Spec of the session and the block of a short-form defer, because the `when` of 444.2 names both. The `purpose` and the `method` also mention the copy, so 444.2 sets both. The slug stays: it names the Case that was ratified, not the copy. The Criterion's line on a fenced block under a sub-point stays true under 444.1 and is kept; the new Estimate holds the reading. `estimate-spec-write-writes-a-defer` writes the `then` block as the reply shows it. The content is kept and only the fence is chosen, so it stands. Several Criteria mention a fence, a `LEDGER` block or the blocks of the Spec in words that stay true when a fence is judged by CommonMark, so they stand: `estimate-prespec-catches-bare-wikilinks`, `estimate-prespec-matches-lines-and-items`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-protocol-case-form`, `estimate-orchestration-defers-in-one-reply`, `estimate-ledger-write-lifts`, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` and `estimate-spec-write-reaches-the-approved-spec`. This Case follows `estimate-one-judgment-one-implementation-followed` and does not change it.

## Problem

The pipeline has no single standard for a fence. The readers disagree on where a block ends, a value with a fence inside is cut, and the writer cannot fence such a value safely. The questions are: which standard holds, where its one judgment lives, how the Spec hook fences a block, and what the schema tells the writer of a Case.

## Given

`guppi/ratified.py` — writes the `then` and `tasks` blocks of a Case into the Spec
**＋** `guppi/materialize.py` — gives the fence of a block, beside the one judgment of a fence
**＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, written by the hook once it stands
**＋** `tests/test_ratified.py` — the tests of the write
**＋** `rule-spec-write` — its `How it works` describes the write
**＋** `estimate-spec-write-copies-the-ratified-case` — the promise of the write
**＋** `rule-one-judgment-one-implementation` — one judgment lives in one module

## History

- 2026-09-27 created · raw/2026-09-26/2300/ledger.md#case-444.2
