# Note — Case 968 (Frontier C8, source brief; lesson L50 of session 0431)

## Questions
- R1 **Where the boolean of a `create` is fixed** — rec (c) one shared function; answer (c).
- R2 **What happens to a value outside the allowed list** — rec (a) hook refuses; answer (a).
- R2 **When the session also changes a page schema** — rec (a) values from schema on disk; answer (a).
- R2 **Whether `case-schema.md` describes the form** — rec (a) one sentence; answer (a).
- R2 **How the change is checked** — rec (a) new Estimate on rule-materialize; answer (a).

## Read
- case-schema.md, ratification.md, case-example.md (whole)
- lesson-spec-write-lifts-a-create-value-as-a-string; rule-spec-write head; rule-case-protocol head + section headings; rule-materialize head; rule-one-judgment head
- ratified.py 34-45, 160-460, 580-633; materialize.py 905-1050; prespec.py 1600-1690; lint.py 90-110, 236-250; casecheck.py docstring
- estimate-materialize-lifts-a-create-by-the-schema; Criterion lines of estimate-spec-write-* and estimate-case-protocol-*
- tests: test_case_schema.py (whole), test_materialize copy_schemas, test_schemas list, test_prespec core tests
- 0431 case-956, case-965; 1831 case-966, case-967
- https://pyyaml.org/wiki/PyYAMLDocumentation

## Open forks
- none

## To do
- Case written to cases/case-968.md; answer with summary; fix findings by Edit
