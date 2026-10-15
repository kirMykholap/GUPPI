<!-- approved 22:36:32 · session 2f0f015b -->

# Session 1959

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

```then
create:
- slug: estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets
  ref: rule-clean-branch
  kind: QA
  purpose: Whether each Estimate that guppi ship takes into the clean version holds each pointer to a case, a decision or a session in a bracket of its own, so that the build prints no line on it
  method: 'by hand, after the librarian''s run of this session: uv run --project .guppi pytest .guppi/tests/test_ship.py -m live, read against the Criterion'
  tags:
  - ci
  - plugin
update:
- slug: estimate-ask-finds
  set:
    method: 'by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the answer of ask-guppi in its agent transcript read against the Criterion and the event log, recorded in the estimate line (the render of case 782)'
  change: the pointer of the method stands in a bracket at its end
- slug: estimate-ask-query-before-a-create
  set:
    method: 'by hand, after a case-guppi builds a Case with a create without a ref on the rendered .claude/agents/ask-guppi.md: its transcript, its Grep and Glob calls and the context of its Case read against the Criterion, recorded in the estimate line (the render of case 626.1)'
  change: the pointer of the method stands in a bracket at its end, and the method waits for the event it names
- slug: estimate-ask-opens-a-decision-only-for-a-finding
  set:
    method: 'by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript and the findings of its answer read against the Criterion, recorded in the estimate line (the render of case 800.2)'
  change: the pointer of the method stands in a bracket at its end
- slug: estimate-case-check-sends-back-a-faulty-round
  set:
    method: 'uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form whose After lines have no dash, a round in form whose After lines have the dash, a title line without the colon, a question with no Now line, no lone Options label, no option with an After line and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand at the Retro of a session in which a case-guppi answered with a round, uv run --project .guppi guppi casecheck --subagent run from the repository with a payload on stdin of agent_type case-guppi and an agent_transcript_path to a copy, in the scratchpad, of a transcript of a case-guppi of that session cut after a round and before any Write of a case file: the copy as cut exits 0 and prints nothing; the copy with the colon removed from a title line of its last round exits 2, its stderr naming that question, the title line it misses, and telling case-guppi to answer with the round whole again; the same faulty round added again as a later output exits 0; the plan file of the session is unchanged by the runs (the reading taken at the Retro of the session of case 747)'
  change: the pointer of the method stands in a bracket at its end
- slug: estimate-orchestration-acknowledges-the-opening-with-the-frontier
  set:
    method: by hand, at the Retro of the session whose Spec set the new Render of rule-orchestration that the Criterion describes, that Render in its spec.md read against the Criterion (the session of case 769)
  change: the pointer of the method stands in a bracket at its end
- slug: estimate-orchestration-names-related-cases-in-the-dispatch
  set:
    method: 'by hand at the Retro of the session that dispatched case-guppi for the Cases of a batch with their related Cases: the Agent calls of that dispatch in its transcript, read against the Criterion (session 2249, Cases 682 and 683); a Case of the batch or a related Case left unnamed counted in the reading line'
  change: the pointers of the method stand in a bracket at the end of their sentence
- slug: estimate-orchestration-signs-items-taken-together
  set:
    method: 'by hand at the Retro of the session that took up the Cases of a batch together with a Case built again: the replies in its transcript from the dispatch of those Cases to the reply that acknowledged that batch, read against the Criterion (session 2249, Cases 682 and 683 with Case 681 built again)'
  change: the pointers of the method stand in a bracket at its end
- slug: estimate-prespec-confirms-the-findings-once
  set:
    method: 'by hand, after a /pre-spec whose findings send a Case back to its case-guppi, on the rendered .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line (the render of case 638)'
  change: the pointer of the method stands in a bracket at its end, and the method waits for the event it names
- slug: estimate-search-leaves-out-decisions-in-every-agent
  set:
    method: 'by hand, after a session that runs on the rendered .claude/rules/search-leaves-out-decisions.md: the transcripts of the main agent and of each ask-guppi and case-guppi of that session, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line (the render of case 664.1)'
  change: the pointer of the method stands in a bracket at its end, and the method waits for the event it names
- slug: estimate-skill-sprint-close-leads-the-closing-session
  set:
    method: by hand, at the Retro of the session whose Spec set the new Render of rule-skill-sprint-close that the Criterion describes, that Render in its spec.md, vault/wiki/orchestration.md and entity-sprint-migration under vault/archive/migration/ read against the Criterion (the session of case 791)
  change: the pointer of the method stands in a bracket at its end
- slug: estimate-skill-sprint-open-merges-the-closed-sprint-branch
  set:
    method: by hand, at the Retro of the session whose Spec set the new Render of rule-skill-sprint-open that the Criterion describes, that Render in its spec.md read against the Criterion (the session of case 789)
  change: the pointer of the method stands in a bracket at its end
- slug: estimate-sprint-close-next-session-opens-the-sprint
  set:
    method: pytest .guppi/tests/test_ledger.py -k sprint and .guppi/tests/test_materialize.py -k sprint; by hand, at the Retro of the session whose Spec set the step of the Render of rule-brief that writes the first line of the brief's Cases, .claude/skills/hi/SKILL.md, .claude/skills/sprint-open/SKILL.md and that step read against the Criterion (the session of case 779)
  change: the pointer of the method stands in a bracket at its end
```

```tasks
- [ ] create `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets`
- [ ] update `estimate-ask-finds`
- [ ] update `estimate-ask-query-before-a-create`
- [ ] update `estimate-ask-opens-a-decision-only-for-a-finding`
- [ ] update `estimate-case-check-sends-back-a-faulty-round`
- [ ] update `estimate-orchestration-acknowledges-the-opening-with-the-frontier`
- [ ] update `estimate-orchestration-names-related-cases-in-the-dispatch`
- [ ] update `estimate-orchestration-signs-items-taken-together`
- [ ] update `estimate-prespec-confirms-the-findings-once`
- [ ] update `estimate-search-leaves-out-decisions-in-every-agent`
- [ ] update `estimate-skill-sprint-close-leads-the-closing-session`
- [ ] update `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
- [ ] update `estimate-sprint-close-next-session-opens-the-sprint`
- [x] `.guppi/pyproject.toml`: under `[tool.pytest.ini_options]`, the marker `live` registered under `markers`, and `addopts` that leaves it out, `-m "not live"`; a comment there holds no pointer.
- [x] `.guppi/tests/test_ship.py`: a test marked `live`, whose name does not hold `estimate`, runs `ship.ship` over this repository into `tmp_path` with a version it passes, and asserts that no line it gives back names a page under `vault/wiki/estimates/`.
- [ ] read `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets`
```

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

```then
update:
- slug: estimate-case-check-notes-a-then-line-shared-by-siblings
  set:
    status: pending
    method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py .guppi/tests/test_prespec.py -k sibling
  change: the Criterion replaced whole — its pointer stands in a bracket, it promises the note of the hook alone, and the method keeps its pytest run alone
```

```tasks
- [ ] update `estimate-case-check-notes-a-then-line-shared-by-siblings`
- [ ] read `estimate-case-check-notes-a-then-line-shared-by-siblings`
```

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

```then
update:
- slug: estimate-ledger-write-holds-a-decision-line-off-the-stored-case
  set:
    status: pending
  change: the Criterion replaced whole — its pointer stands in a bracket at the end of its sentence
```

```tasks
- [ ] update `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`
- [ ] read `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`
```

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

```then
update:
- slug: estimate-orchestration-defer-example-passes-the-hook
  set:
    status: pending
  change: the Criterion replaced whole — its pointer stands in a bracket, and the insight stands archived
```

```tasks
- [ ] update `estimate-orchestration-defer-example-passes-the-hook`
- [ ] read `estimate-orchestration-defer-example-passes-the-hook`
```

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

```then
update:
- slug: estimate-ratification-case-id-carries-the-sprint
  set:
    status: pending
    method: 'uv run --project .guppi pytest .guppi/tests/test_caseid.py; by hand at the Retro of the session that sets this method: the Render of rule-orchestration in vault/wiki/orchestration.md and the Render of rule-ratification in vault/wiki/ratification.md read against the Criterion'
  change: the Criterion replaced whole — its pointers stand in brackets; the method reads the live Renders
