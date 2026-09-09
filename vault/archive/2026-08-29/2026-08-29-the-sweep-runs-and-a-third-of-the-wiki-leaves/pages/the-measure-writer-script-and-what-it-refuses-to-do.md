---
title: "The measure writer script, its refresh pass, and what its check refuses to do"
type: proposal
status: archived
authority: measure-writer-design
basis: inference
sprint: S3
created: 2026-08-25
decided_by: [[a-gauge-is-written-by-a-script-that-runs-the-command]]
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-check.sh", "scripts/vault-inject.sh"]
tags: [vault, harness, record-schema]
---

# What it would be

**A script that owns the numbers in a measure region.** The librarian names a page and a subject and
runs it; the script resolves them, refuses what it cannot resolve, runs the command the region names,
and writes the reading beside it ([[a-gauge-is-written-by-a-script-that-runs-the-command]]).

**A refresh pass walks every measure region in the corpus**, runs each command and writes each number.
The librarian runs it when it has finished writing pages.

# The check does not run the commands, and that is a design decision rather than an omission

**`--check` reads shape and executes nothing.** Running each gauge's command and comparing would
execute arbitrary commands taken from page content, at unbounded cost — **one gauge may name a
command that costs 38 minutes**.

**What protects a gauge from a lie is that it names the command anyone can re-run.** That is
re-checkability, not a guarantee, and the distinction is worth keeping in view
([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]]).

# The destination bracket needs a subject as well as a page

**A gauge destination is `[gauge:<page-slug>/<subject-slug>]`; testimony keeps one name.** One page can
legitimately carry more than one gauge, so the subject cannot default to the page — and the
uniqueness check that is already deferred compares subjects rather than pages
([[a-measure-line-names-its-destination-in-brackets-after-the-kind]],
[[a-gauge-is-checked-for-uniqueness-and-the-check-waits-for-subjects]]).

# The writer half needs an instruction and the check half does not

**The check needs no instruction anywhere.** The gate would invoke it the way rules 12 and 13 already
invoke `vault-inject.sh --check` and `vault-authority.sh --check`, and a missing script is red by the
gate's own missing-file note ([[a-check-asks-by-running-the-writer-it-checks]]).

**The writer half is written as a rule page rather than a fourth hand-maintained copy.** The
instruction to run the gate after a write already exists in three hand-maintained copies and is
rendered from no rule page — `job_hunt_ai_vault/CLAUDE.md:48`, `.claude/agents/vault-librarian.md:146`
and `.claude/skills/ingest/SKILL.md:128` and `:285`. **Adding a fourth would reproduce the defect
diagnosed in the feedback rule the same day**
([[the-feedback-rules-extra-destination-is-withdrawn]]).

**So the rule page would govern `.claude/agents/vault-librarian.md`, `job_hunt_ai_vault/CLAUDE.md` and
`.claude/skills/ingest/SKILL.md`** — and the vault's own instruction file would gain its first
rendered region, since no rule page governs it today
([[governs-is-a-path-from-the-repository-root]]).

# What it costs, in the unit that matters

**Delegating a check to a script costs about 1.5 s on this gate** — rule 13 runs
`vault-authority.sh --check` for 1.5 s and rule 12 runs `vault-inject.sh --check` for 3.57 s, against
a 15.3 s total. **But the suite runs the gate about 171 times against a 34m8s total**, so a delegated
check adds roughly four minutes to the suite rather than 1.5 seconds to a run. **It lands in the same
budget the owner asked to shrink** ([[the-gate-flag-fork-is-recorded-and-nothing-is-built]]).

# What is open

- **A destination naming a page that does not exist** must be an error with a named verdict, on the
  model of `BAD VERDICT` in the coverage script
  ([[the-page-verdict-is-checked-for-the-pages-existence-and-not-for-the-claim]]). Without it a typo
  in a slug is a silently dropped number.
- **Rule 11 has to recognise a `measure` region explicitly** and declare it out of scope, rather than
  letting it escape the `malformed` verdict by an accident of spelling
  ([[the-measure-section-grammar-is-one-line-per-number]]).
- **Nothing checks a measure region inside `wiki/`.** Rule 11 walks the harness sweep alone.

# Implemented 2026-08-26, and this page takes `status: implemented`

**`scripts/vault-measure.py` exists with all three modes and all five refusals**, proved by 59 cases
in `scripts/vault-measure-selftest.py` — `caught 59, missed 0`. **The live page carrying the claim is
[[vault-measure-py]]**, and it is what a reader goes to now.

**All three open items above were closed by the build.** A destination naming a page nothing answers
is one of the five refusals; **rule 11 recognises a measure marker**; and **rule 15 of
`scripts/vault-check.sh` is what reaches a measure region inside `wiki/`**
([[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]).

**The cost estimate in the section above is wrong by a factor of eight, measured.** *"Roughly four
minutes to the suite"* reads **0.28 s per gate run, about 50 seconds over the suite** — and the
figure it was extrapolated from omitted the interpreter search and the spawned process
([[a-cost-measured-on-a-script-is-not-the-cost-it-adds-to-what-runs-it]]). **The paragraph is left as
written**, because it is what the owner was asked to accept
([[the-gate-rule-is-built-before-the-scanner-exclusion-and-the-cost-is-accepted]]).

**One thing is built and unexercised: `--refresh` has never written a number outside a fixture**,
because no measure region exists in the corpus yet. That is a population of zero, not a gap in the
build.

**It is not `deprecated` and carries no `superseded_by:`.** An implemented proposal was never false
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]],
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
