# imports
import random
 
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
  "TERMINATE", "DESTROY", "SAVE", "BARK", "MEOW", "START", "RESET"
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
    "When will we graduate?", "I'd like a free job please! No, I don't have experience"
]

# Function names
all_function_names = [
    "do_this", "turn_on", "turn_off", "move_up", "move_down", "move_left", "move_right",
    "save_this", "delete_this", "kill_task", "start_task", "find_this", "start_clock",
    "end_clock", "check_this", "touch_grass", "meme_generator", "hack_the_bank",
    "job_finder"
]

# Default comment so that the word "None" isn't shown everywhere
BLANK = "// No syntax provided\n"

# This one string will be the entire code. Probably isnt needed
code = ""

# Proteus Binary Operators
bin_ops = [
    '*', '/', '%', '+', '-', '<<', '>>', '<', '>', '<=', '>=', '==',
    '!=', '^', '&&', '||', '*=', '/=', '%=', '+=', '-=', '<<=', '>>=', '^='
]

# Hold all generated varaible syntax
variables = []

# Hold all generated states syntax
states = []

# Hold all generated events syntax
events = []

# Hold all generted actor syntax
actors = []

# Holds all generated functions
functions = []

# Utilities
# Pick a random number
rand_num = lambda x, y: random.randint(x, y)

# Random item from a list
rand_list_entry = lambda from_list: random.choice(from_list)

# I was getting annoyed with the "None" errors.
# Not sure why they're happening since im using the BLANK string as a default
none_checker = lambda check: check if check is not None else BLANK

# Clear everything...just like the name suggests
def clear(var_list, state_list, event_list, actor_list):
    var_list.clear()
    state_list.clear()
    event_list.clear()
    actor_list.clear()
    return ""

# FormalFuncArgs: '(' [Type VarName (',' Type VarName)*] ')'
def formal_func_args():
    args_list = []
    for _ in range(rand_num(1, 5)):
        rand_var_type = rand_list_entry(all_var_types)
        rand_var_name = rand_list_entry(all_var_names)
        args_list.append(rand_var_type + " " + rand_var_name)
        args = ', '.join(args_list)
    return args

# Note: doesn't have the "()"
def make_args():
    args_list = []
    for _ in range(rand_num(1, 5)):
        rand_var_type = rand_list_entry(all_var_types)
        args_list.append(rand_var_type)
        args = ', '.join(args_list)
    return args

# Make an INVALID variable value
def make_invalid_var_value():
    # Picks a random name from the list
    name = rand_list_entry(all_var_names)

    # Randomly Decides if var is a constant
    if rand_num(0, 1):
        # Picks a random variable type (non-constant)
        var_type = rand_list_entry(all_var_types)
        match rand_num(0, 2):
            # int
            case 0:
                return f"{var_type} {name} = {rand_num(0, 1000)};\n"
            # string
            case 1:
                return f"{var_type} {name} = \"{rand_list_entry(all_string_values)}\";\n"
            # bool
            case 2:
                return f"{var_type} {name} = true;\n" if rand_num(0, 1) else f"{var_type} {name} = false;\n"
    else:
        # Picks a random variable type (constant)
        var_type = rand_list_entry(all_var_types)
        match rand_num(0, 2):
            # int
            case 0:
                return f"const {var_type} {name} = {rand_num(0, 1000)};\n"
            # string
            case 1:
                return f"const {var_type} {name} = \"{rand_list_entry(all_string_values)}\";\n"
            # bool
            case 2:
                return f"const {var_type} {name} = true;\n" if rand_num(0, 1) else f"const {var_type} {name} = false;\n"

