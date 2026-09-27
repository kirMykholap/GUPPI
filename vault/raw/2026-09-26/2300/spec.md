<!-- approved 03:55:33 · session 7aae220a -->

# Spec — session 2300, 2026-09-26

## Case 443 — a round of questions before a Case is built

> **context:**
> Today the main agent takes up a Frontier item that needs a decision and dispatches `case-guppi` with the person's words. `case-guppi` reads the vault and the frame and answers with the Case. When the words do not give a choice, it answers with one question alone and no Case heading. Forks that the person would want to discuss are found only when the Case is shown, so there is no time to discuss them first. The person has long wanted `/grill-me` adapted to this. `/grill-me` asks in rounds: numbered questions, each with a recommended answer, then a wait for the answers. It stands as `.claude/skills/grill-me/SKILL.md`, and no rule page governs it. The Closed section of the sprint says it is kept without a page. Two of its sentences do not fit `case-guppi`. One tells the agent to dispatch a sub-agent for a fact, and `case-guppi` cannot dispatch. The other makes the user's word the only confirmation, but for `case-guppi` the showing of the Case and its ratification are the confirmation. The Render of `rule-case-build` has `case-guppi` answer with that one question alone. The Render of `rule-case-protocol`, `vault/wiki/case-schema.md`, has the main agent put a heading-less answer to the person as a question.
>
> The vault query on `rule-skill-grill-me` gives this. Exists: none. Near: `rule-skill-hi` is the rule page of another skill and the pattern for this one. `rule-case-build` governs the agent that will load the skill. `rule-orchestration`, deferred by its decision, would move the triage of a Frontier item and the dispatch out of `case-schema.md` into a rule of its own. This Case does not take that defer up: it changes the triage text where it stands today. Missing: a page that governs `.claude/skills/grill-me/SKILL.md`. Rules: `rule-rules-schema` requires `governs`, `render_mode`, a `## Render` and an Estimate on a render rule. `rule-render-harness` and `rule-governed-files-hook` make the page the one source of the file. Tags: `harness`, `workflow`. The slug `rule-skill-grill-me` is free, and no archived page carries it.
>
> The frame gives this. The `skills` field of a subagent's frontmatter puts the full text of a skill into the subagent's context at startup. It works with `tools: Read, Grep, Glob` and needs no Skill tool. It does not work for a skill with `disable-model-invocation: true`, and `grill-me` has none (https://code.claude.com/docs/en/sub-agents.md, as the person gave it). The sentence of the sprint's Closed section on `/grill-me` would become false, so 443.1 replaces it on `entity-sprint-migration`, and `vault/wiki/sprint.md` is rendered again. The `SubagentStop` check of `rule-case-check` does not check or store an answer with no Case heading. If a round follows a Case the agent already built, the check takes that earlier Case again and stores the same text, so a round breaks nothing there. The question template of the skill becomes an indented code block. The chat form of a Case cannot carry a fence inside a fenced value, and that limit is a Frontier item of its own. `estimate-language-followed` is not touched: a round shown in Russian is chat with the owner, as its Criterion says. `estimate-case-protocol-case-form` reads the Cases shown, and a round is no Case. `estimate-case-protocol-loaded` promises only that the file equals the Render. The Case splits by promise: the skill, the agent's answer and the main agent's showing are three Estimates.

> **problem:**
> How `case-guppi` discusses the forks of a Frontier item with the person before it builds the Case, and where the rules of that round live: in the skill, in the agent's instructions, or in the Case schema.

### Case 443.1 — `rule-skill-grill-me`: the grill-me skill gets its rule page

> **given:**
> `rule-skill-grill-me` — the new rule page, the source of the skill's text
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill it renders
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise of the skill
> **＋** `rule-plan-mode` — the parent of the new page
> **＋** `rule-render-harness` — `uv run guppi render` and its `--check`
> **＋** `entity-sprint-migration` — the Closed section, which names `/grill-me` as kept without a page
> **＋** `vault/wiki/sprint.md` — rendered from `entity-sprint-migration`

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, each numbered, with a title, a body and a recommended answer, and the agent waits for the answers before the next round.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

```then
create:
- slug: rule-skill-grill-me
  type: rule
  kind: Leaf
  purpose: Prevents an interview from acting on a plan before each of its decisions is put to the person and settled, and the skill that runs it from being a file no rule page governs
  enforcement: render
  governs: .claude/skills/grill-me/SKILL.md
  render_mode: full
  ref: rule-plan-mode
  tags:
  - harness
  - workflow
  sections:
    Purpose: 'Prevents an interview from acting on a plan before each of its decisions is put to the person and settled, and the skill that runs it from being a file no rule page governs. `/grill-me` asks in rounds: the frontier of a design tree, the questions whose prerequisites are settled, each with a recommended answer. It served the person''s own interviews without a page until case 443.1. The same text serves `case-guppi`, which loads it through the `skills` field of its frontmatter ([[rule-case-build]]), so two of its sentences name no one agent: a fact is found by the agent itself, or by a sub-agent when the agent can dispatch one; the shared understanding is confirmed by the user''s word unless the instructions that started the grill name another confirmation. The question template is an indented code block, the form it took when case 443.1 was written, before case 444 let a fenced value carry a shorter fence.'
    Render: |-
      <!-- rule-skill-grill-me -->
      ---
      name: grill-me
      description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
      ---

      Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

      Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

      Each question should be formatted like so:

          ❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

          ➡️ <your recommended answer>

      Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

      Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), find it yourself, or dispatch a sub-agent when you can dispatch one; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

      The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the shared understanding is confirmed: by the user's word, unless the instructions that started the grill name another confirmation.
      <!-- /rule-skill-grill-me -->
- slug: estimate-skill-grill-me-asks-in-rounds
  type: estimate
  ref: rule-skill-grill-me
  kind: QA
  purpose: grill-me asks in rounds, finds facts itself and acts only after the shared understanding is confirmed, as the one text its rule page renders
  method: uv run guppi render --check; by hand, one /grill-me of the person in a session after the render, its rounds read in the chat
  tags:
  - harness
  - workflow
update:
- slug: entity-sprint-migration
  replace:
  - old: 'Kept without a page: `/grill-me`; `git pull` in `/hi`'
    new: '`/grill-me` has its page since case 443.1, `rule-skill-grill-me`. Kept without a page: `git pull` in `/hi`'
  change: /grill-me has its rule page (case 443.1)
```

```tasks
- [ ] create `rule-skill-grill-me`
- [ ] create `estimate-skill-grill-me-asks-in-rounds`
- [ ] update `entity-sprint-migration`
- [ ] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
- [ ] `uv run guppi sprint`
- [ ] read `estimate-skill-grill-me-asks-in-rounds`
```

### Case 443.2 — case-guppi asks in rounds before it builds the Case

> **given:**
> `rule-case-build` — the rule of `case-guppi` and its Render
> **＋** `.claude/agents/case-guppi.md` — the agent file it renders
> **＋** `estimate-case-build-writes-the-case` — the promise of the agent's answer
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill the agent loads by its `skills` field
> **＋** `vault/wiki/case-schema.md` — the form of the Case the agent reads
> **＋** `.claude/agents/ask-guppi.md` — the vault query the agent runs itself
> **＋** `.claude/settings.json` — the hooks the agent reads for a Case that changes a hook
> **＋** `rule-case-check` — the `SubagentStop` check of the agent's answer

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else.
> **＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, from the heading to the fence of `ratification`, and nothing else.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** It writes no file and no ledger line.

```then
update:
- slug: rule-case-build
  replace:
  - old: and answers with the Case alone; the main agent shows it
    new: and answers with a round of questions by the skill `grill-me` while a fork of the item is open, and with the Case alone when none is; the main agent shows it
  - old: and answer with the Case alone. Asked again by SendMessage with the person's question or change.
    new: and answer with a round of questions while a fork is open, or with the Case alone. Asked again by SendMessage with the person's answers, question or change.
  - old: 'tools: Read, Grep, Glob'
    new: |-
      tools: Read, Grep, Glob
      skills: [grill-me]
  - old: 'a later message holds the person''s question or change on the Case you built. You decide nothing the person has not decided: when the Case needs a choice the words do not give, answer with that question alone, with no Case heading.'
    new: a later message holds the person's answers to your round of questions, verbatim and untranslated, or the person's question or change on the Case you built. You decide nothing the person has not decided.
  - old: 'Answer with the Case in the chat form of the schema, from its heading to the fence of `ratification`, and nothing else: no line before it, no note after it.'
    new: |-
      After you read the frame, look for the forks of the item: a choice the Case needs that the person's words do not give. Check the item against each kind of fork: the bound — what enters `given` and what does not; the alternative — a second reasonable `recommend`; the promise — a new Estimate, or a Criterion replaced; the split — one promise or sub-cases; the exceptions — the `－` lines of `then`; and what is left not done. While a fork is open, answer with a round of questions by the skill `grill-me`, loaded into your context by the `skills` field: its numbered questions, each with a title, a body and your recommended answer, in English, with no Case heading and nothing else. The main agent shows the round to the person and sends you the answers; answer with the next round, or with the Case when no fork is left. A round may come at the first answer on an item, after a message on a Case you built, and in Work Mode when a ratified Case is built again. The showing of the Case and its ratification confirm the shared understanding: no step of confirmation follows the last round.

      When no fork is open, answer with the Case in the chat form of the schema, from its heading to the fence of `ratification`, and nothing else: no line before it, no note after it.
  - old: Asked again by a message, answer with the Case whole again, changed as asked.
    new: Asked again by a message, answer with the Case whole again, changed as asked, or with a round when the message opens a fork.
  change: case-guppi loads grill-me by the skills field and answers with a round of questions while a fork is open (case 443.2)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
    purpose: case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame and answers with it alone
    method: 'by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case, one Case with a create without a ref and one that changes a hook; the tokens and seconds of each dispatch in the estimate line'
  change: the Criterion replaced whole — case-guppi answers with a round of questions while a fork is open (case 443.2)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-writes-the-case`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-the-case`
```

### Case 443.3 — the main agent relays a round

> **given:**
> `rule-case-protocol` — the rule of the Case schema and of the showing of a Case
> **＋** `vault/wiki/case-schema.md` — its Render, the text the main agent follows
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing
> **＋** `rule-case-build` — the agent that answers with a round or with the Case
> **＋** `rule-case-check` — the `Stop` comparison of a showing with the answer
> **＋** `.claude/agents/ask-guppi.md` — the vault query the main agent dispatches at pre-spec
> **＋** `rule-language` — Russian in the chat, English in the repository

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions or answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case.
> **＋** An answer with no Case heading is a round of questions: the main agent shows it translated into Russian, slugs, paths and quotations unchanged, and no Case is shown.
> **＋** No step of confirmation follows the last round: the next showing is the Case.
> **＋** The main agent shows the Case of the answer whole at every showing — its name, `context`, `problem` and `recommend` translated into Russian, its `given`, `when`, `then`, `tasks` and `ratification` as the answer holds them — and its own text after one horizontal rule; a showing that the `Stop` comparison of `rule-case-check` refuses is followed, before the person answers, by a reply that shows the answer whole, translated the same way.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is shown and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`.
    new: A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do the person's answers to a round of questions, verbatim and untranslated.
  - old: an answer with no Case heading is a question, which the agent puts to the person, and no Case is shown.
    new: an answer with no Case heading is a round of questions by the skill `grill-me` (`rule-case-build`), which the agent shows translated into Russian, slugs, paths and quotations unchanged, and no Case is shown; a round may come at the first answer on an item, after a question or a change on a shown Case, and in Work Mode when a ratified Case is built again, and the showing of the Case and its ratification confirm the rounds, with no step of their own. An item that needs no decision — Work, a reading again — the agent closes alone, with no dispatch.
  - old: and the agent's own text; `given`
    new: a round of questions of `case-guppi`, translated the same way, and the agent's own text; `given`
  change: the main agent shows a round of case-guppi translated and passes the person's answers verbatim (case 443.3)
- slug: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — a round shown translated, the answers passed verbatim, no step of confirmation (case 443.3)
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] update `estimate-case-protocol-shows-the-built-case`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-shows-the-built-case`
```

## Case 444 — the fence standard

> **context:**
> Several readers in the pipeline decide where a fenced block opens and where it closes, and each one uses its own pattern. `guppi/materialize.py` knows only backtick fences and closes a block on the next line of backticks. `guppi/ratified.py` reads a fenced value under a sub-point and ends it at the first line of three backticks. `guppi/casecheck.py` requires that `ratification` opens and closes with exactly three backticks. `guppi/prespec.py` imports the pattern of `materialize`. `guppi/ledger.py` has a pattern of its own, and it is the only reader that knows tildes. None of them knows the length of a fence. So a sub-point value that holds its own fence, such as a template of questions with a code block in it, is cut at the inner fence. For this reason, a Case ratified earlier in this session moves the template in `.claude/skills/grill-me/SKILL.md` into an indented block. Today the file still holds a fenced block, and this Case does not change what that Case does. The Spec hook writes the `then` and `tasks` blocks with a fixed fence of three backticks, so a value with a fence inside would break the block it is written into. One judgment in several copies is what `rule-one-judgment-one-implementation` forbids.
> No rule page describes a fence. `rule-spec-write` describes the blocks it writes but not their fence. The Render of `rule-case-protocol` allows a fenced block under a sub-point and says nothing about a fence inside it. `rule-ledger-write` stays deferred on another question. Only the code of `guppi/ledger.py` changes, and its `How it works` stays true, because a `LEDGER` block is still a fence opened with that tag. Case 445 of this session takes up `rule-spec-reconcile`: a guard replaces the comparison of the plan with a ratified copy, and the Spec hook no longer writes that copy. Neither the guard nor this Case changes the other. The one `create` has a `ref`, so the vault query was not run. The slug `estimate-materialize-judges-a-fence` is free in `wiki/` and in `archive/`.
> `guppi/ledger.py` cannot import `guppi/materialize.py` at the top of the module, because `materialize` imports `ledger`. It imports inside the function, as it already does for `parse_line`. The writer depends on the readers: today a fence of four backticks is read as a fence tagged with a backtick. So 444.2 depends on 444.1. Case 445 changes `rule-spec-write` with its own `replace` pairs. Its first pair and the pair of 444.2 stand in one sentence of `How it works`, the one that ends in "appended otherwise". Their anchors do not overlap, so both apply. The other pairs of Case 445 stand in other sentences. The pair of 444.3 and the pairs of Case 445 on `rule-case-protocol` stand in different sentences.
> The Criterion of `estimate-spec-write-copies-the-ratified-case` describes the blocks the hook writes, so 444.2 replaces it whole, and Case 445 leaves that Estimate to 444.2. The new Criterion does not mention the ratified copy, because Case 445 removes it. It covers the blocks written into the Spec of the session and the block of a short-form defer, because the `when` of 444.2 names both. The `purpose` and the `method` also mention the copy, so 444.2 sets both. The slug stays: it names the Case that was ratified, not the copy. The Criterion's line on a fenced block under a sub-point stays true under 444.1 and is kept; the new Estimate holds the reading. `estimate-spec-write-writes-a-defer` writes the `then` block as the reply shows it. The content is kept and only the fence is chosen, so it stands. Several Criteria mention a fence, a `LEDGER` block or the blocks of the Spec in words that stay true when a fence is judged by CommonMark, so they stand: `estimate-prespec-catches-bare-wikilinks`, `estimate-prespec-matches-lines-and-items`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-protocol-case-form`, `estimate-case-protocol-defers-in-one-reply`, `estimate-ledger-write-lifts`, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` and `estimate-spec-write-reaches-the-approved-spec`. This Case follows `estimate-one-judgment-one-implementation-followed` and does not change it.

> **problem:**
> The pipeline has no single standard for a fence. The readers disagree on where a block ends, a value with a fence inside is cut, and the writer cannot fence such a value safely. The questions are: which standard holds, where its one judgment lives, how the Spec hook fences a block, and what the schema tells the writer of a Case.

### Case 444.1 — one judgment of a fence for every reader

> **given:**
> `guppi/materialize.py` — holds the one judgment of a fence and reads the blocks and sections of a Case by it
> **＋** `guppi/ratified.py` — reads the sections and the fenced values of the chat form
> **＋** `guppi/prespec.py` — reads the lines of a Case outside a fence
> **＋** `guppi/casecheck.py` — checks the fence of `ratification`
> **＋** `guppi/ledger.py` — reads the lines of a `LEDGER` fence
> **＋** `tests/test_materialize.py` — runs every reader over the same texts
> **＋** `rule-materialize` — the rule that owns `guppi/materialize.py`, the `ref` of the new Estimate
> **＋** `estimate-materialize-judges-a-fence` — the promise of the one judgment
> **＋** `rule-one-judgment-one-implementation` — one judgment lives in one module

> **when:**
> A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `case_text` and `criterion_text` of `guppi/materialize.py`, `quoted_sections` and `fenced_value` of `guppi/ratified.py`, `plan_prose` of `guppi/prespec.py`, the check of `ratification` in `guppi/casecheck.py`, or `ledger_lines` of `guppi/ledger.py`.

> **then:**
> A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
> **＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
> **＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
> **＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
> **＋** Every one of these readers takes the judgment from the functions of `guppi/materialize.py`, and they all give the same answer for the same text.
> **－** No reader keeps a fence pattern of its own: the `FENCE` of `guppi/ledger.py`, the `OPEN_FENCE` of `guppi/ratified.py`, and the tests on three backticks in `guppi/ratified.py` and `guppi/casecheck.py` are removed.

```then
create:
- slug: estimate-materialize-judges-a-fence
  type: estimate
  kind: QA
  purpose: 'Every reader of a fence judges it by the functions of guppi/materialize.py, as CommonMark does: a fence closes only on a run of its own character at least as long'
  method: uv run pytest tests/test_materialize.py -k fence
  tags:
  - harness
  - workflow
  - tests
  ref: rule-materialize
```

```tasks
- [ ] create `estimate-materialize-judges-a-fence`
- [x] `guppi/materialize.py` — one function that reads the opening of a fence (its character, its length, its tag) and one that says whether a line closes it; `then_blocks`, `tagged_blocks`, `case_text` and `criterion_text` judge by them; `FENCE` replaced; the docstring names the judgment
- [x] `guppi/ratified.py` — `quoted_sections` and `fenced_value` judge by the functions of `guppi/materialize.py`; `OPEN_FENCE` and the close on three backticks removed
- [x] `guppi/prespec.py` — `plan_prose` judges by the functions of `guppi/materialize.py`
- [x] `guppi/casecheck.py` — `form_findings` judges the fence of `ratification` by the functions of `guppi/materialize.py`
- [x] `guppi/ledger.py` — `ledger_lines` judges by the functions of `guppi/materialize.py`, imported inside the function since `guppi/materialize.py` imports this module; its `FENCE` removed
- [x] `tests/test_materialize.py` — one test, named so that `-k fence` picks it, runs every reader of the `when` over the same texts (a fence inside a longer fence, a tilde fence, a closing line with a shorter run, a word after the run, a sub-point value that holds a fence) and asserts they answer alike
- [ ] read `estimate-materialize-judges-a-fence`
```

### Case 444.2 — the Spec hook fences a block by its content

> **given:**
> `guppi/ratified.py` — writes the `then` and `tasks` blocks of a Case into the Spec
> **＋** `guppi/materialize.py` — gives the fence of a block, beside the one judgment of a fence
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, written by the hook once it stands
> **＋** `tests/test_ratified.py` — the tests of the write
> **＋** `rule-spec-write` — its `How it works` describes the write
> **＋** `estimate-spec-write-copies-the-ratified-case` — the promise of the write
> **＋** `rule-one-judgment-one-implementation` — one judgment lives in one module

> **when:**
> The `Stop` hook `uv run guppi ratified` writes a Case into the plan file or into `raw/<date>/<hi HHMM>/spec.md` (a whole Case, a deferred Case in the short form, or the parent of a sub-case) with its block tagged `then` or `tasks`.

> **then:**
> Each block opens with a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least, and closes with a fence of the same length.
> **＋** One function of `guppi/materialize.py`, beside the one judgment of a fence, gives that fence.
> **＋** When `tagged_blocks` and `then_blocks` of `guppi/materialize.py` read the block back, they give its content whole.
> **－** A block with no run of three backticks inside keeps its fence of three backticks.

```then
update:
- slug: rule-spec-write
  replace:
  - old: a block tagged `then` built from the sub-points of `tasks`, and a block tagged `tasks` of the task lines without their sub-points;
    new: a block tagged `then` built from the sub-points of `tasks`, and a block tagged `tasks` of the task lines without their sub-points, each opened and closed by a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least (case 444.2);
  change: the fence of the then and tasks blocks is chosen by their content (case 444.2)
- slug: estimate-spec-write-copies-the-ratified-case
  set:
    status: pending
    purpose: The ratified Case enters the plan file in the words of the stored answer of case-guppi, the then block built from the sub-points, each block fenced by its content
    method: uv run pytest tests/test_ratified.py -k write; the live reading by hand, the plan file after the first ratification of a session
  sections:
    Criterion: |-
      When:
      The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads the session's transcript for the last earlier reply that shows `## Case N —` whole, and `<plan>.checked.json` beside the plan file for the answer of `case-guppi` stored under Case N.

      Then:
      The hook writes the stored answer of Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as the answer holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `recommend` and `ratification` are not written.
      **＋** Each of the two blocks opens and closes with a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least; `tagged_blocks` of `guppi/materialize.py` reads it back whole.
      **＋** The same fence rule holds for the blocks the hook writes into `raw/<date>/<hi HHMM>/spec.md` once it stands, and for the `then` block of a short-form defer it writes under `## Deferred`.
      **＋** A last showing of Case N that differs from the stored answer — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
      **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
      **＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item — the one judgment `guppi/materialize.py` lifts by and `guppi/generate.py` applies by — is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` on stderr, and nothing of the Case is written.
      **＋** A value that holds a backtick in an outer span not padded on both sides is refused: exit 2 with `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
      **＋** No plan file in the event log, no showing of Case N whole, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
      **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
  change: the Criterion replaced whole — the fence of each written block is one longer than the longest fence inside it; the ratified copy no longer named (cases 444.2, 445.2)
```

```tasks
- [ ] update `rule-spec-write` — one `replace` pair in `How it works`
- [ ] update `estimate-spec-write-copies-the-ratified-case` — the Criterion replaced whole, the purpose and the method with no ratified copy
- [x] `guppi/materialize.py` — one function that gives the fence for a text: backticks one longer than the longest run of backticks that opens a line of the text, three at the least
- [x] `guppi/ratified.py` — `spec_section`, `deferred_section` and `write_parent` fence the `then` and `tasks` blocks by the function of `guppi/materialize.py`
- [x] `tests/test_ratified.py` — a test named so that `-k write` picks it: a `sections` value that holds a fence of three and one of four backticks is written in a block fenced by five, and `tagged_blocks` reads it back whole; a block with no fence inside keeps three
- [ ] read `estimate-spec-write-copies-the-ratified-case`
```

### Case 444.3 — the schema says an outer fence is longer than any fence inside

> **given:**
> `rule-case-protocol` — its Render holds the sentence on the chat form of a sub-point value
> **＋** `vault/wiki/case-schema.md` — the file rendered from it

> **when:**
> The agent or `case-guppi` reads `vault/wiki/case-schema.md` to write the value of a sub-point of `tasks` as a fenced block.

> **then:**
> `vault/wiki/case-schema.md` says that a fenced block under a sub-point opens with a fence longer than any fence of the same character inside it.
> **－** The sentence on a code span and its padding (case 402) stays as it stands.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: or a fenced block under the sub-point; a Case off this form is not written
    new: or a fenced block under the sub-point, its opening fence longer than any fence of the same character inside it (case 444.3); a Case off this form is not written
  change: a fenced value opens with a fence longer than any fence inside it (case 444.3)
```

```tasks
- [ ] update `rule-case-protocol` — one `replace` pair in its Render
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 445 — the plan is written by the hooks alone: a guard on the plan, the ratified copy removed, `/hi` only in plan mode

> **context:**
> Today the hooks write each Case into the plan file. The `Stop` hook of `rule-spec-write` writes the stored English answer of `case-guppi`, and it writes a short-form defer from the reply. The agent can still edit the plan by hand. `uv run guppi ratified --edit` on `PostToolUse` compares an edited plan with the ratified copy `<plan>.ratified.md`, which the same hook function writes beside it. The comparison covers only what the scripts apply, so a change of a name, `context` or `problem` passes without a word. In session 1745 the agent showed the short-form defer of Case 442. It then edited the plan to translate its heading, `context` and `problem`, and `estimate-case-protocol-defers-in-one-reply` failed on that edit. Case 423 deferred this question to `rule-spec-reconcile`. Case 441 answered its second half. `case-guppi` answers in English, the main agent translates only for the chat, and a short form is written in English as it is shown. After that, no step needs the agent to edit the plan. Once nothing but the hook writes the Cases, the copy only compares the plan with itself.
>
> The person decided the following. Every edit of a plan file that exists is refused for the whole session, not only while a line under `## Cases` is open. The one exception is a `Write` that creates a plan file with one title line. The agent's edits of the stores `<plan>.checked.json` are refused too. The ratified copy goes, and with it the `--edit` hook, the marks `<plan>.waiting.json` and the comparison of pre-spec with the copy. The Cyrillic finding of pre-spec stays, and its Estimate moves to `rule-language`. `/hi` opens a session only in plan mode, and a payload with no `permission_mode` is refused. A session repaired without `/hi` is a known path, since the fix of session 1745 was made that way. The refusal is the promise of `rule-event-log`, whose hook writes the `hi` line. `rule-skill-hi` only describes it. In session 1337 a session that began outside plan mode wrote a second plan file under another name. With `/hi` refused outside plan mode, that path needs no exception in the guard. The second count of C4 is text after the Frontier in the defer reply. No mechanical check covers it, and it is not done here. `estimate-case-protocol-defers-in-one-reply` stays failed until a later reading. The ticks of `raw/<date>/<hi HHMM>/spec.md` are out of this Case and are Frontier item C14. The agent still ticks that file, so the guard does not cover it.
>
> The frame gives the following. A call the guard refuses has no `PostToolUse`, so the `event tool` hook writes no `tool Write:` line for it, and `plan_path` of `guppi/ledger.py` still names the plan. The docstring of `guppi/guard.py` records the same for its own refusals. `is_plan` of `guppi/ratified.py` and `plan_path` judge a plan path with two copies of one test, and 445.1 puts that test in one function. `uv run guppi guard` stands on the same `PreToolUse` matcher and refuses only files that a rule page governs. No rule page governs a plan file, so the two hooks judge different files. The hooks of one `UserPromptSubmit` group run in parallel. So the refusal of `/hi` lives in `uv run guppi event prompt`, which writes the `hi` line; a refusal in `guppi gate` would still leave the line written. The agent's `Skill` call of `hi` is no path, because the skill carries `disable-model-invocation: true`. The hooks documentation lists `permission_mode` among the input fields common to every event, and its example of `UserPromptSubmit` carries the field. No probe in the repository has read it on that event, so the `method` of `estimate-event-log-records` reads it live. `ratified.untranslated` today reads only the Cases before `## Deferred`, so a short form shown in Russian would pass. 445.4 extends it to `## Deferred`, which is why the person kept the finding. At the first ratification, sub-case 445.5 carried two ledger lines. One created `estimate-skill-hi-opens-only-in-plan-mode`, and one updated `rule-skill-hi`. The ledger only grows, and that Estimate is no longer created. So 445.7 carries the update of `rule-skill-hi` with `{supersedes:case 445.5}`, which retires both lines of 445.5 and takes its section out of the plan.
>
> The frame also gives these contradictions. Case 444.2, ratified in this session, replaces the Criterion of `estimate-spec-write-copies-the-ratified-case`, and its `when` and one `＋` line name the ratified copy. One Criterion is not signed twice in one session, so this Case does not name that Estimate. 444.2 goes back to its `case-guppi` to drop the copy and is ratified again. In the same step, its `case-guppi` corrects the sentence of Case 444's `context` that says `rule-spec-reconcile` stays deferred. The last `－` line of `estimate-spec-write-writes-a-defer` says the ratified copy gets no defer. It stays true when no copy exists, so it stands. The Render of `rule-language` and one `＋` line of `estimate-language-followed` still say that the prose is translated into English before approval. That has been false since Case 441. They stand here and are Frontier item C15. Some Estimates stay true and stand. `estimate-hi-writes-frontier` and `estimate-hi-no-read-calls` read a `/hi` that opens a session, and a refused `/hi` opens none. `estimate-default-mode` promises that the session opens in Plan Mode, and 445.6 enforces that. `estimate-hook-registry-rendered` promises only that the file equals the Render. `estimate-case-protocol-shows-the-built-case` already says that the agent edits no Case in the plan, and the guard keeps that true. The `Result` sections and History lines that name the copy are records and stay.

> **problem:**
> Whether a guard refuses every edit of the plan by the agent while a line under `## Cases` of the Frontier is open, and when and how the prose of a Case is translated (the question of case 410).

### Case 445.1 — the guard refuses the agent's edits of the plan file and its store

> **given:**
> `rule-spec-reconcile` — the rule whose guard this is
> **＋** `estimate-spec-reconcile-shows-a-changed-case` — the promise of the rule
> **＋** `guppi/ratified.py` — the hook `uv run guppi ratified --guard`, and the `--edit` hook it replaces
> **＋** `guppi/ledger.py` — `plan_path`, and the one function that judges a plan path
> **＋** `tests/test_ratified.py` — the tests of the guard
> **＋** `.claude/plans/` — the folder of the plan files and of their stores `<plan>.checked.json`
> **＋** `rule-hook-registry` — the registrations of `.claude/settings.json`
> **＋** `.claude/settings.json` — the file rendered from it

> **when:**
> The agent calls `Edit`, `Write` or `MultiEdit` on a file under `.claude/plans/`, and `uv run guppi ratified --guard` on `PreToolUse` reads the path and the content of the call.

> **then:**
> The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
> **＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way.
> **＋** A refusal writes one line of the refusal to the day's event log and no `tool` line, so `plan_path` of `guppi/ledger.py` still names the plan file.
> **＋** A plan file is a `.md` file under `.claude/plans/`, judged by one function of `guppi/ledger.py` that `plan_path` uses too.
> **－** An edit of a file outside `.claude/plans/` is not judged by this hook.
> **－** A payload the hook cannot read: exit 0 with one line on stderr.
> **－** No `PostToolUse` hook compares an edit of the plan: `uv run guppi ratified --edit` and the marks `<plan>.waiting.json` are gone.

```then
update:
- slug: rule-spec-reconcile
  replace:
  - old: The prose of a Case — its name, `context` and `problem` — is Russian in the ratified copy and English in the approved Spec, so it is not compared; everything the scripts apply is.
    new: 'Since case 441 the hooks alone write the Cases into the plan: the `Stop` hook of `rule-spec-write` writes the stored answer of `case-guppi`, and a Case changes only through its `case-guppi` and a new ratification. The agent writes only the title line that creates the plan, and a hook refuses any other edit of it before it lands; the comparison with a ratified copy that stood here from case 387.3 is gone (case 445.1).'
  sections:
    How it works: '`uv run guppi ratified --guard` on `PreToolUse` of `Edit`, `Write` and `MultiEdit`. A plan file is a `.md` file under `.claude/plans/`, judged by one function of `guppi/ledger.py` that `plan_path` also uses; the store `<plan>.checked.json` of `rule-case-check` lies beside it. The hook refuses every `Edit` and `MultiEdit` of a plan file or a store, every `Write` of a store, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run. The one exception is a `Write` of a plan file that does not exist whose content, trimmed, is one line that opens with `# ` — the title line the agent writes before the first dispatch of `case-guppi`; the hooks find the plan by that write in the event log, so no hook can create it. A refusal writes one line to the day''s event log; a refused call has no `PostToolUse`, so it leaves no `tool` line and does not move `plan_path`. The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and this hook does not judge them. A payload the hook cannot read: exit 0 with one line on stderr; it never raises. Until case 445.1 the rule was a comparison: `guppi ratified --edit` on `PostToolUse` compared an edited plan with a ratified copy `<plan>.ratified.md` and marked a changed Case in `<plan>.waiting.json` for its showing; the copy, the marks and that hook are gone.'
  set:
    implementation_ref:
    - guppi/ratified.py
    - guppi/ledger.py
    - tests/test_ratified.py
    - .claude/settings.json
  change: the guard refuses the agent's edits of the plan and its store, the title line that creates the plan excepted; the comparison with the ratified copy goes (case 445.1)
- slug: estimate-spec-reconcile-shows-a-changed-case
  rename: estimate-spec-reconcile-refuses-an-edit-of-the-plan
  set:
    status: pending
    purpose: An edit of the plan file or its store by the agent is refused, the one Write that creates the plan with its title line excepted
    method: uv run pytest tests/test_ratified.py -k guard; by hand, the first refused edit of the plan in a session after the change
  change: the Criterion replaced whole — the guard refuses the edit instead of comparing it with the ratified copy (case 445.1)
- slug: rule-hook-registry
  replace:
  - old: '"command": "uv run guppi guard", "timeout": 30 } ] },'
    new: '"command": "uv run guppi guard", "timeout": 30 }, { "type": "command", "command": "uv run guppi ratified --guard", "timeout": 30 } ] },'
  - old: '"uv run guppi spec", "timeout": 30 } ] }, { "matcher": "Edit|Write|MultiEdit", "hooks": [ { "type": "command", "command": "uv run guppi ratified --edit", "timeout": 30 } ] },'
    new: '"uv run guppi spec", "timeout": 30 } ] },'
  change: guppi ratified --guard registered on PreToolUse of Edit, Write and MultiEdit; guppi ratified --edit removed from PostToolUse (case 445.1)
```

```tasks
- [ ] update `rule-spec-reconcile`
- [ ] update `estimate-spec-reconcile-shows-a-changed-case`
- [ ] update `rule-hook-registry`
- [ ] `uv run guppi render`: `.claude/settings.json`
- [x] `guppi/ledger.py` — one function judges whether a path is a `.md` file under `.claude/plans/`; `plan_path` uses it
- [x] `guppi/ratified.py` — `--guard` for `PreToolUse`: refuses as the `then` says, writes the line of the refusal, judges a plan path by the function of `guppi/ledger.py`; `edit`, `check_marks`, `read_marks`, `marks_of`, `MARKS_SUFFIX`, `is_plan`, the `--edit` flag and the call of `check_marks` in `stop` removed; the docstring
- [x] `tests/test_ratified.py` — tests named so that `-k guard` picks them: an `Edit` and a `MultiEdit` of a plan refused; a `Write` of an existing plan refused; a `Write` that creates a plan with one title line let through, with a title and a Case refused; every edit of a `.checked.json` refused; a file outside `.claude/plans/` let through; no `tool` line written on a refusal; the tests of the `--edit` hook and the marks removed
- [ ] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
```

### Case 445.2 — the Spec hook writes no ratified copy

> **given:**
> `rule-spec-write` — the rule of the Spec hook
> **＋** `estimate-spec-write-checks-the-written-case` — the promise of the check after the write
> **＋** `guppi/ratified.py` — the write into the plan, its copy and `spec.md`
> **＋** `tests/test_ratified.py` — the tests of the write
> **＋** `rule-case-protocol` — its Render describes the write and the edit of the plan
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `rule-case-check` — its `How it works` names what it leaves to `/pre-spec`
> **＋** `guppi/casecheck.py` — its docstring names the same

> **when:**
> The `Stop` hook `uv run guppi ratified` has written Case N into the plan file after a reply whose `LEDGER` block holds the decision lines of Case N.

> **then:**
> The hook runs the checks of `prespec --check` on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
> **＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
> **＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan file.
> **＋** A finding of a Case not written in this run is not reported.
> **－** On the re-fire (`stop_hook_active`) nothing is checked: exit 0.
> **－** A Case not written in this run, and a defer-only Case, which the hook writes under `## Deferred`, are not checked.
> **－** The Frontier is not read, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
> **－** A ledger line of the window that does not parse is no finding of this check.
> **－** The plan is compared with no other file, and no ratified copy `<plan>.ratified.md` is written.

```then
update:
- slug: rule-spec-write
  replace:
  - old: 'into the plan file named by `gate.plan_path` and into the ratified copy `<plan>.ratified.md` beside it, outside the repository:'
    new: 'into the plan file named by `gate.plan_path`, outside the repository:'
  - old: without the Frontier, the ratified copy, the translation and the grammar of the ledger, which stay with `/pre-spec`
    new: without the Frontier, the translation and the grammar of the ledger, which stay with `/pre-spec`
  - old: the ratified copy gets none, and the check after the write does not run on it (case 421.1)
    new: the check after the write does not run on it (case 421.1)
  - old: from the plan file, the ratified copy and, once it stands, `spec.md` in the session's folder
    new: from the plan file and, once it stands, `spec.md` in the session's folder
  change: the hook writes no ratified copy (case 445.2)
- slug: rule-case-protocol
  replace:
  - old: the agent does not edit a Case in the plan file, and `rule-spec-reconcile` names an edit of the plan that changes what the scripts apply.
    new: the agent does not edit the plan file, and the hook of `rule-spec-reconcile` refuses its edit, the title line that creates the file excepted (case 445.1).
  - old: removes it from the plan file, the ratified copy and, once it stands,
    new: removes it from the plan file and, once it stands,
  - old: into the plan file and into the ratified copy `<plan>.ratified.md` beside it, outside the repository, and, once
    new: into the plan file, outside the repository, and, once
  change: the plan has no ratified copy, and the agent's edit of the plan is refused (cases 445.1, 445.2)
- slug: rule-case-check
  replace:
  - old: the Frontier and the ratified copy left to `/pre-spec`
    new: the Frontier left to `/pre-spec`
  change: pre-spec compares the plan with no ratified copy (case 445.2)
- slug: estimate-spec-write-checks-the-written-case
  set:
    status: pending
  change: the Criterion replaced whole — the Case is written into the plan file alone, no ratified copy (case 445.2)
```

```tasks
- [ ] update `rule-spec-write`
- [ ] update `rule-case-protocol`
- [ ] update `rule-case-check`
- [ ] update `estimate-spec-write-checks-the-written-case`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `guppi/ratified.py` — `write_case`, `write_parent` and `remove_superseded` write the plan and, once it stands, `spec.md`, and no copy; `copy_of`, `COPY_SUFFIX` and the title of a copy removed; the docstring
- [x] `guppi/casecheck.py` — the docstring no longer names the ratified copy
- [x] `tests/test_ratified.py` — the tests of the copy removed; a test named so that `-k write` picks it asserts that no `.ratified.md` file is written beside the plan
- [ ] read `estimate-spec-write-checks-the-written-case`
```

### Case 445.3 — a superseded Case leaves the plan file and the Spec, with no copy

> **given:**
> `estimate-spec-write-removes-a-superseded-case` — the promise of the removal
> **＋** `rule-spec-write` — the rule of the Spec hook
> **＋** `guppi/ratified.py` — `remove_superseded`
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the Spec of the session

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds a decision line carrying `{supersedes:case N}`, and it has written the Case of that line in the same run.

> **then:**
> The hook removes the section of Case N — its heading, its sections, its `then` and `tasks` blocks, and the sections of its sub-cases — from the plan file.
> **＋** Once `raw/<hi date>/<hi HHMM>/spec.md` stands, it removes every section of Case N and of its sub-cases from it too.
> **＋** A `{supersedes:case N.M}` removes the section of that sub-case alone; its parent and its other sub-cases stay.
> **＋** A section of Case N under `## Deferred` is removed the same way.
> **－** A Case N that neither file holds — a Case of an earlier session, a defer taken up — is no refusal, and nothing is removed.
> **－** A line whose own Case the hook refused or did not write removes nothing.
> **－** On the re-fire (`stop_hook_active`) nothing is removed: exit 0.

```then
update:
- slug: estimate-spec-write-removes-a-superseded-case
  set:
    status: pending
    purpose: A Case superseded by a decision line of the reply leaves the plan file and spec.md, with its sub-cases
  change: the Criterion replaced whole — no ratified copy to remove it from (case 445.3)
```

```tasks
- [ ] update `estimate-spec-write-removes-a-superseded-case`
- [ ] read `estimate-spec-write-removes-a-superseded-case`
```

### Case 445.4 — the Cyrillic finding of pre-spec becomes the check of `rule-language`

> **given:**
> `rule-language` — the rule that the repository is written in English, the target of the new Estimate
> **＋** `estimate-language-spec-prose-in-english` — the new promise
> **＋** `estimate-prespec-checks-the-ratified-copy` — the promise it replaces
> **＋** `rule-prespec` — the rule of `/pre-spec`
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from it
> **＋** `guppi/prespec.py` — `guppi prespec --check`
> **＋** `guppi/ratified.py` — `untranslated` and `differences`
> **＋** `tests/test_prespec.py` — the tests of the check

> **when:**
> `guppi prespec --check <plan>` runs at `/pre-spec` and reads the plan file.

> **then:**
> A name, `context` or `problem` of a Case of the plan that holds a Cyrillic letter: one finding naming the Case and the part.
> **＋** A short-form Case under `## Deferred` is read the same way.
> **＋** A plan whose names, contexts and problems hold no Cyrillic letter gives no finding of this check.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.
> **－** The plan is compared with no other file: no ratified copy is read.

```then
create:
- slug: estimate-language-spec-prose-in-english
  type: estimate
  ref: rule-language
  kind: QA
  purpose: Pre-spec finds a name, context or problem of a Case of the plan that holds a Cyrillic letter, a short form under Deferred included
  method: uv run pytest tests/test_prespec.py -k cyrillic
  tags:
  - harness
  - workflow
update:
- slug: rule-prespec
  replace:
  - old: It also prints one line for every Case of the plan whose ids, `given`, `when`, `then`, `then` block or `tasks` differ from its section in the ratified copy `<plan>.ratified.md` beside the plan file, for every Case of the plan with no section there and every section there with no Case in the plan — a Case a `{supersedes:case N}` of the window names excepted, and a parent with sub-cases in the copy, every one of them named by such a line (case 417), and the Cases under `## Deferred` not compared — and for every name, `context` or `problem` still holding a Cyrillic letter — `case-guppi` writes English, and such a Case goes back to it (cases 387.4, 441).
    new: It also prints one line for every name, `context` or `problem` of a Case still holding a Cyrillic letter, a short form under `## Deferred` included — `case-guppi` writes English and a short form is shown in English; such a Case goes back to its `case-guppi`, and such a short form is shown again as a new short Case (cases 387.4, 441, 445.4).
  change: pre-spec compares the plan with no ratified copy; the Cyrillic finding reads Deferred too (case 445.4)
delete:
- slug: estimate-prespec-checks-the-ratified-copy
  impact: The comparison with the ratified copy ends with the copy (case 445.2); the Cyrillic finding it also held moves to estimate-language-spec-prose-in-english; rule-prespec loses it from estimates by the cascade
```

```tasks
- [ ] delete `estimate-prespec-checks-the-ratified-copy`
- [ ] create `estimate-language-spec-prose-in-english`
- [ ] update `rule-prespec`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] `guppi/ratified.py` — `differences`, `compared_parts`, `outside_deferred` and `COMPARED` removed; `untranslated` reads every Case of the plan, `## Deferred` included
- [x] `guppi/prespec.py` — `--check` drops the comparison with the ratified copy and keeps the Cyrillic finding; the docstring
- [x] `tests/test_prespec.py` — the tests of the ratified copy removed; tests named so that `-k cyrillic` picks them: a Cyrillic name, `context` and `problem` found, one under `## Deferred` found, Cyrillic in `given` or in a block not found, an English plan clean
- [ ] read `estimate-language-spec-prose-in-english`
```

### Case 445.6 — the event log refuses a `/hi` outside plan mode

> **given:**
> `rule-event-log` — the rule of the event log and of the `hi` line
> **＋** `estimate-event-log-records` — its promise
> **＋** `guppi/event.py` — `uv run guppi event <name>`, and `event prompt`, which writes the `hi` line on `/hi`
> **＋** `guppi/gate.py` — the marks `prespec`, `retro` and `handoff`
> **＋** `tests/test_event.py` — the tests of the event hooks
> **＋** `tests/test_gate.py` — the tests of the marks
> **＋** `raw/<date>/event_log.md` — the day's event log
> **＋** `.gitignore` — keeps the log out of git

> **when:**
> A session starts, a tool call completes, the person submits a prompt, or the agent calls a skill through `Skill`; `uv run guppi event <name>` and `uv run guppi gate` read the JSON payload through a pipe, its `session_id` the stamp.

> **then:**
> After the start and one tool call, `raw/<date>/event_log.md` carries a `session-start` line with the session's stamp and a `tool` line after it.
> **＋** On `/hi` whose `permission_mode` is `plan`, when no `hi` of this stamp follows its first `session-start`: the line `- HH:MM:SS <stamp> hi` and its `hi:` line on stdout, which names the session's folder; a second `/hi` writes nothing and prints `hi: already recorded`, with the time and the folder; exit 0.
> **＋** On `/hi` whose `permission_mode` is any other value — `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` — or is missing or empty, a second `/hi` included: no line, nothing on stdout, exit 2 with a reason on stderr that tells the person to turn plan mode on and type `/hi` again; Claude Code blocks the prompt, and the skill does not run.
> **＋** Any other prompt is silent, and its `permission_mode` is not read: exit 0; an error goes to stderr only, exit 0.
> **＋** A call of `pre-spec`, `retro` or `handoff` through `Skill` that the gate lets through appends `- HH:MM:SS <stamp> <mark>` — `prespec`, `retro`, `handoff` — in the form `guppi event` writes; a refusal writes no line; `hi` and other skills get no mark.
> **＋** `git check-ignore` reports the log ignored by `.gitignore`; a hook invocation with piped stdin that refuses nothing exits 0 and finishes under 2 s.

```then
update:
- slug: rule-event-log
  replace:
  - old: a second `/hi` of the same session and any other prompt write nothing (case 111.1).
    new: a second `/hi` of the same session and any other prompt write nothing (case 111.1); a `/hi` whose `permission_mode` is not `plan`, missing or empty included, writes no line, prints nothing on stdout and exits 2 with the reason on stderr, and Claude Code blocks the prompt (case 445.6).
  - old: 'The hook never fails the session: any error goes to stderr and the exit code is 0.'
    new: 'The hook never fails the session on an error: any error goes to stderr and the exit code is 0; its one exit 2 is the refusal of a `/hi` outside plan mode (case 445.6).'
  set:
    implementation_ref:
    - guppi/event.py
    - guppi/gate.py
    - guppi/cli.py
    - tests/test_gate.py
    - tests/test_event.py
    - .claude/settings.json
  change: no hi line outside plan mode; the refusal exits 2 (case 445.6)
