<!-- approved 04:45:52 · session 4e339a31 -->

# Spec — session 0248, 2026-09-30

## Case 534 — Python in a session prints UTF-8

> **context:**
> The agent often runs its own Python scripts through the Bash tool. On Windows, Python writes console output in the locale's code page. `guppi/cli.py` measured that code page as cp1252 on 2026-09-09. The Bash tool reads those bytes as UTF-8. So a character outside cp1252 stops the script at the print, which is the case `lesson-bash-tool-heredoc-escapes-interpreted` records. A character inside cp1252, such as the dash, goes through without an error and reaches the agent as U+FFFD. Here that happened at the reading of `estimate-context-size-warns-past-the-limit` (reading L4 of `raw/2026-09-30/0138/ledger.md`). The script ran with no encoding set, printed the dash of `guppi context --prompt` as U+FFFD, and the handoff called it a defect of the hook. The transcript of session 876c4080 holds the correct dash in the hook's stdout and in the text the agent received, and no U+FFFD at all. A second run of the same script with `PYTHONIOENCODING=utf-8` printed the dash. The hook needs no fix. The main agent reads that Estimate again and writes a lesson line; neither is part of this Case. Today `.claude/settings.json` has no `env` block. `rule-settings` is its frame, with three children: `rule-default-mode`, `rule-permissions` and `rule-hook-registry`. None of the three owns an environment. The renderer takes a child's text bare into a `.json` target and finds each child by its marker line in the frame. The vault's answer: no page covers the environment of a session. The near pages are `rule-settings`, the frame that gets the new marker line; `lesson-bash-tool-heredoc-escapes-interpreted`, the manual workaround of setting `PYTHONIOENCODING` in each command; and `lesson-hooks-windows-stdin-encoding`, the hook side, already fixed in code. The tags `harness` and `session` fit. The slugs `rule-python-utf8` and `estimate-python-utf8-output-intact` are free. In the frame, four texts contradict the change. The Purpose and the `purpose` of `rule-settings` both say three rules share the file. The Purpose of `rule-hook-registry` says the file is one text of three rules. The Criterion of `estimate-settings` lists the three children and their key order. This Case changes all four. The sentence of `rule-hook-registry` says "several rules" in place of a number, so a later child leaves it true. That page's `estimate-hook-registry-rendered` speaks of the hooks, so a pair in its Purpose leaves it alone. Sub-case 534.2 replaces the Criterion of `estimate-settings` whole. Two of its lines change on purpose: the line on the order of the children now names the fourth child and the key order, and the line on what `rule-settings` holds now names a variable of the environment too. The lesson stands as it is: it records what was true when it was written. `estimate-default-mode` and `estimate-permissions` speak of the `permissions` keys, which do not change. `rule-harness` stays as it is, since the new rule's parent is `rule-settings`.

> **problem:**
> The Bash tool starts each Python process of a session in the locale's code page. Unless each command sets the encoding, a dash reaches the agent as U+FFFD and other characters stop the script. That already produced one false reading and one false Frontier item. The harness should set UTF-8 once, for every Python process of the session, through a ratified rule.

### Case 534.1 — the env block sets PYTHONUTF8

> **given:**
> `rule-python-utf8` — the new rule; its Render is the `env` block of the settings file
> **＋** `estimate-python-utf8-output-intact` — the promise of the new rule
> **＋** `rule-settings` — the frame of `.claude/settings.json`; takes the marker line of the new child
> **＋** `rule-hook-registry` — a sibling child; its Purpose names the rules that share the file
> **＋** `.claude/settings.json` — the rendered file; its `env` reaches the processes of the session
> **＋** `rule-render-harness` — the renderer; a `.json` target takes a child's text bare
> **＋** the Bash tool of Claude Code — runs the agent's commands in the environment of the session

> **when:**
> A session starts with `.claude/settings.json` as `uv run guppi render` wrote it from `rule-settings`, and the agent runs a Python script through the Bash tool, with no encoding set in the command, that prints a dash and a character outside cp1252.
> **＋** The hooks of `.claude/settings.json` run in the same session.

> **then:**
> `.claude/settings.json` carries `"PYTHONUTF8": "1"` under `env`, the text of `rule-python-utf8`.
> **＋** The script runs in UTF-8 mode, and the dash reaches the agent in the output of the Bash tool as the dash, not as U+FFFD.
> **＋** The character outside cp1252 prints, and the script does not stop at the print.
> **＋** The output of a hook of `.claude/settings.json` reaches the agent as before, its dashes kept.
> **－** The Render of `rule-python-utf8` holds no key other than `PYTHONUTF8`.

```then
create:
- slug: rule-python-utf8
  type: rule
  kind: Leaf
  purpose: Prevents a Python script that a session runs on Windows from printing through the code page of the locale, where a dash reaches the agent as U+FFFD and a character outside the code page stops the script
  enforcement: render
  governs: .claude/settings.json
  render_mode: partial
  ref: rule-settings
  tags:
  - harness
  - session
  sections:
    Purpose: 'Prevents a Python script that a session runs on Windows from printing through the code page of the locale (measured cp1252, `guppi/cli.py`). The Bash tool reads the output as UTF-8: a character outside the code page stops the script at the print, and a character inside it, such as the dash, reaches the agent as U+FFFD without an error. A reading of 2026-09-30 took that mark for a defect of `guppi context --prompt`, while the transcript held the dash (case 534). `PYTHONUTF8=1` in the `env` of `.claude/settings.json` puts every Python process of the session in UTF-8 mode: the console, the pipes and the default encoding of a file opened without one. The `guppi` commands set UTF-8 on their own stdout and stderr in `guppi/cli.py` and do not depend on it.'
    Render: |-
      <!-- rule-python-utf8 -->
        "env": {
          "PYTHONUTF8": "1"
        }
      <!-- /rule-python-utf8 -->
- slug: estimate-python-utf8-output-intact
  type: estimate
  ref: rule-python-utf8
  kind: QA
  purpose: A Python script the agent runs through the Bash tool with no encoding set prints a dash and a character outside cp1252 intact, and the hooks keep their output
  method: 'uv run guppi render --check and json.load of .claude/settings.json; then by hand at a later session start: a Python script run through the Bash tool with no encoding in the command prints a dash and a character outside cp1252, and the tool output shows both; the Stop line of guppi context shows its dash'
  tags:
  - harness
  - session
update:
- slug: rule-settings
  set:
    purpose: Keeps the rules that share .claude/settings.json from becoming two copies of one file
  sections:
    Purpose: |-
      Keeps the rules that share `.claude/settings.json` from becoming two copies
      of one file. The permission mode a session opens in, what may be written without a
      question, which hook fires on which event, and the environment every process of the
      session runs with are different rules with different criteria, and one file carries
      them all. This page is the file: its body is the whole of `settings.json`, and each
      `<!-- child -->` line names the page that owns that text.

      `parent: rule-harness`: the file belongs to no phase of the session.
    Render: |-
      <!-- rule-settings -->
      {
        "permissions": {
      <!-- rule-default-mode -->
      <!-- rule-permissions -->
        },
        "hooks": {
      <!-- rule-hook-registry -->
        },
      <!-- rule-python-utf8 -->
      }
      <!-- /rule-settings -->
  change: a fourth child, rule-python-utf8, owns the env block after hooks
- slug: rule-hook-registry
  replace:
  - old: the file is one text of three rules
    new: the file is one text of several rules
  change: the Purpose no longer counts the rules that share .claude/settings.json; rule-python-utf8 joined them
```

