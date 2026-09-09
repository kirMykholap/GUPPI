---
title: "`plan` stays the project's default permission mode, and a headless run that must write passes its mode by flag"
type: decision
status: current
authority: default-permission-mode
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", ".claude/settings.json"]
tags: [harness, process, agents]
---

# The ruling, 2026-08-26

*(the owner selected it, against removing the default and against building a mechanism for
exceptions.)*

**`.claude/settings.json` keeps `permissions.defaultMode: "plan"`.** A headless run that needs to
write passes its mode on the command line, explicitly, in the one place that knows it needs to.

# Why the default is where the strictness belongs

**The default binds the interactive case, which is every ordinary session**, and plan mode is what
makes a session present its work before writing it — the trigger `/pre-task` hangs on
([[a-pre-task-runs-between-the-plan-and-its-approval]], [[plan-mode-blocks-edits-and-not-a-subagent-dispatch]]).

**A flag binds the exception, and it is visible in the command that takes it.** An exception carried
in a settings file is invisible at the moment it applies.

# The decision was taken without one fact that has since been established

**Named here rather than buried:** the ruling was taken before anyone had read the documented
precedence of the settings files, which says the project file overrides the user file and that
`defaultMode` is special-cased ([[the-settings-files-have-a-documented-precedence-and-defaultmode-is-special-cased]]).
**The fact supports the ruling rather than undermining it** — the project value is the one that
takes effect — and it is recorded because the order was the other way round.

# Rejected

**Rejected: dropping the project default** and letting each machine's user settings decide. That
makes the mode a property of whose laptop it is.

**Rejected: a mechanism for exceptions** — a marker file, an env var, a second settings file. The
flag already exists and costs nothing.
