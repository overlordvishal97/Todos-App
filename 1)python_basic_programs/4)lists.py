#list use square brackets
#RANGE 
#You can create a list of numbers automatically using a range. For example:

#list(range(1, 10))

#That will output:

#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#As you can see we just needed to specify the list boundaries inside range(). So, we specified 1and 10. Note that 10 is not included in the list. The generated list always runs up to one number before the upper number. In our example, it goes up to 9 since the upper number is 10.

#You can also specify a step as a third argument:

#list(range(1, 10, 2))

#That will output:

#1, 3, 5, 7, 9]

#So, the count happens every two items starting from 1 and ending at 9.

#lists use square brackets '[]'

#dir=directory

student_grades = [9.1,8.8,7.5]

mysum = sum(student_grades)
length = len(student_grades)    #len = builtin function
mean = mysum / length
print(mean)
 
#max function prints the max value of the object
#count function counts the specific number in the object 





student_grades = [9.1,8.]