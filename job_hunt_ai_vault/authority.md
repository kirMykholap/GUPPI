# Authority dictionary

`authority:` is the index a claim is looked up in **before** a page is written
([[authority-becomes-the-index-and-is-required-outside-rules]]). The admission rule is decided by
that lookup — no new page where an existing one can carry the claim
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]) — and looking up four hundred flat
slugs is not a lookup. **A family is.** This file turns *does this claim already have a page* into
*read these nine pages and decide*, which is a question a reader can answer.

**Which slugs exist is in the tree and needs no file. Which slugs answer the same question is
nowhere and cannot be derived** — not from the frontmatter, not from the folder, not from the words
in the slug. That is why this is a hand-written register rather than a generated list, and it is
exactly the standing `tags.md` has.

**The half that IS derivable is the half that drifts**, so it is audited rather than trusted:

```
bash scripts/vault-authority.sh --check          # the register against the tree, both directions
bash scripts/vault-authority.sh --near <slug>    # the family a candidate belongs to
bash scripts/vault-authority.sh --group <name>   # the members of one family, with their titles
```

**Slugs are written as plain text and never as `[[wikilinks]]`.** A register that linked every page
would join the link sweep of rule 5, and then no page in this vault could ever be an orphan again —
the orphan rule would run, pass, and prove nothing. That is the trap the generated catalogue
carried and part of why it was replaced by a query ([[the-index-is-a-map-not-a-catalogue]]). The
spelling is load-bearing and is not a formatting preference.

**A family is grouped by the question, never by the vocabulary.** `ledger-retention` and
`ledger-archive` share a word and belong together; `map-admission` and `where-things-are` share none
and answer the same question. Two slugs belong in one family when a reader asking about one would
need to have read the other.

**Every slug is in exactly one family and none is left over.** A slug in two families makes the
lookup ambiguous in the direction that hides a page — whichever family is read first answers, and
the other is never opened. A slug in no family is a page the lookup cannot reach, which is the
defect this register exists to remove, so there is no `misc` bucket here and there never may be.

**Aliases carry the Russian**, for the same reason `tags.md` carries its own: retrieval is grep, the
corpus is English and the questions often are not
([[aliases-carry-the-question-across-languages]]).

## Families

- group: the two job sites
  definition: what each source gives us, what it does that nothing else does, and how a raw listing
    becomes a stored vacancy. Answers "where does a vacancy come from, and what is odd about it
    there".
  slugs: [work-ua-source, dou-source, http-cache-side-effect, request-politeness, collection-modes,
    description-fullness-producer, field-overwrite-rules, salary-reparse]
  aliases: [work.ua, dou.ua, доу, воркуа, источник, источники, source, сайт вакансий, парсер,
    парсинг, зарплата, salary, вежливость, rate limit, пагинация, csrf, cookie, куки]

- group: a collection run
  definition: what starts a run, what finishes it, what it may not do, and what state it leaves in
    the database. Answers "what happens when I press collect".
  slugs: [collection-execution, batch-finalisation, run-interruption-policy, collection-deferrals,
    startup-sweep-coverage, staleness-window, summary-line-content]
  aliases: [сбор, сбор вакансий, collection, запуск сбора, батч, batch, прогон, run, поток,
    daemon, прерывание, перезапуск, свежесть, staleness, итог сбора, сводка]

- group: a vacancy that disappeared
  definition: how we decide a vacancy is gone, what that decision is scoped to, and when it must be
    refused. Answers "why did this row go grey, or why did it not".
  slugs: [deactivation-rules, deactivation-scope, empty-listing-handling, frame-source-of-truth,
    city-frame-matching, orphan-deactivation]
  aliases: [деактивация, deactivation, исчезла, пропала вакансия, закрыта, рамка сбора, frame,
    город, city, пустая выдача, сирота, orphan]

- group: the vacancy table
  definition: which rows are on screen, in what order, under which profile, and what the columns
    say. Answers "why is this row here, or here rather than there".
  slugs: [vacancy-list-rules, list-ordering-source, tag-condition-placement, tag-deletion,
    cleared-chips-vs-fresh-page, chip-state-after-collection, profile-selection,
    profile-name-uniqueness, status-vocabulary, time-display]
  aliases: [таблица вакансий, список, фильтры, filters, сортировка, sorting, чипы, chips, теги,
    tags, профиль, profile, статус, status, время, дата, страница списка]

- group: the two pages and how they update themselves
  definition: the shell, the swaps, the polling and the address bar — the htmx mechanics of the
    interface, and how a claim about the screen is checked. Answers "how does the page change
    without a reload".
  slugs: [shell-and-pages, error-swap-safety, address-bar-updates, empty-state-recovery,
    swap-target-invariant, post-collection-refresh, idle-page-polling, restart-to-see-changes,
    browser-harness, browser-walk-method]
  aliases: [htmx, свап, swap, обновление страницы, поллинг, polling, адресная строка, url,
    пустое состояние, empty state, шаблон, jinja, браузер, browser, playwright, перезапуск uvicorn]

- group: the front end's stack
  definition: what is deliberately not adopted in the browser, and what our own JavaScript may and
    may not do. Answers "may I write this in the browser".
  slugs: [frontend-stack, js-scope, javascript-rule-delivery, table-rendering-approach,
    stylesheet-approach]
  aliases: [JavaScript, JS, свой JS, React, фронтенд, фреймворк, framework, грид, grid, стили, CSS,
    палитра, дизайн-система, какие строки на экране, клиентский код]

- group: the application's own structure
  definition: the layers, the boundary tests that hold them, the database the suite runs against,
    and what has to be running at all. Answers "how is this codebase put together, and what keeps
    it that way".
  slugs: [boundary-tests, boundary-overclaiming, normalisation-boundary, migration-drift,
    entity-coverage, guard-enforcement-shape, test-database, test-database-guard, docker-startup,
    suite-hangs-without-a-database]
  aliases: [архитектура, architecture, слои, layering, границы, AST, миграции, migrations,
    тестовая база, TEST_DATABASE_URL, docker, докер, нормализация, модель, SQLAlchemy,
    suite висит, зависает, нет базы, docker не запущен, таймаут подключения]

- group: finding a page in this store
  definition: how retrieval works here, what the index is and is not, and why a search engine was
    not built. Answers "how do I find the page I need".
  slugs: [index-purpose, index-location, index-and-schema-roles, page-list-artefact,
    pages-base-review, compilation-vs-retrieval, retrieval-narrowing, vector-retrieval,
    vector-extension, alias-target-kinds, reading-funnel-delivery, authority-family-ceiling,
    catalogue-binding-column, authority-check-staleness, authority-check-asymmetry,
    register-rendering-design, authority-per-type-uniqueness, authority-family-grouping,
    cross-type-slug-as-graph, paired-authority-requirement, authority-convergence-pass]
  aliases: [поиск, retrieval, найти страницу, index.md, индекс, карта, map, каталог, catalogue,
    grep, ripgrep, векторы, vectors, эмбеддинги, embeddings, pgvector, сужение, narrowing, папка,
    алиас на страницу, цель словарной записи, слово ведёт на страницу, reading-funnel,
    funnel-delivery, catalogue-delivery, воронка чтения, как искать в vault, широкая половина,
    потолок в десять страниц, vault-catalogue.sh,
    устаревшая строка реестра, stale row, --check в обе стороны, both directions,
    асимметрия проверки, asymmetry, реестр рендерится со страницы, register rendered from a page,
    сходимость слагов, convergence, свести authority, свести слаги, объединить под одним slug,
    один slug на цепочку типов, chain of types, вручную пройтись по страницам, manual pass,
    у кого какой authority, кто несёт слаг, who carries the slug,
    507 слагов, archive в реестре,
    один слуг на несколько типов, per-type uniqueness, слуг внутри типа, same slug different types,
    цепочка одного вопроса, chain of one question, граф без поля Links, семейства authority,
    families, группировка корпуса, corpus grouping, парность concept и entity, required pair]

- group: the tag dictionary and the two languages
  definition: what a tag is for, when one is split or kept, and how a question asked in Russian
    reaches a page written in English. Answers "what do I call this, and in which language".
  slugs: [alias-purpose, batches-tag, schema-tag-split, standing-tag-advisories,
    term-transliteration, language-scope, english-migration-method, migration-warning-language,
    translation-remainder-scope, english-sweep-design, approval-plan-language,
    external-pages-grouping]
  aliases: [теги, tags.md, tag, алиас, aliases, синоним, русский, english, язык, language,
    перевод, транслитерация, словарь тегов, плотность тега, кириллица в тестах,
    фикстурные данные, product output, вывод пользователю, миграция на английский,
    что можно оставить по-русски,
    на каком языке план, план на русском, план на утверждение, approval plan, plan language,
    язык плана, план вне репозитория, .claude/plans, план который читает владелец,
    external, внешние страницы, что мы не контролируем, чужие системы,
    один тег на всё внешнее, PowerShell в двух папках, две папки на один предмет]

