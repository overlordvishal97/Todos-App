#'{}'brackets if you want to use the dictionary data type
#dictionary is made of key and value pair

student_grade = [9.1,8.8,7.5]
student_grades = {"Marry": 9.1,"sim": 8.8, "John": 7.5 }

mysum = sum(student_grades)
length = len(student_grades)    
mean = mysum / length
print(mean)

#keys function in dict prints only keys of the dictionary when used 
#example (student_grades.keys())
#values function in dict prints only values of the dictionary when used
#example (student_grades.values())