```tasks
- [x] create `rule-python-utf8`
- [x] create `estimate-python-utf8-output-intact`
- [x] update `rule-settings`
- [x] update `rule-hook-registry`
- [x] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-python-utf8-output-intact` at a later session start
```

### Case 534.2 — the settings file is rendered from four children

> **given:**
> `estimate-settings` — the promise that the settings file is rendered whole and loads
> **＋** `rule-settings` — the frame of `.claude/settings.json`
> **＋** `rule-default-mode` — the child that owns `defaultMode`
> **＋** `rule-permissions` — the child that owns `allow`
> **＋** `rule-hook-registry` — the child that owns the hooks
> **＋** `rule-python-utf8` — the child that owns `env`
> **＋** `.claude/settings.json` — the rendered file
> **＋** `vault/raw/<date>/event_log.md` — the day's event log that a session start writes to

> **when:**
> `uv run guppi render` writes `.claude/settings.json` from `rule-settings` and its children, and the next session starts from that file.

> **then:**
> The file is the Render of `rule-settings`, and the text of each child replaces its `<!-- child -->` line in the order of `children`: `rule-default-mode`, `rule-permissions`, `rule-hook-registry`, `rule-python-utf8`. That order gives the order of the top-level keys of the file: `permissions`, `hooks`, `env`.
> **＋** The file parses as JSON, and `uv run guppi render --check` exits 0.
> **＋** The next session start writes its `session-start` line into `vault/raw/<date>/event_log.md`, from the hooks of the rendered file.
> **－** `rule-settings` holds no rule of its own about what a hook, a permission or a variable of the environment may be.

```then
update:
- slug: estimate-settings
  set:
    status: pending
    purpose: The settings file is rendered whole from rule-settings and its children, parses as JSON and loads at session start
  change: the Criterion replaced whole — a fourth child, rule-python-utf8, and the env key after hooks
```

```tasks
- [x] update `estimate-settings`
- [x] read `estimate-settings` at a later session start
```

## Case 535 — Five glossary rows agree with the pages that define them

> **context:**
> The table in the `## Terms` section of `entity-glossary` gives one row per term: the term, its meaning in one line, and the page that defines it. `uv run guppi glossary` writes `vault/wiki/glossary.md` from this table at the librarian's run, and `/hi` loads that file into every working session. At the `/hi` of this session, a reading of `estimate-glossary-terms-defined` came back failed. Its ledger line counts three rows that contradict the page they point to. First, the `Decision page` row gives `## Context` only to a Case without `given`, but `rule-decisions-schema` also gives it to the two-line body of a Case superseded in its own session (case 299.4). Second, the `Main agent, Subagent` row has the main agent write ledger lines "until the Retro commit", but `rule-retro` ends Retro with one `LEDGER` block in the reply after that commit (case 531.8). Third, the `Plan Mode` row covers only Cases ratified or deferred. But `rule-case-protocol` also closes an item that needs no decision without a Case, leaves an item of the sprint for later, and keeps a backlog item as it stands (cases 356.1, 356.2, 421.4, 451.1). The subagent that took the reading also noted two more false rows, which the ledger line does not count, since neither contradicts its `where` page. The `Types` row says a `delete` sets `status: deleted`, but no page schema allows that status, and the docstring of `guppi/generate.py` sets `archived` with a History line `deleted`. The `CLAUDE.md, case-schema.md` row names two of the rules spliced into `CLAUDE.md`, while `rule-claude-md` names three (case 360). The person chose to fix all five rows, to keep the promise as it stands, and to have the `Plan Mode` row name every way an item closes. This is an `update`, so no vault query was run. The frame holds no hook. The Estimates of `rule-glossary` promise the render, the check of the file and the ticks, not the content of the rows, so they are not touched. The Criterion of `estimate-glossary-terms-defined` still says what the rows must meet, so it is not replaced. Its next reading comes at a later `/hi`, after the librarian's run writes the rows. For that reason the Case holds no `read` line, since Retro would count one as debt.

> **problem:**
> Five rows of the glossary, a file loaded into every session, say something that a page of the vault or the code contradicts. The words of those rows must change to agree with the pages.

> **given:**
> `entity-glossary` — the table of terms, whose rows this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, loaded by `/hi`
> **＋** `rule-glossary` — renders the table and stops the write when a row is off its form
> **＋** `rule-decisions-schema` — defines the body of a Decision page
> **＋** `rule-retro` — defines where the last ledger lines of a session stand
> **＋** `rule-case-protocol` — defines Plan Mode, the close of a Frontier item and the types of a decision
> **＋** `rule-claude-md` — defines what `CLAUDE.md` holds
> **＋** `guppi/generate.py` — its docstring defines what a `delete` sets

> **when:**
> A reader reads a row of `vault/wiki/glossary.md` at `/hi`, after `uv run guppi glossary` wrote it from `entity-glossary` at the librarian's run.

> **then:**
> The row `Decision page` gives `## Context` also to the two-line body of a Case superseded in its own session, as `rule-decisions-schema` does.
> **＋** The row `Main agent, Subagent` puts the last ledger lines in the one reply that ends Retro, after its commit, as `rule-retro` does.
> **＋** The row `Plan Mode` names each way a Frontier item closes, as `rule-case-protocol` does: a Case that is ratified or deferred, an item that needs no decision and closes with no Case, an item of the sprint left for later, and a backlog item kept as it stands.
> **＋** The row `Types` says a `delete` sets `archived` with a History line `deleted`, as the docstring of `guppi/generate.py` does.
> **＋** The row `CLAUDE.md, case-schema.md` names the three rules spliced into `CLAUDE.md`, as `rule-claude-md` does.
> **－** No other row of `entity-glossary` changes, and no row is added or removed.

