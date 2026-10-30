<!-- approved 04:50:49 · session 51022d6e -->

# Session 0304 — the items of the brief of 2341

## Case 919 — The code and the tests hold no stray pointer to a case

> **context:**
> `guppi ship --check`, a step of `uv run --project .guppi guppi check`, judges in place each file outside `vault/` that the clean version of GUPPI takes, and prints a line for each pointer to a case, a decision or a session that stands outside a bracket of its own, since the clean version drops such a bracket whole and a pointer outside one would reach it. In a test file it judges only the comments and the docstrings, by `masked_strings` and `outside` of `.guppi/guppi/pointers.py`, and `bare_numbers` of `.guppi/guppi/ship.py` adds each bare case number there. The last run, under `## Flags` of `vault/wiki/brief.md`, printed `ship: .guppi/tests/test_render.py:500: a reference to a case: Case 914` among its 11 lines: the docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed`, added by Case 914, opens with the words `Case 914:`. Nothing caught it before the librarian's run: Work Mode runs `guppi check` once before the first change, the Retro skill says not to run it, and `guppi test`, `uv run --project .guppi pytest -q` by `guppi.toml`, skips each test with the mark `live` by the `addopts` of `.guppi/pyproject.toml`, the mark of a test that reads the live vault, which `plan` of `.guppi/guppi/ship.py` and so `check` read. Case 919.1 moves the pointer into a bracket at the end of the sentence, as `rule-clean-branch` sets it, and sets `estimate-clean-branch-code-holds-pointers-only-in-brackets` `pending` with its Criterion written back unchanged, since that Criterion already promises that `guppi ship --check` prints no line on a file under `.guppi/tests/`, its line on `.guppi/tests/test_casecheck.py` still holds by the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)`, and the reading at Retro gives it a fresh Result in place of a `passed` that the check made false. Case 919.2 adds a test without the mark `live` that judges each file under `.guppi/` by `judged` of `.guppi/guppi/ship.py`, the function `check` calls for each file, with empty sets of known and loose slugs, so it reads no page; the two sides part on two inputs: a marker line of a page without `core: true`, which `leftovers` judges only by the loose slugs that `plan` reads from the vault, and a file that a page without `core: true` renders, which `plan` leaves out, and the new sentence of `rule-clean-branch` and the `then` of Case 919.2 say that the test judges neither, so no answer of the test claims to be the whole check. A Grep of `.guppi/guppi/` for `import.*\bjudged\b|\bjudged\(|from guppi.pointers import|pointers\.outside|\boutside,` printed `.guppi/guppi/ship.py` and `.guppi/guppi/prespec.py`: the judgment of a pointer lives in `.guppi/guppi/pointers.py` and `judged` is its one caller for a file, so the test imports it and holds no copy, as `rule-one-judgment-one-implementation` sets it. A Grep of `.guppi/tests/` for `rule-clean-branch|estimate-clean-branch-code-holds|test_render\.py|test_ship\.py` printed `.guppi/tests/test_ship.py` alone, whose hits write files under a temporary root, so no test reads a file this Case changes live. `rule-clean-branch` keeps `deferred_by: decision-case-893.1`, the Frontier item C4: the `update` of Case 919.2 changes one sentence and leaves the defer to C4, and `check_backlog` of `.guppi/guppi/casecheck.py` judges only open Frontier lines whose source is `backlog`, which C4 is not. The session's ledger holds no `error` lesson, so no line carries a mark.

> **problem:**
> A test docstring holds a pointer to a case outside a bracket, so `guppi check` is red and the clean version would carry it; and no step before the librarian's run judges the code and the tests for such a pointer, so the next one is found as late as this one.

> **recommend:**
> - **How should the docstring be fixed?**
>   - Recommended: (a) move the pointer into a bracket at the end of the sentence.
>   - Answer: agreed, (a).
> - **How should the fix be checked?**
>   - Recommended: (a) set `estimate-clean-branch-code-holds-pointers-only-in-brackets` back to `pending`, its Criterion unchanged, and read it at Retro.
>   - Answer: agreed, (a).
> - **Should the Case also add a guard against a repeat?**
>   - Recommended: (a) fix this one docstring only.
>   - Answer: (b), also add a test that runs the pointer check over the live `.guppi/` folder.
> - **What should the guard test judge, and how does it run?**
>   - Recommended: (a) an unmarked test over the files of `.guppi/` alone, by `judged` of `.guppi/guppi/ship.py`, with no read of the vault.
>   - Answer: agreed, (a).
> - **How should the guard be checked?**
>   - Recommended: (a) a new Estimate on `rule-clean-branch`.
>   - Answer: agreed, (a).
> - **Should `rule-clean-branch` say that the guard exists?**
>   - Recommended: (a) add one sentence after the passage on `guppi ship --check`.
>   - Answer: agreed, (a).

### Case 919.1 — The docstring of the test of --paths holds its pointer in a bracket

> **given:**
> `.guppi/tests/test_render.py`: the docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship --check`, which judges the docstring.
> **＋** `estimate-clean-branch-code-holds-pointers-only-in-brackets`: set `pending`, its Criterion written back unchanged.
> **＋** `rule-clean-branch`: sets the bracket of a pointer.

> **when:**
> `uv run --project .guppi guppi ship --check` of `.guppi/guppi/ship.py` judges `.guppi/tests/test_render.py` in the working tree.

> **then:**
> It prints no line on `.guppi/tests/test_render.py`.
> **＋** The docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed` holds its pointer to a case in a bracket at the end of its sentence, as `rule-clean-branch` sets it.
> **－** The fix changes no line of `.guppi/tests/test_render.py` but that docstring.

```then
update:
- slug: estimate-clean-branch-code-holds-pointers-only-in-brackets
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      At Retro of the session, `uv run --project .guppi guppi ship --check` of `.guppi/guppi/ship.py` judges the working tree, and `uv run --project .guppi guppi ship --review <folder>` builds the clean version into an empty folder.

      Then:
      `uv run --project .guppi guppi ship --check` prints no line on a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
      **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
      **＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
      **－** The rewording changes no line but a comment or a docstring, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
      **－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.
  change: 'pending again: guppi ship --check printed a line on .guppi/tests/test_render.py; the Criterion stands'
```

```tasks
- [x] `.guppi/tests/test_render.py`: the docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed` reads `Run as the close command runs it, --paths writes no carriage return, on Windows too, so $(...) hands git add each path as it stands (case 914).`, its code spans kept as they stand, in two lines of at most 100 characters.
- [x] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
- [x] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`
```

### Case 919.2 — guppi test judges the code and the tests for a stray pointer

> **given:**
> `.guppi/tests/test_ship.py`: the new tests of the live code.
> **＋** `.guppi/guppi/ship.py`: `judged`, `tree_files`, `read_text`, `LEFT_OUT` and `NOT_CLEANED`, which the tests call and read.
> **＋** `rule-clean-branch`: the page that states the guard.
> **＋** `estimate-clean-branch-tests-judge-the-live-code`: the new check of the guard.
> **＋** `rule-retro`: lets no red test stand at Retro.

> **when:**
> `uv run --project .guppi guppi test` runs the tests of `.guppi/tests/` in the repository of GUPPI.

> **then:**
> A test of `.guppi/tests/test_ship.py` walks the code and the tests under `.guppi/` by `tree_files`, leaves out `LEFT_OUT` and `NOT_CLEANED`, and runs `judged` of `.guppi/guppi/ship.py` over each file, the same judgment as the step of the clean version, and passes when `judged` returns nothing for every file.
> **＋** Where a comment or a docstring under `.guppi/` holds a pointer outside a bracket of its own or a bare case number, the test fails and shows the file and the line of each.
> **＋** The test carries no mark `live` and reads no page of the vault, so `uv run --project .guppi guppi test` runs it.
> **＋** A second test runs the same walk over a temporary folder whose test file has a docstring that opens with `Case 5:`, and finds that line.
> **－** It judges no file of the harness, no file at the root of the project and no marker line of a page without `core: true`; those stay with the step `--check` of `.guppi/guppi/ship.py`.

```then
create:
- slug: estimate-clean-branch-tests-judge-the-live-code
  ref: rule-clean-branch
  kind: QA
  purpose: Whether guppi test judges the code and the tests under .guppi/ for a pointer outside its bracket and a bare case number, with no read of the vault, so that a stray one goes red before the librarian's run
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k live_code, and uv run --project .guppi guppi test, read against the Criterion at Retro
  tags:
  - plugin
  - tests
update:
- slug: rule-clean-branch
  replace:
  - old: and `uv run --project .guppi guppi check` runs it;
    new: and `uv run --project .guppi guppi check` runs it; a test of `.guppi/tests/test_ship.py` runs the same judgment, `judged` of `.guppi/guppi/ship.py`, over each file under `.guppi/` that the clean version holds, with no read of the vault and so no judgment of a marker line, and `uv run --project .guppi guppi test` fails on a pointer outside its bracket or a bare case number there before the librarian's run;
  change: a test of guppi test judges the code and the tests under .guppi/ for a pointer outside its bracket
```

```tasks
- [x] `.guppi/tests/test_ship.py`: a helper that walks the files under `.guppi/` of a root by `ship.tree_files`, but `ship.LEFT_OUT` and `ship.NOT_CLEANED`, reads each by `ship.read_text` and returns the lines of `ship.judged` with empty sets of known and loose slugs; a test with no mark `live` that asserts the helper returns no line on `REPO`; a test that asserts it returns the line of a docstring that opens with `Case 5:` in a test file under a temporary root; the name of each test holds `live_code`.
- [x] create `estimate-clean-branch-tests-judge-the-live-code`
- [x] update `rule-clean-branch`
- [x] read `estimate-clean-branch-tests-judge-the-live-code`
```

## Case 920 — Four shipped checks drop the words that hold only in GUPPI, and the defer of the clean branch ends

