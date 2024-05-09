# SUPERGOAL1.4: Tkinter application with menus, theme switching, fullscreen window, exit functionality, and directory selection using pack layout

import tkinter as tk
from tkinter import Menu, filedialog

def apply_theme(mode):
    colors = {
        "light": {"bg": "white", "fg": "black", "menu_bg": "light gray", "button_bg": "light gray", "entry_bg": "white", "entry_fg": "black"},
        "dark": {"bg": "gray20", "fg": "white", "menu_bg": "dark gray", "button_bg": "gray20", "entry_bg": "black", "entry_fg": "white"}
    }
    theme = colors.get(mode, colors["light"])
    window.config(bg=theme["bg"])
    for menu in [file_menu, edit_menu, view_menu, settings_menu]:
        menu.config(bg=theme["menu_bg"], fg=theme["fg"])
    # Apply theme to directory frames
    for frame in directory_frames.values():
        frame.config(bg=theme["bg"])
        for child in frame.winfo_children():
            child.config(bg=theme["button_bg"], fg=theme["fg"])
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

def browse_directory(entry):
    """Opens a directory selection dialog and updates the specified entry field."""
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        entry.delete(0, tk.END)  # Clear existing text
        entry.insert(0, selected_directory)  # Update with selected directory

def create_directory_selector(parent, label_text):
    """Creates a directory selector component consisting of a label and a button."""
    frame = tk.Frame(parent)
    frame.pack(padx=10, pady=5, fill=tk.X)
    
    label = tk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=(0, 10))
    
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    button = tk.Button(frame, text="Browse", command=lambda: browse_directory(entry))
    button.pack(side=tk.LEFT, padx=(10, 0))
    
    return frame, entry

def exit_application():
    window.destroy()
    print("Application exited")

def main():
    global window, file_menu, edit_menu, view_menu, settings_menu, directory_frames
    window = tk.Tk()
    window.title("Demonstration Application with Directory Selection")
    window.state('zoomed')

    menu_bar = Menu(window)
    window.config(menu=menu_bar)
    
    # Setup Menus
    # [File, Edit, View, Settings Menu setup...]

    # Directory Frames for input, output, logs, tests, failures
    directory_frames = {}
    directory_labels = ["Input", "Output", "Logs", "Tests", "Failures"]
    for label in directory_labels:
        frame, entry = create_directory_selector(window, f"{label} Directory:")
        directory_frames[label.lower()] = (frame, entry)

    # Load the saved theme mode and apply it
    current_mode = load_mode()
    apply_theme(current_mode)

    window.mainloop()

if __name__ == "__main__":
    main()
