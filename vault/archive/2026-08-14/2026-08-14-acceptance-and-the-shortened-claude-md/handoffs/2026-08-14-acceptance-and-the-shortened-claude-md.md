---
session: 2026-08-14
sprint: S0
commits: none
---

# Handoff — 2026-08-14

The first session that began with a brief it did not ask for. Its work was the acceptance run the
second brain had never had under honest conditions, and three changes the run and the owner's
questions produced.

## 1. State

**Done.**

- **The acceptance run, five questions, five PASS.** Q1–Q4 from
  `docs/superpowers/plans/2026-08-13-acceptance-questions.md`, dispatched as four parallel
  `vault-librarian` agents; Q5 was the owner's own question, asked through `/vault-ask`.
- **`CLAUDE.md` cut from 218 lines to 112** — a map plus four rules, no wikilinks.
- **The in-session feedback channel built**: `.superpowers/sdd/vault-feedback.md`, wired into
  `/handoff`, `/vault-ask` and `CLAUDE.md`.
- **The brief lost its `Active unblocked tasks` section**; `/ingest` step 7 learned to transfer
  `measure:` and `lint:` lines out of section 7, not only misses.
- **`CLAUDE.md`'s AST-test count corrected from five to seven** before the table moved to the vault.

**Not done.** `/lint` has still never run — see section 6. The wiki page that mandates the brief's
removed section has not been superseded; that is this ingest's job. The acceptance results are
recorded here and **not** in the acceptance file itself.

**In flight.** Nothing being edited. **Nothing was committed this session** — `commits: none` is
literal. `git status` flags 23 files; `git diff --numstat` shows **6**. The real changes are
`CLAUDE.md`, three skills (`handoff`, `ingest`, `vault-ask`), and `tags.md` + `log.md` written by
the librarians during the run. The other 17 differ only in line endings, cause unidentified.

**Next step.** `/ingest`, then the owner decides what to commit. Before any code work: open a
sprint. Nothing is queued and the plans end at the visual layer of 2026-08-12.

**Checks.** `bash scripts/vault-check.sh` — ok, one standing advisory (`process` on 23 pages).
**`pytest` was not run and `ruff` was not run**, deliberately: nothing under `src/` or `tests/` was
touched. The only Python executed was a one-off edit script against `CLAUDE.md`.

## 2. Entities

**Appeared.** `.superpowers/sdd/vault-feedback.md` — the session-local draft that now feeds section
7. Git-ignored, lives beside `progress.md`, drained and re-headered by `/handoff`.

**Observed for the first time, both previously unverified.**

- **The `SessionStart` hook fires.** The brief arrived unasked, marked `SessionStart:clear hook
  success:`, carrying the full text of `brief.md` and no staleness warnings. `$CLAUDE_PROJECT_DIR`
  expands correctly in the shell the harness spawns hooks with on Windows. The matcher that fired
  was `clear`; `startup` shares the same matcher string and command but has still not been
  observed on its own.
- **The `PreToolUse` guard fires.** It fired twice on `CLAUDE.md`, once on `Edit` and once on
  `Write`, injecting its advisory text. Advisory as designed: it did not block and did not fail.

**Changed in kind.** `CLAUDE.md` is no longer rules-with-explanations. It is a map, four rules, and
pointers. The brief is one section shorter.

## 3. Decisions

**`CLAUDE.md` is a map plus a handful of working rules; everything else lives in the vault.**
Owner's decision, 2026-08-14. What left: the JavaScript section, the seven-row boundary table, the
swap-target-invariant paragraph, all twelve "rules that bite silently", the six bullets of how a
slice is executed, most of the tests section, and the whole environment section. **Rejected:**
keeping any of it as a summary alongside the vault — nothing is duplicated, and a rule that
survived has to stand without a footnote. **Obliges:** every removal was checked against the vault
first (all nineteen cited pages exist), and this ingest owes the same line-by-line comparison the
previous move was held to.

**All wikilinks were removed from `CLAUDE.md`.** `[[page]]` is Obsidian syntax that resolves inside
the vault and is inert outside it; in `CLAUDE.md` it read as a citation the reader cannot follow.
**Obliges:** the routes to the vault are now `/vault-ask`, `/pre-task`, and the by-hand `rg` recipe,
and all three must stay in the file.

**Four rules stay in `CLAUDE.md`, chosen by one test: obeying them late is the same as not obeying
them.** The production database (no second chance), fix-the-cause-never-the-test, JavaScript may not
decide which rows are on screen, and slice execution overrides any skill — that last one because a
skill will actively and confidently say otherwise.

