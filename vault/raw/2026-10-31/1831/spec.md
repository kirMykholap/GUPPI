<!-- approved 22:32:06 · session 7ac5901f -->

# Session 1831 — the failed readings of Case building and showing

## Case 966 — The builder follows a changed step to the one who carries it out

> **context:**
> When a Case of `case-guppi` changes what a step writes, copies or shows, the Render of `rule-case-build` has it search `vault/wiki/rules/` and `.claude/` for the name of the output and the name of the step, and read each text that reads that output or does the same step (case 924). A word search misses a text that does the same step without its words. At the Retro of session 0431, `estimate-case-build-reads-the-readers-of-a-changed-step` failed: 1 of 11 findings of `ask-guppi` at the `/pre-spec` of session 0128 was Case 952, which changed how step 2 of `/sprint-open` asks the goal of a sprint and missed `.claude/skills/grill-me/SKILL.md`, whose shape every question of a round takes. Its builder searched `goal in one sentence|its goal` over `.claude/` (agent transcript `agent-a52a60ef552b7f46f.jsonl`, line 122) and never read grill-me. The step hands its work on: line 20 of `.claude/skills/sprint-open/SKILL.md` says that `case-guppi` puts each other question to the person, and `.claude/agents/case-guppi.md` loads grill-me by its `skills` field. So the person chose that the builder, beside the word search, follows the step to each agent, skill or hook that carries it out, and to each skill such an agent loads by its `skills` field. The new text and the bracket of its sentence keep the form of a page with `core: true`. The Criterion of the Estimate already promises the result that failed, that each skill that does the same step is read, so the person chose to write it back word for word as this Case's `when` and `then`; its `method` named the `/pre-spec` of session 0128 and now waits for the `/pre-spec` of the first session whose `case-guppi` runs on the new Render, since this session's `/pre-spec` runs on the old one and the Render lands at the render. The sentence on a new member of a list, the object of Frontier item C6, is a promise of its own and stays out of this Case; a graph of the links between pages and files, which the person asked about, is Frontier item C10 and stays out too. A Grep `does the same step|do the same step` over `vault/wiki/` printed `brief.md`, `estimates/estimate-case-build-reads-the-readers-of-a-changed-step.md`, `rules/rule-case-build.md` and `insights/insight-case-build-changes-a-step-without-reading-its-readers.md`, and over `.claude/` printed `agents/case-guppi.md`; the hit in `brief.md` is not read, and the `## Proposal` of the insight, which suggests a Grep of the step's output or of its name, stands, since it is a suggestion that `decision-case-924` already actioned and the word search stays. `.guppi/tests/test_guppi_package.py` reads every file of `.claude/` and the live pages for the old commands `uv run guppi` and `uv run pytest` and the old paths `guppi/` and `tests/`, in `test_no_caller_runs_the_code_or_the_tests_without_the_project` and `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it`; the new text holds none of those four strings. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> A builder that searches only for the words of a changed step misses the skill that carries the step out under other words, so `/pre-spec` finds the miss after the person has ratified the Case.

> **recommend:**
> - **How the builder finds a text that does the same step**
>   - Recommended: (a) follow the step to the agent, skill or hook that carries it out, and to each skill such an agent loads by its `skills` field.
>   - Answer: (a), as recommended.
> - **How the change is checked**
>   - Recommended: (a) keep the Criterion of `estimate-case-build-reads-the-readers-of-a-changed-step` word for word and set it to wait for a new reading, its method waiting for the `/pre-spec` of a session on the new Render.
>   - Answer: (a), as recommended.
> - **Whether this Case also covers Frontier C6**
>   - Recommended: (a) separate Cases; this Case changes only the sentence on the texts that do the same step.
>   - Answer: (a), as recommended; a graph of the links becomes a new Frontier item, with no Case yet.

> **given:**
> `rule-case-build`: its Render, rendered into `.claude/agents/case-guppi.md`, gains the following of a step to the one who carries it out.
> **＋** `estimate-case-build-reads-the-readers-of-a-changed-step`: its `method` changes, and its Criterion is written back word for word.
> **＋** `vault/wiki/rules/` and `.claude/`: the texts the agent searches for the readers of a step.
> **＋** `log.md` and `brief.md`: files whose hits are not read.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: rule-case-build
  replace:
  - old: and for the name of the step, and read each step and skill that reads that output or does the same step, the steps after it in the same text and the new path your Case adds included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in case 924).
    new: and for the name of the step; follow the step too to each agent, skill or hook that carries it out — one the step dispatches, loads, runs or writes a prompt for — and to each skill that such an agent loads by its `skills` field, since a skill that sets the form of every step of its kind, such as the shape of every question of a round, need not hold the words of the step; and read each step and skill that reads that output or does the same step, the steps after it in the same text, the new path your Case adds and each agent, skill and hook the step leads to included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966).
  change: case-guppi follows a changed step to each agent, skill or hook that carries it out, and to each skill such an agent loads, beside the word search