```

```tasks
- [ ] update `estimate-ratification-case-id-carries-the-sprint`
- [ ] read `estimate-ratification-case-id-carries-the-sprint`
```

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

```then
update:
- slug: estimate-prespec-hook-reports-a-pointer-outside-a-bracket
  set:
    status: pending
    purpose: 'Whether the check of the plan finds a pointer to a case, a decision or a session that stands outside a bracket of its own in the new text of a page with core: true, or of an Estimate whose target carries core: true, its method and its new Criterion included'
  change: 'the Criterion replaced whole — pre-spec judges the new text of an Estimate whose target carries core: true'
```

```tasks
- [ ] update `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
- [x] `.guppi/guppi/prespec.py`: the reading of the new Criterion in `criterion_notes` moves into one function that `criterion_notes` and `check_pointers` call; `check_pointers` takes the Cases of the plan and judges an Estimate whose target carries `core: true`, by `core_as_left` over the item of the plan that writes the target, else over its live page; `written_texts` adds the `method` of a `create` and of `set`; the module docstring says it.
- [x] `.guppi/tests/test_prespec.py`: tests whose names hold `pointer` — a pointer outside a bracket in the `method`, in a `sections` value and in the `when` or `then` of the Case of an Estimate of a core target is a finding; the same in an Estimate of a target without `core` is none; an `update` that names a part has no new Criterion judged.
- [ ] read `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
```

## Case 824 — The shipped rules name the languages by role and GUPPI's repository by name

> **context:**
> `guppi ship` of `.guppi/guppi/ship.py` copies each page with `core: true` into the clean version of GUPPI that other projects install. `estimate-clean-branch-ships-neutral-texts` (case 822.7, pending, target `rule-clean-branch`) promises that no sentence of those rules, entities and `CLAUDE.md` holds only in the repository of GUPPI. The `/pre-spec` of session 0553 found that its reading would fail on sentences that call the documentation language English or say "this repository" where the repository of GUPPI is meant (`vault/wiki/brief.md`, `## Next session`). The Renders of `rule-case-build` and `rule-case-protocol` say that the person's answer in `recommend` is written in English. The Purpose of `rule-spec-write` says that `case-guppi` writes the Case in English. The Purpose of `rule-language` says that the manner of the English in the vault is ASD-STE100. In a project whose documentation language is German, each of these sentences is wrong. `rule-morph` says that the copied `guppi.toml` holds the languages and commands "of this repository" and that the read rules name "this repository's" transcripts folder; in an installed project "this repository" is that project, but the values are GUPPI's.
>
> The person chose to reword the five named pages and `rule-permissions` (Q1). A Grep of `this repository|English|Russian|repository of GUPPI` over `vault/wiki/rules/` printed 33 hits in 17 files: `rule-claude-md`, `rule-case-build`, `rule-case-protocol`, `rule-clean-branch`, `rule-entities-schema`, `rule-github-repository`, `rule-guppi-config`, `rule-guppi-package`, `rule-harness`, `rule-morph`, `schema.yaml`, `rule-permissions`, `rule-where-to-stop`, `rule-language`, `rule-spec-write`, `rule-rules-schema` and `rule-skill-wait-what`. Each hit was read. These hits stand:
> - The History lines of `rule-claude-md`, `rule-case-build`, `rule-case-protocol`, `rule-language` and `rule-spec-write`; the Criterion leaves History out.
> - `rule-clean-branch` and `rule-github-repository`, which carry no `core: true` and do not ship.
> - `rule-guppi-config`, `rule-guppi-package` and `rule-harness`, which name the repository of GUPPI as such and so hold in any project.
> - `rule-where-to-stop`, whose sentence on what git in this repository cannot undo holds in any project.
> - `rule-skill-wait-what` and the `## Language` of `rule-case-protocol`, which say that ASD-STE100 is for English only and applies when that language is English.
> - The `core` line of `schema.yaml`, `rule-entities-schema` and `rule-rules-schema`, which this Case leaves to the Frontier item on `rule-rules-schema`.
>
> The same Grep over `vault/wiki/entities/` printed hits in `schema.yaml`, `entity-guppi` and `entity-guppi-repository`. `entity-guppi` already names the repository of GUPPI as such (case 822.7), and `entity-guppi-repository` carries no `core: true`. A Grep of `c--PROJECTS-GUPPI` over `vault/wiki/rules/` printed only `rule-permissions`: two of its hits are in its Render and the third is in its Purpose. The Render is a sample in a fenced block that the Criterion leaves out, and the setup Case of `rule-morph` sets its folder. The Purpose sentence enters this Case. Case 825 of this session renames the install Case of `rule-morph` to the setup Case and sets the whole Purpose of `rule-morph` after this Case. Its new Purpose already names the repository of GUPPI in the two sentences this Case rewords, so the two Cases agree there. This Case calls that Case the setup Case in each sentence it writes. The remaining words "at install" in `rule-permissions` are left to Case 825.
>
> The person chose `{{documentation_lang}}` in the two Renders and plain words in the Purposes (Q2). In this repository both rendered files, `.claude/agents/case-guppi.md` and `vault/wiki/case-schema.md`, read word for word as before, so `uv run --project .guppi guppi render --check` finds no drift. The Criteria of `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-build-writes-the-case` say "in English". They stand: they are true in this repository, and the Criterion of `estimate-clean-branch-ships-neutral-texts` lists such sentences of shipped Estimates for a later Case and does not fail on them. The Criterion of `estimate-permissions` names `c--PROJECTS-GUPPI` and stands for the same reason. An `update` of a Purpose or of a Render touches no Estimate of the live reading (`case-schema.md`, case 378.5). The person chose to name the repository of GUPPI rather than remove the sentences (Q3). A Grep of `case-schema\.md|case-guppi\.md|rule-case-build|rule-case-protocol|rule-language|rule-spec-write\.md|rule-morph|rule-permissions|in English` over `.guppi/tests/` printed `test_render.py`, `test_recall.py`, `test_guard.py`, `test_glossary.py`, `test_config.py` and `test_case_schema.py`. Each of these reads a copy under a temporary folder, except `test_case_schema.py`, which reads only the block tagged `case` of the live `case-example.md` or `case-schema.md`, and this Case does not change that block.
>
> The check is `estimate-clean-branch-ships-neutral-texts`, whose Criterion stands, since it already promises what this Case changes (Q4). Its `method` needs `uv run --project .guppi guppi ship --allow-draft`. The brief's `## Readings due` reports for the reading of `estimate-clean-branch-installs-as-a-plugin`: "`guppi ship --allow-draft` exits 1 with no tag `prod-x.y.z`". `run` of `.guppi/guppi/ship.py` prints "ship: no tag prod-x.y.z in the history of HEAD; nothing written" in that case. The `method` now waits for that tag as an event it names before a colon, the form that `case-schema.md` accepts (case 781). It carries its pointer in a closing bracket. Its target, `rule-clean-branch`, carries no `core: true`, so the widened `/pre-spec` of Case 823.6 does not judge it. The tag itself is another Frontier item of this session. The rule against which each option was judged is the Criterion of `estimate-clean-branch-ships-neutral-texts`. The new text of each pair keeps each pointer it held in a bracket at the end of its sentence (`case-schema.md`, case 807.4). The brief's `## Readings at the close` reports: "`make test`: 1 failed, 1699 passed, 6 skipped (exit 2)". That failure is in `test_guppi_package.py` on `tests/`, and no text of this Case touches it.

> **problem:**
> Shipped rule pages call the documentation language English and say "this repository" where they mean the repository of GUPPI, so they read false in an installed project, and the check that should catch this is due but cannot run without a version tag.

> **recommend:**
> - **Which pages does this Case rewrite?**
>   - Recommended: (b) the five pages and `rule-permissions`.
>   - Answer: agreed, (b).
> - **How does a sentence name the language?**
>   - Recommended: (a) the placeholder in rendered text, plain words elsewhere.
>   - Answer: agreed, (a).
> - **How is a sentence about GUPPI's own repository reworded?**
>   - Recommended: (a) name GUPPI's repository.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (b) that check stands, and its method waits for a tag.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: a `/pre-spec` finding: Case 825 renames the install Case to the setup Case, so this Case should use that name in the sentences it writes.
>   - Taken: the `then` lines on `rule-morph` and `rule-permissions` and the `context` say "setup Case", and `given` names the file of Case 825.

> **given:**
> `rule-language`: the rule of the two languages, whose Purpose names the manner of the vault's text.
> **＋** `rule-case-build` and `rule-case-protocol`: the rules whose Renders say in which language the person's answer stands in `recommend`.
> **＋** `.claude/agents/case-guppi.md` and `vault/wiki/case-schema.md`: the files rendered from those two Renders.
> **＋** `rule-spec-write`: the rule of the Spec hook, whose Purpose says in which language `case-guppi` writes a Case.
> **＋** `rule-morph`: the rule of the setup Case, whose Purpose says what the copied settings hold.
> **＋** `rule-permissions`: the rule of the allow list, whose Purpose names the folder of saved transcripts.
> **＋** `vault/raw/2026-10-15/1959/cases/case-825.md`: the Case that names the setup Case of `rule-morph` and sets its whole Purpose after this Case.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the check of the texts of the clean version, whose `method` is set anew.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, the target of that check.

