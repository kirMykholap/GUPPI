---
session: 2026-08-31
sprint: S3
commits: none
---

# Handoff — 2026-08-31

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

Every section stays, always. An empty one is a legal answer — write "none". A dropped one is
knowledge that was never asked for, and nothing else in this repository looks inside `raw/`.

Each section names where `/ingest` files it. **That mapping lives here and nowhere else** — the
skill reads it rather than carrying a copy, because a copy drifts from what it copied and this
one drifted for three days as `section 7`.

## State

**The cleanup's pages half moved for the first time, and both halves are reported because reporting
one is reporting half.**

| | before | after |
|---|---|---|
| `wiki/` total | 630 | **520** |
| `wiki/decisions/` | 340 | **211** |
| `wiki/rules/` | 17 | **36** |
| `binding: prohibition` | 295 | **166** |
| `bash scripts/vault-catalogue.sh \| wc -c` | 139,210 | **112,690** |
| `wiki/` text, bytes | 2,930,812 | **2,377,729** |

The catalogue stood at 201,927 bytes before the cleanup began, so it is down **44 %** against that.

**Done.** The cleanup table is regenerable and English. The hook delivers `render: authority`. The
53 verdicts are set and ratified. Nineteen rule pages exist and `index.md` lists them. 129 decisions
are in `archive/2026-08-31/2026-08-31-the-families-become-rules/pages/`. The vault's `CLAUDE.md`,
the two folder schemas and `docs/who-reads-the-vault.md` are repaired.

**Not done, by ratified scope.** The 35 harness-facing families and their 164 prohibitions are
untouched. The convergence pass over the ~245 live non-decision pages is next session's. Nothing is
committed — the whole session stands in the working tree at `a4a3e00`.

**In flight.** Nothing.

**Next step.** The convergence pass, then the second kind of family.

**Checks, each from its own invocation.** `make smoke` exit 0, run in the foreground twice — once
before the retro and once after the last tracked write. `powershell -NoProfile -File
scripts/hook-selftest.ps1 < /dev/null` → `caught 229, missed 0`. `bash scripts/vault-check.sh` exit
0 with the two standing advisories — four filenames counting, region coverage `11 of 17`. `bash
scripts/vault-authority.sh --check` agrees, `authority.md` untouched and 63 families intact. `make
style` passes with `scripts/` newly inside it. `scripts/session-dialogue-selftest.py` caught 52,
`scripts/vault-measure-selftest.py` caught 59, both missed 0. `bash
scripts/vault-check-selftest.sh` was **not** run — it costs 34 to 60 minutes and belongs at a
sprint's close.

## Entities

**`.claude/hooks/serve-the-rule.ps1` changed and its dormant half is now written.** It reads
`render:` and `tool_name`, neither of which it read before. A `render: authority` page is matched on
the `authority:` slug of the file being touched, exactly, with no resolution through `authority.md`.
Its silence is now scoped by mode as well as by path: silent on `Edit|Write` inside `wiki/`,
speaking on `Read` there, silent in `archive/` and on the six registers in both directions, and
ending the run at once on a `Read` outside the vault so each half fires on one mode. The note it
prints branches by delivery kind. Measured at 389–478 ms on the write path and 392–450 ms on the
read path with 36 pages in `wiki/rules/`.

**`.claude/settings.json` registers that hook on `Read`.** That registration is what makes the
`authority:` half reachable at all, because the write path is silent exactly where a slug exists.

**`scripts/build-families-table.py` is new.** It regenerates `docs/vault-cleanup-families.md` in
English from `authority.md`, the frontmatter of every live page, and the hand-written verdicts in
`docs/vault-cleanup-verdicts.md`, which it reads rather than overwrites. The old generator existed
only in another session's temp directory, was in no commit, and destroyed any verdict written by
hand.

**`scripts/build-family-rules.py` is new.** It drafts one `wiki/rules/` page per vault-facing
family and refuses outright to write a title carrying a measurable quantity.

**`docs/vault-cleanup-verdicts.md` is new** — the hand-written half of the table, one line per
family, which the generator reads.

**Nineteen pages appeared in `wiki/rules/`**, all `render: authority`, all carrying `authority:` and
no `governs:` and no marked slice.

## Decisions

**owner:** «Все, что внутри vault - по правилу A. Все, что вне - не имеет authority. Там только
рендер в конкретный файл.» And, put as his own position and then ratified: «Я считаю, что хук не
должен искать ничего кроме конкретного Authority. А уже наша задача будет сделать так, чтобы
authority у файлов были одни у разных типов страниц.»

A `render: authority` rule is found by the touched file's own `authority:` slug, and that mode
serves pages inside the vault alone. **Rejected: the session's proposal that the hook resolve a
member slug through its family group in `authority.md`** — the family register is an instrument of
the cleanup and must not become a runtime dependency. This removed `paths:` from the hook entirely:
the field gains no second reader and needs no second checker.

**owner:** «У gate правило какраз работает как нужно. У двух porposal не может быть один slug
authority. Как и у двух любых типов. Это доволняет нашу схему, что типы порождают друг друга, а gate
следит за тем, чтобы они не дублировались.»

