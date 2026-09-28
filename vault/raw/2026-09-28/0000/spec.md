<!-- approved 03:37:02 · session d34b4c59 -->

# Spec — session 0000, 2026-09-28

## Case 470 — `estimate-skill-grill-me-asks-in-rounds` is read on a round of `case-guppi` too

> **context:**
> `.claude/skills/grill-me/SKILL.md` is the text of `rule-skill-grill-me`. It reaches an agent in two ways: the person types `/grill-me`, or `case-guppi` loads it through `skills: [grill-me]` and asks the rounds of Plan Mode with it. The `When` of `estimate-skill-grill-me-asks-in-rounds` names only the person's typed command. So no round of `case-guppi` counts toward a reading. The handoff of session 2050 counts 14 such rounds in that session. The person seldom types `/grill-me`, so the reading may never come and `rule-skill-grill-me` stays in `draft`.
> In the round, the person chose to widen the trigger to both paths. For `case-guppi`, the instructions that started the grill name the confirmation: the showing of the Case and its ratification (`rule-case-build`). The line on confirmation therefore holds as written. The `－` line on dispatching a sub-agent stays true on both paths.
> At pre-spec, `ask-guppi` found that the new `When` would sign the form of a round of `case-guppi` twice. `estimate-case-build-writes-the-case` already signs "a round of questions in the form of `.claude/skills/grill-me/SKILL.md`", so one bad round would fail two Estimates. The person agreed to this fix: the form line reads only the person's `/grill-me`. On a round of `case-guppi`, this Estimate reads the frontier rule, finding facts and the confirmation, and a `－` line leaves the form to `estimate-case-build-writes-the-case`. That Estimate's Criterion is not touched.
> This Case does not fix the two rounds that broke the frontier rule, in 465 and in the fourth round of 467. That fix is a separate promise on `rule-case-build`. Under this Case, a round that breaks the rule again counts as a `failed` reading of this Estimate. The Context of case 466 says this Estimate does not change. It stands in the Spec of session 2050 and on the live pages `decision-case-466.1` and `decision-case-466.2`. A Decision page records what held when it was written, so that sentence does not become false. The Purpose of `rule-skill-grill-me` still holds. The Case has no `create`, so no vault query ran.

> **problem:**
> The promise of the grill-me skill can be read only on a command the person seldom types. The path where the skill is actually used, the rounds of `case-guppi`, gives no reading. The Estimate may stay `pending`, and its rule `draft`, with no end.

> **given:**
> `estimate-skill-grill-me-asks-in-rounds` — the promise of the skill, its Criterion replaced whole and its method changed
> **＋** `rule-skill-grill-me` — the rule the Estimate reads, unchanged
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill text both paths load
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by its `skills` field and names the confirmation of its rounds
> **＋** `estimate-case-build-writes-the-case` — the promise of the form of a round of `case-guppi`, unchanged

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** On the person's `/grill-me`, each question is numbered, with a title, a body and a recommended answer.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** The form of a round of `case-guppi` is not read here: it is the promise of `estimate-case-build-writes-the-case`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

```then
update:
- slug: estimate-skill-grill-me-asks-in-rounds
  set:
    status: pending
    method: uv run guppi render --check; by hand, one round read in the chat in a session after the render, of the person's /grill-me or of case-guppi
  change: the Criterion replaced whole — a round of case-guppi reads the frontier rule, finding facts and the confirmation; the form of its questions stays with estimate-case-build-writes-the-case (case 470)
```

```tasks
- [x] update `estimate-skill-grill-me-asks-in-rounds`
- [ ] read `estimate-skill-grill-me-asks-in-rounds` — `uv run guppi render --check`; by hand, one round of the person's `/grill-me` or of `case-guppi` in a session after this one
```

## Case 472 — A check of the answer of `case-guppi` compares the promise lines it writes

