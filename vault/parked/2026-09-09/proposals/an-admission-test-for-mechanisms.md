---
title: "An admission test for mechanisms, mirroring the one built for pages, and no verdict was given"
type: proposal
status: current
authority: mechanism-admission
basis: measurement
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-a-claim-is-looked-up-before-a-page-is-written/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md", "scripts/vault-authority.sh"]
decided_by: [[the-harness-versus-product-split-is-recorded-and-not-acted-on]]
tags: [harness, process, vault]
---

# The figure that produced the question

**Since 2026-08-12 there are 119 commits, 95 of them touching `.claude/`, `scripts/` or the vault,
and none touching `src/`.** The product has not moved in nine days. The owner asked how the work can
move onto what matters rather than being permanent repair, and was shown that figure.

**Not all of it is drift.** Product work deliberately does not interleave into this sprint
([[product-work-does-not-interleave-into-the-vault-sprint]]). What the figure supports is narrower:
the harness admits mechanisms the way `/ingest` used to admit pages — by default.

# The proposal, raised by the session

**A mechanism earns its place only where something concrete was measurably blocked without it**, and
**a decision naming a mechanism must also name what keeping it costs.** It is the shape of the
admission rule taken for pages the same day, one level up
([[occams-razor-is-the-ground-rule-for-the-vault]],
[[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

**Nothing here budgets for the maintenance surface a mechanism creates.** A hook, a script, a
selftest case and a rule page each have to be kept true afterwards, and the standing evidence is that
they are: five mechanisms were found built and wired to nothing in the same sweep, and a required
field reached into the selftest in two separate waves
([[a-rule-over-every-page-makes-every-test-fragile]]).

# **No verdict was given**, and the reason to record it anyway

**The owner did not answer.** It is on the sprint's next list as a discussion, together with the five
unwired mechanisms and the question of whether a hook should refuse rather than advise
([[advisory-is-the-default-for-a-hook]]).

**Recorded because the argument was made with a number in front of it**, and a proposal that survives
only in the chat that produced it is the failure this folder exists to prevent
([[chat-is-not-a-channel-that-survives-the-session]]).

# What is open

**Who applies it.** The page admission rule renders into the librarian, which is the party holding
the pen; a mechanism is built by a session, and no ritual in this project reviews a mechanism before
it is built except `/pre-task` — whose own scope is a ruling of the same day
([[the-pre-task-enumeration-covers-every-folder-but-lessons]]).

**And what it would do to what already exists.** The test is stated about admission; nothing was said
about the mechanisms already here, and *retiring* one is a different operation with a different cost.

# The detector this page's *what is open* asks for, designed and not built — 2026-08-21

**An orphan detector: a branch reporting a script, skill or agent that no hook, ritual or agent
names.** It answers the half this page left open — *what it would do to what already exists* — by
making the condition mechanical instead of a sweep somebody remembers to run.

**Its evidence is that the sweep was done by hand and found six.** Every mechanism wired that day
had been built and called by nothing: `scripts/vault-archive.sh`, `/vault-lint`,
`scripts/vault-catalogue.sh`, `/vault-ask`'s trace, the `ingested:` check and the ledger drain that
was cancelled rather than built ([[vault-archive-sh]], [[the-pre-task-ledger]],
[[the-reading-funnel-is-delivered-as-a-procedure]]). **The detector would have printed all six.**

**owner: it waits until the wiring lands.** Recorded and not built, which is why it is here rather
than in `decisions/` — the deferral is one line and the design is what would otherwise be lost
([[proposals-are-a-folder-not-a-status]]).

**Where it would live is not decided.** The cheap form is a branch of `bash scripts/vault-check.sh`,
which already walks the harness for other reasons; the shape of *names it* is the open part, because
a mechanism can be named in prose, in a `governs:` line, in `.claude/settings.json` or in a skill's
body, and only some of those are greppable ([[a-path-detector-for-prose-references]],
[[deletion-keys-on-the-marker-and-nothing-else]]).

**What not building it costs**: the next mechanism built and wired to nothing is found the next time
somebody sweeps by hand, and the last sweep was occasioned by the owner asking a different question
([[the-harness-is-no-longer-visible-to-its-owner]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# Re-measured, and the verdict is *not a criterion* — 2026-08-22

**The figure at the head of this page was taken on 2026-08-21 and reads 119 commits since
2026-08-12, 95 touching `.claude/`, `scripts/` or the vault, and none touching `src/`.** Measured
again on this date, by the session reporting it rather than quoted from a journal:

| | 2026-08-21 | 2026-08-22 |
|---|---|---|
| commits since 2026-08-12 | 119 | **128** |
| touching the harness or the vault | 95 | **107** |
| `src/` last moved | 2026-08-12 | **2026-08-12**, in `e15a12c` |

**Ten days.** The direction is unchanged and the gap has widened by nine commits in one day. The
head figure is not patched: it is a true reading of the day it was taken
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**The instrument is `git log`** over the three paths and over `src/`, which is the same reader both
readings used and is named here because a figure whose instrument is unnamed cannot be re-derived
([[an-unsourced-number-is-dropped-not-chosen]]).

## The verdict this page says was never given

**It has one now, and it is narrow: the admission test is *not* S2's seventh acceptance criterion.**
The criterion the owner took instead is the `authority` index, which is **decided by a command**; an
admission test for mechanisms is decided by a judgement, and that is the ground the swap was made on.
**No criterion's reading is restated here**, which is the owner's alone ([[a-sprint-closes-on-its-goal]]).

**Nothing here refuses the proposal itself.** What was decided is what to do about the split now —
record it and move on ([[the-harness-versus-product-split-is-recorded-and-not-acted-on]]) — so this
page stays `current` and is not retirable: it was neither built nor refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]],
[[the-proposal-status-cannot-tell-built-from-refused]]).

**The orphan detector below is untouched by the ruling** and is still designed, unbuilt and waiting
on the wiring, which landed.
