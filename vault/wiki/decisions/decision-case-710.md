---
type: decision
case: "710"
status: current
children: ["[[decision-case-710.1]]", "[[decision-case-710.2]]"]
origin: raw/2026-10-07/0636/ledger.md#case-710
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow, render, session]
---

## Problem

A shell command can rewrite a file of the repository with CRLF line endings, a byte-order mark or another encoding, and no check sees it: the guard before a Bash call reads only heredocs, and no hook judges a PowerShell call.

## Recommend

- **Where the check catches a file changed through a shell command**
  - Recommended: (b) check the files after the call: a new hook after each shell call reads the files git sees as changed or new and reports each one with a CRLF line ending, a byte-order mark, or bytes that are not valid UTF-8.
  - Answer: agreed, (b), after the main agent explained the round again in plain words.
- **Which shell tools the check covers**
  - Recommended: (b) Bash and PowerShell.
  - Answer: agreed, (b).
- **Which page holds the new check**
  - Recommended: (a) a new rule page, such as `rule-shell-write-check`, with its own Estimate; `rule-bash-guard` and its Estimate stay as they are, and `rule-hook-registry` gains the hook entries.
  - Answer: agreed, (a).
- **Which files the check looks at after each call**
  - Recommended: (a) every changed or new file, ignored files left out, at every call, so a faulty file is reported again until it is repaired.
  - Answer: agreed, (a).
- **What the hook does with a faulty file**
  - Recommended: (b) repair what is safe and report the rest: the hook turns CRLF into LF and removes a byte-order mark, names the files it repaired, and only reports a file that is not valid UTF-8 or holds UTF-16 text.
  - Answer: agreed, (b).
- **What happens to the Insight page**
  - Recommended: (a) mark it fixed and correct its Pattern: `actioned`, `addressed_by` the decision of this Case, and a Pattern that names the three lessons.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of pre-spec: a hook does run on PowerShell, `uv run guppi event tool`, so `context` and `problem` should say that no hook judges or guards a PowerShell call.
  - Taken: `context` and `problem` now say that no hook judges a PowerShell call, and that the only hook on it logs the call.
- **Change**
  - Asked: a finding of pre-spec, which the person agreed with: write `addressed_by` as the quoted wikilink to `decision-case-710.1`, as the schema sets, and keep the bare slug only if the check of the file refuses that link, quoting its refusal in `context`.
  - Taken: the check refused the link, so the bare slug stands, and `context` quotes the refusal.

## History

- 2026-10-07 created · raw/2026-10-07/0636/ledger.md#case-710
