student_grades = {"Marry": 9.1,"Sim": 8.8,"John": 7.5}
for grades in student_grades.items():
    print(grades)

#Output would be in tuples as you know dictionary is made of keys and values if you want values replace items() with values or keys.
#('Marry', 9.1)
#('Sim', 8.8)
#('John', 7.5)
    
#Dictionary loop and string formatting
# you can combine a dictionary for loop with string formatting to create text containing information from the dictionary:
phone_numbers = {"John smith": "+37682929928","Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0],pair[1]))


# Another (better) way to do it::

phone_numbers = {"John smith": "+37682929928","Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

# In both cases the output is:
# John smith has as phone number +37682929928
# Marry simpsons has as phone number +423998200919

#Example 1 :-Loop over Dictionary and format (E)
# Make the code print out the following output using a for loop:
# John smith : +37682929928
# Marry simpsons: +423998200919
# so the code should loop over the dictionary items and in each iteration should print out the dictonary key, a colon, a space, and the corresponding value.
phone_numbers ={"John smith": "+37682929928","Marry simpsons":"+423998200919"}
for key,value in phone_numbers.items():
    print("{}: {}".format(key,value))

#Example 2:-Loop over Dictoinary and Replace 
# Loop over the phone numbers values and in each loop print out the phone number, but with '00' instead of '+' In other words, your code should output:
# 0037682929928
# 00423998200919
phone_numbers = {"John smith": "+37682929928","Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print(value.replace("+","00"))
# 
# 
# #