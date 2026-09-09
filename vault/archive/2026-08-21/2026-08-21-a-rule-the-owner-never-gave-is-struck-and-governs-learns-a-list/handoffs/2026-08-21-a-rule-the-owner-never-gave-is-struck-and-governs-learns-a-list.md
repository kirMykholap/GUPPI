---
session: 2026-08-21
sprint: S2
commits: none
---

# Handoff — A rule the owner never gave is struck, and `governs:` learns a list

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

**Read this first, because it changes how the rest of this journal should be read.** This session
found that `wiki/decisions/advisory-is-the-default-for-a-hook.md` carries a quote block attributed
to the owner, stamped `basis: human`, stating a rule **he says he never gave**. The words are a
previous session's English paraphrase, written into a journal under `**owner:**`, compiled by the
librarian into a quote, and reasoned from as his word for three days.

**So the `**owner:**` convention this template opens with is the mechanism that produced the
defect.** Every `**owner:**` line below is his words, in Russian, copied from the conversation.
Where this session understood something rather than heard it, it is written in the session's own
voice and is not signed. That distinction is new and it is the point of the session.

## State

**The session ran from 23:00 on 2026-08-21 into 2026-08-22**, and is dated by its start.

**Nothing was committed.** HEAD is `340ccb0`, unchanged from session start, and six files stand
modified in the working tree: `scripts/vault-inject.sh`, `scripts/vault-check.sh`,
`scripts/vault-check-selftest.sh`, `scripts/hook-selftest.ps1`, `.claude/skills/retro/SKILL.md`,
`job_hunt_ai_vault/wiki/rules/_schema.yaml`.

**Done:** `governs:` takes a list, in both readers and in the schema. `/retro` gained a
ratification step. The hook set became a test rather than a sentence.

**Not done, and named in the approved plan rather than lost:** striking the false rule, the
quote-is-Cyrillic rule, the shared reading-discipline rule page, the `/pre-task` agent, the
`PostToolUse` hook on `Agent`, and the blocking write gate. The plan is
`C:\Users\kir\.claude\plans\toasty-munching-otter.md` and states on its face that it is two to
three sessions rather than one.

**Checks.** `bash scripts/vault-check-selftest.sh` — **caught 147, missed 0**, from 144; the count
moved by exactly the three cases added. `scripts/hook-selftest.ps1` — **caught 114, missed 0**,
from 110; moved by exactly the four cases added. `bash scripts/vault-check.sh` exits 0 with the one
standing advisory, `a region or whole generation covers 4 of 15`. `bash scripts/vault-inject.sh`
reports 0 rewritten, 0 generated, 0 removed, 0 problems. Each exit code read from its own
invocation.

**Not run, and said so:** `uv run pytest` and `ruff` — **no Python changed**, and the plan says to
state that rather than claim a green suite. No browser walk. `vault-check-selftest.sh` was run
twice; the first run is the one that found the real defect.

**Next step:** the quote-is-Cyrillic rule, first, ahead of the pre-task chain — the owner's
ordering.

## Entities

**Changed: `scripts/vault-inject.sh`.** It gained `governs_targets()`, a parser accepting a bare
path and an inline list and refusing anything else, and its walk now feeds the main loop one
`page<TAB>destination` pair per line instead of one page. The two-hundred-line loop body is
untouched: every `continue` in it already meant *abandon this destination and take the next*, which
is exactly what it has to mean now.

**Changed: `scripts/vault-check.sh`.** The frontmatter pass gained `govsplit()`, written from the
same four rules as the injector's parser so the two readers cannot disagree about spelling. The
`governs|` fact is now emitted once per destination, and rule 11's address comparison asks
**membership** rather than equality.

**Changed: `scripts/hook-selftest.ps1`.** It carries the register of which hook refuses and which
speaks, as four cases rather than prose.

**Changed: `.claude/skills/retro/SKILL.md`.** A ratification step between the gate and the writing
of the retro file.

**Changed: `job_hunt_ai_vault/wiki/rules/_schema.yaml`.** The `governs:` entry documents the list
form and why the block form is refused.

