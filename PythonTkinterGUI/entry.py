#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:58:07 2020

@author: zaron
"""

from tkinter import *

# The following line must always be the first line when using TKinter
root = Tk()

# Create and display entry box
e=Entry(root, width=50, bg="blue", fg="white", borderwidth=10)
e.pack()
e.insert(0, "Enter your name: ")

# Function for button action
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

# Create a button
myButton = Button(root, text="Enter Your Name", fg="blue", bg="red", command=myClick)

# Display on the screen
myButton.pack()

# Creates the loop that will run until the program ends
root.mainloop()