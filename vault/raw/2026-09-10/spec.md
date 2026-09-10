<!-- approved 10:25:13 · session c640ade7 -->

# GUPPI — Slice 3: materialize, generate, cleanup, librarian, retro, handoff

Spec слайса. Собран из Cases 29–41, ратифицированных в сессии E 2026-09-10. Ledger-строки
уже в `raw/2026-09-10/ledger.md`, написаны хуком. Этот документ копирует в
`raw/2026-09-10/spec.md` хук `guppi spec` при одобрении. Его читает `guppi materialize`:
под каждым Case стоит YAML-блок с тегом `then` (Case 30, место задано в Case 34). Всё в
блоках — по-английски, это ложится в vault. Проза — по-русски, как в чате.

Форма блока `then`: `create` (slug, type, kind, purpose, enforcement, implementation_ref или
governs и render_mode, parent, children, tags, sections, estimate), `update` (slug, file для
Rule-class файла, set, sections, replace, change), `defer` (slug, type, purpose), `new_tags`.
Категория страницы — из префикса slug. Rule-class файлы (`index`, `glossary`, `case-schema`,
`<cat>-schema`, `<cat>-schema-yaml`, `claude-md`, `migration-plan`) правит главный агент
руками в Work Mode; скрипт их не трогает, но Decision-страница на них ссылается.

## Контекст

После Slice 2 vault пишется руками: страницы, `log.md`, History, brief. Decision-страниц нет
ни одной за 41 Case. Уроки живут строками в ledger. Retro и handoff идут по памяти, без
skill'ов. Slice 3 закрывает это: три скрипта (`materialize`, `generate`, `cleanup`), агент
`librarian-guppi` из семи правил, MOC `rule-harness` для инструментов без фазы, фаза
End of Work (`/retro`, хук перед `/handoff`, `/handoff`), новый формат Case и правки
документов, которые из всего этого следуют.

Из брифа: пять чтений Slice 2 — два взяты сегодня (`hook-registry-rendered`, `ask-finds`),
`pretask-reconciles` взято этим Plan Mode, `pretask-hook-gates` и `spec-capture-appends`
снимаются этим одобрением. Case 28 (Method для MOC ручных чтений) закрыт и закоммичен.

## Case 29 — Slice 3: scope and order

> **context:**
> `sprint.md` называет Slice 3: materialize, generate, librarian, retro, handoff. Карта Slice 0 шире: ещё Work Mode и `subagent-guppi`.

> **problem:**
> Граница слайса и порядок Cases.

> **recommend:**
> Slice 3 = `rule-documentation` с детьми, `rule-end-of-work`, `rule-harness`, конвенция Spec, сопутствующие правки. Work Mode и `subagent-guppi` — Slice 3b, свой Plan Mode: в миграции работу делает главный агент, цепочке нечего enforce'ить.

> **given:**
> Черновики `rule-documentation` и `rule-end-of-work` лежат в `docs/migration/`.
> **＋** Агент, отрендеренный в сессии, виден только со следующей. Хуки проекта внутри субагента не работают.
> **－** Phase 1 миграции не требует Work Mode.

> **when:**
> Следующая сессия открывает Frontier.

> **then:**
> `rule-work-mode` и `rule-subagent-guppi` стоят в `rules-index.md` как `draft` placeholder.
> **＋** `sprint.md` называет Slice 3b после Slice 3.

> **ratification:** ратифицирован.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Prevents implementation starting before the plan, branch and baseline exist
  - slug: rule-subagent-guppi
    type: rule
    purpose: Prevents implementation drifting from the ratified plan while it is being executed
```

## Case 30 — the `then` block

Ратифицирован, затем перекрыт Case 34: блок `then` живёт в Spec, не в чате. Форма блока —
как в шапке этого документа. Записи ниже дают только строку History; содержание несёт Case 34.

```then
update:
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "then carries a YAML block tagged then, read by guppi materialize (superseded by case 34 on where the block lives)"
  - slug: rule-case-protocol
    change: "the Render names the then block (superseded by case 34)"
```

## Case 31 — `rule-materialize`

> **context:**
> Первый шаг Documentation. Скрипт собирает `raw/<date>/materialize.yaml` из ledger и Spec. Librarian читает yaml вместо ledger и Spec (§10).

> **problem:**
> Форма yaml, грамматика строк, ledger со Spec старше конвенции, имена Decision-страниц.

> **recommend:**
> `uv run guppi materialize [--date]`. Одна запись на строку ledger. Маршрут по §5. Содержание из блоков `then` Spec. Decision-страница одна на Case (31.1). Существующий yaml дополняется (41).

> **given:**
> `index.md` §4: `decision` → действие, содержание из Spec; `estimate` → статус и результат; `lesson` → `create` из строки; `supersedes` — цепочка.
> **＋** `guppi/ledger.py` разбирает строки: переиспользуется.
> **＋** Ledger 2026-09-09: 85 строк, HTML-комментарии, строки без времени, `{ref}`, `{source}`, `{supersedes}`. Его Spec без блоков `then`. Страницы уже существуют.
> **－** Decision-страниц нет ни одной.

> **when:**
> Librarian или главный агент запускает `uv run guppi materialize`.

> **then:**
> В `raw/<date>/materialize.yaml` есть запись на каждую строку-запись ledger, в порядке ledger: `case`, `kind`, `category`, `slug`, `ref`, `source`, `supersedes`, `origin`, `line`, `text`, `decision`, `fields`, `sections`, `replace`, `change`, `incomplete`, `exists`.
> **＋** `category` — из префикса slug; Rule-class файл — `file` с путём.
> **＋** Вложенный `estimate` из блока `create` — своя запись `create`.
> **＋** `estimate`-строка для страницы этого ledger сложена в её запись; для ранней страницы — запись `estimate`.
> **＋** `lesson`-строка — запись `create` в `lessons` с `root_cause`, `Trigger`, `Root cause`; `origin` `#L<n>`.
> **＋** Запись, перекрытая `supersedes`, несёт `superseded_by`.
> **＋** Блока `then` под Case нет — `incomplete: then`. Страница `create` уже на диске — `exists: true`.
> **＋** Одна Decision-запись на Case: `decision: decision-case-<N>`, `case_text` из семи цитат, `targets` из всех строк Case.
> **－** Строка, которую грамматика не разобрала, — в `unparsed`; скрипт продолжает.
> **－** Существующий yaml не переписывается: см. Case 41.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-materialize
    type: rule
    kind: Leaf
    purpose: Prevents the librarian from reading the ledger and the Spec itself, or from routing a decision by guesswork
    enforcement: check
    implementation_ref: [guppi/materialize.py, tests/test_materialize.py]
    parent: rule-documentation
    tags: [harness, workflow, ledger]
    sections:
      Purpose: |
        Prevents the librarian from reading the ledger and the Spec itself, or from routing
        a decision by guesswork. The yaml is the one input a clean context needs. Every line
        of the ledger is an entry. Its route is computed from `index.md` §5. Its content is
        lifted from the `then` block of its Case in the Spec. What is missing is named, not
        invented. If a route cannot be derived from the ledger and the Spec alone, that is a
        defect of the ledger, and it shows here.
      How it works: |
        `uv run guppi materialize [--date YYYY-MM-DD]` reads `raw/<date>/ledger.md` and
        `raw/<date>/spec.md` and writes `raw/<date>/materialize.yaml`.

        One entry per record line, in ledger order. Fields: `case`, `kind` (`create`,
        `update`, `delete`, `defer`, `estimate`, `lesson`), `category` (from the slug
        prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`; a Rule-class file
        is `file` with its path), `slug`, `ref`, `source`, `supersedes`, `superseded_by`,
        `origin` (`raw/<date>/ledger.md#case-N`; a lesson `#L<n>`), `line`, `text` (the
        ledger line), `tags` (from `{tags:...}`), `fields`, `sections`, `replace`, `change`
        (from the `then` block), `incomplete` (required fields the block lacks), `exists`
        (a create whose page is on disk), `applied` (set by `guppi generate`).

        The Spec is read by headings `## Case N` and `### Case N.M`. Under a heading, every
        fenced block tagged `then` up to the next heading is YAML; a leading `> ` is
        removed. The entry for a slug is the item with that `slug` under the key of its
        kind. A Leaf's nested `estimate` becomes its own `create` entry. An `estimate` line
        for a page created in the same ledger is folded into that create (`status`,
        `result`); for an earlier page it is an `estimate` entry, an update. A `lesson` line
        is a `create` in `lessons`: `kind`, `root_cause` and the sections `Trigger` and
        `Root cause` from the line. A line with `{supersedes:case N}` marks the entries of
        case N `superseded_by`. One decision entry per Case: `decision: decision-case-<N>`,
        `case_text` (the seven quoted sections of the Case, verbatim, in the language of
        the Spec), `targets` (one item per line of the Case). A line the grammar does not
        parse goes under `unparsed`; the script continues.

        An existing yaml is extended, never rewritten (case 41): entries whose `line` is
        present stay as they are, with the librarian's edits and the `applied` marks; new
        ledger lines become new entries at the end; an entry whose stored `text` differs
        from the ledger line at that number is reported on stderr and left alone; a later
        `supersedes` adds `superseded_by` to the earlier entry and changes nothing else; an
        `estimate` line for a create already `applied` becomes its own `estimate` entry.
        The count of entries added goes to stdout. Exit 0.
    estimate:
      slug: estimate-materialize-assembles
      kind: QA
      context: "The yaml is the librarian's whole view of the session. An entry routed wrong, or a line dropped, is a decision that never becomes a page."
      criterion: |
        Against a temp vault: a ledger with timed and untimed lines, HTML comments, a create
        with ref and tags, a Leaf create whose estimate sits nested in the Spec's then
        block, an update with set, sections and replace, a delete, a defer without ref, a
        supersedes chain, an estimate line for a page of this ledger and one for an earlier
        page, a lesson line and one unparsable line yields a yaml with one entry per record
        line in ledger order, each with case, kind, category, slug, origin, line, text and
        the decision slug of its Case; the nested estimate is its own create entry; the
        superseded entry carries superseded_by; the first estimate line is folded into its
        create, the second is an estimate entry; the lesson entry carries root_cause and
        origin #L<n>; the unparsable line is under unparsed; a create without a then block
        is marked incomplete, a create whose page exists is marked exists; a Rule-class slug
        routes to file with its path; one decision entry per Case carries case_text and
        targets. An existing yaml gains only the entries of ledger lines it does not hold,
        keeps its edited and applied entries, reports a text mismatch, gains superseded_by
        from a later supersedes, and turns an estimate line for an applied create into an
        estimate entry. Live: --date 2026-09-09 over the 85-line ledger yields no unparsed
        line and every create marked exists; the reading records the counts per kind.
      method: pytest in tests/test_materialize.py against a temp vault; the live reading once by hand
