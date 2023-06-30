#Important points to know:-
# for loops end when the container is exhausted.
# While loops end when the condition is false.


username = ''

while username != "pypy":
    username = input("Enter username: ")

#Example 1:-
#what does the following code output?
a=0
while a < 5:
    a = a + 1
    print(a)

#output:-1,2,3,4,5 
#the loop continues until a is not less than 5 anymore.


#Example 2:-
#what will the following code output?
a = 10
while a > 0:
    x = a + 1
    print(x)

#output :- 11,11,11,11,11,...
# 

#While loop with break and continue.(this is more readable than the one on top it seems.)
while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue
# 
# 
# #