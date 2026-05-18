import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'student.db')

def search_student(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE Name = ?", (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows