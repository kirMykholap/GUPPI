## Case 823 — Shipped Estimates hold their pointers in brackets

> **context:**
> `guppi ship` of `.guppi/guppi/ship.py` builds the clean version of GUPPI. Since case 822 it also writes each `passed` Estimate whose target page it writes and whose `method` names no `make` target (`ships`). It then reads every file it wrote and exits 1 on each pointer (a reference to a case, an id `decision-case-N` or a mention of a session) that stands outside a bracket of its own, judged by `outside` of `.guppi/guppi/pointers.py` (`leftovers`, `settled`). The order in `run` is: the draft pages with `core: true` first, which exit 1 without `--allow-draft`; then the tag `prod-x.y.z`, which exits 1 when none stands; only then the build and the pointer lines. So the run at this session's `/hi`, with no tag, printed no pointer line. `guppi ship --check`, the last step of `guppi check`, judges only files outside `vault/` and never sees an Estimate. The handoff of session 1739 (`vault/raw/2026-10-15/1739/handoff.md`, Observations) reports that a build with the real vault printed 20 `ship:` lines in 16 shipped `passed` Estimates whose Criterion, `method` or `purpose` holds a pointer outside a bracket. While those stand, every run of `.github/workflows/prod.yml` fails, a tag `prod-0.2.0` included. `/pre-spec` cannot catch a new one: `check_pointers` of `.guppi/guppi/prespec.py` judges only the new text of a page with `core: true` (`core_as_left`), Estimates carry no `core`, and `written_texts` reads no `method` and no Criterion.
>
> The person chose to rewrite these Estimates at their source and to widen `/pre-spec` to the new text of an Estimate whose target has `core: true`. A Grep of `^(\*\*|[A-Za-z`])[^\n]*([Cc]ases? \d|decision-case-\d|[Ss]essions? (\d{4}-\d\d-\d\d/)?\d{4}\b)` over `vault/wiki/estimates/` printed lines in these files: `estimate-ask-finds`, `estimate-ask-query-before-a-create`, `estimate-ask-opens-a-decision-only-for-a-finding`, `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`, `estimate-case-build-reads-the-test-code-over-a-changed-text`, `estimate-case-check-notes-a-then-line-shared-by-siblings`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-clean-branch-ships-the-tests`, `estimate-clean-branch-pages-hold-pointers-only-in-brackets`, `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`, `estimate-orchestration-acknowledges-the-opening-with-the-frontier`, `estimate-orchestration-defer-example-passes-the-hook`, `estimate-orchestration-marks-each-round-of-a-batch`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-generate-writes-the-decision-page`, `estimate-orchestration-signs-items-taken-together`, `estimate-prespec-checks-the-form-of-an-item`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-prespec-confirms-the-findings-once`, `estimate-ratification-case-id-carries-the-sprint`, `estimate-session-phases-in-order`, `estimate-search-leaves-out-decisions-in-every-agent`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-skill-sprint-open-merges-the-closed-sprint-branch`, `estimate-spec-write-writes-a-defer`, `estimate-sprint-close-next-session-opens-the-sprint`. Each hit was read, and ten files stand. In eight the pointer is in a code span or in a bracket at the end of its sentence: `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`, `estimate-case-build-reads-the-test-code-over-a-changed-text`, `estimate-clean-branch-ships-the-tests`, `estimate-orchestration-marks-each-round-of-a-batch`, `estimate-generate-writes-the-decision-page`, `estimate-prespec-checks-the-form-of-an-item`, `estimate-prespec-gathers-the-answers-after-findings` and `estimate-spec-write-writes-a-defer`. Two are not shipped: `estimate-clean-branch-pages-hold-pointers-only-in-brackets` targets `rule-clean-branch`, which carries no `core`, and the `method` of `estimate-session-phases-in-order` names `make test-session`. The other sixteen are `passed`, and their targets carry `core: true`. They hold twenty pointers outside a bracket, the count the handoff gives. Twelve hold them only in the `method`, and Case 823.1 sets a new `method` for each, which keeps them `passed`. Four hold them in the `## Criterion`, which changes only whole, so Cases 823.2 to 823.5 each replace one and set it `pending`, to be read again at this Retro.
>
> Each new `method` was read against the predicates `/pre-spec` runs over a `method` the plan sets, as they stand now (`form_finding`, a nested function of `.guppi/guppi/prespec.py`, and `tied_to_a_one_off_moment` and `waits_for_another_session` of `.guppi/guppi/lint.py`). A `method` that named the session of an earlier Case now names that session by what happened in it, such as the session whose Spec set the new Render of a rule, since this Case is the one that sets the `method` and the words "the session that set this method" would point at this session. The three that waited for `/hi` or a later session (`estimate-ask-query-before-a-create`, `estimate-prespec-confirms-the-findings-once`, `estimate-search-leaves-out-decisions-in-every-agent`) now open with `by hand, after <event>:`. Each pointer now stands in a bracket at the end of its `method`. The `method` of `estimate-case-check-notes-a-then-line-shared-by-siblings` keeps only its pytest command. The `method` of `estimate-ratification-case-id-carries-the-sprint` reads the live Renders at this Retro. Both changes are in place of readings that cannot happen in this session.
>
> The `/pre-spec` check of `rule-case-check` notes each Criterion line that the new Criterion does not carry. Each such line in Cases 823.2 to 823.5 is the line that held the pointer, with its pointer moved into a bracket at the end. In Case 823.2 the sentence on what `case-guppi` does with the note is dropped, as the person chose: the new `method` is the pytest run alone, which reads the note of the hook and not a later answer of `case-guppi`. In Case 823.6 the last line of the Criterion of `estimate-prespec-hook-reports-a-pointer-outside-a-bracket` changes on purpose: an item of an Estimate of a core target is now judged. The insight line of `estimate-orchestration-defer-example-passes-the-hook` now says what holds: `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands under `vault/archive/migration/2026-10-10/1555/insights/` with `status: archived`.
>
> The check of Case 823.1 is a new Estimate. `.guppi/tests/test_guppi_package.py` already runs `ship.ship` over the live repository with a version it passes itself, so a test can read the real build with no tag. That test would fail from Work Mode until the librarian's run lands the new texts, against `rule-retro`, which takes no red test as expected, and it would join the runs of `estimate-clean-branch-writes-a-clean-copy` and `estimate-clean-branch-ships-the-tests` over `test_ship.py`. So, as the person chose, it carries the pytest marker `live`, which the default run of `.guppi/pyproject.toml` leaves out, and the new Estimate runs it by hand with `-m live` after the librarian's run of this session; the Retro stays green, and those two Estimates are not touched. `vault/wiki/brief.md` `## Readings at the close` reports the last run of the tests: "`make test`: 1 failed, 1699 passed, 6 skipped (exit 2)."
>
> A Grep of `pointer outside` over `vault/wiki/` printed `case-schema.md`, `estimate-clean-branch-ships-the-passed-estimates`, `estimate-clean-branch-writes-a-clean-copy`, `rule-lint`, `rule-clean-branch`, `estimate-clean-branch-ships-the-tests`, `rule-case-protocol` and `estimate-clean-branch-pages-hold-pointers-only-in-brackets`; over `.claude/` it printed nothing. Each hit stays true:
> - `rule-clean-branch` still exits 1 on each pointer and says a Case rewords the text at its source.
> - `/pre-spec` still finds a pointer in the new text of a page with `core: true`, as `rule-clean-branch`, `rule-case-protocol` and its Render `case-schema.md` say. Case 823.6 only adds the Estimates of such pages.
> - The Criterion of `estimate-clean-branch-ships-the-passed-estimates` still holds: a pointer in a shipped Estimate makes the build exit 1.
> - `rule-lint` speaks of `guppi ship --check` alone.
>
> The Frontier items C4 (`estimate-clean-branch-pages-hold-pointers-only-in-brackets`, `rule-rules-schema`), C1 (the tag and `prod.yml`), C6 and C9 are not touched here. The draft pages with `core: true` still stop the build after this Case.
>
> For Case 823.6 the new Criterion of an Estimate is read by `/pre-spec` in `criterion_notes` of `.guppi/guppi/prespec.py`: `written_criterion` of the item, else `criterion_text(case_texts(...))`. `lift_criterion` of `.guppi/guppi/materialize.py`, the writer, lifts the same. The two part only on a Criterion written under `sections` as blank text. There `lift_criterion` keeps the blank and `criterion_notes` reads the Case's `when` and `then`. That gap stands as before: Case 823.6 moves the reading of `criterion_notes` into one function that both checks of `prespec.py` call, and names `lift_criterion` as no shared judgment. A Grep of `def check_pointers|def written_texts|def core_as_left` over `.guppi/guppi/` found each only in `prespec.py`, so the widened check adds no second copy.

