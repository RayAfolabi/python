class Bank:
    def __init__(self):
        self.minimum = 100
        self.balance = 1000
    def get_balance(self):
        return self.balance
    def withdraw(self, amount):
        if amount < self.minimum:
            print('No money for you')
        else:
            self.balance = self.balance - amount
            return amount


my_bank = Bank()
my_bank.withdraw(100)
balance = my_bank.get_balance()
print(balance)
my_bank.withdraw(50)
balance = my_bank.get_balance()
print(balance)