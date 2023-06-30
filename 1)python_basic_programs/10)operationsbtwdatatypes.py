#list,strings and tuples have a positive index system:
#["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#   0     1     2     3     4     5     6
#  -7    -6    -5    -4    -3    -2    -1  negative indexing system
# In a list the 2nd,3rd and 4th items can be accessed with:
# data = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#days[:3]
#output:['Mon','Tue','Wed']

#Last three items of a list:
#days =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#days[-3:]
#output:['Fri','sat','sun']

#Everything but the last:
#days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#days[:-1]
#output:["Mon","Tue","Wed","Thu","Fri","Sat"]

#everything but the last two:
#days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#days[:-2]
#Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

#a single in a dictionary can be accessed using its key:
#phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
#phone_numbers["Marry Simpsons"]
#Output: '+423998200919'