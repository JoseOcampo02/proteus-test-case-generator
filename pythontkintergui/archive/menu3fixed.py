# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:43:28 2024

@author: wayne
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:41:48 2024

@author: wayne
"""

import tkinter as tk
from tkinter import Menu

def apply_theme(mode):
    """Apply the theme to the application."""
    if mode == "light":
        window.config(bg="white smoke")
        # For demonstration, setting the menu background directly
        # Note: Tkinter's default Menu widget may have limited styling options
        menu_bar.config(bg="light gray", fg="black")
    elif mode == "dark":
        window.config(bg="gray12")
        # Similarly, setting the menu for dark mode
        menu_bar.config(bg="dark gray", fg="white")
    
    # Update other widget styles here as needed
    # This is where you'd iterate over window.winfo_children() for widgets that support styling
    
    save_mode(mode)

def apply_theme(mode):
    """Apply the theme to the application."""
    if mode == "light":
        window.config(bg="white smoke")
        for widget in window.winfo_children():
            if isinstance(widget, (tk.Menu, tk.MenuItem)):
                widget.config(bg="light gray", fg="black")
    elif mode == "dark":
        window.config(bg="gray12")
        for widget in window.winfo_children():
            if isinstance(widget, (tk.Menu, tk.MenuItem)):
                widget.config(bg="gray20", fg="white")
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
    """Set the application to light mode."""
    apply_theme("light")
    print("Light mode selected and saved")

def set_dark_mode():
    """Set the application to dark mode."""
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
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # File menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=lambda: print("New File"))
    file_menu.add_command(label="Open", command=lambda: print("Open File"))
    file_menu.add_command(label="Save", command=lambda: print("Save File"))
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Edit menu
    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Undo", command=lambda: print("Undo Action"))
    edit_menu.add_command(label="Redo", command=lambda: print("Redo Action"))
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # View menu
    view_menu = Menu(menu_bar, tearoff=0)
    view_menu.add_command(label="Zoom In", command=lambda: print("Zooming In"))
    view_menu.add_command(label="Zoom Out", command=lambda: print("Zooming Out"))
    menu_bar.add_cascade(label="View", menu=view_menu)

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
