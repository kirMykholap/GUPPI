---
title: "An instrument that answers half a question in the voice of a whole one, and the acceptance criterion it made undecidable"
type: lesson
status: archived
authority: half-answered-command
basis: code
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md", "scripts/vault-authority.sh", "sprint.md"]
tags: [harness, testing, process]
---

# What happened

**`scripts/vault-authority.sh` dispatched on `case "${1:---list}"`.** So

```
bash scripts/vault-authority.sh --check --binding
```

ran the check, **dropped `--binding` without a word**, exited 0, and printed a report that looked
complete. Nothing was missing from the output except the half that was not run.

**It was found within a minute of that exact command being named as an acceptance criterion's
decider.** The command was run once to confirm it worked; the `--binding` figures were simply absent.

**So the criterion was undecidable for the whole of its life** — about sixty seconds — **and nothing
said so.** A decider that answers half its question reads exactly like a decider whose other half
found nothing to report.

# The class, met from a new angle

**This is the direction of failure this project keeps meeting**: towards *nothing to report*, which
is the output its reader most wants to see and the one nothing about invites a second look
([[an-instrument-that-fails-towards-nothing-to-do]]).

**What is new is the voice.** The earlier instances were instruments that measured wrongly. This one
measured correctly and **spoke as though it had measured more than it did** — the failure is in the
scope of the claim rather than in its content, so re-running it produces the same clean answer
([[a-claim-labelled-measured-came-from-an-instrument-reporting-its-own-exit-code]],
[[an-argument-can-be-true-of-one-surface-and-silent-about-another]]).

**A shell `case` on `$1` is the mechanism**, and it is silent by construction: every argument after
the first is simply never looked at, so there is no branch where an unread flag could be reported.

# The repair, and the shape of it

**A loop over the argumentless modes, with the exit code the worst of those run rather than the
last.** Taking the last would reintroduce the same defect one layer down — a red check followed by a
green count would exit 0 ([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]],
[[a-non-zero-exit-from-the-gate-no-longer-names-one-event]]).

**The operand-taking modes keep single dispatch and refuse anything after them.** `--near <slug>` and
`--group <name>` consume their argument, so a trailing flag there is a usage error rather than a mode
to run ([[the-gate-exits-on-a-usage-error-with-a-code-of-its-own]]).

# What it says about naming a command as a decider

**A criterion decided by a command inherits that command's silences.** The pattern this project uses
— *name the command, not the number* — removes the need to trust a document and replaces it with the
need to trust an instrument ([[a-sprint-closes-on-its-goal]],
[[measurement-settled-what-argument-could-not]]).

**The cheapest guard is the one that worked here: run the decider once, on the day it is named, and
read its output against what the criterion asks.** That is what caught this, and it is a minute
([[hand-probe-a-new-mechanism-before-running-the-suite]]).

# The repair itself widened an approved scope

**It was made without asking**, because the criterion the owner had just set was otherwise
undecidable ([[an-approved-scope-was-widened-by-a-step-that-was-forced-rather-than-chosen]],
[[narrowing-a-scope-notifies-and-widening-it-asks]]).

*(Compiled from `raw/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md`.)*