- slug: estimate-event-log-records
  set:
    status: pending
    method: pytest in tests/test_event.py and tests/test_gate.py with piped JSON payloads against a temp vault; the git-ignore and timing readings once by hand, through a pipe, written into the estimate line; by hand, one /hi outside plan mode and one in it, the permission_mode of each payload written into the reading
  change: the Criterion replaced whole — a /hi outside plan mode writes no hi and exits 2; the Given folded into When (case 445.6)
```

```tasks
- [ ] update `rule-event-log`
- [ ] update `estimate-event-log-records`
- [x] `guppi/event.py` — one function judges a `/hi` payload by its `permission_mode`; `run` on `prompt` writes no line, prints nothing on stdout and exits 2 with the reason on stderr when it refuses; the docstring: errors still exit 0, the refusal exits 2
- [x] `tests/test_event.py` — tests named so that `-k plan_mode` picks them: `/hi` with `plan` writes the line; with `default`, `acceptEdits`, `auto`, `dontAsk` or `bypassPermissions`, with the field missing and empty: exit 2, no line, nothing on stdout; a second `/hi` outside plan mode refused; another prompt outside plan mode exit 0
- [ ] read `estimate-event-log-records`
```

### Case 445.7 — `rule-skill-hi` says that `/hi` opens a session only in plan mode

> **given:**
> `rule-skill-hi` — the rule of `/hi`, whose `How it works` describes who opens a session
> **＋** `rule-event-log` — the rule whose hook refuses a `/hi` outside plan mode
> **＋** `rule-session` — a working session goes from Session Start to Plan Mode

> **when:**
> The agent or the person reads the `How it works` of `rule-skill-hi`.

> **then:**
> It says that only the person opens a working session, and only in plan mode.
> **＋** It names `rule-event-log` as the rule whose hook refuses a `/hi` outside plan mode, and says that `defaultMode: plan` does not hold when the mode changes before `/hi`.
> **－** It promises no behaviour of its own: the refusal is read on the Estimate of `rule-event-log`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: '`disable-model-invocation: true` in the frontmatter: only the person opens a working session.'
    new: '`disable-model-invocation: true` in the frontmatter: only the person opens a working session, and only in plan mode: the hook of `rule-event-log` refuses a `/hi` whose `permission_mode` is not `plan`, missing or empty included, writes no `hi` line, and Claude Code blocks the prompt (case 445.6). `defaultMode: plan` in `.claude/settings.json` does not hold when the mode changes before `/hi`; a session begun outside plan mode once wrote its plan file under a second name. A session repaired without `/hi` stays possible: it holds no Case.'
  change: the page says /hi opens a session only in plan mode, refused by the hook of rule-event-log (case 445.7)
```