- slug: estimate-case-build-reads-the-readers-of-a-changed-step
  set:
    status: pending
    method: 'by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on following a step to the one who carries it out: the findings of ask-guppi at that /pre-spec, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count and the transcript in the estimate line'
  change: pending again after the failed reading of session 0431, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render that follows a step to the one who carries it out
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] update `estimate-case-build-reads-the-readers-of-a-changed-step`
- [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`
```

## Case 967 — A graph of the links between pages and harness files

> **context:**
> A builder of a Case finds the texts a change touches by searching for words, and it misses a text that does the same work in other words. In session 0128 the builder of Case 952 changed how `/sprint-open` asks the goal of a sprint and never read `.claude/skills/grill-me/SKILL.md`, though the link was written down: `.claude/skills/sprint-open/SKILL.md` names `case-guppi`, and `.claude/agents/case-guppi.md` loads `grill-me` by its `skills` field. Case 966 of this session has the builder follow a changed step to the agent, skill or hook that carries it out; the person asked for a general way that finds every link, so that a missed link is fixed by writing it once (Frontier C10). Nothing of a graph exists today. `links_of` of `.guppi/guppi/lint.py`, read whole, gives the links of a page's `LINK_FIELDS` and each `[[slug]]` of its body outside a code span, History included, and most pages name a page in a code span, so it misses those. The person chose the following. Hand-off links are not written in a new field but read from the names in the rendered files, since `rule-rules-schema` says what a rule reads among the rules follows from `implementation_ref` and `governs` and is never written (case 305). A page body gives a link by each slug it names outside History. The command shows one step, out and in, with a purpose line per neighbour. The check of a link named only in prose is not built, since the reading of names takes its place; this is left not done. The builder could not run the command: it has no Bash, the subagents page of Claude Code (https://code.claude.com/docs/en/sub-agents) says the `tools` field takes whole tools, and the permissions page (https://code.claude.com/docs/en/permissions, Hook approvals in plan mode) says that in plan mode a `PreToolUse` hook's `"allow"` has no effect on a call that is not read-only; so the person chose that a `SessionStart` hook writes the whole graph into `.guppi/links.md` and the builder reads the block of each page it changes by a Grep. The whole graph is built because the links into a page stand only in other texts. Three sub-cases follow, one per promise: the command on a new entity `entity-link-graph` under `entity-guppi` (967.1), the step of the builder on `rule-case-build` (967.2), and the hook on a new rule `rule-link-graph-at-session-start` under `rule-harness` (967.3), since `rule-hook-registry` says a new hook comes in the Case that creates the hook's Rule.
>
> The command takes the text of each rendered file from `render_units`, `fill_placeholders` and `plan` of `.guppi/guppi/render.py`, read whole, which `run` of that file calls over `read_category(..., "rules")`: `plan` returns the text that `guppi render` writes into each file. So the hook need not wait for `render --sync`, which runs on the same event. Which rule renders a file is the judgment of `render_units`: `governed` of `.guppi/guppi/guard.py` and `governed_paths` of `.guppi/guppi/prespec.py`, both read whole, judge which file a page governs, a `check` rule included, and they part on a list in `governs` and on `status: deleted`, so neither is named as the shared judgment. The path fields are `REWORD_PATH_FIELDS` of `.guppi/guppi/generate.py`, `implementation_ref`, `governs` and `code_ref`; `PATH_FIELDS` of `lint.py` leaves out `code_ref`, since it lists the paths lint checks for existence, and stands. A Grep `agents/|skills/|"agents"|"skills"` over `.guppi/guppi/` printed `ship.py`, `render.py` and `recall.py`, none a judgment of the name of an agent or a skill in a text, so the new reading of names is no second copy; a Grep `"root_cause"|"pattern"` over `.guppi/guppi/` printed `event.py`, `generate.py` and `materialize.py`, none a map of the field that gives the index line of a category, which the recipe of `.claude/agents/ask-guppi.md` sets in text. The command reads no Decision page, as `rule-search-leaves-out-decisions` sets. `entity-link-graph` and `rule-link-graph-at-session-start` carry `core: true`, since `rule-case-build` and `rule-hook-registry` carry it and their new texts name the file and the hook; `core` is written as one code span `true`, the form that Case 968 of this session sets, and by Case 968 the librarian's run loads it as the boolean true, though this session's `/pre-spec` reads both pages as not core. Case 969.3 archives `estimate-guppi-keeps-no-defer-of-its-shape` of `entity-guppi`, and the pair of 967.1 changes only the Purpose and the `purpose` of that page, so the two do not clash. A Grep `guppi links|"links"` over the repository, `decisions/`, `raw/` and `archive/` left out, printed nothing, and a Glob `vault/**/*{link-graph,reads-the-link-graph}*.md` printed nothing, so the command name and the new slugs are free. The Enforcement paragraph of `vault/wiki/rules/schema.yaml`, the Render of `rule-rules-schema`, says that in the harness a thing is a Rule when its code is a guard that refuses a case, and the new hook refuses nothing, since a `SessionStart` hook cannot block (`lesson-hooks-sessionstart-cannot-block`); the page is still a Rule, as the person chose, since `rule-hook-registry` registers a new hook only with the hook's Rule, and the vault already keeps a hook that writes a file as a Rule with `enforcement: hook`, `rule-librarian-report-copy`, whose purpose is that the librarian's report stands in a file; the sentence of the schema stands, and the gap between it and those pages is left to a later Case. Two Estimates of `rule-case-build` speak of the frame and stand: the Criterion of `estimate-case-build-writes-the-case` promises the reading of each page and file that `given` names, which still holds, and the reading of the graph is a promise of its own in 967.2; the Criterion of `estimate-case-build-reads-by-need-and-in-parts` sets which texts are read whole and which in parts, and the new sentence opens a neighbour by that same rule, so it adds no kind of text. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> A builder that searches only for words misses a text that is linked to the change but holds none of its words, because no command shows the links of a page or a file in one place, out and in.

> **recommend:**
> - **How much this Case covers**
>   - Recommended: (a) one Case with a sub-case for each part.
>   - Answer: (a), as recommended.
> - **Where a hand-off link comes from**
>   - Recommended: (b) derived from the names in the rendered files, with no new field.
>   - Answer: (b), as recommended.
> - **Which page describes the command**
>   - Recommended: (a) a new entity, `entity-link-graph`, under `entity-guppi`.
>   - Answer: (a), as recommended.
> - **How far the command looks**
>   - Recommended: (a) one step in both directions.
>   - Answer: (a), as recommended.
> - **What becomes of the check of prose names**
>   - Recommended: (a) no check in this Case; it is reported as not done.
>   - Answer: (a), as recommended.
> - **Which texts give a link by a name**
>   - Recommended: (b) the rendered harness files and the body of each page outside its History.
>   - Answer: (b), as recommended.
> - **Where the step of `case-guppi` stands**
>   - Recommended: (a) in the paragraph on the frame, for each page and file the Case changes.
>   - Answer: (a), as recommended.
> - **How the command is checked**
>   - Recommended: (a) a new Estimate on `entity-link-graph`, with a test and a live run.
>   - Answer: (a), as recommended.
> - **How the step of `case-guppi` is checked**
>   - Recommended: (a) a new Estimate on `rule-case-build`.
>   - Answer: (a), as recommended.
> - **How `case-guppi` gets the output of the command**
>   - Recommended: (b) a hook at the start of each session writes the whole graph into a file, and the builder reads that file; (a), Bash with a hook in the header, was not recommended, since the documentation does not confirm that its call runs in Plan Mode without a prompt.
>   - Answer: (b); the person first chose (a), then (b) when asked again, asked why the graph covers all pages, and kept (b) after the answer that the builder reads only the blocks of what its Case changes.
> - **Which page describes the hook that writes the graph**
>   - Recommended: (a) a new rule, `rule-link-graph-at-session-start`, under `rule-harness`.
>   - Answer: (a), as recommended.

### Case 967.1 — The command prints the neighbours of a page or a file

> **given:**
> `entity-link-graph`: the new page of the graph and its command.
> **＋** `entity-guppi`: its parts gain the graph.
> **＋** `estimate-link-graph-prints-the-neighbours`: the new check of the output.
> **＋** `.guppi/guppi/links.py`: the new module of the command.
> **＋** `.guppi/guppi/cli.py`: the list of commands.
> **＋** `.guppi/guppi/pages.py`: its docstring names the modules that share it.
> **＋** `.guppi/tests/test_links.py`: the new test.
> **＋** `rule-search-leaves-out-decisions`: keeps the text of Decision pages out of every search.
> **＋** `vault/wiki/`: the live pages the command reads.
> **＋** `vault/wiki/decisions/`: the Decision pages the command leaves out.
> **＋** `.guppi/guppi/lint.py`: `links_of`, the reading of the links of a page.
> **＋** `.claude/agents/` and `.claude/skills/`: the agents and skills whose names the command reads.

> **when:**
> `uv run --project .guppi guppi links <slug or path>` runs over the live pages of `vault/wiki/` and the text that `guppi render` writes into each file a rule renders.

> **then:**
> It prints the block of that page or file: a line `## <slug or path>`, its purpose line, then one line per neighbour that says `out` or `in`, the kind of link and the neighbour, with the purpose line of a neighbour that is a page.
> **＋** A page links out by its fields, and by its `[[slug]]` links outside `## History`, as `links_of` of `.guppi/guppi/lint.py` reads them from the page with its History left out, by each path of its `implementation_ref`, `governs` and `code_ref`, and by each slug of a live page that its body names outside `## History`, in a code span or not.
> **＋** A rendered file links out by each name it holds: an agent of `.claude/agents/` anywhere, a skill of `.claude/skills/` after a slash, alone in a code span or in a `skills:` list, and a command of `.guppi/guppi/cli.py` as `guppi <name>`.
> **＋** The name of an agent or a skill links to the page that renders its file, and the name of a command to each page whose `implementation_ref` names its module.
> **＋** Each link out of one page or file is a link into the other, and a file inside a folder that a page names links into that page.
> **＋** The purpose line of a page is its `purpose`, of a lesson its `root_cause` and of an insight its `pattern`.
> **－** It reads no page under `vault/wiki/decisions/` and prints no Decision page as a neighbour.
> **－** A slug or path that is neither a live page nor a file prints one line that says so, and the command exits non-zero.

```then
create:
- slug: entity-link-graph
  ref: entity-guppi
  type: entity
  kind: Leaf
  purpose: The links between the vault pages and the harness files, each written once, and a command that prints the neighbours of a page or a file with their purpose lines
  code_ref:
  - .guppi/guppi/links.py
  - .guppi/tests/test_links.py
  core: 'true'
  tags:
  - harness
  - workflow
  sections:
    Purpose: A builder that searches only for words misses a text that is linked to the change in other words. The graph reads each link where it is written — a field of a page, a `[[slug]]`, a slug named in the body, a path field, and the name of an agent, a skill or a command in a rendered file — and `uv run --project .guppi guppi links <slug or path>` prints the neighbours of one page or file, out and in, each with its purpose line, so the reader opens only the neighbours that bear on its question. A missed link is fixed by writing the name once where it belongs (as set in case 967.1).
- slug: estimate-link-graph-prints-the-neighbours
  ref: entity-link-graph
  kind: QA
  purpose: Whether guppi links prints, for a page or a file, each neighbour out and in with the kind of link and the purpose line, from the fields, the body, the path fields and the names in the rendered files, and no Decision page
  method: 'uv run --project .guppi pytest .guppi/tests/test_links.py, which runs the command over a vault in a temporary folder for each kind of link in both directions; and by hand, in Work Mode of this session: the output of uv run --project .guppi guppi links .claude/skills/sprint-open/SKILL.md, which names case-guppi, and of uv run --project .guppi guppi links .claude/agents/case-guppi.md, which names grill-me, read against the Criterion, the output in the estimate line'
  tags:
  - harness
update:
- slug: entity-guppi
  replace:
  - old: Its parts are the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of the vault that are content, not rules.
    new: Its parts are the sprint as a kind (`entity-sprint`), the glossary (`entity-glossary`) and the graph of the links between the pages and the harness files (`entity-link-graph`), the things of GUPPI that are not rules (as set in case 967.1).
  set:
    purpose: GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint, the glossary and the graph of the links between pages and harness files, and in the repository of GUPPI also that repository on GitHub
  change: the graph of the links between pages and harness files is a part of GUPPI
```

```tasks
- [ ] create `entity-link-graph`
- [ ] update `entity-guppi`
- [ ] create `estimate-link-graph-prints-the-neighbours`
- [x] `.guppi/guppi/links.py`: the command `links`, which imports `links_of` of `.guppi/guppi/lint.py` over the page with its `## History` left out, `REWORD_PATH_FIELDS` of `.guppi/guppi/generate.py`, `render_units`, `fill_placeholders` and `plan` of `.guppi/guppi/render.py`, `key` and `relative` of `.guppi/guppi/guard.py`, and `COMMANDS` of `.guppi/guppi/cli.py` inside the function that reads the names of commands, since `cli.py` imports the module.
- [x] `.guppi/guppi/cli.py`: `COMMANDS` holds `links`.
- [x] `.guppi/guppi/pages.py`: its docstring names `links` among the modules that share it.
- [x] `.guppi/tests/test_links.py`: the test of each line of the Criterion over a vault in a temporary folder.
- [ ] read `estimate-link-graph-prints-the-neighbours`
```

### Case 967.2 — The builder reads the links of what its Case changes

> **given:**
> `rule-case-build`: its Render, rendered into `.claude/agents/case-guppi.md`, gains the reading of the graph in the paragraph on the frame.
> **＋** `estimate-case-build-reads-the-link-graph-of-what-it-changes`: the new check of that reading.
> **＋** `.guppi/links.md`: the graph that the hook of `rule-link-graph-at-session-start` writes.
> **＋** `vault/raw/2026-10-31/1831/cases/case-966.md`: the Case that changes another paragraph of the same Render.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case it builds, before it answers with its summary.

> **then:**
> For each page and file the Case changes, it finds the block of that page or file in `.guppi/links.md` by a Grep for its line `## <slug or path>` with lines of context.
> **＋** From that block it judges, by what each neighbour is for, which neighbours bear on the change.
> **＋** It opens each neighbour whose purpose line bears on the change, whole or in parts as the Render sets for its kind of text.
> **＋** Each neighbour that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** Where `.guppi/links.md` is missing or holds no block of that page or file, the `context` of the Case says so.

```then
create:
- slug: estimate-case-build-reads-the-link-graph-of-what-it-changes
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi reads, for each page and file its Case changes, its block in .guppi/links.md, and opens each neighbour whose purpose line bears on the change
  method: 'by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on .guppi/links.md and whose start wrote that file: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether a Grep of .guppi/links.md names each page and file the Case changes and whether each neighbour that bears on the change is opened or named in context; the count and the transcripts in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
update:
- slug: rule-case-build
  replace:
  - old: the hooks registered on the same event in `.claude/settings.json` and the rule of each. When the Case changes the code of a check,
    new: 'the hooks registered on the same event in `.claude/settings.json` and the rule of each. Read too, for each page and file the Case changes, its block in `.guppi/links.md`, the graph of the links between the pages and the harness files that a hook writes at the start of the session: find it by a Grep for its line `## <slug or path>` with lines of context, read the purpose line of each neighbour it names, out and in, and open each neighbour whose purpose line bears on the change, whole or in parts as the paragraph that opens with the reading of `vault/wiki/case-schema.md` sets for its kind of text; each one the change makes false enters the Case, or `context` names it and says why it stands, and where the file is missing or holds no block of that page or file, `context` says so (as set in case 967.2). When the Case changes the code of a check,'
  change: case-guppi reads the block of each page and file its Case changes in the graph of links, and opens each neighbour that bears on the change
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] create `estimate-case-build-reads-the-link-graph-of-what-it-changes`
- [ ] read `estimate-case-build-reads-the-link-graph-of-what-it-changes`
```

### Case 967.3 — A hook writes the graph at the start of each session

> **given:**
> `rule-link-graph-at-session-start`: the new rule of the hook.
> **＋** `.guppi/links.md`: the graph file the hook writes.
> **＋** `rule-hook-registry`: its Render registers the hook on `SessionStart`.
> **＋** `rule-harness`: its Purpose names the hook among the tools of the harness.
> **＋** `estimate-link-graph-at-session-start-writes-the-file`: the new check of the file.
> **＋** `.guppi/guppi/links.py`: the command and its `--write`.
> **＋** `.guppi/.gitignore`: keeps the graph out of git.
> **＋** `.guppi/tests/test_links.py`: the test of `--write`.
> **＋** `.guppi/tests/test_guppi_package.py`: reads `.claude/settings.json` and `.guppi/.gitignore` live.

> **when:**
> Claude Code starts a session in the repository, and the `SessionStart` hook `uv run --project .guppi guppi links --write` runs.

> **then:**
> It writes `.guppi/links.md` whole: one block per live page and per file that a page or a rendered file names, in the form `guppi links` prints.
> **＋** It takes the text of each rendered file as `guppi render` writes it, so its result does not depend on whether `render --sync` on the same event has run.
> **＋** `.guppi/.gitignore` keeps `.guppi/links.md` out of git.
> **－** An error stops no session: the hook prints one line on stderr and exits 0.

```then
create:
- slug: rule-link-graph-at-session-start
  ref: rule-harness
  type: rule
  kind: Leaf
  purpose: Prevents a Case builder from reading a graph of links that is missing or older than the start of its session
  enforcement: hook
  implementation_ref:
  - .guppi/guppi/links.py
  - .guppi/tests/test_links.py
  - .claude/settings.json
  applies_to:
  - entity-link-graph
  core: 'true'
  tags:
  - harness
  - session
  sections:
    Purpose: Prevents a Case builder from reading a graph of links that is missing or older than the start of its session. The builder has no tool that runs a command, so `uv run --project .guppi guppi links --write` runs on `SessionStart` and writes the whole graph into `.guppi/links.md`, which git ignores; the builder reads the block of each page and file its Case changes by a Grep. Pages and rendered files change at the librarian's run, so the file written at the start stays current through the session. The hook takes the text of each rendered file as `guppi render` writes it, and an error prints one line and stops no session (as set in case 967.3).