```then
update:
- slug: entity-glossary
  replace:
  - old: '`## Context` only for a Case without `given`, such as the short form of a deferred decision, and never `## Given`'
    new: '`## Context` only for a Case without `given`, such as the short form of a deferred decision, and in the two-line body of a Case superseded in its own session (case 299.4), never `## Given`'
  - old: Runs Cases and writes ledger lines, until the Retro commit
    new: Runs Cases and writes ledger lines, the last of them in the one reply that ends Retro, after its commit (case 531.8)
  - old: Frontier items discussed as Cases until each is ratified or deferred
    new: 'The Frontier worked item by item: an item that needs a decision is a Case until it is ratified or deferred, an item that needs none closes with no Case, an item of the sprint may be left for later and a backlog item kept as it stands; it ends when no item of the Cases list is open (cases 356.1, 356.2, 421.4, 451.1)'
  - old: '`delete` sets `status: deleted` after an impact analysis, the librarian archives'
    new: '`delete` sets `status: archived` with a History line `deleted`, after an impact analysis, and `guppi cleanup` moves the file to the archive'
  - old: '`rule-language` and `rule-agent-writing` in their markers (cases 59.8, 272, 288.3)'
    new: '`rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers (cases 59.8, 272, 288.3, 360)'
  change: the rows Decision page, Main agent, Plan Mode, Types and CLAUDE.md agree with the pages that define them (case 535)
```

```tasks
- [x] update `entity-glossary` — five rows agree with the pages that define them
- [x] `uv run guppi glossary`
```

## Case 536 — case-guppi gives the meaning of the person's words and never quotes them

> **context:**
> The main agent sends the person's words and answers to `case-guppi` in Russian, verbatim and untranslated, as `rule-case-protocol` requires. The frame of `case-guppi` in `rule-case-build` says to write the whole Case in English, but it does not say what to do with a quotation of those words. So `case-guppi` has copied the person's Russian words into the `context` of a Case. The pre-spec language finding then found a letter outside the Latin script, and the Case was built and ratified again. This happened twice. Case 512 quoted the person in Russian in its context (`lesson-case-build-quotes-the-person-in-the-chat-language`). At the rebuild of Case 524, its context held the person's Russian reply (`lesson-case-build-rebuild-quotes-the-relayed-words`). Both lessons are clustered under `insight-case-form-chat-form-read-by-no-script`, which is open in the backlog. The person asked for one line in the frame of `case-guppi` so that it does not write their words verbatim.
> The Case adds one sentence to the Render of `rule-case-build`. The sentence uses the placeholders `{{chat_lang}}` and `{{documentation_lang}}`, which the render fills from `rule-guppi-config` (case 476.1). No page is created, so no vault query ran. In the frame, `estimate-case-build-writes-the-case` already promises the Case "whole in English". A Russian quotation breaks that line, so a reading against it catches one. The person chose to leave that Estimate as it stands (round answer (b)), and its reading can still run in this session. `estimate-case-build-writes-a-plain-round` is about the shape of a round and is not touched. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` is about readers in code and is not touched either. The line of `rule-case-protocol` that has the main agent relay the words verbatim stands: the new sentence governs what `case-guppi` writes, not what it gets. The `－` line of `estimate-language-spec-prose-in-english` says that a quotation in `given`, `when` or `then` keeps its language. That line describes what the check reads, and it grants no permission, so it stands. This Case does not add the language finding to the `SubagentStop` check of `rule-case-check`: Case 537 of this session does that. This Case leaves the backlog item `rule-prespec-script-skips-code-spans` as it stands.

> **problem:**
> `case-guppi` gets the person's words in Russian and has no instruction about quoting them. So a Case sometimes holds a Russian quotation, the pre-spec language finding refuses it, and the Case is built and ratified again.

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the rendered frame
> **＋** `rule-case-protocol` — the main agent relays the person's words verbatim and untranslated
> **＋** `rule-prespec` — its language finding refuses a name, `context` or `problem` with a letter outside the script of the documentation language

> **when:**
> The main agent sends `case-guppi`, by the dispatch or by `SendMessage`, the person's words or answers in the chat language, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> `case-guppi` gives the meaning of the person's words in the documentation language in the Case it answers with.
> **＋** No part of the Case quotes the person's words word for word.
> **＋** The language finding of `rule-prespec` finds no quotation of the person in the name, `context` or `problem` of a Case built this way.
> **－** The main agent still relays the person's words to `case-guppi` verbatim and untranslated, as `rule-case-protocol` requires.

```then
update:
- slug: rule-case-build
  replace:
  - old: You decide nothing the person has not decided.
    new: 'The person''s words reach you in {{chat_lang}}: give their meaning in {{documentation_lang}}, and quote none of them word for word in the Case. You decide nothing the person has not decided.'
  change: case-guppi gives the meaning of the person's words in the documentation language and quotes none of them word for word in the Case (case 536)
```

```tasks
- [x] update `rule-case-build` — one sentence added to its Render: `case-guppi` gives the meaning of the person's words and never quotes them
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
```

## Case 537 — The check of each answer of case-guppi runs the language finding, and the insight closes

