#Krew_Yevgeniy Gorbachev, Tiffany Cao
#SoftDev  
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
data = {}
c.execute('CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)')

with open('students.csv') as csvfile0:
    data = csv.DictReader(csvfile0)
    for row in data:
        c.execute('INSERT INTO roster (name, age, id) VALUES (\"{name}\", {age}, {id})'.format(name = row['name'], age = row['age'], id = row['id']))


data2 = {}
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)") #command executed

with open('courses.csv') as csvfile1: #open and read courses.csv file and store as dictionary
    data2 = csv.DictReader(csvfile1)
    for row in data2: #for every row in reader, insert values into courses table
        c.execute("INSERT INTO courses (code, mark, id) VALUES (\"{code}\", {mark}, {id})".format(code = row['code'], mark = row['mark'], id = row['mark']))

#============================== ============================

db.commit() #save changes
db.close()  #close database