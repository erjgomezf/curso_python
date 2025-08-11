from datetime import datetime
from .exceptions import withdrawTimeRestrictionsError

class BankAccount:
    # Inicializa la cuenta bancaria con un saldo inicial
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction(f"Cuenta creada con saldo: {self.balance}")
        
    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(f"{message}\n")
        
    # Métodos para depositar, retirar y obtener el saldo
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Depósito realizado: {amount}, nuevo saldo: {self.balance}")
        return self.balance
    
    def validate_schedule_for_withdraw(self):
        now = datetime.now()
        weekday_now = int(now.weekday())
        if now.hour < 9 or now.hour >= 17 or weekday_now >= 5:
            raise withdrawTimeRestrictionsError("Los retiros solo se permiten entre las 9:00 y las 17:00 horas de lunes a viernes.")
        
        
    def withdraw(self, amount):
        self.validate_schedule_for_withdraw()
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self._log_transaction(f"Retiro realizado: {amount}, nuevo saldo: {self.balance}")
            return self.balance
        else:
            self._log_transaction("Saldo insuficiente para retirar")
            print("Saldo insuficiente para retirar")
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Diponible en cuenta: {self.balance}")
        return self.balance
    
    
    # Metodo para realizar una transferencia entre cuentas
    def transfer(self, amount, other_account):
        if amount > 0 and self.balance >= amount:
            self.withdraw(amount)
            other_account.deposit(amount)
            return True
        else:
            print("Saldo insuficiente para la transferencia")
        return False
    
'''
if __name__ == "__main__":
    account1 = BankAccount(balance=1000)
    print(account1.get_balance())
    
    #account2 = BankAccount(balance=500)
    
    account1.deposit(200)
    print(f"Account 1 balance after deposit: {account1.get_balance()}")
    #account1.withdraw(3000)
    
    #account1.transfer(3000, account2)
    #print(f"Account 1 balance after transfer: {account1.get_balance()}")
    #print(f"Account 2 balance after transfer: {account2.get_balance()}")
'''