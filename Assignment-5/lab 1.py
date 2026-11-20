class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display(self):
        print("Account holder:", self.name)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")

account = BankAccount(name)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display()

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
