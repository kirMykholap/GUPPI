<!-- approved 15:15:19 · session b66cc24a -->

# Spec — session 1228, 2026-09-25

## Case 419 — `case-guppi` builds the Case, a hook checks it before the showing

> **context:**
> Today the main agent reads the pages itself. Before a `create` it asks the vault through `ask-guppi`, sends the frame to `frame-guppi` for a check, and writes the Case into the chat itself. No script reads the form of a Case in the chat. The hook of `rule-spec-write` checks a Case only after its ratification. So a fault of the form is found by the person or by `ask-guppi` at pre-spec. This happened in session 0051 and is recorded in `insight-case-form-chat-form-read-by-no-script`. Case 416 deferred a new scheme until a live probe. The probe showed two facts. First: `SubagentStop` with exit 2 sends the subagent back with the text of the hook, and the payload holds `agent_type`, `last_assistant_message` and `stop_hook_active`. Second: a Case cannot be shown through `systemMessage`. So the main agent shows the Case, and a hook compares the showing with the checked answer. This Case takes the core of the scheme of 416: who builds a Case, how it is checked, and how the showing is compared. `{supersedes:case 416}` lifts the defer from every page 416 deferred. The parts outside the core are to be deferred again by a short Case: the defers written by the hook, a guard on the plan with the translation after it, and a rule of its own for the orchestration. The question of Case 403, whether a subagent pays, becomes the method of the Estimate of `case-guppi`. `frame-guppi` read the frame of every sub-case and found a contradiction: the Purpose of `rule-ask` named `ask-guppi` the one entry point, each call in the event log; 419.1 rewrites that Purpose whole. `ask-guppi` was not dispatched: the one `create` of a rule, `rule-case-check`, has a `ref`; a Glob found the slugs `rule-case-check` and `rule-case-build` free. Estimates left alone, and why: `estimate-ask-finds` reads how `ask-guppi` answers, not who calls it; the Estimates of `rule-skill-hi` read the Frontier; the Estimates of `rule-spec-write` read the write after ratification; `estimate-hook-registry-rendered` reads only that the file equals the Render.

> **problem:**
> How a Case is built, checked and shown, so that the person sees only a Case that passed the checks of pre-spec, and the reading of the vault and the frame does not fill the main agent's context.

### Case 419.1 — The main agent dispatches `case-guppi` and shows its answer unchanged

> **given:**
> `rule-case-protocol` — the rule of the Case: who builds it, and the story sections
> **＋** `vault/wiki/case-schema.md` — its render
> **＋** `estimate-case-protocol-checks-its-frame` — the Estimate of the frame read before a showing, renamed `estimate-case-protocol-shows-the-built-case`
> **＋** `rule-ask` — the rule of `ask-guppi`: who asks the vault, and when
> **＋** `.claude/agents/ask-guppi.md` — its render
> **＋** `rule-skill-hi` — the rule of `/hi`: its sentence on the vault before a `create`
> **＋** `.claude/skills/hi/SKILL.md` — its render
> **＋** `rule-prespec` — the rule of pre-spec: its sentence on the question before a `create`

> **when:**
> The main agent takes up a Frontier item that needs a Case, the person answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call; nothing of the Case stands in the chat before the answer.
> **＋** A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`.
> **＋** The main agent shows the Case of the answer whole and unchanged, and its own text stands after one horizontal rule.
> **＋** An answer that holds no Case heading is a question the main agent puts to the person, and no Case is shown.
> **＋** The plan file stands with its title line before the first dispatch of the session.
> **＋** The main agent dispatches `ask-guppi` once, at pre-spec, and neither `ask-guppi` nor `frame-guppi` before a showing.
> **－** A deferred decision in the short form is written by the main agent, with no dispatch.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: '## The vault before a `create`'
    new: '## Who builds a Case'
  - old: 'Before a `create` without a `ref`, ask the vault first: does this exist, what conflicts, what sits in `draft`, which tags fit. Dispatch the `ask-guppi` agent with one short question and put the answer in `context`. An `update` carries a `ref` and reads the page itself. Before the first showing of a Case that changes the behaviour of a rule or of a hook, the agent dispatches `frame-guppi` ([[rule-frame-check]]) with the lines of the Case''s `given` and a few lines on what it changes — in the prompt of the call, not in the chat — and fixes each contradiction it returns before the showing, or says why it stands; before a showing again it sends only the lines of `given` added since and the pages changed since. A Case that changes no behaviour of a rule or a hook dispatches nothing; the pages the agent edits by a `replace` pair it reads itself (case 391.2).'
    new: 'Every Case, in Plan Mode and in Work Mode, at its first showing and at every showing again — a ratified Case that changed included — is built by the agent `case-guppi` (`rule-case-build`): the agent dispatches it with the Case id, the Frontier item and its source, and the person''s words on it — in the prompt of the call, not in the chat — and creates the plan file with its title line before the first dispatch of the session. A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`. The agent shows the Case of the answer whole and unchanged, its own text after one horizontal rule; an answer with no Case heading is a question, which the agent puts to the person, and no Case is shown. `case-guppi` asks the vault before a `create` and reads the frame itself; the agent dispatches `ask-guppi` once, at pre-spec. A deferred decision in the short form is the agent''s own, written with no dispatch (case 419.1).'
  - old: what `frame-guppi` found
    new: what `case-guppi` found in the frame
  change: every Case is built by case-guppi and shown unchanged; ask-guppi at pre-spec only (case 419.1)
- slug: estimate-case-protocol-checks-its-frame
  rename: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
    purpose: A Case is built by case-guppi and shown by the main agent unchanged
  change: renamed; the Criterion replaced whole — the Case built by case-guppi and shown unchanged (case 419.1)