```

### Case 31.1 — Decision pages: one per Case, out of the search path

> **given:**
> Схема decisions: одна страница на строку. Case 11 дал бы восемь одинаковых страниц.
> **＋** Render `ask-guppi` не запрещает Grep по `wiki/`.
> **－** Индексов decisions нет и не будет.

> **when:**
> `guppi generate` пишет Decision-страницу. `ask-guppi` ищет.

> **then:**
> Одна страница на Case, slug `decision-case-<N>`, строки Case — список `targets`.
> **＋** `ask-guppi` не открывает и не grep'ит `wiki/decisions/`, если вопрос не «почему так решили».
> **－** Ничего не архивируется.

> **ratification:** ратифицирован.

```then
update:
  - slug: decisions-schema
    file: vault/wiki/decisions/schema.md
    change: "one page per Case; kind, target_category, target_slug, ref, source move into a targets list; slug is decision-case-<N>; raw/ stays in place, it is not archived with the session"
  - slug: decisions-schema-yaml
    file: vault/wiki/decisions/schema.yaml
    change: "required [type, case, status, targets, origin, sprint, created, tags]; optional [supersedes, superseded_by]; values: status only"
  - slug: rule-ask
    change: "the agent does not open or grep wiki/decisions/ unless the question asks why something was decided"
    replace:
      - old: "Grep `vault/wiki/index.md` when the proposal may cross a rule of the vault itself."
        new: "Grep `vault/wiki/index.md` when the proposal may cross a rule of the vault itself. Do not open or grep `vault/wiki/decisions/` unless the question asks why something was decided; then reach the Decision through the page's `origin`. Decisions have no index on purpose."
```

## Case 32 — `rule-page-generation`

> **context:**
> Единственный писатель в `wiki/`. Пишет страницы, обратные ссылки, History, `log.md`, теги, считает `built`.

> **problem:**
> Что скрипт выводит механически, какими шаблонами, как ведёт себя при ошибке и повторе.

> **recommend:**
> `uv run guppi generate [--date]` применяет записи yaml по порядку и помечает их `applied`. Ошибка записи — stderr, остальные применяются, exit 1. Чего нет в записи, того нет на странице.

> **given:**
> Черновик: коллизия — ошибка; страница создаётся всегда; `origin`, `status`, `parent`, `children`, backlinks — производные.
> **＋** У Estimate нет статуса `archived`, хотя схема уроков велит архивировать Estimate error-урока. Статуса `deleted` нет ни в одной `schema.yaml`.
> **＋** `sprint` — первый заголовок `## <id>` в `sprint.md`.
> **－** Все 34 страницы и `log.md` написаны руками.

> **when:**
> Librarian или главный агент запускает `uv run guppi generate`.