> **problem:**
> Sixteen shipped Estimates hold pointers outside a bracket, so every build of `prod` exits 1, and `/pre-spec` cannot catch a new one in an Estimate.

> **recommend:**
> - **How does the build stop failing on these Estimates?**
>   - Recommended: (a) leave such an Estimate out of the copy.
>   - Answer: the pages must be rewritten, (b).
> - **Does `/pre-spec` catch such a reference in the new text of an Estimate?**
>   - Recommended: (b) add it as a sub-case.
>   - Answer: (b).
> - **How is a reference in a `method` reworded?**
>   - Recommended: (a) move the reference into a bracket at the end, and fix the wait where `/pre-spec` would report it.
>   - Answer: agreed, (a).
> - **How are the four Estimates whose Criterion changes read again?**
>   - Recommended: (a) give those two a `method` that runs in this session.
>   - Answer: agreed, (a).
> - **What checks that no shipped Estimate holds such a reference?**
>   - Recommended: (a) a new Estimate with a test over the live repository.
>   - Answer: agreed, (a).
> - **What checks that `/pre-spec` judges the new text of an Estimate?**
>   - Recommended: (a) replace that Estimate's Criterion.
>   - Answer: agreed, (a).
> - **What does the line on the insight say in the new Criterion of the defer-example Estimate?**
>   - Recommended: (a) say what holds now, the reference in a closing bracket.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a `/pre-spec` finding — seven new methods said "the session that set this method", which would point at this session.
>   - Taken: each names the session by what happened in it, its pointer in the bracket at its end.
> - **Change**
>   - Asked: a `/pre-spec` finding — `form_finding` is a nested function of `.guppi/guppi/prespec.py`, not of `lint.py`.
>   - Taken: `context` says so.
> - **Change**
>   - Asked: a `/pre-spec` finding — the live test is red until the librarian's run; the person chose a pytest marker that the default run leaves out.
>   - Taken: the test carries the marker `live`, `.guppi/pyproject.toml` registers it and leaves it out by default, and the new Estimate runs it with `-m live`.
> - **Change**
>   - Asked: a `/pre-spec` finding — the Criterion of Case 823.2 asked what only a later `case-guppi` shows; the person chose to drop that sentence.
>   - Taken: the sentence is dropped; the Estimate promises the note of the hook alone.

