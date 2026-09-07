---
title: "The commit step is typed into `/ingest` without a rule page, and the debt is recorded instead"
type: decision
status: current
authority: commit-step-rule-debt
binding: deferral
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md", ".claude/skills/ingest/SKILL.md"]
tags: [harness, process, vault]
---

# What the owner selected, 2026-08-29

**The commit step goes into `.claude/skills/ingest/SKILL.md` as typed text, with no `wiki/rules/` page
behind it, and the debt is recorded in an HTML comment at the step.** He selected it from the plan.

**Rejected: writing the rule page first and rendering the step from it**, which is the arrangement the
harness build exists to reach.

# The fork `/pre-task` raised, and why it was a fork at all

**Two live pages disagreed about whether an untested imperative in a harness file must come from a
rule page**, and the disagreement is what made this a choice rather than an omission:

- `the-harness-is-compiled-not-maintained` required it, of harness files generally.
- [[a-definition-may-render-into-the-repository-claude-md]] narrows the requirement to `CLAUDE.md`.

**The first of those is now in `archive/`**, swept on 2026-08-29, and the second does not reach a
skill file. **So nothing live states the obligation the debt is against** — the debt is real, its
governing page is frozen, and that is the honest reading rather than a reason to drop it
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

# What the step says

**It stands in `After the librarian returns`, outside the block quoted to the librarian.** It puts the
owner's reading of `git diff` before the commit, requires an English message naming what was compiled,
and requires `git status --short` to print nothing afterwards.

**Its placement follows [[the-librarian-writes-unattended]]**: the librarian does not commit, and step
12 of the quoted block already ends the librarian's half by archiving the source.

# The term of this deferral

**It arrives when the rule page is written or when a live page says none is owed.** Until then the
imperative is held by no test and no render, which is the condition
[[every-rule-in-wiki-rules-owes-a-mechanical-instrument]] names — and which
[[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]] priced once
already.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
