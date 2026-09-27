<!-- approved 23:28:40 · session f09409c4 -->

# Spec — session 2050, 2026-09-27

## Case 464 — The file-route Estimate says what generate does with an unknown category

> **context:**
> `materialize` gives `category: unknown` to the entry of a ledger line whose slug has no category prefix (case 320). `generate` then treats that entry in one of four ways, by its kind. A `create` fails with `category 'unknown' is not a vault folder`. A `defer` with no page fails the same way. An `update` applies to the page of that slug, in whatever folder it is in. A `delete` prints `outside the vault, nothing to archive`, applies and ticks its line (case 48). Case 460.1 relied on the `update` road: it renamed `harness-senduserfile-renders-a-markdown-file-on-the-phone`, and that entry was `category: unknown`.
> The Criterion of `estimate-sprint-migration-file-route-gone` (status `passed`, from case 320) says the entry "lands `category: unknown`, and `generate` reports an error instead of 'applied by hand'". That is true for a `create` and a page-less `defer`. It is false for an `update` and a `delete`. The docstring of `guppi/generate.py` already describes both roads that apply (cases 460.1, 463). In session 1819 the person left the Estimate as it stood (Q7), and the brief flagged the contradiction again.
> The Criterion also keeps the old shape: a `Given:` block, and a `－` line that only bounds the edit ("`rule-morph` is untouched"). Its `method` still reads "at the close of theme 5", and theme 5 is closed. `tests/test_generate.py` covers the unknown-category `delete` (`test_a_delete_outside_the_vault_applies_and_a_delete_of_a_missing_page_fails`, `test_a_delete_of_an_unknown_category_is_outside_the_vault`). No test covers the `update`, the `create` or the page-less `defer` of that category.
> The item is an `update` of an existing page, so no vault query ran. In the frame: the `purpose` of the Estimate and the Purpose of `entity-sprint-migration` stay true. No sentence of `rule-page-generation` speaks of an unknown category outside its History. Of the Estimates of `rule-page-generation`, `estimate-generate-fails-alone` names only failures in general, and the unknown `create` failing agrees with it. `estimate-generate-renames` speaks of the page's own category prefix, which a page found in its folder has. Neither speaks of the unknown category, so both stand. The code does not change.
> In the rounds, the person chose these answers: replace the Criterion so that it describes the code; write it in the current model, with no `Given:`, the input in `When:` and the `rule-morph` line dropped; state all four roads; add tests for the untested roads and set a `method` without theme 5.

> **problem:**
> A `passed` Estimate promises that `generate` reports an error for every entry of unknown category. The code applies the `update` and the `delete` of such an entry, and a ratified Case depends on the `update` applying. The promise and the behaviour disagree, and no test holds three of the four roads.

> **given:**
> `estimate-sprint-migration-file-route-gone` — the promise that the file route is gone
> **＋** `guppi/` — the scripts the file route left
> **＋** `guppi/generate.py` — applies or fails the entry of each kind, and ticks the line of an applied entry
> **＋** `guppi/materialize.py` — `category_of` gives the entry of a slug with no prefix `category: unknown`
> **＋** `guppi/prespec.py` — `check_governed` refuses an `update` item that carries `file`
> **＋** `tests/test_generate.py` — the tests of the unknown-category roads
> **＋** `vault/wiki/sprint.md` — shows the status of the Estimate

> **when:**
> `generate` applies a `materialize.yaml` that holds an entry lifted from a ledger line whose slug has no category prefix.
> **＋** `make test` and `make lint` run on the tree.

> **then:**
> No file under `guppi/` holds `RULE_CLASS`, `rule_class`, `applied by hand` or `prose_names`.
> **＋** An `update` item that carries `file` is a `pre-spec` finding: `check_governed` refuses any such item, not only one on a governed path.
> **＋** The entry of a ledger line whose slug has no category prefix lands `category: unknown`.
> **＋** `generate` fails a `create` of that entry, and a `defer` of it with no page, with `category 'unknown' is not a vault folder`.
> **＋** `generate` applies an `update` of that entry to the page of that slug in any folder, and ticks its line.
> **＋** `generate` applies a `delete` of that entry with the stdout line `outside the vault, nothing to archive`, and ticks its line.
> **＋** `make test` is green, and `make lint` has no finding on a schema.
> **－** `generate` prints "applied by hand" for no entry.

```then
update:
- slug: estimate-sprint-migration-file-route-gone
  set:
    status: pending
    method: rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/ empty; uv run pytest tests/test_generate.py -k unknown — the update applied in any folder, the create and the page-less defer failed, the delete outside the vault; make test; make lint
  change: the Criterion replaced whole — an update of category unknown applies, a delete applies outside the vault, a create and a page-less defer fail; Given out; the method without theme 5 (case 464)
```

