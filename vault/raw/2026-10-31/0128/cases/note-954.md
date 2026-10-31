# Note — Case 954 (C6, estimate-search-leaves-out-decisions-refuses-ask-guppi)

## Questions
- Q1 **What to do with the deferred reading** — rec (b) test by hand in Work Mode, method changed; answer "Ок" = (b).
- Q2 **How the trial reaches `ask-guppi` outside `/pre-spec`** — rec (b) Case also changes the sentence of rule-orchestration; answer "Ок" = (b). Split: 954.1 trial + method + defer retired; 954.2 rule-orchestration.
- Q3 **How the change to the rule is checked** — rec (a) new Estimate read by the trial itself; answer "Ок" = (a).
- Q4 **How wide the exception is** — rec (b) only a hook that judges the calls of ask-guppi; answer "Ок" = (b).
- Q5 **When the trial runs** (round 4) — the rule text lands only at the librarian's render, after this Work Mode; rec (a) the trial waits for the first Work Mode after that render; answer "Ок" = (a).
- BUILT: cases/case-954.md written (954.1, 954.2); summary sent with Other Case 950.2 (a － pointer line after the "only at pre-spec" line of its Criterion). Searches of context rerun, same output.
- /pre-spec findings 1,2,3,9,10 fixed: exception covers Work reading; 954.1 Criterion written back + pending; methods name the session whose brief puts the reading under Work; new 954.3 (rule-ask, rule-search-leaves-out-decisions, estimate-ask-tries-a-decision-call-only-for-a-hook-trial). Two **Change** items in recommend. Cases 950, 952, 953 rebuilt at the same time: read none.

## Read
- case-schema.md, ratification.md, case-example.md
- estimate-search-leaves-out-decisions-refuses-ask-guppi.md whole; rule-search-leaves-out-decisions.md; decision-case-936.md
- brief.md (line 34, Flags line 54); backlog.md line 14
- .claude/settings.json whole; grepguard.py whole; test_grepguard.py test names
- 0304 spec.md 644-713; .claude/agents/ask-guppi.md whole; case-953.md; case-950.md whole
- rule-orchestration.md whole to line 107: line 39 sentence "the agent dispatches `ask-guppi` only at pre-spec, ... as `rule-prespec` sets it (cases 634.3, 674.2)." — to change. Line 33 stands.
- Case 950.2 writes back Criterion of estimate-orchestration-shows-the-built-case, line "it dispatches `ask-guppi` only at pre-spec, ... never to build a Case, ..." -> Other Case: pointer to new Estimate.
- Grep `dispatches `?ask-guppi`? only|ask-guppi`? only at|only at pre-spec|only at `/pre-spec`` over {vault/wiki/**,.claude/**,.guppi/**}: orchestration.md, log.md, rule-orchestration.md, estimate-orchestration-shows-the-built-case.md
- .guppi/tests/test_orchestration.py whole (reads only showing/defer blocks of orchestration.md: stands)
- hooks doc https://code.claude.com/docs/en/hooks
- ledger: no lesson[error], no {addresses:

## Open forks
- Q5

## To do
- new Estimate slug estimate-orchestration-starts-ask-guppi-for-a-hook-test (Glob free?); write case-954.md; summary with Other Case 950.2
