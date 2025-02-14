
from tkinter import *
root = Tk()

#Title:
root.title("Login")
root.iconbitmap("Employee.ico")

#Geometry of window:
root.geometry("825x500+420+230") #+300 --> the top left corner will be 300 pixels from the left, +200 --> it will  be 200 pixels below from the top of the screen.
root.resizable(False,False)

#Background colour of window:
root.config(bg = "#fff") #fff-white,#000 -black, root.config is used to change the background colour of window


#Framing:
f1 = Frame(root,width = 300, height = 300,bg = "linen")
f1.place(x = 450,y = 110)


#Headings
Headings_1 = Label(root,text = "Employee Management System",fg = "cadet blue",bg = "white",font = "Palatino 17 bold")
Headings_1.place(x = 70,y = 34)

Headings_2 = Label(root,text = "Good to see you again!",fg = "LightSlateBlue",bg = "white",font = "Palatino 16 bold")
Headings_2.place(x = 450,y = 34)

Headings_3 = Label(root,text = "Log in to your account",fg = "Black",bg = "white",font = "cosmicon 10")
Headings_3.place(x = 452,y = 70)

#Username_heading inside frame:
Headings_4 = Label(root,text = "Username:",fg = "gray20",bg = "linen",font = "Helvetica 13 bold")
Headings_4.place(x = 460,y = 115)


#Password_heading inside frame:
Headings_5 = Label(root,text =  "Password:",fg = "gray20",bg = "linen",font = "Helvetica 13 bold")
Headings_5.place(x = 460,y = 180)

Headings_6 = Label(root,text = "Don't have an account?",fg = "black",bg = "linen",font = "Microsoft 10",border = 0)
Headings_6.place(x = 462,y = 288)

Headings_7 = Label(root,text = "@powered by-TEAM FALCON",fg = "Black",bg = "white",font = "cosmicon 8")
Headings_7.place(x = 350,y = 479)

#Variable storing data entered as entries:
username_var = StringVar()
password_var = StringVar()

#Username entry box:
username_entry = Entry(root,width = 23,fg = "black",bg = "white",font = "Aerial 8",border = 2,relief = "ridge")
username_entry.place(x = 462,y = 145)

#Password entry box:
password_entry = Entry(root,width = 23,fg = "black",bg = "white",font = "Aerial 8",border = 2,relief = "ridge")
password_entry.place(x = 462,y = 210)








#Background  image of window:
bg_image=PhotoImage(file="Login page bg 3.png")
bg_image_label = Label(image=bg_image,bg="white").place(x = 20,y = 105)

EMS_icon = PhotoImage(file = "EMS.png")
EMS_icon_label = Label(image = EMS_icon,bg="white").place(x = 10,y = 30)


#Buttons:
b1 = Button(root,text = "Log in ",fg = "burlywood",bg = "white",font = "Palatino 10 bold",border = 2,relief = "ridge")
b1.place(x = 462,y = 250)

b2 = Button(root,text = "Register account",fg = "burlywood",bg = "white",font = "Palantino 10 bold")
b2.place(x = 610,y = 285)

#for mouse cursor 
def mouse_near(n):
    n.widget.config(bg ="red")#when cursor came near it change the colour to red
    

def mouse_far(n):
   n.widget.config(bg="white")#it reset the colour when cursor goes far
    

b1.bind("<Enter>",mouse_near)
b1.bind("<Leave>",mouse_far)
b2.bind("<Enter>",mouse_near)
b2.bind("<Leave>",mouse_far)




root.mainloop()




