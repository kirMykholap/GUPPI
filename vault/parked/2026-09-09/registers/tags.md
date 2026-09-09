# Tag dictionary

Consult before minting. If an existing tag fits, use it; if you reject a candidate word in favour
of an existing tag, record the rejected word as an **alias**.

Aliases are not decoration. Retrieval is grep, and this corpus is part Russian and part English:
a question asked in Russian reaches an English page only through an alias. Every Russian word
below is one that a real question is likely to use.

`/lint` flags: **a tag that selects more than ten pages inside one folder of `wiki/`** (split
candidate), a tag used nowhere (dead), two tags with near-identical definitions (merge candidates).

*(This line read «a tag on more than ~15–20 pages» until 2026-08-16, while `vault-check.sh` said
«more than 20» — one rule with two numbers, which
[[dynamic-tag-classification-by-a-skill]] listed as open. There is now one number and it is
measured inside a single folder: **ten** is the ceiling a reader opens for one question, so it is a
property of the reader and does not move when the corpus does, and folders grow at different rates
for different reasons. `archive/` is not measured, because nothing is answered from it. The
reasoning is [[the-folder-is-the-first-narrowing]]; the five lines that stand at `2036d98` are
named in [[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]. The old band was not merely
imprecise: measured per folder at `2036d98`, `testing` is 5 of 47 pages in `decisions/` and 13 of
19 in `lessons/`, and one corpus-wide count cannot say that.)*

## Tags

- tag: frontend
  definition: the browser side as a subject — what runs there, what may run there, and what the
    interface looks like. Minted 2026-08-13 after both acceptance runs reported that no alias
    reached the JavaScript and React pages: the Russian questions landed only because those
    English words happen to appear in filenames. Extended 2026-08-14 by the third acceptance run,
    which asked about rewriting «весь вид приложения» in React: the vocabulary of a *rewrite* —
    вид on its own, SPA, компонент, остров, сборка, TypeScript — reached nothing, so the words a
    migration question uses are now aliases even where the answer they lead to is «we do not have
    that and here is the decision that says why»
    Extended again 2026-08-14 by the fourth acceptance run, which asked what is decided about
    JavaScript: the question landed only because the Latin word is in a filename, while
    браузер, джаваскрипт, клиентский код and инлайн reached nothing at all, and «скрипт» reached only
    the `checks` tag — the vault's own shell scripts, which is the wrong page entirely
  aliases: [JavaScript, JS, React, фронтенд, фронт, вёрстка, внешний вид, вид, интерфейс, клиент, стили, CSS,
    дизайн, design, дизайн-система, design system, палитра, palette, токены, tokens, тема, theme,
    тёмная тема, dark mode, Pico, Bulma, daisyUI, фреймворк, framework, иконки, icons, скриншот, screenshot,
    переписать, переписывать, rewrite, переезд, migration of the front end, SPA, single-page,
    остров, острова, island, islands, компонент, компоненты, component, components,
    Vue, Svelte, TypeScript, TS, сборка, build step, bundler, Vite, webpack, npm, node_modules,
    SSR, гидратация, hydration, состояние в вкладке, client state, state management,
    браузер, browser, джаваскрипт, клиентский код, скрипт на странице, инлайн, inline script,
    переключатель темы, theme toggle, сортировка в браузере, client-side sorting,
    какие строки на экране, which rows are on screen, свой JS, our own JavaScript,
    фильтрация в браузере, сборка параметров запроса, request parameters in the browser,
    ненаписанный тест на JS, owed JS test]
  since: 2026-08-13
  extended: 2026-08-17 (third session) — the JavaScript rule left the repository's `CLAUDE.md`
    for a page ([[our-javascript-does-not-choose-which-rows-are-on-screen]]), and the words the
    rule itself uses reached nothing: `какие строки на экране`, `свой JS`,
    `сборка параметров запроса`. The owed AST test is filed under `testing` by its aliases and
    needs no word here

- tag: web
  definition: the FastAPI / Jinja layer as such — pages, routes, templates, the shell. Narrowed on
    2026-08-13 at 22 of 56 pages: where `htmx` or `filters` already says what the page is about,
    `web` adds nothing and only dilutes the tag
  aliases: [веб, интерфейс, страница, шаблон, page, template, UI, роут, route, оболочка, shell,
    навигация, navigation, base.html, индикатор, indicator, две страницы, two pages]
  since: 2026-08-13

- tag: filters
  definition: the vacancy list's query and its controls — chips, search, checkboxes, pagination
  aliases: [фильтры, чипы, chips, поиск, search, выборка]
  since: 2026-08-13

- tag: data
  definition: field-level rules on stored vacancy data — normalisation, upsert, overwrite, re-parse
  aliases: [данные, нормализация, normalisation, upsert, поля, разбор, parsing, зарплата, salary,
    город, city, локация, location, дата, date, описание, description]
  since: 2026-08-13

- tag: tag-model
  definition: profile tags and the links between tags, profiles and vacancies — the model the chip
    row is built from. Not to be confused with the tags of this dictionary
  aliases: [теги, тег, связка, link, ProfileTag, чип]
  since: 2026-08-13

- tag: htmx
  definition: htmx mechanics specifically — swaps, targets, triggers, headers, out-of-band updates
  aliases: [htmx, swap, фрагмент, fragment, hx-trigger, hx-swap]
  since: 2026-08-13

- tag: collection
  definition: the act of gathering vacancies from a source — the run itself, what starts it, what
    it is polite about, what it defers. Narrowed on 2026-08-13: it had reached 17 of 29 pages and
    had stopped classifying, so bookkeeping went to `batches`, judgement to `deactivation`, and
    field rules to `data`
  aliases: [сбор, прогон, парсинг, parse, run, собрать]
  since: 2026-08-13

- tag: batches
  definition: the run's bookkeeping — `parse_batches`, who opens and closes a batch, staleness,
    the startup sweep
  aliases: [пачки, батчи, batch, parse_batches, финализатор, finaliser]
  since: 2026-08-13

- tag: testing
  definition: test design and evidential power — what a test proves, and how it stops proving it.
    A shell check that guards a rule counts: `checks` and `scripts` were considered on 2026-08-13
    and rejected, because `vault-check.sh` fails a build for the same reason `pytest` does
  aliases: [тесты, тест, покрытие, coverage, pytest, фикстура, fixture, проверка, check,
    stdin, стандартный ввод, закрыть stdin, < /dev/null, фоновый запуск вешает,
    backgrounding hangs, висит на нуле CPU, замер без stdin, measured without stdin,
    через трубу, through a pipe, форма вызова, invocation shape,
    привязка к позиции, positional dependency, последний блок файла, фикстура истекла,
    ворота молча перестали проверять, silent pass, exit 0 без проверки, пустой stderr,
    checks, scripts, скрипт, инвариант, invariant, приёмка, приемка, acceptance,
    приёмочные вопросы, acceptance questions, эталонный ответ, answer key, тестовая база,
    test database, TEST_DATABASE_URL, conftest, conftest.py, TRUNCATE, create_all, боевая база,
    production database, счётчик, количество, count, counts, сколько тестов, расхождение,
    drift, устаревшее число, название теста, названия тестов, test name, test names,
    переименовать тесты, renaming tests, 263 теста, имена на русском, измерение, замер,
    измерить, measurement, measured, инструмент, instrument, второй инструмент,
    second instrument, тихий сбой, silent failure, ложный ноль, grep -P, неподдерживаемый флаг,
    перемерить, remeasure, достоверность, точность страницы, fidelity, сверка, сверить,
    сверка с источником, сверка с кодом, страница устарела, page out of date, фикстура,
    fixture, песочница, sandbox, материализовать файл, materialise, тест проходит без кода,
    green with the code reverted, откатить код и запустить тест, селфтест, selftest,
    сколько идёт селфтест, восемь минут, 8m04s, стоимость прогона, контрольная сумма, checksum,
    избыточность, redundancy, перечисление, enumeration, закрытый набор, closed set, предикат,
    predicate, согласие не истина, agreement not truth, гейт зелёный а правило неверно,
    замер вместо спора, measured not argued, заведомо рабочий, known-good,
    известно рабочий компонент, подменить компонент, тест падает по своей причине,
    test fails for its own reasons, сломан не тот, копия списка, copied list, свип, sweep,
    тихий кейс, quiet test case, плейсхолдер, placeholder, unexpected none,
    сообщение об ошибке, diagnostic wording, вердикт не может сработать, unreachable verdict,
    недостижимый вердикт, когда это сработает, когда вердикт срабатывает,
    second report of somebody else's failure, откатить и перезапустить, revert and re-run,
    доказать откатом, proved by reverting, процессов на страницу, processes per page,
    стоимость спавна, process spawn, 40 ms, померить прежде чем оптимизировать,
    measure before optimising, не тот знаменатель, самое правдоподобное предложение,
    the believable sentence, непроверенное утверждение, run_clean, run_case_absent,
    исключение из advisory, advisory exemption, косметическое изменение, cosmetic change,
    тест грепает вывод, какие кейсы ничего не доказывают, формат вывода важен, проба, probe,
    нонс в раннбуке, nonce in the runbook, загрязнение инструмента, contaminated instrument,
    чистый наблюдатель, clean observable, прогон против старого кода, pre-change run,
    кейс который проходил и до, a case that passes before, посадить страницу и откатить,
    plant and revert, нельзя проверить в песочнице, cannot test in a sandbox,
    фикстуры покраснели, fixtures went red, фикстуры это тоже корпус,
    the fixtures are a corpus, песочница, sandbox, зеркало репозитория,
    mirror of the repository, фикстура переименовала субъект, renamed fixture, приманка, decoy,
    поддельный ваулт, decoy vault, пустышка, placeholder, зелёный на пустышках,
    green on placeholders, run_found, run_clean, порядок циклов, loop ordering, код возврата,
    exit code, статус команды, command status, через пайп, through a pipe,
    конвейер съел статус, exit code of the last stage, tail, grep -c, счёт селфтеста,
    selftest score, первый диагноз, first diagnosis, не та причина, not the cause,
    селфтест красный, selftest is red, сколько идёт селфтест, selftest wall clock, SIGPIPE,
    141, pipefail, grep -q, тихий grep, herestring, herestring вместо пайпа, флейк, flake,
    тест краснеет сам по себе, case fails for its own reason, плантер, planter,
    фикстура устарела, ассерт в стенде измерения, assertion in a harness, сломанный инструмент,
    broken instrument, замер хука, timing a hook, измерять хук из PowerShell,
    measure a hook from PowerShell, пустой payload, empty payload, параллельный selftest,
    parallel selftest, JOBS, воркер, worker, вердикт в переменной, verdict in a variable,
    subshell, подоболочка, заглушка гейта, stubbed gate, порог параллельности, parallel floor,
    мета-тест, meta-test, охранник базы, database guard, require_disposable_database,
    MIGRATION_CHECK_DATABASE_URL, DROP DATABASE, TRUNCATE, докер не запущен,
    docker is not running, тесты висят, the suite hangs, подсадить нарушение,
    plant an offender, прочитать обратно, read it back, редактировать работающий скрипт,
    editing a running script, своя фикстура, own fixture, занять файл у корпуса,
    borrow from the corpus, проверять фразу а не условие,
    assert the sentence not the condition, announcement versus condition,
    зелёный гейт как условие, green gate case, ложный MISSED, false MISSED,
    реальное дерево как фикстура, real tree as a fixture, сломано по-настоящему, collect-only,
    сообщение assert, assertion message, f-string в сообщении, ast-проход, ast pass,
    FormattedValue, интерполяции совпадают, interpolations identical, контроль, control,
    дрейф машины, machine drift, парное измерение, paired reading, зелёный до механизма,
    green before the change, пол прогона, run floor]
  since: 2026-08-13
  extended: 2026-08-15 — two measurements failed in one session, in opposite directions
    ([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]), and the audit
    separated the two directions a page can be stale in
    ([[fidelity-to-a-source-and-fidelity-to-the-tree]]). `measurement`, `fidelity` and `instrument`
    were each considered as tags of their own and rejected: all three are questions about what a
    check or a number proves, which is what this tag is defined as
  extended: 2026-08-16 (second session) — a gate was designed and its guarantee was named in the
    same breath ([[a-gate-guarantees-agreement-never-truth]],
    [[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]]). `контрольная сумма`,
    `закрытый набор`, `перечисление` and `согласие не истина` reached nothing. `checksum` and
    `predicate` were considered as tags of their own and rejected — both are questions about what a
    check proves

  extended: 2026-08-17 — a new hook was proved and the proving broke twice for its own reasons
    ([[a-test-that-fails-for-its-own-reasons-proves-nothing]],
    [[a-known-good-component-locates-the-fault-in-the-harness]]), and two selftest cases were found
    quiet because they read a copied list ([[a-copied-list-drifts-and-a-sweep-cannot]]).
    `known-good` and `diagnostics` were considered as tags of their own and rejected: both are
    questions about what a check proves, which is what this tag is defined as
  extended: 2026-08-17 (third session) — a case was nearly written that would have passed with the
    code reverted ([[a-test-built-from-a-specification-can-pass-without-the-code]]), a fixture was
    found materialising the wrong field's paths ([[a-fixture-must-materialise-what-the-subject-reads]]),
    and the suite's cost became a function of the corpus rather than of the machine
    ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]). The vocabulary of all three reached
    nothing: `фикстура`, `песочница`, `материализовать файл`, `откатить код и запустить тест`,
    `тест проходит без кода`, `селфтест`, `сколько идёт селфтест`, `восемь минут`. `fixture`,
    `sandbox` and `cost` were each considered as tags of their own and rejected — a fixture, a
    sandbox and a run's wall clock are all questions about what a check proves and what proving it
    costs, which is what this tag is defined as
  extended: 2026-08-18 (the ingest of that session) — an approved verdict turned out to be
    unreachable ([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]), two cases were proved by
    running the old code ([[reverting-the-code-tells-you-whether-a-test-tests-anything]]), and an
    optimisation was measured to be counting the wrong unit
    ([[measure-before-optimising-and-count-processes-not-pages]]). The words reached nothing:
    `недостижимый вердикт`, `когда это сработает`, `доказать откатом`, `процессов на страницу`,
    `померить прежде чем оптимизировать`. **`reachability`, `benchmark` and `profiling` were each
    considered as tags of their own and rejected** — whether a check can fire, and what it costs to
    run, are both questions about what a check proves, which is what this tag is defined as.
    `откатить код и запустить тест` has been an alias here since 2026-08-17 and now has a page
  extended: 2026-08-18 (second session) — an advisory exemption was found
    untestable by a clean run ([[a-clean-run-cannot-test-an-advisory-exemption]]) and a reformat
    turned out to be load-bearing for a case that greps the output
    ([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]). The words reached nothing:
    `run_case_absent`, `исключение из advisory`, `косметическое изменение`, `тест грепает вывод`.
    **`assertions` was considered as a tag of its own and rejected** — what an assertion can and
    cannot see is what this tag is defined as

  extended: 2026-08-19 — the selftest's own fixtures went red before the rule they were never
    written for ([[the-fixture-corpus-goes-red-before-the-rule-it-was-never-written-for]]),
    running the suite against the pre-change scripts became the thing that makes a case evidence
    ([[a-case-that-passes-before-the-change-tests-nothing]]), and a verdict was shown to be
    provable only in the real tree
    ([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).
    `probe` and `fixtures` were each considered as tags of their own and rejected — both are
    instruments, and every question about one is a question about what a test is worth here
  extended: 2026-08-19 (third) — a suite went to a fifth of its cases because its sandbox
    renamed the vault, and the vocabulary of a *sandbox*, a *placeholder green* and an *exit code
    read through a pipe* reached nothing
  extended: 2026-08-23 (the ingest of the session that struck three refusals) — a local proof was
    reported as a regression run, and the vocabulary separating the two reached nothing:
    `подсадил нарушителя`, `planted offender`, `прогнать весь селфтест`, `regression run`,
    `новый вердикт сработал`, `старые вердикты`, `caught 157 missed 1`, `локальная проверка`,
    `кейс не запустился`, `no such file`. And from the same session's shell failures: `TMPDIR`,
    `временная папка`, `temp directory`, `scratchpad`, `переменная окружения пустая`,
    `unset variable`, `путь в корень`, `фоновый запуск ничего не написал`
    ([[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]],
    [[tmpdir-is-empty-in-this-shell-so-a-path-built-from-it-lands-at-the-root]],
    [[a-planted-offender-is-proved-by-reading-it-back]])
  extended: 2026-08-23 (the ingest of the session that made a cause a field and landed the style
    rule) — the suite was measured again and its shape was written down for the first time, and
    none of that vocabulary reached anything: `мутационный тест`, `mutation test`, `сломать одно`,
    `форма сьюта`, `run_clean`, `чистый кейс`, `clean case`, `одно правило за раз`,
    `one rule at a time`, `ускорить сьют`, `антивирус`, `virus scanner`, `исключить песочницу`,
    `exclude the sandbox`, `зашитый слаг`, `hardcoded slug`, `plant_rule_page`,
    `переименование ломает тесты`, `обрезанный вывод`, `truncated output`,
    `потерял диагностику`, `куда делся MISSED`. **`mutation-test` and `sandbox` were each
    considered as tags of their own and kept as aliases**: how the checks are checked is what this
    tag already names ([[the-selftest-is-a-mutation-test-of-the-gate]],
    [[a-clean-case-built-on-a-helper-that-plants-a-red-tree-can-never-be-green]],
    [[a-fixture-helper-that-hardcodes-a-page-slug-couples-every-case-built-on-it]],
    [[a-truncated-report-hides-the-line-it-was-run-for]])
  extended: 2026-08-26 (the ingest of the two journals of that day) — the owner named the three
    checks apart and the vocabulary of the naming reached nothing at all: `smoke`, `смоук`,
    `быстрый прогон`, `fast run`, `по тому что трогали`, `what the session touched`,
    `единая точка входа`, `single entry point`, `одна команда`, `one command`, `make`, `Makefile`,
    `GNU Make`, `chocolatey`, `три имени`, `three names`, `gate это только vault-check`,
    `пол прогона`, `floor`, `выбор кейсов называет сессия`, `named by the session`,
    `сколько стоит сьют`, `once a sprint`, `раз в спринт`, `перестаём гонять каждую сессию`.
    **`smoke` and `suite` were each considered as tags of their own and kept as aliases**: which
    check runs when is test design, which is what this tag already names.
    And from the same day's hang: `интерпретатор`, `interpreter`, `python3`, `заглушка`, `stub`,
    `Microsoft Store`, `WindowsApps`, `висит`, `hangs`, `не отвечает`, `проба существования`,
    `command -v`, `таймаут не спасает`, `timeout does not help`, `taskkill`, `MSYS сигнал`,
    `не доходит до Windows-процесса`, `bash -x`, `трассировка`, `trace`, `дефект без кейса`,
    `defect with no case`, `59 кейсов не видят ветку`
    ([[gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning]],
    [[the-smoke-runner-is-built-first-thing-next-session]],
    [[the-suite-stops-running-every-session]],
    [[an-interpreter-probe-must-choose-what-works-rather-than-what-exists]],
    [[a-defect-one-day-old-outlived-the-selftest-that-shipped-with-it]],
    [[a-trace-answered-in-ninety-seconds-what-an-hour-of-process-archaeology-did-not]])
  extended: 2026-08-26 (the vault pass of the session that gave the checks an entry point) — the
    entry point was built and two defects hid inside it, and none of that vocabulary reached
    anything: `make recipe`, `рецепт make`, `stdin`, `стандартный ввод`, `< /dev/null`,
    `закрыть стандартный ввод`, `close standard input`, `exec < /dev/null`, `висит на нуле CPU`,
    `zero CPU`, `рекурсия make`, `jobserver`, `sub-make`, `кейс не забиндился`,
    `argument binding`, `ParameterArgumentTransformationError`, `голое слово`, `bare word`,
    `command mode`, `забыл доллар`, `missing sigil`, `-match`, `счётчик не сдвинулся`,
    `counter did not move`, `caught 169`, `caught 175`, `грепать вывод проверки`,
    `filtered reading`, `фильтр скрыл дефект`, `SMOKE-EXIT`.
    **`make` and `stdin` were each considered as tags of their own and kept as aliases**: how a
    check is run and what hides its output is test design, which is what this tag already names
    ([[a-command-in-a-make-recipe-hangs-while-it-inherits-standard-input]],
    [[a-statement-starting-with-a-bare-word-is-a-command-call-in-powershell]],
    [[a-truncated-report-hides-the-line-it-was-run-for]])
  extended: 2026-08-26 (the ingest of the journal that landed the entry point) — the smoke gate's
    own vocabulary reached nothing: `smoke gate`, `смоук-гейт`, `гейт на handoff`,
    `не даёт сдать журнал`, `зелёный прогон`, `green smoke`, `последняя строка смоука`,
    `latest smoke row`, `перезаписан после прогона`, `written over`, `фоновый прогон`,
    `background run`, `run_in_background`, `нет маркера нет строки`, `no marker no row`,
    `git check-ignore`, `--stdin ничего не получает`, `оценка была неверна в рассуждении`,
    `estimate reasoning`, `пол в 101 секунду`, `floor`.
    **`hooks` and `smoke` were each considered as tags of their own and kept as aliases.**
    `hooks` is what `harness` already names — the files that instruct an agent — and a fifth word
    for the same set is a word that selects a subset of an existing tag; `smoke` is a name for one
    run of the checks, which is test design ([[the-smoke-gate-hooks]],
    [[the-smoke-gate-records-observations-and-the-reader-derives-the-refusal]],
    [[a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code]],
    [[an-estimate-can-be-wrong-in-its-reasoning-and-not-only-in-its-number]])
- tag: architecture
  definition: layering and the boundaries between layers, including the AST tests that hold them
  aliases: [архитектура, границы, boundary, слои, layers, зависимости,
    AST-тест, AST test, тест границы, boundary test, упал тест границы, boundary test failed,
    править тест, edit the test, починить причину, fix the cause, нельзя править тест]
  since: 2026-08-13
  extended: 2026-08-17 (third session) — the rule that a failing boundary test is fixed at its
    cause became a page ([[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]]). The
    vocabulary of a test going red reached nothing at all: `AST-тест`, `упал тест границы`,
    `править тест`, `починить причину`. `boundaries` was considered as a tag of its own and
    rejected: the boundaries and the layering they hold are what this tag is defined as

- tag: db-schema
  definition: the database as a structure — tables, columns, indexes and constraints, the Alembic
    revisions that build them, and keeping those revisions in step with the ORM models. `data` is
    about the values in a row; this tag is about the shape of the row. Minted 2026-08-13 after a
    whole-branch review found that `rg -il "колонк|таблиц|миграц|схем"` over the wiki returned
    nothing at all: the corpus had schema knowledge and no way in for a question about it
  aliases: [схема, schema, схема БД, база данных, БД, database, DB, таблица, таблицы, table, колонка,
    колонки, column, columns, индекс, index, constraint, ограничение, внешний ключ, foreign key,
    миграция, миграции, migration, migrations, Alembic, алембик, upgrade, downgrade, ревизия,
    revision, ORM, модель, модели, model, models, SQLAlchemy, PostgreSQL, постгрес, DDL,
    ALTER TABLE, create_all]
  since: 2026-08-13
  extended: 2026-08-18 — **the definition above covers only the database, and
    the corpus has been using this tag for the record schema as well** since 2026-08-17:
    `governs:`, the marker's type word, the frontmatter core and now the rejection of `quantity:`
    ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
    [[authority-beside-governs-is-forbidden-on-any-page]]). Recorded rather than resolved: whether
    the second use earns a tag of its own, or this definition is widened, is the owner's call at
    the next `/vault-lint`. Aliases for that half: `схема записи`, `record schema`, `фронтматтер`,
    `frontmatter`, `поле страницы`, `page field`, `какие поля обязательны`
  renamed: 2026-08-19 — **the word was `schema` until today, and the call recorded in the line
    above is taken**: the second use earns a tag of its own, `record-schema`, minted below, and
    this half is renamed with it. The definition, the mint date and the database aliases are
    untouched; only the tag word moved, on six pages. **The bare word was retired as a tag on both
    halves rather than kept on this one**, because a general word left on one of two meanings is
    the drift, not a cure for it — the 2026-08-13 definition said *database* in its first clause
    and the corpus tagged record pages with it anyway, so a word that reads as either is decided by
    whoever types it next ([[the-schema-tag-splits-into-db-schema-and-record-schema]]). It survives
    as an **alias on both entries**, which is a different job: an alias carries a question to the
    dictionary, and the dictionary is where an ambiguous word is supposed to be resolved by a
    reader with both definitions in front of him. No page is ever tagged with an alias, so the
    duplication cannot re-create the drift

