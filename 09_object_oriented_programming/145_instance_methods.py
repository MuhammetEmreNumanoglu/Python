class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

    def get_balance(self):
        return self.balance

account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print("Final balance:", account.get_balance())