**Unchanged and worth naming because a reader will look for them:** there is no `pre-task` agent —
`.claude/agents/` holds `vault-librarian.md` alone — and no `PostToolUse` registration on `Agent`.
Both are in the plan and neither is built.

## Decisions

**owner: не было такого правила. Это правило неправильное.**

Said of `advisory-is-the-default-for-a-hook`, whose quote block reads *"advisory is the default for
a hook. A hook may refuse an operation only where the action is irreversible and the refusal cannot
be wrong — both conditions at once."* **The page is struck**, and it is not yet struck in the tree:
the strike is step `A1` of the plan and needs the librarian, `wiki/` having one writer. Eleven
mentions across nine files, four of them load-bearing — `entities/the-plan-check-hook`,
`entities/the-librarian-lock-hook`, `entities/session-hooks` and
`concepts/the-guard-branch-lives-inside-a-hook-that-already-runs` all take their advisory status
from it, and the lock takes its licence to refuse from it.

**owner: "ни один hook в репозитории не запрещает" - ложное утверждение.**

It is, and the same page asserts both halves: at line 61 that `lock-the-librarian.ps1` is built and
refuses, at line 96 that no hook in this repository blocks. `entities/session-hooks.md` carries the
dead sentence too.

**The three-condition test replaces it**, ratified by the owner from options this session authored,
so the wording below is the session's and the ruling is his. A hook may refuse when **the condition
is measured rather than judged**, when **that measurement is reliable at the point the hook
stands**, and when **the refusal says how to clear it**; where it cannot measure, it allows and
says so aloud. Rejected: the struck page's *irreversible and cannot-be-wrong*, on the ground that
the owner never set it. Applied, it gives the same answers the tree already holds — the lock
refuses, `check-the-plan.ps1` and the write net speak — for reasons that can be checked.

**owner: окей, но не применимо например для случая когда цитата будет на английском. То есть правило не универсальное. Я бы оставил, но это точно не может быть CORE, так как слишком специфично**

Said of the quote-is-Cyrillic rule. **It stands, its verdict is an advisory rather than red, and it
does not enter `CLAUDE.md`'s core.** The precedent named at the time: the filename verdict is an
advisory while the title verdict is red, so the shape already exists here. Rejected: a red verdict,
because a genuine English quote from the owner would trip it falsely.

**owner: ратификация принимается. Хороший механизм. Тоже вводим.**

Built this session as step 5 of `/retro`. Rejected: relying on the language test alone — a check
separates a quote from a paraphrase by its alphabet, and only the owner separates a *faithful*
paraphrase from a wrong one.

**owner: да, разрешаю**

A standing permission to dispatch agents inside the vault's rituals — `/pre-task` phase 2,
`/vault-ask`, `/ingest`. Given at the retro, after the session reported that a session-level
instruction forbidding unrequested dispatch had cut phase 2 out of this session's own ritual and
was about to stop `/ingest`.

**The block-list form of `governs:` becomes a red verdict rather than silence.** The session
proposed silent refusal and argued for it; the owner took the stronger form. The reason is that a
YAML editor, or the PyYAML parser already on the sprint list, reads the block form as perfectly
legal — so a silent refusal stops being a guard and becomes a trap. **Not built.**

**DIVERGENCE: `/pre-task` ran at half strength and the plan was approved on it.** The rule places
the ritual between the plan and its approval. Phase 1 ran — `vault-catalogue.sh`, 576 rows, 17
constraining pages selected, about 12 opened in full, and the plan's `Constraints` section is its
output. **Phase 2 did not.** What was lost is specific: phase 2 carries the clause *say what is
missing from this shortlist*, and that clause is the only thing in the design that reviews phase 1,
so the plan was checked against pages its own author chose. The cause was the session-level
instruction above, not a rule of this repository, and it was reported rather than worked around.

**DIVERGENCE: four misses were carried rather than written when they surfaced.** The rule is to
write a miss into `.superpowers/sdd/vault-feedback.md` in the same turn and never carry it; plan
mode forbids writes and forbade it four times running. All lines were drained the moment plan mode
ended. Recorded as **one defect in where the obligation sits** rather than four lapses: the
obligation is on the session, and the session is the party plan mode disarms.

## How it is built

