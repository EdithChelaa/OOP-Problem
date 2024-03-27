from wallet import create_user, deposit, withdraw, transfer, get_balance, delete_user_by_name,delete_user_by_id

def main():
    #initialize input descriptions
    while True:
        print("\nCrypto-Wallet CLI:")
        print("0. Create Account")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Balance Inquiry")
        print("5. Delete Account by Username")
        print("6. Delete Account by ID")
        print("7. Exit")

        #manage inputs
        choice = input("Enter your choice (0-7): ")
        if choice == "0":
            username = input("Enter a Username: ")
            password = input("Enter a new Password: ")
            create_user(username, password)
        elif choice == "1":
            username = input("Enter username: ")
            amount = float(input("Enter amount to deposit: "))
            password = input("Enter password: ")
            deposit(username, password, amount)
        elif choice == "2":
            username = input("Enter username: ")
            amount = float(input("Enter amount to withdraw: "))
            password = input("Enter password: ")
            withdraw(username, password, amount)
        elif choice == "3":
            sender = input("Enter sender's username: ")
            recipient = input("Enter recipient's username: ")
            amount = float(input("Enter amount to transfer: "))
            sender_password = input("Enter password: ")
            transfer(sender, recipient, sender_password, amount)
        elif choice == "4":
            username = input("Enter username: ")
            password = input("Enter password: ")
            get_balance(username, password)
        elif choice == "5":
            username = input("Enter username: ")
            password = input("Enter password: ")
            delete_user_by_name(username, password)
        elif choice == "6":
            user_id = int(input("Enter user ID: "))
            delete_user_by_id(user_id)
        elif choice == "7":
            print("Exiting Crypto-Wallet. Goodbye!")
            break
        else:
            print("Invalid choice!!! Please enter a number between 0 and 7.")

if __name__ == "__main__":
    main()
