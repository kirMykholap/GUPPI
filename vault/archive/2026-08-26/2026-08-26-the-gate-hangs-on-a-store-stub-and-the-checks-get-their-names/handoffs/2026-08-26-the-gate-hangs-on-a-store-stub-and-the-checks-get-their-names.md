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

**THIS IS THE SECOND JOURNAL OF 2026-08-26 AND IT IS COMPILED AFTER THE FIRST.** The other is
`2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.
Two uncompiled sources carry the same date, so the ingest's *oldest first* tie-break has nothing
to break the tie with; the order is stated here instead. **It exists because `/handoff` stands
before `/ingest` in the ritual and the conversation does not stop when the journal is written** —
everything below was decided after the first journal was already immutable.

## State

**A gate that hung for an hour was diagnosed, the fix landed, and the owner named the check
system.**

**Done.**

- **`scripts/vault-check.sh` — rule 15's interpreter probe repaired.** It chose the first candidate
  that *existed* rather than the first that *worked*, and on this machine `python3` resolves to the
  Microsoft Store stub, which neither answers nor exits. A candidate resolving under `WindowsApps`
  is now skipped **without being run**. Gate afterwards: **21.5 s, exit 0, `VAULT-CHECK: ok`.**
- **`.claude/agents/vault-librarian.md` — the gate instruction repaired.** It said *"After any
  write, run `bash scripts/vault-check.sh`"* and described something nobody has ever done. It now
  says once at the end of a writing pass, injector first, with the discrepancy written beside it.
- **The orphaned suite processes were killed**, which took `taskkill //PID <winpid> //F //T` after
  `TaskStop` and `kill -9` both failed to reach them.

**Not done, and named as the next session's first work by the owner:** the smoke runner, the single
entry point, and the proposal page that settles who runs which check and when.

**Ordered for today by the owner:** `raw/` is to be cleaned. See `Decisions`.

**Checks.** `bash scripts/vault-check.sh` — **exit 0**, `VAULT-CHECK: ok`, 20.45 s after the last
edit, region coverage `8 of 15` with the same seven files unmarked. `bash -n scripts/vault-check.sh`
— clean. **`vault-check-selftest.sh` was killed unfinished at 56 minutes** and has no reading.
`hook-selftest.ps1` — caught 148, missed 0, exit 0, 2m17s, from earlier in the day. `uv run pytest`
not run and owes nothing: no product Python or template was touched.

## Entities

- **`scripts/vault-check.sh` changed.** Rule 15's interpreter probe now refuses a `WindowsApps`
  candidate unrun. The order of candidates is unchanged; behaviour on a machine without the stub is
  identical.
- **`.claude/agents/vault-librarian.md` changed.** Its gate instruction now matches the ritual.
- **`python3` on this machine is not an interpreter.** It is
  `AppData/Local/Microsoft/WindowsApps/python3` → `PythonSoftwareFoundation.PythonManager`, and it
  hangs rather than failing. The working interpreter is `python` → `/c/Python314/python`.
- **`make` exists here** — GNU Make 4.4.1 at `/c/ProgramData/chocolatey/bin/make`, via chocolatey.
- **`scripts/vault-archive.sh` — its handoff cargo is still untouched.** The script accepts
  `handoffs` as one of five kinds and has never been run on one.

## Decisions

### The three checks are named apart, and "gate" keeps the meaning it had

**owner selected**, against calling the fast selftest a gate:

- **gate** — `bash scripts/vault-check.sh` alone. It reads the **live corpus**, builds no sandbox
  and breaks nothing. Sixteen rules. 21.5 s on a 682-file corpus.
- **smoke** — a fast run over what the session actually touched. **It does not exist and must be
  built.**
- **suite** — the full sweep.

**The word was the whole point.** `gate` already names the thing being checked; using it for the
checker would put one word on both sides. This project has paid for that exact shape once: for
three days *retrospective* meant both a session's end and a sprint ritual, and it put two live,
contradictory answers in the vault about when `/ingest` runs.

### smoke is built first thing next session

> **owner:** «Строим обязательно. Это первый вопрос на следующую сессию!»

**What the session recommended and he did not contradict:** the selection is **named by the session,
not guessed** — the session made the edits and passes what it touched as an argument; a session that
edited rule 15 and ran rule 11's case proves nothing and nothing would catch that. And **one case is
too thin**: a floor runs always, plus what the session names.

**Composition the session recommended:** the three cheap selftests **in full** —
`hook-selftest.ps1` at 2m17s, `session-dialogue-selftest.py` at 52 cases,
`vault-measure-selftest.py` at 59 — plus `vault-check-selftest.sh` **narrowed**. Only the last one
is expensive, and the reason is structural: it is the only one that copies the corpus per case.

### suite stops running every session

