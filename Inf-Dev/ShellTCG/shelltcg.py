#Argparse Test
import argparse
import datetime
import random
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog
import sys
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


args = parser.parse_args()


#Toggleables

event_count = 1
global_const_count = 1
func_count = 1
actor_count = 1
actor_item_count = 1
state_item_count = 1
safe_var_assign = True
safe_event_calling = True
max_state_depth = 1
 

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


# this jank ass code bro
def SetArgsToggleable():
    global event_count
    global global_const_count
    global func_count
    global actor_count
    global actor_item_count
    global state_item_count
    global safe_var_assign
    global safe_event_calling
    global max_state_depth
    

# I had no other coice fr
    if args.EventCount != event_count:
        event_count = args.EventCount
    if args.GlobalConstCount != global_const_count:
        global_const_count = args.GlobalConstCount
    if args.FuncCount != func_count:
        func_count = args.FuncCount
    if args.ActorItems != actor_item_count:
        actor_item_count = args.ActorItems
    if args.ActorsNum != actor_item_count:
        actor_count = args.ActorsNum
    if args.StateNum != actor_item_count:
        state_item_count = args.StateNum
    if args.UnsafeVariableDeclare:
        safe_var_assign = False
    if args.UnsafeEvent:
        safe_event_calling = False
    if args.MaxStateDepth != max_state_depth:
        max_state_depth = args.MaxStateDepth

    if args.Debug:
        print("EC: " + str(event_count) + " GCC: "+ str(global_const_count) + " FC:"+ str(func_count) + " AItemC: "+ str(actor_item_count) +" AC: " + str(actor_count) + " SItemC: "+ str(state_item_count) + " SafeVar: " + str(safe_var_assign) + " SafeEvent: " + str(safe_event_calling)+ " MSD: " + str(max_state_depth))
        
    printProtey()

def main():
    #print("-h, --help for flags descriptions")
    # GUI Selection
    if args.GUI:
        GUI()

    #Shell Selection
    if args.Shell:
       shell()
        
    SetArgsToggleable()



# jank ass combination
# All possible usable names, variables, etc.

# State name list
all_state_names = [
  "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
  "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
  "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
  "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New_Hampshire",
  "New_Jersey", "New_Mexico", "New_York", "North_Carolina", "North_Dakota", "Ohio",
  "Oklahoma", "Oregon", "Pennsylvania", "Rhode_Island", "South_Carolina", "South_Dakota",
  "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West_Virginia",
  "Wisconsin", "Wyoming"
]

# Actor name list
all_actor_names = [
  "Keanu_Reeves", "Danny_Devito", "Quentin_Tarantino", "Christoph_Waltz", "Arnold_Schwarzenegger",
  "Samuel_L_Jackson", "Rami_Malek", "Tom_Hanks", "Morgan_Freeman", "Bruce_Willis", "Daniel_Radcliffe",
  "Heath_Ledger", "Henry_Cavill"
]

# Variable name list
all_var_names = [
  "count", "timer", "check", "flag", "var", "key", "value", "add", "name", "nikto",
  "index", "scope", "numOfThings", "result", "data", "redeem", "hack", "isOn",
  "isOff", "area", "map", "foo", "something", "sum", "total", "id", "url", "item",
  "message", "config", "hydra", "script", "temp"
]

# Event name list
all_event_names = [
  "STOP", "GO", "LEFT", "RIGHT", "UP", "DOWN", "LIFT", "DROP", "LOOK",
  "OPEN", "CLOSE", "TURN", "SHOVE", "JUMP", "FALL", "REST", "ACTIVATE",
  "TERMINATE", "DESTROY", "SAVE", "BARK", "MEOW"
]

# Variable types
all_var_types = [
  "int", "string", "bool"
]

# Proteus exclusive types
all_proteus_var_types = [
    "state", "actor", "event", "statemachine"
]

# All possible string inputs
all_string_values = [
    "Proteus words and stuff", "Wiegley should give us an A", "Next CSUN strike when?",
    "Testing group is superior", "Here's a random string", "input, input, input, inputs!",
    "Help, I'm trapped in here", "stuff and fluff", "debug this code for a prize", "go touch grass",
    "When will we graduate?", "I'd like a free job please! No, I don't have job experience"
]

# Function names
all_function_names = [
    "do_this", "turn_on", "turn_off", "move_up", "move_down", "move_left", "move_right",
    "save_this", "delete_this", "kill_task", "start_task", "find_this", "start_clock",
    "end_clock", "check_this", "touch_grass", "meme_generator", "hack_the_bank",
    "job_finder"
]

# ------------------------------------------------- Utilities --------------------------------------------------------------------

# Pick a random number
rand_num = lambda x, y: random.randint(x, y)

# Random item from a list
rand_list_entry = lambda from_list: random.choice(from_list)

# Remove used name from list
remove_used_name = lambda name, name_list: name_list.remove(name)

# Check if list is empty
empty_checker = lambda check_list: True if(check_list) else None

# Clear everything...just like the name suggests
def clear(var_list, state_list, event_list, actor_list):
    var_list.clear()
    state_list.clear()
    event_list.clear()
    actor_list.clear()
    return ""

def make_args():
    args_list = []
    for _ in range(rand_num(1, 5)):
        args_list.append(rand_list_entry(all_var_types))
        args = ', '.join(args_list)
    return args

def indent(IC) -> str:
    indent_as_string = ""
    for _ in range (IC):
        indent_as_string += "    "
    return indent_as_string

# -------------------------------------------------------- Program start --------------------------------------------------------------

