---
title: "`scripts/vault-archive.sh`, the first tool here that moves a path and rewrites its citations"
type: entity
status: current
authority: archive-script
basis: code
sprint: S2
created: 2026-08-20
supersedes: "[[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]]"
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-archive.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [vault, harness, process]
---

# What it is

```
bash scripts/vault-archive.sh [--dry-run] <date> <session> <kind> <file>...
```

Built 2026-08-20. It performs, in one run, the three operations its proposal named: **move** the
files to `archive/<date>/<session>/<kind>/`, **emit** the old-path-to-new-path mapping, and
**rewrite** every `sources:` line naming an old path
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]],
[[the-archive-gains-a-folder-per-session-inside-the-date]]).

**It runs the gate itself afterwards and exits on that code**, because a filesystem cannot make
move-and-rewrite atomic and the window between them is red.

**It rewrites `wiki/` and `archive/`, and never `log.md`**
([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]).

## No regular expression ever sees a path

Finding is `grep -F`; rewriting is `awk` with `index()` and `substr()`
([[a-path-is-never-a-pattern]]). The first version escaped for `sed` and the escape did not survive
being written into the file — the instrument then reported *cited by 0 page(s)* about nine pages
that cite the path ([[an-instrument-that-fails-towards-nothing-to-do]],
[[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]]).

## The owner's recollection that a script already existed is not so

What the store carried was the **procedure** ([[a-page-rename-is-sed-and-verify]]); `scripts/` held
nine files and none of them rewrote a path.

## Its first cargo, and what that run measured

The probe scaffolding, on 2026-08-20 ([[the-probe-scaffolding-is-archived-whole-into-specs]]).
Counts were verified against an independent hand count before anything moved: nine pages cite
`probe/RUNBOOK.md`, three cite `_probe-paths.md`, two cite `instructions-loaded.ps1`.

**Measured on the real tree after the run, rather than reported by the script**: eighteen lines
changed and all eighteen are `sources:` lines; no old path remains in any citation, checked per
file by grep rather than inferred from a successful exit. Thirteen prose mentions of the runbook
are untouched, which is correct — a page recording history is supposed to name a path that no
longer exists ([[a-path-detector-for-prose-references]]).

## It depends on a rule that had never been written down

A `sources:` path inside the vault is vault-relative; one outside it is written from the
repository root ([[a-sources-path-inside-the-vault-is-vault-relative]]).

## It gained its caller on 2026-08-21, and the call is forward-only

**`/ingest` runs it as step 12, the last thing the ingest does** — after step 10, because step 10
runs `vault-coverage.sh` against the source path and this moves that path
([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]).

**Until then it had no callers at all**, and it was one of the mechanisms the owner was shown as
built and wired to nothing ([[an-admission-test-for-mechanisms]]).

**Only the journal the ingest just compiled moves.** The journals that accumulated before this step
existed stay in `raw/handoffs/` — **owner: сначала только вперёд** — because sweeping them is 480
`sources:` lines in one commit and is its own piece of work
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]]).

**What the call buys beyond an emptier `raw/`**: the uningested-journal alarm in
`.claude/hooks/session-brief.ps1` reads sidecar absence in `raw/handoffs/`, so once compiled
journals leave, a non-empty `raw/handoffs/` comes to mean *work that was never compiled* rather than
*history that piled up* ([[the-sidecar-is-the-single-definition-of-compiled]], [[session-hooks]]).

