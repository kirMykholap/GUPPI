---
type: decision
case: "775"
status: current
children: ["[[decision-case-775.1]]", "[[decision-case-775.2]]", "[[decision-case-775.3]]"]
origin: raw/2026-10-10/2350/ledger.md#case-775
sprint: plugin
created: 2026-10-10
tags: [sprint, git, workflow, harness, session, render]
---

## Problem

No rule sets where the merge of a closed sprint's own branch into `main` stands at the opening of the next sprint. The closing Case leaves an unticked line that does not hold the choices the merge needs, `/sprint-open` does not name the merge, and the brief gave that line under `Cases` while `/sprint-close` says `Work`.

## Recommend

- **Where should the merge step be written?**
  - Recommended: (a) in the opening Case: `/sprint-close` writes no merge line, and the opening Case holds the merge tasks when the session is not on `main`, so no leftover line reaches the brief.
  - Answer: agreed, (a).
- **How should the merge run?**
  - Recommended: (a) a fast-forward only, `git merge --ff-only`, with a stop for the person on a refusal, as the first condition of `vault/wiki/where-to-stop.md` sets it.
  - Answer: agreed, (a).
- **Which branch does the new sprint work on?**
  - Recommended: (a) always a new branch named by the sprint id, made from `main` after the merge, and the old branch deleted by `git branch -d`, a refusal a stop.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) two sub-cases: a new Estimate on the merge tasks of the opening Case, and the Criterion of the closing check replaced so that the closing Case holds no merge line, both read by hand at the Retro of this session against the new Renders in its Spec.
  - Answer: agreed, (a).
- **What if the session that opens a sprint is already on `main`?**
  - Recommended: (a) no merge, only the new branch: the opening Case makes the branch `<new sprint id>` from `main` and switches to it.
  - Answer: agreed, (a); replaced by the question on what the opening Case holds when the session is on `main`, since Work Mode stops on `main` before that task runs.
- **What does the opening Case hold when the session is on `main`?**
  - Recommended: (a) no git task on `main`: Work Mode stops on `main` as it always does, and the person makes the branch `<new sprint id>` and moves to it.
  - Answer: agreed, (a).
- **Change**
  - Asked: the findings of `/pre-spec`. A refused merge is no fork that needs a new Case, so it does not fit the first condition of `vault/wiki/where-to-stop.md`, and its sixth condition covers `/box` alone. The person chose (a): widen the sixth condition to a refusal of `git merge --ff-only` or `git branch -d` in the merge tasks of the opening Case, and replace the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` to take it in. Two facts of `context` were also corrected: the hits of `tests/test_sprint.py`, and the claim on where the merge is stated.
  - Taken: Case 775.1 names the sixth condition in its step and its `－` line. The widened condition and the replaced Criterion stand as Case 775.3, since they are a promise of their own on `rule-where-to-stop`. `context` is corrected.

## History

- 2026-10-11 created · raw/2026-10-10/2350/ledger.md#case-775
