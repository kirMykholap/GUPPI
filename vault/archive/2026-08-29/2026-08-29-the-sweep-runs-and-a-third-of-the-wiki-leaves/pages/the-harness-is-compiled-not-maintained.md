---
title: "The harness is compiled from rule pages, not maintained by hand"
type: decision
status: archived
authority: harness-ownership
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [harness, process]
---

# Decided 2026-08-16: the harness stops being a maintained file and becomes a build product

**The harness** is the set of files that instruct an agent before it does anything — the two
`CLAUDE.md` files, the skills, the agents, the hooks, `settings.json`. Until this decision nobody
owned it: it was edited wherever it was noticed, and every staleness this project has recorded
lived in one of those files ([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

**A rule is written once as a page; the harness file is its output.** That is the whole change. The
rule pages are the source, the harness files are rendered, and the mechanism is
[[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]. The page type it needs was already
decided: [[rules-becomes-a-type-of-its-own]].

## What becomes a rule page

**A paragraph becomes a rule page if it is imperative and not enforced by a test.** Where a test
holds the rule, **the test is the rule** and no page is written — which keeps the rule set small
and keeps it from competing with the checks that already fail a build.

## Rejected

- **The librarian maintaining the harness files directly.** It never deletes text — that invariant
  is what makes unattended writing reviewable ([[the-librarian-writes-unattended]]) — and **a
  harness file must shrink**. The property that makes the librarian trustworthy is exactly the one
  that makes it unfit to keep a file whose value is in what it stops saying
  ([[the-paragraph-was-deleted-on-purpose]]).
- **Leaving the harness outside anyone's zone**, which is the status quo and is what produced every
  recorded instance ([[no-rule-reads-a-harness-file]]).
- **Symlinks from the harness file to the page.** Refused on a measurement rather than an argument:
  `core.symlinks=false` in this repository and `ln -s` produces a copy on this machine, so a
  committed symlink checks out as a text file holding a path — `CLAUDE.md` would contain one line
  and no instructions. It would also hard-code the vault's directory name, which nothing may do
  ([[the-vault-directory]]). One of the two questions on [[measurement-settled-what-argument-could-not]].

## What it obliges

- **A harness change has to be captured when it is decided**, not classified afterwards —
  [[a-harness-change-is-recorded-when-it-is-decided]].
- **The writer stays single.** The librarian writes both the decision page and the rule page; what
  runs after it is a script, not a second agent — [[the-steward-is-scripts-that-run-after-the-librarian]].
- **The gate this produces guarantees agreement and not truth**, which has to be written beside the
  design or the mechanism reads as stronger than it is —
  [[a-gate-guarantees-agreement-never-truth]].

**Nothing of this is built.** What blocks construction, and what each delay costs, is
[[what-the-harness-build-waits-on]].