- group: the shell this repository is driven from
  definition: the quoting, the pipes, the exit codes and the encodings that have broken a script
    here. Answers "why did my command do something other than what it says".
  slugs: [awk-quote-hazard, backslash-through-a-generator, prose-transport,
    powershell-backtick-escape, powershell-append-bom, editing-a-running-script,
    sigpipe-under-pipefail, exit-code-through-a-pipe, glob-anchoring-failure, console-encoding,
    tmpdir-unset, double-dash-operand, truncated-report, path-resolution-owner,
    shell-write-net, shell-write-prohibition, shell-write-instruction-refusal,
    msys-signal-reach, hang-diagnosis-order, check-ignore-stdin, make-recipe-stdin,
    powershell-command-mode-parse, pipefail-grep-q, background-launch-stdin-hang,
    awk-program-home]
  aliases: [bash, powershell, шелл, shell, кавычки, quoting, экранирование, escape, heredoc, awk,
    пайп, pipe, exit code, код возврата, pipefail, glob, кодировка, cp1252, BOM, кириллица,
    TMPDIR, временная папка, temp directory, scratchpad, переменная окружения пустая,
    unset variable, путь в корень, фоновый запуск ничего не написал,
    двойное тире, double dash, --include, операнд, operand, опция после тире,
    grep без фильтра, unfiltered grep, обрезанный вывод, truncated output,
    tail, потерял диагностику, lost the diagnosis, куда делся MISSED,
    кто разрешает путь, who resolves a path, /tmp на Windows, tmp does not exist,
    bash мапит а программа нет, NL = chr(10), назвать перевод строки,
    check-ignore, git check-ignore, --stdin, стандартный ввод, stdin, труба в нативную команду,
    ничего не пришло на вход, ignored path, игнорируемый путь, .gitignore из скрипта,
    make recipe, рецепт make, висит на нуле CPU, zero CPU, hang, зависает,
    закрыть стандартный ввод, close standard input, exec < /dev/null, рекурсия make, jobserver,
    голое слово, bare word, command mode, забыл доллар, missing sigil, -match,
    не забиндился аргумент, argument binding, ParameterArgumentTransformationError,
    grep -q в конце пайпа, grep -q inverts, SIGPIPE от grep, тест перевёрнут,
    пустая выборка проверяется неправильно,
    фоновый запуск вешает, backgrounding hangs, run_in_background висит, набор не возвращается,
    awk -f, вынести awk в файл, программа в кавычках, embedded awk, апостроф в комментарии]

- group: line endings
  definition: what is pinned to LF, when a class is pinned, and what a checkout rewrites underneath
    a working copy. Answers "why does this file look changed when nothing changed".
  slugs: [line-ending-policy, line-ending-widening, line-ending-churn,
    lf-pin-working-copy-blindness, yaml-line-ending-pin, git-status-stat-cache,
    cr-counting-instrument, awk-text-mode-asymmetry, yaml-pin-ratification-order,
    python-line-ending-pin, crlf-anchored-assertion, text-mode-round-trip,
    working-copy-byte-census, vault-crlf-renormalisation]
  aliases: [переводы строк, line endings, CRLF, LF, CR, gitattributes, git status, git diff,
    нормализация строк, renormalize, шум в диффе, ратификация пина, порядок ратификации,
    политика внутри файла, *.py, питон пин, python pin, закрепить py, sed -i по .py,
    CRLF в ассерте, end-of-line anchor, якорь конца строки]

- group: the permission mode and the approved scope
  definition: what mode a session is in, who can see it, what an approval covers, and what survives
    a compaction or a clear. Answers "am I allowed to do this now, and does that still hold".
  slugs: [permission-mode-visibility, permission-mode-cache-safety, vscode-initial-permission-mode,
    approved-scope-lifetime, scope-change-protocol, compaction-survival, exit-plan-mode-events,
    plan-mode-and-subagents, config-reload, scope-widening-chosen-step, scope-widening-forced-step,
    scope-departure-ratified-late, default-permission-mode, settings-file-precedence]
  aliases: [режим, permission mode, plan mode, режим плана, ExitPlanMode, согласованный объём,
    approved scope, расширить объём, компакт, compact, clear, кеш, cache, перезапуск сессии,
    вынужденный шаг, forced step, побочная правка, helper extraction, не спросил,
    ратифицирую, ратификация постфактум, замена шага, replacement, дивергенция, divergence]

- group: who may write the vault
  definition: the one-writer property, what it covers, where it has been broken and what the
    exceptions are. Answers "may I edit this file, or does the librarian".
  slugs: [vault-librarian, librarian-write-permission, librarian-modes, one-writer-guarantee,
    one-writer-scope, one-writer-note-channel, out-of-band-write-pair,
    vault-schema-write-permission, wiki-write-exception, harness-writer,
    schema-hand-edit-divergence,
    lessons-collector-write-scope, one-writer-register-set, librarian-gate-cadence,
    archiver-runner-divergence, verdict-and-pen-separation, register-writer-exception,
    family-rule-authorship]
  aliases: [библиотекарь, librarian, кто пишет vault, один писатель, one writer, права на запись,
    редактировать вручную, hand edit, параллельные агенты, регистры, divergence, дивергенция,
    CLAUDE.md ваулта, схема ваулта, правка руками, клаузула ещё не написана,
    сборщик уроков пишет, collector writes, второй писатель, паралелить не можем, через библиотекаря]

- group: the hooks that stand around a session
  definition: which hook fires when, what each of them cannot do, and how one is measured. Answers
    "what runs by itself around my work".
  slugs: [session-hooks, dispatch-hook-surface, subagent-hook-reach, hook-bash-discovery,
    hook-refusal-test, hook-measurement-harness, hook-versus-text-scope,
    journal-gate-hook, plan-check-hook, refusal-shapes, dispatch-record-hook,
    feedback-catcher-hook, message-display-event, hook-probe-side-effects,
    schema-exception-flag, hook-pipeline-merge, hook-payload-encoding,
    hook-side-effect-register, smoke-gate-hooks, smoke-gate-inference,
    observed-run-verdict-source,
    feedback-reminder-hook, rule-server-hook]
  aliases: [смоук-гейт, smoke gate, три хука, three hooks, напоминалка, reminder, регистратор,
    recorder, ворота на handoff, gate the handoff, зелёный прогон, green run, строка смоука,
    smoke row, устаревший прогон, stale run, что записано а что выведено, observation versus
    inference, маркер в выводе, printed marker, SMOKE-EXIT, нет маркера нет строки,
    фоновый запуск, background run, run_in_background, check-ignore, git не игнорирует,
    хук, хуки, hook, hooks, settings.json, SubagentStart, PreToolUse, PostToolUse, событие,
    event, блокирующий хук, advisory, отказ, refusal, полезная нагрузка, payload,
    запись диспатча, кто записал строку, ledger row, hook records, dispatch row,
    хук который только пишет, регистрация хука,
    MessageDisplay, событие сообщения, message_id, delta, final, стриминг, streaming,
    ловец фидбека, catch-the-feedback.ps1, поймать блок, зонд, probe, пробный вызов хука,
    побочный эффект теста, side effect of testing, ротация леджера зондом,
    исключить _schema.yaml, schema exception, отдельный флаг, объединить хуки, common pipeline, один конвейер]
  note: fourteen slugs on 2026-08-24, three of them landed in one ingest - the feedback catcher,
    the event it fires on, and what testing a hook by hand costs - and each is a question about a
    hook rather than about the thing the hook serves. Rebalancing is a judgement about the corpus
    and belongs to `/vault-lint`, so nothing here split it.

- group: the hooks that refuse
  definition: the librarian lock and the write net — the two places a hook says no, what each
    matches on, and what a refusal hides while it stands. Answers "why was I stopped".
  slugs: [librarian-dispatch-lock, lock-matcher-strategy, lock-diagnostic-masking,
    guard-chain-order, guard-branch-mechanism, net-session-id-requirement,
    pre-task-net-vault-exclusion, lock-deadlock-hand-write, sprint-gate-refusal,
    hook-blocking-register, refusal-event-bound, handoff-gate-refusal,
    single-page-register-deadlock]
  aliases: [лок, lock, замок, блокировка, сеть записи, write net, guard, гард, matcher, session_id,
    отказ на запись, исключение vault из сети, дедлок, deadlock, какие хуки блокируют,
    ворота спринта, UserPromptSubmit, аварийный выход,
    gate-the-handoff.ps1, блокировать handoff, ворота перед handoff, устаревший прогон, stale run,
    протухший smoke, не пускает в handoff, точка невозврата, point of no return,
    одна страница ломает ворота, замок на одной странице, слуг вне authority.md, unregistered slug,
    сирота и слуг сразу, кто может починить красные ворота]

- group: the pre-task ritual
  definition: when `/pre-task` fires, what it dispatches, what it writes about itself, and what it
    is worth. Answers "do I owe a pre-task here, and what happens if I do".
  slugs: [pre-task-trigger, pre-task-rule-delivery, pre-task-dispatch-unit,
    pre-task-state-machine, pre-task-state-library, pre-task-value, pre-task-fallback-gap,
    pre-task-column-states, ritual-self-recording, once-per-session-precondition,
    divergence-recurrence-reading, pre-task-enumeration-scope, pre-task-phase-split,
    pre-task-enforcement, pre-task-half-strength, pre-task-phase-2-obligation,
    pre-task-agent-file, plan-versus-tree-defects, pre-task-dispatch-contradiction,
    pre-task-order-divergence, pre-task-binding-filter, pre-task-corpus-loss,
    plan-constraint-enumeration, lessons-enumeration-widening, pre-task-on-an-override-session,
    pre-task-reading-scope]
  aliases: [pre-task, пре-таск, ритуал, ritual, перед задачей, план, первая запись, триггер,
    trigger, состояние ритуала, state machine, раз за сессию, рецидив, recurrence,
    повторное нарушение, три случая подряд, pre-task-coverage, enumeration-breadth,
    что перечисляет pre-task, какие папки проверяются, охват ритуала, широта проверки плана,
    две фазы, phase 1, phase 2, каталог, catalogue, короткий список, shortlist, узкий диспатч,
    ритуал обязателен, enforced, агент вместо скилла, pre-task-two-phase,
    enumeration-in-main-context, вторая фаза обязательна, всегда диспатчить,
    не спавнить агентов, что пропущено в списке, what is missing from this list,
    ревью собственного списка, план врёт про дерево, plan wrong about the tree,
    поймал пять пунктов, уже ратифицировано, already ratified, счёт в плане устарел,
    противоречие двух правил, forbidden to dispatch, да запускаем,
    pre-task после первой записи, план был первой записью, первый write это план, порядок ритуала,
    отвечает по пунктам плана, per item of the plan, обязательство вне плана невидимо,
    что нельзя ломать в план, what must not be broken as items,
    что потерял pre-task после свипа, binding живёт только на decision,
    экстренная сессия, override session, обход правил, сессия идёт против правил,
    отчёт неразделён, undifferentiated report, механические поломки против запретов,
    pre-task читает слишком много, reads too much, релевантная страница, relevant page,
    смысл совпал, matching in meaning, поиск вместо перечисления, search instead of enumeration]

