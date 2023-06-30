#Warm or Cold(E)
#define a function that:
#1)takes a temperature as parameter2)returns warm if the temperature is greater than 7 3)returns cold if the temperature is equal or less than 7
#if i called you function with foo(10) it would return warm. if i called it with foo(7) or foo(5)

def Temp(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"
    
print(Temp(20))