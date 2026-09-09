---
title: "A generated harness map, built by a script from the settings file and the hook files"
type: proposal
status: current
authority: harness-map-generation
basis: human
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md"]
decided_by: [[the-fog-finding-is-recorded-and-not-acted-on]]
tags: [harness, vault, process]
---

# The design, offered 2026-08-20 and not built

**One file, built by a script from `.claude/settings.json` and the hook files it names**, saying
what stands around a session: which events are registered, which script each one runs, what each
script does, and which of them are libraries registered nowhere.

**It cannot go stale, because it is generated from the tree it describes** — the same idiom this
project already uses for a rule rendered into the file it governs, and for the page list that is a
query rather than a file of rows ([[the-harness-is-compiled-not-maintained]],
[[the-page-list-is-a-query-not-a-generated-file]]).

**It is offered against a measured failure**: the owner cannot see the harness in any of the four
directions it was offered in ([[the-harness-is-no-longer-visible-to-its-owner]]).

# What it would take

- **a generator**, in the same family as `scripts/vault-inject.sh`, reading the settings file and
  the scripts it points at ([[vault-scripts]]);
- **a destination**, which is a governed file and therefore inside the region-or-generation
  accounting the sprint's criterion counts
  ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]);
- **a decision about hand-edits**, since a generated file is deleted and rewritten by its own marker
  ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

# What is open, and the first item is not a build question

**The language.** Everything durable here is English by rule, and a map exists to be read by the
owner. Whether this artefact is the exception is a rule change and therefore his; nothing should be
built until it is answered, because the answer changes what is generated
([[migrating-the-repository-to-english]]).

**Whether a map is the right instrument at all.** The second repair offered that night was a session
that builds nothing and only makes the existing visible — no artefact, no maintenance, and nothing
that survives the session. Both were declined for the night and neither was refused
([[the-fog-finding-is-recorded-and-not-acted-on]]).

**What it would oblige:** one more generated file in the governed set, and one more thing that goes
wrong quietly if its generator stops being run — which is what the injector's own check exists for
and what a new generator would owe a case in the selftest
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
