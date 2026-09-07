---
session: 2026-08-19
sprint: S2
commits: 3c5dd8f..bade6c9
---

# Handoff — 2026-08-19

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

## State

**Done.** Three of the brief's alarms were put to the owner and answered, and two of the three were
executed in the tree. The vault's `CLAUDE.md` gained a `## Who writes what` section naming who may
write the gate's own input. `basis` moved from `optional:` to `required:` in all six
`wiki/*/_schema.yaml`. And **`scripts/vault-check-selftest.sh` was found red, diagnosed, and
repaired** — it had been reporting `caught 24, missed 96` against a corpus whose only changes since
the last ingest were two `probe/RUNBOOK.md` commits.

**Not done: the guard.** The owner chose it as this session's body of work. It was not started,
because the instrument that would have verified it was returning a fifth of its cases. Building it
would have produced something unverifiable that looked finished. He was told plainly at the end and
re-chose commit-and-ritual over starting it then.

**In flight: nothing.** Two commits, `71c79e9` and `bade6c9`, and the working tree carries only the
untracked `probe/instructions-loaded.log`.

**Next step**, in this order: the guard as a branch in `.claude/hooks/ask-the-vault.ps1` reading
`.claude/rules/`; then the AST rule's move, which waits on it; then the `record-schema` sweep and
the three trim candidates at `/vault-lint`, ratified as a deferral at this retro.

**Checks.** `bash scripts/vault-check.sh` exits 0, prints `ok`, with **20 advisories** and zero
`note` lines — nineteen tag density and one region coverage at `1 of 14`, unchanged.
`bash scripts/vault-inject.sh` reports **0 rewritten, 0 problems**. `bash
scripts/vault-check-selftest.sh` reports **caught 120, missed 0**, restored from `caught 24,
missed 96`. `pytest`, `ruff check` and `ruff format` were **not run and correctly so** — no product
code was touched, which is what the sprint's fourth blocking question decided.

## Entities

**Changed: `scripts/vault-check-selftest.sh`.** Its sandbox now mirrors the repository rather than
renaming the vault into `vault_copy`, its `governs:` sweep runs before the `sources:` placeholder
loop, and it carries a new case runner, `run_found`, which grades a case on whether discovery landed
on a real vault instead of on a whole-run green.

**Changed: the six `wiki/*/_schema.yaml`.** `basis` is `required:` in every one, with a three-line
comment above it naming the ruling and citing the page it is written on, as their own header rule
demands.

**Changed: `job_hunt_ai_vault/CLAUDE.md`.** A `## Who writes what` section, immediately after the
opening paragraph, stating the one-writer rule, the registers clause of 2026-08-17, and the new
clause about the gate's input.

**Appeared: nothing.** **Taken out of service: nothing.**

## Decisions

**owner: what the gate reads as its own input is the session's to write — `job_hunt_ai_vault/CLAUDE.md`
and every `wiki/*/_schema.yaml` — the owner reads the diff before the commit, the librarian writes
neither, and no divergence is recorded for either.** *Rejected:* the librarian's, like the registers;
and the owner's alone. *Why:* this file is the librarian's own instructions and the schemas constrain
what it may write, so a librarian writing them is the one arrangement in which a change has no reader
but its author. What made the two hand-edits of 2026-08-19 safe was never the recording — it was that
no librarian was running and that the change was a `git diff` the owner read, and the clause states
those two properties instead of the paperwork. *It now obliges:* the two divergences already on the
record stand as history and are not retracted; the clause the brief has asked for twice is closed.
**The `_schema.yaml` half widened the question as it was asked and was put to the owner separately
before it was taken.**

**owner: `basis` is core.** *Rejected:* leaving it `optional:` and saying so on the frontmatter-core
page. *Why:* that page already calls it *"the only field conflict resolution rests on"*, and a field
conflict resolution rests on cannot be one a page may omit. **The argument runs from the decision and
explicitly not from the corpus** — reasoning from what every page happens to carry is how `quantity:`
entered this store. *It now obliges:* the enumeration check is still owed and `basis: banana` passes
today; the owner was offered it in the same question and took the narrower option.

**owner: what an archived page *asserts* is frozen; how it is *found* is live.** *Rejected:* both
options the question was framed with — `archive/` as frozen testimony like `raw/`, and `archive/` as
live retired content. *Why:* the two rules disagreeing about `archive/` are not both answered by a
widening. Rule 6 governs findability, so it reaches `archive/` — an archived page carrying a word the
dictionary no longer defines is a real defect, found live in the `schema` tag split. Rule 10 governs
what a title asserts, so it does not — [[the-wiki-has-five-folders-and-tasks-is-not-one]] is archived
*because* its count went stale, and repairing it erases the evidence. *It now obliges:* every rule
written against `wiki/` from now on is answered by asking which half it governs, instead of
inheriting the question. **Recorded and not built** — the owner deferred the check change so it would
not eat the session's body.

