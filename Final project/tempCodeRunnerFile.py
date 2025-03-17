from customtkinter import *
from PIL import Image
from tkinter import messagebox
from database import *
import employee_portal

def on_closing():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

#Function to call login function from database:
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == '' or password == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
        return

    user = check_login(username, password)  # Call database function
    if user:
        role = user[3]  # Role is stored in the 4th column
        messagebox.showinfo('Success', f'Successful login as {role}')
        root.withdraw()  # Hide the login window instead of destroying it

        if role == 'Admin':
            from admin_portal import admin_portal  # Import the Admin portal
            admin_portal()  # Open the admin portal
        elif role == 'Employee':
            from employee_portal import employee_portal  # Import the Employee portal
            employee_portal(username)  # Open the employee portal
    else:
        messagebox.showerror('Error', 'Incorrect credentials!')

######################################################################### Reset password window #########################################################################
def forgot_password():
    forgot_window = CTkToplevel(root)
    forgot_window.title("Forgot Password")
    forgot_window.geometry("400x300")
    forgot_window.resizable(0,0)
    forgot_window.configure(fg_color="white")

    #Labels:
    username_label = CTkLabel(forgot_window, text="Username: ", text_color='black', font=("aerial", 16, "bold"))
    username_label.place(x=20, y=50)

    email_label = CTkLabel(forgot_window, text="E-mail: ", text_color='black', font=("aerial", 16, "bold"))
    email_label.place(x=20, y=120)

    #Entries:
    username_entry = CTkEntry(forgot_window, fg_color='white', text_color='black', width=200, height=35)
    username_entry.place(x=130, y=50)

    email_entry = CTkEntry(forgot_window, fg_color='white', text_color='black', width=200, height=35)
    email_entry.place(x=130, y=120)

    def reset():
        username = username_entry.get()
        email = email_entry.get()
        new_password = "1234"  

        if reset_password(username, email, new_password): 
            messagebox.showinfo("Success", f"Password reset to: {new_password}")
        else:
            messagebox.showerror("Error", "Username or email not found!")

    #Button for resetting password:
    reset_button = CTkButton(forgot_window, text="Reset Password", command=reset, height=37)
    reset_button.place(x=160, y=190)