# Make a VALID variable value
def make_valid_var_value(input):
    # Picks a random name from the list
    name = rand_list_entry(all_var_names)

    if rand_num(0, 1):
        # Makes var based on input type (non-constant)
        match input:
            case "int":
                return f"int {name} = {rand_num(0, 1000)};\n"
            case "string":
                return f"string {name} = \"{rand_list_entry(all_string_values)}\";\n"
            case "bool":
                return f"bool {name} = true;\n" if rand_num(0, 1) else f"bool {name} = false;\n"
    else:
        # Makes var based on input type (constant)
        match input:
            case "int":
                return f"const int {name} = {rand_num(0, 1000)};\n"
            case "string":
                return f"const string {name} = \"{rand_list_entry(all_string_values)}\";\n"
            case "bool":
                return f"const bool {name} = true;\n" if rand_num(0, 1) else f"const bool {name} = false;\n"

# Type: 'int' | 'string' | 'bool'
# DefGlobalConst: 'const' Type VarName '=' ConstExpr ';'
# In each of these, we randomly decide if we want the variable to be a valid type or not
def define_variables(type_input):
    variable = ""  # Initialize the variable
    match type_input:
        case "int":
            variable = make_valid_var_value("int") if rand_num(0, 1) else make_invalid_var_value()
        case "string":
            variable = make_valid_var_value("string") if rand_num(0, 1) else make_invalid_var_value()
        case "bool":
            variable = make_valid_var_value("bool") if rand_num(0, 1) else make_invalid_var_value()
        case _:
            print("Invalid type entered")
            variable = "Invalid type\n"

    variables.append(variable)
    return variable

# DefEvent: 'event' EventName '{' [Type (',' Type )*] '}' ';'
def define_event(args=BLANK):
    event_name = rand_list_entry(all_event_names)
    event = ""

    # Decide if the event will have types or not
    if rand_num(0, 1) == 0:
        # No types
        event = f"event {event_name} {{}};\n"
    else:
        event = f"event {event_name} {{{args}}};\n"
    events.append(event)
    return event

# Needs work
# Stmt: IfStmt | WhileStmt | DecStmt | AssignStmt | ExitStmt | ApplyStmt | SendStmt | PrintStmt | PrintlnStmt
def define_statement(IfStmt=BLANK, WhileStmt=BLANK, DecStmt=BLANK, AssignStmt=BLANK,
                    ExitStmt=BLANK, ApplyStmt=BLANK, SendStmt=BLANK, PrintStmt=BLANK, PrintlnStmt=BLANK):
    statement_code = ""
    params = [IfStmt, WhileStmt, DecStmt, AssignStmt, ExitStmt, ApplyStmt, SendStmt, PrintStmt, PrintlnStmt]
    for param in params:
        if param is not BLANK:
            statement_code += param + "\n"
    return statement_code

# Block: '{' Stmt* '}'
def define_block(Stmt=BLANK):
    return f" {{\n{none_checker(Stmt)}}}\n"

# DefFunc: 'func' FuncName FormalFuncArgs ['->' Type] Block
# FormalFuncArgs: '(' [Type VarName (',' Type VarName)*] ')'
'''
func get_temp() -> int {
    // Always > dark_threshold so it reaches the ExposingDark state.
    return dark_threshold + 1;
}

// Functions simulating camera device.
func camera_power_on() {
    monitor ! POWERING_ON{};
    System ! READY{};
}
'''
# A little confused here cause FormalFuncArgs doesn't seem to be used in the examples so im not sure how to combine them right, edit later i guess
def define_func(FormalFuncArgs=BLANK, Block=BLANK):
    func_code = f"func {rand_list_entry(all_function_names)}"
    rand_var_type = rand_list_entry(all_var_types)

    # randomly decides if theres args
    if rand_num(0, 1):
        # Randomly pick if func is a method with args
        if rand_num(0, 1):  # Is method
            func_code += f"({FormalFuncArgs}) -> {rand_var_type}{Block}"
        else: # Not method
            func_code += f"({FormalFuncArgs}){Block}"
    else:
        # Randomly pick if func is a method without args
        if rand_num(0, 1):  # Is method
            func_code += f"() -> {rand_var_type}{Block}"
        else: # Not method
            func_code += f"(){Block}"
        functions.append(func_code)
    return func_code

