# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:18:49 2024

@author: wayne
"""

import tkinter as tk
from tkinter import filedialog

def create_directory_selector(parent, label_text, button_text, on_button_click):

    

    frame = tk.Frame(parent)
    frame.pack(pady=5)
    
    label = tk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=(0, 10))
    
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    button = tk.Button(frame, text=button_text, command=lambda: on_button_click(entry))
    button.pack(side=tk.LEFT, padx=(10, 0))
    
    return entry  # Return the entry widget if you need to access its value later

def browse_directory(entry):
    """Opens a directory selection dialog and updates the specified entry field."""
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        entry.delete(0, tk.END)  # Clear existing text
        entry.insert(0, selected_directory)  # Update with selected directory

window = tk.Tk()
window.title("Directory Selection")

# Create directory selectors
input_dir_entry = create_directory_selector(window, "Input Directory:", "Browse", browse_directory)
output_dir_entry = create_directory_selector(window, "Output Directory:", "Browse", browse_directory)
logs_dir_entry = create_directory_selector(window, "Logs Directory:", "Browse", browse_directory)

window.mainloop()

class DirectorySelector(tk.Frame):
    def __init__(self, parent, label_text, button_text, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack(pady=5)
        
        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.button = tk.Button(self, text=button_text, command=self.browse_directory)
        self.button.pack(side=tk.LEFT, padx=(10, 0))
    
    def browse_directory(self):
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected_directory)

# Usage
window = tk.Tk()
window.title("Directory Selection")

input_selector = DirectorySelector(window, "Input Directory:", "Browse")
output_selector = DirectorySelector(window, "Output Directory:", "Browse")
logs_selector = DirectorySelector(window, "Logs Directory:", "Browse")

