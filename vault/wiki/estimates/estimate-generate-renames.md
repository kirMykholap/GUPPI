---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: An update with rename moves the page to its new slug and rewrites every link to it in the live pages, History and Result untouched
method: pytest in tests/test_generate.py against a temp vault; the live reading once by hand, the librarian's run on a real rename
origin: raw/2026-09-20/0527/ledger.md#case-258.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, tests]
---

## Criterion

Given:
An `update` item may carry `rename: <new slug>` beside `set`, `sections`, `replace`, `change`; the ledger line names the old slug.
**＋** The id of a page is its filename; the new slug carries the same category prefix.
**＋** `origin` is never rewritten; the archive, `raw/`, `log.md` and `brief.md` are not pages.
**－** A taken slug — live or archived — and a foreign prefix: an error on a `create`, the same on a `rename`.

When:
`guppi generate` applies an `update` whose item carries `rename`.

Then:
The file `wiki/<category>/<old>.md` becomes `<new>.md`; the page's History gets "renamed from `<old>` · [[decision-case-N]]"; the item's `set`, `sections` and `replace` apply to the new file.
**＋** In every live page of `wiki/` — Decision pages included — every `[[old]]` becomes `[[new]]`, every `REF_FIELDS` value holding the old slug becomes the new one, and the old slug as a whole word in the body outside `## History` and `## Result` becomes the new one; every page touched, Decision pages excepted, gets the History line "ref `<old>` → `<new>` · [[decision-case-N]]".
**＋** The Decision page of the Case is written as today — by the slug of the ledger line, before the entries; the walk retargets its link like any other.
**＋** The order of application is the order of the yaml: an `update` of the same page from an earlier Case lands on the old file, and the `rename` moves it with the page.
**－** A taken slug or a foreign prefix: the entry is `failed`, nothing is moved.
**－** `origin`, `## History` and `## Result` of any page, the archive, `raw/`, `log.md` and `brief.md` are untouched; `guppi sprint` redraws `sprint.md` from the sprint page.

## History

- 2026-09-20 created · [[decision-case-258.1]]