> **context:**
> `guppi ship` copies into the clean version each `passed` Estimate whose target page it writes, its Criterion as it stands here (the Purpose of `rule-clean-branch`). The reading of `estimate-clean-branch-ships-neutral-texts` of 2026-10-29 listed Criterion sentences that hold only in the repository of GUPPI, for a Case of a later session to rewrite. Four of them still wait under the defer that `decision-case-893.1` set on `rule-clean-branch`: `estimate-compact-recall-reloads` gives the session folder `raw/2026-09-28/2229/` of this repository as its example, `estimate-ask-query-before-a-create` names Russian and English, `estimate-synthesis-keeps-actioned-by-the-mark` ends a line with the bare case number `(302.2)`, which `guppi ship` does not remove since no word `case` stands before it, and `estimate-synthesis-clusters` names `estimate-documentation-completes`, which the clean version does not hold, since its `method` names a target of the `Makefile`. Case 908 kept the four under the defer because a replaced Criterion sets its Estimate `pending` and the cascade sets its rule `draft` until the reading passes, and `rule-synthesis`, `rule-ask` and `rule-compact-recall` stand `built` with `core: true`; while a page with `core: true` stands `draft`, `guppi ship <folder>` writes nothing. The brief flags the defer as stale, and `backlog.md` lists `rule-clean-branch` as put off in 13 sessions. The last run of `guppi check`, under `## Flags` of `vault/wiki/brief.md`, printed `9 pages with core: true stand draft`, so the clean version is already blocked, and this Case adds three rules to that list.
>
> The person chose to rewrite all four now and to retire the whole defer. Each sub-case replaces the Criterion of one Estimate whole, the old Criterion carried line by line but the one sentence it rewords, and that Estimate checks it. The rule the new texts keep is the Criterion of `estimate-clean-branch-ships-neutral-texts`, which accepts a sentence that states its condition, such as in the repository of GUPPI, and `rule-clean-branch`, which sets a pointer in a bracket of its own that `guppi ship` removes whole; that Criterion stands, since this Case changes texts it judges and not its promise. The `method` of both synthesis Estimates names the librarian without opening with `after` and an event before a colon: `kept_method_waits` of `.guppi/guppi/prespec.py` reports a kept `method` for which `waits_for_another_session` of `.guppi/guppi/lint.py` holds, and that predicate holds for a part that names the librarian unless `waits_for_an_event` matches it, a part that opens with `after`, or `by hand, after`, and names its event before a colon. So Cases 920.3 and 920.4 set each `method` in that form, and each Estimate stays `pending` until its event. The `method` of `estimate-ask-query-before-a-create` already opens with `by hand, after` and names its event, so it stands, and the Estimate waits for a Case that creates a page with no `ref`. The `method` of `estimate-compact-recall-reloads` names no later session and stands; the person chose a stop in Work Mode at which they run `/compact`, so that Retro reads it.
>
> The defer also lists `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question` and `estimate-case-check-sends-back-a-faulty-case`, which Frontier item C2 of this session holds; by the person's answer the defer goes whole, and if C2 ends with no Case, the handoff of this session names those three, as the handoff of session 2341 did. The defer also lists six Estimates whose pointers hold once the Estimate each names passes and ships; the reading of 2026-10-29 read each shipped Estimate whole and listed none of the six. Case 920.5 names `rule-clean-branch` by an `update` with only `change` and carries `{supersedes:case 893.1}`, as `case-schema.md` sets the taking up of a deferred decision; `estimate-generate-writes-the-decision-page` already checks that a superseding Case clears the earlier slug from the `deferred_by` of each page it names, and its Criterion stands, since this Case changes no code of `generate`. Case 919.2 updates `rule-clean-branch` by one pair in this session, and its `context` leaves the defer to this item; the `update` of Case 920.5 changes no text of the page.
>
> A Grep of the repository, `vault/raw/` and `vault/archive/` left out, for `2026-09-28/2229|in Russian or in English|\(302\.2\)|flag of such a read` printed `vault/wiki/log.md`, `estimates/estimate-ask-query-before-a-create.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `estimates/estimate-compact-recall-reloads.md`, `estimates/estimate-generate-walks-dates.md`, `estimates/estimate-lint-catches-a-broken-fence.md`, `estimates/estimate-prespec-catches-a-broken-fence.md`, `estimates/estimate-synthesis-keeps-actioned-by-the-mark.md` and `estimates/estimate-synthesis-clusters.md`: besides the four pages, the hits are log lines, a Result and `origin` fields, which stand. A Grep of `vault/wiki/`, `log.md` and `brief.md` left out, for `synthesis-keeps-actioned|synthesis-clusters|ask-query-before|compact-recall-reloads` printed `rules/rule-ask.md`, `rules/rule-compact-recall.md`, `rules/rule-synthesis.md`, `estimates/estimate-ask-finds.md` and `estimates/estimate-clean-branch-ships-neutral-texts.md`: fields `estimates`, History lines and a Result, which stand. The same Grep of `.guppi/` and of `.claude/` printed nothing. Of the tests of `.guppi/tests/` that read the live vault, the live build of `test_ship.py` judges each Estimate the clean version takes, and a `pending` Estimate stays out of it; the new texts hold no pointer outside a bracket. The session's ledger holds no `error` lesson, so no line carries a mark.

> **problem:**
> Four checks that ship with GUPPI hold a sentence true only in its own repository, and the defer that keeps their rewrite on `rule-clean-branch` has been put off for 13 sessions and is flagged as stale.

> **recommend:**
> - **Which of the four checks does this Case rewrite now?**
>   - Recommended: (a) all four now, and the defer goes.
>   - Answer: agreed, (a).
> - **What happens to the rest of the note when it is retired?**
>   - Recommended: (a) retire the whole defer; item C2 carries its three checks.
>   - Answer: agreed, (a).
> - **How does the recall check give its sample session folder?**
>   - Recommended: (a) a general pattern, `raw/<date>/<hi HHMM>/`.
>   - Answer: agreed, (a).
> - **How does the vault-query check name the two languages?**
>   - Recommended: (a) by their role, the language of the chat and the language of the repository.
>   - Answer: agreed, (a).
> - **What becomes of the bare case number in the check of a marked lesson?**
>   - Recommended: (a) a pointer in its own bracket, `(as set in case 302.2)`.
>   - Answer: agreed, (a).
> - **What becomes of the link to a check that does not ship, in the clustering check?**
>   - Recommended: (a) state the condition, in the repository of GUPPI.
>   - Answer: agreed, (a).
> - **How do the two synthesis checks say when they are read?**
>   - Recommended: (a) rewrite both methods in the form that names the event.
>   - Answer: agreed, (a).
> - **When is the live part of the recall check read?**
>   - Recommended: (a) in this session: a stop of Work Mode at which the person runs `/compact`, read at Retro.
>   - Answer: agreed, (a).

### Case 920.1 — The recall check gives its session folder as a pattern

> **given:**
> `estimate-compact-recall-reloads`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/recall.py`: the hook the Criterion speaks of.
> **＋** `.claude/skills/hi/SKILL.md`: the `@` files the hook lists.
> **＋** `raw/<date>/<hi HHMM>/`: the pattern of the session folder the header names.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.

> **when:**
> The client compacts the context of a session, on the person's command or on its own, and `SessionStart` fires with `source: compact` and runs `.guppi/guppi/recall.py`.

> **then:**
> With a `hi` in the session's window, stdout holds a header line, "recall: the context was compacted at HH:MM:SS; the session is" followed by the session folder under the vault, such as `raw/<date>/<hi HHMM>/`, and "Read before the next reply:". Then comes one path per line: the `@` files of `.claude/skills/hi/SKILL.md` in their order, the session's `frontier.md` when it exists, and the Spec when one exists. Last come the line `Frontier:` and the text of `frontier.md` as it stands.
> **＋** The Spec is the `spec.md` of the folder, or before the approval the plan file the event log names last.
> **＋** The list of paths is the `@` lines of the skill file at the moment the hook fires, with no copy in the code: a file added to those lines is in the list without a change to the hook.
> **＋** The texts of the files, the Frontier apart, are not printed, only the paths; the output stays under 10,000 characters.
> **－** Without a `hi` in the window, nothing is printed on stdout, and the exit is 0.
> **－** Another `source` gives nothing: the matcher keeps the hook from firing, and the code checks `source` itself.
> **－** Exit 0 always; an error prints nothing and blocks nothing; the hook writes no file and no event line — `session-start compact` is written by `guppi event`.

```then
update:
- slug: estimate-compact-recall-reloads
  set:
    status: pending
  change: the Criterion replaced whole — the example session folder is a pattern, not a folder of this repository
```

```tasks
- [x] update `estimate-compact-recall-reloads`
- [x] stop: in Work Mode, the person runs `/compact` in the working session, so that the hook of `rule-compact-recall` fires with `source: compact`.
- [x] read `estimate-compact-recall-reloads`
```

### Case 920.2 — The vault-query check names the languages by their role

> **given:**
> `estimate-ask-query-before-a-create`: its Criterion is replaced whole.
> **＋** `.claude/agents/case-guppi.md`: the agent that runs the query.
> **＋** `.claude/agents/ask-guppi.md`: the recipe of the query, rendered from `rule-ask`.
> **＋** `vault/wiki/rules/`: the folder of the first Grep of the query.
> **＋** `vault/archive/`: the folder the Glob of a slug runs over.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A page that already holds the thing is found by meaning, whether the person's words name it in the language of the chat or in the language of the repository, and the `context` of the Case names its slug.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
> **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
> **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
> **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.

```then
update:
- slug: estimate-ask-query-before-a-create
  set:
    status: pending
  change: the Criterion replaced whole — the languages are named by their role
```

```tasks
- [x] update `estimate-ask-query-before-a-create`
- [ ] read `estimate-ask-query-before-a-create`
```

### Case 920.3 — The check of a marked lesson holds its case number in a pointer bracket

> **given:**
> `estimate-synthesis-keeps-actioned-by-the-mark`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian, who does the synthesis.
> **＋** `rule-clean-branch`: sets the bracket of a pointer.
> **＋** `decision-case-M`: the placeholder for the decision that the `actioned` Insight names.
> **＋** `.guppi/guppi/lint.py`: `waits_for_an_event`, which judges the wait of the `method`.

> **when:**
> The librarian, at synthesis, hangs a lesson whose entry carries `addressed_by: decision-case-N` on an existing Insight of the same pattern that stands `actioned` with `addressed_by: decision-case-M`.

> **then:**
> When case N is later than case M — compared number by number, `378.5` after `378.4` — the `update` carries `set: {addressed_by: decision-case-N}`, and `status` stays `actioned`.
> **＋** When case N is not later than M, the `update` carries no `addressed_by`: the field stays `decision-case-M`, and `status` stays `actioned`.
> **＋** Either way the `update` carries `children` plus the lesson; the lesson is `clustered`, the cascade archives it, and the brief reports the pair beside the synthesis.
> **＋** An Insight born from a marked lesson gets, right after its `create`, an `update` with `set: {status: actioned, addressed_by: decision-case-N}` (as set in case 302.2).
> **＋** A lesson with no `addressed_by` sets an `actioned` Insight `open` with `set: {status: open}`, and a new Insight is born `open`.
> **－** `addressed_by` never names two decisions.

```then
update:
- slug: estimate-synthesis-keeps-actioned-by-the-mark
  set:
    status: pending
    method: 'by hand, after a librarian''s run that puts a lesson with `addressed_by` under an Insight that stands `actioned`: the yaml and the brief read against the Criterion'
  change: the Criterion replaced whole — the case number stands in a pointer bracket; the method names its event
```

```tasks
- [x] update `estimate-synthesis-keeps-actioned-by-the-mark`
- [ ] read `estimate-synthesis-keeps-actioned-by-the-mark`
```

### Case 920.4 — The clustering check states where the flag of a read lives

