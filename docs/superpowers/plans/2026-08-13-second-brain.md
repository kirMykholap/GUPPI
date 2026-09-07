# Second Brain Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: `superpowers:executing-plans`. Steps use checkbox
> (`- [ ]`) syntax for tracking.
>
> **This plan overrides the writing-plans default of subagent-driven execution.** `CLAUDE.md`,
> section «How a slice is executed», says the code is written in the main session against the
> plan, with one independent reviewer per task and the review cycle kept whole. That rule was
> measured and it wins here.

**Goal:** Replace the 129 KB `docs/HANDOFF.md` with a vault of compiled knowledge, a librarian
subagent that reads it, and a brief that is generated at the end of each session and injected at
the start of the next.

**Architecture:** Three layers — `vault/raw/` holds immutable session journals, `vault/wiki/`
holds atomic compiled pages in four categories, `vault/CLAUDE.md` is the schema. One subagent
(the librarian) is the only writer of the wiki and the only reader that sees it whole. Two entry
points: a brief generated at session end and `cat`-ed by a `SessionStart` hook, and a topic query
callable mid-work by the owner or by an agent. Retrieval is `ripgrep` plus `[[wikilinks]]`; there
is no vector index in this phase.

**Tech Stack:** Markdown, YAML frontmatter, `ripgrep`, Claude Code agents / skills / hooks,
PowerShell for the hook command, git.

**Spec:** [`docs/superpowers/specs/2026-08-13-second-brain-design.md`](../specs/2026-08-13-second-brain-design.md).
Section references below (§n) are to that document.

## Global Constraints

- **English for everything written into the repository** — the vault, the schema, the agent and
  skill definitions, commit messages, this plan. Russian only for chat with the owner and for
  product content the owner sees (the web page, CLI output). `CLAUDE.md`, «Language».
- **Add no new dependencies** — neither Python packages nor npm. Nothing in this plan needs any:
  `ripgrep` ships with Claude Code, PowerShell ships with Windows, git is already here.
- **Line width 100** for prose in markdown. Do not run `ruff format` over `docs/` or `vault/` —
  it reports noise on markdown code blocks.
- **`vault/` is entirely tracked in git** (§16). `.superpowers/sdd/` stays git-ignored.
- **Never delete text from a vault page** (§6, §11). A page is retired by setting
  `status: deprecated`, adding `superseded_by:`, and moving it to `vault/archive/`.
- **The wiki has exactly one writer, the librarian.** No task in this plan adds a second.
- **The Python test suite must stay green.** No task here touches `src/` or `tests/`, so
  `uv run pytest -q` should be unaffected; Task 10 is the only task that edits `CLAUDE.md`, and
  it edits prose only.

## How verification works in this plan

This plan builds markdown, agent definitions and hooks — not Python. There is no `pytest` for a
wiki page. The TDD cycle is kept, with a shell check standing where a unit test would:

1. write the check and run it, **see it fail**;
2. do the work;
3. run the same check, **see it pass**;
4. commit.

Every check below is a command whose output you can read. Where the deliverable is judgement
work — the wording of a compiled page — the check verifies structure (fields present, links
resolve, no duplicate `authority`) and the **acceptance questions of Task 4** verify the content.

---

### Task 1: Vault skeleton and schema

**Files:**
- Create: `vault/CLAUDE.md`
- Create: `vault/index.md`
- Create: `vault/tags.md`
- Create: `vault/log.md`
- Create: `vault/raw/handoffs/.gitkeep`
- Create: `vault/wiki/decisions/.gitkeep`, `vault/wiki/concepts/.gitkeep`,
  `vault/wiki/entities/.gitkeep`, `vault/wiki/lessons/.gitkeep`
- Create: `vault/archive/.gitkeep`
- Create: `scripts/vault-check.sh`

**Interfaces:**
- Consumes: nothing.
- Produces: the directory layout of §10, and `scripts/vault-check.sh` — the structural check every
  later task re-runs. It exits non-zero on any violation and prints one line per problem.

- [ ] **Step 1: Write the failing check**

Create `scripts/vault-check.sh`:

```bash
#!/usr/bin/env bash
# Structural checks over vault/. Exits 1 and prints one line per violation.
# Run: bash scripts/vault-check.sh
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
fail=0
note() { echo "VAULT-CHECK: $*"; fail=1; }

# 1. Layout exists
for d in vault/raw/handoffs vault/wiki/decisions vault/wiki/concepts \
         vault/wiki/entities vault/wiki/lessons vault/archive; do
  [ -d "$d" ] || note "missing directory: $d"
done
for f in vault/CLAUDE.md vault/index.md vault/tags.md vault/log.md; do
  [ -f "$f" ] || note "missing file: $f"
done

# 2. Every wiki page carries the required frontmatter fields
while IFS= read -r page; do
  for field in title type status created sources tags; do
    grep -q "^${field}:" "$page" || note "$page: missing frontmatter field '$field'"
  done
done < <(find vault/wiki -name '*.md' 2>/dev/null)

# 3. type must agree with the folder it sits in (§11)
while IFS= read -r page; do
  folder=$(basename "$(dirname "$page")")      # decisions|concepts|entities|lessons
  want=${folder%s}                              # decision|concept|entitie|lesson
  [ "$want" = "entitie" ] && want=entity
  got=$(grep -m1 '^type:' "$page" | sed 's/^type:[[:space:]]*//')
  [ "$got" = "$want" ] || note "$page: type '$got' disagrees with folder '$folder'"
done < <(find vault/wiki -name '*.md' 2>/dev/null)

# 4. No two current pages claim the same authority (§11)
dupes=$(grep -h '^authority:' $(find vault/wiki -name '*.md' 2>/dev/null) 2>/dev/null \
        | sort | uniq -d)
[ -z "$dupes" ] || note "duplicate authority among current pages: $dupes"

# 5. Every [[wikilink]] resolves to a page that exists somewhere in the vault
while IFS= read -r link; do
  find vault -name "${link}.md" | grep -q . || note "broken wikilink: [[${link}]]"
done < <(grep -rho '\[\[[^]]*\]\]' vault --include='*.md' 2>/dev/null \
         | sed 's/^\[\[//; s/\]\]$//' | sort -u)

[ "$fail" -eq 0 ] && echo "VAULT-CHECK: ok"
exit "$fail"
```

- [ ] **Step 2: Run it to verify it fails**

```bash
bash scripts/vault-check.sh
```

Expected: several `VAULT-CHECK: missing directory: …` lines and exit status 1, because nothing
exists yet. Confirm with `echo $?` printing `1`.

- [ ] **Step 3: Create the layout**

```bash
mkdir -p vault/raw/handoffs vault/wiki/decisions vault/wiki/concepts \
         vault/wiki/entities vault/wiki/lessons vault/archive
for d in vault/raw/handoffs vault/wiki/decisions vault/wiki/concepts \
         vault/wiki/entities vault/wiki/lessons vault/archive; do
  touch "$d/.gitkeep"
done
```

- [ ] **Step 4: Write `vault/CLAUDE.md` — the schema**

This is the single source for the rules of the store (§6, §10). The librarian's definition points
at it and must not restate it. Content, verbatim:

````markdown
# Vault schema

This vault is the project's compiled knowledge. Raw session journals arrive in `raw/handoffs/`;
the librarian compiles them into atomic pages under `wiki/`. Obsidian reads this directory; the
librarian writes it. **The librarian is the only writer of `wiki/`.**

## Layout

| Path | What it is |
|---|---|
| `raw/handoffs/` | session journals as they were written. **Immutable** — read, never edited |
| `wiki/decisions/` | what we chose, when, why, what we rejected, what it obliges |
| `wiki/concepts/` | how something is built and why it works that way |
| `wiki/entities/` | what exists and what it is like — modules, tools, external systems |
| `wiki/lessons/` | what we learned the hard way — failure classes, costs |
| `archive/` | deprecated pages, and the handoffs of closed sprints |
| `index.md` | map of the territory: categories, naming, current sprint, hub pages |
| `tags.md` | the tag dictionary — definitions and aliases |
| `log.md` | the librarian's actions, and misses reported against it |
| `sprint.md` | the current sprint — goal, acceptance criteria, changes to the goal; and closed ones |
| `brief.md` | derived. Regenerated at every ingest. **Never a source** |

