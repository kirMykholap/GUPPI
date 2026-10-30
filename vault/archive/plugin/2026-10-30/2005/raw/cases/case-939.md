## Case 939 — The reading of the clean pages passes --allow-draft

> **context:**
> `estimate-clean-branch-pages-hold-pointers-only-in-brackets` checks that the pages with `core: true`, the `schema.yaml` of each category and the files of `.claude/` that such pages render hold each pointer to a case in a bracket of its own. Its `method` and the `When` of its Criterion build the clean copy by `uv run --project .guppi guppi ship --review` into an empty folder. In `run` of `.guppi/guppi/ship.py`, a build into a folder first calls `drafts`, which lists each page that `is_draft_core` accepts. When that list is not empty and `--allow-draft` is not passed, `run` prints the list and returns 1 before it calls `version` or `ship`. With `--allow-draft` it prints the list, which sets no exit code, then calls `version`, which returns 1 with nothing written when no tag `prod-x.y.z` stands in the history of HEAD, and then `ship`, which writes the copy and gives the lines. I read `run`, `drafts`, `version`, `ship`, `settled`, `judged` and `check` of `.guppi/guppi/ship.py` whole for these claims. The brief reports the last `guppi check` (`## Flags` of `vault/wiki/brief.md`): "13 lines, exit 1 — 13 pages with `core: true` stand `draft`". It also reports that `git tag --merged HEAD` prints `prod-0.2.0`. So the reading as written gives the draft list and no line on the brackets. Case 928 fixed the same gap in the Estimate of the code by `--check`, which judges no file under `vault/`, and left this Estimate as it stood; the handoff of session 1713 carried it on.
>
> The person chose to pass `--allow-draft` in the `When` and the `method`, and to read at Retro of this session. The rule that governs the change is the form of a promise in `case-schema.md`: a part inside a Criterion is refused, and a promise changes only by a Criterion replaced whole. So the Case replaces the Criterion whole and sets the Estimate `pending`. The new `When` names the flag, the tag and Retro. The old `When` line is not carried, since the command it names writes nothing while a draft page with `core: true` stands. The `Then` lines stand as they were, and one new `－` line says that the lines on draft pages set no exit code and are no part of this promise. The new `method` names the flag and holds no pointer, since the copy takes this Estimate once it is `passed`. The `purpose` speaks of what `guppi ship --review` prints and of the brackets it removes, which the new command still does, so it stands.
>
> `rule-clean-branch` gives `--allow-draft` one purpose: it writes the copy for an install by hand from that folder, which is where a check that needs an install reads it. A finding of `/pre-spec` named that sentence, and the person chose that this Case replaces it so that it names both uses: the install by hand and the reading of the pages by `--review`. The pair adds no behaviour of the code. `estimate-clean-branch-refuses-a-draft-core-page`, an Estimate of `rule-clean-branch`, already checks what the flag does: its Criterion says that with `--allow-draft` the build writes the copy and prints the draft lines, which set no exit code. Its Criterion names no purpose of the flag, so it stands. A Grep of `allow-draft` over `vault/wiki/estimates/` with the glob `estimate-clean-branch-*.md` printed `estimate-clean-branch-ships-neutral-texts.md`, `estimate-clean-branch-installs-as-a-plugin.md`, `estimate-clean-branch-writes-the-session-files.md`, `estimate-clean-branch-refuses-a-draft-core-page.md` and `estimate-clean-branch-ships-the-tests.md`. The methods of `estimate-clean-branch-ships-neutral-texts` and `estimate-clean-branch-ships-the-tests` also pass the flag for a reading with no install. By the person's answer, the new sentence names the two uses the finding named, so these other readings are not named in it. A Grep of `install by hand` over `.guppi/`, `.claude/`, `.github/` and `plugin/` printed `.guppi/guppi/ship.py`: line 26 of its module docstring and line 631, the help of `--allow-draft`. Both name the install, and neither says that the flag serves only that. This Case changes no code, so both stand. A Grep of `ship --review` over `vault/wiki/` printed `vault/wiki/brief.md`, `vault/wiki/rules/rule-clean-branch.md`, `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`, `vault/wiki/estimates/estimate-clean-branch-refuses-a-draft-core-page.md` and `vault/wiki/estimates/estimate-clean-branch-pages-hold-pointers-only-in-brackets.md`; over `.claude/` it printed nothing. The two other Estimates set what the folder build does, and this Case changes no code, so they stand; the rule's hits say what `--review` lists, which stays true; the `brief.md` hit is not read. A Grep of `pages-hold-pointers-only-in-brackets` over `.guppi/tests/` printed nothing, so no test reads this page live. I read the finished files of Cases 937, 942 and 943 of this session whole. Case 943 writes a clean copy by `guppi ship --allow-draft` in Work Mode for the install by hand, which is the first use of the new sentence, into a folder of its own, so it shares no folder with this reading. Case 942 changes docstrings under `.guppi/guppi/`, which are outside this promise. It drops a section from core pages, and Case 937 changes core pages, but both changes land at the librarian's run, after Retro, so this reading at Retro judges the pages before those changes. None of them changes `rule-clean-branch` or this Estimate, so this Case needs no change against them. The ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> The reading of the pages that ship, as its `method` and its Criterion write it, exits 1 and writes nothing while any page with `core: true` stands `draft`.

