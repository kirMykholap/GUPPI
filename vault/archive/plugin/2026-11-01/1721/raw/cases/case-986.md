## Case 986 — The builder reads the whole block of each page it changes, again at the final check

> **context:**
> At the start of each session a hook writes `.guppi/links.md`, the graph of the links between the pages and the harness files: one block per page and per file, each neighbour with its purpose line. The Render of `rule-case-build` tells `case-guppi` to find the block of each page and file its Case changes by a Grep with lines of context, while it reads the frame, and to say in `context` where the file holds no block. The reading of `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed in session 0141: 2 of 4 Cases of session 2307 found the block of each existing page and file they change, and no `context` said that a page it creates has no block. In the transcripts under `~/.claude/projects/c--PROJECTS-GUPPI/8d8876d7-f627-4f65-95f7-cb7b7172cd46/subagents/`, a Grep with the pattern `"pattern":"[^"]*","path":"[^"]*links\.md"` showed that each build searched the file with one pattern of the pages it had in mind early in the build (Case 972 at line 142 of `agent-ab08bcaa476ca5d9f.jsonl`, Case 975 at line 82 of `agent-aa121a9ddfe7235f9.jsonl`), and the pages and files it missed were not in that pattern. The handoff of session 0141 also notes that a Grep with `-A 40` printed part of the 96-line block of `rule-case-build`. The person chose to read the blocks again at the check of the finished Case, for each page and file the tasks change whose block was not read; to read each block whole, from its heading to the next heading; to expect no block of a page or file the Case creates and say nothing of it; and to replace the Criterion of the Estimate whole, with its `purpose` and `method` set anew. The rule that governs the options is `rule-case-build` itself, and `case-schema.md`, by which a promise changes only by a Criterion replaced whole; a Criterion kept would still demand a line on a created page. Four lines of the old Criterion are rewritten on purpose: the `When` line now covers the whole build up to the summary, since the reading moves to the final check too; the first `Then` line now names only a page or file that exists before the Case and reads the block whole from its line; the line on judging the neighbours now speaks of each block, since a build reads more than one; and the `－` line on a missing block now names only a page or file that exists before the Case, with a second `－` line for a created one. The Purpose of `rule-link-graph-at-session-start` says the builder reads a block by a Grep, which the Read of the whole block makes partly false, so it gets a pair. A Grep `links\.md|link graph|graph of the links` over `vault/wiki/` printed `brief.md`, `entity-guppi.md`, `estimate-case-build-reads-the-link-graph-of-what-it-changes.md`, `log.md`, `rule-case-build.md`, `rule-harness.md`, `rule-link-graph-at-session-start.md` and `estimate-link-graph-at-session-start-writes-the-file.md`; `brief.md` and `log.md` are not read, `entity-guppi` and `rule-harness` name the graph as a part of GUPPI and a hook of the harness and stand, and the Criterion of `estimate-link-graph-at-session-start-writes-the-file` speaks of how the file is written, not read, and stands. A Grep `links\.md` over `.claude/` printed `.claude/agents/case-guppi.md`, which the render changes. The blocks of `rule-case-build`, `.claude/agents/case-guppi.md`, the Estimate and `rule-link-graph-at-session-start` in `.guppi/links.md` were read whole; no neighbour is made false: `entity-link-graph` says the reader opens only the neighbours that bear on its question, which still holds, and the Estimates of `rule-case-build` other than this one speak of other steps. `estimate-case-build-checks-the-finished-case` lists the searches of the final check and not this one; it stands, since this Estimate checks the new reading at that check, and nothing is signed twice. `estimate-case-build-reads-by-need-and-in-parts` stands: a block read whole by a Read with `offset` is a part of a file read in parts. A Grep `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed `test_guppi_package.py`, whose tests refuse the old commands and a path that starts with `guppi/` or `tests/`, by `reword_pattern` of `.guppi/guppi/generate.py`, which I read whole; the new texts hold no such command or path. Case 985 of this session changes the sentence on a changed step in the same paragraph of the Render as the new sentence of the final check; the pairs touch different sentences and say nothing against each other. The session's ledger holds no `error` lesson.

> **problem:**
> The builder reads the graph of links once, early, so a page or file added to the Case later is never looked up, a long block is cut short, and a created page is held to a duty it cannot meet.

> **recommend:**
> - **When does the builder read the blocks?**
>   - Recommended: (a) again at the final check, for each page and file the tasks change whose block was not read.
>   - Answer: agreed, (a).
> - **What about a page or file the Case creates?**
>   - Recommended: (a) no block expected, nothing said.
>   - Answer: agreed, (a).
> - **How does the builder read a long block whole?**
>   - Recommended: (a) find the line, then read to the next heading.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) rewrite that check whole.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: its Render holds the sentence on `.guppi/links.md` and the check of the finished Case.
> **＋** `.claude/agents/case-guppi.md`: rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-the-link-graph-of-what-it-changes`: its Criterion is replaced whole.
> **＋** `rule-link-graph-at-session-start`: its Purpose says how the builder reads a block.
> **＋** `.guppi/links.md`: the graph of the links that the builder reads.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and answers with its summary.

> **then:**
> For each page and file the Case changes that exists before the Case, it finds the line `## <slug or path>` of its block in `.guppi/links.md` by a Grep with the line number, and reads the block whole, from that line to the next line that opens with `## `.
> **＋** At the check of the finished Case, it lists each page and file that the tasks of the Case change, and reads the block of each one whose block it has not read in that build.
> **＋** From each block it judges, by what each neighbour is for, which neighbours bear on the change.
> **＋** It opens each neighbour whose purpose line bears on the change, whole or in parts as the Render sets for its kind of text.
> **＋** Each neighbour that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** Where `.guppi/links.md` is missing or holds no block of a page or file that exists before the Case, the `context` of the Case says so.
> **－** A page or file the Case creates has no block, and the `context` of the Case says nothing of it.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` Read too, for each page and file the Case changes, its block in `.guppi/links.md` ``
>   - new: `` Read too, for each page and file the Case changes that exists before the Case, its block in `.guppi/links.md` ``
>   - old: `` find it by a Grep for its line `## <slug or path>` with lines of context, read the purpose line ``
>   - new: `` find its line `## <slug or path>` by a Grep with its line number, read the block whole by a Read from that line to the next line that opens with `## `, and read on where the block goes past the limit of that Read; read the purpose line ``
>   - old: `` and where the file is missing or holds no block of that page or file, `context` says so (as set in case 967.2). ``
>   - new: `` and where the file is missing or holds no block of such a page or file, `context` says so; a page or file the Case creates has no block yet, and `context` says nothing of it (as set in cases 967.2 and 986). ``
>   - old: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. ``
>   - new: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. List each page and file that the tasks of the Case change, and read the block in `.guppi/links.md` of each one that exists before the Case and whose block you have not read in this build, as the paragraph on the frame of the Case sets it (as set in case 986). ``
>   - change: `the builder reads the whole block of each existing page and file it changes, again at the check of the finished Case, and says nothing of a page it creates`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `rule-link-graph-at-session-start`
>   - old: `the builder reads the block of each page and file its Case changes by a Grep.`
>   - new: `the builder finds the block of each page and file its Case changes by a Grep and reads it whole.`
>   - change: `the builder finds a block by a Grep and reads it whole`
> - [ ] update `estimate-case-build-reads-the-link-graph-of-what-it-changes`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether case-guppi reads whole, for each page and file its Case changes that exists before the Case, its block in .guppi/links.md, again at the check of the finished Case for each one whose block it has not read, opens each neighbour whose purpose line bears on the change, and says nothing of a page it creates"
>     method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on reading the block of .guppi/links.md again at the check of the finished Case: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether a Grep of .guppi/links.md and a Read from its line cover the whole block of each existing page and file the tasks of the Case change, and whether each neighbour that bears on the change is opened or named in context; the count and the transcripts in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the block read whole, again at the final check, and no word on a created page; pending again after the failed reading of session 0141`
> - [ ] read `estimate-case-build-reads-the-link-graph-of-what-it-changes`

> **ratification:**
> ```
> - decision[case 986][update][rule-case-build]{ref:rule-case-build}
> - decision[case 986][update][rule-link-graph-at-session-start]{ref:rule-link-graph-at-session-start}
> - decision[case 986][update][estimate-case-build-reads-the-link-graph-of-what-it-changes]{ref:rule-case-build}
> ```