The target state is one `authority:` slug carried along a chain of types — decision to proposal or
rule to concept or entity — and rule 3 of the gate guards it by refusing two pages of one type
sharing a slug. **Rejected: the session's framing of that refusal as an obstacle to convergence.**

**owner:** «Но мы проведем уборку вручную. То есть сами найдем страницы, которые можно обьеденить
под одним slug. Значит нам нужно будет вручную пройтись по страницам и исправить у них authority
после чистки.»

The convergence is done by hand, page by page, after the sweep. **Rejected: anything mechanical.**

**owner:** «берем текущие descisions и обьединяем их в группу под ним authority. Этот один authority
и станет для новой страницы rule, которая будет содержать заголовок этих descisions, а сами
descsions уйдут.» And in the same exchange: «Каждый authority - одна запись в rules/.»

His own restatement of the family mechanism, recorded because the slug-resolution question was
opened against it.

**owner:** «мы вообще должны переработать pre-task. Сейчас он читает слишком много. Поиск должен
давать ему релевантные страницы, а не заставлять читать все и только там pre-task иожет углубится.
Что такое релвантная страница? - може судить по authority. Смысл совпал? - читаем. Но это отдельный
разбор vault-ask.»

`/pre-task` reads too much and is to be reworked so that search hands it relevant pages instead of
the whole enumeration, relevance judged by whether an `authority:` slug matches in meaning. **Ruled
a separate discussion belonging to `vault-ask`**, so it is a topic and not work in the cleanup.

**owner:** «мы еще не закрыли фронтир вопросов. Зачем ты показываешь план? НАм нужно закончить
фронтир»

The frontier is closed before a plan is shown, not after. He interrupted `ExitPlanMode` with five
items still open. **Rejected: presenting a plan while any frontier item is undiscussed.**

**owner:** «200000 контекста уже забито. Это кошмар. Пытаемся экономить»

Context is to be economised. Recorded because it changed how the rest of the session was worked —
targeted reads instead of whole files, and no re-reading of what was already held.

**owner selected: «генератором»** — the 19 family rule pages are drafted by a generator under the
librarian's dispatch, and the librarian reads the output whole, repairs it and answers for it.
Chosen against the librarian authoring them by hand, on the ground that the clauses are already
machine content — a title and a slug lifted out of frontmatter. This works around the one-writer
clause by permission rather than by argument, which is why it is written here.

**owner selected: «переводим»** — `docs/vault-cleanup-families.md` is translated into English rather
than declared an exception to the forward-only English rule. Chosen against writing an exception
page. **The second half of that case — whether the verdicts live in the table or in a file of their
own — he did not answer**, and it stands as the session's.

**owner selected: «Первый род - сейчас. Второй обсуждаем на следующей сессии»** — only the
vault-facing families are built this session; the harness-facing kind, whose text must be rendered
into a file and cannot be a list of titles, is discussed next. Chosen against building both.

**owner selected: «в следующей»** — the manual convergence pass over the ~245 live non-decision
pages runs next session. Chosen against folding it into the tail of an already long session, on the
ground that 245 judgements made tired are 245 hurried ones.

**owner selected: «понял. Да, можно»** — `index.md` gains a section listing the new rule pages with
a link each, which narrows the standing prohibition that `index.md` carries hub pages and nothing
else. Chosen against writing a link into each of ~290 decisions before they moved.

**owner selected: «принимается»** — the 53 cleanup verdicts as the session set them: 18
`vault-facing` families holding 131 prohibitions, 35 `harness-facing` holding 164, and `none` used
nowhere. Shown as enumerated prose in chat, every family named with its count, and with the two
borderline calls named by the session itself.

**owner selected: «окей, согласен»** — the four rules lifted for the cleanup are four different
outcomes rather than one. `what-travels-from-a-rule-page-is-a-marked-slice` and
`a-decisions-archival-condition-is-read-off-its-binding` are **narrowed permanently**, because a
`render: authority` rule carries no slice by construction and a prohibition discharged into a rule
now leaves by the ordinary path. `every-rule-in-wiki-rules-owes-a-mechanical-instrument` stays
lifted until S3 closes, and reading criterion 1 is his.
`the-decisions-folder-is-censused-before-its-type-system-is-redesigned` is **discharged rather than
deleted** — the cleanup table is the reading it asked for and the verdicts are the half it lacked.
He had offered to delete it («может просто уберем ее?») and took the recommendation against, because
that page is the only record of why the table was built at all.

**owner selected: «согласен»** — "outside any sprint" takes the narrow reading: the cleanup is not
counted to S3 but is governed by the rules like any work. Chosen against the wide reading, which
would have cost a live rule and a slice rendered into the repository's `CLAUDE.md` right now. The 24
deferrals naming no sprint name S3, worked next session.

**owner selected: «откладываем, согласен»** — the three old pairs and seven `RAISED, NOT RESOLVED`
markers are deferred, with one exception: the marker standing on the suspension of
`a-decisions-archival-condition-is-read-off-its-binding`, whose ground this session removed.

