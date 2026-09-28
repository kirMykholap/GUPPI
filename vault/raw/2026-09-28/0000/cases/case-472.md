## Case 472 — A check of the answer of `case-guppi` compares the promise lines it writes

> **context:**
> `case-guppi` writes the promise lines of a Case next to the lines around them. When it replaces the Criterion of an Estimate whole, it writes the new lines from the old ones and the change. When it splits a Case, it writes each sub-case's `then` next to its siblings'. The `SubagentStop` check of `rule-case-check` runs `judge` of `guppi/prespec.py`, and no judgment in it compares those lines. So a dropped or doubled promise reaches the person and is found only by ask-guppi at pre-spec, after ratification. The Insight `insight-case-build-promise-lines-compared-by-no-check` holds four child lessons of this kind: a Criterion line dropped (441.2), finding texts lost (459, 460.3), one promise signed in two wordings (445.5 and 445.6), and two promises in one sub-case where one Criterion was written under `sections` (460.2). The last one passes `check_form`, because it counts an Estimate `update` only with `set: {status: pending}` and not when it writes its Criterion.
> In the rounds the person chose these answers. A script cannot tell a reworded line from a dropped one, so a difference is a note, not a finding. The note goes back to `case-guppi` once by exit 2, and it never keeps the Case from being shown. The output of an exit-0 `SubagentStop` hook reaches neither the subagent nor the main agent, so exit 2 is the only way back. The comparisons live in `guppi/prespec.py`. `guppi/casecheck.py` imports them (`rule-one-judgment-one-implementation`), and `guppi prespec --check` prints them as `note:` lines. The count of `check_form` is fixed in the same Case. There are three sub-cases, one per promise.
> After the first build, pre-spec found four faults, and the person agreed to the fixes. First, "a Criterion replaced whole" is now judged by `names_a_part` of `guppi/materialize.py`, the predicate `materialize` lifts by (case 296). An Estimate `update` that names no part replaces the Criterion whole: `change` alone, any `set.status`, or a written `sections: Criterion`. So `check_form` now also counts an `update` with `set: {status: passed}`, which the old test called a reading. Second, the store replaces the entry of a Case at each answer, so 472.1 keeps the sent notes across a later answer. Third, the note mechanism is signed in 472.1 alone, and 472.2 signs only its comparison. Fourth, the Purpose of `rule-atomicity` names the narrower refusal, so 472.3 rewords it.
> What the frame shows: `.claude/settings.json` has one hook on `SubagentStop`, `guppi casecheck --subagent`, and the file does not change. The sentence of `rule-materialize` "it is how one Case touches two promises (case 204)" would become false under 472.3, so 472.3 replaces it. The `Given` line of `estimate-atomicity-rendered` says pre-spec refuses a Case with two Estimate items and no written Criterion. That stays true, since such a Case is still refused, so the Estimate is not touched. A change to the Purpose of `rule-atomicity` touches no Estimate. `estimate-prespec-notes-a-long-chain` speaks only of the long chain and stands. `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-shows-only-the-checked-case` stand: a note is not a finding, the file of the Case is still written when an answer has no finding, and the `Stop` check does not refuse a showing for a note. A test of case 327 in `tests/test_prespec.py` holds two written Criteria in one Case, so it changes. The `given` of 472.1 and of 472.3 holds eight `＋` lines. They are the files each sub-case touches, not a second promise. No `create` here is without a `ref`, so no vault query ran. A Glob found both new slugs free, and no page holds such a comparison. The Insight has no `deferred_by`, so no `{supersedes}` is needed.

> **problem:**
> A Criterion replaced whole can lose a line. One promise can be signed in two sibling sub-cases in two wordings. A sub-case can carry two promises when one Criterion is written under `sections`. No check sees any of these before the person ratifies, so the Case is built again after pre-spec.

> **recommend:**
> Compare the old and new lines of each Criterion replaced whole, and the `then` lines of sibling sub-cases, by functions of `guppi/prespec.py`. Send each difference back to `case-guppi` once as a note, which it judges by meaning, and print it at pre-spec as a `note:` line. In `check_form`, count every Estimate item that replaces a Criterion by `names_a_part`. Blocking findings were rejected: a script cannot tell a sound rewording from a dropped line.

### Case 472.1 — A line of a Criterion replaced whole that the new Criterion does not carry is a note, sent back to `case-guppi` once