```tasks
- [ ] update `estimate-sprint-migration-file-route-gone`
- [x] `tests/test_generate.py`: an `update` of `category: unknown` applies to its page in a category folder and ticks its Spec line; a `create` and a page-less `defer` of `category: unknown` fail with `not a vault folder`; each test name holds `unknown`
- [ ] `uv run guppi sprint`
- [ ] read `estimate-sprint-migration-file-route-gone`
```

## Case 465 — The method of estimate-carry-over-writes names the render check and a reading by hand

> **context:**
> The carry skill `.claude/skills/carry/SKILL.md` is the Render of `rule-carry-over`. It is a prompt. After the person chooses "conserve" at the fork of `ExitPlanMode`, the agent reads the tree, rewrites the brief, writes `carry.md`, runs `guppi backlog` and commits. The `method` of `estimate-carry-over-writes` says "pytest over the skill's render, plus one live reading of a carried-over session". No test covers the skill: `pytest tests/test_render.py -k skill` deselects all 26 tests (brief of session 1819). What the Estimate promises is what the agent does after it reads the prompt, and pytest cannot run that.
> The Estimate is `pending`. Case 451.9 replaced its Criterion, and the live reading of that Criterion is still owed. `render --check` covers the `－` line "SKILL.md equals the Render". `tests/test_backlog.py` and `tests/test_materialize.py` cover the code that reads `carry.md`, under their own Estimates. `estimate-skill-grill-me-asks-in-rounds` gives a prompt skill the same kind of method: "uv run guppi render --check; by hand, …".
> In the frame I found no contradiction. `check_method` in `guppi/lint.py` passes a method that holds `by hand`. The `method` description in `vault/wiki/estimates/schema.yaml` asks for where and when a reading is taken, and the new text says both. The Criterion of `estimate-lint-checks-the-method` is about lint's behaviour, and this Case does not change lint. This Case changes only the `method` field. The Criterion and the status stay, so no other Estimate of `rule-carry-over` is touched. `rule-spec-box` stays out of the frame: nothing here makes a sentence of it false.
> In the round, the person agreed to: change the method and write no test; the proposed wording; change only `method`; keep `rule-spec-box` out.

> **problem:**
> The method of `estimate-carry-over-writes` names a pytest that does not exist and cannot check the promise. A reader who follows the method finds nothing to run. The reading stays owed, and the Estimate cannot be read as its method says.

> **given:**
> `estimate-carry-over-writes` — the promise of the carry skill, whose `method` changes
> **＋** `rule-carry-over` — the rule whose Render the Estimate checks
> **＋** `.claude/skills/carry/SKILL.md` — the rendered skill that `render --check` compares
> **＋** `vault/wiki/brief.md` — the brief the carry skill rewrites
> **＋** `vault/wiki/backlog.md` — the backlog that `guppi backlog` writes during a carry
> **＋** `tests/` — the test folder, where no test covers the carry skill
> **＋** `guppi/lint.py` — `check_method` classifies the `method` of an Estimate
> **＋** `vault/wiki/estimates/schema.yaml` — the description of the `method` field

> **when:**
> A reader takes the reading of `estimate-carry-over-writes` by its `method`.
> **＋** `uv run guppi lint` reads the `method` of `estimate-carry-over-writes`.

> **then:**
> The `method` names `uv run guppi render --check`, and one reading by hand of the first `/carry` after the fork of `ExitPlanMode`: the tree, `vault/wiki/brief.md`, `carry.md`, `vault/wiki/backlog.md` and the commit.
> **＋** `check_method` gives `estimate-carry-over-writes` no `method` finding.
> **－** The `method` names no pytest and no file under `tests/`.
> **－** The Criterion and the `pending` status of `estimate-carry-over-writes` stay as they are.

```then
update:
- slug: estimate-carry-over-writes
  set:
    method: uv run guppi render --check; by hand, the first /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md and the commit read
  change: the method names render --check and a reading by hand; no test targets the carry skill (case 465)
```

```tasks
- [ ] update `estimate-carry-over-writes`
```

## Case 466 — The first round of `case-guppi` on an item opens with a short context of the item

