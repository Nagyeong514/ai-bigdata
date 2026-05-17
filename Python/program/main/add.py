#add.py

import sqlite3
import os

def calculate_grade(average):
    # 성적 등급 산출 로직입니다.
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

def insert_student(student_id, name, mid, final):
    # 평균 및 등급을 계산합니다.
    average = (float(mid) + float(final)) / 2
    grade = calculate_grade(average)
    
    db_path = os.path.join(os.path.dirname(__file__), '../data/student.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "INSERT INTO student (ID, Name, Mid, Final, Average, Grade) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (student_id, name, mid, final, average, grade))
    
    conn.commit()
    conn.close()
    
    return {
        "ID": student_id,
        "Name": name,
        "Mid": mid,
        "Final": final,
        "Average": average,
        "Grade": grade
    }