> **given:**
> `estimate-synthesis-clusters`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian, who does the synthesis.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.
> **＋** `.guppi/guppi/lint.py`: `waits_for_an_event`, which judges the wait of the `method`.
> **＋** `vault/wiki/lessons/`: the lessons the synthesis groups.
> **＋** `vault/wiki/insights/`: the Insights the lessons join.
> **＋** `vault/archive/`: the archive, whose read fails nothing here.
> **＋** `estimate-documentation-completes`: the check that, in the repository of GUPPI, flags such a read.

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
> **＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every page the librarian opens at synthesis to judge whether a lesson shares its root cause is named in the report with the outcome: the Insight it joined, or none and why. A read of its Trigger, Root cause, `root_cause`, Pattern or `pattern` outside the two Greps is such an opening.
> **＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
> **－** A read at synthesis of only the fields `status`, `insight`, `children` and `tags` of a page under `vault/wiki/lessons/` or `vault/wiki/insights/`, made to learn which lessons are grouped or which lessons an Insight holds, is not named in the report and fails nothing here.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line until the close of its sprint, and, in the repository of GUPPI, the flag of such a read is the promise of `estimate-documentation-completes`.

```then
update:
- slug: estimate-synthesis-clusters
  set:
    status: pending
    method: 'by hand, after a librarian''s run whose `materialize.yaml` holds at least two lesson entries: the yaml and the report read against the Criterion'
  change: the Criterion replaced whole — the flag of a read is named in the repository of GUPPI only; the method names its event
```

```tasks
- [x] update `estimate-synthesis-clusters`
- [x] read `estimate-synthesis-clusters`
```

### Case 920.5 — The defer of the clean branch ends

> **given:**
> `rule-clean-branch`: the page whose `deferred_by` names `decision-case-893.1`.
> **＋** `decision-case-893.1`: the deferred decision this Case takes up.
> **＋** `.guppi/guppi/generate.py`: clears the defer of a page the superseding Case names.
> **＋** `estimate-generate-writes-the-decision-page`: checks that clearing.
> **＋** `vault/raw/2026-10-30/0304/cases/case-919.md`: Case 919.2 updates `rule-clean-branch` in this session.

> **when:**
> The librarian's run applies the Spec of this session by `generate` of `.guppi/guppi/generate.py`.

> **then:**
> `rule-clean-branch` holds no `deferred_by`, and `decision-case-893.1` stands `superseded`.
> **＋** `guppi backlog` writes no line of `rule-clean-branch` for a defer.
> **－** No text of `rule-clean-branch` changes by this Case.

```then
update:
- slug: rule-clean-branch
  change: 'the defer of case 893.1 taken up: its four Criteria rewritten by case 920, its other checks held by a Frontier item or passed'
```

```tasks
- [x] update `rule-clean-branch`
```

## Case 921 — An Ask question at /hi names the place of the text it asks about

> **context:**
> At `/hi` the main agent puts each open `A` line of the Frontier to the person as a question: the Estimate by slug and the question as the brief gives it. When that question asks the person to judge a text, it names no place where the text stands and quotes none of it, and `/hi` reads no saved chat of an earlier session (case 670.5), so it cannot quote a reply that stood only in such a chat. At the `/hi` of session 2341 the line A2 asked whether "the report that `/handoff` showed after the librarian's run of session 1930" gave the counts, the flags and the lint total; the person read another report, the main agent wrote a failed reading on it, and only `case-guppi` of Case 913 showed the report held the flags and other counts (ledger of session 2341, lines 3 and 5). Lesson L41 of that session, `lesson-hi-asks-a-reading-of-a-text-it-names-no-place-of`, records it; the rule it breaks is `rule-agent-writing`, which tells the agent to name a real source. The person chose that `/hi` names the place of such a text: a file by its path and section, with a quotation of the part the question judges, or a reply shown only in the chat of an earlier session by that session, its date and the reply, with a plain sentence that the agent cannot open that chat; the reading line names that place as its source. Only `rule-skill-hi` changes: every Ask question reaches the person at `/hi`, whoever wrote it, and the reply that acknowledges the opening Case of a sprint puts the `A` lines "as `/hi` does" in `orchestration.md`, so it follows the new text with no change; `rule-handoff` and the librarian's frame `rule-brief` keep the form of the question they write. A Grep for `the Estimate by slug and its question` over `vault/wiki/` printed `orchestration.md`, `rule-orchestration.md`, `estimate-orchestration-asks-in-the-grill-me-shape.md`, `estimate-orchestration-acknowledges-the-opening-with-the-frontier.md`, `rule-skill-hi.md` and `estimate-hi-takes-its-readings.md`, and over `.claude/` printed `.claude/skills/hi/SKILL.md`. The person chose that the texts of `rule-orchestration` and its two Estimates stand: they say which form an Ask question keeps, its own and not the question template, and that the reply puts the `A` lines as `rule-skill-hi` sets it; the question still holds the Estimate by slug and its question, and none of them says what else it holds. The Criterion of `estimate-hi-takes-its-readings` holds the line on how an `A` line is put to the person, so this Case replaces it whole, with its `purpose`; its `method`, a reading of the new Render of `rule-skill-hi` in the Spec at the Retro of the session that changes it, stands. Its line that only the reading step opens pages becomes false once `/hi` opens the file it quotes. A question such as A2 names a report and no path, and the handoff and the brief keep that form, so on a finding of `/pre-spec` the person chose that the step that puts the `A` lines looks for the text by a Grep or a Glob over the files of the repository, never a saved chat, and takes a text it finds in no file as one shown only in a chat. The new Render and the new Criterion both name that step as the one that opens the file it quotes, beside the step that reads the `W` lines. `estimate-hi-writes-frontier` keeps its Criterion: the `A` line in `raw/<date>/<hi HHMM>/frontier.md` keeps its form, since the place stands in the question of the chat and in the reading line alone. `estimate-hi-no-read-calls` speaks of the blocks of the skill and stands. `rule-skill-hi` has `core: true`, so its new sentences carry the pointer to this Case in a bracket at their end, which `.guppi/tests/test_guppi_package.py` reads through a live run of `guppi ship`. The ledger of this session holds no `lesson[error]` line, so no `{addresses:...}` mark stands; lesson L41 belongs to session 2341, and its fix ratified in this session gets no mark.

> **problem:**
> An Ask question at `/hi` that asks the person to judge a text names no place where the text stands and quotes none of it, so the person's answer and the reading line written on it can rest on another text than the one the Estimate means.

> **recommend:**
> - **What should `/hi` say beside an Ask question that asks the person to judge a text?**
>   - Recommended: (a) name the place, and quote the text when it is in a file; for a text shown only in the chat of an earlier session, name that session by its date and start time and the reply, and say that the agent cannot open that chat; the reading line names the same place.
>   - Answer: agreed, (a).
> - **Which page sets this: `/hi` alone, or also the writers of the Ask question?**
>   - Recommended: (a) `/hi` alone; only `rule-skill-hi` changes.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) replace the Criterion of `estimate-hi-takes-its-readings`, its `purpose` with it; its `method` stands.
>   - Answer: agreed, (a).
> - **Do the words in `orchestration.md` on the form of an Ask question change too?**
>   - Recommended: (a) leave them and their two Estimates as they are; `context` says why they stand.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: on a finding of `/pre-spec`, the person agreed that when the question names no path, `/hi` looks for the text by a Grep or a Glob over the files of the repository, such as the brief, the handoff of the session and the page of the Estimate, never a saved chat; when it finds the text it names the path and the section and quotes it, and when it does not, it takes the text as one shown only in a chat; the Render and the Criterion name alike the step that opens the file.
>   - Taken: the new Render and `then` say that the step that puts the `A` lines searches for the text and opens the file it finds; the `－` line on the pages opened names both steps and no saved chat; the `purpose` names the search.

> **given:**
> `rule-skill-hi`: the rule of `/hi`, whose Render sets how an `A` line is put to the person and how its answer is written.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from `rule-skill-hi`.
> **＋** `estimate-hi-takes-its-readings`: its Criterion and `purpose` are replaced.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose `## Ask` lines `/hi` puts to the person.
> **＋** `vault/wiki/brief.md`: the brief, whose `Ask the person` list gives the `A` lines and their questions.
> **＋** `rule-agent-writing`: the rule that tells the agent to name a real source.
> **＋** `.guppi/tests/test_guppi_package.py`: runs `guppi ship` over the live repository, which removes the bracket of a pointer to a Case.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When that question asks the person to judge a text and names no path, the step that puts the `A` lines looks for the text by a Grep or a Glob over the files of the repository, such as `vault/wiki/brief.md`, the handoff of the session and the page of the Estimate. When the text is in a file of the repository, the agent names the path and the section of that file and quotes the part the question judges. When it finds no such file, it takes the text as one shown only in the chat of an earlier session: it names that session by its date and the time of its `hi:` line and the reply that showed the text, and says in a plain sentence that it cannot open that chat.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result and the place it named for the text as its source, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** An open `W` line whose reading cannot run now stays open under `## Work` and is no line under `## Cases`.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only two steps open pages: the step that reads the open `W` lines opens the page of the Estimate of each of them, and the step that puts the `A` lines opens the file it found or the question names, to quote it. Neither opens a saved chat.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: 'Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question.'
    new: 'Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. When that question asks the person to judge a text, name its place. When the question names no path, this step looks for the text by a Grep or a Glob over the files of the repository, such as the brief, the handoff of the session and the page of the Estimate, and opens the file it finds, never a saved chat. For a text in a file of the repository, name the path and the section of the file, with a quotation of the part the question judges. For a text it finds in no file, take it as one shown only in the chat of an earlier session: name that session by its date and the time of its `hi:` line and the reply that showed it, such as the reply after `/handoff` that showed the report of the librarian, with a plain sentence that you cannot open that chat (as set in case 921).'
  - old: then write its reading line in a `LEDGER` block of the reply, which ends in text, the answer as its result (case 531.13).
    new: then write its reading line in a `LEDGER` block of the reply, which ends in text, the answer as its result and the place you named for the text as its source (cases 531.13, 921).
  change: an Ask question that asks the person to judge a text names its place and quotes it when it stands in a file; the reading line names that place as its source
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, leaves each other open W line open under Work with no Cases line, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, with the place of a text the question asks the person to judge, searched for in the files of the repository when the question names no path, and a quotation of it when it stands in a file, writes the answer and that place as its reading line, and opens no page but the Estimates of its open W lines and the file it quotes
  change: the Criterion replaced whole — an Ask question that asks the person to judge a text names its place and quotes it when it stands in a file, and the reading line names that place
