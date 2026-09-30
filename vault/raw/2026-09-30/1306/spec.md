<!-- approved 17:02:07 · session 96eeee58 -->

# Spec — session 1306, 2026-09-30

## Case 541 — The supersedes row of the glossary says which defers a supersede clears

> **context:**
> The table in the `## Terms` section of `entity-glossary` gives one row per term: the term, its meaning in one line, and the page that defines it. `uv run guppi glossary` writes `vault/wiki/glossary.md` from this table at the librarian's run, and `/hi` loads that file into every working session. This session a reading of `estimate-glossary-terms-defined` came back failed on one row. The row `ref`, `slug`, `supersedes` says that each `{supersedes:case N}` block marks every entry of its Case superseded and clears its `deferred_by`. `rule-case-protocol` says that `generate` clears a defer only from the pages that the superseding Case names. The docstring of `guppi/generate.py` says the same: a target that the superseding Case does not names keeps its `deferred_by` (case 467.3). So when an old defer points at two pages and the new Case names one of them, the other page stays in the backlog, but the row says it leaves. The same reading found that the other rows agree with their pages, the rows that case 535 rewrote among them. The row `deferred_by`, the field text of `rule-rules-schema` and a sentence of `rule-entities-schema` also say that a `supersedes` clears `deferred_by`, and they do not say that the page must be named. The row copies its page word for word, so the reading counted no contradiction there. The person chose to fix only the row the reading found, so these three stay as they are. This is an `update`, so no vault query was run. The frame holds no hook. The Estimates of `rule-glossary` promise the render, the check of the file and the ticks, not the content of the rows, so they are not touched. The Criterion of `estimate-glossary-terms-defined` still says what the rows must meet, so it is not replaced. Its next reading comes at a later `/hi`, after the librarian's run writes the row. For that reason the Case holds no `read` line, as case 535 held none.

> **problem:**
> A row of the glossary, a file that every session loads, says that a supersede clears every defer of the Case it names. The code and `rule-case-protocol` clear a defer only from the pages that the new Case names. The wording of the row must change to agree with the page.

> **given:**
> `entity-glossary` — the table of terms, whose row this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, loaded by `/hi`
> **＋** `rule-glossary` — renders the table and stops the write when a row is off its form
> **＋** `rule-case-protocol` — the `where` page of the row, which says from which pages a supersede clears a defer
> **＋** `guppi/generate.py` — its docstring says which targets lose their `deferred_by` on a `supersedes`

> **when:**
> A reader reads the row `ref`, `slug`, `supersedes` of `vault/wiki/glossary.md` at `/hi`, after `uv run guppi glossary` wrote it from `entity-glossary` at the librarian's run.

> **then:**
> The row says that each `{supersedes:case N}` block marks every entry of its Case superseded, and that `generate` clears a defer only from the pages that a decision line of the superseding Case names, as `rule-case-protocol` and `guppi/generate.py` say.
> **－** No other row of `entity-glossary` changes, the row `deferred_by` included, and no row is added or removed.

```then
update:
- slug: entity-glossary
  replace:
  - old: each of which marks every entry of its Case superseded and clears its `deferred_by` (cases 200.2, 429)
    new: each of which marks every entry of its Case superseded; `generate` clears a defer only from the pages that a decision line of the superseding Case names (cases 200.2, 429, 467.3)
  change: 'the row ref, slug, supersedes: a supersede clears a defer only from the pages the superseding Case names (case 541)'
```

```tasks
- [x] update `entity-glossary` — the row `ref`, `slug`, `supersedes` says which defers a supersede clears
- [x] `uv run guppi glossary`
```

## Case 542 — A short defer is written with no Retro moment

> **context:**
> When the person defers a decision, the `Stop` hook of `rule-spec-write` writes it in the short form under `## Deferred`. It uses the plan file while `spec.md` in the session's folder does not stand, and `spec.md` once it stands. Case 531.14 gave a short defer one moment, the close of Plan Mode: Retro puts nothing off, and what it would put off is a line of `handoff.md`. `rule-case-protocol`, `rule-retro`, the `retro` skill and the glossary row Retro already say this. Five texts still name Retro as the moment of a defer. The Purpose of `rule-spec-capture` says the hook writes a defer-only Case "at Retro", and so does the docstring of `guppi/spec.py`, which it mirrors (case 200.4). The "How it works" section of `rule-spec-write` and the docstring of `guppi/ratified.py` say it too. So does the Criterion of `estimate-spec-write-writes-a-defer`. The code comments in `guppi/ratified.py` and `guppi/materialize.py` and a test name in `tests/test_ratified.py` say the same. Case 531.14 named `rule-spec-write` in its `given` but gave it no `update`. The hook's behaviour stays: it still writes a defer into `spec.md` once that file stands. After case 531.14 no step of the protocol reaches that path, but that does not make any sentence false once "at Retro" is gone. The Criterion of `estimate-spec-write-writes-a-defer` is replaced whole, since it names Retro. Two of its lines change on purpose. The first line no longer names Retro or Plan Mode as the moment: it names only whether `spec.md` stands. The exception on the ratified copy `<plan>.ratified.md` goes, because the hook has written no such copy since case 445.2. Its other half stays: the check after the write does not run on a defer. The other lines are carried word for word. The other Estimates of `rule-spec-write` and of `rule-spec-capture` do not name Retro and are not touched. The History lines that name Retro stay: they record what was decided then. The open defer on `rule-spec-write` by case 475 is a different bug, about a Case built again as a parent. It stays in the backlog, and this Case does not supersede it. This Case creates no page, so the vault query was not run.

> **problem:**
> Two pages, an Estimate and the code still say the hook writes a short defer at Retro, and Retro puts nothing off since case 531.14. Each such sentence is false and must be corrected without changing what the hook does.

> **given:**
> `rule-spec-write` — the `Stop` hook that writes a short defer, its "How it works"
> **＋** `estimate-spec-write-writes-a-defer` — the promise that the hook writes a short defer, its Criterion replaced whole
> **＋** `rule-spec-capture` — the writers of `spec.md`, its Purpose
> **＋** `guppi/ratified.py` — the hook, its docstring and the comment on the target of a defer
> **＋** `guppi/spec.py` — the docstring that names the writers of `spec.md`
> **＋** `guppi/materialize.py` — the comment on the short form in the check for an incomplete Case
> **＋** `tests/test_ratified.py` — the test of a defer written into `spec.md`
> **＋** `rule-case-protocol` — a short defer has one moment, the close of Plan Mode

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while `spec.md` in the session's folder does not stand, and of that `spec.md` once it stands: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **＋** A key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
> **＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
> **－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
> **－** The check after the write does not run on the Case.

```then
update:
- slug: rule-spec-capture
  replace:
  - old: removes a superseded Case, and writes a defer-only Case at Retro under `## Deferred` (cases 421.1, 441)
    new: removes a superseded Case, and writes a defer-only Case under `## Deferred` (cases 421.1, 441, 542)
  change: 'the Stop hook of rule-spec-write writes a defer-only Case under ## Deferred with no Retro moment; Retro puts nothing off (case 542)'
