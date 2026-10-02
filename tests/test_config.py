"""`guppi/config.py`: the settings of `guppi.toml` and the table of the languages.

Rule page: `vault/wiki/rules/rule-guppi-config.md`. The tests write a small `guppi.toml` in
a temp folder; nothing here touches the repository's own file.
"""

import pytest

from guppi import config

SETTINGS = '# guppi settings\ndocumentation_lang = "en"\nchat_lang = "ru"\n'


def test_the_table_names_each_code_and_its_script():
    assert config.name_of("en") == "English"
    assert config.name_of("ru") == "Russian"
    assert config.script_of("en") == "Latin"
    assert config.script_of("ru") == "Cyrillic"
    assert all(language.name and language.script for language in config.LANGUAGES.values())


def test_parse_gives_both_codes():
    assert config.parse(SETTINGS, "guppi.toml") == {"documentation_lang": "en", "chat_lang": "ru"}


@pytest.mark.parametrize("key", config.KEYS)
def test_a_missing_key_is_an_error_naming_the_source_and_the_key(key):
    text = "\n".join(line for line in SETTINGS.splitlines() if not line.startswith(key))
    with pytest.raises(config.ConfigError, match=f"guppi.toml: no key {key}"):
        config.parse(text, "guppi.toml")


def test_an_unknown_code_is_an_error_naming_the_source_and_the_key():
    text = SETTINGS.replace('"ru"', '"xx"')
    with pytest.raises(config.ConfigError, match="rule-guppi-config: chat_lang = 'xx'"):
        config.parse(text, "rule-guppi-config")


def test_a_text_that_is_not_toml_is_an_error():
    with pytest.raises(config.ConfigError, match="does not parse as TOML"):
        config.parse("documentation_lang = en\n", "guppi.toml")


def test_read_settings_reads_the_file_at_the_root(tmp_path):
    (tmp_path / "guppi.toml").write_text(SETTINGS, encoding="utf-8", newline="\n")
    assert config.read_settings(tmp_path)["chat_lang"] == "ru"


def test_read_settings_on_a_missing_file_is_an_error(tmp_path):
    with pytest.raises(config.ConfigError, match="guppi.toml: missing"):
        config.read_settings(tmp_path)


def test_outside_finds_a_letter_of_another_script():
    assert config.outside("a Case with один word", "en")
    assert not config.outside("A plain English line — with `code`, 42 and «quotes».", "en")
    assert not config.outside("Déjà vu, naïve", "en")
    assert config.outside("Русский текст with a Latin word", "ru")
    assert not config.outside("Русский текст — 42.", "ru")
    # inside a code span a Latin letter is accepted, any other judged as in prose (case 589.1)
    assert not config.outside("Русский текст про `rule-prespec` и `guppi/config.py`.", "ru")
    assert config.outside("An English line with `слово` in a code span.", "en")
    assert config.outside("Русский текст с `α` в коде.", "ru")
