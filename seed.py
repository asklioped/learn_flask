import sqlite3

conn = sqlite3.connect('cms.db')
cur = conn.cursor()

cur.execute('''
INSERT INTO pages (title, content) VALUES (?, ?)''', ("Головна", "Це головна сторінка"))
cur.execute('''
INSERT INTO pages (title, content) VALUES (?, ?)''', ("Про нас","Це сторінка про нас"))

conn.commit()
conn.close()