class BankAccount :
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
         self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.balance}")

person1 = BankAccount("Prasanna", 123456789, 1000)
person1.deposit(1000)
person1.withdraw(-500)
person1.display_balance()
