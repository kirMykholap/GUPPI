<!-- approved 15:26:56 · session 313225df -->

# Spec — session 1508, 2026-10-10

## Case 753 — The finished close rule leaves the closing milestone

> **context:**
> Slice 5 of `entity-sprint-migration`, the last milestone of the sprint, holds two items: `rule-sprint-close` and the close line of `migration`. `guppi sprint` ticks an item when each page it names stands `built`, `passed` or `archived`. The cascade sets a rule `built` only when each of its live Estimates stands `passed`, and nothing archives `rule-sprint-close` before the close. Six Estimates of `rule-sprint-close` stand `passed`. Three stand `pending`: `estimate-sprint-close-runs-in-the-librarian-run`, `estimate-sprint-close-takes-the-readings-in-groups` and `estimate-sprint-close-next-session-opens-the-sprint`. Each one waits for the closing session or the session after it. So the item cannot be ticked before the close, and each `/hi` takes it again as a Frontier line from the current milestone (`rule-skill-hi`). The person wants it settled in this session, so that the next session closes the sprint by `/sprint-close` with the close line as the only sprint item. This Case removes the item from Slice 5. `rule-sprint-close` stays `draft`. The closing Case settles its three pending Estimates, by a reading, `--carry` or `--archive-unread`, as `rule-skill-sprint-close` sets it. The close line stays the last item of the last milestone, as `rule-skill-sprint-open` writes it. A Grep for `Slice 5` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/sprint.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-morph.md`, `vault/wiki/entities/entity-sprint-migration.md`, `tests/test_sprint.py`, `vault/wiki/estimates/estimate-hi-writes-frontier.md` and `vault/wiki/estimates/estimate-sprint-items-move-only-by-a-case.md`. `brief.md` and `log.md` were not read. `sprint.md` is rendered from the sprint page by the task line below. `backlog.md` and `rule-morph.md` name Slice 5 in the purpose of `rule-morph` as an old place of that item, which this Case does not touch. `tests/test_sprint.py` builds its own sprint page under a temporary folder and reads no live file. The Results of the two Estimates record past readings, and a record stands. The Criterion of `estimate-sprint-items-move-only-by-a-case` says that a line of the sprint page moves only through an entry of a ratified Case, and this Case is such an entry. `estimate-sprint-renders-the-backlog` checks this change: its Criterion says that `guppi sprint` renders the current milestone whole from the page, and that a line with no wikilink keeps its milestone open. That Criterion speaks of the render in general and not of this item, so it stands. No Estimate of `entity-sprint-migration` speaks of the milestones, so none is touched. One of them limits the choice that this Case leaves to the closing Case: `estimate-sprint-migration-lint-clean`. Its Criterion forgives an `unread` line in `make lint` before the closing librarian's run only on an Estimate of the sprint page, or on an Estimate whose `method` names a moment at or after that run and that the close line names by `--carry`. `estimate-sprint-close-runs-in-the-librarian-run` and `estimate-sprint-close-next-session-opens-the-sprint` have such a moment. If the closing Case archives either of them unread, that Criterion is not met. The choice stays with the closing Case, as the person decided, and that Criterion stands as the limit the closing Case reads.

> **problem:**
> The milestone item `rule-sprint-close` cannot be ticked before the sprint closes, because its last three Estimates can only be read at the close or after it. So it comes back at every `/hi`, and the closing session must put it off again.

> **recommend:**
> - **What closing C1 does to the sprint page**
>   - Recommended: (a) take the item out of Slice 5; the rule's content is finished, and the closing Case handles its waiting checks like any other unread check.
>   - Answer: agreed with the recommendation, (a).
> - **Who decides what happens to the three waiting checks**
>   - Recommended: (a) leave it to the closing Case, which sorts the checks into groups and picks carry or archive-unread for each one.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `entity-sprint-migration`: the sprint page whose Slice 5 loses the item.
> **＋** `vault/wiki/sprint.md`: the file `guppi sprint` renders from the sprint page.
> **＋** `rule-sprint-close`: the rule the removed item names.
> **＋** `/hi`: the skill that opens the next session and writes its Frontier.
> **＋** `rule-skill-hi`: takes the items of the current milestone as Frontier lines.
> **＋** `rule-skill-sprint-close`: the closing session settles each pending Estimate.

> **when:**
> The librarian applies the update of `entity-sprint-migration` and runs `uv run guppi sprint`; the next session opens with `/hi` and reads `vault/wiki/sprint.md`.

> **then:**
> Slice 5 of `entity-sprint-migration` and of `vault/wiki/sprint.md` holds the close line of `migration` alone.
> **＋** The `/hi` of the next session takes the close line as the only Frontier line from the sprint, as `rule-skill-hi` sets it.
> **－** `rule-sprint-close` keeps its status, and each of its Estimates keeps its status until the closing session settles it, as `rule-skill-sprint-close` sets it.

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: '- [[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (cases 612.1, 627) - the close of `migration`'
    new: '- the close of `migration`'
  change: 'Slice 5 holds the close line alone: rule-sprint-close left the milestone, its pending Estimates settled by the closing Case (case 753)'
```

```tasks
- [x] update `entity-sprint-migration`
- [x] `uv run guppi sprint`
```

## Case 754 — case-guppi reads the test code over a live text a Case changes

