import pytest
from src.bank_account import BankAccount

def test_sum():
    a = 4
    b = 4
    assert a + b == 8

@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),
    (1300, 2300),
    (3000, 4000)
])
def test_deposit_multiple_ammounts(ammount,expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    
    new_balance = account.deposit(ammount)
    assert new_balance == expected
