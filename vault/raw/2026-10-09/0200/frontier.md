# Frontier — 2026-10-09 / 0200

## Cases

- [-] C1 — `rule-sprint-close`, what the close of a sprint moves to the archive and what it keeps (cases 612.1, 627) · sprint · defer
- [-] C2 — the close of `migration` — `/sprint-close`, a session of its own · sprint · defer
- [x] C3 — Build 743.6 and 743.8 again: `type: rule` on the `create` items of `rule-skill-sprint-open` and `rule-skill-sprint-close`, and marks that retire ledger lines 15 and 19, whose `{ref:rule-session}` is stale · brief · case 746
  - near `insight-ledger-ratified-line-never-withdrawn`
- [x] C4 — `rule-skill-sprint-open` and `rule-skill-sprint-close` stand under `rule-session`, not under `rule-session-start` and `rule-plan-mode` as Case 743 says; `estimate-session-phases-in-order` stands `passed` · brief · case 746
- [x] C5 — `estimate-skill-sprint-open-asks-the-opening-questions` — failed · brief · case 746
- [x] C6 — `estimate-skill-sprint-close-leads-the-closing-session` — failed · brief · case 746
- [x] C7 — `estimate-case-check-sends-back-a-faulty-round` — failed: its method asks for a round the hook sends back live, which did not occur after the change · brief · case 747
- [x] C8 — `lesson-case-build-rule-create-without-type`: no check before the Spec judges the fields `materialize` requires of a `create` item · brief · case 748
- [x] C9 — `lesson-ledger-rebuilt-create-keeps-the-stale-ref`: a rebuilt Case that changes the `ref` of a `create` line leaves the first line, with its stale ref, as an entry of the yaml · brief · case 749
  - near `insight-ledger-ratified-line-never-withdrawn`
- [-] C10 — `rule-morph`: the lint finding `deferred` 2 times since case 239 stands until a Case decides the page · brief · defer case 750
  - near `rule-morph`

Backlog: 5 items

## Work

- [ ] W1 — `estimate-hi-takes-a-conserved-spec` · brief
- [ ] W2 — `estimate-brief-written` · brief
- [ ] W3 — `estimate-sprint-close-runs-in-the-librarian-run` · brief
- [ ] W4 — `estimate-sprint-close-next-session-opens-the-sprint` · brief
- [ ] W5 — `estimate-sprint-close-takes-the-readings-in-groups` · brief
- [ ] W6 — `estimate-sprint-migration-leftovers-gone` · brief
- [ ] W7 — `estimate-sprint-migration-lint-clean` · brief
- [ ] W8 — `estimate-sprint-migration-merges` · brief
- [x] W9 — The 4 unticked code boxes of Case 733 in `vault/archive/migration/2026-10-08/0213/raw/spec.md` (`guppi/lint.py`, `guppi/prespec.py`, `tests/test_prespec.py`, `tests/test_lint.py`); Case 738 keeps them unticked · brief · work

## Ask

- [ ] A1 — `estimate-hi-writes-frontier` — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item? · brief
