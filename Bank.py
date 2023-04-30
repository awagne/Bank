import Account

class Bank:

    accounts = []

    def __init__(self, accounts):
        self.accounts = accounts

    def createAccount(self):
        owner = input("Enter Account Name")
        accountType = input("Enter Account Type")
        account = Account(owner, accountType)
        self.accounts.append(account)

    def deleteAccount(self, accountNum):
        for account in self.accounts:
            if(account.getNum() == accountNum):
                self.accounts.remove(account)

    def display(self):
        for account in self.accounts:
            account.display()
            print("")