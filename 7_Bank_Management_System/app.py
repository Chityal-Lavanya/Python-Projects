from datetime import datetime

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class Account:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name

        # Encapsulation
        self.__balance = balance

        self.transactions = []

        if balance > 0:
            self.transactions.append(
                f"Account created with ₹{balance:.2f}"
            )

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Deposit
    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than 0."
            )

        self.__balance += amount

        self.add_transaction(
            f"Deposited ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} deposited successfully.")

    # Withdraw
    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than 0."
            )

        if amount > self.__balance:
            raise InsufficientBalanceError(
                "Insufficient balance."
            )

        self.__balance -= amount

        self.add_transaction(
            f"Withdrawn ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} withdrawn successfully.")

    # Add transaction
    def add_transaction(self, message):

        time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.transactions.append(
            f"{time} - {message}"
        )

    # Display transaction history
    def show_transactions(self):

        print("\n===== TRANSACTION HISTORY =====")

        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print(transaction)

    # Display account details
    def display_account(self):

        print("\n===== ACCOUNT DETAILS =====")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.name)
        print(f"Balance        : ₹{self.__balance:.2f}")

class SavingsAccount(Account):

    def __init__(self, account_number, name, balance=0):
        super().__init__(
            account_number,
            name,
            balance
        )

        self.account_type = "Savings Account"

class Bank:

    def __init__(self):
        self.accounts = {}

    # Create account
    def create_account(self):

        account_number = input(
            "Enter account number: "
        ).strip()

        if account_number in self.accounts:
            print("Account already exists!")
            return

        name = input(
            "Enter account holder name: "
        ).strip()

        try:

            initial_deposit = float(
                input("Enter initial deposit: ")
            )

            if initial_deposit < 0:
                raise InvalidAmountError(
                    "Initial deposit cannot be negative."
                )

            account = SavingsAccount(
                account_number,
                name,
                initial_deposit
            )

            self.accounts[account_number] = account

            print("\nAccount created successfully!")

        except ValueError:
            print("Invalid amount! Please enter a number.")

        except InvalidAmountError as error:
            print(error)

    # Find account
    def find_account(self):

        account_number = input(
            "Enter account number: "
        ).strip()

        if account_number not in self.accounts:
            print("Account not found!")
            return None

        return self.accounts[account_number]

    # Deposit money
    def deposit_money(self):

        account = self.find_account()

        if account is None:
            return

        try:

            amount = float(
                input("Enter deposit amount: ")
            )

            account.deposit(amount)

        except ValueError:
            print("Invalid amount!")

        except InvalidAmountError as error:
            print(error)

    # Withdraw money
    def withdraw_money(self):

        account = self.find_account()

        if account is None:
            return

        try:

            amount = float(
                input("Enter withdrawal amount: ")
            )

            account.withdraw(amount)

        except ValueError:
            print("Invalid amount!")

        except InvalidAmountError as error:
            print(error)

        except InsufficientBalanceError as error:
            print(error)

    # Check balance
    def check_balance(self):

        account = self.find_account()

        if account is None:
            return

        print(
            f"Current Balance: ₹{account.get_balance():.2f}"
        )

    # Show transaction history
    def transaction_history(self):

        account = self.find_account()

        if account is None:
            return

        account.show_transactions()

# Main Program
bank = Bank()


while True:

    print("\n------------------------------")
    print("     BANK MANAGEMENT SYSTEM")
    print("--------------------------------")

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Account Details")
    print("7. Exit")

    choice = input(
        "\nEnter your choice: "
    ).strip()

    if choice == "1":

        bank.create_account()

    elif choice == "2":

        bank.deposit_money()

    elif choice == "3":

        bank.withdraw_money()

    elif choice == "4":

        bank.check_balance()

    elif choice == "5":

        bank.transaction_history()

    elif choice == "6":

        account = bank.find_account()

        if account:
            account.display_account()

    elif choice == "7":

        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice! Please select 1-7.")