> **context:**
> `case-guppi` writes the promise lines of a Case next to the lines around them. When it replaces the Criterion of an Estimate whole, it writes the new lines from the old ones and the change. When it splits a Case, it writes each sub-case's `then` next to its siblings'. The `SubagentStop` check of `rule-case-check` runs `judge` of `guppi/prespec.py`, and no judgment in it compares those lines. So a dropped or doubled promise reaches the person and is found only by ask-guppi at pre-spec, after ratification. The Insight `insight-case-build-promise-lines-compared-by-no-check` holds four child lessons of this kind: a Criterion line dropped (441.2), finding texts lost (459, 460.3), one promise signed in two wordings (445.5 and 445.6), and two promises in one sub-case where one Criterion was written under `sections` (460.2). The last one passes `check_form`, because it counts an Estimate `update` only with `set: {status: pending}` and not when it writes its Criterion.
> In the rounds the person chose these answers. A script cannot tell a reworded line from a dropped one, so a difference is a note, not a finding. The note goes back to `case-guppi` once by exit 2, and it never keeps the Case from being shown. The output of an exit-0 `SubagentStop` hook reaches neither the subagent nor the main agent, so exit 2 is the only way back. The comparisons live in `guppi/prespec.py`. `guppi/casecheck.py` imports them (`rule-one-judgment-one-implementation`), and `guppi prespec --check` prints them as `note:` lines. The count of `check_form` is fixed in the same Case. There are three sub-cases, one per promise.
> After the first build, pre-spec found four faults, and the person agreed to the fixes. First, "a Criterion replaced whole" is now judged by `names_a_part` of `guppi/materialize.py`, the predicate `materialize` lifts by (case 296). An Estimate `update` that names no part replaces the Criterion whole: `change` alone, any `set.status`, or a written `sections: Criterion`. So `check_form` now also counts an `update` with `set: {status: passed}`, which the old test called a reading. Second, the store replaces the entry of a Case at each answer, so 472.1 keeps the sent notes across a later answer. Third, the note mechanism is signed in 472.1 alone, and 472.2 signs only its comparison. Fourth, the Purpose of `rule-atomicity` names the narrower refusal, so 472.3 rewords it.
> What the frame shows: `.claude/settings.json` has one hook on `SubagentStop`, `guppi casecheck --subagent`, and the file does not change. The sentence of `rule-materialize` "it is how one Case touches two promises (case 204)" would become false under 472.3, so 472.3 replaces it. The `Given` line of `estimate-atomicity-rendered` says pre-spec refuses a Case with two Estimate items and no written Criterion. That stays true, since such a Case is still refused, so the Estimate is not touched. A change to the Purpose of `rule-atomicity` touches no Estimate. `estimate-prespec-notes-a-long-chain` speaks only of the long chain and stands. `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-shows-only-the-checked-case` stand: a note is not a finding, the file of the Case is still written when an answer has no finding, and the `Stop` check does not refuse a showing for a note. A test of case 327 in `tests/test_prespec.py` holds two written Criteria in one Case, so it changes. The `given` of 472.1 and of 472.3 holds eight `＋` lines. They are the files each sub-case touches, not a second promise. No `create` here is without a `ref`, so no vault query ran. A Glob found both new slugs free, and no page holds such a comparison. The Insight has no `deferred_by`, so no `{supersedes}` is needed.

> **problem:**
> A Criterion replaced whole can lose a line. One promise can be signed in two sibling sub-cases in two wordings. A sub-case can carry two promises when one Criterion is written under `sections`. No check sees any of these before the person ratifies, so the Case is built again after pre-spec.

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

```then
create:
- slug: estimate-case-check-notes-a-criterion-line-not-carried
  type: estimate
  ref: rule-case-check
  kind: QA
  purpose: A line of a Criterion replaced whole that the new Criterion does not carry goes back to case-guppi once as a note, and pre-spec prints it, with no Case held back
  method: uv run pytest tests/test_casecheck.py tests/test_prespec.py -k note, then by hand the first note the hook sends back to case-guppi
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: a later answer for the same id replacing it.
    new: a later answer for the same id replacing it but for the notes sent for that id, which it keeps (case 472.1).
  - old: It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else.
    new: 'It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. It runs besides the comparisons of `guppi/prespec.py` that `/pre-spec` prints as notes: each line of the `## Criterion` of an Estimate that a Case of the answer replaces whole — an `update` that names no part, by `names_a_part` of `guppi/materialize.py` — which no line of the new Criterion equals once the operand, the labels and whitespace are set aside, is a note. A note goes back to `case-guppi` once: the hook exits 2 with the notes on stderr and stores them in the entry of the Case apart from the findings; a note the store already holds for the same Case id is not sent again, the file of the Case is written as for an answer with no finding, and the `Stop` check does not refuse a Case for a note (case 472.1).'
  change: a line of a Criterion replaced whole that the new Criterion does not carry is a note, sent back to case-guppi once and kept in the store (case 472.1)
