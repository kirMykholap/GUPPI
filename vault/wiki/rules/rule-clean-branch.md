---
type: rule
kind: Leaf
purpose: Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install
status: built
enforcement: check
implementation_ref: [guppi/ship.py, tests/test_ship.py, .github/workflows/prod.yml]
estimates: ["[[estimate-clean-branch-writes-a-clean-copy]]", "[[estimate-clean-branch-code-holds-pointers-only-in-brackets]]", "[[estimate-clean-branch-pages-hold-pointers-only-in-brackets]]"]
applies_to: ["[[entity-guppi-repository]]"]
origin: raw/2026-10-13/1753/ledger.md#case-804.6
sprint: plugin
created: 2026-10-13
tags: [ci, git, plugin]
---

## Purpose

Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install. `guppi ship` builds that version from the working tree into an empty folder: `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page with `core: true` and each file rendered from such a page, but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project. It gives each page `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line, and keeps in its link fields only the pages it writes.

A pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — stands in this repository in a bracket of its own at the end of its sentence, together with the words that go with it, such as `(as set in case 12)` or `(measured 2026-09-25, session 0051)`, so that the sentence reads whole without it. `guppi ship` removes each bracket that holds a pointer whole, every word in it included, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays. A case number with no word `case` or `cases` before it, such as `(274.1)`, is no form of a pointer, and `guppi ship` does not remove it; in a comment or a docstring of a Python file it exits 1 on each bracket that holds only case numbers, on each comment or docstring that opens with one or more case numbers, joined as in such a bracket, followed by a colon, and on each comment whose whole text is one or more case numbers joined the same way, and it judges no code outside them. It writes any other `[[…]]` link to a page or a file it does not write as the slug in a code span. A case id in a code span or a fenced block, of a Markdown file or of the text of a `schema.yaml`, or in the form of a line after `[case `, `#case-` or `:case `, is no pointer; the example Case of `case-example.md` and of the Render of `rule-case-example` stands in a fenced block, and the text around it is judged and cleaned like the text of any other page. It exits 1 on each pointer that stands outside such a bracket, and on each section of a page without `core: true`; a Case rewords that text at its source. `guppi ship --review` also lists each bracket it removes that holds words beside its pointer, so that a word the sentence needs is found and moved out of the bracket. `guppi ship --check` judges in place each file outside `vault/` that the clean version holds — the code, the harness and the files at the root of the project — and `make lint` runs it; `/pre-spec` finds a pointer outside such a bracket in the new text of a page with `core: true` before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run (case 807).

The workflow `.github/workflows/prod.yml` runs it on each push to `main`, and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch. It writes the result to the branch `prod` as one new commit on top of the last, whose message names the commit it was built from, and writes none when nothing changed or when the command exits 1. It pushes with a deploy key of this repository with write access, whose private half is the repository secret `PROD_DEPLOY_KEY`; deploy keys stand on the bypass list of the ruleset on `prod` that [[rule-github-repository]] sets. This rule and the workflow belong to this repository: neither carries `core`, and `.github/` is not part of the clean version (case 804).

## History

- 2026-10-13 created · [[decision-case-804.6]]
- 2026-10-13 estimate estimate-clean-branch-writes-a-clean-copy added · [[decision-case-804.6]]
- 2026-10-13 status: draft → built · cascade
- 2026-10-14 updated: a pointer stands in a bracket of its own, which guppi ship removes whole; a link to a page left out becomes its slug; --review and --check (case 807.1) · [[decision-case-807.1]]
- 2026-10-14 estimate estimate-clean-branch-code-holds-pointers-only-in-brackets added · [[decision-case-807.3]]
- 2026-10-14 updated: a case number stands with its word; guppi ship reports a bare one in a comment or a docstring of the code · [[decision-case-808.1]]
- 2026-10-14 estimate estimate-clean-branch-pages-hold-pointers-only-in-brackets added · [[decision-case-809]]
- 2026-10-14 status: built → draft · cascade
- 2026-10-14 updated: guppi ship reports a list of bare case numbers at the opening of a comment or a docstring, or alone in a comment · [[decision-case-811]]
- 2026-10-14 status: draft → built · cascade
- 2026-10-14 updated: guppi ship judges and cleans the text around the example Case; only its fenced blocks are set aside · [[decision-case-815]]
