# SUPERGOAL1.9: Tkinter application with "HSM Options" box, dropdown menu, toggle button, and slider.

import tkinter as tk
from tkinter import ttk

def toggle_button():
    button_text.set("Off" if button_text.get() == "On" else "On")

def main():
    global window, button_text
    window = tk.Tk()
    window.title("Tkinter Application with Toggle Button and Slider")
    window.geometry("800x600")

    # Menu setup with dummy actions and an exit option
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=window.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # HSM Options Frame
    hsm_frame = tk.LabelFrame(window, text="HSM Options", padx=5, pady=5)
    hsm_frame.pack(padx=10, pady=10, fill=tk.X, side=tk.LEFT, anchor="nw")

    # Checkboxes for HSM Options
    for i in range(1, 5):
        tk.Checkbutton(hsm_frame, text=f"HSM Option {i}").pack(anchor="w")

    # Dropdown Menu (Combobox) below HSM Options
    dropdown_frame = tk.Frame(window)
    dropdown_frame.pack(padx=10, pady=10, fill=tk.X, side=tk.LEFT, anchor="nw")

    label = tk.Label(dropdown_frame, text="Select an option:")
    label.pack(anchor="w")

    combo_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
    combobox = ttk.Combobox(dropdown_frame, values=combo_options)
    combobox.pack(anchor="w")
    combobox.current(0)

    # Toggle Button under the HSM box
    button_text = tk.StringVar(value="On")
    toggle_button = tk.Button(window, textvariable=button_text, command=toggle_button)
    toggle_button.pack(pady=5)

    # Slider (Fun Bar) under the dropdown menu
    slider_label = tk.Label(window, text="Fun Bar:")
    slider_label.pack()
    fun_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal")
    fun_slider.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