## Choosing a category

- `concepts` describes the **product**; `lessons` describes **us, working on the product**.
- A `decision` has a date and a rejected alternative. A `concept` has neither.
- An `entity` is a noun with properties. A `concept` is a mechanism with consequences.
- Deferring something is a **decision**: it has a date, a reason and a rejected alternative
  ("do it now"). It goes in `decisions/`, not into a category of its own.
- A measurement is not a page. The number lives on the `lessons/` page it justifies, marked
  `basis: measurement`. A bare number without its conclusion is useless; a conclusion without its
  number is unfalsifiable.

## Page schema

One entity or one decision per file. `kebab-case` filenames, descriptive — **the filename is part
of the search surface**, because retrieval is `ripgrep` plus links.

```yaml
---
title: "The batch finaliser has exactly one owner"
type: concept              # decision | concept | entity | lesson — must match the folder
status: current            # current | deprecated
authority: batch-finalisation   # the question this page alone answers. Optional
basis: code                # human | code | measurement | external | inference
sprint: S1                 # where it came from, NOT what it belongs to
created: 2026-08-13
sources: ["[[handoff-2026-08-13]]", "docs/superpowers/plans/2026-08-06-shell-and-two-pages.md"]
tags: [collection, batches]
supersedes: [[old-page]]        # on a successor only
superseded_by: [[new-page]]     # on a retired page only
---
```

### `status` and supersession

Two statuses only. Supersession is a **relation**, not a status. When a page is replaced:

1. write the successor with `status: current` and `supersedes: [[old-page]]`;
2. set the old page to `status: deprecated`, add `superseded_by: [[new-page]]`;
3. move the old page into `archive/`.

**The link is written in both directions on purpose.** Obsidian shows a human the backlink, but
the librarian greps: a deprecated page that does not name its successor is a dead end.

**Nothing is ever deleted.** An entity taken out of service — a module cut, a tool replaced — is
deprecated, not removed. "Why did we move away from X" is a legitimate question six months later.

### `authority`

The question a page is the **sole** answer to — a slug, not an enum. Pages that do not claim sole
ownership of a question simply omit it. Two `current` pages carrying the same value are a
contradiction, found mechanically:

```
rg "^authority:" vault/wiki -o | sort | uniq -d
```

### `basis`

What the page rests on. It ranks conflicts without the librarian overstepping: a page on
`inference` cannot argue with a page on `human`; a page on `code` loses to the code itself.

| value | meaning |
|---|---|
| `human` | the owner decided it in conversation |
| `code` | it follows from code and tests, and is verifiable by reading them |
| `measurement` | a number obtained by measuring |
| `external` | an article, vendor documentation, upstream behaviour |
| `inference` | the librarian concluded it. The weakest; re-check before relying on it |

### `sprint`

**Origin, not membership.** A page about batch finalisation is not "sprint 3's" — it is timeless
and merely entered the vault in sprint 3. If the field meant membership, a query about the
current sprint would return only recent knowledge and older invariants would be forgotten.

## Tags

Categories are static and few — *what kind* of knowledge. Tags are dynamic and many — *what it is
about*. A page has exactly one category (its folder) and **2–4 tags**. A page with ten tags is not
classified, it is smeared.

**Consult `tags.md` before minting a new tag.** If an existing tag fits, use it. When you consider
a new tag and reject it in favour of an existing one, **record the rejected word as an alias** —
it is what a future grep will hit, and it is how a question asked in Russian reaches an English
page.

## Contradictions

If two `current` pages claim the same `authority`, mark **both** with

```markdown
> [!CAUTION] CONTRADICTION
> Also claimed by [[other-page]]. Unresolved.
```

and raise it in the brief. **Do not choose a winner.** Deciding which of two rules is the real one
is a judgement about the project, not about the store. Asking the owner in chat is welcome but is
not sufficient: an answer given in chat leaves no artefact. The marking is the artefact.

## What does not belong here

- Rules that are *enforced* by tests or that must be obeyed before anyone would think to ask —
  those stay in the repository's own `CLAUDE.md`.
- Task status. The task tracker owns that. The vault owns what we *learned* from a task.
- Anything git already records better: file lists, diffs, commit history.
````

- [ ] **Step 5: Write `vault/index.md` — the map**

`index.md` is a map of the territory, not a catalogue of pages (§12). It must not grow when pages
are added. Content:

```markdown
# Index — map of the vault

Retrieval is **`ripgrep` first, then `[[links]]`**. You do not need to find every relevant page,
only one, and walk from there. This file exists for what grep cannot supply.

## Categories

| Folder | The question it answers |
|---|---|
| `wiki/decisions/` | what we chose, when, why, what we rejected, what it obliges |
| `wiki/concepts/` | how it is built and why it works that way |
| `wiki/entities/` | what exists and what it is like |
| `wiki/lessons/` | what we learned the hard way |

Full rules in [`CLAUDE.md`](CLAUDE.md).

## Naming

`kebab-case`, descriptive, no dates in the filename. The filename is part of the search surface.

## Current sprint

**None declared.** Until a sprint is opened, `sprint:` on new pages is `S0`.

## Hub pages

_None yet — added as subjects grow large enough to need an entry point._
```

- [ ] **Step 6: Write `vault/tags.md` and `vault/log.md`**

`vault/tags.md`:

```markdown
# Tag dictionary

Consult before minting. If an existing tag fits, use it; if you reject a candidate word in favour
of an existing tag, record the rejected word as an **alias**.

`/lint` flags: a tag on more than ~15–20 pages (split candidate), a tag used nowhere (dead), two
tags with near-identical definitions (merge candidates).

## Tags

_Empty. Filled at the first ingest._

<!-- Entry shape:
- tag: page
  definition: a page of the application's web interface (/vacancies, /collection) — not a wiki page
  aliases: [страница, screen, view, ui-page]
  since: 2026-08-13
-->
```

`vault/log.md`:

```markdown
# Librarian log

Append-only. Entries are grouped under a `## YYYY-MM-DD` heading, and **each entry is one line
beginning with its kind**, so the log stays greppable:

```
- ingest: <what was read; what was created, updated, deprecated, and why>
- miss: <what the brief or an answer failed to supply, and where it surfaced>
- measure: brief=<bytes>
- lint: <findings>
```

A `miss` is reported by a session through section 7 of its handoff and transferred here by
`/ingest`. A working agent never writes to this file directly — the vault has one writer.

