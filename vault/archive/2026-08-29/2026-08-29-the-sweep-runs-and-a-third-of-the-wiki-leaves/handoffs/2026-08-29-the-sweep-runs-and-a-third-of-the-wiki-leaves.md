---
session: 2026-08-29
sprint: S3
commits: none
---

# Handoff — 2026-08-29

Anywhere below, a line beginning **owner:** is the owner's own testimony.

## State

**Done.** Six of the seven S3 items the owner took were built, proved and left green. Item 41 he
parked mid-session.

- **42 — `--only` stops reading a typo as a pass.** An unmatched substring now refuses with exit 2
  before the sandbox is built; `--list` prints the twelve sections as well as the cases; `--only`
  matches a section name as well as a case name; the baseline copy left the `pass` tally; and the
  count case the file's header has promised since 2026-08-24 was written and fired.
- **32 — the archiving sweep, built and RUN.** 239 pages left `wiki/`.
- **33 — the advisory on a live link into a retired page**, behind `--lint`, one line per dead
  target.
- **37 — the admission rule's first audit**, ten pages judged.
- **40 — the `VAULT-FEEDBACK` requirement now lives in one hook** registered on two events.
- **43 — the reply-silence counter**, split into a counter that cannot speak and a speaker that
  cannot count.

**Not done.** Item 41, parked by the owner. Nine deferrals from the retro, each naming where it is
picked up; six of them need S3 items that do not exist yet.

**In flight: the whole session's work is uncommitted.** 239 renames-with-modification and eleven
modified files, nothing staged as a commit. HEAD is still `d6a488b` from the previous session.

**Checks, each from its own invocation:**

- `bash scripts/vault-check.sh` — **exit 0**, 24 s, one standing advisory at `9 of 15`.
- `bash scripts/vault-check-selftest.sh` — **caught 194, missed 0, exit 0, 29m12s**, whole and
  unfiltered.
- `powershell -File scripts/hook-selftest.ps1` — **caught 217, missed 0**, 3m15s.
- `bash scripts/vault-authority.sh --check` — the register and the tree agree, **507 slugs**.
- `make smoke` — **SMOKE-EXIT: 0**, 3m56s, foreground. Verified still valid at the door of
  `/handoff`: every modified tracked file is older than the run.
- `make style` — all checks passed, 88 files.
- `make test` — **not run.** No Python changed this session.

## Entities

**`scripts/vault-archive.sh` gained a sweep mode.** `--sweep <date> <session>` walks `decisions/`,
`lessons/`, `proposals/` and `rules/`, applies each folder's criterion, writes `status: archived`
before moving, moves into `archive/<date>/<session>/pages/`, rewrites `sources:` citations,
continues past a page it may not move, collects those refusals and prints them **before** the gate
runs, appends one line to `log.md`, and exits 1 when anything was refused or the gate is red. Its
preconditions were factored into a routine that returns a refusal instead of ending the process —
the single largest change in the file. `--dry-run` extends to it. It computes the longest
destination path before moving anything and refuses the whole run over 240 characters.

**`scripts/vault-check.sh` gained the deprecated-link advisory** and lost a defect: two advisories
printed the word `advisory:` on their continuation lines.

**`scripts/vault-check-selftest.sh` gained sections in `--list`, section matching in `--only`, an
exit-2 refusal for an empty selection, a `BASELINE` record kind, and the count case.** Its three
source sweeps became functions because they now have two callers.

**`scripts/vault-authority.sh --check` changed what "stale" means.** A register row is stale only
when no page in `wiki/` **or `archive/`** carries the slug.

**`.claude/hooks/remind-the-feedback.ps1` now owns the `VAULT-FEEDBACK` requirement**, registered on
`UserPromptSubmit` and on `PostToolUse`/`Skill`, with a ritual branch that is not counter-gated. It
also reads the reply-silence count.

**`.claude/hooks/remind-the-smoke.ps1` lost the feedback demand** and keeps the smoke half.

**`.claude/hooks/catch-the-feedback.ps1` gained a counter** and still prints nothing on every path.

**`.claude/hooks/probe-message-display.ps1` existed for one measurement and was deleted.**

**`.claude/skills/vault-lint/SKILL.md` gained the sweep step**, after the lessons dispatch and
before the audit.

**`wiki/` is a third smaller.** 762 pages to 523: `decisions/` 341 to 276, `lessons/` 182 to 12,
`proposals/` 49 to 45. `entities/`, `concepts/` and `rules/` are untouched.

## Decisions

**owner:** «значит продолжаем разговор по оптимизации, архивации и процессов. Наша задача -
подготовить детальный план действий и имплементировать сегодня решения»

**The scope of the day was his**, and he narrowed it again after the plan was sized: S3 items 32,
33, 37, 40, 41, 42, 43, dropping 34, 35, 36, 38 and 39 from the seven-item recommendation the
session put to him. Item 41 he parked later in the same session.

