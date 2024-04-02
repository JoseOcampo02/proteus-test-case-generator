import tkinter as tk
from tkinter import ttk

class DropdownBox:
    def __init__(self, parent):
        self.var = tk.StringVar()
        self.combobox = ttk.Combobox(parent, textvariable=self.var, state="readonly",
                                     values=["Unique Item 1", "Unique Item 2", "Unique Item 3", "Unique Item 4", "Unique Item 5"])
        self.combobox.pack()
        self.combobox.bind("<<ComboboxSelected>>", self.on_select)

    def on_select(self, event=None):
        print(f"Selected: {self.var.get()}")
