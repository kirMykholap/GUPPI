---
session: 2026-08-20
sprint: S2
commits: 53892df..abd2a53
---

# Handoff — 2026-08-20

Fourth session of the day. Three harness debts from the brief's alarms were built and committed;
the retro found that the owner cannot see the harness in any of the four directions it was offered,
and he chose to record that rather than act on it.

Anywhere below, a line beginning **owner:** is the owner's own testimony.

## State

**Done, and committed as `abd2a53`.**

- **`/ingest` selects its source by sidecar absence.** `.claude/skills/ingest/SKILL.md` picked *the
  newest handoff by the date in its name*, and three journals now carry `2026-08-20`. It now takes
  the handoffs in `raw/handoffs/` matching `2*.md` that have no `<name>.coverage.tsv` beside them,
  oldest first where there is more than one, and says there is nothing to ingest rather than picking
  one. The frontmatter `description:` and the paragraph describing the `SessionStart` hook were
  corrected in the same change.
- **The `SessionStart` hook writes a `session-start:<source>` row**, and `Read-LedgerState` resets
  the pre-task state on `session-start:clear` and not on `compact`.
- **The pre-task ledger holds one session**, rotated whole at `startup` into
  `.superpowers/sdd/ledger/pre-task-ledger.<yyyy-MM-ddTHHmmss>.tsv`, with a `#`-prefixed pointer row
  opening the fresh file.

**Checks, each read from its own invocation.** `scripts/hook-selftest.ps1` reports
**`caught 107, missed 0`**, from 94 — thirteen cases added and the count moved by thirteen.
`bash scripts/vault-check.sh` exits **0** with one advisory: `a region or whole generation covers
3 of 15`, **and the unmarked files are unchanged**, twelve of them, named in the advisory.
`uv run ruff check src tests` and `uv run ruff format --check src tests` are clean over 88 files.
**The test suite was not run and no Python changed.** No browser walk; the product has not moved.

**Measured, not assumed:** Docker is **not running**, so the 14 migration tests are still owed
against their condition. Applying the new selection rule to the real tree: **18 handoffs matching
`2*.md`, none uncompiled**, three of them dated `2026-08-20` — so the branch that fires today is
*nothing to ingest*, and the tie-break bites at the next `/handoff` rather than now.

**Not done, deliberately:** the three readings that are the owner's, the governed-file count, the
migration tests, the `/handoff` drain of the ledger, and `log.md` rotation. All were on the plan's
own *Deliberately not done* list before it was approved.

**In flight: nothing.** The tree is clean after `abd2a53`.

**Next step:** the seven-item `next` list on `sprint.md` is untouched and its first item is still the
prose-path detector. Whether the fog finding below displaces it is the owner's.

## Entities

- **`.superpowers/sdd/ledger/` appeared** — the pre-task ledger's archive, one file per rotated
  session, git-ignored like everything under `.superpowers/`. **Nothing prunes it and nothing reads
  it.**
- **The pre-task ledger changed shape.** It used to be one file growing without bound; it is now one
  file per session with the previous ones beside it. Its `pre_task` column gained a third value,
  `-`, for a row that asserts nothing about the ritual.
- **`.claude/hooks/session-brief.ps1` gained a second and a third side effect.** It stamped the
  session identifier; it now also rotates the ledger on `startup` and appends the session-start row.
  It still prints nothing while doing any of it.
- **Two functions appeared in `.claude/hooks/pre-task-state.ps1`:** `Invoke-LedgerRotation`, and
  `New-PreTaskState`, which exists so the fresh state is built in one place rather than two.

## Decisions

- **`/ingest` chooses its source by the sidecar.** *Rejected:* the `ingested:` line of `brief.md`,
  which the brief itself proposed — it names the one journal last compiled and cannot order the
  remaining two of three same-day journals. *Rejected:* mtime, which any checkout rewrites and which
  the skill already forbade. **Obliges:** the predicate is scoped to `raw/handoffs/` with the `2*.md`
  filter, because `raw/plans/` and `raw/specs/` hold artefacts that are frozen and cited rather than
  compiled and will never earn a sidecar. **Nothing in `decisions/` ruled on ingest source selection
  before this**, so nothing is superseded — the by-the-date rule lived as prose in one skill file.
