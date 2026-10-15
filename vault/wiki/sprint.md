# Sprint

## plugin

GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand. Done when every Estimate of this page passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).

**Done when**

- [ ] Whether the session that closes sprint plugin runs /sprint-close from the close line up to the end of Work Mode with no step done or fixed by hand · pending
- [ ] Whether README.md says what GUPPI is and what it is for, its main parts and how to install and use it, as the person confirms · pending
- [ ] Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch main by the owner alone · pending
- [ ] Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data and with the version of its tag prod-x.y.z, and fails when one remains or when no such tag stands in its history · pending
- [ ] Whether the clean version, written into a local folder by guppi ship --allow-draft, installs as a Claude Code plugin into an empty project, /guppi:install copies GUPPI there, and /hi runs there · pending

## Milestones

### [ ] The clean branch

- [ ] [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint; what remains: once Work Mode commits the fix of `guppi ship` that cleans the text around the example Case (case 815), the owner pushes `plugin` and a tag `prod-2` on its last commit, and the CI run it starts is read by its Estimate · draft, pending

### [ ] The plugin — 4 items: the clean version made into a Claude Code plugin, [[rule-morph]], the README on what the project is and what it is for and on its main parts and its use, the close of `plugin` — `/sprint-close`, a session of its own

## Closed

- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)
