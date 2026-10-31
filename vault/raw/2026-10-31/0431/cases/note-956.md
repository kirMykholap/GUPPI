# Note — Case 956 (item C3, estimate-close-reports-the-run failed)

## Questions
- Q1 How the report reaches the disk — rec: none (fact not checked) — Answer: (a) a script writes the file; person added: must understand what blocks the librarian, but 1a covers the gap; their picture: librarian writes report as its text, a hook copies it, main agent then sends the file instead of retyping
- Q2 A check for a missing report — rec: (a) no new check — Answer: (a)
- Q3 What copies the text into the file — round 2 rec (a) librarian's Bash call to a guppi command before commit; NOT answered in round 2: person asked where the script takes the text, proposed: report passed in librarian's return, a hook copies it, main agent reads, shows and commits. Round 3 asks Q3 again (same title), rec (c) the person's route — Answer: (c)
- BUILT: case-956.md written (956.1 hook rule+estimate+registry; 956.2 rule-close, rule-documentation, estimate-close-reports-the-run, probe task; 956.3 rule-handoff + estimate-handoff-dispatches; 956.4 rule-spec-box + estimate-spec-box-runs-a-conserved-spec). Next: summary; fix findings by Edit only.
- Q4 What /handoff shows the person — rec (a) text of the file, returned text + note when none — Answer: (a)
- Q5 Finding out what triggers the refusal — rec (a) probe by hand in Work Mode, knowledge lesson — Answer: (a)

## Read for the frame
- vault/wiki/case-schema.md, ratification.md (whole)
- rules/rule-close.md, estimates/estimate-close-reports-the-run.md (whole)
- .claude/agents/librarian-guppi.md (whole); .claude/skills/handoff/SKILL.md (whole)
- .guppi/guppi/guard.py (whole); ratified.py 892-1085
- .claude/settings.json hooks (SubagentStop: casecheck --subagent)
- casecheck.py outputs/subagent_outputs (1284-1331): reads text blocks AND SubagentHandback message from agent_transcript_path
- event_log 2026-10-31 lines 1025-1079
- transcript 850a2e1e subagents/agent-afc9f2b665331e424.jsonl: l219 Write report.md, l220 tool_use_error "Subagents should return findings as text, not write report files...", v2.1.312; l230 final report; l231 handback
- lesson-hooks-subagentstop-reads-the-last-text-not-the-handback
- archive case-944.md context
- WebFetch sub-agents docs, errors.md all parts, CHANGELOG first 100k: refusal undocumented

## Open forks
- none. Q6 "What happens to the report of this session's own run" rec (b) one-off task commits it in this session — Answer: (b); task added in 956.3, context sentence added. Other findings 1.1-1.5, 1.9 (new 956.5 estimate-close-commits), 2.1 (context) fixed by Edit; Change item added. Built at same time: 959, 960, 961, 962 — do not read.

## To do
- Change from Case 960 (read whole): methods of 956.3/956.4 read dispatch line + text shown in session transcript under ~/.claude/projects/, estimate line names it; Change item + context sentence added. Answer with summary; re-ratified with 960.