```tasks
- [ ] update `rule-skill-hi`
```

## Case 446 — The rule of the language drops the translation step before approval

> **context:**
> The `## Language` section of `CLAUDE.md` is the Render of `rule-language`. It says that the name of a Case, its `context`, `problem` and `recommend` "are Russian in the chat and are translated into English in the Spec before its approval". The Criterion of `estimate-language-followed` repeats the step: "The name, `context` and `problem` are translated into English in the Spec before its approval."
> Since Case 441 this step does not exist. `case-guppi` answers in English. The main agent translates the prose into Russian only for the chat. The hook of `rule-spec-write` writes the stored English answer into the Spec. So nobody translates anything into English before approval.
> Case 441 also made the main agent write a short-form defer in English in the chat, and the hook writes it as shown. This makes a second part of the same sentence false. The Render and the Criterion both say that the name, `context` and `problem` of every Case are Russian in the chat, but a short-form Case is English there.
> The Criterion has one more fault: it says `recommend` enters the Spec, and it does not. The Decision pages of Case 441 record that the person kept the sentence then because the result still held. They also name the smallest wording: "are Russian in the chat and English in the Spec".
> The vault's answer: this Case creates no page, so there was no slug to ask about. Among the live pages and the files of the repository, the sentence stands in three places only: `CLAUDE.md`, the Render of `rule-language` and the Criterion of `estimate-language-followed`. Decision pages are not counted in that search. No code tests the sentence. The sentence also stands in records under `raw/` and `archive/`: the Spec and `materialize.yaml` of session 1745, the Spec and `materialize.yaml` of the archived session 1859 of 2026-09-23, and the Frontier of this session. Those files keep it as records, and this Case does not change them.
> `case-guppi` read the frame and found three things that stay as they are. The `## Language` section of `vault/wiki/case-schema.md` already states the English answer and the English short form, so it stays true and does not change. The `Purpose` of `rule-language` and its `purpose` field also stay true. `estimate-claude-md-rendered` only promises that the file equals the Render and is loaded, so this Case does not touch it (case 378.5).
> `estimate-language-followed` stands `failed` from session 1745. This Case replaces its Criterion whole and sets it `pending`. After that, the ledger hook refuses a reading of it in this session (case 428.1). So Frontier line W32 cannot close by a reading this session.