- tag: record-schema
  definition: a page in this vault as a structure — which frontmatter keys a record must carry and
    which it may, what each one means, and what the folder, the status, the marker and the
    `<!-- text -->` slice say about the record they sit on. `vault` is this store as a subject —
    who writes it and what it is for; this tag is the shape of one record inside it, exactly as
    `db-schema` is the shape of one row. Split off `schema` on 2026-08-19 after the corpus had been
    using that word for both meanings since 2026-08-17
    ([[the-schema-tag-splits-into-db-schema-and-record-schema]]). `frontmatter`, `page-schema` and
    `fields` were each considered as the name and are aliases instead: the first two name one
    spelling of the thing rather than the thing, and `fields` collides with the product's data
    Extended 2026-08-28 with the two status values minted that day. **`status` was considered as a
    tag of its own and rejected**: which words a `status:` may hold, and what each of them obliges,
    is the shape of a record and nothing else
    ([[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]],
    [[a-status-value-is-either-an-address-or-a-stage-and-the-gate-treats-them-oppositely]])
  aliases: [схема, schema, схема записи, record schema, схема страницы, page schema,
    форма записи, устройство страницы, фронтматтер, frontmatter, шапка, шапка страницы,
    метаданные, metadata, YAML, поле, поля, field, fields, поле страницы, page field,
    поле фронтматтера, frontmatter key, ключ, ключи, key, keys, какие поля обязательны,
    which fields are required, обязательное поле, required field, необязательное поле,
    optional field, легальные ключи, legal keys, _schema.yaml, схема папки, folder schema,
    завести поле, mint a field, новое поле, new field, убрать поле, remove a field,
    что можно писать в шапке, authority, governs, basis, status, type, sprint, created,
    processed, обработано, обработанное решение, archived, архивировано, недоехавший переезд,
    half-finished move, метка перехода, значение статуса, status value, адрес или стадия,
    address or stage, освобождает slug, frees the slug,
    decided, sources, supersedes, superseded_by, updated, quantity, тип записи, record type,
    категория, category, папка, folder, зрелость, maturity, маркер, marker, слайс, slice,
    размеченный текст, marked text, набор легальных ключей, legal key set, ключи по папке,
    per-folder keys, неизвестный ключ, unknown key, необъявленный ключ, undeclared key,
    папка без схемы, folder with no schema, схема ничего не даёт, empty schema,
    что кодирует схема, what the schema encodes, решено а не наблюдено, decided not observed,
    basis обязателен, is basis required, ядро фронтматтера, frontmatter core, дата пометки,
    дата исправления, correction note date, когда текст стал ложным, заглушить проверку,
    silence a check, декларация-глушитель, silencing declaration, что такое archive,
    what is archive, охват правил, rule reach, правила читают только wiki, basis обязателен,
    basis is core, basis required, перечисление basis, basis enumeration,
    что утверждает архивная страница, what an archived page asserts, заморожено против живого,
    frozen versus live, находимость, findability, правило 6 и archive, rule 6 widens, values,
    набор значений, legal values, значение вне списка, basis banana, перечисление значений,
    value enumeration, схема значений, пустой набор значений, render обязателен,
    render required, режим доставки, delivery mode, кто несёт governs, who may carry governs,
    governs только в rules, governs is rules-only, страница которая рендерится это правило,
    a page that renders is a rule, концепт с governs, concept carrying governs,
    перенос концепта в rules, authority обязателен в concepts, значения статуса, status values,
    третье значение статуса, third status value, implemented, внедрено, внедрённый proposal,
    implemented proposal, легальный статус, legal status, статус зашит в скрипте,
    hardcoded status pair, блок status в схеме, status block, current и deprecated,
    три состояния proposal, three proposal states, причина страницы, cause of a page, idea,
    полумысль, half-thought, сужение вердикта, narrowed verdict,
    раздел measure, measure region, грамматика measure, measure grammar, датчик называет команду, a gauge names its command, назначение в скобках, destination in brackets, две части в скобке]
  since: 2026-08-19

  extended: 2026-08-19 (second) — the key set became a thing the gate reads from a yaml per
    folder ([[the-per-folder-frontmatter-schema]],
    [[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]), and the vocabulary of that
    change reached nothing: «набор легальных ключей», «неизвестный ключ», «папка без схемы».
    `frontmatter-keys` and `key-set` were each considered as tags of their own and rejected —
    which keys a record may carry is the shape of a record, which is what this tag already is.
    Two rulings about a record's own text join it the same day: the date a correction note
    carries ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]) and what
    `archive/` is, which is undecided
    ([[what-archive-is-stays-undecided-and-the-rules-reading-wiki-disagree-about-it]]).
    `archive` was considered as a tag and rejected: it is a folder, and the question about it is
    which record rules reach it
  extended: 2026-08-19 (third) — `basis` moved from optional to required, and what an archived
    page asserts was separated from how it is found
  extended: 2026-08-21 — the owner overturned his own ruling that any page may carry `governs:`,
    and the field went back to `wiki/rules/` alone
    ([[governs-is-a-property-of-wiki-rules-alone]]). The vocabulary of a folder being decided by
    what a page *delivers* rather than by what it *says* reached nothing: «кто несёт governs»,
    «governs только в rules», «страница которая рендерится это правило», «концепт с governs»,
    «перенос концепта в rules», «authority обязателен в concepts». **`rules` was reconsidered as a
    tag of its own and rejected again**: which folder a record belongs in is the shape of a record,
    which is what this tag is, and the reasons a rule reaches a file are `harness`
  extended: 2026-08-23 — `status` stopped being two-valued. `implemented` was admitted for
    `wiki/proposals/`, the legal set moved out of `scripts/vault-check.sh` and into every folder's
    `_schema.yaml`, and the vocabulary of a *state* rather than a *shape* reached nothing:
    «значения статуса», «третье значение статуса», «внедрено», «легальный статус», «статус зашит в
    скрипте», «блок status в схеме»
    ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
    **`status` was considered as a tag of its own and rejected**: which values a field may carry is
    the shape of a record, which is what this tag already is. The disposition the value serves —
    where an implemented proposal goes — is `vault` and `process`
    ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]])
  extended: 2026-08-23 (the ingest of the session that struck three refusals) — two fields were
    admitted by ruling and neither exists in any schema, so the words a question about them would
    use reached nothing: `Links`, `поле Links`, `викиссылки в поле`, `wikilinks in a field`,
    `sources работает плохо`, `провенанс`, `provenance`, `два смысла у одного поля`, `decided_by`,
    `кто решил`, `causing decision`, `ссылка на решение`, `refused`, `отклонённый proposal`,
    `статус refused`, `метка открывает состояние`, `a mark that opens a state`, `стадия`, `stage`,
    `метка против адреса`, `realised`. `links` and `provenance` were each considered as tags of
    their own and are aliases instead: both name one field of a record, which is what this tag is
    already the shape of ([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]],
    [[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]],
    [[a-refused-proposal-is-archived-and-takes-status-refused]],
    [[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]])
  extended: 2026-08-23 (the session after the one that struck three refusals) — a key's legal
    folders became a question of their own. `decided_by:` was
    narrowed from every schema to `wiki/proposals/` and `wiki/rules/`, required in the second of
    them, and the vocabulary of *where a field may live* reached nothing: «в каких папках поле
    легально», «где поле обязательно», «только в двух папках», «ключ против значения»,
    «неизвестный ключ краснеет», «цепочка причин», «решение порождает proposal или rule»
    ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]). **`folder-scope` was
    considered as a tag of its own and rejected**: which folders a key is legal in is the shape of a
    record, which is what this tag already is. The same day settled that a refused proposal carries
    no `superseded_by:`, whose words — «отказ это причина», «a refusal is a cause», «отклонённый без
    superseded_by» — are the shape of a record too
    ([[a-refused-proposal-is-archived-and-takes-status-refused]])
  extended: 2026-08-23 (the ingest of the session that made a cause a field and landed the style
    rule) — `decided_by:` became a declared key with a verdict behind it, and a requirement that
    holds only under one status had to find a home outside the schema. The words such a question
    arrives in reached nothing: `условное требование`, `conditional requirement`,
    `обязательно если`, `required when`, `схема не умеет условие`, `где живёт условие`,
    `refused без decided_by`, `idea и decided_by`, `статус и решение`,
    `зрелость против авторизации`, `maturity versus authorisation`, `порядок промоушена`,
    `promotion order`, `сначала back-fill потом required`. **`promotion` was considered as a tag of
    its own and kept as an alias**: in what order a field lands is a fact about the record schema
    ([[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]],
    [[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]],
    [[a-verdict-pairing-the-idea-status-with-a-named-decision]],
    [[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]])