- slug: rule-spec-write
  replace:
  - old: under `## Deferred` of the plan file, or of `spec.md` in the session's folder once that file stands, at Retro; the check after the write does not run on it (case 421.1)
    new: under `## Deferred` of the plan file, or of `spec.md` in the session's folder once that file stands; the check after the write does not run on it (cases 421.1, 542)
  change: 'a short defer goes under ## Deferred of spec.md once it stands, with no Retro moment (case 542)'
- slug: estimate-spec-write-writes-a-defer
  set:
    status: pending
  change: the Criterion replaced whole — a defer goes into spec.md once it stands, with no Retro moment; the clause on the ratified copy dropped (case 542)
```

```tasks
- [x] update `rule-spec-capture` — the writers of `spec.md`: a defer-only Case with no Retro moment
- [x] update `rule-spec-write` — a short defer goes into spec.md once it stands, with no Retro moment
- [x] update `estimate-spec-write-writes-a-defer` — the Criterion replaced whole: no Retro moment, no ratified copy
- [x] `guppi/spec.py` — the docstring: the `Stop` hook of `rule-spec-write` writes a defer-only Case under `## Deferred`, "at Retro" dropped
- [x] `guppi/ratified.py` — the docstring of the defer: "(Retro)" dropped; the comment on the target of a defer: it goes to `spec.md` once that file stands, with no Retro
- [x] `guppi/materialize.py` — the comment on the check for an incomplete Case names the short form of a defer, not of Retro
- [x] `tests/test_ratified.py` — `test_write_a_defer_at_retro_goes_into_the_spec_of_the_folder` renamed to `test_write_a_defer_once_the_spec_stands_goes_into_it`, its body unchanged
- [x] `uv run pytest tests/test_ratified.py -k defer` green
- [x] read `estimate-spec-write-writes-a-defer` — `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change, in a later session
```

## Case 543 — Two faults in the form of a round of case-guppi

> **context:**
> Two readings failed on the rounds of questions that `case-guppi` writes. First, `estimate-case-build-writes-a-plain-round` failed because the first round on Case 534 ended, after its last question, with a list of the files the agent checked, named by session ids alone. The frame `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, already says that a round holds nothing else but the context of a first round. But Claude Code also gives every sub-agent a general note: in its final response, share the file paths that are relevant to the task. The frame does not say that this note does not apply to a round. The list does not help the person, and it does not help the main agent either: the main agent shows the round translated line by line, it reads none of those files to do so, and it asks `case-guppi` for a fact when it needs one.
> Second, `estimate-skill-grill-me-asks-in-rounds` failed because the label `**Options:**` came out indented by four spaces in most rounds. This session saw the same in the rounds on Cases 541 and 542. Markdown shows a line indented four spaces after a blank line as code. The cause is the question template of `.claude/skills/grill-me/SKILL.md`, rendered from `rule-skill-grill-me`. The whole template is an indented code block, and its Options label has eight spaces where the `**Now:**` line and each option have four. `case-guppi` copies it as it stands.
> The eight spaces came from the page writer. `replace_hits` of `guppi/generate.py` splits the `old` of a pair into its words and joins them with any whitespace, so the leading spaces of `old` are never matched. The pair of case 511.1 had an `old` that opened with four spaces and a `new` that opened with four spaces. The match started at the first word, so the page kept its four spaces and `new` added four more. Pre-spec replays each pair by the same function (`check_pairs` of `guppi/prespec.py`), and the Case check hook of `rule-case-check` runs the same checks through `judge`. So neither of them could see the doubled indent. No live `materialize.yaml` under `vault/raw/` holds a pair whose `old` or `new` opens with whitespace, so no signed pair waits on the old matching.
> In the frame, `estimate-case-build-writes-the-case` already promises that a round holds nothing else. Its Criterion stands, and so does that of `estimate-case-build-writes-a-plain-round`: the person chose to replace no Criterion for the note after a round. The Criterion of `estimate-skill-grill-me-asks-in-rounds` already asks for the label alone on its line, so it stands too. `estimate-generate-writes` promises a `replace` with whitespace collapsed and exactly one occurrence, and `estimate-prespec-simulates-the-pairs` promises a replay with whitespace collapsed as `generate` collapses it. Both stay true: the leading spaces never make an anchor miss or hit twice. So the new promises go to new Estimates, and those two Criteria are not replaced. The Criterion of `estimate-case-check-sends-back-a-faulty-case` says the hook runs `judge` of `guppi/prespec.py`, so a new finding of `judge` reaches it with no change there. Both new slugs are free, and each `create` carries a `ref`, so no vault query ran. No open backlog line of the Frontier names a page of this Case.

> **problem:**
> A round of `case-guppi` can end with a list of files, because a general instruction of Claude Code asks for one and the frame does not set it aside. The grill-me template shows the `**Options:**` label four spaces too deep, so each round shows it as code. The writer made that indent: the leading spaces of an `old` are never matched, and the leading spaces of a `new` are added after the ones on the page. Neither pre-spec nor the Case check catches a pair that doubles an indent.

### Case 543.1 — A round of case-guppi ends with its last question

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the frame rendered from it

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The round ends with the `➡️` line of its last question and the lines of a list under it.
> **＋** No horizontal rule, no list of the files `case-guppi` read and no note stand after it, even where a general instruction of Claude Code asks a sub-agent to share file paths.
> **－** A first round still opens with its `**Context:**` paragraph before its first question.

```then
update:
- slug: rule-case-build
  replace:
  - old: no step of confirmation follows the last round.
    new: 'no step of confirmation follows the last round. A round ends with the `➡️` line of its last question and the lines of a list under it: no horizontal rule, no list of the files you read and no note stand after it, even where a general instruction asks you to share file paths.'
  change: 'a round of case-guppi ends with its last question: no list of files and no note after it (case 543.1)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-writes-a-plain-round` — in a later session after the render: one first round and one later round of `case-guppi` read in the chat against the Criterion
```

### Case 543.2 — The Options label of the grill-me template stands at the indent of the other lines

> **given:**
> `rule-skill-grill-me` — the rule whose Render is the grill-me skill and its question template
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill rendered from it
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by its `skills` field

> **when:**
> `uv run guppi render` writes `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`, and `case-guppi`, which loads it by `.claude/agents/case-guppi.md`, answers with a round of questions.

> **then:**
> In the question template the label `**Options:**` stands at the indent of the `**Now:**` line and of each option.
> **＋** In a round the label stands alone on the line before the first option, at column 0, and shows as bold text, not as code.
> **－** No other line of the template changes.

```then
update:
- slug: rule-skill-grill-me
  replace:
  - old: |-
      > <the quoted words, as the source holds them>

              **Options:**
    new: |-
      > <the quoted words, as the source holds them>

          **Options:**
  change: the Options label of the question template stands at the indent of the other lines (case 543.2)