> **context:**
> When an item has an open fork, `case-guppi` answers with a round of questions in the form of `.claude/skills/grill-me/SKILL.md`. The main agent translates the round into Russian and shows it line by line. The Render of `rule-case-build` makes the round "its numbered questions ... with no Case heading and nothing else". The Render of `rule-case-protocol` has the main agent add nothing between the questions and put its own text only after the last question. So the round opens straight with `❓ **Q1**`. In session 2050 the first rounds for Cases 464 and 465 did this, and the person saw the questions with nothing to explain the item.
> In the rounds, the person chose these answers. `case-guppi` writes the context, because it has read the frame before it asks, and the main agent has not. Only the first round on an item carries it. The person's own `/grill-me` stays as it is, so `rule-skill-grill-me`, its Render and `estimate-skill-grill-me-asks-in-rounds` do not change. The context is one prose paragraph under the label `**Context:**`, with no fixed limit. Its parts follow the Language paragraph of `case-schema.md` (case 449): a sentence per part where one is enough, and a part with nothing to say left out, such as "where it goes wrong" for an item that is not a defect. The person judges its length.
> The change touches two promises, so there are two sub-cases (`rule-atomicity`). 466.1 covers the round `case-guppi` writes. 466.2 covers how the main agent shows it. `rule-case-check` neither checks nor stores an answer with no Case heading, and its `Stop` comparison reads only Cases. So a round with a context passes both hooks unchanged, if the context carries no Case heading. `.claude/settings.json` and `guppi/casecheck.py` do not change, and no code judges the form of a round. `estimate-language-followed` says a round of `case-guppi` is shown "translated from the answer". The context is part of the answer, so that line stays true. `estimate-case-protocol-loaded` promises three things: `case-schema.md` equals the Render, it stands in the context after `/hi`, and `CLAUDE.md` repeats no paragraph of it. None of these speaks of a round, so it is not touched (case 378.5). The Language paragraph of `case-schema.md` still holds. The Case has no `create`, so no vault query ran.

> **problem:**
> The first round on an item reaches the person with no framing. The person reads questions about a mechanism before being told what the item is, what goes wrong today, or what the round decides. No sentence of the vault lets `case-guppi` or the main agent put a context before the first question, and two sentences forbid it.

### Case 466.1 — `case-guppi` opens its first round on an item with a context paragraph

> **given:**
> `rule-case-build` — its Render, the paragraph on the forks and the round
> **＋** `.claude/agents/case-guppi.md` — the file rendered from `rule-case-build`
> **＋** `estimate-case-build-writes-the-case` — the promise of the agent, its Criterion replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round, unchanged
> **＋** `vault/wiki/case-schema.md` — the form of the Case the agent reads first, and the Language paragraph the context follows
> **＋** `.claude/agents/ask-guppi.md` — the vault query the agent runs before a `create` without a `ref`
> **＋** `.claude/settings.json` — the hooks the agent reads for a Case that changes a hook
> **＋** `rule-case-check` — the `SubagentStop` hook that checks and stores only an answer with a Case heading

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, from the heading to the fence of `ratification`, and nothing else.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round.
> **－** It writes no file and no ledger line.

```then
update:
- slug: rule-case-build
  replace:
  - old: in English, with no Case heading and nothing else.
    new: 'in English, with no Case heading and nothing else but the context of a first round. The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out. A later round on the item, a round after a message on a Case you built and a round in Work Mode carry no context, and no context carries a Case heading.'
  change: the first round of case-guppi on an item opens with a short context of the item (case 466.1)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole — the first round on an item opens with a Context paragraph (case 466.1)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-writes-the-case`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-the-case` — by hand, the first and a later round of a dispatch on an item with a fork, in a session after the render
```

### Case 466.2 — The main agent shows the context of a first round translated before its first question

> **given:**
> `rule-case-protocol` — its Render, the paragraph "Who builds a Case", where a round is shown
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing, its Criterion replaced whole
> **＋** `.claude/agents/case-guppi.md` — the agent that writes the round and its context
> **＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round
> **＋** `rule-case-check` — the hooks that write the file of a Case and compare its showing
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that the main agent sends
> **＋** `.claude/agents/ask-guppi.md` — the vault query the main agent dispatches at pre-spec

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions or answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case.
> **＋** An answer with no Case heading is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: line by line, slugs, paths and quotations unchanged — each question in the order
    new: line by line, slugs, paths and quotations unchanged — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order
  change: the main agent shows the context of a first round translated in place before its first question (case 466.2)
- slug: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — the context of a first round shown translated before its first question (case 466.2)
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] update `estimate-case-protocol-shows-the-built-case`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-shows-the-built-case` — by hand, the first rounds shown in a session after the render, against the answers of `case-guppi` in the transcript
```

## Case 467 — A backlog item leaves when the Case that decides it names its page

