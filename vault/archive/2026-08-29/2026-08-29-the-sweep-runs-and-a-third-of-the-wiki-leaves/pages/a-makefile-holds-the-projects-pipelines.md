---
title: "A `Makefile` holds the project's pipelines, and `## Commands` points at it"
type: proposal
status: archived
authority: makefile-design
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
decided_by: [[the-command-list-moves-into-a-makefile]]
tags: [harness, process, testing]
---

# Designed 2026-08-17 on the owner's decision, and not built

The decision is [[the-command-list-moves-into-a-makefile]]: a `Makefile`, not `scripts/do.sh`.

## What it would take

**The targets are already written down, as four commands in prose and a fifth in the vault's schema:**

| Target | What it runs |
|---|---|
| `test` | `uv run pytest -q` |
| `lint` | `uv run ruff check src tests` and `uv run ruff format src tests` |
| `up` | `docker compose up -d --build` |
| `vault` | **`vault-inject.sh` then `vault-check.sh`, in that order** — the write ritual, which is the one thing prose has never been able to enforce ([[vault-scripts]]) |
| `check` | `lint` then `test` then `vault` |
| `help` | the target list, which is the generator's business rather than a typed comment ([[a-generator-fills-a-marked-region-from-the-tree]]) |

**`make` is not installed in this environment** — Git Bash ships none — so the work includes installing
it, which the owner priced at five minutes and accepted.

## What is open

- **Whether `make vault` may run the injector**, which *writes*. A target that edits tracked files is a
  different kind of thing from one that reports, and this project has a rule about the register write
  ritual but none about a build target performing it
  ([[hand-edits-of-the-wiki-are-a-recorded-divergence]]).
- **Whether the selftest gets a target.** It costs 8m04s and would be the one target nobody runs
  ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).
- **Whether `## Commands` becomes a pointer or a generated region.** A pointer is available today; a
  generated region waits on the generator.

## What not building it costs

**The ordered pipeline stays a thing remembered rather than a thing run.** `inject` then `check` is the
current ritual and it exists only as a sentence in the vault's `CLAUDE.md` and in the librarian's
instructions — and a rule that lives only in prose is the failure this whole sprint is about
([[no-rule-reads-a-harness-file]]).

**And `## Commands` goes on drifting**: its stated `~2 s` for `vault-check.sh` is `4.9 s` measured
([[the-repository-claude-md-after-the-rules-left-it]]).

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

# The owner revived the question and gave it a second job — 2026-08-26

> **owner:** «И да, делаем единую точку входа. Мы когда-то обсуждали make. Можем воскресить вопрос.»

**The single entry point is decided; whether `make` is the shape of it is reopened rather than
settled** ([[the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate]]).

**The second job is the checks.** `smoke` and `suite` each have to become one command, or naming them
apart buys nothing ([[gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning]]).

**Two facts this page did not have:**

- **`make` is present on this machine** — GNU Make 4.4.1 at `/c/ProgramData/chocolatey/bin/make`, via
  chocolatey, measured 2026-08-26.
- **The no-new-dependencies rule does not reach it.** That rule names Python packages and npm.

**Running "the checks" today is four commands typed by hand, and the fourth is the one somebody
forgets** — which is the gap, stated as a cost rather than as a preference.

**Where it is decided:** the proposal page settling who runs which check and when, ordered as the
next session's first work ([[a-proposal-page-settles-who-runs-which-check-and-when]]).

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*

# It is built — 2026-08-26

**The `Makefile` exists at the repository root and `## Commands` in `CLAUDE.md` is a pointer to
`make help`.** Both halves of this page's title landed on 2026-08-26, nine days after it was written
([[the-makefile]]).

**What the built file has that this page designed:** `test` and `style` targets, and a `## Commands`
that names one command instead of four. **What it has that this page did not design:** `gate`,
`smoke` and `suite`, which came out of the arrangement decided the same day
([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

**What is still not built is this page's own first item — a `vault` target for the injector-then-gate
ritual.** No target in that file writes, and nothing in this project decides that a build target may
perform a ritual that edits tracked files. The ritual stays typed, which this page called the one
thing prose has never been able to enforce.

**`status: implemented` and not `deprecated`.** The design was not replaced for going false; it was
carried out. The page stays in `wiki/` while it is tested for having a live page that names it, and
moves only once it passes
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

## One sentence above is false and is marked rather than removed

**"Retired with `superseded_by:` the day it is built or refused"** — overturned 2026-08-23. A built
proposal takes `status: implemented` and carries no `superseded_by:`, and a refused one takes
`status: refused` and carries `decided_by:` instead
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]],
[[a-refused-proposal-is-archived-and-takes-status-refused]]).

**It is struck by this note and not deleted**, because the sentence records what the rule was when
the page was written ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).
