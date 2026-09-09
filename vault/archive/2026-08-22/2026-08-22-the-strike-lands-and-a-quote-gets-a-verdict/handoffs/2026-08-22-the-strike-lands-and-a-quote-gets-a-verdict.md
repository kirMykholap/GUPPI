---
session: 2026-08-22
sprint: S2
commits: 638a433..5112e25
---

# Handoff — 2026-08-22

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

**A line beginning `owner selected:` is a shape ruled into existence during this session's own
retro**, and it is not a quotation. It carries the label of an option this session authored and he
chose from a rendered menu — his ruling, the session's words, and the words were on his screen when
he took them. Where it changes the meaning, what it was chosen *against* is written with it. See
`Harness`.

**Measured on this session, because it is the reason that shape exists:** of ten owner utterances,
**two were his own words** — *«что сегодня делаем?»* and *«согласен с рекомендациями»* — and neither
settles anything. All eight rulings arrived as menu selections. He raised it himself.

Every section stays, always. An empty one is a legal answer — write "none". A dropped one is
knowledge that was never asked for, and nothing else in this repository looks inside `raw/`.

## State

**Done, and each verified by its own command.**

- **`A1`, the strike.** `advisory-is-the-default-for-a-hook` is `deprecated`, carries
  `superseded_by:`, and moved into `archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/pages/`.
  Five pages that took a disposition from it are re-argued against the three-condition test — four
  named in the plan, the fifth found by the librarian while executing.
- **`vault-archive.sh` gained a `pages` kind**, the fifth and the first that is not an inbox kind.
- **`A2`, a quote is Cyrillic.** A `wiki/rules/` page governing **two** destinations — the first in
  this corpus — with regions rendered into `.claude/skills/handoff/SKILL.md` and
  `.claude/skills/ingest/SKILL.md`. Rule 14 of the gate is an advisory behind `--lint`.
- **The block-form `governs:` verdict**, joining the existing frontmatter verdicts rather than
  taking a number.
- **`B4`**, `.claude/hooks/record-the-dispatch.ps1` on `PostToolUse` for `Agent|Task`.
- **PyYAML declared** as a dev dependency.
- **The seventh S2 criterion** is written into `sprint.md`, and its decider was repaired the minute
  after it was set.
- **`.claude/skills/retro/SKILL.md`** gained the third attribution shape and the
  decisions-not-utterances clause, during the retro that produced them.

**Not done, and deliberately:** `B1` and `B3` (out of the approved scope; `B3` goes first next
session at a higher price than it had this morning), `B5` (gated), `A4` (waits on the owner reading
27 blocks).

**In flight:** nothing. Working tree clean at `5112e25`.

**Checks, each exit code read from its own invocation.**

- `bash scripts/vault-check.sh` → **0**, one standing advisory, `a region or whole generation
  covers 6 of 15`. **The numerator moved and the denominator did not**; the remaining unmarked
  files are otherwise unchanged, and no criterion is read off here.
- `bash scripts/vault-check-selftest.sh` → **caught 158, missed 0**, from 147. Eleven cases added.
  Run against the exact tree that was committed, after two earlier runs measured trees that had
  since moved.
- `powershell scripts/hook-selftest.ps1` → **caught 123, missed 0**, from 114. Nine cases added.
- `bash scripts/vault-inject.sh` → **0**, and idempotent: a second run rewrote 0 regions.
- `bash scripts/vault-authority.sh --check --binding` → **0**, both halves, after the repair.
- `bash scripts/vault-check.sh --lint` → 27 owner-attributed blocks named, one per line.

**Not run, and said so:** `uv run pytest -q`, `ruff check`, `ruff format --check`, and no browser
walk. **No Python changed** — `git status --porcelain | grep -c '\.py$'` returns 0 — so none of
them is owed, and this is stated rather than a green suite being claimed.

**Next step:** `B3`, the `/pre-task` agent, whose price rose today.

## Entities

