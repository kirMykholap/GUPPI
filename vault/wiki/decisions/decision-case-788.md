---
type: decision
case: "788"
status: current
children: ["[[decision-case-788.1]]", "[[decision-case-788.2]]", "[[decision-case-788.3]]", "[[decision-case-788.4]]", "[[decision-case-788.5]]", "[[decision-case-788.6]]", "[[decision-case-788.7]]"]
origin: raw/2026-10-12/2349/ledger.md#case-788
sprint: plugin
created: 2026-10-12
tags: [sprint, ledger, hooks, harness, session, workflow, render, schema, git]
---

## Problem

A Case id is one global number, so two people who run sprints on parallel branches write the same ids, and their pull requests clash on Decision pages, Case files and `{supersedes:case N}` marks.

## Recommend

- **What should a Case id look like when it carries its sprint?**
  - Recommended: (a) the sprint id, a hyphen, then the number, such as `plugin-12.1`, one spelling in ledger lines, page names, file names and branch names.
  - Answer: agreed, (a).
- **How does a sprint id stay unique when two people open sprints at the same time?**
  - Recommended: (a) the sprint id starts with its author's GitHub name, such as `kir-plugin`, and the opening Case refuses an id that a live or archived sprint page holds.
  - Answer: agreed, (a).
- **What happens to the Case numbers that already exist?**
  - Recommended: (a) they stay as they are; a plain number means a Case from before sprint ids, and every reader takes both forms for good.
  - Answer: agreed, (a).
- **When does the new numbering start?**
  - Recommended: (a) at the next sprint that `/sprint-open` opens; `plugin` keeps global numbers to its close.
  - Answer: agreed, (a).
- **Is this one Case or two?**
  - Recommended: (a) one Case with two sub-cases: one for `/sprint-open` and its check of the id, one for the id form and every reader of it.
  - Answer: agreed, (a); later replaced by the answer to the question whether Case 788 should split into more parts.
- **How does the main agent find the next Case number inside a sprint?**
  - Recommended: (a) one function in code gives the next number from the Decision pages of the open sprint, live and archived, and the session's ledger; a command prints it, the main agent runs it before it dispatches a new Case, and the check of a Case file uses the same function for a Case built again.
  - Answer: agreed, (a).
- **What checks that a new sprint id is unique?**
  - Recommended: (a) the ledger hook refuses the `create` of a sprint page whose id a live or archived sprint page already holds; `case-guppi` asks for an id that starts with the author's GitHub name, and no code checks the name.
  - Answer: agreed, (a).
- **Which checks confirm the two sub-cases?**
  - Recommended: (a) two new Estimates, each checked by a test: one on `rule-skill-sprint-open` for the ledger hook and a taken or free sprint id, one on `rule-ratification` for each reader of a Case id over both forms; the existing Estimates stay as they are.
  - Answer: agreed, (a); later changed by the answers on the check of the opening questions and on the split.
- **Which id does the opening Case of a new sprint take?**
  - Recommended: (a) the main agent asks the sprint id first, in one plain question before the dispatch; the opening Case is `<id>-1`; the command reads the open sprint from the `create` line of the sprint page in the session's ledger, else from `sprint.md`.
  - Answer: agreed, (a).
- **How does the command know that a sprint keeps plain numbers?**
  - Recommended: (a) a fixed list in `guppi/caseid.py`: `migration` and `plugin` keep plain numbers, and every other sprint takes the new form.
  - Answer: agreed, (a).
- **Which judgment says that a sprint id is taken?**
  - Recommended: (a) the ledger hook calls `has_page`: an id is taken when its page stands live, or archived outside a `raw/` folder, even with a broken header.
  - Answer: agreed, (a).
- **Should the check of the opening questions be rewritten now that the main agent asks for the sprint id first?**
  - Recommended: (a) rewrite `estimate-skill-sprint-open-asks-the-opening-questions` whole: the main agent asks the id first, the prompt gives it to the opening Case `<id>-1`, `case-guppi` asks the rest; read by hand at the Retro of this session.
  - Answer: agreed, (a).
- **Should Case 788 split into more parts after the review findings?**
  - Recommended: (a) seven parts, one check each: the taken sprint id, the id asked first, the id form and its readers, the count of the next id, `/box`, the guard of a Case file, and the check of an id held by another agent.
  - Answer: agreed, (a).
- **Change**
  - Asked: the findings of `/pre-spec`, with the person's answers: set which id the opening Case takes and how the open sprint is known; count the next id by one function that also sees Cases dispatched but not ratified; judge a taken sprint id by the judgment the code already shares; name the checks of `/box`, of the guard of a Case file and of the check of an id held by another agent; let the test of the new check run what its Criterion states.
  - Taken: the parts 788.3 to 788.7 hold these fixes. The command holds the id it prints in the store. The test of 788.2 runs `held_number` and the naming of a Case file, and the line on the Decision page of a new-form id left its Criterion.

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-788
