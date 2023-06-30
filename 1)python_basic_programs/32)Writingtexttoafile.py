#you can even cut short the code from 31st file by using open functions read = 'r' or you can even create a new file using write 'w' 
with open("fruits.txt","r") as myfiles:
    content=myfiles.read()
    
print(content)

#write a new program using 'w' it can also overwrite the existing file which will erase the files in the file with new data.

with open("vegetables.txt","w") as myfiles:
    myfiles.write("tomato,brinjal")

#if want to write content in the file in different lines use \n
with open("vegetables.txt",'w') as myfiles:
    myfiles.write("Tomato\nbrinjal\ncucumber\nOnion\nGarlic")
    
#Reading and processing text
#read the bear.txt file, and print out the first 90 characters of its content.
#myfiles =open("bear.txt")
#contents=myfiles.read()
#print(contents[:90])

#Files processing inside function
#Define a function that gets a single string character and a filepath as parameters 
# and returns the number of occurences of that character in the life.

def foo(American,filepath="bear.txt"):
    file=open(filepath)
    content=file.read()
    return content.count(American)

#this function counts the number of times this word repeated in this program.

#Write first 90
#Create a first.txt file that contains the first 90 characters of bear.txt.

with open("bear.txt",'r') as myfile:
    content =myfile.read()
    
with open("bear.txt",'w') as myfile:
    file.write(content[:90])
    
#this extract its first 90 characters with python, and write those characters in first.txt with python.
