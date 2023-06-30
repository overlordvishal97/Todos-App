from tkinter import *
from Account_detail import Account_Details


account=Account_Details

#  def get_selected_row(event):
#      global selected_tuple
#      index=list1.curselection()[0]
#      selected_tuple=list1.get(index)
# #     e1.delete(0,END)
#     e1.insert(END,selected_tuple[1])
    
def deposit_command():
    # list1.delete(0,END)
    # for row in account.deposit(list1):
        # list1.insert(row)
        
def withdraw_command():
    
    
    # list1.delete(0,END)
    # for row in account.withdraw(selected_tuple[0]):
        # list1.delete(selected_tuple[0])
        
        
window=Tk()


window.wm_title("Account_Details")

l1=Label(window,text="Amount")
l1.grid(row=0,column=0)

#entries
amount_text=StringVar()
e1=Entry(window,textvariable=amount_text)
e1.grid(row=0,column=2)

list1=Listbox(window,height=6,width=35)
list1.grid(row=1,column=0,rowspan=6,columnspan=2)

#Scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#Scrollbar linked to list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# list1.bind('<<ListboxSelect>>',get_selected_row)
 
b1=Button(window,text="Deposit",width=12,command=deposit_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Withdraw",width=12,command=withdraw_command)
b2.grid(row=3,column=3)

window.mainloop()

        