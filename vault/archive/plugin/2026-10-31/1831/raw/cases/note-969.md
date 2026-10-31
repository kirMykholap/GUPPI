# Note — Case 969 (C9, defer of case 963 on rule-estimates-schema)

## Questions
ROUND 2 ANSWERED: "Ok" = Q3 (a), Q4 (a), Q5 (a), Q6 (a), all as recommended. No fork open. CASE BUILT into case-969.md (969.1 schema+case-schema, 969.2 lint, 969.3 delete two); summary sent. Next: fix findings by Edit only.
Round 1:
- Q1 How a one-time Estimate is told apart — rec (a) it targets the live sprint page, no new field. Answer: (c) both joined: targets the live sprint page and carries the marker; lint reports a marked Estimate whose target is not a sprint page
- Q2 Whether this Case also sorts the existing Estimates — rec (b) the two known ones too (archived), no full pass. Answer: (b)
Round 2 (sent):
- Q3 The name of the marker — rec (a) once: true. Answer: pending
- Q4 Whether case-schema.md tells the builder — rec (a) a sentence in the Render of rule-case-protocol beside the sprint-page Estimate sentence. Answer: pending
- Q5 How the lint finding is checked — rec (a) Criterion of estimate-lint-checks-the-statuses replaced, a line added. Answer: pending
- Q6 How the archive of the two Estimates is checked — rec (a) estimate-cleanup-moves names it, no new Estimate. Answer: pending

## Read
- case-schema.md, ratification.md (whole); rule-estimates-schema.md (whole)
- estimates: estimate-estimates-schema-checked (Criterion lists optional fields exactly -> must be replaced), -method-names-its-evidence, estimate-backlog-keeps-the-work-taken-out-of-a-built-page (passed, ledger 1831 L1), estimate-guppi-keeps-no-defer-of-its-shape (passed), estimate-lint-checks-the-statuses, estimate-cleanup-moves
- raw/2026-10-31/0431/spec.md L857-870 (case 963 defer)
- cases 966, 967, 968 of 1831 (968: shared fn reads create value as YAML where schema values hold no text -> covers once too)
- ship.py ships/plan; sprint_close.py L1-205; generate.py cascade L1383-1409, delete L1140-1156; cleanup.py docstring (slug leaves estimates lists); pages.py is_core/is_draft_core; ledger.py is_sprint_page L910-920 (ledger imports only event, pages); lint.py docstring L1-80, check_schema L236-261, unmet_conditions L182-207, check_status L547-583
- entity-sprint (core, "its Estimates are its Definition of done"), entity-sprint-plugin (not core); rule-backlog, entity-guppi core: true
- test_schemas.py grep: nothing lists optional fields

## Open forks
- Q3-Q6

## To do
- sub-cases: 969.1 schema field (replace Criterion estimate-estimates-schema-checked; supersedes case 963), 969.2 lint check in check_status via is_sprint_page (estimate-lint-checks-the-statuses), 969.3 delete the two
- greps: list-member (core in optional lists), glossary Estimate row, rule-lint text on status findings, rule-lint Purpose
- ledger lesson greps; case-example read before write