**owner selected: «Да, добавляем»** — `scripts/` joins `make style`, the check half only. Put to him
with the cost measured first: 10 findings across the folder, two auto-fixable. `ruff format --check
scripts` is deliberately not added, because it would fail on six existing files and reformatting
scripts nobody is reviewing belongs in a diff someone reads.

**owner selected: «пройди список и принеси выводы»** — the retro list is worked by the session,
which brings conclusions, rather than by an interview. Chosen against `grill-me` and against no
conversation at all.

**Diverged, and each is a decision with a rejected alternative.**

**The retro skill's step 2 mandates `AskUserQuestion` and the session asked in prose.** The live
prohibition `review-list-shape` requires enumerated prose in chat rather than a rendered menu, and
the standing rule is that how a slice is executed is the owner's and overrides a skill. Rejected:
obeying the skill. The two instructions disagree and one of them should be narrowed.

**The session read none of the 134,036-byte session extract beyond its headings**, where step 0 of
the retro asks it to be read. Its premise is that memory at the end of a long session is a
compaction of itself; this session's context was never compacted and held every owner turn verbatim,
and the owner had asked for context to be economised. Rejected: spending ~35k tokens re-reading what
was already in hand. The skill has no way to tell the two cases apart.

**Decisions the session took, in its own voice, not his.** He confirmed them as the session's rather
than signing them. The `Read` matcher was wired on the session's own measurement rather than on his
ruling, its precondition having asked for a measurement first. A `Read` outside the vault ends the
run, and the six registers stay silent in both directions. The verdicts live in a file of their own.
Part two of the cleanup is excluded as a narrowing under
`narrowing-a-scope-notifies-and-widening-it-asks`, announced rather than asked. And the session read
"the verdicts are set by the session and brought as one block" as already decided by two pages of
the corpus, against the prose of the brief and `sprint.md` which say the owner writes them.

## How it is built

**The lookup delivery, end to end.** A family of `authority.md` becomes one page in `wiki/rules/`
carrying `render: authority`, one `authority:` slug and no `governs:`. `serve-the-rule.ps1` opens
the head of the file being touched, reads its `authority:`, walks the head of every page in
`wiki/rules/`, and hands over any `current` page whose slug is equal. Nothing is resolved: the match
is string equality and the family register is not read at runtime.

**Why the write path had to stay silent and the read path had to speak.** The silence exists so the
librarian is not served a rule about every page of an ingest. But a slug exists only under `wiki/`,
which is exactly where the write path is silent — so with writes alone the `authority:` half has no
occasion to fire at all. Splitting the silence by mode is what gives it one, and it is the owner's
own ground: one almost always searches first and acts afterwards, so the search is where a rule can
catch you.

**Why a clause is a title.** Only two of the 295 prohibitions carried a `# The rule text` section,
so there was no written rule text to lift. Titles in this store are sentences that state a claim,
which is what makes the substitution work and what makes the pages generatable.

**Which slug a family rule takes, and why the mechanical answer was wrong.** The generator picks the
earliest-decided member's slug — the answer that opened the question. That decision then leaves for
`archive/`, so nothing live carries the slug and the hook matches nothing. The librarian moved the
slug on 14 of 18 pages onto one already carried by a live concept or entity of the same family,
which is the convergence direction and gives the delivery coverage on the day it is built.

**Both orders of the family-rule act redden the gate, and that is a property rather than a mistake.**
Writing the pages first leaves them orphaned — rules 4 and 5 build the linked set from `wiki/`,
`archive/`, `index.md`, `tags.md` and `sprint.md`, and nothing points at a page just created.
Writing the `index.md` lines first leaves broken wikilinks. A red gate locks the librarian out
through `lock-the-librarian.ps1`, and the librarian is the only party who may write `index.md`. So
the generator must run **inside** the librarian's dispatch.

**Why no row was written into `authority.md`.** `vault-authority.sh --check` computes
`ungrouped = tree − register`, and a slug inherited from a member of the family is already grouped.
Its stale direction widens to `archive/`, so the 129 moved pages do not strand their rows either.
The register is untouched at 63 families.

**Why an archived decision is still reachable and how far.** The clause of each family rule names its
decision by `[[wikilink]]`, which is also what satisfies the archiver's precondition that a live page
under `wiki/` names the slug. The claim therefore survives in `wiki/`; the reasoning and the rejected
alternative are one hop away in `archive/`, which nothing sweeps and `/pre-task` does not read.

## Lessons

**A dict keyed by a field that stopped being unique loses rows silently.** The first run of the table
generator reported 293 prohibitions where the tree holds 295. `authority:` became shareable across
types on 2026-08-30 and the code was written on 2026-08-31 against the older assumption; the two
pages lost were exactly the two slugs carried by two pages each. **The defect was a day older than
the code that contained it**, which is the shape worth remembering: a mapping written correctly
against last week's invariant is wrong today and reports nothing.

**A path list written by `pathlib.write_text` on Windows carries CRLF into the filename.** The sweep
list was generated without `newline="\n"`, Python translated the line endings, and
`scripts/vault-archive.sh` refused the first file with `no such file` because the `\r` was inside
the name. Caught by a refusal on the first item rather than by reading, which is the archiver
working as designed.

