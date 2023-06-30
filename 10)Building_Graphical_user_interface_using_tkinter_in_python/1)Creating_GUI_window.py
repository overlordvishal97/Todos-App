from tkinter import *

window = Tk()

def miles_to_km():
    print(e1_value.get())
    kms=float(e1_value.get())*0.62137
    t1.insert(END,kms)
    #this gives an error cause it can't multiply with an nonint as 
    # it is a float so inorder for it to work you have to convert the e1 to float.
    

b1=Button(window,text="Execute",command=miles_to_km)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
#this height is used to manipulate the size of the window  
# and width is used to manipulate the width.
t1.grid(row=0,column=2)
#you can use pack() for the button to work but grid() has more options.


window.mainloop()