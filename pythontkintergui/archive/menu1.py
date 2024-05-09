# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:29:55 2024

@author: wayne
"""

import tkinter as tk

def open_file():
    print("Open File...")

def save_file():
    print("Save File...")

def set_dark_theme():
    print("Setting Dark Theme...")

def set_light_theme():
    print("Setting Light Theme...")

window = tk.Tk()
window.title("Tkinter Application with Menu Bar")

# Create a menu bar
menu_bar = tk.Menu(window)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create a "Settings" menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Dark Theme", command=set_dark_theme)
settings_menu.add_command(label="Light Theme", command=set_light_theme)
menu_bar.add_cascade(label="Settings", menu=settings_menu)

# Configure the window to use the menu bar
window.config(menu=menu_bar)

window.mainloop()
