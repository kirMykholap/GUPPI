# Brief — 2026-10-04, session 1934: the close of a sprint and the check of a Case against the session, built from the conserved Spec of 1439

## Where things stand

- Session 1934 ran the conserved Spec `vault/raw/2026-10-04/1439/spec.md`: Cases 627 (627.1–627.5), 628 (628.1–628.12) and 629 (629.1–629.5), ratified in session 1439; 630 and 631 are its short-form defers.
- Code: `guppi/sprint_close.py` (new: the command `sprint-close`, its preview, `--carry`, `--archive-unread`, the refusal, the marks, `guppi cleanup`, the tick of its line), `guppi/cli.py`, `guppi/ledger.py`, `guppi/materialize.py`, `guppi/render.py`, `guppi/backlog.py`, `guppi/casecheck.py`; docstrings of `guppi/sprint.py`, `guppi/generate.py`, `guppi/prespec.py`.
- Tests: `tests/test_sprint_close.py` (new), `tests/test_ledger.py`, `tests/test_materialize.py`, `tests/test_sprint.py`, `tests/test_generate.py`, `tests/test_backlog.py`, `tests/test_casecheck.py`.
- Readings of the session: `estimate-ask-finds` failed; `estimate-orchestration-signs-a-batch-together`, `estimate-ratification-ledger-line-form`, `estimate-hi-takes-a-conserved-spec` passed. One lesson: `lesson-prespec-one-ask-guppi-run-samples-the-spec`.
- This librarian run, two yamls applied (`guppi generate`: 76 pages written or changed for 1439, 8 for 1934; 0 for 0004 and 0112, applied earlier):
  - decisions: 27 created (627, 627.1–627.5, 628, 628.1–628.12, 629, 629.1–629.5, 630, 631); 3 superseded and archived (`decision-case-566`, `decision-case-570`, `decision-case-615`).
  - rules: 19 updated by 22 entries; `rule-case-rebuild-cost` deleted and archived; by the cascade 7 to `draft` (`rule-backlog`, `rule-brief`, `rule-case-build`, `rule-page-generation`, `rule-sprint`, `rule-synthesis`, `rule-work-mode`) and 2 to `built` (`rule-orchestration`, `rule-ratification`).
  - estimates: 5 created (`estimate-sprint-close-runs-in-the-librarian-run`, `estimate-sprint-close-takes-the-readings-in-groups`, `estimate-sprint-close-next-session-opens-the-sprint`, `estimate-case-check-sends-back-a-clash-with-another-case`, `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`); 17 updated; 2 deferred (`estimate-spec-write-reaches-the-approved-spec` by 630, `estimate-lint-runs-every-step` by 631); 4 readings applied.
  - entities: `entity-sprint-migration` updated twice (627.1, 628.9); its `deferred_by` of case 615 cleared once, by 627.1.
  - lessons: 1 created, then clustered. insights: 1 updated (synthesis).
  - `rule-sprint-close` carries `enforcement: check` and `implementation_ref: [guppi/sprint_close.py, tests/test_sprint_close.py]` (627.1) and a `## How it works` (628.1).
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 76 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
  - `lesson-prespec-one-ask-guppi-run-samples-the-spec` joined `insight-prespec-after-findings-loop-unruled`; the Insight was `actioned` (`addressed_by: decision-case-561.1`) and is `open` again, its `addressed_by` standing.

## Readings due

