# check_db.py

import sqlite3
import pandas as pd

conn = sqlite3.connect("data/student.db")
df = pd.read_sql("SELECT * FROM student", conn)
print(df.head())
conn.close()