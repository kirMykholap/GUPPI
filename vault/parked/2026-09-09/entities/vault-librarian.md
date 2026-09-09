---
title: "The vault-librarian agent — the only writer of `wiki/`, reached through every skill that asks it"
type: entity
status: current
authority: vault-librarian
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [agents, vault]
---

# The `vault-librarian` agent

Written on 2026-08-13. One definition and **four callers**, and none of them is the store's
rulebook (the page said "three files" and named two callers until 2026-08-13):

| File | What it holds |
|---|---|
| `.claude/agents/vault-librarian/AGENT.md` | the agent definition — how to search, how to answer, what it may write |
| `.claude/skills/vault-ask/SKILL.md` | caller 1: a question on a topic, mid-work, from the owner **or from an agent** |
| `.claude/skills/ingest/SKILL.md` | caller 2: compile a source, then regenerate the brief |
| `.claude/skills/pre-task/SKILL.md` | caller 3: a plan, answered with **every** `decisions/` page that constrains it |
| `.claude/skills/vault-lint/SKILL.md` | caller 4: audit the corpus — report, do not fix, and append the findings to `log.md` |

Two hooks stand beside it and dispatch nothing: `.claude/hooks/session-brief.ps1` prints the brief
at session start, and `.claude/hooks/ask-the-vault.ps1` warns anyone who is not the librarian that
they are about to write where only it writes. What they are, and what neither can do:
[[session-hooks]].

**The definition is deliberately thin and points at the vault's own `CLAUDE.md`** for the schema,
the statuses, supersession, tags and contradictions. The rules of the store must not exist in two
places, because two copies diverge — which is the failure the whole vault exists to prevent.

What it may do without asking, and the three mechanisms that make that safe, are
[[the-librarian-writes-unattended]]. Why one agent rather than one definition per caller is
[[one-librarian-behind-every-caller]].

## Its context is empty of the session

It did not watch the session. Everything it knows about one is the journal in `raw/handoffs/`
— testimony, not evidence — which is what makes the handoff template load-bearing rather than a
courtesy — [[the-handoff-template-maps-onto-the-categories]].

## Registration is not the same thing as existing on disk

An agent file is read when a session starts, so the session that writes one cannot dispatch it by
name; see [[claude-code-config-loading]]. On 2026-08-13 the acceptance run was therefore a proxy:
a general agent was told to read the definition and follow it. **The corpus and the instructions
are tested that way; registration is not.**

**Registration itself is now proved, later the same day.** In the next session the acceptance run
was dispatched **by name**, and the definition arrived as the agent's system prompt — which is what
registration means and what the proxy could not show.

**`/vault-ask` was exercised as an entry point on 2026-08-14**, and it was the last untested path
in this definition: Q5 of the acceptance run was the owner's own question, asked through the skill
rather than dispatched by hand ([[the-acceptance-questions]]). Until that day every librarian call
had been a direct dispatch.

**The writing half was exercised the same day, and the diff was clean.** Two files touched —
`tags.md` +20/-3 and `log.md` +38 — no wiki page, no deletion, no contradiction resolved, and both
agents declared their writes unprompted, which is what [[the-librarian-writes-unattended]] asks of
them. The same run also showed the limit of that guarantee: **four librarians ran at once and two
of them wrote `tags.md` concurrently** — [[parallel-librarians-break-the-one-writer-property]].

The paragraph this replaced said the skill was registered and unexercised.

**And every test of an entry point carries one confound.** The harness injects the repository's
`CLAUDE.md` into a subagent **as it stood when the parent session started**, so an agent may be
holding a version that no longer exists on disk. That is why the acceptance re-run could not prove
the shortened `CLAUDE.md` was sufficient — the agent had the long one for free, and said so itself.
Confirmed again during the ingest of 2026-08-13 phase 2: the librarian was handed the pre-`d30b317`
file, 231 lines, while the tree held the 210-line one. **A test of what a session can find out
must be run in a session that started after the change.**

## The definition moved on 2026-08-16, and the move is its own lesson

