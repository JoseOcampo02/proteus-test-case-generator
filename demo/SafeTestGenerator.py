import random
import string


# All possible usable names, variables, etc.

# State name list
all_state_names = [
  "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
  "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
  "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
  "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New_Hampshire",
  "New_Jersey", "New_Mexico", "New_York", "North_Carolina", "North_termDakota", "Ohio",
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

#Set code output to none



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

def setDebug (d):
    debug = d;

# -------------------------------------------------------- Program start --------------------------------------------------------------

def returnProteus():
    proteus_program = generate_program()
    if debug: 
         printProteus(proteus_program)
    return proteus_program


def printProteus(p):
    print("PASS START----------------------------------------------------------------")
    print(p)
    print("PASS END------------------------------------------------------------------")
    print("\n")
    

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

# ActorItem: DefHSM | DefActorOn | DefMember
def generate_actor_item(IC, depth) -> str:
    actor_item_string = ""

    choices = ['DefHSM',  'DefMember']

    choice = random.choice(choices)

    match choice:
        case 'DefHSM':
            actor_item_string = generate_statemachine(IC, depth)
        #case 'DefActorOn':
            #actor_item_string = generate_actor_on(IC)
        case 'DefMember':
            actor_item_string = generate_member(IC, depth)

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

# def generate_actor_on(IC):
#     event_name = random.choice(all_event_names)  # picks a random event name
#     on_block = "{\n" + indent(IC + 1) + "pass\n" + indent(IC) + "}\n"
#     return indent(IC) + f"on {event_name} {on_block}\n"

# Toggleable
event_count = 1
global_const_count = 1
func_count = 1
actor_count = 1
actor_item_count = 1
state_item_count = 1
safe_var_assign = True
safe_event_calling = True
max_state_depth = 1
debug = False

