---
type: decision
case: "21"
status: current
kind: [create, create]
target_slug: [rule-lint, estimate-lint-catches]
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## When

```
create:
  slug: rule-lint
  type: rule
  kind: Leaf
  purpose: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
  enforcement: check
  implementation_ref: [guppi/lint.py, tests/test_lint.py, Makefile]
  parent: rule-documentation
  tags: [harness, workflow]
  estimate:
    slug: estimate-lint-catches
    kind: QA
    criterion: against a temp vault seeded with one page per defect class, `guppi lint` names each defective page with the class and nothing else, exits 1, and exits 0 with no output on a clean vault; the two Method classes (26.2) are seeded too. Against the live vault — the first run's findings are each either an item of the brief's known-false list or become a Case
    method: pytest in tests/test_lint.py, one test per defect class; the live reading once by hand
update:
  slug: estimate-session-start-context
  change: Method → "`make test-session-start`, the pipeline over tests/test_event.py and tests/test_ledger.py; the two end-to-end readings by hand"
```

Классы дефектов `guppi lint` (читает `vault/wiki/<category>/`, архив исключён; печатает
`<category>/<slug>: <what>`, exit 1 при любой находке; ничего не пишет):

1. schema: отсутствует обязательное поле или секция; значение вне `values`; не выполнен
   `conditional`.
2. schema-prose: `schema.md` называет поле или секцию, которых нет в `schema.yaml`, или
   наоборот.
3. ref: slug в `parent`, `children`, `estimates`, `target`, `addressed_by` или `[[slug]]`
   в теле, которого нет ни среди живых, ни среди архивных страниц.
4. origin: файл ledger или строка `[case N]` не существуют.
5. path: путь в `implementation_ref` или `governs` не существует.
6. orphan: живая страница, которую не называет frontmatter ни одной другой живой
   страницы; MOC без `parent` считается названным через детей и Estimates.
7. status: `built` при Estimate не `passed`; `passed`/`failed` без `## Result`; Estimate,
   чей `target` не перечисляет её; `draft` при всех Estimates `passed` (сообщает, не
   ставит — `built` ставит генератор слайса 3).
8. method (26.2): у Estimate с Leaf-целью `## Method` называет существующий путь `tests/…`
   или содержит «by hand»; у Estimate с MOC-целью — `make <target>`, и цель есть в
   `Makefile`.

`Makefile`: `lint` = `guppi render --check` + `guppi index --check` + `guppi lint`;
`test-session-start` = `pytest tests/test_event.py tests/test_ledger.py`;
`test-plan-mode` = `pytest tests/test_spec.py tests/test_pretask.py`. Заголовок Makefile
(«ни одна цель не пишет в дерево») остаётся верным.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-21
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