> **recommend:**
> - **How the reading of the pages runs while a core page stands draft**
>   - Recommended: (a) add `--allow-draft` and replace the Criterion whole.
>   - Answer: agreed, (a).
> - **When the new reading is taken**
>   - Recommended: (a) at Retro of this session.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`, which the person agreed to: the sentence of `rule-clean-branch` that gives `--allow-draft` the install by hand as its one use should name both uses, the install by hand and the reading of the pages by `--review`.
>   - Taken: an `update` of `rule-clean-branch` replaces that sentence, and `estimate-clean-branch-refuses-a-draft-core-page` is named as the check of the flag.

> **given:**
> `estimate-clean-branch-pages-hold-pointers-only-in-brackets`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship`, whose `--allow-draft` and `--review` the reading runs.
> **＋** `vault/wiki/` and `.claude/`: the pages and the harness files the reading judges.
> **＋** `rule-clean-branch`: sets the clean version and the option `--allow-draft`; its sentence on the uses of that option is replaced.
> **＋** `estimate-clean-branch-refuses-a-draft-core-page`: checks what `--allow-draft` does.
> **＋** `rule-retro`: sets Retro.

> **when:**
> At Retro of the session, `uv run --project .guppi guppi ship --allow-draft --review <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder, with a tag `prod-x.y.z` in the history of HEAD.

> **then:**
> It prints no line on a pointer outside a bracket of its own in a page under `vault/wiki/` with `core: true`, in the `schema.yaml` of a category or in a file of `.claude/` that such a page renders.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as the history of this repository that a pointer names, when a thing was measured or which session a pointer names.
> **＋** No bracket that `--review` lists on those files holds the definition of a term that its sentence needs, or the slug of a page with `core: true` by which its sentence names the rule that sets what it says.
> **－** Each page under `vault/wiki/` keeps every pointer it held, with the words that go with it, in a bracket, and each sentence keeps its meaning in this repository.
> **－** A line on a page with `core: true` that stands `draft` sets no exit code and is no part of this promise.
> **－** A line on a file under `.guppi/guppi/` is no part of this promise.

> **tasks:**
> - [ ] update `estimate-clean-branch-pages-hold-pointers-only-in-brackets`
>   - set: `{status: pending, method: "by hand, at Retro: the lines of uv run --project .guppi guppi ship --allow-draft --review into an empty temporary folder on vault/wiki/ and .claude/, read against the Criterion"}`
>   - change: `the Criterion replaced whole — the reading passes --allow-draft, so no draft page with core: true stops it`
> - [ ] update `rule-clean-branch`
>   - old: `for an install by hand from that folder, which is where a check that needs an install reads it, and the workflow never passes that option`
>   - new: `` for an install by hand from that folder, which is where a check that needs an install reads it, and for the reading of the pages that the clean version holds by `--review`, and the workflow never passes that option ``
>   - change: `--allow-draft also serves the reading of the pages by --review`
> - [ ] read `estimate-clean-branch-pages-hold-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 939][update][estimate-clean-branch-pages-hold-pointers-only-in-brackets]{ref:rule-clean-branch}
> - decision[case 939][update][rule-clean-branch]{ref:rule-clean-branch}
> ```
