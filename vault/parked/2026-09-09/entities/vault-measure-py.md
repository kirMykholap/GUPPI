---
title: "`scripts/vault-measure.py` — the only writer of a gauge's number, and what it refuses to write"
type: entity
status: current
authority: measure-writer-script
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-measure.py", "scripts/vault-measure-selftest.py"]
tags: [vault, harness, testing]
---

# What it is

**Appeared 2026-08-26.** The writer of the vault's `measure` regions, and the only thing in this
repository that writes a gauge's number. It is the build of
[[the-measure-writer-script-and-what-it-refuses-to-do]], on the owner's ruling that a script does
the mechanical work and the librarian reads its errors
([[a-gauge-is-written-by-a-script-that-runs-the-command]]).

| mode | what it does |
|---|---|
| write | takes `--page`/`--role`, plus `--subject`/`--command` for a gauge or `--value`/`--conditions` for testimony |
| `--refresh` | walks every region in the corpus, runs each gauge's command, and writes the reading beside it |
| `--check` | reads shape and **executes nothing** |

**Testimony appends and is never replaced. A gauge is replaced by subject.** The two roles differ
because a measurement made under stated conditions is a fact about a day, while a gauge is a
standing reading of one subject ([[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]]).

# The five refusals, each exiting 2

1. a slug nothing answers;
2. a slug two folders answer;
3. a gauge with no command, or with no subject;
4. testimony with no conditions;
5. a gauge subject another `current` page already carries
   ([[a-gauge-is-checked-for-uniqueness-and-the-check-waits-for-subjects]]).

**Exit 2 means a refusal here and also a usage error**, following `scripts/vault-archive.sh` and
against the gate, catalogue, coverage and authority scripts, which reserve 2 for a usage error
alone. That fork is why the gate rule reading this script reads lines rather than the exit code
([[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]).

# Its selftest, and the one case that proves the `--check` claim

**`scripts/vault-measure-selftest.py` — 59 cases in its own throwaway vault**, reported
`caught 59, missed 0` on 2026-08-26. Each of the five refusal guards was removed in turn and
reddened only its own cases: 2, 2, 1, 1, 2.

**One case proves `--check` executes nothing**, by giving a gauge a command that would create a file
and asserting the file does not exist afterwards, paired with `--refresh` creating it. That is the
shape a negative claim needs: an assertion that something did **not** happen is worth nothing unless
the paired positive is shown to happen ([[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]]).

# What it has not done yet

**`--refresh` has never written a number outside a fixture**, because no measure region exists in
the corpus. `uv run python scripts/vault-measure.py --check` read exit 0 over **0 regions** on
2026-08-26 — a clean run over an empty population, which is not evidence about the pass.

# What it parses, and the one defect its own cases caught

**The region's spelling is what this script reads**, and it is written down on a page of its own
because it exists in no other description
([[the-measure-regions-spelling-fences-the-command-in-backticks]]).

**Its bounds were one line short on the way in**, so the first measurement written into a region
landed outside it and `--refresh` walked past a gauge it could not see. Fourteen cases went red
together and located it
([[an-off-by-one-in-region-bounds-was-located-by-the-cases-that-went-red-together]]).

# It is the first Python script on the suite's sandbox copy list

The suite copies its scripts by name, and a gate rule that runs an uncopied script reddens every
clean case at once ([[a-gate-rule-that-runs-a-script-is-coupled-to-the-suites-sandbox-copy-list]]).
