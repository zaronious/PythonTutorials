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
myLabel = Label(root, text="Hello World!")

# Shoving it to the screen
myLabel.pack()

# Creates the loop that will run until the program ends
root.mainloop()