> **problem:**
> The Render of `rule-language`, which is `CLAUDE.md`, and the Criterion of `estimate-language-followed` describe a step that is gone: an English translation of the prose of a Case before approval. They also say that a short-form Case is Russian in the chat, but it is English there. A session reads a false rule on its first turn, and a reading of the Estimate checks a step nobody takes.

> **given:**
> `rule-language` — its Render is the `## Language` section of `CLAUDE.md`
> **＋** `CLAUDE.md` — the `## Language` section, rendered from `rule-language`
> **＋** `estimate-language-followed` — the Estimate of `rule-language`
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of a session
> **＋** `vault/wiki/case-schema.md` — its `## Language` section and the short form constrain the wording

> **when:**
> A session starts with `CLAUDE.md`, and the agent writes into the repository or into the chat.

> **then:**
> Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the approved Spec in `raw/<date>/<hi HHMM>/spec.md` — is English.
> **＋** The chat with the owner is Russian: the name of a Case, its `context`, `problem` and `recommend`, and the agent's own text.
> **＋** The name, `context` and `problem` of a Case are English in `raw/<date>/<hi HHMM>/spec.md`.
> **＋** A Case's `given`, `when`, `then` and `tasks` — lines and sub-points — are English in the chat and enter `raw/<date>/<hi HHMM>/spec.md` unchanged.
> **＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
> **－** A short-form Case of `vault/wiki/case-schema.md` is not Russian in the chat: it stands there in English, as `raw/<date>/<hi HHMM>/spec.md` holds it.
> **－** The rule speaks of the language, not of the Case form — the form is `vault/wiki/case-schema.md`.

