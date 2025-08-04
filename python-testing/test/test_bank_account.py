import unittest

from src.bank_account import BankAccount


class BankAccountTest(unittest.TestCase):
    
    # Initialize a BankAccount instance before each test
    def setUp(self)-> None:
        self.account = BankAccount(balance=1000)
    
    # Test cases for BankAccount methods
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "Expected balance after deposit to be 1500")

    def test_withdraw(self):
        new_balance = self.account.withdraw(1200)
        self.assertEqual(new_balance, 1000, "Expected balance after withdrawal to be 800")
        
    def test_get_balance(self):
        balance = self.account.get_balance()
        self.assertEqual(balance, 1000, "Expected initial balance to be 1000")
        
    def test_transfer(self):
        other_account = BankAccount(balance=500)
        success = self.account.transfer(1200, other_account)
        self.assertTrue(success, "Expected transfer to be successful")