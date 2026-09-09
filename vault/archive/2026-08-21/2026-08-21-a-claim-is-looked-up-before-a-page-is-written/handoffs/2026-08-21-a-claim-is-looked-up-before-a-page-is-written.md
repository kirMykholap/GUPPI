---
session: 2026-08-21
sprint: S2
commits: 70f2d6c..0577fd1
---

# Handoff — 2026-08-21

## State

**Done.** Occam's razor is the vault's ground rule and it is executable rather than an exhortation.
`scripts/vault-authority.sh` is the lookup it is decided by — `--near`, `--group`, `--list`,
`--check`, `--orphans`, `--binding`, `--trace`. `scripts/vault-catalogue.sh` gained an `authority`
column. Rule 13 of the gate asks its question by running that tool. `job_hunt_ai_vault/authority.md`
holds **51 families over 470 slugs**, none left over and none in two families. `authority:` is
required in every folder but `wiki/rules/`; `wiki/decisions/` carries a required `binding:`.
`governs:` is confined to `wiki/rules/`. Five pages written, 220 back-filled, one decision retired.

**Not done, and named rather than dropped.** `/pre-task` still enumerates `decisions/` alone — the
owner said in as many words that this is wrong. The reading funnel is built at stages 1–2 and no
ritual names it. `lessons/` → `proposals/` is designed and unbuilt. All three are on the Deferred
list below.

**In flight: nothing.** Working tree clean after `0577fd1`, but for this journal.

**Checks, each exit code read from its own invocation.**
`bash scripts/vault-check-selftest.sh` — **caught 141, missed 0**, exit 0, from 136.
`powershell scripts/hook-selftest.ps1` — **caught 108, missed 0**, exit 0, from 107.
`bash scripts/vault-check.sh` — exit 0, one standing advisory (`a region or whole generation covers
5 of 15 harness markdown files`; the unmarked files are unchanged).
`bash scripts/vault-inject.sh` — exit 0, 0 problems.
`bash scripts/vault-authority.sh --check` — `470 slugs grouped`, exit 0. `--orphans` — `every page
outside wiki/rules/ carries an authority`, exit 0. `--binding` — exit 0.
`uv run ruff check src tests` and `ruff format --check` — exit 0.

**`uv run pytest -q` was NOT run, and no browser walk.** No Python changed; `src/` was not touched.
Saying so rather than omitting it.

**Next step:** the Deferred list, headed by `/pre-task`'s coverage.

## Entities

**Appeared.** `job_hunt_ai_vault/authority.md` — the fifth register, the dictionary of `authority`
families. 51 groups, 470 slugs, 543 lines. Hand-written by the librarian, audited against the tree
by `--check` in both directions. Slugs are plain text and **never `[[wikilinks]]`**: a register that
linked every page would join rule 5's link sweep and no page in this vault could be an orphan again.

**Appeared.** `scripts/vault-authority.sh` — seven subcommands. `--trace` is the reverse of the
coverage sidecar, which already recorded source-line → page and had no way back; it is nearly free
because the trail already existed.

**Changed.** `scripts/vault-catalogue.sh` prints `authority` per row — 558 lines, 109,053 bytes, one
command over the whole corpus. It is the wide half of the reading rule, which nobody could pay
before because the wide half was a grep over 479 files.

**Changed.** `.claude/agents/vault-librarian.md` is now a governed file carrying a region: the
admission rule renders into it, so it reaches the librarian in every dispatch rather than being
somewhere it must remember to look. Region coverage moved to 5 of 15 and **the unmarked files are
unchanged.**

**Changed.** `wiki/concepts/` lost `governs:` and `render:` from its schema; two of its pages moved
into `wiki/rules/`. `rg -l '^governs:' wiki/` now returns 13 files, all in one folder.

## Decisions

**Occam's razor is the ground rule of this store.** owner: «Бритва Оккама. Не плодим сущности…
Иначе наша сессия превращается в бесконечную гонку с собой, правки и правки правок, потому что
появилась новая правка. Это должно стать основой всего. Наша задача строить, а не «прикручивать».»
Rejected: leave the intake open and clean up periodically — a periodic clean-up is a one-off against
a standing cause, and nothing here may be deleted, so it shrinks only what is read.

**The danger is recorded rather than hidden, and the owner accepted it.** The rule converts a
**visible** failure into an **invisible** one: two `current` pages sharing an `authority` are a
contradiction the gate finds, while a wrong merge looks like a healthy page. What compensates is the
obligatory trail — every merge says in `log.md` what the lookup returned and why a new page was
still right — and dated breadcrumbs in the page naming the journal an addition came from.