> **context:**
> `vault/wiki/backlog.md` has no state of its own. `guppi backlog` rewrites it whole from the pages that carry `deferred_by`, the open Insights, the `## Backlog` section of the sprint page, and the folders that hold `carry.md`. An item leaves when its source changes. For a deferred page, a Case carries `{supersedes:case M}`, and `generate.clear_deferred_by` then removes Decision M from `deferred_by`. The file changes only in the librarian's run and in `carry`, never while a session runs. The person saw a count that did not move because they read the file before the librarian's run over session 1819. That run took it from 19 to 16 items: cases 459, 462 and 463 removed `rule-claude-md`, `rule-one-judgment-one-implementation` and `rule-page-generation`. The cleared Insights of session 1255 are `actioned`, and neither is in the file.
> The mechanism has two gaps. First, no script checks that a Case which takes an item from the backlog supersedes its defers. Case 429 asks for this, but `prespec` checks only the closer word of a `backlog` line. Second, `clear_deferred_by` clears every target in the superseded Decision's `defer` list. Case 220 and case 243 each defer both `rule-git-context` and `rule-github-issues`, so deciding one page would remove the other from the backlog undecided. Clearing page by page brings up a third point. Cases 459 and 462 decided their items with no decision line on the deferred page. From now on, a Case that decides a backlog item names the page on a decision line. When nothing on the page changes, an `update` with only `change` is enough; it applies and writes a History line, as case 439 showed.
> The vault's answer: both new Estimates carry a `ref`, so no vault query is needed. A Glob of `vault/**/` finds no page for either slug.
> What the frame changes: the sentence of `rule-case-check` "the Frontier left to `/pre-spec`", the case-429 paragraph of `rule-case-protocol`, the finding list in the Render of `rule-prespec`, the sentence of the `rule-backlog` Purpose on how an item leaves, the docstrings of `guppi/casecheck.py` and `guppi/generate.py`, and the `supersedes` line of the Criterion of `estimate-generate-writes-the-decision-page`. The hook of 467.2 is the only hook on `SubagentStop`. 467.1 and 467.2 apply one rule to the page of a `backlog` line: some Case among Case N and its sub-cases both names the page on a decision line other than a `defer` and carries each `{supersedes:case M}`. 467.1 applies it at pre-spec to the Case the closed line names. 467.2 applies it before showing, to each top-level Case of the answer that names the page.
> Estimates not touched, and why:
> - `estimate-prespec-checks-the-frontier` speaks of boxes and closers.
> - `estimate-case-check-sends-back-a-faulty-case` promises that `judge` runs and that a finding goes back, not which checks it holds.
> - The Criterion of `estimate-case-protocol-ledger-line-form` promises the `{supersedes}` blocks of a deferred decision taken up, which stays true. The added requirement, the page named on a decision line, is held by the new `estimate-prespec-requires-a-backlog-item-decided-on-its-page`.
> - `estimate-backlog-renders` and `estimate-backlog-checks-the-file` promise the render from `deferred_by` and its check, which stay true. The update of the `rule-backlog` Purpose touches neither.
> - `estimate-generate-cascades` archives a superseded Decision and leaves `deferred_by` alone.
> - Line 32 of `estimate-git-context-current` records the past supersede of case 106 by case 115.
>
> Not done:
> - no checkboxes in `backlog.md`, and `guppi/backlog.py` is unchanged;
> - `insight-hi-skill-substitution-checked-by-a-model-call` stays until a Case rewrites its Pattern and Proposal with `{supersedes:case 448}`;
> - a `defer` of an Estimate or a lesson still writes no `deferred_by` (no case exists);
> - a Decision superseded for one of its pages is archived by the cascade in the same run, while a page of its `defer` list that the Case did not name still links to it in `deferred_by`; lint accepts the link, and a later supersede still reaches the Decision, since `generate.find` reads the archive.

> **problem:**
> A Case can decide a backlog item without retiring its defers, and nothing catches it. A Case that retires a defer shared by two pages clears both, although it decided one. The item should leave the backlog exactly when a Case decides it, page by page, and a Case that fails to make it leave should be sent back before it is ratified.

### Case 467.1 — pre-spec requires a backlog item decided on its page

> **given:**
> `rule-prespec` — the pre-spec check; its Render is the skill
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from `rule-prespec`, which lists the findings
> **＋** `guppi/prespec.py` — `judge` and `check_frontier`, where the new function lives
> **＋** `tests/test_prespec.py` — the tests of the check
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session, whose lines name the source and the closer
> **＋** `rule-case-protocol` — its case-429 paragraph says how a deferred decision is taken up; its Render is `vault/wiki/case-schema.md`
> **＋** `estimate-prespec-requires-a-backlog-item-decided-on-its-page` — the new promise

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the decision lines of the session's window, and the pages of the vault.

> **then:**
> For each line of the Frontier closed `[x] … · backlog · case N`, each page that its title names in a code span and that carries `deferred_by` is checked against Case N and its sub-cases.
> **＋** A finding when no decision line of Case N or of its sub-cases, other than a `defer`, names that page.
> **＋** A finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and `{supersedes:case M}`.
> **－** A line of another source, an open line, a line closed `work` or put off, and a page without `deferred_by`, such as an open Insight or a note of the sprint page's `## Backlog`, give no finding of this check.