> **given:**
> `rule-case-check` — its `How it works`, the `SubagentStop` check of the answer of `case-guppi` and its store
> **＋** `guppi/casecheck.py` — `subagent` and the store `<plan>.checked.json`, which send and hold the notes
> **＋** `guppi/prespec.py` — the functions that judge the notes, and `check`, which prints them
> **＋** `guppi/materialize.py` — `names_a_part`, the one judgment of an `update` that replaces a Criterion whole, unchanged
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `tests/test_prespec.py` — the tests of `guppi prespec --check`
> **＋** `rule-prespec` — its Render, the sentence on `note:` lines
> **＋** `.claude/skills/pre-spec/SKILL.md` — the file rendered from `rule-prespec`
> **＋** `estimate-case-check-notes-a-criterion-line-not-carried` — the new promise

> **when:**
> `uv run guppi casecheck --subagent` checks an answer of `case-guppi` on `SubagentStop`, or `uv run guppi prespec --check <plan>` checks the plan, and a Case of it holds an `update` of an Estimate that names no part of the page by `names_a_part` of `guppi/materialize.py`, and so replaces its `## Criterion` whole.

> **then:**
> The old Criterion is the `## Criterion` of the Estimate page as it stands. The new one is the Criterion the item writes under `sections`, or else the `when` and `then` of the Case that holds the item.
> **＋** Each line of the old Criterion that no line of the new one equals is a note that names the Case, the Estimate and the line. The operand at the head of a line, the labels `When:`, `Then:` and `Given:`, and whitespace are set aside.
> **＋** The notes of a Case are judged by functions of `guppi/prespec.py`, and `guppi/casecheck.py` imports them, not copies.
> **＋** `uv run guppi prespec --check <plan>` prints each note as a line opening with `note:`, which sets no exit code.
> **＋** `uv run guppi casecheck --subagent` exits 2 with the notes on stderr, beside any findings, and `case-guppi` answers again: it restores the line, or it keeps the change and says why in `context`.
> **＋** It stores the notes it sent for each Case id in `<plan>.checked.json`, apart from the findings, and a later answer for the same id keeps them.
> **－** A note that the store already holds for the same Case id is not sent again, and an answer whose only notes are held exits 0.
> **－** A note is not a finding. The file of the Case is written as for an answer with no finding, and the `Stop` check of `guppi casecheck` does not refuse a showing for a note.
> **－** An Estimate that a Case creates has no old Criterion and gets no note.

> **tasks:**
> - [ ] `guppi/prespec.py` — one function that returns the notes of a Criterion replaced whole, for each Estimate `update` for which `names_a_part` of `guppi/materialize.py` is false, against the page's `## Criterion`; `check` prints the notes beside `chain_notes`; the module docstring names them under Notes
> - [ ] `guppi/casecheck.py` — `check_answer` returns the notes of each Case by the functions of `guppi/prespec.py`; `subagent` keeps the `notes` of the held entry when it replaces the entry of a Case, adds the notes it sends, exits 2 when a note is not already held for that id, and writes the file of the Case when there is no finding; the docstring names the notes
> - [ ] `tests/test_prespec.py` — a Criterion replaced whole that drops a line prints one `note:` line and exits 0; the same Criterion carried line by line, with the operands changed, prints none; an `update` with `change` alone is compared; an `update` that names a part alone and a `create` print none
> - [ ] `tests/test_casecheck.py` — an answer that drops a Criterion line is sent back once with the note; the same answer again exits 0 and writes the file; a third answer for the same id with the same note exits 0, since the note is kept; a `Stop` showing of that Case is not refused for the note
> - [ ] update `rule-case-check`
>   - old: `` a later answer for the same id replacing it. ``
>   - new: `` a later answer for the same id replacing it but for the notes sent for that id, which it keeps (case 472.1). ``
>   - old: `` It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. ``
>   - new: `` It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. It runs besides the comparisons of `guppi/prespec.py` that `/pre-spec` prints as notes: each line of the `## Criterion` of an Estimate that a Case of the answer replaces whole — an `update` that names no part, by `names_a_part` of `guppi/materialize.py` — which no line of the new Criterion equals once the operand, the labels and whitespace are set aside, is a note. A note goes back to `case-guppi` once: the hook exits 2 with the notes on stderr and stores them in the entry of the Case apart from the findings; a note the store already holds for the same Case id is not sent again, the file of the Case is written as for an answer with no finding, and the `Stop` check does not refuse a Case for a note (case 472.1). ``
>   - change: `a line of a Criterion replaced whole that the new Criterion does not carry is a note, sent back to case-guppi once and kept in the store (case 472.1)`
> - [ ] update `rule-prespec`
>   - old: `` holds more than seven **＋** lines — a sign the Case is not atomic; ``
>   - new: `` holds more than seven **＋** lines — a sign the Case is not atomic —, for every line of the `## Criterion` of an Estimate that a Case replaces whole — an `update` that names no part, by `names_a_part` — which no line of its new Criterion equals, the operand, the labels and whitespace set aside (case 472.1); ``
>   - change: `pre-spec prints a note for a line of a Criterion replaced whole that the new Criterion does not carry (case 472.1)`
> - [ ] create `estimate-case-check-notes-a-criterion-line-not-carried`
>   - type: `estimate`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `A line of a Criterion replaced whole that the new Criterion does not carry goes back to case-guppi once as a note, and pre-spec prints it, with no Case held back`
>   - method: `uv run pytest tests/test_casecheck.py tests/test_prespec.py -k note, then by hand the first note the hook sends back to case-guppi`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-case-check-notes-a-criterion-line-not-carried`

> **ratification:**
> ```
> - decision[case 472.1][update][rule-case-check]{ref:rule-case-check}
> - decision[case 472.1][update][rule-prespec]{ref:rule-prespec}
> - decision[case 472.1][create][estimate-case-check-notes-a-criterion-line-not-carried]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 472.2 — Two `then` lines of sibling sub-cases that share most of their words are a note