**owner: the selftest's sandbox is fixed by making it a faithful mirror, not by pointing the check at
its copy.** *Rejected:* exporting `VAULT=` for every case except the two rename cases — five lines,
against roughly seventy. *Why:* it removes the ambiguity and stops exercising discovery in 118 of 120
cases, to work around a sandbox that is not a faithful mirror rather than to make it one.

**owner: `the vault is renamed` is graded on the one question it asks.** *Rejected:* having the
mutation rewrite the eleven citations as it renames, which would restore the green and hide the
finding; and leaving the case red. *Why:* the case exists to prove discovery finds a vault whose name
is nothing like ours and carries spaces, and that half passes — visible in the very output that
failed it. It was asserting a second property nobody chose, that the corpus does not name its own
directory, and that property is false eleven times over.

**owner: the A1 clause's text and the schema comments stand as written.** Put to him after the commit
rather than before, which is the divergence below; ratified unchanged.

### Diverged

**`CLAUDE.md` requires `/pre-task` before implementing anything non-trivial, and it was not run** —
while the session changed a gate script by 149 insertions and 82 deletions and promoted a frontmatter
field across six schemas. *What was done instead:* the vault was read by hand, which `CLAUDE.md`
prescribes when an agent cannot be dispatched. *Rejected:* dispatching the librarian, which a session
instruction forbade outright. **Why it looked unnecessary at the time:** that instruction made the
ritual literally unavailable, and the by-hand paragraph reads as its substitute. **It is not one** —
it substitutes for `/vault-ask`, and the two differ in exactly the way that matters, one asking about
a topic and the other checking a plan against what is already decided. **The rule has no by-hand
form, and that is the divergence's cause rather than its excuse.**

**The A1 clause requires the owner to read the diff before the commit, and the commit that introduced
the clause did not wait for that.** *What was done:* he approved *committing*, having been shown only
the selftest's code diff, and the commit followed. **Why it looked unnecessary:** his "commit and
ritual" read as covering the whole tree, and the clause was two hours old and not yet a habit.
*Remedied inside the session* — the text was put to him and ratified — **but the property was not
exercised at the moment the clause names**, on the clause's first application.

## How it is built

**A fixture that renames what the corpus names by name stops being a fixture of that corpus.** The
selftest copied the vault to `vault_copy` while the corpus cites paths from the repository root, and
eleven of those citations point inside the vault itself. None resolved, so the placeholder loop
materialised `job_hunt_ai_vault/wiki/decisions/_schema.yaml` as an empty file — **and a directory
holding a `wiki/` is the whole of what vault discovery looks for.** The decoy sorted before
`vault_copy` and won every case. **The failure is silent and it runs in the direction of the sandbox
looking fine**, because everything it breaks is reported as an ordinary red the reader attributes to
the case under test.

**A destination that is also a citation loses to whichever loop runs first.** `CLAUDE.md` is both a
`governs:` destination and a `sources:` citation. With the placeholder loop first, the empty
placeholder won over the real file, and the `governs:` sweep's `[ -e ] && continue` guard read it as
already materialised. The comment ten lines above that guard had already stated the consequence —
*"An empty placeholder would satisfy the path and fail the comparison, which is a green that means
nothing"* — and the ordering defeated it. **Ordering is the fix rather than a `[ -s ]` test**, because
an empty file can be a legitimate destination and what is actually true is that the real file wins
over a placeholder standing in for it.

**An exit code read through a pipe belongs to the last stage.** `bash selftest.sh | tail -20` returns
`tail`'s status; `bash selftest.sh > f; grep SELFTEST f` returns `grep`'s. Both are 0 whenever the
last stage succeeds, which it always does. **A measurement of a command's status is only a
measurement when nothing is downstream of it** — capture into a variable on the very next statement.

**What survives a compaction is whatever has something that runs it again**, and delivery is
triggered by the **Read tool** rather than by touching a matching path. Measured in the previous
session and reaching the vault only now: `/compact` fires its own reload event and reloads only the
unscoped project memory; a path-scoped rule's trigger is a Read that already happened and does not
happen again on its own; and an Edit on a matching path delivers nothing at all. **The Edit tool's
read gate is *session*-scoped, not context-scoped**, so it survives a compaction and lets a
post-compaction edit through with no rule in context and no signal that one is missing. Every other
route — a fresh session, a subagent, a first touch of the file — goes through a Read and does get the
rule.