- slug: rule-prespec
  replace:
  - old: holds more than seven **＋** lines — a sign the Case is not atomic;
    new: holds more than seven **＋** lines — a sign the Case is not atomic —, for every line of the `## Criterion` of an Estimate that a Case replaces whole — an `update` that names no part, by `names_a_part` — which no line of its new Criterion equals, the operand, the labels and whitespace set aside (case 472.1);
  change: pre-spec prints a note for a line of a Criterion replaced whole that the new Criterion does not carry (case 472.1)
```

```tasks
- [x] `guppi/prespec.py` — one function that returns the notes of a Criterion replaced whole, for each Estimate `update` for which `names_a_part` of `guppi/materialize.py` is false, against the page's `## Criterion`; `check` prints the notes beside `chain_notes`; the module docstring names them under Notes
- [x] `guppi/casecheck.py` — `check_answer` returns the notes of each Case by the functions of `guppi/prespec.py`; `subagent` keeps the `notes` of the held entry when it replaces the entry of a Case, adds the notes it sends, exits 2 when a note is not already held for that id, and writes the file of the Case when there is no finding; the docstring names the notes
- [x] `tests/test_prespec.py` — a Criterion replaced whole that drops a line prints one `note:` line and exits 0; the same Criterion carried line by line, with the operands changed, prints none; an `update` with `change` alone is compared; an `update` that names a part alone and a `create` print none
- [x] `tests/test_casecheck.py` — an answer that drops a Criterion line is sent back once with the note; the same answer again exits 0 and writes the file; a third answer for the same id with the same note exits 0, since the note is kept; a `Stop` showing of that Case is not refused for the note
- [x] update `rule-case-check`
- [x] update `rule-prespec`
- [x] create `estimate-case-check-notes-a-criterion-line-not-carried`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-case-check-notes-a-criterion-line-not-carried`
```

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

```then
create:
- slug: estimate-case-check-notes-a-then-line-shared-by-siblings
  type: estimate
  ref: rule-case-check
  kind: QA
  purpose: Two then lines of sibling sub-cases that share most of their words are a note of the answer of case-guppi and of pre-spec
  method: uv run pytest tests/test_casecheck.py tests/test_prespec.py -k sibling, then by hand the first sibling note the hook sends back to case-guppi
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored;
    new: Two `then` lines of two sibling sub-cases of the answer whose shared words of four or more characters make 60 percent or more of the words of the shorter line are a note of the same kind (case 472.2). An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored;
  change: two then lines of sibling sub-cases that share most of their words are a note (case 472.2)
- slug: rule-prespec
  replace:
  - old: a `note:` line is not a finding, sets no exit code
    new: and for every pair of `then` lines of two sibling sub-cases whose shared words of four or more characters make 60 percent or more of the words of the shorter line (case 472.2); a `note:` line is not a finding, sets no exit code
  change: pre-spec prints a note for two then lines of sibling sub-cases that share most of their words (case 472.2)
```

```tasks
- [x] `guppi/prespec.py` — one function that returns the notes of sibling `then` lines by the share of their words; `check` prints them with the other notes
- [x] `guppi/casecheck.py` — `check_answer` adds the sibling notes of the answer to the notes of the later sibling
- [x] `tests/test_prespec.py` — two sibling sub-cases with one promise in two wordings print one `note:` line; two siblings with unlike lines print none; a line with no word of four characters is not compared
- [x] `tests/test_casecheck.py` — an answer with two sibling sub-cases that share a promise is sent back with the note; a sub-case answered alone gets no sibling note
- [x] update `rule-case-check`
- [x] update `rule-prespec`
- [x] create `estimate-case-check-notes-a-then-line-shared-by-siblings`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-case-check-notes-a-then-line-shared-by-siblings`
```

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

```then
update:
- slug: rule-prespec
  replace:
  - old: '— a `create`, or an `update` with `set: {status: pending}` — without a written `sections: Criterion` (one promise per Case: split it, by [[rule-atomicity]])'
    new: '— a `create`, or an `update` that names no part of the page by `names_a_part` of `guppi/materialize.py` and so replaces its Criterion whole, written or lifted — (one promise per Case: split it, by [[rule-atomicity]]; case 472.3)'
  change: pre-spec counts every Estimate item that replaces a Criterion, written or lifted, by names_a_part (case 472.3)
