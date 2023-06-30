class Account:
    
    def __init__(self,filepath):
        #if you want to use an argument from __init__ function you just have to use self.argument.
        self.filepath=filepath
        #this enables it to use this in other functions.
        with open(filepath,'r') as file:
            self.balance=int(file.read())
            #the balance is instance variable.
    
    def withdraw(self,amount):
        self.balance=self.balance - amount
    
    def deposit(self,amount):
        self.balance=self.balance + amount
        
    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))
              
account=Account("Bank_account_class//Balance.txt")
# account.withdraw(100)
# account.deposit(300)     
print(account.balance)
account.commit()