> **context:**
> Every answer of `case-guppi` goes through the `SubagentStop` check of `rule-case-check` before the main agent sees it. The check builds each Case of the answer as the Spec would hold it, runs the `/pre-spec` checks over that text through `prespec.judge`, and sends back an answer that has a finding. The language finding of `/pre-spec` is not one of those checks. It is `check_untranslated` of `guppi/prespec.py`, and only `guppi prespec --check` runs it. So a name, `context` or `problem` that holds Russian letters passes the check, and the person sees the Case with them. `/pre-spec` finds the letters near the end of Plan Mode, and then the Case is built and ratified again. This happened twice: Case 512 quoted the person in Russian (`lesson-case-build-quotes-the-person-in-the-chat-language`), and the rebuild of Case 524 held the person's Russian reply (`lesson-case-build-rebuild-quotes-the-relayed-words`). Both lessons are the live children of `insight-case-form-chat-form-read-by-no-script`. That insight is `open` with severity 2, and its `addressed_by` names `decision-case-449`. Case 536, ratified in this session, tells `case-guppi` never to quote the person's words. That closes the cause of the second lesson. The first lesson names the check itself as its cause.
> The person chose three things. First, to close the insight and add the language finding to the check. Second, to make it a finding, not a note. A finding works as every finding of the check works today. It sends a changed answer back to `case-guppi`. When the store already holds the same text with findings, the check stores it again and exits 0, so an unchanged answer is not sent back twice. In `guppi/casecheck.py` no file of the Case is written while a finding stands, in either path, and the `Stop` check refuses to show a Case stored with findings. A note would go back only once, and the file would then be written. Third, to give the check a new promise and not replace the Criterion of an existing one. The check imports `check_untranslated` and calls it on the Spec text it already builds. It holds no copy of the judgment (`rule-one-judgment-one-implementation`). `prespec.judge` does not change, and its docstring keeps the language finding out of `judge`. The one new Estimate has a `ref`, so no vault query ran. The slug `estimate-case-check-refuses-a-letter-outside-the-script` is free.
> In the frame, one sentence of the Purpose of `rule-case-check` says that the text of the story sections is not among the checks, only their presence and their order. The change makes that sentence false, so the Case rewords it. The sentence of `rule-case-protocol` that says no script judges the story sections stands: it speaks of their length and clarity, and `/pre-spec` has judged their script since case 387.4. The Criterion of `estimate-case-check-sends-back-a-faulty-case` says the check runs `judge`, and it does not say that the check runs nothing else. Its line on an unchanged answer holds for the new finding as it holds for any other, so the person left it as it stands. The other four Estimates of `rule-case-check` speak of the `Stop` comparison, the backlog lines and the two notes, and are not touched. `estimate-language-spec-prose-in-english` speaks of `/pre-spec` only, and it stands. `.claude/settings.json` registers no other hook on `SubagentStop`. The new reader needs no old form. It sends the answer back to `case-guppi`, which writes it again, so nothing is lost while the frame of Case 536 waits for the render.
> The insight is set `actioned`, and `addressed_by` names this Case. The cascade of `generate` then archives the two clustered lessons. The rest of its Proposal, a script that judges the text of the story sections, was rejected by case 449. One thing stays not done: the backlog item `rule-prespec-script-skips-code-spans` is left as it stands. When it is taken up, it changes the imported function, and so both checks at once.

> **problem:**
> A Case with Russian letters in its name, `context` or `problem` reaches the person, because the check of each answer of `case-guppi` does not run the language finding. `/pre-spec` finds the letters only later, and the Case is built and ratified again. The insight that records this pattern is still open.

> **given:**
> `rule-case-check` — the rule of the check on each answer of `case-guppi`
> **＋** `estimate-case-check-refuses-a-letter-outside-the-script` — the new promise of the language check
> **＋** `insight-case-form-chat-form-read-by-no-script` — the insight this Case actions
> **＋** `guppi/casecheck.py` — `uv run guppi casecheck --subagent`, the hook on `SubagentStop`, and its store `<plan>.checked.json`
> **＋** `guppi/prespec.py` — `check_untranslated`, the language finding of `/pre-spec`
> **＋** `guppi/config.py` — reads `guppi.toml`, its `documentation_lang`, and judges the script of a letter
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file the hook writes for a Case that passed

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the answer and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the answer that holds a letter outside the script of the language `guppi.toml` sets as `documentation_lang` is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` answers again.
> **＋** While such a finding stands, no `raw/<date>/<hi HHMM>/cases/case-<N>.md` is written for the answer.
> **＋** An answer whose names, contexts and problems hold no such letter gets no finding from this check.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
> **＋** The hook runs `check_untranslated` of `guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
> **－** An answer whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged answer is not sent back twice, and no file is written for it.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

```then
create:
- slug: estimate-case-check-refuses-a-letter-outside-the-script
  type: estimate
  ref: rule-case-check
  kind: QA
  purpose: An answer of case-guppi whose name, context or problem holds a letter outside the script of the documentation language is a finding of the check, and no file of the Case is written while it stands
  method: uv run pytest tests/test_casecheck.py -k script
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: 'the text of the story sections — `context`, `problem` and `recommend` — is not among them, only their presence and their order: the person judges the text (case 449).'
    new: 'the text of the story sections — `context`, `problem` and `recommend` — is not among them, only their presence, their order and the script of the name, `context` and `problem` of a Case, by the language finding of pre-spec: the person judges the text (cases 449, 537).'
  - old: It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else.
    new: 'It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. It runs besides the language finding of `/pre-spec`, `check_untranslated` of `guppi/prespec.py`, imported, over the same text: a name, `context` or `problem` of a Case of the answer that holds a letter outside the script of the documentation language `guppi.toml` sets is a finding of that Case, sent back and stored as any other finding, and a `guppi.toml` that is missing or names a code the table does not hold is one finding, given to the first Case of the answer (case 537).'
  change: the check of each answer of case-guppi runs the language finding of pre-spec as a finding (case 537)
- slug: insight-case-form-chat-form-read-by-no-script
  set:
    status: actioned
    addressed_by: decision-case-537
  change: 'actioned: case-guppi quotes none of the person''s words (case 536), and the check of each answer runs the language finding (case 537)'
```

```tasks
- [x] update `rule-case-check`
- [x] create `estimate-case-check-refuses-a-letter-outside-the-script`
- [x] update `insight-case-form-chat-form-read-by-no-script`
- [x] `guppi/casecheck.py` — `check_answer` imports `check_untranslated` from `guppi/prespec.py` and runs it on the Spec text it builds, each finding to its Case; the docstring says so
- [x] `tests/test_casecheck.py` — tests whose names hold `script`: a Russian letter in a name, a `context` and a `problem` is a finding with exit 2 and no file written; the same answer again is stored and exits 0 with no file written; an English answer passes; a Russian quotation in `then` passes; a missing `guppi.toml` is one finding
- [x] read `estimate-case-check-refuses-a-letter-outside-the-script` at a later session
```

## Case 538 — The brief of `/carry` keeps Next session from the open lines of the Frontier