###################################################################### New account window #################################################################################
def create_account():
    register_window = CTkToplevel(root)

    #Function to open full screen window:
    def maximize_window():
        try:
            register_window.state('zoomed')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    #After 10 milliseconds the window will open in full screen.
    register_window.after(10, maximize_window)

    register_window.title("Create Account")
    register_window.geometry("400x400")
    register_window.configure(fg_color="white")
    
    #Frame:
    frame = CTkFrame(register_window, fg_color="linen", height=600, width=500)
    frame.place(x=600, y=150)

    #Labels:
    Register_heading_label_1 = CTkLabel(register_window, text="Employee Management System", fg_color="white", text_color="steel blue", font=("Goudy Old Style", 35, "bold"))
    Register_heading_label_1.place(x=630, y=90)

    Register_heading_label_2 = CTkLabel(register_window, text="Create a new account", fg_color="linen", text_color="black", font=("Arial", 25))
    Register_heading_label_2.place(x=710, y=160)

    username_label = CTkLabel(register_window, fg_color="linen", text_color="black", text="Username", font=("Arial", 18))
    username_label.place(x=630, y=250)

    password_label = CTkLabel(register_window, fg_color="linen", text_color="black", text="Password", font=("Arial", 18))
    password_label.place(x=630, y=355)

    email_label = CTkLabel(register_window, fg_color="linen", text_color="black", text="Email", font=("Arial", 18))
    email_label.place(x=630, y=460)

    role_label = CTkLabel(register_window, fg_color="linen", text_color="black", text="Role", font=("Arial", 18))
    role_label.place(x=630, y=565)

    #Entries:
    username_entry = CTkEntry(register_window, fg_color="white", text_color="black", width=250, height=37)
    username_entry.place(x=750, y=250)

    password_entry = CTkEntry(register_window, fg_color="white", text_color="black", width=250, height=37)
    password_entry.place(x=750, y=350)

    email_entry = CTkEntry(register_window, fg_color="white", text_color="black", width=250, height=37)
    email_entry.place(x=750, y=450)

    role_box = CTkComboBox(register_window, fg_color="white", text_color="black", values=["Admin", "Employee"], state="readonly", width=250, height=37)
    role_box.place(x=750, y=550)

    #Function for calling register function from database:
    def register():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        role = role_box.get()

        if not all([username, password, email, role]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if create_user(username, password, email, role): 
            messagebox.showinfo("Success", "Account created successfully!")
            register_window.destroy()
        else:
            messagebox.showerror("Error", "Failed to create account!")

    # Button for registering account:
    register_button = CTkButton(register_window, text="Register", width=250, height=37, command=register)
    register_button.place(x=750, y=640)

########################################################################### Login window ##################################################################################
root = CTk()

#Calling the on_closing function and here the predefined text will tell the tkinter to close the window.
root.protocol("WM_DELETE_WINDOW", on_closing)

#Background colour of window:                               
root.configure(fg_color="white")

#Window size:
root.geometry("900x500+650+300")
root.resizable(0, 0)

#Window title:
root.title("Login")

#Login icon in window:
root.iconbitmap("Employee.ico")

#Background images: Firstly, importing the image.
photo_1 = CTkImage(Image.open("image_1.png"), size=(375, 365))
# Adding image to the label, and adding empty text to remove CTk text from images.
photo_label_1 = CTkLabel(root, image=photo_1, text=" ", fg_color="white") 
photo_label_1.place(x=50, y=80)

photo_2 = CTkImage(Image.open("image_2.png"), size=(50, 50))
photo_label_2 = CTkLabel(root, image=photo_2, text=" ", fg_color="white")
photo_label_2.place(x=20, y=30)

#Frame:
frame = CTkFrame(root, width=300, height=300, fg_color="linen", border_color="white", corner_radius=10)
frame.place(x=550, y=100)

#Creating a button frame:
button_frame = CTkFrame(root, fg_color="white")
button_frame.place(x=550, y=400) 

#Heading:
#Adding text in a label, like how we added image.
Heading_label_1 = CTkLabel(root, text="Employee Management System", fg_color="white", text_color="DeepSkyBlue3", font=("Goudy Old Style", 25, "bold"))
Heading_label_1.place(x=90, y=40)

Heading_label_2 = CTkLabel(root, text="Good to see you again!", fg_color="white", text_color="DeepSkyBlue3", font=("Goudy Old Style", 26, "bold"))
Heading_label_2.place(x=568, y=44)

label_3 = CTkLabel(root, text="Don't have an account?", fg_color="linen", text_color="black", font=("Arial", 13))
label_3.place(x=583, y=330)

#Entries:
username_entry = CTkEntry(root, placeholder_text="Username", text_color="black", width=200, height=35, fg_color="white", border_color="grey", border_width=2)
username_entry.place(x=580, y=150)

password_entry = CTkEntry(root, placeholder_text="Password", text_color="black", width=200, height=35, fg_color="white", border_color="grey", border_width=2, show="*")
password_entry.place(x=580, y=210)

#Loading eye icons:
eye_open = CTkImage(light_image=Image.open("eye_open.png"), size=(20, 20))
eye_closed = CTkImage(light_image=Image.open("eye_close.png"), size=(20, 20))

#Function to toggle password visibility:
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")  
        toggle_button.configure(image=eye_closed)
    else:
        password_entry.configure(show="*")  
        toggle_button.configure(image=eye_open)

#Eye Button to toggle password visibility:   
toggle_button = CTkButton(frame, text="", image=eye_open, width=30, height=30, fg_color="linen", command=toggle_password, hover=False)
toggle_button.place(x=227, y=113)

#Labels and buttons:
login_button = CTkButton(root, text="Login", width=200, height=30, cursor='hand2', command=login)
login_button.place(x=580, y=280)

forgot_label = CTkLabel(root, text="Forgot Password?", text_color="steel blue", cursor="hand2", font=("Arial", 12, 'bold'), fg_color='linen')
forgot_label.place(x=674, y=245)
forgot_label.bind("<Button-1>", lambda e: forgot_password())

#Create Account Button (in the main login window)
create_account_label = CTkLabel(root, text="Create Account", text_color="steel blue", cursor="hand2", font=("Arial", 12, 'bold', 'underline'), fg_color='linen')
create_account_label.place(x=722, y=330)
create_account_label.bind("<Button-1>", lambda e: create_account())

root.mainloop()

