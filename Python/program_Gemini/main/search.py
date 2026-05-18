# main/search.py
import sqlite3
import os

def search_student_by_name(name):
    # 경로 설정
    db_path = os.path.join(os.path.dirname(__file__), '../data/student.db')
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # 이름으로 학생 조회
    query = "SELECT * FROM student WHERE Name = ?"
    cursor.execute(query, (name,))
    
    results = cursor.fetchall()
    conn.close()
    return results