import sqlite3

def init_db():
    conn = sqlite3.connect('cms.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS pages (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
       )    
    ''')

    conn.commit()
    conn.close()

    