- slug: rule-materialize
  replace:
  - old: it is signed in the same block, and it is how one Case touches two promises (case 204).
    new: it is signed in the same block, and it is the one promise of its Case or sub-case (cases 204, 472.3).
  change: a written Criterion is the one promise of its Case, not a way to touch two (case 472.3)
- slug: rule-atomicity
  replace:
  - old: The one mechanical refusal of the rule is `pre-spec` on two Estimate items in a Case with no written Criterion, signed for `rule-prespec`.
    new: The one mechanical refusal of the rule is `pre-spec` on two Estimate items in a Case that each set a new Criterion, written or lifted, signed for `rule-prespec` (case 472.3).
  change: the refusal of pre-spec counts a written Criterion too (case 472.3)
- slug: estimate-prespec-checks-the-form-of-an-item
  set:
    status: pending
  change: the Criterion replaced whole — every Estimate item that replaces a Criterion by names_a_part, written or lifted, counts as a promise (case 472.3)
- slug: insight-case-build-promise-lines-compared-by-no-check
  set:
    status: actioned
    addressed_by: decision-case-472.3
  change: 'actioned: a Criterion line not carried and a then line shared by siblings are notes sent back to case-guppi once, and pre-spec counts a written Criterion as a promise (cases 472.1, 472.2, 472.3)'
```

```tasks
- [x] `guppi/prespec.py` — `check_form` counts every Estimate `create` and every Estimate `update` for which `names_a_part` of `guppi/materialize.py` is false, imported; its docstring and the module docstring say so, and drop "without a written `sections: Criterion`"
- [x] `tests/test_prespec.py` — two Estimate items where one writes its Criterion, and two that both write it, are the finding; an `update` with `change` alone and one with `set: {status: passed}` count; an `update` that names a part alone does not; the test of case 327 splits its two Estimates into two sub-cases
- [x] update `rule-prespec`
- [x] update `rule-materialize`
- [x] update `rule-atomicity`
- [x] update `estimate-prespec-checks-the-form-of-an-item`
- [x] update `insight-case-build-promise-lines-compared-by-no-check`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-checks-the-form-of-an-item`
```

## Case 473 — A reader that runs before the page it reads: the red in Work Mode is a handoff note, a refusing reader keeps the old form

> **context:**
> Some Cases change two things at once: a reader in code, and the page or governed file it reads. The reader runs from the working tree as soon as the code is written. The page lands only at the librarian's run, and the governed file at the render in that run. Between those two moments the reader refuses or goes red, and this happens by construction. Two lessons record it. After case 111.3, the Stop hook of session M refused 13 ledger lines: the reader required a stamped `hi`, and the writer of stamped lines reached `.claude/settings.json` only with the next render. That loss was stopped by the 111.6 fallback, which case 136.3 removed once the writer was live. After cases 227 and 229.1, `make lint` was red on the sprint step until the librarian's run.
> `insight-workflow-code-live-before-the-page-it-reads` is `open`, severity 2, and case 238 defers it. Its Proposal is one sentence in `rule-work-mode`. That rule is a `draft` with only a `Purpose`, and 20 Cases defer it. Naming it would take up the whole rule (case 467). So the person chose `rule-retro` for the red half, for now, and will review where it belongs when `rule-work-mode` is taken up. The person chose `rule-case-build` for the fallback half, because `case-guppi` builds every Case and reads its frame.
> The frame. The Render of `rule-retro` already says "Do not run `make lint` here" and "Red tests: fix now … the handoff still needs green". The new sentence leaves tests under that rule. `make lint` runs `render --check`, `sprint --check`, `backlog --check`, `glossary --check` and `guppi lint`. The librarian runs it after the render. A note for the handoff is already one of the four ends of a frontier item, and `rule-handoff` already writes such a note as the end of its item, so `rule-handoff` is not changed. `estimate-retro-loads` promises the readings. `estimate-retro-report-holds-each-fact-once` promises the form of the report, and its frontier already holds "what the agent noticed during Work Mode". Neither Estimate is touched. `estimate-case-build-writes-the-case` promises that `case-guppi` reads the frame and fixes each contradiction, and that stays true. The fallback is a promise of its own, on a new Estimate. Both `create` lines carry a `ref`, so no vault query was run. A Glob of `vault/**/` finds no page for either new slug.
> Not done: `rule-work-mode` stays in the backlog as it is, and no rule about tests changes.

