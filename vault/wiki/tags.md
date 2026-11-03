# Tags

The registry of tags in use. A tag enters this table from a tag line of a ratified Case, or
from a `{newtag:<tag>|<meaning>|<aliases>}` block of a lesson line that declares it with its
meaning and aliases; the librarian's run writes each row and invents none. The `aliases` column carries the Russian words a
question may use for the same subject, so a question in one language reaches a page in
another.

| tag | meaning | aliases (ru) |
|---|---|---|
| session | the working session: how it opens, what it loads, how it closes | сессия, старт сессии |
| hooks | Claude Code hook scripts and their events | хуки, хук |
| harness | the operational layer around the agent: hooks, skills, agents, settings | харнесс, обвязка |
| ledger | the chronological record of decisions, estimates and lessons | леджер, журнал решений |
| git | branch, status, pull: the repository's own state | гит, ветка |
| github | issues and anything else that lives on GitHub rather than in the vault | гитхаб, issues |
| workflow | the order of phases and steps a session follows | процесс, порядок работы |
| render | a Rule page whose body is written into a harness file by the renderer | рендер, генерация файла |
| librarian | the Documentation phase and its agent | библиотекарь |
| tests | the harness's own test suite, its fixtures and clocks | тесты |
| sprint | the sprint page, its backlog and its render | спринт |
| schema | the shape of a page category — its fields, their values and its sections | схема, схема страницы |
| orchestration | the main agent's own work in a session: the Frontier, the dispatch of case-guppi, the showing and signing of a Case, the defers | оркестрация, оркестровка |
| case-build | how case-guppi builds a Case: its rounds, its reading of the frame and the file it writes | сборка кейса, построение кейса |
| prespec | the check of the ratified Cases before the Spec: /pre-spec, its hook and its findings | пре-спек, проверка плана |
| readme | the README of the repository: what the project is, its parts and how to use it | ридми, описание проекта |
| ci | the continuous integration of the repository on GitHub: its runs, its checks and the branches it writes | CI, CI/CD, непрерывная интеграция |
| plugin | GUPPI as a Claude Code plugin: its clean version, its install and its use in another project | плагин |
| retro | the Retro phase: the review of the session's work against its ledger, the readings of Estimates, the lessons and the handoff | ретро, ретроспектива |
| box | /box: a later session running a conserved Spec on its own branch | бокс, законсервированный спек |