> **context:**
> `/carry` ends a planning session whose ratified Spec is left for a later session. It rewrites `vault/wiki/brief.md` in a short shape. Step 1 of `rule-carry-over` (case 451.9) leaves out Readings due and Next session. The root cause of `lesson-carry-short-brief-drops-the-work-list` names the claim behind that step: `make lint` lists the pending Estimates again. But `/hi` builds its Work list and its Ask list from the Next session of the brief alone (`rule-skill-hi`), and it reads neither `make lint` nor the Frontier of the previous session. After the `/carry` of session 2024, the `/hi` of session 0138 had no Work list. The open W lines of the 2024 Frontier and the Readings due of the brief of 1c196e8 stood on no list, and they were restored by hand. Case 531.10 kept the short shape without Next session. The person put the fix off as Case 533, so `rule-carry-over` carries `deferred_by: [[decision-case-533]]` and stands in `backlog.md`. In the round, the person chose two things. First, Next session in the short brief is taken from the open lines of the session's `frontier.md`, and Readings due and Readings at the close stay out. Second, both Criteria that speak of the short brief are replaced whole, one sub-case each. At pre-spec, the person also chose that `Cases` in the brief of `/carry` is always the line "none". `/pre-spec` fails on an open line under `## Cases`, and `/carry` runs only after `ExitPlanMode`, so no such line is open at `/carry`. A deferred decision reaches `/hi` through `backlog.md`, and a sprint item reaches it through `vault/wiki/sprint.md`. No page is created, so no vault query ran. In the frame, the paragraph of the Render of `rule-brief` on the second writer says that Next session is omitted. The last `－` line of `estimate-brief-written` says that the brief of `carry` has no Next session. The change makes both false, so sub-case 538.2 rewrites both. The second line of `estimate-carry-over-writes` still holds, and sub-case 538.1 replaces that Criterion whole with a new line on what the short shape holds. Case 539 of this session removes the move of `generate` that sends a milestone item of the sprint page to the Backlog, and the drop of an emptied milestone. It also changes the words of `rule-brief` on those moves. So, by the person's choice in the round of Case 539, the new Criterion of `estimate-brief-written` no longer says that Flags name those moves. Pre-spec will note on purpose that two old lines of that Criterion are not carried: the line on the moves and the line on the brief of `carry`. Sub-case 538.2 does not touch the text of `rule-brief` on the moves, since Case 539 changes it. The two sub-cases share words about the sections of the brief and the lists of Next session. That is on purpose: each Criterion must read whole without the other, one for the librarian's run and one for `/carry`. The Purpose of `rule-end-of-work` and the Purpose of `rule-backlog` stay true, and `rule-skill-hi` does not change. No code reads the sections of the brief: a Grep of `guppi/` and `tests/` found none. So no reader has to accept an old form. The lesson was written in session 0138, and its fix is ratified in this session, so it gets no mark (case 284.2). `insight-session-vault-knowledge-not-loaded` has `severity: 1`, and of its children only `lesson-carry-short-brief-drops-the-work-list` is live. It stays open, since this Case does not change it. Two things are not done: how `/work` takes up a conserved Spec (Frontier item C4), and the two or three lists of Next session in the brief of the librarian (Frontier item C7).

> **problem:**
> The short brief of `/carry` has no Next session, and `/hi` takes its Work list and its Ask list only from Next session. So the session after a conserved Spec starts with no open work, and the open readings drop out of sight. The frame of the brief and its Estimate still promise that shape.

### Case 538.1 — `/carry` writes Next session from the open lines of the Frontier

> **given:**
> `rule-carry-over` — the rule whose Render is the skill `carry`, the second end of a session beside Work Mode, `/retro` and `/handoff`
> **＋** `.claude/skills/carry/SKILL.md` — the rendered skill
> **＋** `estimate-carry-over-writes` — the promise of what `/carry` writes
> **＋** `vault/wiki/brief.md` — the brief `/carry` rewrites
> **＋** `raw/<hi date>/<hi HHMM>/frontier.md` — the Frontier of the session, whose open lines the brief takes
> **＋** `raw/<hi date>/<hi HHMM>/carry.md` — the mark of a conserved Spec, committed with the rest of `vault/raw/`
> **＋** `vault/wiki/backlog.md` — written by `uv run guppi backlog`, shows the conserved Spec and each deferred decision; a sprint item stands on `vault/wiki/sprint.md`
> **＋** `rule-skill-hi` — `/hi` takes its Work list and its Ask list from the Next session of the brief alone, and `/pre-spec` fails on an open line under `## Cases`

> **when:**
> The agent calls the skill `/carry` on `PreToolUse Skill`, after the person answered "conserve" at the fork `ExitPlanMode` prints. The person never types it.

> **then:**
> The skill reads the tree. When the tree holds changes outside the session folder and `vault/wiki/brief.md`, the skill stops and says that work was done and the ordinary exit applies.
> **＋** Otherwise it rewrites `vault/wiki/brief.md` in the short shape, with no Deferred list.
> **＋** The short shape holds Where things stand, Flags and Next session, with no Readings due and no Readings at the close.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, a list with no item the line "none": `Cases` is always the line "none", since a deferred decision reaches `/hi` through `vault/wiki/backlog.md` and a sprint item through `vault/wiki/sprint.md`; `Work` holds each open `W` line of `raw/<hi date>/<hi HHMM>/frontier.md`, and `Ask the person` each open `A` line with its Estimate by slug, the mark `needs the person` and its question.
> **＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
> **＋** It runs `uv run guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
> **＋** It runs `make style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
> **－** No open `W` or `A` line of `frontier.md` is left out of Next session, so the next `/hi` takes each one into its Frontier.
> **－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
> **－** The work stays sequential, session after session: one conserved Spec, no parallel work.
> **－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

```then
update:
- slug: rule-carry-over
  replace:
  - old: no Readings due, no Next session, no Readings at the close, no Deferred list — the conserved Spec and its targets stand in `backlog.md` (case 451.9); Flags say what the vault does not know about this session.
    new: 'no Readings due, no Readings at the close, no Deferred list — the conserved Spec and its targets stand in `backlog.md` (case 451.9); Flags say what the vault does not know about this session; Next session keeps its three lists, one line per item, a list with no item the line "none": `Cases` always the line "none" — a deferred decision reaches `/hi` through `backlog.md`, a sprint item through the sprint page; `Work` each open `W` line of `vault/raw/<hi date>/<hi HHMM>/frontier.md`; `Ask the person` each open `A` line of it, with its Estimate by slug, the mark `needs the person` and its question. `/hi` takes its Work list from Next session alone, so a line left out is lost to the next session (case 538.1).'
  change: 'the short brief of /carry keeps Next session: Work and Ask the person from the open lines of the session''s frontier.md, Cases the line none (case 538.1)'
- slug: estimate-carry-over-writes
  set:
    status: pending
  change: 'the Criterion replaced whole — the short brief keeps Next session: Work and Ask the person from the open lines of frontier.md, Cases the line none'
```

```tasks
- [x] update `rule-carry-over` — step 1 of the Render keeps Next session: `Work` and `Ask the person` from the open lines of `frontier.md`, `Cases` the line "none"
- [x] update `estimate-carry-over-writes`
- [x] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
- [ ] read `estimate-carry-over-writes` at the first `/carry` after the render, and at the `/hi` after it
```

### Case 538.2 — the frame of the brief says that the brief of `carry` keeps Next session

