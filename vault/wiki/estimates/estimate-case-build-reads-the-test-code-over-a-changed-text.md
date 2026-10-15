---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, for a Case that changes a live file of vault/ or .claude/, reads the code of each test that reads that file live — the test functions, the functions of the test file they call, its helpers included, and the functions of .guppi/guppi/ they call — against the new text, and puts each place where the new text would fail the test into the Case as a task, or says in context why it stands
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; and, for each Case of that session that changes a live file of vault/ or .claude/, its context and tasks read for the tests that read that file live, each one named or said to stand
origin: raw/2026-10-10/1508/ledger.md#case-754
sprint: migration
created: 2026-10-10
tags: [workflow, harness, tests]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes a live file of `vault/` or `.claude/`, by a page `update` or by the render of its rule.

Then:
It searches `.guppi/tests/` for the tests that read that file live, not a copy under a temporary folder.
**＋** For each such test, it reads the new text against the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `.guppi/guppi/` they call.
**＋** Each place where the new text would fail the test enters the Case as a task that changes the test or the text, or its `context` says why it stands.
**－** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` stands `actioned` with `addressed_by: decision-case-754` and leaves the backlog.

## Result

2026-10-10, Retro, the new Render of rule-case-build in vault/raw/2026-10-10/1508/spec.md (Case 754, replace after "(case 736.1).") read against the when and then of Case 754: the sentence covers a Case that changes a live file of vault/ or .claude/ by a page update or by the render of its rule, has tests/ grepped for the tests that read it live and not a copy under a temporary folder, reads the new text against the test functions, each function of the test file they call, helpers included, and the guppi/ functions they call, and puts each failing place into the Case as a task or into context; the update of insight-workflow-fact-signed-from-a-check-that-does-not-cover-it sets actioned with addressed_by decision-case-754. The Cases of the session: 753 changes entity-sprint-migration and sprint.md, and a Grep of tests/ for sprint.md and entity-sprint-migration printed reads under tmp_path or project_dir only (test_sprint, test_backlog, test_ledger, test_archive, test_cleanup, test_generate, test_materialize, test_prespec, test_recall), none live; its context names tests/test_sprint.py as reading no live file. 754 changes rule-case-build, .claude/agents/case-guppi.md and the Insight page; its context names the live reads of tests/ (orchestration.md, case-schema.md, case-example.md, schema.yaml), none of them a file it changes, and a Grep of tests/ for those slugs and case-guppi.md printed none.

## History

- 2026-10-10 created · [[decision-case-754]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1508/ledger.md#L5
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
