#Clyde 'Thluffy' Sinclair
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

with open('students.csv') as file:
    data = csv.DictReader(file)
    for row in data:
        print(row)
        c.execute('INSERT INTO roster (name, age, id) VALUES (\"{name}\", {age}, {id})'.format(name = row['name'], age = row['age'], id = row['id']))
#==========================================================

db.commit() #save changes
db.close()  #close database