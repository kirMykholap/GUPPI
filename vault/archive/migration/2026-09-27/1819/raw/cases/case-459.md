## Case 459 — Lint does not count the Estimates of a render child against a MOC's reading

> **context:**
> Lint checks the `method` of each Estimate. For an Estimate of a MOC, a reading by hand passes only if every Estimate of the MOC's children is a reading too, or if a sibling Estimate names a `make <target>` (cases 112.1, 212). The clause stops a MOC's reading from hiding its children's tests. The code is `check_method` in `guppi/lint.py`, and the promise is `estimate-lint-checks-the-method`.
> The clause is wrong for `rule-claude-md`. `CLAUDE.md` is its Render in `render_mode: full`, with its three children spliced into their markers. Its one Estimate, `estimate-claude-md-rendered`, is a reading: the file equals the Render and every session loads it. Case 445.4 gave the child `rule-language` the Estimate `estimate-language-spec-prose-in-english`, whose `method` is a pytest over pre-spec. Since then lint prints `method: says by hand while estimate-language-spec-prose-in-english names a test file`. Case 454 deferred the item onto `rule-claude-md`.
> Nothing is hidden. By case 378.5, the Estimate of a render rule promises only that the file equals the Render and is loaded. The behaviour a spliced paragraph describes belongs to that child's own Estimate, which is read on its own.
> The frame has five MOCs with `enforcement: render` and `render_mode: full`: `rule-claude-md`, `rule-case-protocol`, `rule-skill-hi`, `rule-settings` and `rule-documentation`. The children of `rule-documentation` are code rules with tests. For that reason the person chose the narrow bound: only the Estimates of a child with `enforcement: render` stop counting. The Estimates of any other child still count.
> The same clause stands in two more places, and this Case changes both. One is the module docstring of `guppi/lint.py`. The other is the description of `method` that `rule-estimates-schema` renders into `vault/wiki/estimates/schema.yaml`.
> The new Criterion keeps every line of the old one. The old third line changes on purpose: it now counts only the counted Estimates of the children. The Leaf finding keeps its exact text. That text stands in quotation marks, not a code span, because the frame check of pre-spec reads a span with a slash as a path.
> The Criterion of `estimate-estimates-schema-checked` does not speak of the `method` description, so it is not touched. `estimate-prespec-catches-a-method-without-a-form` leaves the MOC branch to lint, so it still stands. No Estimate of `rule-claude-md` changes, because its promise is unchanged.
> The decision line carries `{supersedes:case 454}`, so `generate` clears the defer from `rule-claude-md`. The other lint findings in the brief stay with their own items.

> **problem:**
> Lint reports a contradiction on `estimate-claude-md-rendered` that is not one. The clause of cases 112.1 and 212 counts the tested Estimate of a child whose Render is spliced into its parent's file. That Estimate promises the child's own behaviour, not the file, so the parent's reading hides nothing.

> **recommend:**
> On a MOC with `render_mode: full`, lint should not count the Estimates of a child with `enforcement: render`. The Estimates of every other child still count, so the check of case 112.1 stays wherever a reading could hide a child's tests. The change is in `guppi/lint.py`, its tests, the Criterion of `estimate-lint-checks-the-method` and the description in `rule-estimates-schema`. The wider exemption of the whole render MOC was rejected: it would let a future reading on `rule-documentation` hide the tests of its code children.

> **given:**
> `estimate-lint-checks-the-method` — the promise of the `method` check of lint.
> **＋** `guppi/lint.py` — `check_method`, `children_estimates` and the module docstring, the MOC clause of cases 112.1 and 212.
> **＋** `tests/test_lint.py` — the tests of the MOC branch of the `method` check.
> **＋** `rule-estimates-schema` — renders the description of `method` into `vault/wiki/estimates/schema.yaml`.
> **＋** `Makefile` — the targets a `method` may name.
> **＋** `estimate-claude-md-rendered` — the reading of `rule-claude-md` that lint reports today.
> **＋** `rule-lint` — the rule the check belongs to.

> **when:**
> `uv run guppi lint` reads the `method` of each live Estimate: the field, or `## Method` on a page of the old shape.

> **then:**
> For an Estimate of a Leaf, a `tests/` file that exists, the word `pytest`, a `make <target>` of the `Makefile`, or `by hand` passes; else the finding "method: names no tests/ file, pytest or make target and is not a reading".
> **＋** A named `tests/` file that does not exist, or a `make <target>` the `Makefile` does not hold, is a finding.
> **＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it; `by hand` without one passes when every counted Estimate of the children is a reading or a sibling Estimate names a `make <target>` of the `Makefile`; else a finding.
> **＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
> **＋** `estimate-claude-md-rendered` gets no `method` finding.
> **－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
> **－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.

> **tasks:**
> - [ ] update `estimate-lint-checks-the-method`: the Criterion replaced whole
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — on a MOC with render_mode: full the Estimates of a child with enforcement: render are not counted (case 459)`
> - [ ] update `rule-estimates-schema`: the description of `method` in the Render
>   - old: `` and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target. ``
>   - new: `` and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target; on a MOC with `render_mode: full` the Estimate of a child with `enforcement: render` is not counted, since that child's Render is part of the parent's file and its Estimate promises the child's own behaviour (cases 378.5, 459). ``
>   - change: `the method of a MOC's Estimate: the Estimates of a render child of a full MOC are not counted (case 459)`
> - [ ] `guppi/lint.py`: in the MOC branch of `check_method`, skip the Estimates of a child with `enforcement: render` when the MOC has `render_mode: full`; the module docstring, in the `method` class, and the docstrings of `check_method` and `children_estimates` name the exception and case 459
> - [ ] `tests/test_lint.py`: a full MOC with a reading over a render child whose Estimate names a test file passes; the same MOC over a child without `enforcement: render` gives the finding; a MOC without `render_mode: full` over a render child gives the finding
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] read `estimate-lint-checks-the-method`: `uv run pytest tests/test_lint.py`, then `make lint` prints no `method` finding on `estimate-claude-md-rendered`

> **ratification:**
> ```
> - decision[case 459][update][estimate-lint-checks-the-method]{ref:estimate-lint-checks-the-method}{supersedes:case 454}
> - decision[case 459][update][rule-estimates-schema]{ref:rule-estimates-schema}
> ```
