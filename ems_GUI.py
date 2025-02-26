from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox


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

#Header image:
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