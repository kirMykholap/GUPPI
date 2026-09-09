---
session: 2026-08-23
sprint: S3
commits: ad839d4..b383dad
---

# Handoff — 2026-08-23

**The second session of 2026-08-23.** The first is already compiled, under
`archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/`. This session
believed for its whole length that it was 2026-08-24; that error and its 44 landing places are in
`Lessons` below, and one of them is in a commit message and cannot be repaired.

Anywhere below, a line beginning **owner:** is the owner's own testimony.

## State

**Done.** Yesterday's ingest committed as `ad839d4` after the owner read the diff of the files the
gate-input clause covers. `decided_by:` admitted to `wiki/proposals/` and `wiki/rules/` and required
in the latter, with all fifteen rule pages carrying one. `refused` and `idea` minted in
`wiki/proposals/`; `Links:` legal in all six folders. One new gate verdict, one new `--lint` counter,
one new precondition in `scripts/vault-archive.sh`, and one operand bug in the same script repaired.
The five-line style rule written and rendering into `CLAUDE.md`. The vault's own `CLAUDE.md`
corrected in four places.

**Not done, by the owner's ruling.** Phase 7 of the plan — the ratification hook — cut whole.
Criterion 4, region coverage, untouched at `7 of 15`. The ratification sweep untouched at 27 blocks.
The `decided_by:` back-fill in the 31 `proposals/` pages.

**In flight.** Nothing.

**Next step.** The `/ingest` that follows this file, and then the next session's first item: the
`idea` / `decided_by:` pair, which the owner ordered built at the retro after this session had
dropped it.

**Checks.** `bash scripts/vault-check-selftest.sh` — `caught 168, missed 0`, exit 0, read from its
own invocation and not through a pipe. `pwsh scripts/hook-selftest.ps1` — `caught 123, missed 0`,
exit 0, 58 s; it had not been run against the four changed scripts at all. `bash
scripts/vault-inject.sh` — 0 rewritten, 0 generated, 0 removed, 0 problems. `bash
scripts/vault-check.sh` — exit 0, one standing advisory at `7 of 15`. `bash scripts/vault-check.sh
--lint` — exit 0. `bash scripts/vault-authority.sh --check --binding` — exit 0. **`uv run pytest`,
`ruff check`, `ruff format --check` and the browser walk were not run and are not owed**: no Python
changed and the product has not moved since 2026-08-12.

## Entities

**Changed.** `scripts/vault-archive.sh` gained a second precondition — a proposal carrying `status:
refused` is not released without `decided_by:` — and had its `--include` operand repaired.
`scripts/vault-check.sh` gained a verdict on the target of `decided_by:` and a `--lint` counter of
the shortfall. `scripts/vault-check-selftest.sh` gained ten cases and a runner that reads the
injector's own exit and message, which no helper there did before. The six `wiki/*/_schema.yaml`
gained `Links:`; two of them gained `decided_by:`.

**Appeared.** `wiki/rules/write-plainly-name-the-source-and-say-what-is-not-done` — the style rule,
`governs: CLAUDE.md`, one slice, five lines.

**Taken out of service.** None.

## Decisions

**The causal chain, and it is the owner's.** A decision produces a **proposal or a rule** and
nothing else; anything further down names what it descends from in `sources:`. So `decided_by:` is
legal in `wiki/proposals/` and `wiki/rules/` alone and illegal in the other four. This narrows
[[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]], which obliged it in all six and was
one day old. He stated the extension to rules himself, after `/pre-task` found that `authority:` is
forbidden there and the field is therefore the only way a rule can name its decision.

**The all-six argument on that page is false, and was repaired rather than left standing.** It
grounds the obligation on the gate iterating the fields a folder *declares* — true for `values:`,
where a folder left out loses its verdict silently, and false for a **key**: `vault-check.sh:382`
reddens a page carrying a key that appears in neither list. A key fails towards refusing. The
narrowing is therefore safe by construction, not by permission.