- **The ledger holds one session, rotated at `startup`.** The owner's design, taken in conversation.
  *Rejected:* the closing ritual as the trigger, which can be skipped and has been, and which does
  not touch this file at all today. *Rejected:* a line-count threshold, one more number to remember
  for no gain once the file is per-session. **Obliges:** rotation runs on `startup` alone, because a
  `resume`, a `compact` and a `clear` are the same live session and filing its rows away would drop
  its approved scope mid-flight.
- **The `pre_task` column gained a third state rather than defaulting to `no`.** *Rejected:* writing
  `no` on a session-start row — nothing had been asked of the ritual at that moment, so `no` would
  assert to a human at a retro that a ritual had been skipped. **Obliges:** `Add-LedgerLine` takes
  `[object]` rather than `[bool]`, so omitting the argument means `-` and all five existing callers
  are untouched.
- **DIVERGENCE — an approved scope was widened by a helper extraction that was chosen rather than
  forced.** The plan named, for `pre-task-state.ps1`, the third state, the reset, the rotation
  function and the comment block. `New-PreTaskState` is none of those and was neither asked about nor
  notified. *Why it looked unnecessary:* without it the state object is built in two places and a
  field added later reaches one of them — the copy hazard this project repairs everywhere else — and
  the file was already open under an approved plan. **Both are arguments for the change and neither
  is an argument for not asking.** The rule keys on whether the scope grew, not on whether the growth
  was avoidable, and one sentence would have covered it. The four-day-old divergence page of this
  same class names `session-brief.ps1`, which is one of the two files edited tonight.
- **DIVERGENCE — a question shaped like a proposal was executed as a ratified design.** Asked to
  choose between three ways of bounding the ledger, the owner answered with neither: *"а что если
  ledger будет только на одну сессию? ... пускай на нем будет процесс, который обнуляет ledger"*.
  The session answered the design question, **moved the trigger he had named** from the closing
  ritual to `SessionStart`, and went straight to writing the plan. He never said yes; the next gate
  was the plan's own approval, by which point the choice sat inside two hundred lines and the cheap
  moment to say *no, at the end of the session* had gone. *Why it looked unnecessary:* the tool that
  asked the question returned his text as an "answer", and an answer was read as a decision. **He had
  selected none of the three options and was still asking what the ledger was.** *Rejected
  alternative:* one turn, bringing the changed design back for a yes/no before it reached a plan.

## How it is built

- **The sidecar is now the single definition of *compiled*, with three readers agreeing.** A handoff
  is compiled when `<name>.coverage.tsv` sits beside it; that file is written by the ingest that gave
  every unit a verdict. `session-brief.ps1` uses it to find an uncompiled journal, rule 8 of
  `vault-check.sh` uses it to decide whether to judge a journal's form, and `/ingest` now uses it to
  choose its source. **It is a file-existence test and no ordering can break it** — which is the
  property the date-prefix rule lacked, and the reason the 2026-08-17 sort returned the earlier of
  two same-day journals.
- **One row does three jobs.** The `session-start:<source>` row is the instrument for a question
  nobody had measured — whether a `/clear` keeps the session identifier — because two append-only
  rows can be compared and the `.session` stamp, overwritten in place, leaves no *before*. It is the
  reset, dropping everything the session accumulated before a `clear`. And it is what tells the
  rotation that this is a new session rather than the same one resumed, compacted or cleared.
  **It is correct under either answer to the unmeasured question:** a new identifier makes the reset
  land on a state that is already empty.
- **Rotation is a whole-file move and never a read-modify-write**, which is what the ledger's
  append-only design exists to protect: two writers appending short lines do not lose each other's,
  and a read-modify-write silently would. **The reader's race is already handled in the ratified
  direction** — `Read-LedgerState` reads this file 71 to 108 times a session, and one landing between
  the `Test-Path` and the `Get-Content` hits that function's `try`/`catch`, gets a fresh state, and
  asks for the ritual again.