- group: the pre-task ledger
  definition: the file the ritual appends to, what is read out of it, what its columns mean to a
    human, and how it is rotated. Answers "where is the record that the ritual ran".
  slugs: [pre-task-ledger, ledger-retention, ledger-archive, ledger-jobs,
    ledger-rotation-mechanism, ledger-column-honesty, session-start-row]
  aliases: [леджер, ledger, журнал ритуала, ротация, rotation, архив леджера, session-start,
    штамп сессии, колонка, tsv, append-only, ledger-drain, слив ledger, слива нет,
    кто вычитывает леджер, не чистим архив, retention]

- group: the harness transcript and what is read out of it
  definition: what the Claude Code transcript holds, what it cannot hold, who separates the owner
    from the harness inside it, and the extractor that reads one session's dialogue out of it.
    Answers "what was actually said in this session, and can I check it". Added 2026-08-24, when
    the store was read for the first time: 37 files and 255 MB had existed for the life of the
    project with nothing in the repository reading them.
  slugs: [session-floor-reading, session-dialogue-extract, transcript-contents, menu-state-set,
    extract-reading-obligation, dialogue-grouping-defect-deferral, context-argument-blindness]
  aliases: [транскрипт, transcript, стенограмма, .jsonl, session-dialogue.py, извлечь диалог,
    extract the dialogue, что я говорил, what did he say, ход N, turn N, проверить цитату,
    verify a quote, AskUserQuestion, ответ на меню, menu answer, origin.kind, task-notification,
    isMeta, isSidechain, прерывание, interrupt, пустой thinking, empty thinking,
    подагент не в транскрипте, subagent turns, session-transcript.path, шаг 0, step 0]

- group: the end of a session
  definition: what the retro is, what it is not, what it routes into, and what a ritual nobody
    announced is worth. Answers "what do I do when the work is finished".
  slugs: [end-of-session-ritual-name, retro-and-handoff-split, retro-step, retro-transit-file,
    action-queue, unfilled-retro-template, closing-ritual-offset, ritual-visibility,
    unanswered-question, unfilled-retro-detection, retro-mark-gap, retro-mark-gap-response,
    ritual-report-count,
    session-end-instrument, retro-suite-launch, frontier-definition,
    retro-list-method, session-closed-forks-ratification]
  aliases: [ретро, retro, ретроспектива, retrospective, конец сессии, завершение, handoff,
    очередь действий, action queue, транзитный файл, незаполненный шаблон,
    как отличить заполненный ретро, предикат заполненности, YYYY-MM-DD placeholder,
    марки в retro, marks in the retro, счёт закрытых линий, off by one в отчёте,
    хук на конец сессии, SessionEnd hook, спросить дерево, нескомпилированный журнал, uncompiled journal,
    фронтир, frontier, граница вопросов, boundary of questions, открытые вопросы сессии,
    фронтир в брифе, frontier in the brief, пройтись по фронтиру,
    кто отрабатывает список ретро, who works the retro list, изъятие пунктов, carve-out,
    развилки закрытые без вопроса, forks closed without asking, ратификация постфактум]

- group: the journal a session writes
  definition: the handoff, the template it is written to, what `raw/` may hold, and how it is
    emptied. Answers "where does what happened get written down".
  slugs: [handoff-template, handoff-template-form, handoff-retirement-gate, journal-section-rule,
    journal-versus-form, raw-scope, raw-emptying-mechanism, raw-structure-ordering,
    templates-directory, docs-handoff-pointer, raw-archive-migration, session-slug-source,
    raw-sweep-backlog]
  aliases: [хендофф, handoff, журнал, journal, HANDOFF.md, шаблон, template, raw, сырьё,
    свидетельство, testimony, форма, секции журнала, docs/HANDOFF.md, указатель,
    перенос raw в архив, датированный архив, слаг сессии, session slug, как зовётся сессия,
    имя папки сессии, обещание вместо механизма, ретайр среди сессии]

- group: the ingest
  definition: when the ingest runs, how it picks its source, what counts as compiled, and where a
    unit of a journal ends up. Answers "how does a journal become pages".
  slugs: [ingest-cadence, ingest-completeness, ingest-source-selection, compiled-definition,
    verdict-semantics, feedback-lag, harness-change-capture, merged-source-summaries,
    superseded-text-in-a-long-source, intent-vs-testimony, lessons-as-a-queue,
    criterion-reporting-at-ingest,
    ingest-without-a-build, page-verdict-verification, coverage-verdict-resolvability,
    ingest-dispatch-owner, ingest-rewiring-design, librarian-dispatch-owner,
    librarian-file-scope, commit-step-rule-debt, ingest-compression]
  aliases: [вердикт не резолвится, verdict resolvability, проза после слуга, prose after the slug,
    голый слуг, bare slug, coverage считает наличие,
    ingest, инжест, компиляция, compiled, юнит, unit, вердикт, verdict, sidecar, сайдкар,
    покрытие источника, coverage, когда запускать ingest, порядок ритуалов, lessons-to-proposals,
    lessons-queue, уроки в очередь, что делать с уроком, факт и действие, разгрузка lessons,
    критерии в бриф, criteria in the brief, вывод команды критерия, decider output,
    печатать вывод а не вердикт, состояние критериев, где мы по критериям,
    вики опережает действия, wiki ahead of the actions, сессия ничего не построила, только decisions и proposals, вердикт page не проверяет утверждение, page verdict fidelity,
    кто диспатчит, who dispatches, инструмент dispatch, dispatch tool, tools в агенте,
    вложенный субагент, nested subagent, субагент вызывает субагента, один запуск библиотекаря,
    один диспатч а не два, файл агента против скилла, agent file versus skill,
    что лежит в vault-librarian.md, возможности агента, capabilities not process]

- group: the feedback loop back to the librarian
  definition: how a wrong or missing answer is reported, in what vocabulary, and how the vault is
    measured by use rather than by reading. Answers "the vault answered badly — now what".
  slugs: [feedback-channel, feedback-kinds, feedback-drain-vocabulary, harness-feedback-kind,
    agent-boundary-relay, undrainable-queue, chat-durability, fidelity-verification,
    vault-usefulness-measure, acceptance-instrument, miss-recording-obligation,
    feedback-drain-ownership, feedback-recording-mechanism, feedback-record-parsing,
    feedback-record-grammar, mark-quote-obligation,
    librarian-feedback-write, quote-context-requirement, retro-feedback-silence,
    divergence-kind-refusal,
    feedback-reminder-trigger, reminder-fatigue, argued-and-shipped-anyway,
    feedback-requirement-owner, reply-silence-threshold, reply-silence-mechanism,
    message-display-silence]
  aliases: [обратная связь, feedback, vault-feedback.md, miss, промах, жалоба, слив, drain,
    приёмка, acceptance, полезность vault, проверка использованием, log.md, кто чистит файл,
    кто удаляет строку, дважды записано, дубль в log.md, окно между ритуалами, VAULT-FEEDBACK,
    блок в ответе, spoken feedback, сказать а не записать, ловец, catcher,
    plan mode не даёт писать, plan mode cannot write, четыре вида, four kinds,
    decision как вид, decision kind, колонка ноль, column zero, ведущий дефис, leading dash,
    одна запись одна строка, backticks в виде, дословные слова владельца,
    библиотекарь пишет только в log, librarian writes log only, запрос библиотекаря к сессии, цитата с контекстом, quote with context, да окей, вырвано из контекста,
    один хук владеет требованием, one hook owns it, вторая регистрация, second registration,
    порог молчания, silence threshold, счётчик ответов, reply counter,
    MessageDisplay не может говорить, hook cannot speak, additionalContext не доходит,
    зонд, probe, ритуальная ветка, ritual branch]

- group: how the owner is asked
  definition: how a question is put to the owner, how his answer is read, and what a proposal from
    him is and is not. Answers "did he decide that, or was he thinking out loud".
  slugs: [interview-skill, interview-discipline, reading-an-owners-proposal,
    proposal-read-as-ratification, owners-design-intent, owners-method-note,
    unverifiable-means-underdesigned, measurement-over-argument, open-questions-list,
    retro-corpus-question-divergence, question-made-moot, scheduled-conversation-drift,
    review-list-shape,
    reversible-fork-decision, retro-question-form, question-shape]
  aliases: [владелец, owner, интервью, grill-me, спросить, вопрос, ratification, ратификация,
    доверюсь тебе, открытые вопросы, замысел, design intent, как проверишь, спросил зря,
    уже отвечено, мы уже говорили об этом, owner-silence-reading, question-withdrawn,
    молчание как согласие, окей продолжаем, если не возражаешь, снял вопрос сам,
    вопрос стал неактуальным, назначенный разговор, обсудим на следующей сессии,
    не состоялся разговор, четвёртая сессия подряд, вытеснено работой,
    обратимая развилка, reversible fork, решай сам, не показывай варианты, сессия решает сама,
    форма вопроса, question shape, с контекстом и рекомендацией, context and a recommendation,
    как работает сейчас, how it works today, голые вопросы, bare questions,
    я не могу догадываться]

