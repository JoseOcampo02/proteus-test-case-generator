#Argparse Test
import argparse
import datetime
import random
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog
import sys
import SafeTestGenerator
from SafeTestGenerator import *
from handler import bruh
#from reloading import reloading
import string

# Handling Arguments
parser = argparse.ArgumentParser()

# Modal Changing
parser.add_argument("-G", "--GUI", action="store_true",help="Enables GUI", required=False)
parser.add_argument("-S", "--Shell", action="store_true", help="Enables Shell",required=False)

#Debug Mode
parser.add_argument("-D", "--Debug", action="store_true", help="Enters debug mode", required=False)

# Toggleables
parser.add_argument("-event", "--EventCount", nargs='?', default=1, type = int, help = "# of Events", required=False)
parser.add_argument("-const", "--GlobalConstCount", nargs='?', default=1, type = int, help = "# of Global Consts Variables", required=False)
parser.add_argument("-func", "--FuncCount", nargs='?', default=1, type = int, help = "# of Functions", required=False)
parser.add_argument("-actItem", "--ActorItems", nargs='?', default=1, type = int, help = "# of Item in an Actor", required=False)
parser.add_argument("-act", "--ActorsNum", nargs='?', default=1, type = int, help = "# of Actors", required=False)
parser.add_argument("-state", "--StateNum", nargs='?', default=1, type = int, help = "# of States", required=False)
parser.add_argument("-uV", "--UnsafeVariableDeclare", action="store_true", help = "Disables safe variable assignments", required=False)
parser.add_argument("-uE", "--UnsafeEvent", action="store_true", help = "Disable safe events assignment", required=False)
parser.add_argument("-depth", "--MaxStateDepth", nargs='?', default=1,  type = int, help = "Maximum # of Nested States", required=False)
parser.add_argument("-dR", "--DirectoryHandler", action='store_true', help = "Uses Directory Handler to store multilple tests", required=False)


args = parser.parse_args()


#Toggleables


 

# Main Shell
def shell():
    print("Please type the 'help' command for command list.")
    while True:
        command = str(input("$ "))
        match command:
            case "exit":
                print("exiting program...")
                sys.exit()
            case "help":
                print("help - to list available commands")
                print("exit - to close the program")
                print("setPath - to set Paths ")
                print("CodeGen - to generate proteus code")
                print("CompileSwift - to compile proteus code in swift")
                print("GUI - Change to GUI")
            case "GUI":
                print("To return to shell, please close the GUI window")
                GUI()
            case "setPath":
                print("temp")
            case "CodeGen":
                print("temp")
            case "CompileSwift":
                print("temp")
            case _:
                print("Unrecognized Command, please type 'help' to list valid commands.")

# GUI Methods

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

def GUI():
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



def SetArgsToggleable():
    if args.EventCount != SafeTestGenerator.event_count:
        SafeTestGenerator.event_count = args.EventCount
    if args.GlobalConstCount != SafeTestGenerator.global_const_count:
       SafeTestGenerator.global_const_count = args.GlobalConstCount
    if args.FuncCount != SafeTestGenerator.func_count:
        SafeTestGenerator.func_count = args.FuncCount
    if args.ActorItems != SafeTestGenerator.actor_item_count:
        SafeTestGenerator.actor_item_count = args.ActorItems
    if args.ActorsNum != SafeTestGenerator.actor_count:
        SafeTestGenerator.actor_count = args.ActorsNum
    if args.StateNum != SafeTestGenerator.state_item_count:
        SafeTestGenerator.state_item_count = args.StateNum
    if args.UnsafeVariableDeclare:
        SafeTestGenerator.safe_var_assign = False
    if args.UnsafeEvent:
        SafeTestGenerator.safe_event_calling = False
    if args.MaxStateDepth != max_state_depth:
        SafeTestGenerator.max_state_depth = args.MaxStateDepth

    if args.Debug:
        print("EC: " + str(SafeTestGenerator.event_count) + " GCC: "+ str(SafeTestGenerator.global_const_count) + " FC:"+ str(SafeTestGenerator.func_count) + " AItemC: "+ str(SafeTestGenerator.actor_item_count) +" AC: " + str(SafeTestGenerator.actor_count) + " SItemC: "+ str(SafeTestGenerator.state_item_count) + " SafeVar: " + str(SafeTestGenerator.safe_var_assign) + " SafeEvent: " + str(SafeTestGenerator.safe_event_calling)+ " MSD: " + str(SafeTestGenerator.max_state_depth))
        printProtey()    
    if args.DirectoryHandler:
        bruh()

def main():
    #print("-h, --help for flags descriptions")
    # GUI Selection
    if args.GUI:
        GUI()

    #Shell Selection
    if args.Shell:
       shell()


    SetArgsToggleable()

main()