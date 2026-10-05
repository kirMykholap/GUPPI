---
type: decision
case: "664"
status: current
children: ["[[decision-case-664.1]]", "[[decision-case-664.2]]", "[[decision-case-664.3]]"]
origin: raw/2026-10-05/1616/ledger.md#case-664
sprint: migration
created: 2026-10-05
tags: [hooks, harness, session, workflow, render]
---

## Problem

The rule that keeps the text of Decision pages out of a search is text that loads but is not followed. Agents leave the exclusion out, or put it first, where it does not work. The questions were how the exclusion is enforced, whether a Decision page named by `addressed_by` may be opened, whether an agent may Grep inside the folder of the Decision pages, which agents the hook covers, and how the change is checked.

## Recommend

- **How every search leaves out the Decision pages**
  - Recommended: (a) a hook adds the exclusion at the end of the glob of each Grep over the wiki, by changing the call, as the hook of `rule-page-read` does for a read; the rule file keeps only the part on reading a Decision page.
  - Answer: agreed, (a).
- **When an agent may open a Decision page**
  - Recommended: (b) keep the two reasons; a read through `addressed_by` stays a breach that the check counts.
  - Answer: agreed, (b).
- **Which agents the new hook covers**
  - Recommended: (a) every agent, the librarian too.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) two checks: a new Estimate of the hook, read by a test and one live search in the main agent and in a subagent; the existing Estimate rewritten to cover only the load of the file and the reads of Decision pages.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec, may an agent Grep inside `vault/wiki/decisions/`: (a) only a Read, `rule-ask` changes and the hook covers a Grep inside the folder too; or (b) a Grep is allowed for the two reasons, the hook leaves a Grep whose path is inside `decisions/` unchanged, 664.2 says the text arrives by a Read or such a Grep for one of the two reasons, and the frame of `ask-guppi` stays. The person chose (b).
  - Taken: 664.1 leaves unchanged a Grep whose `path` is `vault/wiki/decisions/` or lies in it; 664.1 sets the rule's `purpose` and Purpose anew and makes its Render say the hook covers every agent and a Grep inside the folder is allowed for a reason; 664.2 promises that the text arrives by a Read or such a Grep, for a reason of the frame only.

## History

- 2026-10-05 created · raw/2026-10-05/1616/ledger.md#case-664
