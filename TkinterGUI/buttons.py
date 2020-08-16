from tkinter import *


def my_click():
    my_label = Label(root, text="Look I clicked a Button!!")
    my_label.pack()


root = Tk()


disabled_button = Button(root, text="Click Me!", state=DISABLED)

my_button = Button(root, text="Click Me too!", command=my_click)

disabled_button.pack()
my_button.pack()

root.mainloop()
