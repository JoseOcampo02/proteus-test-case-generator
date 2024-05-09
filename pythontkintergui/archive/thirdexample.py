# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:08:26 2024

@author: wayne
"""
import tkinter as tk

def left_click_pressed(event):
  print("Left button pressed!")

def left_click(event):
  print("Left button clicked!")

def right_click_function(event):
  print("Button right-clicked!")

window = tk.Tk()
window.title("Event Handling")

label = tk.Label(window, text="Click, right-click, or hold left-click on the button:")
label.pack()

button = tk.Button(window, text="Click Me")
button.pack()

# Bind events to the button
button.bind("<Button-1>", left_click_pressed)  # Bind left button press
button.bind("<ButtonRelease-1>", left_click)  # Bind left-click release
button.bind("<ButtonRelease-3>", right_click_function)  # Bind right-click release

window.mainloop()