**A `PreToolUse` hook on `Edit|Write` already runs in this repository, and has since 2026-08-13.**
`.claude/settings.json` registers `.claude/hooks/ask-the-vault.ps1` under exactly that matcher, and
it narrows by path inside the script. So a guard for the path-scoped rule is **a fourth branch in a
script that already spawns**, not a new hook, and the latency the previous session queued up to
measure is sunk. The script's own header already carries the principle such a guard needs: *"A guard
on every edit becomes a ritual performed without reading; a guard on rule-bearing paths fires exactly
where the recorded divergences happened."*

## Lessons

**A number quoted from a run that was not repeated against the tree it is being read on is not a
measurement.** `sprint.md` reads criterion 1 against `caught 120, missed 0`. That figure was measured
on 2026-08-19 **before the page carrying the new `_schema.yaml` citations was compiled in the same
ingest**, and it stopped being true the moment that page landed. Nobody ran the suite again for six
days. Measured this session: **caught 24, missed 96**, reproducing with the schemas reverted to their
committed state.

**A claim labelled *measured* was written from an instrument that reported its own exit code, three
times in one hour, and the third time was while correcting the second.** The session filed that the
suite *"exited 0 throughout, at 24/96 as at 119/1"* and drew a decision out of it — that the exit
code does not read the score. **Both are false.** The script's last line is `[ "$fail" -eq 0 ]`;
measured with one case planted broken, it returns **1**. And the run that produced that correction
ended in a `grep -c` over zero matches, so the harness reported the measuring task as *failed* while
its number was right. **This store already holds the same shape twice** —
[[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]] and
[[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]].

**A test can be green on placeholders rather than on truth, and the placeholders can be its own
setup's.** `run_clean "the vault is renamed"` passed for six days because the sandbox renamed the
vault, so the eleven citations spelling `job_hunt_ai_vault/...` resolved against empty files the
setup had just created. Removing the rename removed the placeholders and the case failed **on a true
statement about the corpus**.

**A retro file that is an unfilled template is worse than an absent one.** The previous session's
`.superpowers/sdd/retro.md` still carried `session: YYYY-MM-DD` and every instruction paragraph, with
the only verdict tokens in it being the ones inside the instructions. **The `/retro` skill names its
failure mode as silence** — *"a session that skips this skill produces no file at all, which looks
the same from the outside as a session with nothing to confess"*. This is a third state nobody named:
the file exists, it is the right size, it opens on the right heading, and it says nothing. Absence is
at least visible to `test -f`.

**The first published diagnosis of a failure can be a real defect and still not be the cause.** Loop
ordering was a genuine bug and fixing it moved the suite from 24 to 86 caught; the cause was the
renamed vault, and the remaining 34 were behind it. **Publishing the first true finding as *the
cause* is the error**, and it was corrected in the same file that carried it, with the earlier line
named.

## Deferred

**The guard, and with it the AST rule's move.** *Consequence of not doing it:* the rule stays in
`CLAUDE.md` and reaches every session unconditionally, which is the safe default; region coverage
stays at `1 of 14`; and the sprint's own *next* line stays where it is. **What changed is the blocker
and not the schedule** — it was the probe, the probe is answered, and now it is the guard. Its shape
is settled: a branch in `ask-the-vault.ps1` that reads `.claude/rules/*.md`, matches each file's
`paths:` against the payload's `file_path`, and injects that file's body, so the rule is defined once
and both triggers hand out the same text. **Its honest cost:** on a normal Read→Edit flow the rule
arrives twice, and the hook cannot see the context to know.

**Rule 6's widening to `archive/`.** The ruling is taken; the check change is not built. *Consequence:*
an archived page carrying a tag the dictionary does not define still passes in silence, which is how
the `schema` split nearly stranded three of them. Its size is already measured on
[[what-archive-is-stays-undecided-and-the-rules-reading-wiki-disagree-about-it]].

**The `basis` enumeration check.** The owner was offered it in the same question as the promotion and
took the narrower option. *Consequence:* `basis: banana` passes today, on a field that now decides
every conflict.

**The `record-schema` sweep and the three trim candidates at `/vault-lint`.** These **fell out of the
session silently** — the brief named them in its *next* list and nothing raised them. *Surfaced at
the retro and ratified as a deferral by the owner:* they go to `sprint.md` as `next`, so the journal
carries them explicitly rather than a second brief carrying them silently.