# DefOn: 'on' EventMatch OnBody
# OnBody: GoStmt | OnBlock
# OnBlock: Block
def event_def_on(OnBody=BLANK):
    event_name = rand_list_entry(all_event_names)
    return f"on {event_name}{OnBody}"

# DefEntry: 'entry' { Block }
def event_def_entry(Block=BLANK):
    event_name = rand_list_entry(all_event_names)
    return f"entry {event_name}{none_checker(Block)}"

# DefExit: 'exit' { Block }
def event_def_exit(Block=BLANK):
    event_name = rand_list_entry(all_event_names)
    return f"exit {event_name}{none_checker(Block)}"

# InitialState: 'initial' StateName ';'
def initial_state():
    state_name = rand_list_entry(all_state_names)
    return f"initial {state_name};\n"

# StateItem: DefOn | DefEntry | DefExit | DefMember | DefMethod | DefState | InitialState
def state_item(DefOn=BLANK, DefEntry=BLANK, DefExit=BLANK, DefMember=BLANK, DefMethod=BLANK, DefState=BLANK, InitialState=BLANK):
    state_code = ""
    params = [InitialState, DefState, DefMethod, DefMember, DefExit, DefEntry, DefOn]
    for param in params:
        if param is not BLANK:
            state_code += param + "\n"
    return state_code
# ^^^^^^ This is the difficult part

# DefState: 'state' StateName '{' StateItem* '}'
def define_state(StateItem=BLANK):
    state_name = rand_list_entry(all_state_names)
    state_code = f"state {state_name} {{\n{none_checker(StateItem)}}}\n"
    states.append(state_code)
    return state_code

# DefHSM: 'statemachine' '{' StateItem* '}'
def define_statemachine(StateItem=BLANK):
    return f"\nstatemachine {{\n{none_checker(StateItem)}}}\n"

# DefActor: 'actor' ActorName '{' ActorItem* '}'
def define_actor(ActorItem=BLANK):
    actor_name = rand_list_entry(all_actor_names)
    actor_code = f"actor {actor_name} {{\n{none_checker(ActorItem)}}}\n"
    actors.append(actor_code)
    return actor_code

# ExprListParen:'(' [Expr (',' Expr)*] ')'
def define_expr_list_paren(Expr):
    return f"({none_checker(', '.join(Expr))})"

# ExprListCurly:'{' [Expr (',' Expr)*] '}'
def define_expr_list_paren(Expr):
    return f"{{{none_checker(', '.join(Expr))}}}"

# PrintStmt: 'print' ExprListParen ';'
def define_print(ExprListParen=BLANK):
    return f"print {ExprListParen};\n"

# PrintlnStmt: 'println' ExprListParen ';'
# PrintStmt: 'print' ExprListParen ';'
def define_println(ExprListParen=BLANK):
    expr = none_checker(ExprListParen)
    return f"println {expr};\n"

# JustGoStmt: 'go' StateName Block
def just_go_stmt(StateName=BLANK, jgs_Block=BLANK):
    state_name = none_checker(StateName)
    block = none_checker(jgs_Block)
    return f"go {state_name} {block}"

# ElseGoStmt: 'go' StateName Block
def else_go_stmt(StateName=BLANK, egs_Block=BLANK):
    state_name = none_checker(StateName)
    block = none_checker(egs_Block)
    return f"go {state_name} {block}"

# DefActorOn: 'on' EventMatch OnBlock
def def_actor_on(EventMatch=BLANK, OnBlock=BLANK):
    event_match = none_checker(EventMatch)
    block = none_checker(OnBlock)
    return f"on {event_match} {block}"

# EventMatch: EventName '{' [VarName (',' VarName)*] '}'

# ReturnStmt: 'return' Expr ';'
def return_stmt(Expr=BLANK):
    expr = none_checker(Expr)
    return f"return {expr};\n"

# ActorItem: DefHSM | DefActorOn | DefMember | DefMethod