- slug: rule-ask
  sections:
    Purpose: 'Prevents a `create` from being proposed without the vault having been asked whether it already holds the thing, or forbids it. One recipe for every caller — the main agent at pre-spec, `case-guppi` at the vault query before a `create`, the librarian, the person — so the search is tuned once, and its cost stays in the searcher''s own context: the index lines and pages never enter the main agent''s. A subagent with read-only tools, dispatched through the `Agent` tool, so the event log records each call; `case-guppi`, which cannot dispatch a subagent, reads this file and runs the recipe itself (case 419.1). The main agent asks once, at pre-spec, for the set of ratified Cases; the librarian asks by finished content afterwards ([[rule-index-check]]). An `update` with a `ref` does not ask: the page itself and a Grep give the `given` (case 154).'
  replace:
  - old: One question before a `create` without a `ref`, and one at pre-spec for the whole set; an `update` with a `ref` reads the page itself.
    new: '`case-guppi` runs this query itself before a `create` without a `ref`; the main agent asks once at pre-spec for the whole set; an `update` with a `ref` reads the page itself.'
  change: the vault query before a create is run by case-guppi; the main agent asks at pre-spec only (case 419.1)
- slug: rule-skill-hi
  replace:
  - old: Before any `create`, ask the vault first ([[rule-ask]]).
    new: Every Case is built by `case-guppi` (`rule-case-build`).
  change: the Case is built by case-guppi, which asks the vault itself (case 419.1)
- slug: rule-prespec
  replace:
  - old: The question to `ask-guppi` before a `create` without a `ref` asks "does this exist"
    new: The vault query of `case-guppi` before a `create` without a `ref` asks "does this exist"
  change: the question before a create is case-guppi's (case 419.1)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `estimate-case-protocol-checks-its-frame`
- [x] update `rule-ask`
- [x] update `rule-skill-hi`
- [x] update `rule-prespec`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-case-protocol-shows-the-built-case`
```

### Case 419.2 — `case-guppi` builds the Case: the vault, the frame and the form

> **given:**
> `rule-frame-check` — the rule of the agent that reads a Case's frame, renamed `rule-case-build`
> **＋** `.claude/agents/frame-guppi.md` — the agent file it renders today, removed
> **＋** `.claude/agents/case-guppi.md` — the agent file it renders after the rename
> **＋** `estimate-frame-check-finds-a-contradiction` — its Estimate, renamed `estimate-case-build-writes-the-case`
> **＋** `vault/wiki/case-schema.md` — the form the agent reads and answers in
> **＋** `.claude/agents/ask-guppi.md` — the vault query the agent runs itself
> **＋** `.claude/settings.json` — the hooks the agent reads for a Case that adds or changes one

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it the person's question or change by `SendMessage`.

> **then:**
> `case-guppi` reads `vault/wiki/case-schema.md` whole before it writes the Case.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` of the Case names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`.
> **＋** Each contradiction it finds is fixed in the Case, or the `context` says why it stands.
> **＋** Its answer is the Case in the chat form of `vault/wiki/case-schema.md`, from the heading to the fence of `ratification`, and nothing else; asked again, it answers with the Case whole again.
> **＋** An answer that needs a choice the person has not made is that question alone, with no Case heading.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** It writes no file and no ledger line.

```then
update:
- slug: rule-frame-check
  set:
    purpose: Prevents a Case from being shown before one agent has built it against the vault, its frame and its form, outside the main agent's context
    governs: .claude/agents/case-guppi.md
  sections:
    Purpose: Prevents a Case from being shown before one agent has built it against the vault, its frame and its form, outside the main agent's context. The agent `case-guppi` gets a Frontier item and the person's words, reads `vault/wiki/case-schema.md`, runs the vault query of `ask-guppi` itself — it cannot dispatch a subagent — reads the pages and files the Case's `given` names, and answers with the Case alone; the main agent shows it unchanged ([[rule-case-protocol]]), and the hooks of `rule-case-check` check it before the showing and compare the showing with it. Until case 419.2 the agent was `frame-guppi`, which read the frame of a Case the main agent wrote and returned the contradictions only; whether a subagent pays for its tokens and time, the question of cases 403 and 408, is the method of its Estimate.
    Render: |-
      <!-- rule-frame-check -->
      ---
      name: case-guppi
      description: Build one Case of Plan Mode from a Frontier item and the person's words — the vault query, the frame, the form — and answer with the Case alone. Asked again by SendMessage with the person's question or change.
      model: opus
      effort: medium
      tools: Read, Grep, Glob
      ---
      You build one Case of Plan Mode. The main agent shows your answer to the person unchanged, and the person ratifies it. The caller's prompt holds the Case id, the Frontier item with its source, and the person's words that bear on it; a later message holds the person's question or change on the Case you built. You decide nothing the person has not decided: when the Case needs a choice the words do not give, answer with that question alone, with no Case heading.

      Read `vault/wiki/case-schema.md` whole first: it is the form, the language and the operands of your answer. Then read the pages the item names — a page is found by a Glob `vault/wiki/**/<slug>.md` — and the code they point to by `governs`, `implementation_ref` or `code_ref`.

      Before a `create` without a `ref`, run yourself the vault query that `.claude/agents/ask-guppi.md` describes, on the question whether the thing exists, what conflicts, what sits in `draft`, which tags fit and whether the slug is free; its answer goes into `context`.

      Before you answer, read the frame of the Case: each page and file its `given` names, the section a line names where it names one, the `## Criterion` of each Estimate a named page lists in `estimates`, and, for a Case that adds or changes a hook, the hooks registered on the same event in `.claude/settings.json` and the rule of each. A contradiction is a sentence of a page or a file that the change would make false or that forbids it, or an Estimate whose Criterion speaks of the thing the change touches and which the Case does not name. Fix each in the Case, or say in `context` why it stands. Open `vault/wiki/decisions/` only as `ask-guppi.md` allows, and `vault/archive/` by slug only.

      Answer with the Case in the chat form of the schema, from its heading to the fence of `ratification`, and nothing else: no line before it, no note after it. A hook checks the answer before the main agent sees it; when it sends findings back, fix the Case and answer with it whole again. Asked again by a message, answer with the Case whole again, changed as asked. Write no file and no ledger line.
      <!-- /rule-frame-check -->
  change: frame-guppi becomes case-guppi, which builds every Case (case 419.2)
