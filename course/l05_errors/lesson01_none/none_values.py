"""
=====================================================================
 LESSON 05.1 - None: the absence of a value
=====================================================================
 GOAL   : Use None to mean "no value", test for it with `is None`,
          and avoid confusing None with other falsy values like 0.
 RUN    : uv run python -m course.l05_errors.lesson01_none.none_values
 OUTPUT :
          result: None  type: <class 'NoneType'>
          find_user(1) = Ada
          find_user(9) = None
          user 9 not found
          Ada Lovelace
          Ada King Lovelace
          discount None -> price 100
          discount 0 -> price 100
          discount 10 -> price 90
          with or: 50 (wrong, 0 was replaced!)
          with is None: 0
 NEXT   : lesson02_exceptions/exceptions.py
=====================================================================
"""

USERS = {1: "Ada", 2: "Linus"}
DEFAULT_VOLUME = 50


def do_nothing() -> None:
    pass  # a function without `return` gives back None


def find_user(user_id: int) -> str | None:
    return USERS.get(user_id)  # None when the id is missing


def full_name(first: str, last: str, middle: str | None = None) -> str:
    if middle is None:
        return f"{first} {last}"
    return f"{first} {middle} {last}"


def apply_discount(price: int, percent: int | None) -> int:
    if percent is None:  # "no discount given"
        return price
    return price - price * percent // 100


def main() -> None:
    # -- 1. CONCEPT: None is a value meaning "nothing here" -----------------
    # There is exactly ONE None object; its type is NoneType.
    result = do_nothing()  # type: ignore[func-returns-value]
    print("result:", result, " type:", type(result))

    # -- 2. CONCEPT: X | None and `is None` ------------------------------
    print("find_user(1) =", find_user(1))
    print("find_user(9) =", find_user(9))
    user = find_user(9)
    if user is None:  # `is`, because there is only one None
        print("user 9 not found")

    # None as a default means "the caller didn't say":
    print(full_name("Ada", "Lovelace"))
    print(full_name("Ada", "Lovelace", middle="King"))

    # -- 3. WHY: None is different from 0 -----------------------------------
    # "No discount" (None) and "a discount of 0 %" are different ideas,
    # even though both leave the price alone here.
    for percent in (None, 0, 10):
        print(f"discount {percent} -> price {apply_discount(100, percent)}")

    # -- 4. PITFALL: `or` treats 0, "" and [] like None ------------------
    chosen_volume = 0  # the user turned the sound off on purpose
    print(f"with or: {chosen_volume or DEFAULT_VOLUME} (wrong, 0 was replaced!)")
    volume = DEFAULT_VOLUME if chosen_volume is None else chosen_volume
    print("with is None:", volume)

    # Other None pitfalls:
    #   if user == None:      # works, but `is None` is the correct test
    #   len(find_user(9))     # TypeError: object of type 'NoneType' has no len()
    #   find_user(9).upper()  # AttributeError: 'NoneType' object has no attribute 'upper'
    # mypy catches the last two: 'Item "None" of "str | None" has no attribute "upper"'.

    # -- 5. TRY IT -----------------------------------------------------
    # a) Write first_even(numbers) -> int | None.
    # b) Call full_name("Ada", "Lovelace", "King") and print it.
    # c) Print None == 0, None is None and bool(None).


if __name__ == "__main__":
    main()
