---
type: decision
case: "18.1"
status: current
targets:
  - {kind: create, category: rules, slug: rule-render-harness, ref: rule-documentation}
  - {kind: create, category: estimates, slug: estimate-render-harness-reproduces, ref: rule-render-harness}
origin: raw/2026-09-09/ledger.md#case-18.1
sprint: migration
created: 2026-09-09
tags: [harness, render]
---

## Then

`uv run guppi render` пишет; `uv run guppi render --check` сравнивает, exit 1, не пишет.
Маркеры: `partial` оставляет их в файле, `full` пишет тело без внешних маркеров.
`SKILL.md` теряет две строки комментариев. Новый тег `render`.

```
create:
  slug: rule-render-harness
  type: rule
  kind: Leaf
  purpose: Prevents a Rule page and the harness file it governs from becoming two copies of one text
  enforcement: check
  implementation_ref: [guppi/render.py, tests/test_render.py]
  parent: rule-documentation        # dangles until Slice 3, like rule-plan-mode did
  tags: [harness, render]
  estimate:
    slug: estimate-render-harness-reproduces
    kind: QA
    criterion: against a temp vault — a full MOC with two partial children renders to the MOC's Render text with each child marker replaced by the child's block, in child order, outer markers dropped; a partial page splices between its markers in an existing file and leaves the markers; a partial target without markers exits 1 with nothing written; --check on a differing file exits 1, names it, writes nothing, and exits 0 on an identical one. Against the live vault — after `uv run guppi render`, `git diff --stat` shows only the two dropped marker lines of .claude/skills/hi/SKILL.md and no change to CLAUDE.md; `guppi render --check` then exits 0
    method: pytest in tests/test_render.py against a temp vault; the live reading once by hand
```

Семантика `guppi render`: обходит `vault/wiki/rules/`, берёт страницы с
`enforcement: render` и текст `## Render` между собственными маркерами. `full` пишет этот
текст как весь файл `governs`, без внешних маркеров; одиночная строка `<!-- child -->`
в нём заменяется Render-текстом ребёнка вместе с его маркерами, в порядке `children`,
блоки детей разделены одной пустой строкой. `partial`, чью цель не держит ни одна
`full`-страница, вклеивается в существующий файл между его маркерами, маркеры остаются.
Ошибки — на stderr, exit 1, ничего не записано: `partial` без маркеров в цели; `full`
называет ребёнка, который не render-страница; две `full` на один файл.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.1
