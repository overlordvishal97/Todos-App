#password controller (E)
#define a function that:
#takes a string as parameter2)returns false if the string contains less than 8 characters3)returns true if the string contains 8 or more characters
#if i called your function with foo("mypass") it would return false. if i called it with foo("mylongpassword") it would return True, and so on.

def passcontroller(password):
    if len(password)  >= 8:
        
        return True
    else:
        return False
    
print(passcontroller("longpasswordzero"))