**owner:** «Я уже говорил ранее, что ingest должен передавать инструкции библиотекарю. В таком
случае библиотекарь сам запускает субагентов и ждет их вердикта. Это один запуск бибилотекаря, а не
два и не три.»

**owner:** «У librarian нет инструмента dispatch - значит нужно добавить ему такой инструмент. Судя
по документации claude : субагенты могут вызывать своих субагентов.»

**owner:** «@.claude/agents/vault-librarian.md должен содержать инструкции про : как искать и писать
в vault, какие субагенты и инструменты у него есть в распоряжении. Но у него не должно быть описания
процесса Ingest. Процесс ingest описывается тут @.claude/skills/ingest/SKILL.md»

That reverses `the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return`,
whose stated ground was that the librarian carries no dispatch tool — a ground repairable by one
entry in a `tools:` line. **Rejected: the session's reading that the librarian is dispatched twice.**
Not built: item 36 is outside today's scope.

**owner:** «страницы в rules/ попадают под архивацию только если есть решение, которое говорит об
этом, а само правило при этом помечено как refused или deprecated»

He corrected himself the next turn: **`refused` is not minted in `rules/` and the status values stay
as they are.** So the criterion is a decision plus `deprecated`.

**owner:** «если у какой-либо страницы есть decided_by со ссылкой на decision - этот decision должен
стать processed и уйти в архив. То есть у библиотекаря должна быть инструкция при добавлении поля
decided_by - выставить processed у decision, на который ссылаемся. А уже архиватор проходит и по
decided_by и по processed(предохраянем себя от ошибок агента). processed по сути остается
косметикой, но далее мы его будем использовать»

**owner:** «в идеале эти реестры должны рендерится. То есть иметь свою страницу rule в vault,
которая рендерить их полностью или частично. В таком случае упоминание будет идти на страницу, а не
на реестр.»

Not today's build. It settles today's narrower question: **the four vault-root registers do not
count as citers.** **Rejected: counting them**, on the ground that `sprint.md` names half the corpus.

**owner:** «Он должен не только напечатать список, а и архивировать его. Действия в log.md. Я думаю
что это именно то, что стоит сделать именно сегодня»

**Taken against the session's recommendation**, which was to hold the 240-page move for a separate
sitting on the ground that the vault only permits it, never obliges it.

**owner:** «sweep дописывает строку в log.md И сообщает тому, кто вызвал(библиотекарю). Библиотекарь
в иделае вообще не должен трогать log.md. Лог должен заполнятсья механичсеки. И так же механичсеки
архивироваться в конце архиватор полностью, а на его месте появистя пустой log.md»

**And the rotation is tied to the sprint close** — he selected that against tying it to `/vault-lint`
or to a sweep run, on the ground that a sweep may fire three times a sprint or not at all.
**Only the sweep's own line is built today.**

**owner:** «снимаем это правило, оно мешает и не несет пользы. Страница уходит в архив с о slug и
authority»

**This repeals the fourth supersession step of 2026-08-22** — remove a retired page's slug from
`authority.md` before the page moves — which was itself an owner-selected ruling. **Rejected: the
session's three options**, which were to revert the move, to teach the archiver to edit the register,
or to have the session edit it once as a divergence. **What it obliges:**
`retiring-a-page-removes-its-slug-from-the-authority-register` is now false and still live in
`wiki/decisions/`, and `scripts/vault-authority.sh --check` was narrowed so that a row whose page has
been archived is not stale.

**owner:** «На будущее - стоит завести правило , чтобы ты всегда так задавал вопросы и подавал
материл. С контекстом, обьяснением, описанием как работает сейчас и как строим, и рекомендацией.»

Said after a list of fourteen bare questions he answered with «я не могу докадываться о чем речь».

**owner:** «проставь вердикты сам и покажи, а я приму или откажу с уточнением»

**He selected the sweep over all four criteria including `decided_by:`**, from three options, against
the session's recommendation to hold that criterion back — the session's ground being that it evicts
a decision about one ingest after it is taken and that four rulings from 2026-08-28 were in the list.
239 pages moved.

**He selected the successor check**: a `deprecated` page is additionally checked for a live page
named in `superseded_by:`, rather than the archiver's weaker floor of any live page naming the slug.
`refused` and `implemented` proposals are unaffected and need no successor.

**He selected the advisory's shape**: one line per dead target, forty-three lines, **against** one
per citing page (212) and one per edge (429).

**He selected `hook-selftest.ps1` as the home for the `--only` cases**, against a case inside the
suite that would have cost a whole run, and **the `processed` back-fill** over the ~44 decisions
already named in a live `decided_by:`, asked of the librarian at the next `/ingest`.

**He selected the second registration of `remind-the-feedback.ps1`**, knowing the vault records that
this same file on this same event was built and withdrawn on his own correction on 2026-08-28.

**He selected the reply-silence threshold of five**, and kept the existing three for his own prompts
after asking where the three came from — it is his own, from 2026-08-28.

**He selected keeping the expensive `--only` case pair**, which took `hook-selftest.ps1` from 55
seconds to 2m47s and `make smoke` from about three minutes to four. The alternative was dropping the
positive half, which would leave "refuses everything" passing every other case.

