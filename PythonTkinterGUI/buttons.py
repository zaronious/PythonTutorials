#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:58:07 2020

@author: zaron
"""

from tkinter import *

# The following line must always be the first line when using TKinter
root = Tk()

# Function for button action
def myClick():
    myLabel = Label(root, text="Look, I clicked the button")
    myLabel.pack()

# Create a button
myButton = Button(root, text="Click Me!", padx=50, pady=50, fg="blue", bg="red", command=myClick)

# Display on the screen
myButton.pack()

# Creates the loop that will run until the program ends
root.mainloop()