- slug: rule-frame-check
  rename: rule-case-build
  change: 'renamed: the rule of the agent case-guppi (case 419.2)'
- slug: estimate-frame-check-finds-a-contradiction
  rename: estimate-case-build-writes-the-case
  set:
    status: pending
    purpose: case-guppi builds a Case against the vault and its frame and answers with the Case alone
    method: 'by hand: two live dispatches in a session after the render, one Case with a create without a ref and one that changes a hook; the tokens and seconds of each dispatch in the estimate line'
  change: renamed; the Criterion replaced whole — case-guppi builds the Case; the method measures its cost (case 419.2)
```

```tasks
- [x] update `rule-frame-check`
- [ ] update `rule-frame-check`
- [x] update `estimate-frame-check-finds-a-contradiction`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] `git rm .claude/agents/frame-guppi.md` — the file no page governs after the rename
- [ ] read `estimate-case-build-writes-the-case`
```

### Case 419.3 — A `SubagentStop` hook checks the Case of `case-guppi`

> **given:**
> `rule-case-check` — the new rule of the hooks that check a Case before the person sees it
> **＋** `guppi/casecheck.py` — the module of its hooks
> **＋** `tests/test_casecheck.py` — its tests
> **＋** `guppi/ratified.py` — the reading of the chat form and the Spec section of a Case, shared with the Spec hook
> **＋** `guppi/prespec.py` — `judge`, the checks of pre-spec, imported
> **＋** `guppi/cli.py` — the command `casecheck`
> **＋** `rule-hook-registry` — the registration of the hook in `.claude/settings.json`
> **＋** `insight-case-form-chat-form-read-by-no-script` — the Insight this check actions
> **＋** `estimate-case-check-sends-back-a-faulty-case` — the Estimate of the check on `SubagentStop`

> **when:**
> `SubagentStop` fires when `case-guppi` answers.

> **then:**
> `uv run guppi casecheck --subagent` reads each Case of `last_assistant_message` in the chat form, by the functions of `guppi/ratified.py`.
> **＋** It builds each Case's section of the Spec in memory, as the Spec hook writes it, and runs `judge` of `guppi/prespec.py` over them, the decision lines of the `ratification` fence standing for the ledger.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` answers again.
> **＋** Each Case of the answer is stored with its findings in `<plan>.checked.json` beside the plan file of the session.
> **＋** On the re-fire (`stop_hook_active`) the findings are stored, and it exits 0.
> **－** An answer with no Case heading, or an answer of another agent, is not checked, not stored, and exits 0.

```then
create:
- slug: rule-case-check
  type: rule
  kind: Leaf
  purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or in other words than the ones that passed them
  enforcement: hook
  implementation_ref:
  - guppi/casecheck.py
  - tests/test_casecheck.py
  - .claude/settings.json
  tags:
  - hooks
  - harness
  - workflow
  - session
  sections:
    Purpose: 'Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or in other words than the ones that passed them. Until case 419 no script read a Case before its ratification: the hook of `rule-spec-write` checks it only after the person signed, and a fault of the form was found by the person or at pre-spec ([[insight-case-form-chat-form-read-by-no-script]]). The checks are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]); a count in a story section is not among them — no script tells a count from other words.'
    How it works: '`uv run guppi casecheck --subagent` on `SubagentStop`. For an answer of `case-guppi` (`agent_type`), it reads the Cases of `last_assistant_message` by the functions of `guppi/ratified.py` that read the chat form, builds the section of each in the Spec in memory as the `Stop` hook of `rule-spec-write` writes it, and runs `prespec.judge` over them, the decision lines of each `ratification` fence standing for the ledger, the Frontier and the ratified copy left to `/pre-spec`. It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. Each Case of the answer is stored, with its findings, in `<plan>.checked.json` beside the plan file of the session, a later answer for the same id replacing it. A finding exits 2 with the findings on stderr, and the agent answers again; on the re-fire (`stop_hook_active`) the hook stores and exits 0. The hooks read stdin as UTF-8 and never raise. An answer with no Case heading is a question and is neither checked nor stored; with no plan file of the session nothing is stored.'
- slug: estimate-case-check-sends-back-a-faulty-case
  type: estimate
  kind: QA
  purpose: A Case of case-guppi that the checks refuse goes back to it before the main agent sees it
  method: uv run pytest tests/test_casecheck.py -k subagent, then by hand the first answer of case-guppi the hook sends back
  tags:
  - hooks
  - harness
  - workflow
  ref: rule-case-check
update:
- slug: rule-hook-registry
  replace:
  - old: '"command": "uv run guppi context", "timeout": 30 } ] } ]'
    new: |-
      "command": "uv run guppi context", "timeout": 30 } ] }
          ],
          "SubagentStop": [
            { "hooks": [ { "type": "command", "command": "uv run guppi casecheck --subagent", "timeout": 30 } ] }
          ]
  change: guppi casecheck --subagent registered on SubagentStop (case 419.3)
- slug: insight-case-form-chat-form-read-by-no-script
  set:
    status: actioned
    addressed_by: decision-case-419.3
  change: 'actioned: the chat form of a Case is checked on SubagentStop before the person sees it; a count in a story section stays unchecked (case 419.3)'
```

