from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html" )

if __name__ == "__main__":
    app.run(debug=True)

#@app.route("/hello", methods=["POST"])
#def hello():
#    name = request.form.get("name")
 #   if(name == ""):
 #       return render_template("index.html" , err=err )
 #   return render_template("hello.html", name=name)