- tag: process
  definition: how we work on this project — slices, reviews, plans, what a session owes the next one.
    Sprints live here too: `sprint` was considered as a tag on 2026-08-13 and rejected, because a
    sprint is a frame around work and not a subject of its own. Extended 2026-08-14 with the
    vocabulary of the rule file itself and of the tooling noise around a session: `claude-md` was
    considered as a tag and rejected — it is a file, and everything asked about it («что осталось в
    CLAUDE.md», «почему его сократили») is a question about how we work
    Extended 2026-08-25: `style` and `amendment` were each considered as a tag and rejected —
    the style rule and its amendment are how we work, and a page about either is found by the
    words below. So is `plans`: a plan is an artefact of the process and not a subject of its
    own.
    Extended 2026-08-28: `archiving` and `reminder` were each considered as a tag and rejected.
    Archiving is how the store is kept workable — a `vault` and `process` question, and the family
    it belongs to is in `authority.md` rather than here
    ([[the-purpose-of-archiving-is-a-cheaper-working-wiki-and-archive-is-a-warehouse]]); a reminder
    is a hook, and hooks are `harness`
    ([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).
  aliases: [процесс, слайс, slice, ревью, review, план, plan, sprint, спринт, ретроспектива,
    retrospective, цель, goal, хендофф, handoff, журнал, journal, CLAUDE.md, правила, rules,
    rule file, карта, map, сократить, урезать, shrink, четыре правила, обратная связь,
    feedback, фидбэк, vault-feedback, пожаловаться на вики, виды фидбека, feedback kinds,
    miss measure decision harness, decision как вид, lint больше не вид сессии,
    process больше не вид сессии, слова библиотекаря, ветка, branch, main, коммитить в main,
    ветка на сессию, branch per session, источник строки ратификации, сказано в разговоре,
    ход N, впервые сформулировано здесь, git status, git diff, CRLF, LF, перевод строки,
    конец строки, line ending, line endings, autocrlf, .gitattributes, шум в диффе,
    грязное дерево, dirty tree, язык, language, английский, English, русский, Russian,
    на английском, на русском, кириллица, Cyrillic, перевод, перевести, переводить, translate,
    translation, перевод на английский, translation pass, массовый перевод, mass-translate,
    локализация, localisation, продуктовый текст, product content, интерфейс на русском,
    что видит владелец, stat cache, кеш stat, размер в индексе, cached size, ls-files, --debug,
    renormalize, git add --renormalize, checkout-index, git add -A, почему git status врёт,
    ложная модификация, прочитать статус дважды, restat, dispatch table, таблица диспатча,
    указатель на скилл, точка входа, entry point, на каком языке план, язык плана,
    план на русском, план на утверждение, approval plan, plan language, план вне репозитория,
    план который читает владелец, план на согласование, каденция, cadence, как часто ingest,
    когда компилировать, батч ингестов, размер документа, объём документа, нечитаемый,
    unreadable, длинный план, plan size, docs/superpowers, план на 4864 строки,
    слишком большой документ, доверять документу, исключение из правила, exception,
    правило с исключениями, ослабить правило, ретроспектива это два ритуала, конец сессии,
    end of session, конец спринта, переименовать скилл, номера секций, section numbers,
    разрез по заголовкам, cut by heading, ретро, retro, ритуал, ritual, ретро сессии,
    session retro, интервью сессии, разбор сессии, открытые вопросы, open questions,
    что осталось нерешённым, verdict, вердикт, объявить скилл, announce the skill,
    не видно что скилл запущен, шаги вслух, steps out loud, ритуал не объявлен,
    unannounced ritual, ритуал незаметен, хиэрдок, heredoc, бэктик, backtick,
    подстановка команды, command substitution, проза в команде, prose in a command,
    потерялся файл, файл не записался, тест на допуск, admission test, что должен знать сессия,
    карта проекта, project map, очередь задач, action queue, бэклог, backlog, Beads, бидс,
    трекер задач, task tracker, пустая директория, empty directory, git clean, дерево чистое,
    tree is clean, git add -A, застейджить всё, wildcard staging, чужой коммит, не тот коммит,
    ветка, branch, ветвление, branching, main, в main напрямую, straight to main, PR,
    pull request, слить, merge, соглашение репозитория, repository convention, заблокировано,
    блокер, blocker, растворить вопрос, dissolve a question, снять блокер, process:,
    четвёртый вид обратной связи, как выполняется срез, выполнение среза, кто пишет код,
    who writes the code, обойти правило, обойти проверку, work around, work around a rule,
    отключить проверку, убрать правило, remove a rule, спросить прежде чем, ask first,
    before you weaken, правило выглядело лишним, the rule looked unnecessary, сначала спроси,
    sprint.md, где спринт, где лежит спринт, какой спринт открыт, which sprint is open,
    что должна знать сессия, с чего начать сессию, маршруты в вики, точки входа в вики,
    транслитерация, transliteration, ваулт, пропозал, кириллицей, английский термин,
    technical term, регистр общения, register, как обращаться к владельцу, сужение скоупа,
    narrowing the scope, расширение скоупа, widening the scope, замена скоупа,
    уведомление против вопроса, notification versus question, вопрос закрывает владелец,
    a question is closed by the owner, спросил и не дождался, задал вопрос и решил сам,
    unanswered question, отклонение от правила, divergence, отзыв пропозала, retire a proposal,
    построенный пропозал, built proposal, что жило только там, lives nowhere else,
    чат не сохраняется, chat does not survive, сказал вслух значит записал, подмена формы,
    replaced shape, форма это содержание, вывести заново, derived what the vault already had,
    вывод вместо поиска, tr -dc, посчитать CR, count CR bytes, grep -c с экранированным CR,
    grep врёт про CRLF, рабочая копия против блоба, working copy versus blob,
    git status молчит, git status says nothing, пин защищает репозиторий а не копию,
    заявление опередило измерение, claim before measurement,
    поправить владельцу после согласия, correct the owner after he agreed,
    лицензия которая не была нужна, unneeded licence, прецедент из брифа,
    precedent from a brief, пре-таск не запускали, pre-task skipped, ручная форма правила,
    by-hand form of a rule, дифф до коммита, diff before the commit,
    ратифицировано после коммита, ratified after the fact, выпало из сессии молча,
    fell out silently, брифом нельзя хранить, a brief is not a destination,
    измерение не повторили, unrepeated measurement, число протухло, a figure went stale,
    порядок изменения из двух половин, two-party change, окно между половинами, падать громко,
    fail loudly, красный лучше advisory, чужой файл в git status,
    a file this session did not touch, спросить владельца или вault,
    ask the owner or the corpus, инструкция по сносу, teardown clause, руководство устарело,
    runbook went false, знаменатель против числителя, denominator versus numerator,
    спрятать файл из знаменателя, форвард-онли, forward-only, единица перевода,
    unit of translation, постепенный перевод, gradual translation, не трогай чужой файл,
    do not change a working file, вширь, breadth, ширина обзора, мы можем ошибиться,
    we may be wrong, увидеть и исправить, see it and fix it, неверная диагностика,
    wrong diagnosis, падает в ноль, fails towards zero, рецидив, recurrence, повтор нарушения,
    repeated divergence, третий раз одно и то же, перевод файла, translation,
    кириллица в тестах, Cyrillic in tests, что остаётся непереведённым, grep как счётчик,
    first match is not a count, посчитать вхождения, count the matches,
    язык предупреждения миграции, migration warning language, alembic downgrade,
    журнал ритуала, ledger, реестр запусков, счётчик правил, rule usage counter,
    сколько раз правило сработало, how often a rule fires, ритуал записывает сам себя,
    self-recorded ritual, утверждённый скоуп, approved scope, один pre-task на скоуп,
    ложная тревога, false alarm, тревога которую перестают читать, alarm fatigue, колонка врёт,
    a column that lies, не должен не значит запускал, правка скрипта во время запуска,
    editing a running script, правило в обе стороны, opposite directions on one day,
    а что если, а что если сделать, предложение владельца, owner's proposal, мысли вслух,
    thinking out loud, он не сказал да, he never said yes, ратификация, ratification,
    утверждение задним числом, ratified after the fact, выбрал ни один из вариантов,
    selected none of the options, вопрос вместо ответа, a question in place of an answer,
    вернуться с изменённым дизайном, bring the design back, один вопрос один ход, one turn,
    тест на присутствие, presence test, вопрос идентичности, identity question, grep -l,
    нашлось не то, matched the wrong thing, уверенно неверный ответ, confidently wrong,
    строка обратной связи опаздывает, feedback arrives late, на сессию позже, one session late,
    порядок ритуалов, order of the rituals, ратификация, ratification, ратифицировать строку,
    шаг 5 ретро, цитата владельца, приписано владельцу, пересказ вместо цитаты, paraphrase,
    не говорил такого, правило которого не было, чьи это слова, разрешаю диспатч,
    standing permission, разрешение на диспатч внутри ритуала, промах в plan mode,
    нельзя записать в plan mode, обязанность на сессии, цитата, quote, цитата владельца,
    его слова, чьи это слова, парафраз, paraphrase, атрибуция, attribution, подпись owner,
    приписано владельцу, кириллица в цитате, английская цитата, ратификация цитаты, verbatim,
    дословно, марка, mark, вид записи, kind line, продолжение, continuation, колонка ноль,
    column zero, слова владельца дословно, his own words,
    поправка, amendment, правка а не supersession, обратимая развилка, reversible fork, решай сам, один вопрос за сообщение, one question per message, простой язык по умолчанию, plain language by default, выполнение в отдельной сессии, execution moves to its own session, перенести выполнение, слишком дорого обсуждать, не хватает внимания, третий перенос, deferred again, назвать спринт или отказать]
  since: 2026-08-13
  extended: 2026-08-15 — the day the new-work exemption became a deferral
    ([[english-is-the-rule-and-the-russian-past-is-deferred]]). `language` and `translation` were
    considered as tags of their own and rejected: the language rule is a rule about how we work, and
    the pages that carry it are read beside the slice rules, not beside the product's own text
  extended: 2026-08-16 — the day the line-ending overstatement got a cause and a fix
    ([[the-stale-stat-cache-behind-git-status]], [[markdown-is-pinned-to-lf]]), `/ingest` moved to a
    per-sprint cadence ([[ingest-is-batched-at-the-retrospective]] — retired 2026-08-17, successor
    [[ingest-runs-after-handoff-at-the-end-of-a-session]]) and the plans were measured
    against the vault ([[the-unreadable-mass-is-in-the-plans-not-the-vault]]). `git` was considered
    as a tag of its own and rejected — `git status`, `CRLF` and `.gitattributes` have been aliases
    here since 2026-08-14, and what git reports about our files is a question about how we work.
    `cadence` and `document-size` were considered and rejected for the same reason
  extended: 2026-08-16 (second session) — «retrospective» was found to name two rituals, the end of
    a session and the end of a sprint ([[ingest-runs-after-handoff-at-the-end-of-a-session]]), and
    the handoff template lost its numbers
    ([[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]]). The words for the ambiguity
    reached nothing: `конец сессии`, `конец спринта`, `переименовать скилл`, `номера секций`.
    `template` was considered as a tag of its own and rejected — the handoff template is the form a
    session's account takes, which is how we work

  extended: 2026-08-17 — the end-of-session ritual was named and split in two
    ([[the-end-of-a-session-is-a-retrospective]], [[retro-interrogates-and-handoff-routes]]), and the
    words for it reached nothing: `ретро`, `retro`, `открытые вопросы`, `очередь задач`. `retro`,
    `ritual` and `beads` were each considered as tags of their own and rejected — a ritual is how we
    work, and Beads is a tool nobody has adopted yet ([[the-retro-has-no-action-queue]]). The
    vocabulary of a wildcard commit and of an invisible empty directory joined for the same reason:
    both are things `git` reports about our tree ([[an-empty-directory-is-invisible-to-git-status]],
    [[staging-by-wildcard-sweeps-the-other-partys-edit]])
  extended: 2026-08-17 (second session) — committing straight to `main` became the repository's
    convention ([[main-is-this-repositorys-branch-convention]]), a blocking question was removed
    by changing the design rather than by answering it
    ([[a-blocker-can-be-dissolved-instead-of-answered]]), and the feedback channel gained a
    fourth kind ([[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]). `ветка`, `ветвление`,
    `straight to main` and `блокер` reached nothing. `git`, `branching` and `blockers` were each
    considered as tags of their own and rejected on the standing ground: what git reports about
    our tree, and how we decide what to do next, are both how we work
  extended: 2026-08-17 (third session) — the first rule of the repository's `CLAUDE.md` became
    a page ([[the-owner-decides-how-a-slice-is-executed]]), and it is the slice-execution rule.
    `как выполняется срез`, `выполнение среза` and `кто пишет код` reached nothing. Note the
    collision this creates and read the phrase, not the word: bare `срез` and `слайс` are
    aliases of `harness`, where they mean the marked text slice a rule page ships. A question
    about how a slice is *executed* is this tag
  extended: 2026-08-17 (second migration) — *ask before you weaken a rule* became a page
    ([[ask-before-weakening-or-working-around-a-rule]]), on the day the owner removed a rule of
    `vault-check.sh` **because it had been asked about rather than worked around**. The vocabulary
    reached nothing: `обойти правило`, `отключить проверку`, `убрать правило`,
    `правило выглядело лишним`. `exceptions` and `governance` were considered as tags of their own
    and rejected — «ослабить правило» and «исключение из правила» have been aliases here since
    2026-08-16, and whether a rule may be bent is a question about how we work. The language rule
    and the closing ritual became pages the same day
    ([[english-in-the-repository-russian-with-the-owner]],
    [[a-session-ends-with-retro-then-handoff-then-ingest]]) and needed no new words: `язык`,
    `ретро` and `конец сессии` already point here
  extended: 2026-08-17 (third session, the rules leave the prose) — a ritual ran and the owner could
    not tell ([[a-ritual-that-runs-unannounced-cannot-be-told-from-improvisation]]), and prose was lost
    twice inside a shell command string ([[prose-does-not-survive-a-shell-command-string]]). The
    vocabulary of both reached nothing at all: `объявить скилл`, `не видно что скилл запущен`,
    `шаги вслух`, `хиэрдок`, `бэктик`, `подстановка команды`, `проза в команде`. `announcement`,
    `visibility` and `shell` were each considered as tags of their own and rejected — whether a step
    can be seen to have run, and how a file's text reaches disk, are both how we work. **`Makefile`,
    `make` and the pipelines went to `harness` instead**, since the command list is a block of a file
    that instructs an agent
  extended: 2026-08-18 — the map of what a session must know before it starts became a rendered page
    ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]), and the words for *where the
    sprint is* reached nothing at all: `sprint.md`, `где спринт`, `какой спринт открыт`,
    `что должна знать сессия`, `точки входа в вики`. `sprint` was reconsidered as a tag of its own and
    rejected again on the 2026-08-13 ground unchanged — a sprint is a frame around work, not a subject.
    **Read the phrase and not the word here too**: bare `карта` is this tag, `карта в CLAUDE.md` is
    `harness`, where the map is a region rendered into a file that instructs an agent
  extended: 2026-08-18 (the ingest of that session) — the owner ruled on the register of every
    report to him ([[english-terms-are-not-transliterated-into-cyrillic]]) and on what a session may
    settle for itself ([[narrowing-a-scope-notifies-and-widening-it-asks]],
    [[a-question-asked-is-not-a-question-answered]],
    [[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]). The words reached nothing:
    `транслитерация`, `ваулт`, `пропозал`, `регистр общения`, `сужение скоупа`,
    `вопрос закрывает владелец`, `задал вопрос и решил сам`, `отзыв пропозала`. **`language` was
    considered again and rejected again** — it has been an alias of this tag since 2026-08-15 and
    the rule about which language is `harness`, where it renders; **`scope` was considered and
    rejected** because what a session may decide on its own is how we work, which is this tag
  extended: 2026-08-18 (second session) — a miss said out loud felt filed and
    was not ([[chat-is-not-a-channel-that-survives-the-session]]), an approved shape was replaced
    invisibly ([[a-replaced-shape-reads-as-no-replacement-when-only-the-shape-moved]]), and a
    criterion the corpus already held was derived from scratch
    ([[deriving-what-the-vault-already-holds-costs-a-round]]). The words reached nothing:
    `чат не сохраняется`, `подмена формы`, `вывод вместо поиска`. **`communication` was considered
    as a tag of its own and rejected** — how a finding reaches its destination is how we work

  extended: 2026-08-19 — line endings were measured twice more and both readings were about the
    instrument rather than the files: `grep -c` with an escaped CR returns the line count
    ([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]), and the LF pin
    protects the blob while `git status` is silent about the working copy
    ([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).
    `instruments` was considered as a tag of its own and rejected — an instrument that lies is a
    fact about how we work, and the pages sit beside `git status` and `.gitattributes`, which
    have been aliases here since 2026-08-14
  extended: 2026-08-19 (third) — a `/pre-task` was skipped because the ritual was unavailable and
    the rule has no by-hand form, and an item carried only in a brief fell out of a session with
    nothing recording that it had
  extended: 2026-08-20 (third) — the ritual acquired a ledger and therefore a rule-usage counter,
    and a column of it was found meaning something other than what it says. `ledger`, `counter` and
    `alarm-fatigue` were each considered as tags of their own and kept above as aliases: all three
    are facts about how we work ([[the-pre-task-ledger]],
    [[a-column-a-human-reads-is-not-the-column-a-branch-reads]],
    [[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]])
  extended: 2026-08-21 — a question shaped like a proposal was executed as a ratified design, and a
    presence test answered an identity question and the wrong answer reached the owner.
    `ratification`, `consent` and `instruments` were each considered as tags of their own and kept
    above as aliases: reading what the owner said, and reading what an instrument said, are both
    facts about how we work
    ([[a-question-shaped-like-a-proposal-was-executed-as-a-ratified-design]],
    [[a-proposal-arriving-where-an-answer-was-expected-is-thinking-out-loud]],
    [[a-presence-test-cannot-answer-an-identity-question]],
    [[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]])
  extended: 2026-08-21 (again) — a question put to the owner was made moot before he answered it,
    and two opposite readings of his assent were applied an hour apart
    ([[a-question-put-to-the-owner-was-made-moot-before-he-answered]]). The words reached nothing:
    `молчание как согласие`, `если не возражаешь`, `окей продолжаем`, `снял вопрос сам`,
    `вопрос стал неактуальным`, `withdrawn question`, `silence as consent`. `consent` was
    reconsidered as a tag of its own and rejected for the second time on the same ground: how an
    answer from the owner is read is a fact about how we work
  extended: 2026-08-22 (the ingest of the strike) — a ruling taken from a rendered menu became its
    own attribution shape, and the words for it reached nothing: `owner selected`,
    `выбрал из вариантов`, `меню`, `menu`, `option label`, `ярлык опции`, `выбрал три сразу`,
    `multi-select`, `противоречащие варианты`, `решение а не реплика`, `кто чистит файл`,
    `кто удаляет строку`, `окно между ритуалами`. **`attribution` and `menu` were each considered as
    tags of their own and kept as aliases**, on the standing ground that how the owner is heard is a
    fact about how we work
    ([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]],
    [[a-multi-select-whose-options-contradicted-each-other-was-read-as-a-union]],
    [[whoever-filed-a-feedback-line-empties-it]])
  extended: 2026-08-22 (the ingest of the pre-task agent) — a list he must confirm got a shape of
    its own, and a file read in part was overwritten whole; neither vocabulary reached anything:
    `список на подтверждение`, `формат списка`, `прозой в чат`, `не меню`,
    `такой формат мне нравится`, `перезаписал файл`, `прочитал частично`, `Write поверх`,
    `заметка в плане`, `потерянный комментарий`, `доказано наполовину`, `цепочка доказана`,
    `в свою пользу`. **`review` and `overwrite` were each considered as tags of their own and kept
    as aliases**: how the owner is shown a list and how a file is written are both facts about how
    we work
    ([[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]],
    [[a-file-read-in-part-was-overwritten-whole]], [[a-chain-proved-in-halves-is-not-proved]])
  extended: 2026-08-23 (the ingest of the session that struck three refusals) — the owner asked for
    a style rule before anything else and it was ratified twice and written nowhere, and every word
    of that ask reached nothing: `стиль`, `style`, `как писать`, `читаемость`, `readability`,
    `KISS`, `простыми словами`, `по простому`, `не могу читать`, `ответ в первом предложении`,
    `пять строк`, `правило стиля`, `многословие`. Also `по одной`, `один пункт за раз`,
    `чёткий план`, `детальный план`, `мы расходимся`, `divergence from the owner`. `style` was
    considered as a tag of its own and is an alias: one unbuilt proposal is not a subject
    ([[a-style-rule-for-the-prose-a-session-writes]], [[how-a-slice-is-executed]])
  extended: 2026-08-23, later the same day — the rule was written, so the words above now reach
    three pages rather than one, and the vocabulary of the **recovery** joins them: `где текст`,
    `where the text is`, `текст потерян`, `the text is lost`, `план вне репозитория`,
    `the plan outside the repository`, `восстановить текст`, `recover the text`,
    `убрать рекламу`, `sales pitch`, `назвать источник`, `name the source`, `что не сделано`,
    `what is not done`. **`style` was reconsidered as a tag of its own and is still an alias**: the
    subject is how we work, and three pages about one rule is a page family rather than a new kind
    of question ([[write-plainly-name-the-source-and-say-what-is-not-done]],
    [[the-style-rule-is-ratified-and-its-text-recovered-from-the-approved-plan]])
  extended: 2026-08-23 (the ingest of the session that made a cause a field and landed the style
    rule) — a session was wrong about the date for its whole length, a scanner flagged a genuine
    owner quote, a one-word option bug ran a guard unfiltered, and the owner set who watches the
    style rule and what it reaches. None of those questions had a word that reached a page:
    `дата`, `date`, `какое сегодня число`, `what is today`, `неверная дата`, `wrong date`,
    `вывел дату`, `inferred the date`, `две сессии за день`, `two sessions in one day`,
    `посмотреть на часы`, `read the clock`, `дата это измерение`, `сканер безопасности`,
    `security scanner`, `сфабрикованная цитата`, `fabricated quote`, `нет реплики пользователя`,
    `no user turn`, `проверить посимвольно`, `character by character`, `двойное тире`,
    `double dash`, `--include`, `операнд`, `operand`, `grep без фильтра`, `unfiltered grep`,
    `не влезает в сессию`, `does not fit today`, `вырезать фазу`, `cut a phase`,
    `перенести на следующую сессию`, `сторож это я`, `the owner watches it`,
    `только для общения`, `chat only`, `распространяется ли на vault`, `критерии в бриф`,
    `criteria in the brief`, `вывод команды критерия`, `decider output`, `три способа закрыть`,
    `three closures`. **`date` and `scanner` were each considered as tags of their own and kept as
    aliases**: getting a fact about the run wrong is a fact about how we work, which is this tag
    word for word
    ([[a-date-is-a-measurement-and-an-inferred-one-is-wrong-wherever-it-was-written]],
    [[a-genuine-owner-quote-was-flagged-by-a-scanner-that-cannot-see-the-dispatch-brief]],
    [[an-option-after-a-double-dash-is-an-operand-and-the-search-runs-unfiltered]],
    [[the-ratification-hook-is-cut-whole-and-what-does-not-fit-moves-to-the-next-session]],
    [[the-style-rules-watcher-is-the-owner-and-it-governs-chat-alone]],
    [[the-librarian-prints-each-criterions-decider-output-into-the-brief]],
    [[the-instrument-criterion-closes-more-ways-than-its-decider-counts]])
  extended: 2026-08-26 (the retro that filed no block for a third time) — the vocabulary of the
    feedback channel going silent at the one ritual that generates the most to record:
    `блок в каждом ходе`, `a block every turn`, `retro не пишет feedback`, `retro files nothing`,
    `молчание канала`, `the channel went silent`, `обязательный VAULT-FEEDBACK`,
    `mandatory feedback block`, `решено против наблюдено`, `resolved versus observed`,
    `в ход когда случилось`, `in the turn it happened`, `нечего записать`, `nothing to record`,
    `третий раз`, `third time`, `правило вместо прозы в скилле`, `a rule instead of prose`,
    `напоминалка не механизм`, `a reminder is not a mechanism`. **`feedback` and `retro` were each
    considered as tags of their own and kept as aliases**: how the channel is used is how we work,
    and the ritual itself is `harness` plus this
    ([[every-turn-of-a-retro-files-a-feedback-block]],
    [[divergence-the-retro-filed-no-feedback-block-while-it-ran]],
    [[speak-the-feedback-in-the-turn-and-the-hook-files-it]])
- tag: deactivation
  definition: the judgement about a vacancy that has disappeared from a source — misses, thresholds,
    the conditions under which a pair is even considered
  aliases: [деактивация, исчезнувшие, пропуск, miss, пропала, деактивировать]
  since: 2026-08-13

- tag: profile
  definition: the profile entity and how one gets selected for a request
  aliases: [профиль, cookie, resolve_profile]
  since: 2026-08-13

- tag: agents
  definition: subagents and what dispatching one costs — and, since 2026-08-13, the hooks that run
    around a session without dispatching anything. `hooks` was considered as a tag of its own and
    rejected: it would have held one page, and everything a hook does here is about how a session
    starts, what it is handed and who may write
  aliases: [агенты, агент, субагент, subagent, диспатч, хук, хуки, hook, hooks, SessionStart,
    PreToolUse, settings.json, при старте сессии, session start, перезапуск сессии, PowerShell,
    .ps1, powershell,
    стоимость, сколько стоит, цена, cost, цена диспатча, subagent_tokens, токены агента,
    сколько токенов, tool_uses, duration_ms, время работы агента, wall-clock, сколько времени,
    четыре диспатча, four dispatches, отчёт агента, agent report, проверить агента,
    маска, mask, роль, role mask, ролевая маска, тело, extra body, лишнее тело,
    скилл, skill, скилл против агента, skill vs subagent, когда диспатчить, зачем диспатчить,
    загрязнение контекста, context pollution, изолированный контекст, isolated context,
    grill-me, интервью, опрос, допрос, раунды, rounds, фронтир вопросов, frontier,
    рекомендованный ответ, recommended answer, дерево решений, design tree,
    стюард, steward, второй писатель, second writer,
    529, агент упал, agent died, упал посреди ответа, resume, возобновить агента,
    resume the agent, перезапустить агента, re-dispatch, повторный диспатч,
    pre-task, /pre-task, префлайт,
    .claude/rules/, правила загружаются, instruction loading, когда грузятся правила,
    paths frontmatter, скоуп по путям, после компакта, after /compact, /compact,
    доходит ли правило до субагента, does a rule reach a subagent, Explore, Plan,
    иерархия CLAUDE.md, CLAUDE.md hierarchy, что читает субагент,
    отчёт субагента, subagent report, непроверенное утверждение агента, компакция, compaction, /compact, сжатие контекста, context compaction, что переживает компакцию, what survives a compaction, событие перезагрузки, reload event, load_reason compact, страж, guard, второй триггер, second trigger, гейт чтения у Edit, Edit read gate, скоуп сессии, session-scoped, правило пропало и не вернулось, the rule does not come back,
    разведчик, разведчики, scout, scouts,
    агент решений, decisions agent, агент уроков, lessons agent, читающий агент, reading agent,
    два режима, two modes, вердикт агента, verdict, contradicts, undesigned, перепись решений, census,
    пять акторов, five actors, вложенный диспатч, nested dispatch, глубина вложенности, spawn depth,
    CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH, форк скилла, context: fork, /subtask, пустой контекст,
    судья и перо, verdict and pen, кто судит и кто пишет, регистрация агента задерживается,
    agent registration delay, агент не диспатчится сразу,
    Explore, параллельные читатели, parallel readers, промежуточный файл,
    intermediate file, стоимость диспатча, per-dispatch floor, читающий агент,
    read-only agent, сколько времени на чтение, fraction of a round trip,
    переезд файла агента, agent file moved, реестр перечитывает, registry re-read,
    оба размещения работают, both layouts resolve, замок скрывает здоровье, lock masks the registry,
    цена диспатча, dispatch price, сколько стоит pre-task, узкая запись, narrow write,
    не та единица измерения, wrong unit, ответ не дошёл до владельца, relay,
    граница агента, agent boundary, самоотчёт агента, self-report,
    план и его утверждение, between the plan and its approval, кто переключает режим, who performs the transition, плановый режим не блокирует диспатч, plan mode does not block a dispatch, кэш промпта, prompt cache, cache-safe, инвалидация кэша, opusplan, сабагент дописывает в родителя, appends to the parent, запись во время планирования, blocked write during planning,
    две фазы ритуала, two-phase ritual, фаза 1, фаза 2, каталог в своём контексте,
    catalogue in the main context, короткий список, shortlist, узкий диспатч, narrow dispatch,
    что пропущено в списке, what is missing from the list, агент вместо скилла, agent not a skill,
    ритуал обязателен, enforced ritual, хук видит какой скилл, the hook sees which skill,
    Skill matcher, PostToolUse, хук на Agent, subagent_type, намерение против работы,
    intent versus work, ритуал изменил работу, the ritual changed the work]
  since: 2026-08-13
  extended: 2026-08-15 — the first four figures for a librarian *dispatch* rather than a question
  extended: 2026-08-20 (second) — a dispatch turned out not to be one price: the 15-to-30-minute
    band is an ingest's, a question is 5m54s and a narrow write 1m24s. `cost` and `relay` were both
    considered as tags and are aliases here instead
    ([[agent-round-trip-cost]]). `cost` and `tokens` were considered as tags of their own and
    rejected — what a dispatch costs is a property of dispatching one. Note that `токены` alone is
    an alias of `frontend`, where it means design tokens: a cost question must say `токены агента`
    or `subagent_tokens`
  extended: 2026-08-16 — the owner stated his model of the tooling
    ([[a-skill-is-a-mask-and-a-subagent-is-a-body]]) and the words for it reached nothing: `маска`,
    `роль`, `тело`, `скилл против агента`, `загрязнение контекста`. `skills` and `mask` were
    considered as tags of their own and rejected — a mask and a body are the two shapes of the same
    question, *what gets dispatched and what it costs*, which is what this tag is defined as
  extended: 2026-08-16 (second session) — the owner added an interview skill mid-session
    ([[grill-me-skill]]) and its method turned out to be the transferable part
    ([[interviewing-in-rounds-asks-only-what-is-unblocked]]). `интервью`, `раунды`, `фронтир`,
    `рекомендованный ответ` reached nothing at all. `interview` was considered as a tag of its own
    and rejected — an interview here is a skill running as a mask, which is what this tag is for
  extended: 2026-08-17 — a librarian died on a 529 with its whole read paid for and was
    **resumed** rather than re-dispatched
    ([[a-dead-subagent-can-be-resumed-instead-of-re-dispatched]]), and two `/pre-task` runs were
    measured against what they found
    ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]). `529`,
    `возобновить агента` and `повторный диспатч` reached nothing. `resumption` and `pre-task`
    were considered as tags of their own and rejected — both are about what dispatching a
    subagent costs and how to avoid paying it twice
  extended: 2026-08-18 (the ingest of that session) — how Claude Code loads `.claude/rules/` was
    written down, along with the one thing its documentation is silent about
    ([[claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read]]), and a subagent's
    report was found carrying one unmeasured assertion among measured ones
    ([[a-subagents-most-believable-sentence-is-the-one-to-measure]]). The words reached nothing:
    `.claude/rules/`, `когда грузятся правила`, `после компакта`,
    `доходит ли правило до субагента`, `отчёт субагента`. **`loading` and `config` were considered
    as tags of their own and rejected**: `конфигурация агента` has been an alias of `harness` since
    2026-08-16, and *what a session or a subagent is handed at start* is what this tag is defined as
  extended: 2026-08-19 (third) — a `/compact` was measured: a path-scoped rule does not come back
    and an Edit does not bring it, so *compaction* and *guard* became words a question uses
  extended: 2026-08-20 (third) — plan mode was written down: it blocks edits and not a dispatch,
    switching modes invalidates no cache, and a librarian answering during planning cannot widen
    `tags.md` because that write is blocked ([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]],
    [[switching-permission-modes-is-cache-safe]]). `plan-mode` was considered as a tag of its own
    and rejected here too: this is about what a dispatch costs and when one may happen
  extended: 2026-08-21 (second session) — the ritual split into a cheap enumeration and a narrow
    dispatch, and a hook was measured to see **which** skill was invoked
    ([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]],
    [[an-argument-can-be-true-of-one-surface-and-silent-about-another]]). The words reached
    nothing: `две фазы`, `короткий список`, `узкий диспатч`, `хук видит какой скилл`,
    `Skill matcher`, `PostToolUse`. **`phases`, `skill-surface` and `enforcement` were considered
    as tags of their own and rejected** — a phase split is a decision about *what gets dispatched
    and what it costs*, which is what this tag is defined as, and a surface a hook can watch is
    the same question asked of a hook
  extended: 2026-08-22 — **the ritual became an agent and the skill was deleted**
    ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]],
    [[a-pre-task-runs-between-the-plan-and-its-approval]]). The words of *how you invoke it* reached
    nothing: `агент pre-task`, `pre-task agent`, `subagent_type`, `как запустить pre-task`,
    `чем диспатчить`, `второй агент`, `агент который ничего не пишет`, `read-only agent`,
    `удалили скилл`, `skill deleted`. **`pre-task` was considered as a tag of its own and rejected**
    — it is a ritual performed by dispatching a subagent, which is what this tag is defined as, and
    its own family already exists in `authority.md`
  extended: 2026-08-22 (the ingest of the pre-task agent) — **the agent acquired a page of its own**
    and a brief was measured to carry a price without its findings; the words reached nothing:
    `.claude/agents/pre-task.md`, `имя агента закодировано`, `dispatch:pre-task`,
    `какие инструменты у агента`, `агент ничего не пишет`, `цена без находок`,
    `находки не дошли`, `бриф библиотекарю`, `узкий бриф`, `широкий бриф`. **`briefing` was
    considered as a tag of its own and kept as an alias**: what an agent is handed is part of what a
    dispatch costs and is worth, which is what this tag is defined as
    ([[the-pre-task-agent]], [[a-brief-that-carries-a-cost-without-its-findings-suppresses-the-finding]])
  extended: 2026-08-26 (the ingest of the two journals of that day) — the rule against dispatching
    an agent unasked was cancelled and found to exist in no file, and the words reached nothing:
    `не диспетчерить без просьбы`, `unasked dispatch`, `правило которого нет в файлах`,
    `rule in no file`, `приходит в системный промпт`, `runtime system prompt`,
    `сессия не может это починить`, `диспатч это норма`, `dispatch is the norm`,
    `фильтр binding в фазе 1`, `binding filter`, `deferral остаётся`, `divergence выбрасывается`.
    **`system-prompt` was considered as a tag of its own and kept as an alias**: what instructs an
    agent is `harness`, and where the instruction comes from is a fact about dispatching one
    ([[the-pre-task-is-performed-by-dispatch-and-the-unasked-dispatch-rule-is-the-wrong-one]],
    [[the-pre-task-keeps-deferral-in-phase-one-and-drops-divergence-alone]])

