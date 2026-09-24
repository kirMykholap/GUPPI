# Brief — 2026-09-24, the librarian's run over sessions 1916 and 2214

## Where things stand

- Session 2214 finished the conserved Spec of 1916 and ratified Case 406. It deferred four questions: 408, 409, 412 and 413. Frontier C1 stays `[-] · sprint`. C2 is closed `· work` and taken up by Case 402.
- Work Mode on the Spec of 1916: the code of Case 402 in `guppi/ratified.py` and `tests/test_ratified.py`. The session's `make test` gave 626 passed, 2 skipped, and `make style` was clean.
- This run applied `raw/2026-09-24/1916/` first, then `raw/2026-09-24/2214/`; `raw/2026-09-24/1303/` had 0 new entries. Case 406 of 2214 replaced the Criterion of `estimate-case-protocol-case-form` after Case 396.1 of 1916 did, so the text of 406 stands.
- Yaml of 1916: 34 entries, all applied. Yaml of 2214: 50 entries. 36 were applied. The 14 on lines 3–14, 17 and 18 were not applied, because Cases 407.1–407.5 and 410 are superseded by 412 and 411 is superseded by 413.
- Pages, from the tree after cleanup:
  - decisions: 42 written (395–413). Cleanup moved 8 to the archive: 394, 407.1–407.5, 410 and 411. 35 new pages remain in the wiki.
  - estimates: 11 created, 15 updated.
  - lessons: 2 created, `lesson-prespec-parent-of-superseded-sub-cases` and `lesson-case-ratification-preview-before-its-targets`.
  - rules: 10 updated.
  - entities: 1 updated, `entity-sprint-migration`.
  - insights: none created or updated.
- Governed files written: `vault/wiki/case-schema.md` by render (Cases 402, 405, 406) and `vault/wiki/sprint.md` by `guppi sprint`. `guppi glossary` wrote nothing new.

## Readings due

No Estimate stands `failed`. 22 stand `pending`:

