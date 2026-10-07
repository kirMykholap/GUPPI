# Brief — 2026-10-07, after the librarian run of session 1804

## Where things stand

- Session 1804 ratified Cases 712, 713, 714, 715, 716 (716.1, 716.2), 717 (717.1, 717.2, 717.3) and the short defers 718, 720, 721. Case 719 was dropped with no decision line (handoff, What actually got done).
- Code: `guppi/lint.py` (`holds`, `unmet_conditions`; `check_schema` reports through it; `matches` removed); `guppi/prespec.py` (`check_conditions`, `created_page`, `kept_method_waits`; `judge` runs `check_conditions` after `check_keys`). Tests: `tests/test_prespec.py`, `tests/test_lint.py`, `tests/test_case_schema.py`. Handoff: `make test` 1415 passed, 6 skipped; `make style` clean.
- Readings of the session: L19–L26, eight Estimates `passed`. Lessons: L27–L30.
- The ledger: 30 lines. The yaml: 33 entries (8 `create`, 13 `update`, 1 `delete`, 4 `defer`, 3 `estimate`, 4 `lesson`), 8 of them added by the synthesis; 5 lines folded into creates (L19, L20, L21, L24, L25); every ledger line is accounted for. 33 entries and 14 decision records carry `applied`; 0 `failed`, 4 `exists` (the 4 defers), 1 `incomplete`, 1 `near`, 0 `merged`; `unparsed: []`.
- Pages created: decisions 14 (712, 713, 714, 715, 716, 716.1, 716.2, 717, 717.1, 717.2, 717.3, 718, 720, 721); estimates 5 (`estimate-orchestration-takes-back-a-ratified-case`, `estimate-prespec-hook-reports-a-schema-condition-not-met`, `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`, `estimate-case-example-passes-the-check`, `estimate-case-build-reads-by-need-and-in-parts`, each `passed` by its folded line); rules 1 (`rule-case-example`, child of `rule-plan-mode`, `built` by the cascade); lessons 4 (`lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped`, `lesson-case-build-splits-a-ratified-leaf-case`, `lesson-orchestration-prompt-named-unrelated-cases`, `lesson-permissions-auto-mode-refuses-editing-the-case-check-store`); insights 2 by the synthesis.
- Pages updated: rules 8 (`rule-insights-schema` by 712; `rule-orchestration` by 713 and deferred by 721; `rule-prespec-hook` two Estimates added by 714, 715; `rule-case-protocol` by 717.1 and deferred by 721; `rule-case-build` by 717.2, `draft` → `built` by the cascade; `rule-plan-mode` child added by 717.1; `rule-case-check` deferred by 720; `rule-sprint-close` deferred by 718, stays `draft`); estimates 3 (`estimate-case-build-writes-the-case` and `estimate-case-build-checks-the-finished-case` method set, pending, then `passed` by L22, L23; `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read` Criterion written back, then `passed` by L26); insights 1 and lessons 2 by the synthesis. `estimate-case-protocol-example-passes-the-check` deleted by 717.1.
- The handoff's Direct instructions: 713's four pairs on `rule-orchestration` applied; `rule-orchestration` and `rule-case-protocol` carry `deferred_by: ["[[decision-case-721]]"]` after their updates. After the render `vault/wiki/case-example.md` holds 1 block tagged `case` and 1 tagged `then`; `vault/wiki/case-schema.md` holds 0 blocks tagged `case`; `uv run pytest tests/test_case_schema.py` 2 passed. The frontmatter of `.claude/agents/case-guppi.md` holds `experimental:` with `cacheTtl: "1h"` after `skills: [grill-me]`. `rule-case-protocol`'s `estimates` no longer lists `estimate-case-protocol-example-passes-the-check`.
- The render wrote `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md`, `vault/wiki/orchestration.md`, `vault/wiki/insights/schema.yaml` and the new `vault/wiki/case-example.md`. The scripts ticked 27 boxes of the 1804 Spec (22 by `generate`, 5 by `render`); no task box stays open. No unticked line of the 1804 Spec holds `guppi sprint-close`; none ran. `guppi materialize` named the 0211, 0425 and 0636 yamls ("extended with 0 entries"); `generate` wrote 0 pages from them.
- `cleanup: 1 page(s) moved`: `estimate-case-protocol-example-passes-the-check` to `vault/archive/migration/2026-10-07/1804/estimates/`.
- `guppi sprint` rewrote `sprint.md` (the `rule-sprint-close` line gains `· decision-case-718`); `guppi backlog` rewrote `backlog.md` (5 items before, 12 after); `guppi glossary` left `glossary.md` unchanged. The run added 61 lines to `log.md`. `generate`, `cleanup`, `render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- `guppi archive` exit 0, no stdout, no stderr; it moved no unit. `raw/2026-10-07/0211`, `0425`, `0636` and `1804` stay: the script looks only at units dated before the day of the run, and 1804 is the session of the run.
- Index check: the one `create` that is not an Estimate is `rule-case-example`. `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 77 lines. `rule-case-protocol` (a Case built in a form the scripts cannot read) is close but not the same (the example of the form, read apart): marked `near: rule-case-protocol`. The index line settled it; no page was opened.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 72 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 34 lines.
- `lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped` joined `lesson-prespec-parent-of-superseded-sub-cases` in the new `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` (open, severity 2).
- `lesson-case-build-splits-a-ratified-leaf-case` joined `insight-ledger-ratified-line-never-withdrawn`. The Insight was `actioned` by `decision-case-671.1`; the update set it `open`, and `addressed_by` stands.
- `lesson-orchestration-prompt-named-unrelated-cases`: none; no index line of either Grep names a prompt of the main agent naming Cases beyond the related ones.
- `lesson-permissions-auto-mode-refuses-editing-the-case-check-store` joined `lesson-permissions-auto-mode-refuses-a-remote-change-despite-the-chat` in the new `insight-permissions-classifier-weighs-the-rules-not-the-persons-word` (open, severity 2).

