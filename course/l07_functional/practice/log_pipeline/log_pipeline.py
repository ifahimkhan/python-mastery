"""
=====================================================================
 PRACTICE 07.A - A lazy log pipeline
=====================================================================
 GOAL   : Analyse a server log with a chain of generators: split into
          lines, parse, filter by level, then summarise with Counter,
          groupby and itertools.
 RUN    : uv run python -m course.l07_functional.practice.log_pipeline.log_pipeline
 OUTPUT :
          parsed 9 of 11 lines
          by level: {'CRITICAL': 1, 'DEBUG': 1, 'ERROR': 3, 'INFO': 3, 'WARNING': 1}
          errors and worse:
            09:00:30 ERROR    payments card declined
            09:01:15 ERROR    db       connection lost
            09:01:16 ERROR    db       connection lost
            09:02:05 CRITICAL payments ledger out of sync
          noisiest services: [('payments', 2), ('db', 2)]
          problems per minute: {'09:00': 1, '09:01': 2, '09:02': 1}
          first critical at: 09:02:05
 DESIGN : Each stage is a small generator that takes an iterable and
          yields results, so stages can be tested alone and combined in
          any order. Nothing is stored until a summary needs it, so the
          same code works for a log of 5 lines or 5 million.
 EXTEND : Read the log from a real file (level 09): only read_lines()
          has to change.
=====================================================================
"""

import itertools
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from enum import IntEnum

TOP_SERVICES = 2
MINUTE_LENGTH = len("HH:MM")
FIELD_COUNT = 4

SAMPLE_LOG = """\
09:00:01 INFO auth user ada logged in
09:00:07 WARNING db slow query (812 ms)
09:00:30 ERROR payments card declined
this line is garbage
09:01:02 INFO auth user bo logged in
09:01:15 ERROR db connection lost
09:01:16 ERROR db connection lost
09:01:40 DEBUG cache hit ratio 0.93
09:02:05 CRITICAL payments ledger out of sync
09:02:09 INFO auth user cy logged out
09:02:30 BOGUS auth unknown level
"""


class Level(IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


@dataclass(frozen=True)
class Entry:
    time: str
    level: Level
    service: str
    message: str


def read_lines(text: str) -> Iterator[str]:
    for line in text.splitlines():
        if line.strip():
            yield line.strip()


def parse_line(line: str) -> Entry | None:
    """One line -> Entry, or None if the line is malformed."""
    parts = line.split(" ", FIELD_COUNT - 1)
    if len(parts) != FIELD_COUNT:
        return None
    time, level_name, service, message = parts
    if level_name not in Level.__members__:
        return None
    return Entry(time, Level[level_name], service, message)


def parse(lines: Iterable[str]) -> Iterator[Entry]:
    for line in lines:
        entry = parse_line(line)
        if entry is not None:
            yield entry


def at_least(level: Level, entries: Iterable[Entry]) -> Iterator[Entry]:
    return (entry for entry in entries if entry.level >= level)


def count_by_service(entries: Iterable[Entry]) -> Counter[str]:
    return Counter(entry.service for entry in entries)


def per_minute(entries: Iterable[Entry]) -> dict[str, int]:
    """Entries per HH:MM. Logs are in time order, so groupby needs no sort."""
    return {
        minute: sum(1 for _ in group)
        for minute, group in itertools.groupby(entries, key=_minute_of)
    }


def _minute_of(entry: Entry) -> str:
    return entry.time[:MINUTE_LENGTH]


def main() -> None:
    entries = list(parse(read_lines(SAMPLE_LOG)))  # list(): we summarise it 4 times
    total_lines = sum(1 for _ in read_lines(SAMPLE_LOG))
    print(f"parsed {len(entries)} of {total_lines} lines")

    by_level = Counter(entry.level.name for entry in entries)
    print("by level:", dict(sorted(by_level.items())))

    problems = list(at_least(Level.ERROR, entries))
    print("errors and worse:")
    for entry in problems:
        print(f"  {entry.time} {entry.level.name:<8} {entry.service:<8} {entry.message}")

    print("noisiest services:", count_by_service(problems).most_common(TOP_SERVICES))
    print("problems per minute:", per_minute(problems))

    first_critical = next(at_least(Level.CRITICAL, entries), None)
    print("first critical at:", first_critical.time if first_critical else "none")


if __name__ == "__main__":
    main()
