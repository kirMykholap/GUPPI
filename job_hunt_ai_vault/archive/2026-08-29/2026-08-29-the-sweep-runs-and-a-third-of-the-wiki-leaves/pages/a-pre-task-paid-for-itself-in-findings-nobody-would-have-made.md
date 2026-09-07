---
title: "The `/pre-task` paid for itself in findings the session would not otherwise have made"
type: lesson
status: archived
authority: pre-task-value
basis: measurement
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/agents/pre-task.md", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [agents, vault, process]
---

# What each run found, on 2026-08-17

**The first `/pre-task`**, before the marked-region build:

- **Two of the four designed verdicts would have been green over an empty `wiki/rules/`.** The
  folder existed and held no page, so the rules that fire on a rule page would have passed by
  examining nothing — the vacuous-pass failure this store keeps meeting
  ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
- **`render:` existed in one page's prose and in no schema.** A design being read as a
  specification named a field nothing could evaluate ([[render-was-not-introduced]]).

**The second `/pre-task`**, before `governs:` was written:

- **`governs:` had no vault-name-free spelling.** Every candidate either hard-coded the vault's
  directory name or resolved ambiguously. That is what surfaced the question the owner then closed
  ([[governs-is-a-path-from-the-repository-root]]).

# Why this is a lesson and not a boast

All three findings are of one kind: **a constraint that the plan had already assumed away.** None
of them was discoverable by writing the code carefully, because in each case the code would have
been written, passed, and been wrong — a green check over an empty set, a field with no writer, a
path that means two files.

