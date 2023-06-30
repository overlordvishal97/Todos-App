#the if condtional works as is in list comprehension file but if you add else condition to the program it throws an error 
# so you have to rewrite the program to by adding the if and else condition to the front and for and in condition to the last.
temps = [221, 234, 340, 230, -9999]

#new_temps = [temp / 10 for temp in temps if temp != -9999]if you add else now it wont work it throws error 
# so you have to add it after moving the if condition to the front and then add the for loop.
new_temps = [temp / 10  if temp != -9999 else 0 for temp in temps]
print(new_temps)


#exercise 1:-
#Zeros instead
#Define a function that takes as parameter a list that contains both numbers and strigns and returns the same list but with zeros instead of strings. 
# for example, i called your function with foo([99, 'no data', 95, 'no data']) it should return [99,095,94,0]
def foo(nums):
    return [i if not isinstance(i,str) else 0 for i in nums]
print(foo([99, 'no data', 95, 94, 'no data']))

# output is correct.

#exercise 2:-
#Convert and sum up
#Define a function that takes as parameter a list that contains decimal numbers as strings and retunrs the sum of those numbers 
#for example, i called your function with foo(['1.2','2.6','3.3']) it should return 7.1. note that the floats of the input list are string datatypes.
def foo(nums):
    return sum([float (i) for i in nums])
print(foo(['1.2','2.6','3.3']))
#output is correct as it dispayed it as float.

