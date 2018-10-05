#The Wicked W's - Jeffrey Wu & Damian Wasilewicz
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
comm = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
def createATable(file):
    with open(file) as coursesFile:
        courses = csv.DictReader(coursesFile)
        first = True; #indicates whether loop is being run for the first time
        c1 = ""
        c2 = ""
        c3 = ""
        for rec in courses:
            if first: #if first time being run, uses names from csv file
                c1 = list(rec.keys())[0]
                c2 = list(rec.keys())[1]
                c3 = list(rec.keys())[2]
            comm.execute("CREATE TABLE " + file[0:-4] + "(" +c1+ "  TEXT, " + c2+ " INTEGER, " +c3+" INTEGER)")
            first = False;
        args = (rec[c1], rec[c2], rec[c3])
        c.execute("INSERT INTO " + file[0:-4] + " VALUES(?, ?, ?)", args)
#==========================================================
createATable("peeps.csv")
createATable("courses.csv")
createATable("occupation.csv")
db.commit() #save changes
db.close()  #close database