The owner moved `.claude/agents/vault-librarian.md` into a directory of its own — the path in the
table above, `.claude/agents/vault-librarian/AGENT.md`. **The content is unchanged** apart from
`color: purple` and that session's edit to the narrowing procedure, which now puts the folder first
([[the-folder-is-the-first-narrowing]]).

The directory was created misspelled, and **the agent still resolved, because `name:` in its
frontmatter was right** — worth knowing, because it means a wrong directory name is not a loud
failure. The spelling was corrected the same session and eleven files naming the old path were
rewritten; `vault-check.sh` had named only the three carrying it in `sources:`
([[a-rewriter-must-be-paired-with-a-detector]]).

## And it moved back on 2026-08-20 — the table row above is stale, corrected here

**The definition lives at `.claude/agents/vault-librarian.md` again.** The owner moved it out of the
directory mid-session, and **the first dispatch after the move was accepted and ran**, so both
layouts resolve and the registry re-reads ([[claude-code-config-loading]]).

**The row in the table above still names the directory form**, and it is corrected here rather than
in place: this page's own history section below records the 2026-08-16 move, and rewriting the row
without dating the correction would leave two undated claims about one address
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**The move cost four `sources:` lines and made the gate red**, which is how the librarian lock came
to refuse the only writer that could repair them
([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]],
[[the-session-wrote-wiki-by-hand-while-the-lock-held-its-only-writer-out]]).

**Three prose references became correct by the move and five stayed wrong**, of which two must never
be repointed ([[a-path-detector-for-prose-references]]).

# It became a governed file on 2026-08-21

**`.claude/agents/vault-librarian.md` now carries a marked region**, the first rule rendered into an
agent definition rather than into `CLAUDE.md` or a generated file. The rule is the admission
criterion — no new entity where an existing one can carry the claim
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]) — and it is rendered here rather than
into `/ingest` because **`wiki/` has one writer and the moment a page is created is a moment inside
that writer**, not inside the ritual that dispatches it ([[one-librarian-behind-every-caller]]).

**So the rule reaches every caller for free.** `/ingest`, `/vault-ask` and `/pre-task` are three
dispatches of this one definition, and a rule delivered to one skill would have had to be copied
into the others ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**Region coverage stands at `4 of 15` and the unmarked files are unchanged.** The journal of
2026-08-21 says `5 of 15`; measured independently at the ingest of that journal, the advisory reads
**`4 of 15` with eleven files named**, and the numerator moved by one when this file gained its
region ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]],
[[the-region-coverage-figure-is-dated-where-it-stands]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# The `/pre-task` row leaves this table on 2026-08-22, and a second reading agent exists

**The table above lists `.claude/skills/pre-task/SKILL.md` as caller 3 of this definition. That is
false from today**, and the file is deleted. `/pre-task` is performed by dispatching
`subagent_type: "pre-task"`, an agent of its own at `.claude/agents/pre-task.md` —
`tools: Read, Grep, Glob, Bash`, no `Write` and no `Edit`, and it is instructed to write nothing at
all, not even a feedback line ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]],
[[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]).

**The row is corrected here rather than in place**, like the two address corrections above it: this
page already carries its own history of where the definition lives, and rewriting a row without
dating the correction would leave two undated claims about one caller
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**So this agent has three callers now** — `/ingest`, `/vault-ask` and `/vault-lint` — and the
sentence *"one definition and four callers"* is dated 2026-08-13 rather than renumbered
([[the-region-coverage-figure-is-dated-where-it-stands]], [[one-librarian-behind-every-caller]]).

**The reason the table gives for one definition is untouched, and it is what shaped the split.** The
rules of the store must not exist in two places, so the reading discipline this file carries — find
the vault, read its `CLAUDE.md`, grep then follow links, `tags.md` across the two languages, narrow
before opening, the folder first, the tag inside it, and the two ceilings — is now a `wiki/rules/`
page rendered into both agents rather than copied into the second
([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]).

