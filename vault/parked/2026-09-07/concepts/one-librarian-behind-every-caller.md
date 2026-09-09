---
title: "One librarian behind every caller, because duplicated instructions diverge"
type: concept
status: current
authority: librarian-modes
basis: inference
sprint: S0
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", ".claude/agents/pre-task.md", ".claude/skills/vault-lint/SKILL.md"]
tags: [agents, retrieval, vault]
---

# One agent, four callers — not four agents

The modes share nearly everything and differ only in their trigger and the shape of their answer.
Written as separate definitions they would drift apart: **that would be the divergence failure
reproduced inside the component built to prevent it.**

Shared, in [[vault-librarian]]'s definition: grep first and then follow `[[links]]`; synthesise
rather than dump; always return the pages used, because an answer that cannot be checked is not an
answer; always report the **negative space** — what the vault does *not* have on the topic.

| | The brief | A question | A plan | An audit |
|---|---|---|---|---|
| Skill | `/ingest`, as its last step | `/vault-ask` | `/pre-task` | `/vault-lint` |
| Exercised | every ingest | **first on 2026-08-14** ([[the-acceptance-questions]], Q5) | never | **first on 2026-08-15**, over 108 pages — the row read "never" until then ([[lint-waits-for-an-open-sprint]]) |
| Trigger | no topic given | a topic given | a plan given | the retrospective |
| Caller | the ingest, at session end; `cat` at session start | mid-work, by the owner **or by an agent** | an agent, before non-trivial work | the owner, once per sprint |
| Answer | state of the sprint: goal, done, not done, what must not be broken | answer + sources + what is missing | **every** constraining `decisions/` page, or an explicit "there are none" | findings appended to `log.md`; writes only where the fix is unambiguous |

**The page said "two entry points" until 2026-08-13**, and its filename still does.
*(It stopped on 2026-08-19, when the rename landed. The clause stands as written: the name
outlived the corrected title by six days, and that gap is why a rename is scheduled as a sweep
rather than taken by the session that happens to notice it.)*
Two of the four were missing, and neither is a variation on the first two: `/pre-task` asks for **completeness
rather than relevance** — a ranked partial answer is dangerous when the decision your plan violates
may be twelfth of eight returned — and `/vault-lint` asks the librarian to read the corpus *as a
corpus*, mark contradictions without resolving them, and report rather than fix. What generalises
is the count of definitions, which is one, not the count of ways in.

## The ten-page ceiling belongs to the question mode, not to the librarian

The librarian is told to stop and report a miss if it opens more than about ten pages for one
question. **That ceiling is scoped to topic queries, and saying so was a correction made on
2026-08-13**, because `/pre-task` asks a different question: *what constrains this plan* — where a
ranked partial answer is the dangerous one, and a ceiling would produce exactly that.

`/pre-task` therefore enumerates frontmatter cheaply across **every** `decisions/` page and opens
only the ones the titles implicate. Same corpus, opposite discipline: the question mode bounds
reading to protect the answer's quality ([[vectors-are-deferred-not-rejected]] — a librarian that
reads forty pages answers worse than one that reads five); the plan mode bounds *opening*, never
*enumerating*.

## The audit reports; merging is not a fix it may apply

`/vault-lint` writes only where the fix is unambiguous. **Merging two near-duplicate pages is not**:
it is supersession — a successor, a `superseded_by:`, a move to `archive/` — and a judgement about
the corpus rather than a defect in it. **Three** merge candidates and two filenames that understate
their pages sit on that agenda in `log.md`, deferred on 2026-08-13 rather than done, for the
retrospective and the owner. *(This line said "four" until 2026-08-15. `log.md` heads that list
with "four pairs" and lists three — table-refreshes-itself + collection-end-resets-the-chips,
absent-values-never-overwrite + description-is-full-has-no-producer, collection-modes-and-why-source-filters-do-not-decide
+ collection-frame-city-check — and this page had copied the heading rather than counting the list.
[[lint-waits-for-an-open-sprint]] had already recorded the discrepancy; this page had not been
brought into line with it. The shape: [[a-stated-count-drifts-from-the-list-it-heads]].)*

## The negative space is half the answer

