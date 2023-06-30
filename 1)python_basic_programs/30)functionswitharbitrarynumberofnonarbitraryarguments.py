def mean(*args):
    return sum(args) / len(args)

print(mean(1,3,4))

#Average function
#define a function that takes an indefintite number of numbers as arguments and returns their average.
# if i called your function with foo(10,20,30,40) it should return the 25, the average of those numbers.
def foo(*args):
    return sum(args) / len(args)

print(foo(10,20,30,40))

#the output of the program is correct then the program is working as intended

#Indefinite number of strings processed
#define a function that takes strings in UPPERCASE and sorted alphabetically.
# for example, if i called your function with foo("snow","glacier","iceberg") it should return ["GLACIER", "ICEBERG","SNOW"] 

def foo(*args):
    args=[x.upper() for x in args]
    return sorted (args)
#sorted gives the value in ascending order.usually it would return ['SNOW', 'GLACIER', 'ICEBERG'] and with sorted it would return ['GLACIER', 'ICEBERG', 'SNOW'] 

print(foo("snow","glacier","iceberg"))

#Args is a nonkeyword argument.

def mean(**kwargs):
    return kwargs

print(mean(a=1,b=2,c=3))

#kwargs is keyword argument and it only works with arguments with keywords like 4 doesn't work it should be a=4 this a keyword argument.

#Indefinite number of keyword arguments.
#Enter the correct parameters inside fine_sum() so that the ouput of the code is 9.

def find_sum(**kwargs):
    return sum(kwargs.values())

print(find_sum(x=4,y=5))

#it gives correct output.