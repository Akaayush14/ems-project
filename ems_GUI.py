from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
from database import *

window = CTk()

#Fullscreen window:
def maximize_window():
    window.state('zoomed')
window.after(10, maximize_window)

#Background colour of window:                               
window.configure(fg_color="cadet blue")

#Window title:
window.title("Employee Management System")

#GUI image:
image_1 = CTkImage(Image.open("GUI image 1.png"), size=(920, 200))
image_label_1 = CTkLabel(window, image=image_1, text=" ", fg_color="white", width=920, height=200)  # Set width and height here
image_label_1.place(x=0, y=0, anchor="nw") 

image_2 = CTkImage(Image.open("GUI image 2.png"), size=(920, 200))
image_label_2 = CTkLabel(window, image=image_2, text=" ", fg_color="white", width=920, height=200)  # Set width and height here
image_label_2.place(relx=1.0, y=0, anchor="ne")

################################################################Left frame(frame-1)######################################################################################
left_frame = CTkFrame(window, fg_color="cadet blue", width=940, height=600)
left_frame.place(x=10, y=210)  # Positioned below image_label_1

#Labels: 
id_label = CTkLabel(left_frame, text='Id', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
id_label.place(x=60, y=45)

name_label = CTkLabel(left_frame, text='Name', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
name_label.place(x=60, y=140)

phone_label = CTkLabel(left_frame, text='Phone', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
phone_label.place(x=60, y=235)

role_label = CTkLabel(left_frame, text='Role', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
role_label.place(x=60, y=330)

gender_label = CTkLabel(left_frame, text='Gender', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
gender_label.place(x=60, y=425)

salary_label = CTkLabel(left_frame, text='Salary', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
salary_label.place(x=60, y=520)

#Entries and comboboxes:
id_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
id_entry.place(x=230, y=40)

name_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
name_entry.place(x=230, y=135)

phone_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
phone_entry.place(x=230, y=230)

role_options = ['Business Analyst', 'Cloud Architect', 'Relational Manager', 'Data Scientist', 'DevOps Engineer', 'IT consultant', 'Network Engineer', 'Software Engineer', 'UX/UI Designer', 'Web Developer']
role_box = CTkComboBox(left_frame, values=role_options, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', state='readonly', width=300, height=45)
role_box.place(x=230, y=325)
role_box.set(role_options[0])

gender_options = ['Male', 'Female', 'Others']
gender_box = CTkComboBox(left_frame, values=gender_options, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', state='readonly', width=300, height=45)
gender_box.place(x=230, y=420)
gender_box.set(gender_options[0])

salary_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
salary_entry.place(x=230, y=515)

#####################################################################Right frame(frame-2)################################################################################
right_frame = CTkFrame(window, fg_color="light grey", width=1090, height=700)
right_frame.place(x=590, y=210)  # Positioned below image_label_2

#Entries and comboboxes:
search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
search_box = CTkComboBox(right_frame, values=search_options, font=('helvetica', 15, 'bold'), fg_color='white', text_color='black', state='readonly', width=200)
search_box.place(x=30, y=10)
search_box.set('Search By')

search_Entry = CTkEntry(right_frame, font=('helvetica', 15, 'bold'), fg_color='white', text_color='black', width=200)
search_Entry.place(x=300, y=10)

#Buttons:
search_button = CTkButton(right_frame, text="Search", width=200)
search_button.place(x=575, y=10)

showall_button = CTkButton(right_frame, text="Show All", width=200)
showall_button.place(x=850, y=10)

#Accessing scrollbar class:
scrollbar = ttk.Scrollbar(right_frame, orient=VERTICAL)
scrollbar.place(x=1605, y=71)

#Adding a tree:
tree = ttk.Treeview(right_frame, height=13, yscrollcommand=scrollbar.set)
tree.place(x=4, y=70, width=1600, height=871)

# Configure the scrollbar to scroll the Treeview
scrollbar.config(command=tree.yview)  # This links the scrollbar to the vertical scroll of the treeview

#Columns in tree:
tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')

#Headings in tree:
tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

#Process to remove extra columns:
tree.config(show='headings')

#Changing widths of columns:
tree.column('Id', width=140)
tree.column('Name', width=160)
tree.column('Phone', width=160)
tree.column('Role', width=200)
tree.column('Gender', width=140)
tree.column('Salary', width=140)

#Styling the tree:
style = ttk.Style()

#Changing font of treeview heading:
style.configure('Treeview.Heading', font=("aerial", 18, "bold"))

###########################################################################Below frame(Frame-3)##########################################################################
button_frame = CTkFrame(window, fg_color="cadet blue", width=1870, height=80)
button_frame.place(x=10, y=840)  # Positioned at the bottom

#Buttons:
new_button = CTkButton(button_frame, text='New Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
new_button.place(x=50, y=10)

add_button = CTkButton(button_frame, text='Add Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
add_button.place(x=400, y=10)

update_button = CTkButton(button_frame, text='Update Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
update_button.place(x=750, y=10)

delete_button = CTkButton(button_frame, text='Delete Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
delete_button.place(x=1100, y=10)

deleteall_button = CTkButton(button_frame, text='Delete All', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
deleteall_button.place(x=1420, y=10)

window.mainloop()