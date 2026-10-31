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

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` Before a `create` without a `ref`, run yourself the vault query that `.claude/agents/ask-guppi.md` describes, on the question whether the thing exists, what conflicts, what sits in `draft`, which tags fit and whether the slug is free; its answer goes into `context`. ``
>   - new: `` Before a `create` without a `ref`, run yourself the vault query that `.claude/agents/ask-guppi.md` describes, on the question whether the thing exists, what conflicts, what sits in `draft`, which tags fit and whether the slug is free; its answer goes into `context`. Run it as soon as you see that your Case will propose such a `create`: where the item asks for a new page, its Grep of the rules is the first Grep of `vault/wiki/` in your build, and where the person chooses one in a round, it is your first Grep of `vault/wiki/` after the answer to that round; a Glob or a Read of a page the item names may come before it, and no Grep of your own for the thing by its words does (as set in case 970.1). ``
>   - change: `case-guppi makes the Grep of the rules of its vault query its first Grep of the vault once it sees a create without a ref`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-runs-the-vault-query-first`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi makes the Grep of the rules of its vault query its first Grep of vault/wiki/ once it sees that its Case proposes a create without a ref`
>   - method: `by hand, after the first build of case-guppi on the Render of rule-case-build that holds the sentence on when the vault query runs, whose Case proposes a create without a ref: the Grep, Glob and Read calls of that build, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript and the line numbers in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
> - [ ] read `estimate-case-build-runs-the-vault-query-first`

> **ratification:**
> ```
> - decision[case 970.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 970.1][create][estimate-case-build-runs-the-vault-query-first]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> ```

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

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `` Then one Grep per other category the question touches: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`. ``
>   - new: `` Then, in each run that makes the Grep of the rules, one Grep for each other category, whatever the question: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`; each of these four Greps takes its pattern as written here, with no word added to it, since you compare meanings, not words (as set in case 970.2). ``
>   - change: `the vault query runs the index Grep of every category whatever the question, each pattern as written with no word added`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] update `estimate-ask-query-before-a-create`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the vault query that case-guppi runs before a create without a ref, by the recipe of ask-guppi, opens with the rules and runs the index Grep of every other category with its pattern as written, finds an existing page by meaning in either language, and names the rule a proposal crosses and the state of a named slug"
>     method: "by hand, after the first build of case-guppi whose Case proposes a create without a ref and that runs on .claude/agents/ask-guppi.md rendered from the Render of rule-ask that runs every category whatever the question: the Grep, Glob and Read calls of that build, read in its agent transcript under ~/.claude/projects/ against the Criterion, and the context of its case file read with them, the transcript and the line numbers in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the query opens with the rules and runs every other index Grep with its pattern as written; the moment in the build is read by estimate-case-build-runs-the-vault-query-first`
> - [ ] read `estimate-ask-query-before-a-create`

> **ratification:**
> ```
> - decision[case 970.2][update][rule-ask]{ref:rule-ask}
> - decision[case 970.2][update][estimate-ask-query-before-a-create]{ref:rule-ask}
> ```

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

> **tasks:**
> - [ ] update `estimate-ask-searches-at-prespec`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether ask-guppi at /pre-spec starts with the Grep of the rules and runs the index Grep of every other category with its pattern as written, then greps and reads as each finding needs, a count over Decision pages not run again"
>     method: "by hand, after the first /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md rendered from the Render of rule-ask that runs every category whatever the question: the Grep, Glob and Read calls of ask-guppi at that /pre-spec, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — at /pre-spec too the agent runs the index Grep of every category with its pattern as written`
> - [ ] read `estimate-ask-searches-at-prespec`

> **ratification:**
> ```
> - decision[case 970.3][update][estimate-ask-searches-at-prespec]{ref:rule-ask}
> ```