**`governs:` takes a bare path or an inline list, and nothing else.** `governs: CLAUDE.md` and
`governs: [CLAUDE.md]` mean the same thing; the inline form is the spelling this corpus already
writes `tags:` and `sources:` in. Thirteen pages carried the bare form and none was touched.

**The block form is refused because the injector writes what it parses.** A spelling that is
half-parsed renders a rule into a subset of its destinations and leaves the gate reading the
remainder as drift. One spelling for the list, checked, beats two where one is guessed at.

**The expansion happens at the walk, not in the loop.** Each page carrying `governs:` is expanded
into one `page<TAB>destination` line before the loop reads it, so the loop body never learns the
field has a syntax. The `grep -l` pre-filter that the wall-clock comment defends is untouched, and
a page naming one destination still costs exactly one iteration.

**Rule 11 asks membership.** Reading the first destination was correct while a page could name one
file and **silently wrong the moment it could name two** — it accused the region sitting in the
*other* governed file, which is the one place the verdict must stay quiet.

**The two parsers are written from the same four rules and are deliberately not shared:** trim,
strip one layer of quotes, split an inline list on commas, and a bare value is a list of one. This
vault already derives its category words identically in two places for the same reason.

**The hook register is a test.** Six registrations across two events, four scripts; the disposition
of each is read off the script by matching `permissionDecision = 'deny'`. Four cases: the
registered set matches the list in both directions, each hook refuses or speaks as listed, exactly
one refuses and it is named, and no refusal is listed on an event that cannot deny.

**The event bounds the question, and that is the finding.** `PostToolUse` fires after the act and
`SessionStart` injects context; neither has a way to deny. **A refusal is possible on `PreToolUse`
alone** — three registrations, not six — so the conversation the owner scheduled twice is a
decision about three things rather than a register of seven.

## Lessons

**A cost figure was quoted for the wrong class a third time, and the store has a page for it.**
`wiki/concepts/the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch.md:41` and
`.claude/skills/pre-task/SKILL.md:59` both quote **`1m24s` and `21.6k tokens`** as the price of
phase 2's read. In `wiki/lessons/agent-round-trip-cost.md` that row is labelled **`a narrow write`
— two frontmatter lines on two named pages**. The figure is in the file a reader opens while
deciding whether to pay. **Phase 2 has never been run**, so its price is unmeasured rather than
merely mis-stated.

**A green gate can be no evidence at all about the branch you just changed.** Measured: making
`govsplit` return nothing left `bash scripts/vault-check.sh` byte-identical and still exit 0.
Every rule page in the corpus governs the file its region already sits in, so rule 11's address
comparison is **unreached by the whole corpus**. Three selftest cases now reach it. The general
form is the lesson and it is unaddressed: nothing enumerates which other verdicts the tree fails to
exercise, and this one was found by accident.

**A measurement about attribution was reported with its two figures swapped, by the session
diagnosing exactly that failure.** *28 English blocks* was said and written where 28 is the Russian
count and **25** is the English one; it reached chat, `vault-feedback.md`, `.claude/skills/retro/SKILL.md`
and the plan before being caught, and all four are corrected. **The count of the retro's own
verdicts was then also miscounted** — twenty-two said in chat against twenty-one in the file, and
the file was corrected from a script rather than from the conversation. Two miscounts in one
session, both in measurements about the session's own record. **This is the argument that the
remedy has to be mechanical rather than attentive**, made against the party that had spent the
session making it.

**Every multi-line edit in this session went through a channel that halves one level of backslash
escaping.** `\t`, `\n` and `\\` reached files as literal or as already-interpreted characters. It
produced: a broken line continuation that made `sort` read a file named `n`; a `printf` carrying a
real tab and a real newline instead of its escapes; `IFS=$'<TAB>'` where `IFS=$'\t'` was meant; a
PowerShell character class `[/\]` that is not a valid regex; and one awk program left calling a
function that had never been inserted — **which the gate then ran, and exited 0**. The remedy that
worked: build every literal from `chr()` and assert the match count before writing. The hazard bit
once more at the end of the session, on the heredoc writing the retro file.

