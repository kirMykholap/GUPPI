"""`guppi.toml` — guppi's one settings file, and the table of the languages it names.

The file is rendered in full from the `## Render` of `rule-guppi-config`; a change is an
`update` of that Render, and the governed-files hook refuses a hand edit. It sets two codes:
`documentation_lang`, the language of the repository, and `chat_lang`, the language of the
chat with the owner. `LANGUAGES` holds each code's name and script. `parse` judges a text of
the file: it must hold both keys, and each code must stand in the table; anything else is a
`ConfigError` that names its source (case 476.1).

The render reads the codes from the Render of `rule-guppi-config` by `parse`, never from
`guppi.toml`, which is its own output; the checks read `guppi.toml` by `read_settings`.
`outside` is the one judgment of a letter's script: the pre-spec finding of a name,
`context` or `problem` in another script imports it through `ratified.untranslated`
(case 476.3). A letter is a character `str.isalpha` accepts; its script is the first word of
its Unicode name, the way `LATIN SMALL LETTER A` and `CYRILLIC SMALL LETTER A` name theirs.
Inside a code span — the pattern `CODE_SPAN` of `guppi/lint.py`, imported, no pattern of its
own — a Latin letter is accepted as well, since a slug, a path or a field name is Latin in any
language; a letter of another script there is judged as in prose (case 589.1).
Rule page: `vault/wiki/rules/rule-guppi-config.md`.
"""

import tomllib
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from guppi.lint import CODE_SPAN

SETTINGS_FILE = "guppi.toml"
SETTINGS_PAGE = "rule-guppi-config"
KEYS = ("documentation_lang", "chat_lang")


@dataclass(frozen=True)
class Language:
    name: str
    script: str  # the first word of the Unicode name of each of its letters


LANGUAGES = {
    "ar": Language("Arabic", "ARABIC"),
    "de": Language("German", "LATIN"),
    "el": Language("Greek", "GREEK"),
    "en": Language("English", "LATIN"),
    "es": Language("Spanish", "LATIN"),
    "fr": Language("French", "LATIN"),
    "he": Language("Hebrew", "HEBREW"),
    "it": Language("Italian", "LATIN"),
    "pl": Language("Polish", "LATIN"),
    "pt": Language("Portuguese", "LATIN"),
    "ru": Language("Russian", "CYRILLIC"),
    "uk": Language("Ukrainian", "CYRILLIC"),
    "zh": Language("Chinese", "CJK"),
}


class ConfigError(Exception):
    pass


def parse(text: str, source: str) -> dict[str, str]:
    """Key → code for each of `KEYS`; a text that does not parse, a missing key or a code
    `LANGUAGES` does not hold is a `ConfigError` naming `source`."""
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"{source}: does not parse as TOML: {exc}") from exc
    settings: dict[str, str] = {}
    for key in KEYS:
        if key not in data:
            raise ConfigError(f"{source}: no key {key}")
        code = data[key]
        if not isinstance(code, str) or code not in LANGUAGES:
            raise ConfigError(f"{source}: {key} = {code!r} is not a language code guppi knows")
        settings[key] = code
    return settings


def read_settings(project_dir: Path) -> dict[str, str]:
    """The codes of `guppi.toml` at the root; a missing file is a `ConfigError` too."""
    path = Path(project_dir) / SETTINGS_FILE
    if not path.is_file():
        raise ConfigError(f"{SETTINGS_FILE}: missing")
    return parse(path.read_text(encoding="utf-8"), SETTINGS_FILE)


def name_of(code: str) -> str:
    return LANGUAGES[code].name


def script_of(code: str) -> str:
    """The script of a code, as a word: `Latin`, `Cyrillic`."""
    return LANGUAGES[code].script.capitalize()


def outside(text: str, code: str) -> bool:
    """True when `text` holds a letter outside the script of the language `code`. Inside a
    code span, read by `CODE_SPAN` of `guppi/lint.py`, a Latin letter is accepted too — a
    slug, a path or a field name is Latin in any language — and a letter of any other
    script is judged as in prose (case 589.1)."""
    script = LANGUAGES[code].script
    spans = {i for match in CODE_SPAN.finditer(text) for i in range(match.start(), match.end())}
    for i, char in enumerate(text):
        if not char.isalpha():
            continue
        of = unicodedata.name(char, "").split(" ", 1)[0]
        if of != script and not (i in spans and of == "LATIN"):
            return True
    return False