```tasks
- [x] create `rule-case-check`
- [x] create `estimate-case-check-sends-back-a-faulty-case`
- [x] update `rule-hook-registry`
- [x] update `insight-case-form-chat-form-read-by-no-script`
- [x] `guppi/ratified.py`: the Spec section of a Case built in memory, apart from its write
- [x] `guppi/casecheck.py`: the `SubagentStop` hook
- [x] `guppi/cli.py`: the command `casecheck`, named among the hook commands of the docstring
- [x] `tests/test_casecheck.py`: `-k subagent` — a clean Case stored, a faulty one exit 2, the re-fire exit 0 with its findings stored, a question and another agent passed
- [ ] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-case-check-sends-back-a-faulty-case`
```

### Case 419.4 — A `Stop` hook compares the shown Case with the checked one

> **given:**
> `rule-case-check` — the rule of the check: its How it works
> **＋** `guppi/casecheck.py` — the module of its hooks
> **＋** `tests/test_casecheck.py` — its tests
> **＋** `guppi/ratified.py` — the reading of a Case in a reply, shared
> **＋** `rule-hook-registry` — the registration of the hook in `.claude/settings.json`
> **＋** `rule-spec-write` — the `Stop` hook beside it, which writes the shown Case into the Spec
> **＋** `estimate-case-check-shows-only-the-checked-case` — the Estimate of the comparison on `Stop`

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json`, line by line once line ends and trailing spaces are the same.
> **＋** A Case the store does not hold, a Case whose text differs from the stored one, or a Case stored with findings exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared.
> **－** On the re-fire (`stop_hook_active`) it exits 0.

```then
create:
- slug: estimate-case-check-shows-only-the-checked-case
  type: estimate
  kind: QA
  purpose: The main agent shows a Case only as case-guppi answered it and the checks passed it
  method: uv run pytest tests/test_casecheck.py -k stop, then by hand the first reply the hook refuses
  tags:
  - hooks
  - harness
  - workflow
  ref: rule-case-check
update:
- slug: rule-case-check
  replace:
  - old: An answer with no Case heading is a question and is neither checked nor stored; with no plan file of the session nothing is stored.
    new: |-
      An answer with no Case heading is a question and is neither checked nor stored; with no plan file of the session nothing is stored.

      `uv run guppi casecheck` on `Stop`, beside `guppi ledger`, `guppi ratified` and `guppi context`, which run in parallel. Each Case the reply shows under its heading with at least one of its sections is compared with the Case of the same id in `<plan>.checked.json`, line by line once line ends and trailing spaces are the same; a parent shown with its sub-cases is compared part by part. A Case the store does not hold, one that differs, or one stored with findings exits 2 with the reason and the findings on stderr. A heading with no section — the acknowledging reply — a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared; on the re-fire (`stop_hook_active`) it exits 0.
  change: the Stop hook compares the shown Case with the checked one (case 419.4)
- slug: rule-hook-registry
  replace:
  - old: '"command": "uv run guppi ratified", "timeout": 30 }'
    new: '"command": "uv run guppi ratified", "timeout": 30 }, { "type": "command", "command": "uv run guppi casecheck", "timeout": 30 }'
  change: guppi casecheck registered on Stop (case 419.4)
```

```tasks
- [x] update `rule-case-check`
- [x] create `estimate-case-check-shows-only-the-checked-case`
- [x] update `rule-hook-registry`
- [x] `guppi/casecheck.py`: the `Stop` hook
- [x] `tests/test_casecheck.py`: `-k stop` — a stored clean Case passes, a missing one, a changed one and one stored with findings exit 2, the acknowledging heading, a `DIFF` fence and a short-form defer pass, a re-shown Case without `recommend` compared, the re-fire exits 0
- [ ] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-case-check-shows-only-the-checked-case`
```

## Case 420 — A vault page read without its History unless the history is asked for

> **context:**
> Every vault page ends with the section `## History`, the record of its changes. Agents read a page whole, its history with it. On the current pages the History is 13% of the text of the vault, 32% on rules and 25% on Estimates. The history costs tokens and also misleads: in session 0051 `frame-guppi` read the order of the `Stop` hooks from the History of `rule-hook-registry` and was wrong (`lesson-hooks-matching-hooks-of-one-event-run-in-parallel`). The person wants the History to stay on the page: in Obsidian the page shows whole. A rule in `.claude/rules/` with `paths:` was weighed. The documentation says it fires on the read of a matching file. But it is text for the model, not a mechanism, and whether it loads inside a subagent is not said. A hook on `Read` works mechanically. The documentation confirms that `PreToolUse` can change the input of a tool through `updatedInput`, that the hooks of `settings.json` fire on the tools of a subagent, and that `PostToolUse` can add `additionalContext`. No live probe has run yet, so it is the first task. On every vault page the History is the last section; no section follows it. `frame-guppi` found that `rule-harness` names in its Purpose the rules outside the pipeline and `estimate-harness-pipeline` reads that list, so the new rule enters it — that is 420.2; and that the docstrings of `guppi/pages.py` and `guppi/cli.py` list the modules and the hook commands — task lines of 420.1. `estimate-hook-registry-rendered` is left alone: it reads only that the file equals the Render.

> **problem:**
> How agents are kept from reading the History of a vault page without an explicit request, the history kept on the page itself.

### Case 420.1 — A hook on `Read` cuts the History of a vault page

