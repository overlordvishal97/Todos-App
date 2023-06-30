monday_temperatures = [9.1,8.8,7.6]

#if you want to round you have to use round from __builtin__ functions.
print(round(monday_temperatures[0]))
print(round(monday_temperatures[1]))
print(round(monday_temperatures[2]))
#if this had 100 objects then it would have been a 100 line code to make it short it can go upto
#two lines of code if we use for loop.
for temperature in monday_temperatures:
    print(round(temperature)) 
    
#for loop cut short the code in this list but it can also be used in the string.
# 
# Example 1:-Loop over the colors items and print out the item in every loop. so, the expected output of your code would be.
# 11,34,98,43,45,54,54
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)

#Example 2:-Loop over Big colors(E)
#Loop over the colors items and print out the item in every loop only if the item is greater than 50. so the output of your program would be: 
# 98,54,54
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    if color > 50:
        print(color)

#Example 3:-Loop over integer color(E) 
# Loop over the colors items and print out the item in every loop only if the item is an integer.so, the output of your program would be:
# 11,43,54,54
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color,int):
        print(color)
 
#Loop over int and big colors(E) 
# loop over the colors items and print out the item in every loop only if the item is an integer and it is greater than 50. so, the output of your program would be:
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if color > 50 and isinstance(color,int):
        print(color)
# 
# 
# 
