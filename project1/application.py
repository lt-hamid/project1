from flask import Flask, render_template , request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template("index.html" )

if __name__ == "__main__":
    app.run(debug=True)     #with this I don't have to re-run the server everytime I make a change 
                            #cause it will automatically be detecting the changes and updating the website for me





@app.route("/home", methods=["GET","POST"])
def home():
    name = request.form.get("name")
    return render_template("home.html", name=name)

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/about" , methods=["GET","POST"])
def about():
    return render_template("about.html")    

@app.route("/citiesweather", methods=["GET","POST"])
def citiesweather():
    return render_template("citiesweather.html")