```

```tasks
- [x] update `rule-skill-grill-me`
- [x] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
- [x] read `estimate-skill-grill-me-asks-in-rounds` — in a later session after the render: `uv run guppi render --check`, then one round of `case-guppi` read in the chat against the Criterion
```

### Case 543.3 — A replace old that opens with spaces takes the spaces before its first word

> **given:**
> `rule-page-generation` — the rule of the writer of pages
> **＋** `guppi/generate.py` — `replace_hits` and `replace_once`, the one matching rule of a `replace` pair
> **＋** `guppi/prespec.py` — `check_pairs`, which replays the pairs by the same function
> **＋** `tests/test_generate.py` — the tests of the writer
> **＋** `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `estimate-generate-replace-takes-the-leading-indent` — the promise this sub-case creates

> **when:**
> `guppi generate` applies a `replace` pair of an `update` entry to a page, or `check_pairs` of `guppi/prespec.py` applies it to a copy of the page, both by `replace_once` of `guppi/generate.py`.

> **then:**
> An `old` that opens with a space or a tab matches, besides its words, every space and tab on the page just before its first word, and `new` takes their place.
> **＋** An `old` that opens with neither matches from its first word, and the spaces and tabs before it on the page stay.
> **＋** Between the words of `old` whitespace stays collapsed: a line break matches any whitespace.
> **－** The spaces and tabs before the first word never make an anchor miss or hit twice: a pair that hits the page once without them still hits it once.

```then
create:
- slug: estimate-generate-replace-takes-the-leading-indent
  ref: rule-page-generation
  kind: QA
  purpose: Whether a replace pair whose old opens with spaces or tabs leaves the indent of its new on the page, and no indent added twice
  method: 'pytest in tests/test_generate.py against a temp vault: an old that opens with spaces over an indented line, one that opens with none, and one whose hit count is the same with and without its leading spaces'
  tags:
  - harness
  - workflow
update:
- slug: rule-page-generation
  change: a replace old that opens with spaces or tabs takes the spaces and tabs before its first word on the page (case 543.3)
- slug: rule-case-protocol
  replace:
  - old: and one that misses or hits twice fails the entry)
    new: and one that misses or hits twice fails the entry; an `old` that opens with spaces or tabs takes the spaces and tabs before its first word on the page too, so the indent of `new` replaces them, and a `new` that opens with spaces or tabs takes an `old` that opens with them, or pre-spec reports the pair — case 543)
  change: how the leading spaces and tabs of a replace pair match (case 543.3)
```

```tasks
- [x] update `rule-page-generation`
- [x] create `estimate-generate-replace-takes-the-leading-indent`
- [x] update `rule-case-protocol`
- [x] `guppi/generate.py`: in `replace_hits`, an `old` that opens with a space or a tab gets a pattern that takes the spaces and tabs before its first word; the docstrings of `replace_hits` and `replace_once` say so
- [x] `tests/test_generate.py`: an `old` and a `new` that both open with four spaces over a line indented four spaces leave four; an `old` with no leading space leaves the page's spaces; the hit count of an anchor is the same with and without its leading spaces
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-generate-replace-takes-the-leading-indent`
```

### Case 543.4 — Pre-spec and the Case check report a pair that adds an indent twice

> **given:**
> `rule-prespec` — the rule of pre-spec, whose Render is `.claude/skills/pre-spec/SKILL.md`
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from it
> **＋** `guppi/prespec.py` — `check_pairs` and `judge`
> **＋** `guppi/generate.py` — the home of the predicate, beside the matching rule of a pair
> **＋** `tests/test_prespec.py` — the tests of pre-spec
> **＋** `rule-case-check` — its hook runs `judge` of `guppi/prespec.py` on each answer of `case-guppi`
> **＋** `estimate-prespec-catches-an-indent-added-twice` — the promise this sub-case creates

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads a plan whose Cases carry `replace` pairs, or the hook of `rule-case-check` runs `judge` of `guppi/prespec.py` over an answer of `case-guppi`.

> **then:**
> A `replace` pair whose `new` opens with a space or a tab while its `old` opens with neither gives one finding with its Case, the page's slug and the opening of its `old`.
> **＋** The predicate lives in `guppi/generate.py`, beside the matching rule of a pair, and `check_pairs` of `guppi/prespec.py` imports it.
> **＋** The hook of `rule-case-check` sends such a Case back to `case-guppi` before the person sees it.
> **－** A pair whose `old` and `new` both open with spaces or tabs, or whose `new` opens with neither, gives no such finding.
> **－** `guppi generate` applies such a pair as before: the finding stands at pre-spec and at the check of the Case only.

```then
create:
- slug: estimate-prespec-catches-an-indent-added-twice
  ref: rule-prespec
  kind: QA
  purpose: Whether pre-spec, and the Case check through judge, report a replace pair whose new opens with spaces or tabs while its old opens with neither
  method: 'pytest tests/test_prespec.py on a temp plan over temp pages: a pair whose new opens with spaces and old with none, one where both open with spaces, one where neither does'
  tags:
  - harness
  - workflow
update:
- slug: rule-prespec
  replace:
  - old: judged on its own and not applied to the copies (case 487.1).
    new: 'judged on its own and not applied to the copies (case 487.1). It prints one line too for every `replace` pair whose `new` opens with a space or a tab while its `old` opens with neither, with its Case, the page''s slug and the opening of its `old`: the page keeps its own indent before the match, and the indent of `new` would stand after it (case 543.4).'
  change: pre-spec reports a replace pair whose new opens with spaces or tabs while its old does not (case 543.4)
```

```tasks
- [x] update `rule-prespec`
- [x] create `estimate-prespec-catches-an-indent-added-twice`
- [x] `guppi/generate.py`: a predicate beside `replace_hits` that says whether a pair adds an indent twice
- [x] `guppi/prespec.py`: `check_pairs` imports the predicate and gives the finding for each pair it judges true
- [x] `tests/test_prespec.py`: the three pairs of the method
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-catches-an-indent-added-twice`
```

## Case 544 — case-guppi checks its finished Case, and its recommend records the rounds onto the Decision page

