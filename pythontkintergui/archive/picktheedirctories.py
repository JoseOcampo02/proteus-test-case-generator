# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:21:58 2024

@author: wayne
"""

import tkinter as tk
from tkinter import filedialog

def browse_directory(entry_name):
  """Opens a directory selection dialog and updates the specified entry field."""
  selected_directory = filedialog.askdirectory()
  if selected_directory:
    entries[entry_name].delete(0, tk.END)  # Clear existing text
    entries[entry_name].insert(0, selected_directory)  # Update with selected directory

window = tk.Tk()
window.title("Directory Selection")

# Dictionary to store entry widgets for each directory
entries = {
    "input_dir": None,
    "output_dir": None,
    "logs_dir": None
}

# Labels and entry fields for each directory
for directory_name, label_text in [("Input", "Input Directory:"), ("Output", "Output Directory:"), ("Logs", "Logs Directory:")]:
  label = tk.Label(window, text=label_text)
  label.pack()

  entry = tk.Entry(window)
  entry.pack()
  entries[directory_name] = entry

# Buttons for each directory selection
for directory_name in entries.keys():
  button = tk.Button(window, text=f"Browse {directory_name}", command=lambda name=directory_name: browse_directory(name))
  button.pack()

window.mainloop()
