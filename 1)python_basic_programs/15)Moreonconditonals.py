def mean(value):
    if isinstance(value,dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
        
    return the_mean
monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Marry": 9.1, "Sim":8.8, "John":7.5}

print(mean(student_grades))

#examples on conditionals
#1)what does the following code output?
x =-10
if x*2 > x:  
    print("greater") 
else:  
    print("less or equal")
#Ans Less or equal

#what would the following code output?
def foo(x,array):
    if x in array:
        return True
    else:
        return False
print(foo(1,[1,2,3]))
print(foo(1,[2,3]))
print(foo(1,['1',2,3]))
#Ans True 
#    False  
#    False

#what is true about the following code ?
if isinstance(x,int) or isinstance(x,float) or x=='1':
    print("valid type!")
else:
    print("Not valid!")
    
#Ans Valid type! because it meets one of the three conditions in line 1.

    