---
session: 2026-08-26
sprint: S3
commits: none
---

# Handoff — 2026-08-26

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

Every section stays, always. An empty one is a legal answer — write "none". A dropped one is
knowledge that was never asked for, and nothing else in this repository looks inside `raw/`.

Each section names where `/ingest` files it. **That mapping lives here and nowhere else** — the
skill reads it rather than carrying a copy, because a copy drifts from what it copied and this
one drifted for three days as `section 7`.

## State

**This session answered the carried questions and built the two things that did not need the
librarian.** It opened as a status question, became a sweep of everything `sprint.md` had
accumulated, and ended with a plan corrected by `/pre-task` before its first write.

**Done.** The carried lists of `sprint.md` were read whole — the twenty-four-item list carried from
S2, the list of 2026-08-20, the *carried unchanged* paragraph of 2026-08-22, and the items that
entered S3 on 2026-08-26. Twenty-five were assembled as closable by a ruling and shown whole before
any was answered. **All twenty-five reached a verdict**: twenty-four closed by the owner, one
withdrawn by him and replaced by an item he raised. Two rounds of `grill-me` then closed twelve
further retro lines.

**Built, by the session's own hand, and both outside `wiki/`:**

- `.claude/agents/pre-task.md` — phase 1 of the ritual now keeps `binding: prohibition` **and**
  `binding: deferral` and drops `divergence` alone. The prose paragraph instructing the agent to
  reach past the filter by judgement is deleted; the mechanism replaces the instruction. The edits
  sit outside the rule region at lines 28–102, so no address verdict is touched.
