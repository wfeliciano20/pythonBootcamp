from tkinter import Tk, Button, Entry, END

root = Tk()
root.title("Simple Calculator")

text_input = Entry(root, width=35, borderwidth=5)
text_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def equal():
    second_number = text_input.get()
    text_input.delete(0, END)
    if math == "addition":
        text_input.insert(0, f_num + int(second_number))
    if math == "subtraction":
        text_input.insert(0, f_num - int(second_number))
    if math == "multiplication":
        text_input.insert(0, f_num * int(second_number))
    if math == "division":
        text_input.insert(0, f_num / int(second_number))


def add():
    first_number = text_input.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    text_input.delete(0, END)


def subtract():
    first_number = text_input.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    text_input.delete(0, END)


def multiply():
    first_number = text_input.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    text_input.delete(0, END)


def divide():
    first_number = text_input.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    text_input.delete(0, END)


def clear_text_input():
    text_input.delete(0, END)


def button_click(number):
    current = text_input.get()
    text_input.delete(0, END)
    text_input.insert(0, str(current) + str(number))


# Create the button with specific width and height
padx = 40
pady = 20
buttons = []

button_1 = Button(root, text=str(1), padx=padx, pady=pady,
                  command=lambda: button_click(str(1)))
buttons.append(button_1)
button_2 = Button(root, text=str(2), padx=padx, pady=pady,
                  command=lambda: button_click(str(2)))
buttons.append(button_2)
button_3 = Button(root, text=str(3), padx=padx, pady=pady,
                  command=lambda: button_click(str(3)))
buttons.append(button_3)
button_4 = Button(root, text=str(4), padx=padx, pady=pady,
                  command=lambda: button_click(str(4)))
buttons.append(button_4)
button_5 = Button(root, text=str(5), padx=padx, pady=pady,
                  command=lambda: button_click(str(5)))
buttons.append(button_5)
button_6 = Button(root, text=str(6), padx=padx, pady=pady,
                  command=lambda: button_click(str(6)))
buttons.append(button_6)
button_7 = Button(root, text=str(7), padx=padx, pady=pady,
                  command=lambda: button_click(str(7)))
buttons.append(button_7)
button_8 = Button(root, text=str(8), padx=padx, pady=pady,
                  command=lambda: button_click(str(8)))
buttons.append(button_8)
button_9 = Button(root, text=str(9), padx=padx, pady=pady,
                  command=lambda: button_click(str(9)))
buttons.append(button_9)
button_0 = Button(root, text=str(0), padx=padx, pady=pady,
                  command=lambda: button_click(str(0)))
buttons.append(button_0)

button_clear = Button(root, text='Clear', padx=87,
                      pady=20, command=clear_text_input)
button_add = Button(root, text='+', padx=39, pady=20, command=add)
button_subtract = Button(root, text='-', padx=41, pady=20, command=subtract)
button_multiply = Button(root, text='*', padx=40, pady=20, command=multiply)
button_divide = Button(root, text='/', padx=41, pady=20, command=divide)
button_equal = Button(root, text='=', padx=98, pady=20, command=equal)


# Position the buttons in the screen
buttons[9].grid(row=1, column=2)
buttons[8].grid(row=1, column=1)
buttons[7].grid(row=1, column=0)

buttons[6].grid(row=2, column=2)
buttons[5].grid(row=2, column=1)
buttons[4].grid(row=2, column=0)

buttons[3].grid(row=3, column=2)
buttons[2].grid(row=3, column=1)
buttons[1].grid(row=3, column=0)

buttons[0].grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