**A measurement can retire the deferral that demanded it.** The `Read` matcher had been deferred on
the premise that `Read` is the most frequent tool call there is. Counted across every transcript this
project has: Bash 5088, Edit 1102, Read 490, Agent 395, Write 392, Grep 49. It is the fourth, and a
third of the write path, because this repository reads with `cat` and `grep`. The precondition was
what produced the number and the number closed the item.

**A predicted regression that does not appear is still a reading worth writing down.** The plan named
the hook's cost as a regression and expected roughly a doubling at 70 rule pages. At 36 pages it
measures 389–478 ms against a recorded 750–930 ms at 17. The folder doubled and the cost did not
rise. This session cannot say whether the old figure is wrong or merely taken in other conditions,
and it did not spend the session finding out.

**A target that covers part of a repository reports clean about the part it covers.** `make style`
ran ruff over `src` and `tests` only. Two new files in `scripts/` produced 21 findings the target
could not see, and the whole folder produced 10 more — none of which had ever been looked at.

**No `/pre-task` counts are recorded for the run this session made**, because the agent's answer did
not carry them in the two-number form the template asks for. It named 148 pages on its shortlist and
33 opened in full, which is the pair, and it is written here rather than lost.

## Deferred

**The 35 harness-facing families and their 164 prohibitions.** Their text belongs in a harness file
and needs `governs:` with a written region, which is prose somebody writes rather than a list of
titles a script assembles. **Consequence of not doing it:** `wiki/decisions/` stays at 211 rather
than falling further, and the cleanup is half done by page count.

**The convergence pass over the ~245 live concepts, entities and proposals.** **Consequence:** four
of the nineteen family rules answer for a family holding no live concept or entity at all —
`retro-ratification`, `page-naming`, `missing-decision-compilation`, `repealed-status-mint` — so
nothing in `wiki/` carries their slug and the hook serves them to nobody. Their coverage waits on a
page being written, not on a slug being moved.

**The nineteenth page's contradiction with its own decision.** That decision says a rule takes the
slug of the decision that caused it, which is right for one decision arriving and wrong for a rule
compiled from a family whose decisions all leave. The page states both cases and chooses neither.
**Consequence:** a reader meets two answers and no verdict.

**The `sources:` split — 29 pages from the repository root against 24 vault-relative**, while
`a-sources-path-inside-the-vault-is-vault-relative` rules for the second. The 19 pages written today
follow the rule. **Consequence:** a sweep nobody has scheduled, and a reader who copies the wrong
neighbour.

**`vault-catalogue.sh` does not print `archive/`.** The 129 decisions moved today are therefore
invisible to `/pre-task` phase 1, and the obliges-and-rejected half of each sits one wikilink deeper
than any instruction sends a reader. **Consequence:** `/pre-task` starts answering with claims rather
than with what a decision obliges. Belongs to the `/pre-task` rework he named as a `vault-ask` topic.

**The 24 deferrals naming no sprint** now name S3 and are worked next session. **Consequence of not
doing it:** `a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused` stays unsatisfied for
a ninth brief.

**The three old pairs — the CRLF count, the `page:` verdict's resolvability, `log.md` rotation — and
seven `RAISED, NOT RESOLVED` markers.** **Consequence:** a tenth, seventh and sixth consecutive
brief carrying them. The eighth marker is not deferred: this session removed its ground.

**`ruff format --check` over `scripts/`.** Six files would be reformatted. **Consequence:** the
folder's formatting drift stays invisible, and this is work not scheduled rather than a deferral
anyone has ratified.

**No instrument guards `docs/vault-cleanup-verdicts.md`.** Nothing checks that its family names still
match `authority.md`, so a renamed family would silently lose its verdict and the generator would
print an empty one. **Consequence:** a hand-written file whose drift has no detector, which is the
shape this store repairs by deletion.

## Feedback to the librarian

Drained verbatim from `.superpowers/sdd/vault-feedback.md`. Three lines carry a note the catcher
added, and the note is carried with them.

