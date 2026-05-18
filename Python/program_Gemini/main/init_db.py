#init_db.py

import sqlite3
import pandas as pd
 
sheets = pd.read_excel("data/student.xlsx", sheet_name=None)
conn = sqlite3.connect("data/student.db")
 
for sheet_name, df in sheets.items():
    df.to_sql(sheet_name, conn, if_exists="replace", index=False)
    print(f"{sheet_name} -> {len(df)}행 저장")
 
conn.close()