- `estimate-case-protocol-case-form` — `rule-case-protocol` draft — by hand, the Cases of a session at its close (`raw/2026-09-24/1916/spec.md`, `raw/2026-09-24/2214/spec.md`).
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (`raw/2026-09-24/1916/spec.md`).
- `estimate-case-protocol-checks-its-frame` — `rule-case-protocol` draft — by hand, at the close of the first session with `frame-guppi` (`raw/2026-09-24/1303/spec.md`).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand: the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-frame-check-finds-a-contradiction` — `rule-frame-check` draft — by hand, two live dispatches in the next session (`raw/2026-09-24/1303/spec.md`).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`, then by hand at the first prompt past 400 000 tokens (`raw/2026-09-24/1303/spec.md`).
- `estimate-harness-pipeline` — `rule-harness` draft — `make test-harness`, the first three steps of `make lint`, and the Purpose by hand (`raw/2026-09-24/1303/spec.md`).
- `estimate-hook-registry-rendered` — `rule-hook-registry` draft — `uv run pytest tests/test_render.py` and `uv run guppi render --check` after the render (`raw/2026-09-24/1303/spec.md`).
- `estimate-prespec-reconciles` — `rule-prespec` draft — by hand, the first `/pre-spec` after the render (method).
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand, the section in `CLAUDE.md` and one reply of the agent against it (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — pytest over the skill's render, plus one live reading of a carried-over session (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`, then the live reading by hand (method).
- `estimate-language-followed` — `rule-language` draft — by hand, the section in `CLAUDE.md`, the session's commit, Spec and chat against it (method).
- `estimate-one-judgment-one-implementation-followed` — `rule-one-judgment-one-implementation` draft — `render --check` exit 0, then by hand the diff of the next Work Mode session (method).
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — by hand, the first `/retro` after the render (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-sprint-renders-the-backlog` — `rule-sprint` draft — `pytest tests/test_sprint.py`, plus one reading of the rendered `sprint.md` after the librarian's run (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the first marked lesson is clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Deferred

1. `rule-frame-check` — deferred by Cases 403 and 408: whether `frame-guppi` pays for its tokens and time, measured by the contradictions it finds. It was judged with the data of sessions 1916 and 2214. Severity: none. Briefs: 2.
2. `rule-context-size` — deferred by Cases 404 and 409: which limit is right and what the `UserPromptSubmit` hook says past it. This is decided once a session reaches the limit. Severity: none. Briefs: 2.
3. `rule-prespec` — deferred by Cases 412 and 413. Under 412: how the Spec is written by hooks alone, with each Case checked at once; the pre-spec findings on Case 407 are answered first. Under 413: which of `estimate-case-protocol-case-form` and `estimate-prespec-checks-the-frame` keeps the line "`when` and `then` name only what `given` names". Severity: none. Briefs: 1.
4. `rule-spec-write` — deferred by Case 412, the same question. Severity: none. Briefs: 1.
5. `rule-spec-reconcile` — deferred by Case 412, the same question. It includes the question of Case 410: when the prose of a Case is translated. Severity: none. Briefs: 1.

The previous brief's item `rule-spec-write` under Case 394 was retired by `{supersedes:case 394}` of Case 402. The open Insight `insight-workflow-code-live-before-the-page-it-reads` is named by the sprint page, so it is not listed here.

## Flags

- `incomplete: [criterion]` on five entries of `raw/2026-09-24/2214/materialize.yaml`: `estimate-prespec-checks-one-case`, `estimate-spec-write-checks-the-written-case`, `estimate-spec-reconcile-shows-a-changed-case`, `estimate-spec-reconcile-writes-a-fragment` and `estimate-prespec-checks-the-ratified-copy`. All five belong to Cases 407.1–407.5, which 412 supersedes, so none was applied.
- `failed`, `near`, `unparsed`: none in the yamls of 1916 and 2214.
- Failed Estimates: none.
- MOC candidates: none.
- Stale defers, from lint: `rule-subagent-guppi` and `rule-work-mode` have been deferred 31 times since case 29. `rule-morph` has been deferred once since case 239.
- Contradictions, both under defer:
  - `ask-guppi` at pre-spec found contradictions in Case 407. They are listed in the `context` of 412.
  - One promise is signed twice: `estimate-case-protocol-case-form` against `estimate-prespec-checks-the-frame`. This is Case 413.
- Lesson `lesson-prespec-parent-of-superseded-sub-cases`: `prespec --check` reports a parent Case whose every sub-case is superseded (`case 407: in the ratified copy, not in the plan`).
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `generate`, `cleanup`, `render`, `sprint`, `glossary`: no stderr lines.
- `make lint`, after the render: exit 2, 91 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages: 1–14, 15.1, 15.3, 16.1, 16.2, 17, 18.1, 18.2, 18.3, 19, 20, 21, 24.1, 25, 26.1, 26.2, 27, 28. That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 31 times since case 29`.
  - `unread: pending` on the 22 Estimates of Readings due.
  - `estimates: unmigrated: 20 pages in the shape before case 193`.

## Next session

Cases:
- The findings of Case 412 on Case 407 are answered first (handoff).
- The person proposes `frame-guppi` on Opus with `effort: medium`. Model and input are confounded in session 2214. This is input to defer 408 (handoff).
- The person proposes that `frame-guppi` write the Case itself and that a `SubagentStop` hook check its form. Still open: whether the showing in the chat may come from the subagent's answer. This is input to defers 408 and 412 (handoff).
- A path-scoped rule for text written into the vault outside a Case, such as the brief of `/carry` or the librarian's reports, was named as a possible Backlog item and not recorded. This asks for a change of the sprint (handoff).
- Defect: `prespec --check` reports a parent Case whose sub-cases are all superseded (`lesson-prespec-parent-of-superseded-sub-cases`, `raw/2026-09-24/2214/ledger.md#L26`).

Work:
- `estimate-case-protocol-case-form`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-case-protocol-checks-its-frame`
- `estimate-case-protocol-ledger-line-form`
- `estimate-frame-check-finds-a-contradiction`
- `estimate-context-size-warns-past-the-limit`
- `estimate-harness-pipeline`
- `estimate-hook-registry-rendered`
- `estimate-prespec-reconciles`
- `estimate-agent-writing-followed`
- `estimate-carry-over-writes`
- `estimate-documentation-completes`
- `estimate-language-followed`
- `estimate-one-judgment-one-implementation-followed`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-session-phases-in-order`
- `estimate-sprint-renders-the-backlog`
- `estimate-synthesis-keeps-actioned-by-the-mark`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- Ledger lines not applied: `raw/2026-09-24/2214/ledger.md` lines 3–14, 17 and 18, which are superseded by 412 and 413.

## Readings at the close

- `make test`: 626 passed, 2 skipped.
- `make lint`: exit 2, 91 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 575, estimates 128, rules 63, lessons 50, insights 21, entities 4.
