#! /user/local/bin/python3.4

class Action:
    # Initializer
    def __init__(self, actionType, amount):
        self.amount = amount
        if actionType == 'W' or actionType == 'D':
            self.actionType = actionType
        else:
            raise ValueError("actionType is not 'W' or 'D'")

class Client:
    # Initializer
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    #String Representation
    def __str__(self):
        rep = self.firstName + " " + self.lastName
        return rep

class Account:
    # Initializer
    def __init__(self, accountNumber, client, amount, minThreshold):
        self.accountNumber = accountNumber
        self.client = client
        self.amount = float(amount)
        self.minThreshold = float(minThreshold)

    # String Representation
    def __str__(self):
        if self.amount >= 0:
            amountstr = "$" + "{0:.2f}".format(self.amount)
        else:
            pos = self.amount * -1
            amountstr = "($" + "{0:.2f}".format(pos) + ")"
        rep = self.accountNumber + ", " + str(self.client) + ", Balance = " + amountstr
        
        return rep

    # performAction
    def performAction(self, action):
        if action.actionType == 'D':
            self.amount = self.amount + action.amount
            self.amount = round(self.amount, 2)
        elif action.actionType == 'W':
            after = self.amount - action.amount
            if after >= 0:
                self.amount = self.amount - action.amount
                self.amount = round(self.amount, 2)
                if self.amount < self.minThreshold:
                    self.amount = self.amount - 10
                    self.amount = round(self.amount, 2)
            else:
                raise ValueError("After withdrawal goes to negative amount.")

class Institute:
    # Initializer
    def __init__(self):
        self.accounts = {}

    # createNew
    def createNew(self, firstName, lastName, accountNumber):
        if accountNumber in self.accounts:
            pass
        else:
            newcli = Client(firstName, lastName)
            newacc = Account(accountNumber, newcli, 500, 1000)
            self.accounts[accountNumber] = newacc

    # performAction
    def performAction(self, accountNumber, action):
        if accountNumber not in self.accounts:
            pass
        else:
            self.accounts[accountNumber].performAction(action)

'''
if __name__ == "__main__":
    print("ACTION")
    act1 = Action('W', 3.5)
    print(act1.actionType)
    print(act1.amount)
    print("")
    print("CLIENT")
    cli1 = Client('John', 'Smith')
    print(str(cli1))
    print("")
    print("ACCOUNT")
    acc1 = Account("15487-79431", cli1, 21985, 1)
    print(str(acc1))
    acc1 = Account("15487-79431", cli1, -7645, 1)
    print(str(acc1))
    acc1 = Account("12345-67890", cli1, 10000, 3000)
    act1 = Action('W', 3000)
    acc1.performAction(act1)
    print(acc1)
    acc1.performAction(act1)
    print(acc1)
    print("")
    print("INSTITUTE")
    ins1 = Institute();
    print(ins1.accounts)
    ins1.createNew('ChulWoo', 'Park', '00279-99426')
    print(ins1.accounts)
    print(ins1.accounts['00279-99426'])
    print(ins1.accounts['00279-99426'].minThreshold)
    ins1.createNew('ChulWoo', 'Park', '00279-99426')
    print(ins1.accounts)
    act1 = Action('D', 10000)
    ins1.performAction('00279-99426', act1)
    print(ins1.accounts['00279-99426'])
'''
