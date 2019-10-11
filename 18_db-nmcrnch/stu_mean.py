import sqlite3

DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute('''SELECT roster.id, mark 
             FROM courses, roster 
             WHERE courses.id = roster.id''')
grades_raw = c.fetchall()
c.execute('''SELECT id
             FROM roster''')
ids = c.fetchall()
grades_nclasses = {entry[0]:[0,0] for entry in ids}
for entry in grades_raw:
    grades_nclasses[entry[0]][0] += 1
    grades_nclasses[entry[0]][1] += entry[1]
print(grades_nclasses)

c.execute('CREATE TABLE IF NOT EXISTS stu_avg (id INTEGER PRIMARY_KEY, gpa REAL)')
for entry in grades_nclasses.items():
    id = entry[0]
    gpa = entry[1][1] / entry[1][0]
    c.execute(f'INSERT INTO stu_avg (id, gpa) VALUES ({id}, {gpa})')

db.commit()
db.close()