---
```

- [ ] **Step 7: Run the check to verify it passes**

```bash
bash scripts/vault-check.sh; echo "exit=$?"
```

Expected: `VAULT-CHECK: ok` and `exit=0`. The frontmatter, `type` and `authority` checks pass
vacuously — there are no pages yet — which is correct at this point.

- [ ] **Step 8: Commit**

```bash
git add vault scripts/vault-check.sh
git commit -m "feat(vault): the store gets a shape and a schema before it gets any knowledge"
```

---

### Task 2: Compile `decisions/` and `concepts/` from the existing handoff

**Files:**
- Create: `vault/wiki/decisions/*.md`, `vault/wiki/concepts/*.md`
- Modify: `vault/index.md` (hub pages, if any subject earns one)
- Modify: `vault/tags.md` (the first tags)
- Modify: `vault/log.md` (one ingest entry)
- Read only: `docs/HANDOFF.md`, `CLAUDE.md`

**Interfaces:**
- Consumes: the schema written in Task 1.
- Produces: the product half of the corpus. Task 4's acceptance questions are answered from these
  pages; Task 10 deletes the `CLAUDE.md` prose that these pages replace.

**Scope note — why this task lists inventory rather than page text.** Authoring forty pages inside
a plan would put the deliverable in the plan. What the plan owes you is the *inputs*: which source
section becomes which page, what question each page is authoritative for, and one fully worked
example to fix the house style. That is what follows.

- [ ] **Step 1: Run the check and record the starting state**

```bash
bash scripts/vault-check.sh; echo "exit=$?"
find vault/wiki -name '*.md' | wc -l
```

Expected: `ok`, `exit=0`, and `0` pages.

- [ ] **Step 2: Read the source and write the inventory**

Read `docs/HANDOFF.md` sections 0.2–0.5, 1, 3, 4, 5–5е, and `CLAUDE.md` sections «Boundaries
enforced by tests» and «Invariants worth knowing before editing». Produce
`vault/log.md` inventory lines — one per intended page — before writing any page:

| Source | Page | Category | `authority` |
|---|---|---|---|
| `CLAUDE.md` «Our own JavaScript is allowed…» | `javascript-policy` | decisions | `js-scope` |
| `CLAUDE.md` «How a slice is executed» | `how-a-slice-is-executed` | decisions | `slice-execution` |
| `CLAUDE.md` boundary table | `architectural-boundaries` | concepts | `boundary-tests` |
| `CLAUDE.md` htmx swap-target invariant + the `<script>` strip | `htmx-swap-target-invariant` | concepts | `swap-target-invariant` |
| `CLAUDE.md` «the tag condition is applied once, at the end» | `vacancy-query-tag-condition` | concepts | `tag-condition-placement` |
| `CLAUDE.md` `tags_set` | `tags-set-marker` | concepts | `cleared-chips-vs-fresh-page` |
| `CLAUDE.md` batch finaliser / `open_batch` / `run_source` | `batch-lifecycle` | concepts | `batch-finalisation` |
| `CLAUDE.md` `PAGE_SIZE`, orphan pairs, ordering tie-breaker | `vacancy-list-invariants` | concepts | `vacancy-list-rules` |
| HANDOFF §0.4 decisions taken during slice 2b | one page per decision | decisions | one each |
| HANDOFF §0.3, §5д, §5е review findings that changed a rule | one page per rule changed | decisions | one each |
| HANDOFF §6 «Известные ограничения» | one page per deferral | decisions | one each |
| HANDOFF §1, §3, §5 mechanisms | one `concepts/` page per mechanism | concepts | one each |

Every row must name a distinct `authority`, or the check in Step 5 will fail — which is the point.

- [ ] **Step 3: Write the worked example first**

`vault/wiki/concepts/batch-lifecycle.md`, verbatim, as the house style all other pages follow:

```markdown
---
title: "A collection batch has exactly one finaliser"
type: concept
status: current
authority: batch-finalisation
basis: code
sprint: S0
created: 2026-08-13
sources: ["docs/HANDOFF.md", "CLAUDE.md"]
tags: [collection, batches]
---

# A collection batch has exactly one finaliser

A batch's **normal** end is written by `run_profile` and by nobody else. Adding a second finaliser
to the runner or to the worker thread produces two owners that disagree about the end time and the
status.

Two other closers exist, and they exist only for a process that can no longer speak for itself:
the startup sweep and the staleness rule, both in `ingest/batches.py`. Neither can disagree with
`run_profile`, because `finish_batch` is scoped to `status='running'` — **the first verdict wins**.

Supporting mechanics, which are the reason the rule is not merely tidy:

- one running batch per profile is a **partial unique index**, not a check in code;
- `open_batch` commits on purpose — the worker thread and the CLI live in other sessions, and an
  uncommitted batch is invisible to them;
- `run_source` commits the journal row as `running` **before** the request. That is what makes
  progress observable, and it is also what makes a killed process leave a dangling row, which
  `sweep_interrupted` and `STALE_AFTER` clean up.

See also [[architectural-boundaries]] for the write boundary that keeps batch writes in
`ingest/batches.py`.
```

- [ ] **Step 4: Write the remaining `decisions/` and `concepts/` pages**

Follow the inventory from Step 2 and the style of Step 3. Rules that bind while writing:

- **Copy the reasoning, not just the rule.** The reason this migration exists is that the "why"
  is what gets lost. A page that states a rule without its consequence has failed.
- Every page gets 2–4 tags, and every new tag is added to `vault/tags.md` **with a definition**
  and with any word you rejected in its favour recorded as an alias.
- Link pages to each other with `[[wikilinks]]` as you go. An orphan is invisible to everything
  except an exact grep hit.
- `basis: code` for anything verifiable by reading `src/` or `tests/`; `basis: human` for the
  owner's decisions; `basis: measurement` where a number is quoted.
- `sprint: S0` throughout — no sprint has been declared yet.

- [ ] **Step 5: Run the check to verify it passes**

```bash
bash scripts/vault-check.sh; echo "exit=$?"
find vault/wiki/decisions vault/wiki/concepts -name '*.md' | wc -l
rg "^authority:" vault/wiki -o | sort | uniq -d
```

Expected: `VAULT-CHECK: ok`, `exit=0`, a page count matching the inventory, and **empty** output
from the duplicate-authority grep. If a duplicate appears, two pages are claiming the same
question: merge them or narrow one of the `authority` values — do not silence the check.

- [ ] **Step 6: Record the ingest in the log**

Append to `vault/log.md`:

```markdown
## 2026-08-13

- ingest: migration of docs/HANDOFF.md part 1 — read §0.2–0.5, §1, §3, §4, §5–5е and CLAUDE.md's
  boundary and invariant sections; created N pages in decisions/ and M in concepts/; deprecated
  none, nothing existed to supersede; tags minted <list>; contradictions found <list, or "none">
```

- [ ] **Step 7: Commit**

```bash
git add vault
git commit -m "feat(vault): the product half of the handoff becomes decisions and concepts"
```

---

### Task 3: Compile `lessons/` and `entities/`

**Files:**
- Create: `vault/wiki/lessons/*.md`, `vault/wiki/entities/*.md`
- Modify: `vault/tags.md`, `vault/log.md`
- Read only: `docs/HANDOFF.md` §0.1, §0.6, §6, §7; `CLAUDE.md` «Commands», «Environment», «Tests»

**Interfaces:**
- Consumes: the schema from Task 1, the tag dictionary as Task 2 left it.
- Produces: the process half of the corpus. Acceptance question 2 ("what does an agent round trip
  cost, and where does that number come from?") is answered from `lessons/`.

- [ ] **Step 1: Run the check and record the starting state**

```bash
bash scripts/vault-check.sh; echo "exit=$?"
find vault/wiki/lessons vault/wiki/entities -name '*.md' | wc -l
```

Expected: `ok`, `exit=0`, `0`.

- [ ] **Step 2: Write the inventory**

| Source | Page | Category | `authority` |
|---|---|---|---|
| HANDOFF §0.6 round-trip measurements | `agent-round-trip-cost` | lessons | `agent-round-trip-cost` |
| HANDOFF §0.6 / `CLAUDE.md` «Tests» suite timings | `test-suite-wall-clock` | lessons | `suite-timing` |
| HANDOFF §7 «факт в двух местах расходится» | `duplicated-facts-diverge` | lessons | `duplication-failure` |
| HANDOFF §7 lessons from the visual slice (three, all about the browser walk) | one page each | lessons | one each |
| HANDOFF §7 «Из более ранних срезов» | one page per failure class | lessons | one each |
| `CLAUDE.md` «Environment» Docker Desktop | `docker-desktop` | entities | `docker-startup` |
| `CLAUDE.md` «Environment» cp1252 console | `windows-console-encoding` | entities | `console-encoding` |
| `CLAUDE.md` «Environment» uvicorn / Jinja auto_reload | `app-restart-required` | entities | `restart-to-see-changes` |
| `CLAUDE.md` «Where things are» static assets | `web-static-assets` | entities | `stylesheet-location` |
| HANDOFF §3 «Что где лежит» per module | one `entities/` page per module worth naming | entities | one each |

- [ ] **Step 3: Write the worked example first**

`vault/wiki/lessons/agent-round-trip-cost.md`, verbatim:

```markdown
---
title: "An agent round trip costs 5 to 35 minutes"
type: lesson
status: current
authority: agent-round-trip-cost
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["docs/HANDOFF.md"]
tags: [process, agents]
---

# An agent round trip costs 5 to 35 minutes

Measured during slice 3, which cost a session of eight to ten hours. That slice ran
implementer → review → fix wave → re-review on each of seven tasks; three or four trips per task
**is** the session. The fix wave alone cost 35 minutes once, and 30 more on a task that was then
thrown away.

What the measurement bought: the implementer trip and the fix-wave trip were removed, because
neither buys anything an edit made in the main session does not. Review stayed, and the cycle
stayed whole. See [[how-a-slice-is-executed]].

**The figure describes implementer trips — agents that write code and run tests.** It does not
describe every subagent call. A librarian call, which greps and reads a dozen pages, is tens of
seconds. Reusing this number for retrieval would overstate the cost by two orders of magnitude;
that mistake was made once, on 2026-08-13, and corrected in the second-brain spec.
```

The last paragraph is the point of the whole exercise: the number and **the boundary of its
applicability** travel together, so the next reader cannot misapply it the way it was misapplied
once already.

- [ ] **Step 4: Write the remaining `lessons/` and `entities/` pages**

Follow the inventory from Step 2 and the style of Step 3. Rules that bind while writing:

- **Copy the reasoning, not just the rule.** The reason this migration exists is that the "why"
  is what gets lost. A page that states a rule without its consequence has failed.
- Every page gets 2–4 tags, and every new tag is added to `vault/tags.md` **with a definition**
  and with any word you rejected in its favour recorded as an alias.
- Link pages to each other with `[[wikilinks]]` as you go. An orphan is invisible to everything
  except an exact grep hit.
- `basis: code` for anything verifiable by reading `src/` or `tests/`; `basis: human` for the
  owner's decisions; `basis: measurement` where a number is quoted.
- `sprint: S0` throughout — no sprint has been declared yet.

Two more that apply to these two categories specifically:

- A `lessons/` page must name **the incident that produced it**. A lesson without its incident is
  an opinion.
- An `entities/` page carries the entity's gotchas as properties — for `docker-desktop`, the
  symptom `cannot find the path ... dockerDesktopLinuxEngine` and the `Start-Process` command that
  fixes it, plus "poll `docker info` rather than sleeping blindly".

- [ ] **Step 5: Run the check to verify it passes**

```bash
bash scripts/vault-check.sh; echo "exit=$?"
find vault/wiki -name '*.md' | wc -l
rg -c '\[\[' vault/wiki --include='*.md' | wc -l
```

Expected: `ok`, `exit=0`, the full page count, and the third number close to the second — most
pages should link to something. Pages that link to nothing are orphans, and Task 9's `/lint` will
list them; fixing them now is cheaper.

- [ ] **Step 6: Append the ingest entry to `vault/log.md`, then commit**

```bash
git add vault
git commit -m "feat(vault): the process half of the handoff becomes lessons and entities"
```

---

### Task 4: The librarian, and mode 2

**Files:**
- Create: `.claude/agents/vault-librarian.md`
- Create: `.claude/skills/vault-ask/SKILL.md`
- Create: `docs/superpowers/plans/2026-08-13-acceptance-questions.md`

**Interfaces:**
- Consumes: the corpus from Tasks 2 and 3, the schema from Task 1.
- Produces: the subagent `vault-librarian`, dispatched by `subagent_type: "vault-librarian"`, and
  the skill `/vault-ask`. Tasks 5, 6, 8 and 9 all dispatch the same agent.

- [ ] **Step 1: Write the acceptance questions and their known answers**

Create `docs/superpowers/plans/2026-08-13-acceptance-questions.md`. This is the failing test: the
questions with the answers **we already know**, written down before the librarian exists, so its
answers can be compared against them rather than judged by whether they sound plausible (§9).

```markdown
# Acceptance questions for the librarian

Phase 1 passes if the librarian answers all of these correctly and completely **while the main
session never reads the vault**. The answers below were written from `docs/HANDOFF.md` before the
librarian existed.

## Q1 — Why does the batch finaliser have exactly one owner, and what breaks if a second is added?
Expected: `run_profile` writes the normal end and nobody else; two owners would disagree about the
end time and the status. The startup sweep and the staleness rule are the only other closers, they
exist for a process that cannot speak for itself, and they cannot disagree because `finish_batch`
is scoped to `status='running'` — first verdict wins.

## Q2 — What does an agent round trip cost, and where does that number come from?
Expected: 5–35 minutes, measured on slice 3. **And the boundary**: the figure describes implementer
trips that write code and run tests, not every subagent call.

## Q3 — What has already been decided about JavaScript, and why was the rule narrowed?
Expected: own JS is allowed where it cannot show a wrong list; decided 2026-08-12, replacing "no JS
of our own beyond htmx and the theme toggle". The honest reason: of four silent defects in slice 3,
three were plain test-coverage gaps any architecture would have had; only the stale-chips one was
htmx-shaped. The real cost is that no test here executes JavaScript.

## Q4 — I am rewriting the view in React. What in the documentation helps, and what gets in the way?
Expected: names the JS policy, the two-page shell, the per-page OOB swap-target invariant, the
"no npm" constraint, and the fact that no test executes JavaScript. Must also report the **negative
space**: no decision has been recorded about a framework migration.

## Q5 — <the owner's own question>
_Open. §20 of the spec: his will be more honest than the four above, which were drafted by the
party that already knows what the file contains._
```

- [ ] **Step 2: Write the librarian agent definition**

`.claude/agents/vault-librarian.md`. It is deliberately thin about the store's rules — those live
in `vault/CLAUDE.md`, and restating them here would put them in two places (§6).

````markdown
---
name: vault-librarian
description: Reads and maintains vault/ — the project's compiled knowledge. Answers a topic query with a synthesis plus its sources, or generates the sprint brief. The only writer of vault/wiki/.
tools: Read, Grep, Glob, Bash, Write, Edit
---

# The librarian

You are the only reader that sees the vault whole, and the only writer of `vault/wiki/`.

**First, always: read `vault/CLAUDE.md`.** It is the single source for the rules of this store —
categories, frontmatter, statuses, supersession, tags, contradictions. Do not rely on memory of
those rules and do not restate them anywhere.

## How to search

**Grep first, then follow links.** You do not need to find every relevant page — only one, and
walk from there via `[[wikilinks]]`.

```
rg -il "<term>" vault/wiki
rg -i "<term>" vault/tags.md          # aliases catch synonyms and the other language
```

The corpus is part Russian and part English. If a query in one language returns little, check
`vault/tags.md` for an alias and search again with the tag's canonical term.

Never read the whole vault. If you find yourself opening more than about ten pages for one
question, stop and say what you could not narrow down — that is a miss worth recording, not a
reason to read everything.

## Answering a topic query

Answer in this order, which is the order of the categories:

1. **what already exists** — from `entities/`
2. **what was already decided** — from `decisions/`
3. **how it is built** — from `concepts/`
4. **what will bite you** — from `lessons/`

Then, always, two closing sections:

- **Sources** — the list of pages you used, by path. An answer that cannot be checked is not an
  answer.
- **Not in the vault** — what the vault does *not* have on this topic. "No decision has been
  recorded about a framework migration" tells the caller it is free to decide, and that the
  decision must be recorded. Without this section, "no constraints exist" is indistinguishable
  from "the librarian did not find them".

Synthesise. Never dump page contents.

## Writing

You may create, update and retire pages under `vault/wiki/`, and update `index.md`, `tags.md` and
`log.md`. You do not ask permission; review happens afterwards through `git diff` and the log.

Three rules bound that freedom:

1. **Never delete text.** Append, or retire the page per `vault/CLAUDE.md` — `status: deprecated`,
   `superseded_by:`, move to `archive/`.
2. **Never resolve a contradiction.** Mark both pages and raise it. Choosing between two rules is
   a judgement about the project.
3. **Never close a sprint, and never decide whether a sprint's goal was met.** Report the state;
   the owner decides.

After any write, run `bash scripts/vault-check.sh` and fix what it reports.

## Recording a miss

When a session reports through section 7 of its handoff that the brief or an answer failed to
supply something, append a `miss` entry to `vault/log.md`: what was missing, and where it
surfaced. Those entries are the only test data this system has.
````

- [ ] **Step 3: Write the mode-2 entry point**

`.claude/skills/vault-ask/SKILL.md`:

```markdown
---
name: vault-ask
description: Ask the project's vault a question - what is already decided, built, known or learned about a topic. Use before starting work on an unfamiliar area, before overriding a written rule, and whenever you are about to assume something about this project's history.
---

# Ask the vault

Dispatch the `vault-librarian` agent with the caller's question. Pass the question through
unchanged, and add the caller's plan if there is one — the librarian answers better against a
concrete plan than against a topic.

Use the Agent tool with `subagent_type: "vault-librarian"`.

Relay the librarian's answer to the user in full, including its **Sources** and **Not in the
vault** sections. Do not summarise away the second one: "nothing recorded" is the answer that
tells you that you are free to decide, and that your decision must be written down.

If the librarian's answer is wrong or incomplete and you discover it later in the session, that is
a **miss** — record it in section 7 of the session's handoff. Do not write to `vault/log.md`
yourself: the vault has exactly one writer.
```

- [ ] **Step 4: Run the acceptance questions — the real check**

In a fresh session, or at least without reading any vault page in the main context, ask each of
Q1–Q4 through `/vault-ask`. For each, compare the librarian's answer against the expected answer
recorded in Step 1.

Expected: four answers that contain the substance of the expected ones, each with a Sources list
naming real pages, and Q4 additionally reporting the negative space.

**A failure here is a defect in the corpus or in the agent definition, not in the questions.**
Common causes and their fixes:

| Symptom | Fix |
|---|---|
| the answer misses the boundary in Q2 | the `lessons/` page did not carry it — add it to the page |
| the librarian could not find a page whose subject was obvious | a tag alias is missing, or the filename is not descriptive |
| the answer is a dump rather than a synthesis | the agent definition is being ignored; tighten the wording |
| Q4 has no "Not in the vault" section | same |

- [ ] **Step 5: Record the result**

Append the verdict to `docs/superpowers/plans/2026-08-13-acceptance-questions.md` — for each
question, pass or fail, and what was changed if it failed. This is the record that phase 1 met its
own criterion.

- [ ] **Step 6: Commit**

```bash
git add .claude/agents .claude/skills docs/superpowers/plans vault
git commit -m "feat(vault): a librarian that answers from the vault, and the questions that judge it"
```

---

### Task 5: The handoff template and `/handoff`

**Files:**
- Create: `.claude/skills/handoff/SKILL.md`
- Create: `vault/raw/handoffs/TEMPLATE.md`

**Interfaces:**
- Consumes: nothing from earlier tasks except the layout.
- Produces: `vault/raw/handoffs/YYYY-MM-DD-<slug>.md` — the file Task 6's `/ingest` reads. The
  section numbers below are load-bearing: `/ingest` files section 2 into `entities/`, 3 into
  `decisions/`, 4 into `concepts/`, 5 into `lessons/`, 6 into `decisions/`, and 7 into `log.md`.

- [ ] **Step 1: Write the template**

`vault/raw/handoffs/TEMPLATE.md`, verbatim:

```markdown
---
session: YYYY-MM-DD
sprint: S0
commits: <first>..<last>          # or "none" if nothing was committed
---

# Handoff — YYYY-MM-DD

## 1. State
Done / not done / in flight / next step.
Checks: tests (how many), `ruff check`, `ruff format --check`, browser walk.

## 2. Entities
Appeared | changed | taken out of service (and why).
Entities, not files — Docker, htmx, a module. Git records the files, and records them better.

## 3. Decisions
What we chose | what we rejected | why | what it now obliges.

## 4. How it is built
Mechanisms understood or corrected. Invariants and their consequences.

## 5. Lessons
What burned us, and the incident that produced it. With the number, if there is one.

## 6. Deferred
What we are not doing now | the consequence of not doing it.

## 7. Feedback to the librarian
What the brief failed to supply / contradictions noticed / questions for the owner.

## 8. Anything else worth keeping
```

- [ ] **Step 2: Write the `/handoff` skill**

`.claude/skills/handoff/SKILL.md`:

```markdown
---
name: handoff
description: Write the session journal at the end of a session, from the template, into vault/raw/handoffs/. Use when a session is ending, when work is being handed over, or when asked to write up what happened.
---

# Write the handoff

The handoff is the **only** channel from this session to the librarian, which did not watch it.
Everything the vault will ever know about today is what you write here.

1. Copy `vault/raw/handoffs/TEMPLATE.md` to
   `vault/raw/handoffs/<YYYY-MM-DD>-<short-slug>.md`.
2. Fill the frontmatter. `commits:` is the range this session produced — get it with
   `git log --oneline <first>..HEAD`. The handoff is testimony; git is the evidence, and the range
   is what lets the two be compared.
3. Fill every section. **An empty section is a legal answer — write "none" — but the section must
   stay.** Nobody misses section 7 on their own; it has to be asked.
4. Section 7 is where a librarian miss goes: something the brief should have told you and did not,
   or a rule you broke because nothing warned you.
5. Do not edit an existing handoff. `raw/` is immutable — a correction is a new line in a later
   handoff, not a rewrite of an earlier one. What the session believed at the time is data.

Then run `/ingest`.
```

- [ ] **Step 3: Write this session's handoff, as the check**

Use the skill on the session that is executing this plan. Then verify the shape:

```bash
ls vault/raw/handoffs/
grep -c '^## ' vault/raw/handoffs/2026-*.md
grep -E '^(session|sprint|commits):' vault/raw/handoffs/2026-*.md
```

Expected: one dated file besides `TEMPLATE.md`, `8` sections, and three frontmatter lines with
real values.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/handoff vault/raw
git commit -m "feat(vault): the journal gets a strict template, because it is the only channel in"
```

---

### Task 6: `/ingest`, and the generated brief

**Files:**
- Create: `.claude/skills/ingest/SKILL.md`
- Create (by running it): `vault/brief.md`

**Interfaces:**
- Consumes: the librarian agent (Task 4), the handoff written in Task 5.
- Produces: `vault/brief.md` — the file Task 7's hook prints. Ingest's **last** step generates it;
  nothing else writes it.

- [ ] **Step 1: Verify the brief does not exist yet**

```bash
ls vault/brief.md 2>&1
```

Expected: `No such file or directory`.

- [ ] **Step 2: Write the ingest skill**

`.claude/skills/ingest/SKILL.md`:

````markdown
---
name: ingest
description: Compile the newest handoff into the vault and regenerate the brief. Run at the end of a session, after /handoff. Use when a session is finishing, after writing the journal, or when asked to update the knowledge base.
---

# Ingest

Dispatch the `vault-librarian` agent (Agent tool, `subagent_type: "vault-librarian"`) with the
instruction below. **One source at a time** — never batch several handoffs. Batching loses the
ability to guide what is emphasised, and it is where an auto-maintained wiki starts to rot.

Instruction to pass:

> Ingest `vault/raw/handoffs/<newest file>`. Follow `vault/CLAUDE.md`.
>
> 1. **Split the source into units and give every unit a verdict.** Run
>    `bash scripts/vault-units.sh <source>`; it emits one line per claim — heading, table row,
>    or a paragraph or bullet opening in bold. Write a verdict for each into the sidecar
>    `<source>.coverage.tsv`, one of exactly four:
>
>    | verdict | meaning |
>    |---|---|
>    | `page:<name>` | compiled into that wiki page |
>    | `journal` | session state, not knowledge. Stays in `raw/`, never enters the wiki |
>    | `elsewhere:<where>` | belongs to `CLAUDE.md`, the code, or the task tracker |
>    | `skip:<reason>` | deliberately not compiled, and why |
>
>    **There is no fifth option.** A unit with no verdict is an unfinished ingest, and
>    `bash scripts/vault-coverage.sh <source>` is what says so.
>
> 2. For a handoff written from our own template the mapping is already known and the verdicts
>    follow it: section 1 is `journal` — it feeds the brief and is **never** compiled, being a lie
>    within a sprint — and sections 2→`entities/`, 3→`decisions/`, 4→`concepts/`, 5→`lessons/`,
>    6→`decisions/`. Section 8 is free-form: file what fits, and if it does not fit any category,
>    say so in the log — a section 8 that fills up repeatedly means the template is missing a
>    section. **For any other document there is no such shortcut, and step 1 is the whole
>    method.**
> 3. Where a new page replaces an old one, retire the old one per the schema — `deprecated`,
>    `superseded_by:`, move to `archive/`. Never delete text.
> 4. Where two `current` pages end up claiming the same `authority`, mark **both** with a
>    `> [!CAUTION] CONTRADICTION` block and raise it in the brief. Do not choose.
> 5. Update `index.md` only if a category, the naming rule, the current sprint or a hub page
>    changed. `index.md` is a map, not a catalogue — it must not grow when pages are added.
> 6. Update `tags.md`: new tags with definitions, and rejected candidate words as aliases.
> 7. Append to `log.md`, under today's `## YYYY-MM-DD` heading and one line per entry: an
>    `- ingest:` line (what was read, created, updated, deprecated, and why), an `- miss:` line
>    per item in the handoff's section 7, and an `- measure: brief=<bytes>` line for the brief you
>    generate in step 8.
> 8. **Last: regenerate `vault/brief.md`.** See below.
> 9. Run `bash scripts/vault-check.sh` and `bash scripts/vault-coverage.sh <source>`, and fix
>    anything either reports. **The ingest is not finished while a unit lacks a verdict.**

### The two qualities, which are not the same check

**Coverage** — nothing was dropped. Mechanical, and 100% is required. It works only because the
*denominator* is produced by a script: if the same party both listed the units and accounted for
them, a forgotten section would simply never appear on the list. That is precisely how §1 of the
old handoff was lost on the first pass.

**Fidelity** — what was compiled says what the source said. **No script can check this.** The
Critical found in task 2 would have passed coverage without a murmur: the page existed, its
identifiers matched, and its content was six months out of date.

Fidelity is checked two ways, both cheap: **sampling** — the sidecar records the source line, so
ten random units opened side by side with their pages take ten minutes and give a real verdict on
whether the system lies — and the **acceptance questions**, whose answers are known in advance.
A review agent is for large migrations only.

Run coverage every time. Sample on every ingest. Pay for an agent when a whole document moves.

## The brief

`vault/brief.md` is derived and is **never a source**. If it is wrong, fix the vault or this
skill — never the brief. A hand-edited brief that survives a session is immediate divergence.

Shape:

```markdown
# Brief — <date of the ingest that produced it>

## Alarms
<only if there is one: a contradiction raised, a missing handoff for the previous session,
 or the brief has outgrown its threshold. Otherwise omit the section entirely.>

## Sprint
<read from `vault/sprint.md`, which is the record; do not restate it from memory>
Goal: <text> — or "no sprint declared; open one before starting work".
Acceptance criteria: <list>.
Progress: <closed / open, as the handoff reported it>.

## State
Done / not done / in flight / next step, from section 1 of the newest handoff.

## Active unblocked tasks
<empty until the task tracker is wired in. Quote its output verbatim then — never paraphrase it.>

## What must not be broken
<three to six lines, each linking to the page that explains it. Not the explanations themselves.>

## Hooks for this work
<"if you touch X, ask the vault about Y" — one line per foreseeable subject, from what the
 sprint's state suggests is next.>
```

**If the previous session left no handoff**, say so in the first line of Alarms. A silently
inherited old brief is the worst available outcome.

Keep the brief short. It is read at the start of every session, and its size is the growth signal
that tells the owner a sprint has stopped being one goal.
````

- [ ] **Step 3: Run it — the check**

Run `/ingest` against the handoff written in Task 5. Then:

```bash
ls -l vault/brief.md
git diff --stat vault/
tail -20 vault/log.md
bash scripts/vault-check.sh; echo "exit=$?"
```

Expected: `brief.md` exists and is a few kilobytes; the diff shows the pages that were created or
changed; the log's last entries include one `ingest`, any `miss` entries from section 7, and one
`measure` line with the brief's size; the check passes.

**Read the diff before committing.** This is the review that replaced asking permission: git says
*what* changed, the log says *why*, and a disagreement between them is itself a finding.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/ingest vault
git commit -m "feat(vault): ingest compiles the journal and leaves a brief behind it"
```

---

### Task 7: The `SessionStart` hook

**Files:**
- Create: `.claude/settings.json`

**Interfaces:**
- Consumes: `vault/brief.md` from Task 6.
- Produces: the brief in the context of every new session, without anyone remembering to ask.

Note on file choice: this goes in `.claude/settings.json` — tracked, shared, part of the project —
not `settings.local.json`, which is git-ignored and personal. Hooks from all settings files merge.

- [ ] **Step 1: Verify no hook exists**

```bash
cat .claude/settings.json 2>&1
grep -r '"hooks"' .claude/ "C:/Users/kir/.claude/settings.json" 2>/dev/null
```

Expected: `.claude/settings.json` does not exist, and no `"hooks"` key anywhere.

- [ ] **Step 2: Write the hook**

`.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -NoProfile -Command \"$p = Join-Path $env:CLAUDE_PROJECT_DIR 'vault/brief.md'; if (Test-Path $p) { Get-Content -Raw $p } else { 'No vault brief exists yet. Run /ingest at the end of this session to create one.' }\""
          }
        ]
      }
    ]
  }
}
```

Three things this shape is doing, each deliberate:

- **`cat`, not generation.** The brief is produced at the *end* of the previous session, when the
  owner is still in context and can see it lie. A `SessionStart` hook is a shell command whose
  stdout is injected; it cannot dispatch a subagent, and the alternatives — a headless run or an
  injected "call the librarian first" instruction — both charge a round trip before the first line
  is typed. `cat` is deterministic: it does not fail, does not vary, and costs nothing.
- **`Test-Path` rather than `-ErrorAction SilentlyContinue`.** A missing file must produce a
  helpful line and exit 0, not a PowerShell error that shows up as a hook failure.
- **`compact` in the matcher.** After compaction the context is rebuilt, and the brief is exactly
  what should survive that.

- [ ] **Step 3: Verify it fires — the check**

Start a new session in this project, or run `/clear` in the current one. The brief's text must
appear in the new context.

If it does not, debug in this order: `claude --debug` shows hook execution; check that
`$env:CLAUDE_PROJECT_DIR` resolved (print it from the same PowerShell); check the JSON parses with
`powershell -NoProfile -Command "Get-Content .claude/settings.json | ConvertFrom-Json"`.

- [ ] **Step 4: Commit**

```bash
git add .claude/settings.json
git commit -m "feat(vault): the brief arrives at session start because a hook prints it, not because someone remembered"
```

---

### Task 8: `/pre-task`, and the rule-override guard

**Files:**
- Create: `.claude/skills/pre-task/SKILL.md`
- Create: `.claude/hooks/ask-the-vault.sh`
- Modify: `.claude/settings.json`

**Interfaces:**
- Consumes: the librarian (Task 4), the settings file (Task 7).
- Produces: a mode-2 call before work starts, and an injected reminder when a rule-bearing file is
  about to be edited.

- [ ] **Step 1: Write the `/pre-task` skill**

`.claude/skills/pre-task/SKILL.md`:

```markdown
---
name: pre-task
description: Check a plan against what the project has already decided, before starting work on it. Use before implementing anything non-trivial, and before changing an area you have not touched this session.
---

# Before the task

Dispatch `vault-librarian` (Agent tool, `subagent_type: "vault-librarian"`) with the plan you are
about to carry out, and this question:

> Here is my plan: <plan>. What in the vault contradicts it, and what supports it? List every
> `decisions/` page that constrains this work, and say explicitly if there are none.

**This is a librarian call, not a bulk read.** An earlier draft had the working agent read
`index.md` and every `current` file in `decisions/` itself. That defeats the point: the decisions
register grows monotonically and is never pruned, the read would land in the *main* context, and
it would happen before every task. The librarian reads them in its own context and returns what
matters.

**Why enumeration and not a search.** For this question a ranked partial answer is dangerous — the
decision your plan violates may be twelfth when the search returned eight. Ask the librarian for
the full list of constraining decisions, not for the most relevant ones.
```

- [ ] **Step 2: Write the guard hook**

`.claude/hooks/ask-the-vault.sh`:

```bash
#!/usr/bin/env bash
# PreToolUse guard. Fires when a rule-bearing file is about to be edited and injects a
# reminder to consult the vault first. Advisory: it never blocks.
input=$(cat)
path=$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

case "$path" in
  *CLAUDE.md|*vault/wiki/*|*vault/CLAUDE.md)
    cat <<'JSON'
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "You are editing a file that carries a project rule. Before you weaken, remove or work around a written rule, run /vault-ask about it. All three recorded divergences in this project looked like the rule seemed unnecessary. If you have already consulted the vault, proceed."
  }
}
JSON
    ;;
  *) exit 0 ;;
esac
```

Make it executable:

```bash
chmod +x .claude/hooks/ask-the-vault.sh
```

- [ ] **Step 3: Register it**

Merge into `.claude/settings.json`, alongside the `SessionStart` block from Task 7:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -NoProfile -Command \"$p = Join-Path $env:CLAUDE_PROJECT_DIR 'vault/brief.md'; if (Test-Path $p) { Get-Content -Raw $p } else { 'No vault brief exists yet. Run /ingest at the end of this session to create one.' }\""
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"${CLAUDE_PROJECT_DIR}/.claude/hooks/ask-the-vault.sh\""
          }
        ]
      }
    ]
  }
}
```

The matcher is narrow on purpose. A guard on every edit becomes a ritual performed without
reading; a guard on rule-bearing paths fires exactly where the three recorded divergences happened.

- [ ] **Step 4: Verify — the check**

```bash
echo '{"tool_name":"Edit","tool_input":{"file_path":"c:/PROJECTS/job hunt ai/CLAUDE.md"}}' \
  | bash .claude/hooks/ask-the-vault.sh
echo '{"tool_name":"Edit","tool_input":{"file_path":"c:/PROJECTS/job hunt ai/src/jobhunt/web/app.py"}}' \
  | bash .claude/hooks/ask-the-vault.sh; echo "exit=$?"
```

Expected: the first prints the JSON with `additionalContext`; the second prints nothing and
`exit=0`. Then edit `CLAUDE.md` in a live session and confirm the reminder appears.

- [ ] **Step 5: Commit**

```bash
git add .claude
git commit -m "feat(vault): ask before overriding a rule, and ask the librarian rather than reading every decision"
```

---

### Task 9: `/lint`, the sprint record, and the growth signal

**Files:**
- Create: `.claude/skills/vault-lint/SKILL.md`
- Create: `.claude/skills/sprint/SKILL.md`
- Create: `vault/sprint.md`
- Modify: `scripts/vault-check.sh` (add the tag checks)

**Interfaces:**
- Consumes: the corpus, the librarian, `vault/log.md`'s `measure` entries.
- Produces: the periodic health check, and the sprint record that `/ingest` reads to fill the
  brief's Sprint section.

- [ ] **Step 1: Extend the structural check with the tag rules**

Append to `scripts/vault-check.sh`, before the final `[ "$fail" -eq 0 ]` line:

```bash
# 6. Tag hygiene (§13)
while IFS= read -r t; do
  n=$(grep -rl "^tags:.*\b${t}\b" vault/wiki --include='*.md' 2>/dev/null | wc -l)
  [ "$n" -eq 0 ] && note "tag '$t' is registered but used nowhere"
  [ "$n" -gt 20 ] && note "tag '$t' is on $n pages — split candidate"
done < <(grep -o '^- tag: .*' vault/tags.md 2>/dev/null | sed 's/^- tag: //')

# 7. Every tag used on a page is registered in the dictionary
while IFS= read -r t; do
  grep -q "^- tag: ${t}\$" vault/tags.md || note "tag '$t' used but not in vault/tags.md"
done < <(grep -rh '^tags:' vault/wiki --include='*.md' 2>/dev/null \
         | sed 's/^tags:[[:space:]]*\[//; s/\]//' | tr ',' '\n' | tr -d ' ' | sort -u | grep -v '^$')

# 8. Orphans — a page nothing links to is invisible to everything but an exact grep hit
while IFS= read -r page; do
  name=$(basename "$page" .md)
  grep -rq "\[\[${name}\]\]" vault --include='*.md' || note "orphan page: $page"
done < <(find vault/wiki -name '*.md' 2>/dev/null)
```

- [ ] **Step 2: Run it to see the new checks bite**

```bash
bash scripts/vault-check.sh; echo "exit=$?"
```

Expected: orphan and unregistered-tag lines for anything Tasks 2–3 left loose. **Fix the pages,
not the check.** Every line it prints is a real defect: an orphan page cannot be found, and an
unregistered tag has no definition, which means the next librarian will guess at its meaning.

- [ ] **Step 3: Write the sprint record and its skill**

`vault/sprint.md`:

```markdown
# Current sprint

**None declared.**

<!-- Shape when one is open:

## S1 — <short name>
Opened: YYYY-MM-DD
Goal: <a checkable statement, not a theme>
Acceptance criteria:
1. <observable>
2. <observable>
Milestones: <list>
Closed: —

### Changes to the goal
- YYYY-MM-DD: <what changed and why>
-->

## Closed sprints

_None._
```

`.claude/skills/sprint/SKILL.md`:

```markdown
---
name: sprint
description: Open, inspect or close a sprint. Use when starting a new body of work, when asked what the current sprint is, or at a retrospective.
---

# Sprint

All work happens inside a sprint, and a sprint is **declared explicitly** — not inferred from
merges or branches, because "sprint" must mean what the owner intends rather than what happened to
coincide with a branch.

## Opening one

Ask the owner for a **goal written as a checkable statement**, not a theme. "Improve collection"
cannot be checked; "collection starts from the browser and its progress is visible" can be, by
looking. Then ask for **2–4 acceptance criteria**.

**Write the criteria now, at the opening.** At the end the owner is motivated to close; only
criteria fixed in advance are honest. This project has an instance already: the visual slice's
single criterion was *"has the owner started opening `/vacancies`"*.

Record it in `vault/sprint.md`, incrementing the number. From then on new vault pages carry that
sprint in `sprint:` — meaning **where the page came from**, never what it belongs to.

## Closing one

**Closure is decided on the goal, not on an empty backlog.** Requiring every task closed makes the
sprint a consequence of the backlog rather than a frame for it, and leaves only two outcomes:
closing tasks for form's sake, or a sprint that never ends.

Leftover work is carried over or dropped — and **dropping is a decision with a reason**, so it
becomes a `decisions/` page. That is the payoff: at the retrospective you can see not only what was
done but what you stopped doing and why, which is otherwise lost in silence.

You may report — "goal of S1: …; 7 of 9 epics closed; two open" — and you may record a closure once
the owner declares it. **You never close a sprint yourself**, for the same reason you never resolve
a contradiction.

On closing: move the sprint's handoffs from `vault/raw/handoffs/` to
`vault/archive/sprints/S<N>/`, and move the sprint's block in `vault/sprint.md` to "Closed
sprints".
```

- [ ] **Step 4: Write `/vault-lint`**

`.claude/skills/vault-lint/SKILL.md`:

````markdown
---
name: vault-lint
description: Audit the vault for contradictions, orphans, broken links and tag drift. Run once per sprint, at the retrospective.
---

# Lint the vault

First run the mechanical checks:

```bash
bash scripts/vault-check.sh
for src in vault/raw/handoffs/*.md; do bash scripts/vault-coverage.sh "$src"; done
```

Everything they report is a defect in the vault, never in the check. Fix the pages. A raw document
with unverdicted units is an **unfinished ingest** — finish it before anything else in the audit,
because every later check is being run against an incomplete corpus.

Then dispatch `vault-librarian` (Agent tool, `subagent_type: "vault-librarian"`) with:

> Audit the vault. Report, do not fix, except where the fix is unambiguous.
>
> 1. **Contradictions the greps cannot see** — two pages that disagree in substance while
>    claiming different `authority` values, or none. Mark both with a
>    `> [!CAUTION] CONTRADICTION` block; do not choose a winner.
> 2. **Stale `status: current`** — pages describing something the code no longer does. Check
>    against `src/` where the page's `basis` is `code`; a `code` page loses to the code itself.
> 3. **Concepts missing** — subjects referenced repeatedly across pages with no page of their own.
> 4. **Tag drift** — two tags whose definitions have converged (merge, one becomes the other's
>    alias), and tags whose definition no longer matches how they are used.
> 5. **The brief's growth** — read the `measure` entries in `log.md` and report the trend.
>
> Append the findings to `log.md` as a `lint` entry.
````

- [ ] **Step 5: Calibrate the growth signal — and do not set a threshold yet**

At the **first sprint's retrospective**, and not before:

```bash
grep '^- measure:' vault/log.md
```

Ask the owner one question: **"did the brief get long?"** His answer is the ground truth; the size
is only its proxy, and only he knows when he began skimming rather than reading. Record the size he
called comfortable in `vault/CLAUDE.md`, and from the next sprint the alarm fires at 3–4× it.

**Do not invent a threshold before that measurement.** The spec names two rejected candidates and
why: a flat 4 KB was made up, and "4× the first brief of a sprint" uses a baseline that is
abnormally small because almost nothing has happened yet — a healthy brief would trip it by the
third session, and an alarm that always fires stops being read. Every other number in this project
— 75 s, 250–360 s, 5–35 min — was measured. This one will be too.

- [ ] **Step 6: Commit**

```bash
git add .claude/skills scripts vault
git commit -m "feat(vault): a lint that finds what the greps cannot, and a sprint that ends on its goal"
```

---

### Task 10: Retire the old entry points

**Files:**
- Modify: `docs/HANDOFF.md` — reduced to a journal
- Modify: `CLAUDE.md` — reduced to rules and a map
- Modify: `vault/index.md` — hub pages, now that subjects exist

**Interfaces:**
- Consumes: everything. This task runs **last** and only once Task 4's acceptance questions have
  passed and Task 7's hook has been seen to fire.

**Why last:** `docs/HANDOFF.md` is the current entry point. Shrinking it before the brief works
would leave the next session with neither. The replacement must be demonstrably working first.

- [ ] **Step 1: Verify the replacement works**

```bash
ls -l vault/brief.md
grep -c 'pass' docs/superpowers/plans/2026-08-13-acceptance-questions.md
bash scripts/vault-check.sh; echo "exit=$?"
```

Expected: a brief exists, the acceptance record shows passes for Q1–Q4, and the check is clean.
**If any of these fails, stop.** Do not shrink the old entry points against a system that has not
proved itself.

- [ ] **Step 2: Reduce `docs/HANDOFF.md` to a journal**

Move the file's knowledge — it is already in the vault after Tasks 2 and 3 — and leave a journal:

```markdown
# Handoff

Session journals now live in `vault/raw/handoffs/`, one per session, written from
`vault/raw/handoffs/TEMPLATE.md` by the `/handoff` skill. The brief a session starts from is
generated by the librarian at the end of the previous one and printed by a `SessionStart` hook.

This file is kept as a pointer only. The knowledge that used to live here was compiled into
`vault/wiki/` on 2026-08-13; the pre-migration text is in git history at `f59084c~1`.

To ask what this project knows: `/vault-ask <question>`.
```

Replace `f59084c~1` with the actual commit that precedes Task 2's commit —
`git log --oneline -- docs/HANDOFF.md | head -3` will show it.

- [ ] **Step 3: Reduce `CLAUDE.md` per §17**

The line is **not** "rule stays, reasoning goes":

> A rule stays in `CLAUDE.md` if it must be obeyed at a moment when nobody would think to ask.

**Keep:** the Language rule; Commands; "add no new dependencies"; «How a slice is executed»; the
map of the five AST boundary tests (the table, not the prose explaining each); the Environment
notes that fire before anyone would ask; the Tests section.

**Move out** — the prose is already in the vault as of Tasks 2–3, so this step deletes rather than
rewrites: the "why" under each invariant, the `<script>`-strip explanation, the JavaScript rule's
justification, the `tags_set` rationale, the `build_vacancy_query` explanation.

Each removed block is replaced by one line naming the page that now holds it, for example:

```markdown
| `tests/unit/test_web_boundary.py` | web routes never touch the database directly — all SQL lives in `web/data/` |

Why each boundary exists: `/vault-ask` about `[[architectural-boundaries]]`.
```

Add a short section at the top of `CLAUDE.md`:

```markdown
## Where the rest of the knowledge is

This file holds the rules that must be obeyed before anyone would think to ask. Everything else —
what was decided, how it is built, what exists, what burned us — is in `vault/`, and you get it by
asking: `/vault-ask <question>`. A brief for the current sprint arrives automatically at session
start.
```

- [ ] **Step 4: Verify nothing was lost — the check**

For each block removed from `CLAUDE.md`, confirm a vault page carries it:

```bash
for q in "tags_set" "swap target" "include_unchipped" "finaliser" "JavaScript"; do
  printf '%s: ' "$q"; rg -il "$q" vault/wiki | tr '\n' ' '; echo
done
```

Expected: every term names at least one page. An empty line means knowledge was deleted rather
than moved — restore it from git and write the page first.

Then ask the librarian Q1–Q4 again. They must still pass with `CLAUDE.md` shortened, which is the
real proof that the move was a move and not a loss.

- [ ] **Step 5: Run the full suite**

```bash
uv run pytest -q
uv run ruff check src tests
uv run ruff format --check src tests
```

Expected: green, clean, clean. No task in this plan touched `src/` or `tests/`, so a failure here
means something unrelated — investigate before committing.

- [ ] **Step 6: Commit**

```bash
git add CLAUDE.md docs/HANDOFF.md vault
git commit -m "refactor(docs): the handoff becomes a journal and CLAUDE.md keeps only what cannot wait to be asked"
```

---

## After the plan

Two items the spec leaves open (§19, §20), neither blocking:

- **The owner's own acceptance question** — Q5 in
  `docs/superpowers/plans/2026-08-13-acceptance-questions.md`. His will be more honest than the
  four drafted by the party that already knows what the file contains.
- **The task tracker.** The brief's "Active unblocked tasks" section stays empty until beads is
  installed, then is filled by quoting `bd` output verbatim — never by paraphrasing it.

And one that follows from doing the work: `docs/second-brain-info.md` and
`docs/second-brain-instructions.md` are source material rather than documentation. They belong in
`vault/raw/`, and moving them there is the natural first exercise of the ingest path.