> **given:**
> `rule-page-read` — the new rule of the hooks that read a page under `vault/wiki/` without its History
> **＋** `guppi/pageread.py` — the module of its hooks
> **＋** `tests/test_pageread.py` — its tests
> **＋** `guppi/pages.py` — the walk over the sections of a page, shared by `history_line`
> **＋** `guppi/cli.py` — the command `pageread`
> **＋** `rule-hook-registry` — the registration of the hooks in `.claude/settings.json`
> **＋** `estimate-page-read-cuts-the-history` — the Estimate of the rule

> **when:**
> An agent — the main agent or a subagent — calls `Read` on a file under `vault/wiki/`.

> **then:**
> When the call carries neither `offset` nor `limit` and the file holds its own `## History` heading, `uv run guppi pageread` on `PreToolUse` sets `limit` to the line before that heading by `updatedInput`, and the agent gets the frontmatter and the body alone.
> **＋** After such a call, `uv run guppi pageread --after` on `PostToolUse` adds one line of `additionalContext`: the History is cut, its first and last line, and a `Read` with `offset` at its first line shows how the page changed.
> **＋** The heading is found by the walk of `split_sections` in `guppi/pages.py`, so a `## History` inside a render block of the page does not count.
> **＋** An `Edit` of the page after the cut read works as after a whole read.
> **－** A call with its own `offset` or `limit`, a file with no `## History`, and a file outside `vault/wiki/` are not changed, and no line is added.
> **－** The page on disk is not changed: in Obsidian it shows whole.

```then
create:
- slug: rule-page-read
  type: rule
  kind: Leaf
  purpose: Prevents an agent from reading the History of a vault page it did not ask for
  enforcement: hook
  implementation_ref:
  - guppi/pageread.py
  - guppi/pages.py
  - tests/test_pageread.py
  - .claude/settings.json
  tags:
  - hooks
  - harness
  sections:
    Purpose: 'Prevents an agent from reading the History of a vault page it did not ask for. Every page ends with `## History`, the record of its changes; it is a third of the text of a rule and a quarter of an Estimate, and an agent that reads it takes old wordings for the current rule — in session 0051 an agent read the order of the `Stop` hooks from the History of `rule-hook-registry` ([[lesson-hooks-matching-hooks-of-one-event-run-in-parallel]]). The page keeps its History, whole in Obsidian; a hook cuts it from a read, and the agent reads it only by asking for its lines. A rule in `.claude/rules/` was weighed and not taken: it is text the agent may follow, and whether it loads inside a subagent is not documented.'
    How it works: '`uv run guppi pageread` on `PreToolUse` of `Read`. For a file under `vault/wiki/` read with neither `offset` nor `limit`, it finds the line of the page''s own `## History` heading by `pages.history_line` — the walk of `split_sections`, so a heading inside a render block does not count — and returns `updatedInput` with `limit` set to the line before it, with no permission decision. `uv run guppi pageread --after` on `PostToolUse` of `Read` adds one line of `additionalContext` after such a call: the History is cut, its first and last line, and a `Read` with `offset` at its first line shows it. A call with its own `offset` or `limit`, a file with no `## History` — `brief.md`, `sprint.md`, `glossary.md`, `log.md`, `case-schema.md` — and a file outside `vault/wiki/` pass unchanged. The page on disk is never changed. The hooks read stdin as UTF-8 and never raise; an error lets the call pass whole.'
- slug: estimate-page-read-cuts-the-history
  type: estimate
  kind: QA
  purpose: A Read of a vault page returns its frontmatter and body, and its History only when asked for
  method: uv run pytest tests/test_pageread.py, then by hand a Read of a vault page in the main agent and in a subagent after the render
  tags:
  - hooks
  - harness
  ref: rule-page-read
update:
- slug: rule-hook-registry
  replace:
  - old: '"command": "uv run guppi bashguard", "timeout": 30 } ] }'
    new: |-
      "command": "uv run guppi bashguard", "timeout": 30 } ] },
      { "matcher": "Read",
        "hooks": [ { "type": "command", "command": "uv run guppi pageread", "timeout": 30 } ] }
  - old: '"command": "uv run guppi ratified --edit", "timeout": 30 } ] }'
    new: '"command": "uv run guppi ratified --edit", "timeout": 30 } ] }, { "matcher": "Read", "hooks": [ { "type": "command", "command": "uv run guppi pageread --after", "timeout": 30 } ] }'
  change: guppi pageread registered on PreToolUse and PostToolUse of Read (case 420.1)
```

```tasks
- [x] live probe in the scratchpad before any code: `updatedInput` sets `limit` on `Read` in the main agent and in a subagent, and `Edit` works after a cut read; a failure brings the Case back
- [x] create `rule-page-read`
- [x] create `estimate-page-read-cuts-the-history`
- [x] update `rule-hook-registry`
- [x] `guppi/pages.py`: `history_line`, the line of the page's own `## History`, by the walk `split_sections` uses; the docstring names `pageread` among its users
- [x] `guppi/pageread.py`: the two hooks
- [x] `guppi/cli.py`: the command `pageread`, named among the hook commands of the docstring
- [x] `tests/test_pageread.py`: a page cut before its History, a `## History` inside a render block not counted, a call with `offset` or `limit`, a hub file and a file outside `vault/wiki/` passed, the line of `--after`
- [ ] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-page-read-cuts-the-history`
```

### Case 420.2 — `rule-harness` names the new rule among the rules outside the pipeline

> **given:**
> `rule-harness` — the MOC of the harness rules; its Purpose names the rules outside the pipeline
> **＋** `estimate-harness-pipeline` — its Estimate, which reads that Purpose
> **＋** `rule-sprint` — the check that runs between the harness files and the pages in `make lint`
> **＋** `rule-page-read` — the rule added among them

