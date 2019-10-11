import sqlite3

DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute('''SELECT roster.id, mark 
             FROM courses, roster 
             WHERE courses.id = roster.id;''')
grades_raw = c.fetchall()
print(grades_raw)

db.close()