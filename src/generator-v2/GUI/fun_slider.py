import tkinter as tk
from tkinter import ttk

class FunSlider:
    def __init__(self, parent):
        self.label = tk.Label(parent, text="Fun Bar:")
        self.label.pack()
        self.slider = ttk.Scale(parent, from_=0, to=100, orient="horizontal")
        self.slider.pack()
