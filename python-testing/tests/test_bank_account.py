import unittest, os
from unittest.mock import patch
from datetime import datetime

from src.exceptions import withdrawTimeRestrictionsError
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
    
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El saldo después del depósito debería ser 1500")
        
    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El saldo después del retiro debería ser 800")
        
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, "El saldo debería ser 1000")
        
    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists(self.account.log_file), "El archivo de log de transacciones debería existir")
    
    def test_count_transactions(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1, "Se esperaba 1 transacción en el log")
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2, "Se esperaba 2 transacciones en el log")
    
    @unittest.expectedFailure
    def test_withdraw_insufficient_funds(self):
        new_balance = self.account.withdraw(1200)
        self.assertEqual(new_balance, -200, "El saldo deberia ser -200 al intentar retirar más de lo que hay en la cuenta")

    @patch('src.bank_account.datetime')
    def test_withdraw_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.account.withdraw(100)

    @patch('src.bank_account.datetime')
    def test_withdraw_outside_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20
        with self.assertRaises(withdrawTimeRestrictionsError):
            self.account.withdraw(100)
            
#**Reto**: Implementa y prueba un metodo para que no se puedan realizar retiros en fines de semana.
