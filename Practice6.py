class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")


account = BankAccount("Prasanna", 10000)

print(account.balance)

account.deposit(5000)
print(account.balance)

account.withdraw(2000)
print(account.balance)

account.withdraw(20000)
