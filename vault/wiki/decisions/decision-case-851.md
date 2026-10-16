---
type: decision
case: "851"
status: current
children: ["[[decision-case-851.1]]", "[[decision-case-851.2]]", "[[decision-case-851.3]]"]
origin: raw/2026-10-16/0342/ledger.md#case-851
sprint: plugin
created: 2026-10-16
tags: [session, harness, git]
---

## Problem

In a folder that is no git repository, `/hi` stops on a git error before the agent's first turn. It neither tells the person that GUPPI needs a git repository nor offers to make one, so a new install never opens its first sprint.

## Recommend

- **What should `/hi` do in a folder that is no git repository?**
  - Recommended: (b) offer to run `git init -b main`, run it on the person's yes and go on to open the first sprint in the same session.
  - Answer: agreed, (b).
- **What should happen when no repository gets made?**
  - Recommended: (a) stop after the note: no `/sprint-open` and no Frontier, and the person types `/hi` again after `git init -b main`.
  - Answer: agreed, (a).
- **How should the branch and status lines stop failing?**
  - Recommended: (a) one GUPPI command, `uv run --project .guppi guppi gitstate`, that prints the branch and the status, or a line that the folder is no git repository, and always exits 0, with a test.
  - Answer: agreed, (a).
- **Should `/guppi:install` change too?**
  - Recommended: (a) only `/hi`; the install keeps running no git command.
  - Answer: agreed, (a).
- **How should we check that this works?**
  - Recommended: (a) a new Estimate on `rule-git-context`, read by a test of the new command and once by hand in an empty folder with GUPPI and no git.
  - Answer: agreed, (a).
- **Where should the name of the main branch be set?**
  - Recommended: (a) leave it to the setup Case of `rule-morph`; this Case uses `git init -b main`.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec, the person agreed that on the yes the agent runs `git init -b main` and stops, telling the person that the repository is made and to type `/hi` again, so that the new `/hi` prints `main` under `Branch:` and `/sprint-open` and `/merge-main` read a real branch; no going on in the same turn.
  - Taken: on the yes the agent runs `git init -b main`, says that the repository is made and ends `/hi`; the person types `/hi` again.
- **Change**
  - Asked: at pre-spec, the person agreed that `git init -b main` stays out of `allowed-tools`, so that Claude Code asks the person to allow it. `rule-default-mode` gets one exception: `git init -b main` at `/hi` on the person's yes is the one write before a Case. The sentence that plan mode does not stop the command is dropped.
  - Taken: `allowed-tools` names `guppi gitstate` alone in place of the two git commands; Case 851.1 adds the exception to the Purpose of `rule-default-mode`; the Render of `rule-git-context` says nothing of plan mode.

## History

- 2026-10-16 created · raw/2026-10-16/0342/ledger.md#case-851