**And it made the brief's `ingested:` line resolvable in a second place**, which is a decision of its
own ([[the-ingested-line-stays-a-filename-and-the-hook-resolves-it-wherever-the-journal-lives]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

## Its first run against a file inside the vault left the gate red, and the defect is one string doing two jobs — 2026-08-21

**The file argument and the citation search are the same string, and inside the vault those are two
different forms.** `[ -e "$f" ]` resolves the argument from the **repository root**, because the
script `cd`s there; `pages_citing "$f"` greps for that same string inside `sources:` lines, which
inside the vault are written **vault-relative**
([[a-sources-path-inside-the-vault-is-vault-relative]]). A journal is therefore
`job_hunt_ai_vault/raw/handoffs/…` to the first test and `raw/handoffs/…` to the second, and no
argument satisfies both.

**Measured on this ingest's live run**, which is step 12's first:

| the argument given | what happened |
|---|---|
| `raw/handoffs/<journal>.md` | `no such file`, exit 2 — nothing ran |
| `job_hunt_ai_vault/raw/handoffs/<journal>.md` | moved 1 file, **`cited by 0 page(s)`**, rewrote 0, and then `THE GATE IS RED AFTER THE MOVE (exit 1)` |

**The gate named the nine pages** whose `sources:` pointed at the moved journal, and the citations
were rewritten by hand with this script's own rule — `^sources:` lines only, fixed-string
substitution, `wiki/` and `archive/` only — after which the gate exits 0. **The window this script
exists to close was open**, and it was closed inside the same turn rather than by the script.

**Why it was green the first time.** Its only previous cargo was the probe scaffolding at
`probe/RUNBOOK.md` — a path **outside** the vault, which by the same rule is written from the
repository root, so the two forms coincided and the defect could not appear
([[the-probe-scaffolding-is-archived-whole-into-specs]]). **A mechanism exercised once on the case
where two forms coincide says nothing about the case where they differ**
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[an-instrument-that-fails-towards-nothing-to-do]]).

**`cited by 0 page(s)` is the dangerous line.** It is the same output a genuinely uncited file
produces, and this script's own header records the last time that number was zero for the wrong
reason. **The gate is what caught it**, which is the arrangement the script was built around: move
and rewrite are one run, and if the tree is left red the script says so rather than exiting 0.

**Not repaired here.** The fix is the script's, and it is a session's file rather than the
librarian's ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]). The shape of it is
one line: search for the citation form as well as the argument form, or normalise the argument to
both roots the way `vault-check.sh` already resolves a `sources:` path.

## The sidecar did not move with the journal — 2026-08-21

**`<name>.coverage.tsv` stayed in `raw/handoffs/` while `<name>.md` went to `archive/`.** The script
moves the files it is given and nothing else, and step 12 gives it the journal alone.

**Source selection and the session-start alarm are unaffected**: both filter `2*.md` and a sidecar
with no journal beside it is not a candidate ([[the-sidecar-is-the-single-definition-of-compiled]]).

**`vault-coverage.sh` on the archived journal is affected, and it fails towards alarm.** With no
sidecar beside it the run falls into evidence mode and exits 1 — *22 of 52 units evidenced* — which
reads exactly like an unfinished ingest ([[a-denominator-is-walked-off-the-input-list]]). The
step-11 loop globs `raw/*/*.md` and will not reach the archived journal at all, so the alarm is
latent rather than firing every session.

**Nothing in the design says which behaviour is right**, and it is recorded rather than chosen: move
the sidecar with the journal, or scope the coverage loop to `raw/` and accept that an archived
source is no longer swept.

*(Compiled from the step-12 run at the ingest of 2026-08-21.)*

# Both defects above were repaired, and the repair had no journal to travel in — 2026-08-21

**The two sections above record their defects as standing. Both were fixed in `340ccb0`**, after the
ingest that wrote them, and this page is dated rather than edited.

- **The path form.** The citation form is now derived from the argument by stripping the vault
  prefix, with a `case` rather than a regular expression, because no regular expression sees a path
  in this file ([[a-sources-path-inside-the-vault-is-vault-relative]], [[a-path-is-never-a-pattern]]).
- **The orphaned sidecar.** `<name>.coverage.tsv` now rides with its source; the day's orphan was
  moved by hand and the archived journal reads `52 of 52 / INGEST COMPLETE`
  ([[the-sidecar-is-the-single-definition-of-compiled]]).

**Both have selftest cases and both were proved to bite**: breaking the path-form line takes the
suite from `caught 144, missed 0` to `caught 142, missed 2`. The script had no cases of its own
before, which is why the defect shipped
([[a-case-that-passes-before-the-change-tests-nothing]]).

**The shape to watch is how this reached the vault at all.** A repair made after `/ingest` has no
journal to travel in — `raw/` is immutable and the sidecar already exists — so
`.superpowers/sdd/vault-feedback.md` is the only channel that survives it
([[vault-feedback-file]], [[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]]).