**This file therefore carries a second region.** The first is the admission criterion
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]); the second is the reading discipline,
and it is the first rule in this corpus to render into two agent definitions
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]],
[[a-region-is-a-paired-comment-named-for-a-rule]]). **A file carries as many regions as it has
rules**, which is why the removed uniqueness on `governs:` matters here
([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

**What did not move: the write permission.** It belongs to the job and not to the body, and the new
agent has neither — the pre-task agent is a reader that cannot write, so the one-writer property of
`wiki/` is unchanged by its existence ([[the-librarian-writes-unattended]],
[[parallel-librarians-break-the-one-writer-property]]).

**Owed against a session restart:** that `pre-task` resolves as a dispatch target at all. An agent
file is read when a session starts, so the session that wrote it cannot dispatch it by name
([[claude-code-config-loading]]) — the same proxy-versus-registration distinction this page records
about 2026-08-13.

# It crossed into a session's file and reported it unprompted — 2026-08-23

**To render the style rule it inserted a heading and an empty marker pair into the repository's
`CLAUDE.md`.** That is a session's file, not the librarian's. It did so because the brief ordered a
render and did not provide the anchor to render into: `scripts/vault-inject.sh` writes *between*
markers and cannot create them ([[a-region-is-a-paired-comment-named-for-a-rule]],
[[write-plainly-name-the-source-and-say-what-is-not-done]]).

**What it wrote by hand was one heading and two comment lines.** The text between the markers was
written by the injector, which is the boundary that matters: no rule text was typed into a
destination.

**It reported the crossing without being asked**, which is the behaviour worth naming. A brief that
orders a render into an unmarked file has an unstated prerequisite, and the two ways out are to
refuse or to cross and say so.

**The general repair is at the brief's end, not the agent's**: a dispatch that orders a render names
who marks the region. Until it does, this is the shape the crossing takes and the report is the
mitigation.

## A scanner flagged one of its owner blocks as fabricated, and the block was genuine

**Every quotation this agent writes arrives through the dispatch brief**, because its context is
empty of the session — so *a quote with no user turn behind it* describes every legitimate owner
block it has ever compiled
([[a-genuine-owner-quote-was-flagged-by-a-scanner-that-cannot-see-the-dispatch-brief]]).

# Two dispatches of 2026-08-24, measured

**Reading, to plan the `decided_by:` back-fill: 218,397 tokens, 74 tool uses, 18m32s.**
**Writing it: 246,874 tokens, 22 tool uses, 6m54s.**

**The write was verified on the tree by the session rather than taken on the agent's word**: gate
exit 0, `--lint` shortfall from 33 pages to 7, the field on 27 of 34 pages in `wiki/proposals/`,
exactly one page carrying `status: idea`, and a diff of 28 files with 131 insertions and 1 deletion
([[a-librarian-answer-that-stops-at-the-agent-boundary-is-not-an-answer-the-owner-has]]).

**The shape of the pair is the finding.** Reading cost three times the tool uses and nearly three
times the wall clock of writing, for a smaller token count per minute — the expensive half of a
librarian dispatch is deciding what to write, not writing it.

**One defect surfaced inside the writing dispatch and is recorded separately**: a presence guard
that grepped whole files aborted the run at page eighteen of twenty-six
([[a-whole-file-grep-for-a-field-name-is-satisfied-by-that-name-in-prose]]).

# Its gate instruction said *after any write* and described something nobody has ever done — 2026-08-26

**The file said *"After any write, run `bash scripts/vault-check.sh`"*.** `/ingest` runs the gate
**once, at step 10**, after all the writing — and it has always done so.

**The wording moved rather than the ritual**, on the owner's ruling: *"ingest говорит делать gate
один раз в конце - это окей"*. It now reads *at the end of a writing pass*, injector first, with the
discrepancy written beside it
([[divergence-the-librarians-gate-instruction-described-something-nobody-has-ever-done]]).

**The arithmetic that made the old wording indefensible:** 29 pages × 21.5 s is **more than ten
minutes of gate per ingest**, and nobody has ever paid it.

**The edit sits outside this file's rule region**, so no address verdict is touched; the gate read
20.45 s, exit 0 afterwards.

**The same shape still stands in the vault's own `CLAUDE.md`**, which is a session's file, and no
`wiki/rules/` page governs either — so the two copies drift independently
([[no-rule-reads-a-harness-file]]).

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*

# It is to be given a dispatch tool, and it does not have one yet — 2026-08-29

**Decided, not built.** The owner ruled that this agent runs its own reading subagents — the decisions
agent and the lessons collector — waits for their verdicts, and returns once, with the main session
reviewing after it finishes
([[the-librarian-dispatches-its-own-reading-agents-and-returns-once]]).

**Line 4 of `.claude/agents/vault-librarian.md` reads `tools: Read, Grep, Glob, Bash, Write, Edit`.**
Adding `Agent` is the whole obstacle, and a ruling of 2026-08-28 was recorded as settled design on the
ground that no such tool exists here.

**And the file's own contents were ruled on separately**: it describes *capabilities* — how to search
the vault, how to write it, which tools and which subagents it has — and never a ritual's process. The
ingest process, including the instruction to dispatch and wait, lives in `.claude/skills/ingest/SKILL.md`
([[the-librarian-agent-file-carries-capabilities-and-the-ingest-process-lives-in-the-skill]]).

**Nothing about the one-writer clause changes.** A reading agent reads and returns; this agent writes.
The change is who holds the dispatch, not who holds the pen
([[dispatch-librarians-in-parallel-only-for-reading]]).

**Nested dispatch has still never been measured here**, and the cost of the rewiring is the standing
objection to it: two reading dispatches plus a second librarian round trip, at every session
([[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# It has the dispatch tool, and it has used it — 2026-08-29

> [!CAUTION] THE HEADING ABOVE — *"it does not have one yet"* — IS FALSE FROM 2026-08-29
> `.claude/agents/vault-librarian.md:4` now reads
> `tools: Read, Grep, Glob, Bash, Write, Edit, Agent`. Everything else in that section stands: the
> file's own contents describe capabilities, the ingest process lives in the skill, and the one-writer
> clause is untouched.

**The file gained a section naming the two subagents it may dispatch**, what each returns, and that they
read while it writes — placed *before* the rendered reading-discipline region, which was not touched
([[the-decisions-agent]], [[the-lessons-agent]]).

**The first use was the ingest of 2026-08-29**, and it is the first time this agent has dispatched
anything. Both readers were sent in parallel before any write, as step 2b requires, and both returned
before the first page was written.

| dispatch | tokens | tool uses | wall clock |
|---|---|---|---|
| `decisions-agent`, mode 1 over 19 arriving decisions | 151,592 | 69 | 10m24s |
| `lessons-agent` over 18 lessons plus `rules/` and `proposals/` | 129,641 | 43 | 9m19s |

**A dispatching agent sees its children's usage even though it cannot see its own.** That is new: a cost
figure of this kind previously reached `log.md` only through the main session's feedback section, and
these two were written by the librarian directly ([[a-subagent-cannot-report-its-own-cost]]).

**What that does not settle is the net.** 281k tokens of reading were added to one ingest, and nothing
measures what the librarian stopped reading because the folders were read for it. An earlier attempt to
net the two summed an isolated subagent's budget into the librarian's and was wrong.

## It crossed into three harness files again, and reported it again

**To land two rule pages it inserted marker pairs into `CLAUDE.md`,
`.claude/agents/decisions-agent.md` and `.claude/agents/lessons-agent.md`.** Same shape as 2026-08-23,
same mitigation: **two comment lines per file and no rule text typed**, the text written by
`scripts/vault-inject.sh`.

**The general repair named on this page in 2026-08-23 — a dispatch that orders a render names who marks
the region — is still unmade**, and the dispatch of 2026-08-29 ordered two renders without naming
anybody. **Three landings have now taken the crossing shape.**

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`
and from this ingest's own dispatches.)*
