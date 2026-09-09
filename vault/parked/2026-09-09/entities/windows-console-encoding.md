---
title: "The host console is cp1252, so any entry point printing Cyrillic must reconfigure stdout"
type: entity
status: current
authority: console-encoding
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md", ".claude/hooks/session-brief.ps1", ".claude/hooks/ask-the-vault.ps1"]
tags: [process, data]
---

# The host console is cp1252

Any **new** entry point that prints Cyrillic must begin with:

```python
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
```

Without it the CLI raises on its first Russian word. The product's console output is Russian by
policy — it is what the owner reads, not documentation — so this applies to every command that
speaks to him.

Related, and equally about what the environment does rather than what the code says: `uv` is on
PATH **since 2026-08-05** — `uv.exe` lives in the per-user scripts directory
(`%APPDATA%\Python\Python314\Scripts`), which was added to the user PATH — so commands are plain
`uv run ...`; `python -m uv run ...` is an equivalent fallback that works in any shell whatever its
PATH, which is why the empty-state hints on the page use the longer form — the owner may paste them
into an older terminal.

## The PowerShell half of the same rule

**Anything in PowerShell that reads or writes our files must set UTF-8 on both ends.** Windows
PowerShell reads and writes in the console codepage unless told otherwise, so the two halves are
separate settings and each has its own failure:

```powershell
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }   # writing
try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }   # reading stdin
$text = Get-Content -Raw -Encoding UTF8 -LiteralPath $file                   # reading a file
```

Without the output half, `.claude/hooks/session-brief.ps1` delivers the brief into a session's
context with every em dash and every Cyrillic word replaced by rubbish — **the brief is the first
thing a session reads, so the corruption is inherited by everything after it.** Verified by writing
a brief containing Cyrillic and comparing the bytes in and out; the case lives in
`scripts/hook-selftest.ps1`, which builds that text from character codes so the `.ps1` itself can
stay pure ASCII: **a `.ps1` without a BOM is read as the ANSI codepage**, which would make the test
file its own bug. `.claude/hooks/ask-the-vault.ps1` sets both, because it is handed JSON on stdin.

This is the same failure as `sys.stdout.reconfigure(encoding="utf-8")` in a Python entry point, on
a different interpreter, and the repository's `CLAUDE.md` points here for it.

**Why there is any PowerShell here at all is not taste**: the hooks are spawned by the OS, which
hands them the `bash` on the system PATH, and that one is broken on this machine — [[session-hooks]].

## One more trap of the same host shell

**`Invoke-WebRequest` without `-UseBasicParsing` fails in non-interactive PowerShell**, on the
attempt to initialise the IE engine. Anything scripted that fetches a URL from this host has to pass
the flag; interactive use hides the problem.
