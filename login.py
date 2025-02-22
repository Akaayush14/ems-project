from customtkinter import *
from PIL import Image
from tkinter import messagebox

def on_closing():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def login():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif username_entry.get() == 'falcon' and password_entry.get() == '1234':
        messagebox.showerror('Success', 'Successful login')
        root.destroy()
        import ems_GUI  
    else:
        messagebox.showerror('Error', 'Incorrect credentials!')

root = CTk()
#calling the on_closing fuction and here the predefined text will tell the tkinter to close the window.
root.protocol("WM_DELETE_WINDOW", on_closing)

#To show a confirmatory window closing message box:
root.protocol("on_closing") 

#Background colour of window:                               
root.configure(fg_color = "white")

#Window size:
root.geometry("900x500+650+300")
root.resizable(0,0)

#Window title:
root.title("Login")

#Login icon in window:
root.iconbitmap("Employee.ico")

#Background images: Firstly, importing the image.
image_1 = CTkImage(Image.open("login-image.png"), size = (375,365))
#Adding image to the label, and addint empty text to remove CTk text from images.
image_label_1 = CTkLabel(root, image = image_1, text = " ", fg_color = "white") 
image_label_1.place(x=50, y=80)

image_2 = CTkImage(Image.open("EMS.png"), size = (50,50))
image_label_2 = CTkLabel(root, image = image_2, text = " ", fg_color = "white")
image_label_2.place(x=20, y=30)

#Frame:
frame = CTkFrame(root, width=300, height=300, fg_color="linen", border_color = "white", corner_radius=10)
frame.place(x=550, y=100)

#Heading:
#Adding text in a label, like how we added image.
Heading_label_1 = CTkLabel(root, text = "Employee Management System", fg_color= "white", text_color ="DeepSkyBlue3", font = ("Goudy Old Style", 25 , "bold"))
Heading_label_1.place(x = 90, y = 40)

Heading_label_2 = CTkLabel(root, text = "Good to see you again!", fg_color= "white", text_color ="DeepSkyBlue3", font = ("Goudy Old Style", 26 , "bold"))
Heading_label_2.place(x = 568, y = 44)

#Entries:
username_entry = CTkEntry(root, placeholder_text = "Username", text_color = "black", width = 200, height = 35, fg_color = "white", border_color = "grey", border_width = 2)
username_entry.place(x = 580, y = 150)

password_entry = CTkEntry(root, placeholder_text = "Password", text_color = "black", width = 200, height = 35, fg_color = "white", border_color = "grey", border_width = 2, show = "*")
password_entry.place(x = 580, y = 210)

#Loading eye icons:
eye_open = CTkImage(light_image = Image.open("eye_open.png"), size = (20,20))
eye_closed = CTkImage(light_image = Image.open("eye_close.png"), size = (20,20))

#Function to Toggle Password Visibility
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")  # Show password
        toggle_button.configure(image=eye_closed)
    else:
        password_entry.configure(show="*")  # Hide password
        toggle_button.configure(image=eye_open)

# Eye Button to Toggle Password Visibility    
toggle_button = CTkButton(frame, text="", image=eye_open, width=30, height=30, fg_color="linen", command = toggle_password, hover = False)
toggle_button.place(x=227, y=113)

#Buttons:
login_button = CTkButton(root, text = "Login", width = 160, height = 35, cursor = 'hand2', command=login)
login_button.place(x = 600, y = 265)

root.mainloop()