**A test that catches its own author is better evidence than a planted offender.** The hook
register's first run printed `MISSED` on two of its four cases, both for real defects in the case
code — an invalid regex, and a scalar indexed as an array while printing the right answer beside
itself. Both directions were therefore observed on the real tree, which is why the four are trusted
without a further proof run.

## Deferred

**The four unbuilt steps of the pre-task chain, in the ratified order.** The reading discipline
into a `wiki/rules/` page; `governs:` taking a list — **done this session**; `/pre-task` becoming an
agent that performs both phases inside one dispatch; a `PostToolUse` hook on `Agent` writing the
ledger row from `subagent_type`; and only then the blocking write gate.

**Phase 1 moves inside the agent**, which reverses the owner's own lifting of the main-context
clause on 2026-08-21. That clause was lifted for the **skill** shape and does not survive the
**agent** shape: if phase 1 stays outside, the empty case leaves no dispatch, so the hook writes no
row and the gate cannot tell *checked and found nothing* from *did not check* — and the empty case
is exactly what a skipper would claim. Recorded as a reversal under a new ground rather than an
oversight.

**Step 3 is the condition of step 4's legality, not a convenience before it.** Under the ratified
test a blocking gate fails condition 2 today: the ledger row cannot be written in plan mode, which
is the exact moment the rule places the ritual, so the gate would refuse sessions that performed
the ritual. Once a hook writes the row, the measurement becomes reliable where the hook stands. The
proposal states the same order for a weaker reason — deadlock risk — which is real and additional.

**The block-list verdict for `governs:`**, ruled red and not built.

**A third row for the ratification table**, put to the owner and not answered — see below.

**Whether a paraphrase is demoted to `basis: inference`**, offered and neither taken nor refused.

**What else in the gate is not exercised by the corpus** — a new line with no home before this one.

**Carried unchanged:** the tag verdict at 126 of 198; the seventh S2 criterion; a machine-readable
format for the registers; the 14 migration tests against Docker; the four owed readings, sixth
session; `authority.md` families over the ceiling; and whether this work earns S2 a seventh
criterion.

**The list of misattributed blocks was printed this session and is below**, to be read next
session. Act only on what the owner disowns.

## Feedback to the librarian

