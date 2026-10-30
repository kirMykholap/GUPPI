## Case 927 — The method of the Makefile Estimate names real targets

> **context:**
> `uv run --project .guppi guppi check` reads the `method` of each Estimate. On an Estimate of a MOC, `check_method` of `.guppi/guppi/lint.py` takes the first match of `MAKE_TARGET`, the word `make` and the word after it, and gives a finding when `holds_target` finds no such target in the `Makefile`. The method of `estimate-harness-make-runs-in-both-shells`, whose target `rule-harness` is a MOC with no parent, says "make with the targets help, style, test and lint", so the check reads `with` as a target and prints `estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`. The brief, `## Flags`, reports it among the 13 lines of `guppi check` at its last run (exit 1), and the work files of each session since 2026-10-15 hold it in their Baseline. Case 838 put this misreading off as a defer on `rule-lint`. The person chose to fix the wording of the page and leave the check as it is: the check keeps what `estimate-lint-checks-the-method` promises, that a `make <target>` the `Makefile` does not hold is a finding. The new method names `make help`, `make style`, `make test` and `make lint`. `MAKE_TARGET` then reads `help` first, and the `Makefile` holds `help:`, so the line goes. `ships` of `.guppi/guppi/ship.py` leaves out of the clean copy an Estimate whose method has a match of `MAKE_TARGET`; the new method still has one, so the Estimate stays out of the copy, as it should, since the copy holds no `Makefile`. I read `check_method`, `is_reading`, `names_a_moc_form`, `names_test_files`, `missing_test_files`, `holds_target` and `sibling_names_a_target` of `lint.py`, and `ships` of `ship.py`. The pytest part of the method names `.guppi/tests/test_lint.py`, which exists, and stands. The Criterion and the status `passed` of the Estimate stand, since only the `method` field changes. A Grep of `^method:.*\bmake [\w-]` over `vault/wiki` printed 11 methods; two more say "make with the target": `estimate-guppi-config-runs-the-test-and-style-commands` and `estimate-lint-runs-every-step`. Their targets are Leafs, where `by hand` passes before any make target is read, so lint gives them no finding; `ships` leaves them out of the clean copy for the same misread word, and this Case leaves that as it stands, by the person's choice of the page over the check. A Grep of `make-runs-in-both-shells` over `.guppi` printed nothing, so no test reads this page. The change is checked by `estimate-lint-checks-the-method`, whose Criterion says that on a MOC a `make <target>` of the `Makefile` passes whatever stands beside it; it stands, since the check does not change, and the `guppi check` of the librarian's run, which the brief reports, shows the line gone. The page changes at that run, so `guppi check` in Work Mode still prints the line. The update of `rule-lint` carries only a History line and retires the defer of case 838, so the librarian's run takes `rule-lint` off the backlog.

> **problem:**
> `guppi check` stays red on one line because the method of `estimate-harness-make-runs-in-both-shells` says "make with", and the check reads `with` as a target of the `Makefile`.

> **recommend:**
> - **Fix the page or the check**
>   - Recommended: (a) reword this one method so that it names the targets as `make help`, `make style`, `make test` and `make lint`.
>   - Answer: agreed, (a).
> - **The put-off decision on rule-lint**
>   - Recommended: (a) take it up and close it in this Case, by an update of `rule-lint` with a History line only.
>   - Answer: agreed, (a).

> **given:**
> `estimate-harness-make-runs-in-both-shells`: the Estimate whose `method` changes.
> **＋** `rule-lint`: the page that holds the defer of case 838.
> **＋** `.guppi/guppi/lint.py`: the check that reads a make target in a `method`.
> **＋** `.guppi/guppi/ship.py`: the copy that leaves out an Estimate with a make target in its `method`.
> **＋** `Makefile`: the file that holds the targets.
> **＋** `estimate-lint-checks-the-method`: the Estimate that checks the `method` of an Estimate.

> **when:**
> `uv run --project .guppi guppi check`, at the librarian's run, reads the `method` of `estimate-harness-make-runs-in-both-shells` with `.guppi/guppi/lint.py`.

> **then:**
> The check reads `make help` as the make target of the `method`, and the `Makefile` holds `help`.
> **＋** The check prints no `method` line for `estimate-harness-make-runs-in-both-shells`.
> **＋** `.guppi/guppi/ship.py` still leaves `estimate-harness-make-runs-in-both-shells` out of the clean copy.
> **－** The Criterion and the status of `estimate-harness-make-runs-in-both-shells` do not change.
> **－** `.guppi/guppi/lint.py` does not change.

> **tasks:**
> - [ ] update `estimate-harness-make-runs-in-both-shells`
>   - set:
>     ```
>     method: "uv run --project .guppi pytest .guppi/tests/test_lint.py -k makefile; by hand, after the Work Mode that builds this change: make help, make style, make test and make lint from PowerShell and from Git Bash on Windows, read against the Criterion"
>     ```
>   - change: `the method names the targets as make help, make style, make test and make lint, so lint reads no target with`
> - [ ] update `rule-lint`
>   - change: `the defer of case 838 is taken up: the method of estimate-harness-make-runs-in-both-shells names real targets, and the check stands`

> **ratification:**
> ```
> - decision[case 927][update][estimate-harness-make-runs-in-both-shells]{ref:rule-harness}
> - decision[case 927][update][rule-lint]{ref:rule-lint}{supersedes:case 838}
> ```
