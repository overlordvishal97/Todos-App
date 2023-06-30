#the function in the previous file which i created can be used for lists datatype but it can't be used for dict datatype so in order for it work we have to use if condition.
from turtle import st


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value)/len(value)
    
    return the_mean

monday_tempurature = [8.8, 9.1, 9.9]

student_grades = {"Marry":9.1,"Sim":8.8,"John":7.5}

print(mean(monday_tempurature))