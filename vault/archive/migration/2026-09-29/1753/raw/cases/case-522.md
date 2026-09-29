## Case 522 — A repeat ticks no line of the Spec

> **context:**
> `guppi generate` writes the entries of `materialize.yaml` into the pages. After it applies an entry, it ticks the entry's line in the Spec beside the yaml. Case 514 made an entry a repeat when its `case`, `kind` and `slug` match those of an entry of the same yaml that is already applied. A repeat changes no page and prints `generate: <slug>: line N repeats line M of case C; nothing applied`. The built code still sends a repeat through the tick, and the handoff of session 1432 says so: "A repeat of Case 514 ticks its line of the Spec, as an applied entry does; the task line said "apply nothing"". In a real session this ticks nothing. When a Case is ratified again, the Spec holds it once with one line per page, so the first entry ticks that line and the repeat finds no open line. The tick only takes effect when a Case's section holds a second line of the same kind and slug. The test fixture of `tests/test_generate.py` holds such a line, `update `rule-root`: a second time`, and the test of two entries ticking two lines went red without the repeat's tick. A repeated `delete` also runs the tick of the `read` lines. It measures "ratified after it" from its own later ledger line, so it can tick a `read` line in a Case that was ratified between the two lines. No promise signed either tick. The person chose in the round that a repeat ticks nothing. `rule-page-generation` says the Spec's lines "are closed by the one who did the work", and a repeat does no work. The Criterion of `estimate-generate-ticks-the-spec` still says "Each further entry of one kind and slug in one Case ticks the next such line, in order". That sentence dates from case 226.1, before a second entry of one kind and slug in one Case became a repeat, so this Case replaces the Criterion whole. The rest of the Criterion stays word for word, with two changes. The trigger "applied an entry of `materialize.yaml` and marked it `applied`" now covers a repeat as well. The first line of the result is limited to an entry that was applied, and it loses its sentence on further entries. The docstring of `guppi/generate.py` says a repeat "ticks its line of the Spec as an applied entry does (case 514)" and "Two entries of one kind and slug tick two lines, in order", so both sentences change. The sentence of `rule-page-generation` "Once an entry is applied, the script ticks its line" does not exclude a repeat on its own. The same page says a repeat "is marked applied", and `estimate-generate-fails-alone` says it "is marked `applied`". Read alone, the sentence would therefore imply a tick. The page's sentence on Case 514 names the repeat, and this Case adds "ticks no line of the Spec" to it. That sentence settles the point for a repeat, so the general sentence stands as it is. `estimate-generate-fails-alone` stands. Its Criterion describes the repeat and says nothing of the Spec, so no sentence of it becomes false. `generate` is no hook, and it refuses nothing between the change of the code and the change of the text, so no old form is kept. The Case creates no page, so no vault query was needed. The reading of `estimate-generate-ticks-the-spec` waits for a later session, because the ledger hook refuses a reading of a page this session changes (case 428.1).

> **problem:**
> A repeat applies nothing, but it ticks a line of the Spec, and no promise names that tick. When a Case's section holds a second line of the same kind and slug, the repeat marks it as done although nobody did its work. A repeated `delete` can also tick a `read` line of a Case ratified after the first `delete`.

> **recommend:**
> A repeat ticks no line in any Spec. The promise lives in `estimate-generate-ticks-the-spec`, because that Estimate is the promise on ticks. Its trigger is widened to cover a repeat, and a `－` line says that a repeat ticks nothing. A second line of the same kind and slug then stays open, and Retro counts it, which shows the flaw in the Spec. The rejected option was to keep the tick and sign it. That would close lines for work that no one did.

> **given:**
> `guppi/generate.py` — applies the entries and ticks the Spec
> **＋** `materialize.yaml` — the entries `generate` reads and marks
> **＋** `spec.md` — the Spec of a session folder under `vault/raw/`, whose lines `generate` ticks
> **＋** `vault/archive/` — the archived sessions, whose Specs `generate` does not read
> **＋** `tests/test_generate.py` — the tests of `generate`
> **＋** `rule-page-generation` — the rule of `generate`
> **＋** `estimate-generate-ticks-the-spec` — the promise on the ticks of the Spec

> **when:**
> `uv run guppi generate` marks an entry of `materialize.yaml` `applied`. Either it applied the entry, or it found the entry to be a repeat: a `create`, `update`, `delete` or `defer` entry whose `case`, `kind` and `slug` match those of an entry of the same `materialize.yaml` already marked `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry that was applied, in the `spec.md` of the same unit, the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`. Nothing else in the file changes.
> **＋** For an `estimate` entry, a `create` entry with `folded` and a `delete` entry, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]`. The Spec beside the yaml comes first, then the Specs of the other session folders, oldest first.
> **＋** In the Spec beside the yaml, for an `estimate` or a `delete` entry, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the entry's `line` is not the entry's line, and the search goes on.
> **＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` is not the entry's line. For the Spec beside the yaml, the marks come from the run's entries. For another Spec, they come from the `materialize.yaml` beside it. With no yaml beside a Spec, nothing is skipped there.
> **＋** A `create` entry with `folded` ticks both its page line and its `read` line. The filter by `line` does not apply to it, and the filter by `superseded_by` does.
> **＋** A `delete` entry ticks both its page line in its own Case and the `read` lines of its slug.
> **－** A repeat ticks no line in any `spec.md`. A second line `` - [ ] <kind> `<slug>` `` in the section of its Case stays unticked, and a repeated `delete` leaves the `read` lines of its slug as they stand.
> **－** A line, a section or a Spec not found raises no error and prints nothing on stderr. The entry is `applied` all the same.
> **－** A `lesson` entry and an entry marked `failed` tick no line. A `delete` that fails leaves the `read` lines of its slug as they stand.
> **－** A `spec.md` under `vault/archive/` is not read.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `is marked applied and changes no page, so a Case approved again`
>   - new: `is marked applied, changes no page and ticks no line of the Spec, so a Case approved again`
>   - old: `changes each page once (case 514).`
>   - new: `changes each page once (cases 514, 522).`
>   - change: `a repeat ticks no line of the Spec (case 522)`
> - [ ] update `estimate-generate-ticks-the-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a repeat ticks no line of any Spec; a second entry of one kind and slug in one Case no longer ticks the next line`
> - [ ] `guppi/generate.py`: in `apply`, the repeat branch no longer calls `vault.tick`. In the docstring, the repeat sentence says that a repeat ticks no line of the Spec, and the sentence "Two entries of one kind and slug tick two lines, in order" is removed.
> - [ ] `tests/test_generate.py`: the test of two entries of one kind and slug is rewritten. The first entry ticks its line, the second prints the repeat line, and the line `update `rule-root`: a second time` stays `- [ ]`. A new test: a `delete` in one Case, a later Case with a `read` line of its slug, and a repeat of the `delete` after that later Case. The `read` line of the later Case stays `- [ ]`.
> - [ ] read `estimate-generate-ticks-the-spec`

> **ratification:**
> ```
> - decision[case 522][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 522][update][estimate-generate-ticks-the-spec]{ref:estimate-generate-ticks-the-spec}
> ```
