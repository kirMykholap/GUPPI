---
name: vault-ask
description: Ask the project's vault what is already decided, built, known or learned about a topic. Use before starting work on an unfamiliar area, before overriding or working around a written rule, and whenever you are about to assume something about this project's history.
context: fork
agent: Explore
background: false
---

# Ask the vault

**You are a fork with an empty context.** Nothing of the caller's conversation reached you: what you
have is the question in `$ARGUMENTS` and this file. Read the store, answer the question, and hand
back one report. **You write nothing** — not a page, not a register, not a note.

Everything after this line is the procedure. Follow it in order and stop as soon as you have an
answer worth handing back.

## The question

$ARGUMENTS

**If it names a plan rather than a topic, say so in your report and answer it anyway.** A plan is
answered better than a bare word — but completeness over a plan is what `/pre-task` promises and
this skill does not, and the caller has to know which of the two he got.

<!-- rule: the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault -->
## Start here, every time

**Find the vault.** It is the top-level directory containing a `wiki/`; its name is the name
Obsidian displays and the owner changes it, so never assume one:

```bash
VAULT=$(ls -d */wiki 2>/dev/null | head -1 | sed 's|/wiki$||')
```

**Then read `$VAULT/CLAUDE.md`.** It is the single source for the rules of this store — categories,
frontmatter, statuses, supersession, tags, contradictions. Do not rely on memory of those rules,
and do not restate them anywhere.

## How to search

**Grep first, then follow links.** You do not need to find every relevant page — only one, and
walk from there via `[[wikilinks]]`.

```bash
rg -il "<term>" "$VAULT/wiki"
rg -i "<term>" "$VAULT/tags.md"      # aliases catch synonyms and the other language
```

The corpus is part Russian and part English: the pages are English, and the questions often are
not. **If a query in one language returns little, look up the term in `tags.md` — the aliases exist
for exactly this — and search again with the tag's canonical word.**

`$VAULT/index.md` is a map, not a catalogue. It names the categories, the naming rule, the current
sprint, and hub pages that are entry points into large subjects. Read it when you do not know where
to start; it will not list the page you want.

**Narrow before you open anything.** A full-text grep is the widest possible net and it is already
too wide: at `94483b1`, `rg -il vault "$VAULT/wiki"` matches **116 of 118** pages and `check`
matches 84. Go in this order, and stop as soon as you have a page worth walking from.

**The folder comes first, when the question names its kind.** The five folders are a
classification the search was not using, and they are the cheapest narrowing there is - already
written, free to apply, and never stale:

| the question | the folder |
|---|---|
| what was decided about X, what may I not do | `decisions/` |
| how does X work, why is it built that way | `concepts/` |
| what burned us, what went wrong | `lessons/` |
| what exists, and what is it like | `entities/` |
| what did we plan and never do | `proposals/` |

**If the question does not name its kind, search `wiki/` whole.** A guessed folder is a silent
miss - the page exists, the grep is clean, and nothing tells you that you looked in the wrong half.

```bash
DIR="$VAULT/wiki"                                  # or one folder of it, when the kind is known
rg --files "$DIR" | rg -i "<term>"                 # filenames - they are written to be searched
rg -l "^tags:.*<tag>" "$DIR"                       # then the tag, looked up in tags.md first
rg -il "<term>" "$DIR"                             # full text last, and only if those found nothing
```

**The tag is applied inside the folder, not instead of it.** On its own it stopped narrowing some
time ago: `tags: vault` selects 51 pages at `94483b1`, five times the ceiling below, while the same
tag inside `concepts/` selects 11. `vault-check.sh` now measures tag density per folder for exactly
this reason and names the folder in its advisory.

If a full-text grep returns more than about fifteen files, do not start opening them: go back to
`tags.md` and narrow. That list will keep growing, and the day it stops being eyeball-able is not
announced.

**Never read the whole vault.** If you find yourself opening more than about ten pages for one
question, stop and say what you could not narrow down. That is a miss worth reporting, not a reason
to read everything. **The ceiling is about topic queries.** `/pre-task` asks a different question —
"what constrains this plan" — where a ranked partial answer is the dangerous one; there you
enumerate frontmatter cheaply across every `decisions/` page and open only what the titles
implicate.

<!-- /rule: the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault -->

## Three things the discipline above does not say, and this skill needs

**The catalogue is one command and it no longer prints the archive.**

```bash
bash scripts/vault-catalogue.sh
```

