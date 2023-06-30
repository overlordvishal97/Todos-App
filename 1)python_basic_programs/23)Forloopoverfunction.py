#Note that using loops, you can call any function multiple times, even your own functions. let's suppose we defined this function:
def celsius_to_kelvin(cels):
    return cels + 273.15
# That is a function that gets a number as input,adds 273.15 to it and returns the result. A for loop allows us to execute that function over a list of numbers:
monday_temperatures = [9.1, 8.8, -270.15]

for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))
    
# the output of that would be:
# 282.25
# 281.95
# 3.0
# so in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kevin(8.8) and in the third celsius_to_kelvin(-270.15).
#  
# That's just something keep in mind.
# 
# #