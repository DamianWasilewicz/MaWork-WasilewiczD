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
with open('templates/peeps.csv', 'r') as file:
    read = csv.DictReader(file)
    for r in read:
        comm_peeps = "INSERT INTO mypeeps(name, age, id) VALUES('" + r['name'] + "', " + r['age'] + ", " + r['id'] + ");"
        c.execute(comm_peeps)

#populating table-comm_occupations
with open('templates/courses.csv', 'r') as file:
    read = csv.DictReader(file)
    for r in read:
        comm_courses = "INSERT INTO classes(name, mark, osis) VALUES('"+ r['code'] + "', " + r['mark'] + ", " + r['id'] + ");"
        c.execute(comm_courses)
comm_grade = """
    SELECT
        mark
    FROM
        classes
    WHERE
        osis == 3
    """
def computeAvg():
    list = c.execute(comm_grade)
    number = list.fetchone()[0]
    number2 = list.fetchone()[0]
    print((number + number2)/ 2)

comm_avg = """
    CREATE TABLE IF NOT EXISTS avgs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        osis INTEGER,
        avg INTEGER)
        """
c.execute(comm_avg)

#comm_avgs = "INSERT INTO avgs(name, osis, avg) VALUES('"+ 'sasha' + "', " + '3' + ", " + 'int(computeAvg())' + ");"
#c.execute(comm_avgs)
db.commit() #save changes
computeAvg()
db.close()  #close database
