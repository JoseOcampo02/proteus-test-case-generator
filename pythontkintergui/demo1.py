# -----------------------------------------------------------------------------
# Authors: Wayne Rasmussen
# Date:    05/10/2024
# -----------------------------------------------------------------------------

# HSM frontend demo

import tkinter as tk
from tkinter import ttk, filedialog

def on_combobox_select(event=None):
    global dropdown_var
    print(f"Selected: {dropdown_var.get()}")

def toggle_button_command():
    global button_text
    button_text.set("Off" if button_text.get() == "On" else "On")

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

def main():
    global window, button_text, dropdown_var
    window = tk.Tk()
    window.title("Tkinter Application with Comprehensive Features")
    window.geometry("800x600")

    # Menu setup with dummy actions and an exit option
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=window.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Left-side container setup
    left_container = tk.Frame(window)
    left_container.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    # HSM Options Frame
    hsm_frame = tk.LabelFrame(left_container, text="HSM Options", padx=5, pady=5)
    hsm_frame.pack(fill=tk.X)

    # Checkboxes within HSM Options
    for i in range(1, 5):
        tk.Checkbutton(hsm_frame, text=f"HSM Option {i}").pack(anchor="w")

    # Toggle Button below HSM Options
    button_text = tk.StringVar(value="On")
    toggle_btn = tk.Button(left_container, textvariable=button_text, command=toggle_button_command)
    toggle_btn.pack()

    # Fun Slider below Toggle Button
    slider_label = tk.Label(left_container, text="Fun Bar:")
    slider_label.pack()
    fun_slider = ttk.Scale(left_container, from_=0, to=100, orient="horizontal")
    fun_slider.pack()

    # Dropdown Box below Fun Slider
    dropdown_label = tk.Label(left_container, text="Select an Option:")
    dropdown_label.pack()
    dropdown_var = tk.StringVar()
    dropdown = ttk.Combobox(left_container, textvariable=dropdown_var, state="readonly",
                            values=["Unique Item 1", "Unique Item 2", "Unique Item 3", "Unique Item 4", "Unique Item 5"])
    dropdown.pack()
    dropdown.bind("<<ComboboxSelected>>", on_combobox_select)

    # Right-side container for directory selection
    directory_container = tk.Frame(window)
    directory_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Directory selection UI elements
    directories = ["Input", "Output", "Logs", "Tests", "Failures"]
    for directory in directories:
        create_directory_selector(directory_container, directory)

    window.mainloop()

if __name__ == "__main__":
    main()