```

```tasks
- [x] update `rule-skill-hi`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
- [x] update `estimate-hi-takes-its-readings`
- [x] read `estimate-hi-takes-its-readings`
```

## Case 922 — The Case-id check states where its list of plain sprints matters

> **context:**
> `guppi ship` copies into the clean version each `passed` Estimate whose target page it writes, its Criterion as it stands, and removes each bracket that holds a pointer to a case by `removed` of `.guppi/guppi/pointers.py`. The reading of `estimate-clean-branch-ships-neutral-texts`, taken at the `/hi` of session 1930, listed in its `## Result` fourteen shipped Estimates whose Criterion holds a sentence true only in the repository of GUPPI, and the handoff of session 2341 named five of them as still waiting. Each of the other nine has had its Criterion replaced since that reading, by its History: Case 920.1–920.4 of this session rewrites `estimate-compact-recall-reloads`, `estimate-ask-query-before-a-create`, `estimate-synthesis-keeps-actioned-by-the-mark` and `estimate-synthesis-clusters`; case 918.1 and case 918.2 name the language of `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-build-writes-the-case` by its role, case 918.3 names the code page of the locale in `estimate-python-utf8-output-intact` in place of `cp1252`, case 918.4 opens the Criterion of `estimate-guppi-package-is-ready-after-the-install` with the condition in the repository of GUPPI, and case 917.1 has `estimate-sprint-close-moves-old-event-logs` read `vault/.gitignore`, a file that `guppi ship` writes into the clean version by `VAULT_IGNORE` of `.guppi/guppi/ship.py`. Four of the five were rewritten later in session 1930, after that reading: by their History, case 908.1 named the transcripts folder of `estimate-permissions` as the one the Render of `rule-permissions` names, case 908.2 named the language of `estimate-orchestration-forwards-a-discussion-question` by its role, and cases 904.1 and 904.3 removed the old path of the answer text from `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-example-passes-the-check`; each stands `passed` on its new text. The person chose to leave those four as they stand, so this Case changes none of them, and since the defer of `decision-case-893.1` goes by Case 920.5, the line that says the four are done is one that `/handoff` writes after the Retro commit, in the section of the Render of `rule-handoff` that fits it, `## Observations`; this Case leaves no task on that file in Work Mode, since that Render has `/handoff` write the handoff as one document in its sections, in their order, once the tree is clean.
>
> The fifth, `estimate-ratification-case-id-carries-the-sprint`, was rewritten by case 880.15 before the reading, and the reading still listed it for `PLAIN_SPRINTS`. With its pointer brackets removed, its sentence reads that the sprints that `PLAIN_SPRINTS`, a fixed list in `.guppi/guppi/caseid.py`, names keep plain ids to their close; the clean version takes `.guppi/guppi/caseid.py` as it stands, `ship.py` leaving out only the files of its `LEFT_OUT`, and there `PLAIN_SPRINTS = ("migration", "plugin")` names two sprints of GUPPI. The person chose to add one sentence after it that states its condition, in the repository of GUPPI, which the Criterion of `estimate-clean-branch-ships-neutral-texts` accepts: a sentence that states its condition holds as it reads in a project that installed GUPPI. That Criterion is the rule of this Case, and it stands, since this Case changes a text it judges and not its promise. The new sentence holds no pointer, and it says what the comment above `PLAIN_SPRINTS` in `.guppi/guppi/caseid.py` says, that the list holds the sprints opened before sprint ids came in. This Case replaces the Criterion of `estimate-ratification-case-id-carries-the-sprint` whole, every line as it stands and the one sentence added, and that Estimate checks it; its `purpose` and `method` speak of no sentence that changes and stand. The replaced Criterion sets it `pending`, and `rule-ratification`, `core: true`, already stands `draft`, so the clean version loses nothing more; its `method`, the tests of `.guppi/tests/test_caseid.py` and the two Renders, runs at the Retro of this session.
>
> A Grep of the five pages under `vault/wiki/estimates/` for `GUPPI|Russian|English|c--|migration|plugin|old path|writer is live|case \d` printed, inside a `## Criterion`, only lines 23 and 25 of `estimate-ratification-case-id-carries-the-sprint`; its other hits are `sprint` fields, History lines and Results, which stand. A Grep of the repository, `vault/raw/` and `vault/archive/` left out, for `ratification-case-id-carries-the-sprint` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `.guppi/tests/test_caseid.py`, `vault/wiki/estimates/estimate-clean-branch-ships-neutral-texts.md` and `vault/wiki/rules/rule-ratification.md`: the docstring of the test, a Result, the field `estimates` and a History line, which the change does not make false; the brief and the log are not read. Of the tests that read the live vault, the live build of `.guppi/tests/test_ship.py` leaves a `pending` Estimate out and judges a shipped one by `outside` of `.guppi/guppi/pointers.py`, and the new sentence holds no pointer; `.guppi/tests/test_guppi_package.py` looks for old commands and paths, and the new sentence holds none. The Greps of the session's ledger for `lesson\[error\]` and `\{addresses:` printed nothing, so no line carries a mark.

> **problem:**
> The handoff of the last session named five shipped checks that still held a sentence true only in the repository of GUPPI, but four of them were rewritten after the reading that listed them, and the fifth names a fixed list whose sprints exist only in the repository of GUPPI without saying so.

> **recommend:**
> - **What does this Case do with the four checks already rewritten?**
>   - Recommended: (a) leave them as they stand; the handoff says they are done.
>   - Answer: agreed, (a).
> - **What becomes of the plain-id sentence of the Case-id check?**
>   - Recommended: (b) add a sentence that states where the list matters, in the repository of GUPPI.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: at `/pre-spec`, drop the Work Mode task that writes a line into the handoff of this session, since the Render of `rule-handoff` has `/handoff` write that file whole after the Retro commit.
>   - Taken: the task and its line of `given` are gone; the `context` says that `/handoff` writes the line in `## Observations`.
> - **Change**
>   - Asked: at `/pre-spec`, the reading listed fourteen Estimates, not five; check the others against the words it named and fix the count.
>   - Taken: the `context` gives the fourteen and names the Case that replaced the Criterion of each of the other nine; none still holds the words the reading named, so no round was needed.

> **given:**
> `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/caseid.py`: holds `PLAIN_SPRINTS` and reads a Case id in both forms.
> **＋** `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py`, `.guppi/guppi/materialize.py`: the readers of a Case id.
> **＋** `vault/wiki/orchestration.md`: the Render of `rule-orchestration` that the main agent follows.
> **＋** `vault/wiki/sprint.md`: the sprint page whose first heading gives the open sprint.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of a session, whose `create` line of a sprint page gives the open sprint.
> **＋** `/sprint-open`: the skill that sets the id of the opening Case of a sprint.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.

> **when:**
> `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py` or `.guppi/guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
> **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run --project .guppi guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
> **＋** Or `uv run --project .guppi guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.

> **then:**
> A Case id of a sprint that `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py` does not list is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case (sprint ids came in with case 788.2).
> **＋** The readers read a Case id through `.guppi/guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
> **＋** The sprints that `PLAIN_SPRINTS`, a fixed list in `.guppi/guppi/caseid.py`, names keep plain ids to their close (the sprints of that list opened before case 788.2).
> **＋** In the repository of GUPPI, that list names the sprints opened before sprint ids came in.
> **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
> **＋** `uv run --project .guppi guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
> **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
> **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
> **－** The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id.
> **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
> **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
> **－** An id with no sprint part, such as `785.1`, stays as it is, and no page, file or citation is renamed.

```then
update:
- slug: estimate-ratification-case-id-carries-the-sprint
  set:
    status: pending
  change: the Criterion replaced whole — a sentence states that, in the repository of GUPPI, PLAIN_SPRINTS names the sprints opened before sprint ids came in
```

```tasks
- [x] update `estimate-ratification-case-id-carries-the-sprint`
- [x] read `estimate-ratification-case-id-carries-the-sprint`
```

## Case 923 — The main agent states what a subagent did only from its transcript

> **context:**
> The main agent sometimes writes a fact that a source already holds from its own reading or impression, not from the source. `insight-orchestration-writes-from-its-own-reading` clusters two such slips. In `lesson-orchestration-claimed-a-reading-before-taking-it` the main agent said that no "modified since read" refusal came in the session, from its impression of the summaries of `case-guppi`, which do not show their tool errors, and read the transcripts only later. In `lesson-orchestration-retyped-a-ratification-line` it retyped a ledger line of a showing from its own reading of the defers, with the wrong `{supersedes:...}` mark, where the summary held the right one.
>
> The second slip is already covered. The Render of `rule-orchestration` says that the `ratification` of a showing holds the ledger lines as the summary holds them, `estimate-orchestration-shows-the-built-case` promises it, and the `Stop` check of `rule-case-check` refuses a showing that differs from the stored text, which is how that slip was caught. The Proposal of the Insight asks for such a check, and it already stands. The first slip broke only the general sentence of `rule-agent-writing` that a claim is no wider than the output it rests on. No text says where a fact about a subagent's tool calls comes from, and no check caught that slip. The person chose one sentence in the Render of `rule-orchestration`, placed after the sentence on the short form written with no dispatch, and a new Estimate on it. The Insight is set `actioned` by this Case, with the bare slug `decision-case-923` in `addressed_by`, as `rule-insights-schema` sets it. The existing Estimates of `rule-orchestration` speak of other promises, so their Criteria stand.
>
> A Grep for `written with no dispatch` over `vault/wiki/` printed `vault/wiki/orchestration.md` and `vault/wiki/rules/rule-orchestration.md`, so the anchor of the pair falls once on the Rule page. A Grep for `transcript` over the `*.md` files of `.claude/` printed only `.claude/skills/hi/SKILL.md`, whose readings at `/hi` read no transcript of an earlier session. The new sentence speaks only of a subagent of the session, so it does not cover that moment. The report of `.claude/skills/pre-spec/SKILL.md` gives the list of what the `ask-guppi` run did not check, and by `.claude/agents/ask-guppi.md` the last lines of that list name each rule a search of `ask-guppi` broke. That is a subagent's own report of its calls, which the new sentence lets the main agent pass on marked as that report, so the report of `/pre-spec` stands as it is. A Grep for `orchestration` over `.guppi/tests/` printed `test_orchestration.py`, `test_casecheck.py`, `test_onward.py` and `test_ratified.py`. Only `test_orchestration.py` reads `vault/wiki/orchestration.md` live, and its functions `example`, `store_of_showing` and `defer_records` read only the blocks tagged `showing` and `defer`, which the new sentence does not touch. A Grep for the slug of the Insight over `vault/wiki/`, `.guppi/` and `.claude/` printed `brief.md`, `backlog.md`, `log.md` and the two lesson pages. The lesson pages name the Insight in their `insight` field, which stays true. A Glob `vault/wiki/**/estimate-orchestration-states-*.md` printed nothing, so the new slug is free. The ledger of the session holds no `lesson[error]` line and no `{addresses:` mark, so this Case closes no lesson of this session.

> **problem:**
> No text says that a fact about what a subagent did comes from its transcript. The main agent stated such a fact from the subagents' summaries, which do not show their tool errors.

