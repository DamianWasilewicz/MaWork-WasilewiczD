#ErlenmeyerFlasks-WasilewiczD-MingM
#SoftDev1 pd6
#K #10: Jinja Tuning
#2018-09-23
#import flask, template, random, and file reading necessities
from flask import Flask, render_template
import csv, random
from csv import reader
#import functions and dictionary from ErlenmeyerFlasks.py
from util import ErlenmeyerFlasks
app = Flask(__name__)

#home page
@app.route("/")
def main_page():
    #loads html template
    return render_template("home.html")

@app.route("/occupations")
def occupy():
    #calls rendertemplate and passes OCCLIST and the random occupation as arguemnts
    return render_template("occupations.html",
    #list used to create table
    table = ErlenmeyerFlasks.randomOcc("data/occupations.csv"),
    #value used to find random occupation to display
    rand = ErlenmeyerFlasks.randomNum(ErlenmeyerFlasks.randlist))

if __name__ == "__main__":
    app.debug = True
    app.run()
