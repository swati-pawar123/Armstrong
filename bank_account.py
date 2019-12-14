class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, dept_amount):
        self.balance = self.balance + dept_amount
        print(f"Added {dept_amount} to the balance")

    def withdrawal(self, wd_amt):
        if self.balance > wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal accepted")
        else:
            print("You does not have enough fund")

    def __str__(self):
        return f"owner:{ } \n balance:{ }"


account = Account("abc", 1000)
print(account.deposite(100))
#print(account.withdrawal(500))