**Appeared: `.claude/hooks/record-the-dispatch.ps1`.** Registered on `PostToolUse` for `Agent|Task`,
writing one ledger row per **returned** dispatch as `dispatch:<subagent_type>`. Post rather than
pre because a returned result is evidence of work where a requested dispatch is evidence only of
intent. It can never refuse — `PostToolUse` fires after the act — so it is not a candidate for the
refusal test at all. **It has never fired**: it was registered after this session's dispatches
began, and its live firing is owed against a restart.

**Changed: `scripts/vault-archive.sh`** — a fifth `kind`, `pages`, and the first that does not come
from `raw/`. Its `sources:` rewrite had nothing to do on its first cargo, because no page cited the
retired page in `sources:`; that is correct here and not the instrument failing.

**Changed: `scripts/vault-authority.sh`** — the argument dispatch became a loop over the
argumentless modes, with the exit code the worst of those run rather than the last. The
operand-taking modes keep single dispatch and refuse anything after them.

**Changed: `scripts/vault-check.sh`** — rule 14, and the `blockgoverns` verdict.

**Changed: PyYAML** — from an undeclared transitive extra of `uvicorn[standard]` to a declared dev
dependency. It was always installed; nothing about the product needs it.

**Taken out of service: `wiki/decisions/advisory-is-the-default-for-a-hook.md`**, retired to the
dated archive.

## Decisions

**owner selected: Датированно, по решению** — chosen **against** the flat practice every other
retired page follows. The archive decision has said since 2026-08-16 that retired wiki pages are
dated by the day they were retired; the tool could not express that destination, so about thirty
pages went flat instead and **the practice quietly outvoted the rule for six days with no
instrument reporting it.** Rejected: keeping the flat form, which is what the plan had assumed from
reading the tree rather than the corpus.

**owner selected: Да — authority как индекс** — the seventh S2 acceptance criterion, chosen
**against** the admission rule and the `binding:` field. Written in the sprint's own shape: *"`authority:`
is on every page outside `wiki/rules/`, and the register agrees with the tree in both directions"*,
decided by `bash scripts/vault-authority.sh --check --binding`. The admission rule is the most
important of the three and is decided by no command; this sprint has already carried one criterion
of that shape.

**owner selected: Объявить PyYAML** — chosen **against** a generated sidecar per register and
against leaving five scripts hand-parsing YAML. **This does not open the dependency rule**: the
harness holding onto another package's extra *is* the fragility that rule exists to prevent.

**owner selected: B4 строим, B5 ждёт** — chosen **against** building both, and against dropping the
chain. The blocking write gate becomes legal only once the recorder has fired for real.

**owner selected: Записываем и идём дальше** — the harness-versus-product split, chosen **against**
making it S2's seventh criterion, against opening the next sprint on the product, and against
deferring it to this retro. Measured by the session rather than quoted: **128 commits since
2026-08-12, 107 touching the harness or the vault, and `src/` last moved on 2026-08-12** in
`e15a12c`. `proposals/an-admission-test-for-mechanisms` now has its verdict: not a criterion.

**owner selected: За --lint** — the quote advisory's channel, chosen **against** a bare run naming
all 27 and against a bare-run counter with the list behind the flag. 27 blocks would otherwise
print on every run until a sweep that waits on him.

**A divergence: an approved scope was widened twice without asking.** `scripts/vault-authority.sh`
and `scripts/vault-check-selftest.sh` were both repaired outside the plan. Both were forced — the
first made the criterion he had just set undecidable, the second turned the whole suite red — and
**that is exactly how it looked at the time**, which is the clause this section exists for. Ruled
afterwards under a narrower rule than the session used: **a repair without which the approved work
does not run does not have to be asked for, provided it is named in the report.** Rejected: *"files
that are already the session's"*, which admits anything under `scripts/`.

**A divergence: `/pre-task` phase 2 was read by hand rather than dispatched**, on the standing
instruction against spawning agents unasked — so the clause it exists for, *say what is missing from
this list*, was put to nobody, on the second consecutive day that has happened. Ruled: the
instruction does not reach the ritual. Rejected: obeying the instruction and asking oneself the
question in writing, which is not a review.

**A divergence: a multi-select whose options contradicted each other was read as a union without
asking.** No harm followed; the reading was right. Ruled: the session stops and asks, once.

