class ATM:
    def __init__(self):
        self.balance = 0
        self.history = []

    def display_balance(self):
        print(f"Current balance: {self.balance:.2f}")

    def transaction_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            for transaction in self.history:
                print(transaction)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew {amount:.2f}")
            print(f"Withdrew {amount:.2f}")
            self.display_balance()

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited {amount:.2f}")
        print(f"Deposited {amount:.2f}")
        self.display_balance()

    def transfer(self, amount, target_account):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            target_account.deposit(amount)
            self.history.append(f"Transferred {amount:.2f} to account {id(target_account)}")
            print(f"Transferred {amount:.2f} to account {id(target_account)}")
            self.display_balance()

    def quit(self):
        print("Thank you for using the ATM. Goodbye!")

def main():
    atm = ATM()
    target_account = ATM()  # Another account for transfer demonstration

    while True:
        print("\nATM Menu:")
        print("1. Transaction History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            atm.transaction_history()
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '4':
            amount = float(input("Enter amount to transfer: "))
            atm.transfer(amount, target_account)
        elif choice == '5':
            atm.quit()
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()