---
session: 2026-08-17
sprint: S2
commits: aebb308..e38a4ab
---

# Handoff — 2026-08-17

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

## State

**Done.** S1 closed on its goal with criterion 4 written unmet. Every alarm the opening brief
carried is discharged. Rule 10 of `vault-check.sh` exists and the corpus passes it. The
end-of-session ritual is named, split and built: `.claude/templates/handoff.md`,
`.claude/templates/retro.md`, `.claude/skills/retro/`, and a `PostToolUse` hook that runs the gate
when a journal lands. `raw/` is an inbox. S2 is open with all four blocking questions answered and
a sixth acceptance criterion added at opening.

**Not done.** The marked regions and the `asserts:` predicate set — the two remaining items that
block harness construction. The `idea` status is decided and not built. The `PreToolUse` lock on the
librarian dispatch is designed and not built.

**In flight.** Nothing. Tree clean at `e38a4ab`.

**Next step.** Build the marked regions, then the predicates. Add `idea` to the status set and to
rule 2. Establish the agent-dispatch matcher string, then write the `PreToolUse` lock.

**Checks.** `vault-check.sh` ok, seven advisories each named by a decision. `vault-check-selftest.sh`
caught 71, missed 0 — was 61 at session start. `hook-selftest.ps1` caught 40, missed 0 — was 29.
`vault-coverage.sh` seven of seven `INGEST COMPLETE`. `ruff check` and `ruff format` clean. **`pytest`
not run and no browser walk: no Python and no product code changed all day.**

## Entities

**Appeared.**

- `.claude/templates/` — a directory that did not exist. It holds `handoff.md` and `retro.md`.
- `.claude/skills/retro/SKILL.md` — the interrogation step that now precedes `/handoff`.
- `.claude/hooks/check-the-journal.ps1` — a third hook, `PostToolUse` on `Write|Edit`, narrowed
  inside the script to `raw/handoffs/*.md`.
- `quantity:` — a frontmatter field, on nineteen pages. Free text: it says why the number in a
  title is not a count.
- `archive/handoffs/` — a directory holding the old numbered handoff template.

**Changed.**

- `scripts/vault-check.sh` gained rule 10 and rewrote rule 8.
- `scripts/vault-check-selftest.sh` and `scripts/hook-selftest.ps1` both grew.
- `.claude/skills/handoff/SKILL.md`, `.claude/skills/ingest/SKILL.md`,
  `.claude/skills/vault-ask/SKILL.md`, `.claude/skills/vault-lint/SKILL.md`,
  `.claude/agents/vault-librarian/AGENT.md` and the repository's `CLAUDE.md` all lost their copies
  of the section mapping.
- `.gitattributes` pins `*.ps1` and `*.json` to LF, alongside `*.sh` and `*.md`.
- The vault's own `CLAUDE.md` gained a `quantity:` section, a corrected `authority` command, and a
  clause narrowing supersession.

**Taken out of service.** `raw/handoffs/TEMPLATE.md` — moved to `archive/handoffs/`, not deleted.
[[ingest-is-batched-at-the-retrospective]] — deprecated and archived.

## Decisions

**`/ingest` runs at the end of every session, and the batched page is retired.** Two `current`
pages, both `basis: human`, both dated 2026-08-16, answered one question differently. The owner
retired the earlier one; the successor takes `supersedes:` and `authority: ingest-cadence`. The
measurement the retired page rested on is not lost — the successor already carried it in the form
that survives: one dispatch, sources compiled one at a time inside it. **Rejected:** keeping both
with a resolved note, which leaves two live answers to one question.

**A title corrected in place is not a supersession.** Supersession is for a changed claim. Here the
filename is the identity — it is the search surface and what every wikilink resolves to — so
striking a stale number out of a title moves no address and strands nothing. Superseding on a title
change would mean a page is identified by its title, which is not how anything here addresses a
page. **Rejected:** full supersession for each of eighteen retitles, priced at eighteen new pages,
eighteen archived, and every inbound link rewritten. Renaming the *file* is the other operation and
is explicitly not this one.