- miss: brief.md and sprint.md say "99 verdicts"; the table holds 105 empty markers - 54 in part one, 51 in part two. Surfaced when the table was counted directly at session start.
- miss: the cleanup's own input has no carrier. `docs/vault-cleanup-families.md` names its generator as `scratchpad/build_families_table.py`, which is in no commit and exists only in another session's temp directory; it also overwrites the file whole, so the first hand-written verdict makes the table unregenerable.
- miss: `bash scripts/vault-check.sh --rules` reports 19 headings where 18 exist - its self-sweep matches `^# [0-9]` and picks up a wrapped comment line at vault-check.sh:240.
- measure: on a4a3e00, `wiki/` holds 630 pages and 2,930,812 bytes; `bash scripts/vault-catalogue.sh | wc -c` prints 139,210. 295 pages carry `binding: prohibition`, they sit in exactly 53 of the 63 registered families, and zero slugs are ungrouped. Two carry `target_kind: repeal`, so a sweep moves 293 and leaves 47 in `decisions/`. This measures the corpus, not the cleanup's progress - the pages half has not moved.
- measure: only 2 of the 295 prohibition pages carry a `# The rule text` section, which is what makes a family rule's clause the decision's title rather than a written-out rule.
- miss: the vault has no answer for how a `render: authority` rule reaches a file with no frontmatter. The ratified key is the touched file's own `authority:` slug, which exists only under `wiki/`, while 275 of the 295 prohibitions are about `.claude/`, `scripts/` and `src/`. Surfaced when a plan for the hook's branch was checked by /pre-task.
- miss: a family rule inherits ONE member decision's slug, but a family holds up to fifteen. Matching slug-to-slug reaches one page of fifteen; reaching the family means the hook resolves both slugs through `authority.md`, which nothing says it does.
- miss: `docs/vault-cleanup-families.md` carries 696 Cyrillic lines of 1819 and is a repository document. The English rule is forward-only with the file as its unit, so regenerating that file whole puts all of it under the obligation - and the session's own first plan would have minted a second Russian file in `docs/` beside it.
- miss: `scripts/vault-archive.sh --sweep` does not select a discharged prohibition. Its `decisions/` selector takes `deprecated`, `divergence`, `processed` and slugs named in some page's `decided_by:` - about 57 of the 293, because a rule page's `decided_by:` names exactly one decision. The remaining ~236 need named batches, and named mode exits 2 on the first refusal.
- miss: the rule page for the rule about rules does not exist. The decision stands, `render: authority` is carried by no page in the tree, and the proposal requires that page be written first - so the family sweep is 54 pages, not 53.
- measure: `vault-authority.sh --check` computes `ungrouped = tree - register`, so a rule page inheriting its causing decision's slug adds ZERO rows to `authority.md`. The deferral `the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages` rests on "writing the pages alone produces 53 ungrouped slugs", and that premise is false under inheritance. Its basis is `code`.
- decision: the session understood it - part two of the cleanup table (51 concepts/entities groups, 194 pages) is out of this session's scope. Read as a narrowing under `narrowing-a-scope-notifies-and-widening-it-asks`, so it is announced rather than asked, on the owner's own refusal to name an exit criterion for those two folders.
- decision: the owner said it - a `render: authority` rule is found by the touched file's own `authority:` slug, and that mode serves pages inside the vault ALONE. Everything outside the vault carries no `authority:` and is delivered by rendering into a named file, `governs:` plus `render: region|whole`. This settles the fork the session raised and removes `paths:` from the hook entirely - the field gains no second reader and needs no second checker.
    (marked as his words and carrying no quotation - a quotation keeps his own words in guillemets; if these are yours rather than his, the shape is `the session understood it`)
    (the quotation exists and is carried in `## Decisions` above: «Все, что внутри vault - по правилу A. Все, что вне - не имеет authority. Там только рендер в конкретный файл.»)
- decision: the session understood it - the cleanup verdict is therefore three-valued, not two. A family about the vault's own pages becomes a `render: authority` rule; a family whose text belongs in a harness file becomes a `governs:` rule under the delivery that already works; a family that is neither produces no rule. The table legend's two values (живое/мёртвое) predate the ratification above.
- miss: a `governs:` rule needs a marked region in its destination file, and `what travels from a rule page is a marked slice` is one of the four rules suspended FOR the cleanup. The second kind of family therefore lands on a requirement that is currently lifted, and no page says what a family rule does about it.
- decision: the owner selected it - the 54 family rule pages are written by a generator under the librarian's dispatch, and the librarian reads the output whole, repairs it and answers for it. Put to him as a recommendation against the librarian authoring them by hand; he answered «генератором».
- decision: the owner selected it - `docs/vault-cleanup-families.md` is translated into English rather than declared an exception to the forward-only English rule. Put to him as a recommendation with the alternative of writing an exception page; he answered «переводим». The second half of that case - whether the verdicts live in the table or in a file of their own - was not answered and stands on the session's recommendation.
- miss: nothing in the corpus says what `/pre-task` reads once `decisions/` is emptied. Phase 1 filters `decisions/` for prohibitions, `vault-catalogue.sh` stopped printing `archive/` on 2026-08-30, and a family rule's clause is a title - so the obliges-and-rejected half of every archived prohibition sits one wikilink deeper than any instruction sends a reader.
- decision: the owner said it - `/pre-task` reads too much and is to be reworked so that search hands it relevant pages instead of the whole enumeration, with relevance judged by whether an `authority:` slug matches in meaning; deepening happens only there. He ruled it a separate discussion belonging to `vault-ask`, so it is recorded as a topic and not as work in the cleanup.
    (marked as his words and carrying no quotation - a quotation keeps his own words in guillemets; if these are yours rather than his, the shape is `the session understood it`)
    (the quotation exists and is carried in `## Decisions` above, beginning «мы вообще должны переработать pre-task».)
