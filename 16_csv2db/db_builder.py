#The Wicked W's - Jeffrey Wu & Damian Wasilewicz
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
def makeTable(filename):
    with open(filename, 'r') as files:
        courses = csv.DictReader(filename)
        first = 0
        for rec in courses:
            if first == 0:
                comm = "CREATE TABLE " + filename[:len(filename) - 4] + " ("
                for col in rec.keys():
                    comm += "'" + col + "' BLOB, "
                    c.execute(comm[:len(comm) - 2] + ")")
                    first = 1
            comm2 =  "INSERT INTO " + filename[:len(filename) - 4] + " VALUES ("
            for info in rec.keys():
                comm2 += "'" + rec[info] + "',"
                c.execute(comm2[:len(comm2)])

#==========================================================
makeTable("peeps.csv")
makeTable("courses.csv") #run for both csv files
c.execute("SELECT * FROM peeps")
print(c.fetchall())
c.execute("SELECT * FROM courses")
print(c.fetchall()) #print data from each table

db.commit() #save changes
db.close()  #close database