> **given:**
> `estimate-brief-written` — the promise of the frame of the brief
> **＋** `rule-brief` — the frame of the brief; its Render is spliced into the frame of the librarian
> **＋** `.claude/agents/librarian-guppi.md` — the rendered frame of the librarian
> **＋** `vault/wiki/brief.md` — the brief that the librarian and `/carry` write
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the handoff the librarian reads
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose open lines the brief of `carry` takes
> **＋** `vault/wiki/backlog.md` — holds the deferred items the brief does not list; a sprint item stands on `vault/wiki/sprint.md`
> **＋** `rule-carry-over` — the second writer of the brief

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
> **＋** Where things stand, Readings due, Flags and Readings at the close are as before.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
> **＋** An item stands in one list only. A list with no item is the line "none".
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

```then
update:
- slug: rule-brief
  replace:
  - old: Readings due, Next session and Readings at the close are omitted; so is the Deferred list — the conserved Spec and its targets stand in `backlog.md`; Flags say what the vault does not know about this session (cases 190.4, 451.8).
    new: Readings due and Readings at the close are omitted; so is the Deferred list — the conserved Spec and its targets stand in `backlog.md`; Flags say what the vault does not know about this session; Next session keeps its three lists — `Work` the open `W` lines of the session's `frontier.md`, `Ask the person` its open `A` lines, `Cases` always the line "none", since a deferred decision reaches `/hi` through `backlog.md` and a sprint item through the sprint page — because `/hi` takes its Work list from Next session alone (cases 190.4, 451.8, 538.2).
  change: 'the brief of carry keeps Next session: Work and Ask the person from the open lines of the session''s frontier.md, Cases the line none (case 538.2)'
- slug: estimate-brief-written
  set:
    status: pending
  change: the Criterion replaced whole — the brief of carry keeps Next session, Work and Ask the person from the open lines of frontier.md and Cases the line none; Flags no longer name the moves of generate that case 539 removes
```

```tasks
- [x] update `rule-brief` — the paragraph on the second writer says that the brief of `carry` keeps Next session: `Work` and `Ask the person` from the open lines of `frontier.md`, `Cases` the line "none"
- [x] update `estimate-brief-written`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] read `estimate-brief-written` at the librarian's run after the render
```

## Case 539 — `generate` moves no line of the sprint page, and the finish conditions stand only under Done when

> **context:**
> After the cascade, `guppi generate` reads the `frontier.md` of every session. It moves to the `## Backlog` of the sprint page any milestone item that three sessions in a row put off, and it drops a milestone that the move leaves with no item (cases 354.1, 354.2). The librarian's run over session 0138 moved four items out of Slice 5 — closing of `entity-sprint-migration`: `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `rule-spec-box` and `rule-morph`. The first two are Estimates of the sprint page, its finish conditions, and they can be read only at the close. So every session puts them off, and the move always takes them. `vault/wiki/backlog.md` now lists them as work put off in 3 sessions, while `vault/wiki/sprint.md` still shows them under Done when, which it reads from the page's `estimates`. The move worked as ratified. The person chose three things. First, the move goes, because in practice it gets in the way: a line of the sprint page moves only when the person asks for it. Second, the finish conditions of a sprint stand under Done when and are never item lines, so each milestone holds exactly the items whose closing closes it. Third, `rule-spec-box` and `rule-morph` stay in the Backlog. In the second round the person also chose three things. `estimate-sprint-moves-a-passed-over-item` is renamed to `estimate-sprint-items-move-only-by-a-case` and gets the opposite promise, with a test. `estimate-sprint-drops-an-emptied-milestone` is deleted. The principle is one sentence in `rule-sprint`, and no check enforces it. The Criterion of `estimate-brief-written`, replaced by Case 538.2 in this session, named the Flags line on moves. That Case is rebuilt by its own `case-guppi` without the line, so this Case does not touch that Estimate. By the same rule, `estimate-sprint-migration-leftovers-gone` also leaves Slice 5, which then holds only its note on the close of a sprint. The note keeps the milestone open. No page is created without a `ref`, so no vault query ran.
> In the frame, the change makes six texts false, and this Case rewrites each one. The first is the sentence of `rule-sprint` on the move. The second is two sentences of the Purpose of `rule-page-generation`: the list of the steps and of what they read, where no step reads the Frontiers any more, and the sentence on the move. The third is the Flags item and the sentence on how the sprint page changes in the Render of `rule-brief`; those pairs stay off the paragraph on `carry` that Case 538.2 rewrites. The fourth is the reason that the Render of `rule-skill-hi` gives for opening a sprint line with its slugs in code spans, namely that `generate` counts it; the form of the line stays, and `guppi backlog` still reads its slugs for its count. The fifth is the words "the reader of the sprint move" in `rule-backlog` and in the docstring of `guppi/backlog.py`. The sixth is the same words in the Criterion of `estimate-backlog-renders`: at pre-spec the person chose to replace that Criterion whole, in sub-case 539.4. `estimate-hi-writes-frontier` asks for the slug in a code span and gives no reason, so it stands. `estimate-sprint-renders-the-backlog` promises one Done when line per Estimate, and that does not change. The functions `frontiers` and `frontier_marks` stay in `guppi/generate.py`, because `guppi/backlog.py` imports them. The History lines of the moves already made stay on the sprint page. The code change runs from the working tree in Work Mode. No reader refuses an old form in the meantime, so no old form is kept.
> Three things will look like gaps at the check and are on purpose. First, sub-case 539.1 carries no line of the old Criterion of `estimate-sprint-moves-a-passed-over-item`: the count, the move, its History line and its exceptions are the promise the person chose to reverse. Second, sub-case 539.4 carries every line of the old Criterion of `estimate-backlog-renders` but one. The line on the count now names `generate.frontier_marks` without the words on the move, and it adds that `guppi/backlog.py` holds no copy of that reader. Third, some sub-cases share words. Sub-cases 539.1 and 539.2 both say that the sprint page changes only by a Case: one for `generate`, one for the frame of the librarian. Sub-cases 539.1 and 539.3 both say that the rule pages no longer name the move, each for its own pages. Sub-cases 539.3 and 539.4 both speak of the lines of `## Deferred` in `backlog.md`: one for the sprint page, one for the promise of the script. Each sub-case keeps its words so that it reads alone. Not done: a check that refuses a finish condition written as an item, which the person did not take; the close of a sprint, still a note of Slice 5 (Frontier item C2); and `rule-spec-box` and `rule-morph`, which stay in the Backlog.

> **problem:**
> `generate` moves sprint items by a count of put-offs. That count always reaches the finish conditions of the sprint, which can only be read at the close, so the move turns them into put-off work in `backlog.md`. The person wants no line of the sprint page to move without their request. They also want the finish conditions to stand only under Done when, so that each milestone holds exactly the items whose closing closes it.