> **when:**
> Someone reads `rule-language`, `rule-case-build`, `rule-case-protocol`, `rule-spec-write`, `rule-morph` and `rule-permissions` in the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.

> **then:**
> The Purposes of `rule-language` and `rule-spec-write` and the Renders of `rule-case-build` and `rule-case-protocol` name the language of a Case and of the person's answer in it as the documentation language, or by `{{documentation_lang}}`, never as English.
> **＋** `rule-language` says that ASD-STE100 Simplified Technical English is the manner of the vault's text when the documentation language is English.
> **＋** `rule-morph` says that, until the setup Case, `guppi.toml` holds the languages and the commands of the repository of GUPPI, and the read rules of `rule-permissions` name the folder of its saved transcripts.
> **＋** `rule-permissions` says that the folder of saved transcripts is named after the path of the project, and that its read rules name the folder of the repository of GUPPI until the setup Case of `rule-morph` sets the project's own.
> **＋** In the repository of GUPPI each changed sentence keeps its meaning, and `.claude/agents/case-guppi.md` and `vault/wiki/case-schema.md` render word for word as before.
> **－** The Render of `rule-permissions`, the History of each page and the Estimates these pages list do not change.

```then
update:
- slug: rule-language
  replace:
  - old: manner of the English that lands in the vault — ASD-STE100 Simplified Technical English — is the
    new: manner of the text that lands in the vault — ASD-STE100 Simplified Technical English when the documentation language is English — is the
  change: the Purpose names ASD-STE100 only for a documentation language that is English
- slug: rule-spec-write
  replace:
  - old: '`case-guppi` writes the whole Case in English, and a hook copies'
    new: '`case-guppi` writes the whole Case in the documentation language, and a hook copies'
  change: the Purpose names the language of a Case by its role
- slug: rule-case-build
  replace:
  - old: a sub-item `Answer:` with the person's answer in English, both as they stood
    new: a sub-item `Answer:` with the person's answer in {{documentation_lang}}, both as they stood
  change: the Render names the language of an answer in recommend by its placeholder
- slug: rule-case-protocol
  replace:
  - old: what it recommended, the person's answer in English, both as they stood when the person answered it
    new: what it recommended, the person's answer in {{documentation_lang}}, both as they stood when the person answered it
  - old: a sub-item `Answer:`, the person's answer in English, both as they stood
    new: a sub-item `Answer:`, the person's answer in {{documentation_lang}}, both as they stood
  change: the Render names the language of an answer in recommend by its placeholder
- slug: rule-morph
  replace:
  - old: the commands of the keys `test` and `style` of this repository,
    new: the commands of the keys `test` and `style` of the repository of GUPPI,
  - old: name the folder of this repository's saved transcripts under `~/.claude/projects`,
    new: name the folder of the saved transcripts of the repository of GUPPI under `~/.claude/projects`,
  change: the Purpose names the repository of GUPPI where it meant it by this repository
- slug: rule-permissions
  replace:
  - old: 'The saved transcripts of this project, under `~/.claude/projects/c--PROJECTS-GUPPI/` outside the repository, are on the list for reading only:'
    new: 'The saved transcripts of the project, under a folder of `~/.claude/projects/` named after the path of the project outside the repository, such as `c--PROJECTS-GUPPI` for the repository of GUPPI, are on the list for reading only:'
  - old: 'The folder name follows where this repository sits on the person''s disk:'
    new: 'The read rules name the folder of the repository of GUPPI, after where that repository sits on the person''s disk:'
  change: the Purpose names the folder of saved transcripts by how it is named, and the repository of GUPPI where it meant it by this repository
- slug: estimate-clean-branch-ships-neutral-texts
  set:
    method: 'by hand, after a tag prod-x.y.z stands in the history of HEAD and after the librarian''s run of the session that set this method: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and the pages and the files it wrote read against the Criterion, each sentence that holds only in the repository of GUPPI listed in the estimate line (the session of case 824)'
  change: the method waits for a tag prod-x.y.z, without which guppi ship writes nothing
```

```tasks
- [ ] update `rule-language`
- [ ] update `rule-spec-write`
- [ ] update `rule-case-build`
- [ ] update `rule-case-protocol`
- [ ] update `rule-morph`
- [ ] update `rule-permissions`
- [ ] update `estimate-clean-branch-ships-neutral-texts`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
```

## Case 825 — Setup comes before the first sprint at the first /hi

