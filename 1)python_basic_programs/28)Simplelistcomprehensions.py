temps = [221, 234, 340, 230, -9999]
#if there is a value which can't be displayed then they can be ignored using if condition.
new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)

#Define a function that takes as a parameter a list that contains both integers  
# and strings and returns the list containing only the integers. 
# for example if i called your function with foo([99,'no data',95,94,'no data'])
#it should return [99,95,94]
def foo(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, int):
            new_lst.append(i)
    return new_lst

print(foo([99, 'no data', 95, 94, 'no data']))
#output is correct

#Define a functin that takes as parameter list of numbers and returns the list containing only the numbers that are greater than 0.
# for example, i called under function with foo([-5, 3, -1, 101]) it should return [3, 101].
def foo(letter):
    return[i for i in letter if i>0]

print(foo([-5, 3, -1, 101]))
#output is correct