- miss: the corpus does not say what a family rule of the second kind contains. A `render: region` rule ships a marked slice of connected prose into a harness file; a list of member titles is not that, so the generatable shape decided for the family rules covers only the `render: authority` kind. Nothing names the split or its cost.
- decision: the owner selected it - the cleanup builds only the first kind of family this session, the vault-facing families delivered under `render: authority`; the second kind, whose text must be rendered into a harness file, is discussed next session. Put to him as a recommendation over two alternatives; he answered «Первый род - сейчас. Второй обсуждаем на следующей сессии».
- decision: the session understood it - a family with no rule keeps its decisions in `wiki/decisions/`, because the repeal releases a prohibition only once the family rule carrying its clause exists. This makes the cleanup table's legend false where it says the decisions go to `archive/` in both cases, and the legend is what is rewritten. Follows from the ruling above rather than from a sentence of his.
- decision: the owner selected it - `index.md` gains a section listing the new rule pages with a link each, which narrows the standing prohibition that `index.md` carries hub pages and nothing else. Put to him as the cheaper of two ways to keep the new pages out of the orphan verdict; he answered «Да, можно».
- decision: the owner said it - «берем текущие decisions и обьединяем их в группу под одним authority. Этот один authority и станет для новой страницы rule, которая будет содержать заголовок этих decisions, а сами decisions уйдут». And earlier in the same exchange: «Каждый authority - одна запись в rules/». This is his restatement of the family mechanism and it is the sentence the slug-resolution case is about.
- miss: the design of record does not say how the hook reaches a family rule from a member slug. A family holds up to fifteen `authority:` slugs, a rule page carries one, and the hook's match is slug-to-slug - so eleven of twelve members of a family would serve nothing. Surfaced by working an example through the mechanism rather than by any page saying so.
- decision: the owner said it - the hook looks up nothing but the exact `authority:` slug; the family table is an instrument of the cleanup and must not become a runtime dependency. «Я считаю, что хук не должен искать ничего кроме конкретного Authority. А уже наша задача будет сделать так, чтобы authority у файлов были одни у разных типов страниц.» The session's own recommendation - resolving a member slug through its family group in `authority.md` - is withdrawn.
- decision: the owner said it - the target state is one `authority:` slug carried across a chain of types, `decision → proposal/rule → concept/entity`, with the slug propagating; rule 3 of the gate guards it by refusing two pages of one type sharing a slug, and that is the intended behaviour rather than an obstacle. «У gate правило какраз работает как нужно… Это доволняет нашу схему, что типы порождают друг друга, а gate следит за тем, чтобы они не дублировались.»
- decision: the owner said it - the convergence is done BY HAND: the session finds the pages that can be merged under one slug and repairs their `authority:` after the sweep. «мы проведем уборку вручную… нам нужно будет вручную пройтись по страницам и исправить у них authority после чистки».
- decision: the owner selected it - that manual re-slugging pass over the ~245 live non-decision pages runs in the NEXT session, not this one. Put to him as a recommendation against folding it into the tail of an already long session; he answered «в следующей».
- measure: zero `authority:` slugs are shared across types anywhere in `wiki/`, so on the day the family rules are written the hook serves nothing at all. Delivery coverage starts at zero and grows only with the manual convergence above. This session's measurable result is the archive and the cheaper enumeration, not a working delivery.
- decision: the owner selected it - the four rules lifted for the cleanup are not one thing. `what-travels-from-a-rule-page-is-a-marked-slice` and `a-decisions-archival-condition-is-read-off-its-binding` are narrowed PERMANENTLY, because a `render: authority` rule carries no slice by construction and a prohibition discharged into a rule now leaves by the normal path. `every-rule-in-wiki-rules-owes-a-mechanical-instrument` stays lifted until S3 closes, and reading criterion 1 is his. Put to him as four separate recommendations; he answered «окей, согласен».
- decision: the owner selected it - `the-decisions-folder-is-censused-before-its-type-system-is-redesigned` is NOT deleted. It is discharged: the cleanup table is the reading it asked for, and the Ш2 verdicts supply the half the table lacks - which of a group is in force. He had offered to remove it («может просто уберем ее?») and took the recommendation against, on the ground that the page is the only record of why the table was built at all.
- decision: the owner said it - a `render: authority` rule is found by the touched file's own `authority:` slug and that mode serves pages inside the vault ALONE; everything outside carries no `authority:` and is delivered by rendering into a named file. «Все, что внутри vault - по правилу A. Все, что вне - не имеет authority. Там только рендер в конкретный файл.» The session's proposal to resolve a member slug through its family group in `authority.md` was put and refused: «хук не должен искать ничего кроме конкретного Authority».
- decision: the owner said it - the target state is one `authority:` slug carried along a chain of types, `decision -> proposal/rule -> concept/entity`, and rule 3 of the gate guards it by refusing two pages of ONE type sharing a slug. «У gate правило какраз работает как нужно… типы порождают друг друга, а gate следит за тем, чтобы они не дублировались.» The convergence is done BY HAND: «сами найдем страницы, которые можно обьеденить под одним slug… вручную пройтись по страницам и исправить у них authority после чистки».
- decision: the owner selected it - that manual convergence pass over the ~245 live non-decision pages runs in the NEXT session («в следующей»); the 54 family rule pages are written by a generator under the librarian's dispatch («генератором»); `docs/vault-cleanup-families.md` is translated into English rather than declared an exception to the forward-only English rule («переводим»); `index.md` gains a section listing the new rule pages, narrowing the hub-pages-only prohibition («Да, можно»); only the first kind of family is built this session and the second is discussed next («Первый род - сейчас. Второй обсуждаем на следующей сессии»); the 53 cleanup verdicts as the session set them («принимается»).
- decision: the owner selected it - the four rules lifted for the cleanup are FOUR DIFFERENT OUTCOMES, not one. `what-travels-from-a-rule-page-is-a-marked-slice` and `a-decisions-archival-condition-is-read-off-its-binding` are narrowed PERMANENTLY; `every-rule-in-wiki-rules-owes-a-mechanical-instrument` stays lifted until S3 closes and reading criterion 1 is his; `the-decisions-folder-is-censused-before-its-type-system-is-redesigned` is DISCHARGED rather than deleted - the cleanup table is the reading it asked for and the verdicts are the half it lacked. He had offered to delete it and took the recommendation against. «окей, согласен».
- decision: the owner selected it - "outside any sprint" takes the NARROW reading: the cleanup is not counted to S3 but is governed by the rules like any work. The wide reading was rejected because it would cost a live rule and a slice rendered into the repository's `CLAUDE.md` right now. The 24 deferrals naming no sprint name S3, worked next session. «согласен». And the three old pairs plus seven `RAISED` markers are deferred to S4 with one exception - the marker standing on the suspension of `a-decisions-archival-condition-is-read-off-its-binding`, whose ground this session removed. «откладываем, согласен».
- decision: the owner said it - `/pre-task` reads too much and is to be reworked so search hands it relevant pages rather than the whole enumeration, relevance judged by whether an `authority:` slug matches in meaning. Ruled a separate discussion belonging to `vault-ask`.
    (marked as his words and carrying no quotation - a quotation keeps his own words in guillemets; if these are yours rather than his, the shape is `the session understood it`)
    (the quotation exists and is carried in `## Decisions` above, beginning «мы вообще должны переработать pre-task».)
