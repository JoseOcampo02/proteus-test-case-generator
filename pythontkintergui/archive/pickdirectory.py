# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:17:18 2024

@author: wayne
"""

import tkinter as tk
from tkinter import filedialog

def browse_directory():
  """Opens a directory selection dialog and updates the entry field."""
  selected_directory = filedialog.askdirectory()
  if selected_directory:
    entry.delete(0, tk.END)  # Clear existing text
    entry.insert(0, selected_directory)  # Update with selected directory

window = tk.Tk()
window.title("Directory Selection")

label = tk.Label(window, text="Selected directory:")
label.pack()

entry = tk.Entry(window)
entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack()

window.mainloop()
