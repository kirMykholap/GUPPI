---
title: "Docker Desktop — often not running, and the symptom does not say so"
type: entity
status: current
authority: docker-startup
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [process, architecture]
---

# Docker Desktop

**It is often not running.** The symptom is a path error rather than a plain "not running":

```
cannot find the path ... dockerDesktopLinuxEngine
```

Start it, then **poll `docker info` rather than sleeping blindly** — the engine comes up well after
the process does:

```powershell
Start-Process "$env:LOCALAPPDATA\Programs\DockerDesktop\Docker Desktop.exe"
```

The database and the app both live behind it: `docker compose up -d --build`.

It also owns one gap in cleanup — the startup sweep runs from `docker-entrypoint.sh`, so a bare
`uvicorn` never gets one. See [[sweep-runs-only-under-docker]] and [[app-restart-required]].

## The other way the container refuses to start: line endings

**`docker-entrypoint.sh` with CRLF breaks the container**, and the symptom names the entrypoint
rather than the line endings: `no such file or directory`. A `.gitattributes` with
`*.sh text eol=lf` is what holds it.

That defect sat in the repository from plan A and surfaced only much later, which is the part worth
keeping: **the documented way to start the project — through compose — did not work, and nothing
said so**, because the way people actually ran it at the time went around the entrypoint.
