class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount()

while True:
    i = input("1 for deposit\n2 for withdraw\n3 for quit\n choose an action: ")
    if i == '1':
        amount = int(input("Enter the amount to deposit: "))
        account.deposit(amount)
        print("Deposit successful!")

    elif i == '2':
        amount = int(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
        print("Withdrawal successful!")
    elif i == '3':
        break
    else:
        print("Invalid input. Please try again.")

print(account.balance)