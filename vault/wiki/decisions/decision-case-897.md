---
type: decision
case: "897"
status: current
children: ["[[decision-case-897.1]]", "[[decision-case-897.2]]", "[[decision-case-897.3]]", "[[decision-case-897.4]]", "[[decision-case-897.5]]", "[[decision-case-897.6]]"]
origin: raw/2026-10-28/2312/ledger.md#case-897
sprint: plugin
created: 2026-10-28
tags: [sprint, workflow, harness, git, session, render, librarian, ledger, hooks, case-build, plugin, ci]
---

## Problem

The clean copy fails its check of neutral texts again: shipped rules send a new project to two skills the copy does not hold, the schema justifies a rule by a command the copy lacks, and two shipped methods wait for a moment of GUPPI's past.

## Recommend

- **How much does this Case fix now?**
  - Recommended: (a) the failures only.
  - Answer: agreed, (a).
- **How is the missing-skills group fixed?**
  - Recommended: (b) make each sentence depend on the skill being there.
  - Answer: agreed, (b).
- **How is the reason for the bracket rule reworded?**
  - Recommended: (a) say where the reason holds.
  - Answer: agreed, (a).
- **How are the two methods fixed that wait for a past moment?**
  - Recommended: (a) cut the part tied to the past.
  - Answer: agreed, (a).
- **When is the check read again?**
  - Recommended: (a) wait for the librarian's run of this session.
  - Answer: agreed, (a).
- **Is the Criterion list rewritten now?**
  - Recommended: (a) leave it for a later Case.
  - Answer: agreed, (a).
- **The librarian's frame carries an open put-off: what happens to it?**
  - Recommended: (a) take up the put-off and close it.
  - Answer: (a).
- **How is the merge exception in the librarian's frame worded?**
  - Recommended: (b) put the exception in a bracket with its pointer, as the two other rules do.
  - Answer: agreed, (b).
- **`rule-page-generation` carries a put-off of its own: what happens to it?**
  - Recommended: (a) take up the put-off and put it off again with the same text.
  - Answer: agreed, (a).
- **Does the row `Librarian` of the glossary follow the three rules?**
  - Recommended: (a) widen the row the same way.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, widen the merge exception to any merge of `main` in the librarian frame, `rule-vault-layout` and `rule-page-generation`, with no bracket and no skill name, so that the copy's texts agree, since 897.2 tells a project without `/merge-main` to bring its branch up to `main`.
  - Taken: 897.3 rewords the three rules that way and gains the updates of `rule-vault-layout` and `rule-page-generation`; the wording of Q8 is replaced.
- **Change**
  - Asked: at `/pre-spec`, close the put-off of `rule-documentation` all the same, and say plainly that `estimate-close-commits` stands `pending` and put off.
  - Taken: 897.3 keeps `{supersedes:case 839}`, and `context` says so.

## History

- 2026-10-29 created · raw/2026-10-28/2312/ledger.md#case-897
