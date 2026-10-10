---
type: decision
case: "261"
status: archived
update: ["[[rule-prespec]]", "[[rule-prespec-hook]]", "[[estimate-prespec-reconciles]]", "[[estimate-prespec-checks-the-plan]]", "[[estimate-prespec-hook-gates]]", index, case-schema, glossary]
supersedes: ["[[decision-case-259]]"]
origin: raw/2026-09-20/0740/ledger.md#case-261
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness, hooks, tests]
---

## Context

`rule-prespec` is a Leaf with `enforcement: render`; its Render is the skill `/pre-task`, the check of the ratified set before the Spec is approved. `rule-prespec-hook` is the gate on `PreToolUse ExitPlanMode`, `guppi/pretask.py` and `.claude/settings.json`. Both pages stand `built`, `deferred_by: decision-case-259`; their three Estimates — `estimate-prespec-reconciles`, `estimate-prespec-checks-the-plan`, `estimate-prespec-hook-gates` — all `passed`, and this Case touches all three: the names of the command, the skill, the mark and the tests stand in their Criteria and `method`; by case 204 one Case touches several promises when each item writes `sections: Criterion` itself. The word also lives in the Renders of `rule-skill-hi`, `rule-case-protocol` (→ `CLAUDE.md`), `rule-ask` (→ `ask-guppi.md`), `rule-hook-registry` (→ `settings.json`), in the prose of `rule-ask`, `rule-brief`, `rule-event-log`, `rule-ledger-write`, `rule-retro-commit`, `entity-sprint-migration`, in `index.md`, `case-schema.md`, `glossary.md`, the schemas of entities and estimates, and in the code: `guppi/cli.py`, `guppi/gate.py` (`MARKS`, the mark `pretask`), the docstring of `guppi/pages.py`, `tests/test_pretask.py`, `tests/test_gate.py`, `tests/test_ledger.py`, `Makefile`. The mechanism of 258 — an `update` with `rename` — is built and covered by four tests (434 green at `e69fd95`); its live reading, `estimate-generate-renames`, is the librarian's run on this Case. The slugs `rule-prespec`, `rule-prespec-hook`, `estimate-prespec-*` are free, in `wiki/` and in `archive/`. Decision pages, Lessons, Insights, History, Result, `raw/`, `archive/` and `docs/` are records; they are not rewritten.

## Problem

The name "pre-task" does not say what the skill does: it checks the set before the Spec, it does not ask the vault before a Case. The person keeps "pre-task" for the query before a Case, so one word now names two steps — in `case-schema.md` "pre-task checks the slug" is the query and "pre-task asks for the split" is the check. The mechanical rename moves slugs only; the word in the command, the skill, the mark, the module, the tests and the prose of the live pages has to move separately, and each occurrence needs a judgment on which of the two steps it names.

## History

- 2026-09-20 created · raw/2026-09-20/0740/ledger.md#case-261
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