The cost of a `/pre-task` is one librarian round trip, and this project has been explicit that the
cost is real ([[agent-round-trip-cost]]). The measurement here is the counterweight: **the third
finding changed a decision the session had already argued out in writing and got wrong**
([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).

**The trigger worth copying:** run it before an area you have not touched this session, and before
any plan whose correctness depends on what the tree currently contains.

## Three more, and they settled an argument — 2026-08-18

**`/pre-task` surfaced constraints three times in one session that could not have been queried by
name** — eight `decisions/` pages in the first answer alone. The session did not know the pages
existed, so no topic query would have reached them.

**That evidence decided a live disagreement about `CLAUDE.md`.** The session argued that a rule you
must ask for is a rule you can fail to ask for; the owner's position was that the system is *about
to write something → ask the vault*, and that `/pre-task` enumerates constraints rather than
answering a topic. **The session's own transcript was the evidence, and it was against the session**
([[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]).

**The general form: enumeration beats retrieval when the reader does not know what to ask for.**
That is the same distinction the folder narrowing rests on, from the other end
([[the-folder-is-the-first-narrowing]]).

**The same session paid the other side of this bill too**: a criterion the corpus already held,
written and measured, was derived from scratch and reported as a finding
([[deriving-what-the-vault-already-holds-costs-a-round]]).

# The fourth run, and the fourth time it returned at least one finding — 2026-08-19

**The plan was *guard, then the AST move*.** The librarian surfaced a blocker **neither the brief nor
`sprint.md` named**: the move's destination is a generated file and the `whole` mode did not exist
([[the-whole-mode-owns-a-file-end-to-end]]).

**Following the plan as written would have run the move into a mechanism that was not there.** The
sprint's *next* list had the order right and was silent about the dependency — which is the shape
this page already describes, met from a new direction: the finding was not in the plan's own
material, so no amount of care reading the plan would have produced it.

**Four runs, four times a finding.** That is the whole of the evidence, and it is recorded here
rather than converted into a rate ([[an-unsourced-number-is-dropped-not-chosen]]).

# The fifth measured run — 2026-08-20

**Three blockers returned, and two of them were the owner's to resolve rather than the session's.**

**The sharpest was mechanical and would have shipped:** the approved plan named a `.txt` as the
destination for a rule's text. The governed set is `*.md` under `.claude/` **by property**
([[the-governed-set-is-swept-and-markdown-by-property]]), so a `.txt` would have been invisible to
the address verdict, the hand-edit verdict and the leftover sweep **at once** — the state two of the
owner's rulings exist to forbid ([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]).

**It also caught that `render: whole` refused without `paths:` before a line was written**, which
became a decision of its own ([[paths-is-required-where-it-is-read-and-nowhere-else]]), and it named
the `/retro`-drains-versus-`/handoff`-drains contradiction in the plan
([[the-retro-writes-its-own-transit-file]]).

**And it predicted, in advance, the defect the selftest then caught**: a `paths:` condition written
as one glob matching none of the paths it guards
([[a-refusal-written-as-one-glob-can-match-none-of-the-paths-it-guards]]).

**This is the fifth measured run and the fifth to return at least one finding.** That is the number
to watch, and it has not turned: the day one returns nothing is the day the trigger is worth
re-examining. **The price is now measured too** — a pre-task question is 5m54s, not the 15-to-30
band the rule page used to quote ([[agent-round-trip-cost]],
[[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

**The trigger these runs were counted under has been replaced**
([[the-pre-task-trigger-becomes-the-plan-and-the-first-write]]). The count is unaffected: it is a
count of runs that happened and what they returned, not of the condition that occasioned them.

# The sixth measured run, and the sixth to return at least one finding — 2026-08-20, fourth session

**Three constraints the plan did not have, all of them before approval:**

- **the `pre_task` column would have asserted a skipped ritual** on a row where nothing had been
  asked of it ([[the-pre-task-column-gains-a-state-for-asserting-nothing]]);
- **rule 8 of the gate already answers *is this journal compiled?* by the sidecar**, so the new
  selection rule had a definition to adopt rather than invent
  ([[the-sidecar-is-the-single-definition-of-compiled]]);
- **the vault had deliberately withheld the ledger's retention ruling**, naming it as a decision
  about the project rather than answering it ([[the-pre-task-ledger]]).

**The third is the one worth reading twice.** It turned the ledger item from *working around a
decision the store had made* into *supplying a decision the store had deliberately not made* — a
distinction no reading of the plan produces, because the plan does not know which silences are
deliberate.

**Six runs, six times a finding**, and the count is of runs and what they returned rather than of
the trigger that occasioned them. **The price has a second reading and it is the same**: 5m54s, at
roughly four times the pages opened ([[agent-round-trip-cost]]).

# The seventh run reversed the design instead of adding to it — 2026-08-21

**Phase 1 of the new `/pre-task` was run against a hook design and returned two pages that reversed
it**, in about fifteen seconds, opening two pages
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]):

- **[[the-ritual-records-itself-rather-than-being-detected]]** — a ritual records itself because
  inferring that it ran fails by staying silent in the case the mechanism exists for;
- **[[plan-mode-blocks-edits-and-not-a-subagent-dispatch]]** — the measured fact that plan mode
  blocks edits and not a dispatch, which relocated the whole problem.

**The design about to be built was a hook on the `Skill` tool.** It would have bought zero seconds
at the cost of the one property the mechanism exists for. **Neither page was in the session's head.**

**Seven runs, seven times a finding**, and the count is of runs and what they returned rather than
of the trigger that occasioned them.

## The journal's own reading of this run disagrees with this page, and both are left standing

**The journal calls it *"the first recorded instance of the ritual changing the work rather than
confirming it"*, and says every previously recorded pre-task was skipped or confirmed what was
already believed.** That is not what the sections above record: the third finding of 2026-08-17
*"changed a decision the session had already argued out in writing and got wrong"*, and the sixth
run turned a ledger item from working around a decision into supplying one.

**The reading that survives both is narrower and is the interesting one**: this is the first run
whose findings **reversed a design the session was about to build**, rather than adding a constraint
to one it was about to build correctly. **The journal is not edited** — `raw/` is immutable and what
the session believed is data ([[fidelity-to-a-source-and-fidelity-to-the-tree]],
[[journal-vault-brief-each-artefact-has-one-owner]]).

**The price of this run is the cheap half only.** Fifteen seconds is phase 1, not a dispatch; the
dispatch was not needed ([[agent-round-trip-cost]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# It paid again on 2026-08-22, and the incident is exact

**The plan assumed the flat archive, because that is what the tree shows** — about thirty retired
pages sitting flat in `archive/`, one of them retired the day before. **The corpus said dated**, in a
clause of [[archive-is-dated-by-session-and-holds-what-left-the-working-set]] that nobody had opened.

**Executing the owner's choice then exposed a clause that had been unexecutable for six days.**
`scripts/vault-archive.sh` accepted only the four inbox kinds, so the sanctioned tool could not
express the destination its own decision named, and the practice had quietly outvoted the rule with
no instrument reporting it
([[the-archive-script-gains-a-pages-kind-and-a-retired-page-is-dated-by-its-session]]).

**None of that was reachable by reading the tree**, which is this page's claim met a second time: the
tree shows what was done and the corpus shows what was decided, and a plan built from the first is
confidently wrong in the one direction nothing checks ([[no-rule-reads-a-harness-file]]).

**Phase 2 was not run on this date**, so the finding above came from phase 1 alone — and the finding
phase 2 would have made was paid for instead
([[the-pre-task-always-dispatches-its-narrow-phase]]).

# The citation is repointed, and the trigger this page recommends is not at the new address — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` and now cites `.claude/agents/pre-task.md`.**
The skill was deleted on this date ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]),
and rule 5 of the gate requires every repository path in `sources:` to resolve — a citation to a file
that is not there reads as provenance and is not ([[vault-scripts]]). **The address moves and the
history stays readable**: the runs counted above were run against the skill, and what each returned
is unaffected by where the ritual now lives.

**The trigger did not survive the move, and it had already been replaced.** *"Run it before an area
you have not touched this session"* was the skill's own trigger sentence; the agent's definition
carries no trigger at all, because a trigger is read by the caller and an agent is read after the
dispatch. The trigger now lives in a rule rendered into a hook message, and its second half —
*an area you have not touched this session* — was deliberately dropped on the owner's word
([[a-pre-task-runs-between-the-plan-and-its-approval]],
[[the-pre-task-trigger-becomes-the-plan-and-the-first-write]]). **The sentence above is left as this
page's recommendation and is no longer a description of any file.**

**The new source states a lower count than this page holds.** `.claude/agents/pre-task.md` says
*"Five measured runs are on the record and every one returned at least one finding"*, and so does the
rule page; the sections above record seven, plus the run of 2026-08-22. **This page is the authority
on the count and the harness files are behind it** — a harness file is a session's to write and not
the librarian's, so it is named here rather than corrected
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]],
[[a-stated-count-drifts-from-the-list-it-heads]]).