> **when:**
> `make lint` and `make test-harness` run, and someone reads the Purpose of `rule-harness`.

> **then:**
> The Purpose says: three rules belong to no phase of the session — the renderer, the page `settings.json` is assembled from, lint — and with them the check of `rule-sprint` runs in `make lint`, in this order: the harness files against their pages, the sprint file against its page, the glossary file against its page, then the pages.
> **＋** The Purpose names eight more rules that belong to it and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History.
> **＋** `make test-harness` is green; the first three steps of `make lint` — `render`, `sprint` and `glossary --check` — exit 0 with no output on the committed tree; the fourth, `guppi lint`, is read by its own Estimates.

```then
update:
- slug: rule-harness
  replace:
  - old: 'Seven more belong here and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, and the hook that shows the size of the context (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3).'
    new: 'Eight more belong here and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1).'
  change: the hooks of rule-page-read named among the rules outside the pipeline (case 420.2)
- slug: estimate-harness-pipeline
  set:
    status: pending
  change: the Criterion replaced whole — eight rules outside the pipeline, the hooks of rule-page-read among them (case 420.2)
```

```tasks
- [x] update `rule-harness`
- [x] update `estimate-harness-pipeline`
- [ ] read `estimate-harness-pipeline`
```

## Case 421 — The hook writes a defer, and an unchanged item is not deferred again

> **context:**
> Today a defer works by Case 405. When the person asks to defer an item, the agent in the same reply writes a short Case under `## Deferred` of the plan, shows it, and puts the `defer` line into `LEDGER`. The ratification is the person's word itself. The hook of `rule-spec-write` skips a Case that holds only defers, so a deferred Case is the one Case the agent still writes into the plan by hand. Every defer, a repeated one with the same wording included, creates a Decision page and adds it to `deferred_by`; `rule-work-mode` holds 19 decisions there. The brief carries an item of the previous Deferred list on without a new defer when no `supersedes` retired its decision (`rule-brief`). The source of such an item in the Frontier is `deferred`. What `frame-guppi` found entered the Case: the Criterion of `estimate-spec-write-copies-the-ratified-case` said the agent writes a defer, and it is replaced whole; the Criterion of `estimate-prespec-checks-the-frontier` did not know the new closer; the docstring of `guppi/ratified.py` and a test in `tests/test_ratified.py` state the old behaviour, and they are task lines.

> **problem:**
> Who writes a deferred Case into the Spec, and whether an item already deferred and unchanged needs a decision to stay deferred.

### Case 421.1 — The hook `ratified` writes a deferred Case into the Spec

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case into the Spec
> **＋** `guppi/ratified.py` — the hook
> **＋** `tests/test_ratified.py` — its tests
> **＋** `estimate-spec-write-copies-the-ratified-case` — its Estimate of the write, whose exception for a defer goes
> **＋** `estimate-spec-write-checks-the-written-case` — its Estimate of the check after the write, which names a defer-only Case
> **＋** `estimate-spec-write-writes-a-defer` — the new Estimate of the write of a defer
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec in the session's folder, where a defer of Retro goes

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while Plan Mode lasts, and of `raw/<date>/<hi HHMM>/spec.md` once that file stands, at Retro: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **－** The ratified copy `<plan>.ratified.md` gets no defer, and the check after the write does not run on it.

```then
create:
- slug: estimate-spec-write-writes-a-defer
  type: estimate
  kind: QA
  purpose: The Stop hook writes a deferred Case into the Spec as the reply showed it
  method: uv run pytest tests/test_ratified.py -k defer, then by hand the first defer the person asks for after the change
  tags:
  - hooks
  - harness
  - workflow
  ref: rule-spec-write
update:
- slug: rule-spec-write
  replace:
  - old: A defer-only Case is the agent's, under `## Deferred`.
    new: A defer-only Case — a Case whose lines in the reply are all `defer`, beside other Cases or alone — is written by the same hook from the reply that carries its lines and shows it in the short form — `context`, `problem`, a fence tagged `then` — under `## Deferred` of the plan file, or of `spec.md` in the session's folder once that file stands, at Retro; the ratified copy gets none, and the check after the write does not run on it (case 421.1).
  change: the hook writes a defer-only Case too (case 421.1)
- slug: estimate-spec-write-copies-the-ratified-case
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads the session's transcript and finds the last earlier reply that shows `## Case N —` whole.

      Then:
      The hook writes that Case into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as they stand in the chat; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points.
      **＋** It writes the same text the same way into the ratified copy `<plan>.ratified.md` beside the plan file.
      **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
      **＋** A value that holds a backtick in an outer span not padded on both sides is refused: exit 2 with `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
      **＋** `recommend` and `ratification` are not written.
      **＋** When the last showing of Case N is a `DIFF` block, not the Case whole, the hook writes nothing for it.
      **＋** No plan file in the event log, no showing of Case N, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
  change: the Criterion replaced whole — the exception for a defer-only Case dropped, the hook writes it (case 421.1)
- slug: estimate-spec-write-checks-the-written-case
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The `Stop` hook `uv run guppi ratified` has written Case N into the plan file and its ratified copy after a reply whose `LEDGER` block holds the decision lines of Case N.

      Then:
      The hook runs the checks of `prespec --check`, imported from `guppi/prespec.py`, on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
      **＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
      **＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan and in its ratified copy.
      **＋** A finding of a Case not written in this run is not reported.
      **－** On the re-fire (`stop_hook_active`) nothing is checked: exit 0.
      **－** A Case not written in this run — a last showing that is a `DIFF` block — and a defer-only Case, which the hook writes under `## Deferred`, are not checked.
      **－** The Frontier `raw/<hi date>/<hi HHMM>/frontier.md` is not read.
      **－** The plan is not compared with its ratified copy, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
      **－** A ledger line of the window that does not parse is no finding of this check.
  change: the Criterion replaced whole — a defer-only Case is written by the hook and not checked (case 421.1)