> **recommend:**
> - **What the Case does with the Insight**
>   - Recommended: (b) add one sentence to `orchestration.md`: a fact about what a subagent did is stated only after the main agent reads it in that subagent's transcript, and mark the Insight as dealt with.
>   - Answer: agreed, (b).
> - **Which Estimate checks the new sentence**
>   - Recommended: (a) a new Estimate, `estimate-orchestration-states-a-subagent-fact-from-its-transcript`, read by hand at the Retro of this session and after the first reply under the new Render that states such a fact.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after a finding of `/pre-spec`, the person chose that the sentence tells two cases apart: a fact the main agent states as its own of what a subagent did needs that subagent's transcript, and what a subagent reports of its own calls the main agent may pass on with no transcript, marked as that subagent's report; the report of `/pre-spec` stays as it is.
>   - Taken: the new sentence, the `then` and the `purpose` of the new Estimate now tell the two cases apart.

> **given:**
> `rule-orchestration`: the rule of the main agent's work, rendered into `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the file the main agent loads at `/hi`.
> **＋** `estimate-orchestration-states-a-subagent-fact-from-its-transcript`: the new Estimate of the sentence.
> **＋** `insight-orchestration-writes-from-its-own-reading`: the Insight this Case actions.

> **when:**
> The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, states in a reply what a subagent of the session did: a tool call it made, a tool error it met, or a hook that refused its call.

> **then:**
> Before a reply that states such a fact as its own, the main agent has read that fact in the transcript of that subagent.
> **＋** The reply states no such fact as its own from the summary of the subagent alone.
> **－** What a subagent reports of its own calls, such as the rules a search of `ask-guppi` broke, the main agent may pass on with no transcript, marked as the report of that subagent.
> **－** A ledger line of a showing is still copied from the summary of `case-guppi`, as `vault/wiki/orchestration.md` sets it.

```then
create:
- slug: estimate-orchestration-states-a-subagent-fact-from-its-transcript
  ref: rule-orchestration
  kind: QA
  purpose: Whether the main agent states as its own what a subagent of the session did only after it reads the fact in the transcript of that subagent, and passes on a subagent's report of its own calls marked as that report
  method: 'by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec read against the Criterion; after the first reply of the main agent under that Render that states what a subagent did: that reply and the tool calls of the main agent before it read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - orchestration
update:
- slug: rule-orchestration
  replace:
  - old: A deferred decision in the short form is the agent's own, written with no dispatch (case 419.1).
    new: A deferred decision in the short form is the agent's own, written with no dispatch (case 419.1). A fact of what a subagent of the session did — a tool call it made, a tool error it met, a hook that refused its call — the main agent states as its own only after it reads that fact in the transcript of that subagent, never from its summary alone, since a summary does not show its tool errors; what a subagent reports of its own calls the main agent may pass on with no transcript, marked as the report of that subagent, such as by the words of `ask-guppi` (as set in case 923).
  change: the main agent states what a subagent did only after it reads the fact in its transcript (case 923)
- slug: insight-orchestration-writes-from-its-own-reading
  set:
    status: actioned
    addressed_by: decision-case-923
  change: 'actioned: the main agent states what a subagent did only after it reads the fact in its transcript, in rule-orchestration; the ratification lines of a showing were already copied from the summary and checked by rule-case-check (case 923)'
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] create `estimate-orchestration-states-a-subagent-fact-from-its-transcript`
- [x] read `estimate-orchestration-states-a-subagent-fact-from-its-transcript`
- [x] update `insight-orchestration-writes-from-its-own-reading`
```

## Case 924 — case-guppi reads the steps that read or repeat a step it changes

> **context:**
> A Case can change what one step of a skill, an agent or a hook writes, copies or shows. Today `case-guppi` judges that change from the step in front of it. The Render of `rule-case-build` makes it search for the slug of a page the change makes false and for the name of a field, term or command whose behaviour changes, but nothing makes it read the other steps that read that output, the other skill that does the same step, or the new path its own Case adds. The Insight `insight-case-build-changes-a-step-without-reading-its-readers` clusters two lessons of this cause. In `lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes`, Case 851 claimed that the readers of the `Branch:` line stand, judged by the old path alone, though on its new path the line still read `none: …`. In `lesson-case-build-changes-a-step-without-reading-what-reads-it`, Case 903.2 named only /box as the step that shows the librarian's report though /handoff shows it too, and Case 905 left step 5 of the Render of `rule-plugin-install` checking a file that its new step 4 no longer copies. Each time /pre-spec found the fault after the person had ratified the Case. The person chose one new sentence in the paragraph of the Render on the checks before the summary, placed after the sentence on a fact that no slug marks, with a new Estimate of its own, and a search over the rules and `.claude/` only, since the code readers already have the sentences of cases 736.1, 754 and 869. The pair anchors on that sentence; a Grep of the pattern `For a fact that no slug marks, read the index lines` over `vault/wiki/rules/rule-case-build.md` printed a count of 1. `estimate-case-build-checks-the-finished-case` stands: each line of its Criterion names one check before the summary, and none of them becomes false; the new search is a promise of its own, which the new Estimate checks. No other Estimate of the page speaks of the readers of a step. The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed; it is set `actioned` with `addressed_by: decision-case-924`, the bare slug, as `rule-insights-schema` sets it (case 712). A Grep of the slug of the Insight over the repository outside `vault/raw/` printed `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/archive/plugin/2026-10-29/1930/raw/materialize.yaml` and the two lesson pages: the backlog line names the Insight as the source of this item and this Case does not edit `backlog.md`, the log and the archive are not read, and the lessons keep their `insight` link. `.guppi/tests/test_guppi_package.py` reads every file of `.claude/` and every live page for `uv run guppi`, `uv run pytest`, `guppi/` and `tests/`; the new sentence and the new Estimate name none of them. The session's ledger holds no `lesson[error]` line, so no `{addresses:...}` mark is written. Case 926, whose finished file was read after its build ended, also changes the Render of `rule-case-build`: its pair anchors on the sentence of case 869 in the paragraph on the frame and replaces only that sentence, while the pair of this Case anchors on a sentence of the paragraph on the checks before the summary, so the two `old` values do not overlap and neither pair changes the text the other matches. Each Case renders `.claude/agents/case-guppi.md` after its own pair, which takes both changes. The sentence of Case 926 is about a claim on what code does, and the new sentence here is about the steps of the rules and `.claude/` that read or repeat an output, so neither text contradicts the other; this Case changes neither `estimate-case-build-reads-the-code-it-states` nor the Insight that Case 926 actions.

> **problem:**
> `case-guppi` changes what a step writes, copies or shows from the one step in front of it, and does not read the steps and skills that read that output or do the same step, or the new path its own Case adds, so the Case holds for one step only and /pre-spec finds the rest after the person has ratified it.

> **recommend:**
> - **Where the fix goes**
>   - Recommended: (a) a new sentence in the paragraph of the Render on the checks before the summary, a new Estimate `estimate-case-build-reads-the-readers-of-a-changed-step`, and the Insight set actioned by this Case.
>   - Answer: agreed, (a).
> - **What the reading covers**
>   - Recommended: (a) the steps of the harness texts: the rules in `vault/wiki/rules/` and the files under `.claude/`, the steps after it in the same text and the new path the Case adds.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the /pre-spec finding that the second part of the `method` read the /pre-spec of this session, whose Cases were built on the old Render, and so waited for no event that could show the behaviour.
>   - Taken: that part now waits for the /pre-spec of the first session whose `case-guppi` runs on the Render this Case sets; the first part, the Render in the Spec read at the Retro, stays.

> **given:**
> `rule-case-build`: the Rule whose Render is the prompt of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from that Render.
> **＋** `estimate-case-build-reads-the-readers-of-a-changed-step`: the new check of this promise.
> **＋** `insight-case-build-changes-a-step-without-reading-its-readers`: the Insight this Case actions.
> **＋** `rule-insights-schema`: the rule that sets `actioned` and `addressed_by`.
> **＋** `vault/wiki/rules/`: the Rule pages whose Renders the search reads for steps.
> **＋** `.claude/`: the rendered harness files the search reads for steps.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
create:
- slug: estimate-case-build-reads-the-readers-of-a-changed-step
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, when its Case changes what a step writes, copies or shows or adds a path to it, reads each step and skill that reads that output or does the same step, the steps after it and the new path included, and names each one in context or enters it in the Case
  method: 'by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line; after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of a changed step: the findings of ask-guppi at that /pre-spec read for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
update:
- slug: rule-case-build
  replace:
  - old: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning.
    new: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. When the Case changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, Grep `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step, and read each step and skill that reads that output or does the same step, the steps after it in the same text and the new path your Case adds included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in case 924).
  change: case-guppi reads the steps and skills that read or repeat the output of a step its Case changes, and the new path its Case adds
- slug: insight-case-build-changes-a-step-without-reading-its-readers
  set:
    status: actioned
    addressed_by: decision-case-924
  change: 'actioned: case-guppi reads the steps that read or repeat a step its Case changes'
```

