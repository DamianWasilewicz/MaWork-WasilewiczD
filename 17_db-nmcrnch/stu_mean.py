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

osis_num = 1;

counter = 2

#get grades according to osis number
def get_grade(osis_num):
    comm_grade = "SELECT mark FROM classes WHERE osis ="
    comm_grade += str(osis_num)
    return c.execute(comm_grade)
print (str(get_grade(1).fetchall()[counter][0]) + " " + str(get_grade(1).fetchall()[counter - 1][0]) + " " + str(get_grade(1).fetchall()[counter - 2][0]))

def get_length():
    comm_length = "SELECT count(*) FROM classes WHERE osis ="
    comm_length += str(osis_num)
    return c.execute(comm_length).fetchone()[0]

#print get_length()

#============= I AM HERE ===================================================

# ISSUES WITH FETCHONE() AND GETGRADE
#gets average according to osis number
#def computeAvg(name):
#    cur = get_grade(name)
    #print cur
#    length = get_length()
#    print get_grade().fetchone()[0]
    #return retVal/length

#Create table for averages
comm_avg = """
    CREATE TABLE IF NOT EXISTS avgs(
        id INTEGER PRIMARY KEY,
        name TEXT,
        avg INTEGER,
        osis INTEGER)
        """

#c.execute(comm_avg)
comm_fetch = """
    SELECT mypeeps.name FROM mypeeps, classes
    WHERE mypeeps.id == classes.id
    """
c.execute(comm_fetch)
p = c.fetchall()
#print(p)

#Populate avg table
#while osis_num < 11:
#    comm_getname = "SELECT name FROM mypeeps WHERE osis = "
#    comm_getname += str(osis_num)
#    name = c.execute(comm_getname)
#    avg = computeAvg(name)
#    comm_avgs = "INSERT INTO avgs(name, osis, avg) VALUES({n}{o}{a}).format(n = name[0], o = osis_num, a = avg)"
#    osis_num += 1

#display avg table
comm_display_avg= "SELECT *FROM peeps_avg"

#comm_avgs = "INSERT INTO avgs(name, osis, avg) VALUES('"+ 'sasha' + "', " + '3' + ", " + 'int(computeAvg())' + ");"
#c.execute(comm_avgs)

db.commit() #save changes
db.close()  #close database
