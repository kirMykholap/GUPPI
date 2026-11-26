# Handoff — 2026-11-25, sprint plugin: brief items of session 0816

## Notes from memory

- The person took each recommended answer of every round with a short "ok"; no fork was argued.
- Case 1060 was ratified whole, then `/pre-spec` sent it back; its `case-guppi` rebuilt it with three sub-cases. The main agent first asked for the rebuild under the number 1060, the case-file check refused it, and the Case was built as Case 1063 with `{supersedes:case 1060}` on the lines of 1063.1. A number 1062 was used for a moment by `case-guppi` and never held by `guppi caseid`; `cases/case-1062.md` stands empty.
- For Case 1063 the person chose a one-off reading of the texts over a lasting Estimate on `rule-case-protocol`; the reading checks the words agents read, not an agent acting on them.
- The sprint item `rule-clean-branch` (The clean branch) was put off for a later session.

## Direct instructions to the librarian

- Case 1060 is superseded whole by Case 1063.1: its decision lines (L3–L8) must not apply; `decision-case-1060` is written superseded by 1063.
- The Frontier line of the brief item on a passed one-off Estimate closes `· case 1063`; the item is the Backlog line of `entity-sprint-plugin` that Case 1063.1 removes, so `guppi backlog` should count one item fewer.
- Case 1058 sets `source` on `lesson-plugin-install-writes-a-project-settings-file`; the `guppi check` line of the baseline should no longer print after `generate`.
- The two updates of Estimates in 1063.2 and 1063.3 replace their Criterion whole under `sections` and set `status: pending`; `estimate-case-protocol-case-form` is then read `passed` by line L21 of the ledger, after its update.
- The renders of this session: `.claude/skills/work/SKILL.md`, `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/estimates/schema.yaml`, `.claude/skills/merge-main/SKILL.md`.
- The lesson of L22 names the gap between `orchestration.md` and the Splitting section of `case-schema.md`; check it against the lessons and Insights on Cases built again.

## What actually got done

- Cases ratified: 1058, 1059, 1061, 1063 (1063.1, 1063.2, 1063.3). Case 1060 is superseded by 1063.
- Code: `.guppi/pyproject.toml`, the build line `requires = ["uv_build>=0.11,<0.14"]` and its comment. No test changed.
- `uv run --project .guppi guppi test`: 1994 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L20 `estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine` passed (uv 0.13.10, no warning); L21 `estimate-case-protocol-case-form` passed. Lesson: L22 `lesson-orchestration-case-built-again-in-another-shape-under-its-old-number`.

## Debt

- No box is debt.
- Boxes that wait for the librarian: 24.
- `estimate-work-mode-runs-the-style-check-before-a-stop` — waits for the first `/work` after the librarian's render of `.claude/skills/work/SKILL.md` that reaches a task opening with `stop:`.
- `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again` — waits for the librarian's run of session 2003.
- `estimate-skill-merge-main-joins-a-conflicted-page` — waits for the first `/merge-main` that leaves a conflicted page.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — waits for an acknowledging reply after `/pre-spec` that waits for the person's word; in session 2003 the reply after `/pre-spec` acknowledged every Case and waited for nothing, as in session 0816.

## Observations

- The baseline `guppi check` line on `lesson-plugin-install-writes-a-project-settings-file` (missing `source`) was red before the work; Case 1058 settles it at the librarian's run.
- `guppi prespec --check` printed notes that two Criterion lines of the Estimates of 1063.2 and 1063.3 are not carried; each is the line its sub-case qualifies on purpose.
- The `ask-guppi` run at `/pre-spec` had no web tool and did not check the uv docs claims of Case 1059; the reading of L20 bears out the range on uv 0.13.10.

## For the next session

- Whether `orchestration.md` should say that a ratified Case that comes back in another shape is built under a new number with `{supersedes:case N}`, in Plan Mode too, as `case-schema.md` sets it; the lesson of L22 records the cause.
- The sprint item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch` (The clean branch), put off in this session.

## Ask the person

- `estimate-sprint-plugin-readme-describes-the-project` — needs the person — does `README.md` at the root of the branch `plugin` describe GUPPI as it stands, with its Why, Is it for you, how a session goes, its parts, its install and its use?
