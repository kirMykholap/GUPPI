---
type: rule
kind: Leaf
purpose: Prevents a pull request from reaching main unchecked, and an account other than the owner's from writing to main, or to prod, which only the owner and the workflow of rule-clean-branch write
status: draft
enforcement: check
implementation_ref: [.github/workflows/checks.yml]
estimates: []
applies_to: ["[[entity-guppi-repository]]"]
origin: raw/2026-10-12/2349/ledger.md#case-794
sprint: plugin
created: 2026-10-12
tags: [github, ci, git]
---

## Purpose

Prevents a pull request from reaching `main` unchecked, and an account other than the owner's from writing to `main`, or to `prod`, which only the owner and the workflow of [[rule-clean-branch]] write. The repository of the project is the public repository `GUPPI` on GitHub, on the owner's account, and `origin` points to it. Its history starts at the commit that removed the former product from the repository and made it the harness and the vault. The commits of that product before it are not on GitHub, and no copy of them is kept in this repository (case 794). A ruleset on `main` blocks its deletion and a force push, takes a change only by a pull request, and lets a pull request merge only after the jobs `style` and `test` of `.github/workflows/checks.yml` pass. The job `lint` runs too and shows its result on the pull request, but it blocks no merge, since the red of lint is a signal, not a gate ([[rule-lint]]). The owner is on the bypass list of the ruleset, so the owner's own push and merge still work. No approving review is required, since GitHub lets no one approve their own pull request. A ruleset on the name `prod` blocks the creation, the update and the deletion of the branch and a force push. Only the owner and the deploy keys of the repository bypass it, so a pull request into `prod` cannot be merged, and besides the owner only the workflow `.github/workflows/prod.yml` of [[rule-clean-branch]] writes `prod`, with the one deploy key whose private half is the secret `PROD_DEPLOY_KEY` (case 804). The workflow runs `uv run --project .guppi guppi test`, `uv run --project .guppi guppi check` and `uv run --project .guppi guppi style` on `windows-latest`, where the suite is known to run. It runs on each pull request by the event `pull_request`, never `pull_request_target`, so the code of a pull request reaches no secret. It also runs on each push to a branch other than `prod`. A run of a first-time contributor waits for the owner's approval. Only the owner pushes, by hand when the owner wants, by `! git push`; the one other push is that of the workflow of [[rule-clean-branch]] to `prod` (case 804). A session pushes nothing during a sprint, and a new sprint branch goes up at the owner's first push, after which the workflow runs on it. The owner's own pull request into `main` waits for `style` and `test` too, and the owner's bypass stays for a push the owner makes by hand. The rulesets and the approval are settings of the repository on GitHub, not files: a clone, a fork or an install of GUPPI does not carry them.

## History

- 2026-10-13 created · [[decision-case-794]]
- 2026-10-13 updated: the rule guards entity-guppi-repository, so a live page names it (case 795.1) · [[decision-case-795.1]]
- 2026-10-13 updated: deploy keys on the bypass list of prod, and the workflow of rule-clean-branch writes prod with the key of the secret PROD_DEPLOY_KEY (case 804) · [[decision-case-804.7]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
- 2026-10-15 reworded: `make style` → `uv run --project .guppi guppi style` · [[decision-case-820.7]]
