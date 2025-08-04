class BankAccount:
    # Inicializa la cuenta bancaria con un saldo inicial
    def __init__(self, balance=0):
        self.balance = balance
        
    # Métodos para depositar, retirar y obtener el saldo
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Saldo insuficiente para retirar")
        return self.balance
    
    def get_balance(self):
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
    
if __name__ == "__main__":
    account1 = BankAccount(balance=1000)
    account2 = BankAccount(balance=500)
    
    account1.deposit(200)
    print(f"Account 1 balance after deposit: {account1.get_balance()}")
    account1.withdraw(3000)
    
    account1.transfer(3000, account2)
    print(f"Account 1 balance after transfer: {account1.get_balance()}")
    print(f"Account 2 balance after transfer: {account2.get_balance()}")