### Case 823.1 — The shipped Estimates hold each pointer in a bracket

> **given:**
> `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets`: the new check of the Estimates the build takes.
> **＋** `estimate-ask-finds`: its `method` is set anew.
> **＋** `estimate-ask-query-before-a-create`: its `method` is set anew.
> **＋** `estimate-ask-opens-a-decision-only-for-a-finding`: its `method` is set anew.
> **＋** `estimate-case-check-sends-back-a-faulty-round`: its `method` is set anew.
> **＋** `estimate-orchestration-acknowledges-the-opening-with-the-frontier`: its `method` is set anew.
> **＋** `estimate-orchestration-names-related-cases-in-the-dispatch`: its `method` is set anew.
> **＋** `estimate-orchestration-signs-items-taken-together`: its `method` is set anew.
> **＋** `estimate-prespec-confirms-the-findings-once`: its `method` is set anew.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: its `method` is set anew.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: its `method` is set anew.
> **＋** `estimate-skill-sprint-open-merges-the-closed-sprint-branch`: its `method` is set anew.
> **＋** `estimate-sprint-close-next-session-opens-the-sprint`: its `method` is set anew.
> **＋** `estimate-clean-branch-pages-hold-pointers-only-in-brackets`: the check of the pages with `core: true`, which stays apart.
> **＋** `vault/wiki/estimates/`: the folder of the Estimates the build takes.
> **＋** `.guppi/tests/test_ship.py`: the tests of the build, which gain one over the live repository.
> **＋** `.guppi/pyproject.toml`: the settings of pytest, which register the marker `live` and leave it out by default.
> **＋** `.guppi/guppi/ship.py`: the build of the clean version.
> **＋** `.guppi/guppi/pointers.py`: the one judgment of a pointer outside a bracket.
> **＋** `rule-clean-branch`: the rule that a pointer stands in a bracket of its own.

