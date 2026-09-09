---
title: "The VS Code extension reads its starting permission mode from user settings and ignores the workspace"
type: concept
status: current
authority: vscode-initial-permission-mode
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/settings.json"]
tags: [harness, agents, process]
---

# What the two settings actually govern

**`claudeCode.initialPermissionMode` in *user* settings decides what mode a VS Code session starts
in, and workspace values are ignored entirely.** So `permissions.defaultMode` in this repository's
`.claude/settings.json` **cannot reach the extension**.

**Both are set here.** The repository half covers terminal sessions, including any `claude -p` run;
the user half covers the editor. Neither is redundant and neither covers the other.

# How it was found, and why that matters more than the fact

**The ledger's `permission_mode` column disagreed with the repository's settings on its first row.**
The session reported `auto` while `.claude/settings.json` said `plan`
([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).

**A configuration file that is correct on disk and inert in the running session is invisible to
every reading of that file** — which is the same class as a hook registered correctly and never
loaded, and is why the ledger records observed state rather than configured state
([[claude-code-config-loading]], [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

# A consequence nobody has decided about

**`permissions.defaultMode: "plan"` now applies to every new terminal session in this repository**,
including headless `claude -p` runs. There are none today, and nobody has ruled on what should
happen when there are.

**That was ruled on 2026-08-26**: the project default stays, and a headless run that must write
passes its mode by flag
([[plan-stays-the-projects-default-permission-mode-and-a-headless-run-passes-its-own]]).

# This page's title is at best incomplete, and the documented precedence says why — 2026-08-26

**The precedence is documented and had gone unread for eight sessions**, while this page sat in the
corpus as one of four carrying a reading debt. Most-wins first: managed settings,
`claude --settings`, `.claude/settings.local.json`, `.claude/settings.json`,
`~/.claude/settings.json` — **the project file overrides the user file**, and **`defaultMode` is
special-cased so that `auto` in a project file does not take effect at all**
([[the-settings-files-have-a-documented-precedence-and-defaultmode-is-special-cased]]).

**Measured the same day:** `.claude/settings.json:3` held `plan`, `~/.claude/settings.json` held
`auto`, and the session ran in plan mode — consistent with the documented order and inconsistent with
this page's title.

**The observation can no longer be repeated.** A minute after the measurement the owner changed the
user file to `plan`, so both files agree. **The measurement stands as of when it was taken**; what is
gone is the ability to settle the question by looking.

**And the owner's edit does not reach this project at all** — `.claude/settings.json` already held
`plan` and overrides it. The change takes effect only in projects with no value of their own.

**Not corrected here, because the correction is a claim about behaviour and the evidence for it is
now documentation rather than observation.** Naming the discrepancy is what this section does; a
retitle or a supersession waits for a test ([[the-title-check-asks-and-the-answer-is-a-retitle]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
