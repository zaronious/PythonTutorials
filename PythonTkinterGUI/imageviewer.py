from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("@./firefoxnightly-8.xbm")

my_img1 = ImageTk.PhotoImage(Image.open("./images/1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("./images/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("./images/3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("./images/4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("./images/5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
current_image = 0


def forward():
    global my_label
    global current_image

    current_image += 1
    if current_image > 4:
        current_image = 0

    updateui()


def back():
    global my_label
    global current_image

    current_image -= 1
    if current_image < 0:
        current_image = 4

    updateui()


def updateui():
    my_label = Label(image=image_list[current_image])
    my_label.grid(row=0, column=0, columnspan=3)

    image_label = Label(
        text="Image " + str((current_image + 1)) + " of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E,
    )
    image_label.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=5)

updateui()

root.mainloop()