```then
create:
- slug: estimate-prespec-requires-a-backlog-item-decided-on-its-page
  type: estimate
  ref: rule-prespec
  kind: QA
  purpose: A Case that decides an item taken from the backlog names its page and supersedes every Decision of its deferred_by, or pre-spec reports it
  method: uv run pytest tests/test_prespec.py -k backlog
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-prespec
  replace:
  - old: changes the sprint page (case 314.2), for every ratified Case
    new: changes the sprint page (case 314.2), for every line closed `· case N` whose source segment is `backlog` and whose title names in a code span a page with `deferred_by`, when no decision line of Case N or of a sub-case, other than a `defer`, names that page, or when no Case among them both names the page and carries `{supersedes:case M}` for a Decision M of its `deferred_by` — `generate` clears a defer only from the pages the superseding Case names (case 467.1), for every ratified Case
  change: the finding on a backlog item decided without its page named and its defers superseded (case 467.1)
- slug: rule-case-protocol
  replace:
  - old: so that every defer of the page is retired (case 429).
    new: so that every defer of the page is retired (case 429); the Case, or the sub-case, that carries the blocks also names the page on a decision line other than a `defer` — an `update` with only `change` when nothing on the page changes — since `generate` clears a defer only from the pages the superseding Case names. `/pre-spec` reports a Case that closes a Frontier line of the source `backlog` when no Case among it and its sub-cases both names the page and carries each block; the check of the answer of `case-guppi` sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the answer both names the page and carries each block (case 467).
  change: a Case that takes up a deferred decision names its page on a decision line; what pre-spec and the check of case-guppi's answer each report (case 467)
```

```tasks
- [x] `guppi/prespec.py` — one function that judges the page of a `backlog` Frontier line against the decision lines of a Case and its sub-cases and the page's `deferred_by`: some Case among them names the page on a line other than a `defer` and carries each `{supersedes:case M}`; `check_frontier` calls it on each line closed `[x] … · backlog · case N`
- [x] `tests/test_prespec.py` — a line closed `· backlog · case N` whose page is named by no line of Case N; one whose page is named but whose Decision M is not superseded; one where a sub-case names the page and carries every `{supersedes}` while another sub-case is an `update` of the page with only `change`; a page without `deferred_by`; a line of another source
- [ ] update `rule-prespec`
- [ ] update `rule-case-protocol`
- [ ] create `estimate-prespec-requires-a-backlog-item-decided-on-its-page`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-prespec-requires-a-backlog-item-decided-on-its-page`
```

### Case 467.2 — the check of case-guppi's answer requires the same, on an open backlog line

> **given:**
> `rule-case-check` — the `SubagentStop` check of the answer of `case-guppi`; its text leaves the Frontier to pre-spec
> **＋** `guppi/casecheck.py` — `check_answer` and `subagent`, which will call the function of 467.1
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `guppi/prespec.py` — the one function that judges the page of a `backlog` Frontier line
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session, read for its open lines
> **＋** `rule-one-judgment-one-implementation` — one judgment in one module, imported by both callers
> **＋** `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — the new promise

> **when:**
> `SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

> **then:**
> For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the answer that, itself or through a sub-case, names that page on a decision line other than a `defer`.
> **＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the answer both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` answers again.
> **＋** The judgment is the function of `guppi/prespec.py` that the pre-spec check runs, imported, not copied.
> **－** A Case of the answer that names no such page, an answer while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.

```then
create:
- slug: estimate-case-check-requires-a-backlog-item-decided-on-its-page
  type: estimate
  ref: rule-case-check
  kind: QA
  purpose: A Case of case-guppi that names the page of an open backlog line, where no Case among it and its sub-cases both names the page and supersedes every Decision of its deferred_by, goes back to case-guppi
  method: uv run pytest tests/test_casecheck.py -k backlog, then by hand the first answer of case-guppi on an item taken from the backlog
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: does not judge by their keys (case 436.4), the Frontier left to `/pre-spec`.
    new: 'does not judge by their keys (case 436.4), the Frontier left to `/pre-spec` but for one check: for each open line of the session''s `frontier.md` whose source is `backlog` and each page of its title that carries `deferred_by`, a Case of the answer that, itself or through a sub-case, names the page on a decision line other than a `defer` gets a finding for each Decision of that list when no Case among it and its sub-cases both names the page and carries its `{supersedes}`, by the function of `guppi/prespec.py` that `/pre-spec` runs (case 467.2).'
  change: the answer of case-guppi is checked against the open backlog lines of the Frontier (case 467.2)
```

