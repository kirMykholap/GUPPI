---
type: decision
case: "645"
status: current
children: ["[[decision-case-645.1]]", "[[decision-case-645.2]]", "[[decision-case-645.3]]", "[[decision-case-645.4]]", "[[decision-case-645.5]]", "[[decision-case-645.6]]", "[[decision-case-645.7]]", "[[decision-case-645.8]]", "[[decision-case-645.9]]", "[[decision-case-645.10]]", "[[decision-case-645.11]]", "[[decision-case-645.12]]", "[[decision-case-645.13]]", "[[decision-case-645.14]]", "[[decision-case-645.15]]", "[[decision-case-645.16]]"]
origin: raw/2026-10-05/0311/ledger.md#case-645
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow, session]
---

## Problem

The check reads the text the agent hands back and writes the file from it. So every fix after a finding means generating the whole Case again, and the whole Case enters the main agent's context at every answer. The question was where the check runs, which copy reaches the Spec, what the agent hands back, how the guard tells `case-guppi` from the main agent, how a file changed after its check is caught, and what happens to the handling of an answer of sub-cases alone.

## Recommend

- **When the check reads the file the agent wrote**
  - Recommended: (a) when the agent stops, from the file: the same stop hook finds the file by the agent's own Write and Edit calls and checks it whole; findings are fixed by Edit; rounds and Fact answers stay plain text.
  - Answer: agreed, (a). The person added that `case-guppi` must be allowed to write into `cases/`; as the person recalls, a subagent is not asked for permission to write in Plan Mode, so this stays convenient; the main agent still writes no Case and stays the orchestrator.
- **Which copy reaches the Spec**
  - Recommended: (a) keep the store: the check copies the passed file into it, and the Spec hook and the `Stop` check keep reading it; the sent file must still equal the stored text at the showing and at the Spec write.
  - Answer: agreed, (a).
- **What the agent hands back for a built Case**
  - Recommended: (a) a short summary: the path, then for each Case and sub-case its id and name, the Estimate that checks it with one line on what it checks, and its ledger lines; a ledger line that differs from the file is caught at the showing.
  - Answer: agreed, (a).
- **How the guard tells `case-guppi` from the main agent**
  - Recommended: (a) by the agent's type in the hook input, measured first: a Write or Edit under `cases/` passes only for `case-guppi`, which is refused anywhere else; a probe that waits for the person's word comes first in Work Mode, and work stops if the field is missing.
  - Answer: agreed, (a).
- **How the check of a changed file is itself checked**
  - Recommended: (a) two new Estimates, one for the `Stop` check of a showing and one for the Spec hook; the existing Criteria stand, and nothing clashes with the other Case of the session.
  - Answer: agreed, (a).
- **What happens to the check of a lone sub-case**
  - Recommended: (a) the whole file is judged every time; the lone-part handling and its Estimate are deleted, and the Estimates that say the agent writes no file or hands back the whole Case are replaced.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec, a probe that this session can run, and a context that says the new form is live from the next session.
  - Taken: the probe of 645.3 is made by a subagent this session can dispatch, and measures only whether the `PreToolUse` input names the agent type; the context says the render lands at the librarian's step and is read at the next session.
- **Change**
  - Asked: at pre-spec, check the documentation of Claude Code; when a subagent is dispatched in Plan Mode, no allow rule is needed.
  - Taken: `permissionMode: acceptEdits` in the agent file of `case-guppi` (645.1), no allow rule, and `rule-permissions` and `estimate-permissions` bound the prompt in Plan Mode to the main agent (645.16).
- **Change**
  - Asked: at pre-spec, keep the old form until the writer is live.
  - Taken: 645.2 still reads the answer text and writes the file when the subagent wrote no case file, until a reading of `estimate-case-build-writes-the-case` passes live; a later Case removes that path.
- **Change**
  - Asked: at pre-spec, replace the sentences of `rule-case-build`, `rule-spec-reconcile`, `rule-spec-write` and `rule-case-check` that the Case makes false.
  - Taken: replace pairs in 645.1, 645.3, 645.5 and 645.2, and a `set` of the `purpose` of `rule-spec-write`.
- **Change**
  - Asked: at pre-spec, the summary carries a line when the Case's `context` says another Case should change instead, and the showing shows it.
  - Taken: a line `**Other Case:**` in the summary (645.1), and the main agent asks about that Case from it (645.6).
- **Change**
  - Asked: at pre-spec, the Not done no longer names `case-schema.md`.
  - Taken: removed; Case 646 replaces those sentences.
- **Change**
  - Asked: at pre-spec, replace the Criterion of `estimate-case-check-shows-only-the-checked-case`.
  - Taken: 645.11, its pass condition joined with the comparison of the file.
- **Change**
  - Asked: at pre-spec, replace the four Estimates that speak of the answer as the Case, their moment the Case written into its file, and leave `estimate-case-build-checks-the-finished-case` for the session that takes Case 647 up.
  - Taken: 645.12 to 645.15, and the context says the deferred Estimate stays.

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#case-645
