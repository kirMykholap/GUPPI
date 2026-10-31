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

> **tasks:**
> - [ ] create `entity-link-graph`
>   - ref: `entity-guppi`
>   - type: `entity`
>   - kind: `Leaf`
>   - purpose: `The links between the vault pages and the harness files, each written once, and a command that prints the neighbours of a page or a file with their purpose lines`
>   - code_ref: `[.guppi/guppi/links.py, .guppi/tests/test_links.py]`
>   - core: `true`
>   - tags: `[harness, workflow]`
>   - sections.Purpose: `` A builder that searches only for words misses a text that is linked to the change in other words. The graph reads each link where it is written — a field of a page, a `[[slug]]`, a slug named in the body, a path field, and the name of an agent, a skill or a command in a rendered file — and `uv run --project .guppi guppi links <slug or path>` prints the neighbours of one page or file, out and in, each with its purpose line, so the reader opens only the neighbours that bear on its question. A missed link is fixed by writing the name once where it belongs (as set in case 967.1). ``
> - [ ] update `entity-guppi`
>   - old: `` Its parts are the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of the vault that are content, not rules. ``
>   - new: `` Its parts are the sprint as a kind (`entity-sprint`), the glossary (`entity-glossary`) and the graph of the links between the pages and the harness files (`entity-link-graph`), the things of GUPPI that are not rules (as set in case 967.1). ``
>   - set:
>     ```
>     purpose: "GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint, the glossary and the graph of the links between pages and harness files, and in the repository of GUPPI also that repository on GitHub"
>     ```
>   - change: `the graph of the links between pages and harness files is a part of GUPPI`
> - [ ] create `estimate-link-graph-prints-the-neighbours`
>   - ref: `entity-link-graph`
>   - kind: `QA`
>   - purpose: `Whether guppi links prints, for a page or a file, each neighbour out and in with the kind of link and the purpose line, from the fields, the body, the path fields and the names in the rendered files, and no Decision page`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_links.py, which runs the command over a vault in a temporary folder for each kind of link in both directions; and by hand, in Work Mode of this session: the output of uv run --project .guppi guppi links .claude/skills/sprint-open/SKILL.md, which names case-guppi, and of uv run --project .guppi guppi links .claude/agents/case-guppi.md, which names grill-me, read against the Criterion, the output in the estimate line`
>   - tags: `[harness]`
> - [ ] `.guppi/guppi/links.py`: the command `links`, which imports `links_of` of `.guppi/guppi/lint.py` over the page with its `## History` left out, `REWORD_PATH_FIELDS` of `.guppi/guppi/generate.py`, `render_units`, `fill_placeholders` and `plan` of `.guppi/guppi/render.py`, `key` and `relative` of `.guppi/guppi/guard.py`, and `COMMANDS` of `.guppi/guppi/cli.py` inside the function that reads the names of commands, since `cli.py` imports the module.
> - [ ] `.guppi/guppi/cli.py`: `COMMANDS` holds `links`.
> - [ ] `.guppi/guppi/pages.py`: its docstring names `links` among the modules that share it.
> - [ ] `.guppi/tests/test_links.py`: the test of each line of the Criterion over a vault in a temporary folder.
> - [ ] read `estimate-link-graph-prints-the-neighbours`

