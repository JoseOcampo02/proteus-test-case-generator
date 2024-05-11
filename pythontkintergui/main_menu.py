# -----------------------------------------------------------------------------
# Authors: Wayne Rasmussen
# Date:    05/10/2024
# -----------------------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

def save_quick_action(settings, window):
    filename = filedialog.asksaveasfilename(parent=window, defaultextension=".qaf", filetypes=[("Quick Action Files", "*.qaf")])
    if filename:
        with open(filename, 'w') as f:
            json.dump(settings, f)

def open_quick_action(window, apply_settings_callback):
    filename = filedialog.askopenfilename(parent=window, filetypes=[("Quick Action Files", "*.qaf")])
    if filename:
        with open(filename, 'r') as f:
            settings = json.load(f)
        apply_settings_callback(settings)
        messagebox.showinfo("Quick Action Loaded", "Settings have been loaded successfully.", parent=window)

def delete_quick_action(window):
    filename = filedialog.askopenfilename(parent=window, filetypes=[("Quick Action Files", "*.qaf")])
    if filename and messagebox.askyesno("Delete Quick Action", "Are you sure you want to delete this quick action?", parent=window):
        os.remove(filename)
        messagebox.showinfo("Quick Action Deleted", "The quick action file has been deleted.", parent=window)

def setup_main_menu(window, settings_getter, apply_settings_callback):
    menu_bar = tk.Menu(window)
    
    # File menu with corrected exit command
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=window.destroy)  # Corrected to use destroy
    menu_bar.add_cascade(label="File", menu=file_menu)
    
    # Quick Actions menu
    quick_actions_menu = tk.Menu(menu_bar, tearoff=0)
    quick_actions_menu.add_command(label="New", command=lambda: save_quick_action(settings_getter(), window))
    quick_actions_menu.add_command(label="Save", command=lambda: save_quick_action(settings_getter(), window))
    quick_actions_menu.add_command(label="Open", command=lambda: open_quick_action(window, apply_settings_callback))
    quick_actions_menu.add_command(label="Delete", command=lambda: delete_quick_action(window))
    menu_bar.add_cascade(label="Quick Actions", menu=quick_actions_menu)
    
    window.config(menu=menu_bar)

# Example usage within a Tkinter application context
if __name__ == "__main__":
    def dummy_settings_getter():
        # Dummy function for demonstration
        return {"example_setting": True}

    def dummy_apply_settings(settings):
        # Dummy function for demonstration
        print("Applying settings:", settings)

    root = tk.Tk()
    root.title("Quick Actions Example")
    root.geometry("600x400")

    setup_main_menu(root, dummy_settings_getter, dummy_apply_settings)

    root.mainloop()