> **when:**
> `.guppi/tests/test_ship.py` runs under `uv run --project .guppi pytest -m live` and builds, by `ship` of `.guppi/guppi/ship.py`, the clean version of this repository from its working tree into a temporary folder, with a version the test passes itself.

> **then:**
> No `ship:` line of that build names a page under `vault/wiki/estimates/`.
> **＋** Each Estimate of this repository that the build takes holds each pointer to a case, a decision or a session in its `purpose`, its `method` and its `## Criterion` in a bracket of its own at the end of its sentence, as `outside` of `.guppi/guppi/pointers.py` judges it.
> **＋** Each such Estimate keeps every pointer it held, with the words that go with it, in that bracket.
> **－** The test reads no tag `prod-x.y.z`, and a page with `core: true` stays with `estimate-clean-branch-pages-hold-pointers-only-in-brackets`.
> **－** A run of `uv run --project .guppi pytest` without `-m live` leaves the test out, by the settings of `.guppi/pyproject.toml`.

> **tasks:**
> - [ ] create `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether each Estimate that guppi ship takes into the clean version holds each pointer to a case, a decision or a session in a bracket of its own, so that the build prints no line on it`
>   - method: `by hand, after the librarian's run of this session: uv run --project .guppi pytest .guppi/tests/test_ship.py -m live, read against the Criterion`
>   - tags: `[ci, plugin]`
> - [ ] update `estimate-ask-finds`
>   - set:
>     ```
>     method: "by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the answer of ask-guppi in its agent transcript read against the Criterion and the event log, recorded in the estimate line (the render of case 782)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end`
> - [ ] update `estimate-ask-query-before-a-create`
>   - set:
>     ```
>     method: "by hand, after a case-guppi builds a Case with a create without a ref on the rendered .claude/agents/ask-guppi.md: its transcript, its Grep and Glob calls and the context of its Case read against the Criterion, recorded in the estimate line (the render of case 626.1)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end, and the method waits for the event it names`
> - [ ] update `estimate-ask-opens-a-decision-only-for-a-finding`
>   - set:
>     ```
>     method: "by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript and the findings of its answer read against the Criterion, recorded in the estimate line (the render of case 800.2)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end`
> - [ ] update `estimate-case-check-sends-back-a-faulty-round`
>   - set:
>     ```
>     method: "uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form whose After lines have no dash, a round in form whose After lines have the dash, a title line without the colon, a question with no Now line, no lone Options label, no option with an After line and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand at the Retro of a session in which a case-guppi answered with a round, uv run --project .guppi guppi casecheck --subagent run from the repository with a payload on stdin of agent_type case-guppi and an agent_transcript_path to a copy, in the scratchpad, of a transcript of a case-guppi of that session cut after a round and before any Write of a case file: the copy as cut exits 0 and prints nothing; the copy with the colon removed from a title line of its last round exits 2, its stderr naming that question, the title line it misses, and telling case-guppi to answer with the round whole again; the same faulty round added again as a later output exits 0; the plan file of the session is unchanged by the runs (the reading taken at the Retro of the session of case 747)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end`
> - [ ] update `estimate-orchestration-acknowledges-the-opening-with-the-frontier`
>   - set:
>     ```
>     method: "by hand, at the Retro of the session whose Spec set the new Render of rule-orchestration that the Criterion describes, that Render in its spec.md read against the Criterion (the session of case 769)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end`
> - [ ] update `estimate-orchestration-names-related-cases-in-the-dispatch`
>   - set:
>     ```
>     method: "by hand at the Retro of the session that dispatched case-guppi for the Cases of a batch with their related Cases: the Agent calls of that dispatch in its transcript, read against the Criterion (session 2249, Cases 682 and 683); a Case of the batch or a related Case left unnamed counted in the reading line"
>     ```
>   - change: `the pointers of the method stand in a bracket at the end of their sentence`
> - [ ] update `estimate-orchestration-signs-items-taken-together`
>   - set:
>     ```
>     method: "by hand at the Retro of the session that took up the Cases of a batch together with a Case built again: the replies in its transcript from the dispatch of those Cases to the reply that acknowledged that batch, read against the Criterion (session 2249, Cases 682 and 683 with Case 681 built again)"
>     ```
>   - change: `the pointers of the method stand in a bracket at its end`
> - [ ] update `estimate-prespec-confirms-the-findings-once`
>   - set:
>     ```
>     method: "by hand, after a /pre-spec whose findings send a Case back to its case-guppi, on the rendered .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line (the render of case 638)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end, and the method waits for the event it names`
> - [ ] update `estimate-search-leaves-out-decisions-in-every-agent`
>   - set:
>     ```
>     method: "by hand, after a session that runs on the rendered .claude/rules/search-leaves-out-decisions.md: the transcripts of the main agent and of each ask-guppi and case-guppi of that session, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line (the render of case 664.1)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end, and the method waits for the event it names`
> - [ ] update `estimate-skill-sprint-close-leads-the-closing-session`
>   - set:
>     ```
>     method: "by hand, at the Retro of the session whose Spec set the new Render of rule-skill-sprint-close that the Criterion describes, that Render in its spec.md, vault/wiki/orchestration.md and entity-sprint-migration under vault/archive/migration/ read against the Criterion (the session of case 791)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end`
> - [ ] update `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
>   - set:
>     ```
>     method: "by hand, at the Retro of the session whose Spec set the new Render of rule-skill-sprint-open that the Criterion describes, that Render in its spec.md read against the Criterion (the session of case 789)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end`
> - [ ] update `estimate-sprint-close-next-session-opens-the-sprint`
>   - set:
>     ```
>     method: "pytest .guppi/tests/test_ledger.py -k sprint and .guppi/tests/test_materialize.py -k sprint; by hand, at the Retro of the session whose Spec set the step of the Render of rule-brief that writes the first line of the brief's Cases, .claude/skills/hi/SKILL.md, .claude/skills/sprint-open/SKILL.md and that step read against the Criterion (the session of case 779)"
>     ```
>   - change: `the pointer of the method stands in a bracket at its end`
> - [ ] `.guppi/pyproject.toml`: under `[tool.pytest.ini_options]`, the marker `live` registered under `markers`, and `addopts` that leaves it out, `-m "not live"`; a comment there holds no pointer.
> - [ ] `.guppi/tests/test_ship.py`: a test marked `live`, whose name does not hold `estimate`, runs `ship.ship` over this repository into `tmp_path` with a version it passes, and asserts that no line it gives back names a page under `vault/wiki/estimates/`.
> - [ ] read `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 823.1][create][estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets]{ref:rule-clean-branch}{tags:ci,plugin}
> - decision[case 823.1][update][estimate-ask-finds]{ref:rule-ask}
> - decision[case 823.1][update][estimate-ask-query-before-a-create]{ref:rule-ask}
> - decision[case 823.1][update][estimate-ask-opens-a-decision-only-for-a-finding]{ref:rule-ask}
> - decision[case 823.1][update][estimate-case-check-sends-back-a-faulty-round]{ref:rule-case-check}
> - decision[case 823.1][update][estimate-orchestration-acknowledges-the-opening-with-the-frontier]{ref:rule-orchestration}
> - decision[case 823.1][update][estimate-orchestration-names-related-cases-in-the-dispatch]{ref:rule-orchestration}
> - decision[case 823.1][update][estimate-orchestration-signs-items-taken-together]{ref:rule-orchestration}
> - decision[case 823.1][update][estimate-prespec-confirms-the-findings-once]{ref:rule-prespec}
> - decision[case 823.1][update][estimate-search-leaves-out-decisions-in-every-agent]{ref:rule-search-leaves-out-decisions}
> - decision[case 823.1][update][estimate-skill-sprint-close-leads-the-closing-session]{ref:rule-skill-sprint-close}
> - decision[case 823.1][update][estimate-skill-sprint-open-merges-the-closed-sprint-branch]{ref:rule-skill-sprint-open}
> - decision[case 823.1][update][estimate-sprint-close-next-session-opens-the-sprint]{ref:rule-sprint-close}
> ```

