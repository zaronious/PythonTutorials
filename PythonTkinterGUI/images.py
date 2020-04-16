from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at Codemy.com')
root.iconbitmap('@./firefoxnightly-8.xbm')

my_img = ImageTk.PhotoImage(Image.open("./firefoxnightly.ico"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()