---
title: "The `ingested:` line stays a filename, and the hook resolves it wherever the journal now lives"
type: decision
status: current
authority: ingested-line-resolution
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md", ".claude/hooks/session-brief.ps1", ".claude/skills/ingest/SKILL.md"]
tags: [harness, agents, retrieval]
---

# Decided 2026-08-21, when the ingest began archiving what it compiled

**`brief.md` names the journal it was built from by bare filename**, and the `SessionStart` hook
asks of that name exactly one thing: that the file still **exists**. Once `/ingest` archives the
source as its last step, `raw/handoffs/<name>` stops existing the moment the ingest finishes
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]], [[vault-archive-sh]]).

**So the hook resolves the name in both places it can be** — `raw/handoffs/`, and
`archive/*/*/handoffs/`. A check that looked only in the first would have fired on **every** session
start: the alarm class that fires when nothing is wrong, which this file has already removed twice
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]], [[session-hooks]]).

## What was rejected

**Writing the destination path into the line at step 9 of the ingest.** That is a line asserting a
path three steps before the step that creates it, and it goes false whenever the archive fails while
the brief still reads as though it had not — a claim asserted from intention rather than from the
file ([[a-claim-asserted-from-prose-rather-than-from-the-file]]).

## Why a name and not a path

**A filename is an identity and survives the move; where the file lives is a question for whoever is
looking for it.** That is the same property the vault already relies on for a `[[wikilink]]`, which
resolves by filename anywhere under `wiki/` or `archive/` — which is why moving a page between
folders is not a rename ([[a-page-rename-is-sed-and-verify]]).

**The brief's other stamp is unaffected and asks a different question.** `generated-at:` is
provenance a reader can check without git, and it is compared by nothing
([[the-brief-is-stamped-with-its-commit]], [[staleness-checks-run-at-different-times-and-ask-different-questions]]).

## What it obliges

**Nothing may put a path on that line**, and the reason has to travel with the prohibition: the
failure it prevents is silent in the safe-looking direction — the brief reads as correct while the
file it names is somewhere else.