- group: what the owner said, and what was put in his mouth
  definition: how a line comes to be attributed to the owner, what separates his own words from a
    session's paraphrase of them, and the mechanisms that check the difference. Answers "is this
    sentence his, and may I reason from it as his". Added 2026-08-22, after a rule he had never
    given stood for three days as a quotation stamped `basis: human` and decided three things.
    Separate from "how the owner is asked", which is about putting a question to him: this family
    is about what comes back and how it is written down.
  slugs: [paraphrase-attribution-chain, retro-ratification, retro-menu-attribution,
    ratification-sweep-schedule, contradictory-menu-reading, quote-language-verdict,
    quote-language-rule-design, ask-before-weakening-ratification, quote-scan-false-positive,
    plan-ratification-sourcing, ratification-sweep-outcome, sweep-timing-divergence,
    paraphrase-block-repair, b3-plan-deviation, ratified-paraphrase-basis, retro-verdict-method]
  aliases: [цитата, quote, цитата владельца, приписано владельцу, чьи это слова, его слова,
    не говорил такого, правило которого не было, пересказ, парафраз, paraphrase, attribution,
    атрибуция, ратификация, ratification, кириллица, Cyrillic, английская цитата, basis human,
    ложная цитата, подпись owner, owner selected, выбрал из вариантов, меню, menu,
    option label, ярлык опции, третья форма атрибуции, ratification-third-row,
    решение а не реплика, сводка цитат, свип атрибуций, ratification sweep, 27 блоков, --lint,
    правило без решения, unruled rule, правило которое никто не принимал,
    ретроактивная ратификация, retroactive ratification, задним числом, подписываюсь,
    это мое решение, ратифицировать правило, ratify a rule, ask before you weaken,
    спросить прежде чем ослабить, decided_by пустой, empty decided_by, некуда указать,
    nowhere to point, сканер безопасности, security scanner, сфабрикованная цитата,
    fabricated quote, ложное срабатывание, false positive, нет реплики пользователя,
    no user turn, проверить посимвольно, character by character, ратификация списком,
    one ratification, 26 из 27, sweep внутри сессии, divergence sweep,
    снять подпись owner, remove the signature, переписать блок, голосом сессии, in the session's voice, дубликат блока,
    вердикты ставит сессия, verdicts set by the session, приму или откажу, одним блоком,
    approve or refuse with a correction, одобрение плана как решение, ExitPlanMode ruling]

- group: dispatching an agent
  definition: when a subagent is worth its cost, what it can and cannot report about itself, and
    which of its claims to measure. Answers "should I dispatch, and do I believe what came back".
  slugs: [skill-versus-subagent, agent-round-trip-cost, agent-cost-reporting, subagent-resumption,
    audit-dispatch-order, believable-subagent-claim, derivation-cost,
    objection-against-a-sunk-cost, cost-figure-unit, suite-timing, scout-dispatch-design,
    brief-cost-without-findings,
    unasked-dispatch-resolution,
    decisions-agent-scope, decisions-agent-design,
    decisions-agent-file, lessons-agent-file, agent-architecture-design,
    vault-ask-skill, fork-dividend-measurement]
  aliases: [агент, agent, субагент, subagent, скилл, skill, диспатч, dispatch, стоимость, cost,
    агент решений, decisions agent, агент уроков, lessons agent, пять акторов, five actors,
    два режима, two modes, вердикт, verdict, undesigned, contradicts, перепись, census,
    кто читает vault, who reads the vault, читатель и писатель,
    токены, tokens, round trip, ревью, аудит, audit, resume, возобновить, разведчики, scouts,
    один агент на папку, параллельное чтение, бриф, brief, что передать библиотекарю,
    цена без находок, находки не дошли, отчёт о диспатче,
    диспатч без просьбы, unasked dispatch, какое из двух правил главное, ритуал требует диспатча,
    vault-ask, форкнутый скилл, forked skill, context fork, точка входа поиска, search entry point,
    agent Explore, background false, дивиденды форка, fork dividend, чем форк отличается от диспатча]

- group: what actually reaches a subagent
  definition: what text an agent is handed, by which mechanism, and how that was measured rather
    than assumed. Answers "will this rule be in front of the agent that needs it".
  slugs: [delivery-probe, scoped-rule-delivery-measured, scoped-rule-trigger, rules-file-loading,
    marker-context-cost, probe-instrument-contamination, probe-teardown-destination,
    conditional-delivery-gate, compaction-probe-sequencing, fork-word-collision]
  aliases: [доставка правила, delivery, .claude/rules, paths, scoped rule, зонд, probe, замер,
    что видит агент, контекст агента, nonce, эксперимент,
    fork, форк, context: fork, /subtask, пустой контекст, empty context, чистый старт,
    два механизма одно слово, one word two mechanisms, наследует контекст, inherits the context]

- group: a rule page and the slice that travels
  definition: what makes a page a rule, what part of it is rendered elsewhere, and how rules are
    numbered and ordered. Answers "should this be a rule, and what of it leaves the page".
  slugs: [rules-type, rule-text-boundary, one-slice-per-rule, rule-numbering, rule-ordinals,
    renderable-shapes, harness-ownership, first-migrant, rules-folder-inventory,
    harness-build-design, verdict-number-drift]
  aliases: [правило, rule, wiki/rules, слайс, slice, что переносится, номер правила,
    порядок правил, ordinal, миграция правила, компиляция харнесса, что лежит в wiki/rules,
    режимы доставки, delivery mode, номер вердикта, вердикт без номера]

- group: where a rule's text is sent
  definition: `governs:` and `paths:` — the destination, how it is resolved, who may carry it, and
    what the governed set is. Answers "which file does this rule end up in".
  slugs: [governs-scope, governs-path-resolution, governs-uniqueness, governs-value-syntax,
    governs-outside-rules, authority-beside-governs, rules-folder-gate, paths-requirement-scope,
    paths-scope-source, governed-set, generated-file-without-paths, governs-target-liveness,
    owner-block-rule-destinations, feedback-rule-extra-destination, conditional-delivery-gate-scope,
    rule-delivery-modes, javascript-rule-destination, feedback-region-audience,
    lookup-rule-delivery, rule-about-rules-delivery, rule-versus-prohibition,
    family-rule-from-titles, serve-the-rule-authority-branch]
  aliases: [governs, назначение, destination, путь, path, paths, governed set, куда рендерится,
    ruleclaim, уникальность назначения, от корня репозитория,
    кто может нести governs, who may carry governs, только wiki/rules, rules-only,
    страница которая рендерится это правило, a page that renders is a rule,
    файл который ритуал очищает, a file the ritual empties, git-ignored назначение,
    дедлок инжектора, injector deadlock, куда нельзя рендерить,
    четвёртый адрес, an extra governs address, файл который ритуал очищает, git-ignored destination, куда рендерить правило про цитаты,
    render authority, доставка по слугу, lookup delivery, правило без governs, правило которое никуда не рендерится,
    правило о правилах, rule about rules, чем правило отличается от запрета, rule versus prohibition,
    заголовок как формулировка, clause from a title, ветка по authority не написана, dormant matcher]

- group: the region a rule renders into
  definition: the markers, their form, their placement, and the verdicts that read them. Answers
    "what does the rendered block look like, and where does it go".
  slugs: [region-form, region-separator, region-absence-verdict, marker-as-address, marker-type,
    marker-detection, marker-net-spelling-accident, address-verdict, address-verdict-home,
    wikilink-in-slice, unregioned-prose-layers]
  aliases: [регион, region, маркер, marker, HTML comment, комментарий, разделитель, separator,
    адрес, address, вставка, вставленный текст, wikilink в слайсе, проза вне регионов,
    слои поверх прозы, повелительное наклонение, imperative grep]

- group: the injector
  definition: the writer that renders rules into files, the delivery modes it knows, and the
    blindspots the check found in it. Answers "how does the text get there, and how do we know it
    is the same text".
  slugs: [injector-check-directions, injector-comparison-blindness, injector-cost-model,
    injector-fence-defect, injector-output-severity, injector-render-blindspot,
    absent-render-verdict, delivery-mode-field, whole-delivery-mode, rendered-form-definition,
    governs-list-expansion, injector-orphan-region-removal]
  aliases: [инжектор, injector, vault-inject.sh, render, рендер, whole, сравнение,
    байт в байт, fenced block, фенс, стоимость инжектора,
    осиротевший регион, orphaned region, регион без страницы, удалить регион, remove a region,
    правило свернули в страницу, folded rule, rule folded into a page, нет преемника,
    no successor, потерял governs]

- group: a file the repository generates
  definition: what a generated file is, who owns and deletes it, and what a hand edit to one costs.
    Answers "who wrote this file, and may I edit it".
  slugs: [generated-file-ownership, generated-file-deletion, generated-file-hand-edit-verdict,
    generated-rules-file, generated-text-self-description, ast-move-ground, ast-move-blocker,
    harness-map-generation, tree-sourced-region]
  aliases: [сгенерированный файл, generated, ast-boundaries.md, удаление, deletion,
    маркер владения, ручная правка, hand edit, AST rule, перенос правила, карта харнесса,
    генератор из дерева, регион из дерева, settings.json карта]

- group: a copy of a list drifts
  definition: why a duplicated list is repaired by deleting it rather than extending it, and where
    a copy has already gone stale here. Answers "should I write this list down a second time".
  slugs: [drifting-copy-repair, copied-list-drift, count-drift, catalogue-generation,
    where-things-are, record-schema-trim, mapping-location, first-use-outside-home,
    count-check-design, makefile-design, field-reader-count, derived-register-proof,
    subtotal-as-total, page-provenance-signature]
  aliases: [подпись Compiled from, compiled from, провенанс страницы, page provenance,
    sources несёт то же, рукописная копия источника,
    дрейф, drift, копия списка, дубликат, duplicate, каталог, catalogue, счётчик,
    stated count, устарел, stale, sweep, обход дерева, где что лежит, Makefile, make,
    пайплайны, ## Commands, проверка счётчика, сколько читателей, третий парсер, third parser,
    два парсера, не общий код, кто ещё читает поле, список как тест, печатать а не вести,
    printed register, реестр из кода, подытог вместо итога, subtotal]

