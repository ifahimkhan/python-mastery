"""
=====================================================================
 LESSON 05.6 - Exception groups, except* and notes
=====================================================================
 GOAL   : Report SEVERAL errors at once with ExceptionGroup, handle
          each kind with except*, and add context with add_note().
 RUN    : uv run python -m course.l05_errors.lesson06_exception_groups.exception_groups
 OUTPUT :
          valid form: ok
          3 problems in the form:
            KeyError: 'name'
            ValueError: age must be a number, got 'abc'
            ValueError: email needs an @
          value problems: 2
          missing fields: 1
          note: while reading row 3
 NOTE   : ExceptionGroup and except* arrived in Python 3.11. You will
          meet them again with asyncio TaskGroups (level 11), where
          several tasks can fail at the same time.
 NEXT   : practice/config_parser/config_parser.py
=====================================================================
"""

REQUIRED_FIELDS = ("name", "age", "email")


# -- 1. CONCEPT: collect errors, then raise them together -------------------
# Stopping at the FIRST problem makes users fix a form one field at a time.
# Collect every problem and raise them as one ExceptionGroup instead.
def validate(form: dict[str, str]) -> None:
    problems: list[Exception] = []
    for field in REQUIRED_FIELDS:
        if field not in form:
            problems.append(KeyError(field))
    if "age" in form and not form["age"].isdecimal():
        problems.append(ValueError(f"age must be a number, got {form['age']!r}"))
    if "email" in form and "@" not in form["email"]:
        problems.append(ValueError("email needs an @"))
    if problems:
        raise ExceptionGroup("invalid form", problems)


def main() -> None:
    validate({"name": "Ada", "age": "36", "email": "ada@example.com"})
    print("valid form: ok")

    bad_form = {"age": "abc", "email": "ada.example.com"}
    try:
        validate(bad_form)
    except ExceptionGroup as group:
        # .exceptions holds every error inside the group.
        print(f"{len(group.exceptions)} problems in the form:")
        for error in sorted(group.exceptions, key=str):
            print(f"  {type(error).__name__}: {error}")

    # -- 2. CONCEPT: except* handles each KIND inside a group ------------
    # Every matching except* block runs (unlike plain except, where only
    # one does). Each one receives a smaller group with just its kind.
    try:
        validate(bad_form)
    except* ValueError as values:
        print("value problems:", len(values.exceptions))
    except* KeyError as missing:
        print("missing fields:", len(missing.exceptions))

    # -- 3. CONCEPT: add_note() adds context to any exception -------------
    try:
        try:
            int("x")
        except ValueError as error:
            error.add_note("while reading row 3")
            raise
    except ValueError as error:
        print("note:", error.__notes__[0])  # notes also show in the traceback

    # -- 4. WHY: one report instead of many round trips -------------------
    # Validating a whole form, checking every line of a config file or
    # running several tasks in parallel: all of these can fail in several
    # places at once, and the user deserves the full list.

    # -- 5. PITFALL: mixing except and except* --------------------------
    #   try: ...
    #   except ValueError: ...
    #   except* KeyError: ...
    #   # SyntaxError: cannot have both 'except' and 'except*' on the same 'try'
    # And a plain `except ValueError` does NOT catch a ValueError that sits
    # inside an ExceptionGroup: the group itself is what was raised.

    # -- 6. TRY IT -----------------------------------------------------
    # a) Add a check that name is not empty, and see it appear in the group.
    # b) Remove the except* KeyError block. What happens to the KeyError?
    # c) Add two notes to one exception and print error.__notes__.


if __name__ == "__main__":
    main()
