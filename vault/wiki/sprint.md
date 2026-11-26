# Sprint

## plugin

GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand. Done when every Estimate of this page passes, a one-off Estimate, which carries `once: true`, by one reading that passes, a failed one worked on until a reading passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).

**Done when**

- [ ] Whether the session that closes sprint plugin runs /sprint-close from the close line up to the end of Work Mode with no step done or fixed by hand · pending
- [x] Whether README.md says what GUPPI is and what it is for, its main parts and how to install and use it, as the person confirms · passed
- [ ] Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch main by the owner alone · pending
- [x] Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data and with the version of its tag prod-x.y.z, and fails when one remains or when no such tag stands in its history · passed
- [x] Whether the clean version, written into a local folder by guppi ship --allow-draft, installs as a Claude Code plugin into an empty project, /guppi:install copies GUPPI there, and /hi runs there · passed
- [x] Whether guppi check prints no ref line for estimate-link-graph-prints-the-neighbours once the bare link of its Result stands in a code span, the rest of that page as it stood · passed
- [ ] Whether guppi check prints no ref line for lesson-ledger-reading-writes-a-bare-wikilink once the bare link of its root cause stands in a code span, in the section and the field, the rest of that page as it stood but the line its History gains · pending
- [ ] Whether, after the librarian's run that deletes the graph of links, no .guppi/links.md, no command guppi links and no SessionStart hook for it stand, its pages and Estimates are archived, no live text names them and the tests pass · pending
- [ ] Whether a case-guppi build of the sprint plugin that adds a file outside vault/wiki/ makes and names in context each search and reading for the folders of the new file that rule-case-build sets, the root .gitignore included; passes once · pending
- [ ] What the levels of the dispatch of case-guppi saved in time and tokens per Case, whether the builds got worse, and whether the person keeps them · pending
- [ ] Whether the sprint page says that an Estimate, a one-off one too, is done when it passes, and that a failed one-off reading is not done; read once · pending
- [x] Whether uv sync builds the package guppi from a fresh copy of .guppi/ with no warning that the build line of .guppi/pyproject.toml does not hold the version of uv, on a uv from 0.11 to before 0.14 · passed
- [ ] Whether the form of a Case, case-guppi, pre-spec and the schema of an Estimate say that a passed one-off Estimate gets no update from a later Case and is no missed Estimate, while a pending or failed one is updated as before; read once · pending

## Milestones

### [ ] The clean branch

- [ ] [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint; what remains: the owner pushes `plugin` and a tag of the form `prod-x.y.z` on its last commit, and the CI run it starts is read by its Estimate; while a page with `core: true` that blocks the build stands — a `draft` one never `built`, or one with an Estimate `failed` — that run writes nothing to `prod` · draft, passed

### [ ] The plugin — 4 items: the clean version made into a Claude Code plugin, [[rule-morph]], the README on what the project is and what it is for and on its main parts and its use, the close of `plugin` — `/sprint-close`, a session of its own

## Closed

- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)
