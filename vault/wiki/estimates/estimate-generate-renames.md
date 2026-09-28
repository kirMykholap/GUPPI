---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: An update with rename moves the page to its new slug and rewrites every link to it in the live pages, History and Result untouched
method: pytest in tests/test_generate.py against a temp vault; the live reading once by hand, the librarian's run on a real rename
checked: 2026-09-20
origin: raw/2026-09-20/0527/ledger.md#case-258.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, tests]
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

2026-09-20, the librarian's run on Case 261 (commit 0666763): five pages moved to the prespec slugs, none old; children of rule-plan-mode, estimates of both rules, target of the three Estimates and every wikilink in live pages (32 Decision pages) retargeted, zero old links in wiki/; origin, earlier History and Result keep the old; History renamed from and ref old → new under decision-case-261; deferred_by of 259 cleared by the supersedes, 259 archived; pytest 434 green at 738e3ef

## History

- 2026-09-20 created · [[decision-case-258.1]]
- 2026-09-20 updated: the two placeholders `[[decision-case-N]]` of the Criterion in code spans, so lint reads no link; the text of 258.1 otherwise (case 262) · [[decision-case-262]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0740/ledger.md#L17
- 2026-09-20 updated: the History line of 262 quoted by hand — its placeholder `[[decision-case-N]]` in a code span — a one-off migration; the Criterion the text of 262; the status the one the reading of 09:38:37 in raw/2026-09-20/0740 leaves (case 264.1) · [[decision-case-264.1]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the line on guppi sprint out (case 489.3) · [[decision-case-489.3]]
