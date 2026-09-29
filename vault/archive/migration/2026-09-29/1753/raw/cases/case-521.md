## Case 521 — A comment in a short Case's `then` block is caught, and the cut defer of case 519 is taken up

> **context:**
> When the person puts a decision off, the main agent writes a short-form Case itself. The Case holds a fence tagged `then` in plain YAML with `slug`, `type` and `purpose`. The `Stop` hook of `rule-spec-write` (`guppi/ratified.py`) parses the fence. It checks that each `defer` line has an item with these three keys and no foreign key, then copies the fence into the Spec as the reply shows it. Later `materialize` parses the fence again, and `generate` writes `purpose` under `## Deferred` of the Decision page. In YAML a `#` after a space or a tab starts a comment, so a value without quotes ends before it. At the Retro of session 1432 the short Case 519 held `purpose: Correct the description of ## Criterion in the Render of rule-estimates-schema, …`, and YAML kept only "Correct the description of". That text stands in `materialize.yaml` L36 of 1432, under `## Deferred` on `decision-case-519`, and in the backlog through the `deferred_by` of `rule-estimates-schema`. No check saw it. A full Case built by `case-guppi` does not have this problem. Its values are code spans, and the hook writes their YAML itself with `yaml.dump` of `guppi/ratified.py`, which quotes a value that needs it. A search of every `spec.md` under `vault/raw/` for an unquoted value that holds ` #` found the line of case 519 and no other.
> In one round the person accepted every recommendation. The hook and `materialize` both catch a comment, by one function in `guppi/materialize.py`. Any comment in the fence is a finding, not only a comment after a value. The hook refuses, as it refuses a missing `purpose`. The deferred decision of case 519 is taken up now: the sentence is corrected and case 519 is superseded. The short-form paragraph of `rule-case-protocol` tells the agent to quote such a value.
> What `case-guppi` found in the frame. The round said that `generate` does not apply an entry that `materialize` marks `incomplete`. That is false. `rule-page-generation` says "A page is always created, even incomplete". So the mark of 521.2 names the comment in the yaml that the librarian reads, but it does not stop the page. The refusal of the hook in 521.1 is what keeps the cut text off a page. 521.2 states this as a `－` line and does not change `generate`. `estimate-spec-write-writes-a-defer` promises the checks of a defer, so 521.1 replaces its Criterion whole and keeps each earlier line word for word. The other Estimates of `rule-spec-write` speak of full Cases, the ratified copy, the approved Spec and a superseded Case, and stand. `estimate-materialize-assembles` says that what the block lacks is `incomplete`, never invented. A new reason does not make it false, so it stands. `estimate-materialize-judges-a-fence` speaks of where a fence opens and closes, not of the YAML inside it, and stands. The new promise of `materialize` is the Estimate that 521.2 creates. Its slug `estimate-materialize-marks-a-comment` is free: no page under `vault/wiki/` matches it. It has a `ref`, so no vault query was run. `estimate-estimates-schema-checked` promises the lists of the schema file and that its description and sections name no `Given:` kept on an older page. The corrected sentence keeps both, and an `update` of a Render touches no Estimate of the live reading (case 378.5), so it stands. `estimate-case-protocol-defers-in-one-reply` promises that a defer is shown and written in one reply. It says nothing about the value inside the fence and stands; its failed reading is Frontier item C8. The other hooks on `Stop` in `.claude/settings.json` are `guppi ledger`, `guppi casecheck` and `guppi context`. The ledger hook writes the `defer` line in parallel, whatever `ratified` answers.
> Pre-spec found that the Case defined a comment in two ways. The `then` lines said "after a space or a tab", but the `new` texts of `rule-spec-write` and `rule-materialize` and the sentence of 521.4 said only "after a space". The person accepted the fix. Every text now says "a `#` at the start of a line or after a space or a tab", the one definition that the shared function implements. 521.4 says "after a space or a tab" for a value.
> What the check of the answer notes, and why the notes stand. Two `then` lines of 521.2 share most of their words with 521.1: the definition of a comment, and the `－` line on a `#` inside quotes or inside a `|` or `>` block. This is on purpose. Both sides use one function and the same definition. 521.1 promises what the hook refuses, and 521.2 promises what `materialize` marks. They are separate promises with separate tests, and the test of 521.2 runs both sides over the same fence.
> Code and timing. The hook runs from the working tree as soon as 521.1 is coded, and the sentence of 521.4 reaches `case-schema.md` at the render. In that time the hook may refuse a short Case with an unquoted ` #`. Nothing is lost. The ledger line is written, and the agent shows the Case again with the value in quotes. This is the same path as a refused missing `purpose`. The form it refuses was never correct, so no old form is kept. `materialize` extends an existing yaml and never rewrites it, so L36 of 1432 is not read again.
> Not done: `generate` still applies an entry marked `incomplete`. `materialize.yaml` L36 of 1432 stays as it is. A full Case of `case-guppi` gets no new check, because its values do not pass through hand-written YAML.