```tasks
- [x] update `rule-case-build`
- [x] create `estimate-case-build-reads-the-readers-of-a-changed-step`
- [x] update `insight-case-build-changes-a-step-without-reading-its-readers`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-reads-the-readers-of-a-changed-step`
```

## Case 925 — A hook keeps ask-guppi from reading a Decision page

> **context:**
> `ask-guppi` checks the plan against the vault at `/pre-spec`. Its frame, `.claude/agents/ask-guppi.md` rendered from `rule-ask`, lets it open a Decision page for two reasons: a page of its answer carries `deferred_by`, or the question asks why something was decided. At `/pre-spec` it may open the Decision only after a finding of its own names the page (case 800.2). Only the agent's judgment holds this rule. The hook of `rule-search-leaves-out-decisions`, `.guppi/guppi/grepguard.py`, leaves the Decision pages out of a wide Grep. It lets a Grep inside `vault/wiki/decisions/` pass unchanged, and it never runs on a Read (`before` of that file, read whole). The agent broke the rule twice, by the two children of `insight-ask-guppi-reads-a-decision-outside-its-frame`. At the `/pre-spec` of session 1426 it read the Decision behind the `deferred_by` of `entity-guppi`, a page that no finding named. Case 800.2 then made the text stricter. Case 800 chose text over a hook, since a hook cannot see the findings. At the `/pre-spec` of session 1907 the agent grepped `decision-case-882.3.md`, the Decision behind the `deferred_by` of `rule-clean-branch`, a page that Case 893.1 took up and that no finding named. That was the case that the text of 800.2 forbids. Both times the agent reported the break itself.
>
> The person chose a hook that needs no finding: it refuses every Read of a Decision page and every Grep inside `vault/wiki/decisions/` that `ask-guppi` makes. The hook tells `ask-guppi` from other agents by `agent_type`. The hooks documentation, https://code.claude.com/docs/en/hooks, says that when a subagent calls a tool, the `PreToolUse` input carries the `agent_id` and `agent_type` that identify the subagent, and that a hook denies a call by `permissionDecision: deny`. `ratified.py` reads the same field for `case-guppi` (its docstring: measured 2026-10-05, session 0311). Today only `/pre-spec` dispatches `ask-guppi` as an agent (a Grep of `ask-guppi` over `.claude/` printed `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md`, `.claude/rules/search-leaves-out-decisions.md`, `.claude/skills/hi/SKILL.md` and `.claude/skills/pre-spec/SKILL.md`; the agent file names itself, the hit in `hi/SKILL.md` names the source of a Frontier line, and `case-guppi` runs the recipe itself). So the agent keeps no reason. A finding or an `exists` or `near` line on a page with `deferred_by` names the Decision by its slug, and an answer to why something was decided gives the slug that the page's `origin` points to. `case-guppi`, which runs the recipe itself with its own `agent_type`, keeps both reasons. So the sentence of `rule-case-build` that it opens `vault/wiki/decisions/` only as `ask-guppi.md` allows stays true, and so does the Criterion of `estimate-ask-query-before-a-create` that Case 920.2 sets, since that Criterion speaks of the run of `case-guppi` and Case 920 changes no text of `rule-ask`. By the person's answers, `grepguard` also runs on `Read`: `rule-hook-registry` adds it to the `Read` matcher beside `pageread`, the hook of `rule-page-read`. On a Read under `vault/wiki/` with no `offset` or `limit`, `before` of `.guppi/guppi/pageread.py` (read whole) returns `updatedInput` with `limit` set to the line before `## History` and no permission decision, a Decision page included. The hooks documentation says that when several `PreToolUse` hooks return different decisions, `deny` wins over `defer`, `ask` and `allow`, so the refusal holds and the Read does not run; it does not say what becomes of the `updatedInput`, and the Case rests on nothing of it. `estimate-page-read-cuts-the-history` says that the agent gets the frontmatter and the body, which a refused Read does not give, so Case 925.6 replaces its Criterion with one more `－` line and sets its `method` to a reading in Work Mode; until that reading passes, `rule-page-read`, with `core: true`, stands `draft`. A Grep refusal works once Work Mode changes the code, since the hook already runs on `Grep`. A Read refusal works after the librarian's run renders `.claude/settings.json`. `orchestration.md` says that the agent dispatches `ask-guppi` only at pre-spec, so the live part of the new check waits for the first `/pre-spec` after that render, and reads each Decision call of `ask-guppi` there. `estimate-hook-registry-rendered` promises only that the file equals the Render, so it stands (case 378.5).
>
> Sentences of six checks become false, so the Case has one sub-case per promise. Case 925.1 creates `estimate-search-leaves-out-decisions-refuses-ask-guppi`; a Glob `vault/**/estimate-search-leaves-out-decisions-refuses*.md` printed nothing, so the slug is free, and the `create` has a `ref`, so no vault query runs before it. Case 925.2 replaces the Criterion of `estimate-search-leaves-out-decisions-by-the-grep-hook`, whose lines say that the hook never refuses a call and that a Grep inside the folder passes unchanged; a Grep of `never refuses|refuses no call` over `vault/wiki/` printed only that page. Its `method` waited for the `/hi` of a later session and is set anew, since the Grep exclusion already runs live. Case 925.3 replaces the Criterion of `estimate-search-leaves-out-decisions-in-every-agent`, which gives `ask-guppi` the reasons of its frame. Case 925.4 changes the Render of `rule-ask` and replaces the Criterion of `estimate-ask-opens-a-decision-only-for-a-finding`. Case 925.5 replaces the Criterion of `estimate-ask-finds`, whose line says that a finding on a page with `deferred_by` gives the `## Problem` of its Decision. A Grep of `deferred_by.{0,120}(Problem|open the decision|Decision it names)|(Problem|open the decision).{0,120}deferred_by` over `vault/wiki/` printed `log.md`, `lessons/lesson-ask-guppi-read-a-decision-page-without-a-reason.md`, `insights/insight-ask-guppi-reads-a-decision-outside-its-frame.md`, `estimates/estimate-ask-finds.md` and `rules/rule-ask.md`. The lesson and the Pattern of the Insight record the past and stand. The Insight stands `open` and `backlog.md` lists it, so Case 925.1 sets it `actioned` with `addressed_by` naming its own Decision, which `rule-insights-schema` requires for `actioned`. A Grep of `` reaches the deferred decision|Decisions through `deferred_by` `` over `vault/wiki/` printed `entities/entity-glossary.md`, `glossary.md`, `rules/rule-rules-schema.md` and `rules/schema.yaml`. Their sentences say that `ask-guppi` reaches the deferred decision through the `deferred_by` of an index line, without opening the page that carries it. That stays true: the agent still finds the Decision there, and now names it by that slug. So they stand.
>
> A Grep of `ask-guppi.{0,200}(Decision|decisions/)|(Decision|decisions/).{0,200}ask-guppi` over `vault/wiki/`, `log.md` and `brief.md` left out, printed `backlog.md`, `rules/rule-case-build.md`, the two lessons, the Insight, `rules/rule-search-leaves-out-decisions.md`, `estimates/estimate-search-leaves-out-decisions-in-every-agent.md`, `estimates/estimate-ask-opens-a-decision-only-for-a-finding.md`, `rules/rule-ask.md` and `estimates/estimate-ask-searches-at-prespec.md`. The line of `backlog.md` is the generated line of this item. The `－` line of `estimate-ask-searches-at-prespec` hands Decision reads to `estimate-search-leaves-out-decisions-in-every-agent`, which still reads them, so it stands. The same Grep over `.claude/` printed `.claude/agents/case-guppi.md`, the sentence of `rule-case-build` above. A Grep of `deferred_by|decisions/|Decision` over `.claude/skills/pre-spec/SKILL.md` printed nothing, so the skill sets nothing about Decision reads. A Grep of `agent_type` over `.guppi/guppi/` printed `casecheck.py`, `event.py` and `ratified.py`. Each compares the field with `case-guppi`, or names `subagent_type`, so no code judges a call of `ask-guppi`. The path judgment is `pageread.inside` over `wiki_root(...) / "decisions"`, which `grepguard` already imports, and the Read side uses it too. A Grep of `REPO / "\.claude"|ROOT / "\.claude"|"\.claude" / "(agents|rules)"|rule-ask|rule-search-leaves|rule-hook-registry` over `.guppi/tests/` printed `test_guppi_package.py` and `test_grepguard.py`. `test_guppi_package.py` reads `.claude/settings.json` for the commands of `ledger`, `onward`, `ratified` and `casecheck`, and the files of `.claude/` for `uv run guppi` and `uv run pytest`, which the new texts do not hold. `test_grepguard.py` builds its vault in a temporary folder. Its test that another tool passes unchanged sends a `Read` with no `agent_type`, which still passes. The two lessons were written in sessions 1426 and 1907, so no decision line carries `{addresses:...}` for them (case 284.2), and the session's ledger holds no `error` lesson.

> **problem:**
> A rule that only the agent's judgment holds failed twice: `ask-guppi` read a Decision page for a reason its frame does not name, and the stricter text of case 800.2 did not stop the second read.

> **recommend:**
> - **How should a Decision read outside the frame of ask-guppi be stopped?**
>   - Recommended: (a) a hook refuses every Decision read by `ask-guppi`, and the text drops its reasons: a finding or answer line on a put-off page names the Decision by its slug.
>   - Answer: agreed, (a).
> - **Where does the refusal of a Read run?**
>   - Recommended: (a) the search guard `grepguard` also runs on Read.
>   - Answer: agreed, (a).
> - **One Case or one part per promise?**
>   - Recommended: (a) five parts, one per promise.
>   - Answer: agreed, (a).
> - **How is the refusal checked?**
>   - Recommended: (a) a new check, `estimate-search-leaves-out-decisions-refuses-ask-guppi`.
>   - Answer: agreed, (a).
> - **How is the new text of ask-guppi checked?**
>   - Recommended: (a) rewrite the conditions of `estimate-ask-opens-a-decision-only-for-a-finding`, with its purpose and method.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the `/pre-spec` report, which the person agreed to, asked to put the pointers of the new texts in brackets of their own, to read the live refusal from the first `/pre-spec` after the render instead of a dispatch by hand, to set the Insight `actioned`, to settle the glossary rows and the schema line on `deferred_by`, to settle `estimate-page-read-cuts-the-history`, and to say which hook answer holds on a refused Read.
>   - Taken: the pairs and methods rewritten; the `method` of the new check waits for that `/pre-spec`; Case 925.1 sets the Insight `actioned`; `context` says why the glossary rows and the schema line stand; Case 925.6 adds one exception line to the Criterion of `estimate-page-read-cuts-the-history`; `context` gives the order of precedence of the hooks documentation.

### Case 925.1 — The search guard refuses a Decision read by ask-guppi

> **given:**
> `rule-search-leaves-out-decisions`: the rule of Decision reads; its Purpose and Render change.
> **＋** `.guppi/guppi/grepguard.py`: the hook that refuses the call.
> **＋** `.guppi/tests/test_grepguard.py`: the tests of the hook.
> **＋** `rule-hook-registry`: registers the hook on `Read` too.
> **＋** `.claude/settings.json`: the registrations, rendered from `rule-hook-registry`.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `rule-page-read`: the other hook on `PreToolUse` of `Read`; its code is unchanged.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the new check of the refusal.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `insight-ask-guppi-reads-a-decision-outside-its-frame`: the Insight whose cause the hook closes; set `actioned`.

> **when:**
> `ask-guppi` calls Read with a `file_path` under `vault/wiki/decisions/`, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it, and `uv run --project .guppi guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Read` and of `Grep` in `.claude/settings.json`, reads the call with `agent_type` `ask-guppi`.

> **then:**
> The hook refuses the call by `permissionDecision: deny`, with a reason that names the path and `rule-search-leaves-out-decisions`, and exits 0; the call does not run.
> **＋** The same Read or Grep by the main agent, by `case-guppi` or by the librarian passes unchanged.
> **＋** A Read of `ask-guppi` outside `vault/wiki/decisions/` passes unchanged, and a Grep of `ask-guppi` over a folder that holds `vault/wiki/decisions/` gets the exclusion at the end of its `glob`, as for any agent.
> **－** A Glob of `ask-guppi` that prints the path of a Decision page passes: a path is no text of the page.
> **－** A payload the hook cannot read, or an error, lets the call pass, with one line on stderr.

