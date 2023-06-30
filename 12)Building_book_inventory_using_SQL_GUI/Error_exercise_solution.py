# Exercise: Fixing a Bug in Our Program
# Exercise

# If you haven't already noticed, 
# the program has a bug. When the listbox is empty and the user clicks the listbox,
# an IndexError is generated in the terminal:
#
# 
# 
# 
# Why does this error happen?

# Well, everything starts with the user clicking on the listbox. Clicking the listbox executes the following code:

# list1.bind('<<ListboxSelect>>',get_selected_row) 

# That code calls the get_selected_row  function:

#def get_selected_row(event):
    # global selected_tuple
    # index=list1.curselection()[0]
    # selected_tuple=list1.get(index)
    # e1.delete(0,END)
    # e1.insert(END,selected_tuple[1])
    # e2.delete(0,END)
    # e2.insert(END,selected_tuple[2])
    # e3.delete(0,END)
    # e3.insert(END,selected_tuple[3])
    # e4.delete(0,END)
    # e4.insert(END,selected_tuple[4])

# Since the listbox is empty,  list1.curselection()  will be an empty list with no items. Trying to access the first item on the list with [0]  in line 3 will throw an error because there is no first item in the list. 

# # Try to fix that bug. The next lecture contains the solution.
# 

# Solution: Fixing a Bug in Our Program
# Solution

# def get_selected_row(event):
    #try:
        # global selected_tuple
        # index=list1.curselection()[0]
        # selected_tuple=list1.get(index)
        # e1.delete(0,END)
        # e1.insert(END,selected_tuple[1])
        # e2.delete(0,END)
    #     e2.insert(END,selected_tuple[2])
    #     e3.delete(0,END)
    #     e3.insert(END,selected_tuple[3])
    #     e4.delete(0,END)
    #     e4.insert(END,selected_tuple[4])
# except IndexError:
#             pass

# Explanation

# The error was fixed by simply implementing a try  and except block. When the get_selected_row  function is called,
# Python will execute the indented block under try . If there is an IndexError,
# none of the lines under try  will be executed; the line under except  will be executed, which is pass.
# The pass  statement means "do nothing". Therefore, the function will do nothing when there's an empty listbox.



#To give this program to a friend or share the program you have to change it to .exe file as lot of people don't know about programming
#change it so it looks like application and to do that you need a library called 'pyinstaller'
#And call the pyinstaller in the terminal and link it to the python file.
#for example. pyinstaller --onefile --windowed filename.py
#--onefile creates only one file as the name suggests so it would be clean to run but this will display a terminal of sorts so if you don't want that use '--windowed'.
#now that creates that .exe file.