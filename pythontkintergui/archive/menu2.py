# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:37:12 2024

@author: wayne
"""

import tkinter as tk
from tkinter import Menu

def dummy_command():
    print("Placeholder action")

def set_light_mode():
    print("Light mode selected")

def set_dark_mode():
    print("Dark mode selected")

def main():
    window = tk.Tk()
    window.title("Tkinter Menu Example")

    # Create a menu bar
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # File menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=dummy_command)
    file_menu.add_command(label="Open", command=dummy_command)
    file_menu.add_command(label="Save", command=dummy_command)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Edit menu
    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Undo", command=dummy_command)
    edit_menu.add_command(label="Redo", command=dummy_command)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # View menu
    view_menu = Menu(menu_bar, tearoff=0)
    view_menu.add_command(label="Zoom In", command=dummy_command)
    view_menu.add_command(label="Zoom Out", command=dummy_command)
    menu_bar.add_cascade(label="View", menu=view_menu)

    # Settings menu with a theme submenu
    settings_menu = Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="Preferences", command=dummy_command)

    # Theme submenu
    theme_submenu = Menu(settings_menu, tearoff=0)
    theme_submenu.add_command(label="Light", command=set_light_mode)
    theme_submenu.add_command(label="Dark", command=set_dark_mode)
    settings_menu.add_cascade(label="Select Theme", menu=theme_submenu)

    menu_bar.add_cascade(label="Settings", menu=settings_menu)

    window.mainloop()

if __name__ == "__main__":
    main()
