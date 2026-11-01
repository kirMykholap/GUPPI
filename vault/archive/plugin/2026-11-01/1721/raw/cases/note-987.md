# Note — Case 987 (item C7, insight-plugin-cli-withholds-approval-of-a-long-plan)

Case 987 is RATIFIED (decision lines in ledger). Now: rebuild after /pre-spec findings, same number, same shape (keep every ledger line identical: same items, refs, tags).

## Questions
- Round 1, Q1 "What GUPPI does when the CLI withholds the approval" — rec (c); answer: agreed (c).
- Round 2: Q1 "What the person types" — rec (a) `/approve`; answer: `/approve-spec` (own). Q2 "What the command checks before it takes the Spec" — rec (a); agreed. Q3 "How the person learns the way" — rec (a) agent tells after a refused exit; agreed. Q4 "How the Case is checked" — rec (a) new Estimate test + CLI trial in Work Mode; agreed. Q5 "What becomes of the insight and the README note" — rec (a); agreed.
- Round 3: Q1 "How the agent's words after a refused exit are checked" — rec (a) new Estimate read in CLI trial; agreed.
- Pre-spec change (person "Ок" to main agent): CLI trials not in Work Mode of 1721; methods wait "after the librarian's run of session 1721"; only pytest part read this session -> recommend item **Change**.
- Rebuild done: all five findings fixed by Edit; 987.2 renamed "The agent names the typed approval before it leaves Plan Mode"; case-989 read whole (changes only Purpose last sentence of rule-spec-box); 984 read whole at second pass (its pair under ## Who builds a Case; ours under ## Plan Mode and the Frontier: no clash), context updated, no Sibling line now.
- prespec --check finding fixed: both methods name the event without a session id ("after the librarian's run that applies ... and renders ...").
- Round 4 (answered: agreed (a)): Q1 "When the agent names the way" — rec (a) in the reply that calls ExitPlanMode, a conditional line before the call. Reason: docs permissions: "If you select No without a comment on a prompt from the main conversation, Claude Code stops the turn"; interactive-mode: "On a permission prompt, Esc declines the action, the same as No without a comment".

## Findings of /pre-spec to fix
1. 987.2 wording conditional (no fact the agent can't know).
2. 987.2 moment: no reply turn after Esc (docs above) -> round 4.
3. One owner of hook: rule-spec-capture owns hook; drop implementation_ref from rule-skill-approve-spec create; its Purpose points to rule-spec-capture; rule-spec-capture new text describes typed path fully (refusals) and not "as rule-skill-approve-spec sets it".
4. Name in context: estimate-orchestration-puts-the-harness-before-plan-mode (Then "calls ExitPlanMode only after /pre-spec" stands); estimate-skill-sprint-open-starts-at-hi (is_hi_prompt keeps answers), estimate-event-log-records ("Any other prompt is silent..." — hi_refusal unchanged; /approve-spec judged by spec.py not event hook); estimate-hook-registry-rendered (new hook registered by a line of it: stands); estimate-prespec-hook-reports-a-pointer-outside-a-bracket (When at ExitPlanMode; gate keeps output).
5. onward claim: drop or fix (onward --plan also fires after ledger hook refused the reply just before; silent on STOP:).
- Do not read files of 982, 984, 989 (built at the same time).

## Read
- case-schema, ratification whole; insight; decision-case-957; lessons; schemas; rule pages spec-capture, prespec-hook, work-mode, carry-over L28-39, spec-box L16-37, hook-registry whole, orchestration L1-33; spec.py whole; prespec.py parts; gate.py L1-95; event.py L125-165; ledger.py L610-645; onward.py L1-90; estimates listed in finding 4; case-example.md
- WebFetch: CHANGELOG 0-100k; permission-modes; hooks 0-200k; skills; interactive-mode (Esc row); permissions (comment section)

## To do
- After round 4: Edit case file: context, 987.1 Purpose/Render/pairs, methods (wait after librarian's run), 987.2 when/then/pair/purpose/method, recommend items; rerun searches; summary.
