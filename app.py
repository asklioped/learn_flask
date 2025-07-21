from flask import Flask, render_template
from database import init_db
import sqlite3

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('cms.db')
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM pages")
    pages = cur.fetchall()
    conn.close()

    return render_template("index.html", pages = pages)

if __name__ == ('__main__'):
    app.run(debug=True)