> **context:**
> A new project gets GUPPI in three moves. The person installs the plugin `guppi`, types `/guppi:install`, which only copies the files and builds the Python environment, then reopens Claude Code and types `/hi`. Two pages claim that first `/hi`. `rule-morph` puts the Case that sets the project's settings first (case 817). The session files that `guppi ship` writes make `/hi` start `/sprint-open` first, so the first sprint opens (case 822.3, `estimate-clean-branch-writes-the-session-files`). Neither page gives an order. The pages also call the setup "the install Case" and "the install step", which reads as if `/guppi:install` were itself a Case.
>
> The person chose setup first and the sprint after it, in the same session (Q1). They chose the name "setup" for the Case, "install" only for `/guppi:install` (Q2). They chose the Purpose of `rule-morph` as the one place that tells the whole start in order (Q3), and the Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` replaced whole as the check (Q4). The person also said that `/guppi:install` is no Case and is never ratified, and that the setup is a Case. The new Purpose says both.
>
> The rule that governs the order is the ledger hook of `rule-ledger-write`. `refused_without_sprint` of `.guppi/guppi/ledger.py` refuses each decision line but a `defer` while no live `entity-sprint-` page stands, until a `create` of one stands. The Render of `rule-skill-sprint-open` says "the opening Case is the first Case the session ratifies", and its first step says that no other item is taken up before the opening Case is ratified. The Render of `rule-skill-hi` starts `/sprint-open` first when the brief opens with `open the next sprint`. The Criterion of `estimate-sprint-close-next-session-opens-the-sprint` promises that refusal, and the Criterion of `estimate-skill-sprint-open-starts-at-hi` promises the hook line at `/hi`. These texts stand in this Case. They state what the code and the live skills do today. The key of `guppi.toml` that marks the setup as done does not exist yet. A live skill that waited for that key would show a setup Case in the repository of GUPPI too. So the new Purpose of `rule-morph` says that these steps, the pass of the ledger hook and the key are built in the milestone The plugin, and the milestone line of `entity-sprint-plugin` names them as what remains. The Case that builds them changes those Renders, that rule and those two Estimates. `estimate-clean-branch-writes-the-session-files` and its sentence in `rule-clean-branch`, that the first `/hi` starts `/sprint-open` before the Frontier, stand. With setup first, `/sprint-open` still starts before the Frontier.
>
> A Grep of `install Case|install step|install as done` over `vault/wiki/` printed `log.md`, `rules/rule-clean-branch.md`, `rules/rule-claude-md.md`, `rules/rule-guppi-config.md`, `entities/entity-sprint-plugin.md`, `rules/rule-morph.md` and `estimates/estimate-morph-sets-up-the-project-at-the-first-hi.md`. `log.md` is not read. Each other hit enters this Case. The same Grep over `.claude/` printed nothing. A Grep of `at install\b` over `vault/wiki/` printed `log.md`, `rules/rule-guppi-config.md`, `rules/rule-morph.md` and `rules/rule-permissions.md`. "The questions asked at install" in `rule-guppi-config` and "whose initiation at install sets the folder name" in `rule-permissions` name the setup, and both enter this Case. The hits in `rule-morph` stand in its History, and `log.md` is not read. Case 824 also changes the last sentence of the Purpose of `rule-permissions`, and its pair there replaces only the words before the colon. The pair of this Case replaces only words after the colon, so the two do not overlap, and the ledger applies Case 824 first. Read side by side, the sentence then says that the read rules name the folder of the repository of GUPPI, after where that repository sits on the person's disk, and that another install waits for `rule-morph`, whose setup Case sets the folder name. Both texts fit. Case 824 is built again to write "setup Case" in its own texts, so the pairs of this Case do not need to catch its text. The rename is a pair under `replace` on each page, not a `reword`. `reword_pairs` of `.guppi/guppi/generate.py` fails an entry whose `new` does not already stand in the owner's text, by `owner_text`, and no page holds "setup Case" yet. The sections of the other Estimates whose text says "the install" mean `/guppi:install`, and they stand.
>
> Case 824 of this session changes two sentences of the Purpose of `rule-morph`. The ledger applies it before this Case, and this Case writes that Purpose whole, so the new text keeps the words of Case 824: "of the repository of GUPPI" for the commands and for the folder of saved transcripts. The new texts of `rule-morph`, `rule-claude-md` and `rule-guppi-config`, which carry `core: true`, keep each pointer in a bracket at the end of its sentence (case 807.4). The `purpose` and `method` of `estimate-morph-sets-up-the-project-at-the-first-hi` state the old promise, and are set anew in its `update`. Its `method` waits for the session that builds the setup step, the same event as before. No line of its old Criterion is carried word for word. Each old line comes back with "install Case" or "install step" renamed "setup Case" or "setup step". The new Criterion adds the order before `/sprint-open`, the pass of the ledger hook and the line that `/guppi:install` is no Case. The tests of `.guppi/tests/` that read live pages, `test_guppi_package.py` among them, look for old command and path words that these texts do not hold.

> **problem:**
> Two pages each put a different Case first at the first `/hi` of a new project, with no order between them, and the pages call the setup "the install Case", as if `/guppi:install` were a Case.

> **recommend:**
> - **In what order do setup and the first sprint come?**
>   - Recommended: (a) setup first, then the sprint, in one session.
>   - Answer: agreed, (a).
> - **Should the "install Case" be renamed "setup Case"?**
>   - Recommended: (a) rename to "setup" everywhere.
>   - Answer: agreed, (a).
> - **Where does the start-to-finish description live?**
>   - Recommended: (a) in the Purpose of `rule-morph`.
>   - Answer: agreed, (a).
> - **How is the order checked?**
>   - Recommended: (a) rewrite that check's promise.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a `/pre-spec` finding: `rule-permissions` still says that the folder name is set "at install".
>   - Taken: a pair on `rule-permissions` names the setup Case of `rule-morph` there.

> **given:**
> `rule-morph`: the rule of the setup Case, whose Purpose tells the start of a new project in order.
> **＋** `estimate-morph-sets-up-the-project-at-the-first-hi`: the check of that rule, whose Criterion is replaced whole.
> **＋** `rule-plugin-install`: the rule of `/guppi:install`, the copy before the setup.
> **＋** `rule-skill-hi` and `rule-skill-sprint-open`: the rules of `/hi` and of `/sprint-open`, which opens a sprint.
> **＋** `rule-ledger-write`: the rule of the ledger hook that refuses decision lines while no sprint is open.
> **＋** `rule-guppi-config`, `rule-claude-md` and `rule-permissions`: the rules whose Renders hold the settings of the setup Case, the read rules of the saved transcripts under `~/.claude/projects` among them.
> **＋** `rule-clean-branch` and `entity-sprint-plugin`: pages whose text names the setup Case.

> **when:**
> In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

> **then:**
> `/hi` opens the session as `rule-skill-hi` sets it, and puts the setup Case first, before the opening Case of `rule-skill-sprint-open` and before the Frontier.
> **＋** Once the person ratifies the setup Case, `/hi` starts `/sprint-open` in the same session, and the ledger hook of `rule-ledger-write` writes the decision lines of the setup Case though no sprint is open.
> **＋** The setup step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
> **＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
> **＋** Every value stands in that one setup Case, which the person ratifies or corrects.
> **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the setup as done.
> **－** `/guppi:install` is no Case, and the person ratifies nothing at it.
> **－** Between `/guppi:install` and the ratified setup Case, no settings file changes but by the copy of `/guppi:install` and the render that `/hi` runs.
> **－** The setup step is no skill named `install`.
> **－** The setup step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
> **－** The setup step reads no code of the project and creates no page for it.
> **－** A project whose `guppi.toml` marks the setup as done gets no setup Case at `/hi`.

```then
update:
- slug: rule-morph
  set:
    purpose: 'Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi after /guppi:install, while guppi.toml does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens'
  sections:
    Purpose: |-
      Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` after `/guppi:install`, while `guppi.toml` does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens. The plugin `guppi` installs GUPPI by its skill `/guppi:install`, which copies the files of the clean version into the project, the settings among them, as `rule-plugin-install` sets it. Until the setup Case, those settings name another project: `guppi.toml` holds the languages and the commands of the keys `test` and `style` of the repository of GUPPI, `CLAUDE.md` holds a blank description of the project, the read rules of [[rule-permissions]] name the folder of the saved transcripts of the repository of GUPPI under `~/.claude/projects`, and the code takes the main branch to be `main` (as set in case 693).

      A new project starts in this order. The install is no Case; the setup and the opening of the first sprint are Cases.

      1. The person installs the plugin `guppi`, which the catalogue `guppi-marketplace` lists, as [[rule-plugin-install]] sets it.
      2. The person types `/guppi:install` in the project. It copies the files of GUPPI and builds its Python environment. It decides nothing, so it is no Case, and the person ratifies nothing at it.
      3. The person reopens Claude Code in the project and types `/hi`, which opens the session as [[rule-skill-hi]] sets it: a Case lives only inside a session that `/hi` opened.
      4. While `guppi.toml` does not mark the setup as done, `/hi` puts the setup Case first, before the opening of a sprint and before the Frontier. The person ratifies or corrects it.
      5. Once the setup Case is ratified, `/hi` starts `/sprint-open` in the same session, since the clean version holds the sprint `guppi` closed ([[rule-clean-branch]]). The opening Case of [[rule-skill-sprint-open]] opens the first sprint of the project, and the Frontier comes after it.
      6. The Work Mode of that session writes the settings of the setup Case and runs the tasks of the opening Case.

      The ledger hook of [[rule-ledger-write]] refuses each decision line but a `defer` while no sprint is open. While `guppi.toml` does not mark the setup as done, it writes the decision lines of the setup Case all the same, so that the setup Case is ratified before the opening Case.

      A key of `guppi.toml`, which [[rule-guppi-config]] renders, marks the setup as done: the setup Case sets it, and the clean version holds it unset. The setup step is a skill of the project whose name is not `install`, so that a project never holds both `/install` and `/guppi:install`. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml`, [[rule-claude-md]] for the description of the project in `CLAUDE.md` and [[rule-permissions]] for the read rules, and so sets the key. No settings file changes outside that Case but by the copy of `/guppi:install` and the render that `/hi` runs, which take the values as the clean version holds them ([[rule-ratification]]).

      The setup step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The key, the setup skill, its step in `/hi` and in `/sprint-open`, the pass of the ledger hook for the setup Case and the clean version that holds the key unset are built in the milestone The plugin of [[entity-sprint-plugin]]; until then [[rule-skill-hi]], [[rule-skill-sprint-open]] and [[rule-ledger-write]] put the opening Case first in every project (as set in cases 802, 817 and 825).
  change: 'the Purpose tells the start of a new project in order: /guppi:install is no Case, the setup Case comes first at the first /hi, and /sprint-open follows it in the same session; the install Case is named the setup Case'
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  set:
    status: pending
    purpose: Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the setup as done, puts one setup Case first, before the opening of the first sprint, with the values it finds and the values the person gives, and whether the settings change only by the copy, the render of /hi and the render after that Case is ratified
    method: 'by hand, after the session whose Work Mode builds the setup skill of rule-morph, its step in /hi and in /sprint-open and the pass of the ledger hook for the setup Case: in an empty project, the plugin guppi installed, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of that session, its ledger and the files its Work Mode writes read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the setup Case comes first at the first /hi and /sprint-open follows it in the same session; /guppi:install is no Case
- slug: rule-claude-md
  replace:
  - old: until the install Case of a project writes its own description
    new: until the setup Case of a project writes its own description
  change: the Purpose names the setup Case of rule-morph by its new name
- slug: rule-guppi-config
  replace:
  - old: until the install Case of `rule-morph` sets the project's own commands
    new: until the setup Case of `rule-morph` sets the project's own commands
  - old: The questions asked at install, these two commands among them,
    new: The questions asked at setup, these two commands among them,
  change: the Purpose names the setup Case of rule-morph by its new name
- slug: rule-permissions
  replace:
  - old: whose initiation at install sets the folder name
    new: whose setup Case sets the folder name
  change: the Purpose names the setup Case of rule-morph as the step that sets the folder name