> **problem:**
> No text says that a check which reads a page or a file the same Spec updates is expected to be red in Work Mode, so its red is taken for a finding or for debt. No text asks the author of a Case to keep a refusing reader working until its new writer is live, so a write that is refused in the gap is lost.

### Case 473.1 — A check red before the librarian's run is a note for the handoff

> **given:**
> `rule-retro` — its Render, the paragraph that keeps `make lint` out of Retro
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `make lint` — the checks of the vault, which the librarian runs after the render
> **＋** `rule-handoff` — writes a note for the handoff as the end of its item, unchanged
> **＋** `estimate-retro-report-holds-each-fact-once` — the promise of the form of the report, unchanged
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the new promise

> **when:**
> The person invokes `/retro` in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

> **then:**
> The red or the refusal is an item of the frontier, and it ends as a note for the handoff that names the check and the page or file it waits for.
> **＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
> **－** The red is not debt: the agent does not fix it or revert it into a patch.
> **－** A red test is not such a check: it is fixed or reverted into a patch, and the handoff still needs green.

```then
create:
- slug: estimate-retro-red-check-of-an-updated-page-is-a-handoff-note
  type: estimate
  ref: rule-retro
  kind: QA
  purpose: Whether a check red in Work Mode because it reads a page or a governed file the same Spec updates ends at Retro as a note for the handoff, not as debt, while a red test is still fixed or reverted
  method: one reading by hand at the first /retro after the render in a session whose Spec updates a page or a governed file that make lint reads, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-retro
  replace:
  - old: 'Do not run `make lint` here: the vault is written after handoff, by the librarian.'
    new: 'Do not run `make lint` here: the vault is written after handoff, by the librarian. A check that reads a page or a governed file this session''s Spec updates — `make lint` or one of its steps, or a hook of the working tree — is red or refuses in Work Mode until the librarian''s run writes the page or renders the file, and the `make lint` of that run is its reading: such a red is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt. A red test is not such a check: it is fixed or reverted as above (case 473.1).'
  change: a check red in Work Mode because it reads a page or a file the same Spec updates is a note for the handoff, not debt; a red test stays under the green rule (case 473.1)
```

```tasks
- [x] update `rule-retro`
- [x] create `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — by hand, at the first such `/retro` after the render
```

### Case 473.2 — A reader that loses what it refuses keeps the old form until its writer is live

> **given:**
> `rule-case-build` — its Render, the paragraph on the frame of a Case
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from `rule-case-build`
> **＋** `estimate-case-build-writes-the-case` — the promise that the frame is read and each contradiction fixed, unchanged
> **＋** `rule-retro` — the note for the handoff that a reader which only goes red gets, by 473.1
> **＋** `insight-workflow-code-live-before-the-page-it-reads` — the Insight this Case actions
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — the new promise

> **when:**
> `case-guppi` builds a Case that changes a reader in code and the text or the writer that reader reads, where the reader runs from the working tree at once and the text lands at the librarian's run or the render.

> **then:**
> Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
> **＋** The removal of the old form is left to a Case of a later session, after that reading.
> **－** A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`.
> **－** `insight-workflow-code-live-before-the-page-it-reads` stands `actioned` with `addressed_by: decision-case-473.2` and leaves the backlog.