- slug: estimate-link-graph-at-session-start-writes-the-file
  ref: rule-link-graph-at-session-start
  kind: QA
  purpose: Whether the SessionStart hook writes .guppi/links.md whole at the start of a session, from the text guppi render writes, kept out of git, and stops no session on an error
  method: 'uv run --project .guppi pytest .guppi/tests/test_links.py, which runs guppi links --write over a vault in a temporary folder, a rendered file left unwritten and an error included; and by hand, after the first session start whose .claude/settings.json holds the hook: the time of .guppi/links.md against the session-start line of vault/raw/<date>/event_log.md, its block of .claude/skills/sprint-open/SKILL.md and the output of git status, read against the Criterion, the result in the estimate line'
  tags:
  - harness
  - session
update:
- slug: rule-hook-registry
  replace:
  - old: '{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 } ] },'
    new: '{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 }, { "type": "command", "command": "uv run --project .guppi guppi links --write", "timeout": 60 } ] },'
  change: the SessionStart hook guppi links --write registered
- slug: rule-harness
  replace:
  - old: the hooks that read a page of the vault without its History, and the file under
    new: the hooks that read a page of the vault without its History, the hook that writes the graph of the links between the pages and the harness files at the start of a session, and the file under
  - old: 640, 710.1, 796;
    new: 640, 710.1, 796, 967.3;
  change: the hook that writes the graph of links at the start of a session belongs to the harness