### Case 823.2 — The sibling note keeps its pointer in a bracket

> **given:**
> `estimate-case-check-notes-a-then-line-shared-by-siblings`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the check of an answer of `case-guppi`.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the check of the plan.
> **＋** `rule-case-check`: the rule of the check.

> **when:**
> `uv run --project .guppi guppi casecheck --subagent` checks an answer of `case-guppi` on `SubagentStop`, or `uv run --project .guppi guppi prespec --check <plan>` checks the plan, and the answer or the plan holds two or more sub-cases of one parent.

> **then:**
> Two `then` lines of two sibling sub-cases (sub-cases of one parent, such as N.1 and N.2) are a note when the words that both lines hold make 60 percent or more of the words of the shorter line. A word is a run of letters and digits of four or more characters, and the case of letters is set aside.
> **＋** The note names both Cases and both lines, and it goes where every other note of the check goes (the notes of case 472.1).
> **－** A line with no word of four or more characters is compared with no line.
> **－** A sub-case that the answer holds alone has no sibling in the answer and gets no note from `guppi casecheck`. `guppi prespec --check` compares it with its siblings in the plan.

> **tasks:**
> - [ ] update `estimate-case-check-notes-a-then-line-shared-by-siblings`
>   - set:
>     ```
>     status: pending
>     method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py .guppi/tests/test_prespec.py -k sibling
>     ```
>   - change: `the Criterion replaced whole — its pointer stands in a bracket, it promises the note of the hook alone, and the method keeps its pytest run alone`
> - [ ] read `estimate-case-check-notes-a-then-line-shared-by-siblings`

