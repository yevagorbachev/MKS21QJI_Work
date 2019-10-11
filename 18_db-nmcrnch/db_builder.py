#PreQL_Yevgeniy Gorbachev
#SoftDev pd1
#K18 -- Average
#2019-10-14

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

##################DB population
data = {}
c.execute('CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER PRIMARY_KEY)')

with open('students.csv') as csvfile0:
    data = csv.DictReader(csvfile0)
    for row in data:
        name, age, id = row['name'], row['age'], row['id']
        c.execute(f'INSERT INTO roster (name, age, id) VALUES (\'{name}\', {age}, {id})')


data2 = {}
c.execute('CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)') #command executed

with open('courses.csv') as csvfile1: #open and read courses.csv file and store as dictionary
    data2 = csv.DictReader(csvfile1)
    for row in data2: #for every row in reader, insert values into courses table
        code, mark, id = row['code'], row['mark'], row['id']
        c.execute(f'INSERT INTO courses (code, mark, id) VALUES (\'{code}\', {mark}, {id})')

###################endpop

db.commit() #save changes

db.close()  #close database