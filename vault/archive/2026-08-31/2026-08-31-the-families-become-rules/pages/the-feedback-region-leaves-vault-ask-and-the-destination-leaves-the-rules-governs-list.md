---
title: "The feedback region leaves `vault-ask`, and that destination leaves the rule page's `governs:` list"
type: decision
status: archived
authority: feedback-region-audience
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md", ".claude/skills/vault-ask/SKILL.md", "wiki/rules/speak-the-feedback-in-the-turn-and-the-hook-files-it.md"]
tags: [harness, process, agents]
---

# The ruling, 2026-08-29

**owner:** «снять из vault-ask этот рендер»

**The rendered region [[speak-the-feedback-in-the-turn-and-the-hook-files-it]] is removed from
`.claude/skills/vault-ask/SKILL.md`, and that path leaves the rule page's `governs:` list.**

**The ground is audience.** The block is addressed to the *caller* — speak the miss in your turn and a
`MessageDisplay` hook files it. A forked skill is not the caller: under `context: fork` the `SKILL.md`
becomes the forked agent's own prompt, so the region would tell the fork to speak a block no hook
reads and no caller sees ([[a-forked-skill-starts-empty-and-a-subtask-fork-inherits-everything]]).

**And the requirement is not lost by the removal** — the main agent already carries it, from
`CLAUDE.md`, where the same rule renders.

# It is decided and it is not built

**The region still stands at `.claude/skills/vault-ask/SKILL.md:28-48`, and
`wiki/rules/speak-the-feedback-in-the-turn-and-the-hook-files-it.md:4` still lists that skill in
`governs:`.** Nothing was removed on the day it was ruled.

**Two edits are owed and they are not the same party's.** Dropping the path from `governs:` is a
`wiki/rules/` write and is the librarian's; deleting the marker pair and its text out of the skill
file is a deletion inside a harness file and is a session's
([[the-harness-is-compiled-not-maintained]], [[vault-librarian]]).

**Order matters and the safe order is the other one.** Removing the destination from `governs:` first
leaves an orphan region in a file the injector no longer writes — text that looks rendered, agrees
with nothing, and is checked by nothing, since the tooling that would delete such a region is itself
a proposal ([[the-injector-removes-a-region-whose-rule-folded-into-another-page]]). **So the ingest of
2026-08-29 recorded the ruling and executed neither half**, and the pair is raised in the brief.

# What this is an instance of

**A rule region's audience is a property of the host file's execution mode**, and nothing in this
vault said so before this ruling. It is the first case where changing how a file is run changes who
its rendered text is talking to.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*

# Both halves landed, in the order this page fixed — 2026-08-30

**The region left `.claude/skills/vault-ask/SKILL.md` first, and the destination left
[[speak-the-feedback-in-the-turn-and-the-hook-files-it]]'s `governs:` list afterwards.** The ordering
this page ruled was followed rather than rediscovered, and no orphan region was left behind.

**`/pre-task` found both halves still owed on the day they were done** — the region at
`SKILL.md:28-48` and the `governs:` entry at line 5 of the rule page — and it was one of exactly three
mechanical findings that check returned
([[divergence-the-pre-task-was-dispatched-on-a-session-the-owner-had-declared-an-override]]).

**The file then became the fourth destination of
[[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]**, and the injector
reported `1 region(s) rewritten, 0 problem(s)`. **So the skill lost one region and gained another in
the same session**, and the difference between them is exactly what this page is about: the first was
addressed to a caller the fork does not have, the second is addressed to whoever is reading the store,
which is the fork itself.

**The instance this page names is now a live mechanism rather than a prediction**
([[the-vault-ask-skill]], [[a-forked-skill-starts-empty-and-a-subtask-fork-inherits-everything]]).

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
