<!-- approved 13:12:44 · session f7321efe -->

# Session 0807 — the effort and the model of a case-guppi set at its dispatch

## Case 1029 — The main agent dispatches case-guppi at a chosen effort, and a trial measures it

> **context:**
> Every Case is built by `case-guppi` at one setting: `.claude/agents/case-guppi.md` sets `model: opus` and `effort: medium`, whatever the Case changes. The person finds GUPPI slow, and the handoff of session 0358 reports trial sessions of 45 to 55 minutes, about 40 of them agent time. The brief item C11 and the person's item C15 are merged here by the person's word. The prompt said a Grep of `effort|^model:` over the agent files printed nothing; those files were read, and that statement is false, so medium, not the session level, is the level the trial starts from. No document describes a way to change the effort of a running agent, so raising during the work is not built; the person chose no raise. The page https://code.claude.com/docs/en/sub-agents.md says of a non-fork subagent that Claude can pass an `effort` parameter for one invocation, that "The parameter overrides the `effort` field and stays in effect when the subagent is resumed", that `CLAUDE_CODE_EFFORT_LEVEL` takes precedence over both, and that the parameter "requires Claude Code v2.1.292 or later". The transcript of this session records version 2.1.317, and `.claude/settings.json` sets no such variable in its `env`. The page https://code.claude.com/docs/en/model-config.md says that Opus 5.5 takes `low`, `medium`, `high`, `xhigh` and `max`. The harness does not change for `case-guppi` itself: its frontmatter stays the level of a call that passes none, so `rule-case-build` needs no update, but `estimate-case-build-writes-the-case` says it runs at `effort: medium`, which a call at `low` makes false, so Case 1029.2 replaces its Criterion whole, the line that said so leaving on purpose for two lines that say what the file sets and what the call sets, and sets nothing else of it anew, since its `purpose` and `method` state no level. At the request of the line Other Case of Case 1031, whose file I read whole, the same Criterion also drops the promise and the split from its forks, and its lines on a fix that adds a second behaviour, on a new Case beside a ratified one and on a change asked on a named Case give way to one pointer to `estimate-case-build-settles-form-by-itself`, which Case 1031.1 creates, so that promise is not signed twice; those lines leave on purpose, and the line on a pair of that new Case leaves with them, since its promise and the number, the missing mark and the file of a Case built beside a ratified one go into the Criterion of that Estimate through Case 1031.1, as a finding of `/pre-spec` set it; the pointer keeps the words "and no sub-cases" of the Render of Case 1031.1. The finished file of Case 1031 was read again after its build: its Criterion of that Estimate holds that a change asked on a Case is built under that Case's number, so the line here on a change asked by a message or by `/pre-spec` points to it for that half and keeps only its own words on a number outside Work Mode, and the line here that a fix which changes what a ratified Case set is built again under a new number stands, since 1031.1 does not say it. The `method` of the Estimate is set anew with a reading after a session whose `orchestration.md` holds the text of Case 1029.1, since only the transcript of such a session shows the effort of a call. Since `prespec.py` refuses a second replacement of one Criterion in a session, the change stands here and not in Case 1031. The governing rule of the dispatch is `rule-orchestration`, whose `## Who builds a Case` sets what the prompt of the call holds; the skills `setup`, `sprint-open`, `sprint-close`, `merge-main` and `pr-review` dispatch `case-guppi`, each but `setup` by the words as `vault/wiki/orchestration.md` sets it, and `orchestration.md` is loaded at `/hi`, so one sentence there covers them and no skill changes. The Estimates of `rule-orchestration` were read by `purpose`; `estimate-orchestration-names-related-cases-in-the-dispatch` speaks of the prompt of the call and `estimate-orchestration-shows-the-built-case` of the showing, so neither names the level, and they stand. A Grep of `effort` over the root with the glob `{vault/wiki,.claude,.guppi/guppi}/**` printed 5 files: `vault/wiki/brief.md`, not read as a brief, `.claude/agents/case-guppi.md` and `vault/wiki/rules/rule-case-build.md`, which stand as the default, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, which enters the Case, and `vault/wiki/rules/rule-permissions.md`, whose hit is the word best-effort and stands. `test_orchestration.py` reads `orchestration.md` live, but only its blocks tagged `showing` and `defer`, which the pair does not touch.
>
> The new command is measurement, not behaviour of a session. `.guppi/guppi/context.py` counts tokens for the main agent only: `call_size` sums the input, cache and output tokens of one call, and `is_main` of `.guppi/guppi/ledger.py` with `read_records` keep the records of a file. I read those functions whole, and `user_kind`, `given_back_at` and `transcript_records`. Each agent of a session leaves `subagents/agent-<id>.jsonl` and `agent-<id>.meta.json` beside the transcript, in this session and in the three trial folders of session 0358; the meta file holds `agentType`, `description` and `toolUseId`, and the notification of a finished run holds `subagent_tokens`, `tool_uses` and `duration_ms`, the same text standing on more than one record of the transcript. A Grep of `task-notification|duration_ms|subagent_tokens|meta\.json|"Agent"|subagent_type` over `.guppi/guppi/` printed `casecheck.py`, `event.py` and `ledger.py`; none reads `duration_ms`, `subagent_tokens` or a meta file, and `given_back_at` judges only which text came back, so the module adds no second copy of a judgment and imports `call_size`, `is_main` and `read_records`. The vault query of `.claude/agents/ask-guppi.md` found no page that covers the cost per agent: exists none; near `rule-context-size`, which counts from the transcript; rules `rule-one-judgment-one-implementation`; tags `harness`, `session`, `workflow`. The person chose that page, so the paths go onto it, it stays `built`, and `estimate-context-size-agents-counts-each-agent` stands on it; its three Estimates speak of the size line and its errors and stand. A Grep of `gitstate`, a command that stands in the list, with the same glob in the mode of paths printed 11 files, and the only one that lists the commands is `.guppi/guppi/cli.py`, whose docstring lists hook commands only, so `agents` enters `COMMANDS` and its imports alone; `log.md` was not read. For the new files, a Grep of `\.guppi/guppi/?[\s"'`)]|\.guppi/tests/?[\s"'`)]` printed 11 hits in 6 files of `.guppi/guppi/`, 4 hits in 3 files of `.claude/` and 43 files of `vault/wiki/rules/`, and a Grep of the bare names `guppi/` and `tests/` printed 3 hits in `.guppi/guppi/generate.py`, none in `.claude/` and 79 hits in 41 files of `vault/wiki/rules/`; the hits read name the two folders as places, and none lists their files. For the folder `.guppi/` that holds both, a Grep of `(^|[^\w/.-])\.guppi(/|\b)` printed 250 hits in 38 files of `.guppi/guppi/`, 59 hits in 14 files of `.claude/` and 300 hits in 66 files of `vault/wiki/rules/`, most of them paths under it or the `--project .guppi` of a command, and a Grep of the folder alone, `` \.guppi/[\s"'`)]|\.guppi/$|`\.guppi`|"\.guppi"|'\.guppi' ``, over `.guppi/guppi/` printed `codewrite.py`, `ledger.py` and `ship.py`: `codewrite.py` judges each file written under `.guppi/`, so the new module keeps each pointer in a bracket, and `TREES` of `ship.py` copies `.guppi` whole. A Grep of `os\.walk|\.rglob\(|\.glob\(|\.iterdir\(` printed 46 hits in 14 files of `.guppi/guppi/`, of which the walk of `ship.py` copies and cleans the new module and `casecheck.py` searches for names, the others walking the vault and the session folders; over `.guppi/tests/` it printed 27 hits in 15 files, of which `test_guppi_package.py` reads old command spellings, so the module spells `uv run --project .guppi guppi`, and none other walks a folder of the new files. Two more readers take every file of these folders: the key `style` of `guppi.toml`, `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`, run by `guppi style` and by the CI of the copy, and the collection of pytest under `testpaths = ["tests"]` of `.guppi/pyproject.toml`; neither is made wrong while the new files pass the style check, and the test is collected there by its name. The root `.gitignore` and `.guppi/.gitignore` ignore neither new file. No reader is made wrong.
>
> The trial ends at the close of the sprint `plugin`, where a Research Estimate with `once: true` on `entity-sprint-plugin` asks the person; `once` keeps it out of the clean version, and a page with `core: true` does not wait on it. The `## Purpose` of the sprint page lists five conditions of done while it holds nine Estimates, so the sentence stands unchanged. The change reaches the main agent only at the librarian's render, so this session runs as today and is the baseline, and the reading of the dispatch waits for a later session by the part `after` of its `method`. `ask-guppi` stays as it is, since the count of its findings measures whether the builds got worse. The rest of the brief item, whether the setup and opening Cases need the full build and the audit, is not built here and is put to the person in the reading of Case 1029.4. Of the files the check of this file listed as naming what the Case changes, each was judged by its purpose line or path: they speak of other parts of `orchestration.md`, of `settings.json` or of `rule-context-size` in other terms, and they stand; the hit in `estimate-clean-branch-ships-neutral-texts` is a line of its Result, and the hit in `rule-harness` its list of children. Options on `sonnet`, on a raise and on a smaller effort for `ask-guppi` were not chosen and are not built. The session's ledger does not yet stand, so no lesson is marked.

> **problem:**
> Every Case costs the same build, whatever it changes, and no count shows where the time goes. The person wants the main agent to dispatch `case-guppi` at a chosen effort, a measure of what that gives, and a decision on keeping it.

> **recommend:**
> - **Which level for which Case**
>   - Recommended: (a) three kinds by what the Case changes, `low`, `medium` and `high`, the person's word overriding.
>   - Answer: agreed, (a).
> - **The model at the dispatch**
>   - Recommended: (b) `sonnet` only on the person's word for a session.
>   - Answer: (a) effort only; the call passes no model.
> - **Raising the level during a Case**
>   - Recommended: (b) a new dispatch one level up only when the Case proves to be of a higher kind.
>   - Answer: (a) no raise; the level chosen at the dispatch holds to the end of the Case.
> - **Whether `ask-guppi` enters this Case**
>   - Recommended: (a) it stays out.
>   - Answer: agreed, (a).
> - **How the time and tokens are measured**
>   - Recommended: (a) a command with a test.
>   - Answer: agreed, (a).
> - **When the trial ends**
>   - Recommended: (a) at the close of the sprint `plugin`, a check on the sprint page waiting for the person's answer.
>   - Answer: agreed, (a).
> - **The rest of the brief item**
>   - Recommended: (a) left to the decision after the trial.
>   - Answer: agreed, (a).
> - **The page of the new command**
>   - Recommended: (a) add the paths to `rule-context-size`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by the line Other Case of Case 1031, whose round the person answered (a), the Criterion that Case 1029.2 writes drops the promise and the split from its forks, and its lines on a fix that adds a second behaviour, on a new Case beside a ratified one and on a change asked on a named Case give way to one pointer to `estimate-case-build-settles-form-by-itself`.
>   - Taken: the Criterion of Case 1029.2 changed so; each other word of it stands.

### Case 1029.1 — The main agent passes an effort at each dispatch of case-guppi

> **given:**
> `rule-orchestration`: the page whose Render sets the dispatch of `case-guppi`.
> **＋** `vault/wiki/orchestration.md`: the Render, loaded at `/hi`.
> **＋** `estimate-orchestration-dispatches-case-guppi-at-a-level`: the new check of the level.
> **＋** `.claude/agents/ask-guppi.md`: the agent this Case leaves as it is.

> **when:**
> The main agent, with `vault/wiki/orchestration.md` loaded, dispatches `case-guppi` by the Agent tool for a Case of Plan Mode or Work Mode.

> **then:**
> The call passes the parameter `effort`, by what the Frontier item and the person's words ask the Case to change.
> **＋** The level is `low` for a Case that changes only the text of pages and no code, and for the setup Case and the opening Case of a sprint.
> **＋** The level is `high` for a Case that changes a hook, a check or other code that judges a text.
> **＋** The level is `medium` for every other Case.
> **＋** The person's word on a Case sets another level up to `high`, and the call passes that level.
> **＋** The level holds to the end of the Case, through each `SendMessage`.
> **－** No new dispatch raises the level of a Case.
> **－** No call passes `xhigh` or `max`.
> **－** No call passes the parameter `model`.
> **－** The dispatch of `.claude/agents/ask-guppi.md` does not change.

```then
create:
- slug: estimate-orchestration-dispatches-case-guppi-at-a-level
  ref: rule-orchestration
  kind: QA
  purpose: Whether each call that dispatches case-guppi passes the effort of the kind of its Case, or the person's word up to high, holds it to the end of the Case, and passes no model
  method: 'by hand, at the Retro of the session that creates this Estimate, the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session whose orchestration.md holds this text: each Agent call of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, the transcript in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-orchestration
  replace:
  - old: A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do
    new: 'The call that dispatches `case-guppi` passes the parameter `effort` of the Agent tool, by what the Frontier item and the person''s words ask the Case to change: `low` for a Case that changes only the text of pages and no code, and for the setup Case and the opening Case of a sprint; `high` for a Case that changes a hook, a check or other code that judges a text; `medium` for every other Case (as set in case 1029.1). The person''s word on a Case sets another level up to `high`, and the call passes that level (as set in case 1029.1). The level holds to the end of the Case, through each `SendMessage`; no new dispatch raises it, no call passes `xhigh` or `max`, and no call passes the parameter `model` (as set in case 1029.1). A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do'
  change: the dispatch of case-guppi passes an effort by the kind of the Case
```

```tasks
- [x] create `estimate-orchestration-dispatches-case-guppi-at-a-level`
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-dispatches-case-guppi-at-a-level`
```

### Case 1029.2 — The Criterion of case-guppi takes the level from the call

> **given:**
> `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `.claude/agents/case-guppi.md`: its frontmatter stays the level of a call that passes none.
> **＋** `estimate-case-build-settles-form-by-itself`: the check of Case 1031.1 that the Criterion points to.
> **＋** `raw/2026-11-04/0807/cases/case-1031.md`: the file of Case 1031, which sets how a choice of form is settled.

> **when:**
> The main agent dispatches `case-guppi` of `.claude/agents/case-guppi.md` with the parameter `effort` or with none.

> **then:**
> `case-guppi` runs at the `effort` that the call passes.
> **＋** It runs at `effort: medium`, the value of `.claude/agents/case-guppi.md`, where the call passes none.
> **－** `.claude/agents/case-guppi.md` does not change.

```then
update:
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
    method: 'by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the tokens and seconds of each dispatch of case-guppi in that session, when there was one, in the estimate line; by hand, after a session whose orchestration.md sets the effort of each dispatch of case-guppi: the effort that each Agent call of case-guppi passed or did not pass, in the transcript of that session under ~/.claude/projects/, read against the lines of the Criterion on the effort, the transcript in the estimate line'
  sections:
    Criterion: |-
      When:
      The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
      **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
      **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
      **＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.

      Then:
      `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
      **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
      **＋** It reads each page and file the `given` names; of each Estimate such a page lists it reads the `purpose` line, and the Criterion of each one whose `purpose` speaks of the thing the Case changes; for a Case that adds or changes a hook, it reads the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
      **＋** While a fork is open — the bound, the alternative, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in the language of the repository, with no Case heading and nothing else but the context of a first round.
      **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
      **＋** When no fork is open, it writes the Case whole in the language of the repository in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
      **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
      **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
      **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
      **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
      **＋** Asked, by a message or by a finding of `/pre-spec`, to change a Case, it builds the change as `estimate-case-build-settles-form-by-itself` checks; outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it.
      **＋** A fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases it places as a choice of form, as `estimate-case-build-settles-form-by-itself` checks.
      **＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
      **＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
      **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
      **＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
      **＋** `.claude/agents/case-guppi.md` sets `model: opus`, `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, which Claude Code applies only while the session runs in `default` or `dontAsk` mode.
      **＋** It runs at the `effort` that the call that dispatches it passes, as `estimate-orchestration-dispatches-case-guppi-at-a-level` checks, and at `effort: medium` where the call passes none.
      **＋** In Plan Mode the guard of `rule-spec-reconcile` writes the text of its `Write` or `Edit` into its file and stops the call; a line of the guard that says the file is written it takes as the write done, does not make the call again, and reads the file by `Read` before its next `Edit` of it.
      **＋** `.claude/agents/case-guppi.md` sets `autoCompactWindow: 400000`, so Claude Code compacts the context of `case-guppi` before it reaches 400000 tokens.
      **＋** Before each answer, and first when a message brings the person's answers or a change, `case-guppi` writes `raw/<date>/<hi HHMM>/cases/note-<N>.md` whole by `Write`, N the id of the top-level Case: each question of its rounds by its title with its recommendation and the person's answer, the pages and files it read for the frame, the forks still open, and what is still to do.
      **＋** When its context opens with a summary of earlier work, it reads that note by `Read` before anything else, goes on from what it says, and reads again the pages and files its next step needs.
      **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
      **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
      **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
      **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
      **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
      **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
      **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
      **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
      **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, the file of a new Case it builds beside a ratified Case and its note, and no ledger line.
      **－** It asks no question again whose answer its note holds.
      **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.
  change: the Criterion replaced whole — the frontmatter is the level of a call that passes none
```

```tasks
- [x] update `estimate-case-build-writes-the-case`
- [ ] read `estimate-case-build-writes-the-case`
```

### Case 1029.3 — A command prints the time and tokens of each agent of a session

> **given:**
> `.guppi/guppi/agents.py`: the new module of the command.
> **＋** `~/.claude/projects/`: the folder of the session transcripts it reads.
> **＋** `subagents/agent-<id>.jsonl`: the transcript of one agent, beside `agent-<id>.meta.json`.
> **＋** `.guppi/guppi/cli.py`: the map of the commands.
> **＋** `.guppi/tests/test_agents.py`: the new test of the command.
> **＋** `.guppi/guppi/context.py`: its `call_size`, which the module imports.
> **＋** `.guppi/guppi/ledger.py`: its `read_records` and `is_main`, which the module imports.
> **＋** `rule-context-size`: the page that lists the code of the command.
> **＋** `estimate-context-size-agents-counts-each-agent`: the new check of the command.

> **when:**
> `uv run --project .guppi guppi agents <transcript>` of `.guppi/guppi/agents.py` runs on the path of a session transcript under `~/.claude/projects/`.

> **then:**
> It prints one line for the main agent and one line for each file `subagents/agent-<id>.jsonl` in the folder named after the transcript.
> **＋** The line of the main agent gives its calls, the sum of `call_size` over them, its tool calls, and the seconds from the first record of the transcript to the last.
> **＋** The line of an agent gives its type and description from `agent-<id>.meta.json`, the `effort` that its Agent call passed or `-`, the model of its calls, its calls, the sum of `call_size`, the `call_size` of its last call, and its tool calls.
> **＋** The line of an agent also gives its runs and seconds, from the `duration_ms` of each notification of a finished run, each notification counted once, or `-` where the transcript holds none.
> **－** It writes no file.
> **－** A transcript it cannot read gives one line on stderr and exit 1.
> **－** An agent with no `.meta.json` prints as `unknown`.

```then
create:
- slug: estimate-context-size-agents-counts-each-agent
  ref: rule-context-size
  kind: QA
  purpose: Whether guppi agents prints from a transcript one line for the main agent and one for each agent of the session, with its effort, model, calls, tokens, runs and seconds
  method: uv run --project .guppi pytest .guppi/tests/test_agents.py
  tags:
  - hooks
  - harness
  - session
update:
- slug: rule-context-size
  set:
    implementation_ref:
    - .guppi/guppi/context.py
    - .guppi/tests/test_context.py
    - .guppi/guppi/agents.py
    - .guppi/tests/test_agents.py
    - .claude/settings.json
  replace:
  - old: The size is counted from the transcript, where every API call of the model carries its `usage`.
    new: The size is counted from the transcript, where every API call of the model carries its `usage`. The command `guppi agents` counts from the same records the calls, tokens and seconds of the main agent and of each agent of a session, so that a choice of how agents run rests on a count (as set in case 1029.3).
  change: guppi agents counts the cost of each agent of a session
```

```tasks
- [x] `.guppi/guppi/agents.py`: the module with `run(argv, ...)`, importing `call_size` of `.guppi/guppi/context.py` and `read_records` and `is_main` of `.guppi/guppi/ledger.py`, each pointer in a bracket at the end of its sentence.
- [x] `.guppi/guppi/cli.py`: `agents` in the imports and in `COMMANDS`.
- [x] `.guppi/tests/test_agents.py`: a test over a transcript, a `subagents/` folder and a meta file under a temporary folder, with timestamps fixed in the data, for each line of the `then`, a repeated notification included.
- [x] update `rule-context-size`
- [x] create `estimate-context-size-agents-counts-each-agent`
- [x] by hand, at Retro: the command of `.guppi/guppi/agents.py` run over the transcript of this session and over each main transcript under `~/.claude/projects/C--PROJECTS-guppi-trial-0358-*/`, its output in the handoff of the session as the numbers the trial starts from.
- [x] read `estimate-context-size-agents-counts-each-agent`
```

### Case 1029.4 — The person decides at the close of the sprint whether the levels stay

> **given:**
> `entity-sprint-plugin`: the sprint page that holds the check of the trial.
> **＋** `estimate-sprint-plugin-case-guppi-level-trial-decided`: the new check, once.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI/f7321efe-eca6-49ea-9ba1-c44aec197fd9.jsonl`: the transcript of the session that holds the baseline.
> **＋** `~/.claude/projects/C--PROJECTS-guppi-trial-0358-*/`: the folders of the trial sessions, also the baseline.
> **＋** `.guppi/guppi/agents.py`: the command whose table the reading reads.
> **＋** `.claude/agents/ask-guppi.md`: the audit whose findings the reading counts.
> **＋** `rule-orchestration`: the levels the reading judges.

> **when:**
> The session that closes the sprint `plugin` runs `uv run --project .guppi guppi agents <transcript>` of `.guppi/guppi/agents.py` over `~/.claude/projects/c--PROJECTS-GUPPI/f7321efe-eca6-49ea-9ba1-c44aec197fd9.jsonl`, over the main transcripts under `~/.claude/projects/C--PROJECTS-guppi-trial-0358-*/`, and over the transcript of each session of the sprint after it.

> **then:**
> Determine how much time and how many tokens per Case the levels of `rule-orchestration` saved against those transcripts.
> **＋** Determine whether the findings of `.claude/agents/ask-guppi.md` and the changes the person asked per Case grew.
> **＋** The person answers whether the levels stay, go, or stay on trial, and whether the setup Case and the opening Case need the full build and the audit.
> **－** The session that closes the sprint carries out no such answer: a Case of a later session does.

```then
create:
- slug: estimate-sprint-plugin-case-guppi-level-trial-decided
  ref: entity-sprint-plugin
  kind: Research
  purpose: What the levels of the dispatch of case-guppi saved in time and tokens per Case, whether the builds got worse, and whether the person keeps them
  method: 'by hand, in the session that closes the sprint plugin: the output of guppi agents over the transcripts of the Criterion and the findings of ask-guppi in those transcripts read against the Criterion, the numbers and the person''s answer in the estimate line'
  tags:
  - sprint
  - workflow
  once: true
```

```tasks
- [x] create `estimate-sprint-plugin-case-guppi-level-trial-decided`
- [ ] read `estimate-sprint-plugin-case-guppi-level-trial-decided`
```

## Case 1030 — The clean copy passes its own style and tests, and a test runs them over it

> **context:**
> `guppi ship` builds the clean copy of GUPPI and removes each bracket that holds a pointer. `clean` of `.guppi/guppi/ship.py` calls `removed` of `.guppi/guppi/pointers.py`, which takes the bracket and one space before it and leaves the rest of the line. So a comment that held only a bracket stays as a bare `#`, and a docstring line that held only a bracket stays as spaces, since `BRACKET` takes the line break before a bracket only when a mark of punctuation follows it; the trial copy shows both, in `.guppi/guppi/casecheck.py:1019` and `.guppi/guppi/materialize.py:64`. `lesson-ship-leaves-an-empty-comment-after-a-removed-pointer` records the result at the three trial installs: `ruff check .` found 51 PLR2044, `ruff format` would reformat 5 files, and two tests failed. No record names the 5 files, and this build has no way to run `ruff`. The page https://docs.astral.sh/ruff/formatter/black/ says that "the preceding comment text still contributes to the line width", so a line can change its layout once it loses a pointer, which no edit of the text foresees; hence `ruff format` closes the build. The page https://docs.astral.sh/ruff/formatter/ says that `ruff format --check` exits 0 if no files would be formatted and that `ruff format` exits 2 on abnormal termination. https://raw.githubusercontent.com/astral-sh/ruff/main/crates/ruff_python_formatter/CONTRIBUTING.md lists "The second formatting pass looks different than the first (formatter instability or lack of idempotency)" as a thing its stability checks catch, and the new test reads the result. https://docs.astral.sh/uv/concepts/projects/dependencies/ says "By default, uv includes the `dev` dependency group in the environment (e.g., during `uv run` or `uv sync`)", so `.github/workflows/prod.yml` has `ruff` at its step `uv run --project .guppi guppi ship`, and `.guppi/.venv/Lib/site-packages/ruff/__main__.py` stands, so `python -m ruff` runs. The copy holds no `ship.py`, so it gains no need of `ruff` from this; `rule-guppi-package` says `.guppi/pyproject.toml` declares "pytest and ruff for the tests", which still holds. The page https://docs.astral.sh/ruff/rules/empty-comment/ says a fix is always available but not whether it is safe, so the Case writes the removal itself. The `ask-guppi` audit at `/pre-spec` found that the format, run inside the folder, writes a `.ruff_cache/` into the copy, as `.guppi/.ruff_cache/` of this repository shows; that would break the line of `estimate-clean-branch-writes-a-clean-copy` that says "It writes no cache folder of Python, pytest or ruff" and the exact set of files that `test_it_writes_the_code_the_harness_and_the_core_pages_only` of `.guppi/tests/test_ship.py` asserts, since `SKIPPED_NAMES` keeps the folder out only of the walk over the working tree. The page https://docs.astral.sh/ruff/settings/ says "By default, Ruff stores cache results in a `.ruff_cache` directory in the current project root", and the help that https://docs.astral.sh/ruff/configuration/ quotes gives `--no-cache` as "Disable cache reads", which does not say that nothing is written, and `--cache-dir <CACHE_DIR>` as "Path to the cache directory". So the run takes `--cache-dir` in a temporary folder outside the copy, and the Criterion line and that test stand.
>
> The two failed tests have plain causes. `.guppi/guppi/sprint.py:294` opens a string literal with the bracket, so the space stays at the end of the literal before it and the `/hi` line of the copy ends in a space; `test_hi_setup_pending_prints_the_setup_line_before_the_sprint_line` of `.guppi/tests/test_sprint.py` already takes off the bracket and needs no change once the literals break elsewhere. A Grep of `^\s*f?"\([^"]*cases? \d` over `.guppi/guppi/` printed that line alone. `test_cli_dispatches_to_lint` of `.guppi/tests/test_lint.py` expects a `status` finding that `check_status` of `.guppi/guppi/lint.py` gives only with `ship_stands`, which the copy answers no; it sets `ship_stands` true by `monkeypatch`, since the helper `ship_module` of that file puts a module with no `run` into `sys.modules`, which `.guppi/guppi/cli.py` would import where `cli` is first imported in the test. A new failure of the tests over the copy, from code of this session such as the module of Case 1029, is fixed in Work Mode under the same `then`.
>
> The last output of the checks: `vault/wiki/brief.md`, `## Readings at the close`, says of the working tree "`uv run --project .guppi guppi test`: exit 0, 1956 passed, 6 skipped, 1 deselected", and its `## Where things stand` says "`guppi style` clean"; neither runs over the copy, and the lesson above is the one output over a copy. The rule of what this changes is `rule-clean-branch`, whose `## Purpose` names `.guppi/guppi/pointers.py` in its text but not in `implementation_ref`; the field stays, since the person was asked nothing on it. I read `removed`, `outside`, `masked_strings`, `holds_pointer` and `words_beside` of `.guppi/guppi/pointers.py`, and `clean`, `judged`, `live_code`, `ship`, `settled`, `check` and `run` of `.guppi/guppi/ship.py`. `outside` calls `removed` with `keep_lines`, which keeps each line break the match took, so the wider `BRACKET` moves no line number of a `ship:` line and judges nothing else. A Grep of `\bremoved\(|BRACKET\b|tokenize\.COMMENT` over `.guppi/guppi/` printed `ship.py`, `pointers.py` and `ledger.py`, whose `BRACKET` reads a ledger line; no code there judges an empty comment, so the new function is no second copy, and it reads the comments by `tokenize` as `bare_numbers` does. `--check` writes nothing, so it needs no format. A Grep of `\bremoved\(|ship\.ship\(|ship\.clean\(|ship\.judged\(|ship\.BRACKET|pointers\.BRACKET` over `.guppi/tests/` printed 3 lines in `test_guppi_package.py` and `test_ship.py`. Each sample `.py` file of the builds of `test_ship.py` parses and keeps its text under the format as I read them, with `.guppi/pyproject.toml` of a sample holding no `[tool.ruff]`; a sample `ruff format` refuses would give the new `ship:` line, and Work Mode fixes it. The round said that the `live` mark otherwise keeps a build of the live pages out of `guppi test`; that was wrong, since `test_guppi_package.py` at line 104 already builds this repository in a normal test, so the style test adds no new kind of test.
>
> On the Estimates: `estimate-clean-branch-ships-the-tests` promised that the tests pass in the copy, read by hand after a tag, so its line `In the clean version, ... passes`, its `When` line `Then ... runs in that folder` and the by-hand part of its `method` leave it on purpose for the new `estimate-clean-branch-copy-passes-its-style-and-tests`, and the same `update` sets its `purpose` and `method` anew; its other lines stand word for word. The check refused the two Estimates in one Case, so Case 1030.1 holds the work and the new Estimate and Case 1030.2 the replaced Criterion. `estimate-clean-branch-writes-a-clean-copy` stands: it says the bracket goes with the space before it, which holds, and what it writes of the tests is what `estimate-clean-branch-ships-the-tests` sets. `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets` runs `-m live` over `test_ship.py`, so it also runs the new `live` test; its Criterion stands. `estimate-prespec-hook-reports-a-pointer-outside-a-bracket` stands since `outside` answers as before. A Grep of `estimate-clean-branch-ships-the-tests` over the root with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed `vault/wiki/log.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`; the two pages name it for what stays true. A Grep of `rule-clean-branch` over `.guppi/tests/` printed nothing, so no test reads that page. Not done: `.github/workflows/prod.yml` stays, so a copy whose tests fail can still reach `prod`; whether the suite passes on Linux was not read; `guppi check` over the copy and the `__pycache__/` of the copy (the Frontier item C8) are outside this Case. The finished file of Case 1029 was read whole after its build: it changes no page or file of this Case, and its Case 1029.3 adds `.guppi/guppi/agents.py`, `.guppi/tests/test_agents.py` and the command `agents` in `COMMANDS` of `.guppi/guppi/cli.py`, which the walk of `TREES` takes into the copy. Its module keeps each pointer in a bracket, so the cleaning and the format of Case 1030.1 serve it like any other file, and its test works over a temporary folder with data of its own, so it reads nothing that the copy lacks and runs in the test over the copy; none of it departs from this Case. The lesson stands in the ledger of session 0358, not of this session, so it gets no mark, and the ledger of this session holds no `error` lesson. Of the files the check of this file listed as naming what the Case changes, each was judged by its purpose line or path: they speak of what the copy holds, of its install, or of `settings.json`, `guppi sprint` and `test_lint.py` in other parts, and they stand; `estimate-skill-setup-starts-at-hi` was read, since it names the setup line of `.guppi/guppi/sprint.py`, whose printed text does not change, and `rule-plugin-install` and `estimate-sprint-plugin-installs-as-a-plugin` hold no sentence on the style or the tests of the copy.

> **problem:**
> The clean copy fails its own style commands and two of its own tests, so a project that installs GUPPI starts red, and nothing runs those commands over the copy, so the defect shows only at a trial install.

> **recommend:**
> - **How the copy gets clean style**
>   - Recommended: (a) remove the leftovers, then format the copy with `ruff format` at the end of the build.
>   - Answer: agreed, (a).
> - **Where the new test runs**
>   - Recommended: (c) style in `guppi test`, the tests over the copy under the `live` mark.
>   - Answer: agreed, (c).
> - **A guard before the `prod` branch**
>   - Recommended: (a) leave the workflow as it is.
>   - Answer: agreed, (a).
> - **What checks this Case**
>   - Recommended: (a) a new check, and the old line moves into it.
>   - Answer: agreed, (a).
> - **One Case or two**
>   - Recommended: (a) one Case.
>   - Answer: agreed, (a).
> - **How the old check gives up its promise**
>   - Recommended: (a) two sub-cases.
>   - Answer: (a).

### Case 1030.1 — The clean copy passes its own style and tests

> **given:**
> `rule-clean-branch`: the page of the build of the clean copy.
> **＋** `estimate-clean-branch-copy-passes-its-style-and-tests`: the new check.
> **＋** `.guppi/guppi/ship.py`: the build and its cleaning.
> **＋** `.guppi/guppi/pointers.py`: the removal of a bracket.
> **＋** `.guppi/guppi/sprint.py`: the line of `/hi` whose bracket opens a string.
> **＋** `.guppi/tests/test_ship.py`: the new tests.
> **＋** `.guppi/tests/test_lint.py`: the test that needs the module of `ship`.
> **＋** `guppi.toml`: the keys `style` and `test`, whose commands the tests run.
> **＋** `.github/workflows/prod.yml`: the workflow this Case leaves as it is.
> **＋** `.ruff_cache/`: the cache folder of `ruff`, which the copy does not hold.

> **when:**
> `uv run --project .guppi guppi ship <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean version from the working tree into an empty folder.
> **＋** Then `.guppi/tests/test_ship.py` runs over that folder the commands of the keys `style` and `test` of `guppi.toml`.

> **then:**
> In a Python file it writes, it removes each comment that the removal of a bracket left empty, with the spaces before it, and the whole line where that comment stood alone.
> **＋** In each text file it writes, a bracket that holds a pointer and stands alone on its line goes with that line.
> **＋** As its last step it runs `ruff format` over `.guppi/` of the folder.
> **＋** The commands of the key `style` exit 0 over the folder, in a test that `uv run --project .guppi guppi test` runs.
> **＋** The commands of the key `test` exit 0 over the folder, in a test marked `live`, and a test that needs a file or a module that the clean version does not hold is skipped.
> **－** Where `ruff format` does not start or does not exit 0, it prints one `ship:` line and exits 1.
> **－** That run keeps its cache in a temporary folder outside the folder, so the clean version holds no `.ruff_cache/`.
> **－** `--check` runs no `ruff format`.
> **－** `.github/workflows/prod.yml` does not change, and runs neither command over the folder.

```then
create:
- slug: estimate-clean-branch-copy-passes-its-style-and-tests
  ref: rule-clean-branch
  kind: QA
  purpose: Whether guppi ship leaves no empty comment and no line of spaces where it removed a bracket, formats the Python files of the clean version, and whether the style commands and the tests of the project pass over it
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k own_style; uv run --project .guppi pytest .guppi/tests/test_ship.py -m live -k own_tests
  tags:
  - plugin
  - ci
  - tests
update:
- slug: rule-clean-branch
  replace:
  - old: '`guppi ship` removes each bracket that holds a pointer whole, every word in it included, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays.'
    new: '`guppi ship` removes each bracket that holds a pointer whole, every word in it included, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays. A bracket that stands alone on its line goes with that line, and in a Python file a comment that the removal left empty goes with the spaces before it, and with its line where it stood alone. As its last step it runs `ruff format` over `.guppi/` of the clean version, by the settings of `.guppi/pyproject.toml`, since a line that loses a pointer can take another layout, and it prints a line and exits 1 where that run does not exit 0. So the clean version passes the commands of the key `style` of `rule-guppi-config`: a test of `.guppi/tests/test_ship.py` that `uv run --project .guppi guppi test` runs builds the clean version of this repository and runs them over it, and a test there marked `live` runs the commands of the key `test` over it (as set in case 1030).'
  change: the clean version passes its own style and tests, and a test runs them over it
```

```tasks
- [x] create `estimate-clean-branch-copy-passes-its-style-and-tests`
- [x] update `rule-clean-branch`
- [x] `.guppi/guppi/pointers.py`: `BRACKET` also takes the line break before a bracket that stands alone on its line, and its comment says so.
- [x] `.guppi/guppi/ship.py`: a function reads the comments of a Python text by `tokenize` and removes each one that holds nothing after its `#`, with the spaces before it, and its line where it stood alone; a text that does not tokenize stays as it is; `judged` runs it over a Python file after `clean`.
- [x] `.guppi/guppi/ship.py`: `ship` ends by running a constant `FORMAT`, `ruff format .guppi` by `sys.executable -m ruff`, in the folder after the skeletons, with `--cache-dir` a folder of `tempfile.TemporaryDirectory` outside the copy, removed after the run, and gives one `ship:` line where it does not start or does not exit 0; the module docstring says so, each pointer in a bracket at the end of its sentence.
- [x] `.guppi/guppi/sprint.py`: the string literals of the setup line break so that `the Frontier (rule-skill-setup, case 1017.3)` stands in one literal, and the line printed stays as it is.
- [x] `.guppi/tests/test_lint.py`: `test_cli_dispatches_to_lint` sets `lint.ship_stands` to answer true by `monkeypatch`, so it passes in the clean version too.
- [x] `.guppi/tests/test_ship.py`: tests whose names hold `own_style` over a sample tree: a comment left empty after code and on a line of its own, a docstring line left blank, and a `FORMAT` that exits 2, which gives its `ship:` line and exit 1; `test_it_writes_the_code_the_harness_and_the_core_pages_only` keeps its exact set of written files, so it goes red on a `.ruff_cache/` in the copy.
- [x] `.guppi/tests/test_ship.py`: `test_own_style_passes_over_the_copy`, unmarked, builds this repository by `ship` into a temporary folder and runs each command of the key `style` of `guppi.toml` there, its `uv run --project .guppi` replaced by `sys.executable -m`, each exit 0.
- [x] `.guppi/tests/test_ship.py`: `test_own_tests_pass_over_the_copy`, marked `live`, does the same for the key `test`, by `sys.executable -P -m` with `PYTHONPATH` the `.guppi` of the folder and no `CLAUDE_PROJECT_DIR` or `PYTEST_ADDOPTS` in its environment; the module docstring names both tests and the new Estimate.
- [x] read `estimate-clean-branch-copy-passes-its-style-and-tests`
```

### Case 1030.2 — The check of the shipped tests leaves the promise that they pass

> **given:**
> `estimate-clean-branch-ships-the-tests`: its Criterion is replaced whole.
> **＋** `rule-clean-branch`: the page of the build of the clean copy.
> **＋** `.guppi/tests/test_ship.py`: the tests the copy leaves out.
> **＋** `.guppi/.venv/`: the Python environment the copy leaves out.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes each file under `.guppi/tests/` but `.guppi/tests/test_ship.py`.
> **＋** In a Python file under `.guppi/tests/`, it removes a bracket that holds a pointer only from the comments and the docstrings, and it judges only them for a pointer outside a bracket and for a bare case number.
> **＋** Each other string of such a file is a sample: a case id there, such as `[case 10]` or `(case 320)` in the data of a test, is neither removed nor judged.
> **＋** `--check` judges each file under `.guppi/tests/` in place, in the same way.
> **－** The Python environment `.guppi/.venv/` stays out of the copy.
> **－** In a Python file outside `.guppi/tests/`, it judges the whole text as before.

```then
update:
- slug: estimate-clean-branch-ships-the-tests
  set:
    status: pending
    purpose: Whether guppi ship writes the tests but those of the command ship, cleans and judges only their comments and docstrings, and keeps their other strings as samples
    method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests
  change: the promise that the tests pass in the clean version moves to estimate-clean-branch-copy-passes-its-style-and-tests
```

```tasks
- [x] update `estimate-clean-branch-ships-the-tests`
- [x] read `estimate-clean-branch-ships-the-tests`
```

## Case 1031 — case-guppi settles questions of form itself, and the setup Case asks only what it cannot find

> **context:**
> `case-guppi` lists the kinds of choice it must put to the person, and that list holds the split of an item into Cases and the choice between a new Estimate and a replaced Criterion. Two more sentences of its frame order a question of form: which page lists code that no page covers, and where a fix goes that adds a second behaviour to a ratified Case. So the person answers bookkeeping that changes nothing the Case does. In this session Case 1030 asked one Case or two, and Case 1029 which page lists its new command; `.guppi/guppi/prespec.py` already prints "two promises in one Case — split it" for the split, in the function whose lines 1395 to 1428 I read. The person set the rule: the agent settles form itself and writes the choice in `context`, and asks only where the options differ in behaviour, in cost or in what they block, and the person's first answer of this build chose that both standing questions follow it. The rule that governs this is the one rule of `vault/wiki/ratification.md`: the agent has autonomy over how, none over the contract, and the person still ratifies each Case at its showing, so a settled form breaks nothing; the sentence there that a subagent at a fork never decides stands, since a choice of form is no fork. A choice of form with a real cost stays a question, such as a new page with `core: true` that keeps the clean version from building. The Criterion is no form: `when` and `then` stand before the person at the showing, and the sentences of case-561.11 and 800.1 stand, so a Case that can give no Estimate still asks what its Estimate will check, and `estimate-case-build-answers-what-done-means` stands; its line on a question of how a Case is checked holds for each such question that still comes. By this rule the split into three sub-cases and the choice of Estimates below were settled by the agent with no question.
>
> The Estimates of `rule-case-build` were read by `purpose`. `estimate-case-build-offers-a-page-for-code-no-page-covers` says a round offers the page, so Case 1031.2 replaces its Criterion and sets its `purpose` anew. `estimate-case-build-writes-the-case` lists the promise and the split among the forks and orders a round on the placed fix, and Case 1029.2 of this session already replaces that Criterion; `same_target_findings` of `.guppi/guppi/prespec.py`, read whole with `check_same_target`, refuses a second replacement in a session, so Case 1031.1 creates `estimate-case-build-settles-form-by-itself` for the promise, and Case 1029.2 makes the matching change: in its line that opens "While a fork is open", the words "the promise, the split" leave; its line on a fix that adds a second behaviour, its line "Where the person chooses a new Case beside it" and its line "It does not put a change asked on a named Case into a new top-level Case without the person's answer to a round" give way to a pointer to `estimate-case-build-settles-form-by-itself`, and each other word of its Criterion stands. `estimate-case-build-judges-options-against-the-broken-rule` and `estimate-case-build-records-the-rounds-in-recommend` speak of a round that comes, and they stand. A Grep of `the split` over the root with the glob `{vault/wiki,.claude}/**`, read by its lines, finds the fork list in `rule-case-build`, its render and `estimate-case-build-writes-the-case`; `vault/wiki/case-schema.md` and `rule-case-protocol` say that pre-spec asks for the split, which `prespec.py` asks of the agent and not of the person, so they stand, and the sentence of the schema on proposing a split stands, since a Case shown with its split is that proposal. `.claude/skills/grill-me/SKILL.md` says that decisions are the person's; it stands, since the frame of `case-guppi` says what a fork is, and a settled choice is no silent one, since `context` names it. A Grep of `second behaviour|Case beside` over the root with the glob `{vault/wiki,.claude,.guppi/guppi}/**` printed `.claude/agents/case-guppi.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md` and `vault/wiki/insights/insight-case-build-opens-a-new-case-where-one-was-named.md`; `log.md` was not read, and the insight records in History only that case 870 acted, and the first half of case 870, that a change goes under the number of the Case a message names, stands. A Grep of `offer in a round|turns? (down )?both` with that glob printed `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and the Estimate that Case 1031.2 replaces.
>
> The setup Case of `rule-morph` asks more than its Estimate allows, and `estimate-morph-sets-up-the-project-at-the-first-hi` stands `failed`. The transcripts of the three trial folders show each round asking how the setup is checked, and two asking one Case or several: the rule above closes those. They also show the questions on the keys `test` and `style`, which the person found unclear, and in `empty-git` an empty list for `test`, after which the build asked on `estimate-guppi-tests-green`, since `guppi test` would then run nothing. The person chose the option that asks only where the project holds code of its own, and asked that the question say how the project's tests run together with GUPPI's rather than which commands to set. `commands_of` of `.guppi/guppi/config.py` and `run` of `.guppi/guppi/commands.py` were read for what the keys do. The rule the option answers to is the line of the Criterion that the setup asks only for what it cannot find, and in a project with no code the value can be found. `rule-morph` keeps its sentence that the setup reads no code, since a list of paths is no text of a file. Its sentence that until the setup those settings name another project listed GUPPI's commands among what the setup replaces, which this Case makes false, so a pair of Case 1031.3 says that the setup keeps them (a finding of `/pre-spec`). The option rests on GUPPI's commands passing in a project: `vault/wiki/brief.md`, `## Readings at the close`, says of this repository "`uv run --project .guppi guppi test`: exit 0, 1956 passed, 6 skipped, 1 deselected", not of a copy, and at the moment of the reading the copy passes by Case 1030. The page https://docs.astral.sh/ruff/linter/ says "When linting a directory, Ruff searches for Python files recursively in that directory and all its subdirectories" and that it exits with `1` if violations were found, so the style check of GUPPI also reads the Python files of a project and may go red there: this Case does not change that. A Grep of `` `test` and `style`|key `test`|commands of the keys `` over the root with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed `vault/wiki/brief.md`, not read as a brief, `.claude/skills/setup/SKILL.md`, the replaced Estimate, `.guppi/guppi/cli.py`, `vault/wiki/rules/rule-skill-setup.md`, `vault/wiki/rules/rule-morph.md`, `vault/wiki/rules/rule-guppi-config.md`, `vault/wiki/estimates/estimate-guppi-config-runs-the-test-and-style-commands.md`, `.guppi/tests/test_commands.py`, `.guppi/guppi/commands.py` and `vault/wiki/rules/rule-guppi-package.md`; those that this Case does not change speak of what the keys run or of the repository of GUPPI, and they stand, and `estimate-guppi-tests-green` stands, since GUPPI's commands never leave the key. The setup Case creates no Estimate, as in the trials: its `context` names those that check its pages. `estimate-skill-setup-starts-at-hi` and `estimate-morph-takes-in-the-set-aside-files` speak of the start of the skill and of the set-aside files, and they stand. Its `method` is set anew, since the event it waited for has passed and the reading needs a copy that holds this text, and it adds a project with a source file of its own; the sprint page lists that reading as what remains of the milestone, so no sprint text changes.
>
> A Grep of `agents.*case-guppi|skills.*setup|rule-case-build\.md|rule-morph\.md|rule-skill-setup\.md|rule-guppi-config\.md` over `.guppi/tests/` printed `test_ship.py`, `test_config.py` and `test_casecheck.py`; the hits read build temporary folders or name a path as a string, so no test reads these files live and no test changes. No code changes. The ledger of the session holds no `error` lesson by a Grep of `lesson\[error\]`, so no mark is added. Not done: a Case of a later session may let the style check of GUPPI leave out the code of a project; the wording of the question is set in `rule-skill-setup` and the agent writes it at each setup.
>
> The check of this file listed the files that name the pages this Case changes, and I judged each by its purpose line or path. `rule-skill-grill-me` and `estimate-skill-grill-me-asks-in-rounds` say that each decision goes to the person, and they stand, since a choice of form is no decision of the person but a step the person still sees at the showing. `rule-atomicity` says that a split follows a mechanical test and not taste, which is what lets the agent settle it. `insight-case-build-opens-a-new-case-where-one-was-named` asks that a change go under the number of the Case the main agent names, and that sentence of `rule-case-build` stays. `lesson-case-build-gave-a-sub-case-no-estimate` stands, since each sub-case still names its Estimate. `estimate-skill-sprint-open-asks-the-opening-questions` speaks of the question that ends the setup reply, which does not change. The other files speak of the check, the showing, the ledger, the render or other steps of the frame, and they stand. In Case 1031.2, each line of the old Criterion of `estimate-case-build-offers-a-page-for-code-no-page-covers` that the new one does not carry word for word leaves on purpose: its trigger loses the words "under `vault/wiki/`", its round becomes a choice the agent settles, and its last lines now say "gets no page" in place of "gets no page offered". In Case 1031.3, the line that listed the commands of `test` and `style` among the values asked leaves on purpose for the line on code of the project. The sub-cases 1031.1 and 1031.2 share the words of the rule on form, since 1031.2 applies that rule to the one choice of a page.
>
> By the findings of `/pre-spec`: the Criterion of `estimate-case-build-settles-form-by-itself` also holds the lines of `rule-case-build` that Case 1029.2 points to it — a change goes under the number of the Case it is asked on, a new Case beside a ratified one takes a new number and no `{supersedes:case N}` mark, and the ratified file stays — and its `purpose` says so. At the second pass I read the finished file of Case 1029: its 1029.2 drops "the promise, the split" from the forks and points to this Estimate for a change asked on a Case and for a fix that adds a second behaviour, and it also drops its line on a pair of the new Case, which it leaves to this Estimate, so the Criterion here holds that line too; Case 1029 needs no further change. The `method` of `estimate-case-build-offers-a-page-for-code-no-page-covers` is set anew to a reading of the new Render in the Spec at Retro, since `.claude/agents/case-guppi.md` holds the new text only after the librarian's render.

> **problem:**
> `case-guppi` puts bookkeeping to the person as if it were a decision, and the setup Case of a new project asks for commands that the person cannot place, so the check of the setup fails and each Case costs questions that change nothing.

> **recommend:**
> - **The two standing questions of form**
>   - Recommended: (a) both follow the general rule.
>   - Answer: agreed, (a).
> - **The questions on `test` and `style` at setup**
>   - Recommended: (b) it asks only where the project holds code of its own.
>   - Answer: (b), after a plain explanation; the person first leaned to no question at all, and asks that the question say how the project's own tests and style check run together with GUPPI's, not which commands to set.

### Case 1031.1 — case-guppi settles a choice of form itself

> **given:**
> `rule-case-build`: the page whose Render lists the forks.
> **＋** `.claude/agents/case-guppi.md`: the Render, the frame of the agent.
> **＋** `estimate-case-build-settles-form-by-itself`: the new check.
> **＋** `/pre-spec`: the check whose findings may ask a change of a Case.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`, meets on an item a choice that the person's words do not give.

> **then:**
> A choice of form is how the work splits into Cases and sub-cases, whether a promise takes a new Estimate, a replaced Criterion or an Estimate that already checks the change, which page holds a thing, and where a fix goes that adds a second behaviour to a ratified Case.
> **＋** It settles a choice of form itself, with no question in a round.
> **＋** The `context` of the Case names the choice, and the person sees it at the showing of the Case.
> **＋** A choice of form whose options differ in behaviour, in cost or in what they block is a fork, and it asks that choice in a round.
> **＋** Asked by a message or by a finding of `/pre-spec` to change a Case, it builds the change under the number of that Case.
> **＋** A new Case it builds beside a ratified Case takes the number one above the highest number of the case files and of the decision lines of the session's ledger, or the free number that the guard of its case file names, and carries no `{supersedes:case N}` mark.
> **＋** The file of that ratified Case stays as it is, and a pair of the new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
> **－** A choice of the bound, of a second reasonable `recommend`, of the exceptions or of what is left not done stays a fork.
> **－** A Case that can give no Estimate still asks in a round what its Estimate will check.

```then
create:
- slug: estimate-case-build-settles-form-by-itself
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi settles a choice of form itself and names it in context, asks in a round only where its options differ in behaviour, in cost or in what they block, builds a change under the number of the Case it is asked on, and builds a new Case beside a ratified one under a new number with no supersedes mark, the ratified file left as it is
  method: 'by hand, at the Retro of the session that creates this Estimate, the new Render of rule-case-build in the Spec read against the Criterion; by hand, after a session whose case-guppi.md holds this text: each round of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, the transcript in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: You decide nothing the person has not decided.
    new: You decide nothing the person has not decided, but for a choice of form, as the paragraph on the forks sets it (as set in case 1031.1).
  - old: the alternative — a second reasonable `recommend`; the promise — a new Estimate, or a Criterion replaced; the split — one promise or sub-cases; the exceptions — the `－` lines of `then`; and what is left not done.
    new: 'the alternative — a second reasonable `recommend`; the exceptions — the `－` lines of `then`; and what is left not done. A choice of form is no fork, since it changes how the work is written down and not what it does: how the item splits into Cases and sub-cases, whether a promise takes a new Estimate, a replaced Criterion or an Estimate that already checks the change, which page holds a thing, and where a fix goes. Settle it yourself, ask no question on it, and name the choice in `context`, where the person sees it at the showing of the Case. A choice of form whose options differ in behaviour, in cost or in what they block is a fork, such as a new page with `core: true` that would keep the clean version from building, and you ask it in a round (as set in case 1031.1).'
  - old: 'no sub-cases, you do not place yourself: you write no new file and answer with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it (as set in case 870). Where the person chooses a new Case beside it, you build it in its own file'
    new: 'no sub-cases, you place as a choice of form: the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it, and a round comes only where the two differ in behaviour, in cost or in what they block (as set in case 1031.1). A new Case beside it you build in its own file'
  change: case-guppi settles a choice of form itself and asks only where its options differ in behaviour, in cost or in what they block
```

```tasks
- [x] create `estimate-case-build-settles-form-by-itself`
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-settles-form-by-itself`
```

### Case 1031.2 — case-guppi settles the page of code that no page covers

> **given:**
> `rule-case-build`: the page whose Render sets the offer of a page.
> **＋** `.claude/agents/case-guppi.md`: the Render, the frame of the agent.
> **＋** `estimate-case-build-offers-a-page-for-code-no-page-covers`: its Criterion is replaced whole.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`, builds a Case on an item whose words point to code, a file, a module or a function, that no live page names, by its file or by a folder that holds it, in `code_ref`, `implementation_ref` or `governs`.

> **then:**
> It reads that code in parts, the functions the Case changes and the places that call them, and searches the pages by meaning for the thing that code does.
> **＋** It settles a page only for the thing the Case changes, described from the code it read: where a page already describes that thing, the path added to the field of that page that lists its code; otherwise a new page, its category by the check of the schema of that category, with its slug, its one-line purpose, its parent and its paths.
> **＋** Its `context` gives the slug of the chosen page and why it was chosen.
> **＋** Where the two options differ in behaviour, in cost or in what they block, a round offers them before it writes the Case, and where the person turns down both, it asks in a round which page the Case changes.
> **＋** The page, created or given the path, is a task of the same Case, and the Estimate that checks the change stands on that page.
> **－** Code that the Case does not change gets no page.
> **－** Code that a page names, by its file or by a folder that holds it, gets no page.

```then
update:
- slug: estimate-case-build-offers-a-page-for-code-no-page-covers
  set:
    status: pending
    purpose: Whether case-guppi, on an item that points to code no page covers, reads that code and settles a page only for the thing the Case changes, or the path added to a page that describes it, asks in a round only where the two differ in behaviour, in cost or in what they block, and puts that page into the same Case
    method: by hand, at the Retro of the session that replaces this Criterion, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
  change: the Criterion replaced whole — the agent settles the page, and a round comes only where the options differ
- slug: rule-case-build
  replace:
  - old: 'then offer in a round a page only for the thing the Case changes, described from the code you read:'
    new: 'then settle a page only for the thing the Case changes, described from the code you read:'
  - old: 'The person decides: where the person turns both down, you ask in a round which page the Case changes.'
    new: That is a choice of form, and `context` names the page; where the two differ in behaviour, in cost or in what they block, you offer them in a round, and where the person turns both down, you ask in a round which page the Case changes (as set in case 1031.2).
  change: case-guppi settles the page of code that no page covers
```

```tasks
- [x] update `estimate-case-build-offers-a-page-for-code-no-page-covers`
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-offers-a-page-for-code-no-page-covers`
```

### Case 1031.3 — The setup Case asks on tests only where the project holds code of its own

> **given:**
> `rule-morph`: the page of the setup Case.
> **＋** `rule-skill-setup`: the page whose Render is the skill `/setup`.
> **＋** `.claude/skills/setup/SKILL.md`: the Render, which writes the prompt of the setup Case.
> **＋** `rule-guppi-config`: the page that says what a project does with the commands.
> **＋** `guppi.toml`: the file of the keys `test` and `style`.
> **＋** `guppi-set-aside/`: the folder of the files the install set aside.
> **＋** `estimate-morph-sets-up-the-project-at-the-first-hi`: its Criterion is replaced whole.

> **when:**
> `/setup` of `.claude/skills/setup/SKILL.md` dispatches `case-guppi` for the setup Case of `rule-morph`, in a project whose `guppi.toml` holds `setup_done = false`.

> **then:**
> The setup Case asks the person for the language of the repository, the language of the chat and the description of the project.
> **＋** It looks at the file paths of the project alone, reads no file, and looks for a file of a programming language outside the folders of GUPPI and `guppi-set-aside/`.
> **＋** Where it finds one, one plain question says that GUPPI's own tests and style check keep running in the project, says why it asks, and asks how the project's own tests and style check run beside them.
> **＋** The commands the person gives stand after GUPPI's commands in the keys `test` and `style` of `guppi.toml`.
> **－** Where it finds none, it asks nothing on tests or style, and the keys stay as they are.
> **－** The question names no key of `guppi.toml`.
> **－** GUPPI's commands leave no key, and no key becomes an empty list.
> **－** It asks no question on how the setup Case splits or how it is checked.

```then
update:
- slug: rule-morph
  replace:
  - old: '`guppi.toml` holds the languages and the commands of the keys `test` and `style` of the repository of GUPPI,'
    new: '`guppi.toml` holds the languages of the repository of GUPPI and, in its keys `test` and `style`, the commands of GUPPI, which the setup keeps,'
  - old: asks the person only for the rest, such as the language of the repository and of the chat, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
    new: 'asks the person only for the rest: the language of the repository and of the chat, and the description of the project. GUPPI''s commands stay in the keys `test` and `style` of `guppi.toml`. Where the file paths of the project show a file of a programming language of its own, the skill asks how the tests and the style check of the project run beside GUPPI''s, says why it asks, and adds the commands after GUPPI''s; where they show none, it asks nothing on them. It reads the paths alone (as set in case 1031.3).'
  change: the setup asks on tests and style only where the project holds code of its own
- slug: rule-skill-setup
  replace:
  - old: each a code of the table of `.guppi/guppi/config.py`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project;
    new: 'each a code of the table of `.guppi/guppi/config.py`, and the description of the project, and, by the file paths of the project alone, reading no file, looks for a file of a programming language outside `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`: where it finds none, it asks nothing on tests or style; where it finds one, it says in one plain question that GUPPI''s own tests and style check keep running in this project, that it asks so that Work Mode, the close of a session and the checks on GitHub run those of the project too, and asks how the project''s own tests and style check run beside them, naming no key of `guppi.toml` in the question (as set in case 1031.3);'
  - old: whose Render holds the languages, the commands and `setup_done = true`,
    new: whose Render holds the languages, the commands the person gave after GUPPI's commands, which leave neither key, and `setup_done = true`,
  - old: asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page.
    new: asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page; it asks no question on how it splits or how it is checked, and its `context` names the Estimates that already check the pages it updates (as set in case 1031.3).
  change: the prompt of the setup Case asks on tests and style only where the project holds code of its own
- slug: rule-guppi-config
  replace:
  - old: so its `guppi test` runs the tests of GUPPI until the setup Case of a project sets its own commands.
    new: so its `guppi test` runs the tests of GUPPI, and the setup Case of a project with code of its own adds the commands of that project after them (as set in case 1031.3).
  change: a project keeps the commands of GUPPI and adds its own after them
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  set:
    status: pending
    method: 'by hand, after the librarian''s run of the session that ratifies this Criterion: in an empty git project and in a git project that holds a file of a programming language of its own, the plugin guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of each of those sessions under ~/.claude/projects, its ledger and the files written in it read against the Criterion, recorded in the estimate line'
  sections:
    Criterion: |-
      When:
      In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` holds `setup_done = false`, the person reopens Claude Code and types `/hi`.

      Then:
      `/hi` opens the session and starts `/setup` of `rule-skill-setup`, which puts the setup Case of `rule-morph` first, before the opening Case of the first sprint and before the Frontier.
      **＋** The setup Case takes the name of the project's folder of saved transcripts from the path of the project.
      **＋** It asks the person only for the values it cannot find: the language of the repository, the language of the chat and the description of the project.
      **＋** Where the file paths of the project show a file of a programming language outside `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`, one plain question says that GUPPI's own tests and style check keep running in the project, says why it asks, and asks how the project's own tests and style check run beside them, and the commands the person gives stand after GUPPI's commands in the keys `test` and `style` of `guppi.toml`.
      **＋** Every value stands in that one setup Case, which the person ratifies or corrects, and the ledger hook of `rule-ledger-write` writes its decision lines though no sprint is open.
      **＋** The reply that acknowledges the setup Case shows no Frontier and ends with the open question on what the first sprint is to build, and on the person's answer `/sprint-open` starts in the same session with that answer.
      **＋** The librarian's run of that session writes the settings by the render of the rule pages that hold them, `guppi.toml`, the description of the project in `CLAUDE.md` and the read rules of the saved transcripts, and `guppi.toml` then holds `setup_done = true`.
      **－** `/guppi:install` is no Case, and the person ratifies nothing at it.
      **－** Between `/guppi:install` and that librarian's run, no settings file changes but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs.
      **－** The setup step asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page for it.
      **－** Where the file paths show no such file, it asks nothing on tests or style, and the keys `test` and `style` stay as they are.
      **－** The question names no key of `guppi.toml`, GUPPI's commands leave no key, and no key becomes an empty list.
      **－** It asks no question on how the setup Case splits or how it is checked.
      **－** A project whose `guppi.toml` does not hold `setup_done = false` gets no setup Case at `/hi`.
  change: the Criterion replaced whole — the setup asks on tests and style only where the project holds code of its own
```

```tasks
- [x] update `rule-morph`
- [x] update `rule-skill-setup`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/setup/SKILL.md`
- [x] update `rule-guppi-config`
- [x] update `estimate-morph-sets-up-the-project-at-the-first-hi`
- [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

## Case 1032 — Hook commands name the project folder, so a cd cannot break them

> **context:**
> Each hook of `.claude/settings.json`, and the one hook in the frontmatter of `.claude/agents/librarian-guppi.md`, runs the code as `uv run --project .guppi guppi <name>`, a path read from the folder the shell stands in. `lesson-hooks-relative-project-path-fails-after-a-cd` records the defect: a Bash call ran `cd vault/wiki/estimates && ...`, the shell stayed there, uv found no `.guppi` and exited 2, and every later hook refused each tool call and each reply until the person pressed Esc. The page https://code.claude.com/docs/en/hooks says that handlers "run in the current directory with Claude Code's environment", that both forms of a command export `CLAUDE_PROJECT_DIR`, "the project root where the session started", to the process, that on Windows a shell command runs in Git Bash, or in PowerShell where Git Bash is not installed, and that in a shell command each placeholder is wrapped in double quotes. The person chose that each hook command reads `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi <name>`, and that the Case covers the hook commands only. The code of GUPPI already finds the project by `project_root` of `.guppi/guppi/event.py`, which reads `CLAUDE_PROJECT_DIR` first, so only the start of the command changes. Not checked: how PowerShell reads `${CLAUDE_PROJECT_DIR}` on a Windows machine with no Git Bash.
>
> Four hooks find their own refusals in the transcript by the text of their command: `COMMAND` of `.guppi/guppi/ledger.py`, `.guppi/guppi/onward.py`, `.guppi/guppi/ratified.py` and `.guppi/guppi/casecheck.py`, each built from `PROJECT_RUN` of `ledger.py` and judged by `command_forms`, `refusals_in`, `sent_back_last` and `own_refusals`, which I read whole, with `told` and `spent` of `onward.py` and `own_told` and `last_refused` of `casecheck.py`. Case 1035 of this session found that under Claude Code 2.1.317 the bracket at the head of the `Stop` feedback reads `[command hook <number>]` and names no command, and it sets that the one reader of `.guppi/guppi/ledger.py` takes a refusal as a hook's own when the text after the bracket opens with the name of the hook, whatever the bracket holds, as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` checks; its lines `**Other Case:**` asked this Case to point to that Estimate. So the new start of the command changes no reading of a refusal, and no reader of refusals keeps old forms. `command_forms` stays only for the forms of the registration that `.guppi/guppi/ship.py` removes: the new command and the one with `--project .guppi`, since the code changes in Work Mode and `.claude/settings.json` changes at the render of the librarian's run. `CODE_WRITE_ENTRY` of `.guppi/guppi/ship.py`, read with `without_code_write` and `ship`, is the exact text of the registration of `guppi codewrite`, so it takes the same forms by `command_forms`, the one judgment of the forms of a hook's command; a Grep of `PROJECT_RUN|CODE_WRITE_ENTRY` over `.guppi/guppi/` printed `ledger.py`, `casecheck.py`, `onward.py`, `ratified.py` and `ship.py`, so no other code writes the form. `estimate-clean-branch-ships-no-code-write-hook` already checks that removal, and its Criterion stands, since it speaks of the exact entry, which each form is.
>
> Of the Estimates: `estimate-guppi-package-runs-from-its-own-folder` promises that each hook runs the code through `uv run --project .guppi`, so Case 1032.1 replaces its Criterion and sets its `purpose` and `method` anew; `estimate-hook-registry-rendered` promises only that the file equals the Render, and it stands. `estimate-ledger-write-lifts` and `estimate-case-check-judges-a-showing-after-a-refusal` state the text of the line of their own refusal, so Cases 1032.2 and 1032.3 replace them, one Estimate each, as the check of a Case asks. By the rule on form of case 1031.1, I settled the split into these sub-cases and the choice of replaced Criteria over a new Estimate. In each replaced Criterion, the lines that leave on purpose are the line of `Then` that named the form of a hook, the line that named the text of the refusal, the `When` lines that named a hook by its old command, in 1032.1 the line on a page that names a command with no `--project`, which now speaks of a `--project` that names `.guppi`, and the line on the modules that find their refusals, which now points to `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`, in 1032.2 and 1032.3 the line on the stretch, whose refusal now opens with `ledger:` or `casecheck:` after its bracket, as that Estimate sets it, and in 1032.3 the two `－` lines that named the runs `--prompt` and `--subagent` by the old command, which now name them `guppi casecheck --prompt` and `guppi casecheck --subagent`; each other line stands word for word. The lines of 1032.2 and 1032.3 on the stretch and on a transcript the hook cannot read share their words because the two Criteria held them before, and each speaks of its own hook, so they are no clash; the line of 1032.1 on the modules that find their refusals is the general promise of which those two lines are the case of one hook. A Grep of `` \[uv run|command_forms|either form|without `--project|CODE_WRITE_ENTRY|exact registration `` over the root with the glob `{vault/wiki,.claude}/**` printed `vault/wiki/brief.md` and `vault/wiki/log.md`, not read, `vault/wiki/rules/rule-clean-branch.md`, whose "exact registration" stands, `vault/wiki/rules/rule-guppi-package.md`, `vault/wiki/rules/rule-page-generation.md`, whose "either form" speaks of another thing, `vault/wiki/estimates/estimate-guppi-repository-keeps-the-development-project.md`, which speaks of the root files and the `Makefile` and stands, `vault/wiki/estimates/estimate-spec-reconcile-refuses-a-case-file-another-agent-holds.md`, of the form of an id, and the three Estimates replaced here. A Grep of `` command_forms|without `--project \.guppi`|with `--project \.guppi` and `` over the root with the glob `{vault/wiki,.claude,.guppi/guppi}/**` printed `.guppi/guppi/ledger.py`, `rule-guppi-package.md`, `estimate-guppi-package-runs-from-its-own-folder.md` and `estimate-guppi-repository-keeps-the-development-project.md`, so no other text lists the forms. A count Grep of a hook named by its command, the pattern `` (hook|run|runs|refusal|registers?|registered)[^.\n]{0,40}`uv run --project \.guppi guppi (ledger|onward|ratified|casecheck|event|gate|guard|bashguard|powershellguard|pageread|grepguard|shellwrite|codewrite|frontierguard|prespec|spec|context|sprint --hi|recall|libreport)\b `` over `vault/wiki/`, printed 70 occurrences in 60 files. A Grep of `` (registers?|registered)[^.\n]{0,60}`uv run --project \.guppi guppi `` over `vault/wiki/` printed the three files whose lines state the text of a registration: `estimate-case-check-refuses-text-before-a-round`, whose line on what `.claude/settings.json` registers on `UserPromptSubmit` Case 1032.4 replaces with the new command, and `estimate-retro-onward-sends-the-agent-to-the-handoff` and `estimate-prespec-onward-sends-the-agent-on`, whose lines on the order of the hooks on `Stop` name the old commands; Case 1035 of this session replaces those two Criteria and writes there the registration in the form that 1032.1 renders, `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi …`, as I read in its file whole after its build ended, so this Case does not touch them. The rest of that file agrees with this Case: it reads the own refusal by the name after the bracket as 1032.2 and 1032.3 now state it, its task on `.guppi/guppi/ledger.py` leaves `command_forms` to the forms that `.guppi/guppi/ship.py` removes, as 1032.1 sets, and it changes the refusal tests of `.guppi/tests/test_ledger.py` that 1032.1 leaves to it. Each other hit names a hook by the command that runs it from the root, which runs the same code, and states no text of the registration, so they stand, and so do the module docstrings of `.guppi/guppi/` that say a hook runs as `uv run --project .guppi guppi <name>`. In 1032.4 the lines that leave on purpose are the `When` line and the first three lines of `Then`, which named the runs by the old command and now name them `guppi casecheck` and `guppi casecheck --prompt`, and the line on the registration, which names the new command; each other line stands word for word. Case 1032.4 follows the rule on form of case 1031.1: one Estimate a sub-case. Its lines that share words with lines of 1032.2 and 1032.3 speak of another run, the note on a round at `UserPromptSubmit`, while those speak of the ledger hook and of the count of refusals of the `Stop` run, so they are no clash. `rule-case-check` lists `estimate-case-check-refuses-text-before-a-round` in its `estimates` and states no form of a hook command, so it stands.
>
> `test_each_hook_command_stands_in_the_settings_in_the_new_form` of `.guppi/tests/test_guppi_package.py` reads the live `.claude/settings.json`, and it changes so that it passes on the text before the render and after it (case 868); a Grep of `settings\.json|librarian-guppi\.md` over `.guppi/tests/` printed `test_guard.py`, `test_guppi_package.py`, `test_ratified.py`, `test_render.py` and `test_ship.py`, and only `test_guppi_package.py` reads a live file there. Its other tests look for `uv run guppi` and for paths outside `.guppi/`, which the new text does not hold. `test_each_hook_finds_its_refusals_under_the_command_with_and_without_the_project` and `test_a_plan_refusal_of_onward_is_its_own_in_either_form_and_not_that_of_onward` of `.guppi/tests/test_ledger.py` find a refusal under each form of today, and Case 1035.1 changes them, as it changes each refusal in the tests of `test_onward.py`, `test_casecheck.py` and `test_ratified.py`; this Case tests the forms of `command_forms` alone. Case 1031 changes `.claude/agents/case-guppi.md` and no hook of it, and Case 1030 runs the commands of the keys of `guppi.toml` over the copy and no hook command; neither clashes. The ledger of this session holds no `error` lesson by a Grep of `lesson\[error\]`, and the lesson above stands in the ledger of session 0358, so no mark is added. The check of this file listed the files that name the pages and files this Case changes, and I judged each by its purpose line or path. `estimate-settings` was read: it promises that the rendered file parses as JSON and that the next session start writes its line from its hooks, which the new commands, quoted with `\"` in JSON, keep, so it stands. `estimate-plugin-install-runs-no-hook-before-uv-sync`, `lesson-plugin-install-hooks-of-the-copy-run-at-once` and `estimate-guppi-package-is-ready-after-the-install` speak of when the hooks of the copy first run in an installed project, where `.guppi/` stands under the folder Claude Code is opened in, so they stand. `rule-harness`, `rule-settings`, `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` name `rule-guppi-package` or `rule-hook-registry` as pages and state no form of a hook command. The other listed files speak of other steps of the check, the ship, the ledger, the librarian or the settings, and they stand. Not done: the commands that the skills, the agents and the pages tell an agent to run keep the short form; a Windows machine where PowerShell runs the hooks is not checked; the old form leaves `command_forms` in a Case of a later session.

> **problem:**
> A `cd` in a Bash call moves the folder that every later hook runs in, the relative `--project .guppi` then names no folder, and each hook refuses each tool call and each reply until the person stops the session.

> **recommend:**
> - **How each hook command names the folder of the code**
>   - Recommended: (a) a shell command with the project path in quotes, `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi <name>`.
>   - Answer: agreed, (a).
> - **Which commands the Case covers**
>   - Recommended: (a) the hook commands only.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: Case 1035 of this session asked by its lines `**Other Case:**` that a hook's own refusal be found as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it, by its name after the bracket, and not under the forms of its command.
>   - Taken: in 1032.1 the line on the modules that find their refusals points to that Estimate, `command_forms` keeps only the forms that `.guppi/guppi/ship.py` removes, and the test of `.guppi/tests/test_ledger.py` tests those forms alone; in 1032.2 and 1032.3 the refusal is a line whose text after its bracket opens with `ledger:` or `casecheck:`.
> - **Change**
>   - Asked: the findings of `/pre-spec`: the sentence of `rule-guppi-package` on what its test fails on still says "without `--project .guppi`"; the names and the `change` lines of 1032.2 and 1032.3 still spoke of the forms of the command; and the claim on the count Grep missed the Estimates that state the text of a registration.
>   - Taken: 1032.1 gives `rule-guppi-package` a second pair on that sentence; 1032.2 and 1032.3 take new names and `change` lines on the name after the bracket; `context` names the three Estimates that state a registration, Case 1032.4 replaces `estimate-case-check-refuses-text-before-a-round`, and Case 1035 carries the two Estimates of `guppi onward`.

### Case 1032.1 — Each hook runs the code from the project folder

> **given:**
> `rule-guppi-package`: the page that says how each caller runs the code.
> **＋** `rule-hook-registry`: the page whose Render is the `"hooks"` key of `.claude/settings.json`.
> **＋** `.claude/settings.json`: the rendered hooks.
> **＋** `rule-documentation`: the page whose Render is the agent file of the librarian.
> **＋** `.claude/agents/librarian-guppi.md`: the agent whose frontmatter holds a hook.
> **＋** `.guppi/guppi/ledger.py`: the forms of a hook's command, the forms of the registration that `.guppi/guppi/ship.py` removes.
> **＋** `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`: the check of how a `Stop` hook finds its own refusals, set by Case 1035.1.
> **＋** `.guppi/guppi/ship.py`: the removal of the registration of `guppi codewrite` from the copy.
> **＋** `.guppi/tests/test_guppi_package.py`: the test of the live hook commands.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the forms.
> **＋** `.guppi/tests/test_ship.py`: the tests of the removal.
> **＋** `.guppi/`: the folder of the code, its settings and its tests.
> **＋** `.github/workflows/`: the workflows that run the code.
> **＋** `.guppi/pyproject.toml`: the settings of the package, which declare the tools of the tests.
> **＋** `.venv/`: the Python environment that `.guppi/.gitignore` keeps out of git.
> **＋** `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi"`: the start of each hook command.
> **＋** `rule-case-example`: a page whose example keeps a path of tests of a project.
> **＋** `rule-estimates-schema`: a page whose example keeps a path of tests of a project.
> **＋** `rule-rules-schema`: a page whose example keeps a path of tests of a project.
> **＋** `estimate-guppi-package-runs-from-its-own-folder`: its Criterion is replaced whole.

> **when:**
> In the project, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.
> **＋** A Bash call of that session runs a `cd` into a folder of the project, and the shell stays there.

> **then:**
> The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
> **＋** Each hook of `.claude/settings.json`, and the hook in the frontmatter of `.claude/agents/librarian-guppi.md`, runs the code through `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi"`, so it finds `.guppi/` wherever the shell stands.
> **＋** After the `cd`, the hooks of the next tool call and of the next reply run, and none prints an error or refuses for want of `.guppi/`.
> **＋** Each command of a skill, an agent or a workflow of `.github/workflows/` that runs the code of GUPPI or its tests runs it through `uv run --project .guppi`.
> **＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` with no `--project` that names `.guppi`, outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
> **＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
> **＋** Each `Stop` hook that finds its own refusals in the transcript finds them as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it, whatever the start of its command.
> **＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
> **－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.

```then
update:
- slug: rule-guppi-package
  replace:
  - old: Each caller runs the code as `uv run --project .guppi guppi …` — the hooks of `.claude/settings.json`, the skills and the agents — and the tests as `uv run --project .guppi pytest`.
    new: Each skill and each agent runs the code as `uv run --project .guppi guppi …`, and the tests as `uv run --project .guppi pytest`. Each hook of `.claude/settings.json`, and a hook in the frontmatter of an agent, runs it as `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi …`, the folder that Claude Code was opened in, since a hook runs in the folder the shell stands in, which a `cd` in a Bash call moves for every later hook (as set in case 1032.1).
  - old: fails on a command that runs the code or the tests through `uv run` without `--project .guppi`, in a file of
    new: fails on a command that runs the code or the tests through `uv run` with no `--project` that names `.guppi`, in a file of
  change: each hook runs the code from the folder that Claude Code was opened in, so a cd cannot break it
- slug: rule-hook-registry
  sections:
    Render: |-
      <!-- rule-hook-registry -->
          "SessionStart": [
            { "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi event session-start", "timeout": 30 },
                         { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi render --sync", "timeout": 60 } ] },
            { "matcher": "compact",
              "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi recall", "timeout": 30 } ] }
      ],
      "UserPromptSubmit": [
        { "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi event prompt", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi context --prompt", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi casecheck --prompt", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi sprint --hi", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi spec --typed", "timeout": 30 },
                     { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi gate", "timeout": 30 } ] }
      ],
      "PreToolUse": [

            { "matcher": "ExitPlanMode",
              "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi prespec", "timeout": 30 } ] },
            { "matcher": "Skill",
              "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi gate", "timeout": 30 } ] },
            { "matcher": "Edit|Write|MultiEdit",
        "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi guard", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi ratified --guard", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi frontierguard", "timeout": 30 } ] },
      { "matcher": "Bash",
        "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi bashguard", "timeout": 30 } ] },
      { "matcher": "PowerShell",
        "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi powershellguard", "timeout": 30 } ] },
      { "matcher": "Read",
        "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi pageread", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi grepguard", "timeout": 30 } ] },
      { "matcher": "Grep",
        "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi grepguard", "timeout": 30 } ] }

          ],
          "PostToolUse": [
            { "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi event tool", "timeout": 30 } ] },
            { "matcher": "ExitPlanMode",
              "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi spec", "timeout": 30 } ] }, { "matcher": "Read", "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi pageread --after", "timeout": 30 } ] }, { "matcher": "Bash|PowerShell", "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi shellwrite", "timeout": 30 } ] }, { "matcher": "Edit|Write|MultiEdit", "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi codewrite", "timeout": 30 } ] }
          ],
          "Stop": [
            { "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi ledger", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi ratified", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi casecheck", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi context", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi onward", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi onward --plan", "timeout": 30 } ] }
          ],
          "SubagentStop": [
            { "hooks": [ { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi casecheck --subagent", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi libreport", "timeout": 30 } ] }
          ]
      <!-- /rule-hook-registry -->
  change: each hook command names .guppi under the folder that Claude Code was opened in
- slug: rule-documentation
  replace:
  - old: 'command: uv run --project .guppi guppi event tool'
    new: 'command: uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi event tool'
  change: the hook of the librarian names .guppi under the folder that Claude Code was opened in
- slug: estimate-guppi-package-runs-from-its-own-folder
  set:
    status: pending
    purpose: Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook runs them through .guppi under the folder that Claude Code was opened in, so that a cd in a Bash call cannot break it, every skill, agent, workflow and page runs them through uv run --project .guppi, and the modules and the guards take those forms
    method: 'by hand, after the render of the harness by the librarian''s run of the session that ratifies this Criterion: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py, then a session opened in the project, /hi typed there, a Bash call that runs cd vault/wiki, and a later tool call and reply; the output of its hooks in the transcript of that session under ~/.claude/projects/ read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — each hook runs the code from the folder that Claude Code was opened in
```

```tasks
- [x] update `rule-guppi-package`
- [x] update `rule-hook-registry`
- [x] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [x] update `rule-documentation`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
- [x] `.guppi/guppi/ledger.py`: `PROJECT_RUN` becomes `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" `, a new constant holds the form of today, `uv run --project .guppi `, and `command_forms` gives for a command of `PROJECT_RUN` the command and the same with `--project .guppi`, the forms of the registration that `.guppi/guppi/ship.py` removes, until a Case of a later session removes the old form; no reader of refusals calls it, as Case 1035.1 sets; the module docstring and the docstring of `command_forms` say so.
- [x] `.guppi/guppi/ship.py`: `CODE_WRITE_ENTRY` becomes the entries of the registration of `guppi codewrite` in each form of `command_forms` of `.guppi/guppi/ledger.py`, each command written as JSON writes it, and `without_code_write` removes each; the module docstring says so.
- [x] `.guppi/tests/test_guppi_package.py`: `test_each_hook_command_stands_in_the_settings_in_the_new_form` reads the commands of `.claude/settings.json` as JSON and passes where the `COMMAND` of each hook stands there in its new form or in the form with `--project .guppi`, so it passes before the render and after it until a Case of a later session drops the old form; a new test asserts the same of every hook command of `.claude/settings.json` and of the frontmatter of `.claude/agents/librarian-guppi.md`; the module docstring says so.
- [x] `.guppi/tests/test_ledger.py`: a test asserts that `command_forms` gives for the `COMMAND` of each hook the command and the same with `--project .guppi`, and `test_a_command_without_the_project_has_one_form` gives one form for a command of no `PROJECT_RUN`; the tests of a refusal found under each form are those Case 1035.1 changes.
- [x] `.guppi/tests/test_ship.py`: a test whose name holds `no_code_write_hook` builds a tree whose registration of `guppi codewrite` stands in the new form and finds it removed from both texts.
- [x] update `estimate-guppi-package-runs-from-its-own-folder`
- [ ] read `estimate-guppi-package-runs-from-its-own-folder`
```

### Case 1032.2 — The ledger hook finds its refusals by its name, whatever its command

> **given:**
> `estimate-ledger-write-lifts`: its Criterion is replaced whole.
> **＋** `rule-ledger-write`: the rule of the ledger hook.
> **＋** `.guppi/guppi/ledger.py`: the ledger hook and its reading of refusals.
> **＋** `.guppi/guppi/onward.py`: the hook that calls that reading with its own command.
> **＋** `.guppi/guppi/gate.py`: the gate of a `Skill` call.
> **＋** `.claude/settings.json`: the registration of the hook.
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`: the check of how a `Stop` hook finds its own refusals, set by Case 1035.1.

> **when:**
> The `Stop` hook `guppi ledger` of `.guppi/guppi/ledger.py`, as `.claude/settings.json` registers it, fires at the end of a reply of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` of `.guppi/guppi/gate.py` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** With `stop_hook_active` set, the hook writes and judges the lines as without it.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **＋** For each refused line of the reply just finished, the hook prints its stderr line only when that stderr line does not already stand in its own refusals of the stretch, and exits 2 when it prints one; a repeat of a line already told stays silent.
> **＋** No `hi`, and an error of its own after it read the payload, exit 2 only when no refusal of its own stands in the stretch; otherwise the hook exits 0 and prints nothing.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. Its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line whose text after its bracket opens with `ledger:`, as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it; one function of `.guppi/guppi/ledger.py` judges both, and `.guppi/guppi/onward.py` calls it with its own command.
> **－** A line that a refusal of `rule-ledger-write` refuses does not land while that refusal holds.
> **－** Without a `hi`, the ledger is untouched.
> **－** With `stop_hook_active` set and a transcript it cannot read, it writes the lines of `last_assistant_message` and exits 0.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

```then
update:
- slug: estimate-ledger-write-lifts
  set:
    status: pending
  change: the Criterion replaced whole — its own refusal is a line whose text after its bracket opens with ledger:, and the hook is named apart from the start of its command
```

```tasks
- [x] update `estimate-ledger-write-lifts`
- [x] read `estimate-ledger-write-lifts`
```

### Case 1032.3 — The Case check finds its refusals by its name, whatever its command

> **given:**
> `estimate-case-check-judges-a-showing-after-a-refusal`: its Criterion is replaced whole.
> **＋** `rule-case-check`: the rule of the Case check.
> **＋** `.guppi/guppi/casecheck.py`: the Case check and its count of refusals.
> **＋** `.guppi/guppi/ledger.py`: the reading of refusals it calls.
> **＋** `.claude/settings.json`: the registration of the hook.
> **＋** `<plan>.checked.json`: the store of the checked Cases.
> **＋** `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`: the check of how a `Stop` hook finds its own refusals, set by Case 1035.1.

> **when:**
> The `Stop` hook `guppi casecheck` of `.guppi/guppi/casecheck.py`, as `.claude/settings.json` registers it, fires at the end of a reply of the main agent in a session with a `hi`, and finds a reason to refuse it: a shown Case that differs from `<plan>.checked.json`, a shown Case whose file was not sent or differs from the store, or an error of its own after it read the payload.

> **then:**
> The hook judges the reply the same whether `stop_hook_active` is set or not.
> **＋** It gives a reason that names a Case, opening with `case <id>:`, while fewer than three of its own refusals in the stretch hold a reason of that Case, and any other reason while fewer than three of them hold the same reason.
> **＋** It exits 2 while a reason is left to give, with those reasons on stderr.
> **＋** When no reason is left to give, it exits 0 and prints on stderr one line per Case it let through: "casecheck: case <id> shown unchecked after three refusals; the Spec hook compares it at ratification".
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`; its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line whose text after its bracket opens with `casecheck:`, as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it, judged by `refusals` of `.guppi/guppi/ledger.py`, the function that `guppi onward` calls.
> **－** A text of the main agent's own before a round of `case-guppi` or outside the list of a showing is no reason of the `Stop` run. The run `guppi casecheck --prompt` refuses nothing, so it counts nothing.
> **－** With `stop_hook_active` set and a transcript it cannot read, it exits 0 and prints nothing.
> **－** The run `guppi casecheck --subagent` keeps its own guard, the store.

```then
update:
- slug: estimate-case-check-judges-a-showing-after-a-refusal
  set:
    status: pending
  change: the Criterion replaced whole — its own refusal is a line whose text after its bracket opens with casecheck:, and the hook is named apart from the start of its command
```

```tasks
- [x] update `estimate-case-check-judges-a-showing-after-a-refusal`
- [x] read `estimate-case-check-judges-a-showing-after-a-refusal`
```

### Case 1032.4 — The note on a round names the run of the Case check, not its old command

> **given:**
> `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole.
> **＋** `rule-case-check`: the rule of the Case check.
> **＋** `rule-hook-registry`: the page that renders the registration.
> **＋** `.guppi/guppi/casecheck.py`: the Case check, its run on `UserPromptSubmit` and `is_round`.
> **＋** `.guppi/guppi/ledger.py`: the reading of refusals it calls.
> **＋** `.claude/settings.json`: the registration of the hook.
> **＋** `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi casecheck --prompt`: the command of the run as registered.
> **＋** `case-guppi`: the agent whose rounds the main agent shows.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of how the refusals of the `Stop` run are counted.

> **when:**
> A reply of the main agent shows a round of `case-guppi`, `Stop` fires and `guppi casecheck` of `.guppi/guppi/casecheck.py` runs on it. Then the person sends a message, and `guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

> **then:**
> At `Stop`, `guppi casecheck` refuses no reply for the way it opens a round of `case-guppi`, or for a text of the main agent's own before the round. Its other reasons stand.
> **＋** On `UserPromptSubmit`, `guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends. The turn holds a round when a text that `case-guppi` gave back in it is a round by `is_round` of `.guppi/guppi/casecheck.py`.
> **＋** It finds a fault when the first line of the reply that is neither blank nor the horizontal rule `---` opens neither with `❓ ` nor with a bold label that ends in a colon. While the session's event log holds no `prespec` line of this session after its `hi`, it also finds a fault when the main agent wrote text in the turn after the first round came back and before its last tool call. It judges only the texts after the reply that the last refusal of `guppi casecheck` in the turn follows, judged by `refusals` of `.guppi/guppi/ledger.py`.
> **＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the text before the round, says that the round stands as shown and is not shown again, and tells the agent to open the next round with its Context paragraph or its first question, with nothing before it but a horizontal rule.
> **＋** `.claude/settings.json` registers `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi casecheck --prompt` on `UserPromptSubmit`, as `rule-hook-registry` renders it.
> **－** A reply that opens with the horizontal rule `---` before its round gets no note for it, and neither does a reply with no rule before its round.
> **－** With no fault, in a turn with no round, and for text after the last question, it prints nothing.
> **－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
> **－** The person sees nothing of the note. It stores nothing and writes no file.
> **－** The refusals of the `Stop` run are counted as `estimate-case-check-judges-a-showing-after-a-refusal` sets it, and a layout fault of a round is not one of them.

```then
update:
- slug: estimate-case-check-refuses-text-before-a-round
  set:
    status: pending
  change: the Criterion replaced whole — the registration of guppi casecheck --prompt names .guppi under the folder that Claude Code was opened in
```

```tasks
- [x] update `estimate-case-check-refuses-text-before-a-round`
- [x] read `estimate-case-check-refuses-text-before-a-round`
```

## Case 1033 — The code folder of GUPPI keeps the Python caches out of git

> **context:**
> When the tests of GUPPI run, Python writes its byte code caches into `__pycache__/` folders beside the code, under `.guppi/guppi/` and `.guppi/tests/`. The clean version that `guppi ship` builds holds two ignore files: `.guppi/.gitignore`, whose one line is `.venv/`, and `vault/.gitignore`, which covers the daily event logs. Neither covers `__pycache__/`. In this repository the root `.gitignore` holds `__pycache__/`, so the defect never shows here; the clean version takes no root `.gitignore`, since `ROOT_FILES` of `.guppi/guppi/ship.py` is `CLAUDE.md` and `.gitattributes`. `lesson-plugin-install-leaves-pycache-untracked` records the result in a trial project: the gate refused `/handoff` four times on `.guppi/guppi/__pycache__/` and `.guppi/tests/__pycache__/` until the agent added `__pycache__/` to `.git/info/exclude`. I read `dirty` of `.guppi/guppi/gate.py` and the branch of `run` that calls it: for `/handoff` it runs `git status --porcelain` in the project and refuses with `commit first` when the output is not empty, so each untracked cache folder blocks the handoff. The caches of pytest and ruff do not have this defect: `.guppi/.pytest_cache/.gitignore` and `.guppi/.ruff_cache/.gitignore` stand in this repository, each with the line `*`, written by those tools, so git ignores those folders.
>
> By the rule on form of case 1031.1, I settled these choices with no question. The line goes into `.guppi/.gitignore`, which `tree_files` of `.guppi/guppi/ship.py` copies into the clean version as it stands, and which `/guppi:install` copies into the project. A root `.gitignore` in the clean version is no reasonable option: step 3 of `rule-plugin-install` stops the install when a path of the plugin already stands in the project and is not `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`, so it would stop the install in each project that has its own `.gitignore`, and it would also change how the project ignores its own files. `.git/info/exclude` is no option either, since the install copies nothing under `.git/` and runs no `git` command. No page names `.guppi/.gitignore` in a field of its code: a Grep of `^(code_ref|implementation_ref|governs):.*\.guppi/?(\.gitignore)?["\],]` over `vault/wiki/` printed nothing. `rule-guppi-package` already describes the file in its `## Purpose`, so the Case changes that sentence and adds the path to its `implementation_ref`. One promise, so one Case with no sub-cases. The check is a new Estimate on that page, since `estimate-guppi-package-runs-from-its-own-folder`, whose Criterion says that `.guppi/` holds a `.gitignore` that holds `.venv/`, has its Criterion replaced by Case 1032.1 of this session, and `same_target_findings` of `.guppi/guppi/prespec.py` refuses a second replacement of one Criterion in a session. Its line on `.venv/` stays true, since the file keeps that line. `estimate-guppi-package-is-ready-after-the-install` speaks of `uv` and of the copy of `.claude/settings.json`, and it stands. Case 1032.1 also updates `rule-guppi-package`, by a pair on the next sentence, the one that opens with "Each caller runs the code"; my pair and my `set` of `implementation_ref` touch neither its text nor a field it sets, so the two do not clash.
>
> The rule that governs this is `rule-clean-branch`: it says the clean version holds the package `guppi` with its `pyproject.toml`, `uv.lock` and `.gitignore`, and it stays true. `estimate-clean-branch-writes-a-clean-copy` says the copy writes no cache folder, which `SKIPPED_NAMES` of `.guppi/guppi/ship.py` keeps; it speaks of what the copy writes, not of what git ignores after the tests run, so it stands. A Grep of `gitignore` over the root with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed `.claude/agents/case-guppi.md`, `.guppi/tests/test_ship.py`, `.guppi/tests/test_shellwrite.py`, `.guppi/tests/test_guppi_package.py`, `vault/wiki/rules/rule-guppi-package.md`, `vault/wiki/rules/rule-event-log.md`, `vault/wiki/rules/rule-clean-branch.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/log.md`, `.guppi/guppi/sprint_close.py`, `.guppi/guppi/ship.py`, `.guppi/guppi/event.py`, `.guppi/guppi/archive.py`, `vault/wiki/lessons/lesson-plugin-install-leaves-pycache-untracked.md`, `vault/wiki/glossary.md`, `vault/wiki/estimates/estimate-ask-searches-at-prespec.md`, `vault/wiki/estimates/estimate-clean-branch-ships-neutral-texts.md`, `vault/wiki/estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder.md`, `vault/wiki/entities/entity-glossary.md`, `vault/wiki/brief.md`, `vault/wiki/estimates/estimate-event-log-records.md`, `vault/wiki/estimates/estimate-sprint-plugin-frontierguard-build-read-its-folders-readers.md`, `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`, `vault/wiki/estimates/estimate-sprint-close-moves-old-event-logs.md` and `vault/wiki/estimates/estimate-guppi-package-runs-from-its-own-folder.md`. Of these, the texts that say what `.guppi/.gitignore` holds are `rule-guppi-package`, which the Case changes, the docstring and line 60 of `.guppi/tests/test_guppi_package.py`, which assert the line `.venv/` and stay true, though the task updates the docstring, the Estimate named above, `rule-clean-branch` and the docstring of `.guppi/guppi/ship.py`, which say only that the file is written; `test_ship.py` writes a sample `.guppi/.gitignore` in a temporary folder; the others speak of `vault/.gitignore`, of the event logs, or of reading ignore files during a build, and they stand. The lesson stays as a record. A Grep of `__pycache__|pycache` over the root with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests,.github}/**` printed `.guppi/tests/test_ship.py`, `vault/wiki/log.md`, `.guppi/guppi/ship.py`, `vault/wiki/brief.md`, `vault/wiki/lessons/lesson-plugin-install-leaves-pycache-untracked.md`, `.guppi/tests/test_check.py` and `vault/wiki/estimates/estimate-plugin-install-writes-guppi-into-an-empty-project.md`; the code hits skip or leave out cache folders when they copy a tree, and the Estimate holds the word in a past reading of its `## Result`, so they stand. The only test that reads the live `.guppi/.gitignore` is `test_the_package_its_settings_its_lock_and_its_tests_stand_under_guppi`, which checks the line `.venv/`; the new text keeps it, and the new test reads the file as Work Mode changes it, at the same time. The new test calls `dirty` of `.guppi/guppi/gate.py`, so it judges the tree by the same function as the gate and adds no second copy of that judgment. The ledger of this session holds no line by a Grep of `lesson\[error\]` or of `\{addresses:`, and the lesson stands in the ledger of session 0358, so no mark is added. The check of this file listed the files that name `rule-guppi-package`, `pyproject.toml`, `test_guppi_package.py` or `.gitignore`, and I judged each by its purpose line or path. `rule-harness` is the parent of `rule-guppi-package`, and `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` name it for the path of tests in their examples; none states what `.guppi/.gitignore` holds, so they stand. The files that name `pyproject.toml` speak of pointers, of the commands of `guppi.toml`, of the development project at the root or of a tool's behaviour, and the Case does not change `.guppi/pyproject.toml`, only the field that lists it with the new path. The two Estimates that name `test_guppi_package.py` speak of how `case-guppi` and `ask-guppi` read tests, and the files that name `.gitignore` are those of the Grep above, judged there. Not done: a `__pycache__/` folder of the project's own code outside `.guppi/` is left to the project's own ignore file.

> **problem:**
> A project that installs GUPPI gets no ignore line for the Python caches under `.guppi/`, so after the first run of the tests git lists them as untracked, and the gate refuses `/handoff` until someone ignores them by hand.

> **recommend:**
> - Recommended: add `__pycache__/` to `.guppi/.gitignore`, which the clean version and the install copy as it stands, describe it in `rule-guppi-package` and check it with a new Estimate on that page.
> - Answer: ratified as built

> **given:**
> `rule-guppi-package`: the page that describes `.guppi/.gitignore`.
> **＋** `estimate-guppi-package-keeps-python-caches-out-of-git`: the new check.
> **＋** `.guppi/.gitignore`: the ignore file of the code folder.
> **＋** `.guppi/`: the folder of the code of GUPPI and its tests.
> **＋** `__pycache__/`: the folders of byte code caches that Python writes.
> **＋** `.venv/`: the Python environment, whose line the ignore file keeps.
> **＋** `.guppi/guppi/gate.py`: the gate, whose `dirty` reads the state of the tree.
> **＋** `/handoff`: the skill that the gate refuses while the tree is not clean.
> **＋** `.guppi/tests/test_guppi_package.py`: the new test.
> **＋** `rule-clean-branch`: the build of the clean version, which writes the ignore file as it stands.

> **when:**
> In a git project that holds the code of GUPPI under `.guppi/`, the tests run, and Python writes `__pycache__/` folders beside the code and the tests.
> **＋** Then `/handoff` is called, and `dirty` of `.guppi/guppi/gate.py` reads `git status --porcelain`.

> **then:**
> `.guppi/.gitignore` holds the line `__pycache__/` beside the line `.venv/`.
> **＋** git lists no file of a `__pycache__/` folder under `.guppi/` as untracked, and `dirty` shows none.
> **＋** The gate does not refuse `/handoff` for those caches.
> **＋** The clean version that `rule-clean-branch` builds holds `.guppi/.gitignore` with that line.
> **－** No ignore file outside `.guppi/` changes, the root ignore file of a project included.

```then
create:
- slug: estimate-guppi-package-keeps-python-caches-out-of-git
  ref: rule-guppi-package
  kind: QA
  purpose: Whether .guppi/.gitignore keeps the __pycache__/ folders that Python writes under .guppi/ out of git, so that the gate of /handoff finds no untracked cache in a project that installs GUPPI
  method: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py -k caches
  tags:
  - git
  - plugin
update:
- slug: rule-guppi-package
  replace:
  - old: and a `.guppi/.gitignore` that keeps its Python environment `.guppi/.venv/` out of git.
    new: and a `.guppi/.gitignore` that keeps its Python environment `.guppi/.venv/` out of git, and the `__pycache__/` folders that Python writes beside the code and the tests too, so that a project that installs GUPPI finds no untracked cache under `.guppi/` after its tests run; the root ignore file of the project stays its own (as set in case 1033).
  set:
    implementation_ref:
    - .guppi/pyproject.toml
    - .guppi/.gitignore
    - .guppi/tests/test_guppi_package.py
  change: .guppi/.gitignore keeps the Python caches out of git
```

```tasks
- [x] create `estimate-guppi-package-keeps-python-caches-out-of-git`
- [x] update `rule-guppi-package`
- [x] `.guppi/.gitignore`: a line `__pycache__/` after the line `.venv/`.
- [x] `.guppi/tests/test_guppi_package.py`: a test whose name holds `caches` runs `git init` in a temporary folder, copies the live `.guppi/.gitignore` to `.guppi/.gitignore` there, writes a file under `.guppi/guppi/__pycache__/` and one under `.guppi/tests/__pycache__/`, stages `.guppi/.gitignore` alone, and asserts that `dirty` of `.guppi/guppi/gate.py` lists that file and no other path; the module docstring says that the file holds `__pycache__/` too.
- [x] read `estimate-guppi-package-keeps-python-caches-out-of-git`
```

## Case 1034 — The opening Case of a sprint on main makes the sprint branch, and Work Mode runs that task first

> **context:**
> The opening Case of a sprint moves the work to a branch named by the sprint. When the session starts on the branch of the closed sprint, its first tasks merge that branch and run `git switch -c <id>`. When the session starts on `main`, as the first sprint of every project does, `rule-skill-sprint-open` writes no branch task, and Work Mode, which refuses to start on `main` by `rule-work-mode` and the fifth condition of `rule-where-to-stop`, stops until the person makes the branch by hand. In every trial of session 0358 the run stopped there, and the brief's `## Flags` records it. A task alone would not run, since Work Mode would refuse `main` before it, so the person chose that Work Mode runs that one task first and goes on. The rule that governs the stop is `rule-where-to-stop`: the run stops only on its conditions, and its third condition is an action that git cannot undo; a local branch is one git can undo, so the line opens with no `stop:`. The rule holds for every opening Case built on `main`, since the branch decides it and not the count of sprints. In the first sprint the setup Case of `rule-morph` stands in the Spec before the opening Case, so Work Mode looks for the opening Case in the whole Spec and not at its first line; by the `## Purpose` of `rule-morph`, the setup Case may hold tasks that Work Mode runs, a task that writes a kept part of a set-aside file into a file that no page writes and a task that deletes `guppi-set-aside/` (case 932.2), and those tasks run after the branch line, on the branch `<id>`, so they reach `main` with the sprint branch. Work Mode writes `work.md` after the switch, so the baseline stands on the branch `<id>`, at the same commit. A refusal of `git switch -c <id>`, such as a branch of that name that already stands, becomes a stop on the sixth condition of `rule-where-to-stop`.
>
> By the rule of Case 1031.1 these choices of form were settled with no question: the Case splits into three sub-cases, one per Estimate whose Criterion speaks of the change, and each replaces that Criterion whole rather than creating a new Estimate, since a new one would leave the old line false. `estimate-skill-sprint-open-merges-the-closed-sprint-branch` says that the opening Case holds no task on `main`, and its `purpose` ends with no git task on main, so Case 1034.1 sets both anew; its `method`, a reading of the Render, stands. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` says that the skill stops on `main`, so Case 1034.2 replaces its Criterion and sets its `purpose` and `method` anew. That Estimate carries `deferred_by` Case 1008, whose Problem is that no Case set when or in which client the first load of `/work` on a red check is read; the new `method` names that moment, the first `/work` after the librarian's render of the new Render, so Case 1034.2 retires the defer by `{supersedes:case 1008}`. `estimate-where-to-stop-stops-only-on-its-conditions` says that the agent stops on `main` and names the merge tasks of the opening Case, so Case 1034.3 replaces its Criterion; its `purpose` and `method` stand, since they speak of the conditions in general. The other Estimates of the three pages were read by `purpose`: `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-open-starts-at-hi`, `estimate-skill-sprint-open-refuses-a-taken-sprint-id`, `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`, `estimate-work-mode-takes-the-work-readings` and `estimate-where-to-stop-writes-each-step-whole` speak of other things, and they stand.
>
> A Grep of ``Work Mode does not start|does not start on|stop on `main`|stops on `main`|on main`` over the root with the glob `{vault/wiki,.claude}/**`, files only, printed `vault/wiki/backlog.md`, `.claude/skills/work/SKILL.md`, `vault/wiki/where-to-stop.md`, `.claude/skills/sprint-open/SKILL.md`, `vault/wiki/rules/rule-skill-sprint-open.md`, `vault/wiki/estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline.md`, `vault/wiki/rules/rule-work-mode.md`, `vault/wiki/rules/rule-where-to-stop.md`, `vault/wiki/estimates/estimate-skill-sprint-open-merges-the-closed-sprint-branch.md`, `vault/wiki/estimates/estimate-where-to-stop-stops-only-on-its-conditions.md` and `vault/wiki/insights/insight-case-build-recommends-without-reading-the-governing-rule.md`. The three renders change with their rules; `backlog.md` is written by `guppi backlog` from the `purpose` of the Estimate; the insight speaks of the required checks on `main` on GitHub, and it stands. `.guppi/guppi/box.py` refuses `/box` on `main` by `SHARED_NEVER`, a conserved Spec and not an opening Case, so it stands. `rule-github-repository` and `entity-guppi-repository` speak of pushes and rulesets on GitHub; the new branch is local, and it stands. A Grep of `rule-work-mode|rule-where-to-stop|rule-skill-sprint-open|merges-the-closed-sprint-branch|runs-the-spec-on-a-branch` over `.guppi/` printed `.guppi/tests/test_glossary.py`, `.guppi/tests/test_sprint.py` and `.guppi/guppi/sprint.py`, and a Grep of `sprint-open|skills/work|where-to-stop` over `.guppi/tests/` printed `test_gate.py`, `test_ledger.py`, `test_onward.py` and `test_sprint.py`; the hits name a slug in a sample page or a path in a hook message, so no test reads the changed files live and no test changes. No code changes. The ledger of the session holds no `error` lesson by a Grep of `lesson\[error\]`, so no mark is added. Not done: a project whose main branch has another name, an item of `backlog.md` that stays there.
>
> The check of this file listed the files that name the pages this Case changes, and I judged each by its purpose line or path. `estimate-guppi-repository-stops-in-the-merge-tasks` speaks of the merge tasks of `/pr-review` and `/merge-main`, which the sixth condition keeps, so it stands. The row of Work Mode in `glossary.md` says that `/work` runs the Spec on a branch other than `main`; after the one line that makes the branch, the Spec runs on `<id>`, so the row stands. `rule-session` and `orchestration.md` hold no sentence on `main`: a Grep of `` `main`|on main `` over `vault/wiki/` with the glob `{orchestration.md,rules/rule-session.md}` printed no hit. The other files speak of the opening questions, the hook on `/hi`, the sprint id, the readings, the close, the settings or the form of a skill, and they stand. In each replaced Criterion the old line on `main` leaves on purpose for the new lines that let the branch task through, and in `estimate-where-to-stop-stops-only-on-its-conditions` the words "In the merge tasks" become "In the merge and branch tasks". The three sub-cases share lines on the branch task on purpose: each states the same behaviour from the side of its own page, the skill that writes the task, the skill that runs it and the list of stops.

> **problem:**
> On `main` the opening Case writes no branch task and Work Mode refuses to start, so the first sprint of every project stops until the person makes the branch by hand.

> **recommend:**
> - **How the branch task runs, since Work Mode refuses to start on main**
>   - Recommended: (a) Work Mode runs the branch task first, then goes on.
>   - Answer: agreed, (a).

### Case 1034.1 — The opening Case on main makes the sprint branch

> **given:**
> `rule-skill-sprint-open`: the page whose Render sets the tasks of the opening Case.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the Render, the skill `/sprint-open`.
> **＋** `/hi`: the skill of `.claude/skills/hi/SKILL.md`, whose `Branch:` line names the branch.
> **＋** `estimate-skill-sprint-open-merges-the-closed-sprint-branch`: its Criterion is replaced whole.

> **when:**
> The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, while `/hi` printed `main` under `Branch:`, and dispatches `case-guppi` for the opening Case of the next sprint.

> **then:**
> The opening Case holds as its first task line one line that runs `git switch -c <id>`, `<id>` the id of the new sprint.
> **＋** That line opens with no `stop:`.
> **－** The opening Case holds no merge or deletion task.
> **－** The opening Case puts no question on the branch to the person.

```then
update:
- slug: rule-skill-sprint-open
  replace:
  - old: 'When the branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it.'
    new: 'When the branch is `main`, the opening Case holds as its first task line one line that runs `git switch -c <id>`, and no merge or deletion task: Work Mode runs that line before any other task and the rest of the Spec on the branch `<id>`, and a refusal of it is a stop on the sixth condition of `vault/wiki/where-to-stop.md`; the line opens with no `stop:`, since git can undo a local branch (as set in case 1034.1).'
  change: on main the opening Case makes the branch of the sprint by its first task, with no stop
- slug: estimate-skill-sprint-open-merges-the-closed-sprint-branch
  set:
    status: pending
    purpose: Whether /sprint-open has the opening Case write the close line last, with the /merge-main line just before it only where the project holds that skill, push the closed sprint's branch and open its pull request into main after the person's word, merge it with a merge commit after its checks pass when the person is the owner, and move the work to a branch named by the new sprint, as the first tasks of Work Mode, with a stop on a refusal, and on main make that branch by one first task with no stop
  sections:
    Criterion: |-
      When:
      The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, and dispatches `case-guppi` for the opening Case of the next sprint; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

      Then:
      The prompt of the call names the branch that `/hi` printed under `Branch:` from `.claude/skills/hi/SKILL.md`, and whether the person is the owner of the repository: the login that `gh api user --jq .login` prints is the one that `gh repo view --json owner --jq .owner.login` prints.
      **＋** The opening Case writes the line ``- the close of `<id>` — `/sprint-close`, a session of its own`` as the last item of the last milestone of `entity-sprint-<id>`.
      **＋** Where `.claude/skills/merge-main/SKILL.md` stands in the project, the opening Case writes just before that close line the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own``.
      **＋** When that branch is not `main` and the person is the owner, the opening Case holds as its first tasks, in this order, one task that opens with `stop:` and runs `git push -u origin <branch>`, `gh pr create --base main --fill`, `gh pr checks <branch> --watch` and `gh pr merge <branch> --merge`; then `git fetch origin`, `git switch main`, `git merge --ff-only origin/main`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint.
      **＋** When that branch is not `main` and the person is not the owner, the opening Case holds as its first tasks one task that opens with `stop:` and runs `git push -u origin <branch>` and, when `gh pr view <branch>` shows no open pull request, `gh pr create --base main --fill`; then `git switch -c <id>` and `git branch -d <branch>`, so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges it, by `/pr-review` where the project holds `.claude/skills/pr-review/SKILL.md`.
      **＋** When that branch is `main`, the opening Case holds as its first task line one line that runs `git switch -c <id>`, which opens with no `stop:`.
      **＋** Work Mode runs these tasks before any other task of the Spec, stops before the task that opens with `stop:`, on the fourth condition of `vault/wiki/where-to-stop.md`, runs it after the person's word, and runs the rest of the Spec on the branch `<id>`.
      **－** Where `.claude/skills/merge-main/SKILL.md` does not stand, the opening Case writes no line that names `/merge-main`.
      **－** The owner's pull request is merged only after its checks pass, with a merge commit and never with `--admin`, and no Case reviews it: each of its changes was ratified in its own session.
      **－** The opening Case does not merge `main` into the closed branch.
      **－** When a `git` or `gh` command of these tasks refuses, among them `gh pr checks --watch` on a red check and `gh pr merge` on a pull request that cannot be merged, the agent stops on the sixth condition of `vault/wiki/where-to-stop.md`, shows what stopped it, and goes on from where it stopped after the person's answer.
      **－** When that branch is `main`, the opening Case holds no merge or deletion task.
      **－** The opening Case puts no question on the merge or the branch to the person.
  change: the Criterion replaced whole — on main the opening Case makes the branch of the sprint by its first task, with no stop
```

```tasks
- [x] update `rule-skill-sprint-open`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/sprint-open/SKILL.md`
- [x] update `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
- [x] read `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
```

### Case 1034.2 — Work Mode on main runs the branch task of the opening Case first

> **given:**
> `rule-work-mode`: the page whose Render is the skill `/work`.
> **＋** `.claude/skills/work/SKILL.md`: the Render, the skill `/work`.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the approved Spec that Work Mode runs.
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its Criterion is replaced whole, and its defer is retired.

> **when:**
> The agent calls `/work` of `.claude/skills/work/SKILL.md`, rendered from `rule-work-mode`, on the branch `main`.

> **then:**
> When `raw/<date>/<hi HHMM>/spec.md` holds the opening Case of a sprint, Case `<id>-1`, whose first task line runs `git switch -c <id>`, the agent runs that line before any other task and before it writes `work.md`.
> **＋** It ticks the box of that line and runs the rest of the Spec on the branch `<id>`.
> **－** With any other Spec on `main`, the skill stops and says so, and nothing is written or changed.

```then
update:
- slug: rule-work-mode
  replace:
  - old: It stops on `main`.
    new: It stops on `main`, but for the branch task of the opening Case of a sprint, which it runs first (as set in case 1034.2).
  - old: 'If the branch is `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.'
    new: 'If the branch is `main` and the Spec holds the opening Case of a sprint, Case `<id>-1`, whose first task line runs `git switch -c <id>`, run that line before any other task and before `work.md`, tick its box, and run the rest of the Spec on the branch `<id>`; a refusal of it is a stop on the sixth condition of `vault/wiki/where-to-stop.md` (as set in case 1034.2). With any other Spec on `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.'
  change: on main Work Mode runs the branch task of the opening Case of a sprint first, and stops on main for any other Spec
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    status: pending
    purpose: Whether /work loads while guppi check or guppi test finds something, stops on main but for the branch task of the opening Case of a sprint, which it runs first, writes the baseline of uv run --project .guppi guppi test and uv run --project .guppi guppi check into work.md before the first change — the exit code of each as the last line of its preamble line names it — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs uv run --project .guppi guppi test in full and holds each failing test against the baseline, fixing a new one within ratified work
    method: 'by hand, after the librarian''s render that writes .claude/skills/work/SKILL.md from the Render of rule-work-mode that runs the branch task of the opening Case of a sprint on main: uv run --project .guppi guppi render --check; .claude/skills/work/SKILL.md read against each line of the Criterion; the first /work that loads after that render while uv run --project .guppi guppi check exits 1, its preamble lines, its work.md and its run of the tasks read in the transcript of its session under ~/.claude/projects/ and in its spec.md and work.md against the Criterion; the lines on a Case ratified in Work Mode and on the branch main read in that transcript where that session has them, otherwise against the text of the skill; recorded in the estimate line with the transcript named'
  sections:
    Criterion: |-
      When:
      The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
      **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
      **＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

      Then:
      `uv run --project .guppi guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
      **＋** The skill loads while `uv run --project .guppi guppi check` or `uv run --project .guppi guppi test` finds something: its lines Tests and Lint run both commands with `--exit-zero`, and each line comes back with the output of its command and a last line that names the exit code of its run.
      **＋** On the branch `main`, when `raw/<date>/<hi HHMM>/spec.md` holds the opening Case of a sprint, Case `<id>-1`, whose first task line runs `git switch -c <id>`, the agent runs that line before any other task and before it writes `work.md`, ticks its box, and runs the rest of the Spec on the branch `<id>`.
      **＋** On the branch `main` with any other Spec, the skill stops and says so, and nothing is written or changed.
      **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check`, as the last line of Tests and of Lint names it, with each failing test and each lint finding line as printed, and an empty `## Expected red`.
      **＋** When `work.md` already stands, its `## Baseline` stays as it is.
      **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
      **＋** The reply that acknowledges a Case ratified in Work Mode ends the turn, since the hook of `rule-prespec-onward` sends nothing on once `raw/<date>/<hi HHMM>/spec.md` stands; at the person's next message the run goes on from where it stopped.
      **＋** After the reply that acknowledges a Case ratified in Work Mode, and before the first task of that Case, the agent runs `uv run --project .guppi guppi prespec --check` on the plan file of the session, with the session id of its `hi:` line.
      **＋** When that check prints a line that does not open with `note:`, the agent stops as the first condition of `vault/wiki/where-to-stop.md` sets it and sends the finding to the `case-guppi` of that Case; the run goes on after the person ratifies the fixed Case and the check prints no such line.
      **＋** A task of that Case whose work already stands, done under the sub-case the Case replaces, is ticked in `raw/<date>/<hi HHMM>/spec.md` and not run again.
      **＋** A task that changes `uv run --project .guppi guppi check`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
      **＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `uv run --project .guppi guppi test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
      **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
      **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
      **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
      **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
      **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
      **－** In a `/work` that `/box` calls no Case is ratified, so the check of the plan does not run there: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
  change: the Criterion replaced whole — on main Work Mode runs the branch task of the opening Case of a sprint first; the method names the first /work after the render of that text; the defer of case 1008 retired
```

```tasks
- [x] update `rule-work-mode`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/work/SKILL.md`
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
```

### Case 1034.3 — The branch task of the opening Case is no stop on main

> **given:**
> `rule-where-to-stop`: the page whose Render lists the conditions of a stop.
> **＋** `vault/wiki/where-to-stop.md`: the Render, which `/work` loads.
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions`: its Criterion is replaced whole.

> **when:**
> The agent runs `/work` on the branch `main` with the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`, in its context.

> **then:**
> A Spec that holds the opening Case of a sprint whose first task line runs `git switch -c <id>` is no stop on `main`: the agent runs that line first and goes on on the branch `<id>`.
> **＋** A refusal of a `git` command of the branch task of the opening Case is a stop on the sixth condition, as a refusal of its merge tasks is.
> **－** With any other Spec, the agent stops on `main` and says so.

```then
update:
- slug: rule-where-to-stop
  replace:
  - old: '5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.'
    new: '5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch. A Spec that holds the opening Case of a sprint whose first task line runs `git switch -c <id>` is no stop: Work Mode runs that line first and goes on on the branch `<id>` (as set in case 1034.3).'
  - old: or a `git` or `gh` command of the merge tasks of the opening Case of a sprint refuses;
    new: or a `git` or `gh` command of the merge or branch tasks of the opening Case of a sprint refuses;
  change: the branch task of the opening Case is no stop on main, and its refusal is a stop on the sixth condition
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
      **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

      Then:
      The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
      **＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
      **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
      **＋** A fork that changes a contract is a choice that no ratified Case makes, or a ratified Case that turns out wrong: by a text the agent finds wrong or too narrow, or by a finding of `uv run --project .guppi guppi prespec --check` on the plan after a Case ratified in Work Mode.
      **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
      **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
      **＋** A Spec that holds the opening Case of a sprint whose first task line runs `git switch -c <id>` is no stop on `main`: the agent runs that line first and goes on on the branch `<id>`.
      **＋** In a run of `/box`, the agent stops and asks when `uv run --project .guppi guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
      **＋** In the merge and branch tasks that the opening Case of a sprint holds by `.claude/skills/sprint-open/SKILL.md`, the agent stops, shows what stopped it and asks when a `git` or `gh` command refuses.
      **＋** When the full `uv run --project .guppi guppi test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
      **＋** When the auto mode classifier of Claude Code refuses a tool call that the run needs, the agent ends a reply with a question to the person that gives the shell command doing what the refused call would do, for the person to type after `!` in the prompt.
      **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
      **＋** After the person's answer the run goes on from where it stopped.
      **＋** After the person has run the command that a refusal of the auto mode classifier gave, the run goes on from where it stopped.
      **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
      **－** No other point stops the run, but a stop that a skill the project holds sets in the tasks of its own Case: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.
  change: the Criterion replaced whole — the branch task of the opening Case is no stop on main, and its refusal is a stop
```

```tasks
- [x] update `rule-where-to-stop`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/where-to-stop.md`
- [x] update `estimate-where-to-stop-stops-only-on-its-conditions`
- [x] read `estimate-where-to-stop-stops-only-on-its-conditions`
```

## Case 1035 — Each Stop hook finds its own refusal by its name, whatever bracket Claude Code writes

> **context:**
> At the end of a reply, the ledger hook holds back once an `error` lesson written after a Case of the session and asks for its mark; it knows that it already asked by its own refusal in the stretch, the transcript after the person's last message. `refusals_in` and `sent_back_last` of `.guppi/guppi/ledger.py`, which I read whole with `refusal_records`, `own_refusals`, `command_forms`, `untold`, `silenced`, `unmarked_lessons` and `run`, take a refusal as a hook's own only when a line of a `Stop hook feedback:` record opens with `[<command>]: `, the command of that hook. `guppi ratified`, `guppi casecheck` (`own_told`, `last_refused`, `times_given`, `give`, `stop`, `run`, read whole) and `guppi onward` (`told`, `spent`, `plan_onward`, `run`, read whole) reach their refusals through the same functions. In transcript 5c8c941f of session 0316, on Claude Code 2.1.312, the bracket reads `[uv run --project .guppi guppi ledger]`; in transcript 76379bf1 of session 0358, on Claude Code 2.1.317, it reads `[command hook 1]: ledger: lesson[lesson-hooks-relative-project-path-fails-after-a-cd] held — ...` at line 1829 and again at line 1840, and `onward` refused at lines 1828 and 1839 the same way, since neither found a refusal of its own. The four lessons landed at a later `Stop`, after the session commit, which is why lines 33 to 36 of that ledger missed it. In this build, too, the `PreToolUse` feedback reads `[command hook 4]: ratified: ...`. The page https://code.claude.com/docs/en/hooks says that Claude gets the stderr "prefixed with the event name, the tool name, and the hook's command" and says nothing of `command hook <n>`, so a judgment by that number rests on a fact not checked.
>
> The person chose that a hook knows its own refusal by its name at the head of the text after the bracket, whatever the bracket holds, and that the one shared reader changes for all four hooks. Every line that the `Stop` runs of these hooks print opens with the name: I read each `print` to stderr in `ledger.py`, `onward.py`, `casecheck.py` and `ratified.py`, and the messages `held_message`, `stray_message`, `link_message`, `tag_message` and `off_store_message`. `guppi onward` and `guppi onward --plan` both open with `onward:` today, so the lines of the `--plan` run open with `onward --plan:`, and the name is the words of the command after ` guppi `, which a change of the start of the command, such as Case 1032 makes, leaves alone. By the rule on form of case 1031.1 I settled the split into three sub-cases, a new Estimate for the shared reader on `rule-ledger-write`, whose code it is, and the Criteria replaced of the two Estimates of `guppi onward` that state the bracket. The rule that governs this is `rule-one-judgment-one-implementation`: a Grep of `REFUSAL_HEAD|refusal_records|refusals_in|sent_back_last|Stop hook feedback` over `.guppi/guppi/` printed `casecheck.py`, `ledger.py` and `onward.py`, so one function of `ledger.py` judges a refusal and the others call it; `times_given` of `casecheck.py` reads `casecheck: ` inside the text of its own refusals to count one reason, which is another judgment, and it stands.
>
> A Grep of ``line that opens with `\[`` over `vault/wiki/estimates/` printed `estimate-case-check-judges-a-showing-after-a-refusal.md`, `estimate-ledger-write-lifts.md`, `estimate-prespec-onward-sends-the-agent-on.md` and `estimate-retro-onward-sends-the-agent-to-the-handoff.md`. Case 1032.2 and Case 1032.3 of this session already replace the first two Criteria, and `/pre-spec` refuses a second replacement in one session, so Case 1032 carries the change, as below; Cases 1035.2 and 1035.3 replace the other two. A Grep of `onward:` over the root with the glob `{vault/wiki,.claude}/**` printed `estimate-prespec-onward-sends-the-agent-on.md`, `rule-prespec-onward.md`, `rule-retro-onward.md` and `estimate-retro-onward-exits-2-on-an-error.md`; the two pages of the Retro run name its own `onward: not checked: <error>`, which stands. `estimate-ledger-write-asks-for-the-mark-of-a-lesson` promises the hold once, unless the hook already asked since the person's last message, which holds again with this Case, so its Criterion stands; it passed on piped refusals in the old bracket, which is why the defect went unseen. The other Estimates of the four rules that speak of a refusal in the stretch state no bracket, and they stand. A Grep of `Stop hook feedback|command_forms|OLD_RUN|PROJECT_RUN` over `.guppi/tests/` printed `test_casecheck.py`, `test_ledger.py`, `test_onward.py` and `test_ratified.py`; they build refusals in a temporary transcript, some with a text that opens with no name of a hook, so they change; no test reads a page this Case changes live.
>
> I read the file of Case 1032 whole after its build ended, and it carries what this Case needs of it. In 1032.1, the line of `then` on the modules that find their refusals points to `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`, whatever the start of the command; its task on `.guppi/guppi/ledger.py` keeps `command_forms` only for the forms of the registration that `.guppi/guppi/ship.py` removes, which no reader of refusals calls, as the task of 1035.1 on that module says; and its task on `.guppi/tests/test_ledger.py` tests the forms of `command_forms` alone, while Case 1035.1 changes the two tests of a refusal found under each form. In 1032.2 and 1032.3, the own refusal is a line whose text after its bracket opens with `ledger:`, or `casecheck:`, as the new Estimate sets it, and the name of a hook is the words of its command after ` guppi `, which the new start of the command leaves alone. Its 1032.4 replaces the Criterion of `estimate-case-check-refuses-text-before-a-round`, whose line on the last refusal of `guppi casecheck` in the turn, judged by `refusals` of `.guppi/guppi/ledger.py`, stays true with the reader of 1035.1, so no text of the two Cases clashes. Cases 1035.2 and 1035.3 name the hooks on `Stop` in the form that 1032.1 renders. In the stretch where the change lands, a refusal of the `--plan` run written before it opens with `onward:`, and the Retro run may take it once for its own and stay silent; that loses no line, and the stretch ends at the person's next message, so no old form is kept. The ledger of this session holds no `error` lesson by a Grep of `lesson\[error\]`, so no mark is added.
>
> In each replaced Criterion, the lines that leave on purpose are these. In 1035.2, the line on the stretch, which named the bracket `[<command>]: ` and the commands of the hook and of the ledger hook, now points to the new Estimate and names `onward:` and `ledger:`. In 1035.3, the same line names `onward --plan:` and `ledger:`. The line on a refusal of another hook now names a refusal of the Retro run among them. The line on its reason now opens with the sentence that each of its lines opens with `onward --plan:`. The line on an error of its own now names `onward --plan: not checked: <error>`. The last line now says that the Retro run's lines open with `onward:`. In both, the line on where `.claude/settings.json` registers the hook names the other hooks in the form that Case 1032.1 renders, `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi …`, as the `/pre-spec` audit found, since the old form turns false at the librarian's render. Each other line stands word for word. The audit also found that `run` of `.guppi/guppi/onward.py` prints `onward: not checked: <error>` when it cannot read the payload, before it branches on `--plan`; it exits 0 there, and the task of 1035.3 gives that line `onward --plan:` when `--plan` stands among the arguments, so the lines of 1035.1 and 1035.3 on the opening of each line hold. The lines of 1035.2 and 1035.3 share most of their words because the two Criteria held them before, and each speaks of its own run, so they are no clash. The check of this file listed the files that name the pages and files this Case changes, and I judged each by its purpose line or path. `estimate-ledger-write-exits-2-on-an-error`, `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`, `estimate-case-check-exits-2-on-an-error`, `estimate-retro-onward-exits-2-on-an-error`, `estimate-spec-write-tells-each-reason-once`, `estimate-spec-write-answers-a-refusal` and `estimate-ledger-write-names-the-kind-of-a-user-record` were read by a Grep of `refusal|once a stretch` on each: they speak of the hook's own refusal in the stretch without a bracket, or point to the Estimate that defines it, which this Case makes true again, so they stand. `estimate-prespec-onward-tells-the-loop-from-its-end` speaks of which reason the `--plan` run gives and quotes no opening word, so it stands. The other listed files speak of the ledger, the check of a Case, the materialize, lint, the settings, pre-spec or the orchestration in other steps, and they stand. Not done: the number in `[command hook <n>]` is not read, and the `SubagentStop` run of `guppi casecheck` reads no refusal of its own and does not change.

> **problem:**
> Under Claude Code 2.1.317 the bracket of a refusal names no command, so no `Stop` hook of GUPPI finds its own refusal: the ledger hook holds a lesson again at each repeat, and each hook that tells a thing once a stretch tells it again.

> **recommend:**
> - **How a hook recognises its own earlier refusal**
>   - Recommended: (a) by the hook's name at the head of its own lines, the bracket ignored, the `--plan` run's lines opening with `onward --plan:`.
>   - Answer: agreed, (a).
> - **Which hooks the fix covers**
>   - Recommended: (a) all four hooks, through the one shared reader.
>   - Answer: agreed, (a).

### Case 1035.1 — The shared reader finds a refusal by the name of its hook

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose module holds the reader of refusals.
> **＋** `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`: the new check.
> **＋** `.guppi/guppi/ledger.py`: the ledger hook and the one reader of refusals.
> **＋** `.guppi/guppi/ratified.py`: the hook of `rule-spec-write`, which reads its refusals.
> **＋** `.guppi/guppi/casecheck.py`: the Case check, which counts its refusals.
> **＋** `.guppi/guppi/onward.py`: the hook that sends the agent on, which reads its refusals and those of the ledger hook.
> **＋** `.claude/settings.json`: the registration of the hooks.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the reader and of the hold.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the count of refusals.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the reasons told once.

> **when:**
> A `Stop` hook `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi onward` or `guppi onward --plan`, as `.claude/settings.json` registers it, fires at the end of a reply of the main agent, and the stretch of the transcript at `transcript_path` holds refusals of `Stop` hooks.
> **＋** The ledger hook holds a fresh `lesson[error]` line with no mark, and the agent writes the line again in its next reply.

> **then:**
> A refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:`, and each of its lines that opens with a bracket and `]: ` holds the text of one hook.
> **＋** A refusal is a hook's own when its text after the bracket opens with the name of the hook and a colon, such as `ledger:`, whatever the bracket holds: `[command hook <n>]` or the command of the hook.
> **＋** The name of a hook is the words of its command after ` guppi `, so it stays when the start of the command changes.
> **＋** Every line that these hooks print on stderr at a `Stop` opens with the name of the hook and a colon.
> **＋** One function of `.guppi/guppi/ledger.py` makes this judgment, and `refusals`, `own_refusals` and `sent_back_last` use it for each of the five hooks.
> **＋** The ledger hook asks about the held line once, and the line written again in the next reply lands in the session's ledger at the `Stop` of that reply.
> **＋** Each line that one of these hooks tells once a stretch is told once, and `guppi casecheck` stops at its third refusal of one reason.
> **－** A refusal whose text after the bracket opens with the name of another hook is no refusal of this hook, and `onward:` and `onward --plan:` never match each other.
> **－** No hook reads the number in `[command hook <n>]`.

```then
create:
- slug: estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook
  ref: rule-ledger-write
  kind: QA
  purpose: Whether each Stop hook of GUPPI finds its own refusals in the transcript by its name at the head of the text after the bracket, whatever the bracket holds, by one function of ledger.py, so that a held lesson is asked about once and a line told once a stretch is told once
  method: 'uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_onward.py .guppi/tests/test_casecheck.py .guppi/tests/test_ratified.py, whose refusals stand under [command hook <n>] and under the command; by hand, at the Retro of the session that creates this Estimate: each Stop hook feedback record of the main transcript of that session under ~/.claude/projects/ after the commit of the change read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: and lint reads the name as a broken link (as set in case 977).
    new: and lint reads the name as a broken link (as set in case 977). A `Stop` hook of GUPPI finds its own refusals in the transcript by its name at the head of the text that follows the bracket of a refusal, such as `ledger:`, whatever the bracket holds, the command of the hook or `command hook <n>`, by one function of `.guppi/guppi/ledger.py` that the ledger hook, `guppi ratified`, `guppi casecheck` and `guppi onward` call, so that a held lesson is asked about once and a line told once a stretch is told once (as set in case 1035.1).
  change: each Stop hook finds its own refusal by its name, whatever bracket Claude Code writes
```

```tasks
- [x] create `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`
- [x] update `rule-ledger-write`
- [x] `.guppi/guppi/ledger.py`: `refusals_in` and `sent_back_last` take a refusal as a hook's own when a line of the record opens with a bracket and `]: ` and the text after it opens with the name of the hook and a colon, the name being the words of its command after ` guppi `, by one function both call; `command_forms` is no longer called by them; the module docstring and the docstrings of `refusals`, `refusals_in`, `sent_back_last` and `command_forms` say so.
- [x] `.guppi/guppi/casecheck.py`: the comment of `COMMAND` says that its refusal is found by its name, `casecheck:`.
- [x] `.guppi/tests/test_ledger.py`: each refusal of a hook in the tests opens with the name of the hook after its bracket; new tests find a refusal under `[command hook 1]` and under the command, find none for a text of another hook, keep `onward:` and `onward --plan:` apart, and hold a lesson once under `[command hook 1]` and write it on the repeat.
- [x] `.guppi/tests/test_casecheck.py`: each refusal of a hook in the tests opens with the name of the hook after its bracket, and a test counts three refusals of one reason under `[command hook 3]`.
- [x] `.guppi/tests/test_ratified.py`: each refusal of the hook in the tests opens with `ratified:` after its bracket, and a test tells a reason once under `[command hook 2]`.
- [x] read `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`
```

### Case 1035.2 — The Retro run of onward finds its refusals by its name

> **given:**
> `estimate-retro-onward-sends-the-agent-to-the-handoff`: its Criterion is replaced whole.
> **＋** `rule-retro-onward`: the rule of the hook.
> **＋** `rule-prespec-onward`: the rule of the `--plan` run, which keeps its own judgment.
> **＋** `.guppi/guppi/onward.py`: the hook.
> **＋** `.guppi/guppi/ledger.py`: the reader of the stretch and the refusals.
> **＋** `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`: the check of the reader.
> **＋** `.claude/settings.json`: the registration of the hooks.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff of the session.
> **＋** `vault/wiki/where-to-stop.md`: the conditions of a stop.
> **＋** `.guppi/tests/test_onward.py`: the tests of the hook.
> **＋** `uv run --project .guppi guppi onward`: the command of the hook.
> **＋** `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi ledger`: the ledger hook as `.claude/settings.json` registers it.
> **＋** `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi ratified`: the Spec hook as `.claude/settings.json` registers it.
> **＋** `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi casecheck`: the Case check as `.claude/settings.json` registers it.
> **＋** `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi context`: the hook of the context size as `.claude/settings.json` registers it.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi onward` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, the reply that ended does not open with `STOP:`, and its own refusal is not spent.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook and the hook it belongs to are judged as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it: its own refusal opens with `onward:` after its bracket, and a refusal of the ledger hook with `ledger:`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one. So after a reply that the ledger hook refused, it sends the agent on again at the end of the next reply, the one that writes the refused lines again.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds before the mark `retro`, once `handoff.md` stands, once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
> **＋** It judges the stretch and the refusals in it by `.guppi/guppi/ledger.py`, whose function of the stretch the ledger hook calls too.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi ledger`, `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi ratified`, `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi casecheck` and `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi context`.
> **－** It counts nothing, reads no test result and calls no model. Its judgment is the mark, the file, the refusals in the transcript and the first word of the reply.
> **－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
> **－** It writes no file and no mark.
> **－** `uv run --project .guppi guppi onward --plan` keeps its own judgment, set by `rule-prespec-onward`.

```then
update:
- slug: estimate-retro-onward-sends-the-agent-to-the-handoff
  set:
    status: pending
  change: the Criterion replaced whole — its own refusal is found by its name, whatever the bracket holds
```

```tasks
- [x] `.guppi/guppi/onward.py`: the module docstring says that its own refusal and that of the ledger hook are found by their names, `onward:` and `ledger:`, by the reader of `.guppi/guppi/ledger.py`.
- [x] `.guppi/tests/test_onward.py`: each refusal of a hook in the tests opens with the name of the hook after its bracket, and a test finds the Retro run spent under `[command hook 5]`.
- [x] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
- [x] read `estimate-retro-onward-sends-the-agent-to-the-handoff`
```

### Case 1035.3 — The plan run of onward speaks and is found under its own name

> **given:**
> `estimate-prespec-onward-sends-the-agent-on`: its Criterion is replaced whole.
> **＋** `rule-prespec-onward`: the rule of the hook.
> **＋** `.guppi/guppi/onward.py`: the hook and its reasons.
> **＋** `.guppi/guppi/ledger.py`: the reader of the stretch and the refusals.
> **＋** `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook`: the check of the reader.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: the check of its reasons.
> **＋** `.claude/settings.json`: the registration of the hooks.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the session.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `vault/wiki/orchestration.md`: the layout of a showing and of a Case out.
> **＋** `.guppi/tests/test_onward.py`: the tests of the hook.
> **＋** `uv run --project .guppi guppi onward --plan`: the command of the hook.
> **＋** `/pre-spec`: the skill whose `prespec` line the hook waits for.
> **＋** `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi onward`: the Retro run as `.claude/settings.json` registers it.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session and, after it, a `prespec` line of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block, or a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook and the hook it belongs to are judged as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it: its own refusal opens with `onward --plan:` after its bracket, and a refusal of the ledger hook with `ledger:`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `refusals` of `.guppi/guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply: the one that writes a line again, or an answer with no `LEDGER` block, such as the answer that no Case fixed the cause of the lesson.
> **＋** A refusal of another `Stop` hook in the stretch, one of `uv run --project .guppi guppi onward` included, neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** Each line it prints on stderr opens with `onward --plan:`. Its reason sends the agent on with the Cases still out, to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
> **＋** Each reason adds that, when only the person can go on — a question the person must answer, or a Case that waits only for the person's word — the agent opens with `STOP:` a reply that carries a `LEDGER` block, or that answers a reply the ledger hook sent back, and asks the person instead; that a reply that shows a Case or a round of `case-guppi` carries no `LEDGER` block and opens with no `STOP:` line, in the layout `vault/wiki/orchestration.md` sets; and that while a `case-guppi` has not answered the agent ends the turn as `vault/wiki/orchestration.md` sets it for a Case out and goes on in the turn that the answer opens.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript. `.claude/settings.json` registers it on `Stop`, after `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi" guppi onward`.
> **－** A Case still out, as `rule-prespec-onward` judges it, does not keep it silent: it changes only its reason.
> **－** With no `prespec` line of this session after its `hi` in the event log, it exits 0 and prints nothing, and its reason never tells the agent to call `/pre-spec`.
> **－** A reply with no `LEDGER` block after a reply that the ledger hook did not send back gets no reason, a reply that shows a Case with no line before its first Case heading among them.
> **－** An error of its own after it has read the payload, when a `prespec` line of this session stands after its `hi`, exits 2 with `onward --plan: not checked: <error>` on stderr and the advice, when no Case is left out, to go on with the loop after the findings of `/pre-spec` or to run the check and exit Plan Mode; the advice does not name a call of `/pre-spec`. It does so at most once a stretch, judged by its own refusal in the stretch alone. Before `/pre-spec`, or when it cannot read the `prespec` line, an error of its own exits 0 and does not send the reply back. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run --project .guppi guppi onward` without `--plan` keeps its own judgment, and its lines open with `onward:`.

```then
update:
- slug: rule-prespec-onward
  replace:
  - old: 'after `/pre-spec` it exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, at most once a stretch, judged by its own refusal in the stretch alone (case 597.1).'
    new: 'after `/pre-spec` it exits 2 with `onward --plan: not checked: <error>` on stderr and the advice to go on, at most once a stretch, judged by its own refusal in the stretch alone (case 597.1). Each line it prints on stderr opens with `onward --plan:`, so that its refusals are told apart from those of `rule-retro-onward`, whose lines open with `onward:` (as set in case 1035.3).'
  change: the plan run of onward opens its lines with onward --plan:, so its refusals are found under its own name
- slug: estimate-prespec-onward-sends-the-agent-on
  set:
    status: pending
  change: the Criterion replaced whole — its lines open with onward --plan:, and its own refusal is found by that name
```

```tasks
- [x] `.guppi/guppi/onward.py`: `TO_OUT`, `TO_EXIT`, `TO_LOOP`, the error line of the `--plan` run and the line that `run` prints when it cannot read the payload with `--plan` among its arguments open with `onward --plan:`; the module docstring says so and says that its own refusal is found by that name.
- [x] `.guppi/tests/test_onward.py`: the tests of the `--plan` run expect its lines to open with `onward --plan:`, each of its refusals in the tests opens with that name after its bracket, and a test finds a refusal of the Retro run no refusal of the `--plan` run, and the reverse.
- [x] update `rule-prespec-onward`
- [x] update `estimate-prespec-onward-sends-the-agent-on`
- [x] read `estimate-prespec-onward-sends-the-agent-on`
```

## Case 1036 — The person types git init in a new folder, since /hi stands in Plan Mode

> **context:**
> In a folder that is no git repository, `/hi` prints `none: this folder is no git repository` under `Branch:`, and the step of `rule-git-context` asks whether the agent runs `git init -b main`. Every session of the installed copy opens in Plan Mode by `"defaultMode": "plan"` of `.claude/settings.json`, and `hi_refusal` of `.guppi/guppi/event.py`, read whole, lets a `/hi` through only when its `permission_mode` is `plan`, so leaving Plan Mode is no way out. In the trial of session 0358, recorded in `lesson-git-context-plan-mode-blocks-git-init` and in the Result of `estimate-git-context-offers-git-init`, the person said yes and the agent ran nothing; the transcript `~/.claude/projects/C--PROJECTS-guppi-trial-0358-no-git/2b6bed0c-675a-46ff-8b0d-82e6d19838a8.jsonl`, read at lines 60 to 73, shows at line 64 the agent saying that Plan Mode lets it run no command that changes files and offering `! git init -b main`, at line 70 the person's `<bash-input>git init -b main</bash-input>`, and at line 71 the output `Initialized empty Git repository`. The page https://code.claude.com/docs/en/interactive-mode says of the `!` prefix: "Run shell commands directly without going through Claude". The page https://code.claude.com/docs/en/permission-modes says that in Plan Mode a shell command outside the read-only set prompts for approval, and that "Claude is still instructed to plan without editing", which is what the agent followed in the trial. The person chose that the step asks nothing and tells the person to type `! git init -b main` and then `/hi` again, and that the Case covers only this step of `/hi`.
>
> The rule that governs this is the one rule of `vault/wiki/ratification.md` and the Purpose of `rule-default-mode`: nothing is written before a Case is ratified. Today that Purpose allows one write by the agent, `git init -b main`; with this Case the agent writes nothing before a Case, and the person's own shell command is no call of the agent, so that sentence is set anew. `rule-skill-hi`, under `## How it works`, says that the agent runs `git init -b main` on the person's yes and with the person's leave; that sentence is set anew too, and the rest of the sentence on `allowed-tools` stands. By the rule on form of case 1031.1, I settled one Case with no sub-cases, since the change is one promise, and the Criterion of `estimate-git-context-offers-git-init` replaced whole, with its `purpose` and `method` set anew, rather than a new Estimate; its slug stays, since the step still offers the command. `estimate-default-mode` promises that a session opens in Plan Mode, which holds, so it stands. `estimate-git-context-current` and `estimate-git-context-gitstate-exits-zero` speak of the line `Branch:` and of `guppi gitstate`, which do not change, so they stand. Each line of the old Criterion changes on purpose: the `When` line gains "in Plan Mode"; the first `Then` line tells the person to type the command where it asked a question; the line on the yes, which the agent no longer runs, gives way to the line on the person's own shell command; the line on the no leaves, since no question is asked; the line on the next `/hi` keeps its first half and points to `rule-skill-hi` for the rest; the line "After either answer" becomes a line with no answer in it; and the line on `allowed-tools` loses "the one write before a ratified Case", since the agent runs no write.
>
> A Grep of `git init` over the root with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed `vault/wiki/brief.md` and `vault/wiki/log.md`, not read, `.claude/skills/hi/SKILL.md`, the Render that changes, `vault/wiki/lessons/lesson-git-context-plan-mode-blocks-git-init.md`, `vault/wiki/estimates/estimate-git-context-offers-git-init.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/rules/rule-git-context.md`, `vault/wiki/rules/rule-default-mode.md`, `vault/wiki/estimates/estimate-clean-branch-writes-the-session-files.md`, a `passed` Estimate whose `method` says "/hi typed until its git step has run git init -b main", a step that no longer happens, so the same Case sets that `method` anew by `set` alone, its words on the git step now "/hi typed and ! git init -b main typed as its git step tells", and its Criterion and status stand, since that Criterion speaks of the session files of the copy; and two that stand: `vault/wiki/estimates/estimate-hi-no-read-calls.md`, whose Criterion says `allowed-tools` names no `git init`, which holds; and `vault/wiki/estimates/estimate-git-context-gitstate-exits-zero.md`, where it stands in the Result. A Grep of `skills/hi|rule-git-context|rule-default-mode|rule-skill-hi|git-context` over `.guppi/tests/` printed `test_guard.py`, `test_gitstate.py`, `test_lint.py`, `test_ratified.py`, `test_ship.py` and `test_prespec.py`; each builds a temporary folder or names the path as a string, so no test reads these files live and no test changes. No code changes. Cases 1030, 1031 and 1032 of this session change no page of this Case. The lesson stands in the ledger of session 0358, and the ledger of this session holds no `error` lesson by a Grep of `lesson\[error\]`, so no mark is added. Not done: `/guppi:install` still asks the person to approve a plan, since its session opens in Plan Mode too, which is `rule-plugin-install` and another moment.
>
> The check of this file listed the files that name the pages and files this Case changes, and I judged each by its purpose line or path. `estimate-git-context-current` checks that the context at `/hi` holds the render, the branch and the status and that the skill runs no `git pull`; its `When` was read, and it stands. `estimate-hi-no-read-calls` was read at its line on `allowed-tools`, which holds. `rule-permissions` and `estimate-permissions` say that in Plan Mode the client asks before each edit of the main agent outside the plan file; this Case adds no edit of the agent, so they stand. `rule-settings`, `estimate-settings`, `vault/wiki/rules/schema.yaml` and `rule-rules-schema` name `rule-default-mode` or `rule-git-context` as a child or a marker, and the Render of `rule-default-mode` does not change. The docstrings of `.guppi/guppi/gitstate.py` and `.guppi/guppi/tail.py`, read around their hits, speak of the line `Branch:`, which does not change, and `.guppi/tests/test_gitstate.py` tests that command. `rule-event-log` names Plan Mode only in its History. `estimate-clean-branch-writes-a-clean-copy`, read around its hit, names `estimate-clean-branch-writes-the-session-files` for what the copy writes in place of the session files, which its new `method` does not change, so it stands. The other files name `SKILL.md`, `/hi` or `settings.json` for other skills, other steps of `/hi` or other keys of the settings, and they stand.

> **problem:**
> In a new folder the step of `/hi` offers to run `git init -b main`, but the session stands in Plan Mode, where the agent runs no command that writes, so on the person's yes nothing happens and the check of the step fails.

> **recommend:**
> - **How the repository gets made in a new folder**
>   - Recommended: (a) the person types the command `! git init -b main`; the step asks no question and the agent runs nothing.
>   - Answer: agreed, (a).
> - **What the Case covers**
>   - Recommended: (a) only the step of `/hi` in a folder with no git repository; the plan approval at install stays as it is.
>   - Answer: agreed, (a).

> **given:**
> `rule-git-context`: the page whose Render is the step of `/hi` in a folder with no git repository.
> **＋** `.claude/skills/hi/SKILL.md`: the Render, the skill `/hi`.
> **＋** `rule-skill-hi`: the page of the skill, whose `## How it works` names who runs `git init -b main`.
> **＋** `rule-default-mode`: the page of Plan Mode, whose Purpose names the writes before a Case.
> **＋** `/sprint-open`: the skill that opens a sprint, which this step does not start.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `estimate-git-context-offers-git-init`: its Criterion is replaced whole.
> **＋** `estimate-clean-branch-writes-the-session-files`: its `method` names the git step of `/hi`.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` in a project folder in Plan Mode, and its `Branch:` line, which runs `uv run --project .guppi guppi gitstate` of `rule-git-context`, reads `none: this folder is no git repository`.

> **then:**
> Before `/sprint-open` and before the Frontier, the agent says that GUPPI works only in a git repository, tells the person to type `! git init -b main`, which names the first branch `main`, and then `/hi` again, and ends the reply.
> **＋** The person's `! git init -b main` runs in Plan Mode as the person's own shell command and makes the repository.
> **＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it.
> **－** That `/hi` asks the person no question, starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
> **－** The agent runs no `git init -b main` and writes nothing, as `rule-default-mode` sets it, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name `git init -b main`.

```then
update:
- slug: rule-git-context
  replace:
  - old: Say that GUPPI works only in a git repository, and ask the person whether you run `git init -b main`, which names the first branch `main`. On the person's yes, run `git init -b main` with the Bash tool, say that the repository is made, and tell the person to type `/hi` again. On a no, tell the person to type `/hi` again after `git init -b main`. After either answer, start no `/sprint-open`, write no Frontier, and end the reply.
    new: Say that GUPPI works only in a git repository, and tell the person to type `! git init -b main`, which names the first branch `main` and which Claude Code runs at once as the person's own shell command, in Plan Mode too, and then to type `/hi` again. Ask no question and run no `git init` yourself, since the session stands in Plan Mode and nothing is written before a ratified Case (as set in case 1036). Start no `/sprint-open`, write no Frontier, and end the reply.
  change: the person types git init -b main in a new folder, since /hi stands in Plan Mode
- slug: rule-skill-hi
  replace:
  - old: 'and not `git init -b main`, which the agent runs in a folder that is no git repository only on the person''s yes and with the person''s leave in Claude Code, as `rule-git-context` sets it:'
    new: 'and not `git init -b main`, which the person types as `! git init -b main` in a folder that is no git repository, as `rule-git-context` sets it (as set in case 1036):'
  change: the person, not the agent, runs git init -b main in a new folder
- slug: rule-default-mode
  replace:
  - old: 'One write comes before a Case: at `/hi` in a folder that is no git repository, the agent runs `git init -b main` on the person''s yes, which writes `.git/`, since a session of GUPPI needs a git repository, as `rule-git-context` sets it (as set in case 851.1).'
    new: 'The agent writes nothing before a Case: at `/hi` in a folder that is no git repository, the person types `! git init -b main`, which Claude Code runs as the person''s own shell command and not as a call of the agent, since a session of GUPPI needs a git repository, as `rule-git-context` sets it (as set in case 1036).'
  change: no write of the agent comes before a Case; the person makes the repository
- slug: estimate-git-context-offers-git-init
  set:
    status: pending
    purpose: Whether /hi in a folder that is no git repository tells the person to type ! git init -b main and then /hi again, asks no question, runs no write of its own, opens no sprint and writes no Frontier, and whether the next /hi goes on in the repository the person made
    method: 'by hand, after the librarian''s run of the session that ratifies this Criterion, in a repository that holds the module of the command ship: in an empty folder that is no git repository, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code opened there, /hi typed, ! git init -b main typed as the reply tells, then /hi typed again, and the replies, the context of each /hi and the session folders in the transcripts of those sessions under ~/.claude/projects/, and git branch --show-current, read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the person types git init -b main, and the agent asks nothing and runs nothing
- slug: estimate-clean-branch-writes-the-session-files
  set:
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after the librarian''s run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: in an empty folder that is no git repository, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, the copy and the folder being those of the reading of estimate-git-context-offers-git-init where that reading runs at the same commit, /guppi:install typed, Claude Code reopened, /hi typed and ! git init -b main typed as its git step tells, the next /hi typed, and guppi sprint --check, guppi backlog --check and guppi glossary --check run over the copy, read against the Criterion'
  change: the method follows the git step of /hi, where the person types git init -b main
```

```tasks
- [x] update `rule-git-context`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
- [x] update `rule-skill-hi`
- [x] update `rule-default-mode`
- [x] update `estimate-git-context-offers-git-init`
- [ ] read `estimate-git-context-offers-git-init`
- [x] update `estimate-clean-branch-writes-the-session-files`
```

## Deferred

## Case 1037 — The reading of the searches of ask-guppi at pre-spec put off

> **context:**
> The person put off the rest of the Frontier at the close of Plan Mode. `estimate-ask-searches-at-prespec` stands `failed` (L1 of session 0358): a Grep over the repository root reached `vault/archive/`, and a Glob and a Grep searched the archive by a session path, not by slug. No Case of this session changes `rule-ask`.

> **problem:**
> No Case of this session decides how the searches of `ask-guppi` at `/pre-spec` keep out of the archive and search it by slug.

```then
defer:
  - slug: estimate-ask-searches-at-prespec
    type: estimate
    purpose: "Whether ask-guppi at pre-spec keeps its searches out of vault/archive/ and answers the archive by slug alone; failed in session 0358 (L1), put off at the close of Plan Mode"
```

## Case 1038 — The reading of the searches of case-guppi for the names of what it changes put off

> **context:**
> The person put off the rest of the Frontier at the close of Plan Mode. `estimate-case-build-searches-the-names-of-what-it-changes` stands `failed` (L3 of session 0358): the build of Case 1015 neither read nor named three files whose paths speak of the searches it widens. Case 1031 of this session changes `rule-case-build` on choices of form, not on these searches.

> **problem:**
> No Case of this session decides how `case-guppi` finds and names each file that names what its Case changes.

```then
defer:
  - slug: estimate-case-build-searches-the-names-of-what-it-changes
    type: estimate
    purpose: "Whether case-guppi reads or names in context each file that names what its Case changes; failed in session 0358 (L3), put off at the close of Plan Mode"
```