> **problem:**
> YAML cuts a value without quotes at ` #`, and no check sees the cut. So a short-form Case can reach the Spec, the Decision page and the backlog with a value the person never wrote, as the purpose of case 519 did. The backlog item of `rule-estimates-schema` also carries that cut text, and the sentence it was meant to correct is still wrong.

> **recommend:**
> Put one function in `guppi/materialize.py` that finds a comment in a fence tagged `then`. The `Stop` hook refuses such a short Case while the person can still fix the wording, and `materialize` marks the entries of such a Case for the librarian. Take up the deferred decision of case 519 now: the fix is one sentence, and its reason is already on the page. Add one sentence to the short-form rule so the agent quotes such a value before the hook has to refuse it. Rejected: a warning only, since the cut text would still reach the page, as it did at case 519.

### Case 521.1 — The `Stop` hook refuses a short Case whose `then` block holds a comment

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a deferred Case into the Spec
> **＋** `guppi/ratified.py` — `deferred_section`, which reads the fence tagged `then` of a short Case
> **＋** `guppi/materialize.py` — holds the one function that finds a comment in a fence tagged `then`, and `item_keys`
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, where a defer at Retro is written
> **＋** `tests/test_ratified.py` — the tests of a defer
> **＋** `estimate-spec-write-writes-a-defer` — the promise; its Criterion is replaced whole

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while Plan Mode lasts, and of `raw/<date>/<hi HHMM>/spec.md` once that file stands, at Retro: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **＋** A key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
> **＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
> **－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
> **－** The ratified copy `<plan>.ratified.md` gets no defer, and the check after the write does not run on it.

> **tasks:**
> - [ ] update `rule-spec-write`
>   - old: `` a key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3). ``
>   - new: `` a key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3); so is a `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — by the one function of `guppi/materialize.py`, since YAML drops the rest of the line and no page receives it (case 521.1). ``
>   - change: `a short Case whose then block holds a YAML comment is refused, judged by the function of guppi/materialize.py (case 521.1)`
> - [ ] update `estimate-spec-write-writes-a-defer`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a then block that holds a YAML comment is refused (case 521.1)`
> - [ ] `guppi/materialize.py`: one function that returns the lines of a fence tagged `then` that hold a YAML comment — a `#` at the start of a line or after a space or a tab — a `#` inside a quoted value or a `|` or `>` block not counted
> - [ ] `guppi/ratified.py`: `deferred_section` imports that function and refuses a block with a comment, with the line and the advice to quote the value; the module docstring says so
> - [ ] `tests/test_ratified.py`: a short Case with `purpose: a ## b` unquoted, and one with a tab before the `#`, are refused and not written; the same value in quotes, and a `#` inside a `|` block, are written
> - [ ] read `estimate-spec-write-writes-a-defer` — `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change, at a later session

> **ratification:**
> ```
> - decision[case 521.1][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 521.1][update][estimate-spec-write-writes-a-defer]{ref:estimate-spec-write-writes-a-defer}
> ```

### Case 521.2 — `materialize` marks the entries of a Case whose `then` block holds a comment

> **given:**
> `rule-materialize` — the rule of the librarian's reading of the ledger and the Spec
> **＋** `guppi/materialize.py` — `then_blocks`, the entry of a decision line, the function that finds a comment, and the docstring list of `incomplete`
> **＋** `raw/<date>/<HHMM>/spec.md` — the Spec whose fences tagged `then` `materialize` reads
> **＋** `rule-spec-write` — the rule of the `Stop` hook that imports the same function
> **＋** `tests/test_materialize.py` — the tests of the lift
> **＋** `rule-page-generation` — the rule of `generate`, which writes a page even from an `incomplete` entry
> **＋** `estimate-materialize-marks-a-comment` — the new promise

> **when:**
> `uv run guppi materialize` lifts the entries of a Case N from its fences tagged `then` in `raw/<date>/<HHMM>/spec.md`.

> **then:**
> A fence of Case N that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — gives each decision entry of Case N `incomplete: [comment]`, and the run does not fail.
> **＋** The entry keeps the values that YAML read, and nothing is invented for the text after the `#`.
> **＋** The comment is found by the same function of `guppi/materialize.py` that the `Stop` hook of `rule-spec-write` imports, so both give the same answer for the same fence.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text and gives no mark.
> **－** `generate` still applies an entry so marked, since a page is always created, even incomplete.