### Case 539.1 — `generate` moves no line of the sprint page

> **given:**
> `guppi/generate.py` — the script; the move and the drop after the cascade are removed
> **＋** `tests/test_generate.py` — the tests of the move, replaced by one test that nothing moves
> **＋** `rule-sprint` — the rule of the sprint page; says how its lists change
> **＋** `rule-page-generation` — the rule of `generate`; names the steps it computes beyond the yaml and what they read
> **＋** `estimate-sprint-moves-a-passed-over-item` — the promise of the move, renamed and turned to its opposite
> **＋** `estimate-sprint-drops-an-emptied-milestone` — the promise that an emptied milestone leaves, deleted
> **＋** `entity-sprint-<id>` — the sprint page, its `## Milestones`, `## Backlog` and History
> **＋** `frontier.md` under `vault/raw/` and `vault/archive/` — the Frontiers the move counted

> **when:**
> `uv run guppi generate` runs over the vault with one live page `entity-sprint-<id>`, and the `frontier.md` of three or more sessions in a row, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names an item of its `## Milestones` in a code span.

> **then:**
> After the run, `## Milestones` and `## Backlog` of `entity-sprint-<id>` stand as before it, each line in its place, unless an entry of the run changes the page.
> **＋** A milestone whose items were all put off keeps its heading under `## Milestones`.
> **＋** `guppi/generate.py` writes no line about a move into the History of `entity-sprint-<id>`, and it prints no such line on stdout.
> **＋** A line of `entity-sprint-<id>` moves only through an entry of a Case the person ratified, an `update` that `generate` applies like any other.
> **－** `rule-sprint` and `rule-page-generation` name no move of a sprint line by `generate`.

```then
update:
- slug: rule-sprint
  replace:
  - old: 'the backlog changes by an `update` of the sprint page, a Case, and by one move of `generate`: a milestone item passed over in three sessions in a row goes to the Backlog, and a milestone the move left with no line leaves the Milestones (cases 354.1, 354.2).'
    new: 'the milestones and the backlog change only by an `update` of the sprint page, a Case: `generate` moves no line of the page, however many sessions put an item off (case 539.1).'
  change: the move of a passed-over item and the drop of an emptied milestone removed; the sprint page changes only by a Case (case 539.1)
- slug: rule-page-generation
  replace:
  - old: the pages, the Specs, the ledgers and the Frontiers of `raw/` and the archive by the steps this page names — the cascade, the move of the sprint, the ticks of the Spec
    new: the pages, the Specs and the ledgers of `raw/` by the steps this page names — the cascade, the ticks of the Spec
  - old: After the cascade, the script moves a milestone item of the sprint page passed over in three sessions in a row to its Backlog, by the Frontiers of `raw/` and the archive, and drops a milestone the move left with no line (`rule-sprint`, cases 354.1, 354.2).
    new: 'The script moves no line of the sprint page: a milestone item leaves its milestone only by a Case (`rule-sprint`, case 539.1).'
  change: the move of a passed-over sprint item and the drop of an emptied milestone removed, and with them the reading of the Frontiers (case 539.1)
- slug: estimate-sprint-moves-a-passed-over-item
  rename: estimate-sprint-items-move-only-by-a-case
  set:
    status: pending
    purpose: Whether generate leaves every line of the sprint page in place, a milestone item put off in many sessions in a row included, so that a line moves only by a Case
    method: 'uv run pytest tests/test_generate.py -k moves_no_line; then by hand, the History of entity-sprint-<id> after the librarian''s run of a later session: no line of generate on a move'
  change: renamed from estimate-sprint-moves-a-passed-over-item and the Criterion replaced whole — generate moves no line of the sprint page (case 539.1)
delete:
- slug: estimate-sprint-drops-an-emptied-milestone
  impact: 'The promise ends with the move (case 539.1): no milestone is emptied by generate, so none is dropped; cleanup takes the slug out of the estimates of rule-sprint'
```

```tasks
- [x] update `rule-sprint` — the sprint page changes only by a Case
- [x] update `rule-page-generation` — the move leaves the steps of the script, and no step reads the Frontiers
- [x] update `estimate-sprint-moves-a-passed-over-item` — renamed; the Criterion replaced whole: nothing moves
- [x] delete `estimate-sprint-drops-an-emptied-milestone`
- [x] `guppi/generate.py` — `move_passed_over`, `passes_in_a_row`, `PASSES_TO_MOVE` and their call after the cascade removed, and the paragraph of the docstring on the move; `frontiers` and `frontier_marks` stay, since `guppi/backlog.py` imports them
- [x] `tests/test_generate.py` — the six tests of the move removed; one test `test_generate_moves_no_line_of_the_sprint_page`: a sprint page whose items are put off in three and more sessions in a row stands unchanged after the run, and stdout names no move
- [x] read `estimate-sprint-items-move-only-by-a-case` in a later session, after the librarian's run
```

### Case 539.2 — the brief names no move of the sprint

> **given:**
> `rule-brief` — the frame of the brief, whose Render is spliced into the frame of the librarian
> **＋** `.claude/agents/librarian-guppi.md` — the rendered frame of the librarian
> **＋** `vault/wiki/brief.md` — the brief the librarian writes
> **＋** `entity-sprint-<id>` — the sprint page
> **＋** `guppi/generate.py` — the script whose printed lines the Flags read

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run, with `.claude/agents/librarian-guppi.md` rendered from `rule-brief`.

> **then:**
> The frame asks for no Flags line on an item that `guppi/generate.py` moved to the Backlog of `entity-sprint-<id>`, and none on a dropped milestone, so the Flags of `vault/wiki/brief.md` hold no such line.
> **＋** The frame says that `entity-sprint-<id>` changes only by a Case.
> **－** The other kinds of flag that the frame names stand as before, the lint output included.
> **－** The paragraph of the frame on the brief of the skill `carry` does not change here.

```then
update:
- slug: rule-brief
  replace:
  - old: contradictions; every item `generate` moved to the Backlog in this run — its slug, its milestone, the count and the sessions — and every milestone it dropped, from the lines it printed (case 354.4); the lint output.
    new: contradictions; the lint output.
  - old: the sprint page changes by a Case, or by the move of `generate` (case 354.1), and
    new: the sprint page changes only by a Case (case 539.2), and
  change: Flags no longer name items moved to the Backlog or milestones dropped; the sprint page changes only by a Case (case 539.2)
```

```tasks
- [x] update `rule-brief` — Flags name no move of the sprint, and the sprint page changes only by a Case
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
```

### Case 539.3 — the finish conditions of a sprint stand only under Done when