```tasks
- [x] `guppi/casecheck.py` — `subagent` passes the session's `frontier.md` and the records of the `ratification` fences to the function of `guppi/prespec.py` for each open `backlog` line and each top-level Case of the answer that names its page; the docstring sentence "The Frontier and the grammar of the window stay with `/pre-spec` (case 445.2)" names this one exception
- [x] `tests/test_casecheck.py` — an answer whose Case names the page of an open `backlog` line without its `{supersedes}`, sent back; the same with every `{supersedes}`, passed; a sub-case that names the page and carries every `{supersedes}` beside a sub-case that is an `update` of the page with only `change`, passed; a Case naming the page only in a `defer` line; no open `backlog` line
- [ ] update `rule-case-check`
- [ ] create `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
- [ ] read `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
```

### Case 467.3 — generate clears a defer only from the pages the superseding Case names

> **given:**
> `guppi/generate.py` — `decision` and `clear_deferred_by`, and the docstring that describes a `supersedes`
> **＋** `tests/test_generate.py` — the tests of the Decision page and of a `supersedes`
> **＋** `rule-page-generation` — the rule of `generate`, whose mechanism lives in the docstring
> **＋** `estimate-generate-writes-the-decision-page` — its Criterion states the clearing of every target of the `defer` list
> **＋** `rule-backlog` — its Purpose says how an item leaves the backlog
> **＋** `vault/wiki/backlog.md` — the file `guppi backlog` writes from `deferred_by`

> **when:**
> `uv run guppi generate` writes the Decision page of a Case whose decision lines carry `{supersedes:case M}`.

> **then:**
> Decision M is set `superseded`, and the Case is appended to its `superseded_by`.
> **＋** Each page of the `defer` list of Decision M that a decision line of the Case names drops Decision M from its `deferred_by`. An empty `deferred_by` is dropped.
> **＋** A later Case that supersedes Decision M again clears the pages it names in the same way.
> **－** A page of the `defer` list that no decision line of the Case names keeps Decision M in its `deferred_by`, and stays in `vault/wiki/backlog.md`.

```then
update:
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
  change: the Criterion replaced whole — a supersedes clears deferred_by only on the pages the superseding Case names (case 467.3)
  sections:
    Criterion: |-
      When:
      `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

      Then:
      One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Context` and `## Problem` from `case_text`, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
      **＋** The page is written before the first entry of its lines, so their History lines name it.
      **＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
      **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
      **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
      **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
      **－** The page holds no `## When` and no `## Criterion`: the promise lives on the Estimate.
- slug: rule-backlog
  replace:
  - old: a Case that decides it supersedes its defer
    new: a Case that decides it names its page on a decision line and supersedes its defer (case 467.3)
  change: an item leaves when the Case that decides it names its page and supersedes its defer (case 467.3)
```

```tasks
- [x] `guppi/generate.py` — `clear_deferred_by` takes the slugs that the superseding record's `targets` name and clears only those pages; the docstring sentence "removes its slug from the `deferred_by` of every target of its `defer` list" says the same
- [x] `tests/test_generate.py` — a Decision that defers two pages, superseded by a Case naming one of them: one page cleared, one kept; a second Case superseding the same Decision, then archived, and naming the other page: that page cleared too
- [ ] update `estimate-generate-writes-the-decision-page`
- [ ] update `rule-backlog`
- [ ] read `estimate-generate-writes-the-decision-page`
```

## Case 468 — One standard for the account of a session: each fact once in the Retro report and in the handoff

> **context:**
> `/retro` opens with a numbered list of what is not done. The list holds every unticked box of `raw/<date>/<hi HHMM>/spec.md`, per Case, each marked as waiting for the librarian, waiting for a later session, or debt. At Retro most of these boxes are the page and render lines of the session's own Cases, so the list names each Case and its pages. The close then names every ratification per Case with the same pages, and "what got done" and "what is not done" repeat parts of the opening list. At the `/retro` of session 1819, `estimate-retro-report-holds-each-fact-once` was read `failed` for this reason (line 39 of `raw/2026-09-27/1819/ledger.md`), and the person asked for one standard. `handoff.md` has the same defect. The handoff of session 1819 named the failed reading both in `## Notes from memory` and in `## What actually got done`, and named the next-session items in the notes and again in the instructions to the librarian.
> The person chose one standard for both documents. The frontier numbers only what needs an end in this Retro. The librarian's boxes are one count line, and the later-session `read` lines are one line of slugs. The close has three parts, each fact in one part only. A reading or a lesson that ends an item of the frontier is named under What is not done, not under What got done. The handoff's `## What actually got done` carries the close. The librarian does not read the chat, so this is the one repeat, across two documents for two readers. Inside `handoff.md` each fact stands in one section. The handoff's What is not done differs from the close in three ways, because the file has no frontier. It names each open item in a few words. The text of a note for the handoff, one of the four ends that `rule-retro` allows, stands there as that item's end. The two lines under the frontier stand under it, because the paragraph of `rule-retro` on the readings already sends the later-session Estimates to the handoff.
> What the frame changes: the frontier paragraph and the close paragraph of the Render of `rule-retro`, the `purpose` of `estimate-retro-report-holds-each-fact-once`, and the section list of the Render of `rule-handoff`. The section names stay, so `rule-brief` still reads "Where things stand" from `## What actually got done`. `estimate-brief-written` still finds its "handoff flag with a question" in the notes or among the open items. `estimate-retro-loads` promises the readings, not the form of the report, so it is not touched. `estimate-handoff-dispatches` promises the three sections, the dispatch and no commit, which still hold, so it is not touched. `estimate-end-of-work-order` promises the order of the steps, which does not change. The Purpose of `rule-handoff` ("what actually got done") still holds. The one `create` has a `ref`, so no vault query ran. A Glob of `vault/**/` finds no page for `estimate-handoff-holds-each-fact-once`.
> Not done: the form of `brief.md` does not change.

