myfile =open("fruits.txt")
print(myfile.read())

#Read text from file and print
#on the side panel there's a bear.txt file. the existing code opens that file in read mode. 
#Below that code. please read the file content and print out the content.

#file = open("bear.txt")
#print(file.read())

#if you want to print the file many times then the usual print function wont work as you can only use read function once after the result will be an empty string.
#so inorder for it to work you have to save it in a variable then print it  and you can print it as many times as you want.
myfile =open("fruits.txt")
content = myfile.read()
#   |
# variable
print(content)
print(content)


#after the use close the file. it also clears the opened file in the temporary memory.

myfile = open("fruit.txt")
content = myfile.read()
myfile.close() 

print(content)

#the code above 23 to 25th line can be shortened using 'with'.
with open("fruits.txt") as myfiles:
    content = myfile.read()
        
print(content)

#you might be wondering where is close() function with the 'with' context managers the close function will be applied implicitly.

# if the file is in different directory then try using /(slash) after the directory name.