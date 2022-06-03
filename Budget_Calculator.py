class Category():
    withdrawals = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = None):   # deposit money into the account   
        
        if description is None:
            description = ""

        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description= ""):  # withdraw money from the account
        if self.check_funds(amount) :       # if the account has enough funds, withdraw money from the account
            self.ledger.append({"amount": -amount, "description": description})
            self.withdrawals += amount
            return True

        else:
            return False

    def get_balance(self):  # get the balance of the account
        sum = 0
        for i in self.ledger:       # add the ledger amounts together
            sum += i["amount"]
        return sum

    def transfer(self, amount, wallet):   # transfer money from one account to another
        if self.check_funds(amount) : # if the account has enough funds, transfer money from one account to another
            self.withdraw(amount, f"Transfer to {wallet.name}")
            wallet.deposit(amount, f"Transfer from {self.name}")
            return True
        else: # if a description is provided
            return False

    def check_funds(self, amount):   # check if the account has enough funds
        balance = self.get_balance()
        if balance >= amount:
            return True
        else:
            return False

    def __repr__(self):
        temp = (30 - len(self.name))//2
        arr = []
        arr.append(temp*"*" + self.name + temp*"*"+"\n")
        for item in self.ledger:
            amount = '{0:.2f}'.format(item["amount"])
            temp1 = (23-len(item['description'])) * " "
            temp2 = (7-len(amount)) * " "
            arr.append(f"{item['description'][0:23]}{temp1}{temp2}{amount}\n")
        arr.append(f"Total: {round(self.get_balance(),2)}")
        return "".join(arr)


def create_spend_chart(categories):     # create a chart of the spendings

    category = Category
    total_spend = dict()
    sum_total_spend = 0

    for category in categories:
        total_spend[category.name] = category.withdrawals
        sum_total_spend += category.withdrawals  


    for key, value in total_spend.items():    # add the total spendings together
        total_spend[key] = value/sum_total_spend * 100


    row = "Percentage spent by category"  # add the title
        
    for i in range(100, -1, -10):
        row += f'\n{str(i).rjust(3)}|'
        for j in total_spend.values():
            if j > i:
                row += " o "
            else:
                row += "   "
        row += " "
                
    row += "\n    ----------\n"

    max_length = max(total_spend.keys(), key=len)

    for i in range(len(max_length)):
        row += " " * 4
        for name in total_spend.keys():
            if i < len(name):
                row += " " + name[i] + " "
            else:
                row += " " * 3
        row += " \n"

    row = row.rstrip() + " " * 2

    return row

entertainment = Category("Entertainment")
business = Category("Business")
food = Category("Food")
food.deposit(900, "Initial deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)



print(food)
#print(clothing)

print(create_spend_chart([business, food, entertainment]))

