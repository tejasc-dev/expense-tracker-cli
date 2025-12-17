import sqlite3

db_name = "expenses.db"

def get_connection():
    return sqlite3.connect(db_name)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT NOT NULL,
                   description TEXT NOT NULL,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL
            
                   )  """)
    
    conn.commit()
    conn.close()