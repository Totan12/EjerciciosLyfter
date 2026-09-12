class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Monto depositado: {amount} ||  Balance general: {self.balance}")
        else:
            print("El monto a depositar tiene que ser mayor a cero.")

    def withdraw( self, amount):
        if amount > 0:
            self.balance -= amount
            print(f"Monto retirado: {amount} ||  Balance general: {self.balance}")
        else:
            print("El monto a retirar tiene que ser mayor a cero.")


class SavingsAccount(BankAccount):
    def __init__(self, balance,  min_balance):
        super().__init__(balance)
        self.min_balance = balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Error: No se puede retirar: {amount}. Su cuenta debe tener el mínimo requerido. ({self.min_balance}).")
        
        #Aqui estamos llamando a la funcion "PADRE".
        super().withdraw(amount)


