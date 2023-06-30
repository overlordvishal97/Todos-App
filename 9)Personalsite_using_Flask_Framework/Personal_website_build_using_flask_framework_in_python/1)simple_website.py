from flask import Flask
#we are importing thel class of the library 

app=Flask(__name__)
#you are instantiating that class that object.
#__name__ is special variable that will get as value the name of the python script.
@app.route('/')
#this is a decorator.
#/ this used to close the url and open the url.
#if you want another page you would add a decorator.
def home():
    return "Website content goes here!"

@app.route('/asus/')
def asus():
    return "my phone model is Asus zenfone 6z!"
#you will get an error if so then change the function because we can't have the same function.


if __name__=="__main__":
    app.run(debug=True)
    
#if you want to access other homepage then you have to use decorator used for the website to access the website.
#this website will show simple strings in the next one we will use html templates.