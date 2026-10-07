## Case 731 — The method of the Frontier check is spelled as a reading by hand

> **context:**
> `make lint` sorts the `method` of each Estimate into the forms that `rule-estimates-schema` names. For an Estimate of a MOC, `check_method` in `guppi/lint.py` passes a `make <target>` of the Makefile, or the words `by hand` when no counted Estimate of the children names a test. `rule-skill-hi` is a MOC with `render_mode: full`, and its three children have `enforcement: render`, so none of their Estimates is counted. Case 723.3 set the `method` of `estimate-hi-writes-frontier` to the person's answer at the `/hi` after the close of a sprint, with no words `by hand`, so lint did not read it as a reading and printed the `method` finding that a MOC's Estimate names no `make <target>`. The person chose to put the words `by hand` at the head of the method and keep the rest word for word, since `rule-estimates-schema` calls them the one spelling of a reading. Only the `method` field changes: the update names a part, so the Criterion and the status stay as Case 729 of this session leaves them, and Case 729 kept the method's meaning, which this Case keeps too. The new method names the person in the part that names `/hi`, so `waits_for_another_session` does not judge it a wait, and the `tests/` path keeps it a form for pre-spec. `estimate-lint-checks-the-method` checks the change: its Criterion says that `by hand` passes on a MOC when every counted Estimate of the children is a reading, and on a MOC with `render_mode: full` the Estimates of a child with `enforcement: render` are not counted. That Criterion covers this page as it stands, so it is not replaced, and the `make lint` of the librarian's run, which the brief reports, shows the finding gone. Pre-spec and the check of the Case file leave the MOC branch to lint, and the person chose to leave that gap as it is. A Grep of `` names no `make `` over the repository, `vault/raw/` and `vault/archive/` left out, printed `guppi/lint.py` and `vault/wiki/brief.md`; the brief names the finding and the librarian writes it anew. A Grep of `the person's answer at the /hi` over the same paths printed `vault/wiki/estimates/estimate-hi-writes-frontier.md`, `tests/test_prespec.py`, `tests/test_lint.py` and `vault/wiki/estimates/estimate-context-size-shown-after-each-reply.md`. The test hits are fixtures of methods of their own, and the last hit is a Result line, so they stand.

> **problem:**
> The `method` of `estimate-hi-writes-frontier` names a reading by the person without the words `by hand`, so `make lint` reports that the Estimate of a MOC names no `make <target>`.

> **recommend:**
> - **How is the lint finding removed?**
>   - Recommended: (a) put "by hand" back into the method; only the `method` field changes.
>   - Answer: agreed, (a).
> - **Which check proves the fix?**
>   - Recommended: (a) no new check: `estimate-lint-checks-the-method` stands, and the `make lint` of the librarian's run shows the finding gone.
>   - Answer: agreed, (a).
> - **Is the gap that let the wording through closed too?**
>   - Recommended: (a) leave it: this Case fixes only the one method.
>   - Answer: agreed, (a).

> **given:**
> `estimate-hi-writes-frontier`: the check of the Frontier of `/hi`; its `method` is set anew.
> **＋** `rule-skill-hi`: the MOC the Estimate checks, with `render_mode: full`.
> **＋** `guppi/lint.py`: `check_method` judges the `method` of an Estimate of a MOC.
> **＋** `tests/test_prespec.py`: the unit tests the method names.
> **＋** `rule-estimates-schema`: sets `by hand` as the one spelling of a reading.
> **＋** `estimate-lint-checks-the-method`: the check of the judgment of `check_method`; its Criterion stands.
> **＋** `vault/raw/2026-10-08/0050/cases/case-729.md`: the Case of this session that replaces the Criterion of the same Estimate.

> **when:**
> `make lint` runs `check_method` of `guppi/lint.py` over the `method` of `estimate-hi-writes-frontier`, an Estimate of the MOC `rule-skill-hi`.

> **then:**
> The method opens with the words `by hand`, and `check_method` takes it as a reading.
> **＋** Lint prints no `method` finding for `estimate-hi-writes-frontier`.
> **＋** The method still names the person's answer at the `/hi` of the session after the close of a sprint, and the frontier findings of `guppi prespec --check` in `tests/test_prespec.py`.
> **－** The Criterion and the status of `estimate-hi-writes-frontier` do not change.

> **tasks:**
> - [ ] update `estimate-hi-writes-frontier`
>   - set:
>     ```
>     method: "by hand: the person's answer at the /hi of the session after the close of a sprint, on whether the Frontier came out as the Criterion says, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"
>     ```
>   - change: `the method opens with "by hand", the one spelling of a reading, so lint reads it as one (case 731)`

> **ratification:**
> ```
> - decision[case 731][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```