**The editing boundary, so the rule does not undermine fidelity.** Appending, reordering and marking
a sentence false are allowed. **A sentence a source asserted is never rewritten**: `raw/` is
immutable and the coverage sidecar is keyed by source line, so a rewrite leaves a verdict pointing
at text that is gone.

**`authority:` is required outside `wiki/rules/`.** owner, at the retro. An index a page may omit is
an index with holes, and the holes are invisible — a lookup returning nothing reads exactly like a
question nobody has answered.

**`decisions/` declares what it does to a reader.** `binding: prohibition | deferral | divergence`,
required. The folder held three different things and answered as one: a plan checked against it got
a list of *relevant* pages where it needed a list of what *stops* it. An absent value reads as
`prohibition` — the safe direction. Rejected: split the folder, which is cleaner because a folder
cannot lie, but the folder set is closed and a move rewrites an address. A field is reversible; a
rename is not. **The risk is named rather than hidden:** it is a self-declaration, and this store
withdrew `quantity:` for exactly that.

**`governs:` is a property of `wiki/rules/` alone**, overturning the owner's own decision of
2026-08-17. owner: «Если у концепта появляется governs - Он становится правилом. Поэтому authority =
required в concepts. А governs из concepts уходит.» A page that renders its text into another file
IS a rule by the folder set's own definition, so the two `concepts/` pages moved rather than being
exempted. What the overturned decision was right about is recorded with it.

**The pre-task ledger is drained by nothing, and that is the ruling.** owner: «Слив ledger не
строим.» Two `current` pages assert the opposite in the same words —
[[the-pre-task-ledger]] and [[the-retro-writes-its-own-transit-file]] — and need a dated correction
rather than retirement: the reasoning that put the drain on `/handoff` rather than `/retro` is still
sound, what changed is that there is no drain to assign. The rows are not lost; rotation files each
session away, and the owner ruled the same day that the archive is not pruned.

**`.superpowers/sdd/ledger/` is not pruned.** owner, early in the session, and **recorded nowhere
until now** — the verdict existed only in chat for eight hours.

**CORE is the owner's alone to define**, and the list emerges during development. owner: «CORE
определяется только мной. В процессе разработки мы придем к конкретному списку.» The session
proposed an admission test for it and it was not adopted.

**S2 stays open.** owner: «мы не закрываем S2. Еще есть много вопросов.» Whether this work becomes
its seventh criterion is deferred to the next session.

**No divergence is recorded, and one candidate was examined and ruled not to be one.** `authority`
was left `optional` in `concepts/` where the approved plan said `required` — a narrowing, which
notifies rather than asks, and forced: the plan as approved was unexecutable for the two pages
carrying `governs:`. **The plan was approved in an unexecutable form**, which is a fact about the
session's pre-task rather than its execution.

## How it is built

**Rule 13 asks by running the tool, never by re-deriving it** — rule 12's shape, for its reason: a
check that re-derives what a tool derives is two answers waiting to differ. What counts as a page
nothing can look up is defined once, in `vault-authority.sh`.

**Severity was staged, and the staging is the design.** Rule 13 printed advisories while 470 slugs
were minted and grouped, then flipped to `note` in the same session — **and that flip is the
acceptance test for the marking**. Red before the corpus carried the field is read by
`lock-the-librarian.ps1` as a refusal to dispatch the only writer permitted to clear it. Applied the
other way first, measured at **233 verdicts**, reverted, reordered.

**A folder move is not a rename here.** The link check resolves a `[[wikilink]]` by **filename**
anywhere under `wiki/` or `archive/`, so moving a page between folders strands nothing and does not
need the rewriter-and-detector pair. Measured by reading the resolver, before agreeing to the move.

**The injector derives a marker's type word from the folder, not from the page.** So moving a rule
page between folders changes what its marker must say — four markers in `CLAUDE.md` were retyped.

**The register has a checked half and an unchecked half.** `--check` parses `slugs:` and compares
both directions against the tree; `definition:` and `aliases:` are read by no instrument at all.
Same standing `tags.md` has.

**The funnel, as designed in conversation:** the question's words → aliases → a family → `title` and
`authority` across the corpus in one command → open at most ten → one hop along wikilinks, titles
only. **The ten-page ceiling is about opening a page, never about searching for one** — that
distinction was already written in the librarian's agent file and nothing was delivering the wide
half.

