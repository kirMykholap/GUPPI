## Case 898 — The clean copy is judged by what holds in an installed project

> **context:**
> `guppi ship` builds the clean version of GUPPI that other projects install. It removes each bracket that holds a pointer to a case or a session, and nothing else. `estimate-clean-branch-ships-neutral-texts` promises that no sentence of the shipped rules, entities and `CLAUDE.md`, and no `purpose` or `method` of a shipped Estimate, holds only in the repository of GUPPI. Its reading in the Plan Mode of this session (ledger line 1 of this session) failed on seven pages and 34 methods, and called about thirty more items doubtful. The readers had no single yardstick. They passed the conditional sentences on `/merge-main`, but they failed the sentence of `rule-case-protocol` that says "since, in the repository of GUPPI, `guppi ship` removes that bracket", which is conditional as well. The person chose the yardstick: a sentence passes when it holds as it reads in a project that installed GUPPI.
> By that yardstick, the flagged pages stand as they are. The shipped `entity-guppi` says that in the repository of GUPPI a third part is `entity-guppi-repository`, and that the clean version does not hold that page. `rule-clean-branch` sets that `guppi ship` writes a link to a page it does not ship as the slug in a code span, so no page that stays here reaches the clean version, and its Purpose holds. `rule-case-protocol`, `rule-lint`, and the `core` field texts of `rule-entities-schema`, `rule-rules-schema` and `rule-estimates-schema` state their condition. The `origin` and `sprint` field texts, `rule-rules-schema` on the Estimates a core page brings, and the last sentence of `rule-guppi-package` say what `guppi ship` did to the files the project holds. `rule-harness` says that the clean version holds no `Makefile`, which is true there. The shipped `ratification.md` and `rule-ratification` name no sprint, since `guppi ship` removed the bracket that named `migration` and `plugin`. The copy of `.guppi/guppi/caseid.py` in the clean version still holds `PLAIN_SPRINTS = ("migration", "plugin")`, and `is_plain` there answers yes for a sprint with either name. The person left that code value to a Case of its own, since this promise reads texts. Of the doubtful items, `rule-page-generation` and `rule-vault-layout` speak of a merge of `main` into a branch, which any project with git can do; `rule-spec-reconcile` states its own condition ("until the writer is live"); `rule-spec-box` and `rule-work-mode` say what is not built or decided yet; and `estimate-case-build-finds-an-existing-judgment` names `.guppi/guppi/`, which the clean version holds. All of them stand.
> For the methods, the person chose that a kind of moment that comes again in any project stands. This follows `rule-estimates-schema`: "A reading names its moment by its kind … and any such moment after the render counts". So "the Retro of the session that changes it", "the new Render … in the Spec", "the Spec that changes it" and "the session that replaces this Criterion" stand. A method that names one moment in the past of GUPPI is reworded to name a kind of moment instead. These are "the next session", "the first … under the new Render", "the first /pre-spec of a session whose Cases case-guppi built with … the Render … that sets this Criterion", "the first Case file … after the Work Mode that changes the guard", "the first librarian run whose frame holds this Render" and "the VS Code chat". Other methods with the word first name an event that a new project has not met yet, such as the librarian's first run or the first marked lesson. These fit "the word 'first' stands only for an event that has never happened" of `rule-estimates-schema`, and they stand. A Grep of `^method:.*(next session|later session|\bfirst\b|VS Code|the session that set|this session|session \d|2312|the Retro of this)` over the `vault/wiki/estimates/` of the shipped copy in the scratchpad folder `ship-0327` printed 38 lines in 38 files. Eight of them, the Estimates of Cases 898.2 and 898.3 but `estimate-one-judgment-one-implementation-followed`, enter this Case. That ninth one comes from the list of the reading, since "the next Work Mode session" does not match the pattern. The other 30 name a kind of moment, or a first event that a new project has not met. The new methods were checked against `tied_to_a_one_off_moment`, `waits_for_another_session` and `waits_for_an_event` of `.guppi/guppi/lint.py`, which `/pre-spec` calls. Each part of a new method that waits for a session opens with `by hand, after <event>:`, and no part says "first … after the render" or "first … after the change".
> Case 898.1 replaces the Criterion of `estimate-clean-branch-ships-neutral-texts` with this yardstick. Its `purpose` already says "hold no other sentence true only in the repository of GUPPI" and stands. Its `method` names the librarian's run of session 2312, so it is set anew to wait for the run of the session that replaces this Criterion. Cases 898.2 and 898.3 only set `method` fields, so this Case keeps the status and the Criterion of each of those Estimates. `estimate-clean-branch-ships-neutral-texts` checks their new methods at its next reading. `ships` of `.guppi/guppi/ship.py` writes an Estimate into the clean copy only while it is `passed`. Case 901 replaced Case 899 of this session, and it leaves `estimate-permissions` out. So no Case of this session sets that Estimate `pending`, and the clean copy keeps it with the method that 898.2 gives it. The Criterion sentences of shipped Estimates are Frontier item C3, which Case 901 takes up, and this Case leaves them out. Case 900 sets the methods of `estimate-git-context-offers-git-init` and `estimate-guppi-package-is-ready-after-the-install` so that each says it runs where the module of the command `ship` stands. The first `－` line of 898.1 passes such a sentence. A Grep of `wiki_root\(REPO|read_vault\(.*REPO|REPO / "vault"|ship\.ship\(REPO` over `.guppi/tests/` printed `test_generate.py`, `test_guppi_package.py`, `test_schemas.py` and `test_ship.py`. `test_generate.py` and `test_schemas.py` read only the live `schema.yaml` files, which this Case does not change. The docstring of `test_guppi_package.py` says that no live Estimate names `uv run guppi`, `uv run pytest` or a path that the pairs `guppi/` and `tests/` would change, and the new methods keep the commands and the paths of the old ones as they were. `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` of `test_ship.py` asserts that the build of this repository prints no line on a page under `vault/wiki/estimates/`, and the new methods hold no case id, decision id or session id.