- tag: vault
  definition: this knowledge store as a subject — its schema, its categories, who writes it, what
    it refuses to do, and the scripts that hold it. Not the project's code. Minted 2026-08-13 with
    the first ingest of a session journal; `librarian`, `knowledge-base`, `second-brain`, `wiki`
    and `obsidian` were all considered as tags and are kept below as aliases instead.
    Extended 2026-08-14 by the first ingest of an owner's **note** rather than a session journal:
    the vocabulary of *what was asked for versus what exists* reached nothing at all — `заметка`,
    `инструкция`, `намерение`, `каталог`, `tasks`, `расхождение`. `intent`, `design-intent`,
    `notes`, `divergence` and `tasks` were each considered as tags of their own and rejected: they
    are all questions about this store — what it was told to be, and what it became
    Extended 2026-08-25: `attribution` was considered as a tag and rejected — whose words a
    block carries is a question about this store's records, and the words below reach it.
    Extended 2026-08-30 (the ingest of the session that gave a decision a target): the whole
    vocabulary of the decision lifecycle reached nothing — `жизненный цикл решения`,
    `decision lifecycle`, `мишень`, `target`, `target_kind`, `рукопожатие`, `handshake`, `цепочка`,
    `chain`, `что считать выполненным`, `открытые решения`, `open decisions`,
    `доводить решения до реализации`, `отмена`, `repeal`, `repealed`, `отменить правило`,
    `галочка`, `checkbox`, `разделы страницы`, `body sections`, `lifecycle_from`, `дата отсечения`,
    `dated cut`, `когорта`, `cohort`, `перепись решений`, `census`, `контейнер proposal`,
    `ключ proposal`, `кейс вырос в proposal`. **`lifecycle` and `repeal` were each considered as
    tags and are aliases instead**: the first is a question about how this store's own records move,
    which is what this tag is, and the second is one value of one field
    ([[a-decision-declares-its-target-and-the-handshake-closes-it]],
    [[a-cancelled-page-takes-a-status-of-its-own]], [[the-decision-lifecycle]]).
    Extended 2026-08-30 (the ingest of the session that made a rule findable by lookup): the
    vocabulary of the cleanup reached nothing — `чистка`, `уборка`, `cleanup`, `семейство`,
    `family`, `фасовка по семействам`, `таксономия`, `taxonomy`, `нефункциональные требования`,
    `функциональные требования`, `вердикты по семействам`, `99 вердиктов`,
    `сжать корпус`, `shrink the corpus`, `слуг на несколько типов`, `per-type authority`.
    **`cleanup` and `taxonomy` were each considered as tags and are aliases instead**: the first
    names one operation on this store rather than a subject a page is about, and the second is the
    folder question `record-schema` and this tag already answer between them
    ([[the-authority-register-groups-the-corpus-and-the-family-is-the-unit-of-a-cleanup]],
    [[concepts-are-non-functional-requirements-and-entities-are-functional]],
    [[a-prohibition-family-becomes-one-rule-page-served-by-a-hook]]).
  aliases: [хранилище, вики, wiki, база знаний, knowledge base, второй мозг, second brain,
    чистка, чистка vault, уборка, cleanup, семейство, family, фасовка по семействам,
    группировка корпуса, таксономия, taxonomy, нефункциональные требования,
    non-functional requirements, функциональные требования, functional requirements,
    вердикты по семействам, 99 вердиктов, сжать корпус, shrink the corpus,
    vault-facing, harness-facing, обращено к ваулту, обращено к харнессу,
    трёхзначный вердикт, three-valued verdict, первый род, второй род, first kind, second kind,
    сходимость, convergence, свести слаги, объединить под одним authority,
    правило по слагу, rule served by lookup, генератор правил, family rule generator,
    слуг на несколько типов, per-type authority, один слуг разные типы, замок реестра,
    register deadlock,
    жизненный цикл решения, decision lifecycle, мишень, target, target_kind, рукопожатие,
    handshake, цепочка решений, chain, что считать выполненным, discharged decision,
    открытые решения, open decisions, список нереализованных, taken and not built,
    отмена, repeal, repealed, отменить правило, cancel a rule, галочка, checkbox,
    разделы страницы, body sections, lifecycle_from, required_from, дата отсечения, dated cut,
    когорта, cohort, перепись решений, census, контейнер proposal, ключ proposal, lifecycle,
    корпус про себя, about itself, доля продукта, product share,
    Obsidian, обсидиан, librarian, библиотекарь, ingest, инжест, brief, бриф, справка,
    конспект, Karpathy, Карпати, PARA, Forte, HANDOFF.md, разделить файл, split the file,
    generated-at, устарел, устаревший, stale, свежесть, штамп, stamp, коммит в брифе,
    устаревшая страница, deprecated, superseded_by, замена страницы, supersession, архив,
    archive, один писатель, one writer, параллельно, параллельный запуск, parallel, гонка,
    race, lost update, потерянная запись, вердикт, verdict, sidecar, coverage.tsv, заметка,
    заметка владельца, записка, note, notes, owner's note, инструкция, инструкции,
    instructions, конфигурация, configuration, конституция, constitution, намерение, замысел,
    задумка, intent, design intent, спецификация, spec, каталог, catalogue, catalog,
    автоматически обновляемый, auto-updated index, tasks, tasks/, задачи, статус задач,
    task status, папка задач, active, статус active, current, статус страницы, page status,
    расхождение, divergence, отклонение, diverged, не построено, не реализовано, unbuilt,
    not built, что просил владелец, what the owner asked for, компиляция, компилировать,
    скомпилированный, compilation, compiled, синтез, synthesis, суммаризация, summarisation,
    энциклопедический, слой, слои, layer, layers, трёхуровневая, три слоя, three-layer,
    конституция, constitution, метод, методология, method, catalogue.md, vault-catalogue.sh,
    генерируемый, сгенерированный, generated, автогенерация, автообновление, каталог страниц,
    список страниц, list of pages, каталог сгенерирован, вторая заметка, метод-заметка,
    method note, обе заметки, both notes, две заметки, противоречат друг другу, disagree,
    разошлись, предложение, предложения, proposal, proposals, wiki/proposals/, предложено,
    отложено, отложить, отложенное, deferred, deferral, пятая категория, fifth category,
    что планировали, что не сделали, что планировали и не сделали,
    what we planned and never did, не построили, backlog, бэклог, папка предложений,
    статус предложено, аудит, аудит базы знаний, аудит вики, линт, /lint, /vault-lint,
    проверка здоровья, health check, ревизия хранилища, что нашёл аудит, находки, findings,
    замечание, advisory, отложено владельцу, owed to the owner, долг перед владельцем,
    шесть находок, переименовать страницу, retitle, заголовок страницы неверен, false title,
    ссылка в архив, link into archive, ссылается на устаревшую страницу, тип записи,
    record type, тип страницы, page type, rules, тип rules, правила как страницы, шаблон типа,
    template per type, схема на тип, schema per type, что утверждает страница,
    что устаревает запись, неверно оформлено, mis-filed, raw/, перенести raw,
    архивировать источники, датированный архив, dated archive, переписать пути, path rewriter,
    переезд файла, file move, битые пути, польза вики, используется ли вики,
    сколько раз спросили, изменил ли ответ, usefulness, метрика хранилища, чем мерить вики,
    обвязка, харнесс, оснастка, сборка правил, правило как страницу, rule page, инжектор,
    injector, внедрить правило, зона, zone, governs, asserts, harness, harness-build,
    harness-gate, harness-layout, шлюз, gate, ворота, симлинк, symlink, свидетельство,
    testimony, артефакт, артефакты, artefact, artifact, спека, спеки, план, планы, заморозить,
    freeze, где лежат спеки, инбокс, inbox, пустой raw, sessions/, archive/<date>, updated,
    штамп, дата обновления, устаревание страницы, детектор устаревания, staleness detector,
    подозрительная страница, suspect, реестр, register, реестр authority, authority register,
    слаг, slug, минтить, mint, ядро полей, frontmatter, фронтматтер, поля страницы,
    обязательные поля, required fields, построено или отклонено, built or refused, идея, idea,
    status: idea, зрелость записи, maturity, заголовок с числом, quantity,
    количество в заголовке, поправить заголовок, retitle, правка заголовка на месте,
    title corrected in place, кто пишет вики, ручная правка вики, шаблон хендоффа,
    handoff template, секция Harness, pages.base, base, bases, Obsidian base, база,
    база Obsidian, базы, плагин Bases, запрос вместо файла, query not a file, каталог удалён,
    catalogue deleted, реестры, registers, кто правит index.md, who edits the registers,
    вид обратной связи, feedback kind, четвёртый вид, четвёртая категория обратной связи,
    quantity, поле quantity, декларация количества, эскейп-хэтч, escape hatch,
    число в имени файла, digits in a filename, переименование страницы, page rename,
    sed и проверка, sed-and-verify, дыра в log.md, log.md hole, набор ссылок, link set,
    висячая ссылка, dangling link, входящие ссылки, inbound links,
    цифра в заголовке отменяется, что уехало вместе с адресом, sed переписал цитату,
    sed rewrote a quotation, цитата против адреса, quotation versus address,
    голое упоминание слага, bare slug mention, голый слаг, bare slug,
    чем считать входящие ссылки, how to count inbound links, имя каталога ваулта,
    vault directory name, ссылки на путь ваулта, citations of the vault path,
    переименовать ваулт, rename the vault, кто пишет схему ваулта, who writes the vault schema,
    вход гейта, gate input, _schema.yaml, схема папки, folder schema,
    archive/<date>/<session>/, папка на сессию, folder per session, имя папки сессии,
    session folder name, очистка raw, emptying raw, скрипт а не агент,
    a script rather than an agent, таблица соответствий, mapping table, детектор путей в прозе,
    prose path detector, путь в тексте, path in a body, структура внутри raw,
    structure inside raw, порядок миграции, migration order, ротация лога, log rotation,
    лог растёт, the log grows, logs/, лог не переписывается, the log is never rewritten,
    архив переписывается, archive is rewritten, что оставило рабочий набор,
    what left the working set, номер правила, which rule is it, правило 5 или 11,
    один писатель и цитаты, one writer and citations, переписать sources при переименовании,
    repoint a citation, кто может править wiki руками, who may hand-edit the wiki,
    правка руками при красном гейте, путь в прозе, path in prose, историческая ссылка,
    claim about a past time, не переписывать прозу, параллельно только на чтение,
    parallel only for reading, потерянная запись, lost update, вне очереди, out-of-band write,
    диффы не читаю, I do not read diffs, принятый риск, accepted risk, видимость ошибки,
    findability of a mistake, заметка про одного писателя, one-writer note, раз в сессию,
    once per session, сайдкар, sidecar, coverage.tsv, файл покрытия, что значит скомпилирован,
    what compiled means, выбор источника ингеста, ingest source selection,
    какой хендофф компилировать, which handoff to compile, самый новый по дате, newest by date,
    три журнала за день, three journals in one day, тай-брейк, tie-break, нечего компилировать,
    nothing to ingest, проверка существования файла, file-existence test, ingested:,
    generated-at:, штамп брифа, brief stamp, архивирование источника, archiving the source,
    шаг 12, только вперёд, forward only, журнал уехал в архив, the journal moved,
    где искать скомпилированный журнал, имя файла а не путь, a filename not a path,
    плотность тегов на каждом ingest, density at every ingest, каденция советов,
    advisory cadence, теги ничего не классифицируют, the tags classify nothing,
    архив это история, archive is history, вики источник истины, wiki is the source of truth,
    убрать из прямой видимости, out of direct view, proposal уезжает в архив,
    ссылка остаётся в новом документе, живая страница цитирует proposal,
    a live page cites the proposal, датчик, gauge, свидетельство, testimony, роль числа,
    ратификация, ratification, показать список целиком, shown whole, пустое поле, absent field,
    вики опережает действия, the wiki runs ahead of the actions, сессия ничего не построила, только decisions и proposals, снять подпись owner, remove the owner signature, переписать блок голосом сессии, отменить проверку кириллицы, the alphabet test is overturned, библиотекарь пишет только в log]
  since: 2026-08-13
  extended: 2026-08-15 (again) — `wiki/proposals/` was added, and the vocabulary of *what we planned
    and never did* reached nothing: `предложение`, `отложено`, `что не сделали`. `proposal`,
    `proposals`, `deferred`, `backlog` and `intent` were each considered as tags of their own and
    rejected — a proposal is a page shape of this store, and every question about one is a question
    about how the store files an intention it has not built ([[proposals-are-a-folder-not-a-status]])
  extended: 2026-08-15 (third time) — the first `/vault-lint` ever ran, and the vocabulary of *an
    audit and what it left open* reached nothing: `аудит`, `линт`, `находки`, `отложено владельцу`.
    `audit`, `lint` and `findings` were each considered as tags of their own and rejected — an audit
    here is this store checking itself, which is what the tag is for
    ([[the-audits-findings-are-owed-to-the-owner]])
  extended: 2026-08-15 — the second owner's note was compiled, and the vocabulary of *the method*
    reached nothing: `компиляция`, `RAG` against a page rather than a tag, `слои`, `конституция`,
    `синтез`. `compilation`, `philosophy` and `catalogue` were each considered as tags of their own
    and rejected: all three are questions about what this store is and how it was told to be built
  extended: 2026-08-16 — three vocabularies reached nothing at all. *What a record of each type
    asserts*: `тип записи`, `шаблон типа`, `что утверждает страница`
    ([[a-schema-per-type-says-what-a-record-asserts]], [[rules-becomes-a-type-of-its-own]]).
    *Moving the sources*: `перенести raw`, `переписать пути`, `датированный архив`
    ([[moving-raw-into-a-dated-archive]]). *Whether the store is used at all*: `польза вики`,
    `сколько раз спросили` ([[the-measurement-is-whether-the-vault-changed-what-a-session-did]]).
    `rules`, `templates` and `usefulness` were each considered as tags of their own and rejected —
    a type, a template and a usage measure are all properties of this store
  extended: 2026-08-16 (second session) — the record schema was settled field by field
    ([[the-frontmatter-core-is-fixed-and-updated-joins-it]]) and `raw/` got a meaning
    ([[raw-holds-testimony-and-artefacts-are-frozen]],
    [[archive-is-dated-by-session-and-holds-what-left-the-working-set]]). Three vocabularies reached
    nothing: *the field core and the new stamp* — `updated`, `ядро полей`, `штамп`, `детектор
    устаревания`; *testimony against artefact* — `свидетельство`, `артефакт`, `где лежат спеки`,
    `пустой raw`; *the register the `authority` field lacks* — `реестр`, `слаг`, `минтить`.
    `frontmatter`, `fields`, `staleness` and `register` were each considered as tags of their own
    and rejected: a field, a stamp and a register are all machinery of this store. **`harness` was
    the one candidate accepted** — see below, and note that the harness pages deliberately carry
    `harness` **instead of** a second `vault`, because the density advisory is measured per folder
    ([[the-folder-is-the-first-narrowing]])

  extended: 2026-08-17 — an idea got a home in `proposals/` with a status of its own
    ([[an-idea-is-a-proposal-with-an-immature-status]]) and a title correction was decided not to be
    a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]). `idea`, `maturity` and
    `quantity` were each considered as tags and rejected — all three are questions about how this
    store records things. `идея` and `правка заголовка на месте` reached nothing before this
  extended: 2026-08-17 (second session) — `catalogue.md` became `pages.base`
    ([[pages-base]], [[the-page-list-is-a-query-not-a-generated-file]]), the folder set reached
    six ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]), and the one-writer rule gained the
    registers ([[the-one-writer-rule-covers-the-registers-too]]). Three vocabularies reached
    nothing: `pages.base`, `база Obsidian`, `запрос вместо файла`; `реестры`,
    `кто правит index.md`; and `вид обратной связи` ([[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]).
    **`base`, `bases` and `registers` were each considered as tags of their own and rejected** —
    an artefact holding the page list and a file only the librarian may write are both questions
    about this store's own machinery. `catalogue` was reconsidered and rejected for the third
    time, on the ground it was rejected on before
  extended: 2026-08-17 (third session) — a proposal was found wrong about the hole it described
    ([[a-proposal-can-be-wrong-about-the-hole-it-describes]]), `pages.base` stopped being a review
    item ([[pages-base-is-not-a-review-item]]), and two pages were retired by the session that
    performed the change they described ([[the-repository-claude-md-after-the-rules-left-it]]).
    The words reached nothing: `дефект в предложении`, `предложение оказалось неверным`,
    `кто проверяет proposal`, `не смотреть на pages.base`, `не ревьюить файл`. `proposals` was
    reconsidered as a tag of its own and rejected for the second time — a defect in an unbuilt
    design is a question about this store's own machinery, which is what this tag is defined as
  extended: 2026-08-18 (second session) — the `quantity:` field was rejected
    outright ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), a rename was
    measured rather than feared ([[a-page-rename-is-sed-and-verify]]) and `log.md` was found
    outside the link set the gate reads ([[log-md-is-outside-the-link-set-the-check-reads]]). The
    words reached nothing: `поле quantity`, `эскейп-хэтч`, `дыра в log.md`, `набор ссылок`,
    `входящие ссылки`. **`renaming` and `linkcheck` were each considered as tags of their own and
    rejected** — moving an address and checking that links resolve are both questions about this
    store's own machinery

  extended: 2026-08-19 (second) — the sixteen renames were executed and both of their surprises
    were about a string substitution being a string substitution: it rewrote two quotations
    ([[sed-cannot-tell-an-address-from-a-quotation]]) and it caught the bare mentions a
    link-graph rewriter would have missed
    ([[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]). `renaming` was
    considered as a tag of its own and rejected — `переименование страницы` and `inbound links`
    have been aliases here since the rule reached filenames
  extended: 2026-08-19 (third) — the corpus was found to cite the vault by its literal directory
    name, and who writes what the gate reads as its own input was decided
  extended: 2026-08-20 (third) — the out-of-band write pair was answered: *parallel only for
    reading* became a rule rendered into the repository's `CLAUDE.md`, and diff-reading was declined
    with the risk accepted. The words reached nothing: `вне очереди`, `потерянная запись`,
    `диффы не читаю`. `concurrency` and `lost-update` were considered as tags of their own and
    rejected — who may write this store and when is what this tag is defined as
    ([[dispatch-librarians-in-parallel-only-for-reading]],
    [[the-out-of-band-write-pair-is-answered-by-a-rule-and-a-declined-risk]])
  extended: 2026-08-21 — Occam's razor became the store's ground rule and the corpus gained a
    second register ([[occams-razor-is-the-ground-rule-for-the-vault]],
    [[authority-becomes-the-index-and-is-required-outside-rules]],
    [[an-admission-test-for-mechanisms]], [[a-machine-readable-format-for-the-registers]],
    [[lessons-become-a-queue-drained-into-proposals]]). Added: `бритва Оккама`, `Occam`,
    `не плодим сущности`, `допуск страницы`, `page admission`, `искать перед тем как писать`,
    `look it up before writing`, `семья слугов`, `реестр вопросов`, `authority.md`,
    `формат реестра`, `yaml для реестров`, `уроки в очередь`, `lessons as a queue`,
    `допуск механизма`, `mechanism admission`, `цена поддержки механизма`.
    `admission`, `registers` and `occam` were each considered as tags of their own and kept as
    aliases: what may enter this store and what indexes it are both facts about the store
  extended: 2026-08-22 (the ingest of the strike) — a retirement gained a fourth step and a
    mid-session one gained a naming problem, and neither vocabulary reached anything:
    `четвёртый шаг`, `fourth step`, `убрать слаг из реестра`, `строка без страницы`,
    `красный гейт после переноса`, `слаг сессии`, `session slug`, `имя папки сессии`,
    `ретайр среди сессии`, `обещание вместо механизма`, `плоские страницы в архиве`,
    `только вперёд`, `forward-only`, `свип атрибуций`, `ratification sweep`, `--lint`.
    **`retirement` and `sweep` were each considered as tags of their own and kept as aliases**: how
    a page leaves this store is a fact about the store
    ([[retiring-a-page-removes-its-slug-from-the-authority-register]],
    [[the-session-slug-is-written-to-a-file-and-the-handoff-reads-it]],
    [[the-ratification-sweep-waits-for-a-session-of-its-own]])
  extended: 2026-08-22 (the ingest of the pre-task agent) — **a built proposal stopped going to the
    archive**, and the vocabulary of the ruling reached nothing: `пометка built`, `built mark`,
    `построенный proposal`, `не уезжает в архив`, `что делать с построенным предложением`,
    `третий статус`, `third status`, `что запланировали и не сделали`. **`proposals` and `built`
    were each considered as tags of their own and kept as aliases**: what a folder of this store
    holds and how a page leaves it are facts about the store
    ([[a-built-proposal-stays-in-proposals-with-a-built-mark]],
    [[proposals-are-a-folder-not-a-status]])
  extended: 2026-08-23 (the ingest of the session that struck three refusals) — the owner reversed
    what `archive/` is and ruled a third disposition for a proposal, and the words a question about
    it would use reached nothing: `архив это история`, `archive is history`,
    `вики источник истины`, `wiki is the source of truth`, `убрать из прямой видимости`,
    `out of direct view`, `внедрённый proposal`, `implemented proposal`, `отклонённый proposal`,
    `refused proposal`, `что уехало в архив пусть лежит`, `обратно из архива`,
    `back from the archive`, `сирота`, `orphan`, `кто на неё ссылается`, `who points at it`,
    `один тег на всё внешнее`, `external`, `внешние страницы`, `чужие системы`. **`external` is
    ruled as a tag and is deliberately not minted here** — no page carries it and a tag selecting
    nothing prints a dead-tag advisory on the day it lands
    ([[the-pages-about-what-this-project-does-not-own-get-one-shared-tag]],
    [[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]],
    [[a-refused-proposal-is-archived-and-takes-status-refused]])
  extended: 2026-08-26 (the ingest of the two journals of that day) — the owner overturned the
    forward-only clause and `raw/handoffs/` was swept whole for the first time, and the words that
    question arrives in reached nothing: `почистить raw`, `clean raw`, `убрать из raw`,
    `свип журналов`, `sweep the journals`, `весь бэклог`, `the whole backlog`,
    `464 из 682`, `две трети корпуса`, `удалить вручную`, `delete by hand`,
    `адрес в никуда`, `broken address`, `только вперёд`, `forward only`, `отменено владельцем`,
    `overturned`, `перенос и переписывание одним прогоном`, `move and rewrite in one run`.
    **`archive-sweep` was considered as a tag of its own and kept as an alias**: how this store
    empties its inbox is a fact about the store.
    And from the same day's register work: `потолок семьи`, `family ceiling`, `около десяти`,
    `пятый регистр`, `fifth register`, `кто пишет authority.md`, `who writes authority.md`,
    `authority у proposal`, `паралельный ратифицированный парафраз`, `basis остаётся human`
    ([[raw-handoffs-is-swept-whole-today-and-the-forward-only-clause-is-overturned]],
    [[the-authority-registers-family-ceiling-is-deleted]],
    [[authority-md-is-a-register-the-one-writer-clause-names]],
    [[a-paraphrase-that-survived-ratification-keeps-basis-human]])
  extended: 2026-08-28 (the ingest of that day's journal) — the output side of the store was
    decided, and the words that conversation arrives in reached nothing:
    `зачем архивировать`, `why archive at all`, `подметать рабочую вики`, `sweep the working wiki`,
    `архив это склад`, `the archive is a warehouse`, `экономит токены`, `saves tokens`,
    `обработанное решение`, `processed decision`, `решение больше не нужно`,
    `порождённая страница`, `produced page`, `критерий выхода`, `exit criterion`,
    `предикат архивации`, `archival predicate`, `цитата это не тест`, `citation is not a test`,
    `агент по решениям`, `decisions agent`, `кто диспатчит ingest`, `who dispatches the ingest`.
    **`archiving` was considered as a tag of its own and kept as an alias**: which pages leave the
    working wiki, and why, is a fact about this store — and the family that gathers those pages
    lives in `authority.md`, where a family is what a lookup returns
    ([[the-purpose-of-archiving-is-a-cheaper-working-wiki-and-archive-is-a-warehouse]],
    [[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]],
    [[a-citation-is-not-a-test-in-a-corpus-this-densely-linked]],
    [[the-decisions-agent-reads-only-and-runs-at-every-ingest]])
  extended: 2026-08-29 (the ingest of the first sweep) — the sweep ran and a third of `wiki/` left,
    and the vocabulary of that day reached nothing: `первый свип`, `the first sweep`,
    `239 страниц`, `вики стала на треть меньше`, `a third smaller`, `--sweep`, `режим свипа`,
    `sweep mode`, `один проход по корпусу`, `one pass over the corpus`, `селектор`, `selector`,
    `сколько стоит свип`, `слаг остаётся при архивации`, `keeps its slug`,
    `четвёртый шаг отменён`, `the fourth step is repealed`, `реестр не трогаем`,
    `живой преемник`, `live successor`, `правило без инструмента`,
    `a rule with no instrument`, `фикстура нарушала правило`.
    **`archiving` was reconsidered on the day the sweep actually ran and is still an alias** — the
    first real run changed the size of this store and not the kind of thing it is
    ([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]],
    [[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]],
    [[the-sweep-is-a-mode-of-the-archiver-and-inherits-its-refusals]],
    [[a-selector-is-one-pass-over-the-corpus-and-never-one-pass-per-page]])
  extended: 2026-08-31 (the ingest of the session that turned the families into rules) — the
    cleanup's own vocabulary reached nothing, because it had never been written into a page:
    `vault-facing`, `harness-facing`, `первый род`, `второй род`, `трёхзначный вердикт`,
    `сходимость`, `convergence`, `свести слаги`, `генератор правил`. **`cleanup` was reconsidered
    as a tag of its own for the third time and is still an alias** — the cleanup changed the size
    of this store twice now and not the kind of thing a page about it is about; and **`family` was
    reconsidered and rejected again**, because a family is the unit of one operation rather than a
    subject a page can be about ([[the-cleanup-verdict-names-which-delivery-a-family-gets]],
    [[only-the-vault-facing-families-are-built-and-the-harness-facing-kind-waits]],
    [[the-slug-converges-by-hand-along-the-chain-of-types]],
    [[the-family-rules-are-drafted-by-a-generator-inside-the-librarians-dispatch]])

- tag: retrieval
  definition: finding the right page — grep, wikilinks, tags and aliases, and the vectors that are
    deferred. The subject is recall: what a question reaches and what it silently misses. Minted
    2026-08-13; `search`, `vectors` and `embeddings` were rejected as tags in its favour
  aliases: [поиск, search, найти, grep, ripgrep, вектора, векторы, vectors, эмбеддинги, embeddings,
    vault-ask, форк, fork, форкнутый скилл, forked skill, context fork, чистый контекст,
    точка входа поиска, search entry point, agent Explore, обойти граф грепом, walk the graph,
    цепочка одного вопроса, chain of one question, один слуг несколько типов,
    каталог без архива, catalogue without the archive,
    RAG, recall, находимость, ссылки, links, синонимы, aliases,
    имя файла, имена файлов, название файла, названия файлов, filename, filenames, naming,
    именование, как назвать страницу, префикс, prefix, категория в имени, kebab-case,
    переименовать, rename, поисковая поверхность, search surface,
    где лежит index.md, корень хранилища, vault root, путь к файлу,
    теги вики, теги страниц, теги в хранилище, сколько тегов, tag count, словарь тегов,
    tag dictionary, классификация, классификация тегов, tag classification, сгруппировать теги,
    grouping, разделить тег, split a tag, объединить теги, merge tags, порог, threshold,
    дрейф, дрейф понятий, concept drift, Smart Connections, Dataview, плагин, plugin,
    заголовок, заголовок страницы, title, titles, числа в заголовке, цифры в заголовке,
    numbers in titles, количество в заголовке, measurable quantity, форма заголовка, title form,
    как назвать заголовок, как формулировать заголовок, существительное, noun phrase,
    подтег, уточнение тега, refinement, строгое подмножество, strict subset, слить теги,
    число в имени файла, имя файла с количеством, filename quantity, переименовать страницу,
    сколько ссылок на страницу, входящие ссылки, inbound links, 23 ссылки,
    порядковое числительное, ordinal numeral, второй в заголовке, первый в заголовке,
    какие слова считаются количеством, which words count, список слов, word list,
    предикат заголовка, title predicate, исключение из правила заголовка,
    почему второй считается, why second counts, можно ли объявить исключение,
    поле quantity, quantity field, объявить число безопасным, escape hatch,
    подзаголовок, подзаголовки, заголовок в тексте, заголовок раздела, body heading, section heading,
    число в подзаголовке, счёт в подзаголовке, number in a heading, counting heading,
    что читает правило, what the rule reads, предмет правила, читает ли правило текст страницы,
    длина заголовка, title length, длинный заголовок, long title, слишком длинный заголовок,
    ограничение длины, length limit, сколько символов, character count, самый длинный заголовок,
    longest title,
    воронка чтения, reading funnel, стадии поиска, широкая половина, wide half,
    потолок в десять страниц, ten-page ceiling, открыть страницу против найти страницу,
    перечислить фронтматтер, enumerate frontmatter, одна команда по всему корпусу,
    vault-catalogue.sh, семейство вопросов, family of slugs, реестр authority, authority.md,
    что перечисляет pre-task, какие папки читает план, охват перечисления, enumeration scope]
  since: 2026-08-13
  extended: 2026-08-15 (again) — the owner's design for a tag-classifying skill was recorded
    ([[dynamic-tag-classification-by-a-skill]]), and the words a question about *the tags themselves*
    would use reached the wrong entry or none: `теги` resolves to `tag-model`, which is the profile
    tags of the product, and `классификация`, `дрейф`, `порог` reached nothing at all.
    `classification`, `taxonomy` and `drift` were each considered as tags of their own and rejected —
    grouping the dictionary is what the dictionary is for, and that is recall
  extended: 2026-08-15 — the day filenames became a recorded decision. The vocabulary of *naming*
    reached nothing at all: `имя файла`, `префикс`, `kebab-case`, `переименовать`. `naming` was
    considered as a tag of its own and rejected — a filename here exists to be grepped, so every
    question about one is a question about retrieval
  extended: 2026-08-16 — the day a *title* became a rule as well as a filename
    ([[a-title-names-what-is-counted-instead-of-counting-it]],
    [[the-titles-form-follows-the-records-type]]). The vocabulary of a title reached nothing:
    `заголовок`, `числа в заголовке`, `форма заголовка`. **`naming` was reconsidered and rejected
    again**, on the 2026-08-15 ground unchanged: a title here is read out of a grep result, so a
    question about one is a question about recall. `titles` was rejected with it. Also extended with
    the vocabulary of a tag that refines another, after the `batches` merge was refused
  extended: 2026-08-17 (third session) — **the no-quantity rule was extended by the owner to cover
    filenames as well as titles** ([[the-title-rule-extends-to-filenames]]), so the address and the
    claim are now under one rule and only one of them is checked. The words of that distinction
    reached nothing: `число в имени файла`, `имя файла с количеством`, `переименовать страницу`,
    `сколько ссылок на страницу`, `входящие ссылки`, `inbound links`. **`filenames` was reconsidered
    as a tag of its own and rejected for the third time**, on the 2026-08-15 ground unchanged: a
    filename here exists to be grepped
    ([[batches-stays-a-tag-of-its-own]])
  extended: 2026-08-19 — **the word list behind the no-quantity rule became a decision of its own**
    ([[ordinals-count-and-first-does-not]]), and the vocabulary of *which words count* reached
    nothing: a question about why `second` is a violation while `first` is not had no way in at all.
    Added: `порядковое числительное`, `ordinal numeral`, `второй в заголовке`, `первый в заголовке`,
    `какие слова считаются количеством`, `which words count`, `список слов`, `word list`,
    `предикат заголовка`, `title predicate`, `исключение из правила заголовка`,
    `почему второй считается`, `why second counts`, `можно ли объявить исключение`,
    `поле quantity`, `объявить число безопасным`, `escape hatch`. **`titles` and `naming` were not
    reconsidered this time** — the 2026-08-15 ground has held through three refusals and nothing new
    was offered against it
  extended: 2026-08-19 (again) — **the rule's two boundaries were settled**, and both are questions
    a reader arrives with rather than terms the corpus uses
    ([[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]],
    [[the-length-of-a-title-is-unbounded-and-no-check-measures-it]]). Nothing reached them: a
    question about a counting subheading had no way in at all — `подзаголовок`, `заголовок в тексте`,
    `body heading`, `число в подзаголовке` — and neither had a question about how long a title may
    be: `длина заголовка`, `длинный заголовок`, `ограничение длины`, `сколько символов`. Both are
    **closed** questions, so the aliases exist to deliver an answer rather than a gap, which is the
    one job a boundary page has
  extended: 2026-08-21 — the funnel a question travels was named end to end and the ritual's
    enumeration was ruled too narrow ([[the-folder-is-the-first-narrowing]],
    [[the-reading-funnel-is-delivered-as-a-procedure]],
    [[the-pre-task-enumeration-covers-every-folder-but-lessons]]). The words reached nothing:
    `воронка чтения`, `широкая половина`, `перечислить фронтматтер`, `какие папки читает план`.
    `funnel`, `enumeration` and `catalogue` were each considered as tags of their own and kept
    above as aliases — every one of them is a question about what a search reaches, which is what
    this tag is defined as
  extended: 2026-08-22 — **the funnel stopped being prose in one agent and became a rendered rule**
    ([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]), delivered to
    the librarian and to the new `pre-task` agent from one page. The words of *the shared half*
    reached nothing: `общая дисциплина чтения`, `shared reading discipline`, `правило чтения`,
    `как читать хранилище`, `дисциплина чтения`, `один текст в двух агентах`,
    `второй читающий агент`, `second reading agent`, `сужение перед открытием`,
    `narrow before opening`, `потолок в десять страниц у топикового запроса`,
    `ceiling is about topic queries`, `исключение для pre-task`, `pre-task carve-out`.
    **`reading-discipline` was considered as a tag of its own and rejected** — what the discipline
    protects is what a question reaches, which is this tag's definition word for word

- tag: external
  definition: the subject of the page is something this project does not own — a job site, a
    runtime, a vendor tool, another team's spec toolkit. **It is about the subject, never about
    what the page rests on**: `basis: external` means the page argues from an article or vendor
    documentation, and the two sets overlap without coinciding — a page about Docker Desktop
    measured on this machine is `basis: measurement` and external in subject, and a page about our
    own injector argued from an upstream changelog is `basis: external` and internal in subject
    ([[the-pages-about-what-this-project-does-not-own-get-one-shared-tag]]).
    Ruled by the owner on 2026-08-23 — «все внешние описать одним тегом "external"» — and
    deliberately left unminted that day, because a tag selecting nothing is a dead tag. **Minted at
    the ingest of the second session of that day, on his one-word instruction «отчекань»**, and
    applied to one page rather than to the set: which of the pages about PowerShell, Docker,
    work.ua, dou.ua, htmx, Claude Code and Playwright belong in it is a judgement about the corpus
    and goes to `/vault-lint` ([[dynamic-tag-classification-by-a-skill]]).
    The set it is meant to gather cuts across `entities/` and `concepts/`, which is exactly why it
    is a tag and not a folder: the folder answers *what kind of knowledge is this* and the tag
    answers *what is it about* ([[the-folder-is-the-first-narrowing]])
  aliases: [внешнее, внешний, внешние, external, чужое, не наше, not ours, стороннее,
    третья сторона, third party, вендор, vendor, чужая система, чужие системы, foreign system,
    один тег на всё внешнее, внешние страницы, external pages, что мы не контролируем,
    what we do not own, апстрим, upstream, внешний инструмент, external tool,
    Obsidian CLI, обсидиан, спек-кит, openspec, spec-kit, Docker, PowerShell, htmx, Playwright,
    work.ua, dou.ua, площадка, job site]

- tag: harness
  definition: the files that instruct an agent before it does anything — both `CLAUDE.md` files, the
    skills, the agents, the hooks and `settings.json` — taken as a **subject of their own**: who
    owns them, how a rule reaches them, and how they go stale. Minted 2026-08-16, when the harness
    became a build product rather than a maintained set of files
    ([[the-harness-is-compiled-not-maintained]]) and the seventh divergence between a harness file
    and the corpus was recorded ([[no-rule-reads-a-harness-file]]). `rules`, `injector`,
    `templates` and `config` were each considered and are kept below as aliases instead. It is
    **not** a synonym for `process`: `process` is how we work, this is the files that tell an agent
    how to work, and every recorded staleness in this project has lived in one of them
    Extended 2026-08-25: `measurement` was considered as a tag for the measure section and its
    writer script and rejected — the section is a record shape (`record-schema`) and the script
    is a harness file, and no page needs a third word.
    Extended 2026-08-30 (the ingest of the session that gave a decision a target and the reply a
    form) — the seventeenth rule page landed and the vocabulary of the reply format reached nothing:
    `формат общения`, `reply format`, `форма ответа`, `один кейс`, `one case`, `схема кейса`,
    `case schema`, `не переходить к следующему кейсу`, `no next case`, `фронтир`, `frontier`,
    `нумерованный список`, `numbered list`, `дважды за сессию`, `walked twice`,
    `маркеры ставит сессия`, `who marks the region`, `две стороны посадки правила`.
    **`frontier` and `reply-form` were each considered as tags and are aliases instead**: the first
    is a working concept whose three carriers are three existing subjects — the sprint, the brief and
    a skill — and the second is the shape of a message, which is what `process` already covers
    ([[the-reply-is-a-report-answers-and-one-case]],
    [[the-frontier-is-one-concept-with-three-carriers]],
    [[a-decision-with-a-rule-target-cannot-close-inside-a-single-ingest]]).
    Extended 2026-08-30 (the ingest of the session that made a rule findable by lookup) — a rule
    gained a delivery that renders into no file, a fourteenth hook appeared, and none of the
    vocabulary reached a page: `доставка правила`, `rule delivery`, `по слугу`, `lookup`,
    `render authority`, `правило о правилах`, `rule about rules`, `serve-the-rule`,
    `семейство запретов`, `prohibition family`, `правило против запрета`.
    **`rule-delivery` and `hooks` were each considered as tags and are aliases instead**: the first
    is one property of a rule page, which this tag is already the subject of, and the second would
    split a fourteen-member family off the harness for no question a reader asks differently
    ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]],
    [[the-rule-server-hook]],
    [[a-rule-differs-from-a-prohibition-by-having-an-address-and-by-nothing-else]]).
  aliases: [обвязка, харнесс, оснастка, конфигурация агента, agent config, файлы правил,
    доставка правила, rule delivery, по слугу, lookup, найти правило по authority,
    render authority, правило которое никуда не рендерится, правило о правилах, rule about rules,
    serve-the-rule, serve-the-rule.ps1, хук выдаёт правило, семейство запретов,
    prohibition family, правило против запрета, rule versus prohibition, rule-delivery, hooks,
    ветка по authority, authority matcher, matcher Read, ServedRuleFiles, served-rule,
    формат общения, reply format, форма ответа, отчёт о действиях, один кейс, one case,
    схема кейса, case schema, не переходить к следующему кейсу, no next case,
    фронтир, frontier, нумерованный список, numbered list, дважды за сессию, walked twice,
    маркеры ставит сессия, who marks the region, две стороны посадки правила, two parties,
    правило не садится в одну сессию, reply-form, наследство сессии, не читать прошлый handoff,
    rule files, правило как страница, rule page, rules, wiki/rules/, инжектор, injector,
    внедрение правил, inject, зона, zone, per-directory CLAUDE.md, CLAUDE.md по директориям,
    маркер, marker, размеченный регион, marked region, регион, region, разметка, markup,
    render, рендер, отрендерить, whole-file render, settings.json, governs, asserts, предикат,
    predicate, закрытый набор предикатов, harness-build, harness-gate, harness-layout, шлюз,
    gate, ворота, гейт, симлинк, symlink, ln -s, core.symlinks, копия вместо ссылки,
    hooks, хуки как класс, три хука, smoke gate, gate-the-handoff.ps1, record-the-smoke.ps1,
    remind-the-smoke.ps1, подпись Compiled from, compiled from, Makefile, make, цель make,
    скилл против решения, skill contradicts a decision, расхождение скилла, стюард, steward,
    шаблон, template, .claude/templates/, check-the-journal.ps1, PostToolUse, UserPromptSubmit,
    гейт на журнал, journal gate, ворота на журнал, транзитный файл, transit file,
    .superpowers/sdd/retro.md, шаблон ретро, retro template, найти bash, WSL shim, matcher,
    subagent_type, замок на диспатч, lock on dispatch, шаблон хендоффа, handoff template,
    секция Harness, vault-inject.sh, --check, отрендерить правило, слайс, срез, вырезка,
    marked slice, размеченный кусок, что уезжает со страницы, what travels, text slice,
    маркер текста, правило 11, правило 12, rule 11, rule 12, номер правила, rule number,
    правило 9, rule 9, отозванное правило, retired rule, переиспользовать номер, renumber,
    advisory, предупреждение, покрытие регионами, region coverage, 0 of 13, подметание, sweep,
    swept, обход файлов, governed set, управляемый набор, режим whole, whole mode, целиком,
    отрендерить файл целиком, миграция правила, rule migration, перенос правила,
    первое правило, first rule page, какое правило переехало, migrated rule, правило четыре,
    rule 4, уникальность governs, governs uniqueness, два правила на один файл,
    two rules one destination, один регион на файл, region per file, оставшиеся правила,
    remaining rules, гейт красный, gate is red, жёсткий перенос, hard break,
    два пробела в конце, trailing spaces, пробелы в конце строки, побайтово, byte for byte,
    байт в байт, byte-equal, пустой дифф, empty diff, фенс в слайсе, fenced block in a slice,
    блок кода в правиле, code fence, длина строки в правиле, Makefile, make, мейкфайл,
    make check, пайплайн, pipeline, конвейер, диспатчер, dispatcher, do.sh, список команд,
    command list, какие команды запускать, генератор, generator, сгенерировать регион,
    регион из дерева, generated region, из дерева, тип в маркере, type in the marker,
    полный адрес, complete address, адрес в вики, инертное поле, silently inert,
    поле ничего не делает, ни рендер ни отказ, адресный вердикт, address verdict,
    регион не в том файле, region in the wrong file, оставшаяся копия, leftover copy,
    дубликат региона, два направления, two directions, карта в CLAUDE.md,
    что удалили из CLAUDE.md, где что лежит, where things are, номер правила в списке, ordinal,
    порядковый номер, нумерованный список, карта рендерится, map region, регион карты,
    карта как страница, map as a page, определение может рендериться, definition may render,
    описательная страница, descriptive record, первое предложение, first sentence,
    вики-ссылка в слайсе, wikilink in a slice, сепаратор, separator, разделитель,
    пустая строка после слайса, blank line after the slice, пустая строка между регионами,
    blank line between regions, абзацный отступ, paragraph break, идемпотентность региона,
    idempotent region, форма региона, rendered form, одна переменная, комментарии вырезаются,
    comments are stripped, HTML-комментарий, block comment, сколько стоит маркер, marker cost,
    байты на диске, bytes on disk, хвостовой перевод строки, trailing newline,
    подстановка команды, command substitution, сентинел, sentinel, слепое сравнение,
    blind comparison, гейт не сравнивал, MessageDisplay, событие отображения сообщения,
    message_id, delta, final, index, ловец фидбека, catch-the-feedback.ps1, поймать фенс,
    fenced block, VAULT-FEEDBACK, сказать в ответе, spoken in the reply, хук вместо записи,
    hook instead of a write, транскрипт, transcript, стенограмма сессии, session-dialogue.py,
    извлечь диалог, session-transcript.path, третий транзитный файл, third transit file,
    зонд хука, probe hook, побочный эффект зонда, ротация леджера, restamped the session, *.py,
    пин питона, python pin, закрепить py, LF для py, единственное число, singular,
    множественное число, plural, слово типа, type word, выметено с дерева, swept off the tree,
    легальность выводится, legality is derived, .claude/rules/, paths-скоуп, paths scope,
    условная доставка, conditional delivery, правило по пути, path-scoped rule,
    InstructionsLoaded, загрузка правил, rules loading, правило не доедет,
    a rule that never loads, ветка гейта, gate branch, nogoverns, ruleclaim,
    authority рядом с governs, authority beside governs, правка руками внутри региона,
    hand-edit inside a region, регион переписывается целиком, зонд, probe, нонс, nonce,
    path_glob_match, причина загрузки, load reason, файл правил генерируется, generated file,
    маркер генерации, generated marker, удаление по маркеру, marker-guarded deletion,
    править руками запрещено, paths на странице, синхронизация paths, самый широкий паттерн,
    widest pattern, частотный кэш, frequency cache, как часто спрашивают правило, Core,
    ядро CLAUDE.md, что бутстрапит вопрос, что необратимо, убрать правило из CLAUDE.md,
    правило JavaScript уезжает, одиннадцатый регион, регистр в чате,
    инструкция о регистре joins the slice, ветка в хуке, hook branch, additionalContext,
    дополнительный контекст, правило приходит дважды, rule arrives twice,
    латентность на каждую правку, latency per edit, процесс уже спавнится,
    already spawned on every edit, незаполненный шаблон, unfilled template,
    шаблон ретро не заполнен, YYYY-MM-DD, токен вердикта, verdict token, словарь дренажа,
    drain vocabulary, вид обратной связи, feedback kind, vault-feedback.md, страж, guard,
    сторожевая ветка, guard branch, второй триггер, second trigger, правило после компакта,
    rule after a compact, перевыдача правила, re-delivery, режим whole построен,
    whole mode built, генерируемый файл, ast-boundaries.md, правка сгенерированного файла,
    hand edit of a generated file, красный вердикт, red verdict, удаление по маркеру построено,
    sweep of destinations, осиротевший файл, orphaned file, values, набор значений,
    legal values, значение вне списка, basis banana, перечисление значений, value enumeration,
    схема значений, render обязателен, render required, режим доставки, delivery mode,
    критерий шесть, criterion wording, полностью сгенерирован, fully generated, советующий хук,
    advisory hook, хук блокирует, blocking hook, может ли хук отказать, необратимое действие,
    irreversible action, отказ не может быть ошибкой, harness: как вид, harness kind,
    пятый вид, fifth feedback kind, замок, lock, отказ хука, hook refusal, deny,
    permissionDecision, условный отказ, conditional refusal, абсолютный отказ,
    absolute refusal, Agent, Task, инструмент диспатча, dispatch tool, SubagentStart,
    PreToolUse matcher, хуки в сабагенте, hooks in subagents, --lint, флаг линта, lint flag,
    код выхода 2, exit 2, неизвестный аргумент, unknown argument, vault-archive.sh,
    скрипт архивации, archive script, переписать sources, rewrite citations, vault-relative,
    путь от корня вики, путь от корня репозитория, repo-relative, тяжесть вердикта, severity,
    note против echo, взаимоблокировка, deadlock, тупик, gate deadlock, замок против правила,
    lock versus rule, кто чистит красный гейт, who clears a red gate, аварийный выход из замка,
    escape hatch, обратная кавычка, backtick, экранирование в PowerShell, PowerShell escape,
    сломанная команда, mangled command, отказ называет несуществующую команду, ash scripts,
    двойная кавычка, отсутствующий render, absent render, красный за отсутствие поля,
    порядок изменения схемы, schema change order, неизвестный ключ красный, unknown key is red,
    сначала схема потом страница, канал вывода инжектора, injector channel,
    только красный канал, no advisory channel, values при допуске поля, values on admission,
    поле допущено во вторую папку, режим планирования, plan mode, ExitPlanMode,
    выход из режима плана, план на утверждение, plan approval, PostToolUse на инструменте,
    режим разрешений, permission mode, permissions.defaultMode,
    claudeCode.initialPermissionMode, пользовательские настройки, user settings,
    настройки воркспейса, workspace settings, сообщение хука, hook message,
    .claude/hooks/messages/, доставка правила хуком, правило в сообщении,
    rule delivered by a hook, режим whole без paths, без фронтматтера, no frontmatter block,
    триггер pre-task, pre-task trigger, когда запускать pre-task, точка ритуала,
    moment of the ritual, склейка глоба, glob anchoring, ведущая звёздочка, leading star,
    путь без префикса, unprefixed path, дот-сорс, dot-source, библиотека хука, hook library,
    не зарегистрирован, registered nowhere, ротация, rotation, ротировать, rotate,
    обнулить ledger, reset the ledger, архив ledger, ledger archive, .superpowers/sdd/ledger/,
    один файл на сессию, one file per session, per-session file, удержание, retention,
    сколько хранить, how long to keep, ничего не подрезает, nothing prunes it, session-start,
    source, startup, resume, строка старта сессии, session-start row, перенос файла целиком,
    whole-file move, read-modify-write, чтение-изменение-запись, append-only, только дозапись,
    гонка читателя, reader race, третье значение, прочерк, dash, ничего не утверждает,
    asserts nothing, туман, fog, невидимость харнесса, harness visibility,
    не понимаю что происходит, I do not understand what is happening, карта харнесса,
    harness map, сгенерированная карта, generated map, показать что происходит,
    make it visible, четыре направления, язык карты, language of the map, governs списком,
    governs takes a list, список назначений, inline list, блочная форма, block form,
    красный вердикт на блок, одна форма списка, реестр хуков, hook register,
    какие хуки отказывают, which hooks refuse, hook-selftest.ps1,
    PreToolUse единственное событие, только PreToolUse, событие не может отказать,
    permissionDecision, deny, три условия отказа, измеримое условие, как снять отказ,
    refusal says how to clear it, ветка которую корпус не проходит, unexercised branch,
    гейт зелёный ни о чём, зависимость, dependency, зависимости, dependencies, pyproject.toml,
    uv.lock, PyYAML, транзитивная зависимость, transitive extra, dev dependency,
    объявить зависимость, record-the-dispatch.ps1, запись диспатча, dispatch row,
    строка о диспатче, вердикт про блочный governs, block list, --lint, за флагом lint,
    --rules, --list, --only, режим, mode, фильтр, filter, реестр правил, rule register,
    печатать реестр, printed register,
    vault-measure.py, скрипт пишет число, the script writes the number, refresh датчиков, режим без вердикта, subset mode, объединить хуки, hook pipeline, исключить _schema.yaml, отдельный флаг для заметки, .claude/rules для правил вики, closed_by, чем закрыто правило,
    правило 15, rule 15, гейт запускает скрипт, gate runs a script, читает строки а не код возврата,
    reads lines not the exit code, делегированное правило, delegated rule,
    список копирования песочницы, sandbox copy list, восьмой скрипт, копируется по имени,
    missing file, все чистые кейсы красные, all clean cases red,
    обратные кавычки в регионе, backticks in the region, команда с пайпом, command with a pipe,
    как пишется measure, spelling of the region, чтение после кавычки,
    четыре состояния меню, four menu states, прерывание это ответ, interrupt is an answer,
    resolve_menus, меню без ответа, lost menu,
    писать файл только Write, write with the tool, не через heredoc, never through a shell,
    sed вместо Write, перевод строки съел файл, text mode round trip, read_text write_text,
    перепись CR, CR census, скрытые байты, invisible bytes,
    зонд по реальному дереву, plant and revert, реестр побочных эффектов хуков,
    снять сторож целиком, if false, мутация не полная, incomplete mutation,
    pwsh нет на машине, no pwsh, powershell -NoProfile -File, Windows PowerShell 5.1,
    не-ASCII в хук, non-ASCII payload, восемь знаков вопроса, UTF-8 файл вместо пайпа,
    фоновая задача жива или мертва, buffered stdout, буферизованный вывод,
    suite в фоне на ретро, suite in the background, шаг 0 ретро,
    архиватор, archiver, status archived, свип по lessons, цикл уроков, lessons cycle,
    счётчик очереди уроков, queue counter, пол очереди, queue floor,
    политика архивации, archiving policy, бесконечный рост, endless growth]
  since: 2026-08-16
  extended: 2026-08-26 — the harness half of the committed plan was built. `measurement`,
    `archiving` and `encoding` were each considered as tags and rejected: a measure region is a
    record shape, an archiver is a vault script, and an encoding defect is a fact about the shell.
    The words that reached nothing before this ingest: `гейт запускает скрипт`,
    `список копирования песочницы`, `не через heredoc`, `перепись CR`, `pwsh нет на машине`,
    `фоновая задача жива или мертва`, `цикл уроков`
  extended: 2026-08-17 — a third hook was written and the forms moved into `.claude/templates/`
  extended: 2026-08-20 (second) — the lock fired for the first time and deadlocked against the
    one-writer rule, an escape ate the command inside a refusal, and the `render:` default was
    removed in the order the gate's key set forces. `deadlock`, `escaping` and `injector-severity`
    were each considered as tags and kept above as aliases instead: all three are facts about the
    files that instruct an agent
    ([[the-journal-gate-hook]], [[claude-templates-directory]]). `hooks` and `templates` were
    considered again as tags of their own and rejected again: a hook and a template are both files
    that instruct an agent, which is this tag. The words that reached nothing before:
    `check-the-journal.ps1`, `PostToolUse`, `UserPromptSubmit`, `transit file`, `subagent_type`
  extended: 2026-08-17 (second session) — the regions and the injector were **built**
    ([[a-region-is-a-paired-comment-named-for-a-rule]],
    [[what-travels-from-a-rule-page-is-a-marked-slice]],
    [[the-governed-set-is-swept-and-markdown-by-property]]). The vocabulary of *what a rule page
    ships* reached nothing at all: `слайс`, `срез`, `вырезка`, `что уезжает со страницы`,
    `text slice`. So did the vocabulary of *a rule by its number*: `правило 11`, `номер правила`,
    `отозванное правило` ([[a-retired-rule-number-is-never-reused]]). **`rules`, `regions`,
    `injector` and `markup` were each reconsidered as tags of their own and rejected again**, on
    the 2026-08-16 ground unchanged — a region, a slice and a renderer are all machinery for
    getting a rule into a file that instructs an agent, which is what this tag is defined as.
    `advisory` was considered and rejected too: it is already an alias of `vault`, where it means
    the check's density lines, and rule 11's advisory is the same instrument
    ([[an-advisory-prints-one-line-and-sorts-what-it-names]])
  extended: 2026-08-21 — the pre-task ledger acquired a retention rule and an archive folder, and
    the owner reported that he cannot see the harness at all. `ledger-rotation`, `retention` and
    `visibility` were each considered as tags of their own and kept above as aliases: a rotation
    policy and a map of the hooks are both facts about the files that instruct an agent
    ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]],
    [[the-ledger-archive-directory]], [[the-harness-is-no-longer-visible-to-its-owner]],
    [[a-generated-harness-map]]). The words that reached nothing: `ротация`, `обнулить ledger`,
    `session-start`, `туман`, `карта харнесса`
  extended: 2026-08-17 (third session) — **the first rule page was written**
    ([[the-owner-decides-how-a-slice-is-executed]]), which is the migration this machinery was
    built for. The vocabulary of the move itself reached nothing: `миграция правила`,
    `перенос правила`, `первое правило`, `какое правило переехало`. `migration` was considered as
    a tag of its own and rejected — moving a rule out of a harness file and into a page it is
    rendered back from is this tag's whole subject, and the words are aliases instead
  extended: 2026-08-17 (after the first rule page) — the remaining rules of the repository's
    `CLAUDE.md` became pages ([[the-suite-never-runs-against-the-production-database]],
    [[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]],
    [[our-javascript-does-not-choose-which-rows-are-on-screen]]), and the migration hit the
    uniqueness of `governs:` ([[a-deprecated-rule-does-not-render]]). The words of that collision
    reached nothing: `уникальность governs`, `два правила на один файл`, `один регион на файл`,
    `гейт красный`. `collision` and `uniqueness` were considered as tags of their own and rejected —
    what `governs:` may name is a question about how a rule reaches a harness file, which is what
    this tag is defined as
  extended: 2026-08-17 (second migration) — five more blocks of the repository's `CLAUDE.md` became
    pages ([[english-in-the-repository-russian-with-the-owner]],
    [[a-pre-task-runs-before-anything-non-trivial]],
    [[ask-before-weakening-or-working-around-a-rule]],
    [[a-session-ends-with-retro-then-handoff-then-ingest]],
    [[write-the-miss-into-vault-feedback-before-the-turn-ends]]), and the migration met the
    **byte fidelity** of a slice: one rule carries markdown hard breaks — trailing double spaces
    that are content — and another cannot render at all until a fenced code block inside a
    `<!-- text -->` slice survives the injector. The vocabulary of that reached nothing:
    `жёсткий перенос`, `два пробела в конце`, `побайтово`, `пустой дифф`, `фенс в слайсе`.
    `fidelity` was considered as a tag of its own and rejected — it is already an alias of
    `testing`, where it means what a page's claim is worth against its source, and this is about
    whether a rule's text arrives unchanged, which is machinery for getting a rule into a harness
    file. The words for *asking before weakening a rule* went to `process` instead, since that is a
    question about how we work rather than about the files
  extended: 2026-08-17 (third session, the rules leave the prose) — the migration finished, the
    uniqueness of `governs:` was **removed** rather than deferred
    ([[governs-uniqueness-is-removed-and-the-pair-carries-it]]), and three unbuilt mechanisms were
    designed: field-driven injection, a generator that fills a region from the tree, and a `Makefile`
    ([[the-marker-carries-a-type-and-governs-is-read-as-a-field]],
    [[a-generator-fills-a-marked-region-from-the-tree]], [[a-makefile-holds-the-projects-pipelines]]).
    The words of all three reached nothing: `генератор`, `пайплайн`, `мейкфайл`, `тип в маркере`,
    `полный адрес`, `инертное поле`, `регион не в том файле`, `оставшаяся копия`, `два направления`.
    **`make`, `makefile`, `generator`, `address` and `marker-type` were each considered as tags of
    their own and rejected** on the 2026-08-16 ground unchanged — a command list, a generator and a
    marker are all machinery for getting text into a file that instructs an agent. `Makefile` is filed
    here and **not** under `testing`, even though `make check` would run the suite: the artefact is a
    harness file, and what it runs is a different question
  extended: 2026-08-18 — field-driven injection was **built** at `e83ce28`, and the first record
    outside `wiki/rules/` rendered: the map
    ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
    [[governs-becomes-a-property-of-any-page]], [[the-marker-carries-the-records-type]]). The
    vocabulary of a *descriptive* record that ships text reached nothing: `карта рендерится`,
    `map region`, `карта как страница`, `определение может рендериться`, `описательная страница`,
    `первое предложение`, `вики-ссылка в слайсе`. **`map` was considered as a tag of its own and
    rejected**: bare «карта» is already an alias of `process`, and `карта в CLAUDE.md` has been an
    alias here since 2026-08-17 — a map rendered into a file that instructs an agent is this tag,
    and the phrase is what separates them
  extended: 2026-08-18 (the ingest of that session) — the injector changed four times and the gate
    turned out not to be comparing what it claimed
    ([[the-injector-writes-the-separator-inside-the-region]],
    [[a-command-substitution-strips-the-newline-a-gate-compares]],
    [[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]],
    [[block-comments-are-stripped-before-claude-md-reaches-the-model]]), and conditional delivery
    was designed ([[moving-a-rule-into-claude-rules-with-a-paths-scope]]). The vocabulary of the
    separator, of the blind comparison and of a path-scoped rule reached nothing at all:
    `сепаратор`, `пустая строка после слайса`, `хвостовой перевод строки`, `подстановка команды`,
    `сентинел`, `paths scope`, `условная доставка`, `InstructionsLoaded`, `nogoverns`, `ruleclaim`.
    **`injection`, `separator`, `rendering` and `rules-loading` were each considered as tags of
    their own and rejected** on the 2026-08-16 ground unchanged — how text gets into a file that
    instructs an agent, and whether it arrives at all, is what this tag is defined as. `newline` and
    `whitespace` were considered and rejected too: `жёсткий перенос` and `два пробела в конце` have
    been aliases here since 2026-08-17 and this is the same subject one byte over
  extended: 2026-08-18 (second session) — the probe that measures conditional
    delivery ([[the-conditional-delivery-probe]]), the design for generating a governed file whole
    ([[generating-a-claude-rules-file-whole-from-its-vault-page]]), the criterion for what stays in
    `CLAUDE.md` ([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]) and the
    refusal of a frequency cache ([[no-frequency-cache-for-claude-md]]). The words reached nothing:
    `зонд`, `нонс`, `path_glob_match`, `маркер генерации`, `частотный кэш`, `Core`,
    `самый широкий паттерн`. **`probe`, `generation`, `core` and `caching` were each considered as
    tags of their own and rejected** — a measurement of the delivery mechanism, a writer for a
    governed file, and a rule about which rules arrive unconditionally are all questions about the
    files that instruct an agent, which is what this tag is defined as
  extended: 2026-08-19 (third) — a guard for a path-scoped rule turned out to be a branch in a hook
    that already spawns, and the drain's vocabulary was found to disagree with the template that
    routes it