## Lessons

**A rule that delegates by running a script can be silenced by a zero-byte stub.** Measured: with an
empty `scripts/vault-authority.sh`, rule 13 printed **not one line** — it ran, produced nothing, and
reported nothing, so every case written for it would have passed having tested nothing. The
selftest's own sandbox manufactures such stubs: its placeholder loop materialises every path a page
cites in `sources:` as an empty file. What protected the two delegating tools was only that the
explicit `cp` runs before that loop and the loop leaves a real file alone — an ordering nobody had
stated. A guard now refuses to run the suite at all if either tool is empty.

**Making a field required couples every fixture that plants a page, and the coupling arrives in two
waves.** Wave one is the schema: nine cases planted pages without `authority:`. Wave two is the
admission rule itself: once those pages carried a slug, rule 13 reddened them again because the slug
sat in no family. The second wave is the interesting one — **a fixture that plants a page and not
its register entry is testing a corpus this project would refuse.**

**A ruling can abolish a case's subject, and the repair is conversion rather than deletion.**
Confining `governs:` left `a concept page that renders` testing a page that cannot exist. Converted:
same subject, reversed verdict, now asserting the schema refuses it. Deleting it would have left
nothing asserting that what used to be legal no longer is. **Five runs, and the check was never
wrong**: 136 → 132/9 → 133/8 → 141/0 → 140/1 → 141/0.

**A list this file had already drifted twice on drifted a third time.** `empty_vault` in the
selftest kept its register list by hand; its own comments record the first two drifts and both times
state the repair — derive the set, never list it — and both times the list was extended instead. Now
a sweep of the vault's top-level markdown.

**A broken wikilink in a `.yaml` schema is invisible to the gate.** Rule 4 sweeps `.md`. A slug
written into `wiki/decisions/_schema.yaml` from memory rather than from the tree reached nothing and
reddened nothing; it surfaced only because the librarian copied it onto a page.

**Two figures were wrong in briefs written to serve the very rule they contradicted.** The slug
count was given as 423 moving by four; it moved by three, because a rule page carries no
`authority:` — arithmetic that counted a rule page as a slug-bearer in a brief about the rule that
forbids it. And an acceptance figure of "about thirty deferrals" came from a title grep counting
`rejected` and `declined`, which mark **prohibitions**; the real figure is 18.

**A claim reasoned from the page instead of read from the tool.** A brief asserted that moving a
rule page between folders leaves its rendering unchanged. The injector reads the folder. Same shape
as a presence test answering an identity question, one level up.

**The session applied opposite readings of the owner's silence within one hour** — "unless you
object" taken as consent, «окей, продолжаем» taken as insufficient. Both defensible, both cannot be
the rule. owner: «да, это был не конкретный ответ. Будем работать дальше, чтобы понимать что делать
в таких ситуациях.»

**It asked for a ruling and then removed the need for it.** The one-writer question was put to the
owner, and before he answered the session found a formulation making it moot — a librarian judging
by hand and applying with its own `Bash` loop is one writer either way. The result appears correct;
the route went around the question rather than through it. owner: «выносим как урок».

**Worth keeping: the admission rule caught a real duplicate on its first live use, against the
session's own inclination.** Superseding `governs-becomes-a-property-of-any-page` needed a slug;
`--near governs-scope` replied *"that question has a page, do not write a second"* and pointed at
the page being overturned. The slug was inherited. A new one would have left `governs-scope` grouped
in the register and carried by no live page — the stale half `--check` exists to catch.

**Worth keeping: measuring before agreeing turned an expensive-looking ruling cheap.** «governs
уходит из concepts» looked like it needed the rewriter-and-detector pair over 26 inbound links.
Reading the resolver took minutes and the ruling went from blocked to half an hour.

## Deferred

**`/pre-task` must cover `concepts/`, `entities/`, `proposals/` and `rules/`, not `decisions/`
alone.** owner raised it explicitly; the session built the index those folders are searched by and
did not touch the ritual that would use it. **First item.** Cost of not doing it: the guarantee that
a plan is checked against everything decided remains false, and the corpus proved the cost in this
very session — `proposals/a-generated-harness-map` held a finished design, was not found, and was
nearly written again.

**The reading funnel is not delivered as a procedure.** Stages 1–2 are built; no skill names
`vault-catalogue.sh` or `authority.md`. Cost: the instrument exists and nobody is told to use it,
which is the same shape as the five mechanisms found unwired.

