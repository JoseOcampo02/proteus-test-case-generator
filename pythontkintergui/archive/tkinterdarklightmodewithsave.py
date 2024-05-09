# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:24:09 2024

@author: wayne
"""

import tkinter as tk

# Function to set dark mode
def set_dark_mode():
    with open("mode.txt", "w") as file:
        file.write("dark")
    apply_mode("dark")

# Function to set light mode
def set_light_mode():
    with open("mode.txt", "w") as file:
        file.write("light")
    apply_mode("light")

# Function to apply the mode (dark or light)
def apply_mode(mode):
    if mode == "dark":
        window.config(bg="gray12")  # Dark background
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg="gray20", fg="white")
    else:
        window.config(bg="white smoke")  # Light background
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg="light gray", fg="black")

# Read the saved mode from the file (if exists) and apply it
def read_and_apply_saved_mode():
    try:
        with open("mode.txt", "r") as file:
            mode = file.read().strip()
            apply_mode(mode)
    except FileNotFoundError:
        apply_mode("light")  # Default to light mode if file not found

window = tk.Tk()
window.title("Dark/Light Mode Example")

# Initialize mode from saved setting
read_and_apply_saved_mode()

# Dark mode button
dark_mode_button = tk.Button(window, text="Dark", command=set_dark_mode)
dark_mode_button.pack(pady=10)

# Light mode button
light_mode_button = tk.Button(window, text="Light", command=set_light_mode)
light_mode_button.pack(pady=10)

window.mainloop()
