#So if you are thinking how to add content to the file without overwriting it is you can check open function using help 
# If you use 'x' instead of 'w' then it wont overwrite the existing file 
# but the problem is it won't write at all if it is existing file it is only used for creating new files.
# So instead we use 'a' append to add the new content to the existing content of the file.
# 
with open("vegetables.txt",'a+') as myfile:
#also if you want to use read function after append then you have to use + after append 'a'    
    myfile.write("\nlemon")
    myfile.seek(0)
#this seek function is used to return the cursor to the top so that it won't display blank space instead of content.    
    content = myfile.read()
#if you won't use seek and just use read then it will display blank so that seek will return the cursor to the start
# so that the content can be displayed.
print(content)


#Read and Append 
# Append the text of bear1.txt to bear2.txt in other words,bear2txt should contain its text and the text of bear1.txt after that.

with open("bear1.txt",'r')as myfile:
    content=myfiles.read()
    
with open("bear2.txt",'a')as myfiles:
    myfiles.write(content)
 

#Copy n-times
#the existing content of data.txt looks like this:
# 1.3,1.5
# 2.3,2.7
# 
# Use python to modify the content looks like below:
#1.3,1.5
# 
with open("data.txt",'a+')as myfiles:
    myfiles.seek(0)
    content=myfiles.read(content)
    myfiles.seek(0)
    myfiles.write(content)
    myfiles.write(content)
    
# 
#
# Cheatsheet(fileprocessing)
# 
# you can read an existing file with python.
with open("file.txt") as file:
    content = file.read()
    
#you can append text to an existing file without overwriting it:
    with open("file.txt",'a') as file:
        content = file.write("Even more sample text")
        file.seek(0)
        content = file.read()
# 
# 
# 
# #
 