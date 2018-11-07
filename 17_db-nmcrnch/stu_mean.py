#Holly Halls
#Damian Wasilewicz, Sophia Xia
#SoftDev1 pd1
#K17 -- Average, ... or Basic?
#2018-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os        #for deleting discobandit


file = "discobandit.db";

#opens file in write mode, which turns it into a blank file
open("discobandit.db",'w').close()


DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

comm_peeps = """
CREATE TABLE IF NOT EXISTS mypeeps(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    osis INTEGER)
"""
comm_courses = """
CREATE TABLE IF NOT EXISTS classes(
    id INTEGER PRIMARY KEY,
    name TEXT,
    mark INTEGER,
    osis INTEGER)
"""
#execute command lines creating tables
c.execute(comm_peeps)
c.execute(comm_courses)

#populating table - peeps
with open('data/peeps.csv', 'r') as file:
    read = csv.DictReader(file)
    for r in read:
        comm_peeps = "INSERT INTO mypeeps(name, age, id) VALUES('" + r['name'] + "', " + r['age'] + ", " + r['id'] + ");"
        c.execute(comm_peeps)

#populating table-comm_occupations

with open('data/courses.csv', 'r') as file:
    read = csv.DictReader(file)
    for r in read:
        comm_courses = "INSERT INTO classes(name, mark, osis) VALUES('"+ r['code'] + "', " + r['mark'] + ", " + r['id'] + ");"
        c.execute(comm_courses)

#============================================================================
comm_display_classes= "SELECT * FROM classes"
displayC = c.execute(comm_display_classes).fetchall()
#print(displayC)
osis_num = 1;

#get grades according to osis number
def get_grade(osis_num):
    comm_grade = "SELECT mark FROM classes WHERE osis ="
    comm_grade += str(osis_num)
    return c.execute(comm_grade).fetchall()
#print get_grade(osis_num)

#gets average according to osis number
def computeAvg(osis_num):
    cur = get_grade(osis_num)
    length = len(cur)
    ctr = length -1
    retVal = 0
    while ctr >= 0:
        retVal += int(cur[ctr][0])
        ctr -= 1
    return retVal/length
#print computeAvg(osis_num)

#Create table for averages
comm_avg = """
    CREATE TABLE IF NOT EXISTS peeps_avgs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        avg INTEGER,
        osis INTEGER)
        """
c.execute(comm_avg)

#Populate avg table
comm_len = "SELECT * FROM mypeeps"
length = len(c.execute(comm_len).fetchall())
#print length
while osis_num < length +1:
    comm_getname = "SELECT name FROM mypeeps WHERE mypeeps.id = "
    comm_getname += str(osis_num)
    name = c.execute(comm_getname).fetchone()[0]
    #print name
    avg = computeAvg(osis_num)
    #print avg
    params = (None, name, avg, osis_num)
    c.execute("INSERT INTO peeps_avgs VALUES(?,?,?,?)", params)
    osis_num += 1

#display avg table
comm_display_avg= "SELECT * FROM peeps_avgs"
display = c.execute(comm_display_avg).fetchall()
#print display
comm_display_classes = "SELECT * FROM classes"
displayc = c.execute(comm_display_classes).fetchall()
#add a course to the table classes
def add_course(nname, nmark, nosis):
    columns = (nname, nmark, nosis)
    c.execute("INSERT INTO classes(name, mark, osis) VALUES(?,?,?)", columns)

add_course("IT", 100, 11)
#print(displayc)


db.commit() #save changes
db.close()  #close database
