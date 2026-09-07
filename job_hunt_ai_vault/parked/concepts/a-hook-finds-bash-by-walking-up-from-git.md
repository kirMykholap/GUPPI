---
title: "A hook finds `bash` by walking up from `git`, because it cannot name it"
type: concept
status: current
authority: hook-bash-discovery
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/hooks/check-the-journal.ps1", "scripts/hook-selftest.ps1"]
tags: [agents, harness]
---

# The problem this machine sets

**`bash` on the system PATH is the WSL shim** in `WindowsApps`, and with no distro installed it
answers `execvpe(/bin/bash) failed`. **Git's bash is not on PATH at all.** A hook is spawned by the
OS rather than by an agent's shell, so it gets the broken one ([[session-hooks]]).

So a hook that has to run a `bash` script cannot call `bash`, and cannot have the path written into
it either: the answer differs per machine.

# The derivation

`.claude/hooks/check-the-journal.ps1` resolves `git`, then **walks up from its directory until a
`bin\bash.exe` appears**:

| layout | where `git` sits | levels up to `Git\bin\bash.exe` |
|---|---|---|
| this machine | `Git\mingw64\bin\git.exe` | three |
| a default install | `Git\cmd\git.exe` | two |

**Counting levels would have worked on one layout and been silent on the other** — which is the same
defect as an exception written by filename, one level down
([[a-journal-is-told-from-a-form-by-a-property-not-a-filename]]): naming an instance where a
property was available.

# Finding nothing, it says so

The hook prints **THE GATE DID NOT RUN**, and why, and what to run by hand. That branch is not
decoration: a guard that is silently absent is worse than none, and this project has shipped one
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). `scripts/hook-selftest.ps1`
exercises it by taking `git` off PATH — and that case had to be fixed before it proved anything,
because stripping PATH also stripped the interpreter it invoked by name
([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

# What `bash` on PATH actually is on this machine — 2026-08-29

**It is the WSL shim in `WindowsApps`.** A script invoked as bare `bash` from PowerShell here runs
**under a different operating system** — a different filesystem layout, different line endings on
anything it writes, and a `git` that is not the one the repository is checked out with.

**That is the concrete failure the walk-up avoids**, and it had not been written down: this page gave
the mechanism and the reason it cannot name a path, and never said what the wrong answer would have
been.

**`Find-Bash` in `.claude/hooks/vault-path.ps1` derives it from where `git` is**, and the suite's new
`--only` cases are its **third** caller ([[vault-scripts]]). A helper on its third caller is no longer
an implementation detail of one hook.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
