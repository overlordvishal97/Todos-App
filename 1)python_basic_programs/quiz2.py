"""
question 2
What would the following code output?

First, think of the answer without running the code on your IDE. Then, 
verify it by typing and running the code on your IDE and then select the correct answer.


"""

def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))