- slug: rule-clean-branch
  replace:
  - old: which the install Case of `rule-morph` replaces with the description of the project
    new: which the setup Case of `rule-morph` replaces with the description of the project
  change: the Purpose names the setup Case of rule-morph by its new name
- slug: entity-sprint-plugin
  replace:
  - old: 'the install step that the first `/hi` after `/guppi:install` runs; what remains: the install skill, its step in `/hi`, the key of `guppi.toml` that marks the install as done, and the clean version that ships that key unset'
    new: 'the setup Case that the first `/hi` after `/guppi:install` puts before the opening of the first sprint; what remains: the setup skill, its step in `/hi` and in `/sprint-open`, the key of `guppi.toml` that marks the setup as done, the pass of the ledger hook for the setup Case while no sprint is open, and the clean version that ships that key unset'
  change: the milestone line of rule-morph names the setup Case, its order before the first sprint and what remains of it
```

```tasks
- [ ] update `rule-morph`
- [ ] update `estimate-morph-sets-up-the-project-at-the-first-hi`
- [ ] update `rule-claude-md`
- [ ] update `rule-guppi-config`
- [ ] update `rule-permissions`
- [ ] update `rule-clean-branch`
- [ ] update `entity-sprint-plugin`
- [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

## Case 826 — The tags retro and box stand in tags.md and on their lessons

> **context:**
> A tag enters `vault/wiki/tags.md` only from a ratified Case, and the ledger hook refuses a lesson line whose tag that file does not hold and no ratified Case of the session declares (case 703.2). At the Retro of session 1739 two lessons wanted the tags `retro`, `box` and `pre-spec`. No Case could be ratified there, so they were written with listed tags: `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian` carries `workflow` and `tests`, and `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec` carries `prespec` and `workflow`. The handoff of session 1739 left the new tags to a later session. `vault/wiki/tags.md`, read whole, has no row `retro` or `box`, and its row `prespec` covers what `pre-spec` would mean, so this Case adds no second spelling. This Case declares the two tags and adds each to its lesson; an earlier Case gave a lesson the tags the ledger hook had refused in the same way (`vault/wiki/log.md`, the line of 2026-10-08 on case 737). The rules `rule-retro` and `rule-spec-box` and their Estimates keep their tags; each takes the new tag when a later Case changes it. No Estimate is created: `estimate-generate-writes` already checks both writes, since its Criterion says that a tag of `new_tags` lands in `tags.md` and that an `update` applies `set` to the frontmatter; its Criterion stands, since this Case changes neither behaviour. The lessons list no Estimates. The person asked why a new tag needs a Case at all; the guard stays in this Case, and its change is left to a separate Frontier item for the main agent to add, since it touches the ledger hook, the check of a Case file and the one rule of `ratification.md`.

> **problem:**
> The tags `retro` and `box` that two lessons of session 1739 wanted are not registered, so the lessons stand without them.

> **recommend:**
> - **Which new tags to register, with what meaning and Russian aliases**
>   - Recommended: (a) both `retro` and `box`, with the proposed meanings and aliases; no `pre-spec`, since `prespec` covers it.
>   - Answer: agreed with the new tags, (a).
> - **Which pages take the new tags in this Case**
>   - Recommended: (a) the two lessons only.
>   - Answer: agreed, (a).
> - **Which Estimate checks the change**
>   - Recommended: (a) no new Estimate; `estimate-generate-writes` checks it.
>   - Answer: agreed, (a).
> - **Should a new tag still need a ratified Case**
>   - Recommended: (b) keep this Case to the two tags, and add a separate Frontier item that changes the guard.
>   - Answer: agreed, (b).

> **given:**
> `vault/wiki/tags.md`: the registry of tags, which gains the two rows.
> **＋** `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian`: the lesson that takes `retro`.
> **＋** `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec`: the lesson that takes `box`.

> **when:**
> The librarian's run of `guppi generate` applies this Case to `vault/wiki/tags.md` and the two lessons.

> **then:**
> `vault/wiki/tags.md` holds a row `retro` and a row `box`, each with its meaning and its Russian aliases.
> **＋** `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian` carries the tags `workflow`, `tests` and `retro`.
> **＋** `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec` carries the tags `prespec`, `workflow` and `box`.
> **－** `vault/wiki/tags.md` gains no row `pre-spec`.

```then
new_tags:
- tag: retro
  meaning: 'the Retro phase: the review of the session''s work against its ledger, the readings of Estimates, the lessons and the handoff'
  aliases: ретро, ретроспектива
- tag: box
  meaning: '/box: a later session running a conserved Spec on its own branch'
  aliases: бокс, законсервированный спек
update:
- slug: lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian
  set:
    tags:
    - workflow
    - tests
    - retro
  change: tagged retro, the tag the ledger hook refused at the Retro of session 1739
- slug: lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec
  set:
    tags:
    - prespec
    - workflow
    - box
  change: tagged box, the tag the ledger hook refused at the Retro of session 1739
```

```tasks
- [ ] update `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian`
- [ ] update `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec`
```

## Case 827 — A lesson line declares its own new tag

> **context:**
> A tag is a short label on a page. `vault/wiki/tags.md` lists each tag with its meaning and its Russian aliases, and `ask-guppi` maps a Russian question to tags by those aliases. Three guards keep a new tag out until a Case is ratified, read in the code. The ledger hook refuses a fresh lesson line whose tag `tags.md` does not hold and no tag line of a Case ratified in the session declares (`refused_tags` and `tag_message` of `.guppi/guppi/ledger.py`, case 703.2). The check of a Case file sends back a Case that uses such a tag without a tag line (`unlisted_tags` of `.guppi/guppi/casecheck.py`, case 703.1). `tags.md` gains a row only from the `new_tags` of the Spec, by `register_tags` of `.guppi/guppi/generate.py`, and its header says a tag enters only after a Case ratified it. Lessons are mostly written at Retro, where no Case is ratified, so the refusal message sends the tag to the handoff of a later session; at the Retro of session 1739 two lessons lost the tags `retro` and `box` that way, and Case 826 of this session adds them. The person agreed that a lesson line may declare its new tag itself by a block `{newtag:<tag>|<meaning>|<aliases>}`, which the ledger hook accepts and the librarian's run registers; that the check of a Case file stays; that the one rule names this exception; and that the header of `tags.md` changes by a one-off task by hand, with the exception written into every text that makes the script the only writer to `vault/wiki/`.
>
> The block is read once, by `parse_line` of `.guppi/guppi/materialize.py`: both the ledger hook (`refused_tags`) and the lift of `materialize` call that function today for a lesson line, so the two sides share one reading; a Grep of `newtag` over `.guppi/` printed 0 occurrences, so no other reading of the block exists. Until Work Mode changes the code, `parse_line` passes the new block by, so a line with it is refused for its tag as today and judged again at each `Stop`; no line is lost. A Grep of `the new tag goes as a line of the handoff` over the repository outside `vault/raw/` printed `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag.md`, `.guppi/tests/test_ledger.py`, `.guppi/guppi/ledger.py` and three files of `vault/archive/migration/2026-10-07/0636/raw/` (`materialize.yaml`, `spec.md`, `cases/case-703.md`); the first three change in Case 827.1, and the archived ones are records of their session and stand. A Grep of `only writer` over `.claude/`, `vault/wiki/` and `CLAUDE.md` printed `glossary.md`, `librarian-guppi.md`, `log.md`, `rule-page-generation.md`, `entity-glossary.md` and `rule-documentation.md`; `log.md` is a record and is not read, `glossary.md` and `librarian-guppi.md` are renders of the pages Case 827.4 changes, and `rule-vault-layout` says the same in other words (No file of `wiki/` is written by hand). A Grep of `registry of tags` over `vault/wiki/` printed `tags.md`, `glossary.md`, `entity-glossary.md` and `rule-vault-layout.md`, each changed in Case 827.4. The hand edit of the header runs in Work Mode, before the librarian's run writes the exceptions of Case 827.4 into `rule-vault-layout` and `rule-page-generation`; at that moment it rests on `rule-case-build`, which says that a page or a rendered file changes at the librarian's run or the render, or earlier only by a one-off task by hand in Work Mode that a Case names.
>
> These stand: `rule-case-check` and `estimate-case-check-sends-back-an-unlisted-tag`, since the person kept the check of a Case file; the sentence of `rule-case-protocol` and `case-schema.md` on how a Case declares a new tag, and the tag line of `rule-spec-write`, which speak of a Case and claim no other way is closed; `estimate-generate-writes`, whose Criterion says a tag of `new_tags` lands in `tags.md` whatever wrote it there; `estimate-materialize-assembles`, whose line on `new_tags` speaks of Cases; `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, which names the refusal by slug; `estimate-ratification-loaded`, whose `uv run --project .guppi guppi render --check` covers the new sentences of `ratification.md`; the aliases line of `.claude/agents/ask-guppi.md`; the merge sentence of `.claude/skills/merge-main/SKILL.md`, which speaks of what a merge writes; and the context of Case 826, which states the guard as it stood. `.guppi/tests/test_ledger.py` asserts the old words of the refusal, so Case 827.1 changes that test. The new Criterion of `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` keeps each line of the old one but two, which change on purpose: the words of the refusal, and the line on a refused line from an earlier text, which now also lands once its tag is declared. `.guppi/tests/test_guppi_package.py` reads the live pages and every file under `.claude/` for `uv run guppi`, `uv run pytest`, `guppi/` and `tests/`; the new texts write those paths only as `.guppi/guppi/` and `.guppi/tests/`, which its pattern does not match, so it stands. By the person's answer, Case 827.4 creates no Estimate: `estimate-glossary-terms-defined` reads that each row of the glossary agrees with the page it points to, which covers its rows Ratification, Working files and Librarian against `rule-ratification`, `rule-vault-layout` and `rule-documentation`; its Criterion stands, since it already speaks of that agreement, and the header of `tags.md` and the sentences of `rule-vault-layout`, `rule-page-generation` and `rule-documentation` are read by no Estimate.

> **problem:**
> A lesson that needs a new tag cannot have it where most lessons are written: from `/work` to the end of Retro no Case is ratified, so the ledger hook refuses the line, and the tag waits for a Case of a later session.

> **recommend:**
> - **How may a new tag enter outside a Case**
>   - Recommended: (a) a lesson line declares its new tag with its meaning and Russian aliases; the librarian's run registers it, and the one rule and the header of `tags.md` name this way.
>   - Answer: agreed, (a).
> - **Does the check of a Case file change too**
>   - Recommended: (a) the check of a Case file stays; a Case still declares a new tag by a tag line.
>   - Answer: agreed, (a).
> - **How a lesson line writes its new tag**
>   - Recommended: (a) one block `{newtag:<tag>|<meaning>|<aliases>}` per new tag, the tag also in `{tags:...}`, read by `parse_line`.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) three sub-cases: the ledger hook with the Criterion of `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` replaced, the lift with a new Estimate, and the texts with the Criterion of `estimate-ratification-ledger-line-form` replaced.
>   - Answer: agreed, (a).
> - **How the header of `tags.md` changes**
>   - Recommended: (a) a one-off edit by hand in Work Mode, and an exception for that header alone in the pages that make the script the only writer.
>   - Answer: agreed, (a).
> - **Where the exception for the header of `tags.md` is written**
>   - Recommended: (a) a fourth sub-case writes it into `rule-vault-layout`, `rule-page-generation`, `rule-documentation` and `entity-glossary`.
>   - Answer: agreed, (a).
> - **How the fourth sub-case is checked**
>   - Recommended: (a) a new Estimate on `rule-vault-layout`, read by hand after the librarian's run.
>   - Answer: (b) no new Estimate; `estimate-glossary-terms-defined` checks it.
> - **Change**
>   - Asked: a finding of `/pre-spec`: the hand edit of the header of `tags.md` runs in Work Mode, before the exceptions of Case 827.4 land; `context` should name the sentence of `rule-case-build` that allows it at that moment.
>   - Taken: `context` names that sentence of `rule-case-build`; nothing else changed.

### Case 827.1 — The ledger hook writes a lesson whose new tag a lesson line declares

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose Purpose names the refusal of an unlisted tag.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ledger.py`: the hook, `refused_tags` and `tag_message`.
> **＋** `.guppi/guppi/tags.py`: the one reading of the listed tags.
> **＋** `.guppi/guppi/materialize.py`: `parse_line`, the one reading of a ledger line.
> **＋** `.guppi/guppi/casecheck.py`: the check of a Case file, which reads the same tags.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the refusal.
> **＋** `vault/wiki/tags.md`: the registry of tags.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session whose `{tags:...}` holds a tag.

> **then:**
> A fresh lesson line stays out of the ledger while its `{tags:...}` names something outside `vault/wiki/tags.md`.
> **＋** Such a line lands once this session ratified a Case declaring each such name, the decision line of that Case written earlier or in the same `Stop`.
> **＋** Such a line lands when a `{newtag:<tag>|<meaning>|<aliases>}` block declares each such tag, on the line itself or on a lesson line of the session's ledger or of the same `Stop`.
> **＋** A block declares its tag only when that tag stands in the `{tags:...}` of its line and its meaning and aliases are not empty, as `parse_line` of `.guppi/guppi/materialize.py` reads it.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — tag <tag> is not in tags.md and nothing of this session declares it: write the line again with a tag of tags.md, or declare the tag on the line by {newtag:<tag>|<meaning>|<aliases>}, the tag also in its {tags:...}."
> **＋** A refused line from an earlier text of the transcript is judged again at every `Stop` without a word, and is written at the first `Stop` where each of its tags is listed or declared.
> **＋** The ledger hook takes its known tags from `.guppi/guppi/tags.py`, the same source as `.guppi/guppi/casecheck.py`.
> **－** A line that the hook cannot read, or refuses for its prefix, is not judged for its tags.
> **－** The blocks of such a line declare no tag.
> **－** `estimate[...]` and `decision[...]` lines are not judged for their tags, and a line already in the ledger of any session is not judged again.
> **－** In a project with no `vault/wiki/tags.md`, the ledger hook refuses no lesson for its tags.

```then
update:
- slug: rule-ledger-write
  replace:
  - old: so that an unlisted tag reaches no page through a lesson; from `/work` to the end of Retro, where no Case is ratified, its stderr line asks for a tag of `tags.md` and for the new tag as a line of the handoff to a later session; with no `tags.md` no tag is judged (case 703.2).
    new: so that an unlisted tag reaches no page through a lesson; a `{newtag:<tag>|<meaning>|<aliases>}` block of the line itself, or of a lesson line of the session's ledger or of the same `Stop`, declares the tag too, read by `parse_line` of `.guppi/guppi/materialize.py`, when the tag stands in the `{tags:...}` of its line and its meaning and aliases are not empty, so that a lesson brings its new tag with its meaning and aliases at any phase; its stderr line asks for a tag of `tags.md` or for that block; with no `tags.md` no tag is judged (as set in case 703.2, and in case 827.1).
  change: a newtag block of a lesson line declares a new tag for the ledger hook (case 827.1)
- slug: estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag
  set:
    status: pending
    purpose: Whether the ledger hook refuses a fresh lesson line with a tag that tags.md does not hold and that neither a ratified Case of the session nor a newtag block of a lesson line declares, and says why only for the reply just finished
  change: the Criterion replaced whole — a newtag block of a lesson line declares a tag (case 827.1)
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] update `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`
- [x] `.guppi/guppi/materialize.py`: `parse_line` gives a lesson record `new_tags`, one entry of `tag`, `meaning` and `aliases` per `{newtag:<tag>|<meaning>|<aliases>}` block before `trigger:` whose tag stands in the line's `{tags:...}` and whose meaning and aliases are not empty; its docstring says so.
- [x] `.guppi/guppi/tags.py`: `lesson_tags` gives the tags of the `new_tags` of the lesson records it is given; the module docstring names it.
- [x] `.guppi/guppi/ledger.py`: `refused_tags` adds to the listed tags `lesson_tags` of the records of the session's ledger and of the fresh lines not in `skip`; `tag_message` gives the new stderr line; the module docstring says so.
- [x] `.guppi/tests/test_ledger.py`: `test_unlisted_tag_in_the_finished_reply_is_refused_aloud_and_the_rest_lands` asserts the new words in place of the words of the handoff; new tests named `test_unlisted_tag_...`: a tag declared on the line itself lands; a tag declared on a lesson line of the session's ledger lands; a block whose tag is not in the `{tags:...}` of its line, or whose aliases are empty, declares nothing; a block on a line refused for its prefix declares nothing.
- [ ] read `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`
```

### Case 827.2 — materialize lifts the tag a lesson line declares

> **given:**
> `rule-materialize`: the rule of the lift, whose Purpose names what a lesson line carries.
> **＋** `estimate-materialize-lifts-a-tag-of-a-lesson`: the new check of the lift of the block.
> **＋** `.guppi/guppi/materialize.py`: the lift and `parse_line`.
> **＋** `.guppi/tests/test_materialize.py`: the tests of the lift.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of a unit, which holds the lesson line.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the unit, whose Cases declare tags by tag lines.
> **＋** `raw/<date>/<hi HHMM>/materialize.yaml`: the yaml whose `new_tags` gains the tag.

> **when:**
> `uv run --project .guppi guppi materialize` lifts a `lesson[...]` line of the `raw/<date>/<hi HHMM>/ledger.md` of a unit that carries a `{newtag:<tag>|<meaning>|<aliases>}` block.

> **then:**
> The `new_tags` of the `raw/<date>/<hi HHMM>/materialize.yaml` of the unit hold the tag once, with its meaning and its aliases.
> **＋** The tags that the Cases of the `raw/<date>/<hi HHMM>/spec.md` of the unit declare stand first, and a tag that one of them declares keeps the meaning and aliases of that Case.
> **＋** A tag that two lesson lines declare keeps the declaration of the earlier line.
> **＋** The lesson entry carries its tags, its trigger and its root cause as before.
> **－** The yaml gains no entry from a lesson record of `.guppi/guppi/materialize.py` that holds no `new_tags`.

```then
create:
- slug: estimate-materialize-lifts-a-tag-of-a-lesson
  ref: rule-materialize
  kind: QA
  purpose: Whether a tag that a newtag block of a lesson line declares reaches the new_tags of materialize.yaml once, with its meaning and aliases
  method: uv run --project .guppi pytest .guppi/tests/test_materialize.py -k newtag
  tags:
  - harness
  - workflow
  - ledger
update:
- slug: rule-materialize
  replace:
  - old: 'and `incomplete: [addressed_by]` otherwise (case 377.3).'
    new: 'and `incomplete: [addressed_by]` otherwise (case 377.3). A lesson line''s `{newtag:<tag>|<meaning>|<aliases>}` block, read by `parse_line` when its tag stands in the line''s `{tags:...}` and its meaning and aliases are not empty, adds the tag with its meaning and aliases to the yaml''s `new_tags` once, after the tags that the Cases of the Spec declare, a tag already there passed by, so that `generate` adds its row to `tags.md` (as set in case 827.2).'
  change: a newtag block of a lesson line adds its tag to new_tags (case 827.2)
```

```tasks
- [ ] update `rule-materialize`
- [ ] create `estimate-materialize-lifts-a-tag-of-a-lesson`
- [x] `.guppi/guppi/materialize.py`: after the `new_tags` of the Cases of the Spec, the `new_tags` of each lesson record of the unit join the yaml's `new_tags` in ledger order, a tag already there passed by; the module docstring says so.
- [x] `.guppi/tests/test_materialize.py`: tests named `test_newtag_...` over the Criterion of `estimate-materialize-lifts-a-tag-of-a-lesson`.
- [ ] read `estimate-materialize-lifts-a-tag-of-a-lesson`
```

### Case 827.3 — ratification.md sets the block that declares a tag

> **given:**
> `rule-ratification`: the one rule and the form of the ledger lines.
> **＋** `vault/wiki/ratification.md`: the Render of `rule-ratification`.
> **＋** `estimate-ratification-ledger-line-form`: its Criterion is replaced whole.
> **＋** `vault/wiki/tags.md`: the registry of tags.

> **when:**
> The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **＋** A lesson line whose tag `vault/wiki/tags.md` does not hold carries one `{newtag:<tag>|<meaning>|<aliases>}` block per such tag before `trigger:`, the tag also in its `{tags:...}`, the meaning one line and the aliases the words of the chat language for it.
> **－** A lesson whose fix is ratified in another session gets no mark.

```then
update:
- slug: rule-ratification
  replace:
  - old: 'When unsure whether something needs ratification: it does.'
    new: 'When unsure whether something needs ratification: it does. A new tag needs no Decision when a lesson line declares it with its meaning and its {{chat_lang}} aliases, and the librarian''s run adds it to `tags.md` (as set in case 827.3).'
  - old: 'A `create` line carries the ratified tags: `{tags:a,b}`.'
    new: 'A `create` line carries the ratified tags: `{tags:a,b}`. A lesson line whose tag `tags.md` does not hold declares it by one `{newtag:<tag>|<meaning>|<aliases>}` block per new tag, before `trigger:`, the tag also in its `{tags:...}`, the meaning one line and the aliases the {{chat_lang}} words for it; the ledger hook writes the line, and the librarian''s run adds the row to `tags.md` (as set in case 827.3).'
  change: the one rule names a new tag a lesson line declares; the lesson line declares it by a newtag block (case 827.3)
- slug: estimate-ratification-ledger-line-form
  set:
    status: pending
    method: 'by hand, after a session whose ledger holds a lesson and the Case that closes its cause together, a Case that takes up a decision with more than one Case in its deferred_by, and a lesson line that declares a new tag: those lines and their preview read against the Criterion'
  change: the Criterion replaced whole — a lesson line declares a new tag by a newtag block (case 827.3)
```

```tasks
- [ ] update `rule-ratification`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/ratification.md`
- [ ] update `estimate-ratification-ledger-line-form`
- [ ] read `estimate-ratification-ledger-line-form`
```

### Case 827.4 — The header of tags.md changes by a one-off task

> **given:**
> `vault/wiki/tags.md`: the registry of tags, whose header changes by hand.
> **＋** `rule-vault-layout`: the rule that no file of `wiki/` is written by hand.
> **＋** `rule-page-generation`: the rule that the script is the only writer to `wiki/`.
> **＋** `rule-documentation`: the frame of the librarian.
> **＋** `.claude/agents/librarian-guppi.md`: the Render of `rule-documentation`.
> **＋** `entity-glossary`: the terms, with the rows Ratification, Working files and Librarian.
> **＋** `vault/wiki/glossary.md`: the render of `entity-glossary`.

> **when:**
> Work Mode runs the one-off task on `vault/wiki/tags.md`, and a reader reads it, `rule-vault-layout`, `rule-page-generation`, `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md` after the librarian's run.

> **then:**
> The header of `vault/wiki/tags.md` says that a tag enters its table from a tag line of a ratified Case or from a `{newtag:...}` block of a lesson line, and that the librarian's run writes each row and invents none.
> **＋** `rule-vault-layout`, `rule-page-generation` and `.claude/agents/librarian-guppi.md` name that header as the text above the table that a one-off task by hand of a ratified Case changes.
> **＋** The rows Ratification, Working files and Librarian of `vault/wiki/glossary.md` agree with those texts and with `rule-documentation`.
> **－** The one-off task changes no row of the table of `vault/wiki/tags.md`.

```then
update:
- slug: rule-vault-layout
  replace:
  - old: which git joins by their `merge=union` lines in `.gitattributes` (case 790). A file is
    new: 'which git joins by their `merge=union` lines in `.gitattributes` (case 790). The header of `tags.md` above its table is written by hand too: a one-off task that a ratified Case names changes it in Work Mode (as set in case 827.4). A file is'
  - old: '`tags.md` the registry of tags already ratified in a Case.'
    new: '`tags.md` the registry of tags, each declared by a tag line of a ratified Case or by a `{newtag:...}` block of a lesson line, its rows written by `generate`.'
  change: the header of tags.md changes by a one-off task by hand; a tag enters from a Case or a lesson line (case 827.4)
- slug: rule-page-generation
  replace:
  - old: which git joins by their `merge=union` lines in `.gitattributes` (case 790). It lays
    new: 'which git joins by their `merge=union` lines in `.gitattributes` (case 790). The header of `tags.md` above its table is not written by the script: a one-off task by hand that a ratified Case names changes it in Work Mode (as set in case 827.4). It lays'
  change: the header of tags.md is changed by a one-off task by hand, not by the script (case 827.4)
- slug: rule-documentation
  replace:
  - old: and you write only through the scripts named below.
    new: 'and you write only through the scripts named below. The header of `tags.md` above its table is not yours either: a one-off task by hand that a ratified Case names changes it in Work Mode (as set in case 827.4).'
  change: the header of tags.md is changed by a one-off task by hand, not by the librarian (case 827.4)
- slug: entity-glossary
  replace:
  - old: '| Human sign-off on a Decision; nothing in vault or code changes without one |'
    new: '| Human sign-off on a Decision; nothing in vault or code changes without one, but a new tag that a lesson line declares with its meaning and aliases |'
  - old: '`tags.md`, the registry of tags ratified in a Case;'
    new: '`tags.md`, the registry of tags, each from a ratified Case or from a lesson line that declares it, its header changed only by a one-off task by hand that a Case names;'
  - old: and the lines of `log.md` and `tags.md` that git joins (case 790);
    new: and the lines of `log.md` and `tags.md` that git joins (case 790), and the header of `tags.md`, which a one-off task by hand that a Case names changes;
  change: 'the rows Ratification, Working files and Librarian: a new tag a lesson line declares, and the header of tags.md changed by a one-off task by hand (case 827.4)'
```

```tasks
- [x] `vault/wiki/tags.md`: a one-off edit by hand in Work Mode of its header above the table: the sentence that a tag enters only after a Case ratified it says instead that a tag enters from a tag line of a ratified Case or from a `{newtag:...}` block of a lesson line with its meaning and aliases, and that the librarian's run writes each row and invents none; the table stays as it is.
- [ ] update `rule-vault-layout`
- [ ] update `rule-page-generation`
- [ ] update `rule-documentation`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] update `entity-glossary`
- [ ] `uv run --project .guppi guppi glossary`
```

## Deferred

## Case 828 — The note that a core page ships without its Estimates put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. `rule-rules-schema` still says a core page ships without its Estimates. `estimate-rules-schema-checked` and `estimate-clean-branch-pages-hold-pointers-only-in-brackets` speak of what Case 822.1 changed.

> **problem:**
> No Case of this session brings `rule-rules-schema` in line with the shipped Estimates.

```then
defer:
  - slug: rule-rules-schema
    type: rule
    purpose: "Its text still says a core page ships without its Estimates, after Case 822.1 shipped them; put off at the close of Plan Mode of session 1959"
