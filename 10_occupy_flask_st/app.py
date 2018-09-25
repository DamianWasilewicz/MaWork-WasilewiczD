#ErlenmeyerFlasks-WasilewiczD-MingM
#SoftDev1 pd6
#K #10: Jinja Tuning
#2018-09-23
from flask import Flask, render_template
import csv, random
from csv import reader
from ErlenmeyerFlasks import randomOcc, randomNum, randlist
app = Flask(__name__)

@app.route("/")
def main_page():
    #loads html template
    return render_template("home.html")

@app.route("/occupations")
def occupy():
    #calls rendertemplate and passes OCCLIST and the random occupation as arguemnts
    return render_template("occupations.html",
    #list used to create table
    table = randomOcc("occupations.csv"),
    #value used to find random occupation to display
    rand = randomNum(randlist))

if __name__ == "__main__":
    app.debug = True
    app.run()
