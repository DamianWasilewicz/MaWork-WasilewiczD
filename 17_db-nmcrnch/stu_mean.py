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

#============================================================================



#get grades according to osis number
def get_grade(osis_num, counter):
    comm_grade = "SELECT mark FROM classes WHERE osis ="
    comm_grade += str(osis_num)
    c.execute(comm_grade)
    a = c.fetchall()
    answer = 0
    while counter >= 0:
        answer = answer + int((a[counter][0]))
        counter = counter - 1
    return answer

def get_length(osis_num):
    comm_length = "SELECT count(*) FROM classes WHERE osis ="
    comm_length += str(osis_num)
    return c.execute(comm_length).fetchone()[0]

def get_avg(osis_num):
    return int(get_grade(osis_num, get_length(osis_num) - 1)) / int(get_length(osis_num))


#Create table for averages
comm_avg = """
    CREATE TABLE IF NOT EXISTS avgs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        avg INTEGER,
        osis INTEGER)
        """
c.execute(comm_avg)
#Populate avg table
osis_num = 1
while osis_num < 11:
    comm_getname = "SELECT name FROM mypeeps WHERE osis = "
    comm_getname += str(osis_num)
    c.execute(comm_getname)
    name = c.fetchall()
    avg = get_avg(osis_num)
    comm_peeps = "INSERT INTO mypeeps(name, id, avg) VALUES('" + name[0] + "', " + osis_num + ", " + avg + ");"
    c.execute(comm_peeps)
    osis_num += 1


#display avg table
comm_display_avg= "SELECT *FROM peeps_avg"


#comm_avgs = "INSERT INTO avgs(name, osis, avg) VALUES('"+ 'sasha' + "', " + '3' + ", " + 'int(computeAvg())' + ");"
#c.execute(comm_avgs)

db.commit() #save changes
print(c.fetchall())
db.close()  #close database
