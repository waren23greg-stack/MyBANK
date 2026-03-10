import os
from datetime import datetime

ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as f:
            for line in f:
                name, balance = line.strip().split(",")
                accounts[name] = float(balance)
    return accounts

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        for name, balance in accounts.items():
            f.write(f"{name},{balance}\n")

def log_transaction(name, action, amount):
    with open(TRANSACTIONS_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} | {name} | {action} | ${amount:.2f}\n")

def create_account(accounts):
    name = input("Enter account name: ").strip()
    if name in accounts:
        print("Account already exists!")
    else:
        accounts[name] = 0.0
        save_accounts(accounts)
        print(f"Account '{name}' created successfully!")

def deposit(accounts):
    name = input("Enter account name: ").strip()
    if name not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter amount to deposit: $"))
    if amount <= 0:
        print("Amount must be positive!")
        return
    accounts[name] += amount
    save_accounts(accounts)
    log_transaction(name, "DEPOSIT", amount)
    print(f"Deposited ${amount:.2f} | New balance: ${accounts[name]:.2f}")

def withdraw(accounts):
    name = input("Enter account name: ").strip()
    if name not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter amount to withdraw: $"))
    if amount <= 0:
        print("Amount must be positive!")
        return
    if amount > accounts[name]:
        print("Insufficient funds!")
        return
    accounts[name] -= amount
    save_accounts(accounts)
    log_transaction(name, "WITHDRAWAL", amount)
    print(f"Withdrew ${amount:.2f} | New balance: ${accounts[name]:.2f}")

def check_balance(accounts):
    name = input("Enter account name: ").strip()
    if name not in accounts:
        print("Account not found!")
        return
    print(f"Balance for '{name}': ${accounts[name]:.2f}")

def view_transactions():
    name = input("Enter account name: ").strip()
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions yet!")
        return
    print(f"\n--- Transaction History for {name} ---")
    found = False
    with open(TRANSACTIONS_FILE, "r") as f:
        for line in f:
            if name in line:
                print(line.strip())
                found = True
    if not found:
        print("No transactions found for this account.")

def main():
    accounts = load_accounts()
    while True:
        print("\n===== MyBANK =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()