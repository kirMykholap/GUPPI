---
title: "The probe that measures whether a path-scoped rule reaches a subagent"
type: entity
status: current
authority: delivery-probe
basis: code
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/_probe-paths.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/instructions-loaded.ps1"]
tags: [harness, agents, testing]
---

# What it is made of

Laid at `f552abd` on 2026-08-18. Five artefacts, and they belong together:

| Part | What it is |
|---|---|
| `.claude/rules/_probe-paths.md` | the rule under test, scoped `paths: ["probe/*.md"]`, carrying two nonces |
| `probe/probe-target.md` | a throwaway file that exists to be read and edited; it touches nothing real |
| `probe/RUNBOOK.md` | the four probes, how to run each, and what each outcome decides |
| `.claude/hooks/instructions-loaded.ps1` | writes `probe/instructions-loaded.log` on an `InstructionsLoaded` event |
| the `InstructionsLoaded` block in `.claude/settings.json` | registers that hook |

**The nonces are the instrument.** `PROBE-TEXT-4K7QX2` sits in plain text and `PROBE-COMMENT-9M3ZR8`
inside an HTML comment. Neither is guessable, so *"I can see it"* cannot be confused with *"I
inferred it"* — the failure mode of asking an agent whether a rule loaded
([[an-instrument-that-contains-its-own-answers-can-be-gamed]]).

**Two independent observables, on purpose**: a reader quoting a nonce, and the hook's log. If the
matcher spelling is wrong the hook never fires, and a probe resting on one instrument cannot tell
*the rule did not load* from *I did not measure*
([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]).

# What each probe decides

| Probe | Question | What the outcome decides |
|---|---|---|
| 1 | does the mechanism work at all in the main session | if it fails, nothing else in the list matters |
| 2 | **does it reach a subagent that reads a matching file** | pass: the move proceeds as designed. Fail, fixable only by a line in every subagent brief: the move is off — that is a promise, not a mechanism. Fail, fixable by a hook: build the hook, then move |
| 3 | is an HTML comment in a rules file stripped before the model sees it | whether a *generated, do not edit* banner is free or costs context ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]) |
| 4 | after `/compact`, does Edit demand a re-read | if it does, the compaction question closes: the re-read re-triggers the rule ([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]) |

**It deliberately does not measure** whether the rule fires on creating a new file or on a Bash
command. Both are known not to fire, and spending a restart on a known answer buys nothing.

# Its state, and the two things it costs while it stands

**Inert until Claude Code restarts.** A rules file and a hook are read at session start, so the
session that wrote them cannot see them ([[claude-code-config-loading]], [[app-restart-required]]).

**It is committed rather than left in the working tree**, on the owner's instruction that it be
**archived when spent rather than deleted** — `f552abd` is that archive, and clearing the probe is
therefore a deletion whose history survives ([[raw-holds-testimony-and-artefacts-are-frozen]]).

**`.claude/rules/` is governed the moment it exists.** The directory joined rule 11's swept set with
no script change and nobody editing a list, which was demonstrated live rather than argued: the
coverage advisory moved from `1 of 13` to `1 of 14` when the probe file appeared
([[the-governed-set-is-swept-and-markdown-by-property]]). **While the probe stands, the denominator
reads 14**, and the eight files carrying the old fraction are staler than they were
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**If the probes are never run**, the file sits in the governed set indefinitely and that number
never comes back down — which is the consequence recorded against deferring them, not an argument
about the move.

# What it has returned, 2026-08-19

