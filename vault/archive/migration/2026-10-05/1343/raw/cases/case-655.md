## Case 655 — The check of the searches of ask-guppi at pre-spec leaves Decision pages to the check of every agent

> **context:**
> At `/pre-spec` the main agent sends the plan to `ask-guppi`, which searches the vault for findings. `estimate-ask-searches-at-prespec` checks how it searches: the Grep of the rules first, one Grep per other category, then further searches as each finding needs, a count over Decision pages not run again, and no search that reaches `vault/wiki/decisions/` but for the two reasons of its frame. The reading at the `/hi` of session 0109 (L9 of `raw/2026-10-05/0109/ledger.md`) failed: call 16 of agent a390781c7f1241c18 ran a Grep over `vault/wiki` with the glob `!decisions/**`, which left nothing out, and printed 29 lines of Decision pages. Case 640 put `.claude/rules/search-leaves-out-decisions.md` in place with a glob that works and created `estimate-search-leaves-out-decisions-in-every-agent`, which reads the same promise for the main agent, `ask-guppi` and `case-guppi` under the stricter letter of that file. Case 649 deferred this Estimate in session 0311. The `/pre-spec` of session 0311 (transcript 6d53e05d) was the first after both renders. Its three ask-guppi runs, a055d35695650c13f, af56f988c579ddc06 and af7cde916f5b24293, each opened with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` and then grepped the other categories, as `case-guppi` saw in their transcripts. The only reading of `estimate-search-leaves-out-decisions-in-every-agent`, at the `/hi` of this session (L10 of `raw/2026-10-05/1343/ledger.md`), found that no Grep of these runs printed a line of a Decision page, and failed. Among its causes, ask-guppi af56f988c579ddc06 ran a Grep at the repository root with the glob `*.py` and no `!**/decisions/**`, and case-guppi a1cf96ac9df5edd1c read `decision-case-432` for neither reason of its frame; the rest were Greps of the main agent and of case-guppi without the exclusion. The clause this Case hands to that Estimate is thus read there under a stricter letter, and that Estimate stands failed until a Case of its own. The person chose to drop the clause on Decision pages from this Estimate and leave it to `estimate-search-leaves-out-decisions-in-every-agent`, whose Criterion already covers `ask-guppi` and stands. The Criterion is replaced whole: its `when` and its first three lines of `then` are carried word for word, and the old `－` line, that no Grep or Read of the agent reaches `vault/wiki/decisions/` but for the two reasons, is left out on purpose; a new `－` line says that clause is outside this promise. The `purpose` and the `method` of the Estimate state the old promise and the old runs, so the same `update` sets both anew. A reading of an Estimate that a decision line of this session updates waits for a later session, and the ledger hook refuses it (case 428.1). So the reading is taken at the `/hi` of the next session. The new `method` names its moment by its kind, as `rule-estimates-schema` asks of a method by hand: the calls of ask-guppi at a `/pre-spec` after the render, read at the `/hi` of a later session. The first reading takes the three ask-guppi runs of the `/pre-spec` of session 0311, as the person chose. The decision line carries `{supersedes:case 649}`, which retires the defer. `.claude/agents/ask-guppi.md` and the Render of `rule-ask` still forbid a search of Decision pages but for the two reasons; the Case does not touch them, and they stay true. The Criterion of `estimate-ask-finds` is about the form of the answer, not the searches, and stands. The Case creates no page, so no vault query is run. A Grep `estimate-ask-searches-at-prespec` over `vault/wiki` with the glob `!**/decisions/**` printed 4 files: `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-ask-finds.md` and `vault/wiki/rules/rule-ask.md`. The hit in `estimate-ask-finds` is a History line. The hits in `rule-ask` are its `estimates` field, which stands, and a History line. The brief and the log are not read.

> **problem:**
> `estimate-ask-searches-at-prespec` stands failed and deferred. Its clause on Decision pages repeats the promise of `estimate-search-leaves-out-decisions-in-every-agent`, and its reading after the fix by case 640 has not been taken.

> **recommend:**
> - **Which runs the new reading reads**
>   - Recommended: (a) the runs of the previous session's `/pre-spec`, read in this session.
>   - Answer: (a), the runs of the previous session; the time of the reading is set by the later question When the reading is taken, and over which runs.
> - **Whether the check keeps its clause on Decision pages**
>   - Recommended: (a) keep the clause as it stands.
>   - Answer: (b), drop the clause and leave Decision pages to `estimate-search-leaves-out-decisions-in-every-agent`.
> - **When the reading is taken, and over which runs**
>   - Recommended: (a) the `/hi` of the next session reads the runs of the previous session's `/pre-spec`.
>   - Answer: agreed, (a).

> **given:**
> `estimate-ask-searches-at-prespec`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-ask`: the rule the Estimate checks, rendered into `.claude/agents/ask-guppi.md`.
> **＋** `.claude/agents/ask-guppi.md`: the frame of `ask-guppi`, which the Criterion reads.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill whose questions the main agent sends.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check that keeps the clause on Decision pages.
> **＋** `rule-estimates-schema`: the rule on how a method by hand names its moment.
> **＋** `vault/wiki/rules/`: the folder of the rules, whose Grep the agent runs first.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages, left to the other check.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** Whether a Grep or Read of the agent reaches `vault/wiki/decisions/` is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

> **tasks:**
> - [ ] update `estimate-ask-searches-at-prespec`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether ask-guppi at /pre-spec starts with the Grep of the rules and one Grep per other category, then greps and reads as each finding needs, a count over Decision pages not run again"
>     method: "by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md, read in its agent transcript against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the clause on Decision pages left to estimate-search-leaves-out-decisions-in-every-agent; purpose and method set anew (case 655)`
> - [ ] read `estimate-ask-searches-at-prespec`

> **ratification:**
> ```
> - decision[case 655][update][estimate-ask-searches-at-prespec]{ref:rule-ask}{supersedes:case 649}
> ```
