---
title: "The `pre-task` agent"
type: entity
status: current
authority: pre-task-agent-file
basis: code
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified/handoffs/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified.md", ".claude/agents/pre-task.md", ".claude/hooks/pre-task-state.ps1"]
tags: [agents, harness, process]
---

# What it is

**`.claude/agents/pre-task.md` — the ritual as a body rather than as a mask.** It appeared on
2026-08-22 and it is how `/pre-task` is performed from that date: the caller dispatches
`subagent_type: "pre-task"` and there is no other way to do it, because
`.claude/skills/pre-task/` was deleted the same day
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]], [[a-skill-is-a-mask-and-a-subagent-is-a-body]]).

| property | value |
|---|---|
| `name:` | `pre-task` |
| `tools:` | `Read, Grep, Glob, Bash` — **no write tool** |
| `color:` | `cyan` |
| rendered region | the shared reading discipline ([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]) |

# The name is coded, not conventional

**`.claude/hooks/pre-task-state.ps1` reads the literal string `'dispatch:pre-task'`**, and
`Read-LedgerState` treats that row and no other as discharging the ritual
([[the-dispatch-record-hook]], [[the-pre-task-ledger]]). **An agent renamed is an agent whose
dispatch discharges nothing** — the row is still written, it simply says something else, and the
gate goes on asking for a ritual that has been performed. That is not a hypothetical: the same
mechanism produced a false positive on this date, when the ritual ran as a `vault-librarian`
dispatch because this file did not exist yet ([[the-plan-check-hook]]).

# Both phases run inside it, and it dispatches nobody