**A sixth artefact appeared and it is the honest instrument.** `probe/instructions-loaded.log` is
written by the `InstructionsLoaded` hook, is untracked, and grows a line on every path match. It is
uncontaminated by what any reader has seen, which is what makes it the only clean observable for the
first probe — **reading `probe/RUNBOOK.md` to learn how to run the probe hands the reader both
nonces before the measurement starts**
([[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]).

**Three of the four are answered and the answers are in the runbook**: the mechanism works, it
reaches a subagent, and an HTML comment is stripped before either reader sees it. What each result
decides is
[[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]. The fourth needs
`/compact` and is sequenced after the ingest
([[the-compaction-probe-runs-after-the-ingest-and-the-ast-move-waits-on-it]]).

**The runbook gained two corrections to its own method**, both of them contaminations of the
observable it reads rather than errors of fact. They are corrections to a probe's design and they
stand in the runbook; the general shape is on the page named above.

**Clearing it is queued and is not done.** Once the last probe is recorded: delete the probe
directory, `.claude/rules/_probe-paths.md`, the hook and the settings block. `f552abd` is the
archive, so the deletion loses nothing ([[raw-holds-testimony-and-artefacts-are-frozen]]).
**Region coverage reads `1 of 14` for as long as the probe stands.**

# All four are answered, and the condition on deleting it is met — 2026-08-19

**Probe 4 ran and returned against the move.** After `/compact` the Edit proceeds **without a re-read**:
the scoped rule is gone, nothing brings it back, the loss is invisible, and conditional delivery needs a
guard before any real rule moves ([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]],
[[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]]).

**The log is what it rests on, not the session's introspection**, for the reason probe 1 records. Two
lines decide it and neither is something a session could talk itself into: `"load_reason":"compact"` on
the unscoped project memory with **no accompanying `path_glob_match`**, and **no line at all** for the
Edit — the hook never fired, so delivery never fired
([[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]).

**Two things it measured that were not on its list**, and they are the wider finding: delivery is
triggered by the **Read tool** rather than by touching a matching path, and the Edit tool's read gate is
**session**-scoped rather than context-scoped
([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]).

**The runbook's own excusal section is where the assumption hid.** It excused *creating a file* and *a
bare Bash command* as known negatives and **silently assumed Edit was a positive** — which is what made
probe 4 look capable of closing the compaction question rather than opening a wider one.

## Clearing it is now the session's to execute

**`probe/RUNBOOK.md`'s closing paragraph makes deletion conditional on probe 4's answers reaching
`wiki/`, and the ingest of 2026-08-19 is that.** What goes: `probe/`, `.claude/rules/_probe-paths.md`,
`.claude/hooks/instructions-loaded.ps1`, and the `InstructionsLoaded` block in `.claude/settings.json`.
`f552abd` is the archive, so the deletion loses nothing
([[raw-holds-testimony-and-artefacts-are-frozen]]).

**Region coverage returns to a denominator of thirteen when it goes**, and until then it reads `1 of 14`
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]],
[[the-region-coverage-figure-is-dated-where-it-stands]]).

## The teardown is partly executed, and the blocking half is the librarian's — 2026-08-19

**The section above is wrong in one clause and half-executed in the rest.** `f552abd` is **not** the
archive: `sources:` names paths and cannot cite a commit, so twelve citations would have had nowhere
to point. The archive is `job_hunt_ai_vault/archive/`
([[the-archive-gains-a-folder-per-session-inside-the-date]]).

**And the reaching is what forbids the deletion.** Probe 4's answers reached `wiki/`, and the pages
compiled from them cite the scaffolding in `sources:`. Measured at `6bb9a12`: `probe/RUNBOOK.md` on
seven pages, `.claude/rules/_probe-paths.md` on three,
`.claude/hooks/instructions-loaded.ps1` on two ([[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]]).

| Target | State |
|---|---|
| `probe/probe-target.md` | **deleted** — cited in prose and in no `sources:` line |
| `probe/instructions-loaded.log` | **deleted** — same |
| the `InstructionsLoaded` block in `.claude/settings.json` | **removed** — a settings key, not a cited path |
| `probe/RUNBOOK.md` | **stays**, named in `sources:` |
| `.claude/rules/_probe-paths.md` | **stays**, named in `sources:` |
| `.claude/hooks/instructions-loaded.ps1` | **stays and is inert**, named in `sources:` |

**Executed with `bash scripts/vault-check.sh` at exit 0 and 21 advisories before and after,
byte-identical output.**

> **owner:** «удаляй prob обвязку» — 2026-08-19. **The scope was narrowed to what the gate permits,
> and the narrowing is reported rather than asked**
> ([[narrowing-a-scope-notifies-and-widening-it-asks]]).

**What is still blocked needs a ruling and then a rewrite of twelve `sources:` lines**, neither of
which is a session's ([[the-librarian-writes-unattended]]). The ruling owed is **where a machine
artefact lives**: `raw/` holds testimony and freezes artefacts
([[raw-holds-testimony-and-artefacts-are-frozen]]), and neither `raw/handoffs/` nor `raw/notes/` is
a home for a hook log.

**Region coverage did not return to thirteen and will not**, because the fourteenth file is
`.claude/rules/_probe-paths.md`, which stays. It read `1 of 14`, then `1 of 15` once
`.claude/rules/ast-boundaries.md` was generated, and now reads `a region or whole generation covers
2 of 15` under the reworded criterion
([[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]]).

**One consequence of that arithmetic is worth stating plainly**: this probe's scaffolding is now a
permanent member of the governed denominator until the citation rewrite lands.