**Librarian feedback is recorded in the turn it is noticed, not reconstructed at handoff time.**
Owner's observation: the fidelity check as designed — sample ten verdicts and read them beside their
sources — assumes a reader who can judge an English corpus quickly, which for this owner it is not.
So it is not a check he has. **Rejected:** verifying by reading. **Chosen:** verifying by use — the
vault is wrong at the moment it is asked and answers badly, and that moment is free because the work
was happening anyway. **Obliges:** three files carry the rule (`CLAUDE.md`, `/vault-ask`,
`/handoff`), and the draft is drained at handoff or it silently rots.

**The brief's `Active unblocked tasks` section is removed, not kept permanently empty.** A section
that never says anything trains the reader past it. **Obliges:**
`active-tasks-stay-empty-until-a-tracker-exists` must be superseded per the schema.

**An unsourced number is not resolved by choosing one.** The owner does not know which slice
"six hours" refers to and considers the figure unimportant. The fix is to drop the quantity and keep
the claim, not to pick between six and eight-to-ten.

## 4. How it is built

**Writing a wiki page is not a step after the verdict — the verdict *is* the write.** When the
librarian writes `page:X` against a source line, it must create or update X in that same act; the
verdict is the claim that the content landed there. `vault-coverage.sh` enforces the weak half of
this at line 116: `page:<n> does not exist in the wiki` is a `BAD VERDICT`. It cannot enforce the
strong half — that the page says what the source said.

**There are two staleness checks, at two different times, asking different questions.** Step 8 of
`/ingest`, before the brief is written, asks "does this journal match the tree right now?" via
`git log` over the journal's `commits:` range and `git status`. The `SessionStart` hook, next
session, asks "have commits landed since the one carrying `brief.md`?" Neither compares mtimes;
neither subsumes the other.

**A subagent cannot report its own token cost.** The harness reports it to the main session when the
agent finishes, and the main session may not write `log.md`. So a `measure: tokens=` line can only
reach the log through section 7 — which is why the feedback draft carries measurements as well as
misses, and why the first design ("have the librarian record its own cost") was impossible rather
than merely awkward.

**The one-writer property is a convention about who is dispatched, not an enforced lock.** Nothing
serialises two librarians. See section 5.

**Measured cost of a librarian call, for the first time.** Reported as `subagent_tokens`, whose
composition is undocumented: Q1 27584 / 2m54s, Q2 30420 / 2m54s, Q3 58779 / 8m20s, Q4 63400 /
6m53s, Q5 25341 / 1m43s. Q3 and Q4 carried extra instructed work. **Q5 — 25341 tokens, 103
seconds — is the figure for a plain `/vault-ask`.** At Opus 5 list rates that is between roughly
13 and 63 cents depending on what the number counts.

## 5. Lessons

**A parallel fan-out of librarians breaks the vault's one-writer property silently.** Four agents
were dispatched at once; two independently widened the `frontend` tag, and the second reported that
`tags.md` had changed underneath it between its read and its write. Both writes survived because
each re-read immediately before writing and appended surgically — luck, not design. `tags.md` is
the file every librarian wants, which makes it the lost-update target.

**The acceptance instrument can be gamed by its own subject, and had to be forbidden explicitly.**
`docs/superpowers/plans/2026-08-13-acceptance-questions.md` contains the expected answers, written
in advance. An agent that greps for "batch finaliser" can hit that file and produce a flawless run
having read nothing of the vault. Each dispatch carried an explicit prohibition and each agent
reported compliance. This is the same failure shape as every rule in `vault-check.sh` — a check
that passes for the wrong reason — one level up, aimed at the check itself.

**`CLAUDE.md` was wrong where the vault was right, and nothing was looking in that direction.**
It listed five AST boundary tests; there are seven, and `architectural-boundaries` had recorded the
discrepancy already. The project checks pages against code routinely and had never checked the rule
file against either.

**Three counting errors in one day, all the same shape: a stated count drifting from the list it
heads.** Five AST tests versus seven; "six hours" versus eight-to-ten; `log.md` saying "four pairs
of pages" and listing three. Each is prose a script could reach.

**Removing the `CLAUDE.md` confound required a session that started with the shortened file, and
that instrument expires with the session.** The harness injects `CLAUDE.md` into a subagent as it
stood at the *parent session's start*, so every earlier acceptance run silently had the long
version's explanations. Four agents reported the file independently — two by counting a
transcription, two by matching heading order and sampled phrases — all four found the 210-line
post-`d30b317` version. This is the only condition under which the run proves what it claims.

## 6. Deferred

**`/lint` has never run, and the reason is structural.** It is defined as a retrospective activity,
one per sprint; no sprint has ever been opened, so the thing that watches the health of the
knowledge base has never run on its own schedule. **Consequence:** its agenda accrues — three page
pairs proposed for merging, two filenames that understate their pages, two tags past the split
threshold (`process` 23 of 81, `testing` 18), and two recorded gaps (no page for the hooks, none for
the module map). Running the mechanical half costs seconds; the judgement half needs an open sprint
to close against.