**Pinning `*.yaml` to LF.** *Consequence:* `git checkout` writes the six schema files with CRLF, on a
class that now holds a gate input parsed by the same awk the `*.md` pin exists for. **Measured and not
acted on**: the gate exits 0 and prints `ok` with all six in CRLF, so the standing rule —
[[a-file-class-is-pinned-after-it-costs-something]] — says do not pin it.

**Making the selftest cheaper.** It copies the whole vault and runs the whole gate 120 times, and both
grow with the corpus. *Consequence:* roughly five minutes a run on an idle machine, and rising.
**Named as a candidate rather than a task**, because a faster suite that silently stops checking is
the worse failure, and this store has retired a rule for costing 71 seconds at 75 pages and growing
as the square.

**Deleting the probe scaffolding.** Conditional on probe 4's answers reaching `wiki/`, which this
ingest is. *Consequence while it stands:* `.claude/rules/_probe-paths.md` is one of the fourteen files
the region advisory counts.

## Feedback to the librarian

Drained verbatim from `.superpowers/sdd/vault-feedback.md`. The first two entries were written by
the previous session, after its journal had been ingested, and are carried here because that is what
that file is for.

- process: probe 4 was measured on 2026-08-19 **after this session's journal was written and
  ingested**, so the vault does not hold it and `brief.md`'s alarm still says the probe is unrun -
  which is now false in its first half and still true in its second. The answer, both instrument
  readings and the two unplanned findings are in `probe/RUNBOOK.md`, committed as `b5e9698`; it is
  written to be compiled from. **Carry it into the next journal and let the ingest file it**, then
  delete `probe/`, `.claude/rules/_probe-paths.md`, `.claude/hooks/instructions-loaded.ps1` and the
  `InstructionsLoaded` block in `.claude/settings.json`, which that file's closing paragraph makes
  conditional on exactly this. The finding gates a live decision: **the AST boundary rule does not
  move into `.claude/rules/` without a guard**, because a governed file read before a compaction and
  edited after it is edited with no rule in context and no signal that one is missing.

- process: the owner rejected `PreToolUse` on `Edit|Write` as the guard for the path-scoped rule
  (2026-08-19, in chat, after probe 4): it fires on **every** edit and write, and scoping is the
  whole reason `.claude/rules/` with `paths:` was being tried in the first place. Not a closed
  decision - he said the next session works it out - but do not re-propose it without answering
  this. **One thing to carry into that session, because it narrows the objection rather than
  answering it:** the hook does receive the tool input including `file_path`, so it can match the
  path and exit immediately, and no scoping is actually lost. What is lost is a PowerShell process
  spawned on every `Edit|Write` in the repository. So the cost is latency on every edit, not a
  mechanism that cannot tell which file it is looking at - and that is the number to measure before
  the option is either taken or dropped.

- process: **owner's ruling, 2026-08-19 — who writes the gate's own input.** The clause the brief has
  asked for twice is taken and it covers **two** files, not one: `job_hunt_ai_vault/CLAUDE.md` **and**
  every `wiki/*/_schema.yaml`. **What the gate reads as its own input is the session's to write**, the
  owner reads the diff before the commit, the librarian writes neither, and **no divergence is
  recorded for either**. The reason on the record is not convenience: this file is the librarian's own
  instructions and the schemas constrain what it may write, so a librarian writing them is the one
  arrangement in which a change has no reader but its author — and what made the two 2026-08-19
  hand-edits safe was never the recording but the absent librarian and the read diff. The clause is
  written into `job_hunt_ai_vault/CLAUDE.md` under a new `## Who writes what`, by the authority it
  itself grants. **The `_schema.yaml` half is a widening of the question as asked and was put to the
  owner separately before it was taken.** The two divergences already on the record stand as history;
  they are not retracted. Pages owed: the clause, and the correction to
  [[the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed]], whose
  closing paragraph is now answered.