- `estimate-ask-finds` — failed — `rule-ask` draft — method: by hand at the /hi of a later session, the answer of ask-guppi at a /pre-spec after the render of `.claude/agents/ask-guppi.md` by case 626.1. Result: the dispatch at the /pre-spec of 1439 opened with the Grep the Criterion names and gave three numbered lists, but opened with a heading and a summary paragraph, added notes and a "Not checked" list after the findings, and ran several Greps per category beyond the first.
- `estimate-ask-query-before-a-create` — pending — `rule-ask` draft — `- [ ] read` in `raw/2026-10-04/0112/spec.md` L315.
- `estimate-backlog-renders` — pending — `rule-backlog` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L939.
- `estimate-brief-written` — pending — `rule-brief` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L783.
- `estimate-case-build-checks-the-finished-case` — pending — `rule-case-build` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L1234.
- `estimate-case-build-writes-the-case` — pending — `rule-case-build` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L1112.
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — pending — `rule-case-check` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L1151.
- `estimate-case-check-requires-each-question-of-the-rounds` — pending — `rule-case-check` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L1188.
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — pending — `rule-case-check` draft — method: `uv run pytest tests/test_casecheck.py -k clash`, then by hand an answer of case-guppi the hook sends back for this reason.
- `estimate-case-check-sends-back-a-clash-with-another-case` — pending — `rule-case-check` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L1059.
- `estimate-case-check-sends-back-a-faulty-round` — pending — `rule-case-check` draft — method: `uv run pytest tests/test_casecheck.py -k round_form` over a temp agent transcript, then by hand a round the hook sends back live.
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — pending — `rule-case-check` draft — method: `uv run pytest tests/test_casecheck.py -k shape`, then by hand an answer of case-guppi the hook sends back for this reason.
- `estimate-generate-writes` — pending — `rule-page-generation` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L691.
- `estimate-handoff-holds-each-fact-once` — pending — `rule-handoff` draft — `- [ ] read` in `raw/2026-10-04/0112/spec.md` L87.
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L736.
- `estimate-lint-runs-every-step` — pending — `rule-lint` draft — method: by hand, the `make lint` of the Baseline of a /work of a later session whose backlog step is red. Deferred by `decision-case-631`.
- `estimate-session-start-context` — pending — `rule-session-start` draft — method: `make test-session-start`; by hand, one session opened without /hi whose reply carries a LEDGER block, and the ledger of the next working session after its first ratification.
- `estimate-spec-write-reaches-the-approved-spec` — pending — `rule-spec-write` draft — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, a Case ratified in Work Mode. Deferred by `decision-case-630`.
- `estimate-sprint-close-archives-done-insights-and-lone-lessons` — pending — `rule-sprint-close` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L192.
- `estimate-sprint-close-archives-the-decisions` — pending — `rule-sprint-close` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L135.
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — pending — `rule-sprint-close` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L226.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L555.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L462.
- `estimate-sprint-close-settles-unread-estimates` — pending — `rule-sprint-close` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L266.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L497.
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L893.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L857.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L828.
- `estimate-sprint-ticks-the-spec` — pending — `rule-sprint` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L645. This run: `guppi sprint` wrote `vault/wiki/sprint.md` and exited 0 with no stderr; the line `` - [x] `uv run guppi sprint` `` of `raw/2026-10-04/1439/spec.md` (L134) is ticked in the working tree against HEAD; the specs of 0004, 0112, 1439 and 1934 hold no task line whose first code span holds `guppi sprint-close`.
- `estimate-synthesis-clusters` — pending — `rule-synthesis` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L313. This run: the yamls named by `guppi materialize` held 1 `lesson` entry (`raw/2026-10-04/1934`).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` draft — `- [ ] read` in `raw/2026-10-04/1439/spec.md` L602.

## Flags

- Entries marked `incomplete`, `failed`, `near` or `unparsed`: none in the four yamls `guppi materialize` named (0004, 0112, 1439, 1934). Every entry and every decision carries `applied`.
- Failed Estimate: `estimate-ask-finds` (reading of 1934 L1).
- Index check: no `create` other than an Estimate in the yamls; no index Grep was run for it.
- The checks the handoff asked: both `replace` updates of `entity-sprint-migration` (627.1, 628.9) applied, and log.md holds one line "defer by decision-case-615 superseded" for it, under 627.1; `rule-sprint-close` (627.1, 628.1), `rule-orchestration` (628.1, 629.1) and `rule-case-build` (629.2, 629.5) each took both updates; `rule-case-rebuild-cost` deleted, its defers by `decision-case-566` and `decision-case-570` superseded; `guppi/sprint_close.py` stands in `implementation_ref` of `rule-sprint-close`.
- `insight-prespec-after-findings-loop-unruled` reopened by the synthesis: `actioned` → `open`, child `lesson-prespec-one-ask-guppi-run-samples-the-spec` added, `addressed_by: decision-case-561.1` kept.
- Stale defers (make lint): `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239; `rule-subagent-guppi` 31 times since case 29.
- `make lint`: exit 2, 35 finding lines — the 4 stale defers above and 31 `unread` lines (1 failed, 30 pending Estimates). The handoff counted 25 finding lines before the work.
- `guppi cleanup` moved 4 pages to `vault/archive/migration/2026-10-04/1934/`.
- MOC candidates: none found. Contradictions: none found.
- Read beyond the frame: a Grep of `guppi sprint` over the spec.md files of the four units printed two `- [x]` lines of `raw/2026-10-04/1439/spec.md` ticked before this run (L456, L644); needed for the facts of `estimate-sprint-ticks-the-spec` in Readings due. The handoff did not ask for it.