**The acceptance results are not in the acceptance file.** They are in this journal only. The file
still shows Q5 as `_Open_` and carries no record of the 2026-08-14 run — including the confound
removal, which is the whole reason the run mattered. **Consequence:** the designed instrument
disagrees with the record.

**`raw/notes/` — two owner notes, cited by the corpus, with no sidecar.** By this project's own rule
they are unfinished ingests, and the only ones.

**The line-ending churn is unexplained.** 17 files show as modified with byte-identical content.
`vault-check.sh` was exonerated by experiment (15 modified before, 15 after, same md5, same mtime);
the `PreToolUse` hook contains no write. Cause unknown. **Consequence:** `git status` overstates
what changed, which is the shape of alarm this project has already learned not to read.

**The AST test pinning the JavaScript boundary is still owed**, unchanged since 2026-08-12. Its
trigger is the next piece of our own JavaScript, and none has been written.

## 7. Feedback to the librarian

Copied from `.superpowers/sdd/vault-feedback.md`, which was written as the session ran.

- measure: five `vault-librarian` dispatches, the acceptance run of 2026-08-14. Reported by the
  harness as `subagent_tokens`, whose exact composition (input, output or both) is undocumented,
  so it is recorded as observed rather than converted to money: Q1 27584 / 2m54s, Q2 30420 /
  2m54s, Q3 58779 / 8m20s, Q4 63400 / 6m53s, Q5 25341 / 1m43s. Q3 and Q4 carried extra work
  (a search-term report, and writes to `tags.md`) — **Q5 is the figure for a plain `/vault-ask`**
- miss: **`test-suite-wall-clock` states a figure that is in neither of its own sources.** The
  page says suite re-runs took "a large share of the six hours that slice took"; `how-a-slice-is-
  executed`, `agent-round-trip-cost` and the primary journal all say **eight to ten hours**, and
  `grep` over both cited sources (`raw/handoffs/2026-08-12-handoff-before-the-vault.md`,
  `CLAUDE.md`) finds no occurrence of "six hours" at all. Surfaced in the Q2 acceptance answer,
  which reported it as a provenance blur and correctly declined to resolve it; confirmed by grep
  in the main session. **The owner does not know which slice it refers to and considers the number
  unimportant** — so the fix is not to choose a figure. Drop the unsourced quantity and keep the
  claim ("a large share of that slice"), or name the slice if the answer is ever recovered. A
  `basis: measurement` page must not carry a number its sources do not
- miss: **`CLAUDE.md` named five AST boundary tests; there are seven.** `test_parser_boundaries.py`
  and `test_normalize_boundaries.py` are AST-based and were absent from the table, so an agent
  reading only `CLAUDE.md` never learned that `parsers/` and `normalize/` are held away from
  `jobhunt.db`, `jobhunt.ingest`, `jobhunt.web` and `sqlalchemy`. `architectural-boundaries`
  already recorded the discrepancy — the corpus was right and the rule file was wrong, which is
  the direction this project does not usually check. Fixed in `CLAUDE.md` this session; the page
  needs no change
- miss: **two librarian instances wrote the vault at the same time, and nothing prevented it.**
  Four acceptance agents were dispatched in parallel; two of them independently widened the
  `frontend` tag in `tags.md`, and the second reported that the file had changed underneath it
  between its first read and its write. Both writes survived, by luck rather than by design —
  each re-read immediately before writing and appended surgically. The one-writer property the
  vault relies on is a **convention about who is dispatched**, not an enforced lock, and a
  parallel fan-out breaks it silently. Worth a page: the guarantee's real shape, and the
  lost-update hazard on `tags.md` specifically, which is the file every librarian wants
- lint: **`active-tasks-stay-empty-until-a-tracker-exists` is being superseded.** The owner's
  decision of 2026-08-14: the brief's `Active unblocked tasks` section is removed rather than
  kept permanently empty, because a section that never says anything trains the reader past it.
  The `/ingest` skill's brief shape has been changed accordingly in the main session; the page
  that mandates the empty section now contradicts the skill and must be retired per the schema —
  `deprecated`, `superseded_by:`, moved to `archive/`. **This is the first supersession the vault
  has ever performed**: no page carries `status: deprecated`, no frontmatter carries
  `superseded_by:`, and `archive/` holds only `.gitkeep`, so the mechanism is unexercised and
  this is also its first test
