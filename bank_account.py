class BankAccount():
    def __init__(self, name:str, account_number:int):
        self._name = name
        self._account_number = account_number
        self._balance = 0

    def deposit(self, amount):
        self._balance = self.balance + abs(amount)
    
    def withdraw(self, amount):
        if self._balance > 0:
            self._balance = self._balance - abs(amount)

    def balance(self):
        return self._balance