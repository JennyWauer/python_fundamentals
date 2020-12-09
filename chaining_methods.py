class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print('User: {}, Balance: ${}'.format(self.name, self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
        return self

jenny = User('Jenny', 'test@test.com')

zach = User('Zach', 'test2@test.com')

sam = User('Sam', 'test3@test.com')

jenny.make_deposit(5000).make_deposit(150).make_deposit(1000).make_withdrawl(1000).display_user_balance().transfer_money(zach, 1000)

zach.make_deposit(2000).make_deposit(1000).make_withdrawl(100).make_withdrawl(3000).display_user_balance()

sam.make_deposit(3000).make_withdrawl(1000).make_withdrawl(1000).make_withdrawl(150).display_user_balance()