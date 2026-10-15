"""
=====================================================================
 PRACTICE 05.A - Config file parser
=====================================================================
 GOAL   : Parse "key = value" lines, report EVERY bad line with its
          line number in one go, and read typed values safely.
 RUN    : uv run python -m course.l05_errors.practice.config_parser.config_parser
 OUTPUT :
          settings: {'host': 'localhost', 'port': '8080', 'debug': 'yes'}
          port: 8080
          timeout: 30 (default)
          debug: True
          3 errors in the bad config:
            line 2: expected 'key = value', got 'this line has no separator'
            line 3: missing key before '='
            line 5: duplicate key 'port'
          typed read failed: port must be a whole number, got 'eighty'
 DESIGN : ConfigError carries the line number as data. parse_config()
          collects all errors and raises them as one ExceptionGroup, so
          the user can fix the whole file at once.
 EXTEND : Support [sections] that prefix keys, e.g. "server.port".
=====================================================================
"""

COMMENT = "#"
SEPARATOR = "="

GOOD_CONFIG = """\
# server settings
host = localhost
port = 8080

debug = yes
"""

BAD_CONFIG = """\
host = localhost
this line has no separator
= no key here
port = 80
port = 8080
"""


class ConfigError(Exception):
    """A problem in the config. ``line_number`` is None when no line is involved."""

    def __init__(self, message: str, line_number: int | None = None) -> None:
        self.line_number = line_number
        prefix = "" if line_number is None else f"line {line_number}: "
        super().__init__(prefix + message)


def parse_line(line_number: int, line: str) -> tuple[str, str] | None:
    """(key, value) for a setting, None for blank lines and comments."""
    stripped = line.strip()
    if not stripped or stripped.startswith(COMMENT):
        return None
    if SEPARATOR not in stripped:
        raise ConfigError(f"expected 'key = value', got {stripped!r}", line_number)
    key, value = stripped.split(SEPARATOR, 1)  # split at the FIRST = only
    key, value = key.strip(), value.strip()
    if not key:
        raise ConfigError("missing key before '='", line_number)
    return key, value


def parse_config(text: str) -> dict[str, str]:
    """All settings. Raises ExceptionGroup of ConfigError if any line is bad."""
    settings: dict[str, str] = {}
    errors: list[ConfigError] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        try:
            parsed = parse_line(line_number, line)
        except ConfigError as error:
            errors.append(error)
            continue
        if parsed is None:
            continue
        key, value = parsed
        if key in settings:
            errors.append(ConfigError(f"duplicate key {key!r}", line_number))
            continue
        settings[key] = value
    if errors:
        raise ExceptionGroup("invalid config", errors)
    return settings


def get_int(settings: dict[str, str], key: str, default: int) -> int:
    """The setting as an int, the default if it's missing, ConfigError if it's not a number."""
    if key not in settings:
        return default
    try:
        return int(settings[key])
    except ValueError as error:
        raise ConfigError(f"{key} must be a whole number, got {settings[key]!r}") from error


def get_bool(settings: dict[str, str], key: str, default: bool) -> bool:
    value = settings.get(key)
    if value is None:
        return default
    match value.lower():
        case "yes" | "true" | "on" | "1":
            return True
        case "no" | "false" | "off" | "0":
            return False
        case _:
            raise ConfigError(f"{key} must be yes or no, got {value!r}")


def main() -> None:
    settings = parse_config(GOOD_CONFIG)
    print("settings:", settings)
    print("port:", get_int(settings, "port", 80))
    print("timeout:", get_int(settings, "timeout", 30), "(default)")
    print("debug:", get_bool(settings, "debug", False))

    try:
        parse_config(BAD_CONFIG)
    except ExceptionGroup as group:
        print(f"{len(group.exceptions)} errors in the bad config:")
        for error in group.exceptions:
            print(" ", error)

    try:
        get_int({"port": "eighty"}, "port", 80)
    except ConfigError as error:
        print("typed read failed:", error)


if __name__ == "__main__":
    main()
