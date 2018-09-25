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
#creates dictionary with only occupation name
randlist = {}
#takes in file, returns random occupation with weighted probability
def randomOcc(filename):
    #opens file and reads it
    try:
        file = open(filename, "r")
    except:
        print("file not found")
        return 0

    red = file.read()
    #split by lines, excluding title and empty line at bottom
    lines = red.split("\n")[1:-2]
    read = csv.reader(lines)
    #iterates, adds key and weight to OCCLIST
    for r in read:
        temp = float(r[1]) * 10
        randlist[r[0]] = int(temp)
        value = [float(r[1]), r[2]]
        OCCLIST[r[0]] = value
    #to be polite
    file.close()
    return OCCLIST

def randomNum(lists):
    #random number
    randy = random.randint(0, 998)
    #counter keeps track of what percentage we're up to
    counter = 0
    #returns key based with weighted probability
    for key in lists.items():
        #compares random number to % we're up to;
        #if current percentage is greater than randy, return key
        counter+= float(key[1])
        if counter >= randy:
            return key[0]
        #if not, add counter to current percentage