> **problem:**
> The reading of `estimate-clean-branch-ships-neutral-texts` has no single yardstick for a sentence that holds only in the repository of GUPPI. It failed sentences that hold as they read in an installed project. Some methods of shipped Estimates also wait for one moment in the past of GUPPI, which an installed project never meets.

> **recommend:**
> - **Which sentences count as true only in the repository of GUPPI**
>   - Recommended: (a) a sentence that holds as it reads in an installed project passes, because it states its condition or says how the shipped files came about; only sentences that are false or empty there are reworded, and the Criterion gets a line that says this.
>   - Answer: agreed, (a).
> - **Which method moments hold in any project**
>   - Recommended: (a) "the session that changes it", "the new Render" and "the Spec that changes it" stand; methods that point to one moment of the past ("the next session", "the first … under the new Render", the VS Code chat) are reworded to a kind of moment.
>   - Answer: agreed, (a).
> - **What the Case does with the doubtful sentences**
>   - Recommended: (a) judge them by the same yardstick in this Case, reword the ones that fail, and say why the others stand.
>   - Answer: agreed, (a).
> - **The sprint names in the shipped code**
>   - Recommended: (a) the text stands, and the value in the shipped code is left to a Case of its own.
>   - Answer: agreed, (a).

### Case 898.1 — A sentence that holds in an installed project passes

> **given:**
> `estimate-clean-branch-ships-neutral-texts`: its Criterion is replaced whole and its `method` is set anew.
> **＋** `rule-clean-branch`: sets `guppi ship`, which writes the clean version.
> **＋** `entity-guppi`: the page that describes GUPPI.
> **＋** `rule-language`: names the languages.
> **＋** `rule-case-build`: names the languages for `case-guppi`.
> **＋** `CLAUDE.md`: the rendered file of standing instructions.
> **＋** `rule-morph`: its setup Case sets the Render of `rule-guppi-config` and the read rules of the Render of `rule-permissions`.

> **when:**
> Someone reads the pages and the files of the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.

