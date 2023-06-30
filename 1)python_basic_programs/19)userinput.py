def weather_condition(temperature):
    if temperature > 21:
        return "Warm"
    else:
        return "Cold"
#you have to use float in order to get the output or else it will display that '>' this operator is not supported between 'str' and 'int' 
#and the number 21 is converted to 'str' by python so in order for it to work you have to convert it to float.    
user_input = float(input("Enter temperature:"))
print(weather_condition(user_input),type(user_input))
#type(user_input) which will display the type of datatype and you can the above statement by removing the flaot in the user_input function 
# in order to see if it really is 'str'.
#you can also change it to 'int' instead of 'float' if you like.
#but the 'int' can't convert 'float' into 'int' or 'string' it gets confused.
#'float' can convert both 'int' and 'string' into 'float' even 'float' into 'float'.
 