```

## Case 829 — The methods of two MOC Estimates put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. After the `reword` of Case 820.7, `estimate-guppi-tests-green` and `estimate-page-schemas-one-file-per-rule` hold a `method` that does not fit a MOC, and `guppi lint` reports both.

> **problem:**
> No Case of this session gives these two Estimates a `method` that fits a MOC.

```then
defer:
  - slug: estimate-guppi-tests-green
    type: estimate
    purpose: "Its method does not fit a MOC after the reword of Case 820.7, a lint finding; put off at the close of Plan Mode of session 1959"
  - slug: estimate-page-schemas-one-file-per-rule
    type: estimate
    purpose: "Its method says by hand while a child Estimate names a test file, a lint finding; put off at the close of Plan Mode of session 1959"
```

## Case 830 — The tag name in the milestone line put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. The milestone line of `entity-sprint-plugin` still names a tag `prod-2`. `guppi ship` needs a tag `prod-x.y.z`.

> **problem:**
> No Case of this session sets the tag that the milestone line names.

```then
defer:
  - slug: entity-sprint-plugin
    type: entity
    purpose: "Its milestone line names a tag prod-2 where guppi ship needs a tag prod-x.y.z; put off at the close of Plan Mode of session 1959"
```

## Case 831 — The readings that need a tag prod-x.y.z put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. At this session's `/hi`, `guppi ship --allow-draft` exited 1 with `ship: no tag prod-x.y.z in the history of HEAD; nothing written`; the tags `prod-1` and `prod-2` stand. The readings of `estimate-clean-branch-installs-as-a-plugin` and `estimate-plugin-install-writes-guppi-into-an-empty-project`, both failed unread, and of `estimate-guppi-package-is-ready-after-the-install` need that build.

> **problem:**
> No Case of this session lets these readings run before a tag `prod-x.y.z` stands.

```then
defer:
  - slug: estimate-clean-branch-installs-as-a-plugin
    type: estimate
    purpose: "Failed unread: guppi ship --allow-draft writes nothing with no tag prod-x.y.z; put off at the close of Plan Mode of session 1959"
  - slug: estimate-plugin-install-writes-guppi-into-an-empty-project
    type: estimate
    purpose: "Failed unread: no local copy can be built with no tag prod-x.y.z; put off at the close of Plan Mode of session 1959"
  - slug: estimate-guppi-package-is-ready-after-the-install
    type: estimate
    purpose: "Its reading needs a local copy that guppi ship writes only after a tag prod-x.y.z; put off at the close of Plan Mode of session 1959"
