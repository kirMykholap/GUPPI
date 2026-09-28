## Case 460 — A lesson slug carries its prefix: the page renamed, the ledger hook refusing a slug without it, one table of prefixes

> **context:**
> A lesson reaches the vault straight from its ledger line. The ledger hook writes any `lesson[...]` line from a `LEDGER` block. `lesson_entry` in `guppi/materialize.py` sends the line to the lessons folder because it is a lesson record, not because of its slug. `generate` then writes the page under the slug as written. Lint checks that `type` matches the folder and that the `slug` matches the filename, but it never checks the prefix. So ledger line 54 of session 1255 put `harness-senduserfile-renders-a-markdown-file-on-the-phone` into the vault without its `lesson-` prefix, and nothing reported it. A Glob over the six category folders finds no other live page without its category prefix.
> The prefix table is kept twice. `category_of` in `guppi/materialize.py` reads six prefixes, and `generate` imports that table. `guppi/lint.py` keeps its own copy of five prefixes, without `decision-`, for `check_decision` alone. So a `decision-` slug in a Decision list is a page for `materialize`, but lint does not look it up. `CLAUDE.md` calls a second copy of one judgment a defect. The deferred `decision-case-455` covers a different pair of functions.
> The lesson is `new`, and no live page links to it. `brief.md` and `log.md` name it, but they are records. The rules of the lessons schema say a lesson goes through no Case. That covers its birth, not a later change: the one rule still requires a Case to rename a page. The old slug has no prefix, so `materialize` marks the entry of 460.1 `category: unknown` and `incomplete: [category]` (case 320). `generate` still applies it: `Vault.update` finds the page in any folder, and `rename` requires the new slug to open with `lesson-`. `apply` ticks the line of every applied entry, whatever its category. The docstring of `guppi/generate.py` says the opposite, so 460.1 corrects it.
> `estimate-sprint-migration-file-route-gone` promises that a line with no prefix lands `category: unknown` and that `generate` "reports an error instead of 'applied by hand'". That line records the end of the file route. The code never failed an `update` or a `delete` of an unknown category (`test_a_delete_of_an_unknown_category_is_outside_the_vault`), and 460.1 relies on the `update` applying. The person chose to leave that Estimate as it is. The session 1255 entry is marked `applied`, so no rerun creates the old page again.
> The refusal of 460.5 goes beside the refusal of case 428.1 in the same hook. The other `Stop` hooks, `guppi ratified`, `guppi casecheck` and `guppi context`, do not read the slug of a lesson line, and `.claude/settings.json` does not change. The Criterion of `estimate-ledger-write-lifts` promises that every `- lesson[` line lands. That becomes false, so 460.4 replaces it whole with an exception, as case 428.2 did for 428.1. `case-schema.md` makes no claim that every lesson line lands, so it stays as it is. `rule-ledger-write` carries `deferred_by` `decision-case-442`, which is about another gap of the same hook, and 460 leaves it open. 460.3 replaces the Criterion of `estimate-lint-finds-a-broken-link` whole: every old line is kept word for word, and only the `decision` line changes. Live Decision lists name four `decision-` slugs: `decision-case-130.1`, `decision-case-140` and `decision-case-347` are live, and `decision-case-130.2` is archived. So I expect no new finding, but I have not run `make lint`. `rule-vault-layout` and `estimate-vault-layout-holds` are not touched, because the lint layout option was not chosen. The one `create` carries `ref: rule-ledger-write`, so no vault query ran. A Glob found the new Estimate slug and the new lesson slug free.
> 460.5 supersedes 460.2 of the first ratification. The ledger is append-only and still holds the three lines of 460.2, among them an update of `estimate-ledger-write-lifts`, which is now the work of 460.4. The text of the refusal is unchanged. 460.2 leaves the Spec (case 299.1), and its entries are marked superseded.
> In the rounds, the person chose these answers: the rename, a check in the ledger hook, and one table of prefixes; the prefix is added and nothing else changes; a new Estimate for the refusal, with the Criterion of `estimate-ledger-write-lifts` replaced in a sub-case of its own; lesson lines only, with the exceptions of case 428.1; the migration Estimate left as it is; the docstring of `generate` corrected.

> **problem:**
> One lesson page has no `lesson-` prefix, and nothing on the path from the ledger line to the page checks the prefix of a lesson slug. The table that judges a prefix also lives in two modules that already disagree on `decision-`.

