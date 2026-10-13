---
type: decision
case: "787"
status: current
children: ["[[decision-case-787.2]]"]
origin: raw/2026-10-12/2349/ledger.md#case-787
sprint: plugin
created: 2026-10-12
tags: [github, ci, git, sprint, workflow, session, harness]
---

## Problem

The project has no repository on GitHub, so nobody else can propose work and no check runs on a proposal. The vault still promises a pull request into `plugin`, and it states that the repository has no remote.

## Recommend

- **Which page describes the GitHub setup**
  - Recommended: (a) a new rule page `rule-github-repository`, its Estimates empty for now, the sprint Estimate checks the setup until the sprint closes.
  - Answer: agreed, (a).
- **What the ruleset on `main` enforces**
  - Recommended: (a) no deletion, no force push, every change by a pull request, the CI checks must pass before a merge; no approving review; the owner on the bypass list.
  - Answer: agreed, (a).
- **What the ruleset on `prod` enforces now**
  - Recommended: (a) a ruleset now that blocks creation, updates, deletion and force pushes, only the owner bypasses it; the CI writer is added by the later item The clean branch.
  - Answer: agreed, (a).
- **What CI runs, on which machine and when**
  - Recommended: (a) `make test`, `make lint` and `make style` on `windows-latest`, on every pull request by `pull_request` and on every push to `main` and a sprint branch; all three required; a first-time contributor's run waits for approval.
  - Answer: agreed, (a).
- **What the test pull request must prove**
  - Recommended: (a) against `main`, the checks shown, reviewed by the owner with the merge open to the owner, the second account cannot push to `main` or `prod`, then closed without a merge.
  - Answer: agreed, (a).
- **What happens to the claim that the repository has no remote**
  - Recommended: (a) the remote is stated, and `/hi` still runs no pull.
  - Answer: agreed, (a).
- **How the history is checked before it goes public**
  - Recommended: (a) a scan of the whole history for local paths, email addresses, keys and tokens, then a stop for the person's word before the push; a path that names only the user folder stays.
  - Answer: agreed, (a).
- **The repository's name and the branches pushed first**
  - Recommended: (a) `GUPPI`, public, on the owner's account, `main` and `plugin` pushed first.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the fixes of the report of `/pre-spec`. A session pushes nothing during a sprint: the owner pushes a sprint branch by hand, CI runs after that push, and a new branch goes up at the owner's first push. The Case closes the sprint item on the sprint page. The text of `rule-git-context` names how the local `main` and a sprint branch take the work of GitHub. Its `## How it works` leaves as the schema of a rule sets it. The check of the session start waits for the first `/hi` after the push.
  - Taken: in 787.1 the Purpose of `rule-github-repository` says who pushes and when. An `update` of `entity-sprint-plugin` moves the milestone The sprint turn and GitHub to `## Closed`. In 787.2 the facts of `## How it works` move into the Purpose of `rule-git-context`, which names the opening Case of a sprint and `/merge-main`. A one-off task removes the section. The `method` of `estimate-git-context-current` waits for the first `/hi` after the first push, and its trigger is `/hi` alone.
- **How the section `## How it works` leaves `rule-git-context`**
  - Recommended: (c) a new form of `update` that removes a section, set by a Case of its own, which this Case then uses.
  - Answer: agreed, (c); that Case is Case 792 of this session.
- **Change**
  - Asked: the main agent's reading, which the person's answer above settles: no task removes the section by hand, since `rule-vault-layout` says that no file of `wiki/` is written by hand. The section leaves through the `update` itself, in the form that Case 792 sets.
  - Taken: in 787.2 the one-off task is gone. The `update` of `rule-git-context` drops `## How it works` by the key `drop`.
- **When the section `## How it works` leaves `rule-git-context`**
  - Recommended: (b) this session changes only the sentence on the remote inside `## How it works`; a later Case moves the facts into the Purpose and drops the section in one step, once a form of `update` that drops a section exists.
  - Answer: agreed, (b); the Case on that form was put off to the backlog by a defer of `rule-page-generation`.

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-787
- 2026-10-13 child decision-case-787.1 archived · cleanup
