---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent asks for no number when it sends a ratified Case back in Plan Mode and shows it under the number the summary of its case-guppi gives, a new number with supersedes marks included
method: "by hand, at the Retro of this session: the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session in which a ratified Case comes back in another shape: the messages of the main agent to its case-guppi and the showing, read in the transcript of that session under ~/.claude/projects/ against the Criterion, the transcript in the estimate line"
checked: 2026-11-27
origin: raw/2026-11-26/1336/ledger.md#case-1066
sprint: plugin
created: 2026-11-26
tags: [session, workflow]
---

## Criterion

When:
In Plan Mode, with `vault/wiki/orchestration.md` loaded, the main agent sends a ratified Case back to its `case-guppi` and that `case-guppi` answers with the summary of the Case.

Then:
The main agent asks for no number in its message to `case-guppi`.
**＋** The main agent shows the Case under the number of the `**Case:**` line of the summary.
**＋** A new number whose decision lines carry `{supersedes:case N}` is shown as it stands, since the Splitting of `vault/wiki/case-schema.md` sets it.
**－** The main agent does not send the Case back to be built under its old number.

## Result

2026-11-27, at the /hi of session 2214, by hand, transcript ~/.claude/projects/c--PROJECTS-GUPPI/ee662ed3-a713-4708-a454-42866d7e862b.jsonl (session 1402), records counted from 0: the three Plan Mode messages that send a ratified Case back to its case-guppi (946 for 1082 after the person's change; 1152 and 1153 for 1082 and 1085 after the findings of /pre-spec) ask for no number and end "Answer with the summary of the Case as built again"; the summaries came back as Case 1082 (962, 1187) and Case 1085 with the new sub-case 1085.9 (1216), and the main agent showed them under those numbers (979, 1250); no Plan Mode send-back came back under a new number, so the clause on a new number with supersedes was not exercised in Plan Mode; Case 1086 came in Work Mode by a new dispatch (1478)

## History

- 2026-11-26 created · [[decision-case-1066]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L4
