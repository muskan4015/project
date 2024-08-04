import time

print("Please insert your CARD")

time.sleep(5)  # Simulate card insertion time

# Initial settings
password = 1234  # Default PIN for ATM
balance = 5000  # Initial balance
transaction_history = []  # List to store transaction history

def log_transaction(transaction):
    """Logs a transaction to the transaction history."""
    transaction_history.append(transaction)

# Prompt user to enter their PIN
pin = int(input("Enter Your ATM Pin: "))

if pin == password:
    while True:
        # Display menu options
        print("""
            1 == Balance
            2 == Withdraw
            3 == Deposit
            4 == Change PIN
            5 == View Transaction History
            6 == Exit
        """)
        
        try:
            # Get user's choice
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if option == 1:
            # Display current balance
            print(f"Your current balance is {balance}")
        
        elif option == 2:
            # Withdraw funds
            try:
                withdraw_amount = int(input("Please enter the withdraw amount: "))
                if withdraw_amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"Your updated balance is {balance}")
                    log_transaction(f"Withdrew {withdraw_amount}")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif option == 3:
            # Deposit funds
            try:
                deposit_amount = int(input("Please enter the deposit amount: "))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account")
                print(f"Your updated balance is {balance}")
                log_transaction(f"Deposited {deposit_amount}")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif option == 4:
            # Change PIN
            try:
                new_pin = int(input("Enter your new PIN: "))
                confirm_pin = int(input("Confirm your new PIN: "))
                if new_pin == confirm_pin:
                    password = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PINs do not match. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif option == 5:
            # View transaction history
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions found.")
        
        elif option == 6:
            # Exit the ATM
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            # Handle invalid menu options
            print("Invalid option. Please choose a valid option.")
else:
    # Incorrect PIN handling
    print("Wrong PIN. Please try again.")
