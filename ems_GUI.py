from customtkinter import *
from PIL import Image

window = CTk()

#Fullscreen window:
def maximize_window():
    window.state('zoomed')
window.after(10,maximize_window)

#Background colour of window:                               
window.configure(fg_color = "cadet blue")

#window title:
window.title("Employee Management System")

window.mainloop()