- group: the repository's CLAUDE.md
  definition: what stays in that file, what left it, on what criterion, and what a cut to it can
    lose. Answers "does this belong in CLAUDE.md".
  slugs: [claude-md-scope, claude-md-core-criterion, claude-md-assertions,
    claude-md-dispatch-table, claude-md-reachability, claude-md-loss-vs-deletion, map-admission,
    map-region-placement, opposite-rule-moves-on-one-day, rule-frequency-cache,
    claude-md-assertion-ban]
  aliases: [CLAUDE.md, карта, map, диспетчерская таблица, dispatch table, ядро, core, утверждение,
    assertion, что убрать из CLAUDE.md, частота правил, спринт в карте, указывать а не утверждать,
    нормативный абзац, проверяемая ссылка]

- group: a number this project quotes
  definition: where a figure came from, what its denominator is, and every way a number here has
    been wrong. Answers "may I write this number down".
  slugs: [coverage-figure-repair, coverage-denominator-reading, coverage-denominator-source,
    denominator-versus-numerator-repair, region-coverage-criterion-wording, unsourced-figures,
    measured-claim-unmeasured, unrepeated-measurement, mismatched-quantity-comparison,
    claim-before-measurement, date-measurement, measurement-under-load, drift-control,
    unsourced-projection, delegated-cost-measurement, estimate-reasoning-error,
    slice-population-omission]
  aliases: [оценка, estimate, прикидка, рассуждение неверно, wrong reasoning, пол прогона,
    floor of a run, ошибся в три раза, off by a factor,
    цифра, число, number, измерение, measurement, замер, знаменатель, denominator,
    покрытие, coverage, процент, без источника, unsourced, пересчитать, устаревший замер, дата,
    date, какое сегодня число, what is today, неверная дата, wrong date, вывел дату,
    inferred the date, две сессии за день, two sessions in one day, посмотреть на часы,
    read the clock, дата это измерение, шум больше эффекта, noise larger than the effect,
    замер под нагрузкой, measurement under load, параллельная работа, тот же диск, same disk,
    не измерено, контроль, control, дрейф машины, machine drift, прогноз, projection,
    без инструмента]

- group: the gate
  definition: `vault-check.sh` itself — its severities, its exit codes, what it guarantees, and how
    a verdict is proved to fire. Answers "what does the gate actually check, and what does green
    mean".
  slugs: [vault-scripts, gate-severity, gate-exit-codes, gate-exit-ambiguity, gate-guarantee,
    gate-input-clause-first-application, check-by-regeneration, verdict-proof-procedure,
    unreachable-verdict, dropped-type-verdict, gate-cost-decomposition, mode-versus-filter,
    gate-flag-deferral, single-pass-field-reading, shared-rule-heading,
    gate-flag-fork, gate-subset-mode, gate-delegation-reading, gate-rule-build-order,
    gate-subject-writers, interpreter-probe-selection,
    gate-frontmatter-scope, sandbox-verdict-proof-divergence, gate-silent-pass]
  aliases: [гейт, gate, vault-check.sh, проверка vault, красный, red, зелёный, green,
    exit code, вердикт, verdict, severity, регенерация, что гарантирует проверка,
    режим а не фильтр, mode not a filter, --rules, из чего состоит стоимость gate,
    общий проход, shared pass, один проход awk, заголовок на два правила,
    два правила один заголовок,
    флаг пропускающий правила, skip rules flag, режим без вердикта, subset mode, не могу принять решение,
    ворота молча перестали проверять, silent pass, exit 0 но ничего не проверено, пустой stderr,
    все теги неиспользуемые, xargs argument list size, предел аргумента, argument limit]

- group: an advisory rather than a red verdict
  definition: when a finding is printed and not failed, what shape an advisory takes, and what a
    false alarm costs. Answers "should this be red, or a note".
  slugs: [advisory-form, advisory-channel-split, advisory-line-shape, advisory-exemption-testing,
    filename-verdict-severity, false-alarm-cost, vault-lint-item-deferral, advisory-cadence,
    mark-state-versus-address, advisory-continuation-defect]
  aliases: [advisory, предупреждение, не красное, lint, линт, ложная тревога, false alarm,
    шум, noise, форма вывода, отсортировано, канал вывода, как часто печатается, cadence,
    каденция, на каждом ingest, плотность тегов, tag density,
    метка, mark, стадия, stage, адрес, address, что гейт не судит, realised,
    вердикт который убрали, verdict removed, состояние а не место, implemented в wiki,
    advisory на строке продолжения, continuation line, grep -c advisory, счёт advisory завышен,
    54 против 30, только заголовок несёт слово]

- group: the selftest of the vault's own scripts
  definition: the sandbox it works in, its cost, its parallelism, and the floor under it. Answers
    "how are the checks themselves checked".
  slugs: [selftest-cost, selftest-parallelism, selftest-parallel-floor,
    selftest-fixture-source, selftest-sandbox-fidelity, renamed-vault-case-scope,
    sandbox-loop-ordering, parallel-suite-counting, global-rule-test-coupling,
    green-tree-case-deferral, selftest-shape, clean-case-helper-choice, suite-cost-reduction,
    case-list-sweep, filter-placement, sandbox-copy-list-coupling,
    check-system-naming, smoke-runner-build-order, check-entry-point, check-system-proposal-order,
    check-system-arrangement, suite-cost-growth-term, makefile-targets,
    selftest-only-filter, only-case-placement, selftest-section-derivation,
    sweep-counts-its-own-comment, uninstrumented-rule-fixture, case-list-page-refusal,
    literal-hunting-instrument]
  aliases: [цели Makefile, makefile targets, make help, ONLY=, срез сьюта, slice,
    закрыть stdin, </dev/null, prerequisites, зависимости цели, шесть целей,
    селфтест, selftest, песочница, sandbox, параллельно, parallel, стоимость прогона,
    зеркало корпуса, переименованный vault, кейс, case, зелёное дерево, green gate,
    кейс без фикстуры, MISSED на красном дереве, мутационный тест, mutation test, форма сьюта,
    что делает кейс, сломать одно, run_clean, чистый кейс, clean case, зачем полный прогон,
    одно правило за раз, one rule at a time, ускорить сьют, make the suite cheaper, антивирус,
    virus scanner, исключить песочницу, exclude the sandbox, --list, --only, список кейсов,
    case list, фильтр по кейсам, пол прогона, floor,
    make, Makefile, make smoke, make suite, make test, make style, цель, target, точка входа,
    entry point, кто запускает, who runs it, когда запускать, when does it run, что обязывает,
    красный результат, red result, расстановка проверок, check arrangement, style а не lint,
    растёт с корпусом, grows with the corpus, растущий член, the term that grows, константа,
    constant factor, почему сьют дорожает, why the suite gets slower, час прогона, an hour to run,
    18m13s, 27m15s, 34m08s, копия корпуса на кейс, corpus copy per case,
    --only не нашёл ничего, empty selection, опечатка читается как pass, typo reads as a pass,
    секция кейса, case section, где живут кейсы --only, дорогая пара кейсов, expensive pair,
    комментарий попал в свип, comment counted by the sweep, счётчик кейсов, count case,
    фикстура нарушала правило, fixture violated a rule, страница со списком кейсов]
  note: thirteen slugs on 2026-08-23. Recorded rather than split: the three added that day are the
    shape of the suite, the fixture constraint on a clean case, and how to make the suite cheaper —
    and which of them belongs with *a fixture and what it must materialise* is the rebalancing that
    is a carried sprint item

- group: a fixture and what it must materialise
  definition: what a test's setup has to put on disk, why a planted offender is read back, and how
    a fixture stops being a fixture of its subject. Answers "is my setup actually the situation I
    mean".
  slugs: [fixture-corpus-tightening, fixture-materialisation, fixture-renames-its-subject,
    real-breakage-as-a-fixture, plant-and-revert, placeholder-collision,
    green-on-own-placeholders, known-good-probe, hand-probe-before-suite,
    fixture-slug-coupling, fixture-self-containment, real-tree-plant-harness,
    fixture-positional-dependency]
  aliases: [фикстура, fixture, setup, подсадить, planted, offender, заглушка, placeholder,
    известно-хорошее, known good, проверить руками, реальная поломка, хелпер, helper,
    зашитый слаг, hardcoded slug, связанность фикстуры, переименование ломает тесты,
    rename breaks the suite, plant_rule_page, оба конца, both ends, plant_idea_pair,
    слуг в authority.md,
    привязка к позиции, positional dependency, последний блок файла, last block, дописать в конец,
    фикстура истекла, expired fixture, сменила предмет молча]

- group: a test that proves nothing
  definition: the ways a green test carries no evidence, and the procedures that settle whether it
    does. Answers "does this test actually test anything".
  slugs: [test-evidential-power, test-fails-for-itself, case-fails-for-its-own-reason,
    case-from-mechanism, pre-change-suite-run, revert-to-verify-a-test,
    checks-that-pass-vacuously, literal-scanning-tests, announcement-versus-condition,
    collect-only-blindspot, unexercised-branch, pre-existing-green-case, mutation-completeness,
    same-day-defect-no-case]
  aliases: [тест, test, доказательная сила, зелёный тест, проходит всегда, vacuous, откатить,
    revert, до изменения, показать падение, must fail, collect-only, delegated-check-stub,
    пустая заглушка, нулевой файл, правило молчит, делегирующая проверка, зелёный до механизма,
    green before the change, снять сторож, remove the guard]

- group: the instrument and the direction it fails in
  definition: how the tool a claim was measured with has lied here, and which direction of failure
    is the dangerous one. Answers "do I trust this reading".
  slugs: [instrument-failure, instrument-failure-direction, instrument-gaming,
    instrument-reports-itself, coarse-instrument, false-documented-command,
    first-match-read-as-a-count, presence-versus-identity,
    assertion-inside-a-measurement-harness, empty-directory-blindness, half-answered-command,
    field-presence-grep, relocated-script-measurement, guard-match-anchoring,
    measurement-invocation-shape]
  aliases: [инструмент, instrument, врёт, солгал, грубый инструмент, ложное молчание,
    нечего делать, gaming, сам себя измеряет, пустая директория, первое совпадение,
    половина ответа, съел флаг, дропнул аргумент, case "$1", ответил на половину,
    неразрешимый критерий, decider, команда-решатель, греп по всему файлу, field name in prose,
    копия скрипта, relocated copy, 0.8 s,
    замер без stdin, measured without stdin, форма вызова, invocation shape, через трубу, through a pipe,
    цена хука, hook cost, замер в другой форме, замер которому верят]

