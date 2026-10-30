# Handoff — 2026-10-30, the items of the brief of 1713 and the install by hand into five projects

## Notes from memory

- Before the installs the person asked how `/plugin marketplace add` works and whether a real user sees the local path. The answer: a real user adds the catalogue from the branch `prod` of the GitHub repository; the exact form of a git URL with a branch was given from memory and not checked, and `README.md` has no install steps yet.
- The person first typed `/guppi:install` in `C:\tmp\guppi-2005` itself, the folder that holds the five projects. It wrote GUPPI there, and the `/hi` after it ran `git init -b main` there. The person later cleared that folder, the record of what each project held before the install with it. The first `/hi` of `p1-empty` showed `Branch: main` and untracked files of the parent folder, since `p1-empty` stood inside that repository then; this is no defect of the install.
- The reading of `estimate-synthesis-clusters` counts three `sed -n 4p` reads of lesson pages as output of the Grep: the Grep printed those three index lines as `[Omitted long matching line]`, and the librarian printed the same line 4, `root_cause`, to see them. The Criterion does not say whether such a read is an opening that the report must name.
- The reading of `estimate-orchestration-states-a-subagent-fact-from-its-transcript` passed on the `－` line alone: no reply of session 1713 states a subagent's call as the main agent's own, so its `＋` lines were not exercised.
- Case 943 replaced Case 941 and Case 942 replaced Case 940 after `/pre-spec`; each was built again under a new number because its decision lines already stood.

## Direct instructions to the librarian

- The lines of Cases 940 and 941 are superseded by Cases 942 and 943; apply only the entries of the superseding Cases.
- `rule-orchestration` takes two updates, Case 937.2 under `## Plan Mode and the Frontier` and Case 938 under `## Who builds a Case`; they change different sentences.
- Case 942.1 drops `## How it works` from eleven Leaf pages and gives `rule-internal-context` a new `## Purpose`; Case 942.2 rewords `rule-rules-schema`, whose render writes `vault/wiki/rules/schema.yaml`. Check after `generate` that no Leaf page under `vault/wiki/rules/` still holds the section and that no `drop` item failed.
- The readings of `estimate-synthesis-clusters`, `estimate-orchestration-states-a-subagent-fact-from-its-transcript` and `estimate-case-build-reads-the-readers-of-a-changed-step` tick `read` boxes in `vault/raw/2026-10-30/0304/spec.md`; the reading of `estimate-case-build-reads-the-code-it-states` ticks its box in the Spec of the session that made that Case.

## What actually got done

- Cases ratified: 936 (a defer), 937 (937.1, 937.2, 937.3), 938, 939, 942 (942.1, 942.2), 943 (943.1, 943.2, 943.3).
- Code: `.guppi/guppi/generate.py` (`title_slugs`, called by `frontier_marks`), `.guppi/guppi/prespec.py` (`decided_on_its_page` with `by_defer`, `check_backlog_defer_line`, `deferred_pages` on `title_slugs`), `.guppi/guppi/casecheck.py` (`check_backlog` with `by_defer`); the module docstrings of `.guppi/tests/conftest.py`, `ratified.py`, `recall.py`, `event.py`, `gate.py`, `archive.py`, `gitstate.py`, `tail.py`, `pageread.py` and `guard.py` took the facts of the `## How it works` of their pages.
- Tests: `.guppi/tests/test_prespec.py` (five new tests, one narrowed to the source `sprint`), `.guppi/tests/test_casecheck.py` (the backlog test now asks for the mark on a `defer`).
- `uv run --project .guppi guppi test`: 1819 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- In Work Mode the agent wrote the clean copy by `guppi ship --allow-draft` into `C:\tmp\guppi-2005\copy` and made five test projects; at the `stop:` task the person installed into them and answered A1.
- Readings: L1 at `/hi`; L45–L55 at the end of Retro, ten `passed` and one `failed` (`estimate-case-build-reads-the-readers-of-a-changed-step`). Lesson: L56.

## Debt

- No box of code, test or command is left unticked, and no test was reverted.
- 40 boxes of the Spec wait for the librarian.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — the first dispatch of `case-guppi` under the new Render of `rule-orchestration` in which a Case of the session sets the form of a text a check reads and the Case of the item may write text of that kind.
- `estimate-rules-schema-leaf-carries-no-how-it-works` — the librarian's run of this session.
- `estimate-rules-schema-checked` — the librarian's run of this session.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — an install of a project with its own `CLAUDE.md`, `.claude/settings.json` and `.gitattributes`, Claude Code started with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder; the project of this session was installed online (L56), so the line on putting the set-aside files back after a failed `uv sync` was not seen.

## Observations

- `uv run --project .guppi guppi check` was red before the work: 13 lines, each a page with `core: true` that stands `draft` (`## Baseline` of `work.md`).
- In the three projects of `estimate-plugin-install-sets-aside-the-files-of-the-project` that ran (own files online, own files "offline" that ran online, own vault), the install set aside `CLAUDE.md`, `.gitattributes` and, after `uv sync`, `.claude/settings.json` unchanged, listed them in its last message, and left `vault/notes.md` in place. No project of its method holds a file of the install at another path or a `guppi-set-aside/`, so the `－` line on stopping at such a clash is read by no project its method names.
- Moving the facts of `## How it works` into the docstrings, the subagent found two of them false for today's code and moved neither: "subagents inherit no project hook" in `rule-governed-files-hook`, and the condition under which the parent is removed in `rule-spec-write`. Both sections leave with Case 942.1.
- The `/plugin marketplace add` form for a GitHub repository at the branch `prod` was not checked against the Claude Code documentation.

## For the next session

- The failed reading of `estimate-case-build-reads-the-readers-of-a-changed-step`: at the `/pre-spec` of session 1713, Case 931 added `drop` to the update items and missed two texts that list those keys.
- The finding of `/pre-spec` the person left: a backlog line closed `defer case N` by a Case of a conserved Spec in a session of `/box` is a finding of `guppi prespec --check`, before Case 937 and after it, since such a Case has no decision line in the session's window.
- The two facts of the dropped `## How it works` sections that today's code does not bear out: which text is right, and whether a docstring or a page should say it.
- The install steps that the agent gives at a stop: each project's start command written out whole, the offline variables included.

## Ask the person

- `estimate-close-reports-the-run` — needs the person — Did the report that `/handoff` showed after the librarian's run of 2026-10-30 give each part the Criterion names — the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags, the lint total and each part another step of the frame sends to the report — and no test result and no list of files?