```

```tasks
- [x] update `rule-spec-write`
- [x] update `estimate-spec-write-copies-the-ratified-case`
- [x] update `estimate-spec-write-checks-the-written-case`
- [x] create `estimate-spec-write-writes-a-defer`
- [x] `guppi/ratified.py`: the write of a defer-only Case under `## Deferred`, the docstring of the write said anew
- [x] `tests/test_ratified.py`: `-k defer` — a defer written into the plan, into `spec.md` once it stands, replaced on a second showing, several defer-only Cases and one beside a ratified Case in one reply, no showing and a missing item exit 2; `test_write_a_defer_only_case_is_left_to_the_agent` rewritten
- [ ] read `estimate-spec-write-copies-the-ratified-case`
- [ ] read `estimate-spec-write-checks-the-written-case`
- [ ] read `estimate-spec-write-writes-a-defer`
```

### Case 421.2 — The agent only shows a defer, and the hook writes it

> **given:**
> `rule-case-protocol` — the rule of the Case: the short form of a deferred decision
> **＋** `vault/wiki/case-schema.md` — its render
> **＋** `estimate-case-protocol-defers-in-one-reply` — the Estimate of the reply that defers
> **＋** `rule-spec-write` — the hook that writes the deferred Case

> **when:**
> The person asks in the chat to defer an item, in Plan Mode or at Retro.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file or `spec.md`: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** In Plan Mode the reply ends with the Frontier, the line of the item closed `[-] … · defer case N`; at Retro no Frontier is shown.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: in the same reply the agent appends it under the `## Deferred` heading of the plan file, or of `raw/<date>/<hi HHMM>/spec.md` at Retro, shows it, and ends the reply with its ledger line
    new: in the same reply the agent shows it and carries its ledger line, and the `Stop` hook of `rule-spec-write` writes it under the `## Deferred` heading of the plan file, or of `raw/<date>/<hi HHMM>/spec.md` at Retro — the agent writes none of it (case 421.2)
  - old: It stands there before its ledger line, one line per target,
    new: It stands there with one item per target,
  change: the deferred Case is shown by the agent and written by the hook of rule-spec-write (case 421.2)
- slug: estimate-case-protocol-defers-in-one-reply
  set:
    status: pending
  change: the Criterion replaced whole — the agent shows the defer, the hook writes it (case 421.2)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `estimate-case-protocol-defers-in-one-reply`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-defers-in-one-reply`
```

### Case 421.3 — Pre-spec accepts the closer `kept`

> **given:**
> `rule-prespec` — the rule of pre-spec: its Render lists the closers of a Frontier line
> **＋** `.claude/skills/pre-spec/SKILL.md` — its render
> **＋** `guppi/prespec.py` — `CLOSERS` and `check_frontier`
> **＋** `tests/test_prespec.py` — its tests
> **＋** `estimate-prespec-checks-the-frontier` — the Estimate of the Frontier check
> **＋** `vault/raw/<date>/<HHMM>/frontier.md` — the Frontier of the session

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`.

> **then:**
> A missing file is the finding `frontier: <path> is missing`.
> **＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `sprint`, `kept`, `defer case N` is a finding.
> **＋** A line closed `case N` with no heading of Case N in the plan is a finding; one closed `defer case N` with no `defer` item under Case N is a finding.
> **＋** A line closed `[x]` with `sprint` is a finding.
> **＋** A line closed `kept` is clean only on a `[-]` box whose source segment, the one before the closer, is `deferred`; on an `[x]` box or after another source it is a finding.

```then
update:
- slug: rule-prespec
  replace:
  - old: '`[-] … · sprint` is clean, a sprint item left for a later session, no Case and no `defer` needed (case 310.6),'
    new: '`[-] … · sprint` is clean, a sprint item left for a later session, no Case and no `defer` needed (case 310.6), `[-] … · deferred · kept` is clean, an item of the brief''s Deferred list left as it stands, and `kept` on an `[x]` box or after another source is a finding (case 421.3),'
  change: the closer kept, clean on [-] after the source deferred (case 421.3)
- slug: estimate-prespec-checks-the-frontier
  set:
    status: pending
  change: the Criterion replaced whole — the closer kept (case 421.3)
```

```tasks
- [x] update `rule-prespec`
- [x] update `estimate-prespec-checks-the-frontier`
- [x] `guppi/prespec.py`: `kept` among the `CLOSERS` of `check_frontier`, and the finding that names the closers
- [x] `tests/test_prespec.py`: `-k frontier` — `kept` clean on `[-]` after `deferred`, a finding on `[x]` and after another source
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-checks-the-frontier`
```

### Case 421.4 — A deferred item left unchanged closes `kept`, with no decision

> **given:**
> `rule-skill-hi` — the rule of `/hi`: the closers of a Frontier line
> **＋** `.claude/skills/hi/SKILL.md` — its render
> **＋** `rule-case-protocol` — the rule of the Case: the closers of Plan Mode and the short form
> **＋** `vault/wiki/case-schema.md` — its render
> **＋** `estimate-hi-writes-frontier` — the Estimate of the Frontier `/hi` writes
> **＋** `rule-brief` — the brief, whose Deferred list carries an item no `supersedes` retired
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session

> **when:**
> The person invokes `/hi`, the agent assembles the Frontier, and its lines are closed in Plan Mode.