> **context:**
> `case-guppi` asks the person rounds of questions and then writes the Case from the answers and from its reading of the frame. The frame is the pages and files that the Case's `given` names. Two faults of this step were found only at pre-spec, each after ratification, and each cost a second ratification. In session 0248 the person chose an option saying that the brief of `/carry` lists no Cases, and the built Case took its Cases from the open lines of the Frontier (`lesson-case-build-built-case-departs-from-the-chosen-option`). The context of Case 534 said the Case changed all three texts that count the children of `rule-settings`, but the Purpose of `rule-hook-registry` held the same count (`lesson-case-build-frame-count-claimed-over-a-partial-search`). The frame reads only the pages that `given` names. Nothing compares the built Case with the options the person chose, and nothing holds those choices once the session ends: no vault file records the rounds, `recommend` stays in the Case file, and the Decision page carries only `## Problem`.
> The two lessons are the newest children of `insight-case-build-promise-lines-compared-by-no-check` and `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`. Both Insights are open in the backlog, each one reopened by its lesson after an earlier Case had actioned it (cases 472.3, 388). The first Insight also names a Criterion replaced whole that drops a line. The note of pre-spec from case 472 already covers that half, and 544.1 closes the half about the chosen option. The draft rule `rule-case-build-checks-its-sub-cases`, put off by case 480, asks for a side-by-side reading of the sub-cases that change one page before the Case is shown. The person took it up here. A Grep of `vault/wiki/` finds its slug only in `brief.md`, `backlog.md`, `log.md` and `decision-case-480`. The two lessons come from another session and get no mark. Setting each Insight `actioned` lets the cascade of `generate` archive its clustered lessons.
> The person asked that the rounds reach the Decision page, and that this stay one Case with the form of `recommend` rather than become a Case of its own. On the shown Case the person objected that some items of `recommend` showed an earlier recommendation that a later question had replaced, such as `## Note`. Each item now gives the latest recommendation and the latest answer, and 544.2 makes that the rule. Each question keeps its own item, so the check of 544.3 still finds every title.
> The frame gave these findings. `SPEC_SECTIONS` of `guppi/ratified.py` leaves `recommend` out of the Spec, so `materialize` never sees it. A parent Case has no ledger line and so no Decision page: there is no `decision-case-534`. The `decision` class of `guppi/lint.py` refuses a Decision page with no kind list. Its `origin` check looks for `[case N]` in the ledger, which a parent does not have. `guppi/materialize.py` fills a sub-case's `problem` and `recommend` from its parent and needs `problem` on every record. `generate` writes `## Context` for a record whose `case_text` has no `given`. A parent record carries the parent's `given` when the parent has one, and a record with `children` never gets `## Context`. `estimate-materialize-lifts-when-and-then` still holds, because a Case with its own `given` still carries it in its `case_text`, and a sub-case without one carries its parent's. The row `Decision page` of the glossary, the rule that bold is for section labels and operands only, and the sentences of `rule-case-protocol`, `rule-case-check` and `rule-decisions-schema` on `recommend`, the kind lists and the body of a Decision page would become false, so each gets a pair here.
> These Estimates speak of the change, and each one's Criterion is replaced whole: `estimate-spec-write-copies-the-ratified-case`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-case-protocol-case-form`, `estimate-materialize-assembles`, `estimate-generate-writes-the-decision-page`, `estimate-decisions-schema-checked` and `estimate-lint-finds-a-broken-link`. The reading of `estimate-spec-write-reaches-the-approved-spec` on this session's Frontier then waits for a later session. The lines of these Criteria that are not carried word for word are the lines this Case changes on purpose. The then lines that the check found to share words across sub-cases name different pages and different promises. Some Estimates stand. `estimate-case-build-writes-the-case` stands, because case-guppi still reads each page `given` names, and the new checks are a new promise. `estimate-case-check-sends-back-a-faulty-case` stands, because the two new findings are sent back like any other. This session's cases 543.1 and 543.3 change `rule-case-build` and `rule-case-protocol`, and case 542 changes `rule-spec-write`. The pairs here touch other text.
> No reader needs an old form. The two new findings send a Case back to `case-guppi`, and nothing is lost. `materialize` never rewrites a `materialize.yaml`. Decision pages written before are not rewritten. This session's Spec was written by the old Spec hook and holds no `recommend`, so no page of this session gets `## Recommend`. If the code of 544.6 to 544.9 is built before the librarian's run, this session's pages do get the parent pages, `parent`, and sub-case pages with no `## Problem`. The full new shape starts with the Cases of the first session after the code is built. Every `create` carries a `ref`, so no vault query ran, and a Glob finds each new slug free.
> Not done: a similarity search by vectors, any judgment of what an answer says, and a hook that writes the rounds itself. The report of `ask-guppi` at pre-spec stays as a second net.

> **problem:**
> `case-guppi` can build a Case that departs from the option the person chose, and it can sign a claim about every text in the vault after reading only the pages it named. Two sub-cases of one Case can also contradict each other on one page. All three faults are found only at pre-spec, after ratification. The choices the person makes in the rounds are held by no page. The Decision page shows only the problem, and a Case with sub-cases has no page of its own.

### Case 544.1 — case-guppi checks its finished Case before it answers

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the frame rendered from it
> **＋** `.claude/agents/ask-guppi.md` — the recipe of the index lines, judged by meaning
> **＋** `rule-case-build-checks-its-sub-cases` — the rule put off by case 480, taken up here
> **＋** `insight-case-build-promise-lines-compared-by-no-check` — the Insight of the departed option
> **＋** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — the Insight of the claim wider than its search
> **＋** `estimate-case-build-checks-the-finished-case` — the promise this sub-case creates

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one.
> **＋** Where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit.
> **＋** For a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands, and a claim of `context` about every text names the search it rests on.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
create:
- slug: estimate-case-build-checks-the-finished-case
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
  method: 'by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, two sub-cases whose texts on one page contradict; the count of each in the reading line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: When no fork is open, answer with the Case in the chat form of the schema,
    new: |-
      Before you answer with the Case, check it whole, its sub-cases with it. Put each option the person chose in your rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and fix the Case where it departs; where the frame shows after a round that a chosen option cannot hold as written, answer with a round on that point, never with a Case of another behaviour. For each page whose text the change makes false, Grep the live pages of `vault/wiki/` outside `decisions/`, and the code, for its slug, and read each hit that `given` does not name around the line of the hit; a hit in a History line, in `log.md` or in `brief.md` is not read. For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. Each hit the change makes false enters the Case, or `context` says why it stands, and a claim of `context` about every text names the search it rests on. Read side by side the finished new texts of all your sub-cases that change one page, and fix a contradiction between them (case 544.1).

      When no fork is open, answer with the Case in the chat form of the schema,
  change: 'case-guppi checks its finished Case before it answers: the chosen options, the pages that name a changed slug, the sub-cases on one page side by side (case 544.1)'
- slug: insight-case-build-promise-lines-compared-by-no-check
  set:
    status: actioned
    addressed_by: decision-case-544.1
  change: 'actioned: the half on a replaced Criterion is closed by the note of pre-spec (case 472); case-guppi checks its finished Case against the options the person chose before it answers (case 544.1)'
- slug: insight-workflow-fact-signed-from-a-check-that-does-not-cover-it
  set:
    status: actioned
    addressed_by: decision-case-544.1
  change: 'actioned: case-guppi searches the live pages for each slug the change makes false, and a claim about every text names its search (case 544.1)'
delete:
- slug: rule-case-build-checks-its-sub-cases
  impact: its one sentence stands in the frame of rule-case-build; in vault/wiki/ only brief.md, backlog.md, log.md and decision-case-480 name it, and the supersede of case 480 retires that defer
