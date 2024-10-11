# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print("Deposited: ${:.2f}".format(amount))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient funds exist."""
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                print("Withdrew: ${:.2f}".format(amount))
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print("Current Balance: ${:.2f}".format(self.account_balance))

if __name__ == "__main__":
    # This is just for testing the class independently.
    account = BankAccount(100)
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()

