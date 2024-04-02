import tkinter as tk
from tkinter import filedialog

class DirectorySelector:
    def __init__(self, parent, label_text):
        self.parent = parent
        self.label_text = label_text

        # Create frame
        self.frame = tk.Frame(parent)
        self.frame.pack(fill=tk.X, padx=5, pady=5)

        # Label for directory selection
        self.label = tk.Label(self.frame, text=label_text)
        self.label.pack(side=tk.LEFT, padx=5)

        # Entry to display selected directory path
        self.path_entry = tk.Entry(self.frame)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Browse button to trigger directory selection dialog
        self.browse_button = tk.Button(self.frame, text="Browse", command=self.open_directory_dialog)
        self.browse_button.pack(side=tk.RIGHT, padx=5)

        # Unset button to clear the selected directory
        self.unset_button = tk.Button(self.frame, text="Unset", command=self.unset_directory)
        self.unset_button.pack(side=tk.RIGHT, padx=5)

    def open_directory_dialog(self):
        # Open dialog to select a directory
        directory = filedialog.askdirectory()
        if directory:  # If a directory is selected, update the entry with the path
            self.set_selected_directory(directory)

    def get_selected_directory(self):
        # Return the currently selected directory from the entry widget
        return self.path_entry.get()

    def set_selected_directory(self, directory):
        # Set the entry widget to display the selected directory path
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, directory)

    def unset_directory(self):
        # Clear the entry widget to remove the selected directory path
        self.path_entry.delete(0, tk.END)
