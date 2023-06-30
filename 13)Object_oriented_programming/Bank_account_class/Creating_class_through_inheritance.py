class Account:
#Baseclass.
#class which is blueprint or you can call it a prototype that defines the characteristics of an object that is about to be created.
    
    def __init__(self,filepath):
        #instance variables are accesseble by object instance.
        #if you want to use an argument from __init__ function you just have to use self.argument.
        self.filepath=filepath
        #this enables it to use this in other functions. or it will give error or it says not defined.
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
            
#creating new class which is subclass
#inheritance is creating a subclass of a baseclass.
#this subclass shares the methods of the base class plus it has its own methods.
#that are specific to the subclass.
class Checking(Account):
#Subclass.
#Doc string.
    """This class generates checking account objects."""
#class variable.
    
    #datamember.
    type="checking"
    #this is inheritance syntax"(Account)".
    
    #this is also a method its a special method so it is constructor.
    def __init__(self, filepath, fee):
        Account.__init__(self,filepath)
        self.fee=fee
    
    #class method.    
    def transfer(self, amount):
        self.balance=self.balance- amount- self.fee
        
#instantiation.
vishals_checking=Checking("Bank_account_class//vishal.txt",1)
#that 1 is fee of the transfer.
# checking.deposit(109)
vishals_checking.transfer(100)
#the tranfer fee also getting cut with the transfer amount.
print(vishals_checking.balance)
vishals_checking.commit()

#instantiation.
richards_checking=Checking("Bank_account_class//richard.txt",1)
richards_checking.transfer(100)
print(richards_checking.balance)
print(richards_checking.type)
#attribute are 'type'
print(richards_checking.__doc__)