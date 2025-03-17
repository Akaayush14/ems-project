from customtkinter import *
from tkinter import messagebox
from PIL import Image
from database import *

def employee_portal(username):
    #Function to open the window in a maximized state
    def maximize_window():
        try:
            emp_root.state('zoomed')  # Maximize the window
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    emp_root = CTk()
    emp_root.title("Employee Portal")
    emp_root.configure(fg_color="dark sea green")
    emp_root.overrideredirect(False)
    emp_root.after(10, maximize_window)

    #Function to fetch employee details
    def fetch_employee_details():
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM employees WHERE name = ?', (username,))
                employee = cursor.fetchone()
                if employee:
                    id_label.configure(text=f"ID: {employee[0]}")
                    name_label.configure(text=f"Name: {employee[1]}")
                    phone_label.configure(text=f"Phone: {employee[2]}")
                    role_label.configure(text=f"Role: {employee[3]}")
                    gender_label.configure(text=f"Gender: {employee[4]}")
                    salary_label.configure(text=f"Salary: {employee[5]}")
                else:
                    messagebox.showerror("Error", "Employee not found!")
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Failed to fetch employee details: {e}")
            finally:
                conn.close()

    #Function to update employee details
    def update_employee_details():
        new_phone = phone_entry.get()
        new_salary = salary_entry.get()

        if not new_phone or not new_salary:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('UPDATE employees SET phone = ?, salary = ? WHERE name = ?', (new_phone, new_salary, username))
                conn.commit()
                messagebox.showinfo("Success", "Details updated successfully!")
                fetch_employee_details()
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Failed to update details: {e}")
            finally:
                conn.close()

    #Header Images
    photo_4 = CTkImage(Image.open("image_3.png"), size=(920, 200)) 
    photo_label_4 = CTkLabel(emp_root, image=photo_4, text="")
    photo_label_4.place(x=0, y=0)

    photo_5 = CTkImage(Image.open("image_4.png"), size=(920, 200))  
    photo_label_5 = CTkLabel(emp_root, image=photo_5, text="")
    photo_label_5.place(x=790, y=0)

    #Employee Details Labels
    header_label = CTkLabel(emp_root, text=f"Welcome {username}", font=("aerial", 30, "bold"), text_color="black")
    header_label.place(x=700, y=220)

    id_label = CTkLabel(emp_root, text="ID: ", font=("aerial", 20, "bold"), text_color="black")
    id_label.place(x=100, y=300)

    name_label = CTkLabel(emp_root, text="Name: ", font=("aerial", 20, "bold"), text_color="black")
    name_label.place(x=100, y=380)

    phone_label = CTkLabel(emp_root, text="Phone: ", font=("aerial", 20, "bold"), text_color="black")
    phone_label.place(x=100, y=460)

    role_label = CTkLabel(emp_root, text="Role: ", font=("aerial", 20, "bold"), text_color="black")
    role_label.place(x=100, y=540)

    gender_label = CTkLabel(emp_root, text="Gender: ", font=("aerial", 20, "bold"), text_color="black")
    gender_label.place(x=100, y=620)

    salary_label = CTkLabel(emp_root, text="Salary: ", font=("aerial", 20, "bold"), text_color="black")
    salary_label.place(x=100, y=700)

    #Fetch and display employee details on startup
    fetch_employee_details()

    #Update Details Section
    phone_entry = CTkEntry(emp_root, placeholder_text="New phone number", fg_color='white', text_color='black', width=200, height=35)
    phone_entry.place(x=100, y=780)

    salary_entry = CTkEntry(emp_root, placeholder_text="New Salary", fg_color='white', text_color='black', width=200, height=35)
    salary_entry.place(x=370, y=780)

    update_button = CTkButton(emp_root, text="Update Details", command=update_employee_details, width=200, height=35)
    update_button.place(x=650, y=780)

    #Run the employee portal
    emp_root.mainloop()