```

```tasks
- [x] update `rule-case-build`
- [x] create `estimate-case-build-checks-the-finished-case`
- [x] delete `rule-case-build-checks-its-sub-cases`
- [x] update `insight-case-build-promise-lines-compared-by-no-check`
- [x] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-checks-the-finished-case`
```

### Case 544.2 — The recommend of a Case records the rounds

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the frame rendered from it
> **＋** `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `estimate-case-build-records-the-rounds-in-recommend` — the promise this sub-case creates

> **when:**
> `case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, followed by a line `Recommended:` with what the agent recommended and a line `Answer:` with the person's answer in English.
> **＋** Where a later question changed the recommendation or the answer of an earlier one, the earlier item gives the latest recommendation and the latest answer.
> **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
> **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
> **＋** An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, and the other items stand in the parent's `recommend`.
> **＋** A Case with sub-cases carries `problem` on the parent only.
> **－** No item quotes the person's words word for word.

```then
create:
- slug: estimate-case-build-records-the-rounds-in-recommend
  ref: rule-case-build
  kind: QA
  purpose: Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the latest recommendation, the latest answer in English — a sub-case with its own items and no problem
  method: 'by hand: the Case files of a later session after the render, each recommend read against the rounds of its Case in the chat'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: Write no file and no ledger line.
    new: 'Write `recommend` as the schema sets it: one item per question of your rounds on the Case, its first line the title of the question in bold as the round wrote it, then a line `Recommended:` with what you recommended and a line `Answer:` with the person''s answer in English, both the latest where a later question changed them; one item `**Change**`, with a line `Asked:` and a line `Taken:`, for each change the person asked for on a Case you built; with no round, one item of a line `Recommended:` and the line `Answer: ratified as built`. An item whose answer changed only one sub-case stands in a `recommend` under that sub-case''s heading, the others in the parent''s, and a sub-case carries no `problem` (case 544.2). Write no file and no ledger line.'
  change: case-guppi writes recommend as the record of its rounds, the latest recommendation and answer of each question, a sub-case with its own items and no problem (case 544.2)
- slug: rule-case-protocol
  replace:
  - old: '| `recommend` | yes | The agent''s suggestion. Not carried onto the Decision page. |'
    new: '| `recommend` | yes | The record of the choices: one item per question of the rounds of `case-guppi` — the question, what it recommended, the person''s answer in English, both the latest — one per change the person asked for on the shown Case, and, with no round, one item of the recommendation ratified as built; a sub-case carries the items that changed it alone (case 544.2). Carried onto the Decision page as `## Recommend` (case 544.7). |'
  - old: '`recommend` says the choice and why, the rejected option in one sentence (case 267).'
    new: '`recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a line `Recommended:` and a line `Answer:`, the person''s answer in English, both the latest where a later question changed them; a change the person asked for on the shown Case is an item `**Change**` with the lines `Asked:` and `Taken:`; a Case with no round has one item, a line `Recommended:` and the line `Answer: ratified as built` (case 544.2).'
  - old: bold is for section labels and operands only.
    new: bold is for section labels and operands only, and for the title of a question of a round and the title of an item of `recommend`, as the grill-me template sets it (case 544.2).
  - old: '`context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing one there (case 60).'
    new: '`context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing `context` or `given` there (case 60); `problem` stands on the parent only, and a sub-case carries its own `recommend` with the items whose answer changed that sub-case alone, the parent''s `recommend` the rest (case 544.2).'
  - old: The Case holds `context`, `problem`, `given`, `when`, `then`, the `then` block
    new: The Case holds `context`, `problem`, `recommend`, `given`, `when`, `then`, the `then` block
  - old: '`recommend` and `ratification` stay in the chat;'
    new: '`ratification` stays in the chat (case 544.5);'
  change: recommend is the record of the rounds and stands in the Spec, its item titles in bold; a sub-case carries its own items and no problem (cases 544.2, 544.5)
```

```tasks
- [x] update `rule-case-build`
- [x] update `rule-case-protocol`
- [x] create `estimate-case-build-records-the-rounds-in-recommend`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-build-records-the-rounds-in-recommend`
```

### Case 544.3 — The Case check requires each question of the rounds in recommend

> **given:**
> `rule-case-check` — the rule of the check of each answer of `case-guppi`
> **＋** `guppi/casecheck.py` — `uv run guppi casecheck --subagent`, the hook on `SubagentStop`
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `.claude/skills/grill-me/SKILL.md` — the question template whose title line the hook reads
> **＋** `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `estimate-case-check-requires-each-question-of-the-rounds` — the promise this sub-case creates

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

> **then:**
> `uv run guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
> **＋** A title that no item of a `recommend` of the top-level Case or of its sub-cases in the answer opens with, in bold, is a finding of the top-level Case that names the title, sent back and stored as any other finding.
> **－** An answer with no earlier round gives no such finding.
> **－** A title asked in more than one round is looked for once.
> **－** The words of an item after its title are not judged.

```then
create:
- slug: estimate-case-check-requires-each-question-of-the-rounds
  ref: rule-case-check
  kind: QA
  purpose: Whether the check of each answer of case-guppi sends back a Case whose recommend misses the title of a question of its rounds
  method: 'pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, an answer with no round; then by hand the first Case the hook sends back for a missing title'
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: only their presence, their order and the script of the name, `context` and `problem` of a Case, by the language finding of pre-spec
    new: only their presence, their order, the script of the name, `context` and `problem` of a Case, by the language finding of pre-spec, and the title of each item of `recommend` against the questions of the rounds (case 544.3)
  - old: An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored;
    new: For an answer that holds a Case, it reads besides the earlier outputs of the subagent in `agent_transcript_path` that hold no Case heading — its rounds — and takes the title of each question from its line `❓ **Q<n>** - **<title>**:`; a title that no item of a `recommend` of the top-level Case or of its sub-cases in the answer opens with, in bold, is a finding of the top-level Case, sent back and stored as any other finding; a title asked in more than one round is looked for once, and the words of an item after its title are not judged (case 544.3). An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored;
  change: the check of each answer of case-guppi requires the title of each question of its rounds in a recommend of the Case (case 544.3)
- slug: rule-case-protocol
  replace:
  - old: 'no script judges them: the person does'
    new: 'no script judges their text but for the titles of the items of `recommend`, which the hook of `rule-case-check` compares with the questions of the rounds (case 544.3): the person does'
  change: a script reads the titles of the items of recommend (case 544.3)
```

