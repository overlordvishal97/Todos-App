#a for-loop is useful to repeatedly execute a block of code.
#you can create a for-loop like so:
for letter in 'abc':
    print(letter.upper())
    
#output:A,B,C
#As you can see the for-loop repeatedly converted all the items of 'abc' to uppercase.
#the name after for (eg.letter) is just a variable name
#you can loop over dictionary keys as follows:
phone_numbers = {"John smith":"+37682929928","Marry simpsons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
    
#output:-John smith,Marry simpsons

#You can loop over dictionary values:

phone_numbers = {"John smith":"+37682929928","Marry simpsons":"+423998200919"}
for value in phone_numbers.values():
    print(value)

#output:-+37682929928,+423998200919

#We also have while-loops the code under a while-loop will run as long as the while-loop condition is true:

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
    
#the loop above will print out the string inside print() over and over again until the 20th of august 2090.    
