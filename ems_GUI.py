from customtkinter import *
from PIL import Image
from tkinter import ttk

window = CTk()

#Fullscreen window:
def maximize_window():
    window.state('zoomed')
window.after(10,maximize_window)

#Background colour of window:                               
window.configure(fg_color = "cadet blue")

#window title:
window.title("Employee Management System")

#GUI image:
image_1 = CTkImage(Image.open("1.png"), size = (920,200))
image_label_1 = CTkLabel(window, image = image_1, text = " ", fg_color = "white") 
image_label_1.grid(row=0, column=0)

image_2 = CTkImage(Image.open("2.png"), size = (920,200))
image_label_2 = CTkLabel(window, image = image_2, text = " ", fg_color = "white") 
image_label_2.grid(row=0, column=1)

#Left frame:
left_frame = CTkFrame(window, fg_color = "cadet blue")
left_frame.grid(row=1, column=0)

#Label and entry inside left frame: 
id_label = CTkLabel(left_frame, text = 'Id', fg_color = 'cadet blue', text_color = 'white', font = ('aerial', 18, 'bold'))
id_label.grid(row=0, column=0, padx=20,  pady=15, sticky='w')

id_entry = CTkEntry(left_frame, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black', width = 180)
id_entry.grid(row=0, column=1)

name_label = CTkLabel(left_frame, text = 'Name', fg_color = 'cadet blue', text_color = 'white', font = ('aerial', 18, 'bold'))
name_label.grid(row=1, column=0, padx=20, pady=15, sticky='w')

name_entry = CTkEntry(left_frame, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black', width = 180)
name_entry.grid(row=1, column=1)

phone_label = CTkLabel(left_frame, text = 'Id', fg_color = 'cadet blue', text_color = 'white', font = ('aerial', 18, 'bold'))
phone_label.grid(row=2, column=0, padx=20, pady=15, sticky='w')

phone_entry = CTkEntry(left_frame, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black', width = 180)
phone_entry.grid(row=2, column=1)

role_label = CTkLabel(left_frame, text = 'Role', fg_color = 'cadet blue', text_color = 'white', font = ('aerial', 18, 'bold'))
role_label.grid(row=3, column=0, padx=20, pady=15, sticky='w')

role_options = ['Business Analyst', 'Cloud Architect', 'Relational Manager', 'Data Scientist', 'DevOps Engineer', 'IT consultant', 'Network Engineer', 'Software Engineer', 'UX/UI Designer', 'Web Developer',]
role_box = CTkComboBox(left_frame, values = role_options, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black', width = 180, state = 'readonly')
role_box.grid(row=3, column=1)
role_box.set(role_options[0])

gender_label = CTkLabel(left_frame, text = 'Gender', fg_color = 'cadet blue', text_color = 'white', font = ('aerial', 18, 'bold'))
gender_label.grid(row=4, column=0, padx=20, pady=15, sticky='w')

gender_options = ['Male', 'Female', 'Others']
gender_box = CTkComboBox(left_frame, values = gender_options, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black', width = 180, state = 'readonly')
gender_box.grid(row=4, column=1)
gender_box.set(gender_options[0])

salary_label = CTkLabel(left_frame, text = 'Salary', fg_color = 'cadet blue', text_color = 'white', font = ('aerial', 18, 'bold'))
salary_label.grid(row=5, column=0, padx=20, pady=15, sticky='w')

salary_entry = CTkEntry(left_frame, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black', width = 180)
salary_entry.grid(row=5, column=1)

#Right frame:
right_frame = CTkFrame(window, fg_color = "light grey")
right_frame.grid(row=1, column=1)

#Adding label and entry inside right frame:
search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
search_box = CTkComboBox(right_frame, values = search_options, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black', state = 'readonly')
search_box.grid(row=0, column=0)
search_box.set('Search By')

search_Entry = CTkEntry(right_frame, font = ('helvetica', 15, 'bold'), fg_color = 'white', text_color = 'black')
search_Entry.grid(row=0, column=1)

#Creating Buttons
search_button = CTkButton(right_frame, text = "Search", width = 100)
search_button.grid(row=0, column=2)

showall_button = CTkButton(right_frame, text = "Show All", width = 100)
showall_button.grid(row=0, column=3)

#Adding a tree:
tree = ttk.Treeview(right_frame, height = 43)
tree.grid(row=1, column = 0, columnspan=4)

#columns in tree:
tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')

#Headings in tree:
tree.heading('Id', text = 'Id')
tree.heading('Name', text = 'Name')
tree.heading('Phone', text = 'Phone')
tree.heading('Role', text = 'Role')
tree.heading('Gender', text = 'Gender')
tree.heading('Salary', text = 'Salary')

#Process to remove extra columns:
tree.config(show = 'headings')

#changing widths of columns:
tree.column('Id', width = 100)
tree.column('Name', width = 160)
tree.column('Phone', width = 160)
tree.column('Role', width = 200)
tree.column('Gender', width = 100)
tree.column('Salary', width = 100)

#Styling the tree:
style = ttk.Style()
style.configure('Treeview.Heading', font = ("Arial", 18, "bold"))

#Making frame and letting button to be added there:
button_frame = CTkFrame(window)
button_frame.grid(row=2, column = 0)

new_button = CTkButton(button_frame, text = 'New Employee', font = ('helvetica', 15, 'bold'), width = 160, corner_radius = 15)
new_button.grid(row=0, column=0, pady=5)


window.mainloop()