# Note — Case 995 (item C2)

## Questions
- Round 1:
  - **What changes after the failed reading** — rec (a) context lists each search and reading — answer: (a).
  - **Whether the second agent's check is part of this Case** — rec (a) no — answer: (b) yes.
- Round 2 (answer "Ok" = all recommendations):
  - **Where the plan checker's new step goes** — rec (a) new question in /pre-spec list — answer: (a).
  - **How far the plan checker looks on its own** — rec (b) list + own walk Grep — answer: (b).
  - **How the builder's part is checked** — rec (a) Criterion replaced, pending — answer: (a).
  - **How the plan checker's part is checked** — rec (a) new Estimate on rule-prespec, reconciles gets the question — answer: (a).

## Read
- case-schema, ratification, case-example (whole)
- rule-case-build, rule-ask, rule-prespec (whole)
- estimates: reads-the-readers-of-a-new-files-folder, link-graph, prespec-reconciles, ask-searches-at-prespec, checks-the-finished-case; Criteria of rule-ask estimates, confirms-the-findings-once; case-build Criteria in tool-results file
- links.md blocks: rule-case-build, rule-prespec, rule-ask, the three harness files, two estimates
- test_guppi_package.py 1-95; generate.py reword_pattern/reword_text/is_path_pair; lint.py PATH_START; prespec.py check_frame/frame_name
- ledger 2227: no lesson[error]

## Open forks
- none

## To do
- Write case-995.md: 995.1 rule-case-build + estimate; 995.2 rule-prespec + rule-ask + new estimate-prespec-finds-a-reader-of-a-new-files-folder; 995.3 estimate-prespec-reconciles Criterion (split: one promise per sub-case, prespec.py two-promises check).
- Done: written; casecheck notes fixed (reconciles deferred line carried); pre-spec findings 1.5 (tasks block in dispatch list, rule-prespec 2nd pair, 995.3 line) and 2.1 (rule-ask sentence no longer restates the question; estimate-ask-finds in context) fixed. Cases 993, 994, 996 built at the same time: read none.
- Summary again.
