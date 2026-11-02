---
type: decision
case: "1003"
status: current
children: ["[[decision-case-1003.1]]", "[[decision-case-1003.2]]", "[[decision-case-1003.3]]", "[[decision-case-1003.4]]"]
origin: raw/2026-11-02/1337/ledger.md#case-1003
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness, render, tests]
---

## Problem

`/work` and `/retro` run commands that exit non-zero when they find something. Claude Code then refuses to load the skill, so Work Mode cannot start while `guppi check` is red, and Retro cannot start while a test is red.

## Recommend

- **How /work gets the baseline when a command is red**
  - Recommended: (a) a flag on `guppi test`, `guppi check` and `guppi style` that prints the real exit code on a last line and exits 0, and the preamble of `/work` calls the commands with it.
  - Answer: agreed, (a). In the first round the person turned down the option where the agent runs the commands by hand, and asked that the tests run by themselves.
- **Where a draft core page stops things**
  - Recommended: (a) keep the finding in `guppi check`, so CI and the build for prod stay blocked, and only Work Mode stops being blocked.
  - Answer: agreed, (a). The person said that a draft core page must block CI and the push of the plugin to prod, not the work.
- **What happens to the Branch line**
  - Recommended: (a) keep the git line, and drop the sentence about an empty line.
  - Answer: agreed, (a).
- **Whether /retro is fixed in the same Case**
  - Recommended: (a) yes, as a sub-case that changes `rule-retro` the same way.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) replace what `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` promises, test the flag in this session, and read the load after the librarian's render.
  - Answer: agreed, (a).

## History

- 2026-11-02 created · raw/2026-11-02/1337/ledger.md#case-1003
