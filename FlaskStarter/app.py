#Damian Wasilewicz
#SoftDev1 pd6
#K#13: Echo Echo Echo .
#2018-09-27
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
