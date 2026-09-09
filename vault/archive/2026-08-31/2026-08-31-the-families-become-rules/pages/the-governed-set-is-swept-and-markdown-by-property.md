---
title: "The governed set is swept rather than listed, and it is markdown by a property"
type: decision
status: archived
authority: governed-set
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh"]
tags: [harness, testing]
---

# What rule 11 governs, and how it knows

**The governed set is swept, never listed**: both `CLAUDE.md` files, and every `*.md` under
`.claude/`. Thirteen files on 2026-08-17, and the number moves on its own as skills are added.

**Rejected: a written list of governed files.** Two lists of one set drift, and this suite had
already lost cases to exactly that — the selftest held its own copy of the vault layout and went
red when `wiki/rules/` arrived ([[a-copied-list-drifts-and-a-sweep-cannot]]). A swept denominator
cannot fall behind the tree, and a file added to `.claude/` is governed the moment it lands.

## `settings.json` and the four `.ps1` hooks are outside it, by a property

They are excluded because **neither syntax admits an HTML comment**. JSON has no comment form at
all; the marker cannot be written into a `.ps1` in a way that survives being read as PowerShell.

**That is a property, not a list of exceptions**, and the distinction is the whole point: a
property is re-evaluated on every run and cannot go stale, while an exemption list is a second copy
of a judgement that nobody revisits. The rule selects `*.md` and the exclusion falls out.

**The `whole` delivery mode is how those files would ever be governed** — the file is rendered
entire, with no hand-written part. It is designed and unbuilt
([[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]), and until it exists those five files
stay outside the mechanism entirely ([[what-the-harness-build-waits-on]]).

## What the sweep obliges

- **The denominator is walked off the sweep's own input list**, not off the files the scanner
  managed to enter — an empty governed file must still be counted
  ([[a-denominator-is-walked-off-the-input-list]]).
- A file that carries no region is an advisory rather than a failure
  ([[a-governed-file-with-no-region-is-an-advisory]]).

## What the sweep does not reach, measured 2026-08-17

**`docs/` is outside the swept set**, and a copy of the handoff mapping was found there by hand: line 13 of
`docs/HANDOFF.md` says *"section 7 of this session's handoff"*, a numbering that stopped existing on
2026-08-17. The sweep that found six copies of that string found them in both `CLAUDE.md`s, three skills, an
agent and the template — and not that one
([[docs-handoff-is-a-pointer-nothing-routes-through]], [[a-copied-list-drifts-and-a-sweep-cannot]]).

**That is a property of the set's definition rather than a defect in the sweep**, and it is the trade this
page describes from the other side: a set defined by a property is complete over the property and silent
outside it. **Whether `docs/` joins is an open question with nobody's decision behind it**
([[what-the-harness-build-waits-on]]).

**Region coverage stands at `1 of 13` at `814472a`**: the repository's `CLAUDE.md` carries nine regions and
the other twelve files carry none ([[a-governed-file-with-no-region-is-an-advisory]]).

## The sweep was demonstrated live, not argued — 2026-08-18

**`.claude/rules/*.md` joined the governed set the moment the directory landed.** The coverage
advisory moved from `1 of 13` to `1 of 14` when a probe file appeared in it, **and nobody edited a
list** — no script changed, no exemption was added, and the file that arrived was not written by the
harness build ([[the-conditional-delivery-probe]]).

**That is the property doing its job in the direction that is hard to test for.** A written list
fails by omission, silently and at the worst moment; a swept set fails, if at all, by including
something nobody meant — which is visible in the very next run
([[a-copied-list-drifts-and-a-sweep-cannot]]).

**The `1 of 13` in the paragraph above is left standing and dated where it is**, under the rule that
a drifting count is dated or deleted rather than renumbered in eight places
([[the-region-coverage-figure-is-dated-where-it-stands]]).
