---
title: "The Obsidian CLI as a reading surface for this store"
type: proposal
status: current
authority: obsidian-cli-reading-surface
basis: human
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "job_hunt_ai_vault/pages.base"]
decided_by: [[the-obsidian-cli-is-recorded-as-a-proposal-and-not-evaluated]]
tags: [vault, retrieval, external]
---

# Why it is here at all

**The owner asked for it to be recorded: «да, запиши как proposal».** It was raised in conversation
and nothing was built.

# What it would buy

**The official Obsidian CLI searches, lists and queries frontmatter.** That is the same shape as two
things this store maintains by hand:

- `bash scripts/vault-catalogue.sh`, which prints `authority` and `title` across the corpus in one
  pass ([[vault-scripts]], [[pages-base]]);
- `bash scripts/vault-authority.sh --near`, the family lookup a page is admitted through
  ([[authority-becomes-the-index-and-is-required-outside-rules]]).

**Both are reading, and reading is where a general tool can help.** A frontmatter query engine
somebody else maintains is strictly more capable than the `awk` pass here, and the reading surface is
the half of this store that has no test.

# What it cannot carry, and this is the boundary rather than a caveat

**Not the checking and not the injection.** `scripts/vault-check.sh` and `scripts/vault-inject.sh`
encode this project's own contract — which keys a folder admits, what a rule's slice is, which files
a region may land in — and no general tool knows any of it
([[the-per-folder-frontmatter-schema]], [[a-check-asks-by-running-the-writer-it-checks]]).

# The disqualifying condition, named now rather than discovered

**It requires the Obsidian desktop application to be *running*.** The gate is invoked from hooks and
read by `lock-the-librarian.ps1`; a dependency on a GUI being open turns an unattended refusal into
a coin toss ([[the-librarian-lock-hook]], [[the-journal-gate-hook]]).

**So the honest scope is the reading half only**, on a developer's machine, as a convenience beside
the scripts rather than under them. Anything a hook calls stays plain `bash` over the files.

# What is open

- **whether the reading half alone is worth a dependency**, given that nothing here may add one
  without an owner ruling;
- **what it would do that `ripgrep` plus the two scripts does not**, stated as a measurement rather
  than a capability list — the funnel it would join is already delivered as a procedure and is not
  the bottleneck anyone has measured ([[the-reading-funnel-is-delivered-as-a-procedure]]);
- **how it compares with the toolkits this store was already read against**
  ([[openspec-and-spec-kit]]), which is the same question asked of a different tool.
