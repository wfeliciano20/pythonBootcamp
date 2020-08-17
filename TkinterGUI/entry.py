from tkinter import *

root = Tk()

input_text = Entry(root, width=25)
input_text.pack()
input_text.insert(0, "Enter your name: ")


def my_click():
    greeting = f'Hello, {input_text.get()}'
    my_label = Label(root, text=greeting)
    my_label.pack()


my_button = Button(root, text='Enter', command=my_click)
my_button.pack()


root.mainloop()
