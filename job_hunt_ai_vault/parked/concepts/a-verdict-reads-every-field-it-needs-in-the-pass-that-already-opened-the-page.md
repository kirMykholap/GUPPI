---
title: "A verdict reads every field it needs in the pass that already opened the page"
type: concept
status: current
authority: single-pass-field-reading
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check.sh"]
tags: [harness, vault, record-schema]
---

# The mechanism

**Rule 5c already resolves a `decided_by:` wikilink, finds the page it names, and reads that page's
`type:`.** The narrowed `idea` verdict needs one more field off the same page — `binding:` — and it
comes off the same `awk` invocation.

**The citing page's `status:` is not re-read either.** The frontmatter pass that runs first already
holds every page's status and emits a marker for the ones that matter, so the verdict reads what has
already been read.

# Why this is a rule and not an optimisation

**A second loop over the same links is a second reader of one fact**, and two readers of one fact
disagree eventually — usually when one of them is changed and the other is not
([[a-check-asks-by-running-the-writer-it-checks]]).

**It also decides where a verdict lives.** The pair verdict did not become a rule of its own; it
rides the loop that had already opened its subjects. A rule numbered after the last one would have
had to re-derive the resolution that rule 5c performs.

# What it costs

**Nothing measurable, and that is the point.** The pass over the corpus is already the dominant term
in the gate's cost ([[the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to]]), so a field read
inside it is free and the same field read in a new traversal is not.
