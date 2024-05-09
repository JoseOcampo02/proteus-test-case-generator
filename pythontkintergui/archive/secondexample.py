# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:10:22 2024

@author: wayne
"""

import tkinter as tk

window = tk.Tk()
window.title("Grid Layout")


label1 = tk.Label(window, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Label 2")
label2.grid(row=0, column=1)

button = tk.Button(window, text="Click Me")
button.grid(row=1, columnspan=2)  # Spans across two columns


window.mainloop()
