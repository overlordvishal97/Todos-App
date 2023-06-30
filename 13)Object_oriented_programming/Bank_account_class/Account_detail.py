import sqlite3

class Account_Details:
    
    def __init__(self):
        self.conn=sqlite3.connect("balance.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY, amount)")
        self.conn.commit()
        #if you want to use an argument from __init__ function you just have to use self.argument.
        # self.filepath=filepath
        #this enables it to use this in other functions.
        # with open(filepath,'r') as file:
        #     self.balance=int(file.read())
            #the balance is instance variable.
    
    def withdraw(self,amount):
        self.conn=sqlite3.connect
        #self.balance=self.balance - amount
        self.cur.execute("SUBSTRACT FROM ACCOUNT BALANCE (NULL,?)",(amount))
        self.conn.commit()
        
    def deposit(self,amount):
        self.cur.execute("ADD INTO ACCOUNT BALANCE (NULL,?)",(amount))
        #self.balance=self.balance + amount
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
            
# account=Account("Bank_account_class//Balance.txt")
# account.withdraw(100)
# account.deposit(300)     
# print(account.balance)
# account.commit()