> **ratification:**
> ```
> - decision[case 823.2][update][estimate-case-check-notes-a-then-line-shared-by-siblings]{ref:rule-case-check}
> ```

### Case 823.3 — The hold of a ledger line keeps its pointer in a bracket

> **given:**
> `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ledger.py`: the `Stop` hook that writes the ledger.
> **＋** `.guppi/guppi/casecheck.py`: the check whose store the hook reads.
> **＋** `.guppi/guppi/materialize.py`: the reader of a ledger line.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the hook.
> **＋** `rule-ledger-write`: the rule of the hook.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a decision line of a kind other than `defer` that no ledger holds yet.

> **then:**
> The hook compares the line, a `{addresses:<slug>}` block and trailing spaces set aside, with the ledger lines of the `ratification` of the entry stored under its Case id alone in `<plan>.checked.json`, read by the function of `.guppi/guppi/casecheck.py` by which the `Stop` check of a showing reads them.
> **＋** A line equal to one of them lands as before.
> **＋** A line equal to none of them, a line of a Case the store holds no text for, and a line of a session with no plan file is not written; the other lines of the `Stop` land.
> **＋** For such a line of the reply just finished, the hook exits 2 and prints: "ledger: decision[case <N>] not written — it is not a line of the ratification case-guppi stored for case <N>: copy it again as the summary of case-guppi holds it, alone in a LEDGER block, or send the Case back to its case-guppi when the stored line is wrong."
> **＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
> **＋** A held line is judged again at every `Stop` while it stands in a text of the transcript, and never lands while it differs; a line written again that equals a stored line lands.
> **＋** A line written again with `{addresses:<slug>}` added lands when the line without the mark equals a stored line (the mark Case 685 asks for).
> **－** A `defer` line, an `estimate` line and a `lesson` line are not compared.
> **－** A line that `parse_line` of `.guppi/guppi/materialize.py` cannot read, and a line the hook refuses while no live sprint page stands, get that refusal alone and are not compared.
> **－** With `stop_hook_active` set the hook judges the line the same; with the flag set and a transcript it cannot read, the line does not land and the hook prints nothing.

