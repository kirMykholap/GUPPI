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
- [ ] Whether the Renders of the skills that ship name the main branch by {{main_branch}}, or, in the session of a ratified setup Case, by the name that Case sets, which /sprint-open writes into the prompt of the opening Case, their files by the name that rule-guppi-config sets, and the Purposes of rule-git-context and rule-work-mode by words · pending
- [ ] Whether the librarian's agent file names the main branch by {{main_branch}}, and the Purposes of rule-page-generation and rule-vault-layout and the rows Librarian and Work Mode of the glossary by words · pending
- [ ] Whether a new install in a git project made by git init -b master has its setup Case show master as the main branch for correction, its opening Case and Work Mode take master as the main branch in the same session, and its librarian's run write main_branch = "master" into guppi.toml and master into the rendered skills that name the main branch · pending
- [ ] Whether /retro, called by the agent at the end of /work in the Claude Code CLI, loads whatever guppi test and guppi style find, its lines Tests and Style each ending with the line that names the exit code · pending
- [x] Whether the milestone The plugin of the sprint page holds the merge line and then the close line alone, and Closed holds the plugin that installs, the setup and the README; read once · passed

## Milestones

### [ ] The clean branch

- [ ] [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint; what remains: the owner pushes `plugin` and a tag of the form `prod-x.y.z` on its last commit, and the CI run it starts is read by its Estimate; while a page with `core: true` that blocks the build stands — a `draft` one never `built`, or one with an Estimate `failed` — that run writes nothing to `prod` · draft, passed

### [ ] The plugin — 2 items: the merge of `main` into `plugin` — `/merge-main`, a session of its own, the close of `plugin` — `/sprint-close`, a session of its own

## Closed

- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)
- The name of the main branch: a project whose main branch is not main sets its name at the setup, and the code and the skills read it (case 1070)
- The clean version made into a Claude Code plugin: written into a local folder by `guppi ship --allow-draft`, it installs into an empty project, `/guppi:install` copies GUPPI there and `/hi` runs there (case 1075)
- The setup of a new project: `rule-morph` and `rule-skill-setup` built, the setup Case at the first `/hi` after `/guppi:install` before the first sprint (case 1075)
- The README on what the project is and what it is for and on its main parts and its use, as the person confirmed it (case 1075)
