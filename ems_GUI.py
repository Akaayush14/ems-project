from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
from database import * #It imports all functions from database.py

#It shows all the data present in the database:
def show_all():
    try:
        for row in tree.get_children():
            tree.delete(row)
        employees = fetch_all_employees()
        for employee in employees:
            tree.insert("", END, values=employee)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#Function to open full screen window:
def maximize_window():
    try:
        window.state('zoomed')
    except Exception as e:
        messagebox.showerror("Error", f"Are you sure you want to exit?")

#Function to show confirmation when close button is clicked:
def on_closing():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()

#Initializing the main window:
window = CTk()

#After 10 milliseconds the window will open in full screen.
window.after(10, maximize_window)

#It binds the close button to the on_closing function:
window.protocol("WM_DELETE_WINDOW", on_closing)

#Setting window background:                               
window.configure(fg_color="dark sea green")

#Window title:
window.title("Employee Management System")

#Specifying rows and columns when window is resized.
window.grid_rowconfigure(0, weight=1)    #Header
window.grid_rowconfigure(1, weight=4)    #Main content
window.grid_rowconfigure(2, weight=1)    #Buttons
window.grid_columnconfigure(0, weight=1) #Left frame
window.grid_columnconfigure(1, weight=2) #Right frame

#Header Images:
image_1 = CTkImage(Image.open("1.png"), size=(920, 200))
image_label_1 = CTkLabel(window, image=image_1, text=" ") 
image_label_1.grid(row=0, column=0, columnspan=2, sticky="nw")

image_2 = CTkImage(Image.open("2.png"), size=(920, 200))
image_label_2 = CTkLabel(window, image=image_2, text=" ") 
image_label_2.grid(row=0, column=1, columnspan=1, sticky="ne")

################################################################Left Frame######################################################################################
left_frame = CTkFrame(window, fg_color="dark sea green")
left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

#Configuring rows and columns in the left frame:
for i in range(6): #it configures 6 rows in the left frame.
    left_frame.grid_rowconfigure(i, weight=1) #each row is given wt=1, which equally shares the vertical space within left frame.(when left frame is resized, all 6 rows will resize proportionally based on the given ht)
left_frame.grid_columnconfigure(0, weight=1)  #column 0(left clolumn) takes 1 part of horizontal space.
left_frame.grid_columnconfigure(1, weight=2)  #right column takes 2 parts(takes twice space as left column)

#Labels: 
id_label = CTkLabel(left_frame, text='Id', font=('aerial', 20, 'bold'), text_color='gray23')
id_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

name_label = CTkLabel(left_frame, text='Name', font=('aerial', 20, 'bold'), text_color='gray23')
name_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

phone_label = CTkLabel(left_frame, text='Phone', font=('aerial', 20, 'bold'), text_color='gray23')
phone_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

role_label = CTkLabel(left_frame, text='Role', font=('aerial', 20, 'bold'), text_color='gray23')
role_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

gender_label = CTkLabel(left_frame, text='Gender', font=('aerial', 20, 'bold'), text_color='gray23')
gender_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

salary_label = CTkLabel(left_frame, text='Salary', font=('aerial', 20, 'bold'), text_color='gray23')
salary_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

#Entries and comboboxes:
id_entry = CTkEntry(left_frame, fg_color='white', text_color='black', height=33)
id_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

name_entry = CTkEntry(left_frame, fg_color='white', text_color='black', height=33)
name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

phone_entry = CTkEntry(left_frame, fg_color='white', text_color='black', height=33)
phone_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

role_options = ['Business Analyst', 'Cloud Architect', 'Relational Manager', 'Data Scientist', 'DevOps Engineer', 'IT consultant',
                'Network Engineer', 'Software Engineer', 'UX/UI Designer', 'Web Developer']
role_box = CTkComboBox(left_frame, values=role_options, state='readonly', fg_color='white', text_color='black', height=33)
role_box.grid(row=3, column=1, padx=20, pady=10, sticky="ew")
role_box.set(role_options[0])

gender_options = ['Male', 'Female', 'Others']
gender_box = CTkComboBox(left_frame, values=gender_options, state='readonly', fg_color='white', text_color='black', height=33)
gender_box.grid(row=4, column=1, padx=20, pady=10, sticky="ew")
gender_box.set(gender_options[0])

salary_entry = CTkEntry(left_frame, fg_color='white', text_color='black', height=33)
salary_entry.grid(row=5, column=1, padx=20, pady=10, sticky="ew")

#######################################################################Right Frame#######################################################################################
right_frame = CTkFrame(window, fg_color="gray70", height=70)
right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
right_frame.grid_columnconfigure(0, weight=1) #Makes sure that the frame can expand to fill available space in the column.

#Search and buttons:
search_box = CTkComboBox(right_frame, values=['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary'], state='readonly', fg_color='white', text_color='black', height=35)
search_box.set('Search By')#sets the box with the text 'Search By'.
search_box.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

search_Entry = CTkEntry(right_frame, fg_color='white', text_color='black', height=35)
search_Entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

search_button = CTkButton(right_frame, text="Search", height=35)
search_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

showall_button = CTkButton(right_frame, text="Show All", command=show_all, height=35)
showall_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

#Treeview: Using for loop to place all headings in tree through grid placement method.
column = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')
tree = ttk.Treeview(right_frame, columns=column, show='headings', height=44)
for i in column:
    tree.heading(i, text=i)
    tree.column(i, anchor=CENTER, width=120)
tree.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=0, pady=0)

#Styling the tree:
style = ttk.Style()

#Changing font of treeview heading:
style.configure('Treeview.Heading', font=("Arial", 20, "bold"))   #Set font size for headings.
style.configure('Treeview', font=('Arial', 16))  #Set font size for rows.

#Linking the scrollbar to the Treeview:
scrollbar = ttk.Scrollbar(right_frame, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)  #It will set scrollbar size according to the number of data in the treeview.
scrollbar.grid(row=1, column=4, sticky="ns", padx=1) 
scrollbar.configure(command=tree.yview)       #It will link scrollbar to the tree.

#It lifts scrollbar infront of the treeview.
scrollbar.lift()

##################################################################Bottom Frame (Buttons)#################################################################################
button_frame = CTkFrame(window, fg_color="dark sea green")
button_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10) 

new_button = CTkButton(button_frame, text='New employee', height=37)
new_button.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
button_frame.grid_columnconfigure(0, weight=1)

add_button = CTkButton(button_frame, text='Add Employee', height=37)
add_button.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
button_frame.grid_columnconfigure(1, weight=1)

update_button = CTkButton(button_frame, text='Update Employee', height=37)
update_button.grid(row=0, column=2, padx=20, pady=10, sticky="ew")
button_frame.grid_columnconfigure(2, weight=1)

delete_button = CTkButton(button_frame, text='Delete Employee', height=37)
delete_button.grid(row=0, column=3, padx=20, pady=10, sticky="ew")
button_frame.grid_columnconfigure(3, weight=1)

deleteall_button = CTkButton(button_frame, text='Delete All', height=37)
deleteall_button.grid(row=0, column=4, padx=20, pady=10, sticky="ew")
button_frame.grid_columnconfigure(4, weight=1)

window.mainloop()