## Next session

Cases:
- The 12 findings of `ask-guppi` at the `/pre-spec` of 1934 on Cases 627–629, each a Case with `{supersedes}` before the close of migration (handoff, For the next session): `## How it works` on the Leaf `rule-sprint-close` against `rule-rules-schema`, and a Purpose that states behaviour; the `## How it works` left on the Leaf `rule-cleanup`; the sprint page's Estimates called its Definition of done by `entity-sprint`, `rule-sprint` and the Purpose of `entity-sprint-migration`, while the close goes ahead without them; `estimate-sprint-migration-lint-clean` read while five Estimates of the Spec still stand `pending`; the `then` of 628.3 against the per-unit `sprint` of `materialize`; a session that opens a sprint cannot take a conserved Spec, and two "first" in one sentence of `rule-skill-hi`; step 5 of `rule-documentation` reads the Backlog of the sprint page only; the selector `-k session_clash` inside `-k clash`; `estimate-insights-schema-checked`, `estimate-hi-takes-a-conserved-spec`, `estimate-orchestration-asks-in-the-grill-me-shape` and `estimate-work-mode-takes-the-work-readings` not named by the Cases that change what they speak of.
- How `/pre-spec` checks a Spec so that one run of `ask-guppi` is not taken for a check of the whole, and how a Case built again on a finding is read against the vault (handoff, For the next session; `lesson-prespec-one-ask-guppi-run-samples-the-spec`, `insight-prespec-after-findings-loop-unruled` open again).
- `estimate-ask-finds` failed at the /hi of 1934.

Work:
- `estimate-ask-query-before-a-create`
- `estimate-backlog-renders`
- `estimate-brief-written`
- `estimate-case-build-checks-the-finished-case`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-check-sends-back-a-clash-with-another-case`
- `estimate-case-check-sends-back-a-faulty-round`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-generate-writes`
- `estimate-handoff-holds-each-fact-once`
- `estimate-hi-writes-frontier`
- `estimate-lint-runs-every-step`
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- `estimate-sprint-close-archives-the-decisions`
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-settles-unread-estimates`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-ticks-the-spec`
- `estimate-synthesis-clusters`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- The unticked boxes of the Specs: 2 `read` lines of `raw/2026-10-04/0112/spec.md` and 22 `read` lines of `raw/2026-10-04/1439/spec.md`, each naming a reading above.

Ask the person:
- none

## Readings at the close

- `make test`: 1166 passed, 6 skipped.
- `make lint`: exit 2, 35 finding lines (4 stale defers, 31 unread Estimates).
- Pages under `vault/wiki/`: decisions 1055, rules 77, estimates 207, lessons 77, insights 30, entities 4.
- Ledgers: `raw/2026-10-04/1439/ledger.md` 49 lines, `raw/2026-10-04/1934/ledger.md` 5 lines; the yamls account for each of the 54 lines.
