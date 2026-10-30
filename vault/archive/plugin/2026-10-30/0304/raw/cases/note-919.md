# Note — Case 919 (C5: ship line on test_render.py:500)

## Questions
- Q1 How should the docstring be fixed? — rec (a) bracket at the end "(case 914)." — answer: (a)
- Q2 How should the fix be checked? — rec (a) estimate-clean-branch-code-holds-pointers-only-in-brackets pending, Criterion written back unchanged, read at Retro — answer: (a)
- Q3 Should the Case also add a guard against a repeat? — rec (a) fix only — answer: (b) add a test over live .guppi/
- Q4 What should the guard test judge, and how does it run? — rec (a) unmarked test in test_ship.py over .guppi/ files by ship.judged, no vault read — answer: (a)
- Q5 How should the guard be checked? — rec (a) new Estimate estimate-clean-branch-tests-judge-the-live-code on rule-clean-branch — answer: (a)
- Q6 Should rule-clean-branch say that the guard exists? — rec (a) one sentence after the --check passage — answer: (a)

## Read
- case-schema.md, ratification.md (whole)
- test_render.py 470-529; pointers.py whole; ship.py 1-181, 283-345, 457-517, 604-668
- rule-render-harness.md; rule-clean-branch.md 1-40 (deferred_by 893.1, backlog C4)
- estimate-clean-branch-code-holds-pointers-only-in-brackets, estimate-clean-branch-ships-the-tests
- pyproject addopts -m "not live"; guppi.toml test = pytest -q; test_ship.py REPO line 41, live test 1005
- brief Lint line 51; retro SKILL line 20; ledger 0304 no error lessons

## Open forks
- none (check_backlog judges only source backlog; C4 is brief: no supersedes)

## To do
- case-919.md written (919.1, 919.2); answer with the summary; fix findings by Edit
