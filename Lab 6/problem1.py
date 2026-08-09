class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        print("Account details: ")
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("\nAfter deposit")
            print(f"Deposited: {amount}")
            print(f"New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("\nAfter withdraw")
            print(f"Withdrawn: {amount}")
            print(f"New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


# Creating a BankAccount object
account = BankAccount(
    "ACC1001",
    10000,
    "09-08-2026",
    "Samir"
)

# Account information
print("Account Number:", account.account_number)
print("Customer Name:", account.customer_name)
print("Date of Opening:", account.date_of_opening)

# Performing operations
account.check_balance()

account.deposit(5000)

account.withdraw(2000)

account.check_balance()