---
title: "Severity in `vault-check.sh` is decidable, which is what lets a flag be safe"
type: concept
status: current
authority: gate-severity
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# There are two severities and no third

```sh
note() { echo "VAULT-CHECK: $*"; fail=1; }     # a verdict
echo  "VAULT-CHECK: advisory: ..."             # a report
```

A line either goes through `note`, which sets `fail=1`, or it is a bare `echo`. **Nothing in this
script is halfway.**

# Why that matters more than it looks

**"Only lines that cannot fail may go behind `--lint`" is a class rather than a judgement**
([[the-tag-density-advisories-move-behind-lint]]). It can be read off the source, and **nobody can
later move a verdict behind the same argument** by claiming a line is "not really a failure".

The alternative — three severities, or a severity attached by convention rather than by the
function called — turns the flag into a place where checks quietly go to die. That is the shape of
a flag that silently changes what a command does
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

# The channel is narrow on purpose

`advisory:` is one word, printed once per finding, with what it names sorted underneath — so
`grep -c 'advisory:'` counts advisories and nothing else
([[an-advisory-prints-one-line-and-sorts-what-it-names]],
[[the-filename-advisory-prints-one-name-per-line]]). A severity system that is decidable and a
channel that is countable are the two properties the split depended on.

# A verdict's severity can be staged across one session, and the staging is a design — 2026-08-21

**Rule 13 printed advisories while 470 slugs were minted and grouped, then flipped to `note` in the
same session.** Red before the corpus carried `authority:` would have turned the gate red, and
`lock-the-librarian.ps1` reads a red gate as a refusal to dispatch — locking out the only writer
permitted to clear it ([[the-librarian-lock-hook]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**The flip is the acceptance test for the marking.** A severity that can only be raised once every
page satisfies the rule turns "is the corpus marked up?" into a question the gate answers by itself,
with no count to quote and nothing to trust ([[authority-becomes-the-index-and-is-required-outside-rules]]).

**It was applied the other way first and reverted.** Tightening ahead of the corpus was measured at
**233 verdicts**, reverted, and the steps reordered. **The order was the decision, not an accident**,
and it is the same sequence `binding:` followed the same day
([[a-decision-declares-whether-it-binds]], [[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
