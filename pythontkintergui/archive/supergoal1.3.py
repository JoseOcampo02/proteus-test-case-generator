# SUPERGOAL1.3: Tkinter application demonstrating menus, theme switching, fullscreen window, and exit functionality

import tkinter as tk
from tkinter import Menu

def apply_theme(mode):
    colors = {
        "light": {"bg": "white", "fg": "black", "menu_bg": "light gray", "button_bg": "light gray"},
        "dark": {"bg": "gray20", "fg": "white", "menu_bg": "dark gray", "button_bg": "dark gray"}
    }
    theme = colors.get(mode, colors["light"])
    window.config(bg=theme["bg"])
    for menu in [file_menu, edit_menu, view_menu, settings_menu]:
        menu.config(bg=theme["menu_bg"], fg=theme["fg"])
    save_mode(mode)

def save_mode(mode):
    with open("mode_setting.txt", "w") as file:
        file.write(mode)

def load_mode():
    try:
        with open("mode_setting.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "light"

def set_light_mode():
    apply_theme("light")
    print("Light mode selected and applied")

def set_dark_mode():
    apply_theme("dark")
    print("Dark mode selected and applied")

def dummy_feature():
    print("This is a placeholder action")

def exit_application():
    window.destroy()
    print("Application exited")

def main():
    global window, file_menu, edit_menu, view_menu, settings_menu
    window = tk.Tk()
    window.title("Demonstration Application")

    # Set window size to full screen
    window.state('zoomed')

    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # File Menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=dummy_feature)
    file_menu.add_command(label="Open", command=dummy_feature)
    file_menu.add_command(label="Save", command=dummy_feature)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_application)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Edit Menu
    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Undo", command=dummy_feature)
    edit_menu.add_command(label="Redo", command=dummy_feature)
    edit_menu.add_command(label="Cut", command=dummy_feature)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # View Menu
    view_menu = Menu(menu_bar, tearoff=0)
    view_menu.add_command(label="Zoom In", command=dummy_feature)
    view_menu.add_command(label="Zoom Out", command=dummy_feature)
    view_menu.add_command(label="Default View", command=dummy_feature)
    menu_bar.add_cascade(label="View", menu=view_menu)

    # Settings Menu with Theme Submenu
    settings_menu = Menu(menu_bar, tearoff=0)
    theme_submenu = Menu(settings_menu, tearoff=0)
    theme_submenu.add_command(label="Light", command=set_light_mode)
    theme_submenu.add_command(label="Dark", command=set_dark_mode)
    settings_menu.add_cascade(label="Select Theme", menu=theme_submenu)
    menu_bar.add_cascade(label="Settings", menu=settings_menu)

    # Load the saved theme mode and apply it
    current_mode = load_mode()
    apply_theme(current_mode)

    window.mainloop()

if __name__ == "__main__":
    main()