> **owner:** «Перестаем постоянно использовать. Как и говорили ранее - только в очень редких случаях
> или при закрытии спринта.»

**And the cadence agrees with the criterion rather than fighting it.** Criterion 1 of S3 is read off
`missed 0`, and a criterion is read at a sprint's close — which is exactly when the full run now
happens.

**Rejected: keeping the every-session run.** Today is the evidence against it. The suite ran 56
minutes without finishing, its number was never read, and the only thing it accomplished was
starving the gate that `/handoff` must run.

### A single entry point, and `make` is revived

> **owner:** «И да, делаем единую точку входа. Мы когда-то обсуждали make. Можем воскресить вопрос.»

**The gap this closes:** there is no single command today. Running "the checks" is four commands
typed by hand, and the fourth is the one someone forgets. Both `smoke` and `suite` have to become
one command each or the naming buys nothing.

`make` is present on this machine and the no-new-dependencies rule does not reach it — that rule
names Python packages and npm.

### A proposal page settles the check system, and it is next session's first work

> **owner:** «Значит формируем конкретную страницу proposal для того, чтобы разобраться с тестами.
> Как и кто их проводит, когда запускаем и прочее. Это первым делом на следующую сессию»

### DIVERGENCE: the librarian's gate instruction described something nobody has ever done

**The rule as written:** `.claude/agents/vault-librarian.md` said *"After any write, run
`bash scripts/vault-check.sh` and fix everything it reports"*, and the vault's own `CLAUDE.md`
carries the same shape.

**What actually happens:** `/ingest` runs the gate **once, at step 10**, after all the writing.

**The owner's ruling, on being shown it:**

> **owner:** «Тогда нужно исправить инсутркцию для библиотекаря, если она врет. ingest говорит
> делать gate один раз в конце - это окей. Я не замечал каких-то проблем с тем, что библиотекарь не
> проверяет каждую запись через gate.»

**Why it looked unnecessary at the time it was written:** *after any write* is the strictly safer
wording, and nothing measured what it cost. Taken literally, an ingest writing 29 pages pays about
**ten minutes of gate alone** at 21.5 s a run. Nobody has ever paid it, so the instruction was
free-looking and false at the same time.

**Rejected: making the ritual match the instruction.** The owner ruled the ritual correct on the
evidence he has — no problem he has noticed — so the wording moved instead.

### `raw/` is cleaned today, by the script and not by hand

> **owner:** «Тогда передай библиотекарю, что raw нужно почистить сегодня.»

He raised it as a question first — whether he could simply delete the processed files himself and
forget about it — and the answer is no, on a number rather than on caution.

**Measured 2026-08-26: 464 of the 682 live pages name a `raw/` file in their `sources:` line.** That
is 68% of the corpus, and `sources:` is where a page says what it was compiled from. Hand-deletion
leaves two thirds of the store pointing at nothing.

**What to run instead:** `bash scripts/vault-archive.sh [--dry-run] <date> <session> <kind> <file>…`
with `kind = handoffs`. It moves the files into `archive/<date>/<session>/` **and rewrites every
`sources:` citation of them in the same run** — one command by design, because between a move and a
rewrite the gate is red.

**Two constraints the run must respect, both already written into the script or the store:**

1. **A journal with no sidecar does not move.** Both of today's journals acquire theirs during this
   ingest; nothing may be archived before that.
2. **The rewrite is deliberately narrow** — only lines beginning `sources:`, only under `wiki/` and
   `archive/`. On 2026-08-19 a corpus-wide `sed` rewrote two **quotations** along with the
   addresses, because `sed` cannot tell an address from a quotation.

**And there is a recorded hazard on emptying `raw/handoffs/`:** two selftest cases depend on it
being non-empty and fail loudly with the wrong diagnosis when it is not. The repair for that is
recorded as ruled and built; whoever runs the move should confirm that before believing a red
result.

**Reported and not resolved:** the owner says he asked for this before — «сейчас в raw есть куча
файлов, которые там лежат давным давно, хотя я просил их убрать оттуда». The design is on the
record and the script has never been run on a journal.

## How it is built

- **The gate's rule 15 hangs, and the reasoning above it does not cover the case.** Its comment
  provides for an interpreter that is *"present but broken"* on the ground that whatever it writes
  fails to match the good sentence and becomes a note — **which holds for one that returns.** A
  hanging interpreter writes nothing, so there is no note, no verdict, and no end.
- **A wrapper cannot save a probe from a process it cannot kill.** `timeout 15 python3 -c` did not
  return in 90 seconds, because an MSYS signal does not reach a native Windows process. **The guard
  has to refuse the candidate before running it**, which is why the repair is a path test rather
  than a timeout.