It emits one row per live page — page, `authority`, `title`, `status`, `sprint`, `tags` — for the
six folders and for nothing else. Until 2026-08-30 it also printed every page in `archive/`, 70,535
bytes of the 201,927 it produced, and every reader was told to throw that section away. **Use it
when the question is "what is there at all"**, which is the one question grep cannot answer. Do not
use it as a search: it is an enumeration, and reading it costs about a third of what it used to.

**Walk a page's links with grep, never by opening the page.**

```bash
grep -o "\[\[[^]]*\]\]" "$VAULT/wiki/<folder>/<slug>.md"      # where this page points
grep -rl "\[\[<slug>\]\]" "$VAULT/wiki"                        # what points at this page
```

Both answers arrive without the body entering your context. This is why there is no `Links:` field:
it was designed to cache exactly this and was refused on 2026-08-30, because Obsidian derives the
graph from the body for the human and these two commands derive it for you.

**One `authority:` slug may now be carried by several pages of different types**, and that is the
cheapest way through the store there is:

```bash
grep -rl "^authority: <slug>" "$VAULT/wiki"
```

It returns the whole chain of one question — the proposal that raised it, the decision that settled
it, the concept or entity that describes what was built, the rule that renders it. Two pages of the
**same** type sharing a slug is still a contradiction and the gate says so.

## What you hand back

Four sections, in this order, and none of them is optional.

- **Answer** — what the vault says, in the question's own language. Russian if the question was
  Russian.
- **Sources** — the pages you read, by slug. An answer nobody can check is a rumour with the
  citations missing.
- **Not in the vault** — what the store does not decide. **Never summarise this away.** "Nothing has
  been recorded about X" tells the caller he is free to decide and that his decision has to be
  written down; dropping it turns "we never decided" into "there are no constraints", which reads
  the same and is not.
- **What you could not narrow down** — if you opened more than about ten pages, or a grep returned
  more than about fifteen files and you could not cut it, say so. That is a miss worth reporting,
  not a reason to read more.

**If the vault answered wrong, say it in the Answer section and name where.** You cannot file it
yourself: the feedback channel is a fenced block lifted out of a **displayed message** by a
`MessageDisplay` hook, and a fork returns a result rather than a message. **The caller files it**,
in his own reply, which is what the region removed from this file on 2026-08-30 used to say to a
party that could not act on it.

## Why this is a fork and no longer a dispatch

**It dispatched `vault-librarian` until 2026-08-30.** That agent is the vault's only writer, and
using it to read meant every question paid for a writer's instructions, its gate obligations and its
register permissions before it read a line. The design that replaced it is the store's own, written
2026-08-29 and unbuilt until now: **one search entry point, forked, that finds and reports and
writes nothing — used by everyone, the librarian included.**

**A fork starts empty, and that is the property being bought.** The caller's context is not spent on
the pages read here; only the report comes back. What it costs is that everything the search needs
has to arrive in `$ARGUMENTS`, because nothing else does.

**This was the first `context: fork` in this repository.** The mechanism is documented and, until it
ran here, had never been exercised in this project — so the first few runs are the measurement, and
a report that arrives empty or a fork that cannot see the tree is a finding rather than a mystery.

## How this differs from `/pre-task`, and it is a promise rather than a mechanism

- **`/vault-ask` promises relevance.** The input is a question, the output is the best answer the
  corpus holds, plus its sources, plus what it does not have. Completeness is not claimed.
- **`/pre-task` promises completeness over a scope.** The input is a plan, the output is the full
  list of what constrains it — "say explicitly if there are none" — because the decision a plan
  violates may be twelfth when a search returned eight.

**So this skill is never a substitute for that one.** Asking a good question about a plan feels like
checking it and is not, and the difference only shows up in what was never returned.

## The caller records it

**The row is the caller's to write and cannot be written here** — a fork has no session identifier
and `scripts/record-pre-task.ps1` keys on one. The caller runs it after relaying the report:

```
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/record-pre-task.ps1 -Kind vault-ask -Scope "<the question>"
```

**A `vault-ask` row asserts nothing about the pre-task ritual.** It matches no case in the ledger's
state machine, so it is visible in the record and decides nothing, and its pre-task column reads `-`
rather than `no`. **Running this skill never satisfies the advisory that asks for a `/pre-task`** —
the two answer different questions, and a row that quieted that advisory would be claiming a plan
had been checked when only a topic had been looked up.
