import unittest, os

from faker import Faker

from src.user import User  # Assuming User is defined in src/user.py
from src.bank_account import BankAccount  # Assuming BankAccount is defined in src/bank_account.py


class UserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        
    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name_generated, email_generated)
        #print(f"Creando usuario con el nombre: {name_generated} y el correo: {email_generated}")
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)
        
