---
title: "The harness build and its gate, and the ways a rule reaches its destination"
type: proposal
status: current
authority: harness-build-design
basis: human
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
decided_by: [[the-harness-is-compiled-not-maintained]]
tags: [harness, vault, testing]
---

# The mechanism behind the decision, and none of it exists

[[the-harness-is-compiled-not-maintained]] is the decision. This is the design it would take, and
**nothing here is built**: `harness-build`, `harness-gate`, `wiki/rules/` and
`.claude/templates/handoff.md` are all names for things that do not exist on disk.

## Two mechanisms, because there are two different failures

| | what it keeps true | the failure it catches |
|---|---|---|
| **a marked region** | the harness **says** what the vault holds | the ingest skill contradicting the cadence decision ([[ingest-runs-after-handoff-at-the-end-of-a-session]]) |
| **`asserts:`** | the tree **is** what the rule claims | "four types where five folders exist", and a path a file move made false |

Neither subsumes the other, and the two-instrument shape is one this store has arrived at before
([[staleness-checks-run-at-different-times-and-ask-different-questions]], [[fidelity-to-a-source-and-fidelity-to-the-tree]]).

## Four delivery modes, forced by the destination's physical shape

The division is not a taxonomy somebody chose; **remove any one and some file becomes
undeliverable**.

| mode | when | why it has to exist |
|---|---|---|
| `region` | the file is hand-written and only a piece comes from the page | `SKILL.md` and `AGENT.md` are procedures, not projections of knowledge |
| `whole` | the file has no hand-written part at all | **JSON cannot carry a marker because it has no comment syntax** — `settings.json` is rendered whole or not at all |
| `zone` | the destination does not exist yet; the injector creates `<dir>/CLAUDE.md` | this is how a rule reaches a reader **before** the work rather than by search — the property the four rules in the repository's `CLAUDE.md` depend on ([[the-repository-claude-md-becomes-a-dispatch-table]]) |
| `none` | there is no text destination | only the page's `asserts:` reach the tree |

**Region order is given by where the markers already sit**, which answers the standing objection
that many small pages have no natural order.

## One page says what lives where

**`harness-layout`** — a single rule page naming every harness file, carrying the file list in
`asserts:`, so **a harness file nobody described turns the gate red**. That is the answer to the
absence problem a classifier cannot solve
([[a-harness-change-is-recorded-when-it-is-decided]]).

## What it would oblige

- **A closed predicate set first** — [[asserts-is-a-closed-predicate-set-with-a-flat-syntax]].
- **Rules for the regions**, including which files may be exempt from *no region means red* —
  [[marked-regions-and-the-prose-outside-them]].
- **The gate runs at `SessionStart`**, reports into the brief and has a manual entry point; the
  hook is already there ([[session-hooks]], [[the-brief-is-stamped-with-its-commit]]).
- **A `rules` page carries `governs:`, never `authority:`** — a rule issues an instruction rather
  than answering a question, and sharing the slug with its decision would make rule 3 print a
  contradiction on every normal decision-and-rule pair ([[rules-becomes-a-type-of-its-own]]).
- **The gate guarantees agreement, never truth** — [[a-gate-guarantees-agreement-never-truth]].

**The first intended use is real work, not an exercise:** telling the spec-writing skill where to
write its output — a line in `vault-feedback.md`, a rule page, `governs:` on the skill file, a
rendered region, the gate — which is work
[[raw-holds-testimony-and-artefacts-are-frozen]] queued anyway.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

# What of this exists, as of 2026-08-17

`wiki/rules/` is a folder, `scripts/vault-inject.sh` is the injector, and rules 11 and 12 are the
gate. **One of the four delivery modes is built.**

| mode | state |
|---|---|
| `region` | **built** — [[a-region-is-a-paired-comment-named-for-a-rule]] |
| `whole` | designed, unbuilt; it is what would ever govern `settings.json` and the four `.ps1` hooks, which are outside the mechanism because neither syntax admits an HTML comment ([[the-governed-set-is-swept-and-markdown-by-property]]) |
| `zone` | designed, unbuilt |
| `none` | waits on `asserts:`, which is unbuilt ([[what-the-harness-build-waits-on]]) |

**`render:` was not introduced**, so nothing selects between the modes and nothing needs to yet —
one mode, no field ([[render-was-not-introduced]]).

**`harness-layout` does not exist.** The absence problem this page names is unanswered: no page
lists the harness files, so a harness file nobody described still turns nothing red. What exists
instead is the **swept** denominator of rule 11, which reports coverage over the governed set
without asserting anything about what ought to be in it.

**Region order is not given by where the markers sit**, because no markers sit anywhere: the
coverage advisory reads `0 of 13`.

The gate does **not** run at `SessionStart`; it runs when a journal lands
([[the-journal-gate-hook]]) and on demand. And what it guarantees is unchanged
([[a-gate-guarantees-agreement-never-truth]]).

**This page stays `current`** — three of its four modes and its one-page layout register are still
proposals.

# The `whole` mode has a design of its own now — 2026-08-18

**The row above says `whole` is designed and unbuilt. Its first real customer is a
`.claude/rules/` file**, and what that takes — the mode inside `vault-inject.sh`, the generated
marker, the marker-guarded deletion and the regenerate-and-compare check — is
[[generating-a-claude-rules-file-whole-from-its-vault-page]], under the decision
[[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]].

**It is still unbuilt**, and the reason it is being designed now is a single rule's move rather than
the hooks and `settings.json` this row was written about
([[the-ast-rule-moves-to-prove-the-mechanism]]).
