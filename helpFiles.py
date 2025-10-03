from tkinter import Toplevel, Text, Button

def helpModel1():
    # Create a new top-level window for the help text
    help_window = Toplevel()
    help_window.title("About")
    help_window.geometry("500x400")  # Set a reasonable size

    # Create a Text widget with word wrapping
    help_text = Text(help_window, wrap="word", width=60, height=20, padx=10, pady=10)
    help_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Docstring text
    docstring1 = """
    This is about AI model 1...
    """

    help_text.insert("1.0", docstring1)
    help_text.config(state="disabled")  # Make it read-only

    # Add an OK button to close the window
    ok_button = Button(help_window, text="OK", command=help_window.destroy)
    ok_button.pack(pady=10)
    ok_button.config(bg="blue", fg="white")

def helpModel2():
    # Create a new top-level window for the help text
    help_window = Toplevel()
    help_window.title("About")
    help_window.geometry("500x400")  # Set a reasonable size

    # Create a Text widget with word wrapping
    help_text = Text(help_window, wrap="word", width=60, height=20, padx=10, pady=10)
    help_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Docstring text
    docstring2 = """
    This is about AI model 2...
    """

    help_text.insert("1.0", docstring2)
    help_text.config(state="disabled")  # Make it read-only

    # Add an OK button to close the window
    ok_button = Button(help_window, text="OK", command=help_window.destroy)
    ok_button.pack(pady=10)
    ok_button.config(bg="blue", fg="white")

def helpAbout():
    # Create a new top-level window for the help text
    help_window = Toplevel()
    help_window.title("About")
    help_window.geometry("500x400")  # Set a reasonable size

    # Create a Text widget with word wrapping
    help_text = Text(help_window, wrap="word", width=60, height=20, padx=10, pady=10)
    help_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Docstring text
    docstring3 = """
    Hit137: Team Dan_Ext40

    Assignment 3

    Program: AI GUI.py

    Authors: Andrew Morris and Kudzaishe Mutyasira

    Last date modified: 3/10/25
    """

    help_text.insert("1.0", docstring3)
    help_text.config(state="disabled")  # Make it read-only

    # Add an OK button to close the window
    ok_button = Button(help_window, text="OK", command=help_window.destroy)
    ok_button.pack(pady=10)
    ok_button.config(bg="blue", fg="white")