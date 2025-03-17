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

######################################################################Admin page database functionalities:###############################################################
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
        reset_ids()  # Reset IDs after deletion

#Function to delete all records present in the table:
def delete_all_employees():
    result = messagebox.askyesno("Confirm", "Are you sure you want to delete all employees?")
    if result:
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM employees')
                cursor.execute('DELETE FROM sqlite_sequence WHERE name="employees"')
                conn.commit()
                messagebox.showinfo("Success", "All employees deleted successfully!")
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Failed to delete all employees: {e}")
            finally:
                conn.close()

##################################################################Login page database functionalities:###################################################################
#Function to create user table:
def create_users_table():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                email TEXT
            )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to create users table: {e}")
        finally:
            conn.close()

#Call this function to create the table when the application starts:
create_users_table()

#Function to check login credentials:
def check_login(username, password):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            user = cursor.fetchone()
            return user  #Returns the user record if found, otherwise None
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to check login: {e}")
            return None
        finally:
            conn.close()
    return None

#Function to reset password:
def reset_password(username, email, new_password):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND email = ?', (username, email))
            user = cursor.fetchone()

            if user:
                cursor.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
                conn.commit()
                return True  #Password reset successful
            else:
                return False  #User not found
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to reset password: {e}")
            return False
        finally:
            conn.close()
    return False

#Function to create a new user account:
def create_user(username, password, email, role):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)', (username, password, email, role))
            conn.commit()
            return True  #Account creation successful
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to create account: {e}")
            return False
        finally:
            conn.close()
    return False

#############################################################Employee portal database function:##########################################################################
#Function to fetch employee details by name
def fetch_employee_by_name(username):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees WHERE name = ?', (username,))
            employee = cursor.fetchone()  # Fetch the employee record
            return employee
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch employee details: {e}")
            return None
        finally:
            conn.close()
    return None

#Function to update employee details
def update_employee_details(username, new_phone, new_salary):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE employees SET phone = ?, salary = ? WHERE name = ?', (new_phone, new_salary, username))
            conn.commit()
            return True  #Update successful
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to update employee details: {e}")
            return False
        finally:
            conn.close()
    return False

