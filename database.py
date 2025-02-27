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
    
#Function to add an employee record:
def add_employee(name, phone, role, gender, salary):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO employees (name, phone, role, gender, salary)
            VALUES (?, ?, ?, ?, ?)
            ''', (name, phone, role, gender, salary))
            conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to add employee: {e}")
        finally:
            conn.close()
        
#Functions to update the employees ids, phone role, and others:
def update_employee(employee_id, name, phone, role, gender, salary):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE employees
            SET name = ?, phone = ?, role = ?, gender = ?, salary = ?
            WHERE id = ?
            ''', (name, phone, role, gender, salary, employee_id))
            conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to update employee: {e}")
        finally:
            conn.close()
#Function to reset IDs sequentially whenever we delete employe record from the table:
def reset_ids():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees ORDER BY id')
            rows = cursor.fetchall()

            cursor.execute('DELETE FROM employees')
            cursor.execute('DELETE FROM sqlite_sequence WHERE name="employees"')

            for index, row in enumerate(rows, start=1):
                cursor.execute('''
                INSERT INTO employees (id, name, phone, role, gender, salary)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (index, row[1], row[2], row[3], row[4], row[5]))

            conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to reset IDs: {e}")
        finally:
            conn.close()
            
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

#Function to particularly delete an employee record.
def delete_employee(employee_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
            conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to delete employee: {e}")
        finally:
            conn.close()

