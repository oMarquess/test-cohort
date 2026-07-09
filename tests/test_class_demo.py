import pytest
from class_demo import BankAccount

def test_bank_account_initialization():
    account = BankAccount("Charlie", 150.0)
    assert account.owner == "Charlie"
    assert account.balance == 150.0
    assert str(account) == "Account owner: Charlie, Balance: $150.00"

def test_bank_account_default_balance():
    account = BankAccount("Dana")
    assert account.owner == "Dana"
    assert account.balance == 0.0

def test_bank_account_deposit():
    account = BankAccount("Charlie", 100.0)
    new_balance = account.deposit(50.0)
    assert new_balance == 150.0
    assert account.balance == 150.0

def test_bank_account_deposit_negative_value_error():
    account = BankAccount("Charlie", 100.0)
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(-10.0)

def test_bank_account_withdraw():
    account = BankAccount("Charlie", 100.0)
    new_balance = account.withdraw(40.0)
    assert new_balance == 60.0
    assert account.balance == 60.0

def test_bank_account_withdraw_insufficient_funds():
    account = BankAccount("Charlie", 100.0)
    with pytest.raises(ValueError, match="Insufficient funds."):
        account.withdraw(150.0)

def test_bank_account_withdraw_negative_value_error():
    account = BankAccount("Charlie", 100.0)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        account.withdraw(-5.0)
