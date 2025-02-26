from customtkinter import *
from PIL import Image
from tkinter import ttk

window = CTk()
#Fullscreen window:
def maximize_window():
    window.state('zoomed')
window.after(10, maximize_window)

#Background colour of window:                               
window.configure(fg_color="cadet blue")

#Window title:
window.title("Employee Management System")

window.grid_rowconfigure(0, weight=0)  # Prevents image from resizing
window.grid_rowconfigure(1, weight=1)  # Allows left_frame and right_frame to take space
window.grid_rowconfigure(2, weight=0)  # Keeps button_frame at bottom without affecting row 0

#GUI image:
image_1 = CTkImage(Image.open("1.png"), size=(920, 200))
image_label_1 = CTkLabel(window, image=image_1, text=" ", fg_color="white", width=920, height=200) 
image_label_1.grid(row=0, column=0, sticky="nw", columnspan=2)


image_2 = CTkImage(Image.open("2.png"), size=(920, 200))
image_label_2 = CTkLabel(window, image=image_2, text=" ", fg_color="white", width=920, height=200) 
image_label_2.place(relx=1, rely=0, anchor="ne")

################################################################Left frame(frame-1)######################################################################################
left_frame = CTkFrame(window, fg_color="cadet blue", width=940, height=600)
left_frame.grid(row=1, column=0, sticky="nsew", padx=8, pady=10)

#Labels: 
id_label = CTkLabel(left_frame, text='Id', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
id_label.grid(row=0, column=0, padx=55, pady=27)

name_label = CTkLabel(left_frame, text='Name', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
name_label.grid(row=1, column=0, padx=55, pady=27)

phone_label = CTkLabel(left_frame, text='Phone', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
phone_label.grid(row=2, column=0, padx=55, pady=27)

role_label = CTkLabel(left_frame, text='Role', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
role_label.grid(row=3, column=0, padx=55, pady=27)

gender_label = CTkLabel(left_frame, text='Gender', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
gender_label.grid(row=4, column=0, padx=55, pady=27)

salary_label = CTkLabel(left_frame, text='Salary', fg_color='cadet blue', text_color='white', font=('aerial', 20, 'bold'))
salary_label.grid(row=5, column=0, padx=55, pady=27)

#Entries and comboboxes:
id_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
id_entry.grid(row=0, column=1, padx=55, pady=27)

name_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
name_entry.grid(row=1, column=1, padx=55, pady=27)

phone_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
phone_entry.grid(row=2, column=1, padx=55, pady=27)

role_options = ['Business Analyst', 'Cloud Architect', 'Relational Manager', 'Data Scientist', 'DevOps Engineer', 'IT consultant', 'Network Engineer', 'Software Engineer', 'UX/UI Designer', 'Web Developer']
role_box = CTkComboBox(left_frame, values=role_options, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', state='readonly', width=300, height=45)
role_box.grid(row=3, column=1, padx=55, pady=27)
role_box.set(role_options[0])

gender_options = ['Male', 'Female', 'Others']
gender_box = CTkComboBox(left_frame, values=gender_options, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', state='readonly', width=300, height=45)
gender_box.grid(row=4, column=1, padx=55, pady=27)
gender_box.set(gender_options[0])

salary_entry = CTkEntry(left_frame, font=('helvetica', 18, 'bold'), fg_color='white', text_color='black', width=300, height=45)
salary_entry.grid(row=5, column=1, padx=55, pady=27)

#####################################################################Right frame(frame-2)################################################################################
right_frame = CTkFrame(window, fg_color="light grey")
right_frame.place(relx=0.35, rely=0.25, relwidth=0.64, relheight=0.63)

#Entries and comboboxes:
search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
search_box = CTkComboBox(right_frame, values=search_options, font=('helvetica', 15, 'bold'), fg_color='white', text_color='black', state='readonly', width=210)
search_box.grid(row=0, column=0, padx=25, pady=5)
search_box.set('Search By')

search_Entry = CTkEntry(right_frame, font=('helvetica', 15, 'bold'), fg_color='white', text_color='black', width=210)
search_Entry.grid(row=0, column=1, padx=35, pady=5)

#Buttons:
search_button = CTkButton(right_frame, text="Search", width=210)
search_button.grid(row=0, column=2, padx=30, pady=5)

showall_button = CTkButton(right_frame, text="Show All", width=210)
showall_button.grid(row=0, column=3, padx=30, pady=5)

#Adding a tree:
tree = ttk.Treeview(right_frame, height=38)
tree.grid(row=1, column=0, columnspan=4, sticky="nsew")

#Accessing scrollbar class:
scrollbar = ttk.Scrollbar(right_frame, orient=VERTICAL)
scrollbar.place(relx=0.984, relheight=1)

#Linking the scrollbar to the Treeview:
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=tree.yview)

#Bringing the scrollbar to the front:
scrollbar.lift()

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
tree.column('Id', anchor=CENTER, width=180)
tree.column('Name',width=180)
tree.column('Phone', width=180)
tree.column('Role', width=200)
tree.column('Gender', width=180)
tree.column('Salary', width=180)

#Styling the tree:
style = ttk.Style()

#Changing font of treeview heading:
style.configure('Treeview.Heading', font=("aerial", 18, "bold"))

# ###########################################################################Below frame(Frame-3)#########################################################################
button_frame = CTkFrame(window, fg_color="cadet blue")
button_frame.grid(row=2, column=0)  # Positioned at the bottom

#Buttons:
#Lambda function will make the function effective when new button is pressed, not when the code is run.
new_button = CTkButton(button_frame, text='New Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
new_button.grid(row=0, column=0, padx=75, pady=20)

add_button = CTkButton(button_frame, text='Add Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
add_button.grid(row=0, column=1, padx=70, pady=20)

update_button = CTkButton(button_frame, text='Update Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
update_button.grid(row=0, column=2, padx=70, pady=20)

delete_button = CTkButton(button_frame, text='Delete Employee', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
delete_button.grid(row=0, column=3, padx=70, pady=20)

deleteall_button = CTkButton(button_frame, text='Delete All', font=('aerial', 15, 'bold'), width=200, height=35, corner_radius=15)
deleteall_button.grid(row=0, column=4, padx=50, pady=20)

#It will ensure that frames and widgets scale correctly with different screen sizes.
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)


window.mainloop()