**Phase 2 ran later on 2026-08-22 and its cost was measured** — 233,165 tokens, 10m40s, 49 tool uses,
65 pages opened over a 43-page shortlist
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]). **The run count above is
not incremented for it**, because what that run returned was not reported to the librarian: the
figures came back as a price and not as findings. If it produced any, they belong here and are owed
from the session's journal.

# The first run of the `pre-task` **agent**, and it returned four findings the session had wrong — 2026-08-22

**It corrected the plan it was checking in four places**, and each is a constraint the plan had
assumed away rather than a detail it had got slightly wrong:

- **the plan would have deleted a `CONTRADICTION` block on the strength of the owner ratifying the
  page.** The documented procedure marks a resolved contradiction and keeps it, and deletion is the
  one move it forbids ([[a-refusal-is-conditional-or-absolute-and-nothing-else]],
  [[the-index-is-a-map-not-a-catalogue]]);
- **the plan would have renumbered a drifted count**, which two decisions of this corpus refuse
  ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
  [[the-region-coverage-figure-is-dated-where-it-stands]]). **It also named a third copy of the
  sentence, in `.claude/hooks/check-the-plan.ps1`, that was in no plan and that no search for the
  page would have reached** ([[a-pre-task-runs-between-the-plan-and-its-approval]]);
- **an eleventh citation of the deleted skill, in `archive/`**, which the earlier sweep of ten had
  not reached because the gate walks `wiki/` only. **It dangles silently and reddens nothing**, which
  is precisely the case the archive ruling was measured on
  ([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]);
- **an item the plan had deferred *against a session restart* on a page whose measurement was
  false.** [[claude-code-config-loading]] says a new agent needs a restart, and the agent doing the
  checking had itself been created and dispatched in that same session.

