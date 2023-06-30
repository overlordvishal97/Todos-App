#define a function:
def cube_volume(a):
    return a*a*a

#write a conditonal block:
message = "hello there"
if "hello" in message:
     print("hi")
else:
    print("I dont understand")
    
#write a conditonal block of multiple conditions\
message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I dont understand")
    
#Use 'and' operator to check if both condtions are True at the same time:
x = 1
y = 1

if x == 1 and y == 1:
    print("yes")
else:
    print("No")
#output is yes since both x and y are 1.

#Use 'or' operator to check if at least one condition is True:
x = 1
y = 2
if x == 1 or y == 2:
    print("yes")
else:
    print("No")

#output is yes since x is 1.

#Check if a value is of a particular type with.
isinstance("abc",str)
isinstance([1,2,3],list)
print(isinstance("abc",str),isinstance([1,2,3],list))


#OR

type("abc") == str
type([1,2,3]) == list
print(type("abc") == str,type([1,2,3]) == list) 


