## How it is built

**`archive/<date>/<session>/pages/` is where a retired page goes**, and the mechanism now exists.
`vault-archive.sh` moves the file and rewrites `^sources:` citations of it as one run, then runs the
gate itself, because between the two the tree is red and a filesystem cannot make the pair atomic.

**Rule 14 reads bytes, not a character class, and that is a measurement.** Cyrillic is U+0400–U+04FF,
whose UTF-8 lead bytes are exactly 208 to 211; the class is built from those codes under `LC_ALL=C`
so no locale can reinterpret them. It was proved on planted input in both directions before it was
wired into the gate, and its reading — 27 — was reconciled against an independently measured
28-on-2026-08-21 exactly: the ingest added pages, and the struck page carried **two** owner blocks
and took the English one to `archive/`.

**The block-form verdict repairs a diagnosis rather than a colour.** A rules page written in the
block form was already red, because the scalar is empty and `nogoverns` fired — so the gate said *"a
rule with no `governs:`"* about a page naming two destinations plainly, sending the reader to add a
field already there.

**A ledger row is an observation and the discharge is an inference, and they live apart.**
`record-the-dispatch.ps1` writes `dispatch:<type>`; `Read-LedgerState` is what decides that
`dispatch:pre-task` discharges the ritual. A hook writing `pre-task` directly would assert a
conclusion in a column, and a later reader could not tell an inference from a sighting.

**What that repairs:** `/pre-task` records itself by a script the **session** runs, plan mode forbids
the session to write, and the rule places the ritual inside plan mode — so the ritual performed
exactly as written left no row and the guard then reported that none had run. Four times in one
session on 2026-08-21 and once more today. A hook can write during planning.

## Lessons

**`governs:` has three readers and the count lives nowhere.** The gate and `scripts/vault-inject.sh`
were both taught the inline-list form on 2026-08-21, written from the same four rules and
deliberately not shared. The sandbox builder inside `scripts/vault-check-selftest.sh` reads the same
field with a scalar `sed` and nobody counted it. The first rule page to govern two files handed it
`[a, b]` as one destination: it materialised a file under that name, copied neither real
destination, and rule 12 went red in every case — **`caught 112, missed 44` against three real
failures.** The corpus argues that two parsers written from one set of rules beat one shared copy;
**the cost that argument does not name is that a third parser is invisible until a page exercises
the difference.**

**An instrument that answers half a question in the voice of a whole one.**
`scripts/vault-authority.sh` dispatched on `case "${1:-...}"`, so `--check --binding` ran the check,
dropped `--binding` without a word, and exited 0 with a report that looked complete. **Found within
a minute of that command being named as an acceptance criterion's decider** — the criterion was
undecidable for the whole of its life, and nothing said so.

**Two selftest cases ran, passed, and were never counted.** Written as bare `( … ) &` subshells
calling `report` directly, so `next_rf` incremented inside the subshell and the collector iterated
past their files. The suite printed **`caught 156, missed 0`** — a clean number with two cases
missing from it — and **nothing in the suite would ever have said so**: a dropped case looks exactly
like one that was never written. **What found it was arithmetic**: eight added against six reported.

**The session argued in prose what it broke in code.** All three of the above are instruments
failing towards *nothing to report*, and the session spent the day writing comments about exactly
that class while shipping two of them. Each was caught by a different mechanism than attention,
which is the argument itself.

**An apostrophe closes a shell single-quote from inside an awk comment.** `owner's` and `one's`,
twice in one edit, turned the gate into a bash syntax error. This corpus already carries a page
about multi-line edits through a shell; the burn it records is backslashes, and this is the same
class from a different angle. `bash -n` caught it immediately.

**`grep -c` counts lines, not occurrences.** The session reported a `log.md` entry as appearing
twice; it appears once, in a wrapped paragraph. Caught on re-reading and corrected in the same turn.

**A verification line can be the wrong instrument on a correct tree.** The plan asked
`grep -c CONTRADICTION … # 0` and the right answer is 2: the callout is gone and its words survive
inside a dated section, because nothing here is deleted. The question is *is the callout live*, not
*is the word present*.