- lint: **`log.md` says "four pairs of pages" and lists three** (the entry deferring the merge
  agenda). Third counting error found in one day, after five-versus-seven AST tests and
  six-versus-eight-hours. The pattern is specific and worth a rule rather than three separate
  corrections: **a stated count drifts from the list it heads, and nothing checks the two against
  each other.** Both known instances sit in prose that a script could reach
- lint: **`CLAUDE.md` cut from 218 lines to about 110, by the owner's decision of 2026-08-14: it
  is a map plus a handful of working rules, and everything else lives in the vault.** Removed
  wholesale: the JavaScript section, the seven-row boundary table and the swap-target-invariant
  paragraph, all twelve "rules that bite silently", the six bullets of how-a-slice-is-executed,
  most of the tests section, and the whole environment section. **All wikilinks were removed on
  purpose**: `[[page]]` is Obsidian syntax that resolves inside the vault and is inert in
  `CLAUDE.md`, where it reads as a citation an agent cannot follow — the by-hand `rg` recipe and
  `/vault-ask` are the routes, and a rule that survived the cut has to stand without a footnote.
  Every page cited by the old file was confirmed to exist before anything was deleted.
  **What this ingest owes: the check the last move was held to** — read each removed block beside
  the page that now carries it and confirm no page is thinner than the paragraph it replaced. The
  previous shrink (231 to 190) dropped the "all our JavaScript is three inline blocks" sentence
  and the whole-branch review restored it as a **Critical**, which is why this is not optional
- miss: **nothing in the vault describes the test database.** `TEST_DATABASE_URL`,
  `tests/conftest.py` building the schema by fixture, and "never run the suite against the
  production database" appear in `CLAUDE.md` and **in no page at all** — `grep` over the whole
  wiki returns one unrelated hit. Found while checking coverage before the cut above, which is
  the only reason the rule was kept in `CLAUDE.md` instead of moved. The adjacent page,
  `migrations-do-not-drift-from-the-models`, covers `MIGRATION_CHECK_DATABASE_URL` and the
  create_all-never-follows-a-migration trap but says nothing about the ordinary test database or
  the destructive-by-design fixture. **A page is owed**, and until it exists the rule cannot leave
  `CLAUDE.md` — which is the honest reason a four-item list is four and not three
- lint: **`architectural-boundaries` line 25 has gone stale in the other direction.** It reads
  "`CLAUDE.md` names five; there are **seven**" — true when written, and the correction was right.
  `CLAUDE.md` now names no count at all (the table moved to the vault), so the sentence describes
  a file that no longer says that. The page is the survivor and should simply state seven

## 8. Anything else worth keeping

**The acceptance run's results, since they exist nowhere else.** All five PASS.

- **Q1, batch finaliser** — every expected element plus the bonus (`sweep_interrupted` closes only
  `started_by='web'` batches). Drew the `load_state` consequence unprompted, and read the
  no-test-guards-this-rule gap off the page — a gap the *first* acceptance run had found as
  negative space and which has since been compiled into the page. That is the loop closing on a
  single item, visible end to end.
- **Q2, agent round-trip cost** — the number, the provenance, and the boundary that makes an answer
  complete: 5–35 minutes describes *implementer* trips, a librarian call is tens of seconds. Also
  produced the six-hours finding.
- **Q3, JavaScript, asked in Russian** — the narrowed rule, the honest reason (three of slice 3's
  four silent defects were plain coverage gaps), and the owed AST test.
- **Q4, a React rewrite, asked in Russian** — the island rule and its single condition, and the
  required negative space: no decision about a wholesale rewrite exists, and making one would have
  to *supersede* `the-stack-stays-htmx` rather than sit beside it, because `authority:
  frontend-stack` is already claimed.
- **Q5, the owner's question** — "what pages were planned in this project?" Answered: two pages plus
  the shell was the entire planned set; the resume editor and the AI interview are named only as
  examples of the island condition, not as a backlog; `collection-features-deferred` records a
  prediction that did not come true. Negative space: no roadmap page exists at all.

**`/vault-ask` was exercised as an entry point for the first time** — Q5 went through the skill
rather than a direct dispatch, which was the last untested path in the librarian's definition.

**The librarian's writing half was exercised for the first time, and the diff was clean.** Two files
touched (`tags.md` +20/−3, `log.md` +38), no wiki page, no deletion, no contradiction resolved, and
both agents declared their writes unprompted.

**Russian still reaches the corpus only through `tags.md`, and only for vocabulary someone thought
of in advance.** Q3 and Q4 landed because *JavaScript* and *React* survive untranslated into Russian
speech and appear in filenames. `вид`, `браузер`, `клиентский`, `остров`, `переписать` reached
nothing before the run; the agents widened the `frontend` aliases in response. Third and fourth
consecutive run whose entry point was a filename rather than the alias list.