**The end of a session is a retrospective, and `/handoff` follows it.** The sprint-level ritual is
renamed *sprint retrospective*. The word meant both for three days, and that ambiguity is what put
two contradictory answers in the vault about when `/ingest` runs. This settles the open half of
[[ingest-runs-after-handoff-at-the-end-of-a-session]], which recorded the decision to rename and
said the name was not chosen.

**Retro and handoff are different genres and stay apart.** Retro interrogates: it finds what the
session would not volunteer. Handoff routes: it files what retro found. *"Handoff literally means
lay out the session's data and let go"* — **owner:** — which is why its sections are named after the
folders they reach. **Rejected:** folding the interrogation into the handoff template, which would
produce a document that asks and classifies at once and give sections with no destination.

**The retro writes its own transit file, `.superpowers/sdd/retro.md`.** Kept apart from
[[vault-feedback-file]] on the property that makes each work: feedback is written in the turn the
observation is made and is raw; the retro file is written at the end and holds what has been
resolved. The retro reads the feedback file as evidence and does not drain it.

**No action queue.** The retro routes every action item into an address that already exists — a
deferral, a harness line, or nothing, in which case it was not a real item. **Rejected for now:** a
queue of its own, because a queue with no owner becomes a backlog nobody reads and `tasks/` has
been refused twice. Revisited when the project takes on tasks and Beads.

**An idea lives in `proposals/` with `status: idea`**, under the rule that **the folder is the KIND
of a record and the status is its MATURITY**. The owner first proposed `concepts/` with that status;
that was argued down on the record, because `proposals/` exists as a folder precisely so intent
cannot be filed as a record of something built — a failure that happened twice — and because the
schema knows two statuses and rule 2 enforces them. The reconciliation is that a status *is* the
right mechanism for half-thought against designed, and the folder still has to carry the guarantee.

**Product work does not interleave into S2.** The vault continues alone until the owner decides to
test it on the product. The stated default held; the product has not moved since 2026-08-12, and
that is now a decision rather than drift.

**S2 is open**, declared the same day S1 closed, with a sixth acceptance criterion added at opening
because the draft carried the harness build in through a closing paragraph and named it in no
criterion. **Rejected:** opening it next session, which would have started that session outside a
sprint again — the exact failure the owner had just named.

**Two divergences, recorded as decisions because that is what a divergence is.**

- **The librarian is the only writer of `wiki/`, and this session wrote it by hand** — thirty-seven
  pages had a title corrected or a `quantity:` field added, two had `sources:` repointed, one was
  retitled again at the retro. Each write was ordered by the owner, and the vault's own record says
  supersession and deletion belong to the owner's session. The count is stated plainly rather than
  left as a series of small permissions.
- **`git add -A` swept a deletion that was not this session's into this session's commit.** The
  owner had removed a design PDF while the commit was being assembled; he chose to leave it. The
  rule broken is written nowhere, which is part of the finding: staging by wildcard while the other
  party edits the tree is how an unrelated change acquires the wrong commit message.

## How it is built

**Rule 10 asks and does not judge.** No lexical predicate separates the two shapes: *"Two staleness
checks, at two different times"* is a violation, because there are three and the third arrived
without touching the page, while *"...are two different properties"* is not, because a third
property would make the page wrong rather than stale. The titles are grammatically identical. What
separates them is **whether the counted set belongs to the page or to the world outside it**, and no
script reads that. So the check flags and the page answers once, in `quantity:`, in free text
because the reason is the answer. Exempt without a declaration, each because it is not a count: a
code span, an ISO date, a digit glued to a letter, and the word *one*.

**Rule 8 reads the section set from the template and judges a journal only while it is uncompiled** —
while no `.coverage.tsv` sits beside it. The rule protects the ingest about to read the journal, so
it applies to what that ingest has not read; afterwards the form is history that `raw/` immutability
forbids correcting, and a rule failing forever on a file nobody may edit is an alarm you learn not
to read. This is what let the template change at all: journals in the older numbered form left the
rule's scope the moment they were compiled, and nothing had to be moved or rewritten. The hole is
named in the rule's own comment — a journal compiled before anyone runs the check is never judged —
and `/handoff` closes it by running the gate as its last step.