```tasks
- [x] update `rule-case-check`
- [x] update `rule-case-protocol`
- [x] create `estimate-case-check-requires-each-question-of-the-rounds`
- [x] `guppi/casecheck.py`: the pattern of a question line, the rounds read from the earlier outputs in `agent_transcript_path`, the finding for a title missing from every `recommend` of the answer; the docstring says so
- [x] `tests/test_casecheck.py`: the cases of the method
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-check-requires-each-question-of-the-rounds`
```

### Case 544.4 — The Case check refuses a problem in a sub-case

> **given:**
> `rule-case-check` — the rule of the check of each answer of `case-guppi`
> **＋** `guppi/casecheck.py` — `form_findings`, the check of the chat form
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `estimate-case-check-refuses-a-problem-in-a-sub-case` — the promise this sub-case creates

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case that has sub-cases, and `uv run guppi casecheck --subagent` checks the chat form of each Case of the answer.

> **then:**
> A sub-case of the answer that carries a `problem` section is a finding of that sub-case from `form_findings` of `guppi/casecheck.py`, sent back to `case-guppi` and stored as any other finding.
> **＋** A parent that lacks `problem` still gets its finding of a missing section.
> **－** A Case with no sub-cases keeps its `problem` with no such finding.

```then
create:
- slug: estimate-case-check-refuses-a-problem-in-a-sub-case
  ref: rule-case-check
  kind: QA
  purpose: Whether the check of each answer of case-guppi sends back a sub-case that carries its own problem
  method: 'pytest tests/test_casecheck.py -k problem: a sub-case with problem, a parent without problem, a Case with no sub-cases'
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: and that `ratification` holds one untagged fence of ledger lines and nothing else.
    new: and that `ratification` holds one untagged fence of ledger lines and nothing else; a sub-case that carries `problem` is a finding of that sub-case, since `problem` stands on its parent only (case 544.4).
  change: a sub-case that carries problem is a finding of the check of the answer (case 544.4)
```

```tasks
- [x] update `rule-case-check`
- [x] create `estimate-case-check-refuses-a-problem-in-a-sub-case`
- [x] `guppi/casecheck.py`: `form_findings` gives the finding for a sub-case that carries `problem`; the docstring says so
- [x] `tests/test_casecheck.py`: the cases of the method
- [x] read `estimate-case-check-refuses-a-problem-in-a-sub-case`
```

### Case 544.5 — The Spec holds recommend

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case into the Spec
> **＋** `guppi/ratified.py` — `SPEC_SECTIONS` and the writer of a Case's section of the Spec
> **＋** `tests/test_ratified.py` — the tests of the hook
> **＋** `guppi/materialize.py` — `tagged_blocks` and `item_keys`, which read the written blocks back
> **＋** `guppi/casecheck.py` — the comparison of a showing with the stored answer, which the hook imports
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of the Case whose sending the hook reads
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session once it stands
> **＋** `estimate-spec-write-copies-the-ratified-case` — the promise whose Criterion this sub-case replaces

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads `<plan>.checked.json` beside the plan file for the answer of `case-guppi` stored under Case N, and the session's transcript for the `SendUserFile` calls on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and for the last earlier reply that shows Case N with at least one of its sections.

> **then:**
> The hook writes the stored answer of Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then` as the answer holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `ratification` is not written.
> **＋** A sub-case's own `recommend` is written under its heading, and the `context`, `problem` and `recommend` of its parent come from the parent's stored answer.
> **＋** Each of the two blocks opens and closes with a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least, which `tagged_blocks` of `guppi/materialize.py` reads back whole; the same fence rule holds for the blocks it writes into `raw/<date>/<hi HHMM>/spec.md` once it stands, and for the `then` block of a short-form defer under `## Deferred`.
> **＋** No `SendUserFile` call on the file of Case N made after the time the store holds for Case N: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A last showing of Case N that differs from the stored answer in a section it shows — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
> **＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item, or a value that holds a backtick in an outer span not padded on both sides, is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` or `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
> **＋** No plan file in the event log, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys.
> **－** A reply with no showing of Case N is no refusal when the file of Case N was sent after the store.

```then
update:
- slug: rule-spec-write
  replace:
  - old: the heading, `context`, `problem`, `given`, `when` and `then` as they stand,
    new: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then` as they stand — a sub-case's own `recommend` under its heading (case 544.5) —
  - old: the `context` and `problem` of a sub-case's parent come from the parent's stored answer
    new: the `context`, `problem` and `recommend` of a sub-case's parent come from the parent's stored answer
  change: the Spec holds recommend (case 544.5)
- slug: estimate-spec-write-copies-the-ratified-case
  set:
    status: pending
  change: the Criterion replaced whole — the Spec holds recommend, a sub-case's own under its heading (case 544.5)
```

```tasks
- [x] update `rule-spec-write`
- [x] update `estimate-spec-write-copies-the-ratified-case`
- [x] `guppi/ratified.py`: `SPEC_SECTIONS` holds `recommend`, and the writer writes a sub-case's own `recommend` and the parent's from the parent's stored answer; the docstring says so
- [x] `tests/test_ratified.py`: a Case whose `recommend` reaches the plan file, a sub-case with its own `recommend`, a parent's `recommend` from its stored answer
- [x] read `estimate-spec-write-copies-the-ratified-case`
```

### Case 544.6 — materialize gives a parent Case its own record

> **given:**
> `rule-materialize` — the rule of the lift of the ledger and the Spec into one yaml
> **＋** `guppi/materialize.py` — `INHERITED`, the decision record and its needed sections
> **＋** `tests/test_materialize.py` — the tests of the lift
> **＋** `estimate-materialize-assembles` — the promise whose Criterion this sub-case replaces

> **when:**
> `uv run guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

> **then:**
> `materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented.
> **＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
> **＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
> **＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context` and `given` from its parent, never `problem`, `recommend` or `when`, and carries `parent`, the `decision` of its parent.
> **＋** A Case whose sub-cases have decision lines in the unit gets one decision record of its own: its `decision` and its `origin` named by the id of the Case, `case_text` with its `context`, `problem` and `recommend`, and its `given` when it has one, `children` the `decision` of each of its sub-cases in ledger order, and no `targets`.
> **＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
> **＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
> **＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
> **－** No entry of an Estimate is derived from a key of the item of a rule or an entity: an Estimate comes only from its own line.
> **－** A sub-case record without `problem` carries no `incomplete: [problem]`.

```then
update:
- slug: rule-materialize
  change: a sub-case reads no problem or recommend from its parent; a parent Case gets a decision record of its own with children and its given when it has one (case 544.6)
- slug: estimate-materialize-assembles
  set:
    status: pending
  change: the Criterion replaced whole — a sub-case reads no problem or recommend from its parent, and a parent Case gets its own record (case 544.6)
```

```tasks
- [x] update `rule-materialize`
- [x] update `estimate-materialize-assembles`
- [x] `guppi/materialize.py`: `INHERITED` holds `context` and `given`; a sub-case record carries `parent` and needs no `problem`; a parent Case with sub-case lines in the unit gets its own record with `children` and its `given` when it has one; the docstring says so
- [x] `tests/test_materialize.py`: a sub-case with no `problem` or `recommend` of its own, a parent record with `children` and no `targets`, with and without a `given` of its own, a Case with no sub-cases as before
- [x] read `estimate-materialize-assembles`
```

