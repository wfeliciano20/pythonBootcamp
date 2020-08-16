from tkinter import *

root = Tk()

# Creating 2 label widgets
my_label1 = Label(root, text="Hello World")
my_lable2 = Label(root, text="My name is William Feliciano")
# positioning widgets on screen
my_label1.grid(row=0, column=0)
my_lable2.grid(row=1, column=0)

root.mainloop()