```then
create:
- slug: estimate-case-build-keeps-the-old-form-until-the-writer-is-live
  type: estimate
  ref: rule-case-build
  kind: QA
  purpose: Whether a Case that changes a reader and the text it reads, where the reader loses what it refuses before the text lands, keeps the old form in its then until the writer is measured live
  method: one reading by hand at the first Case case-guppi builds after the render that changes a reader and the text or writer it reads, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: Fix each in the Case, or say in `context` why it stands.
    new: 'Fix each in the Case, or say in `context` why it stands. When the Case changes a reader in code and the text or the writer it reads, the reader runs from the working tree at once and the text lands at the librarian''s run or the render; where the reader refuses in between and what it refuses is lost — a hook that refuses a ledger line — `then` says that the reader accepts the old form beside the new one until a reading of the writer passes live, and a Case of a later session removes the old form (cases 111.6, 136.3, 473.2). A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`.'
  change: a reader that loses what it refuses before its writer lands keeps the old form until the writer is measured live (case 473.2)
- slug: insight-workflow-code-live-before-the-page-it-reads
  set:
    status: actioned
    addressed_by: decision-case-473.2
  change: 'actioned: the red of a check before the librarian''s run is a note for the handoff in rule-retro (case 473.1); a reader that loses what it refuses keeps the old form until its writer is measured live, in rule-case-build (case 473.2); the defer of case 238 retired'
```

```tasks
- [x] update `rule-case-build`
- [x] update `insight-workflow-code-live-before-the-page-it-reads`
- [x] create `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — by hand, at the first such Case after the render
```

## Case 474 — The librarian opens an archived page by its slug, reads the saved output of its own command, and finds the form of a synthesis entry in its frame

> **context:**
> This Case replaces Case 471 with the same content. After 471 was ratified again, the plan file still held the first body of 471 under its parent heading, with the same `replace` pairs on `rule-documentation` and `rule-synthesis`. Those first pairs used up the anchors, so the pairs of 471.1 missed and `guppi ratified` refused them. The agent may not edit the plan. A superseding Case removes 471 from the Spec. `remove_case` removes a Case together with its sub-cases, but `mark_superseded` in `guppi/materialize.py` marks only the entries whose case id is exactly the one named. So the lines of 474 carry one `{supersedes:case N}` block each for 471, 471.1 and 471.2 (case 429), and every entry of the three ids is superseded.
> The librarian runs after the handoff with the frame of `rule-documentation`, rendered into `.claude/agents/librarian-guppi.md`. The frame bans every read of `vault/archive/`, and only the prose holds the ban. `estimate-documentation-completes` failed on the librarian run over session 1819. The transcript of that run shows two reads outside the frame. First, the index Grep over `vault/wiki/lessons/` printed 21 KB. The harness saved that output to a file under `~/.claude/projects/…/tool-results/`, and the librarian read the file back. That file is the index lines, and the frame allows the index lines, but the Criterion counts the read as a breach. Second, at 20:40:20 and 20:40:26 the librarian grepped every `vault/raw/*/*/materialize.yaml` for `librarian:` entries, and at 20:40:39 it ran `grep -rln "status: clustered" raw archive`. It was looking for an earlier synthesis entry to copy its form. The event log of 2026-09-27 shows the same search in the librarian run of 04:20:33, over the yaml of session 2026-09-26/1745. It also shows that the librarian run of 18:08–18:13 listed `vault/archive/` and read a file under `~/.claude/projects/`. The line at 23:38:43 comes before the handoff of session 2050, so it is not from a librarian run. The frame names the fields of a synthesis entry but shows none. `tests/test_generate.py` holds a synthesis `create` of an Insight, but the frame does not point to it.
> The full ban also blocks one read that the librarian needs. `guppi/generate.py` fails on a slug taken by an archived page and on a `rename` of an archived page. Its error names only the slug, and archived pages lie at any depth under `vault/archive/`. The frame tells the librarian to say why a script failed, but it may open only pages under `vault/wiki/`. `rule-ask` finds an archived page by slug alone, with the Glob `vault/archive/**/<slug>.md`, and this Case gives the librarian the same lookup.
> `rule-documentation` is `draft`, and `estimate-documentation-completes` is `failed`. The Case creates no page, so no vault query ran. In the frame: the Render of `rule-synthesis` keeps "Do not read the archive", and its Purpose keeps "The archive is not read". Both are about the synthesis, which still does not read the archive. `estimate-synthesis-clusters` says, of the whole run, "no archive file was read". An archived page opened for a script's error would fail that line, so sub-case 474.2 replaces that Criterion whole and limits the line to the synthesis. `estimate-synthesis-keeps-actioned-by-the-mark` speaks only of `addressed_by`, and it stands.
> In the rounds and at pre-spec, the person chose these answers: allow the saved output of the librarian's own command; do not ban the archive completely, but allow the Glob by slug for a script's error and forbid any search of the archive; add no hook; write every form of a synthesis entry in the frame itself, with a ban on reading a `materialize.yaml` that `materialize` did not name; and add the sub-case for `estimate-synthesis-clusters`.