"No decision has been recorded about a framework migration" tells the caller two things: that they
are free to decide, and that the decision must then be recorded. Without that section, "there are
no constraints" is indistinguishable from "the librarian did not find them".

## A topic answer follows the order of the categories

`entities/` → `decisions/` → `concepts/` → `lessons/`: what already exists, what was already
decided, how it is built, what will bite you. **That is also the order of the handoff's sections**
— one sequence to remember rather than two. It holds for `/vault-ask` and for `/pre-task`; the
brief and the audit have shapes of their own.

*`basis` corrected 2026-08-13 from `human` to `inference`.* The spec's decision table gives this
row no owner attribution — unlike the row beside it, "the librarian writes the vault unattended |
owner's call". It is the designer's conclusion, and marking it `human` would let it outrank
anything the owner actually said; the same correction was made to
[[the-index-is-a-map-not-a-catalogue]] on the same day, for the same reason.

Why grep and links are enough for now, and what they cost:
[[the-index-is-a-map-not-a-catalogue]], [[vectors-are-deferred-not-rejected]].

## The owner's model of the same shape, stated 2026-08-16

**A skill is a role mask and a subagent is an extra body**
([[a-skill-is-a-mask-and-a-subagent-is-a-body]]). Read that way, this page's four callers are four
masks over one body, which is why duplicating the definition per caller was the wrong move for a
reason more general than divergence — and it opens the question of whether `/vault-ask` needs the
body at all, or only the mask. That fork is open and measured on one side only.

## The `/pre-task` scope named above is a ruling behind, from 2026-08-21

**"`/pre-task` therefore enumerates frontmatter cheaply across every `decisions/` page" reports the
tree, and the tree is what the owner ruled wrong** on 2026-08-21: four more folders belong in the
enumeration, `lessons/` alone stays out
([[the-pre-task-enumeration-covers-every-folder-but-lessons]]). **Not built**, so the sentence stands
as a description and is dated as a specification.

## The librarian is the agent; `/ingest` is one of the jobs given to it — 2026-08-21

**The owner said plainly that he had been conflating the two**, and the conflation is built into the
design rather than being his error: `/ingest`, `/pre-task`, `/vault-ask` and `/vault-lint` all
dispatch the same `vault-librarian`, and **only the first of them writes** ([[vault-librarian]],
[[the-librarian-writes-unattended]]).

**So *the librarian* names a body, and *the ingest* names a job.** The table above has said this
since 2026-08-13 in the shape of four columns; what it never said in one sentence is the sentence a
reader needs, and it is recorded here because he asked for it somewhere a reader will meet it.

**The write permission belongs to the job, not to the body.** A `/vault-ask` dispatch is the same
agent with the same instructions and it does not write — which is why the one-writer property is a
convention about who is dispatched rather than a lock
([[parallel-librarians-break-the-one-writer-property]], [[the-librarian-lock-hook]]).

## The clause forbidding the enumeration in the main context is lifted — 2026-08-21

**The ten-page ceiling section above is unchanged; what moved is where the *listing* happens.**
`/pre-task` phase 1 runs `bash scripts/vault-catalogue.sh` in the caller's own context — 1.66 s, 566
rows, about 17 KB of titles once filtered — and dispatches only over what it names
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]], [[vault-scripts]]).

**The clause was written when the alternative was opening every file in `decisions/`.** The owner
lifted it deliberately, and the reversal is recorded so that it is not re-derived as an oversight
and quietly restored.

**What is unchanged is the property the ceiling protects.** Enumerating is not opening; phase 1
narrows what is **read** and never what is **listed**, so a ranked partial answer is still what this
mode refuses to give ([[the-pre-task-enumeration-covers-every-folder-but-lessons]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

## The `/pre-task` column names a second body from 2026-08-22, and the table is dated rather than rewritten

**The table's `/pre-task` column describes a caller of this one definition, and that stopped being
true today.** `/pre-task` dispatches `subagent_type: "pre-task"`, whose definition is
`.claude/agents/pre-task.md` — a second agent, with its own tools, its own two phases and no write
permission at all ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]],
[[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]). `.claude/skills/pre-task/` is
deleted, so the row's `Skill` cell names a file that no longer exists.

