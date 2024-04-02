import tkinter as tk

class ToggleButton:
    def __init__(self, parent):
        self.state = tk.StringVar(value="On")
        self.button = tk.Button(parent, textvariable=self.state, command=self.toggle)
        self.button.pack(pady=5)

    def toggle(self):
        self.state.set("Off" if self.state.get() == "On" else "On")
