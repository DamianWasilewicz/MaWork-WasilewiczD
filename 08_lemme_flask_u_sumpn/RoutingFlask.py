#Damian Wasilewicz
#SoftDev1 Pd6
#K #08: Fill Yer Flask
#2018-09-19

#Imports flask from Flask, and render template in order to load html templates
from flask import Flask, render_template
app = Flask(__name__)

#route for main page
@app.route("/")
def main_page():
    #loads html template
    return render_template("base.html")


#route for info, found by adding more to end of url
@app.route("/more")
def basic_info():
    return render_template("info.html")

#route for hobbies, found by adding hobbies to end of url

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
