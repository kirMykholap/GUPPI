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

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` and for the name of the step, and read each step and skill that reads that output or does the same step, the steps after it in the same text and the new path your Case adds included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in case 924). ``
>   - new: `` and for the name of the step; follow the step too to each agent, skill or hook that carries it out — one the step dispatches, loads, runs or writes a prompt for — and to each skill that such an agent loads by its `skills` field, since a skill that sets the form of every step of its kind, such as the shape of every question of a round, need not hold the words of the step; and read each step and skill that reads that output or does the same step, the steps after it in the same text, the new path your Case adds and each agent, skill and hook the step leads to included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966). ``
>   - change: `case-guppi follows a changed step to each agent, skill or hook that carries it out, and to each skill such an agent loads, beside the word search`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-reads-the-readers-of-a-changed-step`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on following a step to the one who carries it out: the findings of ask-guppi at that /pre-spec, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count and the transcript in the estimate line"
>     ```
>   - change: `pending again after the failed reading of session 0431, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render that follows a step to the one who carries it out`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`

> **ratification:**
> ```
> - decision[case 966][update][rule-case-build]{ref:rule-case-build}
> - decision[case 966][update][estimate-case-build-reads-the-readers-of-a-changed-step]{ref:rule-case-build}
> ```
