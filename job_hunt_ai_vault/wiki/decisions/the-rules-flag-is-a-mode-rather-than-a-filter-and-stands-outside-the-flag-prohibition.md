---
title: "`--rules` is a mode rather than a filter, and therefore stands outside the prohibition on hiding a verdict behind a flag"
type: decision
status: current
authority: mode-versus-filter
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# The reading, and the owner confirmed it

> **owner:** «согласен»

**The session ruled that `--rules` is a mode and not a filter, and he confirmed the reading and
ordered it written as a decision page rather than left in a script comment.** The reason he gave for
the page is the reason it is here: the next session meets
[[the-tag-density-advisories-move-behind-lint]] with the flag conversation in front of it, and a
comment inside `scripts/vault-check.sh` is not where that reader looks.

# The distinction, and it is decidable rather than a judgement

**A filter runs the check and shows less of it. A mode runs no check at all.** `--rules` prints the
rule register swept from the script's own headings and exits; it evaluates nothing, it never prints
`VAULT-CHECK: ok`, and it always exits 0.

**So it has no run from which to hide anything.** The prohibition's two properties are about a run
whose output is trimmed: *the exit code is identical with and without the flag*, and *only lines
that cannot fail may go behind it*. Neither has a subject here.

**Rejected: treating any second flag on the gate as the forbidden shape.** That reading would forbid
`--lint`, which the same prohibition created, and it confuses the argument — which is about a
verdict disappearing — with the argument's instrument, which is a flag.

# What it does not authorise

**It does not open the flag that would skip rules 12 and 13.** That one narrows a run and moves the
exit code, which is exactly what the prohibition forbids
([[the-injector-is-cheapened-instead-of-adding-a-flag-and-the-prohibition-is-not-lifted]]).

**And a mode is not a licence to move a check into one.** A flag that ran some rules and printed
some verdicts would be a filter however it was named; what makes `--rules` a mode is that it
reaches the vault at all only to be told not to.
