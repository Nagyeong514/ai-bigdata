import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'student.db')


def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def add_student(student_id, name, mid, final):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    mid = int(mid)
    final = int(final)

    average = (mid + final) / 2
    grade = calculate_grade(average)

    query = """
    INSERT INTO student (ID, Name, Mid, Final, Average, Grade)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(
        query,
        (student_id, name, mid, final, average, grade)
    )

    conn.commit()
    conn.close()