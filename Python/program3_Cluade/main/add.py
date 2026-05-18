import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'student.db')

def add_student(student_id, name, mid, final):
    average = (mid + final) / 2

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO student (ID, Name, Mid, Final, Average, Grade) VALUES (?, ?, ?, ?, ?, ?)",
        (student_id, name, mid, final, average, grade)
    )
    conn.commit()
    conn.close()
    return f"'{name}' 학생이 성공적으로 추가되었습니다. (평균: {average:.1f}, 등급: {grade})"