**A journal is told from a form by a property, not by a filename.** A journal carries a date in
`session:`; a form carries the placeholder. The rule used to skip the template by name, and **an
exception written by filename outlives what it excepted**. The same defect was removed from the lint
skill's coverage loop the same day.

**The mapping travels in two hops, each documented at its own source.** `.claude/templates/retro.md`
carries `→ handoff:` on every section; `.claude/templates/handoff.md` carries `→ ingest:` on every
section. Both skills read those lines rather than restating them. Before this the mapping existed in
six copies.

**The gate hook derives bash rather than naming it.** `bash` on the system PATH is the WSL shim and
Git's bash is not on PATH at all, and a hook is spawned by the OS rather than by an agent's shell.
It walks up from wherever `git` resolves until a `bin/bash.exe` appears — three levels on this
machine, two on a default install. Counting levels would have worked on one layout and been silent
on the other. Finding nothing, it says **THE GATE DID NOT RUN** and why.

## Lessons

**Measurement settled two design points that argument could not.** The word *one* fell out of the
title rule because all fourteen titles using it used it as a pronoun or an invariant, and the gap
between the criterion's expected eight violations and the measured thirty-seven proved the rule was
unenforceable as written rather than merely unenforced. Neither conclusion was reachable by
reasoning about it.

**Running a KNOWN-GOOD component through the same harness locates a fault in the harness.** The new
hook appeared silent on a deliberately malformed journal. The cheap move was not to read the new
hook again but to feed the same payload to the guard that had worked for four days; its identical
silence pointed at the payload in one step. Reusable: when a new thing looks broken, put an old
thing through the same test before believing the test.

**A test that fails for its own reasons proves nothing about its subject.** Twice in one session:
a hand-written JSON payload that was malformed, and a no-git case that stripped PATH and then could
not find its own interpreter. Both times the first reading was "the hook is broken" and both times
the hook was fine.

**Three claims were asserted from prose or from intention rather than from the file, and all three
were wrong**: that `vault-coverage.sh` skips the handoff template (it has never mentioned it), that
a supersession was "one movement" (twelve live pages cite the page), and that a line had been
written to `vault-feedback.md` when it had not. All three were corrected inside the session; the
first two had been repeated to the owner before being measured. The shape matters because the same
habit produced the false titles this session spent the morning removing.

**A copy of a list drifts from the list; a sweep cannot.** Two selftest cases had gone quiet:
`link_only_in_raw` and `fenced_link_reg` cleared the subject's inbound links from a copied list of
registers while the check reads a longer one, so when `tags.md` gained a link neither case tested
anything. Replaced by a sweep of the whole copy.

**An empty directory is invisible to the check this project trusts the tree to.** A stray empty `n/`
sat in the repository root for two days. Git does not track empty directories, so `git status` never
showed it — and `git status` is what every session reads before saying the tree is clean. It was
said three times that day, true of git and false of the disk each time.

**A placeholder that collides with real data is a message that has to be decoded.** Rule 8 printed
`unexpected [none]` when nothing was unexpected, and *none* is the exact word the template tells a
writer to put in an empty section.

**Pin a file class after it costs something, never before.** `*.sh` was pinned because CRLF breaks a
shebang in the container and `*.md` because awk and bash parse the vault's markdown. `*.ps1` and
`*.json` were pinned this session, after an edit script's LF anchors matched nothing in a CRLF file.
The index already held LF for all of them, so the pin changes nothing about the repository and
everything about the working copy, which is what scripts editing those files read.

## Deferred

**The marked regions and the `asserts:` predicate set** — the two items that still block harness
construction, in the order already agreed. Consequence: the harness goes on saying what nothing
checks, and the entity pages about the application cannot be written.

**`status: idea`, decided and not built.** The schema knows two statuses and rule 2 enforces them,
so `idea` has to be added in both, with a selftest case. Consequence: an idea still has nowhere to
go, which is the condition the decision was taken to end.

