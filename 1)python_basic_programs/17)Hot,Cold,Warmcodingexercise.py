#Hot,Warm and Cold
#Define a function that:
#1)takes a temperature as parameter 
#2)returns warm if the temperature is between 15 and 25 , including 15 and 25.
#3)returns cold if the temperature is less than 15.

def tempcontr(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"
print(tempcontr(14))

