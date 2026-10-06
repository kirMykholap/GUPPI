# Brief — 2026-10-06, after the librarian run of session 0104

## Where things stand

- Session 0104 ratified Cases 685 (685.1, 685.2), 686 (686.1, 686.2), 687, 688 (688.1–688.9), 689 (689.1, 689.2) and 690 (690.1–690.3); each was built again at `/pre-spec` and ratified again, and 688.9 was added there.
- Code: `guppi/materialize.py` (`unlinked_lessons`); `guppi/ledger.py` (the reminder after the write, the hold of a decision line off the store); `guppi/onward.py` (`TO_LOOP`, `built_after`, `plan_onward` reads the `prespec` line by `prespec_mark`); `guppi/prespec.py` (`prespec_mark`); `guppi/casecheck.py` (the `Stop` run judges every reply whatever `stop_hook_active` says, a limit of three refusals). Tests: `tests/test_ledger.py`, `tests/test_onward.py`, `tests/test_casecheck.py`. Handoff: `make test` 1316 passed, 6 skipped; `make style` clean.
- Readings: L33–L46 and L49, all 15 `passed`. Lessons: L47, L48.
- The yaml: 43 entries from the 49 ledger lines (L33 folded into the create of L2, L34 into L19, L35 into L6, L37 into L12, L45 into L28, L46 into L30) and 4 added by the synthesis; all 47 carry `applied`, and all 24 decision records; 0 `failed`, 0 `exists`, 0 `incomplete`, 0 `near`, 0 `merged`; `unparsed: []`.
- Pages created: decisions 24 (685, 685.1, 685.2, 686, 686.1, 686.2, 687, 688, 688.1–688.9, 689, 689.1, 689.2, 690, 690.1–690.3); estimates 6 (`estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`, `estimate-prespec-onward-tells-the-loop-from-its-end`, `estimate-case-check-judges-a-showing-after-a-refusal`, `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`, `estimate-case-build-reads-a-prompt-fact-at-its-source`, `estimate-orchestration-says-when-a-rendered-change-lands`, each read `passed` by a folded line); lessons 2 (`lesson-orchestration-batch-rounds-headed-by-own-text`, `lesson-case-build-related-cases-same-sentence-missed`, both `clustered` by the synthesis).
- Pages updated: rules 8 by 13 entries (`rule-orchestration` by 685.1, 686.1, 688.7, 689.1 and 690.2; `rule-ledger-write` by 685.1 and 688.7; `rule-prespec-onward`, `rule-prespec`, `rule-case-check`, `rule-internal-context`, `rule-where-to-stop`, `rule-case-build`); estimates 9 by decisions (Criterion replaced, set `pending`), then each read `passed` (L36, L38–L44, L49); insights 6 (`insight-prespec-after-findings-loop-unruled`, `insight-case-show-built-case-retyped-by-hand`, `insight-session-vault-knowledge-not-loaded`, `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` set `actioned` by 687, 688.8, 689.2 and 690.3; two reopened by the synthesis, below); lessons 2 by the synthesis; decisions 1 (`decision-case-648`, superseded by 686.1).
- The handoff's Direct instructions, checked on the pages: the pair of 685.1 on `rule-orchestration` applied before the pairs of 688.7 (entry L3 before L20); both landed, and the sentence names the reply that answers a held decision line once, under case 688.7. `rule-ledger-write` took the pairs of 685.1 and 688.7 on two sentences, and its `implementation_ref` holds `guppi/casecheck.py`. `rule-prespec-onward` lost `deferred_by: decision-case-648` (History: "defer by decision-case-648 superseded"). `rule-case-check` took its new `purpose` and both pairs of 688.1. No instruction was refused.
- `cleanup: 9 page(s) moved`, to `vault/archive/migration/2026-10-06/0104/`: decisions 1 (`decision-case-648`), lessons 8 (`lesson-carry-short-brief-drops-the-work-list`, `lesson-orchestration-a-ratified-render-change-claimed-live-before-the-render`, `lesson-orchestration-case-heading-named-from-the-frontier-item`, `lesson-orchestration-dispatch-prompt-carried-counts-not-from-a-run`, `lesson-orchestration-heading-of-a-showing-composed-by-the-main-agent`, `lesson-prespec-confirmation-prompt-invites-a-new-finding`, `lesson-prespec-one-ask-guppi-run-samples-the-spec`, `lesson-work-mode-a-staged-moment-promised-inside-a-run-with-no-stop`).
- The scripts ticked 55 boxes of the 0104 Spec; no box of it stays open. The render wrote `vault/wiki/orchestration.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/hi/SKILL.md` and `.claude/agents/case-guppi.md`. `guppi sprint` left `sprint.md` unchanged; `guppi glossary` left `glossary.md` unchanged; `guppi backlog` rewrote `backlog.md`: 10 items before, 7 after. No script printed a line on stderr. The run added 103 lines to `log.md`.
- `guppi materialize` named the 2249 yaml too ("extended with 0 entries"); `generate` wrote 0 pages from it.
- `guppi archive` exit 0, no stderr; it moved one unit, `raw/2026-10-05/2249` → `archive/migration/2026-10-05/2249/raw`, and kept `raw/2026-10-06/0104`, the session of the run.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 79 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 32 lines.
- `lesson-orchestration-batch-rounds-headed-by-own-text` — joined `insight-orchestration-items-taken-together-unruled`: rule-orchestration gives no full form for the rounds of several Cases in one reply, and the agent improvised one. The Insight was `actioned` (`addressed_by: decision-case-684.1`); this run set it `open`, `addressed_by` kept.
- `lesson-case-build-related-cases-same-sentence-missed` — joined `insight-workflow-edit-pair-signed-from-a-grep-fragment`: a replace pair judged against the page as it stands, not against what another Case of the same Spec leaves of the sentence. The Insight was `actioned` (`addressed_by: decision-case-351`); this run set it `open`, `addressed_by` kept.
- Both reopened Insights now stand in `backlog.md`, severity 1.

