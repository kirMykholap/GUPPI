---
type: decision
case: "472.3"
status: current
update: ["[[rule-prespec]]", "[[rule-materialize]]", "[[estimate-prespec-checks-the-form-of-an-item]]", "[[insight-case-build-promise-lines-compared-by-no-check]]", "[[rule-atomicity]]"]
origin: raw/2026-09-28/0000/ledger.md#case-472.3
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness, ledger]
---

## Context

`case-guppi` writes the promise lines of a Case next to the lines around them. When it replaces the Criterion of an Estimate whole, it writes the new lines from the old ones and the change. When it splits a Case, it writes each sub-case's `then` next to its siblings'. The `SubagentStop` check of `rule-case-check` runs `judge` of `guppi/prespec.py`, and no judgment in it compares those lines. So a dropped or doubled promise reaches the person and is found only by ask-guppi at pre-spec, after ratification. The Insight `insight-case-build-promise-lines-compared-by-no-check` holds four child lessons of this kind: a Criterion line dropped (441.2), finding texts lost (459, 460.3), one promise signed in two wordings (445.5 and 445.6), and two promises in one sub-case where one Criterion was written under `sections` (460.2). The last one passes `check_form`, because it counts an Estimate `update` only with `set: {status: pending}` and not when it writes its Criterion.
In the rounds the person chose these answers. A script cannot tell a reworded line from a dropped one, so a difference is a note, not a finding. The note goes back to `case-guppi` once by exit 2, and it never keeps the Case from being shown. The output of an exit-0 `SubagentStop` hook reaches neither the subagent nor the main agent, so exit 2 is the only way back. The comparisons live in `guppi/prespec.py`. `guppi/casecheck.py` imports them (`rule-one-judgment-one-implementation`), and `guppi prespec --check` prints them as `note:` lines. The count of `check_form` is fixed in the same Case. There are three sub-cases, one per promise.
After the first build, pre-spec found four faults, and the person agreed to the fixes. First, "a Criterion replaced whole" is now judged by `names_a_part` of `guppi/materialize.py`, the predicate `materialize` lifts by (case 296). An Estimate `update` that names no part replaces the Criterion whole: `change` alone, any `set.status`, or a written `sections: Criterion`. So `check_form` now also counts an `update` with `set: {status: passed}`, which the old test called a reading. Second, the store replaces the entry of a Case at each answer, so 472.1 keeps the sent notes across a later answer. Third, the note mechanism is signed in 472.1 alone, and 472.2 signs only its comparison. Fourth, the Purpose of `rule-atomicity` names the narrower refusal, so 472.3 rewords it.
What the frame shows: `.claude/settings.json` has one hook on `SubagentStop`, `guppi casecheck --subagent`, and the file does not change. The sentence of `rule-materialize` "it is how one Case touches two promises (case 204)" would become false under 472.3, so 472.3 replaces it. The `Given` line of `estimate-atomicity-rendered` says pre-spec refuses a Case with two Estimate items and no written Criterion. That stays true, since such a Case is still refused, so the Estimate is not touched. A change to the Purpose of `rule-atomicity` touches no Estimate. `estimate-prespec-notes-a-long-chain` speaks only of the long chain and stands. `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-shows-only-the-checked-case` stand: a note is not a finding, the file of the Case is still written when an answer has no finding, and the `Stop` check does not refuse a showing for a note. A test of case 327 in `tests/test_prespec.py` holds two written Criteria in one Case, so it changes. The `given` of 472.1 and of 472.3 holds eight `＋` lines. They are the files each sub-case touches, not a second promise. No `create` here is without a `ref`, so no vault query ran. A Glob found both new slugs free, and no page holds such a comparison. The Insight has no `deferred_by`, so no `{supersedes}` is needed.

## Problem

A Criterion replaced whole can lose a line. One promise can be signed in two sibling sub-cases in two wordings. A sub-case can carry two promises when one Criterion is written under `sections`. No check sees any of these before the person ratifies, so the Case is built again after pre-spec.

## Given

`rule-prespec` — its Render, the sentence on two Estimate items in one Case
**＋** `.claude/skills/pre-spec/SKILL.md` — the file rendered from `rule-prespec`
**＋** `estimate-prespec-checks-the-form-of-an-item` — the promise of the form of an item, its Criterion replaced whole
**＋** `guppi/prespec.py` — `check_form`, which counts the promises of a Case
**＋** `tests/test_prespec.py` — the tests of the form, and the test of case 327 that holds two written Criteria in one Case
**＋** `guppi/materialize.py` — `names_a_part`, the one judgment of an `update` that replaces a Criterion whole, and `item_keys`, both unchanged
**＋** `rule-materialize` — its Purpose, the sentence on a written Criterion
**＋** `rule-atomicity` — its Purpose, the sentence on the one mechanical refusal of the rule
**＋** `insight-case-build-promise-lines-compared-by-no-check` — the Insight this Case actions

## History

- 2026-09-28 created · raw/2026-09-28/0000/ledger.md#case-472.3