> **given:**
> `rule-case-check` — its `How it works`, the `SubagentStop` check of the answer of `case-guppi`
> **＋** `guppi/casecheck.py` — `check_answer`, which adds the sibling notes of an answer
> **＋** `guppi/prespec.py` — the function that compares the sibling lines
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `tests/test_prespec.py` — the tests of `guppi prespec --check`
> **＋** `rule-prespec` — its Render, the sentence on `note:` lines
> **＋** `.claude/skills/pre-spec/SKILL.md` — the file rendered from `rule-prespec`
> **＋** `estimate-case-check-notes-a-then-line-shared-by-siblings` — the new promise

> **when:**
> `uv run guppi casecheck --subagent` checks an answer of `case-guppi` on `SubagentStop`, or `uv run guppi prespec --check <plan>` checks the plan, and the answer or the plan holds two or more sub-cases of one parent.

> **then:**
> Two `then` lines of two sibling sub-cases (sub-cases of one parent, such as N.1 and N.2) are a note when the words that both lines hold make 60 percent or more of the words of the shorter line. A word is a run of letters and digits of four or more characters, and the case of letters is set aside.
> **＋** The note names both Cases and both lines, and it is a note in the sense of case 472.1: it goes where that Case sends a note. `case-guppi` signs the promise in one sub-case, or it keeps both lines and says why in `context`.
> **－** A line with no word of four or more characters is compared with no line.
> **－** A sub-case that the answer holds alone has no sibling in the answer and gets no note from `guppi casecheck`. `guppi prespec --check` compares it with its siblings in the plan.

> **tasks:**
> - [ ] `guppi/prespec.py` — one function that returns the notes of sibling `then` lines by the share of their words; `check` prints them with the other notes
> - [ ] `guppi/casecheck.py` — `check_answer` adds the sibling notes of the answer to the notes of the later sibling
> - [ ] `tests/test_prespec.py` — two sibling sub-cases with one promise in two wordings print one `note:` line; two siblings with unlike lines print none; a line with no word of four characters is not compared
> - [ ] `tests/test_casecheck.py` — an answer with two sibling sub-cases that share a promise is sent back with the note; a sub-case answered alone gets no sibling note
> - [ ] update `rule-case-check`
>   - old: `An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored;`
>   - new: `` Two `then` lines of two sibling sub-cases of the answer whose shared words of four or more characters make 60 percent or more of the words of the shorter line are a note of the same kind (case 472.2). An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored; ``
>   - change: `two then lines of sibling sub-cases that share most of their words are a note (case 472.2)`
> - [ ] update `rule-prespec`
>   - old: `` a `note:` line is not a finding, sets no exit code ``
>   - new: `` and for every pair of `then` lines of two sibling sub-cases whose shared words of four or more characters make 60 percent or more of the words of the shorter line (case 472.2); a `note:` line is not a finding, sets no exit code ``
>   - change: `pre-spec prints a note for two then lines of sibling sub-cases that share most of their words (case 472.2)`
> - [ ] create `estimate-case-check-notes-a-then-line-shared-by-siblings`
>   - type: `estimate`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Two then lines of sibling sub-cases that share most of their words are a note of the answer of case-guppi and of pre-spec`
>   - method: `uv run pytest tests/test_casecheck.py tests/test_prespec.py -k sibling, then by hand the first sibling note the hook sends back to case-guppi`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-case-check-notes-a-then-line-shared-by-siblings`