> **tasks:**
> - [ ] update `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — its pointer stands in a bracket at the end of its sentence`
> - [ ] read `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`

> **ratification:**
> ```
> - decision[case 823.3][update][estimate-ledger-write-holds-a-decision-line-off-the-stored-case]{ref:rule-ledger-write}
> ```

### Case 823.4 — The defer example says where its insight stands

> **given:**
> `estimate-orchestration-defer-example-passes-the-hook`: its Criterion is replaced whole.
> **＋** `.guppi/tests/test_orchestration.py`: the test of the example.
> **＋** `vault/wiki/orchestration.md`: the Render of `rule-orchestration` that holds the example.
> **＋** `.guppi/guppi/ratified.py`: the functions of the `Stop` hook of `rule-spec-write`.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept`: the insight the example addressed, now archived.
> **＋** `rule-orchestration`: the rule of the example.

> **when:**
> `.guppi/tests/test_orchestration.py` runs under `uv run --project .guppi pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `.guppi/guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
> **＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
> **＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
> **＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `.guppi/guppi/ratified.py`, and holds no copy of either.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands archived with `status: archived` (addressed by case 651.3).
> **－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, both tests of `.guppi/tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

> **tasks:**
> - [ ] update `estimate-orchestration-defer-example-passes-the-hook`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — its pointer stands in a bracket, and the insight stands archived`
> - [ ] read `estimate-orchestration-defer-example-passes-the-hook`

> **ratification:**
> ```
> - decision[case 823.4][update][estimate-orchestration-defer-example-passes-the-hook]{ref:rule-orchestration}
> ```

### Case 823.5 — The sprint form of a Case id keeps its pointers in brackets

> **given:**
> `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/caseid.py`: the one reader of a Case id and the command `caseid`.
> **＋** `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py` and `.guppi/guppi/materialize.py`: the readers of a Case id.
> **＋** `.guppi/tests/test_caseid.py`: the tests of the Case id.
> **＋** `vault/wiki/orchestration.md` and `vault/wiki/ratification.md`: the Renders of `rule-orchestration` and `rule-ratification` the reading reads.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of a session, where the command finds the open sprint.
> **＋** `vault/wiki/sprint.md`: the sprint file the command reads when no ledger line names a sprint.
> **＋** `/sprint-open`: the skill that sets the id of the opening Case of a sprint.
> **＋** `rule-ratification`: the rule of the Case id.

> **when:**
> `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py` or `.guppi/guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
> **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run --project .guppi guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
> **＋** Or `uv run --project .guppi guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.

> **then:**
> A Case id of a sprint opened after sprint ids came in is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case (sprint ids came in with case 788.2).
> **＋** The readers read a Case id through `.guppi/guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
> **＋** The sprints `migration` and `plugin` keep plain ids to their close, by a fixed list in `.guppi/guppi/caseid.py` (both opened before case 788.2).
> **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
> **＋** `uv run --project .guppi guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
> **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
> **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
> **－** The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id.
> **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
> **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
> **－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.

> **tasks:**
> - [ ] update `estimate-ratification-case-id-carries-the-sprint`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_caseid.py; by hand at the Retro of the session that sets this method: the Render of rule-orchestration in vault/wiki/orchestration.md and the Render of rule-ratification in vault/wiki/ratification.md read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — its pointers stand in brackets; the method reads the live Renders`
> - [ ] read `estimate-ratification-case-id-carries-the-sprint`

