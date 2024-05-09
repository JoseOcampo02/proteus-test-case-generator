# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:58:03 2024

@author: wayne
"""

import tkinter as tk

window = tk.Tk()
window.title("My Tkinter App")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

def click_function():
    # Code to execute when button is clicked
    print("Button clicked!")


button = tk.Button(window, text="Click Me", command=click_function)
button.pack()


# ... (widget creation)
button.configure(command=click_function)

window.mainloop()