- **The permission mode the session really started in is visible only through this ledger**, and it
  paid again tonight: the previous session's rows carry `auto` and this session's carry `plan`,
  then `acceptEdits` after the owner switched by hand. **No hook event fires when the mode changes**,
  so the mode is recorded only when some other hook fires and reads it from its payload.

## Lessons

- **`grep -l` is a presence test and cannot answer an identity question, and it failed towards a
  confident wrong answer delivered to the owner.** Checking whether two lines still sitting in
  `vault-feedback.md` had already been drained, `grep -l "thirteen unmarked files"` matched the
  previous journal — and the session reported that `/handoff` had failed to empty the file and that
  tonight's run would duplicate a line. **Opening the journal's `Feedback to the librarian` section
  showed the match was on unrelated prose in a different section**, and that the section holds two
  entirely different entries. `/handoff` empties the file correctly. Nothing was deleted, because the
  match was verified before acting on it. The question asked was *is this entry in that section*; the
  instrument answered *does this string appear in that file*.
- **A `vault-feedback.md` line written during an ingest reaches the vault one session late**, and
  this is a property of the order rather than a defect. `/handoff` empties the file and `/ingest`
  runs after it, so anything the ingest itself finds survives into the next session's journal. **The
  previous session's journal documents exactly this about its own inherited line**, which is how it
  was recognised tonight rather than rediscovered.
- **A proposal arriving where an answer was expected is the owner thinking out loud, not deciding.**
  The tell is available at the time and was visible: he had interrupted twice with clarifying
  questions, had selected none of the three offered options, and phrased his own idea as *"а что
  если"*. See the second divergence above.

## Deferred

Eleven questions, each with a destination, from the retro's gate.

- **Whether the rotation trigger stays at `startup`.** He approved a plan containing it; he never
  gave a yes/no on the change itself.
- **Whether the helper extraction was acceptable**, the divergence above.
- **Whether `.superpowers/sdd/ledger/` needs a bound.** *Consequence of not doing it:* the growth
  did not end, it moved — out of the file the hook reads on every edit and into a folder nobody
  reads, at roughly a kilobyte per session.
- **The fog finding.** See `Harness`; it is the largest item here.
- **Whether the `core` criterion still sorts `CLAUDE.md` without a remainder** after `/pre-task` left
  it for a hook message. Second session carrying it.
- **The re-reading of the JavaScript rule page**, whose whole ground is `/pre-task` arriving
  unconditionally.
- **Which reading the conditional-delivery gate carries**, after a second move.
- **What `permissions.defaultMode: "plan"` should mean for a `claude -p` run.**
- **The 14 migration tests**, owed against Docker being up. Measured tonight: **not running**.
- **Criterion 6's reading.** The command was run and the record's disagreement is settled —
  **twelve unmarked files, not thirteen** — but reading the criterion is the owner's and was not
  taken.
- **The `/clear` measurement — WITHDRAWN BY THE OWNER, not deferred against a condition.**
  **owner:** «нет. снимаем, как убираем. Не делаем.» It was offered and he took it off the list.
  *Consequence:* [[the-approved-scope-survives-a-compact-and-not-a-clear]] stays `basis: inference`
  and unmeasured — **and the branch built tonight is correct either way**, which is why withdrawing
  it costs nothing. Written here so the next session does not re-offer it as owed.

## Feedback to the librarian

Drained from `.superpowers/sdd/vault-feedback.md`. Five lines; the three `- harness:` lines from the
same file are in `Harness` below. **The first two were written during the previous session's ingest,
after its handoff had already emptied the file**, and reach the vault one session late by that
ordering rather than by anyone's mistake.