# SendStmt : HSMName '!' EventName ExprListCurly ';'
def send_stmt(HSMName=BLANK, EventName=BLANK, ExprListCurly=BLANK):
    hsm_name = none_checker(HSMName)
    event_name = none_checker(EventName)
    expr = none_checker(ExprListCurly)
    return f"{hsm_name} ! {event_name} {expr};\n"

# GoStmt: JustGoStmt | GoIfStmt
def define_go_stmt(just_go_stmt=BLANK, go_if_stmt=BLANK):
    if just_go_stmt == BLANK and go_if_stmt == BLANK:
        return BLANK
    elif just_go_stmt == BLANK and go_if_stmt != BLANK:
        return go_if_stmt
    elif just_go_stmt != BLANK and go_if_stmt == BLANK:
        return just_go_stmt

# GoIfStmt: 'goif' ParenExpr StateName Block ['else' (GoIfStmt | ElseGoStmt)]

# IfStmt: 'if' ParenExpr Block ['else' (IfStmt | Block)]

# ParenExpr: '(' Expr ')'
def paren_expr(Expr=BLANK):
    expr = none_checker(Expr)
    return f"({expr})"

# Expr: ValExpr | BinOpExpr | ApplyExpr

# ApplyExpr: FuncName ExprListParen
def apply_expr(FuncName=BLANK, ExprListParen=BLANK):
    func_name = none_checker(FuncName)
    expr = none_checker(ExprListParen)
    return func_name + expr

# WhileStmt: 'while' ParenExpr Block
def while_stmt(ParenExpr=BLANK, Block=BLANK):
    expr = none_checker(ParenExpr)
    block = none_checker(Block)
    return f"while {expr}{block}"

# BinOpExpr: ValExpr BinOp Expr
def bin_op_expr(ValExpr=BLANK, BinOp=BLANK, Expr=BLANK):
    val_expr = none_checker(ValExpr)
    op = none_checker(BinOp)
    expr = none_checker(Expr)
    return val_expr + op + expr

# ValExpr: VarExpr | IntExpr | StrExpr | BoolExpr | ActorExpr | StateExpr | EventExpr | ParenExpr

# ConstExpr: IntExpr | BoolExpr | StrExpr

# Generate test case
def generate_fail_case():
    # Wipes old code for new code to be genreted. Lists are cleared, empty string returned
    gen_code = clear(variables, states, events, actors)

    # Make events
    for _ in range(rand_num(0, 5)):
        define_event(make_args())

    # Make variables
    for _ in range(rand_num(0, 20)):
        define_variables(rand_list_entry(all_var_types))

    # Make states
    for _ in range(rand_num(1, 5)):
        entry_event = event_def_entry(define_block())
        exit_event = event_def_exit(define_block())
        function = define_func(formal_func_args(), define_block()) if (rand_num(0,1)) else ""
        on_event = event_def_on(define_block())

        state_code = state_item(DefOn=on_event, DefEntry=entry_event, DefExit=exit_event, DefMethod=function, InitialState=initial_state())
        # Put variables in states
        if variables is not None and len(variables) != 0:
            state_variables = none_checker(rand_list_entry(variables)) + state_code # <--- ISSUE?: Segmentation Fault
            define_state(state_variables) if rand_num(0, 1) else define_state(state_code)
        # Make states if there are no variables made
        else:
            define_state(state_code)

    # Declares events in code (top of code)
    for event in events:
        gen_code += event
    gen_code += "\n"

    # Make initial state
    statemachine = initial_state() + "\n"

    # Put states (which has state contents) inside of statemachine
    for state in states:
        statemachine += state + "\n"

    # Final code (a statemachine)
    statemachine = define_statemachine(statemachine)
    gen_code += define_actor(statemachine)
    if debug:
        printFail(gen_code)
    return gen_code

def printFail(p):
    print("FAIL START----------------------------------------------------------------")
    print(p)
    print("FAIL END------------------------------------------------------------------")
    print("\n")

debug = False