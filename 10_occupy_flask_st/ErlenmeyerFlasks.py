from flask import Flask, render_template
import csv, random
from csv import reader
app = Flask(__name__)


#creates dictionary (empty)
OCCLIST = {}
LINKLIST = {}
#takes in file, returns random occupation with weighted probability
def randomocc(filename):
    #opens file and reads it
    file = open(filename, "r")
    raw = reader(file)
    next(file)
    for r in raw:
        OCCLIST[r[0]] = float(r[1])
    #to be polite
    del OCCLIST['Total']
    file.close()
    return OCCLIST
def linkify(filename):
    #opens file and reads it
    file = open(filename, "r")
    raw = reader(file)
    next(file)
    #iterates, adds key and weight to OCCLIST
    for r in raw:
        LINKLIST[r[0]] = str(r[2])
    #to be polite
    del LINKLIST['Total']
    file.close()
    return LINKLIST
#route for main page
@app.route("/")
def main_page():
    #loads html template
    return render_template("home.html")

def randomO(table):
    #random number
    randy = random.uniform(0, 99.8)
    #counter keeps track of what percentage we're up to
    count = 0
    #returns key based with weighted probability
    for key, value in OCCLIST.items():
        #compares random number to % we're up to;
        #if current percentage is greater than randy, return key
        if count + value >= randy:
            return key
        #if not, add counter to current percentage
        count += value
@app.route("/occupations")
def occupy():
    return render_template("occupations.html",
    table = randomocc("occupations.csv"),
    rand = randomO(randomocc("occupations.csv")),
    lnks = linkify("occupations.csv"))

if __name__ == "__main__":
    app.debug = True
    app.run()