- lint: `wiki/entities/vault-archive-sh.md` records two defects as standing and unrepaired, and both were repaired in `340ccb0` after the ingest that wrote them. The path-form defect (the argument and the citation are two different forms of the same path) and the orphaned sidecar are both fixed, both have selftest cases, and both cases were proved to bite — breaking the path-form line takes the suite from `caught 144, missed 0` to `caught 142, missed 2`. The page needs a dated append, not an edit. **This is the shape to watch: a repair made after `/ingest` has no journal to travel in, because `raw/` is immutable and the sidecar already exists. This file is the only channel that survives it.**
- lint: 66 stale slugs were swept out of twelve `.coverage.tsv` files in `340ccb0` — page names renamed on 2026-08-18 and 19. A sidecar is outside the rename sweep exactly as `log.md` is, and `log-md-is-outside-the-link-set-the-check-reads` should say so about sidecars too. The coverage loop the ingest now runs went from twelve noisy sources to none.
- miss: `wiki/decisions/advisory-is-the-default-for-a-hook.md` renders as a quote block, attributed to the owner and stamped `basis: human`, a ruling **he says he never gave** — «не было такого правила. Это правило неправильное», 2026-08-21. The words are the English paraphrase a session wrote into `raw/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md:77` under `**owner:**`. **It surfaced while a plan was being checked against it**: the two-condition test was about to block step 4 of [[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]], and the obstacle was fabricated. It had already decided three things — the guard's advisory choice, `check-the-plan.ps1`, and the write net. **The owner's ruling: struck.** The chain that produced it runs every session: he speaks Russian, a session paraphrases into English under `owner:`, the librarian renders the paraphrase as a quote, later sessions reason from it as his word — and nothing ever shows him the paraphrase.
- miss: the same page says **"No hook in this repository blocks"** at its foot while its own preceding section names `.claude/hooks/lock-the-librarian.ps1` as built, refusing, and meeting both conditions. `wiki/entities/session-hooks.md` carries the same dead sentence. The false half went false the day the lock landed and stood for a day, and it is unfalsifiable by construction: **nothing enumerates the hook set**, so the claim cannot be checked without reading all seven scripts by hand. This is exactly what `the-system-naming-which-hooks-block` predicted in the sentence *"a statement nobody can check without reading every script"*.
- miss: `wiki/concepts/the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch.md:41` and `.claude/skills/pre-task/SKILL.md:59` both quote **`1m24s` and `21.6k tokens` as the price of phase 2's read**. In `wiki/lessons/agent-round-trip-cost.md` that same row is labelled **`a narrow write` — two frontmatter lines on two named pages**. A write figure is being quoted as a read price, in the file a reader opens while deciding whether to pay. **Third occurrence of the defect `a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices` is about**, and its own closing section — *"having read this page did not prevent it"* — now has a third instance. **Phase 2 has never been run**, so its price is unmeasured rather than mis-stated.
- process: **four times in one session a rule required a write in a turn where writing was forbidden.** The rule *"write the miss into `vault-feedback.md` in that same turn — never carry it in your head"* met plan mode four times on 2026-08-21 and lost four times; `/pre-task`'s own `record-pre-task.ps1` has the identical shape and the identical hole, which `.claude/skills/pre-task/SKILL.md:101` already records as a known gap. This is one defect in **where the recording obligation is placed**, not four instances of bad luck: the obligation sits on the session, and the session is the party plan mode disarms. The same observation is the ground for step 3 of the pre-task chain — a hook can write during planning and a session cannot.
- measure: **53 owner-attributed quote blocks across 44 `wiki/` pages; 25 of them contain no Cyrillic** (the other 28 do), from `grep -rhE '^> \*\*owner' wiki --include=*.md` classified by codepage range, 2026-08-21 - and the first reading of this measurement, given in chat and written here, had the two figures the wrong way round. English does not prove the owner did not say it, and none of the 25 is in his words. A second page sampled at random, `wiki/decisions/a-refusal-is-conditional-or-absolute-and-nothing-else.md`, is `basis: human` and `binding: prohibition` with the ruling **absent from the source it cites** on two search patterns — flagged, not struck; striking a second prohibition on one session's reading is the owner's call.
- measure: **five hook registrations across two events, four scripts.** Three are on `PreToolUse`, the only event where refusal is possible at all; `PostToolUse` fires after the act and `SessionStart` injects context. **Exactly one refuses**: `lock-the-librarian.ps1`, via `permissionDecision = 'deny'`, allowing and saying so when the measurement cannot run. Read from `.claude/settings.json` and the scripts, 2026-08-21.
- process: **step 3 of the pre-task chain is the condition of step 4's legality, not a convenience before it.** Under the ratified test a blocking write gate fails condition 2 today — the ledger row cannot be written in plan mode, which is the exact moment the rule places the ritual — so the gate would refuse sessions that performed it. Once the row is written by a `PostToolUse` hook the measurement becomes reliable where the hook stands and the gate becomes legal. The proposal states the same order for a weaker reason (deadlock risk), and the deadlock risk is real and additional.

## Anything else worth keeping

**The ratification step found a hole in itself on its first run, and it is left as a hole.** The
step admits two shapes — *he said it* and *you understood it*. Its first run found a third: **nine
of this session's rulings were made by the owner choosing among options the session had authored.**
The decision is unambiguously his and the wording is unambiguously the session's. It is more
dangerous than either shape in the table, because an explicit yes makes it read as stronger than a
quote while every word in it was written by the party that wanted the answer. Put to the owner at
the retro and **not answered**, so the table stands at two rows.

**The pre-task ledger recorded the day's whole design argument without being asked to.** Read as
the session left it:

```
23:00:16  session-start:startup  unknown      -
23:52:14  first-write            plan         no
23:52:14  advised-write          plan         no
23:52:29  advised-plan           plan         no
23:57:02  scope-approved         acceptEdits  no
23:58:03  pre-task               unknown      yes
```

Two advisories fired, both correctly by their own data, and **both were wrong**: phase 1 had run.
They could not know, because recording is a write and plan mode forbids writes. The row landed six
minutes later. An advisory that cannot stop anything, and a measurement blind precisely where the
rule places the ritual — the case for building step 3 before step 4, produced by the session making
it.

