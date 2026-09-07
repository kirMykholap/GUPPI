---
title: "The tag-density advisories move behind `vault-check.sh --lint`, and the bare run keeps only what is about this run"
type: decision
status: current
authority: advisory-channel-split
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check.sh", ".claude/skills/vault-lint/SKILL.md"]
tags: [vault, retrieval, harness]
---

# Decided and built 2026-08-20 on the owner's ruling

**A bare `bash scripts/vault-check.sh` went from twenty-one advisories to one.** The line that
survives is region coverage — the only one that was ever about the run in front of you, and the one
the other twenty buried ([[a-governed-file-with-no-region-is-an-advisory]]).

**`/vault-lint` is the only caller that passes the flag**, and it is the only place the split
decision is ever made ([[lint-waits-for-an-open-sprint]]).

## What was rejected

- **Splitting `record-schema`**, which buys about two ingests of quiet and costs a judgement pass
  over sixteen pages ([[record-schema-is-dropped-from-the-trim-candidates]]).
- **Doing nothing again**, which is what had happened five times. The advisory this channel exists
  to carry had by then stood unactioned long enough to become indistinguishable from one that was
  scheduled and skipped ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

## Two properties hold it, and both are selftest cases rather than promises

- **The exit code is identical with and without the flag**, exercised on a green tree and a red one.
  A flag that can change the exit code is hiding a check rather than a report.
- **Only lines that cannot fail may ever go behind it.** That is decidable rather than a judgement,
  because severity in this script is `note` — which sets `fail=1` — against a bare `echo`, with no
  third state ([[severity-in-the-gate-is-decidable-which-is-what-lets-a-flag-be-safe]]). Nobody can
  later move a verdict behind the same argument.

**The flag ADDS lines and never removes a check**: `diff` of the two outputs is additions only, and
an unknown argument exits 2 rather than being ignored
([[the-gate-exits-on-a-usage-error-with-a-code-of-its-own]],
[[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

**The parity cases were proved able to fail**, since they catch nothing today: `--lint` was made to
set `fail=1` in the real tree, the bare run returned 0 against `--lint`'s 1, and the file was
restored in the same command
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

**Suite after the change: `caught 133, missed 0`, exit 0** — the old single density case replaced
by two that pin the flag in both directions, plus the two parity cases.

# One consumer had already made this separation by hand, silently

`.claude/hooks/check-the-journal.ps1` filters the gate's output with
`Where-Object { $_ -notmatch 'advisory' }` before showing it. **That is independent evidence for the
change rather than an argument for it** — the journal hook reached the same conclusion, that these
lines are noise to a reader who is not auditing the corpus, and fixed it at its own end instead of
at the source ([[the-journal-gate-hook]]).

**It also means the hook cannot break on this change**: what was removed from a bare run is exactly
what it was already discarding.

# The cadence half of a later proposal re-argues this — 2026-08-20

**A proposal to give `/vault-lint` a rule-usage axis also asks for it to run after every ingest**
([[a-rule-usage-axis-for-vault-lint]]). **That half inherits this page's problem exactly**: what
moved the density advisories behind `--lint` was that printing them on every run buried the one
advisory that was about that run.

**The rule-usage half does not inherit it** — it is a different question asked of a different
corpus, and nothing about it requires the every-run cadence. The two halves are separable and the
proposal records them as such.

# The channel stands and the cadence is overturned — 2026-08-21

**`/vault-lint` is no longer the only caller that passes the flag.** The sentence above saying it is
went false on 2026-08-21: `/ingest` runs `bash scripts/vault-check.sh --lint` at every session end,
on the owner's ruling ([[the-tag-density-advisories-run-at-every-ingest]]).

**Everything else on this page is untouched.** The flag exists, the bare run still keeps only what is
about that run, the exit code is still identical with and without it, and the two parity cases still
pin it in both directions ([[severity-in-the-gate-is-decidable-which-is-what-lets-a-flag-be-safe]]).

**The reason recorded here is not refuted, and the owner ruled with it in front of him.** An
always-firing advisory stops being read. What changed his answer is that the figures became a
finding — `vault` selects 124 of 193 pages in `decisions/` — and a finding nobody sees is worse than
one they tire of ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

**The gap this page did not see**: the channel it built had exactly one consumer, and that consumer
is defined per sprint and had never run against this corpus
([[lint-waits-for-an-open-sprint]]). **A correct channel with no cadence delivers nothing**, which
is not an argument against the split and is the reason it needed a second caller.

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*
