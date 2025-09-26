"""
Hit137: Team Dan_Ext40

Assignment 3

Program: GUI.py

Authors: Maharun Momo Islam, Moneya Islam, Andrew Morris, Kudzaishe Mutyasira

Last date modified: 26/09/25

"""


import tkinter as tk
from tkinter import *
from tkinter import ttk


root = tk.Tk()  # Creates a blank window
root.title("Tkinter AI GUI")
root.geometry("350x500")  # Window size

# Frame stuff
topFrame = tk.Frame(root)
middleFrame = tk.Frame(root)
bottomFrame = tk.Frame(root)

topFrame.pack()
middleFrame.pack()
bottomFrame.pack()


# Label stuff
theLabel1 = Label(root, text="Model Selection:")
theLabel1.pack()  # Places this widget inside the window
theLabel1.place(x=0, y=0)  # Position with x,y coordinates

# Test function stuff
def doSomething():
    print("Do something!")
def getSelection():
    print("Selected:", selectedItem.get())

# Menu stuff
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)

menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open File ", command=doSomething)
subMenu.add_command(label="Save", command=doSomething)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doSomething)

editMenu = Menu(menu)
menu.add_cascade(label="Models", menu=editMenu)
editMenu.add_command(label="AI Model 1", command=doSomething)
editMenu.add_command(label="AI Model 2", command=doSomething)

editMenu = Menu(menu)
menu.add_cascade(label="Help", menu=editMenu)

editMenu.add_command(label="AI Model 1", command=doSomething)
editMenu.add_command(label="AI Model 2", command=doSomething)
editMenu.add_command(label="About", command=doSomething)

# Combo box stuff
options = ["A", "B", "C", "D"]
selectedItem = tk.StringVar()  # Create a StringVar to holdthe selected item

# Create the Combobox
combobox = ttk.Combobox(root, textvariable=selectedItem, values=options)
combobox.set("Text-to-Image")
combobox.pack()
combobox.place(x=100,y=0)

# Button stuff
loadModelbut = tk.Button(root, text="Load Model", command=getSelection, fg="black", bg="grey")
loadModelbut.place(x=250,y=0)


root.mainloop() # Keeps the window open, the close button breaks the loop