> **then:**
> `entity-guppi` describes GUPPI as a harness and a vault, and not as the thing that the project builds.
> **＋** `rule-language` and `rule-case-build` name the language of the repository and the language of the chat by their role, not as English and Russian.
> **＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that names a past session of it, a line of its sprint page, its machine or a file that the clean version does not hold.
> **＋** No sentence of the `purpose` or the `method` of a shipped Estimate holds only in the repository of GUPPI, such as a `method` that waits for a moment of a past session of it.
> **＋** A `method` that waits for a kind of moment that comes again in any project, such as the Retro of the session that changes its rule or the Spec that changes it, holds.
> **＋** The reader lists, in the estimate line, each sentence of the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
> **－** A sentence that holds as it reads in a project that installed GUPPI does not fail this promise, such as one that states its condition, in the repository of GUPPI or where the module of the command `ship` stands, or one that says what `guppi ship` did to the files the project holds.
> **－** A sentence of the `## Criterion` of a shipped Estimate on that list does not fail this promise.
> **－** The History of a page, a sample in a code span or a fenced block, the values of the Render of `rule-guppi-config` and the read rules of the Render of `rule-permissions`, which the setup Case of `rule-morph` sets, are no part of this promise.

> **tasks:**
> - [ ] update `estimate-clean-branch-ships-neutral-texts`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's run of the session that replaces this Criterion, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence of the Criterion of a shipped Estimate that holds only in the repository of GUPPI listed in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — a sentence that holds as it reads in an installed project passes, and a method may wait for a kind of moment that comes again in any project`
> - [ ] read `estimate-clean-branch-ships-neutral-texts`

> **ratification:**
> ```
> - decision[case 898.1][update][estimate-clean-branch-ships-neutral-texts]{ref:rule-clean-branch}
> ```

### Case 898.2 — The methods of the Case builder and the orchestration wait for a kind of moment

> **given:**
> `estimate-case-build-reads-no-sibling-file-mid-send`: its `method` is set anew.
> **＋** `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`: its `method` is set anew.
> **＋** `estimate-case-build-reads-the-code-it-states`: its `method` is set anew.
> **＋** `estimate-permissions`: its `method` is set anew.
> **＋** `rule-estimates-schema`: a reading names its moment by its kind.

> **when:**
> Someone reads the `method` of `estimate-case-build-reads-no-sibling-file-mid-send`, `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`, `estimate-case-build-reads-the-code-it-states` or `estimate-permissions` in a project that installed GUPPI.

> **then:**
> `estimate-case-build-reads-no-sibling-file-mid-send` and `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` are read after any send of two or more Cases to the builder at once.
> **＋** `estimate-case-build-reads-the-code-it-states` is read after any pre-spec check of a session whose Cases the builder wrote.
> **＋** `estimate-permissions` is read after any Case file the builder writes in Plan Mode.

> **tasks:**
> - [ ] update `estimate-case-build-reads-no-sibling-file-mid-send`
>   - set:
>     ```
>     method: "by hand, after a send of two or more Cases to case-guppi at the same time: the tool calls and the summary of each case-guppi of that send read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `method names a kind of moment, not the first send under the new Render`
> - [ ] update `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`
>   - set:
>     ```
>     method: "by hand, after a send of two or more Cases to case-guppi at the same time: the prompts and messages of the main agent from that send to the showing of its Cases read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `method names a kind of moment, not the first send under the new Render`
> - [ ] update `estimate-case-build-reads-the-code-it-states`
>   - set:
>     ```
>     method: "by hand, after a /pre-spec of a session whose Cases case-guppi built: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the function it read, the count in the estimate line"
>     ```
>   - change: `method names a kind of moment, not the first /pre-spec under the Render that set this Criterion`
> - [ ] update `estimate-permissions`
>   - set:
>     ```
>     method: "the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of .guppi/tests/test_render.py; by hand, after a Case file that case-guppi writes in Plan Mode: the person's word on whether the client asked at that write, and at a Grep of a subagent whose path is the folder of the project's saved transcripts itself and at one whose path is a file under it, recorded in the estimate line, never the agent's, which cannot see the prompt"
>     ```
>   - change: `method names a kind of moment, not the first Case file after a past change of the guard`

