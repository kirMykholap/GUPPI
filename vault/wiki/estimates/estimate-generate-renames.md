---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: An update with rename moves the page to its new slug and rewrites every link to it in the live pages, History and Result untouched
method: pytest in .guppi/tests/test_generate.py against a temp vault; the live reading once by hand, the librarian's run on a real rename
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, tests]
core: true
---

## Criterion

When:
`guppi generate` applies an `update` entry whose item carries `rename: <new slug>`, beside `set`, `sections`, `replace` or `change`, and the ledger line names the old slug.

Then:
The file of the page moves from `<old>.md` to `<new>.md` in its category folder, and the new slug carries the same category prefix. The page's History gets "renamed from `<old>` · `[[decision-case-N]]`", and the item's `set`, `sections` and `replace` apply to the new file.
**＋** In every live page of `vault/wiki/`, Decision pages included, every `[[old]]` becomes `[[new]]`, every `REF_FIELDS` value holding the old slug becomes the new one, and the old slug as a whole word in the body outside `## History` and `## Result` becomes the new one. Every page touched, Decision pages excepted, gets the History line "ref `<old>` → `<new>` · `[[decision-case-N]]`".
**＋** The Decision page of the Case is written by the slug of the ledger line, before the entries, and the walk retargets its link like any other.
**＋** The order of application is the order of the yaml: an `update` of the same page from an earlier Case lands on the old file, and the `rename` moves it with the page.
**－** A taken slug, live or archived, or a foreign prefix: the entry is `failed`, and nothing is moved.
**－** `origin`, `## History` and `## Result` of any page, `vault/archive/`, `vault/raw/`, `log.md` and `brief.md` are untouched.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