> **recommend:**
> The fix has three parts. Rename the page with an `update` and `rename`, which keeps its History and `origin`. Make the ledger hook refuse a lesson line whose slug `category_of` does not put under lessons, so a wrong slug is caught while the lesson is fresh and never reaches the append-only ledger. Make lint import `category_of` instead of keeping its own table. A lint `layout` finding was rejected: it fires only after the page exists, one session later, and each case would need a rename Case like this one.

### Case 460.1 — The SendUserFile lesson takes the `lesson-` prefix

> **given:**
> `harness-senduserfile-renders-a-markdown-file-on-the-phone` — the lesson page that is renamed
> **＋** `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone` — the slug the page takes
> **＋** `guppi/generate.py` — applies the `update` and its `rename`, and ticks the line of an applied entry
> **＋** `guppi/materialize.py` — lifts the decision line into an entry
> **＋** `rule-lessons-schema` — the slug of a lesson: `lesson-`, then the area, then the cause
> **＋** `rule-vault-layout` — the filename is the slug
> **＋** `vault/wiki/brief.md` — a record that names the old slug
> **＋** `vault/wiki/log.md` — a record that names the old slug

> **when:**
> The librarian runs `uv run guppi generate` over the Spec of this session.

> **then:**
> The lesson page stands under the slug `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone`, and no page stands under `harness-senduserfile-renders-a-markdown-file-on-the-phone`.
> **＋** Its History gains a `renamed from` line with the old slug and an `updated:` line with the change, each pointing to case 460.1.
> **＋** Its `origin`, `status`, `kind`, `root_cause`, `source`, `tags`, `## Trigger` and `## Root cause` stay as they were.
> **－** `vault/wiki/brief.md`, `vault/wiki/log.md` and the ledger lines keep the old slug, because they are records.

> **tasks:**
> - [ ] update `harness-senduserfile-renders-a-markdown-file-on-the-phone`: the slug takes the `lesson-` prefix
>   - rename: `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone`
>   - change: `the lesson- prefix added to the slug (case 460.1)`
> - [ ] `guppi/generate.py`: the module docstring says what `apply` does — an applied entry ticks its line whatever its category, an entry with no category (`unknown`) included; only a `lesson` entry and a failed entry tick nothing — and names case 460.1

> **ratification:**
> ```
> - decision[case 460.1][update][harness-senduserfile-renders-a-markdown-file-on-the-phone]{ref:harness-senduserfile-renders-a-markdown-file-on-the-phone}
> ```

### Case 460.3 — Lint judges the prefixes in a Decision list by the one table of `materialize`

> **given:**
> `estimate-lint-finds-a-broken-link` — the promise of the links lint follows; its Criterion is replaced whole
> **＋** `guppi/lint.py` — `check_decision` and its own prefix table
> **＋** `guppi/materialize.py` — `category_of`, the one table of prefixes
> **＋** `tests/test_lint.py` — the tests of the `decision` class
> **＋** `vault/wiki/` — the live pages lint reads
> **＋** `rule-one-judgment-one-implementation` — one judgment lives in one module

> **when:**
> `uv run guppi lint` reads the lists `create`, `update`, `delete` and `defer` of each Decision page under `vault/wiki/`.

> **then:**
> `check_decision` gives each slug of the lists its category by `category_of` of `guppi/materialize.py`, the prefix of a Decision page included.
> **＋** A slug with a category that no live or archived page carries is a `decision` finding.
> **－** A slug without a prefix known to `category_of` is not looked up.
> **－** The other classes of lint answer as before.

> **tasks:**
> - [ ] update `estimate-lint-finds-a-broken-link`: the Criterion replaced whole, every line kept but the `decision` one
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ````
>     When:
>     `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.
>
>     Then:
>     `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
>     **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
>     **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate; a `### case N` block under an Estimate's `## Criterion` with no live or archived `decision-case-N`.
>     **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
>     **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
>     **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
>     ````
>   - change: `the Criterion replaced whole — the prefixes of a Decision list are judged by category_of of guppi/materialize.py, decision- included (case 460.3)`
> - [ ] `guppi/lint.py`: `check_decision` imports `category_of` from `guppi/materialize.py`, and the module's own `PREFIXES` table is removed; the docstring of the `decision` class names case 460.3
> - [ ] `tests/test_lint.py`: a Decision list that names a missing slug with the prefix of a Decision page gives the `decision` finding; one that names a live or archived Decision page gives none; a slug without a known prefix is not looked up
> - [ ] by hand — `make lint` on the live vault: no new `decision` finding
> - [ ] read `estimate-lint-finds-a-broken-link`: `uv run pytest tests/test_lint.py` in a later session

