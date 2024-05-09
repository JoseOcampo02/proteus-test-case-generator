# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:51:14 2024

@author: wayne
"""

import tkinter as tk
from tkinter import Menu

def apply_theme(mode):
    """Apply the theme to the application, iterating over child widgets to apply theme settings."""
    colors = {
        "light": {"bg": "white smoke", "fg": "black", "menu_bg": "light gray", "button_bg": "light gray", "entry_bg": "white", "entry_fg": "black"},
        "dark": {"bg": "gray12", "fg": "white", "menu_bg": "dark gray", "button_bg": "gray20", "entry_bg": "black", "entry_fg": "white"}
    }
    theme_colors = colors.get(mode, colors["light"])  # Default to light theme if mode is unknown

    window.config(bg=theme_colors["bg"])  # Apply background color to the main window

    # Iterate over all child widgets and apply theme colors
    for widget in window.winfo_children():
        widget_type = type(widget)
        if widget_type == tk.Label or widget_type == tk.Button:
            widget.config(bg=theme_colors["button_bg"], fg=theme_colors["fg"])
        elif widget_type == tk.Entry:
            widget.config(bg=theme_colors["entry_bg"], fg=theme_colors["entry_fg"])
        # Add conditions for other widget types as needed

    save_mode(mode)

def save_mode(mode):
    """Save the selected mode to a file."""
    with open("mode_setting.txt", "w") as file:
        file.write(mode)

def load_mode():
    """Load the saved mode from a file."""
    try:
        with open("mode_setting.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "light"  # Default to light mode if file not found

def set_light_mode():
    apply_theme("light")
    print("Light mode selected and saved")

def set_dark_mode():
    apply_theme("dark")
    print("Dark mode selected and saved")

def main():
    global window
    window = tk.Tk()
    window.title("Tkinter Menu Example with Theme Saving")

    # Load and apply saved theme
    current_mode = load_mode()
    apply_theme(current_mode)

    # Create a menu bar
    global menu_bar
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # Settings menu with a theme submenu
    settings_menu = Menu(menu_bar, tearoff=0)
    theme_submenu = Menu(settings_menu, tearoff=0)
    theme_submenu.add_command(label="Light", command=set_light_mode)
    theme_submenu.add_command(label="Dark", command=set_dark_mode)
    settings_menu.add_cascade(label="Select Theme", menu=theme_submenu)
    menu_bar.add_cascade(label="Settings", menu=settings_menu)

    window.config(menu=menu_bar)

    window.mainloop()

if __name__ == "__main__":
    main()