> **then:**
> `create` даёт страницу с полями записи и производными: начальный статус по категории, `origin`, `sprint`, `created`, `parent` из `ref`, `target` из `ref`. Секции в порядке схемы. Первая строка History.
> **＋** Родитель получает `children += slug` в конец, цель Estimate — `estimates += slug`; их секции пересобраны, у них строка History.
> **＋** `update`: `set`, `sections`, `replace` (сравнение со схлопнутыми пробелами, ровно одно вхождение), History `updated: <change>`.
> **＋** `estimate`: `status`, `## Result` целиком, History `status: a → b`. Страница уже в этом статусе с Result — пропуск.
> **＋** `delete`: `status: archived`, History `deleted`. `defer`: History `deferred` или placeholder `draft` из полей Case.
> **＋** `lesson`: страница урока и парный Estimate по шаблону. Decision-страница на Case; `supersedes` ставит ранней `superseded`.
> **＋** Каскад: все Estimates `passed` → `built`; `built` с не-`passed` → `draft`. `severity` Insight пересчитан.
> **＋** Объявленный новый тег — в `tags.md`; необъявленный — сообщён. `log.md`: строка на запись.
> **－** Коллизия, `ref` без страницы, `replace` не найден — запись пропущена, stderr, exit 1.
> **－** Повторный запуск ничего не пишет.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-page-generation
    type: rule
    kind: Leaf
    purpose: Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified
    enforcement: check
    implementation_ref: [guppi/generate.py, tests/test_generate.py]
    parent: rule-documentation
    tags: [harness, workflow, ledger]
    sections:
      Purpose: |
        Prevents a ratified decision from ending the session without a page, or a page from
        carrying a field nobody ratified. The script is the only writer to `wiki/`. It lays
        the content of `materialize.yaml` into schema fields, derives what is derivable and
        writes nothing else. A page is always created, even incomplete: red lint is an
        accurate signal of debt, a decision with no page is the ledger and the vault
        disagreeing silently. A slug collision is an error, never a rename.
      How it works: |
        `uv run guppi generate [--date]` applies the entries of `raw/<date>/materialize.yaml`
        in order and marks each applied entry `applied: <time>` in the yaml, so a rerun
        writes nothing. An entry that fails — a collision, a `ref` naming no page, a
        `replace` whose text is absent or not unique — is reported on stderr and skipped;
        the rest apply; the exit code is 1.

        Initial `status` by category: entity and rule `draft`, estimate `pending`, lesson
        `new`, insight `open`, decision `current`. `sprint` is the first `## <id>` heading
        of `sprint.md`; `created` is the yaml's date. Body sections follow the order of the
        category's `schema.yaml`: `Purpose` from `sections` or the `purpose` line;
        `Estimates`, `Children` (numbered for a rule), `Parent`, `Implementation` from the
        fields; `Render`, `How it works`, `Context`, `Criterion`, `Method`, `Result`,
        `Trigger`, `Root cause`, `Pattern`, `Proposal` from `sections` or the estimate's
        fields. A field or section the entry lacks is not written: lint names it.

        History lines: `created`, `updated: <change>`, `status: a → b`, `deleted`,
        `deferred`, `child <slug> added`, `estimate <slug> added`, each `· <origin>`;
        `log.md` gets the same line with `<category>/<slug>` in front. A `create` with `ref`
        appends the slug to the parent's `children` (order kept) or, for an estimate, to
        the target's `estimates`, and rebuilds that section. An `update` applies `set` to
        the frontmatter, `sections` as whole replacements, `replace` inside the body
        (whitespace-collapsed match, exactly one occurrence), and appends History. An
        `estimate` entry sets `status`, overwrites `## Result` and appends History; a page
        already at that status with a Result is skipped. A `delete` sets `status: archived`
        with History `deleted`; there is no `deleted` status. A `defer` with a page appends
        History `deferred`; without one it writes a placeholder page, `status: draft`, with
        only the fields the Case gave.

        A lesson's paired Estimate is `estimate-<lesson slug without lesson->`, target the
        lesson, tags the lesson's. `error`: kind `QA`, status `passed`, criterion "The
        failure named in Trigger was observed directly", method "The observation itself,
        by hand; recorded in the ledger line", result "Observed. The ledger line is the
        record." `knowledge`: kind `Research`, status `pending`, criterion "The claim in
        Root cause holds when read live", method "One live reading by hand, recorded in
        the estimate line". A missing `source` is not invented; lint names it.

        One Decision page per Case, `decisions/decision-case-<N>.md`: `case`, `status:
        current`, `targets`, `supersedes`, `origin`, `sprint`, `created`, `tags` (the union
        of the targets' tags); body `Context`, `Now`, `Problem`, `Then` from `case_text`
        (`given` fills `Now`). A `supersedes` sets the earlier page `status: superseded`
        and appends the new slug to its `superseded_by`. A decision page that exists is
        skipped. A `create` marked `exists` writes no page and no History; its decision
        page is still written.

        After all entries: an entity or rule whose Estimates are all `passed` becomes
        `built`, a `built` one with an Estimate not passed returns to `draft`, both with a
        History line; the `severity` of every insight is recounted. A tag declared in
        `new_tags` is appended to `tags.md` with its meaning and aliases; a tag used but not
        declared and not registered is reported on stderr and left on the page.
    estimate:
      slug: estimate-generate-writes
      kind: QA
      context: "Every page of the vault comes through this script from Slice 3 on. A derived field computed wrong, or a ratified one dropped, is corrupted everywhere at once."
      criterion: |
        Against a temp vault from one yaml: a MOC rule create, a Leaf child create with ref
        and its nested estimate yield three pages that pass their schema.yaml, the parent's
        children and ## Children in order, the target's estimates and ## Estimates; an
        update with set, sections, replace and change changes the field, the section, the
        text and appends History; a replace absent or not unique fails that entry alone,
        exit 1; a delete sets archived with History; a defer without a page writes a
        placeholder with only the Case's fields; an estimate entry sets status and
        overwrites ## Result, and one whose page already holds that status with a Result is
        skipped; a lesson entry writes the lesson and its paired estimate per kind; one
        decision page per Case with targets, and supersedes marks the earlier page
        superseded; the cascade sets built; a declared new tag lands in tags.md, an
        undeclared one is reported; log.md gains one line per write; applied entries are
        marked and a rerun writes nothing; a create colliding with a page not marked exists
        fails. Live: the 2026-09-10 yaml and the 2026-09-09 backfill; the reading records
        pages created per category, make lint afterwards against the known-false list, and
        git diff --stat.
      method: pytest in tests/test_generate.py against a temp vault; the live reading once by hand
update:
  - slug: lessons-schema
    file: vault/wiki/lessons/schema.md
    change: "an error lesson's Estimate is created passed, not archived; estimates have no archived status; the estimates row and the example follow"
```

## Case 33 — `rule-cleanup`

> **context:**
> Страница со `status: archived` должна уйти из живого vault. Скрипта нет.

> **problem:**
> Куда переносить. Кто правит ссылки. Что с `raw/`.

> **recommend:**
> `guppi cleanup`. Архив `vault/archived/<sprint>/<date>/<category>/<slug>.md`. Скрипт правит `children` и `estimates` живых страниц. Обратный ход тоже его. `raw/` на месте.

> **given:**
> `wiki/archive/` пуст. `index.md` §1 и glossary называют `wiki/archive/`, lint читает его.
> **＋** `vault/archive/` занят старым архивом, 505 файлов, до Slice 5.
> **＋** Каждый `origin` указывает в `raw/<date>/`.
> **－** Черновик велит переносить `raw/`. Это сломает origin.

> **when:**
> Librarian запускает `uv run guppi cleanup`.

> **then:**
> Каждая живая страница со `status: archived` лежит в `vault/archived/<sprint>/<date>/<category>/<slug>.md`.
> **＋** У неё строка History `archived · cleanup`. В `log.md` такая же.
> **＋** Её slug убран из `children` и `estimates` живых страниц. Секции пересобраны. У них строка History.
> **＋** Индексы пересобраны без неё.
> **＋** Страница в архиве со статусом не `archived` вернулась в `wiki/<category>/`. History `restored · cleanup`.
> **－** `children` у Insight не меняются. `[[slug]]` в тексте не меняются.
> **－** Живая страница, чей `parent` или `target` ушёл в архив, остаётся. Флаг в stderr.
> **－** Повторный запуск ничего не переносит. Exit 0.
> **－** Файл, который нельзя перенести, или занятое имя — stderr, exit 1. Остальные переносятся.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-cleanup
    type: rule
    kind: Leaf
    purpose: Prevents an archived page from staying among the live ones, or the indexes from lagging behind the vault
    enforcement: check
    implementation_ref: [guppi/cleanup.py, tests/test_cleanup.py]
    parent: rule-documentation
    tags: [harness, workflow]
    sections:
      Purpose: |
        Prevents an archived page from staying among the live ones, or the indexes from
        lagging behind the vault. `archived` is a status the generator sets. The file move
        is this script's, so a page never disappears by an agent's hand. `raw/<date>/` stays
        where it is: every `origin` points into it and lint checks that path.
      How it works: |
        `uv run guppi cleanup` moves every live page with `status: archived` to
        `vault/archived/<sprint>/<date>/<category>/<slug>.md`. `sprint` is the first `## <id>`
        heading of `sprint.md`, `date` the day of the run. The moved page gets the History
        line `archived · cleanup`; `log.md` gets the same. The slug is removed from the
        `children` and `estimates` lists of live pages, their sections are rebuilt and they
        get a History line; an Insight's `children` keep archived lessons, since `severity`
        counts the live ones. `[[slug]]` links in page bodies are not changed: Obsidian
        resolves a name in any folder, and lint counts archived slugs as known. A live page
        whose `parent` or `target` went to the archive is reported on stderr and left.

        A page under `vault/archived/` whose status is no longer `archived` moves back to
        `wiki/<category>/` with the History line `restored · cleanup`. Then the indexes are
        rewritten with the writer of `guppi index`. A rerun moves nothing and exits 0. A
        file that cannot be moved, or a name already taken in the archive, is reported on
        stderr with exit 1; the other pages still move.
    estimate:
      slug: estimate-cleanup-moves
      kind: QA
      context: "A page left live after archival keeps its index line and its findings. A page moved without its History line loses the trace of when it left."
      criterion: |
        Against a temp vault: every live page with status archived moves to
        vault/archived/<sprint>/<date>/<category>/ under the same file name with a History
        line and a log.md line; its slug leaves the children and estimates lists of live
        pages and their sections, with a History line there; an Insight's children keep
        it; body wikilinks stay; pages with any other status stay; a page in the archive
        whose status is not archived moves back with History restored; the category
        indexes are rewritten without the moved page; a live page whose parent or target
        is archived is reported; a rerun moves nothing and exits 0; an unmovable file or a
        taken name is reported with exit 1 and the rest still move. Live: one run over the
        vault with nothing to move exits 0 and leaves git diff empty.
      method: pytest in tests/test_cleanup.py against a temp vault; the live reading once by hand
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§1: the archive is vault/archived/<sprint>/<date>/<category>/, raw/ stays in place; cleanup moves and restores"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "the archived row names vault/archived/<sprint>/<date>/<category>/ and guppi cleanup"
```

## Case 34 — формат Case

> **context:**
> Case стал тяжёлым. Новый формат должен лечь в `case-schema.md`, Render `rule-case-protocol` и грамматику ledger.

> **problem:**
> Формат живёт только в чате.

> **recommend:**
> Семь блоков: context, problem, recommend, given, when, then, ratification. Операнды **＋** и **－**. Простой язык. `when` плюс `then` — критерий Estimate. Блок `then` — в Spec. Превью — в `ratification`. `{tags}` в строке `create`. Категория из префикса slug.

> **given:**
> `case-schema.md`: шесть секций, `then` несёт страницу целиком.
> **＋** `index.md` §4: грамматика без тегов.
> **－** Про операнды и простой язык не говорит ни один файл.

> **when:**
> Агент пишет Case. Хук `Stop` читает ответ. `guppi materialize` читает Spec.

> **then:**
> Case состоит из семи цитат. Имя блока с двоеточием.
> **＋** Строки given, when, then после первой начинаются с **＋** или **－**.
> **＋** Превью ledger-строк — в `ratification`, fence без тега.
> **＋** Строка `create` несёт `{tags:a,b}`. Категория из префикса slug.
> **＋** В Spec под каждым Case стоит блок `then`.
> **－** В чате блока нет. Правило LEDGER не меняется.

> **ratification:** ратифицирован.

```then
update:
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "seven sections in the order context, problem, recommend, given, when, then, ratification; operands; simple language; when+then is the Estimate criterion; the then block lives in the Spec; the ledger preview sits in ratification; the example is decision-case-<N>"
  - slug: rule-case-protocol
    change: "the Render describes the seven sections, the operands, the then block in the Spec, and {tags} on a create line"
    sections:
      Render: |
        <!-- rule-case-protocol -->
        ## Case protocol

        One reply is one Case, in the seven sections of `case-schema.md`: context, problem,
        recommend, given, when, then, ratification. Never move to the next Case until this
        one is ratified or deferred. Plan Mode does not end while a Frontier item is neither
        ratified nor deferred.

        A follow-up question that asks you to justify a choice does not split the Case; one
        whose answer needs a new choice does — into sub-cases `N.1`, `N.2`. Ratifying a
        parent does not ratify its children.

        A Case renders as `## Case N — name`, then one blockquote per section: its first
        line `**name:**`, its text on the following quoted lines, a blank line between
        sections. In `given`, `when` and `then` every line after the first starts with a
        bold operand: **＋** for one more condition or action, **－** for a limit or an
        exception. `when` and `then` together are the criterion of the Estimate the Case
        creates. Write short sentences, one idea each, in the active voice. A sub-case is
        `### Case N.M — name` under its parent, with its own `given`, `when`, `then` and
        `ratification`; the sections the children share live on the parent. The
        `ratification` section ends with a preview of the ledger lines in an untagged
        fence. The page content itself — fields, prose sections, the Estimate — is a YAML
        block tagged `then` under the Case in the Spec, not in the chat; `guppi
        materialize` reads it, and what is not in that block was signed by nobody.

        Before a `create` without a `ref`, ask the vault first: does this exist, what
        conflicts, what sits in `draft`, which tags fit. Put the answer in `given`.
        Dispatch the `ask-guppi` agent with one short question.

        Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with
        the time of writing. A record is a `- decision[...]`, `- estimate[...]` or
        `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag; the same
        line anywhere else — bare, or in a block with another tag or none — is a preview
        and is never written. A `create` line carries the ratified tags: `{tags:a,b}`.
        Write the `- decision[...]` lines only in the reply that acknowledges ratification;
        `- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson
        exists. Without `/hi` the hook refuses and says so: tell the person, do not retry.
        <!-- /rule-case-protocol -->
  - slug: index
    file: vault/wiki/index.md
    change: "§4: a create line carries {tags:a,b}; §2: seven sections"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "the Case row names the seven sections"
```

## Case 35 — три шага суждения librarian'а

> **context:**
> Между скриптами librarian сверяет новые страницы с индексами, собирает Insight, пишет brief. Каждая — partial render в файл агента.

> **problem:**
> Границы каждого шага.

> **recommend:**
> Три Leaf `render partial`, родитель `rule-documentation`. Новый тег `librarian`.

### Case 35.1 — `rule-index-check`

> **given:**
> §10: единственное суждение — `create` → `update` при дубликате. Остальное — флаг.
> **＋** Индексы: одна строка на живую страницу. Сравнение не идёт между категориями.
> **＋** `handoff.md` несёт прямые указания.

> **when:**
> Librarian прочитал `materialize.yaml` и `handoff.md`.

> **then:**
> Он выполняет указания из `handoff.md` первыми.
> **＋** Для каждой записи `create` сравнивает `purpose` (`criterion`, `root_cause`) со строками индекса той же категории по смыслу.
> **＋** Дубликат: запись становится `update` найденной страницы, `change: merged by librarian: <why>`, пометка `librarian: merged`.
> **＋** Похожая страница: флаг `near: <slug>`.
> **－** Он не читает страницы без нужды. Не меняет содержание. Не сравнивает между категориями.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-index-check
    type: rule
    kind: Leaf
    purpose: Prevents a page from being born twice under two names
    enforcement: render
    governs: .claude/agents/librarian-guppi.md
    render_mode: partial
    parent: rule-documentation
    tags: [harness, workflow, librarian]
    sections:
      Purpose: |
        Prevents a page from being born twice under two names. Pre-task asked the vault
        before the Case; this asks once more, with the finished content, before the page is
        written. It is the one judgment the librarian acts on. Catching a duplicate here
        avoids a page created and merged in the same session.
      Render: |
        <!-- rule-index-check -->
        Index check. Do what `handoff.md` asks first. Then, for each `create` entry in
        `materialize.yaml`, compare its `purpose` (`criterion` for an estimate, `root_cause`
        for a lesson) with every line of `vault/wiki/<category>-index.md` of the same
        category. Compare meanings, not words. Never compare across categories.
        - The same thing already has a page: change the entry to `kind: update` of that
          slug, add `change: "merged by librarian: <why>"` and `librarian: merged`. Keep
          every other field of the entry as it is.
        - A page is close but not the same: keep the entry and add `near: <slug>`.
        Open a page only when its index line is not enough to judge.
        <!-- /rule-index-check -->
    estimate:
      slug: estimate-index-check-merges
      kind: QA
      context: "A duplicate the librarian misses is two pages for one thing; one it invents is a ratified page silently merged away."
      criterion: |
        After a live librarian run: the report names the comparisons made per category; a
        create whose purpose an index line already carries was turned into an update of
        that slug with change "merged by librarian: ..." and the mark librarian: merged,
        with no other field changed; a near match was kept with near: <slug>; no page was
        read when its index line sufficed; no comparison crossed categories.
      method: one reading by hand after the first librarian run, recorded in the estimate line
new_tags:
  - tag: librarian
    meaning: the Documentation phase and its agent
    aliases: библиотекарь
```

### Case 35.2 — `rule-synthesis`

> **given:**
> §8: Insight рождается на втором уроке с общей причиной. `actioned` не конечный.
> **＋** Урок уходит в архив только когда его Insight стал `actioned`; Insight остаётся живым, его `pattern` в `insights-index.md`.
> **－** §8 и `insights/schema.md` велят искать в архиве. Это дорого и ничего не добавляет.

> **when:**
> В `materialize.yaml` есть запись `lesson`.

> **then:**
> Librarian сравнивает `root_cause` со строками `lessons-index.md` и `insights-index.md`.
> **＋** Второй живой урок, Insight нет: `create` в `insights` и `update` обоим урокам.
> **＋** Insight с тем же `pattern`: `update` Insight (`children` плюс урок, `status: open` если был `actioned`) и `update` уроку.
> **＋** Записи помечены `librarian: synthesis`. Генератор ставит Insight `origin: <date> · librarian`.
> **＋** §8 и `insights/schema.md`: архив не читается.
> **－** Он не читает архив, не пишет страницы сам. Один урок остаётся `new`. `Proposal` — предложение.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-synthesis
    type: rule
    kind: Leaf
    purpose: Prevents a pattern of failures from staying a list of unrelated incidents
    enforcement: render
    governs: .claude/agents/librarian-guppi.md
    render_mode: partial
    parent: rule-documentation
    tags: [harness, workflow, librarian, ledger]
    sections:
      Purpose: |
        Prevents a pattern of failures from staying a list of unrelated incidents. One
        lesson is an incident; two with one root cause are a pattern, and a pattern is what
        a later Case can fix. The archive is not read: a lesson is archived only when its
        Insight was actioned, and that Insight stays live with its pattern in the index, so
        a recurrence is caught there at the cost of one index line.
      Render: |
        <!-- rule-synthesis -->
        Synthesis. For each `lesson` entry, compare its `root_cause` with every line of
        `lessons-index.md` and of `insights-index.md`, by meaning.
        - A live lesson has the same cause and no Insight exists: append to the yaml a
          `create` in `insights` with `slug` (`insight-<area>-<pattern>`), `pattern`,
          `children` (both lessons), `tags` (the union), and `sections` `Pattern` and
          `Proposal`; and an `update` for each lesson with `set: {status: clustered,
          insight: <slug>}`.
        - An Insight has the same pattern: append an `update` of it with `children` plus
          the new lesson, and `set: {status: open}` when it was `actioned`; and an `update`
          for the lesson.
        Mark each entry you add with `librarian: synthesis`. One lesson without a pair
        stays `new`; that needs no flag. `Proposal` is a suggestion, never a decision. Do
        not read the archive and do not write pages yourself.
        <!-- /rule-synthesis -->
    estimate:
      slug: estimate-synthesis-clusters
      kind: QA
      context: "A missed pair is a pattern nobody sees; an invented pair is an Insight nobody ratified the basis of."
      criterion: |
        After a live librarian run with at least two lesson entries: the report names the
        comparisons made against lessons-index and insights-index; two lessons with one
        root cause produced one insight create entry with pattern, both children, the union
        of tags, Pattern and Proposal, and one update per lesson setting clustered and
        insight; a lesson matching a live Insight's pattern produced an update of that
        Insight and of the lesson; every added entry carries librarian: synthesis; no
        archive file and no lesson page was read; a lesson without a pair stayed new.
      method: one reading by hand after the first librarian run, recorded in the estimate line
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§8: the archive is not searched; an actioned Insight stays live and its pattern in insights-index catches a recurrence"
  - slug: insights-schema
    file: vault/wiki/insights/schema.md
    change: "Threshold: the archive is not searched; the live Insight's pattern catches a recurrence"
```

### Case 35.3 — `rule-brief`

> **given:**
> `brief.md` и `sprint.md` — рабочие файлы без схемы; их пишет librarian.
> **＋** Отложенное — не больше 7, ранг по severity, потом по числу переносов. Флаги без лимита.
> **＋** Librarian знает о сессии из `handoff.md` и yaml.
> **－** Никто не считает переносы.

> **when:**
> `guppi generate` и `guppi cleanup` отработали. Librarian запустил `make lint`.

> **then:**
> `brief.md` переписан целиком: где стоим; что делать первым; отложенное до 7; флаги без лимита; чтения на закрытие.
> **＋** Пункт отложенного несёт число переносов: прошлое плюс один.
> **＋** `sprint.md` меняется только по указанию из `handoff.md`.
> **－** Ни решений, ни оценок. Только факты и флаги из yaml, handoff и lint.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-brief
    type: rule
    kind: Leaf
    purpose: Prevents the next session from starting without the facts and the flags of this one
    enforcement: render
    governs: .claude/agents/librarian-guppi.md
    render_mode: partial
    parent: rule-documentation
    tags: [harness, workflow, librarian, session]
    sections:
      Purpose: |
        Prevents the next session from starting without the facts and the flags of this one.
        The brief is a shop window, not storage: every deferred item lives on as a draft
        page and pre-task finds it there. So the deferred list is capped, the flags are not,
        and nothing in the brief is a decision.
      Render: |
        <!-- rule-brief -->
        Brief. Run `make lint` and keep its output. Rewrite `vault/wiki/brief.md` in full,
        with these sections in this order:
        - Where things stand: from the "What actually got done" section of `handoff.md` and
          the counts of the yaml, pages created and updated per category.
        - What the next session does first.
        - Deferred: at most seven items. Rank by the `severity` of a related Insight, then
          by the number of times the item was postponed. Take that number from the previous
          brief and add one.
        - Flags, no limit: entries marked `incomplete`, `failed`, `near` or `unparsed`;
          failed Estimates; MOC candidates; stale defers; contradictions; the lint output.
        - Readings at the close: `make test`, `make lint`, page counts.
        Write facts and flags only. Add no decision and no judgment of the work. Change
        `vault/wiki/sprint.md` only when `handoff.md` tells you to, and only as it says.
        <!-- /rule-brief -->
    estimate:
      slug: estimate-brief-written
      kind: QA
      context: "The brief is the whole handover between sessions; a flag left out is debt nobody sees."
      criterion: |
        After a live librarian run: brief.md holds the five sections in order; the deferred
        list has at most seven items, each with its postponement count; every entry marked
        incomplete, failed, near or unparsed in the yaml appears under flags, as does the
        lint output; the brief states no decision; sprint.md changed only if handoff.md
        asked, and as it asked.
      method: one reading by hand after the first librarian run, recorded in the estimate line
```

## Case 36 — `rule-documentation`

> **context:**
> Семь детей фазы ратифицированы. Нужен MOC, который держит порядок и рамку файла агента.

> **problem:**
> Рамка агента и порядок шагов. Три ребёнка — скрипты без Render. Нет шага «коммит».

> **recommend:**
> MOC `render full` в `.claude/agents/librarian-guppi.md`. Дети: materialize, index-check, synthesis, page-generation, cleanup, brief, close. Агент несёт свой хук `PostToolUse`. Estimate: `make test-documentation` плюс живое чтение.

> **given:**
> Renderer требует Render у каждого ребёнка full-страницы.
> **＋** Правило Method: Estimate MOC называет make target.
> **＋** Агент виден со следующей сессии. Хуки проекта внутри субагента не работают.
> **－** Черновик кладёт index-check до generate, synthesis после — два прохода. Один проход лучше.

> **when:**
> Главный агент вызывает агента `librarian-guppi` после `/handoff`.

> **then:**
> Агент идёт по шагам: materialize, index-check, synthesis, generate, cleanup, brief, close.
> **＋** Читает только `handoff.md`, `materialize.yaml`, пять индексов, `tags.md`.
> **＋** Каждая его команда — строка в `event_log.md` через его хук.
> **＋** После запуска у каждой decision-строки есть Decision-страница и страница цели. Нет страницы без решения.
> **＋** Его коммит отдельный. `make test-documentation` зелёный.
> **－** Не останавливается спросить. Ошибка materialize останавливает его с отчётом.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-documentation
    type: rule
    kind: MOC
    purpose: Prevents a ratified decision from ending the session without becoming a vault page
    enforcement: render
    governs: .claude/agents/librarian-guppi.md
    render_mode: full
    children: [rule-materialize, rule-index-check, rule-synthesis, rule-page-generation, rule-cleanup, rule-brief, rule-close]
    tags: [session, workflow, harness, librarian, render]
    sections:
      Purpose: |
        Prevents a ratified decision from ending the session as a ledger line that nobody
        turned into a page. It also prevents the librarian from inventing anything on the
        way. The MOC is the agent file: its Render is the frame, the four children with a
        Render splice into it, the three scripts are called from the frame by name.
      How it works: |
        The librarian is an agent, not a skill, so the clean context is a property of how
        it is invoked, not a rule it must follow. It starts empty and reads four things.
        The order is one pass: the two judgments (index check, synthesis) edit the yaml
        before generation runs, so the generator writes once. Cleanup runs before the
        brief, so the brief sees the final graph and the lint output. The close commits
        only `vault/`, apart from the session's own commit. The agent's own `PostToolUse`
        hook writes its commands to the event log, since a subagent does not inherit the
        project's hooks; the hook is part of this Render and is ratified with it.
      Render: |
        <!-- rule-documentation -->
        ---
        name: librarian-guppi
        description: Turn this session's ratified decisions into vault pages. Runs after handoff, in a clean context, to the end.
        model: opus
        tools: Read, Grep, Glob, Bash, Edit, Write
        hooks:
          PostToolUse:
            - hooks:
                - type: command
                  command: uv run guppi event tool
        ---
        You are the librarian. You are the only writer to `vault/wiki/`, and you write only
        through the scripts named below. You decide one thing: whether a `create` is a
        duplicate. Everything else you flag. You never stop to ask: the person is gone.

        Read four things and nothing else: `vault/raw/<today>/handoff.md`,
        `vault/raw/<today>/materialize.yaml` once it exists, the five
        `vault/wiki/<category>-index.md` files, and `vault/wiki/tags.md`. Open a page only
        when a script reports a problem, or an index line is not enough to judge. Never read
        `ledger.md`, `spec.md`, `plan.md` or `wiki/decisions/`.

        Do the steps in this order.

        1. Run `uv run guppi materialize`. If it exits 1, write the report and stop.

        <!-- rule-index-check -->

        <!-- rule-synthesis -->

        2. Run `uv run guppi generate`. Every line on its stderr is a flag.

        3. Run `uv run guppi cleanup`. Every line on its stderr is a flag.

        <!-- rule-brief -->

        <!-- rule-close -->
        <!-- /rule-documentation -->
    estimate:
      slug: estimate-documentation-completes
      kind: QA
      context: "The phase either turns every ledger line into a page, or the vault and the ledger disagree silently."
      criterion: |
        make test-documentation runs the tests of materialize, generate and cleanup as one
        pipeline, green. Live, after the first librarian run: every decision line of the
        session's ledger has a Decision page and its target page; no page exists that no
        ledger line produced; the agent read only handoff.md, materialize.yaml, the five
        indexes and tags.md unless a script reported a problem; its commands are in
        event_log.md; its commit is separate from the session's; it did not stop to ask.
      method: "`make test-documentation`, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand"
```

### Case 36.1 — `rule-close`

> **given:**
> Коммит librarian'а должен быть отдельным от коммита Retro.
> **＋** Главный агент видит из запуска только отчёт.

> **when:**
> Librarian закончил brief.

> **then:**
> Он запускает `make lint` и держит вывод.
> **＋** Один коммит только путей `vault/`: `docs(vault): librarian, <date>`.
> **＋** Отчёт до двадцати строк.
> **－** Без `--amend`. Ничего вне `vault/`.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-close
    type: rule
    kind: Leaf
    purpose: Prevents the librarian's writes from landing in the session's own commit, or from ending without a commit at all
    enforcement: render
    governs: .claude/agents/librarian-guppi.md
    render_mode: partial
    parent: rule-documentation
    tags: [harness, workflow, git, librarian]
    sections:
      Purpose: |
        Prevents the librarian's writes from landing in the session's own commit, or from
        ending without a commit at all. The Retro commit is the baseline. What the librarian
        changed must be readable as one separate diff, six months on.
      Render: |
        <!-- rule-close -->
        Close. Run `make lint` and keep its output for the report. Commit only paths under
        `vault/`: `git add vault && git commit -m "docs(vault): librarian, <date>"`, never
        `--amend`, never anything outside `vault/`. Then return a report of at most twenty
        lines: pages created and updated per category, entries marked incomplete or failed,
        pages archived, the flags you raised, the lint total. Nothing else.
        <!-- /rule-close -->
    estimate:
      slug: estimate-close-commits
      kind: QA
      context: "The commit separates the librarian's layer from the session's; the report is the only thing the main agent sees of the run."
      criterion: |
        After a live librarian run: git log shows one commit after the Retro commit,
        touching only vault/ paths, with the message convention; the report reached the
        main agent with the counts, the flags and the lint total; the report is twenty
        lines or fewer.
      method: one reading by hand after the first librarian run, recorded in the estimate line
```

### Case 36.2 — renderer: ребёнок без Render

> **given:**
> `render_full` требует маркер для каждого ребёнка и ошибается на ребёнке без Render.
> **－** У `rule-documentation` три ребёнка — скрипты.

> **when:**
> `guppi render` рендерит full-страницу с ребёнком без `enforcement: render`.

> **then:**
> Такой ребёнок ничего не вносит. Маркер не нужен.
> **＋** Критерий `estimate-render-harness-reproduces` дополнен. Тест добавлен.
> **－** Маркер для такого ребёнка — ошибка, ничего не записано.

> **ratification:** ратифицирован.

```then
update:
  - slug: rule-render-harness
    change: "a child without enforcement render contributes nothing to a full render; a marker line for it is an error"
  - slug: estimate-render-harness-reproduces
    change: "criterion: a full page with a child that is not a render page renders without it, and errors on a marker line for it"
    replace:
      - old: "a partial target without markers exits 1 with nothing written;"
        new: "a partial target without markers exits 1 with nothing written; a full page whose children include a page without `enforcement: render` renders as if that child were absent, and exits 1 with nothing written when its text carries a marker line for it;"
```

## Case 37 — `rule-harness`

> **context:**
> Четыре правила не принадлежат фазе: renderer, реестр хуков, lint, индексы.

> **problem:**
> Где им жить.

> **recommend:**
> MOC `rule-harness` без `enforcement`. Дети в порядке `make lint`: render-harness, hook-registry, lint, index. Estimate: `make test-harness`.

> **given:**
> Три страницы несут `parent: rule-documentation`, lint даёт три `ref`-находки. `rule-hook-registry` — под `rule-session-start`, временно.
> **＋** §6: дети Rule MOC упорядочены. Правило Method: make target.

> **when:**
> Кто-то запускает `make test-harness`. Кто-то запускает `make lint`.

> **then:**
> `make test-harness` прогоняет тесты renderer'а, lint и индексов одним pipeline. Зелёные.
> **＋** `make lint` идёт в порядке детей: `render --check`, `index --check`, `guppi lint`. Первые два exit 0.
> **＋** Четыре страницы несут `parent: rule-harness`. Три `ref`-находки ушли.
> **－** `guppi lint` может быть красным на известном ложном.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-harness
    type: rule
    kind: MOC
    purpose: Prevents the tools of the harness from drifting apart from the pages that describe them
    children: [rule-render-harness, rule-hook-registry, rule-lint, rule-index]
    tags: [harness, workflow]
    sections:
      Purpose: |
        Prevents the tools of the harness from drifting apart from the pages that describe
        them. Four rules belong to no phase of the session: the renderer, the hook
        registry, lint and the indexes. They run together in `make lint`, in this order, and
        the order is the content: the harness files are checked against their pages before
        the indexes, the indexes before the pages.
    estimate:
      slug: estimate-harness-pipeline
      kind: QA
      context: "The four tools guard each other: a renderer that drifts is caught by lint, an index that lags by its check."
      criterion: |
        make test-harness runs the tests of the renderer, lint and the indexes as one
        pipeline, green; make lint runs render --check, then index --check, then guppi
        lint, and the first two exit 0 on the committed tree.
      method: "`make test-harness`, the pipeline over tests/test_render.py, tests/test_lint.py and tests/test_index.py; the live reading of make lint by hand"
update:
  - slug: rule-render-harness
    set: {parent: rule-harness}
    change: parent is rule-harness
    replace:
      - old: "`parent: rule-documentation` names the Documentation MOC of Slice 3, which does not exist yet as a page; the reference dangles until then, on purpose."
        new: "`parent: rule-harness` names the MOC of the harness tools: the renderer runs with lint and the indexes, in no phase of the session."
  - slug: rule-hook-registry
    set: {parent: rule-harness}
    change: parent is rule-harness
    replace:
      - old: "`parent: rule-session-start` is temporary: the registry holds the hooks of every phase and moves under a harness-wide MOC when one exists."
        new: "`parent: rule-harness`: the registry holds the hooks of every phase, so it sits with the tools of the harness, in no phase. A hook in an agent's own frontmatter is part of that agent's Render and is ratified with it; this registry holds `settings.json` only."
  - slug: rule-lint
    set: {parent: rule-harness}
    change: parent is rule-harness
    replace:
      - old: "`parent: rule-documentation` names the Documentation MOC of Slice 3, which does not exist yet as a page; the reference dangles until then, on purpose."
        new: "`parent: rule-harness` names the MOC of the harness tools: lint runs with the renderer and the indexes, in no phase of the session."
  - slug: rule-index
    set: {parent: rule-harness}
    change: parent is rule-harness
    replace:
      - old: "`parent: rule-documentation` names the Documentation MOC of Slice 3, which does not exist yet as a page; the reference dangles until then, on purpose."
        new: "`parent: rule-harness` names the MOC of the harness tools: the indexes are written and checked with the renderer and lint, in no phase of the session."
```

## Case 38 — `rule-end-of-work`

> **context:**
> Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

> **problem:**
> Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

> **recommend:**
> MOC, дети: `rule-retro`, `rule-retro-commit`, `rule-handoff`. `/retro` вызывает человек, `/handoff` — агент из Retro, поэтому хук его видит. Хук harness-tests не нужен: `/retro` запускает `make test` и `make style` через `!`.

> **given:**
> `/hi` показал образец skill'а. `rule-pretask-hook` — образец `PreToolUse`-отказа.
> **＋** Команда человека не проходит через `Skill`. `guppi event tool` читает поле `skill`.
> **－** `gh` не авторизован.

> **when:**
> Человек вызывает `/retro`. Агент вызывает `/handoff`. Librarian возвращает отчёт.

> **then:**
> Порядок держится: Retro, коммит, handoff, librarian. Handoff не начинается без коммита. Librarian — без `handoff.md`.
> **＋** `make test-end-of-work` зелёный.
> **－** После handoff главный агент не коммитит.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-end-of-work
    type: rule
    kind: MOC
    purpose: Prevents a session being handed over without a settled account of what happened
    children: [rule-retro, rule-retro-commit, rule-handoff]
    tags: [session, workflow]
    sections:
      Purpose: |
        Prevents a session being handed over without a settled account of what happened. It
        also prevents the librarian's writes from being indistinguishable from the
        session's own, by forcing a commit between the two. Three steps: the Retro
        conversation, the commit gate on the way to handoff, then handoff itself.
    estimate:
      slug: estimate-end-of-work-order
      kind: QA
      context: "The three steps only work in order: a handoff before the commit folds two layers into one diff; a librarian before the handoff has nothing to read."
      criterion: |
        make test-end-of-work runs the tests of the commit gate, green. Live: /handoff is
        refused while the tree is dirty; handoff.md exists before the librarian is
        dispatched; no commit is made between the handoff and the librarian's own.
      method: "`make test-end-of-work`, the pipeline over tests/test_gate.py; the live reading of the order by hand"
```

### Case 38.1 — `rule-retro`

> **given:**
> Retro смотрит на эту сессию. Правка кода допустима, если заканчивает работу из сегодняшнего ledger.
> **＋** Баг — `lesson[error]`. Красные тесты — `lesson[error]` с причиной «почему дошли до Retro с регрессией».
> **－** Skill'а нет.

> **when:**
> Человек вызывает `/retro`.

> **then:**
> В контексте до первого хода: `make test`, `make style`, сегодняшний ledger. Без read-вызовов.
> **＋** В `event_log.md` строка `retro`.
> **＋** Агент обсуждает только эту сессию. Правит только то, что ведёт к строке сегодняшнего ledger.
> **＋** Баг — `lesson[error]`. Отложенный — `defer`.
> **＋** Ответ заканчивается списком ратификаций, сделанного и несделанного. Когда человек одобрил — коммит, потом `/handoff` (Case 40).
> **－** `make lint` в Retro не запускается. Skill вызывает только человек.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-retro
    type: rule
    kind: Leaf
    purpose: Prevents a session from closing on work nobody reviewed, or on a change that traces to no decision
    enforcement: render
    governs: .claude/skills/retro/SKILL.md
    render_mode: full
    parent: rule-end-of-work
    tags: [session, workflow, harness, render]
    sections:
      Purpose: |
        Prevents a session from closing on work nobody reviewed, or on a change that traces
        to no decision. Retro is a conversation over this session only. The tests and the
        style check load before the first turn, so the person reads the result instead of
        waiting for it. The scope rule is mechanical: an edit is allowed when it finishes
        work a line of today's ledger ratified, and is new scope otherwise.
      Render: |
        <!-- rule-retro -->
        ---
        name: retro
        description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
        disable-model-invocation: true
        ---
        Recorded: !`uv run guppi event retro --session "${CLAUDE_SESSION_ID:-}"`

        Tests: !`make test`

        Style: !`make style`

        Ledger of today: !`cat "vault/raw/$(date +%F)/ledger.md"`

        Retro looks at this session only. Discuss what happened with the person in the Case
        form. Edit code only when the edit finishes work that traces to a line of today's
        ledger. Any other change is new scope: write a `- decision[case N][defer][slug]`
        line instead and, when it is a bug, a `- lesson[error][...]` line too. `gh` is not
        available: name a deferred bug in the handoff, so the brief carries it. Red tests
        are a `lesson[error]` whose root cause says why Retro was reached with a
        regression; the handoff still needs green. Do not run `make lint` here: the vault
        is written after handoff, by the librarian.

        Close with three lists: every ratification of this session, one line each; what
        got done; what did not. When the person approves, commit (`make style` clean,
        `make test` green), then call `/handoff`.
        <!-- /rule-retro -->
    estimate:
      slug: estimate-retro-loads
      kind: QA
      context: "A Retro that starts by reading files spends the context it exists to save; one that edits new scope hides a decision."
      criterion: |
        After a live /retro: the first turn's context holds the output of make test, make
        style and today's ledger with no read-tool call; event_log.md carries a retro line;
        every edit made in Retro traces to a line of today's ledger; every bug became a
        lesson[error] line, every deferral a defer line; the closing reply lists the
        ratifications, the done and the not done; the commit precedes the /handoff call.
      method: one reading by hand at the first /retro, recorded in the estimate line
```

### Case 38.2 — `rule-retro-commit`

> **given:**
> Инструкция «закоммить перед handoff» пропускается. Хук `PreToolUse` — нет.
> **－** Если `/handoff` наберёт человек, хук молчит. Сам skill проверяет дерево.

> **when:**
> Инструмент `Skill` вызван со skill `handoff`.

> **then:**
> `uv run guppi gate` читает `git status --porcelain`. Грязное дерево — exit 2 «commit first». Чистое — exit 0.
> **＋** Другой skill или инструмент — exit 0.
> **＋** `rule-hook-registry`: запись `PreToolUse`, matcher `Skill`.
> **－** Хук ничего не пишет и не коммитит.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-retro-commit
    type: rule
    kind: Leaf
    purpose: Prevents the handoff from starting on an uncommitted tree
    enforcement: hook
    implementation_ref: [guppi/gate.py, tests/test_gate.py, .claude/settings.json]
    parent: rule-end-of-work
    tags: [session, workflow, hooks, harness, git]
    sections:
      Purpose: |
        Prevents the handoff from starting on an uncommitted tree. An instruction to commit
        before handoff is a step an agent can skip; a `PreToolUse` hook cannot be skipped.
        The commit is what makes everything the librarian writes afterwards readable as a
        separate layer.
      How it works: |
        `uv run guppi gate` runs on `PreToolUse` with the matcher `Skill`. When
        `tool_input.skill` is `handoff` and `git status --porcelain` is not empty, it exits
        2 with the reason `commit first`, which blocks the call once; when the tree is
        clean it exits 0. Any other skill or tool: exit 0. The hook writes nothing and
        commits nothing. It sees only calls made through the `Skill` tool, which is how the
        Retro skill calls `/handoff`; the handoff skill checks the tree itself for the case
        where the person types it.
    estimate:
      slug: estimate-retro-commit-gates
      kind: QA
      context: "Without the gate, session work and librarian work land in one undifferentiated diff."
      criterion: |
        Given a PreToolUse payload naming the Skill tool with skill handoff: with a dirty
        tree, exit 2 with a reason naming commit first; with a clean tree, exit 0; another
        skill or another tool, exit 0 whatever the tree. Live: the first /handoff called
        from Retro on a dirty tree is refused, and passes after the commit.
      method: pytest in tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand
update:
  - slug: rule-hook-registry
    change: "PreToolUse, matcher Skill → uv run guppi gate"
    sections:
      Render: |
        <!-- rule-hook-registry -->
        {
          "permissions": {
            "defaultMode": "plan"
          },
          "hooks": {
            "SessionStart": [
              { "hooks": [ { "type": "command", "command": "uv run guppi event session-start", "timeout": 30 } ] }
            ],
            "PreToolUse": [
              { "matcher": "ExitPlanMode",
                "hooks": [ { "type": "command", "command": "uv run guppi pretask", "timeout": 30 } ] },
              { "matcher": "Skill",
                "hooks": [ { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] }
            ],
            "PostToolUse": [
              { "hooks": [ { "type": "command", "command": "uv run guppi event tool", "timeout": 30 } ] },
              { "matcher": "ExitPlanMode",
                "hooks": [ { "type": "command", "command": "uv run guppi spec", "timeout": 30 } ] }
            ],
            "Stop": [
              { "hooks": [ { "type": "command", "command": "uv run guppi ledger", "timeout": 30 } ] }
            ]
          }
        }
        <!-- /rule-hook-registry -->
```

### Case 38.3 — `rule-handoff`

> **given:**
> `handoff.md` несёт три раздела. Главный агент не перечитывает артефакты для него.
> **＋** Librarian — агент, его вызывает главный агент.
> **－** Skill'а нет.

> **when:**
> Агент вызывает `/handoff`.

> **then:**
> В контексте `git status --porcelain`. Не пуст — агент останавливается: «commit first».
> **＋** В `event_log.md` строка `handoff`.
> **＋** Агент дописывает `raw/<date>/handoff.md` из памяти: три раздела.
> **＋** Агент вызывает `librarian-guppi` одной строкой. Ждёт отчёт. Показывает его.
> **－** После этого не коммитит. Skill вызывает агент.

> **ratification:** ратифицирован.

```then
create:
  - slug: rule-handoff
    type: rule
    kind: Leaf
    purpose: Prevents the session's memory from being lost between the commit and the librarian
    enforcement: render
    governs: .claude/skills/handoff/SKILL.md
    render_mode: full
    parent: rule-end-of-work
    tags: [session, workflow, harness, render]
    sections:
      Purpose: |
        Prevents the session's memory from being lost between the commit and the
        librarian. The handoff note carries three things no artifact holds: where the
        person hesitated, what the librarian should check first, and what actually got done.
        It is written from memory, because re-reading the artifacts would spend the
        context advantage that is the note's only reason to exist.
      Render: |
        <!-- rule-handoff -->
        ---
        name: handoff
        description: Write the handoff note from memory and hand the session to the librarian.
        ---
        Recorded: !`uv run guppi event handoff --session "${CLAUDE_SESSION_ID:-}"`

        Tree: !`git status --porcelain`

        If Tree above is not empty, stop and say "commit first". Otherwise append to
        `vault/raw/<today>/handoff.md` (create it when missing; `---` before a new document
        in an existing file) a document headed `# Handoff — <date>, <slice or topic>` with
        three sections: `## Notes from memory` (where the person hesitated, what stayed
        unclear, which decisions carried caveats), `## Direct instructions to the
        librarian` (what to check first, what may duplicate what), `## What actually got
        done` (which Cases closed, where the code landed, what is not done). Write it from
        memory; do not re-read the artifacts. Short or empty sections are normal.

        Then dispatch the `librarian-guppi` agent with one line: `Materialize <date>.` Wait
        for its report and show it to the person unchanged. Do not commit after this.
        <!-- /rule-handoff -->
    estimate:
      slug: estimate-handoff-dispatches
      kind: QA
      context: "A handoff written from the artifacts says nothing the artifacts do not; one that skips the librarian leaves the ledger unmaterialized."
      criterion: |
        After a live /handoff: the first turn's context holds git status --porcelain and
        the skill stops on a dirty tree; event_log.md carries a handoff line; handoff.md
        gained a document with the three sections, written without read-tool calls on the
        artifacts; the librarian-guppi agent was dispatched with the date and its report
        was shown unchanged; no commit followed.
      method: one reading by hand at the first /handoff, recorded in the estimate line
```

## Case 39 — хвосты

> **context:**
> Cases 29–38 меняют слова в файлах, которые никто не назвал целиком.

> **problem:**
> Документы противоречат построенному.

> **recommend:**
> Пять `update` руками.

> **given:**
> §3 «sets `status: deleted`». §11 «Regenerated by lint». §1 «appended by hook». Glossary: строки Retro, Handoff, Documentation «(draft)». `CLAUDE.md`: «no `/retro`, `/handoff`, no librarian». `rule-session-start` держит `rule-hook-registry`.

> **when:**
> Агент читает эти файлы в следующей сессии.

> **then:**
> §3: `delete` ставит `archived`. §11: пишет `guppi index`, lint сверяет. §1: `log.md` и History пишут скрипты.
> **＋** Glossary без `deleted`; строки Retro, Handoff, Documentation указывают на страницы.
> **＋** `CLAUDE.md`: `/retro`, `/handoff`, librarian существуют со Slice 3; brief пишет librarian.
> **＋** `rule-session-start`: дети `[rule-skill-hi, rule-event-log, rule-ledger-write]`.
> **－** `docs/migration/` не трогаем до Slice 5.

> **ratification:** ратифицирован.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§3 delete sets status archived, cleanup moves the file; §11 the indexes are written by guppi index and checked by lint; §1 log.md and History are written by generate and cleanup; §9 Work Mode is deferred to Slice 3b"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "no deleted status; the Retro, Handoff and Documentation rows point at rule-end-of-work and rule-documentation; Lesson row: error is born passed"
  - slug: claude-md
    file: CLAUDE.md
    change: "Migration mode: /retro, /handoff and the librarian exist since Slice 3, the gate before /handoff too; the brief is written by the librarian; pages are no longer written by hand"
  - slug: rule-session-start
    set: {children: [rule-skill-hi, rule-event-log, rule-ledger-write]}
    change: rule-hook-registry moves under rule-harness
    replace:
      - old: "The hook registry (4) comes last because it records the registration of children 2–3; it is not a step of the session."
        new: "The hook registry that records the registration of children 2–3 is not a step of the session; it lives under `rule-harness` with the other tools."
```

## Case 40 — находки pre-task

> **context:**
> Cases 31.1, 32, 33, 34 поменяли модель в четырёх местах. Несколько документов говорят по-старому.

> **problem:**
> Следующая сессия увидит две модели.

> **recommend:**
> Шесть `update` словами. Уточнение к 38.1: Retro заканчивается коммитом, потом `/handoff`.

> **given:**
> §2 «Six sections», §3 «Put the result in `now`», `estimate-plan-mode-verified` «in the Case's `now`».
> **＋** §5 и `decisions/schema.md` «never inferred from a slug prefix». §5, §11, glossary, `entities/schema.md`: страница на решение, meaningful slug.
> **＋** §8 «archived immediately». `rules/schema.md`: «its children use `partial`».
> **＋** §9 «Retro → commit → handoff».

> **when:**
> Агент читает эти файлы в следующей сессии.

> **then:**
> §2, §3: семь секций, результат pre-task в `given`. `estimate-plan-mode-verified`: «in the Case's `given`».
> **＋** §5, `decisions/schema.md`: категория явная на странице, скрипт выводит её из префикса, который проверяет pre-task.
> **＋** §5, §11, glossary, `entities/schema.md`: одна Decision-страница на Case, `decision-case-<N>`.
> **＋** §8, glossary: Estimate error-урока `passed`, не `archived`.
> **＋** `rules/schema.md`: ребёнок render-MOC без Render — шаг, который рамка вызывает по имени.
> **＋** `rule-retro`: коммит по одобрению, потом `/handoff`.
> **－** Смысл решений не меняется.

> **ratification:** ратифицирован.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§2 seven sections; §3 the pre-task result goes in given; §5 one Decision page per Case, category explicit on the page and derived from the slug prefix by the script; §8 an error lesson's Estimate is born passed; §11 Decision slugs are decision-case-<N>, grep goes by [case N]"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "Routing Table row: one page per Case, decision-case-<N>; Lesson row: born passed"
  - slug: decisions-schema
    file: vault/wiki/decisions/schema.md
    change: "the category of a target is explicit on the page and derived from the slug prefix by the script"
  - slug: entities-schema
    file: vault/wiki/entities/schema.md
    change: "Slug: the decision that created a page is decision-case-<N>, reachable through origin"
  - slug: rules-schema
    file: vault/wiki/rules/schema.md
    change: "MOCs and enforcement: a child without a Render is a step the frame calls by name and contributes nothing to the file"
  - slug: estimate-plan-mode-verified
    change: "criterion names the Case's given, not now"
    replace:
      - old: "is flagged in the Case's `now` before ratification"
        new: "is flagged in the Case's `given` before ratification"
  - slug: rule-retro
    change: "Retro ends with the commit, then /handoff (the Render of case 38.1 already carries it)"
```

## Case 41 — `materialize` дополняет yaml

> **context:**
> Один ledger материализуется в два приёма.

> **problem:**
> Отказ теряет поздние строки и ломает второй запуск.

> **recommend:**
> Существующий yaml дополняется. Три правила защиты.

> **given:**
> Case 31: «yaml уже есть — exit 1».
> **＋** Каждая запись несёт `line`. `generate` помечает `applied`.
> **－** В этой сессии скрипты бегут по сегодняшнему ledger дважды.

> **when:**
> `uv run guppi materialize` при существующем `materialize.yaml`.

> **then:**
> Записи с известным `line` остаются как были.
> **＋** Новые строки ledger — новые записи в конце.
> **＋** Текст по номеру не совпал — флаг, запись не трогается.
> **＋** Поздний `supersedes` дописывает ранней записи `superseded_by`. Больше ничего.
> **＋** `estimate`-строка для `create` с `applied` — своя запись `estimate`.
> **＋** Stdout: сколько добавлено. Exit 0.
> **－** Критерий `estimate-materialize-assembles` меняется в этой части.

> **ratification:** ратифицирован.

```then
update:
  - slug: rule-materialize
    change: "an existing yaml is extended with the ledger lines it does not hold, never rewritten (the How it works of case 31 already carries it)"
  - slug: estimate-materialize-assembles
    change: "criterion: an existing yaml gains only the entries of ledger lines it does not hold (the Criterion of case 31 already carries it)"
```

## Порядок работы

Тесты первыми, по модулю; после каждого шага `make style` и `make test`. Страницы этого
слайса пишет `guppi generate` из этого Spec — это его живое чтение. До него страниц слайса
нет; Rule-class файлы правятся руками.

1. `tests/test_materialize.py` → `guppi/materialize.py` (разбор строк из `guppi/ledger.py`,
   заголовки Spec, блоки `then`, маршрут §5, `exists`, `incomplete`, `unparsed`, дополнение
   существующего yaml). Команда в `guppi/cli.py`.
2. `tests/test_generate.py` → `guppi/generate.py` (страницы, backlinks, History, `log.md`,
   `tags.md`, Decision-страницы, уроки с парным Estimate, каскад `built`, `severity`,
   `replace`, `applied`, коллизии). Чтение через `guppi/pages.py`.
3. `tests/test_cleanup.py` → `guppi/cleanup.py` (перенос, восстановление, списки
   `children`/`estimates`, индексы через `guppi/index.py`). `guppi/lint.py`: `archived_slugs`
   читает `vault/archived/`.
4. `tests/test_gate.py` → `guppi/gate.py`.
5. `tests/test_render.py`: ребёнок без Render (36.2) → `guppi/render.py`.
6. `Makefile`: `test-documentation`, `test-harness`, `test-end-of-work`; `help` без изменений
   формы.
7. Rule-class файлы руками: `case-schema.md`, `index.md` (§1, §2, §3, §4, §5, §8, §9, §11),
   `glossary.md`, `decisions/schema.md` + `schema.yaml`, `lessons/schema.md`,
   `insights/schema.md`, `entities/schema.md`, `rules/schema.md`, `CLAUDE.md` (блок
   Migration mode), `sprint.md` (Slice 3b).
8. `uv run guppi materialize` по сегодняшнему ledger → проверить yaml (`incomplete`,
   `unparsed`) → `uv run guppi generate` → страницы слайса, `update` существующих,
   Decision-страницы 29–41, placeholder'ы 29, уроки сегодняшней сессии. Ошибки — править
   Spec-блок или скрипт, повторный запуск по `applied`.
9. `uv run guppi render` → `.claude/agents/librarian-guppi.md`, `.claude/skills/retro/`,
   `.claude/skills/handoff/`, `.claude/settings.json`, блок в `CLAUDE.md`. `uv run guppi
   index`. `make lint`.
10. Backfill: `uv run guppi materialize --date 2026-09-09` → `guppi generate` → Decision-
    страницы 1–27, уроки 2026-09-09 и их Estimates. `guppi index`, `make lint`. Чтения
    `estimate-materialize-assembles`, `estimate-generate-writes`.
11. Чтения по рукам, каждое строкой `estimate[...]` в LEDGER-блоке того ответа:
    `cleanup-moves` (пустой прогон), `render-harness-reproduces` (36.2), `harness-pipeline`,
    pipeline-части `documentation-completes` и `end-of-work-order`, `retro-commit-gates`
    (тесты), `pretask-reconciles` (этот Plan Mode), `pretask-hook-gates` и
    `spec-capture-appends` (это одобрение).
12. `/retro` в этой сессии (skill виден сразу): чтение `retro-loads`. Коммит. `/handoff`
    из Retro: чтения `retro-commit-gates` (live) и `handoff-dispatches` в той части, что
    возможна: агент `librarian-guppi` виден только со следующей сессии, диспатч упадёт —
    записать как есть. Brief и `sprint.md` — руками в последний раз.

## Проверка

- `make style`, `make test` — чисто и зелено.
- `make test-documentation`, `make test-harness`, `make test-end-of-work` — зелёные.
- `uv run guppi render --check`, `uv run guppi index --check` — exit 0.
- `uv run guppi lint` — только известное ложное (ниже).
- `git diff --stat` после `generate` и `render`: только ожидаемые файлы.
- `raw/2026-09-10/materialize.yaml` и `raw/2026-09-09/materialize.yaml` существуют, без
  `unparsed`.

## Отложено и известное ложное — в brief

- Живые чтения librarian'а — следующая сессия: `documentation-completes`,
  `index-check-merges`, `synthesis-clusters`, `brief-written`, `close-commits`,
  `handoff-dispatches` (часть с агентом).
- Work Mode и `subagent-guppi` — Slice 3b (Case 29). Два placeholder'а красные у lint
  (без `kind`, `estimates`) до Slice 3b или Slice 5.
- `status: draft` при всех Estimates `passed` — генератор ставит `built` каскадом; что
  останется после шага 8, уходит в brief.
- Уроки `knowledge` 2026-09-09 без `source` — lint назовёт; их Research Estimates `pending`.
- Архив в `ask-guppi` (названный slug проверять по `vault/archived/`) — обсуждается, когда
  дойдём до архива.
- `docs/migration/rule-*.md`, `vault/parked/`, `vault/archive/`, `docs/superpowers/`,
  `docs/HANDOFF.md`, `/grill-me` без страницы, `origin` без upstream, `gh` — Slice 5.
- `raw/2026-09-09/ledger.md`: смешанные line endings, git нормализует.
