root.geometry("560x460")


# User Input Section
from tkinter import filedialog  # for the Browse button

left_box = ttk.Labelframe(root, text="User Input Section")
left_box.place(x=10, y=60, width=330, height=220)

# radios inside the group
var.set(1)
rb_text  = ttk.Radiobutton(left_box, text="Text",  variable=var, value=1, command=doSomething)
rb_image = ttk.Radiobutton(left_box, text="Image", variable=var, value=2, command=doSomething)
rb_text.place(x=10, y=8)
rb_image.place(x=90, y=8)

# Browse button 
def browseFile():
    path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All supported", "*.png *.jpg *.jpeg *.bmp *.txt *.wav *.mp3"), ("All files", "*.*")]
    )
    if path:
        outputBox.insert("end", f"Selected file: {path}\n"); outputBox.see("end")

browseBtn = ttk.Button(left_box, text="Browse", command=browseFile)
browseBtn.place(x=250, y=5)

# input text area
inputText = tk.Text(left_box)
inputText.place(x=10, y=36, width=310, height=120)

# action buttons row
run1Btn  = ttk.Button(left_box, text="Run Model 1", command=doSomething)
run2Btn  = ttk.Button(left_box, text="Run Model 2", command=doSomething)
clearBtn = ttk.Button(left_box, text="Clear",        command=lambda: outputBox.delete("1.0","end"))
run1Btn.place(x=10,  y=165, width=100)
run2Btn.place(x=120, y=165, width=100)
clearBtn.place(x=230, y=165, width=90)

#Model Output Section (group box)
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