def printProtey():
    proteus_program = generate_program()
    print(proteus_program)

# Generates a proteus program as a string by repeatedly appending to a string

# Program: DefEvent* DefGlobalConst* DefFunc* DefActor+
def generate_program() -> str:
    # Start with an empty String
    program = ""

    # DefEvent*
    # Populate string with events
    for _ in range(rand_num(0, event_count)):
        program += generate_event()
    program += "\n"

    # DefGlobalConst*
    # Populate string with GlobalConstants
    for _ in range (rand_num(0, global_const_count)):
        program += generate_global_const()
    program += "\n"

    # Functions and Actors will require indentation henceforth.
    # IC (indentation counter) keeps track of indentation level
    # Depth keep track of how deeply nested the current state is
    IC = 0
    depth = 0

    # DefFunc*
    # Define functions (TODO)

    # DefActor+
    # Define Actors
    for _ in range(rand_num(1, actor_count)):
        program += generate_actor(IC, depth)

    return program

# DefEvent: 'event' EventName '{' [Type (',' Type )*] }' ';'
def generate_event() -> str:

    global all_event_names
    if not all_event_names:
      return ""

    event_name = rand_list_entry(all_event_names)
    remove_used_name(event_name, all_event_names)

    type_list = make_args()
    event = f"event {event_name} {{{type_list}}};\n"
    return event

# DefGlobalConst: 'const' Type VarName '=' ConstExpr ';'
# ConstExpr: IntExpr | BoolExpr | StrExpr
# IntExpr: NUMBER
# StrExpr: STRING
# BoolExpr: BOOL
def generate_global_const() -> str:
    global_const_string = "const " + generate_member(0, 0)

    return global_const_string

# DefMember: Type VarName '=' ConstExpr ';'
def generate_member(IC, depth) -> str:

    global all_var_names
    if not all_var_names:
        return ""

    var_type = rand_list_entry(all_var_types)
    var_name = rand_list_entry(all_var_names)
    remove_used_name(var_name, all_var_names)
    value = ""
    value_type = ""

    if (safe_var_assign):
        value_type = var_type
    else:
        value_type = rand_list_entry(all_var_types)

    match value_type:
        case "int":
            value = rand_num(0, 1000)
        case "string":
            value = "\"" + rand_list_entry(all_string_values) + "\""
        case "bool":
            value = "true" if rand_num(0, 1) else "false"

    return indent(IC) + f"{var_type} {var_name} = {value};\n"

# DefActor: 'actor' ActorName '{' ActorItem* '}'
def generate_actor(IC, depth) -> str:

    global all_actor_names
    if not all_actor_names:
        return ""

    actor_name = rand_list_entry(all_actor_names)
    remove_used_name(actor_name, all_actor_names)

    actor_string = f"actor {actor_name} {{\n"

    for _ in range (rand_num(1, actor_item_count)):
        actor_string += generate_actor_item(IC + 1, depth)
        pass

    actor_string += "}\n"
    return actor_string

# ActorItem: DefHSM | DefActorOn | DefMember | DefMethod
def generate_actor_item(IC, depth) -> str:
    actor_item_string = ""

    # DefHSM -> 0
    # DefActorOn -> 1
    # DefMember -> 2
    # DefMethod -> 3
    #choice = rand_num(0, 0)           # CURRENTLY FORCED TO ONLY PICK DefHSM/DefMember, PENDING IMPLEMENTATION OF OTHER PRODUCTION RULES
    choice = random.choice([0, 2])

    match choice:
        case 0:
            actor_item_string = generate_statemachine(IC, depth)
        case 1:
            pass
        case 2:
            actor_item_string = generate_member(IC, depth)
        case 3:
            pass

    return actor_item_string

# DefHSM: 'statemachine' '{' StateItem* '}'
def generate_statemachine(IC, depth) -> str:
    statemachine_string = ""
    statemachine_string += indent(IC)
    statemachine_string += "statemachine {\n"

    for _ in range (rand_num(0, state_item_count)):
        statemachine_string += generate_state_item(IC + 1, depth)

    statemachine_string += indent(IC)
    statemachine_string += "}\n"
    return statemachine_string

# StateItem: DefOn | DefEntry | DefExit | DefMember | DefMethod | DefState | InitialState
def generate_state_item(IC, depth) -> str:
    state_item_string = ""

    # DefOn -> 0
    # DefEntry -> 1
    # DefExit -> 2
    # DefMember -> 3
    # DefMethod -> 4
    # DefState -> 5
    # InitialState -> 6
    #choice = rand_num(5, 5)      # CURRENTLY FORCED TO ONLY PICK DefState/DefMember, PENDING IMPLEMENTATION OF OTHER PRODUCTION RULES
    choice = random.choice([3, 5])
    match choice:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            state_item_string = generate_member(IC, depth)
        case 4:
            pass
        case 5:
            state_item_string = generate_state(IC, depth + 1)
        case 6:
            pass

    return state_item_string

# DefState: 'state' StateName '{' StateItem* '}'
def generate_state(IC, depth) -> str:
    state_string = ""
    if (depth > max_state_depth):
        return state_string
    state_string += indent(IC)

    global all_state_names
    if not all_state_names:
        return ""

    state_name = rand_list_entry(all_state_names)
    remove_used_name(state_name, all_state_names)

    state_string += f"state {state_name} {{\n"

    for _ in range (rand_num(0, state_item_count)):
        state_string += generate_state_item(IC + 1, depth)

    state_string += indent(IC)
    state_string += "}\n"

    return state_string


main()