> **ratification:**
> ```
> - decision[case 823.5][update][estimate-ratification-case-id-carries-the-sprint]{ref:rule-ratification}
> ```

### Case 823.6 — Pre-spec finds a pointer in the new text of a shipped Estimate

> **given:**
> `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`: its Criterion and its `purpose` are replaced.
> **＋** `.guppi/guppi/prespec.py`: the check of the plan, its `check_pointers`, `written_texts` and `criterion_notes`.
> **＋** `.guppi/guppi/pointers.py`: the one judgment of a pointer outside a bracket.
> **＋** `decision-case-N`: the form of the id of a decision, one kind of pointer.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the check of the plan.
> **＋** `rule-prespec-hook`: the rule of the check at `ExitPlanMode`.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

> **then:**
> It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
> **＋** It prints the same finding for an item of an Estimate whose target, the `ref` of a `create` or the `target` of the live page, carries `core: true` on the live page or as the plan leaves it: in its `purpose`, its `method`, each `sections` value it writes and its new `## Criterion`.
> **＋** The new `## Criterion` of such an Estimate is the one the item writes under `sections`, else the `when` and `then` of its Case, for a `create` and for an `update` that names no part of the page, read by the one function of `.guppi/guppi/prespec.py` by which the note on a Criterion line not carried reads it.
> **＋** The finding names the Case, the page and the pointer.
> **＋** It judges each text by `outside` of `.guppi/guppi/pointers.py`, imported, the judgment that `guppi ship` runs over the files it writes.
> **－** A pointer inside such a bracket, a code span or a fenced block is no finding.
> **－** An item for a page without `core: true` that is no such Estimate, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

> **tasks:**
> - [ ] update `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the check of the plan finds a pointer to a case, a decision or a session that stands outside a bracket of its own in the new text of a page with core: true, or of an Estimate whose target carries core: true, its method and its new Criterion included"
>     ```
>   - change: `the Criterion replaced whole — pre-spec judges the new text of an Estimate whose target carries core: true`
> - [ ] `.guppi/guppi/prespec.py`: the reading of the new Criterion in `criterion_notes` moves into one function that `criterion_notes` and `check_pointers` call; `check_pointers` takes the Cases of the plan and judges an Estimate whose target carries `core: true`, by `core_as_left` over the item of the plan that writes the target, else over its live page; `written_texts` adds the `method` of a `create` and of `set`; the module docstring says it.
> - [ ] `.guppi/tests/test_prespec.py`: tests whose names hold `pointer` — a pointer outside a bracket in the `method`, in a `sections` value and in the `when` or `then` of the Case of an Estimate of a core target is a finding; the same in an Estimate of a target without `core` is none; an `update` that names a part has no new Criterion judged.
> - [ ] read `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`

> **ratification:**
> ```
> - decision[case 823.6][update][estimate-prespec-hook-reports-a-pointer-outside-a-bracket]{ref:rule-prespec-hook}
> ```