- group: a mechanism that fails where nobody is looking
  definition: the failure shapes that survive a review — a wrong diagnosis, a rule explained into
    exceptions, a guard that became what it guards. Answers "what makes a defect invisible here".
  slugs: [first-diagnosis-not-the-cause, wrong-diagnosis-failure, gap-closed-by-mechanism,
    knowing-versus-checking, comment-drift, cosmetic-change-retest, deferred-check-discipline,
    teardown-clause-inversion, shape-substitution, rule-exceptions-in-explanation,
    link-sweep-file-class, partial-read-overwrite, background-job-liveness,
    repealed-invariant-in-fresh-code]
  aliases: [диагноз, diagnosis, невидимый дефект, знать не значит проверять, исключения к правилу,
    отложенная проверка, teardown, подмена формы, дрейф комментария, механизм вместо аккуратности,
    yaml-link-blindness, link-sweep-scope, битая ссылка в схеме, вне обхода, sweep только по .md,
    ссылка которую никто не проверяет]

- group: the per-folder schema
  definition: where the legal keys and values live, how the gate learns them, and in what order a
    schema change lands. Answers "is this frontmatter legal, and who says so".
  slugs: [frontmatter-core, frontmatter-key-set-gate, per-folder-frontmatter-schema,
    per-type-schema-sequencing, schema-value-enforcement, schema-value-location,
    schema-value-parsing, schema-change-order, type-word-source, sources-path-root,
    status-value-set, conditional-requirement-placement, idea-decided-by-pairing,
    idea-decided-by-verdict-design, idea-decided-by-narrowing, schema-values-copy-rule]
  aliases: [фронтматтер, frontmatter, _schema.yaml, схема, schema, ключи, keys,
    допустимые значения, unknown key, порядок изменения схемы, sources, путь в sources, type,
    статус, status, значения статуса, status values, третье значение статуса,
    third status value, implemented, внедрено, легальный статус, legal status,
    статус зашит в скрипте, hardcoded status pair, current и deprecated, блок status в схеме,
    условное требование, conditional requirement, обязательно если, required when,
    схема не умеет условие, где живёт условие, refused без decided_by, idea и decided_by,
    статус и решение, зрелость против авторизации, maturity versus authorisation,
    порядок промоушена, promotion order, сначала back-fill потом required, сужение вердикта,
    narrowed verdict, binding не deferral]

- group: admitting a frontmatter field
  definition: what a new field has to earn before it exists, what a self-declaration costs, and the
    fields that were admitted or withdrawn. Answers "may I add a field for this".
  slugs: [field-admission-test, field-admission-bypass, decision-binding, authority-index,
    register-absence, silencing-declaration, asserts-field-design,
    register-file-format, links-field, links-field-design, decided-by-field,
    decided-by-legal-folders, decided-by-back-fill-method, decided-by-absence-over-false-idea,
    decided-by-archived-target, duplicate-cause-citation, links-field-refusal]
  aliases: [новое поле, field, добавить поле, admission, самодекларация, declaration, реестр,
    register, binding, authority, отозванное поле, checksum, asserts, реестр authority,
    закрытый набор предикатов, словарь вопросов, register-data-format, yaml-for-registers,
    формат реестра, yaml или json, парсер yaml, PyYAML, зависимость ради реестра, Links,
    поле Links, викиссылки в поле, wikilinks in a field, sources работает плохо, провенанс,
    provenance, два смысла у одного поля, decided_by, кто решил, causing decision,
    ссылка на решение, link to the decision, в каких папках поле легально,
    which folders may carry a field, где поле обязательно, where a field is required,
    только в двух папках, two folders only, ключ против значения, key versus value,
    цепочка причин, causal chain, решение порождает proposal или rule,
    пустое поле лучше ложного, absent field, цель в archive, две строки одной причины,
    Links отклонён, Links refused, поле убрано из схем, граф Obsidian из прозы,
    кэш производного свойства, cached derived property, скрипт для Links не строим]
  note: twelve slugs on 2026-08-23, and thirteen later the same day with `decided-by-legal-folders`
    — where that field is legal and where it is required, which is a second question about the same
    field and not the one `decided-by-field` answers. Rebalancing is a judgement about the corpus
    and is a carried sprint item rather than an ingest's. Recorded rather than absorbed: this family
    and *the per-folder schema* are both plausible homes for it, and choosing between them is the
    rebalancing that is still a sprint item.

- group: the no-quantity rule
  definition: why a title and a filename carry no measurable quantity, which words count, and what
    the check does about it. Answers "may this number be in the title".
  slugs: [title-quantities, quantity-rule-subject, quantity-word-list, filename-quantities,
    quantity-field, title-check-mechanism, title-length]
  aliases: [количество, quantity, число в заголовке, цифра в имени файла, слова-счётчики,
    ordinal, порядковое, длина заголовка, переименовать заголовок]

- group: what a page is called and what kind it is
  definition: the folder set, the naming rule, the form a title takes for each type, and correcting
    one. Answers "which folder, and what do I call it".
  slugs: [wiki-categories, proposal-category, page-naming, title-form, title-corrections, idea-home,
    per-type-assertion-schema, concepts-scope-clause,
    gate-suite-entity-split, concepts-entities-taxonomy]
  aliases: [категория, category, папка, folder, тип страницы, type, имя файла, filename,
    kebab-case, заголовок, title, proposals, идея, idea, куда положить страницу,
    что утверждает запись, что делает её устаревшей, схема на тип,
    concepts про продукт, product versus harness, вычеркнуть пункт, о чём папка concepts,
    разделить страницу, entity split, разделение сущностей, хаб, hub page, предметное описание без истории, одна страница или две,
    таксономия, taxonomy, нефункциональные требования, non-functional requirements,
    функциональные требования, functional requirements, чем concept отличается от entity,
    перекос в сторону concepts, парный authority, paired slug]

- group: renaming a page
  definition: what a move costs, what a sweep may touch, what it strands, and why a rewriter needs
    a detector. Answers "may I rename this, and what breaks if I do".
  slugs: [rename-cost, rename-sweep-over-reach, rewriter-and-detector, path-rewrite-mechanism,
    path-rewrite-reach, vault-name-citations, bare-slug-inbound-links, log-link-blindness,
    two-party-change-ordering, prose-path-detector-disposition]
  aliases: [переименование, rename, переезд файла, move, sed, ссылки, links, wikilink,
    битая ссылка, осиротевшая ссылка, имя каталога vault, порядок двух половин,
    путь в прозе, детектор путей, несуществующий путь]

- group: retiring a page
  definition: how a page leaves the working set, what an archived one still asserts, when a
    proposal is retired, and what a text corrected in place owes instead. Answers "this page has
    gone false — is it retired or repaired".
  slugs: [archive-scope, archive-rule-reach, archive-script, archive-session-folder-shape,
    archive-kind-list, archive-link-blindness, deprecated-rule-rendering,
    built-proposal-disposition, refused-proposal-disposition, proposal-status-defect,
    correction-note-date, log-rotation-design, retirement-register-step,
    archive-sweep-placement, implemented-placement-divergence, refusal-archive-ordering,
    archive-sweep-reporting, archive-citation-advisory, archived-status-mint,
    archiving-policy-topic, lessons-cycle, archive-path-length,
    bulk-operation-ruling-check, deprecated-move-precondition,
    log-writer-and-rotation-trigger]
  aliases: [длина пути, path length, Filename too long, core.longpaths, слуг дважды в пути,
    массовая операция, bulk operation, список из ста файлов, проверить список против правил,
    архив, archive, deprecated, устарело, superseded_by, суперсессия, supersession,
    вывести из обращения, retire, отставка страницы, ссылка в архив, ротация log.md,
    log.md растёт, копия лога в архив, kind, вид архива, pages, куда кладут страницу,
    dated archive, датированный архив, четвёртый шаг, fourth step, убрать слаг из реестра,
    authority.md при ретайре, строка без страницы, красный гейт после переноса,
    архив это история, archive is history, вики источник истины, wiki is the source of truth,
    внедрённый proposal, implemented proposal, внедрили предложение, proposal уезжает в архив,
    убрать из прямой видимости, out of direct view, built, реализовано,
    кто цитирует архивную страницу, live page citing a proposal, отклонённый proposal,
    refused proposal, refused, отклонили предложение, статус refused,
    что уехало в архив пусть лежит, обратно из архива, back from the archive, седьмой отказ,
    precondition, живая страница ссылается на слаг, кто двигает в archive, mover,
    обход на этапе lint, implemented остался в proposals,
    отказ свипа, sweep refusal, ненулевой выход, гейт молчит про размещение, counts of moved and refused,
    живой преемник, live successor, superseded_by обязателен перед переездом,
    четвёртый шаг отменён, step repealed, слаг остаётся, keeps its slug,
    лог заполняется механически, log filled mechanically, ротация лога, log rotation,
    в конце спринта, at the sprint close]

