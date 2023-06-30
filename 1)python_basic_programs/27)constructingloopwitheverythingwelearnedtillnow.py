def sentence_maker(phrase):
    interogatives = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return"{}.".format(capitalized)
    
#print(sentence_maker("how are you"))  #we just used it to test the function so i commented(#) to know in the future what this is used for 
results = []
while True:
    user_input= input("Say something: ")
    if user_input == "/end":
        break
    else:
        #if you want your function to run add it in the results  
        results.append(sentence_maker(user_input))
        
#To make it look more like sentence and user friendly you have to use 'join'. 
print(" ".join(results))