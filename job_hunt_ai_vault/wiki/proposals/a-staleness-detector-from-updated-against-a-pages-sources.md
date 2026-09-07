---
title: "A staleness detector built from `updated` against a page's own sources, and why a stamp may not clear a suspicion"
type: proposal
status: current
authority: staleness-detector-design
basis: measurement
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "scripts/vault-check.sh"]
decided_by: [[the-frontmatter-core-is-fixed-and-updated-joins-it]]
tags: [vault, testing]
---

# The instrument for the gap this vault named and measured

[[fidelity-to-a-source-and-fidelity-to-the-tree]] records *fidelity to the tree: checked by
nothing*, with **six pages measured on 2026-08-15 as describing what the repository no longer
does**. This is the design for the check, and **its inputs already exist**.

```
for each page:  d = updated (else created)
                for each source that is a live file of the tree:
                    if that file's last commit is newer than d  ->  the page is SUSPECT
```

**One `git log --name-only` pass dates every file at once**, so the cost is a single process rather
than one per page — the constraint that already shaped `vault-check.sh`
([[vault-scripts]]).

## Its coverage, and the half it cannot see

**91 pages of 142.** The other 51 cite only the immutable `raw/`, which never changes, so they are
invisible to it — **although a page compiled from a journal can go stale against the code exactly as
any other can.** That is a limit written down, not an omission, and it is the shape of limit this
store insists on naming ([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]).

Coverage is **total** for the one class of page that does not exist yet: pages about the
application, whose sources are code
([[entities-describe-the-application-once-the-detector-exists]]).

## `updated` carries no weight it cannot hold

**It is stamped by a script from the diff and means bytes moved** — not that anyone re-read the
sources. So **it must not clear a suspicion**: a typo fix would clear one silently, and silently in
the dangerous direction ([[the-frontmatter-core-is-fixed-and-updated-joins-it]]).

**A suspicion is a finding, and a finding carries an outcome** — fixed, or a page saying why it
stands. That is how every other finding here is closed, and it is S1's criterion 1
([[the-audits-findings-are-owed-to-the-owner]]). The acknowledgement is deliberate and written;
the date is automatic.

## Two mechanics that are easy to get wrong

1. **The stamper compares content excluding its own line**, or it re-triggers on itself forever.
2. **The write ritual becomes stamp, then catalogue, then check** — stamping modifies files, and
  rule 9 would otherwise fail on the catalogue the stamp has just invalidated
  ([[the-catalogue-is-generated-not-maintained]],
  [[the-steward-is-scripts-that-run-after-the-librarian]]).

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).