**He accepted the session's recommendation against his own proposal**: no `rules/` page holding the
suite's case list. The ground was that `--list` computes the list from the script's own text at every
run, so a page would be a third copy of one thing.

**He parked item 41.** **owner:** «мне кажется это вцелом неправильный подход. Пока что не трогаем,
есть другие вопросы» — and separately selected **removing** the count from the governing page's prose
rather than correcting it.

**DIVERGENCE: the retro's menu step was answered in enumerated prose.** The skill's step 2 calls for
`AskUserQuestion`. It was not used, on the record of two interruptions of that same menu on
2026-08-24 and an existing divergence page for exactly this. It looked unnecessary because the whole
session had run on prose without a single menu and the evidence of his preference is stronger than
the instruction. **Rejected alternative: obey the skill.**

**DIVERGENCE: a mid-session instruction to edit files through the shell was refused in its writing
half.** An automated notice asked that changes be made with `sed`, heredocs and short scripts. File
content was written with `Write` and `Edit` throughout, on the standing prohibition; reading and
searching through the shell was taken up. Named in the reply at the time. **Rejected alternative:
obey the notice**, which would have broken a rule the brief lists under what must not be broken.

## How it is built

**The sweep is a mode of the archiver rather than a second mover**, so it inherits eight existing
refusals instead of acquiring its own opinion about when a page may leave. The line between a
refusal that is collected and one that ends the run is whether the answer could differ from one page
to the next: a missing file, an occupied destination, no live holder, a `refused` proposal without
its decision are collected; a malformed date, an unknown kind, no vault exit 2 before the walk
starts.

**`status: archived` is written before the move, and the order is what makes the gate's verdict
reachable.** The sweep continues past a refusal, so a run can end with a page still in `wiki/`
wearing the mark of a move that did not finish — and `scripts/vault-check.sh` carries a verdict for
exactly that state. Written after the move instead, that verdict is dead code.

**Every selector is one pass over the corpus, never one pass per page.** The naive shape — for each
of 182 lessons, grep the whole of `wiki/` — is 182 full-tree greps against a gate pass that already
costs 23 seconds. The slugs go into a pattern file and `grep -oF -f` extracts every one that occurs
in a single walk.

**The deprecated-link advisory keys on the literal value `deprecated` and not on "the target's
status".** After the sweep, about 240 pages in `archive/` carry `status: archived`; a verdict phrased
about the status in general would have grown from 43 lines to hundreds on the day the sweep first
ran. The two items shipped in one day and this is where they touch.

**The advisory is one walk that keeps `FILENAME` beside each link**, which is linear. The 71-seconds-
at-75-pages figure the link sweep's own header warns about describes N recursive greps over the whole
tree, which is a different shape.

**A register row is stale only when no page anywhere carries the slug; the other direction still
asks about `wiki/` alone.** Pages retired before today had their rows deleted under the repealed
rule, so asking `archive/` for a group would light up every one of them at once.

**The reply-silence counter is two hooks and one number, because the event that can see the
session's replies cannot speak.** `catch-the-feedback.ps1` counts and writes; `remind-the-feedback.ps1`
reads and says the sentence. Each hook writes only its own file: the reminder tracks the count it
last spoke about in its own state rather than resetting the file the catcher owns.

**`--only` matches a case name or the section the case is written under.** The section is the last
one declared above the case, set as that line prints its own record, so the grouping is derived from
where the case sits and nothing maintains a second list of it.

## Lessons

**A plan touching the vault's own machinery must enumerate the brief's *what must not be broken*
list as items.** `/pre-task` answers per item of the plan. It was given forty decisions and returned
fourteen corrections; the obligation that a retired page's slug leaves `authority.md` first was in
none of the forty and therefore in none of the fourteen. The sweep then moved 239 pages, left 239
stale rows, reddened the gate on all of them — and `lock-the-librarian.ps1` refused to dispatch the
only party permitted to repair the register. The deadlock was real and was broken by repealing the
rule rather than by satisfying it.

**`grep -q` on the right of a pipeline under `set -o pipefail` inverts the test it is written to
make.** grep leaves on the first match, the upstream `sed` dies of SIGPIPE, and the pipeline reports
that failure. Written as the empty-selection refusal, it fired on every substring that *did* match.
Caught within a minute by running the case; the code carries the reason and this is the lesson.

**A comment that quotes the literal a sweep looks for is counted by that sweep.** `--list` finds an
inline case by the literal `report "..."`, and the paragraph explaining it quotes exactly that — so a
case named `...` appeared in every listing since the flag was built. The count case the file's own
header promised, and which would have caught it, did not exist.

**Two advisories carried the word `advisory:` on their continuation lines** against the owner's
ruling of 2026-08-18, so `grep -c 'advisory:'` — which the brief reports as the count of advisories —
read 54 where the true count is 30. Both were written after that ruling and copied the wrong shape
from each other; the filename advisory, which the ruling was made for, has obeyed it throughout.