**`/pre-task` paid for itself, and the incident is exact.** The plan assumed the flat archive
because that is what the tree shows — thirty retired pages sitting flat, one retired the day before.
The corpus said dated. Executing the owner's choice then exposed a clause that had been
**unexecutable for six days**. None of that was reachable by reading the tree.

**The register-as-test shape earned its second payment inside a week.** Ratified for hooks on
2026-08-21 over a sentence in prose; today the table went red the moment a registration was added
without being listed.

**A dispatch that only executes cannot review its own brief.** The librarian was told step 4 was a
correction owed on `session-hooks`, found it had been made a day earlier, said so and wrote nothing;
it was told four pages took a disposition from the struck rule and found a fifth. **Both are what
phase 2 of `/pre-task` buys**, and this session did not spend it.

## Deferred

**`a-refusal-is-conditional-or-absolute-and-nothing-else` goes to the top of the `A4` list.** It is
`basis: human`, `binding: prohibition`, and the ruling it states is absent from the source it cites,
re-checked at two ingests. **Striking a second prohibition on the session's reading would repeat
the morning's failure exactly**, and he has not read its text. Consequence of waiting: a prohibition
nobody gave stays enforceable for a third session.

**The `A4` sweep of 27 blocks happens next session**, the session bringing each block with its text
and acting only on what he disowns. Not today: twenty-seven read consecutively are read carelessly
by the tenth, and carelessness there costs a rule.

**`B1` and `B3` were not owed today, ratified retrospectively.** The option he selected named six
items including the pre-task agent, and the plan carrying their removal was written before that
answer. `B3` cannot be tested in the session that writes it; `B1` renders into two reading agents of
which the second **is** `B3`. **`Q4` raised `B3`'s price**: once `/pre-task` always dispatches, the
agent stops being a convenience and becomes how the ritual is performed.

**`B5` waits on `record-the-dispatch.ps1` firing in a live session.** Consequence: the pre-task
ledger's plan-mode hole is repaired in principle and unproved in fact.

**The ~30 flat retired pages stay flat**, and the dated clause is forward-only from 2026-08-22.
Sweeping moves thirty addresses and drags `sources:` behind them; the precedent is the English rule,
forward-only with the file as its unit.

**Eleven slugs in the `hooks` family against a ceiling of about ten** go to `/vault-lint`, the ritual
that exists for judgements about the corpus. Rejected: raising the ceiling, which is how a
measurement stops saying anything.

**The quote proposal retires once its one remaining claim moves to the decision page** — whether a
paraphrase is demoted to `basis: inference`. That question goes onto the sprint: it is about the
rank of a paraphrase that survives ratification, and it is its own conversation.

**A commit is split where each half stays independently verified**, which is why the third commit of
this session is ~1200 insertions across 30 files: `vault-check-selftest.sh` carries cases for the
strike, both verdicts and the sandbox repair, so any cut leaves a mechanism arriving without its
test.

## Feedback to the librarian