**A `PreToolUse` lock on the librarian dispatch.** Designed: a hook on the agent-dispatch tool,
narrowed by `subagent_type: vault-librarian`, denying while `vault-check.sh` exits non-zero.
Consequence until then: the expensive irreversible step — fifteen to thirty minutes that compiles a
journal and writes sidecars keyed by line number — can still be spent on a broken input. **One fact
must be established before it is written: the exact matcher string for the agent-dispatch tool.**
Guessing it produces a hook that never fires and looks identical to one with nothing to say.

**A gate that refuses work without an open sprint** — a `UserPromptSubmit` hook denying while
`sprint.md` declares no open sprint. `SessionStart` cannot do it: it injects context and has no way
to refuse. Consequence: nothing stopped this session from working a whole day outside a sprint, and
nothing would stop the next one.

**Moving `raw/` into the dated archive** — a slice of its own. Re-measured: 150 of 165 pages name
`raw/handoffs`, and 23 of those mentions sit in prose where the detector is blind.

**The rewrite of [[the-handoff-template-maps-onto-the-categories]].** Its title was corrected in
place; its body still says the section numbers are load-bearing, and twelve live pages cite it. The
rewrite is the librarian's at this ingest, and nothing enforces that it happens.

**`authority: handoff-template` stayed on a page whose claim changed.** Nothing decided it should;
nothing decided it should not.

## Feedback to the librarian

**Six of the lines below were written by the previous session and never drained** — the one that
produced `aebb308`. It wrote no journal at all, so `raw/` holds nothing for it and its findings have
been sitting in the draft since. They are carried here verbatim and marked, because attributing them
to 2026-08-17 would be wrong. Two of them also use a kind, `process:`, that the draft's own header
does not define — a fourth vocabulary that arrived without being agreed.

**Inherited from the previous session, undrained:**

- process: the closing ritual produces knowledge that the journal cannot contain, because the journal is written before it. This session: the ingest review found four titles carrying a count, and the start-clean check found the SessionStart hook's sort defect - neither existed when /handoff ran. raw/ is immutable so the journal cannot be amended, and vault-feedback.md is the carry: the vault is off-by-one on anything the closing ritual produces, and a reader of the next journal will see these findings attributed to the wrong session. One of the two was knowable earlier - the date-prefix collision is created by /handoff itself when it picks the filename, so that check belongs inside the skill that creates it.
- process: the brief's Alarms section is a queue only the owner can drain, and nothing bounds it. Three items stand on 2026-08-17, two of them supersessions owed since 2026-08-16. An unbounded list that one person alone can shorten will stop being read, which is the failure the density advisories already demonstrate one level down - and the sprint is currently trying to close that very thing as criterion 1.

**Written this session:**

