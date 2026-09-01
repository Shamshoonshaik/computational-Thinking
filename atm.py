# ATM System using Computational Thinking

balance = 10000
correct_pin = 1234

print("===== ATM SYSTEM =====")

pin = int(input("Enter your PIN: "))

# Verify PIN
if pin == correct_pin:

    print("\nPIN Verified Successfully")
    print("\n1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    # Check Balance
    if choice == 1:
        print("\nYour Balance is: ₹", balance)

    # Withdraw Cash
    elif choice == 2:
        amount = int(input("Enter withdrawal amount: ₹"))

        if amount <= balance:
            balance = balance - amount
            print("\nPlease collect your cash.")
            print("Transaction Successful")
            print("Remaining Balance: ₹", balance)
        else:
            print("\nInsufficient Balance")

    # Deposit Cash
    elif choice == 3:
        amount = int(input("Enter deposit amount: ₹"))

        balance = balance + amount

        print("\nAmount Deposited Successfully")
        print("Updated Balance: ₹", balance)

    # Exit
    elif choice == 4:
        print("\nThank you for using the ATM.")

    else:
        print("\nInvalid Choice")

else:
    print("\nIncorrect PIN")
    print("Transaction Cancelled")


