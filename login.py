dev
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
Headings_1.pack()

Headings_2 = Label(root,text = "Good to see you again!",fg = "LightSlateBlue",bg = "white",font = "Palatino 16 bold")
Headings_2.pack()

Headings_3 = Label(root,text = "Log in to your account",fg = "Black",bg = "white",font = "cosmicon 10")
Headings_3.pack()





root.mainloop()



main
