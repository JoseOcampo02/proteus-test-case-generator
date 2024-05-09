# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:27:51 2024

@author: wayne
"""

import customtkinter as ctk

def set_dark_mode():
    ctk.set_appearance_mode("dark")  # Assuming customTkinter has a similar function
    with open("mode.txt", "w") as file:
        file.write("dark")

def set_light_mode():
    ctk.set_appearance_mode("light")  # Assuming customTkinter has a similar function
    with open("mode.txt", "w") as file:
        file.write("light")

def read_and_apply_saved_mode():
    try:
        with open("mode.txt", "r") as file:
            mode = file.read().strip()
            ctk.set_appearance_mode(mode)  # Apply saved mode
    except FileNotFoundError:
        ctk.set_appearance_mode("light")  # Default to light mode

# Set up the GUI using customTkinter widgets
window = ctk.CTk()  # Assuming customTkinter uses a similar constructor
window.title("Dark/Light Mode Example with customTkinter")

read_and_apply_saved_mode()

# Create buttons for switching modes
dark_mode_button = ctk.CTkButton(window, text="Dark", command=set_dark_mode)
dark_mode_button.pack(pady=10)

light_mode_button = ctk.CTkButton(window, text="Light", command=set_light_mode)
light_mode_button.pack(pady=10)

window.mainloop()
