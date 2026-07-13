class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}.")

class InvalidUsernameError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

def validate_username(username):
    if len(username) < 3:
        raise InvalidUsernameError("Username must be at least 3 characters")

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)
    print(f"Tried to withdraw: {e.amount}")

try:
    validate_username("ab")
except InvalidUsernameError as e:
    print(e)
