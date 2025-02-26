import sqlite3
from tkinter import messagebox

#Creating a sqlite database:
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

#Creating the table inside the database(i.e employee.db):
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    role TEXT NOT NULL,
    gender TEXT NOT NULL,
    salary REAL NOT NULL
)
''')
conn.commit()
conn.close()

#Establishing a connection to the employee.db using connect_db():
def connect_db():
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect('employee.db')
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")
        return None
    
#Function to bring or retrieve all employees data from the database(employee.db)
def fetch_all_employees():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees')
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch employees: {e}")
            return []
        finally:
            conn.close()
    return []