- miss: **the journal of 2026-08-20 says "the thirteen unmarked files are unchanged" and the number
  is twelve.** The librarian reported the disagreement at the ingest and correctly did not patch it;
  `raw/` is immutable, so the correction is this line rather than a rewrite. Measured twice that
  session before the ingest: `a region or whole generation covers 2 of 14`, with twelve files named
  in the advisory. Measured after: `3 of 15`, the same twelve named. **Twelve has been the count
  since the numerator became two**, and the thirteen was taken from an older brief describing
  `1 of 14`. The required phrasing is unaffected — it is still *the unmarked files are unchanged*,
  never *coverage improved* — but the figure inside it was wrong in the source the corpus compiled.
  **Measured again tonight, independently: `3 of 15`, twelve named.**

- lint: **the governed denominator moved from 15 to 14 between the previous ingest and that session,
  and nothing recorded it.** The corpus carries `2 of 15` from 2026-08-20's second session; that
  session's first gate run measured `2 of 14`. The drop is real and has a cause already on the
  record — `vault-archive.sh` moved the probe scaffolding out of the working set — but the figure's
  own history skips it, so a reader comparing `2 of 15` with `3 of 15` sees a numerator moving inside
  a stable denominator, which is not what happened. **The denominator fell by one and rose by one for
  unrelated reasons**, and [[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]
  is written for growth only.

- miss: **[[the-brief-is-stamped-with-its-commit]] carries the same false sentence about the hook
  that the ingest skill did.** Its lines 49 and 86 say `ingested:` is *"the one line the hook still
  compares, by name"* and that a mismatch means no ingest ran. The hook stopped doing that on
  2026-08-17: `.claude/hooks/session-brief.ps1` selects by sidecar absence and asks of `ingested:`
  only whether the file it names **exists**. Surfaced in this session's `/pre-task` — the librarian
  found the twin while checking the skill-file copy that was already being repaired. The page is
  `basis: human` and is not a session's to edit; the skill copy was repaired in `abd2a53`.

- miss: **four `current` pages describe the pre-task ledger and its state machine as they were
  before `abd2a53`.** [[the-approved-scope-survives-a-compact-and-not-a-clear]] says *"nothing in
  the code says either sentence… a later reader will otherwise look for the branch that implements
  it"*, and [[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]] says
  *"a `/compact` and a `/clear` are not branches"* — that commit writes the branch, deliberately.
  [[the-pre-task-ledger]] says the file *"grows without bound"*, which rotation ends, and that
  *"`/handoff` drains it"*, which [[the-retro-writes-its-own-transit-file]] also asserts. **That
  drain does not exist**: neither `.claude/skills/handoff/SKILL.md`, nor `/retro`, nor
  `.claude/templates/handoff.md` mentions the ledger, so the first of the file's three stated jobs is
  unbuilt. Verified by grep this session.

- process: **a question shaped like a proposal was executed as a ratified design, and the owner never
  said yes.** The full account is the second divergence under `Decisions`. Recorded here as well
  because it is a finding about the ritual rather than about the corpus: **the repair is one question
  and it costs one turn** — bring a changed design back for a yes/no on its own, before it is written
  into a plan. He also never got the answer he was reaching for, *where are the rows kept and does
  anything keep them*, until he asked a second time, because it was folded into the design instead of
  being answered.

## Anything else worth keeping

**Measurements, each from its own invocation.**

- **A `/pre-task` dispatch cost 5m54s** and enumerated **184 `decisions/` pages**, opening **47 in
  full** — 25 from `decisions/` and 22 from elsewhere. **It found three constraints the plan did not
  have**, all before approval: that the `pre_task` column would have asserted a skipped ritual; that
  rule 8 of the gate already answers *is this compiled?* by the sidecar; and that the vault had
  **deliberately withheld** the retention ruling, which turned the ledger item from *working around a
  decision* into *supplying a missing one*.
- **`hook-selftest.ps1`: 94 to 107 caught, 0 missed.** Thirteen cases added, and the count moved by
  thirteen. **The reset is asserted in both directions on one ledger** — a `session-start:compact`
  row leaves a pre-task standing, a `session-start:clear` row drops it — so a branch that fired
  always, or never, fails one of the pair.
- **The live ledger held 7 rows and 404 bytes across two sessions** when the work began: three from
  `6eddb5ae` at `mode=auto`, four from `fb699ebe` at `plan`, `plan`, `unknown` and `acceptEdits`.
- **18 handoffs match `2*.md` in `raw/handoffs/`, none uncompiled**, three dated `2026-08-20`.
- **Docker is not running** on this machine tonight.

**owner:** on the harness being invisible — «Я вообще не понимаю что происходит в этой сессии. Все
работает непонятно как.»

## Harness

The three `- harness:` lines from `.superpowers/sdd/vault-feedback.md`, plus two work items the
session found and did not build.

- harness: **`/ingest` selects its source by sidecar absence, not by the date in the filename.** The
  skill told the librarian to ingest the newest handoff *by the date in its name*; three journals now
  carry 2026-08-20 and the rule has nothing left to break the tie. The replacement is the test two
  other readers already use — a handoff with no `<name>.coverage.tsv` beside it is uncompiled —
  scoped to `raw/handoffs/` with the hook's `2*.md` filter, because
  [[raw-holds-testimony-and-artefacts-are-frozen]] means `raw/plans/` and `raw/specs/` never earn a
  sidecar. Where more than one is uncompiled they go oldest first, one source at a time inside the
  one dispatch, which is [[ingest-runs-after-handoff-at-the-end-of-a-session]] rather than a new
  ruling. **Nothing in `decisions/` ruled on ingest source selection**, so nothing is superseded.
  Decided and built 2026-08-20, fourth session, in `abd2a53`.

- harness: **the `SessionStart` hook writes a ledger row carrying its `source`, and a `clear` resets
  the pre-task state.** `session-brief.ps1` already parsed `session_id` and stamped it; it now also
  appends `session-start:<source>`, and `Read-LedgerState` drops everything a session accumulated
  before a `session-start:clear` row. This discharges the deferral on
  [[the-approved-scope-survives-a-compact-and-not-a-clear]], whose own text names this repair and
  whose rejected alternative was measuring before shipping. **The measurement itself was then
  withdrawn by the owner** — see `Deferred`. Decided and built 2026-08-20, fourth session.

- harness: **the pre-task ledger holds one session and is rotated at startup.** The owner's design:
  one session per file, records filed away rather than deleted. Rotation runs from the `SessionStart`
  hook and **only** when `source` is `startup`. The whole file moves to
  `.superpowers/sdd/ledger/pre-task-ledger.<yyyy-MM-ddTHHmmss>.tsv`; never a read-modify-write.
  **Rejected:** the end-of-session ritual as the trigger — it can be skipped and has been, and it
  does not touch this file at all today. **Rejected:** a line-count threshold. Decided and built
  2026-08-20, fourth session. **The trigger was moved from where the owner proposed it and he has not
  ratified the move** — see `Decisions`.

- harness: **`/handoff` does not drain the pre-task ledger, and two `current` pages say it does.**
  A work item naming the file to change: `.claude/skills/handoff/SKILL.md`. It matters more after
  `abd2a53` than before, because a session that ends without the ritual now has its rows filed into
  `.superpowers/sdd/ledger/` by the next startup, where a drain would not look even once it exists.
  Not built tonight: it is a change to a closing-ritual skill and was outside the approved scope.

- harness: **the harness is no longer visible to its owner, and this is the session's largest
  finding.** Asked where the fog is, he was offered four candidates — the mechanism, the session's
  course, the vault's register, and what changed on disk — and **he selected all four**. This bears
  on S2's own goal, *the vault is used, not maintained*: the owner's review is the only control this
  project has, and it cannot operate on something he cannot see. **Two repairs were offered and both
  were declined for tonight:** a generated harness map — one file built by a script from
  `settings.json` and the hook files, so it cannot go stale, which is this project's own idiom — and
  a session that builds nothing and only makes the existing visible. **owner:** «Записать, решать
  потом.» Part of the fog is the language: everything durable is written in English by rule, and the
  only Russian he gets is chat, which nothing keeps — so a map, if it is ever built, has a language
  question in front of it that is a rule change and therefore his.
