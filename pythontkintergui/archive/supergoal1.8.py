# SUPERGOAL1.8: Tkinter application with directory selection, HSM Options, and a Dropdown Menu.

import tkinter as tk
from tkinter import ttk  # For the Combobox

def dummy_action(feature_name):
    def action():
        print(f"{feature_name} action triggered")
    return action

def create_menus(window):
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=window.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    for menu_name in ["Edit", "View", "Help"]:
        menu = tk.Menu(menu_bar, tearoff=0)
        for feature_num in range(1, 4):
            menu.add_command(label=f"{menu_name} Feature {feature_num}", command=dummy_action(f"{menu_name} Feature {feature_num}"))
        menu_bar.add_cascade(label=menu_name, menu=menu)

def create_directory_selector(container, label_text):
    frame = tk.Frame(container, padx=5, pady=5)
    frame.pack(side=tk.TOP, fill=tk.X)
    
    tk.Label(frame, text=f"{label_text} Directory:").pack(side=tk.LEFT)
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    tk.Button(frame, text="Browse", command=lambda: print("Browsing directories...")).pack(side=tk.RIGHT)
    
    return frame

def main():
    global window
    window = tk.Tk()
    window.title("Tkinter Application with Enhanced UI")
    window.geometry("800x600")

    create_menus(window)

    directory_container = tk.Frame(window)
    directory_container.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

    for directory in ["Input", "Output", "Logs", "Tests", "Failures"]:
        create_directory_selector(directory_container, directory)

    hsm_frame = tk.LabelFrame(window, text="HSM Options", padx=5, pady=5)
    hsm_frame.pack(padx=10, pady=10, fill=tk.X, side=tk.LEFT, anchor="nw")

    for i in range(1, 5):
        tk.Checkbutton(hsm_frame, text=f"HSM Option {i}").pack(anchor="w")

    dropdown_frame = tk.Frame(window)
    dropdown_frame.pack(padx=10, pady=10, fill=tk.X, side=tk.LEFT, anchor="nw")

    tk.Label(dropdown_frame, text="Select an option:").pack(anchor="w")

    combo_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
    combobox = ttk.Combobox(dropdown_frame, values=combo_options, state="readonly")
    combobox.pack(anchor="w")
    combobox.current(0)

    window.mainloop()

if __name__ == "__main__":
    main()
