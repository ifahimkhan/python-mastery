"""
=====================================================================
 LESSON 05.4 - Custom exceptions
=====================================================================
 GOAL   : Define your own exception types, group them under one base
          class, and give them extra data for the code that catches them.
 RUN    : uv run python -m course.l05_errors.lesson04_custom_exceptions.custom_exceptions
 OUTPUT :
          withdrew 30, balance 70
          InsufficientFundsError: need 50 more (balance 70, asked 120)
          shortfall attribute: 50
          AccountLockedError: account 'ACC-7' is locked
          caught by the base class: ['InsufficientFundsError', 'AccountLockedError']
 NOTE   : `class`, `__init__` and `super()` are level 06. Read the
          classes below as "a new kind of error, based on Exception".
 NEXT   : lesson05_eafp_lbyl/eafp_lbyl.py
=====================================================================
"""


# -- 1. CONCEPT: one base class for your module ---------------------------
# Callers can catch "anything that went wrong in banking" with ONE except.
class BankError(Exception):
    """Base class for every banking error."""


# -- 2. CONCEPT: a subclass per problem, with useful data ------------------
class InsufficientFundsError(BankError):
    def __init__(self, balance: int, amount: int) -> None:
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(f"need {self.shortfall} more (balance {balance}, asked {amount})")


class AccountLockedError(BankError):
    def __init__(self, account_id: str) -> None:
        self.account_id = account_id
        super().__init__(f"account {account_id!r} is locked")


def withdraw(balance: int, amount: int, *, locked: bool = False, account_id: str = "") -> int:
    if locked:
        raise AccountLockedError(account_id)
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


def main() -> None:
    balance = withdraw(100, 30)
    print("withdrew 30, balance", balance)

    try:
        withdraw(balance, 120)
    except InsufficientFundsError as error:
        print(f"{type(error).__name__}: {error}")
        print("shortfall attribute:", error.shortfall)  # data, not just text

    try:
        withdraw(balance, 10, locked=True, account_id="ACC-7")
    except AccountLockedError as error:
        print(f"{type(error).__name__}: {error}")

    caught = []
    for amount, locked in ((500, False), (1, True)):
        try:
            withdraw(balance, amount, locked=locked, account_id="ACC-7")
        except BankError as error:  # the base class catches both kinds
            caught.append(type(error).__name__)
    print("caught by the base class:", caught)

    # -- 3. WHY: names carry meaning -------------------------------------
    # `except InsufficientFundsError` says exactly what you handle. A
    # ValueError could come from anywhere (a typo in int(), a bad date...).
    # Attributes like shortfall let callers react without parsing messages.

    # -- 4. PITFALL: too many, too few, or the wrong base ------------------
    # - Don't create an exception class for every single function. Make one
    #   per thing a caller would handle differently.
    # - Inherit from Exception (or your own base), never from BaseException:
    #   that is reserved for things like Ctrl+C.
    # - End the name with "Error" (PEP 8), e.g. ConfigError, not BadConfig.

    # -- 5. TRY IT -----------------------------------------------------
    # a) Add DailyLimitError(BankError) with a `limit` attribute and raise it above 1000.
    # b) Catch BankError and print error.__class__.__mro__. What is the chain?
    # c) Make InsufficientFundsError ALSO inherit from ValueError. Who can catch it now?


if __name__ == "__main__":
    main()