```then
create:
- slug: estimate-search-leaves-out-decisions-refuses-ask-guppi
  ref: rule-search-leaves-out-decisions
  kind: QA
  purpose: Whether the PreToolUse hook grepguard refuses a Read of a Decision page and a Grep inside vault/wiki/decisions/ made by ask-guppi, and leaves the same calls of every other agent unchanged
  method: 'uv run --project .guppi pytest .guppi/tests/test_grepguard.py; by hand, after the first /pre-spec that runs once the librarian''s run has rendered .claude/settings.json: each Read and each Grep of ask-guppi on vault/wiki/decisions/ in its agent transcript refused, recorded in the estimate line'
  tags:
  - hooks
  - harness
  - session
update:
- slug: rule-search-leaves-out-decisions
  replace:
  - old: a Grep inside `vault/wiki/decisions/` it leaves unchanged, and the file keeps the rule on reading a Decision page
    new: a Grep inside `vault/wiki/decisions/` it leaves unchanged but for a call of `ask-guppi`, whose Read of a Decision page and Grep inside that folder the same hook refuses, and the file keeps the rule on reading a Decision page
  - old: which the hook leaves unchanged, and only
    new: which the hook leaves unchanged but for a call of `ask-guppi`, and only
  - old: 'A Glob may print the path of a Decision page: a path is no text of the page.'
    new: |-
      The frame of `ask-guppi` names no reason to read a Decision page, so the same hook, on `Read` and on `Grep`, refuses a Read of a Decision page and a Grep inside `vault/wiki/decisions/` made by `ask-guppi`, and leaves such a call of another agent unchanged (as set in case 925.1).
      - A Glob may print the path of a Decision page: a path is no text of the page.
  change: the hook refuses a Read of a Decision page and a Grep inside vault/wiki/decisions/ by ask-guppi (case 925.1)
- slug: rule-hook-registry
  replace:
  - old: '"uv run --project .guppi guppi pageread", "timeout": 30 } ] },'
    new: '"uv run --project .guppi guppi pageread", "timeout": 30 }, { "type": "command", "command": "uv run --project .guppi guppi grepguard", "timeout": 30 } ] },'
  change: the hook grepguard registered on PreToolUse of Read beside pageread (case 925.1)
- slug: insight-ask-guppi-reads-a-decision-outside-its-frame
  set:
    status: actioned
    addressed_by: decision-case-925.1
  change: 'actioned: a hook refuses every Decision read of ask-guppi (case 925.1)'
```

```tasks
- [x] update `rule-search-leaves-out-decisions`
- [x] update `rule-hook-registry`
- [x] create `estimate-search-leaves-out-decisions-refuses-ask-guppi`
- [x] update `insight-ask-guppi-reads-a-decision-outside-its-frame`
- [x] `.guppi/guppi/grepguard.py`: `before` refuses a `Read` whose `file_path`, and a `Grep` whose searched path, lies in `vault/wiki/decisions/` when the payload's `agent_type` is `ask-guppi`, by `permissionDecision: deny` with a reason that names the path and `rule-search-leaves-out-decisions`, judged by `pageread.inside` over the folder the exclusion already uses; every other call keeps its behaviour, and the module docstring says so.
- [x] `.guppi/tests/test_grepguard.py`: tests that a `Read` of a Decision page and a `Grep` of that folder and of a file in it by `ask-guppi` are refused; that the same calls by `case-guppi`, by the librarian and with no `agent_type` pass unchanged; that a `Read` of `ask-guppi` outside the folder passes; that a `Grep` of `ask-guppi` over the wiki still gets the exclusion.
- [x] `uv run --project .guppi guppi render`: `.claude/rules/search-leaves-out-decisions.md`
- [x] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [ ] read `estimate-search-leaves-out-decisions-refuses-ask-guppi`
```

### Case 925.2 — The check of the search guard names the one refusal

