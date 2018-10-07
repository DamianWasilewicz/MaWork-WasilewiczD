#The Wicked W's - Jeffrey Wu & Damian Wasilewicz
#SoftDev1 pd0
#K #16: No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os        #for deleting discobandit


file = "discobandit";

## If file exists, delete it ##
#os.remove(file)


DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#creates table and SQL statement to be executed for creating peeps table
comm_peeps = """
CREATE TABLE mypeeps(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    osis INTEGER)
"""
#found out we didn't need one for occupations
#comm_occupations = """
#CREATE TABLE jobs(
#    job TEXT,
#    percentage INTEGER)
#"""

comm_courses = """
CREATE TABLE classes(
    id INTEGER PRIMARY KEY,
    name TEXT,
    mark INTEGER,
    pd INTEGER)
"""
#execute command lines creating tables
c.execute(comm_peeps)
#c.execute(comm_occupations)
c.execute(comm_courses)

#populating table - peeps
with open("peeps.csv") as file:
    read = csv.DictReader(file)
    for r in read:
        comm_peeps = "INSERT INTO mypeeps(name, age, id) VALUES('" + r['name'] + "', " + r['age'] + ", " + r['id'] + ");"
        c.execute(comm_peeps)

#populating table-comm_occupations------defunct
#with open("occupations.csv") as file:
#    read = csv.DictReader(file)
#    for r in read:
#        comm_occupations = "INSERT INTO jobs(Job Class, Percentage) VALUES('" + r['Job Class'] + "', " + r['Percentage'] + ");"
#        c.execute(comm_occupations)

#populating table-comm_occupations
with open("courses.csv") as file:
    read = csv.DictReader(file)
    for r in read:
        comm_courses = "INSERT INTO classes(name, mark, pd) VALUES('" + r['code'] + "', " + r['mark'] + ", " + r['id'] + ");"
        c.execute(comm_courses)
#print data from each table
c.execute("SELECT * FROM mypeeps")
print(c.fetchall())
c.execute("SELECT * FROM classes")
print(c.fetchall())
#c.execute("SELECT * FROM jobs")
#print(c.fetchall())

db.commit() #save changes
db.close()  #close database
