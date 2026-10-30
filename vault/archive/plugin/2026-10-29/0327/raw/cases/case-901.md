## Case 901 — The Criteria of shipped Estimates read in this session hold in an installed project

> **context:**
> `guppi ship` writes into the clean version of GUPPI each `passed` Estimate whose target page it ships, with its Criterion as it stands here. The reading of `estimate-clean-branch-ships-neutral-texts` in this Plan Mode (ledger line 1 of this session) listed shipped Estimates whose Criterion holds a sentence true only in the repository of GUPPI. Case 898 set the yardstick: a sentence passes when it holds as it reads in a project that installed GUPPI. This Case is Case 899 built again under a new number, since the person narrowed it at `/pre-spec` and it no longer holds sub-cases that have decision lines. Its decision lines carry `{supersedes:case 899}` and one mark for each sub-case of Case 899.
> `decision-case-893.1` deferred this rewrite on `rule-clean-branch`, so that a Criterion replaced then would not set each Estimate `pending` and its rule `draft` until its reading. The `status` field of `rule-rules-schema` says that the cascade of `generate` sets a rule `built` only once every Estimate passes. `rule-clean-branch` says that while a rule or an entity with `core: true` stands `draft`, `guppi ship <folder>` writes nothing, so the workflow writes nothing to `prod`. So the person chose to keep in this Case only the Estimates whose reading this session takes, by a test or at its Retro. The others go back on the list of the reading, and the defer of `decision-case-893.1` stays for them. No line of this Case carries a mark that retires that defer.
> Five Estimates stay, each one sub-case. `estimate-sprint-close-next-session-opens-the-sprint` is read by pytest and a reading of the skill files. `estimate-materialize-lifts-a-lesson` and `estimate-materialize-judges-a-fence` are read by pytest. `estimate-case-protocol-case-form` is read on the Cases of this session at its close. `estimate-orchestration-batches-cases-out-at-once` is read at the Retro of this session, once its `method` reads the Render as it stands, since its old `method` reads "the new Render of rule-orchestration in the Spec" and this session does not change that Render. The cost: `rule-sprint-close`, `rule-case-protocol` and `rule-materialize` stand `built` with `core: true`, so each is `draft` from the replaced Criterion until its reading passes in this session. `rule-orchestration` already stands `draft`.
> Seven Estimates leave, since their `method` waits for a live event:
> - `estimate-synthesis-keeps-actioned-by-the-mark` and `estimate-synthesis-clusters` wait for a librarian's run of a given kind.
> - `estimate-permissions` waits for the person's word after a Case file written in Plan Mode.
> - `estimate-orchestration-forwards-a-discussion-question` waits for such a question.
> - `estimate-glossary-terms-defined` waits for the librarian's run.
> - `estimate-ask-query-before-a-create` waits for a Case with a `create` without a `ref`.
> - `estimate-compact-recall-reloads` holds a live reading of a compaction beside its pytest.
> The person added the last two at `/pre-spec`. The first holds "in Russian or in English" and the second the sample session folder "raw/2026-09-28/2229/".
> In the five, the lines change by the yardstick. Three lines named an Estimate that the clean version does not hold, so they now say what they need in their own words, or drop the pointer. `estimate-hi-writes-frontier`, `estimate-orchestration-signs-items-taken-together` and `estimate-orchestration-shows-the-built-case` are `pending`. `estimate-materialize-lifts-a-lesson` said "that day" of a past day of GUPPI. `estimate-materialize-judges-a-fence` listed code names that a past change of GUPPI removed. Four of the Estimates first listed stand by the yardstick of Case 898, and the Case 899 text says why. Two wait for a Case of their own that removes a fallback path from the code.
> A Grep of `wiki_root\(REPO|read_vault\(.*REPO|REPO / "vault"|ship\.ship\(REPO` over `.guppi/tests/` printed `test_ship.py`, `test_generate.py`, `test_guppi_package.py` and `test_schemas.py`. `test_generate.py` and `test_schemas.py` read only the `schema.yaml` files. `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `test_guppi_package.py` looks for `uv run guppi`, `uv run pytest` and the paths `guppi/` and `tests/` where a `reword` changes them, and the new texts keep the commands and paths that the old ones held. `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` of `test_ship.py` asserts no line on a page under `vault/wiki/estimates/`, and the new texts hold no case id. Each of the five is `pending` until its reading, and `guppi ship` writes only `passed` Estimates. So the clean version holds the new Criterion of each one whose reading passes before the next reading of `estimate-clean-branch-ships-neutral-texts`, whose Criterion Case 898.1 replaces.

> **problem:**
> Shipped Estimates hold a Criterion sentence that is false or empty in a project that installed GUPPI. A Criterion replaced now sets its Estimate `pending` and its rule `draft` until its reading, so only the Estimates read in this session are rewritten now.

> **recommend:**
> - **Which Criteria the Case rewrites**
>   - Recommended: (a) rewrite the ten that fail the yardstick of Case 898; the four that hold keep their Criterion and their status, and the Case says why each one stands.
>   - Answer: agreed, (a).
> - **A sentence that names an Estimate the clean copy leaves out**
>   - Recommended: (a) the line says what it needs in its own words, or drops the pointer where the line reads whole without it.
>   - Answer: agreed, (a).
> - **The two sentences on an old path that a later Case removes**
>   - Recommended: (b) a Case of its own removes the two old paths and the two sentences together; this Case leaves them on the reading's list.
>   - Answer: agreed, (b).
> - **Estimates whose new Criterion waits for a live reading**
>   - Recommended: (a) rewrite all ten now; each is `pending` until its reading, and those that wait for a live event leave the clean copy until then.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, narrow the Case to the Estimates whose reading runs in this session, by a test or at its Retro; the others go back on the list of the reading, and the defer of `decision-case-893.1` stays for them.
>   - Taken: five Estimates stay, seven leave, and the Case is built again as Case 901 with marks that retire each sub-case of Case 899.
> - **Change**
>   - Asked: at `/pre-spec`, add `estimate-ask-query-before-a-create` and `estimate-compact-recall-reloads` by the same rule.
>   - Taken: both wait for a live reading, so both leave with the defer, and the `context` says why.

### Case 901.1 — The next session opens the sprint

> **given:**
> `estimate-sprint-close-next-session-opens-the-sprint`: its Criterion is replaced whole.
> **＋** `rule-brief`: its Render writes the `Cases` of Next session in `vault/wiki/brief.md`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill that opens a session.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill that opens a sprint.
> **＋** `vault/wiki/sprint.md`: the page of the open sprint.
> **＋** `entity-sprint-<id>`, `entity-sprint-<new id>` and `entity-sprint-`: the page of a sprint, the closed one and the new one, and the prefix of its slug.
> **＋** `.guppi/tests/test_ledger.py`: the tests of `guppi ledger`.
> **＋** `.guppi/tests/test_materialize.py`: the tests of `guppi materialize`.

> **when:**
> Someone reads `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and the step of the Render of `rule-brief` that writes the `Cases` of Next session in `vault/wiki/brief.md`, for the session that opens after the librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page.
> **＋** Or `.guppi/tests/test_ledger.py` and `.guppi/tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

> **then:**
> The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
> **＋** `/hi` starts `/sprint-open` and writes no `frontier.md` before the opening Case is ratified; then `frontier.md` holds that line first under `## Cases`, closed `[x] … · case N` by the opening Case, and no item of `vault/wiki/sprint.md`.
> **＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
> **＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
> **－** An `estimate` or `lesson` line is not refused for this reason.
> **－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