```

## Case 832 — The when of the install-ready Estimate put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. The `when` of `estimate-guppi-package-is-ready-after-the-install` installs the plugin from the catalogue of the branch `prod`, while its `method` reads a local copy.

> **problem:**
> No Case of this session makes the `when` of this Estimate agree with its `method`.

```then
defer:
  - slug: estimate-guppi-package-is-ready-after-the-install
    type: estimate
    purpose: "Its when names the branch prod while its method reads a local copy; put off at the close of Plan Mode of session 1959"
```

## Case 833 — The harness pipeline reading put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. `estimate-harness-pipeline` failed unread at the Retro of session 1739, with `guppi backlog --check` red there; its text came only at the librarian's run, and its `method` names no such moment. At this session's `/hi`, `estimate-claude-md-rendered`, the other reading this item names, passed.

> **problem:**
> No Case of this session gives `estimate-harness-pipeline` a reading moment after the librarian's run.

```then
defer:
  - slug: estimate-harness-pipeline
    type: estimate
    purpose: "Failed unread at Retro; its method names no moment after the librarian's run that writes the text it reads; put off at the close of Plan Mode of session 1959"
```

## Case 834 — The collection of the tests from the root put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. A finding of `/pre-spec`, not confirmed: whether pytest collects `.guppi/tests/` from the root of a project with no root `pyproject.toml`.

> **problem:**
> No Case of this session checks how the tests run in a project with no root `pyproject.toml`.

```then
defer:
  - slug: rule-guppi-package
    type: rule
    purpose: "Not confirmed whether pytest collects .guppi/tests/ from the root of a project with no root pyproject.toml; put off at the close of Plan Mode of session 1959"
