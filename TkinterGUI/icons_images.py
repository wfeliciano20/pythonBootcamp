from tkinter import Tk, Button, Label
import PIL as pillow
from PIL import ImageTk, Image

root = Tk()
root.title("Icon,Images & exit buttons")
# root.iconbitmap()

quit_button = Button(root, text="Exit Program", command=root.quit)
quit_button.pack()

my_img = ImageTk.PhotoImage(Image.open("mario_PNG57.png"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
