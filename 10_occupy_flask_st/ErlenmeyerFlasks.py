#ErlenmeyerFlasks-WasilewiczD-MingM
#SoftDev1 pd6
#K #10: Jinja Tuning
#2018-09-23
from flask import Flask, render_template
import csv, random
from csv import reader
app = Flask(__name__)


#creates dictionary (empty)
OCCLIST = {}
randlist = {}
#takes in file, returns random occupation with weighted probability
def randomocc(filename):
    #opens file and reads it
    try:
        file = open(filename, "r")
    except:
        print("file not found")
        return 0

    red = file.read()
    #split by lines, excluding title and empty line at bottom
    lines = red.split("\n")[1:-1]
    read = csv.reader(lines)
    #iterates, adds key and weight to OCCLIST
    for r in read:
        randlist[r[0]] = float(r[1])
        value = [float(r[1]), r[2]]
        OCCLIST[r[0]] = value
    #to be polite
    del OCCLIST['Total']
    del randlist['Total']
    file.close()
    return OCCLIST
def randomO(lists):
    #random number
    randy = random.uniform(0, 99.8)
    #counter keeps track of what percentage we're up to
    count = 0
    #returns key based with weighted probability
    for key in randlist.items():
        #compares random number to % we're up to;
        #if current percentage is greater than randy, return key
        if count + randlist[key[0]] >= randy:
            return key
        #if not, add counter to current percentage
            count += randlist[key[0]]
#route for main page
@app.route("/")
def main_page():
    #loads html template
    return render_template("home.html")

@app.route("/occupations")
def occupy():
    return render_template("occupations.html",
    table = randomocc("occupations.csv"),
    rand = randomO(randlist))

if __name__ == "__main__":
    app.debug = True
    app.run()
