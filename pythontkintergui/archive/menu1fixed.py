# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:32:38 2024

@author: wayne
"""

import tkinter as tk
from tkinter import Menu

def set_light_mode():
    # Dummy function for setting light mode
    print("Setting light mode")

def set_dark_mode():
    # Dummy function for setting dark mode
    print("Setting dark mode")

def main():
    window = tk.Tk()
    window.title("My Tkinter App")

    # Create a menu bar
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # Create a "Theme" menu
    theme_menu = Menu(menu_bar, tearoff=0)
    theme_menu.add_command(label="Light", command=set_light_mode)
    theme_menu.add_command(label="Dark", command=set_dark_mode)

    # Add the "Theme" menu to the menu bar
    menu_bar.add_cascade(label="Theme", menu=theme_menu)

    # Continue setting up your application (directory selectors, etc.)

    window.mainloop()

if __name__ == "__main__":
    main()
