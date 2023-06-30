from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def Home():
    return render_template("Home.html")

@app.route('/Asus/')
def Asus():
    return render_template("Asus.html")

if __name__=="__main__":
    app.run(debug=True)
    
#now the code uses layout.html to give options to the homepage like Home and Asus
#which is called Navigation menu.