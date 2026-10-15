import pytest

from course.l06_oop.practice.bank_account.bank_account import (
    Account,
    AccountError,
    InsufficientFundsError,
    SavingsAccount,
    Transaction,
    TransactionKind,
    format_cents,
)


@pytest.mark.parametrize(
    ("cents", "text"),
    [(0, "0.00"), (5, "0.05"), (1999, "19.99"), (100_000, "1000.00"), (-5, "-0.05")],
)
def test_format_cents(cents: int, text: str) -> None:
    assert format_cents(cents) == text


def test_open_deposits_and_withdraws() -> None:
    account = Account.open("Ada", 5_000)
    account.deposit(1_000)
    account.withdraw(2_500)
    assert account.balance == 3_500
    assert [t.kind for t in account.history] == [
        TransactionKind.DEPOSIT,
        TransactionKind.DEPOSIT,
        TransactionKind.WITHDRAWAL,
    ]
    assert account.history[-1] == Transaction(TransactionKind.WITHDRAWAL, -2_500)


def test_withdrawing_everything_is_allowed() -> None:
    account = Account.open("Ada", 700)
    account.withdraw(700)
    assert account.balance == 0


def test_overdraw_raises_and_changes_nothing() -> None:
    account = Account.open("Ada", 1_000)
    with pytest.raises(InsufficientFundsError, match=r"only 10\.00 available") as caught:
        account.withdraw(1_001)
    assert (caught.value.available, caught.value.requested) == (1_000, 1_001)
    assert account.balance == 1_000
    assert len(account.history) == 1


@pytest.mark.parametrize("cents", [0, -1])
def test_amounts_must_be_positive(cents: int) -> None:
    account = Account("Ada")
    with pytest.raises(ValueError, match="must be positive"):
        account.deposit(cents)
    with pytest.raises(ValueError, match="must be positive"):
        account.withdraw(cents)


def test_owner_must_not_be_blank() -> None:
    with pytest.raises(ValueError):
        Account("  ")


def test_history_is_a_read_only_copy() -> None:
    account = Account.open("Ada", 100)
    assert isinstance(account.history, tuple)
    with pytest.raises(AttributeError):
        setattr(account, "balance", 1_000_000)  # noqa: B010 - mypy would refuse the plain form


def test_repr_shows_class_owner_and_balance() -> None:
    assert repr(Account.open("Bo", 1_234)) == "Account(owner='Bo', balance=12.34)"


def test_open_on_a_subclass_builds_the_subclass() -> None:
    savings = SavingsAccount.open("Bo", 20_000)
    assert type(savings) is SavingsAccount, "Hint: the classmethod uses cls(...), not Account(...)"
    assert savings.add_interest() == 200, "default rate is 1 %"


def test_savings_keeps_a_minimum_balance() -> None:
    savings = SavingsAccount("Ada", rate_basis_points=0)
    savings.deposit(15_000)
    assert savings.available() == 5_000
    savings.withdraw(5_000)
    with pytest.raises(AccountError):
        savings.withdraw(1)
    assert savings.balance == 10_000


def test_savings_available_is_never_negative() -> None:
    savings = SavingsAccount("Ada", rate_basis_points=0)
    savings.deposit(50)
    assert savings.available() == 0


def test_interest_rounds_down_to_whole_cents() -> None:
    savings = SavingsAccount("Ada", rate_basis_points=250)
    savings.deposit(12_345)  # 2.5 % of 123.45 = 3.08625
    assert savings.add_interest() == 308
    assert savings.balance == 12_653
    assert savings.history[-1].kind is TransactionKind.INTEREST


def test_zero_interest_adds_no_transaction() -> None:
    savings = SavingsAccount("Ada", rate_basis_points=100)
    savings.deposit(99)  # 1 % of 0.99 rounds down to 0
    assert savings.add_interest() == 0
    assert len(savings.history) == 1
