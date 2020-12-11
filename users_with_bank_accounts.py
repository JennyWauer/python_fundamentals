class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    # adding the deposit method
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self

    def display_user_balance(self):
        print('User: {}'.format(self.name))
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
        return self

class BankAccount:
    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funts: Charging a $5 fee')
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print('Balance: ${}'.format(self.balance))
        return self
    
    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance * self.int_rate)
        return self

jenny = User('Jenny', 'test@test.com')

zach = User('Zach', 'test2@test.com')

sam = User('Sam', 'test3@test.com')

jenny.make_deposit(5000).make_deposit(150).make_deposit(1000).make_withdrawl(1000).display_user_balance().transfer_money(zach, 1000)

zach.make_deposit(2000).make_deposit(1000).make_withdrawl(100).make_withdrawl(3000).display_user_balance()

sam.make_deposit(3000).make_withdrawl(1000).make_withdrawl(1000).make_withdrawl(150).display_user_balance()

# account1 = BankAccount(.05, 200)

# account2 = BankAccount(.1, 2000)

# account1.deposit(1000).deposit(150).deposit(250).withdrawl(200).yield_interest().display_account_info()

# account2.deposit(1000).deposit(3000).withdrawl(2000).withdrawl(20).withdrawl(1000).withdrawl(55).yield_interest().display_account_info()