*(**Extended 2026-08-20**, at the ingest of the guard-and-conditional-delivery session. Candidate
words considered and **rejected as tags**, kept as aliases above: `guard` and `hooks` — a hook and a
branch inside one are files that instruct an agent, which is `harness`; `line-endings` — one class
of defect, not a subject, and it is already reachable through `harness` and `testing`;
`archive` — a directory of the vault, which is `vault`; `blocking` — a property of a hook, and the
question *may a hook refuse* is answered under `harness`. The Russian words that a real question
about this session's work would use and that reached nothing before: `страж`, `второй триггер`,
`правило после компакта`, `значение вне списка`, `тихий grep`, `чужой файл в git status`,
`инструкция по сносу`, `папка на сессию`, `скрипт а не агент`.)*

*(**Extended 2026-08-20**, at the ingest of the session that parallelised the suite and locked the
librarian dispatch. Candidate words considered and **rejected as tags**, kept as aliases above:
`concurrency` and `parallel` — a property of one script, and every question about it is a question
about the harness or about testing; `refusal` — a shape a hook takes, which `harness` already
carries; `scouts` — a class of subagent, which is `agents`; `english` and `language` — the
translation ruling is about how we work, which is `process`, and the page it narrows is reached by
its own filename; `archive`, rejected again for the reason it was rejected on 2026-08-19 — it is a
directory of the vault, which is `vault`. The Russian words a real question about this session's
work would use and that reached nothing before: `замок на библиотекаря`, `отказ с условием`,
`параллельный прогон`, `порог параллельности`, `разведчики по папкам`, `охранник тестовой базы`,
`ротация лога`, `переписать цитаты`, `редактировать работающий скрипт`, `падает в ноль`,
`неверная диагностика`.)*
  extended: 2026-08-20 (third) — the pre-task ritual acquired a moment, an artefact and a hook,
    and the vocabulary of plan mode reached nothing at all: `ExitPlanMode`, `режим планирования`,
    `режим разрешений`, `сообщение хука`, `.claude/hooks/messages/`. `plan-mode`, `permissions`,
    `hooks` and `ledger` were each considered as tags of their own and rejected — a hook, a
    permission mode and a generated message file are all files or events that instruct an agent
    before it does anything, which is what this tag is defined as
    ([[the-plan-check-hook]], [[a-pre-task-runs-between-the-plan-and-its-approval]],
    [[paths-is-required-where-it-is-read-and-nowhere-else]])  extended: 2026-08-22 (the ingest of the strike) — a field acquired a reader nobody had counted and
    a command answered half of itself, and the vocabulary of both reached nothing: `третий парсер`,
    `third parser`, `сколько читателей`, `кто ещё читает поле`, `список как тест`,
    `list that is a test`, `съел флаг`, `дропнул аргумент`, `ответил на половину`,
    `неразрешимый критерий`, `команда-решатель`, `decider`, `не посчитанный кейс`,
    `uncounted case`, `аллокатор в подоболочке`, `next_rf`. `parsers`, `readers` and `decider` were
    each considered as tags of their own and kept as aliases: a field's readers and the command a
    criterion names are both files that instruct or check the harness
    ([[the-count-of-a-fields-readers-lives-nowhere]],
    [[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]],
    [[no-verdict-lives-in-a-variable-in-a-parallel-suite]])
  extended: 2026-08-23 (the ingest of the session that struck three refusals) — this store was read
    against published prior art for the first time, and no word of that vocabulary reached anything:
    `openspec`, `spec-kit`, `speckit`, `spec-driven`, `SDD`, `чужие инструменты`, `prior art`,
    `аналоги`, `converge`, `opsx`, `verify`, `flow-forward`, `пакетирование метода`, `extensions`,
    `presets`, `проверка корпуса против кода`, `corpus versus code`, `lifecycle hooks`. Also from
    the same session: `правило без инструмента`, `unchecked rule`, `у правила должен быть дом`,
    `механически`, `пять правил`, `SessionEnd`, `Stop hook`, `счётчик диспатчей`,
    `гейт на английский`, `седьмой отказ`, `precondition`, `живая страница ссылается на слаг`.
    `prior-art` and `instrument` were each considered as tags and are aliases instead: the first
    names one session's reading rather than a subject, and the second is what `testing` already
    covers ([[openspec-and-spec-kit]], [[every-rule-in-wiki-rules-owes-a-mechanical-instrument]],
    [[vault-archive-sh]])
  extended: 2026-08-29 (the ingest of the first sweep) — the hooks around the feedback channel were
    rearranged and the words for it reached nothing: `один хук владеет требованием`,
    `one hook owns the requirement`, `вторая регистрация`, `second registration`,
    `порог молчания`, `silence threshold`, `счётчик ответов`, `reply counter`,
    `MessageDisplay не может говорить`, `the event cannot speak`, `зонд`, `probe`,
    `ритуальная ветка`, `ritual branch`, `перезапуск не нужен`, `no restart needed`,
    `форма вопроса владельцу`, `question shape`, `с контекстом и рекомендацией`.
    `hooks` and `probe` were each considered as tags and are aliases instead: a hook is machinery of
    the harness, and a probe is one way of measuring it
    ([[the-feedback-requirement-is-owned-by-one-hook-and-registered-on-each-event-it-needs]],
    [[the-reply-silence-counter-is-split-between-the-hook-that-sees-and-the-hook-that-speaks]],
    [[a-hook-on-message-display-cannot-speak-to-the-session]],
    [[every-question-put-to-the-owner-carries-context-and-a-recommendation]])
