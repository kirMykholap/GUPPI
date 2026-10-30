# Note — Case 917 (Frontier C4)

## Questions
Round 1 (answered: "3-b, rest agreed"):
- Q1 How the Estimate names the ignore file — rec (a) Criterion replaced whole + method set, both name vault/.gitignore — Answer: (a)
- Q2 The docstring of the close code — rec (a) name vault/.gitignore — Answer: (a)
- Q3 The event log Estimate with the same bare name — rec (a) leave out — Answer: (b) sub-case replacing its Criterion

## Read
- vault/wiki/case-schema.md, ratification.md (whole)
- estimates/estimate-sprint-close-moves-old-event-logs.md (whole)
- rules/rule-sprint-close.md, rules/rule-clean-branch.md, estimates/estimate-clean-branch-ships-neutral-texts.md
- decisions/decision-case-893.1.md; brief.md; handoff 1930 (grep)
- vault/.gitignore (3 lines); root .gitignore (no event_log lines)
- .guppi/guppi/ship.py 1-30, 150-160, 471-479
- .guppi/guppi/sprint_close.py 30-47 (docstring line 42)
- .guppi/tests/test_ship.py 183-187; test_sprint_close.py event_log tests
- estimates/estimate-event-log-records.md 1-30

## Facts
- guppi ship writes vault/.gitignore (case 893.1). Root .gitignore has no event_log lines.
- No test reads either Estimate page live.

## Open forks
- none. Round 2 Q4 When the event log check can be read — rec (a) drop /hi readings from method — Answer: (a)
- Given fixes done (917.1 paths, 917.2 /hi). Notes "line not carried" are the intended changes.

## To do
- Sub-cases 917.1 (sprint-close estimate + docstring), 917.2 (event-log-records Criterion)
- Other Case line to C3 dropped: Case 918 (C3) took the change in; finished files 913, 915, 916, 918 read, no overlap; no Sibling line now.
- DONE: case-917.md written, searches rerun; summary answered. Next: fix on findings by Edit only.
- Pre-spec 3.1 fixed: context no longer claims a purpose on estimate-event-log-records (it has none). Cases 913, 915, 916, 918 rebuilt at same time: read none of their files.