> **ratification:**
> ```
> - decision[case 472.2][update][rule-case-check]{ref:rule-case-check}
> - decision[case 472.2][update][rule-prespec]{ref:rule-prespec}
> - decision[case 472.2][create][estimate-case-check-notes-a-then-line-shared-by-siblings]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 472.3 — Pre-spec counts every Estimate item that replaces a Criterion as a promise, judged by `names_a_part`

> **given:**
> `rule-prespec` — its Render, the sentence on two Estimate items in one Case
> **＋** `.claude/skills/pre-spec/SKILL.md` — the file rendered from `rule-prespec`
> **＋** `estimate-prespec-checks-the-form-of-an-item` — the promise of the form of an item, its Criterion replaced whole
> **＋** `guppi/prespec.py` — `check_form`, which counts the promises of a Case
> **＋** `tests/test_prespec.py` — the tests of the form, and the test of case 327 that holds two written Criteria in one Case
> **＋** `guppi/materialize.py` — `names_a_part`, the one judgment of an `update` that replaces a Criterion whole, and `item_keys`, both unchanged
> **＋** `rule-materialize` — its Purpose, the sentence on a written Criterion
> **＋** `rule-atomicity` — its Purpose, the sentence on the one mechanical refusal of the rule
> **＋** `insight-case-build-promise-lines-compared-by-no-check` — the Insight this Case actions

> **when:**
> `uv run guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

> **then:**
> A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
> **＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
> **＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
> **＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
> **＋** A key of an item of any kind that `item_keys` of `guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
> **－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

> **tasks:**
> - [ ] `guppi/prespec.py` — `check_form` counts every Estimate `create` and every Estimate `update` for which `names_a_part` of `guppi/materialize.py` is false, imported; its docstring and the module docstring say so, and drop "without a written `sections: Criterion`"
> - [ ] `tests/test_prespec.py` — two Estimate items where one writes its Criterion, and two that both write it, are the finding; an `update` with `change` alone and one with `set: {status: passed}` count; an `update` that names a part alone does not; the test of case 327 splits its two Estimates into two sub-cases
> - [ ] update `rule-prespec`
>   - old: `` — a `create`, or an `update` with `set: {status: pending}` — without a written `sections: Criterion` (one promise per Case: split it, by [[rule-atomicity]]) ``
>   - new: `` — a `create`, or an `update` that names no part of the page by `names_a_part` of `guppi/materialize.py` and so replaces its Criterion whole, written or lifted — (one promise per Case: split it, by [[rule-atomicity]]; case 472.3) ``
>   - change: `pre-spec counts every Estimate item that replaces a Criterion, written or lifted, by names_a_part (case 472.3)`
> - [ ] update `rule-materialize`
>   - old: `it is signed in the same block, and it is how one Case touches two promises (case 204).`
>   - new: `it is signed in the same block, and it is the one promise of its Case or sub-case (cases 204, 472.3).`
>   - change: `a written Criterion is the one promise of its Case, not a way to touch two (case 472.3)`
> - [ ] update `rule-atomicity`
>   - old: `` The one mechanical refusal of the rule is `pre-spec` on two Estimate items in a Case with no written Criterion, signed for `rule-prespec`. ``
>   - new: `` The one mechanical refusal of the rule is `pre-spec` on two Estimate items in a Case that each set a new Criterion, written or lifted, signed for `rule-prespec` (case 472.3). ``
>   - change: `the refusal of pre-spec counts a written Criterion too (case 472.3)`
> - [ ] update `estimate-prespec-checks-the-form-of-an-item`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — every Estimate item that replaces a Criterion by names_a_part, written or lifted, counts as a promise (case 472.3)`
> - [ ] update `insight-case-build-promise-lines-compared-by-no-check`
>   - set: `{status: actioned, addressed_by: decision-case-472.3}`
>   - change: `actioned: a Criterion line not carried and a then line shared by siblings are notes sent back to case-guppi once, and pre-spec counts a written Criterion as a promise (cases 472.1, 472.2, 472.3)`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-checks-the-form-of-an-item`

> **ratification:**
> ```
> - decision[case 472.3][update][rule-prespec]{ref:rule-prespec}
> - decision[case 472.3][update][rule-materialize]{ref:rule-materialize}
> - decision[case 472.3][update][rule-atomicity]{ref:rule-atomicity}
> - decision[case 472.3][update][estimate-prespec-checks-the-form-of-an-item]{ref:estimate-prespec-checks-the-form-of-an-item}
> - decision[case 472.3][update][insight-case-build-promise-lines-compared-by-no-check]{ref:insight-case-build-promise-lines-compared-by-no-check}
> ```
