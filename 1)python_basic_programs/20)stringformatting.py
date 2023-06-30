user_input = input("Enter your name: ")
#this program is used in python 3.3 or below because in some webservers contain python 2 installed so in order for our program to work which should write it like this.
message = "Hello %s!" % user_input
# %s is a special string ^.
#the program below is run in python 3.6 or above because it looks more readable.
message = f"Hello {user_input}"
print(message)

#String formatting with multuple variables.
name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today" 
#To increase the statements in the string formating you just have to add a statement like above.
message ="Hello %s %s" % (name,surname)
#you have to increase the spaceholder(%s) so that it can accomodate surname as well.
message = f"Hello {name} {surname}, Whats up {when}"
#before this there was user_input in the place of name then it would give an error as there is no varaible as 'user_input'.
#inorder to resolve it you just have to change it into the variable which is present in the program.
#you can add more statements to the variable. 
print(message)                  