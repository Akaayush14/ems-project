#calling the on_closing fuction and here the predefined text will tell the tkinter to close the window.
root.protocol("WM_DELETE_WINDOW", on_closing)

#To show a confirmatory window closing message box:
root.protocol("on_closing") 