```

## Case 835 — Stale facts in the contexts of Cases put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. A finding of `/pre-spec` named stale counts and facts in the contexts of Cases 816, 817, 818, 820 and 822. `insight-case-build-claims-what-code-does-without-reading-it` names the same kind of cause.

> **problem:**
> No Case of this session stops a Case from carrying a fact its builder did not read again.

```then
defer:
  - slug: insight-case-build-claims-what-code-does-without-reading-it
    type: insight
    purpose: "Stale counts and facts in the contexts of Cases 816 to 822; put off at the close of Plan Mode of session 1959"
```

## Case 836 — Two lessons with no fixing Case put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. Two lessons of session 0553 have no Case that fixes their cause.

> **problem:**
> No Case of this session fixes the cause of these two lessons.

```then
defer:
  - slug: lesson-ledger-window-stops-at-a-resume-on-the-next-day
    type: lesson
    purpose: "No Case fixes the walk of the event logs that stops at a resume on the next day; put off at the close of Plan Mode of session 1959"
  - slug: lesson-case-build-agent-context-grows-on-every-resume
    type: lesson
    purpose: "No Case fixes the context of a resumed case-guppi that only grows; put off at the close of Plan Mode of session 1959"
```

## Case 837 — The tests/ example against its package check put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. At this session's `/hi`, `test_guppi_package.py` failed on `[tests/]` against `rule-page-generation` and `estimate-generate-rewords`, which name `tests/` as the example of a reword pair; `estimate-guppi-package-runs-from-its-own-folder` was read failed.

> **problem:**
> No Case of this session settles the example against the Criterion that forbids the path.

```then
defer:
  - slug: estimate-guppi-package-runs-from-its-own-folder
    type: estimate
    purpose: "Read failed: its test finds the example tests/ in rule-page-generation and estimate-generate-rewords; put off at the close of Plan Mode of session 1959"
```

## Case 838 — The make target that lint misreads put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. `guppi lint` reads the words "make with the targets …" of a `method` as the Makefile target `with` (`.guppi/guppi/lint.py`, the `MAKE_TARGET` match).

> **problem:**
> No Case of this session fixes how `guppi lint` reads a make target in a `method`.

```then
defer:
  - slug: rule-lint
    type: rule
    purpose: "guppi lint reads make with the targets in a method as the target with; put off at the close of Plan Mode of session 1959"
```

## Case 839 — The commit of the plugin skill at the librarian's close put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 1959. The close of the librarian commits `vault`, `CLAUDE.md`, `.claude` and `guppi.toml` only, while the render now writes `plugin/skills/install/SKILL.md`, which stands untracked.

> **problem:**
> No Case of this session makes the librarian's close commit every file the render writes.

```then
defer:
  - slug: rule-documentation
    type: rule
    purpose: "The librarian's close does not commit plugin/skills/install/SKILL.md that the render writes; put off at the close of Plan Mode of session 1959"
```