### Case 544.7 — generate writes the Recommend and the parent page

> **given:**
> `rule-page-generation` — the rule of the writer of pages
> **＋** `guppi/generate.py` — the writer of the Decision page
> **＋** `tests/test_generate.py` — the tests of the writer
> **＋** `guppi/materialize.py` — the writer of `materialize.yaml` and its decision records
> **＋** `vault/wiki/decisions/decision-case-<N>.md` — the Decision page it writes
> **＋** `estimate-generate-writes-the-decision-page` — the promise whose Criterion this sub-case replaces

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
> **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
> **－** The Decision pages already written are not rewritten.
> **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.

```then
update:
- slug: rule-page-generation
  replace:
  - old: The Decision page of a Case is written before its entries and carries the body of every defer (cases 52.4, 186.1);
    new: The Decision page of a Case is written before its entries and carries the body of every defer (cases 52.4, 186.1), and `## Recommend`, the `recommend` of the Case; a Case with sub-cases gets a page of its own before theirs, with `## Problem`, `## Recommend` and `children` and never `## Context`, and the page of each sub-case carries `parent` and no `## Problem` (case 544.7);
  change: the Decision page carries Recommend; a Case with sub-cases gets its own page, linked to theirs by children and parent (case 544.7)
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
  change: the Criterion replaced whole — Recommend on the page, a page for a parent Case with children and no Context, parent on a sub-case page and no Problem there (case 544.7)
```

```tasks
- [x] update `rule-page-generation`
- [x] update `estimate-generate-writes-the-decision-page`
- [x] `guppi/generate.py`: the Decision page writes `## Recommend`; a record with `children` gets its page first, with no kind list and no `## Context`; a record with `parent` gets the field and no `## Problem`; the docstring says so
- [x] `tests/test_generate.py`: a page with `## Recommend`, a parent page with `children` and no `## Context`, with and without a `given` of its own, a sub-case page with `parent` and no `## Problem`, a short-form defer as before
- [x] read `estimate-generate-writes-the-decision-page`
```

### Case 544.8 — The Decision schema takes Recommend, parent and children

> **given:**
> `rule-decisions-schema` — the rule whose Render is the schema of a Decision page
> **＋** `vault/wiki/decisions/schema.yaml` — the schema rendered from it
> **＋** `guppi/lint.py` — the reader of the schema
> **＋** `tests/test_schemas.py` — the tests of the schemas
> **＋** `cases/case-<N>.md` — the Case file in the folder of a Decision's `origin`
> **＋** `estimate-decisions-schema-checked` — the promise whose Criterion this sub-case replaces
> **＋** `entity-glossary` — the page whose Render is the glossary, with the row `Decision page`
> **＋** `vault/wiki/glossary.md` — the glossary rendered from it

> **when:**
> `guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`, and `guppi lint` reads a page of `vault/wiki/decisions/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by, parent, children`; values `status: current | superseded | archived`; the section `## History` required, `## Context`, `## Problem`, `## Recommend`, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
> **＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
> **＋** A Decision page without `## Context`, and one without `## Problem`, has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, the fields deliberately absent and the body paragraph; `examples` holds the example page.
> **＋** The file says that the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact.
> **＋** The file says that the Case file, `cases/case-<N>.md` in the folder of `origin` with N the id of the top-level Case, holds the whole Case and moves into the archive with its session; that a new page carries `## Context` only for a Case without `given` and without sub-cases, the short form of a deferred decision, and in the two-line body of a Case superseded in its own session; that it never carries `## Given`; and that the pages written before keep the sections they carry.
> **＋** The file says that a new page carries `## Problem` and `## Recommend` for a Case without sub-cases and on the page of a Case with sub-cases, which lists their pages in `children` in place of the kind lists; and that the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem`.
> **－** The example page holds no `## Context` and no `## Given`.

```then
update:
- slug: rule-decisions-schema
  replace:
  - old: 'optional: [create, update, delete, defer, source, supersedes, superseded_by]'
    new: 'optional: [create, update, delete, defer, source, supersedes, superseded_by, parent, children]'
  - old: |-
      required: ["## Problem", "## History"]
        optional: ["## Context", "## Given", "## When", "## Criterion", "## Deferred", "## Note"]
    new: |-
      required: ["## History"]
        optional: ["## Context", "## Problem", "## Recommend", "## Given", "## When", "## Criterion", "## Deferred", "## Note"]
  - old: '`recommend` — if the human accepted the proposal it became `Then`; if they changed it, `Then` holds the change. Either way the original stays in the Case file, `cases/case-<N>.md` in the folder of `origin` (case 513).'
    new: '`recommend` — no field: the body carries it as `## Recommend` (case 544.8).'
  - old: 'The body is the `problem` of the Case that produced it: the one paragraph a reader needs at the end of a link. The rest of the Case — `context`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` — stays in its Case file.'
    new: The body is the `problem` of the Case that produced it — the one paragraph a reader needs at the end of a link — and its `recommend`, the choices made in the rounds, under `## Recommend`. A Case with sub-cases has a page of its own with `## Problem`, the parent's `## Recommend` and `children`, and never `## Context`; the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem` (case 544.8). The rest of the Case — `context`, `given`, `when`, `then`, `tasks`, `ratification` — stays in its Case file.
  - old: A Case without `given`, the short form of a deferred decision, has no Case file, so its page keeps `## Context` as well;
    new: A Case without `given` and without sub-cases, the short form of a deferred decision, has no Case file, so its page keeps `## Context` as well;
  - old: a kind with no line is absent, at least one is present.
    new: a kind with no line is absent, at least one is present but on the page of a Case with sub-cases, which carries `children` instead (case 544.8).
  - old: one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `create` lines
    new: one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `create` lines
  - old: one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `update` lines
    new: one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `update` lines
  - old: one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `delete` lines
    new: one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `delete` lines
  - old: one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `defer` lines
    new: one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `defer` lines
  - old: optional; list of decision quoted wikilinks `"[[slug]]"`. Back-references, written by the script.
    new: |-
      optional; list of decision quoted wikilinks `"[[slug]]"`. Back-references, written by the script.
        parent: |
          optional; a decision quoted wikilink `"[[slug]]"`. On the page of a sub-case, the page of its parent Case, written by the script (case 544.8).
        children: |
          optional; list of decision quoted wikilinks `"[[slug]]"`. On the page of a Case with sub-cases, the pages of its sub-cases in ledger order, written by the script; such a page carries `children` in place of the kind lists (case 544.8).
  - old: Written for a Case without `given`, the short form of a deferred decision, which has no Case file,
    new: Written for a Case without `given` and without sub-cases, the short form of a deferred decision, which has no Case file,
  - old: required. What required a decision. On a defer, what is unresolved.
    new: |-
      optional. What required a decision. On a defer, what is unresolved. On the page of a Case without sub-cases and on the page of a Case with sub-cases; the page of a sub-case carries none (case 544.8).
        "## Recommend": |
          optional. The `recommend` of the Case as it stands: one item per question of the rounds of `case-guppi` — the question, the latest recommendation, the person's latest answer — one per change asked for on the shown Case, or the one recommendation of a Case with no round. On the page of a sub-case its own items, on the page of a Case with sub-cases the rest; absent on a short-form defer and on the pages written before case 544 (case 544.8).
  change: the Decision page carries Recommend; a Case with sub-cases has a page with children in place of the kind lists and no Context, a sub-case page carries parent and no Problem (case 544.8)