- process: **owner's ruling, 2026-08-19 — `basis` is core.** It moves from `optional:` to `required:`
  in all six `_schema.yaml`, executed the same turn, with a three-line comment above it naming the
  ruling and citing [[the-frontmatter-core-is-fixed-and-updated-joins-it]] — the header rule demands a
  decision behind any such move and demands it name its page. **The argument runs from the decision,
  not from the corpus**: that page already calls `basis` *"the only field conflict resolution rests
  on"*, and a field conflict resolution rests on cannot be one a page may omit. The corpus figure is
  corroboration and was explicitly not the reason, which is the distinction
  [[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]] exists to keep.
  **Measured after the change: `vault-check.sh` exits 0 and no page reddens** — `basis` is on **329 of
  329** pages in `wiki/`, five values, `human` 167 / `code` 94 / `measurement` 55 / `inference` 11 /
  `external` 2. The brief's figure of 321 was the pre-ingest count. Page owed: the ruling onto
  [[the-frontmatter-core-is-fixed-and-updated-joins-it]], which asked the question and says *"this page
  should say so"*. **Still owed and not taken this turn:** the enumeration check — `basis: banana`
  passes today, and it is the first of the three debts that page names.

- process: **owner's ruling, 2026-08-19 — what `archive/` is.** Neither of the two options the question
  was framed with was taken. **What an archived page *asserts* is frozen; how it is *found* is live.**
  So rule 6 (every tag is defined in `tags.md`) **widens to `archive/`** — findability is live, and an
  archived page carrying a word the dictionary no longer defines is a real defect, found live in the
  `schema` tag split. Rule 10 (no measurable quantity in a title or filename) **does not widen** — the
  title is what the page asserts, and [[the-wiki-has-five-folders-and-tasks-is-not-one]] is archived
  *because* its count went stale, so repairing it erases the evidence. **The value of the ruling is
  that it is a predicate rather than a verdict**: every rule written against `wiki/` from now on is
  answered by asking which of the two halves it governs, instead of inheriting the question.
  **Recorded, not built** — the owner deferred the check change so it would not eat this session's
  body of work. What it costs when it is built is already measured on
  [[what-archive-is-stays-undecided-and-the-rules-reading-wiki-disagree-about-it]]: four archived pages
  carry a count, three were touched by the tag rename. Pages owed: the ruling, and the retirement of
  that page's deferral.

- process: **the `PreToolUse`-on-`Edit|Write` objection was taken against a cost this repository has
  already been paying since 2026-08-13, and the corpus says so on a page nobody opened.** The owner
  rejected that hook as the guard for the path-scoped rule because *"it fires on every edit and write,
  and scoping is the whole reason `.claude/rules/` with `paths:` was being tried"*. But
  `.claude/settings.json` registers `.claude/hooks/ask-the-vault.ps1` under exactly that matcher, and
  [[session-hooks]] states it in its own table — *"`PreToolUse` | `Edit|Write`, narrowed again by path
  inside the script"*. **A PowerShell process is already spawned on every Edit and Write in this
  repository**, so the latency the previous session queued up to measure is sunk, and the measurement
  is not owed. **What this makes the guard is a fourth branch in a script that already runs, not a new
  hook** — zero new processes. And the script's own header already carries the principle the guard
  needs, written for the same reason: *"A guard on every edit becomes a ritual performed without
  reading; a guard on rule-bearing paths fires exactly where the recorded divergences happened."*
  **This is the shape [[deriving-what-the-vault-already-holds-costs-a-round]] names**, arriving on a
  live decision rather than on a criterion: the question *"what would a guard cost"* was reasoned out
  from scratch across two sessions while an entity page answered it. Recorded so the retro has the
  finding and not just the fix.

- lint: **[[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]] is false in its title, and probe 4
  is what falsified it.** The page holds `authority: scoped-rule-trigger` and `basis: human` — the
  owner's reading, deliberately not `external`, that *"the read the rule needs is the one the editing
  tool already demands"*. Its table's second row says an Edit on a matching path delivers the rule
  **"yes, by implication"**. Probe 4 measured that row false: the Edit tool's read gate is
  **session**-scoped rather than context-scoped, so it survives a `/compact` and lets an Edit through
  with no read in context — and the hook log shows the Edit produced **no line at all**, meaning
  delivery never fired rather than firing unseen. **Delivery is triggered by the Read tool, not by
  touching a matching path.** The consequence is not confined to compaction: the same gate makes the
  fourth and fifth rows (*creating a new file*, *a Bash command*) right for a reason the page does not
  give, and it makes the second and third rows true only while nothing has cleared the context. **This
  is the page the movability criterion rests on**, cited by
  [[moving-a-rule-into-claude-rules-with-a-paths-scope]] to decide which of nine rules can move, so
  the correction reaches that decision and not only this page. Its own closing section already names
  probe 4 as the measurement that would settle it; the measurement came back against it. **The
  retitling and the supersession are the librarian's and the owner's, not this session's.**