> **then:**
> The Frontier, written to `raw/<date>/<hi HHMM>/frontier.md`, is two lists: `## Cases`, lines `- [ ] C<n> — <title> · <source>`, and `## Work`, lines `- [ ] W<n> — <title> · <source>`; an item of the current milestone is a line of its own whose title opens with the slug of each of its pages in a code span; a line closes by appending the closer and keeping the source — `[x] … · case N`, `[x] … · work`, `[-] … · defer case N`, `[-] … · sprint` for a line of the sprint page left for a later session, and `[-] … · deferred · kept` for an item of the brief's Deferred list left deferred as it stands; a line of the sprint never closes `· defer case N`.
> **＋** An item closed `kept` has no short Case and no ledger line; its page keeps its `deferred_by`, and the brief carries the item on.
> **＋** The kind comes from the source. Cases: on a plan branch the unfinished plan, first; the items of the current milestone of `sprint.md`; the `Cases` list of the brief's Next session; the brief's Deferred list, source `deferred`; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`.
> **＋** The milestone is the current one only; a later one, the Backlog and Closed are not items; a decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a list with their detail — the agenda of Plan Mode; the Work as one block; sub-cases are cut in Cases only.
> **＋** A `W` that turns out to need a decision closes `· case N`; a `C` that needs none closes `· work`.
> **－** `Pull:` and `Open issues:` are a Cases item only when `sprint.md` names no decision on them.
> **－** Pre-spec finds an open line under `## Cases`; a `W` line stands open until its work is done and closes `· work` in Work Mode.
> **＋** Claude Code's plan mode is on at `/hi`; the agent writes `frontier.md` and closes its lines all the same, with no refusal in the chat.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: (case 310.5), never `· defer case N` (case 356.2);
    new: (case 310.5), never `· defer case N` (case 356.2); `[-] … · deferred · kept` when an item of the brief's Deferred list, source `deferred`, is left deferred as it stands — no Case, no ledger line, the brief carries it on (case 421.4);
  change: the closer kept for a deferred item left as it stands (case 421.4)
- slug: rule-case-protocol
  replace:
  - old: '`[-] … · sprint` for an item of the sprint left for later — never `· defer case N` (case 356.2).'
    new: '`[-] … · sprint` for an item of the sprint left for later — never `· defer case N` (case 356.2) — and `[-] … · deferred · kept` for an item of the brief''s Deferred list left as it stands (case 421.4).'
  - old: A page-less Slice task goes to `sprint.md`, not into a defer.
    new: 'A page-less Slice task goes to `sprint.md`, not into a defer. An item of the brief''s Deferred list left as it stands is no decision: no short Case, no ledger line; its Frontier line closes `[-] … · deferred · kept`, the page keeps its `deferred_by`, and the brief carries the item on (case 421.4).'
  change: an item left deferred as it stands is no decision, closed kept (case 421.4)
- slug: estimate-hi-writes-frontier
  set:
    status: pending
  change: the Criterion replaced whole — the closer kept; the old Given dropped (case 421.4)
```

```tasks
- [x] update `rule-skill-hi`
- [x] update `rule-case-protocol`
- [x] update `estimate-hi-writes-frontier`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-hi-writes-frontier`
```

## Deferred

## Case 422 — The limit of 400 000 tokens, again

> **context:**
> Cases 404, 409 and 418 deferred the limit of 400 000 tokens in `guppi/context.py` and the text of the `UserPromptSubmit` hook past it. No session has reached the limit yet. This session puts every item that needs a decision after the new scheme of Cases of Cases 419–421.

> **problem:**
> Which limit is right, and what the hook says past it: decided once a session reaches it.

```then
defer:
  - slug: rule-context-size
    type: rule
    purpose: The limit of 400 000 tokens in guppi/context.py, and the text of the UserPromptSubmit hook past it; judged once a session reaches it
```

## Case 423 — The plan written by hooks alone, and when the prose is translated

> **context:**
> Case 416 deferred a guard on the plan and the time of the translation; Case 419 superseded 416 and took only the core of its scheme, so the defer falls. After Cases 419 and 421 the hooks write every Case into the plan, a defer included, and the agent edits the plan only to translate the name, `context` and `problem` before the approval, which `rule-spec-reconcile` watches. This session puts every item that needs a decision after the new scheme of Cases.

> **problem:**
> Whether a guard refuses every edit of the plan by the agent while a line under `## Cases` of the Frontier is open, and when and how the prose of a Case is translated (the question of case 410).

```then
defer:
  - slug: rule-spec-reconcile
    type: rule
    purpose: A guard that refuses the agent's edits of the plan while a line under Cases of the Frontier is open; when and how the prose of a Case is translated (the question of case 410)
```

## Case 424 — The orchestration of the main agent as a rule of its own

> **context:**
> Case 416 deferred the split of `case-schema.md`: the form of a Case read by `case-guppi` only, and the orchestration of the main agent — the triage of a Frontier item, the dispatch, the acknowledging reply, `LEDGER`, defers and the one rule — as a rule of its own loaded by `/hi`. Case 419 superseded 416 and took only the core of its scheme, so the defer falls. The new rule has no page yet; this Spec changes `rule-case-protocol` in Cases 419 and 421, so the defer names the new rule, not that page. This session puts every item that needs a decision after the new scheme of Cases.

> **problem:**
> Whether the orchestration of the main agent leaves `case-schema.md` for a rule of its own loaded by `/hi`, and `case-schema.md` goes to `case-guppi` alone.

```then
defer:
  - slug: rule-orchestration
    type: rule
    purpose: The orchestration of the main agent — the triage of a Frontier item, the dispatch of case-guppi, the acknowledging reply, LEDGER, defers and the one rule — as a rule of its own loaded by /hi, and case-schema.md read by case-guppi alone
```
