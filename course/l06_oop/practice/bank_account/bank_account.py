"""
=====================================================================
 PRACTICE 06.A - Bank accounts
=====================================================================
 GOAL   : Model bank accounts with a guarded balance, a read-only
          transaction history and a savings subclass with its own rules.
 RUN    : uv run python -m course.l06_oop.practice.bank_account.bank_account
 OUTPUT :
          Account(owner='Ada', balance=374.50)
          InsufficientFundsError: cannot withdraw 1000.00, only 374.50 available
          ValueError: amount must be positive, got -5
          interest added: 10.00
          may withdraw: 310.00
          InsufficientFundsError: cannot withdraw 350.00, only 310.00 available
          SavingsAccount(owner='Ada', balance=410.00)
          history:
            deposit      400.00
            interest      10.00
 DESIGN : Money is stored in whole cents (int), never float. The balance
          is a read-only property computed from immutable Transaction
          records, so it can't drift out of sync with the history.
          SavingsAccount overrides one check, not the whole withdraw().
 EXTEND : Add transfer(source, target, cents) that leaves BOTH accounts
          unchanged if the withdrawal fails.
=====================================================================
"""

from dataclasses import dataclass
from enum import Enum
from typing import Self

CENTS_PER_UNIT = 100
BASIS_POINTS = 10_000  # 1 basis point = 0.01 %
SAVINGS_MINIMUM = 10_000  # 100.00 must stay in a savings account
DEFAULT_SAVINGS_RATE = 100  # 1.00 %


class TransactionKind(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    INTEREST = "interest"


@dataclass(frozen=True)
class Transaction:
    kind: TransactionKind
    cents: int  # positive for money in, negative for money out


class AccountError(Exception):
    """Base class for every account problem."""


class InsufficientFundsError(AccountError):
    def __init__(self, available: int, requested: int) -> None:
        self.available = available
        self.requested = requested
        super().__init__(
            f"cannot withdraw {format_cents(requested)}, only {format_cents(available)} available"
        )


def format_cents(cents: int) -> str:
    """1999 -> "19.99", -5 -> "-0.05"."""
    sign = "-" if cents < 0 else ""
    units, rest = divmod(abs(cents), CENTS_PER_UNIT)
    return f"{sign}{units}.{rest:02d}"


class Account:
    def __init__(self, owner: str) -> None:
        if not owner.strip():
            raise ValueError("owner must not be empty")
        self.owner = owner
        self._transactions: list[Transaction] = []

    @classmethod
    def open(cls, owner: str, first_deposit: int) -> Self:
        """Alternative constructor: create the account and fund it in one step.

        `cls` is the class it was called on, so SavingsAccount.open(...) builds
        a SavingsAccount. `Self` says exactly that to mypy (more in level 08).
        """
        account = cls(owner)
        account.deposit(first_deposit)
        return account

    @property
    def balance(self) -> int:
        return sum(transaction.cents for transaction in self._transactions)

    @property
    def history(self) -> tuple[Transaction, ...]:
        return tuple(self._transactions)  # a copy: callers can't edit our list

    def deposit(self, cents: int) -> None:
        _require_positive(cents)
        self._transactions.append(Transaction(TransactionKind.DEPOSIT, cents))

    def withdraw(self, cents: int) -> None:
        _require_positive(cents)
        available = self.available()
        if cents > available:
            raise InsufficientFundsError(available, cents)
        self._transactions.append(Transaction(TransactionKind.WITHDRAWAL, -cents))

    def available(self) -> int:
        """How much may be withdrawn. Subclasses change this one rule."""
        return self.balance

    def __repr__(self) -> str:
        return f"{type(self).__name__}(owner={self.owner!r}, balance={format_cents(self.balance)})"


class SavingsAccount(Account):
    def __init__(self, owner: str, rate_basis_points: int = DEFAULT_SAVINGS_RATE) -> None:
        super().__init__(owner)
        self.rate_basis_points = rate_basis_points

    def available(self) -> int:
        return max(self.balance - SAVINGS_MINIMUM, 0)

    def add_interest(self) -> int:
        """Credit interest (rounded down to whole cents) and return it."""
        interest = self.balance * self.rate_basis_points // BASIS_POINTS
        if interest > 0:
            self._transactions.append(Transaction(TransactionKind.INTEREST, interest))
        return interest


def _require_positive(cents: int) -> None:
    if cents <= 0:
        raise ValueError(f"amount must be positive, got {cents}")


def main() -> None:
    checking = Account.open("Ada", 50_000)
    checking.withdraw(12_550)
    print(checking)

    try:
        checking.withdraw(100_000)
    except InsufficientFundsError as error:
        print("InsufficientFundsError:", error)

    try:
        checking.deposit(-5)
    except ValueError as error:
        print("ValueError:", error)

    savings = SavingsAccount("Ada", rate_basis_points=250)  # 2.50 %
    savings.deposit(40_000)
    print("interest added:", format_cents(savings.add_interest()))
    print("may withdraw:", format_cents(savings.available()))
    try:
        savings.withdraw(35_000)
    except AccountError as error:  # the base class catches every account problem
        print(f"{type(error).__name__}: {error}")
    print(savings)

    print("history:")
    for transaction in savings.history:
        print(f"  {transaction.kind.value:<10} {format_cents(transaction.cents):>8}")


if __name__ == "__main__":
    main()
