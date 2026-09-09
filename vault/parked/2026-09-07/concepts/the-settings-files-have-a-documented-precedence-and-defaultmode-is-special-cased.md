---
title: "The settings files have a documented precedence, and `defaultMode` is special-cased inside it"
type: concept
status: current
authority: settings-file-precedence
basis: external
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md"]
tags: [harness, external, agents]
---

# The order, most-wins first

1. managed settings
2. `claude --settings <file>`
3. `.claude/settings.local.json`
4. `.claude/settings.json`
5. `~/.claude/settings.json`

**The project file overrides the user file.** That is the line this project needed and had never
read.

**`defaultMode` is special-cased**: a value of `auto` in a project file does not take effect at all.

# How it reached this store, and what that cost

**A dispatch to `claude-code-guide` answered it in 84,877 tokens, 1m32s and 17 tool uses** — the
cheapest dispatch this project has measured, against 143,840–230,882 tokens for a `/pre-task`
([[a-brief-that-carries-a-cost-without-its-findings-suppresses-the-finding]]).

**It had gone unread for eight sessions** while
[[the-vs-code-extension-reads-its-starting-mode-from-user-settings]] sat in the corpus as one of four
pages carrying a reading debt, and a decision about `permissions.defaultMode` was taken the same day
without it ([[plan-stays-the-projects-default-permission-mode-and-a-headless-run-passes-its-own]]).

# The one thing this cannot now settle on this machine

**Whether the project file overrides the user file *here* is no longer observable.** Measured
2026-08-26: `.claude/settings.json` held `plan`, `~/.claude/settings.json` held `auto`, and the
session ran in plan mode — which is the documented behaviour. **A minute later the owner changed the
user file to `plan`**, so both files now agree and the observation cannot be repeated.

**The measurement stays true as of when it was taken**; what is gone is the ability to check the
precedence by looking. The documented order is what stands, on `basis: external`, until something
tests it ([[the-region-coverage-figure-is-dated-where-it-stands]]).
