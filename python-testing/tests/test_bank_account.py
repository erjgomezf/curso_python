import unittest, os
from unittest.mock import patch
from datetime import datetime

from src.exceptions import withdrawTimeRestrictionsError, InsufficientFundsError
from src.bank_account import BankAccount


class BankAccountTest(unittest.TestCase):
    
    # Initialize a BankAccount instance before each test
    def setUp(self)-> None:
        self.account = BankAccount(balance=1000, log_file="transactions.txt")
    
    def tearDown(self) -> None:
        if os.path.exists("transactions.txt"):
            #None
            os.remove(self.account.log_file)
    
    def _count_lines(self, filename):
        with open(filename, 'r') as file:
            return len(file.readlines())
    
    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El saldo después del depósito debería ser 1500")
        
    def test_withdraw_decreases_balance_by_withdraw_amount(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El saldo después del retiro debería ser 800")
        
    def test_get_balance_returns_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, "El saldo debería ser 1000")
        
    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists(self.account.log_file), "El archivo de log de transacciones debería existir")
    
    def test_withdraw_logs_each_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1, "Se esperaba 1 transacción en el log")
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2, "Se esperaba 2 transacciones en el log")
    
    @unittest.expectedFailure
    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)


#**Reto**: Implementa y prueba un metodo para que no se puedan realizar retiros en fines de semana.

    @patch('src.bank_account.datetime')
    def test_withdraw_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday.return_value = 0  # Monday
        self.account.withdraw(100)

    @patch('src.bank_account.datetime')
    def test_withdraw_outside_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20
#        mock_datetime.now.return_value.weekday = 0  # Monday
        with self.assertRaises(withdrawTimeRestrictionsError):
            self.account.withdraw(100)
            
    @patch('src.bank_account.datetime')
    def test_withdraw_on_weekday(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday.return_value = 0  # Monday
        self.account.withdraw(100)
        
    @patch('src.bank_account.datetime')
    def test_withdraw_on_weekend(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday.return_value = 5  # Saturday
        with self.assertRaises(withdrawTimeRestrictionsError):
            self.account.withdraw(100)
    
    def test_deposit_multiple_ammounts(self):
        test_cases = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 1300, "expected": 2300},
            {"ammount": 3000, "expected": 4000}
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])
                