**`lessons/` → `proposals/` at ingest.** The librarian reads the lessons at the end of an ingest and
produces **two** records from each — the fact into `concepts/` or `decisions/`, the action into
`proposals/` — and the lesson is archived only once nothing on it lives only there, which is the
clause already ratified for proposals. Owner's design. Cost of not doing it: `lessons/` stays a
store rather than a queue, at 121 pages.

**A real data format for `tags.md` and `authority.md`.** owner: «Правило про лишние зависимости -
окей. Но это то, что нам нужно. Нам нужен yaml или json или еще что-то для ведения тегов и
authority. Запиши, обсудим на следующей сессии.» Measured: **five scripts hand-parse YAML** here and
this session added the fifth. PyYAML 6.0.3 is installed but **transitive, not declared**.

**An admission test for mechanisms, mirroring the one built today for pages.** Raised by the session
after the owner asked how work can move on what matters rather than being permanent repair, and
shown the figure: since 2026-08-12 there are **119 commits, 95 touching harness or vault and none
touching `src/`**. The proposal is that a mechanism earns its place only where something concrete
was measurably blocked without it, and that a decision naming a mechanism must also name what
keeping it costs — nothing here budgets for the maintenance surface a mechanism creates. **No
verdict was given.**

**Eight `authority.md` families hold eleven slugs against a ceiling of ten.** Twenty were at the
ceiling before this work, so the overflow is arithmetic. Rebalancing is a judgement about the corpus.

**`an-authority-register-on-the-model-of-the-tag-dictionary` is now retirable** — both claims that
lived only there were landed. Retiring is the owner's.

**The four owed readings**, carried for a fourth session: whether the `core` criterion still sorts
`CLAUDE.md` without a remainder; the JavaScript rule page whose ground was `/pre-task` arriving
unconditionally; which reading the conditional-delivery gate carries; what
`permissions.defaultMode: "plan"` should mean for a `claude -p` run.

**Whether a hook should refuse a write rather than advise**, and the five built-and-unwired
mechanisms — both to the next session, with the mechanisms discussion. owner: «важно будет обсудить
на следующей сессии это и остальные механизмы работы всей системы.»

**Whether this work becomes S2's seventh criterion.** owner: «обсудим на следующей сессии.»

**The recorded objection that proposals should carry no `authority`** stands unresolved on its page,
marked. Its first test found **no competing pair among 24 proposals**, and in three of four
near-pairs the pages say so themselves.

**Could not close: none.** Twenty-two retro lines, 11 answered, 11 deferred.

## Feedback to the librarian

- process: `/pre-task` guarantees a full enumeration only over `decisions/`. Its own skill says
  "List every `decisions/` page", and the librarian agent repeats it. So 121 `lessons/`, 102
  `concepts/`, 33 `entities/` and 24 `proposals/` fall outside the guarantee. Surfaced when the
  owner asked what `/vault-ask` is for and how the wiki is surveyed at all; the cost was paid in
  this same session, where `proposals/a-generated-harness-map` held a finished design that was not
  found and was nearly written again from scratch.
- process: five mechanisms are built and wired to nothing, found by sweeping every script, skill,
  hook and agent for who names it. `scripts/vault-archive.sh` has zero callers anywhere, while a
  decision says the move "lives inside the ingest" and the ingest skill does not name it.
  `/vault-lint` is named by no skill, agent, hook or setting, and its own decision says it never ran
  "because no sprint has ever been opened" — S2 is open. `scripts/vault-catalogue.sh` reaches the
  librarian through the vault schema but no ritual requires it. `/vault-ask` has no delivery and
  leaves no trace. The `/handoff` drain of the pre-task ledger was already on the record. The
  owner's ruling: record it, discuss next session.
- process: a rule that delegates by RUNNING a script can be silenced by a zero-byte stub, and the
  selftest's own sandbox manufactures those stubs. Its placeholder loop materialises every path a
  page cites in `sources:` as an empty file, and rules 12 and 13 both ask their question by running
  a script. Measured 2026-08-21: with a zero-byte `scripts/vault-authority.sh`, rule 13 printed not
  one line. What protects the two tools today is only that the explicit `cp` runs before the
  placeholder loop and the loop leaves a real file alone; that ordering is invisible and was not
  stated anywhere. A guard now asserts both tools are non-empty before any case runs. The class is
  [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]].