```

```tasks
- [ ] create `rule-link-graph-at-session-start`
- [ ] update `rule-hook-registry`
- [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [ ] update `rule-harness`
- [ ] create `estimate-link-graph-at-session-start-writes-the-file`
- [x] `.guppi/guppi/links.py`: `--write` writes every block into `.guppi/links.md`, prints one line on stderr on an error and exits 0.
- [x] `.guppi/.gitignore`: a line `links.md` after `.venv/`.
- [x] `.guppi/tests/test_links.py`: the test of `--write` over a vault in a temporary folder.
- [ ] read `estimate-link-graph-at-session-start-writes-the-file`
```

## Case 968 — A value of a new page that is not text reaches the page as its value

> **context:**
> When a Case creates a page, each field of the new page is a sub-point of its `create` line, one code span or a fenced block. `put` of `.guppi/guppi/ratified.py`, read whole with `code_value`, `fenced_value` and `read_tasks`, loads a value as YAML only under `set` or when it opens with `[` or `{`, so every other value reaches the Spec as text. `core` written as `true` therefore reaches the Spec as the text "true", and `create_fields` and `_lift_item` of `.guppi/guppi/materialize.py`, read whole, copy it onto the page unchanged; `core_as_left` of `.guppi/guppi/prespec.py`, read whole, answers false for it, since it asks `is True`, and `check_schema` of `.guppi/guppi/lint.py`, read whole, reports it only after the page stands. Session 0431 met this in Case 956.1, which wrote `core` as a fenced `true`, and Case 965 set `core` again by an `update` with `set`; the lesson `lesson-spec-write-lifts-a-create-value-as-a-string` records it, and also that `case-schema.md` gives no form for such a value. The defect is live in this session: Case 967.1 and Case 967.3 create `entity-link-graph` and `rule-link-graph-at-session-start` with `core` written as `true`, so by `put` their `then` blocks hold it as text. The schemas of `vault/wiki/rules/`, `vault/wiki/entities/` and `vault/wiki/estimates/` give `core` the one allowed value `true`; on disk today it is the only field whose allowed values hold no text. Case 969.1 adds to the schema of Estimates, at the render, the field `once` with the one allowed value `true`, and the same reading takes it then; its lint finding asks whether `once` is `True`, which is the value this reading gives. The person chose one function in `materialize.py` that loads a value as YAML for a field whose allowed values in the schema on disk hold no text, which the hook, the lift and `/pre-spec` import; so the two pages of Case 967 come right at the librarian's run, which runs after the code of this session changes, and Case 967 needs no change. A value that reads as none of the allowed values is refused by the hook, and the check of the Case file, which builds the Spec section by `case_section` and `read_tasks` of `ratified.py`, reports it at the build. The allowed values are read from the schema on disk also in a session that changes the schema rule of the category. A Grep `"values"` over `.guppi/guppi/` printed `lint.py` alone: `check_schema` already judges whether a value is one of the allowed values, by `str(value) in [str(a) for a in allowed]`, so that comparison moves into `materialize.py` and both sides import it; with it a value `1` is refused as lint refuses it, though Python takes `1 in [True]` as true. The PyYAML documentation (https://pyyaml.org/wiki/PyYAMLDocumentation) shows `true`, `false`, `on` and `off` loading as booleans. `case-schema.md` gains the form in the sentence of the `## Language` section of `rule-case-protocol` that opens with "The Spec keeps its form", read whole: it names how the hook of `rule-spec-write` reads the chat form of `tasks` — a task line that is an item, its sub-points its keys, the fields of a `create` among them, each value one code span or a fenced block — then the task line `tag`, and ends with a Case off this form not written; the pair adds after the fenced block how a value that is not text is read, and nothing else of the sentence changes. Case 969.1 also writes into that page, a sentence on a one-time Estimate after the one that ends "up to the session that closes it (case 772.4)." in `## The then block lives in the Spec`; the two pairs touch other sentences in other sections, and their new texts do not contradict each other. That `update` of a Render touches no Estimate of the live reading. `estimate-spec-write-copies-the-ratified-case` promises that each value is one code span or a fenced block, which stands, and `estimate-materialize-lifts-a-create-by-the-schema` promises which keys reach the page, which stands; neither speaks of the type of a value, so a new Estimate on `rule-materialize` checks the change. A Grep `core` over `vault/wiki/case-example.md` printed nothing, so `.guppi/tests/test_case_schema.py`, which runs the check of a Case file over that live example with the live schemas, stands; `.guppi/tests/test_schemas.py` reads the live schemas through `check_schema`, whose comparison moves unchanged, and stands. `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`, `passed`, on `rule-prespec-hook`, judges the new text of an item for a page that carries `core: true` "as the plan leaves it", and of an Estimate whose target does so, by `core_as_left` and `core_target` of `prespec.py`, read whole; its Criterion stands, since with this change a `create` that writes `core` as `true` is a page that carries `core: true` as the plan leaves it, which is what its words already promise, and the test of the new Estimate runs `core_as_left` over that value. This session's `/pre-spec` runs on the code as it stands before Work Mode, so it reads the `create` items of `entity-link-graph` and `rule-link-graph-at-session-start` as not core and does not judge their new texts, or those of their Estimates, for a pointer outside a bracket; that gap is a note for the handoff by `rule-retro`, and it closes for later sessions with this change. The finished file of Case 967, read whole after its build again ended, still creates both pages with `core` written as `true` and sets it by no `update`, so the claims on it hold. The lesson stands in the ledger of session 0431, and the ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> A field of a new page whose allowed value is not text, such as `core: true`, reaches the Spec and the page as text, so the page is born without that value, and `case-schema.md` gives no form that avoids it.

> **recommend:**
> - **Where the boolean of a `create` is fixed**
>   - Recommended: (c) one shared function, which the copy hook, the librarian's lift and `/pre-spec` import, loads a value as YAML for a field whose allowed values in the schema hold no text.
>   - Answer: (c), as recommended.
> - **What happens to a value outside the allowed list**
>   - Recommended: (a) the hook refuses it with a line that names the field and its allowed values.
>   - Answer: (a), as recommended.
> - **When the session also changes a page schema**
>   - Recommended: (a) the allowed values are still read from the schema on disk.
>   - Answer: (a), as recommended.
> - **Whether `case-schema.md` describes the form**
>   - Recommended: (a) one sentence in the Render of `rule-case-protocol`.
>   - Answer: (a), as recommended.
> - **How the change is checked**
>   - Recommended: (a) a new Estimate on `rule-materialize`.
>   - Answer: (a), as recommended.

> **given:**
> `.guppi/guppi/materialize.py`: the shared reading of a value and the lift of a `create`.
> **＋** `.guppi/guppi/ratified.py`: `put` and `read_tasks`, the reading of the `Stop` hook and of the check of a Case file.
> **＋** `/pre-spec`, by `core_as_left` of `.guppi/guppi/prespec.py`, and `check_schema` of `.guppi/guppi/lint.py`: the other readers of the value.
> **＋** `vault/wiki/<category>/schema.yaml`: the allowed values of each field.
> **＋** `rule-case-protocol`: its Render, `vault/wiki/case-schema.md`, gains the form of such a value.
> **＋** `estimate-materialize-lifts-a-create-value-by-the-schema`: the new check, on `rule-materialize`.
> **＋** `.guppi/tests/test_materialize.py`: the test of the readers over the same input.
> **＋** `rule-one-judgment-one-implementation`: one judgment lives in one function.

> **when:**
> The `Stop` hook or the check of a Case file reads a sub-point of a `create` item by `read_tasks` of `.guppi/guppi/ratified.py`.
> **＋** `uv run --project .guppi guppi materialize` lifts a `create` item from the `then` block of the Spec.
> **＋** `/pre-spec` judges by `core_as_left` of `.guppi/guppi/prespec.py` whether the page of a `create` carries `core: true`.

> **then:**
> A value of a field whose allowed values in `vault/wiki/<category>/schema.yaml` on disk hold no text, written as one code span or a fenced block, is loaded as YAML, so `true` reaches the `then` block, the page and `core_as_left` as the boolean true.
> **＋** The three readers load the value by one function of `.guppi/guppi/materialize.py`, and whether a value is one of the allowed values is one function of that module, which `check_schema` of `.guppi/guppi/lint.py` imports.
> **＋** A value that loads as none of the allowed values is refused by the hook: exit 2 with `` `<key>`: <value> is not one of <allowed values> `` on stderr, and nothing of the Case is written; the check of a Case file reports the same line as a finding.
> **＋** The allowed values are read from the schema on disk also when the session creates or updates the schema rule of that category.
> **－** A value of a field whose allowed values hold text, or for which the schema names no allowed values, stays text as before.
> **－** `uv run --project .guppi guppi materialize` and `core_as_left` refuse nothing: a value outside the list that reaches them stays as it loads, and `check_schema` reports it on the page.

```then
create:
- slug: estimate-materialize-lifts-a-create-value-by-the-schema
  ref: rule-materialize
  kind: QA
  purpose: Whether a field of a create whose allowed values in the schema hold no text, such as core, reaches the then block, the page and pre-spec as its value by one function, and whether a value outside the list is refused by the hook
  method: 'uv run --project .guppi pytest .guppi/tests/test_materialize.py, which runs the hook''s reading, the lift and core_as_left over the same values; by hand, after the first librarian''s run that creates a page whose create writes core as true: the core field of that page and the output of uv run --project .guppi guppi lint, read against the Criterion, the result in the estimate line'
  tags:
  - harness
  - schema
update:
- slug: rule-case-protocol
  replace:
  - old: its opening fence longer than any fence of the same character inside it (case 444.3);
    new: its opening fence longer than any fence of the same character inside it (case 444.3); a field whose allowed values in the schema of its category hold no text, such as `core`, takes its YAML value as one code span or a fenced block, such as `true`, and the hook, the lift of `materialize` and `/pre-spec` read it as that value, a value that is none of the allowed values refused (as set in case 968);
  change: the form of a field of a create whose allowed values are not text
```

```tasks
- [x] `.guppi/guppi/materialize.py`: a function that gives the `values` of a category's `schema.yaml` on disk, read also for a category whose schema rule the unit changes; a function that judges whether a value is one of the allowed values, the comparison of `check_schema` moved; and a function that loads a text value as YAML for a field whose allowed values hold no text and gives the value and the refusal line when it is none of them; `_lift_item` lifts each field of a `create` through it.
- [x] `.guppi/guppi/ratified.py`: `put` reads each field of a `create` through that function, with the values of the item's category beside the keys of `key_judge`, returns its refusal, and the docstring of the module says so.
- [x] `.guppi/guppi/prespec.py`: `core_as_left` reads the `core` of a `create` through that function.
- [x] `.guppi/guppi/lint.py`: `check_schema` imports the function that judges whether a value is one of the allowed values.
- [x] `.guppi/tests/test_materialize.py`: one test that runs `read_tasks`, the lift and `core_as_left` over `core` written as a code span `true`, as a fenced `true` and as a value outside the list, and asserts that they read alike; and a test of each line of the Criterion.
- [ ] update `rule-case-protocol`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
- [ ] create `estimate-materialize-lifts-a-create-value-by-the-schema`
- [ ] read `estimate-materialize-lifts-a-create-value-by-the-schema`
```

## Case 969 — A one-time Estimate is marked and stands on the sprint page

> **context:**
> Most Estimates promise a behaviour that lasts. A few check one state of the data once, such as `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` of Case 962, whose `purpose` ends "a one-time check of this data" and which the ledger of this session reads `passed`. Nothing tells the two kinds apart. A one-time check stands on the rule it checks, so `cascade` of `.guppi/guppi/generate.py`, read whole, keeps that rule `draft` while it is `pending`, and `is_draft_core` of `.guppi/guppi/pages.py`, read whole, makes such a rule with `core: true` stop `guppi ship`. Once it passes it stays live after the close, since `Close` of `.guppi/guppi/sprint_close.py`, read with `judge_estimates` and `settled`, moves the sprint page and the Estimates it lists and leaves every other `passed` Estimate. And `ships` of `.guppi/guppi/ship.py`, read whole with `plan`, writes a `passed` Estimate whose target carries `core: true` into the clean version; `rule-backlog` and `entity-guppi` carry it, so both known one-time checks would ship. Case 963 put the question off at session 0431, the person liking both ways the main agent named. Now the person chose both together: a one-time Estimate targets the live sprint page and carries `once: true`, and lint reports one whose target is not a sprint page. The sprint page `entity-sprint-plugin` has no `core: true`, so its Estimates never ship, keep no shipped page `draft` and leave with it at the close; a one-time Estimate still `pending` at the close is read or archived unread, as for every Estimate of the sprint page. The sentence of `entity-sprint` that its Estimates are the Definition of done of a sprint stands: a one-time check is part of that done. Case 969.1 adds the field to `rule-estimates-schema` and a sentence to `rule-case-protocol`, since `case-guppi` reads `case-schema.md` and not the schema of Estimates. The pair on `rule-case-protocol` sits in `## The then block lives in the Spec`, in the paragraph on a `create`, read whole: its `old` ends the sentence that names an Estimate whose target is a sprint page the exception whose `method` may wait for a later session of that sprint, up to the session that closes it, and the new sentence after it names the one-time Estimate that stands on that page; no other Case of this session writes into that paragraph. Its decision line on `rule-estimates-schema` carries `{supersedes:case 963}`, which retires the one defer of that page. The `update` of the Render of `rule-case-protocol` touches no Estimate of the live reading, `estimate-case-protocol-loaded`, and `estimate-case-protocol-case-form` speaks of the form of a Case, not of one-time Estimates, so both stand. The Criterion of `estimate-estimates-schema-checked` lists the optional fields and values, which the field makes false, so it is replaced whole; its `purpose` states the shape of the rendered schema in general and stands, and its `method` is set anew to wait for the librarian's run that renders the schema, since the live file gains `once` only at that render and the new tests of `once` skip before it, so the reading cannot be taken at the Retro of this session. Case 968 changes another sentence of `case-schema.md`, in `## Language`, and reads a `create` value whose allowed values hold no text as YAML from the schema on disk; `once` becomes such a field at the render, and no Case of this session creates an Estimate with `once`, so the order does not matter. The finished file of Case 968, read whole after its build ended, holds these claims: it moves the comparison of `check_schema` with the allowed values into `materialize.py`, which `check_status` does not use, and its own `context` names the sentence of Case 969.1 in `## The then block lives in the Spec` and finds no contradiction. The finished file of Case 967, read whole after its build ended, imports `links_of` of `lint.py` unchanged, writes into neither `rule-estimates-schema` nor `rule-case-protocol`, changes no function of `lint.py`, and creates no Estimate with `once`. Case 969.2 puts the finding into `check_status` of `.guppi/guppi/lint.py`, read whole with `check_schema` and `unmet_conditions`, beside the finding of a target that is no entity or rule. A Grep `SPRINT_PAGE|entity-sprint-` over `.guppi/guppi/` printed `prespec.py`, `generate.py`, `materialize.py`, `sprint_close.py`, `ledger.py`, `lint.py`, `sprint.py` and `backlog.py`; `is_sprint_page` of `ledger.py`, read whole, is the one judgment of a sprint page, which `materialize.py`, `prespec.py` and `sprint.py` import, so lint imports it too, and `ledger.py` imports only `event` and `pages`, so no import loop follows. A Grep `"once"|\bonce:` over `.guppi/guppi/` printed `ledger.py` and `prespec.py`, both in prose, so no code judges the field today. `/pre-spec` does not report a `create` with `once: true` whose `ref` is no sprint page; lint reports it once the page stands, and a check at the plan is not done. Case 969.3 archives the two known one-time Estimates: `estimate-guppi-keeps-no-defer-of-its-shape` stands `passed` on its page, and `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` stands `pending` on its page and `passed` only in the first line of the ledger of this session, a reading not yet applied; a `delete` archives either status; `estimate-cleanup-moves`, `passed`, promises that an archived page moves under the archive and its slug leaves the `estimates` of entities and rules, so it checks the move and its Criterion stands. A Grep of the two slugs over `vault/wiki/`, `.claude/` and `.guppi/` printed `brief.md`, `log.md`, `rules/rule-backlog.md` and `entities/entity-guppi.md`; the hits in `brief.md` and `log.md` are not read, and the two pages lose the slug from `estimates` at the cleanup while their History lines stay. A full pass over the other live Estimates is not done. A Grep `deferred_by, core` over `vault/wiki/`, `.claude/` and `.guppi/guppi/` printed `estimates/schema.yaml`, `rules/rule-estimates-schema.md` and `estimates/estimate-estimates-schema-checked.md`, each changed here; the glossary row `Estimate fields` names `method`, `purpose` and `checked` and no other optional field, and stands. `.guppi/tests/test_schemas.py` reads the live schema: its tests take the first field of `values`, `kind`, so the new field breaks none, and its new test of `once: false` runs only where the live schema lists `once`, so it passes before the render and after it. A Grep `^once:` over `vault/wiki/` printed nothing, so the new finding of lint falls on no live page. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> No Case decides how a one-time Estimate is told apart from one that promises a lasting behaviour, so a one-time check keeps its page `draft` while it waits, stays live after its sprint and ships in the clean version.

> **recommend:**
> - **How a one-time Estimate is told apart**
>   - Recommended: (a) it targets the live sprint page, with no new field.
>   - Answer: (c), both joined: it targets the live sprint page and carries a marker, and lint reports a marked Estimate whose target is not a sprint page.
> - **Whether this Case also sorts the existing Estimates**
>   - Recommended: (b) the two known one-time Estimates are archived too, with no full pass.
>   - Answer: (b), as recommended.
> - **The name of the marker**
>   - Recommended: (a) `once: true`.
>   - Answer: (a), as recommended.
> - **Whether the Case form tells the builder about it**
>   - Recommended: (a) one sentence in `case-schema.md`.
>   - Answer: (a), as recommended.
> - **How the new lint finding is checked**
>   - Recommended: (a) a line added to `estimate-lint-checks-the-statuses`, its Criterion replaced whole.
>   - Answer: (a), as recommended.
> - **How the removal of the two old Estimates is checked**
>   - Recommended: (a) `estimate-cleanup-moves` covers it, with no new Estimate.
>   - Answer: (a), as recommended.

### Case 969.1 — The schema of Estimates holds the field once

> **given:**
> `rule-estimates-schema`: its Render, `vault/wiki/estimates/schema.yaml`, gains the field `once`.
> **＋** `rule-case-protocol`: its Render, `vault/wiki/case-schema.md`, says how a one-time Estimate is created.
> **＋** `estimate-estimates-schema-checked`: its Criterion is replaced whole.
> **＋** `.guppi/tests/test_schemas.py`: the tests of the live schemas.
> **＋** `rule-sprint-close`: the close archives the sprint page with its Estimates.
> **＋** `vault/raw/2026-10-31/1831/cases/case-968.md`: the Case that changes another sentence of `case-schema.md`.

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked, deferred_by, core, once`; values `kind: QA | Research`, `status: pending | passed | failed`, `core: true`, `once: true`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
> **＋** An Estimate page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** An Estimate page in the shape with `once: true` has no `schema` finding, and one with any other value of `once` has one finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` and `once` among them; the description of `once` says that a one-time Estimate targets the live sprint page and that lint reports one whose target is not a sprint page; the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds, among its paragraphs, the introduction, the sentence on a one-time Estimate, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
> **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

```then
update:
- slug: rule-estimates-schema
  replace:
  - old: '`target` names an Entity or a Rule; lint reports any other category (case 53.1).'
    new: '`target` names an Entity or a Rule; lint reports any other category (case 53.1). An Estimate that checks one state of the data once, rather than a behaviour that lasts, targets the live sprint page and carries `once: true`: it leaves with the sprint page at the close, keeps no page with `core: true` in `draft` and is not written into the clean version, and lint reports one whose target is not a sprint page (as set in case 969.1).'
  - old: 'optional: [purpose, checked, deferred_by, core]'
    new: 'optional: [purpose, checked, deferred_by, core, once]'
  - old: 'core: [true]'
    new: |-
      core: [true]
          once: [true]
  - old: no Estimate of the repository that builds that version carries it (cases 804, 822).
    new: |-
      no Estimate of the repository that builds that version carries it (cases 804, 822).
        once: |
          optional; `true`. It marks a one-time Estimate: one that checks one state of the data once, such as the lines of a file after a run, rather than a behaviour that lasts. Its `target` is the live sprint page `entity-sprint-<id>`, so it leaves with that page at the close of the sprint, keeps no page with `core: true` in `draft` and is never written into the clean version; lint reports an Estimate with `once: true` whose `target` is not a sprint page (as set in case 969.1).
  change: the field once marks a one-time Estimate, which targets the live sprint page; the defer of case 963 retired
- slug: rule-case-protocol
  replace:
  - old: up to the session that closes it (case 772.4).
    new: 'up to the session that closes it (case 772.4). An Estimate that checks one state of the data once, rather than a behaviour that lasts, targets the live sprint page and carries `once: true`, so it leaves with that page at the close, keeps no page with `core: true` in `draft` and does not ship; lint reports one with `once: true` whose target is not a sprint page (as set in case 969.1).'
  change: 'a one-time Estimate is created on the live sprint page with once: true'
- slug: estimate-estimates-schema-checked
  set:
    status: pending
    method: 'by hand, after the librarian''s run that renders vault/wiki/estimates/schema.yaml from the Render of rule-estimates-schema that holds the field once: the output of uv run --project .guppi pytest .guppi/tests/test_schemas.py -k estimate over that live file, the tests of once among them, and the output of uv run --project .guppi guppi check, no schema finding on wiki/estimates/, read against the Criterion, both outputs in the estimate line'
  change: the Criterion replaced whole — the optional field once with its one value true; the method waits for the render of the schema
```

```tasks
- [ ] update `rule-estimates-schema`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/estimates/schema.yaml`
- [ ] update `rule-case-protocol`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
- [ ] update `estimate-estimates-schema-checked`
- [x] `.guppi/tests/test_schemas.py`: a test that an Estimate page in the shape with `once: true` has no finding, and a test that one with `once: false` has one finding, run only where the live schema lists `once` among its values, so that it passes before the render and after it; a Case of a later session removes that condition.
- [ ] read `estimate-estimates-schema-checked`
```

### Case 969.2 — Lint reports a one-time Estimate off the sprint page

> **given:**
> `.guppi/guppi/lint.py`: `check_status` and the docstring of the class `status` gain the finding.
> **＋** `.guppi/guppi/ledger.py`: `is_sprint_page`, the one judgment of a sprint page `entity-sprint-<id>`.
> **＋** `.guppi/guppi/pages.py`: `ship_stands` and `is_draft_core`, which other findings of the class read.
> **＋** `vault/wiki/`: the live pages lint reads.
> **＋** `/hi`: a moment a `method` may wait for.
> **＋** `estimate-lint-checks-the-statuses`: its Criterion and `purpose` are replaced.
> **＋** `.guppi/tests/test_lint.py`: the test of the finding.
> **＋** `rule-lint`: the rule of the checks of lint.

> **when:**
> `uv run --project .guppi guppi lint` reads the `status` of the live pages under `vault/wiki/`, and the `method`, the `target` and the `once` of each Estimate.

> **then:**
> `status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged for these two.
> **＋** `status`: where `ship_stands` of `.guppi/guppi/pages.py` finds the module of the command `ship`, each entity or rule that `is_draft_core` accepts, with Estimates or without, one finding each.
> **＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
> **＋** `status`: an Estimate with `once: true` whose `target` is not a sprint page `entity-sprint-<id>`, as `is_sprint_page` of `.guppi/guppi/ledger.py` judges it, one finding.
> **＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
> **＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
> **＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
> **－** `guppi lint` in a project that installed GUPPI reports none of these pages, since `ship_stands` answers no there.
> **－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
> **－** A `failed` Estimate earns its `unread` finding whatever its `method` says.
> **－** An Estimate with `once: true` whose target is a sprint page, and an Estimate without `once`, earn no finding of a one-time Estimate.

```then
update:
- slug: estimate-lint-checks-the-statuses
  set:
    status: pending
    purpose: A status its Estimates do not support, a draft page with core true where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, a one-time Estimate whose target is not a sprint page, and a placeholder are findings of lint
  change: the Criterion replaced whole — a one-time Estimate whose target is not a sprint page is a status finding
```

```tasks
- [x] `.guppi/guppi/lint.py`: `check_status` gives one `status` finding `target <slug> is not a sprint page; once: true marks a one-time Estimate` for an Estimate whose `once` is `True` and whose `target` `is_sprint_page` of `.guppi/guppi/ledger.py`, imported, does not accept; the docstring of the class `status` names the finding.
- [x] `.guppi/tests/test_lint.py`: a test of the finding over a vault in a temporary folder: an Estimate with `once: true` on a rule has one finding, one on a sprint page has none, and one without `once` has none.
- [ ] update `estimate-lint-checks-the-statuses`
- [ ] read `estimate-lint-checks-the-statuses`
```

### Case 969.3 — The two known one-time Estimates leave the live pages

> **given:**
> `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`: a one-time check of `rule-backlog`, archived.
> **＋** `estimate-guppi-keeps-no-defer-of-its-shape`: a one-time check of `entity-guppi`, archived.
> **＋** `rule-backlog` and `entity-guppi`: the pages that list them in `estimates`.
> **＋** `estimate-cleanup-moves`: the check of the move into the archive.
> **＋** `.guppi/guppi/ship.py`: `ships`, which writes a `passed` Estimate into the clean version.
> **＋** `vault/wiki/`: the live pages the run reads and changes.
> **＋** `vault/archive/`: where an archived page moves.

> **when:**
> The librarian's run applies the Spec of this session: `uv run --project .guppi guppi generate`, then `uv run --project .guppi guppi cleanup` over `vault/wiki/`.

> **then:**
> `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` and `estimate-guppi-keeps-no-defer-of-its-shape` stand `archived` and move under `vault/archive/`.
> **＋** Their slugs leave the `estimates` of `rule-backlog` and of `entity-guppi`.
> **＋** `ships` writes neither of them into the clean version.
> **－** The other Estimates of `rule-backlog` and `entity-guppi` stay live with their status.

```then
delete:
- slug: estimate-backlog-keeps-the-work-taken-out-of-a-built-page
  impact: A one-time check of the backlog after Case 962, read passed at the /hi of session 1831; rule-backlog no longer lists it and it does not ship
- slug: estimate-guppi-keeps-no-defer-of-its-shape
  impact: A one-time check of entity-guppi after Case 955, read passed at the /hi of session 0431; entity-guppi no longer lists it and it does not ship
```

```tasks
- [ ] delete `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`
- [ ] delete `estimate-guppi-keeps-no-defer-of-its-shape`
```

## Case 970 — The vault query comes first and runs whole

> **context:**
> Before a Case proposes a `create` without a `ref`, `case-guppi` runs the vault query of `.claude/agents/ask-guppi.md` itself. The recipe of `rule-ask` says to start with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then to run one Grep per other category the question touches. The sentence of `rule-case-build` that sends the builder to the recipe does not say where the query falls among the other searches of a build, so a builder reads "start" as the start of the query alone. At the Retro of session 0431 `estimate-ask-query-before-a-create` failed, as its Result says: in the build of Case 787.1 four Greps of `vault/wiki/` by words came before the rules Grep, and its lessons and insights Greps had words added to their patterns; in the build of Case 804.6 three vault searches came before it and no lessons or insights Grep ran. The Grep and Glob calls of both agent transcripts, read for this Case, show the same: the Globs of the pages the item named came first, then Greps of `vault/wiki/` by words, then the index Greps. The person chose that the sentence of `rule-case-build` sets the moment: the rules Grep is the builder's next Grep of `vault/wiki/` once it sees the `create`, and a Glob or a Read of a page the item names may come before it (970.1). The person chose too that the recipe runs every other category whatever the question, each pattern as written with no word added, for every caller (970.2). This keeps the one recipe for every caller that the Purpose of `rule-ask` sets, and follows its rule to compare meanings, not words, which a word added to a pattern breaks. Lessons and insights hold one index line each, 71 together by a Grep `^(root_cause|pattern):` over `vault/wiki/`, so running both every time costs little. The two parts can fail apart and need different fixes, so by `rule-atomicity` they are separate sub-cases: 970.1 creates `estimate-case-build-runs-the-vault-query-first`, and the recipe change, which the person chose to check by replacing the Criteria of `estimate-ask-query-before-a-create` and `estimate-ask-searches-at-prespec`, is 970.2 for the builder's query and 970.3 for the query at `/pre-spec`, since the check of this file takes one promise per sub-case. The first line of each old Criterion, "starts with the Grep ... then runs one Grep per other category the question touches", is replaced on purpose by the line that runs every category; the other lines are carried word for word. The first `then` line of 970.3 shares most of its words with the first two lines of 970.2, and the overlap stands: `rule-atomicity` sets that the same behaviour checked from two angles is one page and two Estimates, here the one recipe of `rule-ask` read once for the builder and once for `ask-guppi` at `/pre-spec`, each with its own trigger, and each Criterion must read without the other. The new Criterion of `estimate-ask-query-before-a-create` leaves the moment in the build to the new Estimate, so nothing is signed twice. A Grep `question touches|per other category|one Grep per` over `vault/wiki/`, `log.md` and `brief.md` left out, printed `estimates/estimate-ask-query-before-a-create.md`, `rules/rule-ask.md` and `estimates/estimate-ask-searches-at-prespec.md`, and over `.claude/` printed `agents/ask-guppi.md`; each enters the Case. `estimate-case-build-writes-the-case` says that before a `create` without a `ref` the builder runs the query, and `estimate-plan-mode-verified` says it runs the query first; both stand, since the change makes neither false and the moment is the promise of the new Estimate. The other sentences of the Render of `rule-ask` on the searches stand: the confirmation at `/pre-spec` still runs no Grep, and the new sentence names only the runs that make the Grep of the rules. Cases 966 and 967.2 change other paragraphs of the same Render of `rule-case-build`, and 967.2 adds a Grep of `.guppi/links.md`, which is no Grep of `vault/wiki/`, so the anchors and the moments do not clash. A Grep `ask-guppi|case-guppi.md|rule-ask` over `.guppi/tests/` printed `test_casecheck.py` and `test_grepguard.py`, which name `ask-guppi` as an agent type and read neither rendered file. The new texts hold none of the old commands and paths that `.guppi/tests/test_guppi_package.py` looks for. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands. The slug `estimate-case-build-runs-the-vault-query-first` is free: a Glob `vault/**/*runs-the-vault-query*` printed nothing.

> **problem:**
> The builder runs word searches of the vault before the rules Grep of the vault query and may skip the lesson and insight searches, so the query does not check the vault in the order and the scope that the recipe means.

> **recommend:**
> - **When the builder runs the vault query**
>   - Recommended: (a) the first search of the vault once the build sees a `create` without a `ref`, set in the builder's text, `rule-case-build`.
>   - Answer: (a), as recommended.
> - **Which per-kind searches the query always runs**
>   - Recommended: (a) every kind every time, each with its pattern as written, in `rule-ask` for every caller.
>   - Answer: (a), as recommended.
> - **How the two parts are checked**
>   - Recommended: (a) two sub-cases: a new Estimate on `rule-case-build` for the moment, and the Criteria of `estimate-ask-query-before-a-create` and `estimate-ask-searches-at-prespec` replaced for the recipe.
>   - Answer: (a), as recommended.

### Case 970.1 — The rules Grep is the first vault search after the builder sees a create

> **given:**
> `rule-case-build`: its Render, rendered into `.claude/agents/case-guppi.md`, sets when the vault query runs.
> **＋** `estimate-case-build-runs-the-vault-query-first`: the new check of that moment.
> **＋** `.claude/agents/ask-guppi.md`: the recipe of the vault query.
> **＋** `vault/wiki/` and `vault/wiki/rules/`: the folders the builder searches.
> **＋** `vault/raw/2026-10-31/1831/cases/case-966.md`: changes another paragraph of the same Render.
> **＋** `vault/raw/2026-10-31/1831/cases/case-967.md`: 967.2 changes another paragraph of the same Render.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that proposes a `create` without a `ref`.

> **then:**
> Where the item asks for a new page, the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` of the vault query of `.claude/agents/ask-guppi.md` is the first Grep of `vault/wiki/` in the build.
> **＋** Where the person chooses the new page in a round, that Grep is the first Grep of `vault/wiki/` after the answer to that round.
> **－** A Glob or a Read of a page the item names may come before that Grep.

```then
create:
- slug: estimate-case-build-runs-the-vault-query-first
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi makes the Grep of the rules of its vault query its first Grep of vault/wiki/ once it sees that its Case proposes a create without a ref
  method: 'by hand, after the first build of case-guppi on the Render of rule-case-build that holds the sentence on when the vault query runs, whose Case proposes a create without a ref: the Grep, Glob and Read calls of that build, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript and the line numbers in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
update:
- slug: rule-case-build
  replace:
  - old: Before a `create` without a `ref`, run yourself the vault query that `.claude/agents/ask-guppi.md` describes, on the question whether the thing exists, what conflicts, what sits in `draft`, which tags fit and whether the slug is free; its answer goes into `context`.
    new: 'Before a `create` without a `ref`, run yourself the vault query that `.claude/agents/ask-guppi.md` describes, on the question whether the thing exists, what conflicts, what sits in `draft`, which tags fit and whether the slug is free; its answer goes into `context`. Run it as soon as you see that your Case will propose such a `create`: where the item asks for a new page, its Grep of the rules is the first Grep of `vault/wiki/` in your build, and where the person chooses one in a round, it is your first Grep of `vault/wiki/` after the answer to that round; a Glob or a Read of a page the item names may come before it, and no Grep of your own for the thing by its words does (as set in case 970.1).'
  change: case-guppi makes the Grep of the rules of its vault query its first Grep of the vault once it sees a create without a ref
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] create `estimate-case-build-runs-the-vault-query-first`
- [ ] read `estimate-case-build-runs-the-vault-query-first`
```

### Case 970.2 — The vault query runs every index Grep with its pattern as written

> **given:**
> `rule-ask`: its Render, rendered into `.claude/agents/ask-guppi.md`, runs every category whatever the question.
> **＋** `estimate-ask-query-before-a-create`: its Criterion, `purpose` and `method` are replaced.
> **＋** `estimate-case-build-runs-the-vault-query-first`: reads the moment of the query in the build.
> **＋** `.claude/agents/case-guppi.md`: sends the builder to the recipe.
> **＋** `vault/wiki/rules/`, `vault/wiki/entities/`, `vault/wiki/lessons/` and `vault/wiki/insights/`: the folders of the index Greps.
> **＋** `vault/archive/`: searched by slug alone.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The query opens with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs, whatever the question, the Grep `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`.
> **＋** Each of those four Greps takes its pattern as the recipe writes it, with no word added.
> **＋** A page that already holds the thing is found by meaning, whether the person's words name it in the language of the chat or in the language of the repository, and the `context` of the Case names its slug.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
> **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
> **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
> **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.
> **－** Where the query stands among the other searches of the build is outside this promise: `estimate-case-build-runs-the-vault-query-first` reads it.

```then
update:
- slug: rule-ask
  replace:
  - old: 'Then one Grep per other category the question touches: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`.'
    new: 'Then, in each run that makes the Grep of the rules, one Grep for each other category, whatever the question: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`; each of these four Greps takes its pattern as written here, with no word added to it, since you compare meanings, not words (as set in case 970.2).'
  change: the vault query runs the index Grep of every category whatever the question, each pattern as written with no word added
- slug: estimate-ask-query-before-a-create
  set:
    status: pending
    purpose: Whether the vault query that case-guppi runs before a create without a ref, by the recipe of ask-guppi, opens with the rules and runs the index Grep of every other category with its pattern as written, finds an existing page by meaning in either language, and names the rule a proposal crosses and the state of a named slug
    method: 'by hand, after the first build of case-guppi whose Case proposes a create without a ref and that runs on .claude/agents/ask-guppi.md rendered from the Render of rule-ask that runs every category whatever the question: the Grep, Glob and Read calls of that build, read in its agent transcript under ~/.claude/projects/ against the Criterion, and the context of its case file read with them, the transcript and the line numbers in the estimate line'
  change: the Criterion replaced whole — the query opens with the rules and runs every other index Grep with its pattern as written; the moment in the build is read by estimate-case-build-runs-the-vault-query-first
```

```tasks
- [ ] update `rule-ask`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/ask-guppi.md`
- [ ] update `estimate-ask-query-before-a-create`
- [ ] read `estimate-ask-query-before-a-create`
```

### Case 970.3 — At /pre-spec the query runs every index Grep with its pattern as written

> **given:**
> `estimate-ask-searches-at-prespec`: its Criterion, `purpose` and `method` are replaced.
> **＋** `.claude/agents/ask-guppi.md`: the recipe, rendered from `rule-ask` as Case 970.2 changes it.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the questions of `/pre-spec`.
> **＋** `vault/wiki/rules/`, `vault/wiki/entities/`, `vault/wiki/lessons/` and `vault/wiki/insights/`: the folders of the index Greps.
> **＋** `vault/wiki/decisions/`: the Decision pages whose count is not run again.
> **＋** `estimate-search-leaves-out-decisions-by-the-grep-hook` and `estimate-search-leaves-out-decisions-in-every-agent`: read what this promise leaves out.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs, whatever the question, the Grep `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, each with its pattern as the recipe writes it and no word added.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

```then
update:
- slug: estimate-ask-searches-at-prespec
  set:
    status: pending
    purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and runs the index Grep of every other category with its pattern as written, then greps and reads as each finding needs, a count over Decision pages not run again
    method: 'by hand, after the first /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md rendered from the Render of rule-ask that runs every category whatever the question: the Grep, Glob and Read calls of ask-guppi at that /pre-spec, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript in the estimate line'
  change: the Criterion replaced whole — at /pre-spec too the agent runs the index Grep of every category with its pattern as written
```

```tasks
- [ ] update `estimate-ask-searches-at-prespec`
- [ ] read `estimate-ask-searches-at-prespec`
```

## Deferred

## Case 971 — The failed readings of showing, dispatch, list members and the report put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1831. Four of them are Estimates that failed at the Retro of session 0431 or at the /hi before it: `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-case-build-reads-each-list-of-a-new-member` and `estimate-close-reports-the-run`. No Case of this session changes the text whose miss each reading found.

> **problem:**
> No Case of this session fixes the cause of these four failed readings.

```then
defer:
  - slug: estimate-orchestration-shows-the-built-case
    type: estimate
    purpose: "A built Case was shown from an answer of case-guppi whose first line was not **Built:**; put off at the close of Plan Mode of session 1831"
  - slug: estimate-orchestration-names-related-cases-in-the-dispatch
    type: estimate
    purpose: "The sentence on a related Case in a dispatch named its new Estimate and not the pages it changes; put off at the close of Plan Mode of session 1831"
  - slug: estimate-case-build-reads-each-list-of-a-new-member
    type: estimate
    purpose: "A builder ran no search for a member already in a list and missed the docstring list of .guppi/guppi/cli.py; put off at the close of Plan Mode of session 1831"
  - slug: estimate-close-reports-the-run
    type: estimate
    purpose: "No report.md of session 0128 stood after the librarian's run; the page stands pending after Case 956.2; put off at the close of Plan Mode of session 1831"
```
