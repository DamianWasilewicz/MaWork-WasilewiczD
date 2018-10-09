#Holly Halls
#Damian Wasilewicz, Sophia Xia
#SoftDev1 pd1
#K17 -- Average, ... or Basic?
#2018-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os        #for deleting discobandit


file = "discobandit";

## If file exists, delete it ##
#os.remove(file)


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

osis_num = 1;

#get grades according to osis number
def get_grade(osis_num):
    comm_grade = "SELECT mark FROM classes WHERE osis ="
    comm_grade += str(osis_num)
    return c.execute(comm_grade).fetchall()
#print get_grade(osis_num)

#returns how many grades a student has
def get_length(osis_num):
    comm_length = "SELECT count(*) FROM classes WHERE osis ="
    comm_length += str(osis_num)
    return c.execute(comm_length).fetchone()[0]
#print get_length(osis_num)

#gets average according to osis number
def computeAvg(osis_num):
    length = get_length(osis_num)
    ctr = length -1
    cur = get_grade(osis_num)
    retVal = 0
    while ctr >= 0:
        retVal += int(cur[ctr][0])
        ctr -= 1
    return int(float(retVal/length))
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
while osis_num < 11:
    comm_getname = "SELECT name FROM mypeeps WHERE mypeeps.id = "
    comm_getname += str(osis_num)
    name = c.execute(comm_getname).fetchone()[0]
    #print name
    avg = computeAvg(osis_num)
    #print avg
    comm_pop = "INSERT INTO peeps_avgs(name, avg, osis) VALUES(\"" + name + "\", " + str(avg) + ", " + str(osis_num) + ");"
    c.execute(comm_pop)
    osis_num += 1

def add_course(nname, nmark, nosis):
    commands = (nname, nmark, nosis)
    c.execute("INSERT INTO classes(name, mark, osis) VALUES(?, ?, ?)", commands)

#display avg table
comm_display_avg= "SELECT name, avg, osis FROM peeps_avgs"
display = c.execute(comm_display_avg)
ctr = 0
#add a course to the table classes

#while ctr < 11:
#print display.fetchall()
    #ctr += 1

#add a course to the table classes
add_course("IT", 100, 11)
add_course("FunTime", 120, 15)
add_course("HaxorsClass", 400, 18)
add_course("Gym", 500, 1000)
comm_display_classes = "SELECT * FROM classes"
display_classes = c.execute(comm_display_classes)

# display_classes.fetchall()

db.commit() #save changes
db.close()  #close database
