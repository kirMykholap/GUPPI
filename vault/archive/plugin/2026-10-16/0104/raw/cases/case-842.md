## Case 842 — The plugin install check waits for a version tag

> **context:**
> `estimate-clean-branch-installs-as-a-plugin` checks that `guppi ship` writes the manifest of the plugin `guppi` and the catalogue `guppi-marketplace` into the clean version, that `claude plugin validate` passes on it, that `.github/workflows/prod.yml` runs that check before it writes `prod`, and that the plugin installs into an empty project. Its by-hand part builds the clean version with `guppi ship --allow-draft`. `.guppi/guppi/ship.py` takes the version from the highest tag `prod-x.y.z` in the history of HEAD, and with no such tag it prints `ship: no tag prod-x.y.z in the history of HEAD; nothing written` and exits 1. The brief of the librarian of session 1959 (`vault/wiki/brief.md`, `## Readings due`) says `git tag` holds `prod-1` and `prod-2` only. So the Retro of session 1739 marked the Estimate `failed` unread, and case 831 put it off. Its `method` waits for an event that has passed, the Work Mode of case 816.1, and does not name the tag.
>
> The tag is the work of Case 841 of this batch, the Frontier item C1. Its case file did not yet stand when this Case was built, so this Case names no tag of its own and waits for any tag `prod-x.y.z` in the history of HEAD. The person chose to set the Estimate `pending`, write its Criterion back unchanged and give it a `method` whose by-hand part opens with `by hand, after a tag prod-x.y.z stands in the history of HEAD:`. By `case-schema.md` (case 781), and by `waits_for_an_event` of `.guppi/guppi/lint.py`, such a part waits for its event, so Retro leaves the Estimate `pending` until the tag stands and marks it failed for no missing tag. The person also chose to do the install step: the agent runs the test, the build, `claude plugin validate` and the reading of the files, and the person adds the folder as a catalogue and installs `guppi` from it in an empty project, as the other install checks of the sprint do. The rule that governs a promise is `case-schema.md`: a promise changes only by a Criterion replaced whole (case 378.4). The Criterion stands: each of its lines still states what `rule-clean-branch` sets, and the failure was the missing tag, not the promise. So the Estimate itself checks this Case, and no new Estimate is made.
>
> The Case takes up the defer of case 831 on this page by `{supersedes:case 831}`. Case 831 also put off `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-guppi-package-is-ready-after-the-install`; those are the items of Cases 843 and 846, and this Case does not settle them. A Grep for `estimate-clean-branch-installs-as-a-plugin` over the repository, `vault/raw/` left out, printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/log.md`; the hit in `rule-clean-branch` is its `estimates` field and a History line, and neither changes. A Grep for `installs-as-a-plugin|after the Work Mode of this change` over `.guppi/` printed nothing, so no test reads this page live. The brief (`## Flags`) reports `guppi check` at exit 1 with `unread: failed` on the 4 failed Estimates, this one among them; with the Estimate `pending`, that line goes after the librarian's run. No `create` stands in the Case, so no query of the vault for a free slug was run.

> **problem:**
> The plugin install check is `failed` and put off. It was never read, because no tag `prod-x.y.z` stood. Its `method` does not say that it waits for that tag, and it does not say who installs the plugin.

> **recommend:**
> - **How does the plugin-install check come back to a reading?**
>   - Recommended: (a) set it `pending`, keep its promise word for word, and make the by-hand part of its `method` wait for a tag `prod-x.y.z` in the history of HEAD; the defer is taken up.
>   - Answer: agreed, (a).
> - **Who installs the plugin into an empty project?**
>   - Recommended: (a) the person installs by `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace` in an empty project in Claude Code; the agent runs the test, the build, `claude plugin validate` and the reading of the files.
>   - Answer: agreed, (a).

