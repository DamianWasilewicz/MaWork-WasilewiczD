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
CREATE TABLE if not exists mypeeps(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER)
"""
comm_courses = """
CREATE TABLE if not exists classes(
    name TEXT,
    mark INTEGER,
    pd INTEGER)
"""
#execute command lines creating tables
c.execute(comm_peeps)
c.execute(comm_courses)

#populating table - peeps
with open("templates/peeps.csv") as file:
    read = csv.DictReader(file)
    for r in read:
        comm_peeps = "INSERT INTO mypeeps(name, age, id) VALUES('" + r['name'] + "', " + r['age'] + ", " + r['id'] + ");"
        c.execute(comm_peeps)

#populating table-comm_occupations
with open("templates/courses.csv") as file:
    read = csv.DictReader(file)
    for r in read:
        comm_courses = "INSERT INTO classes(name, mark, pd) VALUES('" + r['code'] + "', " + r['mark'] + ", " + r['id'] + ");"
        c.execute(comm_courses)

def stalk(studentname): """
    SELECT
        name,
        age,
        id
    FROM
        peeps
    WHERE
        name = studentname
    """

db.commit() #save changes
print "Sucess"
db.close()  #close database
