import unittest, os

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
        
    def test_withdraw_insufficient_funds(self):
        initial_balance = self.account.get_balance()
        new_balance = self.account.withdraw(2000)
        self.assertEqual(new_balance, initial_balance, "El saldo no debería cambiar al intentar retirar más de lo disponible")
