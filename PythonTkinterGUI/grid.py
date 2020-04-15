#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:58:07 2020

@author: zaron
"""

from tkinter import *

# The following line must always be the first line when using TKinter
root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Zaron Gibson")

# Shoving it to the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Creates the loop that will run until the program ends
root.mainloop()