- **The same property governs killing a background job here.** `TaskStop` stops the tracked parent
  and not the tree: 33 processes survived in the suite's process group, and `kill -9` on the MSYS
  PID left eight alive because each had a live Windows child. Only
  `taskkill //PID <winpid> //F //T` reached them.
- **Only one of the four selftests is expensive, and the reason is structural.**
  `vault-check-selftest.sh` builds one sandbox root and one pristine copy of the corpus inside it,
  then gives each of its ~178 cases its own working copy of that baseline and runs the gate inside
  it, through a worker pool. The other three copy no corpus per case, which is why 148 hook cases
  cost 2m17s and 178 gate cases cost an hour.
- **`vault-archive.sh` makes move-and-rewrite one command on purpose.** Between the two the gate is
  red, and a `sources:` path that resolves to nothing is a broken address rather than a wrong claim.

## Lessons

- **An hour was spent diagnosing a starved machine that was actually a hung process.** The gate was
  read as slow, then as contended, then as starved, and only a `bash -x` trace pointed at rule 15.
  **The trace was the first thing that answered**, and it cost 90 seconds. Two rounds of process
  archaeology preceded it and neither was necessary.
- **`stdbuf -oL -eL` does not make a suite's progress visible when the suite accumulates its own
  output.** 28 minutes in, the log held one line. A start timestamp answers *when it began* and not
  *whether it is alive*; liveness had to be inferred from the shell process count.
- **A negative measurement that is not written down gets proposed again.** The session built a
  caveat about ordering on `the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate`, which still
  reads *measure first, then narrow*. **owner: that measurement was already done and gave nothing.**
  The result is in no page, so the next session would have proposed it a third time.
- **A defect one day old outlived its own selftest.** Rule 15 and `vault-measure.py` landed in
  `a03f042` with 59 selftest cases, and none of them can see an interpreter that hangs, because the
  suite runs on a machine where the probe happens to pick a working one.

## Deferred

- **The smoke runner, the single entry point, and the `make` question** — ordered as next session's
  first work, so they are deferred by a day rather than open-ended. **Consequence of the gap:** for
  one more session there is no cheap check, so a session either runs the hour-long suite or runs
  nothing.
- **The narrowing flag on `vault-check-selftest.sh`**, which smoke needs and which does not exist.
- **A selftest case for the hanging-interpreter defect.** The repair landed without one, and the
  suite that would carry it is the expensive one the owner has just taken out of the session loop.
  **Consequence:** nothing mechanical protects the repair.

## Feedback to the librarian

Drained from `.superpowers/sdd/vault-feedback.md` a second time in the same session, after the first
journal took what stood then. **Fifteen records, and none is a `- harness:` line.**