- slug: estimate-decisions-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — Recommend, parent and children in the schema, Problem optional, Context never on the page of a Case with sub-cases (case 544.8)
- slug: entity-glossary
  replace:
  - old: body `## Problem`, `## Deferred` for a Case that put something off, and `## History`;
    new: body `## Problem` and `## Recommend`, `## Deferred` for a Case that put something off, and `## History`; a Case with sub-cases has a page of its own with `## Problem`, `## Recommend` and `children`, and the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem` (case 544.8);
  - old: '`## Context` only for a Case without `given`, such as the short form of a deferred decision,'
    new: '`## Context` only for a Case without `given` and without sub-cases, such as the short form of a deferred decision,'
  change: the row Decision page names Recommend and the pages of a parent and a sub-case (case 544.8)
```

```tasks
- [x] update `rule-decisions-schema`
- [x] update `estimate-decisions-schema-checked`
- [x] update `entity-glossary`
- [x] `tests/test_schemas.py`: a Decision page without `## Problem` and with `## Recommend`, `parent` and `children` has no schema finding
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] `uv run guppi glossary`
- [ ] read `estimate-decisions-schema-checked`
```

### Case 544.9 — lint takes the page of a parent Case

> **given:**
> `rule-lint` — the rule of the check of the live pages
> **＋** `guppi/lint.py` — the `decision` and `origin` classes
> **＋** `tests/test_lint.py` — the tests of lint
> **＋** `guppi/materialize.py` — `category_of`, the one table of the prefixes
> **＋** `vault/wiki/` — the live pages lint reads
> **＋** `vault/raw/` — the session folders whose ledgers an `origin` names
> **＋** `vault/archive/` — the archived pages and sessions
> **＋** `raw/<date>[/<HHMM>]/ledger.md#case-N` — the form of an `origin` that names a Case
> **＋** `decision-` — the prefix of the slug of a Decision page
> **＋** `estimate-lint-finds-a-broken-link` — the promise whose Criterion this sub-case replaces

> **when:**
> `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

> **then:**
> `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
> **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
> **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate.
> **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
> **＋** An `origin` `#case-N` of a Case that has no ledger line of its own is found by a line of one of its sub-cases, `[case N.M]`.
> **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer` and no `children`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
> **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
> **－** A `### case N` line under an Estimate's `## Criterion` is not read as a link.

```then
update:
- slug: rule-lint
  change: a Decision page with children and no kind list, and the origin of a parent Case found by a line of its sub-case, are no findings (case 544.9)
- slug: estimate-lint-finds-a-broken-link
  set:
    status: pending
  change: 'the Criterion replaced whole — the page of a parent Case: children in place of the kind lists, its origin found by a line of a sub-case (case 544.9)'
```

```tasks
- [x] update `rule-lint`
- [x] update `estimate-lint-finds-a-broken-link`
- [x] `guppi/lint.py`: the `decision` class takes a page with `children` and no kind list; `check_origin` finds `#case-N` by a line `[case N.` of a sub-case when no line carries `[case N]`; the docstring says so
- [x] `tests/test_lint.py`: a parent page with `children` and no kind list, a page with neither, a parent `origin` found by a sub-case line, one with no line of either
- [x] read `estimate-lint-finds-a-broken-link`
```

### Case 544.10 — The approved Spec holds recommend

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case into the Spec
> **＋** `guppi/ratified.py` — the writer of a Case's section of `spec.md`
> **＋** `tests/test_ratified.py` — the tests of the hook
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the approved Spec of the session
> **＋** `estimate-spec-write-reaches-the-approved-spec` — the promise whose Criterion this sub-case replaces

> **when:**
> The `Stop` hook `uv run guppi ratified` has written a ratified Case N from its stored answer into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

> **then:**
> The hook writes the same stored answer of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
> **＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
> **＋** A task line whose text stood in a replaced section keeps the box it had there.
> **＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the plan file, come from the parent's stored answer, never from the reply.
> **－** Nothing written into `spec.md` is translated or refused for its language.
> **－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.
> **－** On the re-fire (`stop_hook_active`) nothing is written: exit 0.

```then
update:
- slug: estimate-spec-write-reaches-the-approved-spec
  set:
    status: pending
  change: the Criterion replaced whole — spec.md holds recommend, the parent's from its stored answer (case 544.10)
```

```tasks
- [x] update `estimate-spec-write-reaches-the-approved-spec`
- [x] `tests/test_ratified.py`: tests whose names hold `approved_spec` — a Case whose `recommend` reaches `spec.md`, and a parent's `recommend` from its stored answer
- [ ] read `estimate-spec-write-reaches-the-approved-spec`
```

### Case 544.11 — The form of the Case file takes recommend as a list

> **given:**
> `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `rule-case-check` — its hook writes the Case file
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the Case file the person is sent
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing in the chat
> **＋** `estimate-case-protocol-case-form` — the promise whose Criterion this sub-case replaces

> **when:**
> The hook of `rule-case-check` writes a Case that `case-guppi` built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the main agent sends that file to the person, at its first showing or again.

> **then:**
> The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
> **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-case-protocol-shows-the-built-case`, and the reply ends with a plain question.
> **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
> **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.

```then
update:
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  change: the Criterion replaced whole — recommend is the list of the schema, a sub-case with its own (case 544.11)
```

```tasks
- [x] update `estimate-case-protocol-case-form`
- [x] read `estimate-case-protocol-case-form`
```

## Deferred

## Case 546 — A question the main agent asks the person itself has no question shape

> **context:**
> The question shape of the skill `grill-me` governs a round of `case-guppi`. No rule names that shape for a question the main agent asks the person itself. In session 0248 the main agent asked the person the questions of a pre-spec report in its own shape (`lesson-prespec-report-decisions-off-the-question-shape`). Case 545 deferred this to `rule-skill-grill-me`, which Case 543.2 of the same plan updates; the defer moves to `rule-orchestration`, the rule put off for the orchestration of the main agent.

> **problem:**
> A question the main agent puts to the person outside a round of `case-guppi` — in a pre-spec report, at `/hi` or in Work Mode — follows no shape, so its options and its recommendation read differently from a round.

```then
defer:
  - slug: rule-orchestration
    type: rule
    purpose: The orchestration of the main agent — the triage of a Frontier item, the dispatch of case-guppi, the acknowledging reply, LEDGER, defers and the one rule — as a rule of its own loaded by /hi, and case-schema.md read by case-guppi alone
```
