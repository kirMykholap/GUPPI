## Case 999 — The graph of links is dropped, and case-guppi searches the names of what it changes

> **context:**
> A hook on `SessionStart` runs `uv run --project .guppi guppi links --write`, which writes `.guppi/links.md`: one block per live page and per file, each neighbour out and in with its purpose line. `case-guppi` must read whole the block of each page and file its Case changes. The blocks of busy pages are long, most of their lines the purposes of the page's own Estimates, and the builders read them with a fixed limit and stopped before the end: `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed at the Retro of session 0141 (2 of 4 Cases, one block read by `-A 40` of 96 lines) and again in session 2227 (0 of 2 Cases, the block of `rule-orchestration` read with limit 80; its Result and the brief, `## Readings due`). The person chose to drop the graph whole. Out-links of a page stand in its own frontmatter and links, which `case-guppi` reads already; for in-links `case-guppi` now takes every name of the page or file it changes and runs one Grep that prints only the paths of the files that hold any of them, then one Grep that prints the purpose line of each page on that list, and opens the files that bear on the change. The names are the slug, the file name of each path of `governs`, `implementation_ref` and `code_ref`, the name of the agent or of the skill with its slash, and `guppi <command>` for each command of a module among those paths, since `guppi links` linked a page to a text that names it by any of these. The Grep runs over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`: the person's proposal named `.guppi/`, and the Case keeps to the code and the tests in it, so that the environment `.guppi/.venv/`, which `.guppi/.gitignore` names, stays out of the search; the hook of `rule-search-leaves-out-decisions` adds `!**/decisions/**` to a Grep whose path is the root of the repository. The purpose line of a neighbour, the one thing of a block worth keeping, comes back by the second Grep over the short list. Case 999.1 removes the graph: the two pages, their two Estimates, the code, its tests, the hook and the lines that name them; a new one-time Estimate of the sprint page checks the state once after the librarian's run, since `rule-estimates-schema` sets `once: true` for an Estimate that checks one state of the data once, whose target is the live sprint page. Case 999.2 changes the two sentences of the Render of `rule-case-build` that name `.guppi/links.md`, and renames and replaces the Criterion of the failed Estimate, whose `purpose` and `method` state the old promise and are set anew; its `method` waits for the `/pre-spec` of a session on the new Render through a part that opens with `by hand, after` and names its event before a colon, as `case-schema.md`, the Render of `rule-case-protocol`, sets it (case 781), with no word `first`, which `rule-estimates-schema` keeps for an event that has never happened. No line of the old Criterion is carried word for word, since each one speaks of a block of `.guppi/links.md`, a neighbour of a block or a page with no block: the new Criterion carries what they promised in the terms of the search, the second search at the check of the finished Case, the opening of each file that bears on the change and the entry of each one the change makes false, and drops the lines on a missing file and on a page with no block, since the search needs no file. The other Estimates of `rule-case-build` stand: of their Criteria only the failed one speaks of the graph, by the Grep below. `estimate-sprint-plugin-check-finds-no-bare-slug-link`, a one-time Estimate of `entity-sprint-plugin`, waits for the librarian's run that applies the update of `estimate-link-graph-prints-the-neighbours`; the History of that page holds the line `2026-11-01 updated: the bare link of the Result put in a code span` of Case 973, so the event has come, and the brief of session 2227 (`## Flags`, `guppi check`, exit 1, 7 lines) lists no `ref` line on that page. Once that page moves to the archive, `git log -p -1` on its old path shows the move, not the fix, and the Criterion fails, so the person chose to read it at the Retro of this session, before the librarian's run; whether the git log holds the diff of the Result alone was not read here. `case-guppi` read for its claims on code: `main` of `.guppi/guppi/cli.py`, which prints `guppi: unknown command` and exits 2 for a name outside `COMMANDS`; `run` of `.guppi/guppi/links.py`; `Vault.delete` of `.guppi/guppi/generate.py`, which sets a page `archived`; `Cleanup.unlink` and `Cleanup.flag_dangling` of `.guppi/guppi/cleanup.py`, which take an archived slug out of the `children` lists of live pages and the `estimates` lists of entities and rules and report a live page whose `parent` or `target` is archived, so `rule-harness`, `entity-guppi` and `rule-case-build` need no task for their lists, and the four pages are deleted together so that no `target` dangles; and `tree_files` of `.guppi/guppi/ship.py`, which walks the working tree, so the task that drops `.guppi/links.md` from `LEFT_OUT` comes with a task that deletes the local file by hand. Between the Work Mode that removes `links.py` and the render of `.claude/settings.json` at the librarian's run, a `SessionStart` of this session, such as after a compaction, runs the old hook and gets exit 2; `lesson-hooks-sessionstart-cannot-block` holds that exit 2 is a no-op there, so no session stops and nothing is lost, and the file is deleted after the code so that no hook writes it again. Between the same two moments a `case-guppi` of this session runs on the old Render, finds `.guppi/links.md` missing and says so in `context`, as that Render sets. A Grep for `links\.md|guppi links|link-graph|links\.py|link graph` over the repository with the glob `!vault/{archive,raw}/**` printed 22 files: `vault/wiki/brief.md`, `vault/wiki/sprint.md`, `vault/wiki/log.md`, `vault/wiki/entities/entity-link-graph.md`, `vault/wiki/entities/entity-guppi.md`, `vault/wiki/estimates/estimate-case-build-reads-the-link-graph-of-what-it-changes.md`, `vault/wiki/estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder.md`, `vault/wiki/lessons/lesson-ledger-reading-writes-a-bare-wikilink.md`, `.claude/settings.json`, `.guppi/tests/test_links.py`, `vault/wiki/rules/rule-case-build.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-link-graph-at-session-start.md`, `vault/wiki/rules/rule-hook-registry.md`, `vault/wiki/rules/rule-harness.md`, `.guppi/.gitignore`, `.guppi/guppi/links.py`, `.guppi/guppi/ship.py`, `vault/wiki/estimates/estimate-link-graph-prints-the-neighbours.md`, `vault/wiki/estimates/estimate-link-graph-at-session-start-writes-the-file.md`, `vault/wiki/estimates/estimate-materialize-lifts-a-create-value-by-the-schema.md` and `vault/wiki/estimates/estimate-sprint-plugin-check-finds-no-bare-slug-link.md`. Each enters the Case but these, which stand: `brief.md` and `log.md`, not read; `sprint.md`, whose line `guppi sprint` writes from the sprint Estimate; the `## Result` of `estimate-case-build-reads-the-readers-of-a-new-files-folder` and of `estimate-materialize-lifts-a-create-value-by-the-schema` and the body of `lesson-ledger-reading-writes-a-bare-wikilink`, records of past readings and events, whose slugs lint still counts as known once archived, as the docstring of `cleanup.py` says; the History and `children` of `rule-harness`, which cleanup changes; and the sprint Estimate, read before the move. The `## Purpose` of `rule-harness` also lists among the parts of the harness the hook that writes the graph of the links at the start of a session, citing case 967.3, in words the pattern does not match; `/pre-spec` found it, and 999.1 removes that part and that case from the sentence, so the Criterion of the new Estimate also covers a text that counts the graph among the parts of GUPPI or of its harness, and excepts the Decision pages under `vault/wiki/decisions/`, the record of past decisions, which the Grep of its `method` does not print under the hook of `rule-search-leaves-out-decisions`. The two Greps of the new Render were tried in this build: a Grep for `prespec\.py` at the root of the repository with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed 74 files, under `vault/wiki/`, `.claude/` and `.guppi/guppi/`, none under `vault/wiki/decisions/`; and a Grep for `^(purpose|root_cause|pattern):` over `vault/wiki/` with the glob `**/{rule-harness,entity-guppi,lesson-hooks-sessionstart-cannot-block}.md` printed the three purpose lines; and the glob `{rule-harness,entity-guppi}.md` printed two; but the glob `{rules/rule-harness.md,entities/entity-guppi.md}`, a brace list of paths with their folders, printed nothing, which fits what `ask-guppi` saw in its run of `/pre-spec`; so the new Render gives the second Grep the form `**/{<slug>,<slug>}.md`, bare slugs with no folder, and says so. The appended `!**/decisions/**` took nothing from either Grep that worked. A Grep for `links` over `.guppi/guppi/` with the glob `!links.py` printed 10 files: `lint.py`, `ship.py`, `pages.py`, `prespec.py`, `generate.py`, `ledger.py`, `materialize.py`, `cli.py`, `cleanup.py` and `caseid.py`; of their hits read around the line, `cli.py` and `pages.py` name the module `links` and enter the Case, `ship.py` is named above, and the rest name `links_of`, `body_links`, `unknown_links`, wikilinks or backlinks, which the Case does not touch. A Grep for `links\.md|guppi links|links --write|from guppi import.*links|guppi\.links|links\.run|import links` over `.guppi/tests/` printed only `.guppi/tests/test_links.py`, which reads no live file and goes with the module. A Grep for `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed only `.guppi/tests/test_guppi_package.py`, in its docstring, so no test reads the Render live; that file reads `.claude/settings.json` live, and its test asserts that the commands of four hooks stand there, none of them `links`, so it passes before and after the render. The blocks of `.guppi/links.md` of the pages and files the Case changes were read; their neighbours that bear on the change are those above, and the rest, such as the Estimates of `rule-case-build` and the rules whose `implementation_ref` names `.claude/settings.json`, are not made false. Case 998, whose finished file was read whole once its build ended, replaces the Criterion, `purpose` and `method` of `estimate-case-build-reads-the-readers-of-a-changed-step` and leaves the Render of `rule-case-build` alone, so the two Cases change no sentence in common; its `context` speaks of the block of that Estimate in `.guppi/links.md` as a reading of its own build, which the removal of the file does not make false. A Glob for `vault/**/estimate-*{searches-the-names,link-graph-is-gone,graph-removed}*` printed nothing, so both new slugs are free. The ledger of the session holds no `error` lesson, so the Case carries no `{addresses:...}` mark.

> **problem:**
> `case-guppi` must read whole a block of a generated file of about seven thousand lines to find what points to a page it changes, and the long blocks get cut. The graph meant to make that search quick and cheap became a long list read in full, and the step it serves has failed twice.

> **recommend:**
> - **Which names the search takes**
>   - Recommended: (b) the slug, the file name of each path, the name of the agent or the skill with its slash, and `guppi <command>` for each module that carries a command.
>   - Answer: (b).
> - **The purpose line beside each neighbour**
>   - Recommended: (b) a second search over the pages on the list that prints the purpose line of each.
>   - Answer: (b).
> - **How the new search step is checked**
>   - Recommended: (a) rename the failed Estimate and replace its Criterion by the new step.
>   - Answer: (a).
> - **How the removal of the graph is checked**
>   - Recommended: (a) a new one-time Estimate on the sprint page.
>   - Answer: (a).
> - **The sprint Estimate on the bare link**
>   - Recommended: (a) read it now, before the page moves.
>   - Answer: (a).

### Case 999.1 — The graph of links and its hook are removed

> **given:**
> `estimate-sprint-plugin-link-graph-is-gone`: the new one-time Estimate of the removal.
> **＋** `entity-link-graph`, `rule-link-graph-at-session-start`, `estimate-link-graph-prints-the-neighbours` and `estimate-link-graph-at-session-start-writes-the-file`: the pages deleted.
> **＋** `rule-hook-registry`: the Render of the hooks of `.claude/settings.json`, which loses the hook.
> **＋** `entity-guppi`: the page of GUPPI, which names the graph as a part.
> **＋** `rule-harness`: the rule of the harness, whose Purpose lists the hook that writes the graph.
> **＋** `.guppi/guppi/links.py` and `.guppi/tests/test_links.py`: the code of `guppi links` and its tests, removed.
> **＋** `.guppi/guppi/cli.py`, `.guppi/guppi/pages.py`, `.guppi/guppi/ship.py` and `.guppi/.gitignore`: the files that name the module or `.guppi/links.md`.
> **＋** `entity-sprint-plugin` and `estimate-sprint-plugin-check-finds-no-bare-slug-link`: the sprint page and its one-time Estimate that reads a page deleted here.
> **＋** `rule-estimates-schema`: the rule of a one-time Estimate and of a `method`.
> **＋** `vault/wiki/`: the live pages, searched for a text that still names the graph.
> **＋** `vault/wiki/decisions/`: the Decision pages, the record of past decisions, left out of that search.

> **when:**
> The librarian's run applies the `delete` of `entity-link-graph` and `rule-link-graph-at-session-start` and renders `.claude/settings.json` from `rule-hook-registry`, after the Work Mode that removes `.guppi/guppi/links.py`.

> **then:**
> No file `.guppi/links.md` stands, and no `SessionStart` hook of `.claude/settings.json` runs `guppi links --write`.
> **＋** `uv run --project .guppi guppi links` prints that the command is unknown and exits 2.
> **＋** `entity-link-graph`, `rule-link-graph-at-session-start`, `estimate-link-graph-prints-the-neighbours` and `estimate-link-graph-at-session-start-writes-the-file` stand in the archive, and no live page lists them in a field.
> **＋** No live page of `vault/wiki/`, no file of `.claude/` and no file of `.guppi/guppi/` or `.guppi/tests/` names `.guppi/links.md` or `guppi links`, or counts the graph of the links among the parts of GUPPI or of its harness, outside History lines, a `## Result`, a lesson, the pages under `vault/wiki/decisions/`, `log.md`, `brief.md` and `estimate-sprint-plugin-link-graph-is-gone`.
> **＋** `uv run --project .guppi guppi test` reports no failed test.