## Readings due

Failed: none.

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `12 items`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 1804 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 1 page from `cleanup` under `migration/2026-10-07/1804/`; `guppi archive`: no stdout.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 12 finding lines — 1 `deferred`, 11 `unread`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1415 passed, 6 skipped, on the working tree of this run.

## Flags

- `incomplete`: the create of `rule-case-example` (L8, case 717.1) lacked `type` in its Spec block; the page was written and holds `type: rule`.
- `near`: the create of `rule-case-example` is marked `near: rule-case-protocol`.
- No entry marked `failed` or `unparsed`. No failed Estimate.
- Synthesis: `insight-ledger-ratified-line-never-withdrawn` went from `actioned` (by `decision-case-671.1`) to `open` with its new child `lesson-case-build-splits-a-ratified-leaf-case`.
- Handoff, Notes from memory: in Case 717 the agent first claimed that every answer rewrites the subagent's cache, and corrected itself from the transcripts before the Case was built.
- Handoff, Notes from memory: Case 717, Q4, the one-hour cache for `case-guppi` was taken on the recommendation, while the agent's own numbers showed about 60% more cost on a dispatch with no long pause.
- Handoff, Notes from memory: Case 719 was dropped; Case 713 goes into the vault as first ratified, with the faults F2–F6 that pre-spec found, put off by Case 721.
- Handoff, Notes from memory: the close of `migration` was put off again; this session did not prepare it.
- Handoff, Observations: `make lint` was red before the work, exit 2, 14 finding lines (1 `deferred`, 13 `unread`); it was not run in Retro.
- Handoff, Observations: the store `C:\Users\kir\.claude\plans\adaptive-gathering-dewdrop.checked.json` still holds 713.1 and 713.2; the auto mode classifier refused their removal (L30).
- Contradiction, handoff Observations: the Render of `rule-orchestration` as Case 713 leaves it names only the closer `[-] … · defer case N` in its short-form paragraph, holds one sentence that says both that the `defer` lines add to the source and that the source stays as it is, and `estimate-orchestration-defers-in-one-reply` still says a sprint or backlog item takes no short Case.
- Handoff, Observations: `ask-guppi` at `/pre-spec` reached 170k–201k tokens of context.
- Handoff, Observations: `cacheTtl: "1h"` rests on the Claude Code docs as read; it was not tried live, and every dispatch of the session ran with the five-minute cache.
- Handoff, Observations: `created_page` of `guppi/prespec.py` repeats the derivation of `Vault.create` of `guppi/generate.py`; one test runs both over the same items.
- Handoff, Observations: `tests/test_case_schema.py` keeps the path that reads `case-schema.md`; its Criterion says a Case of a later session removes it. `case-example.md` now stands.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: the lint names none.
- The lint: 12 finding lines — 1 `deferred` (`rules/rule-morph`), 11 `unread` (all `pending`: the 11 Estimates of Readings due); `make lint` exit 2.
- Reads beyond the frame: none.

## Next session

Cases:
- The stale entries 713.1 and 713.2 of the store of the Case-file check: the person removes them by hand or adds a permission rule, and a Case decides how the store drops a sub-case that a Case built again no longer holds (handoff, For the next session; Case 720).
- The pre-spec fixes F2–F6 of Case 713, as a new Case that supersedes 713 (handoff, For the next session; Case 721).
- `rule-case-build` sets no step for a fix that adds a second behaviour to a ratified Case with no sub-cases (handoff, For the next session; L28).
- The close of the sprint `migration`: a session of its own (handoff, For the next session; Case 718).
- `/pre-spec` gave no finding on Cases 713 and 717.1 updating `rule-orchestration` and `rule-case-protocol`, which Case 721 of the same plan defers, though `rule-prespec` says such a pair is a finding (handoff, Observations).

Work:
- `estimate-hi-writes-frontier`
- `estimate-hi-takes-a-conserved-spec`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-brief-written`
- `estimate-backlog-renders`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`

Ask the person:
- none

## Readings at the close

- `make test`: 1415 passed, 6 skipped.
- `make lint`: 12 finding lines — 1 `deferred`, 11 `unread`; exit 2.
- Pages under `vault/wiki/`: rules 77, estimates 244, insights 36, lessons 76, decisions 1268, entities 4.