> **tasks:**
> - [ ] update `rule-materialize`
>   - old: `` lifted from the `then` block of its Case in the Spec — `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it (cases 258.2, 274.3). ``
>   - new: `` lifted from the `then` block of its Case in the Spec — `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it (cases 258.2, 274.3). A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — gives each decision entry of its Case `incomplete: [comment]`: YAML drops the rest of the line, so the value may be cut; the judgment is one function, which the `Stop` hook of `rule-spec-write` imports (case 521.2). ``
>   - change: `a then block that holds a YAML comment marks the decision entries of its Case incomplete: [comment] (case 521.2)`
> - [ ] create `estimate-materialize-marks-a-comment`
>   - type: `estimate`
>   - ref: `rule-materialize`
>   - kind: `QA`
>   - purpose: `A then block that holds a YAML comment gives each decision entry of its Case incomplete: [comment], judged by the one function the Stop hook of rule-spec-write imports`
>   - method: `uv run pytest tests/test_materialize.py -k comment`
>   - tags: `[harness, workflow, ledger]`
> - [ ] `guppi/materialize.py`: the entry of a decision line takes `incomplete: [comment]` when a fence tagged `then` of its Case holds a comment, by the function of 521.1; the docstring list of `incomplete` names `comment`
> - [ ] `tests/test_materialize.py`: a Spec whose short Case holds `purpose: a ## b` unquoted gives its entry `incomplete: [comment]` and `purpose: a`; a tab before the `#` gives the same mark; the value in quotes, and a `#` inside a `|` block, give no mark; one test runs the hook's check and `materialize` over the same fence and asserts they answer alike
> - [ ] read `estimate-materialize-marks-a-comment` — `uv run pytest tests/test_materialize.py -k comment`, at a later session

> **ratification:**
> ```
> - decision[case 521.2][update][rule-materialize]{ref:rule-materialize}
> - decision[case 521.2][create][estimate-materialize-marks-a-comment]{ref:rule-materialize}{tags:harness,workflow,ledger}
> ```

### Case 521.3 — The Estimate schema says the frame of a Case stays in its Case file; the defer of case 519 is retired

> **given:**
> `rule-estimates-schema` — the rule; its Render is the schema of an Estimate page
> **＋** `vault/wiki/estimates/schema.yaml` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `decision-case-519` — the deferred decision on this sentence, with the cut text under `## Deferred`
> **＋** `rule-page-generation` — the rule of `generate`, which retires a superseded defer
> **＋** `estimate-estimates-schema-checked` — the promise of the file; its Criterion stands

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and an agent or the person reads the description of `## Criterion` in it.

> **then:**
> The description says that the Criterion holds no `Given:`, since the frame of the Case stays in its Case file and in the Spec.
> **＋** `generate` sets `decision-case-519` `superseded` and removes it from the `deferred_by` of `rule-estimates-schema`, so the backlog no longer holds the cut text; the cascade archives the page.
> **－** The lists that lint reads from `vault/wiki/estimates/schema.yaml` do not change.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `` no `Given:`: the frame of the Case stays on its Decision page (case 378.2) ``
>   - new: `` no `Given:`: the frame of the Case stays in its Case file and in the Spec (cases 378.2, 513) ``
>   - change: `the description of ## Criterion says the frame of a Case stays in its Case file and the Spec; the defer of case 519 retired (case 521.3)`
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`

> **ratification:**
> ```
> - decision[case 521.3][update][rule-estimates-schema]{ref:rule-estimates-schema}{supersedes:case 519}
> ```

### Case 521.4 — The short-form rule tells the agent to quote a value that holds a `#`

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `rule-spec-write` — the rule of the `Stop` hook that refuses a block with a comment

> **when:**
> The main agent reads `vault/wiki/case-schema.md` and then writes a short-form Case.

> **then:**
> The paragraph of the short form says that a value of the `then` block that holds a `#` after a space or a tab stands in quotes, since YAML reads the rest of the line as a comment, and that the `Stop` hook of `rule-spec-write` refuses a block that holds a comment.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` a `then` block with `defer:` carrying `slug`, `type` and `purpose`; no `recommend` ``
>   - new: `` a `then` block with `defer:` carrying `slug`, `type` and `purpose` — a value that holds a `#` after a space or a tab stands in quotes, since YAML reads the rest of the line as a comment and the `Stop` hook of `rule-spec-write` refuses a block that holds one (case 521.4); no `recommend` ``
>   - change: `the short form quotes a value that holds a # after a space or a tab (case 521.4)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`

> **ratification:**
> ```
> - decision[case 521.4][update][rule-case-protocol]{ref:rule-case-protocol}
> ```