> **given:**
> `estimate-clean-branch-installs-as-a-plugin`: set `pending`, its Criterion kept, its `method` set anew.
> **＋** `rule-clean-branch`: the rule that the Estimate checks.
> **＋** `decision-case-831`: the decision that put the Estimate off.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship` and its option `--allow-draft`.
> **＋** `.guppi/tests/test_ship.py`: the tests of the command `ship`.
> **＋** `plugin/plugin.json` and `plugin/marketplace.json`: the sources of the manifest and of the catalogue.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.
> **＋** `.claude-plugin/`: the folder of the clean version that holds `.claude-plugin/plugin.json`, the manifest, and `.claude-plugin/marketplace.json`, the catalogue.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, or `uv run --project .guppi guppi ship --allow-draft <folder>` into a local folder, builds the clean version, as `rule-clean-branch` sets it, and `claude plugin validate` runs on that folder.
> **＋** In an empty project, someone adds that folder to Claude Code as a catalogue and installs the plugin `guppi` from it.

> **then:**
> `uv run --project .guppi guppi ship <folder>` writes `.claude-plugin/plugin.json` into the clean version, copied from `plugin/plugin.json`, with the `name` `guppi`, a description, the author `kirMykholap` and the repository of the project on GitHub.
> **＋** It writes `.claude-plugin/marketplace.json`, copied from `plugin/marketplace.json`, with the `name` `guppi-marketplace`, the owner `kirMykholap` and one entry, the plugin `guppi`, whose source is the root of the branch.
> **＋** `claude plugin validate` passes on that folder.
> **＋** Before a run of `.github/workflows/prod.yml` commits, it runs `claude plugin validate` on the clean folder.
> **＋** The catalogue adds to Claude Code, and the plugin `guppi` installs from it, with no error.
> **－** A run whose `claude plugin validate` fails fails and writes nothing to `prod`.
> **－** The clean version holds no folder `plugin/`, and this repository holds no folder `.claude-plugin/`.
> **－** Which skills the installed plugin `guppi` loads is no part of this promise.

> **tasks:**
> - [ ] update `estimate-clean-branch-installs-as-a-plugin`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_ship.py; by hand, after a tag prod-x.y.z stands in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty local folder, claude plugin validate run on that folder, the two files of its .claude-plugin/ and the step of .github/workflows/prod.yml that runs claude plugin validate read against the Criterion, then the person's answer after the person adds that folder as a catalogue by /plugin marketplace add <folder> and installs guppi by /plugin install guppi@guppi-marketplace in an empty project open in Claude Code"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `uv run --project .guppi guppi ship <folder>`, or `uv run --project .guppi guppi ship --allow-draft <folder>` into a local folder, builds the clean version, as `rule-clean-branch` sets it, and `claude plugin validate` runs on that folder.
>     **＋** In an empty project, someone adds that folder to Claude Code as a catalogue and installs the plugin `guppi` from it.
>
>     Then:
>     `uv run --project .guppi guppi ship <folder>` writes `.claude-plugin/plugin.json` into the clean version, copied from `plugin/plugin.json`, with the `name` `guppi`, a description, the author `kirMykholap` and the repository of the project on GitHub.
>     **＋** It writes `.claude-plugin/marketplace.json`, copied from `plugin/marketplace.json`, with the `name` `guppi-marketplace`, the owner `kirMykholap` and one entry, the plugin `guppi`, whose source is the root of the branch.
>     **＋** `claude plugin validate` passes on that folder.
>     **＋** Before a run of `.github/workflows/prod.yml` commits, it runs `claude plugin validate` on the clean folder.
>     **＋** The catalogue adds to Claude Code, and the plugin `guppi` installs from it, with no error.
>     **－** A run whose `claude plugin validate` fails fails and writes nothing to `prod`.
>     **－** The clean version holds no folder `plugin/`, and this repository holds no folder `.claude-plugin/`.
>     **－** Which skills the installed plugin `guppi` loads is no part of this promise.
>     ```
>   - change: `read again once a tag prod-x.y.z stands; the Criterion stands, the method waits for the tag and names the person's install`
> - [ ] read `estimate-clean-branch-installs-as-a-plugin`

> **ratification:**
> ```
> - decision[case 842][update][estimate-clean-branch-installs-as-a-plugin]{ref:rule-clean-branch}{supersedes:case 831}
> ```