```then
update:
- slug: rule-language
  replace:
  - old: the name of a Case, its `context`, `problem` and `recommend` are Russian in the chat and are translated into English in the Spec before its approval; its `given`, `when`, `then` and `tasks` are English in the chat, the words that enter the Spec and the vault unchanged.
    new: the name of a Case, its `context`, `problem` and `recommend` are Russian in the chat, and its name, `context` and `problem` are English in the Spec; its `given`, `when`, `then` and `tasks` are English in the chat, the words that enter the Spec and the vault unchanged; a short-form Case is English in the chat, as the Spec holds it.
  change: the prose of a Case is Russian in the chat and English in the Spec, with no translation step before approval since Case 441; a short-form Case is English in the chat (case 446)
- slug: estimate-language-followed
  set:
    status: pending
  change: the Criterion replaced whole — the name, context and problem are English in the Spec with no translation step since Case 441; a short-form Case is English in the chat (case 446)
```

```tasks
- [ ] update `rule-language` — the sentence of the Render on the prose of a Case
- [ ] update `estimate-language-followed` — the Criterion replaced whole
- [ ] `uv run guppi render`: `CLAUDE.md`
- [ ] read `estimate-language-followed` — by hand in a later session
```

## Deferred

## Case 447 — the ticks of Work Mode live in the Spec

