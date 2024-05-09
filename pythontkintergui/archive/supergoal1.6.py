# SUPERGOAL1.6: Tkinter application with directory selection layout and menu features, without dynamic resizing.

import tkinter as tk
from tkinter import Menu, filedialog

def dummy_action(feature_name):
    def action():
        print(f"{feature_name} action triggered")
    return action

def apply_theme(mode):
    print(f"Applying {mode} theme...")  # Placeholder for comprehensive theme application logic.

def browse_directory(entry):
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        entry.delete(0, tk.END)
        entry.insert(0, selected_directory)

def create_directory_selector(container, label_text):
    frame = tk.Frame(container, padx=5, pady=5)
    frame.pack(side=tk.TOP, fill=tk.X)
    
    label = tk.Label(frame, text=f"{label_text} Directory:")
    label.pack(side=tk.LEFT)
    
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    button = tk.Button(frame, text="Browse", command=lambda: browse_directory(entry))
    button.pack(side=tk.RIGHT)
    
    return frame

def create_menus(window):
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # File Menu with Exit option
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=lambda: window.quit())
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Placeholder for additional menus with dummy features
    menu_names = ["Edit", "View", "Help"]
    for menu_name in menu_names:
        menu = Menu(menu_bar, tearoff=0)
        for feature_num in range(1, 4):
            menu.add_command(label=f"{menu_name} Feature {feature_num}", command=dummy_action(f"{menu_name} Feature {feature_num}"))
        menu_bar.add_cascade(label=menu_name, menu=menu)

def main():
    global window
    window = tk.Tk()
    window.title("Tkinter Application with Menus and Directory Selection")
    window.geometry("800x600")  # Fixed window size

    create_menus(window)

    directory_container = tk.Frame(window)
    directory_container.pack(side=tk.RIGHT, fill=tk.Y, expand=True)

    directories = ["Input", "Output", "Logs", "Tests", "Failures"]
    for directory in directories:
        create_directory_selector(directory_container, directory)

    window.mainloop()

if __name__ == "__main__":
    main()