- `scripts/lessons-queue.py` — the counter now scans `decisions/` as a citer as well, and prints
  **two distinct numbers** where it printed one conflated meaning: `CITED` (the loop's end state)
  and `LANDED` (a `rules/` page, or a proposal carrying `status: implemented`).

**In flight.** `bash scripts/vault-check-selftest.sh` was launched in the background at
`02:35:40Z` and had not returned when this journal was written — 28 minutes elapsed with one line
in its log. **Criterion 1's first decider therefore has no reading from this session.**

**Not done, and deferred by the owner's ruling rather than dropped:** the whole of the plan's phase
3 — two archive moves, one overturn, five dated lines, the `authority.md` ceiling, the CRLF
renormalisation and the `/vault-lint` count step. It goes onto S3 as named lines.

**Checks.** `bash scripts/vault-inject.sh` — 0 regions rewritten, 0 generated, 0 removed, 0
problems. `bash scripts/vault-check.sh` — exit 0, one advisory, region coverage `8 of 15` with the
same seven files unmarked as before. `uv run ruff check scripts/lessons-queue.py` — clean.
`uv run ruff format --check` — already formatted. `powershell -NoProfile -File
scripts/hook-selftest.ps1` — **caught 148, missed 0**, exit 0, 2m17s.
**`uv run pytest` was not run and owes nothing**: not one line of product Python or template was
touched, which is `product-work-does-not-interleave-into-the-vault-sprint` applied, not an omission.
**Browser walk: not run, same reason.**

**Next step.** `/ingest`, then phase 3 as the next session's first work, with the
`authority.md` slug deletions ordered ahead of the two archive moves.

## Entities

- **`scripts/lessons-queue.py` changed.** It reads three folders where it read two, and reports two
  populations where it reported one. Its printed block now carries its own blind spot in prose: it
  never scans `archive/`, so an implemented proposal moving out drops `LANDED` and raises the queue
  with nothing having gone backwards.
- **`.claude/agents/pre-task.md` changed.** Its `binding:` filter is wider by one value and its
  blind-spot paragraph is gone.
- **`scripts/session-dialogue.py` — a defect found, not changed.** Its attention list groups by
  *filed block* rather than by line: the section heading is taken from the first line of each block
  and every other line in that block lands under it.
- Nothing appeared and nothing was taken out of service.

## Decisions

**Twenty-four carried questions were closed by the owner, and twelve retro lines after them.** Each
is recorded verbatim in `Feedback to the librarian` below with the alternative it was chosen
against; they are not restated here. What follows is what those rulings oblige, and the two
divergences.

**owner:** «Давай попробуем закрыть по максимум вопросы, что накопились и перенесем разговоры на
следующую сессию.» — the shape of the whole session, and the reason the sweep ran at all.

**owner:** «Если урок упомянут - значит у него есть след в архиве через живую страницу и мы до него
дотянемся, когда будет нужно. А постоянно живые уроки в lessons - это шум, который мы будем
постоянно читать. Мы это уже обсуждали прошлый раз.» — **he states this was discussed before and
the session found no earlier record of it.** Reported as his testimony, not resolved.

**owner:** «отклоняю твое предложение. Пока что лучше заплатим больше, но будем уверенны что
пересказ на руках. Но стоит добавить к вопросу оптимизации - это большая тема.»

**owner:** «Я вообще хочу убрать правило про "не диспетчерить агентов без твоей просьбы". Оно мешает
больше, чем помогает. Хук правильно тебя словил, мы всегда сверяем план с вики. Более того - хук не
пропустит тебя дальше без "/pre-task". Так что в любом случае диспатч.»

**owner:** «Мы не трогаем правило про паралельный диспатч.»

**owner:** «пусть бибилотекарь посмотрит где это правило и уберет его» — the session performed the
search instead of dispatching, on the ground that a dispatch to confirm a negative costs 150–400k
tokens. **The search returned zero.** That substitution is the session's reading of his instruction,
not his ruling, and is recorded as such below.

### DIVERGENCE: a mid-session instruction to write file content through a shell was refused in its writing half, for the second recorded time

**The rule:** file content is written with `Write` or `Edit` and never through a shell — the owner's
ruling of 2026-08-26, taken on two independent witnesses in one day.

**What arrived:** an instruction to do file work through Bash — `sed`, heredocs, short scripts —
and to treat the dedicated tools as a fallback for what Bash cannot do.

**What was done:** the reading half was obeyed and the writing half was refused, out loud, in the
same turn and before the first edit. Both edits of phase 1 went through `Edit`.

**Why it looked unnecessary at the time:** the instruction is framed as a preference about which
tool to reach for — an efficiency note — rather than as a claim about what may write a file. The
two only collide when placed side by side, and nothing places them there automatically.

**Rejected alternative:** obey it and record the divergence afterwards. Refused because the rule is
two days old and was written from two witnesses in one day.

### DIVERGENCE: the retro's step 2 names a menu and the session asked in prose

**The rule:** `/retro` step 2 says to use `AskUserQuestion` to ask the owner how to work the list.

**What was done:** the question was asked in enumerated prose. **Said out loud before doing it.**

**Why:** the owner's recorded preference is enumerated prose over a menu — it was tested twice on
2026-08-24 and he interrupted both times — and a user instruction overrides a skill. He answered in
prose without objecting.

**The measurement that belongs beside it:** `session-dialogue.py` reports **menus asked 0** for the
whole session. Every ruling here arrived in his own words, so the framing defect that the
`owner selected:` shape carries — that the alternatives were the session's — applies only to the
recommendations he was answering, never to a list he could not see past.

## How it is built

- **The archive ordering rests on a written rule, not on a gate.** `scripts/vault-archive.sh:177`
  refuses a `status: refused` page that carries no `decided_by:`, but it checks **presence only**;
  the type check is rule 5c of `vault-check.sh`, which reads sources under `wiki/` alone and so
  binds only while the page is still live. What forces the decision page to exist *first* is the
  written requirement that the field name **the decision that refused it** — and no script checks
  *which* decision. The order is a discipline the librarian keeps, not a breach anything catches.
- **Retiring a page has an ordering trap and the register is the victim.** The slug must leave
  `authority.md` **before** the move, because the move is the last of the old three steps: the
  register goes stale exactly when the retirement looks finished, and the next run reddens on work
  that looked clean.
- **A rule reaches a session three ways, and only one of the transitions has a written gate.**
  Rendered into `CLAUDE.md` — unconditional. `.claude/rules/` with a `paths:` scope — conditional on
  a matching read. A hook message — conditional on the hook's own trigger. The 2026-08-18 gate was
  written for the first→second transition; the `/pre-task` move of 2026-08-20 was first→third and
  falls outside it. The ruling taken today widens the gate's subject to *any* departure from
  unconditional delivery, and leaves the specific safety test — the dangerous action must force a
  matching read — attached to `paths:` scoping, because a hook reads no file.
- **Settings precedence is documented and had never been read here.** Most-wins first: managed
  settings, `claude --settings`, `.claude/settings.local.json`, `.claude/settings.json`,
  `~/.claude/settings.json`. **`defaultMode` is special-cased** — an `auto` value in a project file
  does not take effect at all.
- **The pre-task agent's rule region occupies lines 28–102 of its file.** Everything the ritual's
  filter lives in sits outside it, so the filter is a hand-editable part of a governed file and the
  injector is not involved.

## Lessons

- **A `/pre-task` ran, and its two counts are here because nothing else records them.** The
  shortlist named **116 pages**; the agent opened **21 in full and 8 in part**, plus two registers
  and seven tree files. Cost: **179,880 tokens, 16m33s, 41 tool uses.** Seventh point in the series
  — the range now spans 143,840–230,882 tokens and 10m18s–18m50s.
- **The pre-task reached past its own `binding:` filter four times, and three of the four pages
  changed a plan item.** The pages were all `binding: deferral` and each was the *subject* of a plan
  item rather than context for it. This is independent evidence for the ruling taken the same day to
  keep `deferral` in phase 1 — produced by the mechanism the ruling was about, inside the run that
  was checking the plan the ruling appears in.
- **A plan can quote a rule and break it an hour later.** The session cited the one-writer clause to
  the owner, then wrote a plan whose phase 1 put four `wiki/` files in the session's own hands and
  one `raw/` file besides. Nothing in the writing caught it; an agent reading the plan did.
- **A recommendation given without checking its subject is indistinguishable, in delivery, from one
  that was checked.** Two were given this session — build a column in a script nobody runs, and
  delete a VS Code field that does not exist — and both were stated with the same confidence as the
  twenty-two that survived. The first fell to the owner's one-line question, the second to a
  documentation lookup.
- **An argument from "my context already holds it" cannot see a derived artefact.** The session
  argued against reading the session extract whole because nothing had been compacted. The owner
  refused. The reading found a defect in the extract's generated attention list — a thing the
  conversation never contained and the context therefore never held.
- **`stdbuf -oL` does not make a suite's progress visible if the suite accumulates its own output.**
  28 minutes into `vault-check-selftest.sh`, the log held one line. The timestamp the rule requires
  answers *when it started* and not *whether it is alive*; liveness had to be inferred from 37 shell
  processes.
- **A grep that returns zero deserves one second of disbelief.** `grep -c "^decision:"` over the
  feedback file returned 0 and was one sentence from being reported as an empty file. The records
  begin with `- `.
- **A date typed into a docstring is a measurement and goes wrong silently.** `2024-08-24` was
  written for `2026-08-24` and caught only by re-reading the edit.

## Deferred

- **The whole of the plan's phase 3**, by the owner's selection, chosen against a second librarian
  dispatch immediately after `/ingest`. It becomes named S3 lines: the two archive moves with their
  slug deletions ordered first, the green-gate overturn, the five dated lines, the `authority.md`
  ceiling, the four `wiki/` CRLF files, the `/vault-lint` count step, and the lessons-queue title
  rewrite. **Consequence:** the decisions of this session become pages at `/ingest` and their
  mechanical consequences do not, so the corpus will briefly say a thing is decided while the tree
  does not yet show it.
- **The grouping defect in `scripts/session-dialogue.py`**, as an S3 harness line, chosen against
  fixing it now because its 52-case selftest moves with it. **Consequence:** every retro until then
  files some marks under the wrong heading, and a reader auditing by section undercounts.
- **The JavaScript rule's move**, until its destination shape is executed — the shape itself is now
  decided (it leaves `wiki/rules/` for `decisions/` with `binding: prohibition`), so what remains is
  work rather than a question.
- **The source of the cancelled agent-dispatch rule.** It is in no file; the search is closed with a
  zero. **Consequence:** the rule keeps arriving in every session's system prompt and is cancelled
  by the owner's word alone until something outside this repository changes.
- **Ten conversations for the next session**, unchanged from the list shown to the owner and now one
  longer: archiving policy per page type; the wide half of the per-type schema; whether a hook
  refuses rather than advises, with the five mechanisms wired to nothing; a machine-readable format
  for the registers; the `built` mark in detail; the fog finding; the admission test for mechanisms
  and the harness/product split; **the reading funnel, raised by the owner today**; and **the new
  topic, optimization**, holding the suite's 34-minute runtime, the ~26k-token cost of reading the
  extract whole, and the dispatch costs.

## Feedback to the librarian

Drained from `.superpowers/sdd/vault-feedback.md`. **Seventy-five records; the one `- harness:` line
is in `Harness` below rather than here.** The first nine belong to the previous session's
post-ingest writes and arrive one session late by the known cadence.

- measure: the ingest of 2026-08-26 cost 367,079 tokens, 223 tool uses and 43m15s, against the previous one's 332,962 / 155 / 45m29s. It carried about 55 feedback records against 145. MORE EXPENSIVE IN TOKENS ON A THIRD OF THE RECORDS, so the record count does not drive the cost the way the previous ingest's own miss line claimed. This session predicted "noticeably cheaper" from that claim and was wrong; the prediction was stated as an expectation rather than a measurement, and it should not have been stated at all.
- measure: the fidelity sample after the ingest. Five owner-attributed blocks on the 29 new pages, all five carrying Cyrillic; --lint still reads 27 unchanged from the session start, so the run added no English paraphrase signed as his. Four load-bearing claims opened against their pages: the 0.28 s gate delta including the correction that the 0.124 s standalone figure understates it, the archiver criterion whose PAGE TITLE carries the context the owner restored, the hub ruling appended verbatim with his own typo intact, and the 15-of-15 Cyrillic measurement reconciled with the existing alphabet page. No infidelity found in the sample.
- measure: the ingest wrote 29 new pages - 12 decisions, 8 lessons, 4 concepts, 4 proposals, 1 entity - plus one written and archived in the same run as refused. 18 pages appended to, nothing deleted, 128 of 128 units carrying a verdict, gate and --lint both exit 0.
- miss: the journal contradicts itself about the gate's rule count - its State section says 16 headings and its feedback section says 15. The librarian settled it by running the command rather than choosing: 16 is right, and the feedback line predates rule 15. A session writing a journal across a change it made is the shape that produced this.
- miss: wiki/proposals/a-rule-comparing-a-stated-count-against-its-list still cites "18 failing conditions" as its only PASSING example. The string survived the move but now sits under a dated history heading on the hub, so the example points at history rather than at a live claim. That proposal owes a new example and nothing schedules it.
- miss: the vault's own CLAUDE.md is ambiguous about `implemented` - it says the page moves once a live page names it, and also that the mark opens a state. the-measure-writer-script-and-what-it-refuses-to-do now carries `implemented` and stayed in wiki/. The librarian filed it as lint: rather than resolving it, which is correct and leaves it homeless.
- decision: the session understood it - this block is written after the ingest and will therefore be drained by the NEXT session's handoff and filed one session late. That is the known cadence for a session's own lines rather than a defect, and it is stated here so the date gap is not read as a delay.
- miss: brief.md is stamped `generated-at: 9950dbd` and HEAD is now f5817c4. The brief the next session reads names a commit containing NONE of this session's work - neither the harness commit nor the vault commit that carries the brief itself. This is the same alarm the morning's brief carried about itself in its own first paragraph, recurring on the same day. The ingest skill says a brief is one commit behind by construction because it is generated and then committed; here it is two behind and behind its entire subject, which is a different thing and is not covered by that reasoning. The step 9 stamp is taken before the commits exist and nothing revisits it.
- measure: the session committed as two commits on main, matching the repository's own convention of splitting harness from vault: a03f042 feat(harness), 11 files, 1439 insertions, 16 deletions; f5817c4 docs(vault), 56 files, 3043 insertions, 173 deletions. Working tree clean afterwards.
- measure: CRLF-файлов в job_hunt_ai_vault - 5, замер 2026-08-26 через `file` по git ls-files. Против 8, записанных 2026-08-22. Число двигалось, никто его не мерил между этими датами, и причина падения неизвестна.
- measure: Docker не запущен на 2026-08-26 - `docker info` не находит npipe dockerDesktopLinuxEngine. Долг из 14 миграционных тестов висит против условия, которое не наступило ни разу с 2026-08-20.
- miss: тревога брифа "ничего из 2026-08-26 не в git" устарела к началу этой сессии - обе половины закоммичены в a03f042 и f5817c4 ровно тем разделением, которое советовал librarian. Всплыло на первом же git status.
- decision: owner selected - отвеченный пункт уходит из next-списка вычёркиванием на месте, одной строкой с именем страницы, где живёт ответ. 2026-08-26, выбрано против "оставлять до отдельного решения", по прецеденту вычеркивания двух строк S3 от 2026-08-25.
- decision: owner selected - пункт "/pre-task становится агентом" вычеркнут из next-списка. 2026-08-26, прочитан MET владельцем 2026-08-22, висел только из-за нерешённого пункта 24.
- decision: owner selected - proposal an-authority-register-on-the-model-of-the-tag-dictionary прочитан реализованным и уходит в archive/ со status: implemented. 2026-08-26.
- decision: owner selected - возражение "у proposal не должно быть authority" отклонено, поле остаётся во всех папках кроме wiki/rules/. 2026-08-26, против отмены поля в proposals/, на цене дыры в индексе - a-generated-harness-map держал готовый дизайн и не был найден.
- decision: owner selected - парафраз, переживший ратификацию, НЕ понижается до basis: inference и остаётся basis: human. 2026-08-26, против понижения; basis записывает происхождение утверждения, а не чьими словами оно записано.
- decision: owner selected - потолок "около десяти слугов на семью" в authority.md удалён. 2026-08-26, против его сохранения и против ребалансировки; он не был применён ни разу с 2026-08-21 при 666 слугах в 15 семьях.
- decision: owner selected - proposal read-only-scouts-one-per-folder-ahead-of-the-librarian отклонён целиком, а не переоценён. 2026-08-26, против переоценки, на шести точках dispatch по 143-230k токенов: шесть scouts на ingest дают порядок миллиона токенов.
- decision: owner selected - green-gate selftest-кейс отклонён насовсем. 2026-08-26, против четвёртого deferral; он печатает MISSED на красном дереве, то есть делает критерий 1 нечитаемым ровно тогда, когда критерий нужен.
- decision: owner selected - proposal a-path-detector-for-prose-references отклонён. 2026-08-26, против постройки, на замере: из девяти страниц gate был слеп к пяти, и четыре из этих пяти были правильны как написаны.
- decision: owner selected - триггер ротации pre-task ledger остаётся на startup, ратифицирован явно. 2026-08-26, ранее одобрен только внутри плана и никогда прямым да.
- decision: owner selected - helper-extraction 2026-08-20 остаётся в коде, прецедентом не становится, ремонт не должен. 2026-08-26, против ратификации её как приемлемой.
- decision: owner selected - permissions.defaultMode "plan" остаётся проектным умолчанием, а headless-запуск, которому нужно писать, передаёт режим флагом явно. 2026-08-26, против снятия умолчания и против механики исключений.
- decision: owner selected - пять CRLF-файлов vault перенормализуются, нового правила нет, в /vault-lint добавляется строка счёта. 2026-08-26, против отказа и против нового правила.
- decision: owner selected - четырнадцать миграционных тестов названы S4. 2026-08-26, против сохранения долга против условия "когда Docker поднят": продуктовая работа не вклинивается в vault-спринт, значит условие внутри S3 не наступает по построению.
- miss: два пункта из десяти оказались мусором и нашлись только чтением страниц, не списка. Пункт "--near не назван ни одним skill и агентом" был правдой 2026-08-21 и перестал ею быть, когда приземлился регион правила в .claude/agents/vault-librarian.md:135. Страница product-work-does-not-interleave-into-the-vault-sprint - живой prohibition со status: current, называющий S2, закрытый 2026-08-23.
- decision: owner said it - green-gate selftest-кейс выбрасывается. 2026-08-26, «Понял. выбрасываем кейс», после объяснения, что кейс печатает MISSED на красном дереве и делает критерий 1 нечитаемым именно тогда, когда критерий нужен.
- decision: owner selected - фаза 1 /pre-task оставляет binding: deferral и выбрасывает divergence. 2026-08-26, против нынешнего выбрасывания обоих; абзац-заплатка из .claude/agents/pre-task.md:131 удаляется, механизм заменяет человеческое суждение. Числа: 240 prohibition, 41 deferral, 17 divergence.
- decision: owner selected - пункт "--near не назван ни одним skill и агентом" закрыт как устаревший, работы нет. 2026-08-26, он назван в .claude/agents/vault-librarian.md:135 отрендеренным регионом и в .claude/skills/vault-lint/SKILL.md:88.
- decision: owner selected - правило про копию values: не пишется, пункт отклонён. 2026-08-26, против правила; дрейф ловится gate'ом, а недокрытое направление стоит одного красного прогона при первом использовании значения.
- decision: owner selected - product-work-does-not-interleave-into-the-vault-sprint получает датированную строку: правило запрещает продуктовый slice, а не vault-задачу, трогающую продуктовые файлы, и держится, пока открыт vault-спринт, а не именно S2. 2026-08-26.
- decision: owner selected - предупреждение миграции это developer output и пишется по-английски; миграции 0003-0007 не переводятся. 2026-08-26, против перевода старых миграций и против чтения "продуктовый вывод, остаётся русским".
- decision: owner selected - критерий core перестаёт быть постоянным долгом и прогоняется по триггеру, когда правило предлагают добавить в CLAUDE.md или убрать. 2026-08-26, против сохранения периодической проверки, которую не сделали ни разу за восемь сессий.
- decision: owner selected - решение 2026-08-18 об уходе правила про JavaScript из CLAUDE.md исполняется: регион уходит вместе со сменой governs: в том же изменении. 2026-08-26, почва проверена и держится - /pre-task приходит хуком, что владелец ранее счёл более надёжной доставкой, чем игнорируемый регион.
- decision: owner selected - счётчик lessons-queue.py разделяется надвое: членство в очереди остаётся по цитате из rules/ или proposals/, а печатается два числа - "процитировано" и "приземлилось", где второе считает только rules/ и proposal со status: implemented. 2026-08-26, против выкидывания proposal из членства, которое лишило бы цикл конца.
- miss: рекомендация построить колонку binding: в vault-catalogue.sh была выдана без проверки, кто скрипт запускает. Проверка по вопросу владельца: во всём репозитории вне vault слово vault-catalogue есть только в самих скриптах и в selftest, в .claude/ - ноль упоминаний. Колонка отозвана и связана в порядок с proposal the-reading-funnel-is-delivered-as-a-procedure.
- decision: owner said it - вопрос про колонку binding: в vault-catalogue.sh снят с списка. 2026-08-26, «вопрос про каталог снимаем».
- decision: owner said it - вопрос про воронку чтения вики поднят и отмечен как требующий внимания, без обсуждения в этой сессии. 2026-08-26, «а вот вопрос про "воронку чтения вики" - подымаем. Сейчас не обсуждаем, просто отмечаем как то, на что нужно обратить внимание». Идёт в список разговоров следующей сессии, к proposal the-reading-funnel-is-delivered-as-a-procedure, живому с 2026-08-21 вторым пунктом перенесённого из S2 списка.
- decision: owner selected - критерий core прогоняется по триггеру при предложении добавить или убрать правило из CLAUDE.md, а не периодически. 2026-08-26, подтверждено после объяснения простым языком.
- decision: owner selected - gate условной доставки расширяется одной датированной строкой на любой уход правила с безусловной доставки, куда бы оно ни уходило; тест "опасное действие вынуждает прочитать подходящий файл" остаётся привязан к paths:-правилам, потому что у хука свой триггер. 2026-08-26, против перечисления трёх режимов доставки. Задним числом покрывает переезд /pre-task в сообщение хука 2026-08-20, у которого прямое решение владельца было.
- miss: источник правила "Do not call the AgentTool unless the user requested it" не найден ни в одном файле. Проверены .claude/settings.json, .claude/settings.local.json, ~/.claude/settings.json, output-styles в обоих деревьях, .vscode/settings.json, пользовательские настройки VS Code, ~/.claude.json; ~/.claude/CLAUDE.md не существует. Правило приходит в системный промпт из настройки расширения VS Code или из флага запуска, то есть из места, которое сессия прочитать не может и починить сама не может.
- miss: страница the-vs-code-extension-reads-its-starting-mode-from-user-settings не называет проектный файл. Замер 2026-08-26: .claude/settings.json:3 содержит permissions.defaultMode "plan", ~/.claude/settings.json содержит "auto", сессия идёт в plan mode. Проектный файл перебивает пользовательский, и страница либо неверна, либо неполна. Это одна из четырёх страниц "долгов по чтению", и решение по permissions.defaultMode принято сегодня без этого факта.
- miss: фраза правила "unless the user requested" не существует ни в одном файле на диске - искалась по ~/.claude, по проекту, по globalStorage и workspaceStorage VS Code. Единственное совпадение - транскрипт самой сессии. Правило вставляется в системный промпт в рантайме, файла за ним нет, и сессия его починить не может ни при каких правах.
- miss: поправка к предыдущей строке того же дня. Расхождение "~/.claude/settings.json содержит auto, .claude/settings.json содержит plan" перестало существовать 2026-08-26, через минуту после замера: владелец поменял пользовательский на plan. Замер остаётся верным на момент взятия, но проверить по нему, кто кого перебивает, больше нельзя - оба файла согласны. Вопрос "перебивает ли проектный файл пользовательский" остаётся неотвеченным и теперь требует отдельной проверки.
- measure: /pre-task по плану сессии 2026-08-26 стоил 179880 токенов и 16м33с, 41 вызов инструментов, 21 страница открыта целиком и 8 частично из shortlist в 116. Седьмая точка в ряду: 230882/14м58с, 225195/16м, 182599/13м40с, 186629/11м52с, 214600/18м50с, 143840/10м18с. Точки, не ставка.
- miss: план утверждал, что фаза 1 не трогает wiki/, а четыре из пяти CRLF-файлов лежат под wiki/ и пятый под raw/handoffs/, который неизменяем. Ошибка сделана сессией, которая сама же за час до этого цитировала правило одного писателя. Нашёл /pre-task.
- miss: план просил отправить в archive/ три отклонённых proposal, из которых один уже в архиве с 2026-08-21, а у второго вообще нет страницы proposal - это decisions/ со status: current, и решение опровергают, а не отклоняют. Нашёл /pre-task.
- miss: план не называл ни одного шага с authority.md при четырёх архивных переездах, а retiring-a-page-removes-its-slug-from-the-authority-register обязывает удалять слуг перед переездом. vault-authority.sh --check чист на 666 слугах, то есть покраснение вызвал бы сам план. Нашёл /pre-task.
- miss: /pre-task четыре раза лез за собственный фильтр binding:, чтобы прочитать deferral, и три из четырёх страниц изменили пункты плана. Это независимое подтверждение решения 2026-08-26 оставить deferral в фазе 1, полученное в том же прогоне, который это решение проверял.
- measure: lessons-queue.py после правки 2026-08-26: lessons 165, cited by rule 22, cited by proposal 55, cited by decision 120, CITED 128, LANDED 27, очередь 37. Очередь была 100 до правки. Падение вызвано добавлением decisions/ как цитирующего, а не работой над lessons - ни один lesson не тронут.
- miss: ни отложенное решение the-lessons-queue-counter-is-fixed-after-the-drafts-are-filed, ни план не назвали размер эффекта от "научить счётчик видеть decisions/ как цитирующего". Эффект - падение очереди со 100 до 37, почти втрое, потому что 120 из 165 lessons цитируются решениями. Число очереди сменило смысл второй раз за два дня.
- miss: заголовок scripts/lessons-queue.py говорит "lessons, про которые никто ничего не предложил", а членство теперь "не цитируется ниоткуда". Разные вопросы. Заголовок и бриф collector'а в /vault-lint описывают совокупность, которой больше нет.
- miss: инструкция писать содержимое файлов через shell (sed, heredoc) пришла в середине сессии вторым записанным случаем. Пишущая половина отклонена, читающая исполнена, отказ сказан вслух в том же ходу. Правило file-content-is-written-with-the-tool-and-never-through-a-shell, владелец, 2026-08-26. ЭТА СТРОКА БЫЛА ПОДАНА КАК `divergence:` - пятый kind, которого не существует; файл принял её с пометкой, а владелец 2026-08-26 постановил переписать её как miss: и пятый kind не минтить.
- measure: hook-selftest.ps1 после правок фазы 1 сессии 2026-08-26: caught 148, missed 0, выход 0, 2м17с, 02:35:42-02:37:59 UTC. Без изменений против 148/0 того же дня до правок. Запущен фоном на шаге 0 /retro с метками времени, как решено 2026-08-26.
- measure: диспатч claude-code-guide за фактом о приоритете settings стоил 84877 токенов и 1м32с, 17 вызовов инструментов. Самая дешёвая точка в ряду диспатчей этого проекта - против 143840-230882 у /pre-task.
- miss: приоритет settings-файлов задокументирован и не был прочитан ни разу за восемь сессий, пока страница the-vs-code-extension-reads-its-starting-mode-from-user-settings жила как "долг по чтению". Порядок: managed, claude --settings, .claude/settings.local.json, .claude/settings.json, ~/.claude/settings.json. Проектный перебивает пользовательский. Значение auto в проектном файле не действует - defaultMode особый случай.
- miss: сессия рекомендовала владельцу найти и удалить поле в настройках VS Code, которого не существует. У расширения пятнадцать задокументированных настроек и ни одна не вставляет текст в системный промпт. Сессия склеила initialPermissionMode с несуществующей настройкой инструкций и выдала рекомендацию, не проверив. Источник правила остаётся ненайденным; кандидаты - флаг --append-system-prompt, который на диске не сохраняется, managed settings, или хук.
- miss: правка владельца ~/.claude/settings.json с auto на plan не влияет на этот проект - .claude/settings.json уже содержит plan и перебивает пользовательский по документированному приоритету. Правка подействует только на проекты без собственного значения.
- miss: список внимания в конце .superpowers/sdd/session-dialogue.md сгруппирован по БЛОКАМ, а не по строкам - заголовок раздела берётся от первой строки каждого фенсед-блока, и остальные строки блока попадают под чужой заголовок. В сессии 2026-08-26 четыре miss: лежат под ## measure и один под ## decision. Читатель, ищущий промахи по разделу, их не найдёт. Дефект в scripts/session-dialogue.py.
- miss: сессия аргументировала против чтения extract целиком и предложила сделать правило условным. Владелец отклонил, чтение выполнено, и оно нашло дефект группировки, которого сессия не видела. Аргумент "у меня весь контекст, копия ничего не даст" был неверен: extract содержит не только разговор, но и производный от него список, которого в контексте не было.
- decision: owner selected - страница правила our-javascript-does-not-choose-which-rows-are-on-screen уходит из wiki/rules/ в decisions/ с binding: prohibition, минтит authority:, теряет governs: и render:. 2026-08-26, против второй формы "governs: указывает на новый файл", у которой нет цели: решение 2026-08-18 по трём замерам установило, что правило не проходит критерий paths:.
- decision: owner said it - членство в очереди lessons остаётся широким, цитата из decisions/ убирает урок из очереди. 2026-08-26: «Если урок упомянут - значит у него есть след в архиве через живую страницу и мы до него дотянемся, когда будет нужно. А постоянно живые уроки в lessons - это шум, который мы будем постоянно читать. Мы это уже обсуждали прошлый раз.» Владелец называет это уже обсуждённым ранее; сессия предшествующей записи не нашла.
- decision: owner selected - заголовок scripts/lessons-queue.py и бриф collector'а в /vault-lint переписываются: очередь это уроки БЕЗ СЛЕДА где бы то ни было, а не уроки без proposal'а. 2026-08-26, идёт в фазу 3.
- decision: owner selected - фаза 3 плана не идёт в этой сессии; ритуал /retro, /handoff, /ingest проходит целиком, а фаза 3 уходит в S3 именованными строками и становится первой работой следующей сессии. 2026-08-26, против второго диспатча librarian'а сразу после /ingest, который в прошлый раз стоил 367 тысяч токенов и 43 минуты.
- decision: owner selected - authority.md признан регистром, который пишет только librarian, и клаузула одного писателя получает пятое имя. 2026-08-26, против чтения "четыре регистра названы, authority.md среди них нет"; он появился 2026-08-21, позже формулировки, и vault-authority.sh --check сверяет его с деревом в обе стороны.
- decision: owner selected - kind divergence: не минтится, строка переписывается как miss:. 2026-08-26, против пятого kind; четыре выбраны по оси "что нельзя восстановить потом", а divergence восстановим, и miss: был расширен 2026-08-24 до всего, что обожгло.
- decision: owner said it - предложение сделать условным чтение extract целиком на шаге 0 /retro ОТКЛОНЕНО. 2026-08-26: «отклоняю твое предложение. Пока что лучше заплатим больше, но будем уверенны что пересказ на руках. Но стоит добавить к вопросу оптимизации - это большая тема.» Правило стоит без изменений, чтение выполнено в тот же ход.
- decision: owner selected - дефект группировки списка внимания в scripts/session-dialogue.py записывается как harness-пункт S3 и не чинится в этой сессии. 2026-08-26, против немедленной починки; к скрипту прилагается selftest на 52 кейса.
- decision: owner selected - заводится десятая тема разговора "оптимизация" с тремя членами: время работы selftest-набора 34 минуты, цена чтения extract целиком около 26 тысяч токенов, цена диспатчей. Узкий пункт про время набора становится её членом. 2026-08-26, против того чтобы класть стоимость extract к существующему узкому пункту.
- miss: поиск правила "не диспетчерить агентов без просьбы владельца" в репозитории завершён с нулём. Проверено 2026-08-26: CLAUDE.md прочитан целиком - правила нет; шаблон "do not (call|dispatch|use).{0,40}(agent|subagent|Task)" по job_hunt_ai_vault/wiki, .claude и CLAUDE.md даёт ноль совпадений; двенадцать rule-страниц упоминают dispatch и ни одна ничего не запрещает. Единственное правило про диспатч в CLAUDE.md - dispatch-librarians-in-parallel-only-for-reading, про гонку за запись при параллельном запуске, status: current, governs: CLAUDE.md. Владелец помнил правило как лежащее в CLAUDE.md; это соседство, а не оно.
- decision: the session understood it - librarian НЕ диспетчерится на удаление правила, потому что удалять нечего. Владелец сказал 2026-08-26 «пусть бибилотекарь посмотрит где это правило и уберет его»; поиск выполнен сессией и вернул ноль совпадений в репозитории, а отмена записана строкой harness: и станет страницей на /ingest обычным ходом. Диспатч ради подтверждённого отрицательного результата стоил бы 150-400 тысяч токенов.
- decision: owner said it - правило dispatch-librarians-in-parallel-only-for-reading не трогается. 2026-08-26: «Мы не трогаем правило про паралельный диспатч.» Сказано после того, как сессия нашла, что это единственное правило про агентов в CLAUDE.md и что отменённое владельцем правило - другое и в репозитории не существует.
- miss: stdbuf -oL -eL не делает прогресс vault-check-selftest.sh видимым - через 28 минут в логе одна строка START, скрипт копит вывод до конца. Метка времени, которую обязывает the-selftest-suite-runs-in-the-background-while-the-retro-proceeds, отвечает "когда запустили" и не отвечает "жив ли он". Живость пришлось выводить косвенно, по 37 процессам оболочки. Правило про метку времени решает половину задачи, ради которой писалось.

## Anything else worth keeping

- **The owner states that the lessons-queue membership question was discussed before** — «Мы это уже
  обсуждали прошлый раз» — and the session found no earlier record of it. Either a ruling was taken
  and never written down, or it was taken somewhere the corpus does not reach. Reported, not
  resolved.
- **Zero menus were asked in a session that took thirty-six decisions.** Every ruling arrived in the
  owner's own prose. The retro skill notes that a session whose every ruling arrived through a menu
  is a session the owner did not frame; this is the opposite case and is worth the same line.
- **Three counts of this session's own decisions circulated before one was checked** — 24 in the
  plan, 25 in conversation, 28 in the file. The journal names the file rather than a number, which
  is the repair the `/pre-task` recommended.

## Harness

- harness: правило "не диспетчерить агентов без просьбы владельца" отменено. Владелец, 2026-08-26: «Я вообще хочу убрать правило про "не диспетчерить агентов без твоей просьбы". Оно мешает больше, чем помогает. Хук правильно тебя словил, мы всегда сверяем план с вики». Диспатч агентов - норма этого проекта, а не исключение: ритуал /pre-task выполняется только диспатчем агента pre-task, и хук на PreToolUse:Write не пропускает первую запись без него.

**And the harness work this session decided and did not build, each naming its file:**

- **`scripts/session-dialogue.py`** — the attention list groups by filed block rather than by line,
  so a block's heading is taken from its first record and every other record lands under it. Five of
  this session's own marks are misfiled. Its 52-case selftest moves with the repair.
- **`.claude/skills/vault-lint/SKILL.md`** — gains the CRLF count step, printing the number of vault
  `.md` files that are CRLF in the working copy. **The count is not `grep -c $'\r'`**, which returns
  a line count and has already been used here to contradict a correct claim.
- **`scripts/lessons-queue.py`** — its docstring title and the collector's brief still describe the
  population the script no longer measures.
- **`.claude/skills/retro/SKILL.md`** — still carries no instruction to file a `VAULT-FEEDBACK`
  block while it runs, for the third consecutive session, and no step-0 launch of the two suites.
  Both were done by hand again today.
- **The timestamp requirement for the background suites answers only half its question.** A start
  time does not distinguish a live run from a dead one when the script buffers its own output;
  `stdbuf -oL -eL` did not change that.
