# -----------------------------------------------------------------------------
# Authors: Wayne Rasmussen
# Date:    05/10/2024
# -----------------------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
from hsm_options_box import HSMOptionsBox
from directory_selector import DirectorySelector
from ptg import run_ptg  # Ensure ptg.py is accessible for this import to work
import json
import os

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("COMP 491 Proteus Test Generator")
        self.master.geometry("800x600")

        self.hsm_options = HSMOptionsBox(self.master)
        self.input_directory_selector = DirectorySelector(self.master, "Input Directory:")
        self.output_directory_selector = DirectorySelector(self.master, "Output Directory:")

        self.setup_menus()
        self.setup_buttons()

    def setup_menus(self):
        menu_bar = tk.Menu(self.master)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        quick_actions_menu = tk.Menu(menu_bar, tearoff=0)
        quick_actions_menu.add_command(label="New Quick Action", command=self.new_quick_action)
        quick_actions_menu.add_command(label="Open Quick Action", command=self.open_quick_action)
        quick_actions_menu.add_command(label="Save Quick Action", command=self.save_quick_action)
        quick_actions_menu.add_command(label="Delete Quick Action", command=self.delete_quick_action)
        quick_actions_menu.add_command(label="Unset Settings", command=self.unset_settings)
        menu_bar.add_cascade(label="Quick Actions", menu=quick_actions_menu)

        self.master.config(menu=menu_bar)

    def setup_buttons(self):
        print_settings_btn = tk.Button(self.master, text="Print Settings", command=self.print_settings)
        print_settings_btn.pack(side=tk.BOTTOM, pady=5)

        run_ptg_btn = tk.Button(self.master, text="Run PTG", command=self.convert_and_run_ptg_settings)
        run_ptg_btn.pack(side=tk.BOTTOM, pady=5)

    def print_settings(self):
        settings = self.get_settings()
        print("Current Settings:", settings)

    def convert_and_run_ptg_settings(self):
        settings = self.get_settings()
        run_ptg(**settings)

    def get_settings(self):
        hsm_settings = self.hsm_options.get_user_modified_values()
        input_dir = self.input_directory_selector.get_selected_directory()
        output_dir = self.output_directory_selector.get_selected_directory()

        settings = {'hsm_options': hsm_settings}
        if input_dir:
            settings['input_directory'] = input_dir
        if output_dir:
            settings['output_directory'] = output_dir

        return settings

    def new_quick_action(self):
        self.hsm_options.reset()
        self.input_directory_selector.set_selected_directory('')
        self.output_directory_selector.set_selected_directory('')
        print("New quick action configuration is ready.")

    def save_quick_action(self):
        settings = self.get_settings()
        filename = filedialog.asksaveasfilename(defaultextension=".qaf", filetypes=[("Quick Action Files", "*.qaf")])
        if filename:
            with open(filename, 'w') as f:
                json.dump(settings, f)
            messagebox.showinfo("Save Quick Action", "Quick action saved successfully.")

    def open_quick_action(self):
        filename = filedialog.askopenfilename(filetypes=[("Quick Action Files", "*.qaf")])
        if filename:
            with open(filename) as f:
                settings = json.load(f)
            self.apply_settings(settings)
            messagebox.showinfo("Open Quick Action", "Quick action loaded successfully.")

    def delete_quick_action(self):
        filename = filedialog.askopenfilename(filetypes=[("Quick Action Files", "*.qaf")])
        if filename and messagebox.askyesno("Delete Quick Action", "Are you sure you want to delete this quick action?"):
            os.remove(filename)
            messagebox.showinfo("Quick Action Deleted", "Your quick action has been deleted.")

    def unset_settings(self):
        self.hsm_options.reset()
        self.input_directory_selector.set_selected_directory('')
        self.output_directory_selector.set_selected_directory('')
        messagebox.showinfo("Unset Settings", "All settings have been reset to defaults.")

    def apply_settings(self, settings):
        if 'hsm_options' in settings:
            self.hsm_options.set_values(settings['hsm_options'])
        if 'input_directory' in settings:
            self.input_directory_selector.set_selected_directory(settings['input_directory'])
        if 'output_directory' in settings:
            self.output_directory_selector.set_selected_directory(settings['output_directory'])