- miss: замер по исключению песочницы из антивируса УЖЕ БЫЛ СДЕЛАН и ничего не дал - владелец, 2026-08-26. В vault этого результата нет: proposal the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate жив и несёт порядок "сначала исключение и замер, потом сужение", как будто замер впереди. Сессия построила на этой странице оговорку о порядке и оговорка оказалась ложной. Отрицательный результат замера не записан нигде, и следующая сессия предложит его снова.
- miss: gate висит вечно на правиле 15. scripts/vault-check.sh:1499 выбирает интерпретатор по СУЩЕСТВОВАНИЮ - `for measure_candidate in python3 python py; command -v ... && break` - и на этой машине python3 это заглушка Microsoft Store, /c/Users/kir/AppData/Local/Microsoft/WindowsApps/python3 -> PythonSoftwareFoundation.PythonManager. Она не отвечает и не завершается. Комментарий правила 15 предусматривает интерпретатор "present but broken", который что-то напишет и станет нотой; висящий интерпретатор в это рассуждение не попадает. Правило 15 и vault-measure.py приземлились вчера в a03f042, так что дефекту один день.
- miss: timeout не спасает от заглушки WindowsApps - `timeout 15 python3 -c "print(1)"` не вернулся и за 90 секунд снаружи. Та же причина, что у осиротевших процессов suite: сигнал MSYS не доходит до нативного Windows-процесса, нужен taskkill //T. Защита от висящего интерпретатора обязана стоять ДО запуска, а не вокруг него.
- miss: TaskStop убивает только отслеживаемого родителя, а не дерево. После остановки vault-check-selftest.sh осталось 33 процесса в группе 1447, и kill -9 по MSYS-PID снял не все - у восьми был живой дочерний Windows-процесс, до которого дотянулся только taskkill //PID <winpid> //F //T. Час машинного времени ушёл на диагностику "сломанного gate", который на самом деле голодал.
- measure: gate после правки пробы интерпретатора - 21.5 s, exit 0, VAULT-CHECK: ok, корпус 682 файла. До правки не завершался ни за 5, ни за 10 минут. Записанная стоимость правила 15 на этой машине была 20.2 s, так что 21.5 - это норма, а не остаток проблемы.
- decision: owner said it - smoke строится обязательно и это первый вопрос следующей сессии. 2026-08-26: «Строим обязательно. Это первый вопрос на следующую сессию!»
- decision: owner said it - suite перестаёт запускаться постоянно; только в очень редких случаях или при закрытии спринта. 2026-08-26: «Перестаем постоянно использовать. Как и говорили ранее - только в очень редких случаях или при закрытии спринта.»
- decision: owner said it - делается единая точка входа, и вопрос про make воскрешается. 2026-08-26: «И да, делаем единую точку входа. Мы когда-то обсуждали make. Можем воскресить вопрос.»
- decision: owner selected - имена разведены: gate это только vault-check.sh над живым корпусом, smoke это быстрый прогон по тому, что трогали, suite это полный сквозной прогон. 2026-08-26, против называть gate'ом быстрый selftest - слово уже занято проверяемым, и одно слово с двумя значениями здесь уже стоило двух противоречивых ответов в vault про /ingest.
- miss: инструкция "After any write, run vault-check.sh" в .claude/agents/vault-librarian.md:146 и та же формулировка в vault'овском CLAUDE.md описывают то, чего не происходит. /ingest ставит gate шагом 10, один раз в конце, после всей записи. Буквальное исполнение стоило бы 29 страниц x 21.5 s = больше 10 минут одного gate за ingest. Librarian следует ритуалу, а не своей инструкции, и расхождение никем не замечено.
- measure: make на этой машине есть - GNU Make 4.4.1, /c/ProgramData/chocolatey/bin/make, через chocolatey. Единая точка входа на make технически возможна, и правило "не добавлять зависимости" её не задевает: оно про пакеты Python и npm.
- miss: журнал сессии написан до того, как закончился разговор, и raw/ неизменяем. Всё, что решено после написания журнала 2026-08-26 - разведение gate/smoke/suite, единая точка входа и make, баг заглушки python3 в правиле 15, исправление инструкции librarian'а, заказ на proposal про тесты - в журнал не попало и по умолчанию уехало бы в vault через журнал СЛЕДУЮЩЕЙ сессии. /handoff стоит в ритуале перед /ingest, а разговор после него не заканчивается, и это структурное свойство ритуала, а не случайность этого дня.
- measure: gate после правки инструкции librarian'а - 20.45 s, exit 0, VAULT-CHECK: ok. Регион правила в .claude/agents/vault-librarian.md не задет, правки лежат вне него.
- measure: 464 живые страницы из 682 называют файл raw/ в строке sources:, замер 2026-08-26. Это 68% корпуса. В raw/ 23 файла md, из них 21 журнал, у 20 есть sidecar. Ручное удаление оставило бы две трети корпуса с адресами в никуда.
- decision: the session understood it - на вопрос владельца "могу я просто вручную убрать отработанные файлы из raw/ и забыть" ответ отрицательный, и основание не осторожность, а 464 цитирующие страницы плюс существующий scripts/vault-archive.sh, который переносит и переписывает sources: одним прогоном. Владелец говорит, что просил убрать их оттуда давно; работа спроектирована, скрипт построен и ни разу не запущен на журналах.

## Anything else worth keeping

- **The ritual's own shape produced this journal.** `/handoff` stands before `/ingest`, and the
  conversation does not stop when the journal is written. Today that gap held four owner rulings, a
  one-day-old defect and a direct instruction. **A second journal is the repair available inside the
  ritual as it stands**, and the ingest already provides for more than one uncompiled source. Whether
  something better should exist is not decided here.
- **The owner asked why the gate exists at all if the librarian is the only writer of `wiki/`**, and
  the answer is worth keeping: more than half its rules do not judge librarian output. Rule 8 judges
  a **journal**, written by the session. Rules 11 and 12 judge **regions in harness files**, written
  by the injector. Rule 5b judges the repository `CLAUDE.md`, which is the session's to write, as are
  the per-folder schemas. The librarian is one writer among several, and the gate's own instruction
  says the rest: *each rule exists because that failure has already happened here at least once.*

## Harness

**None filed as a `- harness:` line this time.** What follows is decided harness work, each naming
its file, and it is the same queue the `Deferred` section describes from the other side.

- **A smoke runner** — one command, and it needs a narrowing flag on `scripts/vault-check-selftest.sh`
  that does not exist. The selection is named by the session rather than guessed, with a floor that
  always runs.
- **A single entry point for both smoke and suite**, `make` being the revived candidate and present
  on this machine.
- **`scripts/vault-check.sh`** — rule 15's repair has no selftest case, and the suite that would
  carry it now runs once a sprint.
- **The proposal page settling who runs which check and when**, ordered as next session's first work.