> **context:**
> Some tests in `tests/` read a live page of the vault, or a file under `.claude/`, and run code over it. Today `case-guppi` has one step for them, set by case 736.1: when a Case changes the code of a check, it reads each live file such a test runs through that check. No step covers a Case that changes the text itself, and no step makes the agent read the test's own helper code. Case 751.6 put a horizontal rule before the example of a showing in `orchestration.md`; its context said that `tests/test_orchestration.py` accepts the changed example, judged by the check functions alone. At Retro the test failed: its helper `store_of_showing` read the ledger lines by `fence_ledger_lines` over the whole text, which stops at the first rule, and the Spec held no task for the test (`lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`). The synthesis joined that lesson to `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`, which opened again with severity 1. This Case adds one sentence to the Render of `rule-case-build`, after the sentence of case 736.1, and a new Estimate checks it. The person chose a new promise beside the old one, so the Criterion of `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check` stands: it covers a changed check, and this Case covers a changed text. The sentence of the Render that reads a module of code in parts, checked by `estimate-case-build-reads-by-need-and-in-parts`, stands too: the new step reads named functions of a test file, which is a reading in parts. In the page `rule-case-build`, read whole, no other sentence states how the agent reads a test, so no other sentence becomes false. A Grep of `(ROOT|REPO|parents\[1\]) / "(vault|\.claude)"` over `tests/` printed the live reads of `tests/test_orchestration.py`, `tests/test_generate.py`, `tests/test_materialize.py`, `tests/test_schemas.py` and `tests/test_case_schema.py`: they read `orchestration.md`, `case-schema.md`, `case-example.md` and the `schema.yaml` files, and none of these is a file that this Case changes. The change adds no code under `guppi/`, so no judgment is copied. The new text of `.claude/agents/case-guppi.md` lands at the librarian's render, and only `make lint` reads it, so no old form is kept.

> **problem:**
> When a Case changes a live text that a test reads, nothing makes `case-guppi` read the test's own code over the new text. A claim that the test still passes is then signed on the check functions alone, and the test breaks first at Retro.

> **recommend:**
> - **A new promise or the old one widened**
>   - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-test-code-over-a-changed-text`, beside the old one, which stays as it is.
>   - Answer: agreed, (a).
> - **Which changed texts the step covers**
>   - Recommended: (a) any live file of `vault/` or `.claude/` that the Case changes, by a page `update` or by the render of its rule, when a test reads that file.
>   - Answer: agreed, (a).
> - **How far the reading of the test goes**
>   - Recommended: (a) the whole path the text takes: the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `guppi/` they call.
>   - Answer: agreed, (a).
> - **What enters the Case, and whether the Insight closes**
>   - Recommended: (a) each place where the new text would fail the test enters the Case as a task that changes the test or the text, or `context` says why it stands; the Insight is set `actioned`, with `addressed_by` naming this Case.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule whose Render sets how `case-guppi` reads the frame of a Case.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-the-test-code-over-a-changed-text`: the new check of the step.
> **＋** `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`: the lesson whose cause the step closes.
> **＋** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`: the Insight that lesson reopened; set `actioned`.
> **＋** `rule-insights-schema`: the rule that sets `addressed_by` of an `actioned` Insight to the latest decision.
> **＋** `vault/`: the live pages a Case changes and a test may read.
> **＋** `tests/`: the tests that `case-guppi` searches for a live read of a changed file.
> **＋** `guppi/`: the code that a test calls over the text it reads.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes a live file of `vault/` or `.claude/`, by a page `update` or by the render of its rule.

> **then:**
> It searches `tests/` for the tests that read that file live, not a copy under a temporary folder.
> **＋** For each such test, it reads the new text against the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `guppi/` they call.
> **＋** Each place where the new text would fail the test enters the Case as a task that changes the test or the text, or its `context` says why it stands.
> **－** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` stands `actioned` with `addressed_by: decision-case-754` and leaves the backlog.

```then
create:
- slug: estimate-case-build-reads-the-test-code-over-a-changed-text
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, for a Case that changes a live file of vault/ or .claude/, reads the code of each test that reads that file live — the test functions, the functions of the test file they call, its helpers included, and the functions of guppi/ they call — against the new text, and puts each place where the new text would fail the test into the Case as a task, or says in context why it stands
  method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; and, for each Case of that session that changes a live file of vault/ or .claude/, its context and tasks read for the tests that read that file live, each one named or said to stand
  tags:
  - workflow
  - harness
  - tests
update:
- slug: rule-case-build
  replace:
  - old: each text the new check would refuse enters the Case, or `context` says why it stands (case 736.1).
    new: each text the new check would refuse enters the Case, or `context` says why it stands (case 736.1). When the Case changes a live file of `vault/` or `.claude/`, by a page `update` or by the render of its rule, Grep `tests/` for the tests that read that file live, not a copy under a temporary folder; for each one, read the new text against the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `guppi/` they call; each place where the new text would fail the test enters the Case as a task that changes the test or the text, or `context` says why it stands (case 754).
  change: case-guppi reads the code of a test, its helpers included, over a live text the Case changes (case 754)
- slug: insight-workflow-fact-signed-from-a-check-that-does-not-cover-it
  set:
    status: actioned
    addressed_by: decision-case-754
  change: 'actioned: case-guppi reads the code of a test, its helpers included, over a live text the Case changes (case 754)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] create `estimate-case-build-reads-the-test-code-over-a-changed-text`
- [x] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
- [x] read `estimate-case-build-reads-the-test-code-over-a-changed-text`
```
