# Note — Case 994 (Frontier C3: librarian report by handback alone?)

## Questions
- Q1 How the close tells the librarian to give its report back — rec (a) handback where the tool exists, else last text; answer: Ok = (a)
- Q2 Whether the stop at the first step says the same — rec (a) same wording; answer: Ok = (a)
- Q3 How the change is checked — rec (a) Criterion of estimate-close-reports-the-run replaced, purpose+method set anew, pending; answer: Ok = (a)

## Read
- vault/wiki/case-schema.md, vault/wiki/ratification.md
- vault/raw/2026-11-01/2038/handoff.md
- vault/wiki/rules/rule-close.md whole, estimates/estimate-close-reports-the-run.md whole
- vault/wiki/rules/rule-documentation.md whole (step 1 line 62)
- vault/wiki/rules/rule-librarian-report-copy.md; .guppi/guppi/libreport.py whole; casecheck.py outputs/subagent_outputs (1294-1342); ledger.py read_records
- .claude/agents/librarian-guppi.md lines 1-36, 124-131
- .claude/settings.json SubagentStop: casecheck --subagent, libreport
- lessons: lesson-hooks-subagentstop-reads-the-last-text-not-the-handback, lesson-hooks-subagentstop-fires-before-and-after-the-handback
- .guppi/links.md blocks: rule-close (3988), estimate-close-reports-the-run (990), .claude/agents/librarian-guppi.md (6006), rule-documentation (4062)
- WebFetch tools-reference: SubagentHandback "Provided only in auto mode ..."; sub-agents "plus SubagentHandback for a subagent that reports through it"
- ledger 2227: no lesson[error], no addresses

## Open forks
- none

## To do
- case-994.md written; searches rerun (5 wiki files; .claude: wait-what, librarian-guppi.md); answer with summary
