"""
=====================================================================
 LESSON 02.2 - match: pattern matching
=====================================================================
 GOAL   : Pick one of many branches with match/case: literal values,
          several values with |, a catch-all _, and guards with if.
 RUN    : uv run python -m course.l02_control_flow.lesson02_match.match_statements
 OUTPUT :
          GET -> read
          DELETE -> remove
          PATCH -> unknown method
          sat -> weekend
          wed -> weekday
          404 -> client error
          503 -> server error
          200 -> success
          go north -> walking north
          quit -> bye
          dance -> I don't understand 'dance'
 NOTE   : `match` arrived in Python 3.10. It can also take apart lists,
          tuples and objects (levels 04 and 06).
 NEXT   : lesson03_ranges/ranges.py
=====================================================================
"""


def main() -> None:
    # -- 1. CONCEPT: match a value against literals --------------------
    # The first `case` that matches runs. `_` matches anything: the default.
    # (A for loop over a few values, so one example shows several cases: lesson 02.4.)
    for method in ("GET", "DELETE", "PATCH"):
        match method:
            case "GET":
                action = "read"
            case "POST":
                action = "create"
            case "DELETE":
                action = "remove"
            case _:
                action = "unknown method"
        print(f"{method} -> {action}")

    # -- 2. CONCEPT: several values with | ------------------------------
    for day in ("sat", "wed"):
        match day:
            case "sat" | "sun":
                kind = "weekend"
            case _:
                kind = "weekday"
        print(f"{day} -> {kind}")

    # -- 3. CONCEPT: capture + guard -----------------------------------
    # `case code if ...` captures the value into `code`, then checks the guard.
    for status in (404, 503, 200):
        match status:
            case 200 | 201 | 204:
                meaning = "success"
            case code if 400 <= code < 500:
                meaning = "client error"
            case code if code >= 500:
                meaning = "server error"
            case _:
                meaning = "other"
        print(f"{status} -> {meaning}")

    # -- 4. WHY: match reads like a table of commands -------------------
    # Splitting text into words and matching the pieces is where match shines.
    # split() gives a list (level 04); the pattern [first, second] takes it apart.
    for command in ("go north", "quit", "dance"):
        match command.split():
            case ["go", direction]:
                reply = f"walking {direction}"
            case ["quit"]:
                reply = "bye"
            case _:
                reply = f"I don't understand {command!r}"
        print(f"{command} -> {reply}")

    # -- 5. PITFALL: a bare name captures, it doesn't compare -----------
    #   QUIT = "quit"
    #   match command:
    #       case QUIT:        # SyntaxError: name capture 'QUIT' makes remaining
    #           ...           #              patterns unreachable
    # A bare name ALWAYS matches and stores the value. To compare with a
    # constant, use a dotted name (Commands.QUIT, an Enum in level 06) or a guard.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Add a case "PUT" | "PATCH" -> "update" above the default.
    # b) Add 301 and 302 as "redirect" to the status example.
    # c) Add a command ["take", item] that replies "you take the <item>".


if __name__ == "__main__":
    main()
