---
type: decision
case: "932"
status: current
children: ["[[decision-case-932.1]]", "[[decision-case-932.2]]", "[[decision-case-932.3]]", "[[decision-case-932.4]]", "[[decision-case-932.5]]"]
origin: raw/2026-10-30/1713/ledger.md#case-932
sprint: plugin
created: 2026-10-30
tags: [plugin, harness, session, render, hooks]
---

## Problem

`/guppi:install` refuses a project that already holds its own `CLAUDE.md`, `.claude/settings.json` or another file of the install, so GUPPI cannot install into an existing project. Its files cannot simply be joined to GUPPI's, since the render writes those files whole from ratified pages.

## Recommend

- **What the install does in a project that already holds its own files**
  - Recommended: (c) the install sets the clashing files aside, and the person brings back what they need by ordinary Cases later.
  - Answer: (b) the install sets the files aside, and the setup Case at the first `/hi` shows what they hold, for the person to keep or drop each part. The person first chose (c), asked how the process would go, and then changed the answer to (b).
- **How the first `/hi` learns of the set-aside folder**
  - Recommended: (b) the install writes one line about the folder into the brief it copies.
  - Answer: not answered; the round that asked it was never shown to the person, since the person changed the answer to the first question, and **Where a kept part of a set-aside file lands** and **What happens until the setup step is built** replaced it.
- **Which clashing files the install sets aside**
  - Recommended: (c) `CLAUDE.md`, the files under `.claude/`, `.gitattributes` and `.github/workflows/checks.yml`; a clash under `vault/` or `.guppi/` still stops the install.
  - Answer: agreed, (c).
- **Where the set-aside files go**
  - Recommended: (b) the folder `guppi-set-aside/` at the root, each file under its old path with `.set-aside` added to its name.
  - Answer: agreed, (b).
- **When the project's own `.claude/settings.json` is set aside**
  - Recommended: (a) just before GUPPI's copy, after `uv sync` passes.
  - Answer: agreed, (a).
- **Where a kept part of a set-aside file lands**
  - Recommended: (a) into the pages of GUPPI that already write that file; the setup Case creates no page.
  - Answer: agreed, (a).
- **What happens to the set-aside folder after the setup Case**
  - Recommended: (a) a task of the setup Case deletes it in the Work Mode of the same session.
  - Answer: agreed, (a).
- **What happens until the setup step is built**
  - Recommended: (a) nothing extra, since the published version waits for the setup step anyway.
  - Answer: agreed, (a).
- **How the Case is checked**
  - Recommended: (a) two parts, each with a new check, and the refusal lines of the two checks of the install rewritten.
  - Answer: agreed, (a).
- **Where a kept part lands when no page writes its file**
  - Recommended: (a) the setup Case holds a task that writes the kept part into GUPPI's copy of that file, run in the Work Mode of the same session.
  - Answer: (a).

## History

- 2026-10-30 created · raw/2026-10-30/1713/ledger.md#case-932