- group: draining a folder into the archive
  definition: why the working wiki is swept at all, which criterion each folder leaves by, what a
    sweep does when a move is refused, and what the mark a drained page carries means. Answers
    "should this page still be in `wiki/`, and what decides that". Distinct from *retiring a page*,
    which answers "this one has gone false".
  slugs: [archiving-purpose, archiving-build-scope, archiving-scope-frontier,
    decision-archival-condition, entities-concepts-archival-deferral, processed-status-mint,
    processed-predicate, archive-sweep-refusal-handling, archive-sweep-design,
    deprecated-link-advisory-design, citation-as-predicate, status-value-gate-treatment,
    sweep-first-run-order, sweep-mode-inheritance, sweep-selector-shape, rules-archival-criterion,
    processed-writer, register-citer-standing, deprecated-link-advisory-shape,
    deprecated-link-advisory-key, link-pass-shape, decisions-census-precedence,
    cleanup-rule-suspension, cleanup-folder-scope,
    prohibition-family-rule, authority-rows-same-pass,
    family-verdict-kinds, selector-blind-to-a-new-discharge]
  aliases: [подметание, sweep, обход, подмести вики, разгрузить вики, drain, дренаж,
    зачем архивировать, purpose of archiving, склад, warehouse, дешевле для агента,
    экономит токены, processed, обработано, обработанное решение, decided_by,
    порождённая страница, produced page, предикат архивации, archival criterion, критерий выхода,
    exit criterion, кого архивировать, что архивировать, binding prohibition не архивируется,
    divergence архивируется, deferral по сроку, отказ переезда, refusal, продолжает после отказа,
    выходит ненулевым, ссылка в отменённое, dead link, битая ссылка, advisory на ссылки,
    agent по решениям, decisions agent, агент по урокам, entities и concepts не сегодня,
    рост корпуса, corpus growth, впускная сторона, admission side, adres или стадия,
    address or stage, archived, метка недоехавшего переезда,
    --sweep, режим свипа, sweep mode, первый прогон свипа, first sweep, 239 страниц,
    один проход по корпусу, one pass, селектор, selector, сколько стоит свип, cost of a sweep,
    какой отказ фатален, collected refusal, продолжить после отказа,
    правила архивируются только по решению, rules criterion, кто ставит processed,
    реестры не считаются цитаторами, registers are not citers, sprint.md называет половину корпуса,
    одна строка на мёртвую цель, one line per dead target, ключ по литералу, literal key,
    почему не по статусу, линейный проход по ссылкам, linear link pass,
    чистка, уборка, cleanup, семейство запретов, prohibition family, фасовка по семействам,
    какие папки чистим, out of scope, что не трогаем, вынужденная сессия, forced session,
    вне спринта, outside any sprint, 99 вердиктов, verdict table, таблица семейств,
    строки реестра и страницы одним проходом, rows and pages in one pass, 53 семейства]

- group: what was deferred and what a proposal gets wrong
  definition: the standing deferrals, what waiting costs, and the ways a proposal has been wrong
    about the hole it describes. Answers "was this already designed and put off".
  slugs: [proposal-defects, proposal-frame-change, proposal-mispricing, harness-deferrals,
    structure-deferrals, harness-visibility, harness-visibility-deferral,
    harness-divergence-shape, blocker-dissolution, session-deferrals, pre-task-agent-design,
    harness-product-split-deferral, beads-scheduling, instrument-and-collector-deferral,
    harness-defect-scheduling]
  aliases: [отложено, deferral, deferred, не сейчас, proposal, предложение, что не построено,
    цена ожидания, блокер, blocker, видимость харнесса, туман, незавершённое за сессию,
    куда попадает отложенное, недоказанное утверждение, агент pre-task, PostToolUse,
    хук на Agent, subagent_type, блокирующий гейт, blocking gate, governs списком,
    харнесс против продукта, harness versus product, продукт не двигается, src не менялся,
    записать и жить дальше, коммиты по путям, Beads, Sprint 4, дефекты harness в спринт,
    инструменты правил отложены]

- group: what the vault is and what its answers are worth
  definition: why the store exists, its root principle, what ranks one page's claim against
    another's, and how a claim from it has already been misread. Answers "how much may I lean on
    this page".
  slugs: [vault-origin, vault-artefacts, vault-location, the-stores-root-principle,
    entity-admission, fidelity-axes, settled-fact-assumption, claims-from-prose, audit-outcomes,
    unneeded-licence-citation, mechanism-admission]
  aliases: [vault, база знаний, knowledge base, зачем vault, basis, инференс, inference,
    точность, fidelity, бритва Оккама, Occam, не плодить сущности, аудит, прецедент,
    допуск механизма, механизм заслуживает места, цена поддержки, что стоит держать,
    работа только растёт, ремонт вместо разработки]

- group: the brief a session starts from, and what goes stale
  definition: what the brief carries, what it deliberately does not, how its growth is watched, and
    which staleness check answers which question. Answers "what am I handed at session start, and
    is it still true".
  slugs: [brief-staleness, staleness-timing, task-tracker-boundary, growth-signal, document-size,
    brief-is-not-a-pre-task, staleness-detector-design, ingested-line-resolution]
  aliases: [бриф, brief, brief.md, старт сессии, session start, устаревший бриф, устарело,
    staleness, рост, growth, размер документа, трекер задач, active tasks, бриф не pre-task,
    детектор устаревания, updated против sources, подозрение на устаревание,
    ingested, имя журнала, filename not path, где искать журнал, архив хендофов]

- group: a dependency of this repository
  definition: what may be added, what is merely declared, and what the no-new-dependencies rule
    actually reaches. Answers "may I depend on this". Added 2026-08-22, when a package that was
    installed, imported and undeclared turned out to sit outside a rule that is entirely about it.
    Narrow on purpose: no existing family asks about a package rather than about a field, a
    mechanism or a script. `register-file-format` is the obvious second member and moving it is a
    judgement about the corpus rather than about this slug, so it was left where it is.
  slugs: [dependency-declaration, python3-store-stub]
  aliases: [зависимость, зависимости, dependency, dependencies, pyproject.toml, uv.lock, uv lock,
    PyYAML, pyyaml, транзитивная зависимость, transitive, extra, uvicorn standard, dev dependency,
    dev-зависимость, объявить зависимость, declare, новая библиотека, no new dependencies,
    правило про зависимости, можно ли добавить пакет, python3, интерпретатор, interpreter,
    заглушка, stub, Microsoft Store, WindowsApps, python не отвечает, висит, hangs,
    какой python на этой машине, which interpreter, make, GNU Make, chocolatey]

- group: the sprint and the work that belongs to it
  definition: what a sprint admits, how a slice is executed, how commits are made, and what a
    session may do to a file it did not open. Answers "am I allowed to be doing this work now".
  slugs: [command-list-home, sprint-closure, product-interleave, lint-cadence, branching-convention,
    slice-execution, mid-work-file-changes, wildcard-staging, outside-change-triage,
    running-script-edit-divergence, scope-cut-ruling,
    plan-execution-split, unrequested-harness-change, migration-test-debt-sprint,
    phase-three-deferral, next-list-strike, optimisation-topic, session-scope-2026-08-29,
    strike-form-parking, cleanup-session-standing, frontier-deferral]
  aliases: [спринт, sprint, sprint.md, закрытие спринта, слайс, slice, ветка, branch, main, commit,
    коммит, git add, продуктовая работа, чужие изменения, Makefile, править во время выполнения,
    файл занят, running script, не влезает в сессию, does not fit today, вырезать фазу,
    cut a phase, перенести на следующую сессию, carry to the next session,
    сделать половину, half a phase,
    выполнение в отдельной сессии, execution in its own session, план коммитим, commit the plan, двенадцать пунктов, слишком дорого, не хватает внимания,
    объём дня, scope of the day, какие пункты берём, which items today, припаркован, parked,
    убрать счёт из прозы, remove the count, форма вычёркивания, strike form]

- group: a claim wider than what was checked
  definition: how a session came to assert more than it had verified — a fact about code taken from
    its neighbour, a coverage claim over a surface nobody looked at, a targeted read that could not
    reach a page nobody pointed at — and what would have closed each gap. Answers "did I actually
    check the thing I am about to report". Added 2026-08-21 with the `authority` back-fill: the
    three pages are one session's two errors and the reading that separated them, they cite each
    other, and no existing family asks about the reporter's own claim rather than about the defect.
  slugs: [neighbour-generalisation, verified-coverage-claim, breadth-versus-ritual,
    argument-surface-scope, composed-proof, local-proof-versus-regression,
    unchecked-recommendation,
    self-report-verification, partial-target-clean-report]
  aliases: [проверено, verified, я проверил, допущение, assumption, обобщение, generalisation,
    покрытие, coverage, ширина, breadth, широкое чтение, по указателям, не проверял,
    отчитался как о сделанном, сосед, соседняя функция, поверхность, surface, область аргумента,
    аргумент шире чем проверено, о чём именно страница, скоуп утверждения,
    доказано, proved, цепочка доказана, половина доказательства, две строки не доказывают,
    сложил из двух наблюдений, в свою пользу, критерий 14,
    подсадил нарушителя, planted offender, прогнать весь селфтест, regression run,
    новый вердикт сработал, старые вердикты, caught 157 missed 1, локальная проверка]

- group: what `/vault-lint` looks for, and the axes it has not got
  definition: the semantic passes a librarian runs once a sprint rather than a script running on
    every write — which of the owner's asks were made mechanical, which were built by nothing, and
    why no grep could answer them even in principle. Answers "is this a gate rule or a lint item".
    Added 2026-08-21 with the `authority` back-fill. It is not the severity question — that is
    *an advisory rather than a red verdict* — it is the question of what a semantic pass looks for.
  slugs: [missing-page-detection, entity-decision-reconciliation, tag-classification-skill,
    rule-usage-counting, rule-instrument-obligation, instrument-criterion-decider,
    librarian-repetition-blindness, lessons-queue-instrument-defects, lessons-queue-counter-order,
    lessons-queue-counter-split, lessons-queue-membership]
  aliases: [lint, линт, vault-lint, семантическая проверка, отсутствующая страница,
    негативное пространство, сверить entities с decisions, классификация тегов,
    счётчик правил, как часто срабатывает правило, что искать линту,
    правило без инструмента, unchecked rule, у правила должен быть дом, механически,
    пять правил, SessionEnd, Stop hook, счётчик диспатчей, гейт на английский,
    три способа закрыть, three closures, сторож это я, the owner watches it,
    критерий нельзя выполнить, criterion can never be met, считает только кейсы,
    сборщик уроков, lessons collector, повторяющееся семейство, recurring family,
    очередь уроков, lessons-queue.py, слепота библиотекаря, порог семейства]