> **tasks:**
> - [ ] update `estimate-sprint-close-next-session-opens-the-sprint`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — it names no Estimate that the clean version does not hold`
> - [ ] read `estimate-sprint-close-next-session-opens-the-sprint`

> **ratification:**
> ```
> - decision[case 901.1][update][estimate-sprint-close-next-session-opens-the-sprint]{ref:rule-sprint-close}{supersedes:case 899}{supersedes:case 899.2}{supersedes:case 899.1}{supersedes:case 899.3}
> ```

### Case 901.2 — Cases out at once are a batch

> **given:**
> `estimate-orchestration-batches-cases-out-at-once`: its Criterion is replaced whole and its `method` is set anew.
> **＋** `rule-orchestration`: renders `vault/wiki/orchestration.md`, which sets the steps of a batch.
> **＋** `case-guppi`: the agent that builds each Case.
> **＋** `rule-prespec`: sets the loop after the findings of `/pre-spec`.

> **when:**
> In Plan Mode before `/pre-spec`, a Case of the session goes back to its `case-guppi` — the person questions or changes it, or the person drops a change to it and its `case-guppi` undoes the change — while the `case-guppi` of another Case has not answered or a round of another Case stands unanswered, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The Cases out at the same time are one batch, and take the steps of a batch that `vault/wiki/orchestration.md` sets until each is ratified or deferred.
> **＋** The main agent shows no Case while a round of another Case of the batch stands unanswered: a Case that comes back built waits, and is not shown.
> **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line under the bold label `**Waiting:**`, translated, that names the Cases that have answered and those still out, and nothing else.
> **＋** It shows every round that came back in one list, each question numbered `<Case id>.Q<n>`, and sends each answer to the `case-guppi` of its Case, all in one message.
> **＋** It shows every Case of the batch in one reply, for one ratification.
> **－** A Case that goes back while no other Case of the session is out is shown again alone.
> **－** A batch of items that one answer of the person takes up, and a batch of a ratified Case asked to change while another Case is built, are no moment of this promise.
> **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

> **tasks:**
> - [ ] update `estimate-orchestration-batches-cases-out-at-once`
>   - set:
>     ```
>     status: pending
>     method: "by hand at Retro of the session that replaces this Criterion: the Render of rule-orchestration in vault/wiki/orchestration.md read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — it names no Estimate that the clean version does not hold; the method reads the Render as it stands`
> - [ ] read `estimate-orchestration-batches-cases-out-at-once`

