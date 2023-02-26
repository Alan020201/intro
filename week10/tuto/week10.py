class BankAccount:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited')
        print(f'Your current balance is {self.balance}')
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount} withdrawn')
            print(f'Your current balance is {self.balance}')
        else:
            print(f'Insufficient balance')

# welcome message
print('Welcome to the bank')

# open account
name = input('Enter your name: ')
age = input('Enter your age: ')
address = input('Enter your address: ')

account = BankAccount(name, age, address)

# account options
while True:
    print('Select an option:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Exit')
    option = input()
    if option == '1':
        amount = int(input('Enter the amount to deposit: '))
        account.deposit(amount)
    elif option == '2':
        amount = int(input('Enter the amount to withdraw: '))
        account.withdraw(amount)
    elif option == '3':
        break
    else:
        print('Invalid option')
