# ATM Interface in Python

This project is a simple ATM interface implemented in Python. The interface includes the following features:

1. Transaction History
2. Withdraw
3. Deposit
4. Transfer
5. Quit

## Features

### 1. Transaction History
- Displays a list of all transactions performed, including deposits, withdrawals, and transfers.

### 2. Withdraw
- Allows the user to withdraw a specified amount from their account.
- Checks for sufficient funds before processing the withdrawal.
- Displays the updated balance after the withdrawal.

### 3. Deposit
- Allows the user to deposit a specified amount into their account.
- Displays the updated balance after the deposit.

### 4. Transfer
- Allows the user to transfer a specified amount to another account.
- Checks for sufficient funds before processing the transfer.
- Displays the updated balance after the transfer.

### 5. Quit
- Exits the ATM interface and thanks the user for using the ATM.

## Code Explanation

### Class `ATM`
- `__init__`: Initializes the ATM with a balance of 0 and an empty transaction history.
- `display_balance`: Displays the current balance.
- `transaction_history`: Prints the transaction history. If no transactions have been made, it notifies the user.
- `withdraw`: Deducts the specified amount from the balance if sufficient funds are available and records the transaction. Displays the updated balance.
- `deposit`: Adds the specified amount to the balance and records the transaction. Displays the updated balance.
- `transfer`: Transfers the specified amount to another account if sufficient funds are available, records the transaction, and displays the updated balance.
- `quit`: Prints a goodbye message and exits the program.

### Function `main`
- Initializes an instance of the `ATM` class and another target account for transfer demonstration purposes.
- Provides a menu for the user to interact with the ATM.
- Processes the user's choice and performs the corresponding action by calling the appropriate methods in the `ATM` class.

## Usage

To run the ATM interface, simply execute the `main` function. The user can interact with the ATM through the console, making choices and entering amounts as needed.

### Example
```python
if __name__ == "__main__":
    main()
```

## How to Run

1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file, e.g., `atm_interface.py`.
3. Run the file using the command:
   ```sh
   python atm_interface.py
   ```
4. Follow the on-screen instructions to use the ATM interface.
