#lecture 207
#SQLite is a builtin module so no need to install it
#connecting a database requires five steps.they are step1.connect to database step2.create a cursor object
#step3.write an sql query step4.commit you changes to the database step5.close the connection.
import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
#a good practise is to use capital letters for sql keywords.
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
    
def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    #it is good practice to place the values in variables so that the user can give new values everytime.
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

#insert("Grape juice",10,5)
#indent cltr + [ and ctrl+]

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

update(11,7,"wine glass")
#delete("Grape juice")
print(view())
#rows is returned as python list.