- lint: the ingest-cadence supersession of 2026-08-17 left four live citations arguing from an archived page. `wiki/concepts/claude-md-can-lose-an-assertion-but-cannot-strand-a-page.md` row 6 and `wiki/lessons/no-rule-reads-a-harness-file.md` row 5 both cite [[ingest-is-batched-at-the-retrospective]] as the half of a divergence against `.claude/skills/ingest/SKILL.md`; with the page retired, the skill's line *"one source at a time - never batch several handoffs"* is now correct about compilation and the divergence is only about dispatch, which is what the successor already says. `wiki/lessons/agent-round-trip-cost.md` cites it for the cost arithmetic, which survives, and `tags.md` cites it in a definition. None is a broken link - archive/ resolves - which is exactly [[a-live-page-can-argue-from-a-deprecated-one]] happening again, this time caused by a write rather than found in one.
- lint: the project intends to adopt **Beads** for task tracking later, owner 2026-08-17. Nothing is designed and nothing depends on it yet; it is recorded because the action-queue decision is explicitly deferred *to* it, and a deferral that names no destination is a deferral nobody can pick up.
- measure: the cost of moving `raw/` into the dated archive, re-measured 2026-08-17 at `b6fc6d8`: **150 of 165 pages in `wiki/` name `raw/handoffs`, and 23 of those mentions sit in prose** rather than in `sources:`. [[moving-raw-into-a-dated-archive]] records 115 of 124, which was true when written; the corpus grew and the ratio grew with it. The prose figure is the one that matters, because the detector is complete for `sources:` and blind in prose ([[a-rewriter-must-be-paired-with-a-detector]]).
- lint: **the handoff mapping was copied into six files, and the copies were found only by grepping for a number.** Dropping the section numbers on 2026-08-17 forced a sweep, and `section 7` turned up in `.claude/skills/ingest/SKILL.md`, `.claude/skills/handoff/SKILL.md`, `.claude/skills/vault-ask/SKILL.md`, `.claude/agents/vault-librarian/AGENT.md`, the repository's own `CLAUDE.md`, and `raw/handoffs/TEMPLATE.md` itself. None of them was wrong when written; they drifted by the template changing under them, which is exactly the failure [[marked-regions-and-the-prose-outside-them]] is designed to make impossible. **This is the measured case for that design**: six copies, no detector, and the only reason they were all found is that the thing they copied happened to be a distinctive string. A renamed heading would not have been.
- lint: **a hook cannot call bash on this machine, and the answer is derived rather than written down.** `bash` on the system PATH is the WSL shim; Git's bash is not on PATH at all ([[session-hooks]]). The hook finds it by walking up from wherever `git` resolves until a `bin/bash.exe` appears - three levels here, because `git` sits in `Git/mingw64/bin` while bash sits in `Git/bin`, and a default install puts `git` in `Git/cmd` where the same walk finds it two levels up. Counting levels would have worked on one layout and not the other. When it finds nothing it says **THE GATE DID NOT RUN** and why, which is the branch the selftest exercises by taking git off PATH.
- lint: **two test-harness defects found while proving the hook, both of the same shape: a test that fails for its own reasons proves nothing.** (1) Piping a hand-written JSON payload from bash into `powershell -File` produced silence from the NEW hook and from the KNOWN-GOOD guard alike - the payload was malformed, not the hooks. Building it with `ConvertTo-Json` fixed both. (2) The no-git case stripped PATH and then invoked `powershell` by name, so it failed for want of its own interpreter; it now resolves the interpreter through `$PSHOME`. In both cases the first reading was "the hook is broken", and in both cases the hook was fine.
- lint: `.gitattributes` pins `*.md` and `*.sh` to LF and says nothing about `*.ps1`, which are therefore CRLF on disk. Noticed by an edit script whose anchors used bare LF and matched nothing. Harmless today because PowerShell reads either, but it is the third file class in this repository whose line endings are decided by whatever wrote it last. **Outcome the same day: `*.ps1` and `*.json` pinned to LF, four working copies converted, hook selftest re-run against them and still 40 of 40.**
- lint: **an empty directory is invisible to the check this project trusts the tree to.** A stray empty `n/` sat in the repository root from 2026-08-15 until the owner spotted it by eye on 2026-08-17. Git does not track empty directories, so it never appeared in `git status` - and `git status` is what every session reads, twice, before saying the tree is clean. It was said three times on 2026-08-17, and each time it was true of git and false of the disk. Origin is almost certainly a hand-typed command whose escape was eaten, the same family of defect that cost two debugging passes the same day.
- miss: **the brief called the third supersession one movement, and it is twelve.** I repeated that framing to the owner before measuring. [[the-handoff-template-maps-onto-the-categories]] is cited by **12 live wiki pages**, and most cite it for claims that are still true - the state section is never compiled, `raw/` is immutable, it is the only channel from a session to the librarian. Only its numbering claim died. So the page needs a REWRITE by the librarian at the next ingest, not a retirement: retiring it would strand twelve citations and archive a page whose live content has nowhere else to go. Its title was false as of 2026-08-17 and was corrected in place the same day; the body is what the rewrite has to fix.

## Anything else worth keeping

**The retro earned its place on its first run, and here is the evidence rather than the claim.**
Three things reached this journal only because the interrogation step ran before it: the count of
hand-written `wiki/` edits, which read as routine one permission at a time and as a divergence in
one line; the three claims asserted without checking, two of which had been repeated to the owner;
and the gap in S2's criteria, which surfaced under *what fell out without a decision* and became the
sixth criterion. None would have been in a journal written straight after the work.

**`docs/retro.md` was a reference from another project**, dropped in by the owner to show the shape
of a retrospective and removed by him the same day. It is named here because a foreign skill file
sitting in `docs/` would read as this project's own to a session that found it later.

