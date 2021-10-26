class BankAccount:
# Create a BankAccount class with the attributes interest rate and balance
# Add a deposit method to the BankAccount class
# Add a withdraw method to the BankAccount class
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class
# don't forget to add some default values for these parameters!
    # declaring a class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self,accountName,int_rate, balance=None): 
        self.int_rate = int_rate
        if balance is None:
            self.balance = 0
        else:
            self.balance = balance
        self.accountName=accountName
        BankAccount.all_accounts.append(self)
    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance +=amount
        return self
    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        self.balance -=amount
        return self
    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"{self.accountName} has a balance of $"+str(self.balance))
    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        self.balance += self.balance *self.int_rate
        return self
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

class User:
    # accounts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def createNewAccount(self,accountName):
        self.account=BankAccount(accountName,int_rate=0.02, balance=0)
    def getAccount(self,accountName):
        for account in BankAccount.all_accounts:
            if account.accountName==accountName:
                return account
        print(f"{accountName} is not exsited. Please try a different account name.")

# Create 3 accounts for 1 User
# Initial parameters 
# Create 1 user as an user class, create the user's 1st account, perfom few transactions, then display the account balance
UserName="Guido van Rossum"
UserEmail="guido@python.com"
UserAccountName="Account1"
guido=User(UserName, UserEmail)
guido.createNewAccount(UserAccountName)
guido.getAccount(UserAccountName).deposit(20).deposit(30).deposit(50).withdraw(10).yield_interest().display_account_info()

# Create 2nd account for the user
UserAccountName="Account2"
guido.createNewAccount(UserAccountName)
guido.getAccount(UserAccountName).deposit(200).withdraw(30).deposit(10).withdraw(10).yield_interest().display_account_info()

# Create 3rd account for the user
UserAccountName="Account3"
guido.createNewAccount(UserAccountName)
guido.getAccount(UserAccountName).deposit(200).withdraw(30).withdraw(100).withdraw(10).yield_interest().display_account_info()

# print the total combined balance in all 3 accounts for the user
print(f"{UserName}'s all accounts total balance is ${guido.account.all_balances()}")