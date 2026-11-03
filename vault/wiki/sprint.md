# Sprint

## plugin

GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand. Done when every Estimate of this page passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).

**Done when**

- [ ] Whether the session that closes sprint plugin runs /sprint-close from the close line up to the end of Work Mode with no step done or fixed by hand · pending
- [ ] Whether README.md says what GUPPI is and what it is for, its main parts and how to install and use it, as the person confirms · pending
- [ ] Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch main by the owner alone · pending
- [x] Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data and with the version of its tag prod-x.y.z, and fails when one remains or when no such tag stands in its history · passed
- [ ] Whether the clean version, written into a local folder by guppi ship --allow-draft, installs as a Claude Code plugin into an empty project, /guppi:install copies GUPPI there, and /hi runs there · pending
- [x] Whether guppi check prints no ref line for estimate-link-graph-prints-the-neighbours once the bare link of its Result stands in a code span, the rest of that page as it stood · passed
- [ ] Whether guppi check prints no ref line for lesson-ledger-reading-writes-a-bare-wikilink once the bare link of its root cause stands in a code span, in the section and the field, the rest of that page as it stood but the line its History gains · pending
- [ ] Whether, after the librarian's run that deletes the graph of links, no .guppi/links.md, no command guppi links and no SessionStart hook for it stand, its pages and Estimates are archived, no live text names them and the tests pass · pending
- [x] Whether the case-guppi that built the Case adding .guppi/guppi/frontierguard.py and its test, in session 2155, made and named in context each search and reading for the folders of a new file that rule-case-build sets; read once · passed

## Milestones

### [x] The clean branch

### [ ] The plugin

- [ ] the clean version made into a Claude Code plugin
- [ ] [[rule-morph]] — the setup Case that the first `/hi` after `/guppi:install` puts before the opening of the first sprint; the setup skill `/setup` of `rule-skill-setup`, its step in `/hi` and in `/sprint-open`, the key `setup_done` of `guppi.toml`, the pass of the ledger hook for the setup Case while no sprint is open and the clean version that ships `setup_done = false` are built by case 1017; what remains: the readings by hand of its two Estimates in a new project installed from a copy that `guppi ship --allow-draft` writes, until which `rule-morph` and `rule-skill-setup` stay `draft` and the workflow writes nothing to `prod` · draft
- [ ] the README on what the project is and what it is for and on its main parts and its use
- [ ] the close of `plugin` — `/sprint-close`, a session of its own

## Closed

- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)
