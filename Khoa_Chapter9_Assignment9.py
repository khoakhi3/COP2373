#Khoa Duong
#Assignment 9
#Create a program that defines a BankAcct class with methods to Initialize account info, adjust the interest rate, deposit money, withdraw money, check the balance, calculate interest based on a number of days, and display account details.

# Khoa Duong
# COP2374 – Assignment 9
# This program defines a BankAcct class with methods to initialize account info,
# adjust interest rate, deposit and withdraw money, check balance, calculate interest,
# and display account details using __str__. A test function demonstrates each feature.

# Define the BankAcct class to represent a bank account
class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        # Initialize account holder's name, account number, balance, and interest rate
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Adjust the interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit must be a positive amount.")

    # Withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Return the current balance
    def get_balance(self):
        return self.amount

    # Calculate interest earned based on number of days
    def calculate_interest(self, days):
        return self.amount * self.interest_rate * (days / 365)

    # Display account information and interest
    def __str__(self):
        interest_yearly = self.calculate_interest(365)
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest (1 year): ${interest_yearly:.2f}")


# Function to test the BankAcct class
def test_bank_acct():
    # Create a BankAcct object with initial values
    acct = BankAcct("Khoa", "A123456", 1000.00, 0.05)
    print("Initial account details:")
    print(acct)

    # Test deposit
    acct.deposit(200)
    print("\nAfter depositing $200:")
    print(acct)

    # Test withdrawal
    acct.withdraw(150)
    print("\nAfter withdrawing $150:")
    print(acct)

    # Adjust interest rate
    acct.adjust_interest_rate(0.10)
    print("\nAfter adjusting interest rate to 10%:")
    print(acct)

    # Show interest earned in 30 days
    interest_30_days = acct.calculate_interest(30)
    print(f"\nInterest earned in 30 days: ${interest_30_days:.2f}")

    # Show final balance
    print(f"Current balance: ${acct.get_balance():.2f}")


if __name__ == "__main__":
    test_bank_acct()