> **problem:**
> The frame bans a read that the librarian needs, the read of an archived page named in a script's error, and it does not say how to find that page. It counts the saved output of the librarian's own command as a breach. It gives no example of a synthesis entry, so the librarian searches the yamls of other sessions and the archive for one. Two Estimates fail on reads that the frame should allow or should make needless. Case 471, which decided this, cannot be written into the Spec as it stands.

### Case 474.1 — The frame and the promise of the librarian's run

> **given:**
> `rule-documentation` — the frame of the librarian: its inputs, its bans and its refusals
> **＋** `rule-synthesis` — the synthesis section of the frame
> **＋** `rule-index-check` — the index lines of the frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from both rules
> **＋** `estimate-documentation-completes` — the promise of the phase, its Criterion replaced whole
> **＋** `guppi/generate.py` — the script whose error can name an archived page
> **＋** `guppi/`, `tests/`, `Makefile` — the scripts' own files the librarian may read
> **＋** `vault/archive/`, `vault/archive/**/<slug>.md` — the archive, and the one Glob that finds a page in it by slug; the archive is never searched

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

> **then:**
> `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
> **＋** The librarian read only the following, and nothing else:
> - `handoff.md`, the yamls that `guppi materialize` named, the index lines and `tags.md`;
> - a file where the harness saved the output of one of the librarian's own commands because the output was too long to show;
> - the wiki pages it names in the report, each with the outcome and one of the reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief);
> - a page under `vault/archive/` found by the Glob `vault/archive/**/<slug>.md` for a slug that a script named in an error, named in the report with the error;
> - the unticked `- [ ]` lines of the `spec.md` files, for Readings due and Next session;
> - of the ledger, only the count of its lines and the lines the yaml does not account for, named in the report.
>
> It read no other part of a Spec, no plan, no Decision page, and no `materialize.yaml` that `guppi materialize` did not name. The `Makefile`, `guppi/` and `tests/` are the scripts' own files and may be read.
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
> **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
> **－** The librarian refuses an instruction of the handoff to repair a yaml entry, to read the ledger beyond the one read above, a Spec beyond its `- [ ]` lines or a Decision page, to search the archive, or to open an archived page that no script named in an error. It names what was asked and why in the report, and the refusal does not stop the run.
> **－** The librarian never searches `vault/archive/`: no Grep, `grep`, `find` or `ls` runs over it, and no Glob other than `vault/archive/**/<slug>.md` for a slug a script named in an error.

````then
update:
- slug: rule-documentation
  replace:
  - old: Never read `ledger.md`, `plan.md`, `wiki/decisions/` or `vault/archive/`, nor
    new: Never read `ledger.md`, `plan.md` or `wiki/decisions/`, never search `vault/archive/`, nor read
  - old: name that read in the report (case 349).
    new: 'name that read in the report (case 349). When a script names a slug in an error and you say why it failed, find its page under `vault/archive/` only by the Glob `vault/archive/**/<slug>.md`, open it, and name the page in the report; no other Glob, Grep, `grep`, `find` or `ls` runs over the archive (case 474.1). When the harness saves the output of one of your commands to a file because the output is too long to show, read that file: it is the output of your command (case 474.1).'
  - old: a Spec beyond its unticked lines, a decision page or the archive — you do not
    new: a Spec beyond its unticked lines, a decision page, a search of the archive or an archived page that no script named in an error — you do not
  change: the librarian finds an archived page by the Glob of the slug a script named in an error, never searches the archive, and reads the saved output of its own command (case 474.1)
- slug: rule-synthesis
  replace:
  - old: 'Mark each entry you add with `librarian: synthesis`.'
    new: |-
      Mark each entry you add with `librarian: synthesis`. Read no `materialize.yaml` other than the ones `guppi materialize` names, and look for no earlier entry: the entries of the synthesis have these forms (case 474.1).

      ```yaml
      # a new Insight from two lessons of one cause
      - kind: create
        category: insights
        slug: insight-<area>-<pattern>
        origin: <the origin of the new lesson entry>
        fields: {type: insight, pattern: <the shared cause>, children: [<lesson-a>, <lesson-b>]}
        tags: [<the union of the tags of both lessons>]
        sections: {Pattern: <text>, Proposal: <text>}
        librarian: synthesis
      # right after the create, only when the lesson entry carries addressed_by
      - kind: update
        category: insights
        slug: insight-<area>-<pattern>
        origin: <the origin of the new lesson entry>
        set: {status: actioned, addressed_by: decision-case-N}
        change: born actioned, its cause closed by case N (synthesis)
        librarian: synthesis
      # an existing Insight of the same pattern
      - kind: update
        category: insights
        slug: <the live Insight>
        origin: <the origin of the new lesson entry>
        set: {children: [<its children>, <the new lesson>]}
        change: child <the new lesson> added (synthesis)
        librarian: synthesis
      # set also takes status: open, or addressed_by: decision-case-N, as the rule above says
      # each lesson that joins an Insight
      - kind: update
        category: lessons
        slug: <lesson-a>
        origin: <the origin of the new lesson entry>
        set: {status: clustered, insight: <the Insight>}
        change: clustered under <the Insight> (synthesis)
        librarian: synthesis
      ```
  change: the synthesis shows the form of each of its entries and reads no yaml that materialize did not name (case 474.1)
- slug: estimate-documentation-completes
  set:
    status: pending
  change: the Criterion replaced whole — an archived page found by the Glob of the slug a script named in an error, the archive never searched, the saved output of the librarian's own command allowed, no yaml that materialize did not name (case 474.1)
````

```tasks
- [x] update `rule-documentation`
- [x] update `rule-synthesis`
- [x] update `estimate-documentation-completes`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-documentation-completes` — `make test-documentation` and the live reading of the transcript of the librarian's run in a later session
```

