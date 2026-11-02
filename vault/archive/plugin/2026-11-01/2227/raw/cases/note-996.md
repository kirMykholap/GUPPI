# Note — Case 996 (C1, the clean branch)

## Questions
- Q1 What lets the tagged run write `prod` while harness pages stand draft — rec (c); answer (own words): take core off the blocking pages, backlog entry to give it back
- Q2 Which pages lose `core: true` so the tagged run can write `prod` — rec (c); answer (c)
- Q3 How the build tells a page that was never finished — rec (a) History; answer (a)
- Q4 Whether a failed check still blocks a page that was finished before — rec (a); answer (a)
- Q5 What lint keeps reporting — rec (a); answer (a)
- Q6 How the change is checked — rec (a); answer (a)

## Read
- case-schema.md, ratification.md, case-example.md; rule-clean-branch, rule-lint, estimates (refuses-a-draft-core-page, sprint-plugin-ci, lint-checks-the-statuses)
- pages.py is_draft_core; ship.py drafts, governed, docstring; lint.py check_status; generate.py cascade
- tests: test_ship draft_core, test_lint draft_core, test_guppi_package line 100
- links.md blocks of all changed pages and modules; cases 993-995

## Open forks
- none

## To do
- Case written: vault/raw/2026-11-01/2227/cases/case-996.md; answer with summary; fix findings by Edit