**A rule with no instrument behind it is a rule a fixture can violate for a week.** The selftest's
archive fixture planted a `status: deprecated` page carrying no `superseded_by:` and had done since
2026-08-22. It passed because nothing read the field. The successor check built today reads it, and
the fixture went red rather than the check being wrong.

**A `/pre-task` ran: the shortlist named 123 pages and the agent opened 49 in full, plus 8 in part.**
It returned fourteen corrections to a forty-item plan, of which the largest was a collision between
two items of the same day that neither item's own page could see.

**`bash` on `PATH` under PowerShell on this machine is the WSL shim in WindowsApps**, which would run
a repository script under a different operating system. `Find-Bash` in `.claude/hooks/vault-path.ps1`
derives it from where git is, and the suite's new cases are its third caller.

## Deferred

**Item 41, the strike form, parked by the owner** with the objection unstated. The ratify-or-narrow
fork is neither ratified nor narrowed, and twenty-one wider lines stand in `sprint.md` beside a rule
still asking for the narrow form. **Consequence: whoever reopens it inherits a parked item whose
reason lives in one chat line.**

**The librarian's dispatch tool and the `/ingest` rewiring** — S3 item 36. Decided today, not built.

**A librarian instruction: on adding `decided_by:`, set `processed` on the target.** Decided today,
needs an item of its own.

**The one-off `processed` back-fill** over the ~44 decisions already named in a live `decided_by:`.
Asked of the librarian at the next `/ingest`.

**`log.md` rotates at the sprint close and the librarian stops writing it.** Decided today; it is a
redesign of who holds the pen over the journal and needs an item of its own.

**The four vault-root registers render from `rules/` pages of their own.** His idea, recorded, not
built.

**Whether `--near`, `--group` and `--list` should reach archived pages.** His repeal points at it;
the session named it and deliberately did not build it, because widening the cached corpus walk would
change four subcommands at once.

**The `--check` asymmetry created today**: a row whose page is archived is not stale, while an
archived page is still not required to be grouped.

**A check that `advisory:` never appears on a continuation line.**

**An archival criterion for `entities/` and `concepts/`** — 174 pages, and now a third of `wiki/`.
Already S3 item 38.

**What `/pre-task` lost by the `decided_by:` criterion is unmeasured.** 65 decisions left the set it
enumerates, including four rulings from 2026-08-28. The claims survive on the citing pages, but
`binding:` — the field it filters on to answer *what stops this plan* — exists only on a decision
page. The first reading is its next run.

**Nothing is committed.** 239 renames-with-modification and eleven modified files.

## Feedback to the librarian

**The first four lines below were filed by the previous session's ingest, after its own `/handoff`
had already drained the file.** They have never been compiled and are carried here rather than
dropped.

- miss: журнал 2026-08-28 несёт commits: 65f19ec..215b82e, что по нотации git исключает левый конец и называет четыре коммита, тогда как секция State говорит пять. 65f19ec принадлежит этой сессии. /handoff инструктирует брать диапазон как <first>..HEAD, и эта инструкция сама производит расхождение на единицу. Это иной дефект, чем тот, который журнал сообщает о себе - там речь о коммите, который журнал же и приземляет. Нашёл библиотекарь на шаге 8.
- measure: /ingest 2026-08-28 - 277722 токена, 128 вызовов инструментов, 34 минуты 56 секунд, против оценки 271465 и 34м08с, названной перед тратой по прошлому чтению на журнале сопоставимого размера. Оценка попала по обеим осям. Журнал 61213 байт против 62422 у предыдущего.
- miss: библиотекарь писал содержимое страниц через shell heredoc почти весь ingest, против file-content-is-written-with-the-tool-and-never-through-a-shell, и заметил это только когда heredoc с brief.md не распарсился - ровно тот отказ, который та страница и записывает. Проверено вызывающим независимо, а не принято на слово: ноль CR-байт и ноль символов замены по всем тронутым файлам, все пять русских блоков владельца дошли дословно на именованные страницы. Проверка не является лицензией.
- measure: ревью ingest 2026-08-28 - гейт exit 0 при advisory 9 of 15, coverage 149 из 149 INGEST COMPLETE до и после переезда в архив, 27 новых файлов и 20 изменённых, 48 путей в коммите. Выборка на верность: десять page-вердиктов открыты рядом со строками источника, десять из десяти верны.

**And this session's own lines.**