*(Compiled from the feedback file drained into `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`, and verified against `340ccb0` at that ingest.)*

# It gained a `pages` kind, and with it a destination the archive decision had always named — 2026-08-22

**`pages` joined `handoffs`, `plans`, `specs` and `notes` on the owner's ruling**, and it is the
kind that is not an inbox kind: the others are what leaves `raw/`, while a retired wiki page leaves
`wiki/` ([[the-archive-script-gains-a-pages-kind-and-a-retired-page-is-dated-by-its-session]]).

**The clause it makes executable is [[archive-is-dated-by-session-and-holds-what-left-the-working-set]]**,
which has said since 2026-08-16 that the dated folder holds the wiki pages retired that day. This
script could not express that destination, so about thirty retired pages went flat into `archive/`
instead — **the practice outvoting the rule for six days, with no instrument able to report it.**

**Its first cargo under the new kind is [[advisory-is-the-default-for-a-hook]]**, struck by the
owner on 2026-08-21 and retired into
`archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/pages/`.

**The run reported `cited by 0 page(s)`, and here that reading is correct rather than the instrument
failing.** It was checked independently before the move — `rg '^sources:.*advisory-is-the-default-for-a-hook'`
over `wiki/` and `archive/` returns nothing — which is the discipline this page's own section on
that number asks for: count by hand, then compare
([[an-instrument-that-fails-towards-nothing-to-do]]). **`moved 1 file(s) and 0 sidecar(s)`**: a wiki
page has no `.coverage.tsv` beside it, so the sidecar branch is inert for this kind. The script's own
gate run exits 0.

# It has no mode for repointing a `sources:` line outside a move — 2026-08-22

**The script rewrites `sources:` as part of a **move**, and there is no way to ask it for the rewrite
alone.** The occasion: an already-archived page whose citation had gone dead when
`.claude/skills/pre-task/SKILL.md` was deleted. The page was where it belonged; only its address was
wrong.

