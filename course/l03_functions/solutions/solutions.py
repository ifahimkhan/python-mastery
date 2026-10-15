"""Reference answers for Level 03. Try the exercises first!

Each answer explains WHY it is written this way.
"""

from collections.abc import Callable

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
BINARY_BASE = 2


class FunctionsSolutions:
    # The default lives in the signature, so the body has nothing special to do.
    def greet(self, name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"

    # `numbers` is a tuple (maybe empty). Starting the total at 0 makes
    # total() == 0 work with no special case. (The built-in sum() does the same.)
    def total(self, *numbers: int) -> int:
        result = 0
        for n in numbers:
            result += n
        return result

    # **attributes keeps the order of the keyword arguments, so the output
    # order is predictable. Each pair becomes ` name="value"`.
    def make_tag(self, tag: str, text: str, **attributes: str) -> str:
        opening = tag
        for name, value in attributes.items():
            opening += f' {name}="{value}"'
        return f"<{opening}>{text}</{tag}>"

    # The bare * makes `upper` keyword-only: callers must write upper=True,
    # which reads far better than a mystery True at the end of the call.
    def format_name(self, first: str, last: str, *, upper: bool = False) -> str:
        full = f"{first} {last}"
        return full.upper() if upper else full

    # divmod returns (quotient, remainder). Returning three values really
    # returns one tuple, which callers can unpack: h, m, s = split_seconds(t).
    def split_seconds(self, total_seconds: int) -> tuple[int, int, int]:
        hours, rest = divmod(total_seconds, SECONDS_PER_HOUR)
        minutes, seconds = divmod(rest, SECONDS_PER_MINUTE)
        return hours, minutes, seconds

    # Base case: a single binary digit (0 or 1). Recursive case: the binary
    # of n // 2, followed by the last bit n % 2.
    def to_binary(self, n: int) -> str:
        if n < BINARY_BASE:
            return str(n)
        return self.to_binary(n // BINARY_BASE) + str(n % BINARY_BASE)

    # Euclid: gcd(a, b) == gcd(b, a % b), and gcd(a, 0) == a.
    # `self.` is how a method calls another method of the same object (level 06).
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)

    # The `| None` in the return type warns every caller to check the result.
    def safe_divide(self, a: float, b: float) -> float | None:
        if b == 0:
            return None
        return a / b

    # `func` is a value like any other: call it, then call it on the result.
    def apply_twice(self, func: Callable[[int], int], value: int) -> int:
        return func(func(value))

    # args is a tuple and kwargs a dict, so len() works on both.
    def count_args(self, *args: object, **kwargs: object) -> str:
        return f"{len(args)} positional, {len(kwargs)} keyword"