- decision: the session's scope is the optimisation, archiving and process items of S3, and the day is to produce a detailed plan and implement what is decided - the owner said it, in his own words: "значит продолжаем разговор по оптимизации, архивации и процессов. Наша задача - подготовить детальный план действий и имплементировать сегодня решения"
- measure: 240 of 762 live wiki pages match their folder's archival criterion today - decisions 66 of 341, lessons 170 of 182, proposals 4 of 49, and zero in entities, concepts and rules, which have no criterion. It means the sweep's first run would shrink wiki/ by 31%, and it does NOT mean the suite gets 31% cheaper: the gate reads wiki/ alone so its shared pass shrinks, while the suite's per-case sandbox copies the whole tree and archive/ stays on disk
- measure: the sweep's first run over all four folders would refuse nothing - every selected page already has a live citer, by construction for the decided_by: criterion. It means the continue-past-a-refusal path decided on 2026-08-28 cannot be exercised on this corpus and its selftest case is the only proof of it
- miss: `a-decision-is-processed-when-a-live-page-names-it-in-decided-by` states the loose predicate selects "181 of 329", and the figure cannot be reproduced from the tree under either reading - wikilinks from live proposals and rules give 166, and any-occurrence-of-the-slug also gives 166. The neighbouring figures on the same page reproduce exactly (120 prose-only, the 3-into-archive split, the overlap of 1). Surfaced while sizing S3 item 34
- measure: the three inputs to the decisions agent, re-derived on 2026-08-28 - unprocessed decisions 269 recorded against 279 measured (folder grew 329 to 341, mechanical clauses 60 to 62); prose-only mentions 120 recorded against 120 measured; links into deprecated pages 424/332/210/42 recorded against 429/336/212/43 measured. It means the predicates reproduce and the denominators drift; it does NOT mean any of them has a gauge - no command for any of the three is written down anywhere in the vault or in scripts/
- measure: /ingest costs 271,465 tokens and 34m08s for one source today, and the S3 rewiring adds two reading dispatches (143-230k for the decisions agent, 388,649 and 17m23s for the lessons collector's only real run) plus a second librarian round trip, at every session. It means items 34-36 raise the per-session cost that the optimisation topic's third member exists to lower, and no page in the vault reconciles the two
- miss: `a-narrow-suite-run-that-matches-no-case-still-prints-a-catch` line 17 states the inline cases bypass the --only filter, and they do not - `report()` at vault-check-selftest.sh:274 asks `wanted`, landed in d6bceb2 on 2026-08-25, three days before the lesson was written. The real source of the `caught 1` is the baseline copy at lines 574-583, which calls next_rf directly and never asks `wanted`, and which --list also cannot see. Surfaced while sizing S3 item 42
- miss: `scripts/vault-check-selftest.sh:48-50` promises a count case pinning --list against the number a real run reports, and no such case exists in the file. The comment asserts a guard that is not there
- miss: the strike annotations in sprint.md all read `struck 2026-08-27` and the file contains no `struck 2026-08-28`, while both `an-answered-item-leaves-the-next-list-by-being-struck-in-place` and the S3 item 41 line date the pass to 2026-08-28. A grep for the date the pages name finds nothing
- measure: the deprecated-link figures re-derived on 2026-08-28 evening - 43 slugs, 429 occurrences, 336 page-target pairs, 212 live pages, against the 42/424/332/210 the proposal recorded the same morning. It means the advisory's input drifts within a single day; it does not mean the method disagrees - it reproduces exactly
- measure: a reading dispatch about the harness tripped the subagent instruction-shaped-output filter on `settings-json` for the second recorded time, which `the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns` predicted would happen every time such a dispatch is right to run. It means the filter has no exemption for a reading agent reporting on hook wiring, and the finding is relayed rather than acted on
- decision: /ingest hands the librarian a workflow and the librarian itself dispatches the reading subagents for decisions and lessons, waits for their verdicts, and returns once - the main agent reviews after it finishes. One librarian dispatch, not two. The owner said it, in his own words, restoring the scheme a session had ruled against on 2026-08-28. It reverses `the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return`, whose stated ground was that the librarian carries no dispatch tool
- miss: that page's ground is repairable in one line and the page does not say so. `.claude/agents/vault-librarian.md:4` reads `tools: Read, Grep, Glob, Bash, Write, Edit`; adding `Agent` is the whole obstacle. A ruling was recorded as settled design where it was a missing entry in a tool list
- decision: today's scope is S3 items 32, 33, 37, 40, 41, 42, 43 - the owner selected it from the seven-item recommendation the session put to him, dropping 34, 35, 36, 38 and 39
- miss: [wiki/rules/_schema.yaml] the rules folder schema carries a folder-specific archival criterion - deprecated plus a decision behind the overturn - that names no decision page, against that schema's own header rule requiring a decision to name the page it is written on. It is the only folder-specific archival paragraph of the six. Surfaced by /pre-task against plan decision 10
- miss: [an-answered-item-leaves-the-next-list-by-being-struck-in-place] the page says twenty-three items were struck; sprint.md carries 17 reading `struck 2026-08-27` and 8 reading `struck 2026-08-26`, commit a75d4b5 says twenty-two, and this session's plan said 21. Four counts of one pass. The repair is deleting the count from the prose, not correcting it
- miss: [a-decision-is-processed-when-a-live-page-names-it-in-decided-by] the page says the librarian sets `processed`, and this session read it as the decisions agent's mark. The mechanical route is available today and reaches about 44 of 341 decisions; nothing carries the mark only because no librarian has been asked to apply it
- measure: [none] wiki/ holds 757 `current`, 4 `implemented`, 1 `idea`, 0 `deprecated`, 0 `processed` on 2026-08-28. It means the sweep's deprecated and processed criteria select zero today and the proposals criterion selects four; it does not mean any of them is untested
- measure: [none] taking the baseline copy out of the suite's `pass` tally shifts every published suite count in the corpus by one - caught 133, 141, 148, 156 and 194 across at least six pages. It means the change is corpus-wide and silent; it does not mean any of those readings was wrong when taken
- decision: the librarian's agent file describes its capabilities - how to search the vault, how to write it, which tools and which subagents it has - and never a ritual's process; the ingest process, including the instruction to dispatch the decisions and lessons subagents and wait for them, lives in .claude/skills/ingest/SKILL.md. The owner said it, in his own words, correcting a session that had read the two as interchangeable
- decision: the librarian is given a dispatch tool so it can run its own subagents - the owner said it, citing Claude's documentation that subagents may call subagents. It supersedes the ground on which `the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return` was written, which was that the librarian carries no such tool
- decision: rules/ pages are archived only where a decision says so AND the rule itself is marked deprecated - the owner said it in his own words, then corrected himself the next turn: `refused` is NOT to be minted in rules/ and the status values stay as they are
- decision: when a page gains a decided_by: field the librarian sets `processed` on the decision it points at, and the archiver selects on BOTH decided_by: and processed - the second as insurance against an agent's mistake. `processed` is cosmetic for now and will be used later. The owner said it, in his own words
- decision: the four vault-root registers should ideally be rendered from rule pages of their own, so a mention lands on a page rather than on a register - the owner said it. Not today's build; it settles today's narrower question, that registers do not count as citers
- decision: a deprecated page moving to archive/ is additionally checked for a live successor named in superseded_by:, rather than the archiver's weaker floor of any live page naming the slug - refused and implemented proposals are unaffected and need no successor. The owner selected it
- decision: the sweep RUNS FOR REAL today, not only as a dry-run list, and writes its actions into log.md - the owner said it, in his own words, against the session's recommendation to hold the 240-page move for a separate sitting
- decision: the deprecated-link advisory prints one line per dead target, 43 lines, not per citing page and not per edge - the owner selected it
- decision: S3 item 41 is parked - the owner said the whole strike-in-place approach may be wrong and that it is not touched for now. The count in the governing page is removed from the prose rather than corrected, which he selected separately
- decision: the --only cases go in hook-selftest.ps1 rather than in the suite, and the processed back-fill over the ~44 decisions already named in a live decided_by: is asked of the librarian at the next /ingest - the owner selected both
- decision: remind-the-feedback.ps1 gains a second registration so one hook owns the VAULT-FEEDBACK requirement - the owner selected it, knowing the vault records that this file on this event was built and withdrawn on his correction earlier the same day
- miss: [none] no page says whether a SCRIPT may append to log.md. The one-writer clause names the librarian and is written about agents; `the-steward-is-scripts-that-run-after-the-librarian` is adjacent but does not rule it. Surfaced when the owner ordered the sweep to record its actions there
- decision: the reply-silence threshold is 5 assistant replies and the existing 3 for the owner's prompts stays - the owner selected it, after asking where the 3 came from; it is his own from 2026-08-28 and the session had not proposed changing it
- decision: the sweep appends its own line to log.md AND reports to whoever called it; the librarian should ideally not touch log.md at all; the log is filled mechanically; and at the end the archiver moves the whole file away and an empty log.md takes its place. The owner said it, in his own words. Only the sweep's own line is in today's scope
- miss: [none] nothing in the vault rules whether a maintained case list would be legal beside the derived one `--list` already prints. The owner asked whether a rules/ page should hold the suite's case list; the session recommended against it, citing the printed-versus-maintained ruling, and proposed matching on the suite's own section names instead - which are derived and which --only cannot select on today
- miss: [none] `--list` in scripts/vault-check-selftest.sh has overcounted its inline cases by one since it was built: the sweep finds an inline case by the literal `report "..."`, and the comment above the sweep quotes that same literal to explain what it looks for, so a case named `...` was listed every time. The count case the header says pins `--list` against a real run did not exist, so nothing could see it. Fixed by skipping comment lines; `--list` now reports 181 cases where it reported 182
- measure: [none] scripts/hook-selftest.ps1 went from 55 s at 194 cases to 2m47s at 204. Almost all of the increase is one case - the positive half of the --only pair, which lets a run proceed and therefore pays for a sandbox copy of 762 pages and two gate runs. Measured beside it: one case through --only costs 1m57s and the gate alone costs 23 s. It means `make smoke` grows from about three minutes to about five; it does not mean the suite itself got slower
- measure: [none] the admission rule's first audit, over the ten pages the ingest of 2026-08-26 created: 4 could have been a dated section on an existing page, 4 genuinely needed a page, 2 turn on a ruling nobody has given. The log trail the rule requires is present for 8, partial for 2, absent for none. It means the rule is obeyed in form; it does not mean the lookup was run before the write, which nothing can show - vault-authority.sh --near leaves no trace and the rule calls the log entry "the whole compensation"
- miss: [a-coverage-verdict-is-checked-for-presence-and-never-for-resolvability] the page says vault-coverage.sh resolves a `page:` verdict against the tree "not at all"; scripts/vault-coverage.sh:109 strips everything after " - " and resolves each name, with nine lines of comment saying so deliberately. The neighbouring page `the-page-verdict-is-checked-for-the-pages-existence-and-not-for-the-claim` is right about the same mechanism. Two current pages, adjacent claims, different authority slugs, so rule 3 cannot see the disagreement
- miss: [none] two of the ten pages restate a claim an existing page already carried in a dated section written by the SAME ingest - archive-path-length against `vault-archive-sh`, and smoke-gate-inference against `the-pre-task-state-library`. The admission lookup ran and the log records why a new page was still right, so the rule did not fail; what it does not ask is whether the claim was already being written elsewhere in the same pass
- measure: [none] the selftest's archive section fixture planted a `status: deprecated` page with no `superseded_by:` and had done since 2026-08-22. It passed because nothing read the field. The successor check ordered on 2026-08-29 reads it and the fixture went red; the fixture was repaired, not the check. It means the corpus's supersession rule had no instrument behind it until today
- decision: the sweep runs over all four criteria including decided_by: - the owner selected it from three options the session put to him, against the session's recommendation to hold the decided_by: criterion back. 239 pages moved
- decision: the fourth supersession step of 2026-08-22 - remove a retired page's slug from authority.md - is REPEALED. The owner said it, in his own words: "снимаем это правило, оно мешает и не несет пользы. Страница уходит в архив со slug и authority". It reverses an owner-selected ruling of 2026-08-22, and `retiring-a-page-removes-its-slug-from-the-authority-register` is now false and needs retiring
- miss: [none] neither the session's plan nor the /pre-task run against it carried the obligation that a retired page's slug leaves authority.md first - a rule the brief names under "what must not be broken". The sweep moved 239 pages and left 239 stale rows; the gate reddened on all of them, and lock-the-librarian.ps1 then refused to dispatch the only party permitted to repair the register. The deadlock was real and was broken by repealing the rule rather than by satisfying it
- measure: [none] the first real sweep, 2026-08-29: 239 pages moved in 5m16s, 239 marked status: archived, 1 sources: citation rewritten, 0 refused. wiki/ went from 762 pages to 523 - decisions 341 to 276, lessons 182 to 12, proposals 49 to 45. The gate is green at 24 s and the register agrees at 507 slugs. It means the corpus the gate walks is a third smaller; it does not mean the suite is cheaper, which is unmeasured
- measure: [none] the sweep's dry run over the live corpus costs 3m10s and the real run 5m16s, almost all of it the per-page citation count, which is one grep of wiki/ and archive/ per selected page. It means a sweep is a minutes-long operation rather than a seconds-long one
- miss: [none] two advisories in scripts/vault-check.sh printed the word `advisory:` on their continuation lines - the quote advisory and the decided_by: shortfall - against the owner's ruling of 2026-08-18 that only the headline carries it, because the brief reports `grep -c 'advisory:'` as the count of advisories. Measured before and after the repair on 2026-08-29: the count was 54 and is 30. The filename advisory, which the ruling was made for, has obeyed it since that day
- measure: [none] the deprecated-link advisory, first reading 2026-08-29 after the sweep: 43 retired pages are linked from live wiki pages, and 3 are named in a decided_by: field. A bare gate run is unchanged at 23.6 s and --lint costs 28.6 s, so the advisory is about five seconds. It means the per-page link pass is linear rather than the quadratic shape the rules 4 and 5 comment warns about - that shape was N recursive greps, this is one walk keeping FILENAME
- measure: [none] scripts/hook-selftest.ps1 reports caught 210, missed 0 in 3m15s, from 194 in 55 s this morning. Ten cases came from the --only contract and six from the feedback hook's new ritual half; the wall clock is almost entirely the one --only case that lets a suite run proceed
- decision: the session registered a temporary probe hook on MessageDisplay to measure whether that event can return hookSpecificOutput.additionalContext - the session understood it from the plan the owner approved, which makes the measurement step one of item 43. The probe writes nothing and is removed once the reading is written down
- measure: [none] a hook registered on MessageDisplay CANNOT speak to the session. A probe returning hookSpecificOutput with hookEventName MessageDisplay and additionalContext fired three times with final=true, confirmed by its own marker file, and no context reached the session on any of them. Measured 2026-08-29. It means a reply-silence counter cannot both live on that event and speak from it; it does not distinguish "the event cannot carry context" from "the field is named something else on this event", which the probe could not tell apart
- measure: [none] the full suite reports caught 194, missed 0 in 29m12s on 2026-08-29, against 34m08s at 178 cases on 2026-08-24 and about an hour at 682 files on 2026-08-26. Sixteen more cases and five fewer minutes, after the sweep took wiki/ from 762 pages to 523. It means archiving moved the term that grows, which three earlier proposals aimed constants at; it is NOT a controlled experiment - three readings on three days under different machine load
- measure: [none] the count case pinning --list against a real run fired for the first time and agrees at 194. The suite header has claimed since 2026-08-24 that the two are pinned against each other and nothing pinned them; the register that comment said was guarded was not guarded
- measure: [none] a PostToolUse hook registration added to .claude/settings.json mid-session took effect immediately, with no restart: both remind-the-smoke.ps1 and the new ritual branch of remind-the-feedback.ps1 spoke on the /retro that opened this ritual. It means the plan's stated ground - "unmeasured for this event, so take the strict case" - is now measured and the strict case was not needed; it does not generalise to other events, which stay unmeasured
- measure: [none] the session extract reports 18 owner turns, 88 session replies, 13 feedback marks and ZERO menus. Every ruling this session arrived in the owner's own words rather than through an AskUserQuestion selection. It means the session framed nothing for him to pick from; it does not mean the framing was better, only that it was his
- miss: [none] `grep -q` on the right of a pipeline under `set -o pipefail` inverts the test it is written to make: grep leaves on the first match, the upstream sed dies of SIGPIPE, and the PIPELINE reports that failure. Written into vault-archive.sh as the empty-selection refusal, it fired on every substring that DID match. Caught by the session's own case within a minute, and recorded here because the code comment is not a lesson page
- decision: the retro's menu step was answered in enumerated prose again rather than through AskUserQuestion - the session understood it from the record, which holds two interruptions of that menu on 2026-08-24 and an existing divergence page for exactly this. Recorded as a divergence rather than taken silently
- miss: [none] /pre-task answers PER ITEM OF THE PLAN, so an obligation the plan does not contain is invisible to it. This session gave it forty decisions and it returned fourteen corrections; the authority.md step was in none of the forty and in none of the fourteen, and the sweep then left 239 stale register rows. It means a plan touching the vault's own machinery must enumerate the brief's "what must not be broken" list as items, not only its own decisions
- decision: the retro list is worked by the session alone and the verdicts are brought as one block for the owner to accept or refuse - the owner said it, in his own words: "проставь вердикты сам и покажи, а я приму или откажу с уточнением"
- measure: [none] the retro list is 16 lines: 5 answered, 10 deferred, 1 could-not-close. Nine of the ten deferrals name a destination that does not exist yet - six new S3 items, two librarian writes and one existing item. It means today's rulings outran the sprint list; it does not mean they are lost, since each names where it is picked up
- measure: [none] the ratification list is 23 lines: 19 came from `decision:` marks the channel filed in the turn, 2 marks were the session's own understanding and are not attributed to him, and 4 the marks MISSED and the session found by reading the session's course - keeping the expensive --only case pair, tying log rotation to the sprint close, dropping the rules/ page for the case list, and the plan approval itself. It means the in-turn marking caught roughly five of every six rulings; it does not measure what neither the marks nor the reading caught
- miss: [none] approving a plan through ExitPlanMode is a ruling over every decision the plan carries - forty of them here - and nothing marks it. The channel records rulings made in prose and rulings made from a menu, and has no shape for a ruling made by approving a document
- measure: [none] the green `make smoke` of this session is still valid at the door of /handoff: all eleven modified tracked files are older than the run, and the two files written since - the retro and the feedback drain target - are under .superpowers/sdd/, which carries its own .gitignore. It means the gate's staleness condition was checked rather than assumed; it does not mean the run covered the retro file, which nothing tracks

## Anything else worth keeping

**The session used no menu at all.** Eighteen owner turns, eighty-eight session replies, zero
`AskUserQuestion` calls. Every ruling arrived in his own words. The retro's step 5 distinguishes
*he said it* from *he selected it* precisely because a menu shows him the wording; a session with no
menus has no lines of the second kind that the session itself framed, and the twelve *said* lines
above are all his sentences.

**The `--only` fix caught the session's own mistake within the hour it landed.** A pattern with an
alternation was passed to the suite while testing the advisory cases; the refusal built that morning
returned exit 2 and named the reason. Before today it would have printed `caught 1, missed 0` and
exited 0.

## Harness

- harness: a plan's ratification list carries a source per line, and the forty-item list this session put to the owner carried none until /pre-task caught it. The rule is `every-line-of-a-plans-ratification-list-carries-its-source`, owner-selected 2026-08-24
- harness: this session wrote every `measure:` line without the bracketed destination that `a-measure-line-names-its-destination-in-brackets-after-the-kind` requires. Corrected from the middle of the session onward; the earlier lines in this journal stand as written
- harness: every question the session puts to the owner carries context, an explanation of what the thing is, how it works today, what would be built, and a recommendation. The owner said it, in his own words, after a list of fourteen bare questions he could not answer - "стоит завести правило, чтобы ты всегда так задавал вопросы и подавал материал"
