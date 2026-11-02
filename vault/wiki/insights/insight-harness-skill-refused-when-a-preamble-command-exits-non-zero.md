---
type: insight
pattern: a skill runs a command as a ! shell pattern of its preamble that exits non-zero in a usual state of the project — no git repository for /hi, a red guppi check for /work — and Claude Code refuses to load the whole skill on that exit, so the skill fails exactly when the project is not in the state its command expects
status: actioned
children: ["[[lesson-work-skill-fails-to-load-on-a-red-check]]", "[[lesson-hi-fails-outside-a-git-repository]]"]
severity: 0
addressed_by: "[[decision-case-1003.3]]"
origin: raw/2026-11-02/1337/ledger.md#L7
sprint: plugin
created: 2026-11-02
tags: [harness, workflow, plugin, session, git]
---

## Pattern

Two skills were refused at load by Claude Code with "Shell command failed for pattern": /hi on `git branch --show-current` in a project with no git repository (lesson-hi-fails-outside-a-git-repository), and /work on `guppi check` while the check was red (lesson-work-skill-fails-to-load-on-a-red-check). In both, a ! command of the preamble exits non-zero in a state the project is often in, and the CLI refuses the whole skill on that exit.

## Proposal

A suggestion, not a decision: each ! command of a skill preamble could be written so that it exits 0 whatever it finds and names its own exit code or failure on a line, as case 1003 did for /work and /retro with --exit-zero; the git lines of /hi are not yet written so.

## History

- 2026-11-02 created · raw/2026-11-02/1337/ledger.md#L7
- 2026-11-02 updated: born actioned, its cause closed by case 1003.3 (synthesis) · raw/2026-11-02/1337/ledger.md#L7