> **tasks:**
> - [ ] delete `entity-link-graph`
>   - impact: `the graph of links goes; case-guppi searches the names of what it changes instead (case 999.2); estimate-link-graph-prints-the-neighbours goes with it`
> - [ ] delete `rule-link-graph-at-session-start`
>   - impact: `the SessionStart hook guppi links --write goes from rule-hook-registry; estimate-link-graph-at-session-start-writes-the-file goes with it`
> - [ ] delete `estimate-link-graph-prints-the-neighbours`
>   - impact: `its target entity-link-graph is deleted; estimate-sprint-plugin-check-finds-no-bare-slug-link is read before the move`
> - [ ] delete `estimate-link-graph-at-session-start-writes-the-file`
>   - impact: `its target rule-link-graph-at-session-start is deleted`
> - [ ] update `rule-hook-registry`
>   - old: `{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 }, { "type": "command", "command": "uv run --project .guppi guppi links --write", "timeout": 60 } ] },`
>   - new: `{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 } ] },`
>   - change: `the SessionStart hook guppi links --write removed with the graph of links`
> - [ ] update `entity-guppi`
>   - set:
>     ```
>     purpose: "GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint and the glossary, and in the repository of GUPPI also that repository on GitHub"
>     ```
>   - old: `` Its parts are the sprint as a kind (`entity-sprint`), the glossary (`entity-glossary`) and the graph of the links between the pages and the harness files (`entity-link-graph`), the things of GUPPI that are not rules (as set in case 967.1). ``
>   - new: `` Its parts are the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of GUPPI that are not rules. ``
>   - change: `the graph of links is no longer a part of GUPPI`
> - [ ] update `rule-harness`
>   - old: `the hooks that read a page of the vault without its History, the hook that writes the graph of the links between the pages and the harness files at the start of a session, and the file under`
>   - new: `the hooks that read a page of the vault without its History, and the file under`
>   - old: `796, 967.3; in the repository of GUPPI`
>   - new: `796; in the repository of GUPPI`
>   - change: `the hook that writes the graph of links at the start of a session is no longer a part of the harness`
> - [ ] create `estimate-sprint-plugin-link-graph-is-gone`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether, after the librarian's run that deletes the graph of links, no .guppi/links.md, no command guppi links and no SessionStart hook for it stand, its pages and Estimates are archived, no live text names them and the tests pass`
>   - method: `by hand, after the librarian's run that applies the delete of entity-link-graph and renders .claude/settings.json: the output of uv run --project .guppi guppi links entity-guppi, of git status, of uv run --project .guppi guppi test and of a Grep for links.md, guppi links and graph of the links over vault/wiki/, .claude/, .guppi/guppi/ and .guppi/tests/, and the SessionStart key of .claude/settings.json, read against the Criterion, the outputs in the estimate line`
>   - once: `true`
>   - tags: `[sprint, harness]`
> - [ ] `.guppi/guppi/links.py` and `.guppi/tests/test_links.py`: deleted.
> - [ ] `.guppi/guppi/cli.py`: the import of `links`, the entry `"links"` of `COMMANDS` and the words on `links --write` in the module docstring removed.
> - [ ] `.guppi/guppi/pages.py`: `links` removed from the list of readers in the module docstring.
> - [ ] `.guppi/guppi/ship.py`: the entry `.guppi/links.md` of `LEFT_OUT` and its comment removed.
> - [ ] `.guppi/.gitignore`: the line `links.md` removed.
> - [ ] by hand, in Work Mode after the code tasks above: the local file `.guppi/links.md` deleted.
> - [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
> - [ ] `uv run --project .guppi guppi sprint`
> - [ ] read `estimate-sprint-plugin-check-finds-no-bare-slug-link`
> - [ ] read `estimate-sprint-plugin-link-graph-is-gone`

> **ratification:**
> ```
> - decision[case 999.1][delete][entity-link-graph]
> - decision[case 999.1][delete][rule-link-graph-at-session-start]
> - decision[case 999.1][delete][estimate-link-graph-prints-the-neighbours]
> - decision[case 999.1][delete][estimate-link-graph-at-session-start-writes-the-file]
> - decision[case 999.1][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 999.1][update][entity-guppi]{ref:entity-guppi}
> - decision[case 999.1][update][rule-harness]{ref:rule-harness}
> - decision[case 999.1][create][estimate-sprint-plugin-link-graph-is-gone]{ref:entity-sprint-plugin}{tags:sprint,harness}
> ```

### Case 999.2 — case-guppi searches the names of each page and file it changes

> **given:**
> `rule-case-build`: the Render of `.claude/agents/case-guppi.md`, whose step on the graph is replaced.
> **＋** `estimate-case-build-reads-the-link-graph-of-what-it-changes`: the failed Estimate, renamed, its Criterion, `purpose` and `method` replaced.
> **＋** `.guppi/guppi/cli.py`: `COMMANDS`, which maps each command to its module.
> **＋** `rule-search-leaves-out-decisions`: the hook that leaves the Decision pages out of a Grep over the repository.
> **＋** `rule-estimates-schema`: the rule of the field `method` and of the word `first` in it.
> **＋** `rule-case-protocol`: the rule of a `method` part that waits for an event it names.
> **＋** `vault/wiki/`: the live pages, which the search of names covers.
> **＋** `.guppi/tests/`: the tests, which the search of names covers.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and answers with its summary.

> **then:**
> For each page and file the Case changes that exists before the Case, it searches in one Grep that prints only the paths of the files, over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`, for all its names.
> **＋** The names of a page are its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, the name of the agent or of the skill with its slash whose file its `governs` names, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths; the names of a file are its file name and the agent, skill or command it carries.
> **＋** It prints the purpose line of each page on that list by one more Grep over those pages.
> **＋** It opens each file of the list whose purpose line, or whose path where it has none, bears on the change.
> **＋** At the check of the finished Case, it searches the names of each page and file the tasks of the Case change that it has not searched in that build.
> **＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in `log.md` or `brief.md` is not opened.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old:
>     ```
>     Read too, for each page and file the Case changes that exists before the Case, its block in `.guppi/links.md`, the graph of the links between the pages and the harness files that a hook writes at the start of the session: find its line `## <slug or path>` by a Grep with its line number, read the block whole by a Read from that line to the next line that opens with `## `, and read on where the block goes past the limit of that Read; read the purpose line of each neighbour it names, out and in, and open each neighbour whose purpose line bears on the change, whole or in parts as the paragraph that opens with the reading of `vault/wiki/case-schema.md` sets for its kind of text; each one the change makes false enters the Case, or `context` names it and says why it stands, and where the file is missing or holds no block of such a page or file, `context` says so; a page or file the Case creates has no block yet, and `context` says nothing of it (as set in cases 967.2 and 986).
>     ```
>   - new:
>     ```
>     Find too, for each page and file the Case changes that exists before the Case, each file that names it, since a text may point to it by another name than its slug: take its names — for a page its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, such as `prespec.py` for `.guppi/guppi/prespec.py`, the name of the agent, such as `case-guppi`, or of the skill with its slash, such as `/pre-spec`, whose file its `governs` names, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths; for a file its file name and the name of the agent, the skill or the command it carries — and search for all the names of the Case at once by one Grep in the mode that prints only the paths of the files, its path the root of the repository and its glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**`; then print the purpose line of each page on that list by one Grep of `^(purpose|root_cause|pattern):` in the mode that prints the lines, its path `vault/wiki/` and its glob `**/{<slug>,<slug>}.md` with the bare slug of each page on the list and no folder before it, since a brace list of paths with their folders matches nothing, and open each file of the list whose purpose line, or whose path where it has none, bears on the change, whole or in parts as the paragraph that opens with the reading of `vault/wiki/case-schema.md` sets for its kind of text, leaving out `log.md` and `brief.md`; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in case 999.2).
>     ```
>   - old: `` List each page and file that the tasks of the Case change, and read the block in `.guppi/links.md` of each one that exists before the Case and whose block you have not read in this build, as the paragraph on the frame of the Case sets it (as set in case 986). ``
>   - new: `` List each page and file that the tasks of the Case change, and search the names of each one that exists before the Case and whose names you have not searched in this build, as the paragraph on the frame of the Case sets it (as set in cases 986 and 999.2). ``
>   - change: `case-guppi finds what points to a page or file it changes by one Grep for all its names and the purpose lines of the pages it lists, instead of the block of .guppi/links.md`
> - [ ] update `estimate-case-build-reads-the-link-graph-of-what-it-changes`
>   - rename: `estimate-case-build-searches-the-names-of-what-it-changes`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether case-guppi searches in one Grep that prints only file paths for all the names of each page and file its Case changes that exists before the Case, again at the check of the finished Case for each one it has not searched, prints the purpose lines of the pages on that list, and opens each file that bears on the change"
>     method: "by hand, after the /pre-spec of a session whose case-guppi runs on the Render of rule-case-build that searches the names of each page and file a Case changes: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether one Grep that prints file paths covers all the names of each existing page and file the tasks of the Case change, whether a Grep printed the purpose lines of the pages on its list, and whether each file that bears on the change is opened or named in context; the count and the transcripts in the estimate line"
>     ```
>   - change: `renamed and the Criterion replaced whole — case-guppi searches the names of what it changes, since the graph of links is dropped; pending again after the failed reading of session 2227`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-searches-the-names-of-what-it-changes`

> **ratification:**
> ```
> - decision[case 999.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 999.2][update][estimate-case-build-reads-the-link-graph-of-what-it-changes]{ref:rule-case-build}
> ```
