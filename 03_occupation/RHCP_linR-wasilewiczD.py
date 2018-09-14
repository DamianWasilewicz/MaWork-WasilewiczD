#RHCP-Damian Wasilewicz, Ricky line
#SoftDev1 Pd6
#K06--Stl/O:Getting By With a Little Help From Our Friends
#2018-09-13

#imports the necessary libraries for reading csv files and using random
import csv, random

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
        OCCLIST[r[0]] = float(r[1])
    #to be polite
    file.close()
    #generatoes random float
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

#runs function
print(randomocc("occupations.csv"))
