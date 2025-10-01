import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Toplevel, Text, Button

root = tk.Tk()  # Creates a blank window
root.title("Tkinter AI GUI")
root.resizable(False, False)
root.geometry("560x460")  # Window size

# Color theme
root.configure(bg="light blue")
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background = 'blue', foreground = 'white')
style.map('TButton', background=[('active','red')])

# Test functions
def doSomething():
    print("Do something!")
def getSelection():
    print("Selected:", selectedItem.get())

def show_help():
    # Create a new top-level window for the help text
    help_window = Toplevel()
    help_window.title("About")
    help_window.geometry("500x400")  # Set a reasonable size

    # Create a Text widget with word wrapping
    help_text = Text(help_window, wrap="word", width=60, height=20, padx=10, pady=10)
    help_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Insert the docstring text here
    docstring = """
    Hit137: Team Dan_Ext40

    Assignment 3

    Program: GUI.py

    Authors: Andrew Morris, Kudzaishe Mutyasira

    Last date modified: 26/09/25
    """

    help_text.insert("1.0", docstring)
    help_text.config(state="disabled")  # Make it read-only

    # Add an OK button to close the window
    ok_button = Button(help_window, text="OK", command=help_window.destroy)
    ok_button.pack(pady=10)
    ok_button.config(bg="blue", fg="white")

# Browse button 
def browseFile():
    path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All supported", "*.png *.jpg *.jpeg *.bmp *.txt *.wav *.mp3"), ("All files", "*.*")]
    )
    if path:
        outputBox.insert("end", f"Selected file: {path}\n"); outputBox.see("end")

# Create label 
label1 = Label(root, text="Model Selection:")
label1.pack()  # Places this widget inside the window
label1.place(x=0, y=5)  # Position with x,y coordinates

# Create Menu 
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)

menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open File ", command=browseFile)
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
editMenu.add_command(label="About", command=show_help)

# Combo box 
options = ["Text-to-Image", "Image-to-Image"]
selectedItem = tk.StringVar()  # Create a StringVar to holdthe selected item

# Create the Combobox
combobox = ttk.Combobox(root, textvariable=selectedItem, values=options)
combobox.set("Text-to-Image")
combobox.pack()
combobox.place(x=100,y=5)

# Create button 
loadModelbut = tk.Button(root, text="Load Model", command=getSelection, fg="white", bg="blue")
loadModelbut.place(x=250,y=5, width=120, height=20)

# User Input Section
from tkinter import filedialog  # for the Browse button

left_box = ttk.Labelframe(root, text="User Input Section")
left_box.place(x=10, y=60, width=330, height=220)

# radios inside the group
var = IntVar()
var.set(1)
rb_text  = ttk.Radiobutton(left_box, text="Text",  variable=var, value=1, command=doSomething)
rb_image = ttk.Radiobutton(left_box, text="Image", variable=var, value=2, command=doSomething)
rb_text.place(x=10, y=8)
rb_image.place(x=90, y=8)

# Create browse button
browseBtn = ttk.Button(left_box, text="Browse", command=browseFile)
browseBtn.place(x=250, y=5)

# input text area
inputText = tk.Text(left_box)
inputText.place(x=10, y=36, width=310, height=120)

# action buttons row
run1Btn  = ttk.Button(left_box, text="Run Model 1", command=doSomething)
run2Btn  = ttk.Button(left_box, text="Run Model 2", command=doSomething)
clearBtn = ttk.Button(left_box, text="Clear", command=lambda: outputBox.delete("1.0","end"))
run1Btn.place(x=10,  y=165, width=100)
run2Btn.place(x=120, y=165, width=100)
clearBtn.place(x=230, y=165, width=90)

# Model Output Section (group box)
right_box = ttk.Labelframe(root, text="Model Output Section")
right_box.place(x=350, y=60, width=200, height=220)

ttk.Label(right_box, text="Output Display:").place(x=10, y=6)
outputBox = tk.Text(right_box)
outputBox.place(x=10, y=26, width=180, height=170)

# Model Information & Explanation
info_box = ttk.Labelframe(root, text="Model Information & Explanation")
info_box.place(x=10, y=290, width=540, height=150)

# Selected Model Info
ttk.Label(info_box, text="Selected Model Info:").place(x=10, y=8)
modelNameLbl = ttk.Label(info_box, text="• Model Name: idk", anchor="w")
modelCatLbl  = ttk.Label(info_box, text="• Category idk: (choose)", anchor="w")
modelDescLbl = ttk.Label(info_box, text="• Short Description: idk.", anchor="w")
modelNameLbl.place(x=10, y=30)
modelCatLbl.place(x=10,  y=52)
modelDescLbl.place(x=10, y=74)

#OOP Concepts Explanation
ttk.Label(info_box, text="OOP Concepts Explanation:").place(x=285, y=8)
oopLbl = ttk.Label(
    info_box,
    text=(
        "• Where Multiple Inheritance is used\n"
        "• Why Encapsulation was applied\n"
        "• How Polymorphism & Method Overriding are shown\n"
        "• Where Multiple Decorators are applied"
    ),
    justify="left"
)
oopLbl.place(x=285, y=30) 

root.mainloop() # Keeps the window open, the close button breaks the lo