## Readings due

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `7 items`, `## Conserved Specs` empty, 7 lines under `## Deferred`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 0104 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 9 pages from `cleanup` under `migration/2026-10-06/0104/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 12 finding lines — 1 `deferred`, 11 `unread`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1316 passed, 6 skipped, on the working tree of this run.

No Estimate stands `failed`.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed`. Failed Estimates: none.
- Handoff, Observations: `make lint` was red before the work, exit 2 — `backlog.md` differed from its sources, `rule-morph` deferred, 11 `unread: pending` lines.
- Handoff, Observations: one reading line of Retro was written as `- estimate-` with no `[`, so it was no ledger line and was lost with no message; it was written again as L49. No hook tells a near-miss prefix from prose.
- Handoff, Observations: the hold of case 682.1 named all nineteen Cases of the session in its question, once for each of the two Retro lessons.
- Handoff, Observations: `make lint` was not run in Retro; nothing of the 0104 Spec is marked under `## Expected red`.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: none found. Contradictions: none found.
- The lint: 12 finding lines — 1 `deferred` (`rules/rule-morph`), 11 `unread: pending` (the 11 Estimates of Readings due); `make lint` exit 2.
- Reads beyond the frame: none.

## Next session

Cases:
- The person left `rule-work-mode`, `rule-spec-box`, `entity-guppi` and `rule-morph` in the backlog; the Plan Mode and pre-spec group (685–688) and the knowledge group (689, 690) are done (handoff, For the next session).
- `rule-sprint-close` and the close of migration stay for the session that closes the sprint (handoff, For the next session).
- Whether a line inside a `LEDGER` block that opens with `- decision`, `- estimate` or `- lesson` but not with the bracket should be refused aloud rather than dropped (handoff, For the next session).
- The question of the 682.1 hold names every Case of the session; whether it should name fewer (handoff, For the next session).

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

- `make test`: 1316 passed, 6 skipped.
- `make lint`: 12 finding lines — 1 `deferred`, 11 `unread`; exit 2.
- Pages under `vault/wiki/`: rules 75, estimates 231, insights 32, lessons 73, decisions 1199, entities 4.
