---
title: "Staging by wildcard while the other party edits the tree gives an unrelated change the wrong commit message"
type: lesson
status: archived
authority: wildcard-staging
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md"]
tags: [process, agents]
---

# What happened, 2026-08-17

`git add -A` swept a deletion that was not the session's work into the session's commit: the owner
had removed a design PDF while the commit was being assembled. **He chose to leave it**, so the
outcome is recorded rather than repaired.

**The rule broken is written nowhere**, and that is part of the finding.

# The shape

Two parties edit one working tree — an agent and the owner, in the same minutes. `git add -A` names
no files, so it stages **whatever the tree happens to hold at that instant**, including changes the
committing party has never seen. The commit message then describes one of the two sets of changes
and is attached to both.

**The damage is not to the code, which is intact; it is to the history**, which is the one artefact
this project uses to review the librarian and every other unattended writer
([[the-librarian-writes-unattended]]). A commit whose message does not describe its contents is a
review that cannot be performed later.

# What would prevent it

- **Stage by path** when anyone else may be editing — the file list is short and known, because the
  session that did the work knows what it touched.
- **Read `git status` immediately before committing**, not at the start of the assembly — and note
  that it will not show an empty directory either
  ([[an-empty-directory-is-invisible-to-git-status]]).
- Recorded, not enforced: this is a working agreement, and the repository's `CLAUDE.md` is where a
  rule of that kind would go if the owner wants one
  ([[the-repository-claude-md-becomes-a-dispatch-table]]).