> **problem:**
> The account of a session repeats itself. The Retro report names the same Cases, pages and open items in the frontier and in each part of the close. The handoff names the same facts in more than one section. The person reads everything several times, and no text of the vault says which part holds which fact.

### Case 468.1 — The Retro report holds each fact once

> **given:**
> `rule-retro` — its Render, the frontier and the close of `/retro`
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `estimate-retro-report-holds-each-fact-once` — the promise of the report, its Criterion replaced whole and its `purpose` rewritten
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, with its unticked boxes
> **＋** `uv run guppi tail` — the Tail of the session's ledger
> **＋** `make test` and `make style` — the checks the skill loads before the first turn
> **＋** `estimate-retro-loads` — the promise of the readings at Retro, unchanged

> **when:**
> The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes, and the agent writes the frontier and the close.

> **then:**
> The frontier is one numbered list of what needs an end in this Retro: each unticked box that is debt, and what the agent noticed during Work Mode.
> **＋** A `read` line without its line in the Tail, whose slug this session neither creates nor updates, is debt, and so is a box of code, a test, a command or a migration left unticked.
> **＋** Under the list stand two lines, not numbered: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it.
> **－** The frontier names no box that waits for the librarian one by one, and holds no list of the ratifications.
> **＋** The close has three parts. Ratified is one line with the ids of the Cases ratified, from `uv run guppi tail`, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page.
> **＋** What got done holds the commit, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier.
> **＋** What is not done holds each number of the frontier with the end it took, and its ledger line number where it has one, with no text of the item and no repeat of the two lines under the frontier.
> **－** No Case, box, reading or lesson is named in two parts of the report.

```then
update:
- slug: rule-retro
  replace:
  - old: 'Open with the frontier, in one message and with no read call: the list of what is not done, numbered: the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session''s folder, case 73), per Case — a `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above listed as waiting for the librarian, whose scripts tick them (cases 226, 250, 270), not as debt — a `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, listed as waiting for a later session, neither debt nor the librarian''s (case 428.4) — another `read` line without its line in the Tail is debt, and the lines of a Case a `{supersedes:case N}` line of the Tail names are not counted at all, its work stands under the superseding Case (case 282); what you noticed during Work Mode, in the same list — bugs, forks, a contract that turned out imprecise.'
    new: 'Open with the frontier, in one message and with no read call. First sort the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session''s folder, case 73). A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above wait for the librarian, whose scripts tick them (cases 226, 250, 270); they are not debt. A `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, waits for a later session; it is neither debt nor the librarian''s (case 428.4). Another `read` line without its line in the Tail is debt, and so is a box of code, a test, a command or a migration left unticked. The lines of a Case that a `{supersedes:case N}` line of the Tail names are not counted at all; its work stands under the superseding Case (case 282). The frontier is one numbered list of what needs an end in this Retro: each box that is debt, and what you noticed during Work Mode — bugs, forks, a contract that turned out imprecise. Under the list write two lines, not numbered: the count of the boxes that wait for the librarian, with no list of them, and the slugs of the `read` lines that wait for a later session. The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1).'
  - old: 'Close with three lists: every ratification of this session, one line per Case, by the Tail above grouped by Case, this session''s folder first, a Case a `{supersedes:case N}` line names not counted; what got done; what is not done — the opening list by its numbers, each item with the end it took.'
    new: 'Close with three parts, each fact in one part only. Ratified: one line with the ids of the Cases ratified, by the Tail above, this session''s folder first, a Case that a `{supersedes:case N}` line names not counted, and no page. What got done: only what no other part holds — the commit, the code files and tests changed, the result of `make test` and `make style`, the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier; no Case and no item of the frontier restated. What is not done: each number of the frontier with the end it took, and its ledger line number where it has one, with no text of the item and no repeat of the two lines under the frontier. No Case, box, reading or lesson is named in two parts of the report (case 468.1).'
  change: 'the report of /retro holds each fact once — the frontier numbers only what needs an end, the librarian''s boxes one count line, the close three parts: the Case ids, what got done, the numbers with their ends (case 468.1)'