**The enumeration and the reading happen in one body.** The split that lived across the caller and a
dispatched reader is gone, and the reason it had to go is the empty case: when only the reading was
dispatched, a run that found nothing left no dispatch at all, so nothing could tell *checked and
found nothing* from *did not check*
([[the-pre-task-always-dispatches-its-narrow-phase]],
[[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**It writes nothing** — no page, no register, no `log.md`, no feedback file. It holds `Bash` because
phase 1 is a script, and a shell redirect is outside the guards that watch `Edit` and `Write`, so
**the prohibition is the agent's to keep rather than the harness's to enforce**. What it finds it
says in its answer, and the caller records it.

**The two counts come back in the answer and are written by the caller.** How many pages the
shortlist named and how many were opened in full: the agent returns both and writes neither, they
are recoverable from nothing else afterwards, and they travel into the journal through `/handoff`
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

# Its first run, and what it cost

**146,705 tokens, 57 tool uses, 13m36s** — 53 pages shortlisted from 362 filtered rows, **16 opened
in full and 16 in part**, with 2 reached past the `binding:` filter and 5 reached only by link. Read
off the harness's usage report rather than reported by the agent, which cannot see its own cost
([[a-subagent-cannot-report-its-own-cost]], [[agent-round-trip-cost]]).

**Three items in, five corrections out**, and every item it was given came back changed
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

# What it knows about its own blind spot

**Phase 1 keeps only `binding: prohibition` from `decisions/`**, and the agent's own text tells it to
reach past that filter when the plan's subject is a ratified deferral — a clause written on the
session's own finding and **ratified by the owner after the fact rather than before**
([[a-replacement-and-a-widening-were-ratified-after-the-fact]]). **Whether the filter itself stays is
a question for the owner and is on the sprint**, argued for in three places in the corpus and against
in none.

**And phase 1 as written cannot be performed from the catalogue alone.**
`bash scripts/vault-catalogue.sh` prints Page, Authority, Title, Status, Sprint and Tags, and no
`binding:` column, so the agent carries a second `grep` over one folder to get it
([[the-page-list-is-a-query-not-a-generated-file]], [[vault-scripts]]).

# It enumerates `wiki/` and reads none of the registers — 2026-08-23

**`sprint.md`, `tags.md`, `authority.md` and `index.md` are outside everything the agent reads.**
Its enumeration is `bash scripts/vault-catalogue.sh` over the folders, and the catalogue's rows come
from page frontmatter alone ([[vault-scripts]], [[the-page-list-is-a-query-not-a-generated-file]]).

**Measured against one plan on that date, `sprint.md` alone held 24 open *next* items, seven
acceptance criteria and four owner readings that bear on nine items of the plan being checked.**
None of it is in the catalogue's output, so none of it could reach the answer.

**It cost nothing that day only because the caller named the sprint-level moves explicitly in the
brief** — which is exactly the dependency a ritual exists to remove
([[knowing-a-rule-is-not-a-mechanism]]).

**It is not obviously a defect to repair by adding the registers.** The agent's whole design is a
cheap enumeration narrowing to a narrow dispatch, and `sprint.md` is 82 KB of prose with no
frontmatter to filter on ([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).
What is recorded here is the gap and its size, not a repair.

# Its `binding:` filter widened and its override paragraph went — 2026-08-26

**Phase 1 now enumerates `binding: prohibition` **and** `binding: deferral`, and discards
`divergence` alone.** The prose paragraph telling the agent to reach past the filter by judgement is
deleted; the mechanism replaces the instruction
([[the-pre-task-keeps-deferral-in-phase-one-and-drops-divergence-alone]]).

**The rule region of this file occupies lines 28–102.** Everything the ritual's filter lives in sits
**outside** it, so the filter is a hand-editable part of a governed file and the injector is not
involved — which is why the two edits touched no address verdict
([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]],
[[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

## The run of that day, and the seventh point in the cost series

**Shortlist 116 pages; the agent opened 21 in full and 8 in part, plus two registers and seven tree
files. 179,880 tokens, 16m33s, 41 tool uses.**

**The series now spans 143,840–230,882 tokens and 10m18s–18m50s over seven points**
([[agent-round-trip-cost]]). Points, not a rate.

**And the run reached past its own filter four times, changing three plan items** — every one of the
four a `binding: deferral` page that was the *subject* of an item rather than context for it. That is
the mechanism producing the evidence for the ruling about itself, inside the run that was checking
the plan the ruling appears in.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*

# The run of 2026-08-29, and the obligation it could not see

**The two counts: the shortlist named 123 pages and the agent opened 49 in full, plus 8 in part.**
That is the widest shortlist and the deepest reading either count has recorded here. Against a
forty-item plan it returned **fourteen corrections**, the largest of them a collision between two
items of the same day that neither item's own page could see.

**And it missed the thing that then cost the day.** The obligation that a retired page's slug leaves
`authority.md` before the page moves — a rule the brief carries under *what must not be broken* — was
in none of the forty items and therefore in none of the fourteen corrections. The sweep moved 239
pages, left 239 stale register rows, reddened the gate on every one of them, and
`lock-the-librarian.ps1` then refused to dispatch the only party permitted to repair the register
([[the-librarian-lock-hook]]).

**It is not a defect in the agent: `/pre-task` answers per item of the plan.** An obligation the plan
does not contain is invisible to it, and the repair is on the plan's side
([[a-plan-touching-the-vaults-own-machinery-enumerates-what-must-not-be-broken-as-items]]).

**What the run's corpus lost that day is unmeasured.** The sweep that followed took 65 decisions out
of `wiki/`, including four rulings of 2026-08-28. Their claims survive on the citing pages, but
`binding:` — the field phase 1 filters on — exists only on a decision page, so the enumeration that
answers *what stops this plan* is smaller by that much and nobody has read the difference
([[what-the-pre-task-lost-to-the-decided-by-criterion-is-unmeasured]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# Two runs in one session, and the shortlist scales with the item count while the opened count does not — 2026-08-29

| run | items | shortlisted | opened | tokens | tool uses | wall clock |
|---|---|---|---|---|---|---|
| 2026-08-29, earlier | 11 | 71 | 38 full + 7 part | 185,319 | 50 | 11m19s |
| 2026-08-29, later | 19 | ~120 | 34 full or substantial | 194,447 | 62 | 11m11s |
| 2026-08-29, previous session | 40 | 123 | 49 full + 8 part | — | — | — |

**About 6.5 shortlisted per item on the first two.** The shortlist tracks the item count; **the opened
count does not** — 38, 34 and 49 across plans of eleven, nineteen and forty items.

**An eleven-item plan is not much cheaper than a forty-item one.** 185k against 161k and 143,840 over
earlier plans. **Nothing separates the enumeration's fixed cost from the per-item cost**, and the two
runs above do not isolate it either.

## Both runs paid for themselves, and the second overturned the session's own recommendation

**The first found 239 pages sitting under an archive folder naming no session** — against a prohibition
of 2026-08-19, predicted verbatim on 2026-08-22, and caught by nothing until then. Repaired for one
command and one edit before the commit, against 239 committed paths afterwards
([[the-archive-gains-a-folder-per-session-inside-the-date]]).

**The second killed plan part F as unbuildable and stopped the `decided_by:` widening one step before
it was built** — the widening having been designed by the session, recommended by it, and accepted by
the owner ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]],
[[the-unreachable-verdict-is-dropped-and-replaced]]).

## Two corrections to what the runs reported

**Phase 1 keeps four folders whole.** `.claude/agents/pre-task.md:130` keeps `concepts/`, `entities/`,
`proposals/` and `rules/` **entire** and filters only `decisions/`, at line 118, on
`binding: prohibition` or `deferral`. **The claim that `/pre-task` reads decisions instead of the other
folders is false**; what only `decisions/` carries is `binding:`.

**And one run reported that `make test` has never run in this repository. It has** — 614 passed, exit 0,
133 s on 2026-08-27. The claim came from [[the-makefile]], which records the Docker-down state at the
Makefile's build and was not updated by that reading.

# A third reading, 2026-08-30, and the cost decomposes

| run | items | shortlisted | opened | tokens | tool uses | wall clock |
|---|---|---|---|---|---|---|
| 2026-08-30 | 29 | 62 | 41 | 258,830 | 86 | 15m01s |

**Against 194,447 over nineteen items and 185,319 over eleven**, the three runs give **a fixed part of
about 160,000 tokens and a marginal part of about 3,400 per item.**

**So halving a plan's item count saves about 50,000 tokens, not half.** The fixed part is the
catalogue enumeration over 894 rows, **so the real lever is the size of the corpus and not the size of
the plan.**

**This run made 86 calls at about 3,010 tokens each**, against a measured band of 1,552–2,170 for flat
ingests, because it held 41 fully-opened pages.

# It earned its cost for the third session running, and where the findings came from

**Four of its nine findings were errors in what the session had already told the owner** — including
that `record-the-smoke.ps1` applied no command test on the recording path, which was false: line 59
already carried one and the defect was that it was **loose**, not absent.

**Five of its nine findings came from the TREE and were reachable by no grep of `wiki/`.** That is the
argument for the ritual that no reading of the corpus can replace: the agent reads the machinery, not
only the record of it.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*

# The next reading, and the first one where the ritual cost more than it returned — 2026-08-30, later

| run | items | shortlisted | opened | tokens | tool uses | wall clock |
|---|---|---|---|---|---|---|
| 2026-08-30, the cleanup plan | 6 phases | 96 | 36 full + 8 registers and schemas + 9 files of the tree | 211,755 | 47 | 14m01s |

**It sits below the line the decomposition on this page predicts.** A fixed part of about 160,000
tokens plus roughly 3,400 per item predicts about 259,000 for twenty-nine items, and this run — a plan
of six phases touching the vault's own machinery — came in at 211,755. **That is not the price of an
ordinary run in either direction**, and it is recorded so the series stays comparable rather than
tidy.

**This is the run the owner did not want.** He had declared the session an emergency going around the
rules and said the ritual was not needed for it; it was dispatched anyway
([[divergence-the-pre-task-was-dispatched-on-a-session-the-owner-had-declared-an-override]]).

**Exactly three of its findings were mechanical breakages.** The other twenty were live prohibitions
he was in the act of lifting. **On a session whose purpose is to override, this agent's report is
equally loud for a rule that breaks the machine and a rule that has already been decided against**,
and it cannot tell them apart — the completeness it promises is what makes it so. **That is the first
recorded condition under which the ritual is harmful rather than merely expensive**, and no page in
this store scopes it.

**The three that were real, for the record**: rule 13 reddening on 53 ungrouped slugs
(`scripts/vault-authority.sh:244`), the `nogoverns` verdict firing on a rule with no `governs:`
(`scripts/vault-check.sh:484` plus the schema), and the feedback region still standing in
`.claude/skills/vault-ask/SKILL.md` while a live rule named that file in `governs:`.

**And it corrected the session three times running on facts the session had already asserted to the
owner** — the census claim, the target of a gate edit, and a line number in this agent's own
definition. **The second carrier of these counts is gone**: `agent-round-trip-cost` left in the sweep
of 2026-08-29, so this page is the only live one.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
