def mainoops_basics():
    class student:                              #TASK 1    
        def __init__(self,name,grade):
            self.name=name
            self.grade=grade
        def study(self):
            print(self.name,"is studying")
            print(self.grade, "grade")
            
    s1=student("ashni","A")
    s2=student("manoj","A+")
    s1.study()
    s2.study()



    #TASK 2
    class BankAccount:
        def __init__(self,balance):
            self.balance=balance
        def deposit(self,amount):
            self.balance=self.balance+ amount
            print("amount deposited:",self.balance)
        def withdraw(self,amount):
            if amount>self.balance:
                return "insufficient balance"
            self.balance=self.balance-amount
            return f"withdraw successful {amount}"
        def check_balance(self):
            print("current balance",self.balance)
            
    balance = int(input("Enter starting balance: "))
    account = BankAccount(balance)        
    while True:
        print("\n 1.Deposit")
        print("2.withdraw")
        print("3.check_balance")
        print("4.exit")
        
        choice = int(input("enter the choice:"))
        if choice ==1:
            amount= int(input("enter the amount to deposit:"))
            account.deposit(amount)
        
        elif choice ==2:
            amount= int(input("enter the amount to withdraw:"))
            U= account.withdraw(amount)
            print(U)
            
        elif choice ==3:
            account.check_balance()
            
        elif choice ==4:
            print("thank you")
            break 

        else:
            print("invalid choice")
            

                