**A refused proposal carries `decided_by:` and no `superseded_by:`.** *(owner selected, chosen
against his own first design, which was `superseded_by:` naming the refusing decision.)* Two grounds
were put to him and he took them: a per-folder schema states one required set for the whole folder
and cannot express "required when the status is X"; and `superseded_by:` is written in both
directions on purpose, so a proposal pointing at a decision would need that decision to claim it
supersedes a proposal, which asserts a different claim.

**So the conditional lives in `scripts/vault-archive.sh` and not in a gate verdict.** *(The session's
consequence, not his ruling — he had accepted a verdict in `vault-check.sh`.)* `/pre-task` found that
verdict unreachable: a refused proposal is in `archive/` by the time the rule applies, and the
frontmatter pass reads `wiki/` alone. The refusal moved to the moment of the move, which is the last
point anything sees the page.

**No second existence check was written for `decided_by:`.** Measured before deciding: a target that
resolves to nothing already prints `broken wikilink`, because a wikilink in frontmatter is swept
exactly like one in the body; a target that exists and is an `entity` printed nothing and the gate
exited 0. Only the second is new. A second existence check would be a second reader of a fact rule 5
already reads.

**`refused` is not admitted to `decisions/`.** A decision is not refused, it is overturned, and
`deprecated` + `superseded_by:` already does that.

**The whole `concepts`/`lessons` bullet struck from the vault's `CLAUDE.md`.** *(owner: «Вычеркнуть
полностью».)* The session recommended keeping the `lessons` half and was overruled. Verified first
that the claim is not stranded: `lessons` is defined independently in the Layout table and in
`index.md`.

**The `--include` operand repaired in `scripts/vault-archive.sh`.** *(owner: «чинить».)* Asked three
times across the session before it was answered.

**The rule `ask-before-weakening-or-working-around-a-rule` is ratified, nine days after it began
being enforced.** It had no decision behind it at all: written into `CLAUDE.md` by the session that
shortened the file at `36e9e4c` of 2026-08-14, and accounted for nowhere. The librarian refused to
point the field at the nearest plausible page and reported it instead. The text was read to him and
he answered:

> **owner: да, это мое решение. Подписываюсь**

**The `idea` / `decided_by:` pair is to be built.** *(owner: «нужно построить».)* This session had
built it from his own sentence and then dropped it, arguing that it makes `status` mean
*authorisation* where his ruling of 2026-08-17 makes it mean *maturity*, and that the verdict would
redden all 31 proposals on the day it lands. The objection was raised twice and overruled. **The
ordering is part of the item**: the verdict must follow the back-fill of the 31 proposals, never
precede it, or it reddens the tree and locks the librarian out of the work that would clear it.