**Three of the four are of this page's one kind and the fourth is a new one.** The first three are
constraints the plan had assumed away. The fourth is the store being **wrong** rather than merely
unread — the plan consulted the right page, got a stale measurement, and deferred work that was
already done ([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).

**No total is stated here.** The sections above record seven runs plus the run of 2026-08-22 whose
findings were never reported, and adding them would be arithmetic rather than a claim any page makes
([[an-unsourced-number-is-dropped-not-chosen]], [[a-stated-count-drifts-from-the-list-it-heads]]).
**What is recorded is the run and what it returned**, which is what this page has always counted.

**The rule page's copy of the old count came out in the same change and was not renumbered**, on
this run's own finding ([[a-pre-task-runs-between-the-plan-and-its-approval]]).

**Its price is measured and is the first reading of the agent rather than of the skill** — 146,705
tokens, 57 tool uses, 13m36s, 53 pages shortlisted from 362 filtered rows, 16 opened in full and 16
in part ([[agent-round-trip-cost]],
[[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

# What the phase-2 run of 2026-08-22 returned, arriving a day late — 2026-08-22, at the ingest

**The section above says of that run: *"If it produced any, they belong here and are owed from the
session's journal."* They are these, and the journal is where they came from**
([[a-brief-that-carries-a-cost-without-its-findings-suppresses-the-finding]]):

- **`scripts/vault-catalogue.sh` does not emit `binding:`, and phase 1 is specified to filter on
  it.** The catalogue's columns are Page, Authority, Title, Status, Sprint and Tags, so **the ritual
  as written cannot be performed from the catalogue alone** — it needs a second pass over one folder.
  Nothing in `wiki/` stated the catalogue's column set before this ([[vault-scripts]],
  [[the-page-list-is-a-query-not-a-generated-file]]).
- **The `prohibition`-only filter drops five of the pages most load-bearing for a plan whose subject
  is a ratified deferral**, headed by [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]] —
  which **is** the ruling that plan executed — and [[the-ratification-sweep-waits-for-a-session-of-its-own]],
  which schedules one of its stages.

**The second finding is a second cause of an incident this page already records.** The recorded
shortlist miss of 2026-08-22 is that same page falling through that same shortlist, and the corpus
attributes it to one cause only — a list built from `title:` and `authority:` by the party that wrote
the plan. **Nobody noticed the other half: a perfect title match would have been filtered out
first.**

**The run count is still not incremented for it and no total is stated.** What is recorded is the run
and what it returned, which is what this page counts ([[an-unsourced-number-is-dropped-not-chosen]],
[[a-stated-count-drifts-from-the-list-it-heads]]).

**Whether the filter stays is the owner's and is on the sprint.** The corpus argues *for* it in three
places and against it nowhere, and a plan whose subject is a ratified deferral and a filter that
drops deferrals are structurally blind to each other.

# The run of 2026-08-23, its two counts and what it returned

**The counts, which nothing else records and neither of which is recoverable afterwards**: the
shortlist named about **190** pages of **364** filtered catalogue rows, and the agent opened **38**
in full. **It reached past the `binding:` filter three times deliberately, and five of its findings
came from pages reachable only by a link.**

**Those two clauses are the first direct evidence about the two design questions this page keeps
raising.** The `prohibition`-only filter was reached past on purpose three times — so the filter is
costing something the agent can feel — and five findings came from pages no shortlist named, which
is the case for phase 2 following links rather than reading the shortlist
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**Its price, over a ten-phase plan with three named deep-dives: 230,882 tokens and 14m58s**
([[agent-round-trip-cost]]).

**What it found: eight contradictions with live prohibitions, and one false premise the plan rested
on.** The load-bearing ones:

- **the 2-4 acceptance-criteria range is a `binding: prohibition` and not a skill preference** —
  the plan had treated it as advice;
- **`record-the-dispatch.ps1` writes no in-flight row**, so a parallel-dispatch counter has nothing
  to read ([[the-dispatch-record-hook]],
  [[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]);
- **a written list of governed destinations is refused** by
  [[the-governed-set-is-swept-and-markdown-by-property]].

**All three are of the kind this page was written about**: a constraint the plan had already assumed
away, which no amount of careful writing would have surfaced.

**And the catalogue's missing `binding:` column is now a second-day finding rather than a first-day
one.** The section above records it from 2026-08-22; on 2026-08-23 phase 1 again carried a second
grep over one folder for it, and it is a carried sprint item ([[vault-scripts]]).

# The run of the second session of 2026-08-23, and it killed three items of the plan as factually wrong

**The two counts, which nothing else records and neither of which is recoverable afterwards**: the
shortlist named **99** pages and the agent opened **33** in full, plus two registers, two
`_schema.yaml` and five tree files.

**Its price: 225,195 tokens and 16 minutes** ([[agent-round-trip-cost]]). **The figures are copied
as observed and are not converted to a rate** — a token count and a wall clock measured on one run
of one plan divide into a number that means nothing about the next one
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**What it found: three items of the approved plan were factually wrong, and it removed them.**

- **a selftest case for a gate verdict named `realised`** — a verdict that had been written and
  removed the same day on the owner's own correction, so the case would have tested nothing that
  exists ([[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]]);
- **an archive step for a journal already sitting in `archive/`**;
- **a gate verdict that could never fire**, because the page it judged is in `archive/` by the time
  the rule applies and the gate's frontmatter pass reads `wiki/` alone
  ([[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]],
  [[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

**And it reversed an ordering**, which is the second time a run of this ritual has changed the shape
of a plan rather than adding to it: the plan promoted a field to `required:` before back-filling it,
which reddens the gate and locks the librarian out of the fill
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

**Three of the four are the kind this page was written about**: a premise the plan had already
assumed, which no amount of careful writing would have surfaced — because the plan's author had no
reason to doubt it.

**The session it ran inside was wrong about the date for its whole length**, and the ritual did not
catch that ([[a-date-is-a-measurement-and-an-inferred-one-is-wrong-wherever-it-was-written]]). The
ritual reads the store against a plan; it does not read the clock.

# The run of 2026-08-25, and it is the fifth point rather than a rate

**The shortlist named 88 pages and the agent opened 34 in full** — 31 `wiki/` pages plus the vault's
`CLAUDE.md`, `authority.md` and `sprint.md` partially, 758 of 1402 lines. **Cost: 214,600 tokens, 73
tool uses, 18m50s** ([[a-subagent-cannot-report-its-own-cost]]).

**What it bought, on a plan the owner had not yet approved:** it killed one plan item outright, found
a selftest case the plan would have broken, caught a scope widening nobody had asked about, corrected
a population count from eight to fifteen, and found a prohibition collision the session had walked
past ([[the-feedback-rules-extra-destination-is-withdrawn]],
[[governs-is-a-path-from-the-repository-root]],
[[the-harness-defects-found-this-session-enter-the-sprint-one-line-each]],
[[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]]).

**The two counts are recorded because nothing else records them**: across runs they are the only
evidence on whether the cheap phase discards too much
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

# A sixth point, and the cheapest on record — 2026-08-26

**The shortlist named 443 pages and the agent opened 40 in full**, plus the vault's `CLAUDE.md`,
three sections of `sprint.md` and seven tree files. **143,840 tokens and 10m18s**, against the five
on record at 182,599–230,882 tokens and 11m52s–18m50s.

**It is a point, not a rate.** The run was over a committed execution plan rather than a plan being
written, which is a different question and probably a cheaper one.

**What it bought:** it found that the committed plan orders about eight librarian writes its own
ingest had already carried out, and that the plan cites a line number that expires on first contact
([[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

# A seventh point, on a plan that looked finished — 2026-08-28

**The shortlist named 93 pages and the agent opened 42 in full**, plus seven non-vault files read or
executed. **161,000 tokens, 12.8 minutes, 47 tool uses.**

**What it bought on a five-step plan the session believed was checked:** that `make style` reads only
`src tests` and therefore touches nothing in a 36-path vault commit; that committing another
session's ingest owes the five review commands `/ingest` names; that `make smoke` runs twice per
session by design where the plan had it once; and it dissolved both items the session had framed as
disputed — one of them because the session had read a condition the owner retired on 2026-08-24 as
still live ([[a-sweep-may-run-inside-a-session-when-the-list-is-assembled-in-advance-and-shown-whole]]).

**The two counts are recorded because nothing else records them.** This shortlist is the narrowest on
record and the run is the second cheapest.
