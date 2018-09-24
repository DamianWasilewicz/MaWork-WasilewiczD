from flask import Flask, render_template
import csv, random
app = Flask(__name__)


#creates dictionary (empty)
OCCLIST = {}
#takes in file, returns random occupation with weighted probability
def randomocc(filename):
    #opens file and reads it
    file = open(filename, "r")
    red = file.read()
    #split by lines, excluding title and empty line at bottom
    lines = red.split("\n")[1:-1]
    read = csv.reader(lines)
    #iterates, adds key and weight to OCCLIST
    for r in read:
        #creates list
        #mylist=list()
        #mylist.append(float(r[1]))
        #mylist.append(r[2])
        OCCLIST[r[0]]=mylist
    #to be polite
    file.close()
    return OCCLIST
#route for main page
@app.route("/")
def main_page():
    #loads html template
    return render_template("home.html")

@app.route("/occupations")
def occupy():
    return render_template("occupations.html",
    table = randomocc("occupations.csv"))

if __name__ == "__main__":
    app.debug = True
    app.run()