> **given:**
> `estimate-search-leaves-out-decisions-by-the-grep-hook`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/grepguard.py`: the hook the Criterion speaks of.
> **＋** `.claude/settings.json`: where the hook is registered.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `!**/decisions/**`: the exclusion the hook puts at the end of a `glob`.

> **when:**
> The main agent or any subagent calls Grep, and `uv run --project .guppi guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Grep` in `.claude/settings.json`, reads the call.

> **then:**
> When the searched folder — the `path` of the call, or the working directory when the call has none — is a folder that holds `vault/wiki/decisions/`, the hook returns the call by `updatedInput` with `!**/decisions/**` at the end of its `glob`, after a space when the `glob` holds another filter, and with no permission decision.
> **＋** A `glob` that already ends with `!**/decisions/**` is not changed; one that holds it elsewhere gets it again at the end.
> **＋** The Grep then prints no line and no path of a file under `vault/wiki/decisions/`.
> **＋** A call of the librarian is changed in the same way as a call of any other agent.
> **－** A Grep of an agent other than `ask-guppi` whose `path` is `vault/wiki/decisions/` or lies in it passes unchanged: an agent greps there only for a reason of its frame.
> **－** A Grep whose `path` is one file outside `vault/wiki/decisions/`, or a folder that does not hold `vault/wiki/decisions/`, passes unchanged.
> **－** The hook refuses no call but a Read or a Grep of `ask-guppi` on a Decision page, which `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads; a payload it cannot read or an error lets the call pass unchanged.

```then
update:
- slug: estimate-search-leaves-out-decisions-by-the-grep-hook
  set:
    status: pending
    method: uv run --project .guppi pytest .guppi/tests/test_grepguard.py, then by hand in Work Mode a Grep over vault/wiki/ with no glob in the main agent and in a subagent, whether it prints a file under vault/wiki/decisions/, recorded in the estimate line
  change: the Criterion replaced whole — the hook refuses the Decision reads of ask-guppi alone (case 925.2)
```

```tasks
- [x] update `estimate-search-leaves-out-decisions-by-the-grep-hook`
- [x] read `estimate-search-leaves-out-decisions-by-the-grep-hook`
```

### Case 925.3 — The check of Decision reads gives ask-guppi no reason

> **given:**
> `estimate-search-leaves-out-decisions-in-every-agent`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `.claude/agents/ask-guppi.md`: the frame that names the reasons of `case-guppi`.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal.
> **＋** `estimate-search-leaves-out-decisions-by-the-grep-hook`: the check of the exclusion in a wide Grep.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, outside this promise.

> **when:**
> A session starts after `uv run --project .guppi guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Read, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it.

> **then:**
> `.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
> **＋** The text of a Decision page reaches `case-guppi` only by a Read of its path or by a Grep whose `path` is `vault/wiki/decisions/` or lies in it, for a reason of `.claude/agents/ask-guppi.md`: a page of its answer carries `deferred_by`, or the question asks why something was decided.
> **＋** The text of a Decision page reaches the main agent for no reason, and reaches `ask-guppi` by no call.
> **－** An `addressed_by` that names a Decision page is no reason to read it.
> **－** Whether the hook refuses a Read or a Grep of `ask-guppi` on a Decision page is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.
> **－** Whether a Grep over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
> **－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

```then
update:
- slug: estimate-search-leaves-out-decisions-in-every-agent
  set:
    status: pending
    purpose: Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, and the text of a Decision page reaches case-guppi only for a reason its frame names, the main agent for none and ask-guppi by no call
    method: 'by hand, after a session that runs on the rendered .claude/rules/search-leaves-out-decisions.md and .claude/agents/ask-guppi.md: the transcripts of the main agent and of each ask-guppi and case-guppi of that session, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line (the render of case 925)'
  change: the Criterion replaced whole — ask-guppi reads no Decision page, case-guppi keeps the reasons of its frame (case 925.3)
```

```tasks
- [x] update `estimate-search-leaves-out-decisions-in-every-agent`
- [x] read `estimate-search-leaves-out-decisions-in-every-agent`
```

### Case 925.4 — ask-guppi names a Decision by its slug and opens none

> **given:**
> `rule-ask`: the rule of `ask-guppi`; one passage of its Render changes.
> **＋** `.claude/agents/ask-guppi.md`: the file rendered from `rule-ask`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill that dispatches `ask-guppi` at `/pre-spec`.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `estimate-ask-opens-a-decision-only-for-a-finding`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-search-leaves-out-decisions`: a Decision page is read only for a reason the frame of the agent names.
> **＋** `estimate-ask-finds`: the check of what a finding gives.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check of Decision reads in every agent.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> `ask-guppi` runs no Read of a page under `vault/wiki/decisions/` and no Grep whose `path` is that folder or lies in it.
> **＋** A page that carries `deferred_by` has its Decision left unread, whether a finding names the page or not, and also when a Case of the plan changes that page.
> **－** What a finding on a page with `deferred_by` gives is outside this promise: `estimate-ask-finds` reads it.
> **－** Whether the hook refuses such a call is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.
> **－** Decision reads by the main agent and by `case-guppi` are outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads them.

```then
update:
- slug: rule-ask
  replace:
  - old: 'Do not open or grep `vault/wiki/decisions/` except for two reasons: a page in your answer carries `deferred_by` — open the decision it names and give its `## Problem` on the `exists` or `near` line, or, at `/pre-spec`, in the finding that names the page, since a deferred decision is something already decided; at `/pre-spec` you open it only after a finding of yours names the page, never to judge whether a finding stands, and a page that carries `deferred_by` and stands in no finding has its Decision left closed (case 800.2); or the question asks why something was decided — reach the Decision through the page''s `origin`.'
    new: 'Run as the agent `ask-guppi`, you open and grep no page under `vault/wiki/decisions/`, and a hook refuses such a Read or Grep (as set in cases 925.1 and 925.4). A page in your answer that carries `deferred_by` you name with the slug of the Decision that field names, on the `exists` or `near` line, or, at `/pre-spec`, in the finding that names the page, since a deferred decision is something already decided, and you quote none of its text; a question why something was decided you answer with the slug of the Decision that the page''s `origin` points to. A caller that runs this recipe itself, `case-guppi`, opens or greps `vault/wiki/decisions/` only for two reasons: a page in its answer carries `deferred_by` — it opens the decision that field names and gives its `## Problem` on the `exists` or `near` line — or the question asks why something was decided — it reaches the Decision through the page''s `origin`.'
  change: ask-guppi opens no Decision page and names the Decision of a page with deferred_by by its slug; case-guppi, running the recipe itself, keeps the two reasons (case 925.4)
- slug: estimate-ask-opens-a-decision-only-for-a-finding
  set:
    status: pending
    purpose: Whether ask-guppi at /pre-spec reads no Decision page, the Decision of a page with deferred_by left unread whether a finding names the page or not
    method: 'by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript read against the Criterion, recorded in the estimate line (the render of case 925.4)'
  change: the Criterion replaced whole — ask-guppi reads no Decision page at /pre-spec (case 925.4)
```

```tasks
- [x] update `rule-ask`
- [x] update `estimate-ask-opens-a-decision-only-for-a-finding`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/ask-guppi.md`
- [x] read `estimate-ask-opens-a-decision-only-for-a-finding`
```

### Case 925.5 — A finding on a put-off page names its Decision by slug

> **given:**
> `estimate-ask-finds`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.claude/agents/ask-guppi.md`: the frame rendered from `rule-ask`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill whose questions the agent answers.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the search rule the list of what was not checked names.
> **＋** `vault/raw/<date>/event_log.md`: the log of the dispatch.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
> **＋** Then stands one numbered list of findings under each question that `.claude/skills/pre-spec/SKILL.md` sets, in the order of that file.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` names the Decision that field names by its slug and quotes none of its text.
> **＋** After the findings stands one list of what the questions ask that the agent did not check. The list says "none" when the agent checked all of it and its searches broke no rule of `.claude/agents/ask-guppi.md` or of `.claude/rules/search-leaves-out-decisions.md`. Its last lines name each rule of those files that a search broke, one line each, and say whether a finding rests on what that search printed. Then stands a list of the paths of the files the agent read.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** `.claude/agents/ask-guppi.md` does not list the questions of `/pre-spec` itself.
> **－** Nothing but its numbered findings, or "none" alone, stands under a question. No sentence says what the agent checked and found sound, and this includes a clash with another Case that it did not find.
> **－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
> **－** An answer with no list of paths holds the promise as well.

```then
update:
- slug: estimate-ask-finds
  set:
    status: pending
    method: 'by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the answer of ask-guppi in its agent transcript read against the Criterion and the event log, recorded in the estimate line (the render of case 925.4)'
  change: the Criterion replaced whole — a finding on a page with deferred_by names its Decision by slug, with none of its text (case 925.5)
```

```tasks
- [x] update `estimate-ask-finds`
- [x] read `estimate-ask-finds`
```

### Case 925.6 — The check of the history cut leaves a refused Read out

> **given:**
> `estimate-page-read-cuts-the-history`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/pageread.py`: the hook that cuts the History, unchanged.
> **＋** `.guppi/guppi/pages.py`: `split_sections`, which finds the heading.
> **＋** `.guppi/tests/test_pageread.py`: the tests of the hook.
> **＋** `.claude/settings.json`: where the hooks on `Read` are registered.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal of a Read.
> **＋** `vault/wiki/`: the folder of the pages whose History the hook cuts.

> **when:**
> An agent — the main agent or a subagent — calls `Read` on a file under `vault/wiki/`.

> **then:**
> When the call carries neither `offset` nor `limit` and the file holds its own `## History` heading, `uv run --project .guppi guppi pageread` on `PreToolUse` sets `limit` to the line before that heading by `updatedInput`, and the agent gets the frontmatter and the body alone.
> **＋** After such a call, `uv run --project .guppi guppi pageread --after` on `PostToolUse` adds one line of `additionalContext`: the History is cut, its first and last line, and a `Read` with `offset` at its first line shows how the page changed.
> **＋** The heading is found by the walk of `split_sections` in `.guppi/guppi/pages.py`, so a `## History` inside a render block of the page does not count.
> **＋** An `Edit` of the page after the cut read works as after a whole read.
> **－** A call with its own `offset` or `limit`, a file with no `## History`, and a file outside `vault/wiki/` are not changed, and no line is added.
> **－** The page on disk is not changed: in Obsidian it shows whole.
> **－** A `Read` that another hook on `PreToolUse` of `Read` refuses does not run, and the agent gets no text of the page: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads that refusal.

```then
update:
- slug: estimate-page-read-cuts-the-history
  set:
    status: pending
    method: uv run --project .guppi pytest .guppi/tests/test_pageread.py, then by hand in Work Mode a Read of a vault page in the main agent and in a subagent, recorded in the estimate line
  change: the Criterion replaced whole — a Read that another hook refuses is outside the promise (case 925.6)
```

```tasks
- [x] update `estimate-page-read-cuts-the-history`
- [x] read `estimate-page-read-cuts-the-history`
```

## Case 926 — case-guppi reads what a function calls and the input it walks over before it states what the function does

> **context:**
> `case-guppi` sometimes states what code of the repository does without reading the code that decides it. Case 869 gave `rule-case-build` a sentence against this: read whole the function that decides the claim, each of its conditions, and name it in `context`; it set `insight-case-build-claims-what-code-does-without-reading-it` to `actioned`. The fault came back in session 2312: the trigger of `lesson-case-build-judged-a-check-by-the-last-stretch-of-the-transcript` says that Case 896.4, as first ratified, said that the check on `SubagentStop` takes a round that wrote only the note for an answer with no file written, and that ask-guppi at `/pre-spec` found that `written_case_files` reads every `Write` and `Edit` of the whole transcript; this Case states nothing of that code beyond what the lesson says. Its root cause says that `case-guppi` described `written_case_files` from its name and docstring without following what its loop over `agent_transcript_path` collects, and that it did not search for an existing judgment of the name of a Case file. That lesson reopened the Insight, which now stands `open` in `## Deferred` of `backlog.md` with no `deferred_by`. The sentence of case 869 does not ask for what the input of a function holds, and that input decided this claim. So the sentence now also asks for each function called on the way to the claim and for the place where the caller takes the input that the function walks over. It also says that the name and the docstring of a function are no reading of it. The governing rule is `rule-case-build` itself, together with the line of `CLAUDE.md` that a claim names a real source. The second half of the root cause stands under the sentence of case 752, which already names the Grep of `.guppi/guppi/` for an existing judgment that Case 896.4 skipped. Its Estimate, `estimate-case-build-finds-an-existing-judgment`, checks that search, and its Criterion stands, since no sharper text would have changed that skip. `estimate-case-build-reads-the-code-it-states` checks the sentence, so its Criterion is replaced whole, and its `purpose` and `method` are set anew, since both state the old promise. The `method` ties its event to the Render this Case sets, a `/pre-spec` of a session whose `case-guppi` runs on `.claude/agents/case-guppi.md` as rendered by case 926, since the `/pre-spec` of this session runs before that render and judges Cases built on the sentence of case 869; it names a kind of moment, not the first such `/pre-spec`, as case 898.2 set the method. A Grep of `.guppi/tests/` for `case-guppi\.md|rule-case-build` printed `.guppi/tests/test_guppi_package.py` alone. Its `test_no_caller_runs_the_code_or_the_tests_without_the_project` reads each file under `.claude/` live, through `callers`, for `uv run guppi` and `uv run pytest`, and its `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` reads each live page, through `live_pages`, for those and for `guppi/` and `tests/`; the new sentence, the new Criterion, `purpose` and `method` and the `change` lines name none of them, so the test stands. A Grep of the repository outside `vault/archive/` for `estimate-case-build-reads-the-code-it-states` printed `vault/raw/2026-10-30/0304/cases/case-926.md`, `vault/raw/2026-10-30/0304/cases/case-924.md`, `vault/raw/2026-10-30/0304/cases/note-926.md`, `vault/raw/2026-10-30/0304/ledger.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/lessons/lesson-brief-lists-transcript-readings-under-work.md`. That lesson records the `/hi` of session 1805 and stands, the ledger holds the decision line of this Case on that Estimate, `log.md` is not read, and `case-924.md` names that Estimate only to say that Case 924 does not change it. Case 924, whose finished file was read after its build ended, also changes the Render of `rule-case-build`: its pair anchors on the sentence on a fact that no slug marks, in the paragraph on the checks before the summary, and adds one sentence after it on the steps that read or repeat a changed step. This Case anchors on the sentence of case 869 in the paragraph on the frame, so the two `old` values do not overlap and neither pair changes the text the other matches; each Case renders `.claude/agents/case-guppi.md` after its own pair, and the render takes both changes. Case 924 says that the code readers already have the sentence of case 869, and this Case keeps that sentence and only widens it, so neither text makes the other false. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> `case-guppi` read the function that decided a claim but not what the input of that function holds, and it took the name and the docstring of the function for its behaviour, so a Case was ratified on a false claim about a check.

> **recommend:**
> - **What the Case changes in the sentence on a claim about code**
>   - Recommended: (a) sharpen the sentence: a name or a docstring is no reading; read each function called on the way, and where the function walks over an input, the place where its caller takes that input; name each in `context`.
>   - Answer: agreed, (a).
> - **The second half of the lesson: the search for an existing judgment**
>   - Recommended: (a) leave the sentence of case 752 as it stands; `context` says why.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-reads-the-code-it-states`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the `/pre-spec` finding that the `method` of `estimate-case-build-reads-the-code-it-states` does not tie its event to the new Render, so the `/pre-spec` of this session, which runs before the render, would meet it.
>   - Taken: the `method` waits for a `/pre-spec` of a session whose `case-guppi` runs on `.claude/agents/case-guppi.md` as rendered by case 926.

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, holds the sentence on a claim about code.
> **＋** `.claude/agents/case-guppi.md`: the rendered agent file of `case-guppi`.
> **＋** `estimate-case-build-reads-the-code-it-states`: the Estimate of that sentence; its Criterion is replaced whole.
> **＋** `insight-case-build-claims-what-code-does-without-reading-it`: set `actioned`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and states in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out.

> **then:**
> Before it states the claim, `case-guppi` reads whole the function that decides it, each of its conditions and not only the line it cites.
> **＋** It reads each function that this function calls on the way to what it states.
> **＋** Where the function walks over an input, such as a transcript or a list of files, it reads the place where the caller of the function takes that input.
> **＋** The `context` of the Case names the file and the function that `case-guppi` read for the claim.
> **＋** The `context` of the Case also names each function called on the way and the place of the input that `case-guppi` read for the claim.
> **＋** A claim about code that `case-guppi` did not read stays out of the Case.
> **－** The name and the docstring of a function do not stand for a reading of it.
> **－** `case-guppi` still reads a module of code in parts: the deciding function is one of those parts.
> **－** Each function it reads on the way to the claim is one of those parts too.

```then
update:
- slug: rule-case-build
  replace:
  - old: Before you state in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out, read whole the function that decides it, each of its conditions and not only the line you cite, and name its file and the function in `context`; that function is one of the parts of its module that you read, and a claim about code you did not read stays out of the Case (case 869).
    new: Before you state in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out, read whole the function that decides it, each of its conditions and not only the line you cite, each function it calls on the way to what you state, and, where it walks over an input such as a transcript or a list of files, the place where its caller takes that input, so that you know what the input holds; the name of a function and its docstring are no reading of it; name in `context` the file and each function you read for the claim; those functions are among the parts of their modules that you read, and a claim about code you did not read stays out of the Case (as set in cases 869 and 926).
  change: case-guppi reads, for a claim about code, each function called on the way and where the caller takes the input, and takes no name or docstring for a reading (case 926)
- slug: estimate-case-build-reads-the-code-it-states
  set:
    status: pending
    purpose: Whether case-guppi, before it states what a function or a script of the repository does, prints or leaves out, reads whole the function that decides it, each function it calls on the way and the place where its caller takes the input it walks over, takes no name or docstring of a function for a reading of it, names in context the file and each function it read, and keeps out a claim about code it did not read
    method: 'by hand, after a /pre-spec of a session whose Cases case-guppi built with .claude/agents/case-guppi.md rendered from a Render of rule-case-build that asks, for a claim about code, for each function called on the way and the place where the caller takes the input: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the functions it read — the deciding function, each function it calls on the way and the place where its caller takes the input — the count in the estimate line'
  change: the Criterion replaced whole — the functions called on the way and the source of the input are read too, and a name or a docstring is no reading
- slug: insight-case-build-claims-what-code-does-without-reading-it
  set:
    status: actioned
    addressed_by: decision-case-926
  change: 'actioned again: case-guppi reads each function called on the way and where the caller takes the input, and takes no name or docstring for a reading (case 926)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-case-build-reads-the-code-it-states`
- [x] update `insight-case-build-claims-what-code-does-without-reading-it`
- [x] read `estimate-case-build-reads-the-code-it-states`
```