> **ratification:**
> ```
> - decision[case 898.2][update][estimate-case-build-reads-no-sibling-file-mid-send]{ref:rule-case-build}
> - decision[case 898.2][update][estimate-orchestration-rechecks-a-sibling-after-a-joint-send]{ref:rule-orchestration}
> - decision[case 898.2][update][estimate-case-build-reads-the-code-it-states]{ref:rule-case-build}
> - decision[case 898.2][update][estimate-permissions]{ref:rule-permissions}
> ```

### Case 898.3 — The other methods wait for a kind of moment

> **given:**
> `estimate-brief-carries-the-run-facts`: its `method` is set anew.
> **＋** `estimate-language-followed`: its `method` is set anew.
> **＋** `estimate-ledger-tail`: its `method` is set anew.
> **＋** `estimate-context-size-shown-after-each-reply`: its `method` is set anew.
> **＋** `estimate-one-judgment-one-implementation-followed`: its `method` is set anew.
> **＋** `rule-estimates-schema`: a reading names its moment by its kind.

> **when:**
> Someone reads the `method` of `estimate-brief-carries-the-run-facts`, `estimate-language-followed`, `estimate-ledger-tail`, `estimate-context-size-shown-after-each-reply` or `estimate-one-judgment-one-implementation-followed` in a project that installed GUPPI.

> **then:**
> `estimate-brief-carries-the-run-facts` is read after any librarian's run.
> **＋** `estimate-language-followed` is read after the close of any session.
> **＋** The Tail line that `estimate-ledger-tail` checks is compared once, after a session start of any session.
> **＋** `estimate-context-size-shown-after-each-reply` is read in the chat of any client.
> **＋** `estimate-one-judgment-one-implementation-followed` is read on the diff of the Work Mode of any session.

> **tasks:**
> - [ ] update `estimate-brief-carries-the-run-facts`
>   - set:
>     ```
>     method: "by hand, after a librarian's run: vault/wiki/brief.md read against the run's report in the transcript of that run, recorded in the estimate line"
>     ```
>   - change: `method names a kind of moment, not the first librarian run under this Render`
> - [ ] update `estimate-language-followed`
>   - set:
>     ```
>     method: "by hand, after the close of a session: CLAUDE.md against the Render of rule-guppi-config, and the commit, the Spec and the Case files of that session against the section"
>     ```
>   - change: `method names a kind of moment, not the next session`
> - [ ] update `estimate-ledger-tail`
>   - set:
>     ```
>     method: "pytest .guppi/tests/test_tail.py; by hand, after a /hi: the Tail line against a run of uv run --project .guppi guppi tail by hand, written into the estimate line"
>     ```
>   - change: `method names a kind of moment, not the /hi of the next session`
> - [ ] update `estimate-context-size-shown-after-each-reply`
>   - set:
>     ```
>     method: "uv run --project .guppi pytest .guppi/tests/test_context.py; the live reading by hand, the line after the replies of a session in the chat"
>     ```
>   - change: `method names the chat, not the VS Code chat`
> - [ ] update `estimate-one-judgment-one-implementation-followed`
>   - set:
>     ```
>     method: "render --check exit 0, then by hand the section in CLAUDE.md and the diff of the Work Mode of a session — a judgment made in two places imported from one module, or a test over both sides"
>     ```
>   - change: `method names a kind of moment, not the next Work Mode session`

> **ratification:**
> ```
> - decision[case 898.3][update][estimate-brief-carries-the-run-facts]{ref:rule-brief}
> - decision[case 898.3][update][estimate-language-followed]{ref:rule-language}
> - decision[case 898.3][update][estimate-ledger-tail]{ref:rule-ledger-tail}
> - decision[case 898.3][update][estimate-context-size-shown-after-each-reply]{ref:rule-context-size}
> - decision[case 898.3][update][estimate-one-judgment-one-implementation-followed]{ref:rule-one-judgment-one-implementation}
> ```