> **ratification:**
> ```
> - decision[case 967.1][create][entity-link-graph]{ref:entity-guppi}{tags:harness,workflow}
> - decision[case 967.1][update][entity-guppi]{ref:entity-guppi}
> - decision[case 967.1][create][estimate-link-graph-prints-the-neighbours]{ref:entity-link-graph}{tags:harness}
> ```

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

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` the hooks registered on the same event in `.claude/settings.json` and the rule of each. When the Case changes the code of a check, ``
>   - new: `` the hooks registered on the same event in `.claude/settings.json` and the rule of each. Read too, for each page and file the Case changes, its block in `.guppi/links.md`, the graph of the links between the pages and the harness files that a hook writes at the start of the session: find it by a Grep for its line `## <slug or path>` with lines of context, read the purpose line of each neighbour it names, out and in, and open each neighbour whose purpose line bears on the change, whole or in parts as the paragraph that opens with the reading of `vault/wiki/case-schema.md` sets for its kind of text; each one the change makes false enters the Case, or `context` names it and says why it stands, and where the file is missing or holds no block of that page or file, `context` says so (as set in case 967.2). When the Case changes the code of a check, ``
>   - change: `case-guppi reads the block of each page and file its Case changes in the graph of links, and opens each neighbour that bears on the change`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-reads-the-link-graph-of-what-it-changes`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi reads, for each page and file its Case changes, its block in .guppi/links.md, and opens each neighbour whose purpose line bears on the change`
>   - method: `by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on .guppi/links.md and whose start wrote that file: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether a Grep of .guppi/links.md names each page and file the Case changes and whether each neighbour that bears on the change is opened or named in context; the count and the transcripts in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
> - [ ] read `estimate-case-build-reads-the-link-graph-of-what-it-changes`

> **ratification:**
> ```
> - decision[case 967.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 967.2][create][estimate-case-build-reads-the-link-graph-of-what-it-changes]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> ```

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

> **tasks:**
> - [ ] create `rule-link-graph-at-session-start`
>   - ref: `rule-harness`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents a Case builder from reading a graph of links that is missing or older than the start of its session`
>   - enforcement: `hook`
>   - implementation_ref: `[.guppi/guppi/links.py, .guppi/tests/test_links.py, .claude/settings.json]`
>   - applies_to: `[entity-link-graph]`
>   - core: `true`
>   - tags: `[harness, session]`
>   - sections.Purpose: `` Prevents a Case builder from reading a graph of links that is missing or older than the start of its session. The builder has no tool that runs a command, so `uv run --project .guppi guppi links --write` runs on `SessionStart` and writes the whole graph into `.guppi/links.md`, which git ignores; the builder reads the block of each page and file its Case changes by a Grep. Pages and rendered files change at the librarian's run, so the file written at the start stays current through the session. The hook takes the text of each rendered file as `guppi render` writes it, and an error prints one line and stops no session (as set in case 967.3). ``
> - [ ] update `rule-hook-registry`
>   - old: `{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 } ] },`
>   - new: `{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 }, { "type": "command", "command": "uv run --project .guppi guppi links --write", "timeout": 60 } ] },`
>   - change: `the SessionStart hook guppi links --write registered`
> - [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
> - [ ] update `rule-harness`
>   - old: `the hooks that read a page of the vault without its History, and the file under`
>   - new: `the hooks that read a page of the vault without its History, the hook that writes the graph of the links between the pages and the harness files at the start of a session, and the file under`
>   - old: `640, 710.1, 796;`
>   - new: `640, 710.1, 796, 967.3;`
>   - change: `the hook that writes the graph of links at the start of a session belongs to the harness`
> - [ ] create `estimate-link-graph-at-session-start-writes-the-file`
>   - ref: `rule-link-graph-at-session-start`
>   - kind: `QA`
>   - purpose: `Whether the SessionStart hook writes .guppi/links.md whole at the start of a session, from the text guppi render writes, kept out of git, and stops no session on an error`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_links.py, which runs guppi links --write over a vault in a temporary folder, a rendered file left unwritten and an error included; and by hand, after the first session start whose .claude/settings.json holds the hook: the time of .guppi/links.md against the session-start line of vault/raw/<date>/event_log.md, its block of .claude/skills/sprint-open/SKILL.md and the output of git status, read against the Criterion, the result in the estimate line`
>   - tags: `[harness, session]`
> - [ ] `.guppi/guppi/links.py`: `--write` writes every block into `.guppi/links.md`, prints one line on stderr on an error and exits 0.
> - [ ] `.guppi/.gitignore`: a line `links.md` after `.venv/`.
> - [ ] `.guppi/tests/test_links.py`: the test of `--write` over a vault in a temporary folder.
> - [ ] read `estimate-link-graph-at-session-start-writes-the-file`

> **ratification:**
> ```
> - decision[case 967.3][create][rule-link-graph-at-session-start]{ref:rule-harness}{tags:harness,session}
> - decision[case 967.3][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 967.3][update][rule-harness]{ref:rule-harness}
> - decision[case 967.3][create][estimate-link-graph-at-session-start-writes-the-file]{ref:rule-link-graph-at-session-start}{tags:harness,session}
> ```