- process: `authority.md` has a checked half and an unchecked half, and the brief argued for the
  unchecked one without saying so. `--check` parses `slugs:` and compares it against the tree in
  both directions; `definition:` and `aliases:` are read by no instrument at all. So a missing or
  wrong Russian alias fails silently and forever, in the permissive direction — and the aliases are
  precisely what the register was argued for on retrieval grounds. Same standing `tags.md` has, so
  it is not a regression; it is a gap nobody had named.
- process: `empty_vault` in the selftest kept its register list by hand and drifted for the THIRD
  time on 2026-08-21, when `authority.md` joined rule 1's existence check. The fixture's own
  comments already record the first two drifts and both times state the repair — derive the set,
  never list it — and the list was extended rather than swept on both occasions. It is now a sweep
  of the vault's top-level markdown off the pristine tree. Same class as
  [[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]], and the instructive part is that
  the file argued against itself twice in its own margin and lost both times.
- process: making a frontmatter field required couples every selftest fixture that plants a page,
  and the coupling arrives in two waves rather than one. Wave one is the schema: nine cases planted
  a page without `authority:` and went red on rule 2. Wave two is the admission rule itself: once
  those pages carried a slug, rule 13 reddened them again because the slug sat in no family in
  `authority.md`. The second wave is the more interesting one — it is the rule reaching into the
  suite and saying that a fixture planting a page and not its register entry is testing a corpus
  this project would refuse. Repaired with a `plant_slug` helper the fixtures call.
- process: a register's own prose can carry a `[[wikilink]]` that resolves to nothing and no
  instrument sees it. `authority.md` contains the literal `[[wikilinks]]` inside a code span, in the
  sentence forbidding wikilinked slugs. Harmless today because the file is deliberately outside rule
  5's link sweep, and named here because the day it is admitted to that sweep it would redden — and
  because it is the same blind spot the `.yaml` schemas have, found the same session.
- process: a brief I wrote asserted that moving a rule page between folders leaves its rendering
  unchanged. False, and the librarian measured it: `scripts/vault-inject.sh` derives the marker's
  type word from the FOLDER, not from the page, so all four markers in the repository's `CLAUDE.md`
  had to be retyped from `<!-- concept: … -->` to `<!-- rule: … -->`. The claim was reasoned from
  what the page carries rather than read from the injector — the same shape as
  [[a-presence-test-cannot-answer-an-identity-question]], one level up.
- lint: `lessons/` becomes a queue rather than a store. At the end of an ingest the librarian reads
  the lessons and produces TWO records from each — the fact into `concepts/` or `decisions/`, the
  action into `proposals/` — and the lesson is archived only once nothing on it lives only there,
  which is the clause already ratified for proposals. The proposals reach the owner through the
  brief and he decides. Owner's design this session; not built in it.
- lint: `wiki/proposals/an-authority-register-on-the-model-of-the-tag-dictionary.md` is built by
  this session's work and was NOT retirable on its own test until this session landed the two claims
  that lived only there — the obligation to record a rejected candidate slug as an ALIAS, and its
  falsified prediction that a register would make `authority` "rare rather than universal". Both are
  now on `authority-becomes-the-index-and-is-required-outside-rules`. Retiring the proposal is the
  owner's judgement and was deliberately not taken.
- measure: the vault stood at 479 pages and 2.9 MB in `wiki/` before this session, all
  `status: current`, none `deprecated`; `archive/` held 27 pages and 216 KB. By folder: 189
  decisions, 121 lessons, 102 concepts, 33 entities, 24 proposals, 10 rules. Created per day since
  2026-08-13: 80, 16, 19, 23, 110, 49, 43, 124, 15. `authority:` was carried by 423 pages, every
  value distinct; 56 carried none, of which 24 were proposals and 10 rules.
- measure: end of the session. `wiki/` holds 483 pages, 470 carrying `authority:` and 0 of the 11
  rules pages carrying one; `authority.md` holds 51 families over 543 lines and 41,782 bytes;
  `vault-catalogue.sh` prints 558 lines and 109,053 bytes. `wiki/decisions/` declares 168
  `prohibition`, 18 `deferral`, 6 `divergence`, and every `DIVERGENCE:` title matches its value.
  `vault-check-selftest.sh` caught 141, missed 0 (from 136); `hook-selftest.ps1` caught 108, missed
  0 (from 107). `vault-check.sh`, `vault-inject.sh`, `vault-authority.sh --check/--orphans/--binding
  /--trace`, `vault-catalogue.sh`, `ruff check` and `ruff format --check` all exit 0. The suite was
  NOT run — no Python changed.
- measure: since 2026-08-12 there are 119 commits, 95 touching `.claude`, `scripts` or the vault,
  and none touching `src/`. The product has not moved in nine days. This is the figure behind the
  owner's question about whether the work only ever grows.
- measure: five hand-written YAML parsers live in `scripts/` — `vault-check.sh`, `vault-inject.sh`,
  `vault-catalogue.sh`, `vault-units.sh` and the `vault-authority.sh` this session added. PyYAML
  6.0.3 is present in `.venv` but is **transitive** and absent from `pyproject.toml`.

## Anything else worth keeping

**The librarian's own report caught two errors in the briefs it was given**, and both were the
session's. It is the second session running in which the reviewing party found what the writing
party asserted without checking. Worth keeping because it is evidence about the review arrangement
rather than about either error.

## Harness

- harness: THE PRE-TASK LEDGER IS NOT DRAINED BY ANYTHING, and that is now the ruling rather than a
  gap. Owner at the retro of 2026-08-21: «Слив ledger не строим.» Asked three times across the
  session before it was answered. Two `current` pages assert the opposite in the same words —
  [[the-pre-task-ledger]] ("`/handoff` drains it, not `/retro`") and
  [[the-retro-writes-its-own-transit-file]] ("the ledger joins `vault-feedback.md` as a file
  `/handoff` drains") — and both need a dated correction, not a retirement: the reasoning that
  assigned the drain to `/handoff` rather than `/retro` is still sound, what changed is that there
  is no drain to assign. The rows are not lost: rotation files each session into
  `.superpowers/sdd/ledger/`, which is read by a human at a retro and by nothing else, and the owner
  ruled the same day that it is not pruned. This closes the alarm that has stood since 2026-08-20
  and it closes it by cancelling the work, not by doing it.
- harness: the ingest gains an admission criterion — a unit that qualifies, corrects or extends a
  claim an existing page already owns is appended to that page, and a new page is created only when
  no `current` page owns the claim. Decided by the owner this session as "Occam's razor, do not
  multiply entities", to be the ground rule rather than one more check. It renders from a
  `wiki/rules/` page into `.claude/agents/vault-librarian.md`, because the rule binds the librarian
  alone.
- harness: `authority:` becomes required on every page outside `wiki/rules/`, where it stays
  forbidden; `job_hunt_ai_vault/authority.md` joins the registers beside `tags.md`, holding families
  of authority slugs and their aliases, grouped by the librarian's judgement and never by a script's
  word overlap. Owner's decision this session.
- harness: `decisions/` gains a required `binding:` field with three values — `prohibition`,
  `deferral`, `divergence` — because the folder holds three different things and only one of them
  forbids anything. Measured at 189 pages: 6 carry a `DIVERGENCE:` title and about 30 record a
  deferral; filled, the real figures are 168 / 18 / 6. An absent value reads as `prohibition`, the
  safe direction. Owner's decision this session.
- harness: `governs:` is confined to `wiki/rules/`, owner's ruling at the retro of 2026-08-21: «Если
  у концепта появляется governs - Он становится правилом. Поэтому authority = required в concepts. А
  governs из concepts уходит.» It OVERTURNS his own ratified decision of 2026-08-17
  ([[governs-becomes-a-property-of-any-page]]), which is retired with a successor. Two `concepts/`
  pages moved into `wiki/rules/`; measured first, the link check resolves a wikilink by FILENAME
  anywhere under `wiki/` or `archive/`, so a folder move strands nothing and is not the rename this
  project requires a rewriter-and-detector pair for. `concepts/_schema.yaml` lost `governs` and
  `render` and gained `authority` as required, so `authority:` now has no exception anywhere outside
  `wiki/rules/`.
- harness: `.claude/skills/pre-task/SKILL.md` and `.claude/agents/vault-librarian.md` both say the
  enumeration covers "every `decisions/` page". The owner ruled that wrong: it must cover
  `concepts/`, `entities/`, `proposals/` and `rules/` as well, with `lessons/` deliberately excluded
  because they are to become a queue drained at ingest. **Not built this session.** The work item
  names its files.
- harness: no skill or agent names `scripts/vault-catalogue.sh` or `job_hunt_ai_vault/authority.md`,
  so the wide half of the reading rule — enumerate frontmatter across the corpus in one command, then
  open at most ten — reaches nobody. The instrument exists and no ritual requires it. **Not built
  this session.**