**So the eleventh citation was corrected by hand.** The edit was restricted to the `^sources:` line —
which is the script's own narrowing, and the whole defence against `sed` rewriting a quotation as
though it were an address — **but the narrowing was obeyed by care rather than by the tool**
([[knowing-a-rule-is-not-a-mechanism]], [[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]).

**The gate would never have reported it.** The frontmatter walk is `find "$VAULT/wiki"`, so a dangling
citation inside `archive/` reddens nothing and dangles silently ([[vault-scripts]]).

**Named and not repaired.** A `--repoint` mode is a change to a script with a selftest behind it, and
it is a session's to build rather than a librarian's to invent.

# It gained a seventh refusal, and it is the first that guards the store rather than the run — 2026-08-23

**Under `kind = pages` it exits 2 unless a live page under `wiki/` names the slug of the page being
archived.** The other six refusals protect the run — a bad date, an unknown kind, a missing file, a
destination that already exists, a failed move, a red gate afterwards. **This one protects the
corpus**: `archive/` is outside rules 2, 3, 6, 7 and 14, outside the injector sweep, outside
`vault-authority.sh`, and `/pre-task` discards it as retired text, so a page archived with nothing
pointing at it has left the store rather than been filed in it
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

**It fires before anything moves, and the placement is the design.** The script runs the gate at the
end, so a check placed there would report on a move that has already happened — and a red gate locks
the librarian out of the store it was about to repair
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**Scoped to `pages` alone.** A handoff, a plan, a spec and a note are not addressed by slug, so the
branch is inert for the four inbox kinds
([[the-archive-script-gains-a-pages-kind-and-a-retired-page-is-dated-by-its-session]]).

## Two definitions of *cited* now live in this one script and they disagree

| the reader | what it matches | what it misses |
|---|---|---|
| `pages_citing`, which drives the rewrite | a path on a `sources:` line | every `[[wikilink]]` and every bare mention |
| the new precondition | the slug as a plain string anywhere in a live page | nothing, and it cannot tell a pointer from a mention |

**On 2026-08-23 the first reported `cited by 0 page(s)` about a page five live pages name.** That
reading is correct for what `pages_citing` is *for* — it exists to find the lines that need
rewriting, and no line needed rewriting — but it prints in the voice of an answer to *is anybody
pointing at this*, which is a different question and the one the precondition asks
([[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]],
[[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]).

**Neither is wrong and the pair is the hazard.** A reader of this script's output sees two counts of
*cited* on one run and nothing says they answer different questions. The repair designed for it is a
field a script fills from the body's wikilinks
([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]],
[[links-is-filled-by-a-script-from-the-bodys-wikilinks]]), and it is not built.

## The loose match is safe on a measurement, not by construction

**A hyphenated slug does not occur in ordinary prose**, which is what makes matching the bare slug
anywhere in a page safe rather than reckless. **Measured over all 530 slugs on 2026-08-23: exactly
one page would be refused, and it is the corpus's single orphan** — a true positive, so the sweep
found no false one at all.

**The measurement is of this corpus on this date and is not a property of the rule.** A slug of two
short words, or a page quoting a slug inside prose about slugs, would both defeat it; the register
of `authority:` slugs is written as plain text for a related reason
([[authority-becomes-the-index-and-is-required-outside-rules]]).

## It has no selftest case, and criterion 2 of S3 is decided by one

**Neither `scripts/vault-check-selftest.sh` nor `scripts/hook-selftest.ps1` knows about this
refusal.** It was verified by planting an offender in the real tree in both directions, which
proves the verdict fires and says nothing about whether it survives the next refactor
([[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]],
[[a-case-that-passes-before-the-change-tests-nothing]]).

*(Compiled from `raw/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md`.)*

# It gained an eighth refusal and lost a real bug — 2026-08-23, in the second session of that day

**The eighth refusal is conditional on a status.** A proposal carrying `status: refused` is not
released without `decided_by:`, and the script exits 2 saying so. The requirement cannot be stated
in `wiki/proposals/_schema.yaml`, which declares one required set for the whole folder, so it lives
here — the same route `paths` under `render: whole` already took
([[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]],
[[a-refused-proposal-is-archived-and-takes-status-refused]]).

**It was placed here rather than in the gate, and that placement is a correction.** The owner had
accepted a verdict in `scripts/vault-check.sh`; `/pre-task` found it unreachable, because a refused
proposal is in `archive/` by the time the rule applies and the gate's frontmatter pass reads `wiki/`
alone. The moment of the move is the last point anything sees the page.

## The `--include` operand bug, and what it let through

**`grep -rlF -- "$slug" "$VAULT/wiki" --include='*.md'` searched with no filter.** After `--`,
`--include` is an operand — a path — and `grep` reported `No such file or directory` on it into the
`2>/dev/null` beside it. **`wiki/*/_schema.yaml` carries thirteen real page slugs in its comment
blocks**, so the `pages` precondition counted a mention in a schema comment as a live page naming
the slug ([[an-option-after-a-double-dash-is-an-operand-and-the-search-runs-unfiltered]]).

**Repaired on the owner's one-word ruling — «чинить» — and proved by switching the line back and
forth**: with the fix the page is refused with exit 2; without it the archiver walks straight past
the precondition and reports `cited by 0 page(s)`.

**The two-definitions-of-*cited* hazard recorded above is unchanged by this.** The repair makes the
precondition ask its own question correctly; it does not merge the two readers.

*(Compiled from `raw/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md`.)*

# Its `handoffs` cargo was untouched until 2026-08-26, and then it carried the whole inbox

**The script has accepted `handoffs` as one of its five kinds since it was built and had never been
run on one.** Every cargo it had carried was `specs` or `pages`.

**The forward-only clause is what kept it that way**, and the owner overturned it on 2026-08-26:
`raw/handoffs/` is swept whole, not just the source the ingest compiled
([[raw-handoffs-is-swept-whole-today-and-the-forward-only-clause-is-overturned]]).

**The width, measured that day: 464 of the 682 live pages name a `raw/` file on their `sources:`
line — 68% of the corpus.** That is larger than the 480-line figure the struck clause quoted, and it
is why the owner's first proposal — deleting the processed files by hand — was refused on a number
rather than on caution.

**One run per journal.** The destination is `archive/<date>/<session>/handoffs`, and date and session
slug differ per journal, so a sweep of twenty-two journals is twenty-two invocations — each of which
runs the gate itself at the end, which is where most of the wall clock goes.

**The sidecar rides with its source**, by the repair of 2026-08-21, so `<name>.coverage.tsv` needs no
separate argument ([[the-sidecar-is-the-single-definition-of-compiled]]).

**The hazard on emptying `raw/handoffs/` was confirmed repaired before the run.** Two selftest cases
used to append into whichever real journal sorted first and failed loudly with the wrong diagnosis
when there was none; both now plant their own file in `raw/notes/`, and `.gitkeep` keeps the
directory alive on a fresh clone ([[raw-gains-its-internal-structure-before-the-move]],
[[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md` and the step-12 sweep of that ingest.)*

# Its destination path repeats the session slug, and that reached a Windows limit — 2026-08-26

**`archive/<date>/<slug>/handoffs/<slug>.coverage.tsv` carries the session slug at two levels**, and
with a 78-character journal name the path reached 240 characters before the working copy's prefix.
**Git refused to index the file — `Filename too long`** — and it was unblocked with
`core.longpaths true`, which is a per-clone setting that travels with nothing
([[an-archive-path-repeats-the-session-slug-and-reaches-the-windows-limit]]).

**Nothing here measures a path.** The repetition is deliberate — it makes an archived directory
self-describing — and long descriptive slugs are deliberate too. The product of the two is what fails,
and the cheap end to hold is the journal name `/handoff` picks.

**Who runs it was divided by a plan and the division did not survive the ordering** — the librarian
ran it, reported the departure in the turn, and the one-writer property was unaffected
([[divergence-the-librarian-ran-the-archiver-the-plan-gave-to-the-session]]).

# It still has no sweep mode — measured 2026-08-28

**It takes an explicit file list, lines 38–41 and 117, and searches for nothing.** The sweep decided
on 2026-08-24 and given its failure mode on 2026-08-28 is still unwritten
([[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]],
[[the-archive-sweep-continues-past-a-refused-move-and-collects-its-refusals]]).

**And its `kind=pages` precondition would be inert under the criterion proposed for `decisions/`.**
Lines 145–161 require a live page under `wiki/` naming the slug; the criterion is *a live page names
the decision in `decided_by:`*, which entails it. The guard is identically true and can never refuse
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

**That is not a defect in the guard.** It is a floor against losing a page, and selecting which pages
should go is a different job ([[a-citation-is-not-a-test-in-a-corpus-this-densely-linked]]).

# The sweep mode was built and run — 2026-08-29

**The heading above went false the next day.** `--sweep <date> <session>` exists, and its first run
moved 239 pages out of `wiki/`.

```
bash scripts/vault-archive.sh [--dry-run] --sweep <date> <session>
```

**What one run does, in order:** walk `decisions/`, `lessons/`, `proposals/` and `rules/`; apply each
folder's criterion; write `status: archived` onto every selected page **before** moving it; move it
into `archive/<date>/<session>/pages/`; rewrite `sources:` citations that named the old path; continue
past any page it may not move; print the collected refusals **before** the gate runs; append one line
to `log.md`; and exit 1 if anything was refused or the gate came back red.

**It inherits the eight refusals the named-file mode already had rather than acquiring its own**
([[the-sweep-is-a-mode-of-the-archiver-and-inherits-its-refusals]]). The preconditions were factored
into a routine that **returns** a refusal instead of ending the process — the single largest change in
the file, and the thing that makes *continue past a refusal* possible at all.

**`--dry-run` extends to it**, and it computes the longest destination path before moving anything,
refusing the whole run over 240 characters — the limit this page already records
([[an-archive-path-repeats-the-session-slug-and-reaches-the-windows-limit]]).

**Measured on the live corpus, 2026-08-29:** the dry run costs **3m10s** and the real run **5m16s**.
Almost all of it is the per-page citation count, which is one grep of `wiki/` and `archive/` per
selected page. A sweep is a minutes-long operation, not a seconds-long one. The selectors themselves
are one pass each and are not where the time goes
([[a-selector-is-one-pass-over-the-corpus-and-never-one-pass-per-page]]).

**The first run: 239 pages moved, 239 marked `status: archived`, 1 `sources:` citation rewritten,
0 refused.** `wiki/` went from 762 pages to 523 — `decisions/` 341 to 276, `lessons/` 182 to 12,
`proposals/` 49 to 45; `entities/`, `concepts/` and `rules/` have no criterion and were untouched.
The gate was green afterwards at 24 s and the register agreed at 507 slugs
([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]]).

**Zero refusals was predicted and is not evidence.** Every selected page already had a live citer, by
construction for the `decided_by:` criterion, so the continue-past-a-refusal path could not be
exercised on this corpus at all — its selftest case is the only proof of it.

**It gained one refusal it did not have: a `deprecated` page is now additionally checked for a live
page named in its `superseded_by:`**, rather than the weaker floor of any live page naming the slug
([[a-deprecated-page-needs-a-live-successor-named-in-superseded-by-before-it-may-leave]]).

**A defect found and fixed inside the hour:** the empty-selection refusal was written as `grep -q` on
the right of a pipeline under `set -o pipefail`, and it fired on every substring that *did* match
([[grep-q-on-the-right-of-a-pipeline-under-pipefail-inverts-the-test]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# The session name comes off the command line and nothing checks it — 2026-08-29

**The script takes the session as an argument and never derives it**, and that is how the first sweep
put 239 pages into a folder naming no session, against a prohibition four sessions old
([[the-archive-gains-a-folder-per-session-inside-the-date]]).

**The repair, measured while it was still uncommitted:** 239 pages moved with `git mv`, **one `sources:`
citation rewritten**, three prose mentions left standing, gate exit 0 in 19.4 s with the advisory
unchanged. **One command and one edit.** The same repair after a commit is 239 committed paths and
nobody has done it, so there is no number for the other side.

**The journal's own filename carries date and slug and is sitting right there**, which is what makes
this an argument for derivation rather than for care.

## The successor check cannot see an archived repeal

**It fires only on `status: deprecated`** (`scripts/vault-archive.sh:239`), **and the sweep writes
`status: archived`.** So a page taken by the `decided_by:` criterion is never asked for its
`superseded_by:`.

**2 of 241 archived pages carry the field, and both were set by hand at an ingest.** For 237 the absence
is correct — a spent decision is not superseded — **but nothing distinguishes a spent decision from a
repealed one at the moment of the move**, and only the second owes a successor
([[a-rules-page-leaves-only-on-a-decision-and-a-deprecated-mark]]).

**And the sweep's own criteria, read off the run of 2026-08-29:** 66 decisions left — 22 on
`binding: divergence` alone, which is unconditional, and 44 because a live page named them in
`decided_by:` — against the three OR'd criteria at `scripts/vault-archive.sh:376-386`. **Only pages that
acquired a holder were taken mechanically.**

# Three additions on 2026-08-30

**An absolute refusal to release a decision carrying `target_kind: repeal`.** Such a decision is the
only live carrier of the fact that something no longer exists, so it never leaves
([[a-decision-declares-its-target-and-the-handshake-closes-it]]).

**A second release route, for `status: repealed`**, which reads `decided_by:` rather than
`superseded_by:` and forbids a `superseded_by:` outright.

**`repealed` joined the sweep candidates, for `rules/` alone.**

**The unconditional refusal for a `deprecated` page without a live successor is UNTOUCHED**, and the
second route was minted precisely so that test did not become conditional on a field a page could
simply omit ([[a-cancelled-page-takes-a-status-of-its-own]]).

**Verification: syntax clean, gate exit 0, and a dry sweep runs and maps its candidates.** The
archive-script section of the selftest reads **caught 21, missed 0** with three new cases — a
`target_kind: repeal` decision refused, a `repealed` page without `decided_by:` refused, and the same
page with it released and carrying no `superseded_by:`. **The passing direction is asserted off the
TREE and not off the exit code**, because this script ends by running the gate and a sandbox red for
an unrelated reason would fail the case with the wrong diagnosis.

**What is NOT built here**: the handshake as a release criterion
([[the-sweep-reads-the-handshake-before-it-releases-a-decision]]) and the refused-proposal route
([[a-refused-proposal-releases-every-decision-in-its-list]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`, extended 2026-08-30.)*