> **ratification:**
> ```
> - decision[case 901.2][update][estimate-orchestration-batches-cases-out-at-once]{ref:rule-orchestration}{supersedes:case 899.4}{supersedes:case 899.6}
> ```

### Case 901.3 — The file of a Case keeps the form of the schema

> **given:**
> `estimate-case-protocol-case-form`: its Criterion is replaced whole.
> **＋** `rule-case-protocol`: renders `vault/wiki/case-schema.md`, the form of a Case.
> **＋** `rule-case-check`: the hook that checks the file of a Case.
> **＋** `rule-orchestration`: renders `vault/wiki/orchestration.md`, which sets how a Case is shown.
> **＋** `case-guppi`: the agent that writes the file of a Case.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.

> **when:**
> `case-guppi` writes a Case it built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the hook of `rule-case-check` checks it, and the main agent sends that file to the person, at its first showing or again.

> **then:**
> The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
> **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `uv run --project .guppi guppi check` of the librarian's run.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification`, as `vault/wiki/orchestration.md` sets the showing, and the reply ends with a plain question.
> **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
> **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.

> **tasks:**
> - [ ] update `estimate-case-protocol-case-form`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — it names no Estimate that the clean version does not hold`
> - [ ] read `estimate-case-protocol-case-form`

> **ratification:**
> ```
> - decision[case 901.3][update][estimate-case-protocol-case-form]{ref:rule-case-protocol}{supersedes:case 899.5}{supersedes:case 899.7}
> ```

### Case 901.4 — A lesson line carries its source

> **given:**
> `estimate-materialize-lifts-a-lesson`: its Criterion is replaced whole.
> **＋** `rule-materialize`: the commands `guppi materialize` and `generate`.
> **＋** `.guppi/tests/test_materialize.py`: the tests of the lesson entry.

> **when:**
> `guppi materialize` reads a `- lesson[...]` ledger line whose braces carry `{source:...}`.

> **then:**
> The entry carries `source` in its `fields`, and `generate` writes it into the page's frontmatter.
> **＋** A `knowledge` lesson whose line carries no `source` is still marked `incomplete: [source]`; an `error` lesson never is.
> **－** The applied entries of the yamls of earlier sessions are not rewritten: each records what the parser did in its own session.

> **tasks:**
> - [ ] update `estimate-materialize-lifts-a-lesson`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the yamls of earlier sessions, not a past day of GUPPI`
> - [ ] read `estimate-materialize-lifts-a-lesson`

> **ratification:**
> ```
> - decision[case 901.4][update][estimate-materialize-lifts-a-lesson]{ref:rule-materialize}{supersedes:case 899.8}{supersedes:case 899.10}
> ```

### Case 901.5 — Every reader judges a fence alike

> **given:**
> `estimate-materialize-judges-a-fence`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/materialize.py`: holds the one judgment of a fence.
> **＋** `.guppi/guppi/ratified.py`: a reader of a fence.
> **＋** `.guppi/guppi/prespec.py`: a reader of a fence.
> **＋** `.guppi/guppi/casecheck.py`: a reader of a fence.
> **＋** `.guppi/guppi/ledger.py`: a reader of a fence.
> **＋** `.guppi/guppi/lint.py`: a reader of a fence.

> **when:**
> A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `quoted_sections` and `criterion_text` of `.guppi/guppi/materialize.py`, `fenced_value` of `.guppi/guppi/ratified.py`, `plan_prose` and `check_pairs` of `.guppi/guppi/prespec.py`, the check of `ratification` in `.guppi/guppi/casecheck.py`, `ledger_lines` of `.guppi/guppi/ledger.py`, or the class `fence` of `.guppi/guppi/lint.py`.

> **then:**
> A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
> **＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
> **＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
> **＋** `fence_breaks` is built on `fence_opening` and `closes_fence`, so each break it reports is a line these readers keep as content, or an end of section they reach inside a fence.
> **＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
> **＋** Every one of these readers takes the judgment from the functions of `.guppi/guppi/materialize.py`, and they all give the same answer for the same text.
> **－** No reader keeps a fence pattern or a test on three backticks of its own.

> **tasks:**
> - [ ] update `estimate-materialize-judges-a-fence`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — no list of the code names a past change of GUPPI removed`
> - [ ] read `estimate-materialize-judges-a-fence`

> **ratification:**
> ```
> - decision[case 901.5][update][estimate-materialize-judges-a-fence]{ref:rule-materialize}{supersedes:case 899.9}
> ```