**The column is not rewritten and the count in this page's opening — one agent, four callers — is
left as it stands.** Both were true from 2026-08-13 until this morning, and a statement about a day
is dated where it stands rather than renumbered
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]],
[[the-region-coverage-figure-is-dated-where-it-stands]]). Three callers of the librarian remain:
`/ingest`, `/vault-ask` and `/vault-lint`.

**What did not change is this page's title, and it is why the change was affordable.** *Duplicated
instructions diverge* is exactly the reason a second definition was not allowed to be a second copy:
the reading discipline the two agents share is one `wiki/rules/` page rendered into both, not text
typed twice ([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]],
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]). **The principle is being honoured
by rendering rather than abandoned by copying** — which is the whole reason the injector exists
([[no-rule-reads-a-harness-file]]).

**And the section above — *The ten-page ceiling belongs to the question mode, not to the librarian* —
survives the split in a stronger form.** It argued that one definition can carry two opposite
disciplines because the ceiling is scoped to topic queries. With two definitions the scoping is
structural: the ceiling and its carve-out travel into both agents inside the rendered slice, and the
topic answer's shape — Sources, Not in the vault, the category order — stays the librarian's alone,
deliberately outside it. **That was the owner's ruling of 2026-08-22**, and its ground is this
section's own: rendering the topic discipline into the pre-task agent would ship it a rule it must
not follow.

**What the split costs, named rather than repaired:** the two closing sections of an answer are now
stated in two files in two sets of words. The rule page records that as an accepted duplication
rather than an oversight.

## The `/pre-task` citation is repointed to the agent, and the claim it supported is the one that changed — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` and now cites `.claude/agents/pre-task.md`**,
because the skill was deleted on this date and rule 5 of the gate requires every repository path in
`sources:` to resolve — a citation to a file that is not there reads as provenance and is not
([[vault-scripts]]). **The address moves and the history stays readable**: the table above was
compiled from the skill, on days when the skill was what `/pre-task` meant.

**The claim this page cited it for is exactly the claim the section above dates.** The skill was
caller 3 of one definition; the agent is a **second definition**, so the new address does not support
*one agent, four callers* and is not offered as supporting it. It is cited as the file the `/pre-task`
column now describes.

**Two claims of this page do hold at the new address, and they are the ones worth checking.** The
ten-page ceiling with its `/pre-task` carve-out, and *enumerates frontmatter cheaply and opens only
what the titles implicate*, are both in `.claude/agents/pre-task.md` — inside the region rendered
from [[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]], which is why
they are the same words in both agents rather than two copies that can drift.

## A fifth caller joins the table, and it is a second brief to the same body — 2026-08-24

**`/vault-lint` now dispatches the `vault-librarian` twice**: once as the lessons collector, which
reads the undrained lessons and writes `proposals/`, and then as the audit
([[the-librarian-is-blind-to-a-recurring-family-from-where-it-stands]]).

| | The lessons collector |
|---|---|
| Skill | `/vault-lint`, first dispatch |
| Exercised | **never** — built 2026-08-24, first run deferred to a session of its own |
| Trigger | a queue given: `uv run python scripts/lessons-queue.py` |
| Caller | the owner, once per sprint, plus on demand |
| Answer | families of lessons, written as `proposals/` pages |

**It runs before the audit dispatch**, because the audit is scheduled after the last write of what
it audits and this one writes ([[the-audit-is-dispatched-after-the-writes]]).

**It is the second writing caller this page has ever had.** `/ingest` was the only one, and the
one-writer property has always been a convention about who is dispatched rather than a lock — so a
second writing mode is a second occasion to keep them out of each other's way, not a change to the
rule ([[parallel-librarians-break-the-one-writer-property]], [[the-librarian-lock-hook]]).

**What makes the position work is what the librarian does not carry into it.** At an ingest it
stands inside one session's context; a fresh dispatch reading the whole queue has none, which is the
whole of the fix. **The fix is the position, not the agent** — and that is this page's own argument,
applied to a mode rather than to a definition.

*(`basis: inference` on this page loses to the owner's ruling that the collector exists at all;
what is inferred here is the shape of the table, not the mode.)*
