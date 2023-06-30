#Section 24
#lecture 207
#SQLite is a builtin module so no need to install it
#connecting a database requires five steps.they are step1.connect to database step2.create a cursor object
#step3.write an sql query step4.commit you changes to the database step5.close the connection.
import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
#a good practise is to use capital letters for sql keywords.
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
    
def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    #it is good practice to place the values in variables so that the user can give new values everytime.
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')"% (item,quantity,price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    #it works but this string formatting is risky to use('%s').so we made the new one and commented the old one out.
    conn.commit()
    conn.close()

#insert("Grape juice",10,5)
#indent cltr + [ and ctrl+]

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Orange",10,15)
update(20,25,"Apple")
#delete("Orange")
print(view())
#rows is returned as python list.