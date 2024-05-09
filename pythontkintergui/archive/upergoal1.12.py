# SUPERGOAL1.12: Ensuring visibility of directory selection UI on the right side with organized left-side UI elements.

import tkinter as tk
from tkinter import ttk, filedialog  # Corrected to include filedialog import

def toggle_button_command():
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
    global window, button_text
    window = tk.Tk()
    window.title("Tkinter Application with Visible Directory Selection")
    window.geometry("800x600")

    # Left-side container for HSM Options, On/Off button, and Fun Slider
    left_container = tk.Frame(window)
    left_container.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    # HSM Options Frame within the left container
    hsm_frame = tk.LabelFrame(left_container, text="HSM Options", padx=5, pady=5)
    hsm_frame.pack(fill=tk.X)

    # Checkboxes for HSM Options
    for i in range(1, 5):
        tk.Checkbutton(hsm_frame, text=f"HSM Option {i}").pack(anchor="w")

    # Toggle Button below the HSM Options box
    button_text = tk.StringVar(value="On")
    toggle_btn = tk.Button(left_container, textvariable=button_text, command=toggle_button_command)
    toggle_btn.pack()

    # Fun Slider below the Toggle Button
    slider_label = tk.Label(left_container, text="Fun Bar:")
    slider_label.pack()
    fun_slider = ttk.Scale(left_container, from_=0, to=100, orient="horizontal")
    fun_slider.pack()

    # Right-side container for directory selection
    directory_container = tk.Frame(window)
    directory_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Directory selection UI
    directories = ["Input", "Output", "Logs", "Tests", "Failures"]
    for directory in directories:
        create_directory_selector(directory_container, directory)

    window.mainloop()

if __name__ == "__main__":
    main()
