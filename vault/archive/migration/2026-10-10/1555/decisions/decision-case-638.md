---
type: decision
case: "638"
status: archived
update: ["[[rule-prespec]]", "[[rule-ask]]", "[[estimate-prespec-confirms-the-findings-once]]"]
origin: raw/2026-10-05/0109/ledger.md#case-638
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Problem

The frame of `ask-guppi` asks for one line per finding at the confirmation. Both runs of the last `/pre-spec` wrote reasons of several sentences instead. Both added a list of files read, and one added a list of what it did not check. Their verdicts were right. The main agent's message also invited a new finding, which the frame forbids. The question is whether that form is enforced or loosened, what else the answer may hold, and whether the message gets a rule of its own.

## Recommend

- **How the form of the confirmation answer is held**
  - Recommended: (a) allow a short paragraph: for each finding, the verdict on its own line under its number, then at most a short paragraph of up to three sentences on why; the rule text and the check's wording change to match.
  - Answer: (a).
- **What else may stand in the confirmation answer**
  - Recommended: (a) findings only, even where a general instruction asks for file paths.
  - Answer: (b) after the findings, one list of the paths of the files the agent read; no list of what it did not check.
- **Whether the main agent's confirmation message gets its own rule**
  - Recommended: (a) the `/pre-spec` rule says the message asks only whether each finding is closed and invites no new finding and no new judgment of the Case; the check gets a line on it.
  - Answer: the person asked for an explanation, then said they are not sure but will try it as planned: (a).
- **Change**
  - Asked: at the `/pre-spec` of this session, the run of `ask-guppi` found that the ban on a list of what was not checked goes against `rule-agent-writing`, and leaves a confirmation that breaks its frame no line to say so. Asked whether the confirmation takes the form of the first answer or keeps the form as chosen, the person chose (a), the form of the first answer, as recommended.
  - Taken: after the findings stands a list of what was not checked, "none" when all is checked and no rule broken, its last lines one per rule a search broke, as Case 639 sets it for the first answer; then the list of files read; `rule-agent-writing` and the case file of Case 639 enter `given`.
- **Change**
  - Asked: the same `/pre-spec` found that the `context` counted the sentences of the two answers and named their lists differently from the `## Result` of the Estimate.
  - Taken: the counts and the lists now come from the two agent transcripts, which the `context` names, and the `problem` says which run added which list.

## History

- 2026-10-05 created · raw/2026-10-05/0109/ledger.md#case-638
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