> **context:**
> Today the approved plan is copied to `raw/<date>/<hi HHMM>/spec.md`, and the same file holds the state of the work. The agent ticks its boxes in Work Mode, `generate` ticks the page and `read` lines, `render`, `sprint` and `glossary` tick their command lines, and the Spec hook keeps the ticks of unchanged task lines when a Case is ratified again. Retro, the librarian and `/carry` read the unticked boxes of `spec.md` as open work. So the Spec is at once the signed record and a working file, and the guard of Case 445.1 cannot cover it. The person wants the Spec written by the hook alone and the ticks moved to a separate work file, `raw/<date>/<hi HHMM>/work.md`, the seed of the implementation plan of `rule-work-mode`. The change touches eight promises and a one-off migration of every session under `raw/`.

> **problem:**
> Where the ticks of Work Mode live, and whether the Spec may change during the work other than by the hook. The person defers the decision until the sprint reaches Work Mode; until then the ticks stay in `spec.md` as they are.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The ticks of Work Mode move out of the Spec into a work file made at approval, the seed of the implementation plan; spec.md is then written by the hook alone and guarded like the plan
```

## Case 448 — the Pattern and Proposal of an actioned Insight contradict its newest lesson

> **context:**
> The Insight `insight-hi-skill-substitution-checked-by-a-model-call` names a lapsed login as the cause of the missing verdict on the `!` commands of `/hi`, and `/login` as the cure. Its newest child, `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier`, and Case 439 say that the server-side classifier of client 2.1.282 gives no verdict for a typed substitution, and `/login` did not help. The librarian clustered the lesson under the Insight, kept it `actioned` by Case 439, and left the Pattern and Proposal unchanged, flagging the contradiction in the brief.

> **problem:**
> The Pattern and Proposal of the Insight state a cause and a cure that its newest lesson and Case 439 refute. How they are rewritten is deferred.

```then
defer:
  - slug: insight-hi-skill-substitution-checked-by-a-model-call
    type: insight
    purpose: The Pattern and Proposal name a lapsed login and /login, while the newest lesson and Case 439 name the server-side classifier of client 2.1.282
```