- group: how a rule closes its instrument obligation
  definition: the ways a rule in `wiki/rules/` satisfies acceptance criterion 1 — a selftest case, a
    page carrying the argument that no instrument can express it, or a mechanism the owner watches
    himself — and the register that would record which closure each rule took. Answers "how does
    this rule close, and who says so". Added 2026-08-25, when two rules were closed in one session
    and neither closure had anywhere to be recorded. It is not *what `/vault-lint` looks for*, which
    holds the obligation itself (`rule-instrument-obligation`) and the decider that counts it: this
    family is about the closures.
  slugs: [ask-before-weakening-instrument, rule-weakening-detector, rule-closure-mark-deferral,
    rule-closure-register-design, parallel-dispatch-closure, parallel-dispatch-counter-argument]
  aliases: [чем закрыть правило, how a rule closes, closed_by, случай в селфтесте, case name,
    страница вместо инструмента, a page instead of an instrument, наблюдаю сам,
    the owner watches it, ослабление правила, weakening a rule, слайс изменился,
    the slice changed, правило изменили без supersession, счётчик диспатчей не выражает правило,
    a counter cannot express it, .claude/rules файл, generated rules file]

- group: the prose this project writes
  definition: the style the sessions, the plans and this store are written in, and what the owner
    can and cannot read. Answers "how should this be written for him". Added 2026-08-23 with one
    member, narrow on purpose: no existing family asks about the prose itself. *How the owner is
    asked* is about the shape of a question put to him; this is about the writing.
    Extended 2026-08-23, the same day, when the rule was finally written: `style-rule-ratification`
    is a second question and not the same one — *what was ratified, and where its text came from* —
    and the words a future reader arrives with are about the recovery rather than the style. The
    text was believed lost because a repository-wide grep cannot see the plan the owner approves,
    which lives outside the tree.
  slugs: [session-writing-style, style-rule-ratification, style-rule-watch-and-scope,
    style-rule-amendment]
  aliases: [стиль, style, как писать, читаемость, readability, KISS, простыми словами,
    по простому, не могу читать, ответ в первом предложении, пять строк, правило стиля,
    длинные тексты, многословие, ратификация правила стиля, style rule ratification,
    где текст правила, where the text is, восстановленный текст, recovered text,
    план вне репозитория, the plan outside the repository, утерянное правило, lost rule,
    ратифицировано но не записано, ratified and never written, убрать рекламу, sales pitch,
    что не сделано, what is not done, сторож правила, who watches the rule,
    только для общения, chat only, распространяется ли на vault, does it govern the wiki,
    правило стиля и вики,
    поправка, amendment, простой язык по умолчанию, plain language by default, один вопрос за сообщение, one question per message, рассуждение можно пропустить]

- group: the toolkits this store was read against
  definition: the published spec-driven-development tooling this vault has been compared with,
    what each has that this does not, and where they disagree with each other. Answers "has
    somebody already built this, and what did they do differently". Added 2026-08-23 with one
    member; it is not *a dependency of this repository*, because nothing here depends on either.
  slugs: [external-spec-toolkits, obsidian-cli-reading-surface]
  aliases: [openspec, spec-kit, speckit, spec-driven, SDD, чужие инструменты, prior art,
    аналоги, converge, opsx, verify, flow-forward, пакетирование метода, extensions, presets,
    проверка корпуса против кода, corpus versus code,
    Obsidian CLI, обсидиан, obsidian, официальный CLI, запрос по frontmatter,
    frontmatter query, нужен запущенный Obsidian, requires the app running]

- group: how a measurement is written down
  definition: whether a number is testimony for a claim or a gauge of how much now, where each
    lives, and the marked section they are written in. Answers "this number - where does it go".
  slugs: [measurement-role-split, measure-section-shape, measure-section-design,
    measure-destination-syntax, gauge-uniqueness,
    gauge-writing-mechanism, measure-section-grammar, measure-writer-design,
    measure-region-spelling, measure-writer-script, region-bounds-off-by-one,
    negative-measurement-record, hand-typed-date]
  aliases: [измерение, measurement, свидетельство, testimony, датчик, gauge, сколько сейчас,
    how much now, мутирует, роль числа, раздел measure, marked section, назначение марки,
    единственность датчика, куда положить число,
    кто пишет число, who writes the number, скрипт запускает команду, refresh датчиков, vault-measure, грамматика раздела measure, строка на число, стохастическое поведение, less stochastic]

- group: a deferral with a proposal behind it, and the decision nobody compiled
  definition: the rulings that produced a proposal and were never written as a page, and the
    proposals that therefore named no cause. Answers "who ruled on this proposal, and when".
  slugs: [register-format-deferral, rule-usage-axis-deferral, lessons-queue-deferral,
    reading-funnel-deferral, obsidian-cli-deferral, suite-narrowing-order,
    missing-decision-compilation,
    repeated-deferral]
  aliases: [отложено, deferred, обсудим на следующей сессии, decided_by пустой, причина не
    скомпилирована, шесть страниц решений, yaml для реестров, счётчик правил, очередь lessons,
    воронка чтения, Obsidian CLI, сужение suite, полный прогон в конце,
    третий перенос, deferred again, назвать спринт, name the sprint, отказ которого никто не произнёс]

- group: a decision's own lifecycle — what it declares, and what closes it
  definition: the mechanism minted on 2026-08-30 by which a decision names the one thing it
    produces, is discharged by that thing naming it back, and leaves the folder on that handshake
    rather than on any citation. Answers "what is this decision waiting for, and how would I know it
    was done". Distinct from *draining a folder into the archive*, which answers when a page may
    leave; this family answers what makes a decision **finished**.
  slugs: [decision-target-declaration, decision-discharge-criterion, decision-release-criterion,
    target-kind-value-set, proposal-checkbox-meaning, repealed-status-mint,
    processed-removal-condition, lifecycle-date-scope, page-body-sections,
    refused-proposal-decision-release, repeal-decision-review-cadence, decision-lifecycle-container,
    proposal-opening-trigger, tasks-scheduling]
  aliases: [жизненный цикл решения, decision lifecycle, мишень, target, target_kind, цепочка,
    chain, рукопожатие, handshake, две стрелки, both directions, выполненное решение,
    discharged decision, что считать выполненным, закрыть решение, close a decision,
    открытые решения, open decisions, список нереализованных, taken and not built,
    доводить решения до реализации, галочка, checkbox, ратификация не завершение,
    отменённый proposal, refused proposal takes its decisions, repeal, отмена, repealed,
    отменить правило, cancel a rule, разделы страницы, body sections, обязательные разделы,
    sections block, lifecycle_from, required_from, дата отсечения, dated cut, когорта, cohort,
    299 страниц, перепись решений не проводилась, none вместо deferral, пятое значение,
    контейнер proposal, ключ proposal, proposal key, кейс вырос в proposal, задачи, tasks,
    action не закрывается, очередь решений, decision queue, правило 16, правило 17]

- group: the form of a reply, and the frontier it opens with
  definition: what a message to the owner is made of, in what order, how many questions it may work
    at once, and where the list of open questions lives between sessions. Answers "how do I write to
    him, and what do I show him first". Distinct from *the prose this project writes*, which is about
    how a sentence is built rather than what a message contains.
  slugs: [reply-form-ratification, reply-form-instrument, ratification-hook-deferral,
    session-inheritance, rule-landing-two-parties, brief-frontier-generation,
    feedback-target-grammar, carried-and-new-in-one-list, retro-open-question-deferral]
  aliases: [формат общения, reply format, форма ответа, отчёт о действиях, report of actions,
    один кейс, one case, схема кейса, case schema, контекст вопрос рекомендация ратификация,
    не переходить к следующему кейсу, no next case, фронтир, frontier, список фронтира,
    numbered list, нумерованный список, статус по каждому пункту, дважды за сессию, walked twice,
    перед планом и на retro, отложено через фидбек, marked deferred, sprint.md фронтир,
    brief генерируется, generated from sprint, grill-me расширяет, наследство сессии,
    inheritance, не читать прошлый handoff, previous handoff, бриф плюс feedback,
    маркеры ставит сессия, who marks the region, две стороны посадки правила, two parties,
    правило не садится в одну сессию, target в скобках, target in the bracket,
    куча вопросов, a pile, перенесённые и новые в одном списке, шестнадцать вопросов]

- group: what a review of the session's own record costs, and what it is worth
  definition: the instruments this project points at its own output — the retro's steps, the plan
    check, the advisories — and the measurements of what each of them actually returned. Answers
    "was that review step worth running, and what did it catch that nothing else would".
  slugs: [retro-menu-divergence, retro-ratification-abandonment, unnamed-attribution-shape,
    unclearable-verdict-recurrence, advisory-debt-decay, corpus-self-reference-share,
    session-fixed-context-cost]
  aliases: [меню в retro, menu step, прозой а не меню, enumerated prose, ратификация списком,
    ratification step, нет контекста, стена фрагментов, форма не названа, shape not named,
    он сказал но не назвали форму, атрибуция без формы, вердикт который не снять,
    unclearable verdict, красный навсегда, permanently red, третий раз в том же месте,
    advisory не гасят, debt count, 9 of 15, 9 of 17, счётчик долга, decoration,
    корпус про себя, about itself, доля продукта, product share, 12 процентов,
    124 коммита, 2 коммита в src, что грузится до первого промпта, fixed context cost,
    50 KB, 13000 токенов, CLAUDE.md дважды, injected twice, вложенный CLAUDE.md]