- miss: `scripts/vault-archive.sh --sweep` does not select a discharged prohibition. Its `decisions/` selector takes `deprecated`, `divergence`, `processed` and slugs named in some page's `decided_by:`; a rule page's `decided_by:` names exactly one decision, so the sweep would have moved about 57 of 293. The 129 were moved by named batches after a `--dry-run`, which collects refusals and moves nothing.
- miss: the session ran `scripts/build-family-rules.py` itself and walked straight into the register deadlock - 18 orphan rule pages reddened the gate, and a red gate locks out the librarian through `lock-the-librarian.ps1`, who is the only party who may write the `index.md` lines that clear the orphans. Both orders go red; the generator has to run INSIDE the librarian's dispatch. Reverted and re-run correctly, and the ordering is a property of the mechanism rather than a mistake of judgement.
- miss: `make style` runs ruff over `src` and `tests` only, so `scripts/` is unlinted. Two new files there produced 21 findings the target could not see.
- miss: the rule about rules had a decision and no page. `render: authority` was carried by nothing in the tree, so the family sweep was 19 pages rather than 18, and the proposal requires that page be written FIRST.
- measure: after the sweep, `wiki/` holds 520 pages against 630 - decisions 340 to 211, rules 17 to 36, prohibitions 295 to 166. `bash scripts/vault-catalogue.sh | wc -c` prints 112,690 against 139,210 before it and 201,927 before the cleanup began, which is 44 percent off every dispatch. `wiki/` text is 2,377,729 bytes against 2,930,812. Both halves moved for the first time.
- measure: `Read` is NOT the most frequent tool call in this repository, which is the premise the `Read` matcher was deferred on. Across every transcript this project has: Bash 5088, Edit 1102, Read 490, Agent 395, Write 392, Grep 49. `Read` is a third of the `Edit|Write` path, so registering the matcher adds about a third to a hook that already fires 71 to 108 times a session.
- measure: `serve-the-rule.ps1` costs 389-478 ms on the write path and 392-450 ms on the read path with 36 pages in `wiki/rules/`, measured through a pipe on 2026-08-31. The figure recorded for 17 pages is 750-930 ms, so the folder doubled and the cost did not rise. One of the two readings is taken in conditions the other was not, and this session does not know which.
- measure: 14 of the 19 new rule pages carry an `authority:` slug also carried by a live concept or entity, so the lookup delivery serves something on the day it was built. The session had predicted zero, on the correct measurement that no slug was shared across types beforehand; the librarian moved the slug off the earliest-decided decision - which leaves for `archive/` - and onto a page that stays.
- miss: the retro skill's step 2 mandates `AskUserQuestion`, and the live prohibition `review-list-shape` requires enumerated prose in chat rather than a rendered menu. The session asked in prose, on the standing rule that how a slice is executed is the owner's and overrides a skill. The two instructions disagree and one of them should be narrowed.
- measure: the session extract reports 20 owner turns, 49 session replies, 10 feedback marks and ZERO menus - every ruling this session arrived in his own words rather than through a list the session framed. The retro skill flags the opposite shape as worth a line; this is the good direction of the same measurement.
- measure: `.superpowers/sdd/vault-feedback.md` holds 48 marks - 22 `decision:`, 16 `miss:`, 8 `measure:`, 2 `harness:` - against a session of 20 owner turns. Not drained here; `/handoff` drains it.
- miss: the session read none of the 134,036-byte extract beyond its headings, because this session's context was never compacted and it already held every owner turn verbatim. Step 0 exists because memory at the end of a long session is a compaction of itself; that premise did not hold here, and the skill has no way to tell the two cases apart.
- measure: four of the five family rule pages that serve nothing sit in families holding ZERO live concepts or entities - `retro-ratification`, `page-naming`, `missing-decision-compilation`, `repealed-status-mint`. There is no slug to converge onto, so their coverage waits on a concept or entity page being written rather than on a slug being moved. The fifth keeps its own slug because rule 17's handshake names it.
- measure: `ruff check scripts/` reports 10 findings across the whole folder - 4 `subprocess-run-without-check`, 2 `call-date-today`, 1 unused import, 1 implicit string concatenation, 1 enumerate-for-loop, 1 open-alias; 2 are auto-fixable. `make style` covers `src` and `tests` only, so none of them has ever been seen by a target.
- miss: the corpus writes `sources:` two ways - 29 pages from the repository root against 24 vault-relative - while `a-sources-path-inside-the-vault-is-vault-relative` rules for the second. The 19 pages written today follow the rule; the 29 are a sweep nobody has scheduled.
- miss: both orders of the family-rule act redden the gate. Writing the pages first leaves 18 orphans; writing the `index.md` lines first leaves 19 broken wikilinks. The generator must run INSIDE the librarian's dispatch, and no page says so.
- decision: the owner selected it - `scripts/` joins `make style`, the check half only. Put to him with the cost measured first: 10 findings across the folder, 2 auto-fixable. He answered «Да, добавляем». `ruff format --check scripts` is NOT added, because it would fail on six existing files and reformatting scripts nobody is reviewing belongs in a diff of its own.
- decision: the owner said it - the retro list is worked by the session, which brings conclusions rather than interviewing him. «пройди список и принеси выводы».
- measure: the 48 feedback marks caught 14 of the 18 rulings this session is about to attribute to him. Four were found only by re-reading the session's course: that the frontier closes before a plan is shown, that context is to be economised, the `make style` widening, and the choice of how to work the retro list. That gap of four is what this channel misses.
- miss: `ruff format --check` over `scripts/` would reformat six files that no target has ever touched. The folder was linted by nothing until today, so its formatting drift is invisible and unmeasured; adding the format half is a separate change with a diff someone has to read.