- slug: estimate-retro-report-holds-each-fact-once
  set:
    status: pending
    purpose: Whether the report of /retro holds each fact once — the frontier numbers only what needs an end, the boxes that wait for the librarian one count line and the read lines that wait for a later session one line of slugs; the close holds the Case ids, what got done and the numbers of the frontier with their ends
  change: the Criterion replaced whole and the purpose rewritten — the frontier numbers only what needs an end; the close holds the Case ids, what got done and the numbers with their ends (case 468.1)
```

```tasks
- [ ] update `rule-retro`
- [ ] update `estimate-retro-report-holds-each-fact-once`
- [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-report-holds-each-fact-once` — by hand, at the first `/retro` after the render
```

### Case 468.2 — The handoff holds each fact once, its account the Retro close

> **given:**
> `rule-handoff` — its Render, the sections of `handoff.md`
> **＋** `.claude/skills/handoff/SKILL.md` — the skill rendered from `rule-handoff`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the document the skill writes
> **＋** `rule-retro` — the close of the Retro, which the handoff carries, and the four ends of an item, a note for the handoff among them
> **＋** `rule-brief` — reads "Where things stand" from `## What actually got done` by name, unchanged
> **＋** `estimate-handoff-dispatches` — the promise of the three sections, the dispatch and no commit, unchanged
> **＋** `estimate-handoff-holds-each-fact-once` — the new promise

> **when:**
> The person invokes `/handoff` after the Retro of the session, on a clean tree, and the agent writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `## What actually got done` holds the three parts of the close of the Retro of `rule-retro`: Ratified and What got done as the person approved them, and What is not done in the form below.
> **＋** What is not done names each item of the frontier in a few words with the end it took, since the numbers of the frontier are not in the file, and the text of a note for the handoff stands there as the end of its item.
> **＋** Under What is not done stand the two lines under the frontier: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats.
> **＋** `## Direct instructions to the librarian` holds only what to check first and what may duplicate what.
> **－** No Case, reading, lesson or open item is named in two sections of `handoff.md`.
> **－** The three section names stay as they are, so `rule-brief` reads `## What actually got done` as before.

```then
create:
- slug: estimate-handoff-holds-each-fact-once
  type: estimate
  ref: rule-handoff
  kind: QA
  purpose: Whether handoff.md holds each fact once — the Retro close in What actually got done, each open item named once with its end, the notes and the instructions to the librarian only their own facts
  method: one reading by hand at the first /handoff after the render, against the close of its Retro, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-handoff
  replace:
  - old: '`## Direct instructions to the librarian` (what to check first, what may duplicate what), `## What actually got done` (which Cases closed, where the code landed, what is not done).'
    new: '`## Direct instructions to the librarian` (what to check first, what may duplicate what), `## What actually got done` (the three parts of the close of the Retro: Ratified and What got done as the person approved them; What is not done names each item of the frontier in a few words with the end it took, since the numbers of the frontier are not in this file, the text of a note for the handoff standing there as the end of its item, and under it the two lines under the frontier — the count of the boxes that wait for the librarian and the slugs of the `read` lines whose slug this session creates or updates). A fact stands in one section only: a Case, a reading, a lesson or an open item named in one section is not named in another (case 468.2).'
  change: the handoff holds each fact once — What actually got done carries the Retro close, a note for the handoff stands as the end of its item, the notes and the instructions hold only their own facts (case 468.2)
```

```tasks
- [ ] update `rule-handoff`
- [ ] create `estimate-handoff-holds-each-fact-once`
- [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [ ] read `estimate-handoff-holds-each-fact-once` — by hand, at the first `/handoff` after the render
```

## Deferred

## Case 469 — A supersede of an archived Decision brings the page back from the archive

> **context:**
> After case 467.3, `generate.clear_deferred_by` clears a defer only from the pages the superseding Case names, so a Decision that deferred two pages can be superseded twice, by two Cases. The cascade archives a superseded Decision in the run of its first supersede, and `guppi cleanup` moves it to `vault/archive/`. At the second supersede, `generate.decision` finds the page in the archive and sets its `status` to `superseded` again. `cleanup` moves a page whose status is no longer `archived` back to `vault/wiki/decisions/`, and the cascade of the next run archives it again. The page makes a round trip and gains two History lines, with no change of meaning.

> **problem:**
> Whether a supersede of an archived Decision keeps its `archived` status and only appends to `superseded_by`, or the round trip stays as it is.

```then
defer:
  - slug: rule-page-generation
    type: rule
    purpose: A supersede of a Decision already archived keeps it archived and only appends the superseding Case to its superseded_by, so cleanup does not bring it back from the archive (seen in session 2050, after case 467.3)
```