> **given:**
> `rule-sprint` — the rule of the sprint page; its `estimates` are the Definition of done
> **＋** `entity-sprint-migration` — the sprint page, its `## Milestones` and `## Backlog`
> **＋** `vault/wiki/sprint.md` — written by `uv run guppi sprint`
> **＋** `vault/wiki/backlog.md` — written by `uv run guppi backlog`
> **＋** `rule-backlog` — the rule of `backlog.md`; names the reader of the count
> **＋** `guppi/backlog.py` — the script; its docstring names the reader of the count
> **＋** `rule-skill-hi` — the rule whose Render is the skill `/hi`; gives the form of a sprint line of the Frontier

> **when:**
> The librarian runs `uv run guppi sprint` and `uv run guppi backlog` after `generate` has applied the update of `entity-sprint-migration`, and a reader reads `rule-sprint`, `rule-backlog` and `rule-skill-hi`.

> **then:**
> `vault/wiki/sprint.md` shows each Estimate of `entity-sprint-migration` under Done when only, and no item of a milestone or of `## Backlog` names one of them.
> **＋** Slice 5 — closing holds only its note on the close of a sprint, and it stays the current milestone, open.
> **＋** `vault/wiki/backlog.md` lists no Estimate of `entity-sprint-migration`. The other lines of the page's `## Backlog` stay, and `backlog.md` lists them with their counts as before.
> **＋** `rule-sprint` says that the Estimates of a sprint page stand only under Done when, never as an item line, so that each milestone holds exactly the items whose closing closes it.
> **＋** `rule-backlog` and the docstring of `guppi/backlog.py` name `generate.frontier_marks` as the reader of the count, with no move of the sprint.
> **＋** `rule-skill-hi` keeps the form of a sprint line, its title opening with its slugs in code spans, and gives no count by `generate` as its reason.
> **－** The `estimates` of `entity-sprint-migration` do not change, so the Done when list stays whole.
> **－** No check refuses an item line that names an Estimate of the sprint page.

```then
update:
- slug: rule-sprint
  replace:
  - old: whose `estimates` are its Definition of done and whose `## Milestones` lists the Slices in order
    new: whose `estimates` are its Definition of done — rendered under Done when and never written as an item line of a milestone or of the Backlog, so that each milestone holds exactly the items whose closing closes it (case 539.3) — and whose `## Milestones` lists the Slices in order
  change: the Estimates of a sprint page stand only under Done when, never as an item line (case 539.3)
- slug: entity-sprint-migration
  sections:
    Milestones: |-
      ### Slice 5 — closing

      - the close of a sprint — `entity-sprint-<id>` and the Estimates it lists go to the archive together once each has passed: a done-condition of a sprint has nothing left to guard after the close; not yet decided (case 478.2)
    Backlog: |-
      - the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
      - reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319)
      - reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319)
      - reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319)
      - a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301)
      - [[rule-work-mode]] — the rest of Work Mode past the skill `/work` of case 479.2: the test of each Estimate written first and turned green, and the full model the person plans; cases 183, 206
      - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206
      - [[rule-spec-box]] — the Spec box, case 207, after Slice 3b
      - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
  change: 'the finish conditions lint-clean, merges and leftovers-gone stand only under Done when: off Slice 5 and the Backlog (case 539.3)'
- slug: rule-backlog
  replace:
  - old: The count reads the Frontier files by `generate.frontier_marks`, the reader of the sprint move, and the Specs
    new: The count reads the Frontier files by `generate.frontier_marks`, and the Specs
  change: the reader of the count named without the sprint move, removed by case 539.1 (case 539.3)
- slug: rule-skill-hi
  replace:
  - old: '`` — so that `generate` counts it (case 354.3).'
    new: '``.'
  change: a sprint line keeps its slugs in code spans; the count by generate, removed by case 539.1, is no longer its reason (case 539.3)
```

```tasks
- [x] update `rule-sprint` — the Estimates of a sprint page stand only under Done when
- [x] update `entity-sprint-migration` — the finish conditions off the item lists
- [x] update `rule-backlog` — the reader of the count named without the move
- [x] update `rule-skill-hi` — the form of a sprint line kept, the count by `generate` gone as its reason
- [x] `guppi/backlog.py` — the docstring of the module and of `sessions_of` name `generate.frontiers` and `generate.frontier_marks` without "the reader of the sprint move"
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run guppi sprint`
```

### Case 539.4 — the promise of `backlog.md` names its count reader without the move

> **given:**
> `estimate-backlog-renders` — the promise of what `guppi backlog` writes
> **＋** `guppi/backlog.py` — the script `uv run guppi backlog`, which the librarian runs after `guppi sprint`
> **＋** `vault/wiki/backlog.md` — the file it writes; the governed-files hook refuses a hand edit
> **＋** `guppi/generate.py` — `frontier_marks`, the reader of the Frontier lines; `generate` applies the defers
> **＋** `guppi/materialize.py` — the Spec reader; `materialize` lifts the defers
> **＋** `entity-sprint-<id>` — the sprint page, its `## Backlog`
> **＋** `rule-carry-over` — the skill `carry`, which writes `carry.md` and runs the script
> **＋** `vault/wiki/`, `vault/raw/` and `vault/archive/` — the pages, and the session folders with their `frontier.md`, `spec.md` and `carry.md`

> **when:**
> `uv run guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.

> **then:**
> The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
> **＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `guppi/materialize.py`.
> **＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of `entity-sprint-<id>`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
> **＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, and `guppi/backlog.py` holds no copy of that reader.
> **＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
> **＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
> **－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

```then
update:
- slug: estimate-backlog-renders
  set:
    status: pending
  change: the Criterion replaced whole — the reader of the count named without the sprint move, removed by case 539.1 (case 539.4)
```

```tasks
- [x] update `estimate-backlog-renders`
- [x] read `estimate-backlog-renders` in a later session: `uv run pytest tests/test_backlog.py`, and `vault/wiki/backlog.md` after the librarian's run
```

## Deferred

## Case 540 — `/work` has no words for taking up a conserved Spec

> **context:**
> `/work` runs Work Mode on the approved Spec of the session, `raw/<date>/<hi HHMM>/spec.md`, and names no other Spec. In session 0138 the conserved Spec of session 2024 was run from its own folder: its boxes were ticked there, and its `carry.md` was deleted in Work Mode. `rule-work-mode` says nothing of that path (handoff of 0138, What is not done).

> **problem:**
> A session that takes up a conserved Spec runs Work Mode by the agent's own reading, since `rule-work-mode` does not say which `spec.md` to run, where to tick its boxes, or when to delete `carry.md`.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Prevents implementation starting before the plan, branch and baseline exist
```