**The librarian reports each criterion's decider output at ingest, and it goes into the brief.**
*(owner's design, refined in conversation.)* Not a judgement — the output of the command each
criterion names. His first proposal was that the librarian read criteria and rewrite the sprint; he
withdrew it once the session named the standing prohibition that forbids the party doing the work
from judging whether it is done. **What his design fixes is a real gap**: the librarian reported
state in enormous detail all day and no criterion was read, because the report is too long for
"done or not" to fall out of it.

**Criterion 3 reworded**, and its `314 pages` figure with it. *(The session's wording, ratified by
plan approval — the same shape S3's own criteria carry.)* The field is legal where it means
something and the `--lint` count is over those folders. The `314` was not derivable from anything:
no page carried the field then or now, and `wiki/` held about 530 pages that day.

**The style rule's watcher is the owner.** *(owner: «сторож - я».)* It has no mechanical instrument
and is now the sixth rule in that condition. **This is a third closure shape for criterion 1**,
alongside an instrument and a page saying why none is possible — and the criterion's decider counts
only the first. Fixing the command to count all three is his ruling.

**The style rule does not govern what is written into `wiki/`.** *(owner: «Правило стиля только для
общения - это правильно».)* The librarian works to its own rules.

**Phase 7 cut whole.** *(owner: «окей, согласен с твоим разделением. Переносим на следующую сессию
все, что не влазит сегодня».)* Rejected: doing half of it, which would leave an unregistered hook
and a rule naming a destination that does not exist.

## How it is built

**A rule's decision could not be named until today, and `sources:` is why.** A rule page carries its
decisions inside `sources:` mixed with the file it governs and with every other citation. Ten of the
fifteen named at least one `decisions/` page there, five named none, and two of the ten reached one
only through `archive/`. No reader — human or script — could tell which entry was the cause. That is
the hole `decided_by:` closes, and the field found it: nine days of reading had not.

**Promoting a field to `required:` has a recorded order, and it is not on a page.** It is a comment
block in `wiki/proposals/_schema.yaml`: legal and optional first, then the back-fill, then promote.
Required first turns the gate red, and `lock-the-librarian.ps1` reads a red gate as a refusal to
dispatch — locking out the only writer permitted to fill the field. The plan had it backwards and
`/pre-task` reversed it.

**A conditional requirement cannot live in a per-folder schema, and the store already had the
shape.** `rules/_schema.yaml` says so about `paths` under `render: whole`: the injector reports it,
because the schema states one required set for a whole folder. `refused` + `decided_by:` took the
same route.

**The link sweep resolves a wikilink by filename alone.** `resolvable` is built by stripping the
directory from every `.md` under `wiki/` and `archive/`, so moving a page changes nothing and
**renaming** one breaks every inbound link. That is the difference between the two fields: a path in
`sources:` addresses a place and is rewritten by the archiver; a wikilink in `decided_by:` addresses
a name and is never touched by a move.

**The archive exclusion follows the four RAW kinds and not the whole of `archive/`.** Proved in both
directions: a journal there with an unresolvable wikilink leaves the gate green, and a retired
**page** there with the same wikilink reddens it. Without the second half the pair would only prove
the sweep got quieter, which is the direction a defect hides in.

**The suite is a mutation test of the checker.** Each case takes a known-good copy, breaks exactly
one thing, runs the gate and asserts it reddened **with the message naming that thing**; the copy is
per case because a leaked breakage makes the next case fail with the wrong diagnosis. The cost
follows from the shape: 102 of the cases break one thing and evaluate all twenty rules.

## Lessons

**`/pre-task` ran between the plan and its approval and killed three items of it as factually
wrong** — a selftest case for the verdict `realised`, written and removed the same day on the owner's
own correction; an archive step for a journal already sitting in `archive/`; and a gate verdict that
could never fire. It also reversed the promote-first ordering above. **Its two counts: the shortlist
named 99 pages and the agent opened 33 in full**, plus two registers, two `_schema.yaml` and five
tree files. It cost 225,195 tokens and 16 minutes.

**A date is a measurement and this session did not measure it.** It inferred today from the previous
session's date; the previous session was the first of 2026-08-23 and this is the second. Nothing was
consulted — not `date`, not `git log`, not the brief's own `# Brief — 2026-08-23` heading. The wrong
date reached **44 places**, including a `decided:` frontmatter field and the message of `ad839d4`,
which says the ingest was *committed a day late* and cannot be repaired because git history is not
rewritten. **Three of the 44 were not date strings but intervals computed from one** — *one day old*,
*the day-old page*, and a citation that after repair would have read as a page rejecting its own
ruling — so a grep for the digits alone would have left the corpus asserting what no line said.
Caught by a subagent whose environment reported the real date and which **reported the conflict
rather than conforming to its brief**.

**An exit code read from the wrong stage of a pipeline, four times in one session.** `grep -c`
printing `0` exits 1 and broke three `&&` chains; `bash suite | tail -25` reported exit 0 while the
suite had `missed 1`. The store carries a page on exactly this and the session cited it after the
third occurrence rather than before the first. **Knowing the page exists is not the mechanism.**

**`tail -25` on a suite hides the one line worth reading.** The report prints each MISSED case with
its detail; truncating cut the diagnosis and left a choice between a blind 30-minute re-run and
reasoning from the fixture helpers.

**A chained command reported success after the chain had already broken.** A `python -c` failed on
quoting, `&&` skipped the `cat` that was to write two feedback lines, and an unconditional `echo` on
the next line printed `recorded.` anyway. Nothing had been recorded.

**A `run_clean` case built on `rule_page` can never be green**, because that helper plants a rule
page without the region its destination needs and the gate is red on that. Its companion red case
was red for two reasons at once, passing partly for the wrong one. Cost: one 30-minute suite run.
The helper that plants both is `region_resolves`.

**Proving each fixture by hand before writing it into the suite paid twice in one session.** The
first probe of the schema changes planted new pages and failed on tag count, orphanhood and an
unregistered `authority` — and two of its apparently passing red cases could have been passing for
those reasons. Rebuilt to mutate real pages. Each proof cost seconds; the suite costs thirty minutes.

**The suite's cost is superlinear in the corpus and the sandbox is not the reason.** Measured
2026-08-23: **1635 s** at 543 pages against the store's recorded **368 s at 379 pages** — 1.43x the
pages, 4.4x the time. The sandbox is 6.3 MB and 733 files. `sys` 35m against `user` 15m says file
I/O, and eleven workers reach only 1.7x speedup, so they contend on disk. The multiplied term is the
gate itself, which went from 8.5 s to about 13 s as the corpus grew and runs once per case.

## Deferred

**The ratification sweep — 27 blocks across 22 pages, deferred a third consecutive time**, and the
first time with the list in front of him. *(owner: «ужас конечно... Давай не сейчас».)* Consequence:
`basis: human` pages outrank everything in a conflict and none of these has been checked against him,
now for a fourth session. **Two of the 27 sit on pages this session's work rests on** — the clause
letting a session write the schemas, and the rule that legal values live in each folder's schema.

**The `decided_by:` back-fill in the 31 `proposals/` pages.** Consequence: the `idea` pair the owner
ordered built cannot land until this does, or it reddens all 31.

**The hook that writes `- miss:` in plan mode.** *(owner: «напомнить об этом в следующей сессии».)*
Consequence: the feedback rule has now been broken eight times, always for the same reason, and this
would give one of the six instrument-less rules its instrument.

**Region coverage, criterion 4**, at `7 of 15`. Consequence named by its own page: the eight unmarked
files are unchanged, and this is never to be reported as coverage improving.

**Beads** — a question to him next session. The session does not know what the word means here, which
is the whole of the problem, and it has been named twice without ever being put back to him.

**Obsidian CLI as a proposal.** *(owner: «да, запиши как proposal».)* The official CLI searches, lists
and queries frontmatter, and could strengthen the reading surface — the catalogue and the family
lookup. It cannot carry the checking or the injection: those encode this project's own contract, which
no general tool knows. And it requires the Obsidian desktop app to be **running**, which is
disqualifying for a gate invoked from hooks and read by `lock-the-librarian.ps1`.

**Whether the style rule also governs `wiki/`** — answered no for now, and the question was raised by
the proposal and never put to him before today.

## Feedback to the librarian

- miss: the ingest of 2026-08-23 filed the deferral *a proposal for a corpus-versus-code check is owed and not written* onto `wiki/entities/openspec-and-spec-kit.md` alone. That page carries the observation that the two external toolkits have such a command and this project does not; it does not carry the commitment. The template routes `Deferred` to `decisions/` for the deferral and `proposals/` where a design sits behind it, and neither page exists. Found by the fidelity sample after the ingest reported INGEST COMPLETE, at line 246 of the journal — coverage was 88 of 88 and could not have seen it.
- miss: the brief of 2026-08-23 alarms that the five-line style rule is lost — "grep -ril KISS over the whole repository matches the journal and nothing else", "the five lines survive only in the chat log", and recovering them "means asking you again". They are not lost. The full text is in the approved plan that opened S3, at `C:/Users/kir/.claude/plans/agile-percolating-wall.md` lines 167-172, under phase A1. The search was scoped to the repository, and the plan the owner reads in order to approve it lives outside the repository by the language rule saying so. Surfaced in the first minutes of the session, reading the brief beside the plan it was generated from — so an alarm was raised, and a question was owed to the owner, on a document that exists.
- miss: the brief of 2026-08-23 alarms that `vault-check-selftest.sh` "had silently gone to `caught 157, missed 1`" and calls it a suite regression found by accident. Run today on a green tree it reports `caught 158, missed 0`, exit 0. There is no regression: the missed case is `lock allows the librarian on a green gate`, which prints MISSED whenever the tree is red, and the tree was red at the moment yesterday's figure was taken. The brief presents a property of a known deferred case as a defect in the suite, and the plan for today carried a phase to diagnose it. Surfaced by running the suite as the first work of the day.
- miss: a second ratification of the owner's exists only in a journal and was never compiled — his ruling that `the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault` is one page carrying two sections and not a third page. It lives in `archive/2026-08-22/.../handoffs/` and in a section of the rule page, and in no `decisions/` page. Found by the librarian while filling `decided_by:` across `wiki/rules/`; it is the same class as the finding about `ask-before-weakening-or-working-around-a-rule` and was found by the same mechanical pass.
- process: reading the diff of 2026-08-23 I took `scripts/vault-inject.sh` hardcoding the pair `current`/`deprecated` for a second register of a list the corpus had just ruled must have one, and it is not. The script states the reason in place, at lines 259-263: this script is the WRITER, and a writer that learns its legal set from the same file as the reader can agree with the reader while both are wrong. So the duplication is deliberate and is the opposite of the gate defect it resembles. Recorded because the resemblance is close enough that a later reader will make the same wrong call, and nothing outside that comment says so — no page carries the writer-and-reader-do-not-share-a-register argument, and the corpus is where it would be looked for.
- process: `scripts/vault-archive.sh` wrote `grep -rlF -- "$slug" "$VAULT/wiki" --include='*.md'`, and `--include` placed after `--` is an OPERAND rather than an option — grep reports `No such file or directory` on it, suppressed by the `2>/dev/null` beside it, and searches with no filter at all. `wiki/*/_schema.yaml` carries **13 real page slugs** inside its comment blocks, so the `pages` precondition counted a mention in a schema comment as a live page naming the slug. **Repaired 2026-08-23 on the owner's ruling** and proved by switching the line back and forth: with the fix the page is refused with exit 2, without it the archiver walks straight past the precondition and reports `cited by 0 page(s)`.
- process: this session inferred today's date from the previous session's date instead of reading the clock, and was wrong by a day for its whole length. The previous session was the FIRST session of 2026-08-23; this is the second. Nothing was consulted — not `date`, not `git log`, not the brief's own `# Brief — 2026-08-23` heading — and the wrong date reached **44 places**: nine schema comments, three script comment blocks, four feedback lines, seven lines of `sprint.md`, seven of `log.md`, two registers, three `decisions/` pages, and a `decided:` frontmatter field. It also reached the commit message of `ad839d4`, which says the ingest was "committed a day late" and cannot be repaired because git history is not rewritten. Caught by a subagent whose environment reported the real date and which REPORTED THE CONFLICT rather than conforming to the brief it was given. Three of the 44 were not date strings at all but intervals computed from one — "one day old", "the day-old page", and a citation that after repair would have read as a page rejecting its own ruling — so a grep for the digits would have left the corpus asserting things no line stated. The generalisable half: a date is a measurement, and this store's own rule is that a count is written with its date or not written; the session treated the one number every record carries as the one number it did not have to measure.
- measure: `bash scripts/vault-check-selftest.sh` costs **1635 s wall clock** (27m15s; user 15m11s, sys 32m51s) on 2026-08-23, over a corpus of 543 pages under `wiki/`, reporting `caught 158, missed 0`, exit 0. The figure the store carries is **368 s parallel at 379 pages**. So a 1.43x corpus cost 4.4x the time, and `sys` exceeding `user` says where it went. Two later runs the same day, at 167 and 168 cases, took 29m50s and comparable. The superlinear shape is the thing worth keeping, not the number.
- lint: the `authority.md` family *admitting a frontmatter field* stood at twelve slugs over a ceiling of ten and this session took it to **thirteen**, then to fourteen with the two ratification pages. The owner read it as a symptom rather than an item: «плохо. Еще один показатель, что vault растет быстро и что делать мы не знаем». Rebalancing is a judgement about the corpus and belongs to `/vault-lint`.
- lint: the `external` tag was ratified and never minted. *(owner: «отчекань».)*

## Anything else worth keeping

**The librarian crossed a boundary and reported it unprompted.** To render the style rule it inserted
the empty marker pair and a heading into the repository's `CLAUDE.md` — a session's file, not its —
because the brief asked for a render without providing the anchor to render into. One heading and two
comment lines; the text between the markers was written by the injector.

**A subagent's result was flagged by a security scanner as a fabricated owner quote.** It was not: the
scanner sees the subagent's transcript, in which no user turn exists, because the quotation reached it
through the dispatch brief — which is how this ritual is designed to work. The written block was
checked character by character against what he typed and matched, and it is the only Cyrillic on the
page. **The check was worth running anyway**: a fabricated quote signed with his name is this
project's worst failure mode, and "I am confident" is not a verification.

**The proposal that carried the style rule took `status: implemented`** — the first use of the value
minted the day before.

## Harness

- harness: `scripts/vault-check.sh` — the link sweep now excludes the four RAW archive kinds (`handoffs`, `plans`, `specs`, `notes`) from the set whose outbound links must resolve, while leaving them resolvable as targets. Decided and applied 2026-08-23, AFTER the previous ingest closed, so no page records the repair itself. The cause: archiving a journal moved it from `raw/`, which the sweep excludes, into `archive/`, which it reads whole — and the owner's own Russian in that journal contains `[[викиссылки]]` as an illustration. `vault-archive.sh` reversed its own move and step 12 of that ingest could not finish. The exemption now follows the file rather than the directory, on the same ground the `raw/` exclusion already states: archiving does not make a file mutable. **It now has a selftest case in both directions.**
- harness: **the librarian is to print, at each ingest, the output of the command each sprint criterion names** — the output, never a judgement — **and that output goes into the brief.** The owner's design, and his addition of the brief is the load-bearing half: it puts the criteria state at the front of the next session instead of leaving it to be excavated. This does not touch the prohibition on the librarian judging whether a goal was met; he considered overturning that and withdrew it once the prohibition was named. Files to change: `.claude/agents/vault-librarian.md` and whatever generates `brief.md`.
- harness: **criterion 1's decider counts only selftest cases, and the criterion permits two other closures** — a page saying no instrument is possible, and, as of today, *the owner watches it*. The command must count all three or the criterion can never read as met however much work is done. The owner ruled the command is what changes.
- harness: **`Links:` is legal in all six schemas and no script writes it.** The writer was ruled to be a script rather than an agent because an agent filling a field by reading its own page is a field that drifts. *(owner: «значет нужен скрипт, добавляем в спринт».)*
- harness: **the suite's sandbox path should be excluded from the virus scanner before anything is rebuilt** — it costs nothing, it is reversible, and it is a measurement rather than a change. Then: give `scripts/vault-check.sh` a way to run one rule, since 102 of the cases break one thing and evaluate all twenty; the 30 `run_clean` cases must keep running the whole gate, because *nothing anywhere went red* cannot be narrowed. **Cost of the second, stated now rather than discovered later:** running all twenty rules gives incidental coverage that nobody designed and nobody watches, and narrowing removes it silently.
- harness: **`plant_rule_page` now hardcodes `decided_by: [[a-refused-proposal-is-archived-and-takes-status-refused]]` and 43 cases stand on it.** Renaming or retiring that page reddens forty-three cases at once for a reason none of them is about, and nothing points at the coupling from the page's end. The safe shape is a fixture that plants its own decision page.