- miss: **the journal archived by this ingest carries the attribution split BACKWARDS in its corrected form, and the librarian caught it.** `2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md` says *25 English blocks*. Measured from `HEAD` (nothing was committed, so `HEAD` is the pre-ingest tree) with a Python reader over the codepoint range U+0400-U+04FF: **53 blocks on 44 pages, 25 WITH Cyrillic, 28 WITHOUT**. The session's FIRST reading was right and its correction made it wrong. `raw/` is immutable so the journal stands; `.claude/skills/retro/SKILL.md` and the plan file are corrected back to 28.
- miss: **the list of misattributed blocks printed in that journal is the wrong list**, generated by the same broken instrument, and is short by three: `decisions/a-value-outside-the-schemas-list-is-red.md:17`, `decisions/an-absent-render-is-red-on-a-page-that-renders.md:17`, `decisions/what-the-gate-reads-as-its-own-input-is-the-sessions-to-write.md:17`. The librarian named all three independently. The corrected list of 28 is reproducible and should be regenerated rather than copied.
- lesson: **a Cyrillic character class in this environment's grep is not an instrument.** `grep -c '[a-ya-YayoYO]'` (written with the Cyrillic letters) reports the split REVERSED on this corpus: it is byte-oriented here, the letter range does not map onto UTF-8 sequences, and it misses the two letters that sit outside the alphabetic run in Unicode order. Two readers that do work: an awk matching the UTF-8 lead-byte range, and Python matching the codepoint range. **The wrong instrument agreed with itself across two separate runs**, which is how it survived a correction and got written into three files. Any future sweep of this kind names its reader.
- miss: **the same journal states the hook registration count twice and differently, and both are wrong.** `How it is built` says *six registrations across two events, four scripts*; the `measure:` line says *five across two events, four scripts*. Read from `.claude/settings.json`: **six registrations, THREE events** - `SessionStart`, `PreToolUse`, `PostToolUse` - **and five distinct scripts**, `check-the-plan.ps1` being registered on two events. Three are on `PreToolUse`, which is the load-bearing half and is correct as written. **The table inside `scripts/hook-selftest.ps1` is correct and has all six rows**; only the prose about it was wrong, which is the argument the register was built on turned against its own description.
- process: **three counting errors in one session, all in measurements about the session's own record**, and each was caught by a different party: the attribution split (caught by the librarian at ingest), the retro's verdict count (caught by the session, from a script, after stating it in chat), and the hook registration count (caught by the librarian). None was caught by reading carefully. The session spent itself arguing that a rule which survives being written down needs something that runs, and produced three errors of exactly the kind attention cannot catch. **The one that matters for design: the corrected figure was written into three files by hand, so one wrong reading propagated in a single step and no check anywhere would have noticed.**
- miss: **the archive decision and the archive practice disagree about where a retired page goes, and nothing reports it.** [[archive-is-dated-by-session-and-holds-what-left-the-working-set]] says the dated folder holds *"the wiki pages retired that day, dated by the day they were retired"*, refined into `archive/<date>/<session>/` by [[the-archive-gains-a-folder-per-session-inside-the-date]]. **Every retired page in the tree is flat in `archive/`** - 30-odd of them, including `read-only-scouts-one-per-folder-ahead-of-the-librarian`, retired 2026-08-21, the day after the refinement. And `scripts/vault-archive.sh` accepts only `handoffs|plans|specs|notes`, so the sanctioned tool cannot express the destination its own decision names. **It surfaced at the `/pre-task` for the strike of `advisory-is-the-default-for-a-hook`**, where the plan had assumed the flat form from the practice and the corpus said otherwise. The owner ruled for the dated form this session; whether the flat ones are swept is his and is untouched.
- miss: **a page retired mid-session cannot be dated by the design that dates it.** The session folder is named from the journal's own filename ([[the-archive-gains-a-folder-per-session-inside-the-date]]), and the journal does not exist until `/handoff` runs at the end of the session - so a retirement performed at any other moment has no legal folder name to move into. Worked around here by fixing the slug at the start and binding `/handoff` to it, which is a session's promise rather than a mechanism. **It surfaced while executing the ruling above**, not while reading it: the decision is silent on when the retirement happens, and every prior retirement was flat, so nothing had ever tested the ordering.
- process: **`/ingest` files a `vault-feedback.md` line into `log.md` and does not remove it; only `/handoff` empties the file.** Five entries written between the handoff and the ingest of 2026-08-21 are in `log.md` and still stand in the file - so the next `/handoff` will drain them into a second journal and the next `/ingest` will file them a second time. The header of the file describes the two-stage transfer correctly and neither stage owns the deletion for lines written in that window. Found by reading the file at the start of the next session, which is the only place the duplication is visible.
- miss: **retiring a page now means editing `authority.md`, and nothing in the corpus says so.** Moving `advisory-is-the-default-for-a-hook` out of `wiki/` left `hook-blocking-default` as a register row no page carries, which rule 13 reddens through `vault-authority.sh --check`. **It surfaced inside the archive script's own gate run** - left alone, the move would have ended with `THE GATE IS RED AFTER THE MOVE`, so the librarian removed the slug before moving rather than after. **This is the first retirement since `authority:` became required on 2026-08-21**, so the supersession procedure in the vault's `CLAUDE.md` - write the successor, deprecate the old, move it to `archive/` - has never mentioned a fourth step it now needs. Recorded and not minted as a rule: that is the owner's.
- miss: **a fifth page takes a disposition from the struck rule and the `/pre-task` shortlist did not find it.** `wiki/decisions/the-pre-task-becomes-an-agent-and-the-ritual-is-enforced` cites `advisory-is-the-default-for-a-hook` for *"the gate that watches for it stops advising and starts refusing"* - a disposition, not context - while the plan named only four. **It surfaced in the librarian's execution, not in the check**, which is exactly the review phase 1 cannot perform on itself: the shortlist is built from `title:` and `authority:` by the party that wrote the plan, and this page's title says nothing about hooks. The phase-2 clause that asks the librarian what is MISSING from the list is what would have caught it, and this run read phase 2 by hand instead of dispatching.
- process: **the script changed before the corpus said so.** `scripts/vault-archive.sh` already carried its new `pages` kind when the librarian started, so the `decisions/` page recording the change was written after the change it records. That is the same ordering as the defect the change repairs - the archive clause said retired pages are dated while the tool could not express it, and the practice quietly outvoted the rule for six days. Worth a minute at the retro: a session may edit `scripts/` directly and only the librarian may record why, so every harness change is briefly undocumented by construction.
- miss: **the command the owner named as the seventh criterion's decider silently ran half of itself.** `scripts/vault-authority.sh` dispatched on `case "${1:---list}"`, so `bash scripts/vault-authority.sh --check --binding` ran the check, **dropped `--binding` without a word**, and exited 0 with a report that looked complete. **It surfaced within a minute of the criterion being set** - the decider was run once to confirm it works, and the `--binding` figures were simply absent from the output. The repair is a loop over the argumentless modes, with the exit code the worst of those run rather than the last, and the operand-taking modes left single-dispatch. **The class is the one this project keeps meeting**: an instrument that answers half a question in the voice of a whole one, failing towards *nothing to report*. Worth noting on the criterion's own page that it was unrunnable as written for the first minute of its life.
- miss: **`governs:` has a THIRD parser and nobody counted it.** The gate and `scripts/vault-inject.sh` were both taught the inline-list form on 2026-08-21, written from the same four rules and deliberately not shared. The sandbox builder in `scripts/vault-check-selftest.sh` reads the same field with a scalar `sed` and was not touched. **It surfaced on the first rule page in the corpus to govern two files**: the loop that materialises every governed destination was handed the literal string `[a/one.md, b/two.md]` as one destination, materialised a file under that name, copied neither real destination, and rule 12 went red in every case - `caught 112, missed 44` against three real failures. The corpus has a page arguing that two parsers written from one set of rules beat one shared copy; **the cost that argument does not name is that a third parser is invisible until a page exercises the difference**, and the count of readers lives nowhere.
- process: **the sandbox is a mirror in the places somebody remembered to mirror.** `.claude/` is copied one file deep - `templates/handoff.md` - and everything else under it is either materialised from a `governs:` sweep or faked as an empty placeholder. That worked while every rule governed `CLAUDE.md` or a file the sweep found. The suite's own comments already reject working around an unfaithful sandbox rather than making it faithful, and this is the same argument arriving at a directory rather than at a filename.
- process: **two selftest cases ran, passed, and were never counted, and only arithmetic caught it.** They were written as bare `( ... ) &` subshells calling `report` directly, so `next_rf` incremented inside the SUBSHELL, the parent case number never moved, and the collector iterated past their report files. The suite printed `caught 156, missed 0` - a clean number with two cases silently missing from it. **Nothing in the suite would ever have said so**: a dropped case looks exactly like a case that was never written. What found it was adding up what had been added - eight - against what was reported - six. Repaired by giving them a runner that allocates in the parent, as every other runner here already does. The general shape is the one this repository keeps meeting from a new angle: a green number is evidence about the cases that ran, and says nothing about the ones that did not.

