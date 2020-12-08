class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print('User: {}, Balance: ${}'.format(self.name, self.account_balance))

    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)

jenny = User('Jenny', 'test@test.com')

zach = User('Zach', 'test2@test.com')

sam = User('Sam', 'test3@test.com')

jenny.make_deposit(5000)
jenny.make_deposit(150)
jenny.make_deposit(1000)
jenny.make_withdrawl(1000)
jenny.display_user_balance()
jenny.transfer_money(zach, 1000)

zach.make_deposit(2000)
zach.make_deposit(1000)
zach.make_withdrawl(100)
zach.make_withdrawl(3000)
zach.display_user_balance()

sam.make_deposit(3000)
sam.make_withdrawl(1000)
sam.make_withdrawl(1000)
sam.make_withdrawl(150)
sam.display_user_balance()