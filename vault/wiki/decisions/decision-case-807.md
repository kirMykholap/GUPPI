---
type: decision
case: "807"
status: current
children: ["[[decision-case-807.1]]", "[[decision-case-807.2]]", "[[decision-case-807.3]]", "[[decision-case-807.4]]"]
origin: raw/2026-10-13/2118/ledger.md#case-807
sprint: plugin
created: 2026-10-13
tags: [ci, plugin, harness, git, sprint, workflow, session, ledger]
---

## Problem

The clean copy cannot be written: the script fails on pointers it cannot remove safely, and it cuts pointers out of longer brackets in a way that can leave words that mean nothing. No rule says how a pointer is written so that the script can remove it, and nothing keeps new text in such a form.

## Recommend

- **How should a pointer inside a sentence of the code be reworded?**
  - Recommended: (a) move the pointer into brackets at the end of the sentence.
  - Answer: not answered; the person stopped the round to ask what is removed from the pages and how. It was replaced by **What is the one form a pointer takes, so the script strips it at every build?**
- **Does `guppi ship` learn to clean more forms, or is every leftover reworded at its source?**
  - Recommended: (c) reword every leftover at its source, and the check flags each number of a list of sessions.
  - Answer: not answered; replaced by **What is the one form a pointer takes, so the script strips it at every build?** and later by **What marks a bracket that the script removes?**
- **Does this Case also reword the pages and the files built from them?**
  - Recommended: (b) run `guppi ship` now and cover the pages too.
  - Answer: not answered; replaced by **Does this Case also reword the page leftovers, which needs a run of the script before I build?**
- **What is the one form a pointer takes, so the script strips it at every build?**
  - Recommended: (a) a bracket that holds only pointers to Cases, decisions or sessions; any other bracket with a pointer is listed, and each number of a list of sessions is flagged.
  - Answer: agreed, (a); later replaced by **What marks a bracket that the script removes?**
- **What happens to a link to a page that does not ship?**
  - Recommended: (a) the script turns it into the slug in a code span.
  - Answer: agreed, (a).
- **Where is the right form checked as new text is written?**
  - Recommended: (a) in the check of the plan for pages, told to `case-guppi` in `case-schema.md`, and in `make lint` for the code and the harness, both importing the one check of `guppi/ship.py`.
  - Answer: agreed, (a).
- **Does this Case also reword the page leftovers, which needs a run of the script before I build?**
  - Recommended: (a) yes, after a run of `uv run guppi ship` saved in the session folder.
  - Answer: agreed, (a); the run was made. Later replaced by **Does this Case still reword the pages, now that the script's list will change?**
- **What happens to a pointer that shares a bracket with other words?**
  - Recommended: (b) also strip a pointer that ends a bracket after a comma, a semicolon or a dash.
  - Answer: not answered; the person asked who checks that the script removes nothing needed, and asked that a pointer and the words that go with it, session numbers and times among them, stand inside the bracket. It was replaced by **What marks a bracket that the script removes?**
- **What marks a bracket that the script removes?**
  - Recommended: (a) any bracket that holds a pointer is removed whole; a pointer outside a bracket fails the run; the script lists every bracket that holds a pointer and other words, so that each is reviewed once.
  - Answer: agreed, (a).
- **Does this Case still reword the pages, now that the script's list will change?**
  - Recommended: (a) this Case changes the script, writes the rule, adds the two guards and rewords the code; a Case of the next session rewords the pages from the list of the changed script.
  - Answer: agreed, (a), in place of the earlier answer.
- **How does the script treat the ids of example Cases?**
  - Recommended: (a) the script reads a fenced block of a Markdown file as a sample, like a code span, and leaves `case-example.md` and the Render of `rule-case-example` out of the pointer check.
  - Answer: agreed, (a).
- **How does the script read the text of a `schema.yaml`?**
  - Recommended: (a) the script reads a code span in a `schema.yaml` as it reads one in Markdown.
  - Answer: agreed, (a).
- **How does the Case split, and how is each part checked?**
  - Recommended: (a) three sub-cases, each with its own check.
  - Answer: agreed, (a); later replaced by **How is the rewording of the code checked, now that one sub-case cannot carry two checks?**
- **How is the rewording of the code checked, now that one sub-case cannot carry two checks?**
  - Recommended: (a) four sub-cases: the new step of `make lint` and the rewording of the code are separate.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec, carry each line of the old Criteria that still holds, say why a dropped line is dropped, and date the check of the plan before the Spec is approved, not before a Case is signed.
  - Taken: 807.1 carries word for word the lines on the pages and files left out, on the sections of a page without `core: true` and on the form of a line, and the `context` says why three lines stand rewritten; the Purpose of `rule-clean-branch` says that `/pre-spec` finds a pointer before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run.
- **Change**
  - Asked: at pre-spec, `--check` judges every file outside `vault/` that `guppi ship` writes, the root files included, and the rewording of the code covers only the files Work Mode may edit.
  - Taken: `--check` judges `guppi/`, `.claude/` and the root files in 807.1, 807.2 and the Purpose of `rule-clean-branch`; 807.3 rewords `guppi/`, `Makefile`, `pyproject.toml` and `.gitattributes`, and a line on `.claude/` or `CLAUDE.md` goes to the handoff with the pages.
- **Change**
  - Asked: at pre-spec, the `context` names `SESSION` among the patterns of `guppi/ship.py` that judge a pointer.
  - Taken: the `context` names it.
- **Change**
  - Asked: at pre-spec, the line of 807.1 on `--check` leaves out `uv.lock`, as the task and the `context` do.
  - Taken: the line says that `--check` judges each file it would write outside `vault/` but `uv.lock`.

## History

- 2026-10-14 created · raw/2026-10-13/2118/ledger.md#case-807
