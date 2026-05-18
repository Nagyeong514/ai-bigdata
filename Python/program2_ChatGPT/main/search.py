import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'student.db')


def search_student(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT * FROM student WHERE Name = ?"
    cursor.execute(query, (name,))

    result = cursor.fetchall()

    conn.close()

    return result