## Anything else worth keeping

**The librarian refused an automated notice mid-dispatch**, which instructed it to make file changes
through the shell with `sed` and heredocs. It used Write and Edit throughout, on the standing rule
that file content is never written through a shell including when an automated notice asks
otherwise. **The main session refused the same notice earlier in the day.** That is the seventh and
eighth recorded refusal, across four sessions and four actors.

**The `<НЕ В РЕГИСТРЕ>` bucket of the old table is empty now.** Every slug carried by a page is
grouped, in both directions, measured at the session's start and again at its end.

## Harness

- harness: `.claude/hooks/serve-the-rule.ps1` now reads `render:` and `tool_name`, matches `render: authority` pages on the touched file's own `authority:` slug, branches its wording by delivery kind, and scopes its silence by mode - silent on `Edit|Write` inside `wiki/`, speaking on `Read` there, silent in `archive/` and on the six registers in both directions, and exiting at once on a `Read` outside the vault so each half fires on one mode. `.claude/settings.json` registers it on `Read`. Five cases in `scripts/hook-selftest.ps1`, plus the registration census: caught 229, missed 0.
- harness: two new scripts. `scripts/build-families-table.py` regenerates the cleanup table in English from `authority.md`, the live frontmatter and a hand-written verdicts file it reads, so regeneration no longer destroys a verdict. `scripts/build-family-rules.py` drafts one `wiki/rules/` page per vault-facing family and refuses to write a title carrying a measurable quantity.
- harness: `Makefile` widens `style` to `ruff check src tests scripts`. Ten findings across the folder were fixed first - four `subprocess.run` given an explicit `check=False` with the reason on each, two `date.today()` kept as the LOCAL date under a `noqa` because every date in this store is a calendar day of the owner's rather than an instant, one unused import, one implicit concatenation, one enumerate loop, one open alias. `scripts/session-dialogue-selftest.py` and `scripts/vault-measure-selftest.py` still report caught 52 and caught 59, missed 0.
- harness: the retro skill's step 2 and the live prohibition `review-list-shape` disagree - one mandates `AskUserQuestion`, the other requires enumerated prose in chat. One of the two should be narrowed, and the skill is the cheaper end.
- harness: `.claude/skills/retro/SKILL.md` step 0 asks the extract to be read whole, with no exception for a session whose context was never compacted. A session that still holds every owner turn verbatim pays ~35k tokens to re-read what it has. The step needs a condition, or a sentence saying to read the marks and the headings when the transcript is still in hand.