**The list of owner-attributed quote blocks carrying no Cyrillic, printed 2026-08-21.** Twenty-five
of fifty-three, across forty-four pages. To be read by the owner; nothing here is a verdict.

```
decisions/a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker.md:31
decisions/a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker.md:42
decisions/a-hand-edit-to-a-generated-rules-file-is-red.md:17
decisions/advisory-is-the-default-for-a-hook.md:17
decisions/authority-beside-governs-is-forbidden-on-any-page.md:18
decisions/core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed.md:17
decisions/render-is-reinstated-and-required-now-that-another-mode-has-a-writer.md:18
decisions/the-ast-rule-moves-to-prove-the-mechanism.md:17
decisions/the-date-of-a-correction-note-is-the-date-the-text-became-false.md:17
decisions/the-frontmatter-core-is-fixed-and-updated-joins-it.md:79
decisions/the-gate-learns-the-legal-key-set-from-a-yaml-per-folder.md:17
decisions/the-gate-learns-the-legal-key-set-from-a-yaml-per-folder.md:43
decisions/the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count.md:42
decisions/the-legal-value-list-lives-in-each-folders-schema.md:17
decisions/the-maps-region-replaces-the-prose-it-duplicated.md:35
decisions/the-quantity-field-is-rejected-and-the-rule-stays-unconditional.md:17
decisions/the-renamed-vault-case-is-graded-on-the-question-it-asks.md:17
decisions/the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs.md:18
decisions/the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed.md:31
decisions/the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed.md:74
decisions/the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed.md:94
decisions/the-wide-half-of-the-per-type-schema-is-a-conversation-not-a-task.md:17
decisions/what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live.md:18
lessons/a-question-asked-is-not-a-question-answered.md:22
rules/english-in-the-repository-russian-with-the-owner.md:147
```

**`wiki/decisions/a-refusal-is-conditional-or-absolute-and-nothing-else.md` heads that list.** It
is `basis: human`, `binding: prohibition`, and the ruling it states is **absent from the source it
cites** on two search patterns. Flagged and deliberately not struck: striking a second prohibition
on one session's reading is the owner's call.

## Harness

- harness: `scripts/vault-archive.sh` joined the copy list in `scripts/vault-check-selftest.sh` and has three cases of its own. It had none before, which is why the defect above shipped.
- harness: the owner ratified nine things on 2026-08-21 and they are the approved plan `toasty-munching-otter`: strike `advisory-is-the-default-for-a-hook` and replace it with a **three-condition test** — the condition is measured not judged, the measurement is reliable at the point the hook stands, the refusal says how to clear it, plus allow-and-say-so on a failed measurement; a `wiki/rules/` page making **a quote Cyrillic** with an **advisory** verdict in `vault-check.sh` (not red, and not in `CLAUDE.md`'s core, both his rulings); a **ratification step in `/retro`** over every `owner:` line before `/handoff` routes it; **`governs:` takes a list**, scheduled between steps 1 and 2 rather than left conditional; **phase 1 moves inside the pre-task agent**, reversing his own lifting of the main-context clause, which was lifted for the skill shape and does not survive the agent shape; and the hook list lives in **`scripts/hook-selftest.ps1`**, a case per registration, never in prose alone.

**Build the quote-is-Cyrillic rule first next session**, ahead of the pre-task chain — the owner's
ordering. A `wiki/rules/` page governing both `.claude/skills/handoff/SKILL.md` and
`.claude/skills/ingest/SKILL.md`, which is the second customer for the `governs:` list landed this
session, plus one new numbered **advisory** verdict in `scripts/vault-check.sh` and cases in both
directions.

**`scripts/vault-check.sh` owes a red verdict for the block-list form of `governs:`**, on the
owner's ruling.

**`.claude/skills/retro/SKILL.md` owes a third row in its ratification table**, if the owner takes
it: *the decision is his, the wording is the session's* — written as "the owner chose X from the
options put to him", never in quotation marks.

**`scripts/hook-selftest.ps1` will need a case for the `PostToolUse` hook on `Agent`** when that
hook is built, alongside the register added this session.