### Case 474.2 — The synthesis promise bans the archive at synthesis only

> **given:**
> `estimate-synthesis-clusters` — the promise of the synthesis, its Criterion replaced whole
> **＋** `rule-synthesis` — the synthesis section of the frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file that holds the synthesis
> **＋** `materialize.yaml` — the yaml the synthesis appends its entries to
> **＋** `vault/wiki/lessons/`, `vault/wiki/insights/` — the folders the Greps of the synthesis run over
> **＋** `vault/archive/` — the archive, which the synthesis does not read

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The report names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, and the comparisons made against their lines, by meaning.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
> **＋** A lesson without a pair stays `new`.
> **－** The synthesis reads no file under `vault/archive/`: an actioned Insight stays live with its pattern in its index line.

```then
update:
- slug: estimate-synthesis-clusters
  set:
    status: pending
    method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries
  change: the Criterion replaced whole — the ban on the archive is the synthesis's, not the whole run's; the base text and the block of case 147.4 folded into one Criterion (case 474.2)
```

```tasks
- [x] update `estimate-synthesis-clusters`
- [ ] read `estimate-synthesis-clusters` — by hand, the yaml and the report of a live librarian run with at least two lesson entries, in a later session
```

## Deferred

## Case 475 — The Spec hook keeps the body of a Case rebuilt as a parent

> **context:**
> Case 471 was ratified whole, then built again after pre-spec as a parent with sub-cases 471.1 and 471.2 and ratified again. The hook of `rule-spec-write` replaced the parent's prose in the plan file from the new answer, but kept the old body of 471 — its `given`, `when`, `then`, `then` block and `tasks` — under the parent heading. The old `replace` pairs used up the anchors, `guppi ratified` refused 471.1, and the Case had to be superseded by Case 474 (lesson `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`).

> **problem:**
> A ratified Case that is built again as a parent with sub-cases cannot be written into the Spec: the hook keeps the sections the new answer leaves to its sub-cases, and the only way out is a new Case id.

```then
defer:
  - slug: rule-spec-write
    type: rule
    purpose: The Spec hook, writing a Case built again as a parent with sub-cases, drops the body the new answer leaves to its sub-cases, so the Case keeps its id
```