> **ratification:**
> ```
> - decision[case 460.3][update][estimate-lint-finds-a-broken-link]{ref:estimate-lint-finds-a-broken-link}
> ```

### Case 460.4 — A lesson line refused for its slug does not land

> **given:**
> `estimate-ledger-write-lifts` — the promise that the lines of a `LEDGER` block land; its Criterion is replaced whole
> **＋** `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger
> **＋** `guppi/ledger.py` — the hook
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `tests/test_gate.py` — the tests of the gate's advice
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the ledger of the session
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — the refusal of a reading, an exception
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the refusal of a lesson slug, an exception

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **－** An `estimate[...]` line the hook refuses by `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-lesson-without-its-prefix` does not land.
> **－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

> **tasks:**
> - [ ] update `estimate-ledger-write-lifts`: the Criterion replaced whole
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a lesson line refused for its slug does not land (case 460.4)`
> - [ ] read `estimate-ledger-write-lifts`: `uv run pytest tests/test_ledger.py tests/test_gate.py` in a later session

> **ratification:**
> ```
> - decision[case 460.4][update][estimate-ledger-write-lifts]{ref:estimate-ledger-write-lifts}
> ```

### Case 460.5 — The ledger hook refuses a lesson line whose slug lacks `lesson-`

> **given:**
> `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger
> **＋** `guppi/ledger.py` — the hook, beside the refusal of case 428.1
> **＋** `guppi/materialize.py` — `category_of`, the one table of prefixes, and `parse_line`
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the new promise
> **＋** `rule-one-judgment-one-implementation` — one judgment lives in one module
> **＋** `rule-lessons-schema` — the slug of a lesson

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session. `category_of` of `guppi/materialize.py` does not put its slug under the lessons folder: the slug does not start with the lesson prefix.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — a lesson slug starts with lesson-, then the area, then the cause: write the line again with the prefix."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A lesson line whose slug starts with the lesson prefix is written as before. A line already in the ledger of any session is not judged again.
> **－** `estimate[...]` and `decision[...]` lines are not judged by their prefix.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

> **tasks:**
> - [ ] create `estimate-ledger-write-refuses-a-lesson-without-its-prefix`
>   - type: `estimate`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses a lesson line whose slug does not open with lesson-, and says why only for the reply just finished`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] update `rule-ledger-write`: the refusal of a lesson slug without its prefix in `## How it works`
>   - old: `A reading of the new slug of a rename is not caught here: no decision line names it.`
>   - new: `` A reading of the new slug of a rename is not caught here: no decision line names it. A lesson names its category (case 460.5): a `lesson[<slug>]` line whose slug `category_of` of `guppi/materialize.py` does not put under `lessons` — a slug that does not open with `lesson-` — is not written, since `materialize` sends a lesson line to `lessons/` by its record, not by its slug, and a slug with no prefix reached the vault that way (session 1255, ledger line 54); as for a refused reading, the hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, skips an older one without a word, and writes the other lines as before. ``
>   - change: `the ledger hook refuses a lesson line whose slug lacks lesson- (case 460.5)`
> - [ ] `guppi/ledger.py`: a function that returns the fresh `lesson[...]` lines whose slug `category_of` does not put under `lessons`, read by `parse_line` and `category_of` imported inside the function as `changed_by_session` does; `run` drops them with the refused readings, prints the stderr line for each one in the reply just finished, and exits 2 when either refusal speaks; the module docstring names case 460.5
> - [ ] `tests/test_ledger.py`: a lesson line without `lesson-` in the finished reply is not written, and the hook exits 2 with the stderr line; the same line in an earlier text is skipped silently; a `lesson-` line and the other lines of the `Stop` are written; a lesson line already in a ledger is not judged; an estimate or decision line without a prefix is not refused by this check
> - [ ] read `estimate-ledger-write-refuses-a-lesson-without-its-prefix`: `uv run pytest tests/test_ledger.py` in a later session

> **ratification:**
> ```
> - decision[case 460.5][create][estimate-ledger-write-refuses-a-lesson-without-its-prefix]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}{supersedes:case 460.2}
> - decision[case 460.5][update][rule-ledger-write]{ref:rule-ledger-write}
> ```
