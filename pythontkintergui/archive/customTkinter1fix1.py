# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:52:06 2024

@author: wayne
"""

import customtkinter as ctk
import time

# Define functions for button clicks
def hi_click():
    print("Hi!")

def bye_click():
    print("Bye!")

def choose_directory():
    # Implement your directory selection logic here
    print("Directory chosen")

# Initialize the main window
app = ctk.CTk()
app.geometry("400x300")
app.title("CustomTkinter Example")

# Set light/dark mode toggle
mode_var = ctk.IntVar(value=0)  # 0: light, 1: dark

def toggle_mode():
    mode = mode_var.get()
    if mode == 0:
        ctk.set_appearance_mode("dark")
        mode_var.set(1)
    else:
        ctk.set_appearance_mode("light")
        mode_var.set(0)

mode_button = ctk.CTkButton(
    master=app, text="Toggle Mode (Light/Dark)", command=toggle_mode
)
mode_button.pack(pady=10)

# Create buttons
hi_button = ctk.CTkButton(master=app, text="Hi", command=hi_click)
hi_button.pack(pady=10)

bye_button = ctk.CTkButton(master=app, text="Bye", command=bye_click)
bye_button.pack(pady=10)

directory_button = ctk.CTkButton(
    master=app, text="Choose Directory", command=choose_directory
)
directory_button.pack(pady=10)

# Create slider
slider_value = ctk.DoubleVar()

def slider_changed(value):
    print(f"Slider value: {value:.2f}")

slider = ctk.CTkSlider(
    master=app,
    from_=0.0,
    to=10.0,
    command=slider_changed,
    variable=slider_value,
)
slider.pack(pady=10)

# Create progress bar
progress_bar = ctk.CTkProgressBar(master=app)
progress_bar.pack(pady=10)

# Simulate progress
start_time = time.time()  # Time when the loop starts
total_time = 100  # Total desired simulation time in seconds

for i in range(101):
    # Calculate progress based on elapsed time
    elapsed_time = time.time() - start_time
    progress = (elapsed_time / total_time) * 100

    # Set progress bar value
    progress_bar.set(progress)

    # Update the GUI (important for smooth progress bar update)
    app.update()

    # Small delay to simulate some work being done
    time.sleep(0.01)  # Adjust sleep time as needed for your application

# Start the main event loop
app.mainloop()
