import unittest, os

from faker import Faker

from src.user import User  # Assuming User is defined in src/user.py
from src.bank_account import BankAccount  # Assuming BankAccount is defined in src/bank_account.py


class UserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        self.user = User(self.faker.name(), self.faker.email())
        
        
    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name_generated, email_generated)
        #print(f"Creando usuario con el nombre: {name_generated} y el correo: {email_generated}")
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)
        
    def test_user_with_multiple_account(self):
        
        
        for _ in range(3):
            bank_account = BankAccount(
                self.faker.random_int(min=1000, max=9999, step = 50),
                log_file = self.faker.file_name(extension='.txt')
            )
            
            self.user.add_account(account = bank_account)
            
        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(expected_value, value, "El saldo total del usuario debería ser igual a la suma de los saldos de sus cuentas")
        
    def tearDown(self) -> None:
        for account in self.user.accounts:
            os.remove(account.log_file)