- process: **the immutability warning cannot tell a template being filled in from testimony being rewritten.** The `Write` guard fired while `/handoff` filled the copy it had just made from `.claude/templates/handoff.md` - correct in general and wrong here, because the file had existed for one minute and had no sidecar. **The test that separates the two already exists and is used by three other readers**: `<name>.coverage.tsv` beside it is what *compiled* means, and `/ingest`, the `SessionStart` hook and rule 8 all answer with it. A journal with no sidecar is being written; one with a sidecar is testimony. Found while writing this journal.

## Anything else worth keeping

**The session slug was chosen by the session and `/handoff` was bound to it by a promise.** The
archive folder is named `2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict` and this journal
matches it. `Q12` ruled the mechanism that replaces the promise; the mechanism is not built.

**Two literal quotations exist from this session and both are in the header**, which is the whole
argument for the shape ruled into existence at its retro.

**The retro ran as `grill-me`, the agent asking, three rounds plus one the owner opened himself** —
nineteen questions put to him, three more closed by reading the repository rather than spending his
attention. **22 lines: 18 answered, 4 deferred, 0 could-not-close.**

## Harness

- harness: **`/retro` gains a third attribution shape and ratifies decisions rather than utterances.** Decided 2026-08-22, on the owner's question - the two literal quotations this session produced were *«что сегодня делаем?»* and *«согласен с рекомендациями»*, and neither settles anything, while all eight real rulings arrived as selections from options the session authored. **`owner selected:`** records the option label verbatim, plus what it was chosen against where that changes the meaning. The ground is a property rather than a courtesy: the defect that produced the struck rule was never that the words were English or session-written, it was that **nothing ever showed him the wording** - and an option label was on his screen when he chose it, so there is no interpretation step and nothing that can drift. Its own defect is different and is written beside it: **the alternatives were the session's**, and on the very day the shape was ratified he selected three options at once because the set did not contain what he meant. Step 5 also stops ratifying remarks that settle nothing; the session brought him a session-opening question for signature beside seven real rulings, and a list padded with nothing is read less carefully. Both changes are in `.claude/skills/retro/SKILL.md`.
- harness: **`/pre-task` always dispatches phase 2**, owner's ruling 2026-08-22 - the standing instruction against spawning agents unasked does not reach the ritual. Phase 2 failed to run on both days the corpus records for it, and the clause it exists for, *say what is MISSING from this list*, was therefore put to nobody. Measured cost this session: the shortlist named four pages taking a disposition from the struck rule and there were five; the fifth was found by the librarian while executing, not by the check. The list is built from `title:` and `authority:` by the party that wrote the plan, so asking oneself to find its holes is not a review.
- harness: **who filed a feedback line empties it.** `/ingest` files each line into `log.md` and removes nothing today; only `/handoff` empties the file, so lines written between the two are filed and survive to be filed again. Owner's ruling 2026-08-22: the drain belongs to whichever ritual performed it. Rejected: `/ingest` not reading the file at all, which loses the lines written during the ingest itself - four of them today, three found by the librarian.
- harness: **a fourth step joins the supersession procedure**: retiring a page now means removing its slug from `authority.md`, because `authority:` became required on 2026-08-21 and a moved page leaves a register row no page carries. The vault's `CLAUDE.md` is the session's to edit and the owner reads the diff. Rejected: teaching the archive script to edit the register itself, which would make it a second writer of a file that has exactly one.
- harness: **the count of readers of `governs:` becomes a selftest case**, not a sentence on a page - the shape the owner ratified for the hook register on 2026-08-21, which paid for itself the same week. A list that is also a test cannot drift from what it describes, and the proposal arguing that two parsers written from one set of rules beat one shared copy is unauditable while nothing says how many there are. Three exist and the third was found by a red tree.
- harness: **the session slug is written to a file by whoever first needs it, and `/handoff` reads it** rather than inventing one. Owner's ruling 2026-08-22, closing the ordering hole the dated archive opened: a session folder is named from the journal's filename and the journal does not exist until `/handoff` runs, so a page retired mid-session has no legal folder name. Worked around today by a promise the session had to remember. Rejected: performing every retirement after `/handoff`, which splits the strike in two and leaves a `deprecated` page sitting in `wiki/` for half a session.
