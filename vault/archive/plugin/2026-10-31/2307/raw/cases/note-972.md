# Note — Case 972 (item C9)

## Questions
- Round 1, Q1 **How the wait form is fixed** — recommended (b) pre-spec reports the near miss; answer: (b).
- Pre-spec finding A: **How pre-spec reports the near miss** — recommended (a) a `note:` line, no exit code; answer: (a).

## Read
- case-schema.md, ratification.md, case-example.md
- lint.py 640-779; prespec.py 10-31, 95-119, 194-207, 966-979, 1280-1395, 1455-1486, 2150-2190
- test_lint.py 480-505, 825-869; test_prespec.py 1405-1484
- rule-lint, rule-prespec-hook, estimate-prespec-hook-reports-a-method-that-waits-for-another-session, estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session, estimate-lint-checks-the-statuses, estimate-link-graph-at-session-start-writes-the-file; methods of the 7 grep files
- .guppi/links.md blocks

## Open forks
- none

## To do
- Findings A, B, C fixed by Edit in case-972.md (decision line exists at ledger line 5; number kept, shape kept). Answer with summary. Cases 973-975 built at same time: read none.
