class BankAccount:
    account_balance= 0
    def __init__(self, initial_balance=0) -> None:
        pass
    def deposit(self, amount):
        self.amount = amount
        self.account_balance += amount
        return self.account_balance
    def withdraw(self, amount):
        self.amount = amount
        if (self.account_balance - amount) >= 0:
            self.account_balance = self.account_balance - amount
    def display_balance():
        pass