## Harness

- harness: the librarian's monopoly on wiki/ needs a stated exception. Owner permitted the main session to edit four titles directly on 2026-08-17, after the librarian had returned: no concurrency, and the owner reviews the diff before the commit. Today the rule reads as absolute and the guard hook says so, so every such repair is an undocumented divergence. The rule owes a clause: who may write wiki/ when the librarian is not running, and what makes it safe (no parallel writer, review before commit). **[inherited, previous session]**
- harness: the SessionStart hook picks the newest journal with 'Sort-Object Name -Descending | Select-Object -First 1', which orders two journals sharing a date prefix ALPHABETICALLY BY SLUG, not chronologically. **[inherited, previous session]**
- harness: OUTCOME for the SessionStart sort defect above - fixed 2026-08-17 in .claude/hooks/session-brief.ps1 by the main session, not the librarian, under the same permission as the four titles. The check now asks whether each journal has a .coverage.tsv sidecar instead of comparing the brief's 'ingested:' against whichever name sorts last, and a second cheap clause fires when the brief names a journal that does not exist. Proved in both directions before committing. **[inherited, previous session]**
- harness: **the end-of-session ritual is named and split in two, owner 2026-08-17.** The end of a session is a **retrospective** - "retro" - and `/handoff` follows it. The sprint one is renamed "sprint retrospective" and is not designed yet.
- harness: **retro becomes a step of its own, with its own skill and its own template.** Retro interrogates, handoff routes.
- harness: **the retro writes its own transit file, `.superpowers/sdd/retro.md`**, beside [[vault-feedback-file]] and not inside it. Feedback is written in the turn the observation is made and is raw; the retro file is written at the end and holds what has been resolved.
- harness: **the list of open questions is built on every session; the conversation is offered.** Building the list is not optional - a session cannot judge that it has no open questions, since not seeing them is the failure. An owner who skips the conversation has deferred the questions, which is a resolution; silence is not.
- harness: **no action queue for now.** Revisited when the project takes on tasks and Beads.
- harness: the mapping now lives in `.claude/templates/handoff.md` alone - each section carries a `→ ingest:` line and `/ingest` reads them there. `.claude/templates/retro.md` carries the other hop, `→ handoff:`, for the same reason.
- harness: **the gate runs as a `PostToolUse` hook** on `Write|Edit`, narrowed inside `.claude/hooks/check-the-journal.ps1` to `raw/handoffs/*.md`. Post rather than Pre because the condition being checked is the journal EXISTING; blocking is off the table for the same reason, so the hook is loud instead.
- harness: **the handoff template left `raw/` by being ARCHIVED, not deleted.** Deleting it would have falsified provenance. It sits at `archive/handoffs/TEMPLATE.md` and both citing pages point there. `raw/` now holds nothing but journals.
- harness: `.claude/skills/vault-lint/SKILL.md` no longer skips `*/TEMPLATE.md` in its coverage loop. Measured after removing it: seven of seven sources report `INGEST COMPLETE`. The migrated 2026-08-12 document carries no frontmatter at all, so it could not have been filtered by a field either.
- harness: **S2's fourth blocking question is answered: the vault continues alone and product work does not interleave.**
- harness: **an idea lives in `proposals/` with `status: idea`**, under the rule that the folder is the KIND of a record and the status is its MATURITY. **Not built**: the schema knows two statuses and rule 2 checks them, so `idea` has to be added in both, with a selftest case.
- harness: **a gate that refuses work without an open sprint** - deferred, design agreed: a `UserPromptSubmit` hook that denies while `sprint.md` declares no open sprint. `SessionStart` cannot do it.
- harness: **the gate should also refuse the ingest, not only report the journal** - owner's reading, and it is right. The shape: a `PreToolUse` hook on the agent-dispatch tool, narrowed by `subagent_type: vault-librarian`, returning `permissionDecision: deny` while `vault-check.sh` exits non-zero. **One fact must be established before it is written: the exact matcher string for the agent-dispatch tool in this harness.** Guessing it produces a hook that never fires and looks identical to one that has nothing to say.