- miss: **`vault-check-selftest.sh` is red and has been, and the `caught 120, missed 0` that
  `sprint.md` reports criterion 1 against was not re-run against the tree that now exists.** Measured
  2026-08-19 on a corpus whose only changes since the ingest are two `probe/RUNBOOK.md` commits: the
  suite reports **caught 24, missed 96**, and it reports the same failure with the `_schema.yaml`
  files reverted to their committed state, so **the `basis` promotion is not the cause** — the
  baseline run reached 63 missed before it finished. **The cause is an ordering bug between two
  sandbox-construction loops.** The `sources:` placeholder loop runs first and creates
  `$PRISTINE/CLAUDE.md` as a **zero-byte file**, because current pages cite `"CLAUDE.md"` in
  `sources:`. The `governs:` loop then runs and opens with `[ -e "$PRISTINE/$dest" ] && continue`, so
  it skips the destination it was written to materialise and the real file is never copied. **The
  comment ten lines above that guard states the consequence exactly** — *"An empty placeholder would
  satisfy the path and fail the comparison, which is a green that means nothing"* — so the failure
  mode was understood and the ordering defeated it. What the sandbox then reports is ambient red:
  `CLAUDE.md:65` and `:84` *"not a marker alone on its line"*, and `marked regions cover 0 of 14`
  against the real tree's `1 of 14`. **Every frontmatter case goes MISSED behind it.** The fix is
  ordering, not a new condition: run the `governs:` loop first, since the `sources:` loop already
  guards with `[ -e ] ||` and will not clobber. **The lesson is the one this suite exists to prevent,
  committed inside the suite**: a number quoted from a run that was not repeated against the tree it
  is being read on ([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]],
  [[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

- measure: **`_schema.yaml` is not pinned to LF and `git checkout` writes all six with CRLF.**
  Measured by counting CR bytes rather than by `grep`, which this store has already recorded returning
  a line count instead ([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]): after a
  `git checkout --` of the six files, each carries 29-30 CR bytes; the blob at HEAD carries 0, and the
  files as written by a bash tool carry 0. `.gitattributes` pins `*.sh` and `*.md` and names the exact
  reason for the second — *"parsed by awk and bash, on the host and in the container alike: a CR is a
  byte inside the field, not a line ending"* — and `_schema.yaml` is parsed by that same awk, in
  `vault-check.sh`'s schema loop. **Reported and not acted on, because it has not cost anything yet**:
  measured the same turn, `bash scripts/vault-check.sh` exits 0 and prints `ok` with all six schemas
  in CRLF, so the parser tolerates it today. That is the standing test on
  [[a-file-class-is-pinned-after-it-costs-something]], and this is a third class arriving at it after
  `*.tsv` and `*.yaml` elsewhere. **What it did cost is diagnosis time**, which is not the gate's
  correctness and is not offered as the trigger.

- process: **the selftest's sandbox renamed the vault, and that is what broke it — the fix is to stop
  renaming it.** Correcting the `miss:` above, which named the loop ordering as the cause: ordering
  was **a** defect and not **the** one. `cp -r "$REPO/$VAULT_DIR" "$PRISTINE/vault_copy"` renamed the
  vault inside a sandbox whose whole job is to be the repository, while **the corpus cites paths from
  the repository root and eleven of those citations point inside the vault itself** — six at
  `job_hunt_ai_vault/CLAUDE.md`, two at `job_hunt_ai_vault/wiki/decisions/_schema.yaml`, and one each
  at `sprint.md`, `index.md` and `pages.base`. Under the renamed copy none resolved, so the
  placeholder loop materialised `job_hunt_ai_vault/wiki/decisions/_schema.yaml` as an empty file —
  **and a directory holding a `wiki/` is the whole of what vault discovery looks for.** The decoy
  sorted before `vault_copy` and won every case. **The date is readable off the corpus**: the two
  `_schema.yaml` citations were compiled on 2026-08-19, in the same ingest that created those files,
  and the `caught 120, missed 0` of that day was measured before the page carrying them landed.
  **Rejected: pointing the check at the copy with `VAULT=`** — five lines, and it stops exercising
  discovery in 118 of 120 cases to work around a sandbox that is not a faithful mirror rather than to
  make it one; discovery keeps the two rename cases it already had. **The ordering fix is kept on its
  own merits**: `CLAUDE.md` is both a `governs:` destination and a `sources:` citation, and with the
  placeholder loop first the empty file won over the real one. **The general shape is worth a page:
  a fixture that renames what the corpus names by name stops being a fixture of that corpus** — and
  it fails silently, in the direction of a green exit code.

- lint: **the corpus cites the vault by its literal directory name eleven times, so the vault cannot
  be renamed without a rewrite — and nothing had recorded that.** Surfaced by the mirrored sandbox:
  with the copy no longer renamed, `run_clean "the vault is renamed"` fails, and the eleven lines it
  prints are `sources names a path that does not exist: job_hunt_ai_vault/...` on nine pages. **The
  half the case exists for passes** — the check found `a vault with spaces` and named it in every
  message, so discovery is name-independent and space-safe, which is visible in the output that fails
  the case. What fails is a second property the case was asserting without meaning to. **It was green
  on placeholders, not on truth**: under the old `vault_copy` rename, those citations resolved against
  empty files the sandbox itself had created. **This is the `raw/` class again**
  ([[moving-raw-into-a-dated-archive]], 115 of 124 pages) at a smaller size, and it belongs with
  [[a-rewriter-must-be-paired-with-a-detector]]. **What the case should assert is the owner's call**:
  narrowing it to discovery alone is the honest reading, but narrowing a gate's assertion is not a
  session's to decide ([[ask-before-weakening-or-working-around-a-rule]]).

- measure: **the gate's selftest went from `caught 24, missed 96` to `caught 119, missed 1` on two
  sandbox fixes, and the new discovery case was proved by plant-and-revert.** The readings, in order,
  all on 2026-08-19: **24/96** with the schemas as committed (the baseline, so the `basis` promotion
  is not implicated); **86/34** with the `governs:` loop moved ahead of the placeholder loop; **119/1**
  with the sandbox mirroring the repository's vault directory name; the last one is `the vault is
  renamed`, which is the corpus finding above and not a suite defect. **`run_found` was proved able to
  fail before it was believed** ([[a-case-that-passes-before-the-change-tests-nothing]]): the
  mutation was replaced with one that moves the vault to depth 3, past discovery's `maxdepth 2`, the
  case reported MISSED with the other 119 unchanged, and the plant was reverted in the same command
  ([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]). **The suite's exit code
  is its score and always was**: its last line is `[ "$fail" -eq 0 ]`. Measured with one case
  planted broken: `TRUE EXIT WITH ONE FAILURE = 1`.

- process: **a claim labelled `measured` was written from an instrument that reported its own exit
  code, three times in one hour, and the third time was while correcting the second.** This session
  filed a `measure:` line saying the selftest *"exited 0 throughout, at 24/96 as at 119/1"* and drew a
  decision out of it — that the exit code does not read the score. **Both are false.** The script's
  last line is `[ "$fail" -eq 0 ]`, so its exit code has always been its score; measured with one case
  planted broken, it returns **1**. The line above is corrected in place rather than left with a
  retraction beside it, because `/ingest` files these into `log.md` and a false measurement filed as
  history is worse than one never written.
  **The instrument was a pipeline, every time.** `bash selftest.sh | tail -20` returns `tail`'s status;
  `bash selftest.sh > f; grep SELFTEST f` returns `grep`'s. Both are 0 whenever the last stage
  succeeds, which it always does. **And the correcting run repeated it**: the probe's own compound
  command ended in `grep -c` over zero matches, so the harness reported the measurement task as
  *failed with exit code 1* while the number it produced was correct.
  **This store already holds the same shape about `grep`**
  ([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]) and about instruments naming
  their own answer ([[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]). What is
  new is the generalisation and it is worth a page: **an exit code read through a pipe belongs to the
  last stage, so a measurement of a command's status is only a measurement when nothing is downstream
  of it.** The habit that would have caught all three is one line: capture into a variable on the very
  next statement, never through `|` and never after a trailing `grep`.

- process: **the previous session's `retro.md` is an unfilled copy of the template, and the skill's
  stated failure mode does not cover that.** Found at `.superpowers/sdd/retro.md`, stamped 02:38 on
  2026-08-19, still carrying `session: YYYY-MM-DD` and every instruction paragraph, with the only two
  occurrences of `answered:`/`deferred:`/`could-not-close:` being the ones inside the instructions.
  **The `/retro` skill names its failure mode as silence** — *"a session that skips this skill
  produces no file at all, which looks the same from the outside as a session with nothing to
  confess"*. This is a **third state that nobody named and that is worse than both**: a file exists,
  it is the right size, it opens on the right heading, and it says nothing. Absence is at least
  visible to `test -f`; an unfilled template passes that and every other cheap check.
  **What would catch it is one line, and it is the same shape the vault already uses elsewhere**: a
  retro whose frontmatter still reads `YYYY-MM-DD`, or which contains no verdict token outside the
  instruction paragraphs, has not been written. Recorded rather than fixed, because `/retro` is a
  skill and its wording is not this session's to change.

## Anything else worth keeping

**Reading the vault by hand overturned a live decision that had stood for two sessions**, and the
incident is worth more than the fix. The owner had rejected `PreToolUse` on `Edit|Write` as the guard
because it would fire on every edit and write; the previous session queued a latency measurement to
price it and wrote down that the measurement was what the option waited on. The hook has been
registered under exactly that matcher since 2026-08-13 and [[session-hooks]] states it in its own
table. **Nobody had opened the page, because nobody asked.** The cost was sunk, the measurement was
not owed, and the option's whole objection dissolved on one line of an entity page.

**Refusing to build against a red instrument.** The guard was the chosen body of this session and was
not started once the suite came back at `caught 24, missed 96`. Building it would have produced
something unverifiable that looked finished, and the session would have reported it as done.

**Plant-and-revert did what it is for, twice.** It proved `run_found` able to fail before its score
was believed — the mutation was replaced with one moving the vault past discovery's `maxdepth`, the
case reported MISSED with the other 119 unchanged, and the plant was reverted in the same command.
And the same discipline is what made the exit-code claim get re-measured instead of re-read.

## Harness

**Build the guard as a branch in `.claude/hooks/ask-the-vault.ps1`.** It scans `.claude/rules/*.md`,
parses each file's `paths:` frontmatter, matches it against the payload's `file_path`, and injects
that file's body as `additionalContext`. The rule stays defined once — generated whole from its vault
page — and both triggers hand out the same text: the native Read delivery, and this hook on the
operation probe 4 measured going through unguarded. **Zero new processes**, because the hook already
spawns on every `Edit|Write`. Owner confirmed this shape. Cases owed in `scripts/hook-selftest.ps1`,
which currently covers the guard's existing branches only.

**`CLAUDE.md`'s fallback paragraph needs a line about `/pre-task`.** It tells a session that cannot
dispatch an agent to read the vault by hand with two `rg` commands — which substitutes for
`/vault-ask` and not for `/pre-task`, a topic lookup being a different thing from a plan checked
against what is already decided. **A divergence was recorded this session for exactly that gap.**
Either the paragraph says what a session does instead, or the rule says non-trivial work does not
proceed without the librarian.

**`/retro` should be able to tell an unfilled template from a written retro.** The skill names its
failure mode as the file being absent; the previous session left a file that exists, is the right
size, opens on the right heading and says nothing. A retro whose frontmatter still reads
`YYYY-MM-DD`, or which holds no verdict token outside the instruction paragraphs, has not been
written.

**`.superpowers/sdd/vault-feedback.md` and `.claude/templates/handoff.md` disagree about the drain's
vocabulary.** The feedback file's header names four kinds — `miss:`, `lint:`, `measure:`, `process:`
— and the handoff template's `Feedback to the librarian` section says *"Its `- harness:` lines go to
`Harness` instead"*. **There is no `harness:` kind in the file that is being drained.** This session's
harness items were written as `process:` and routed here by hand, which is exactly the transfer the
matching vocabularies were meant to make mechanical. One of the two documents is wrong and it is not
this session's to choose which.

**Pin `*.yaml` to LF in `.gitattributes` — deferred, with its trigger named.** `git checkout` writes
the six `_schema.yaml` with CRLF, and that class now holds a gate input parsed by the same awk the
`*.md` pin exists for by name. Measured: the gate exits 0 and prints `ok` with all six in CRLF, so
[[a-file-class-is-pinned-after-it-costs-something]] says do not pin it yet. **What it did cost is
diagnosis time**, which is not offered as the trigger.

**Delete the probe scaffolding once this ingest lands:** `probe/`, `.claude/rules/_probe-paths.md`,
`.claude/hooks/instructions-loaded.ps1`, and the `InstructionsLoaded` block in
`.claude/settings.json`. `probe/RUNBOOK.md`'s closing paragraph makes deletion conditional on probe
4's answers reaching `wiki/`, and this journal is that. Region coverage returns to a denominator of
thirteen.

**The selftest's cost is a candidate and not a task.** It copies 401 files and runs the whole gate
120 times; measured, the copy is ~0.25 s and the diff ~0.14 s, and the gate is the rest — roughly
five minutes on an idle machine. A faster suite that silently stops checking is the worse failure,
which is why this is written down rather than acted on.
