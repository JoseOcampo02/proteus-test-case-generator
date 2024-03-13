
# imports
from tempfile import TemporaryDirectory
import os
import subprocess
import random
import string
import os.path
from pathlib import Path
import sys
# Global event dictionary
eventIDDict = []

# Creates temporary directory and file for output
def main():
    with TemporaryDirectory() as temp_dir:
        tempdir = temp_dir
        fileName = "input.proteus"
        FILE = os.path.join(tempdir, fileName)
        print(FILE)
        
        with open(FILE, "w") as f:
            generateProgram(f)

        '''
        contents = open(FILE).read()
        print("\n")
        print(contents)
        print("\n")
        '''
        
        # Text editor of choice here    
        #subprocess.Popen("cat" + FILE)
        home = str(Path.home())
 #       print(home)
        
        os.system("type "+ FILE)

        Output = os.path.join(home, "Desktop\\output.txt")
#        print(Output)
        # Path to Proteus.exe
        result = subprocess.run(["SwiftProteus.exe", "build", FILE])
#        print(result.returncode)
#        print(result.stderr)
#        print(result.stdout)
        print("")
        os.system("type "+ Output)
       # subprocess.run(["cat"], "C:/Users/abpax/Desktop/output.txt")
        print("");
        print("Successfully exited")

# Program: DefEvent* DefGlobalConst* DefFunc* DefActor+
def generateProgram(f):
    generateEvents(f, random.randint(0, 5))
    #generateGlobalConsts(f)
    #generateFuncs(f)
    generateActors(f, random.randint(1, 3))
    
# DefEvent: 'event' EventName '{' [Type (',' Type )*] }' ';'
def generateEvents(f, count):
    for _ in range(count):
        myIdentifier = randomIdentifier()
        myTypes = randomTypes()
        global eventIDDict
        eventIDDict += myIdentifier
        f.write("event " +
                myIdentifier +
                " {" +
                myTypes +
                "};\n")
    f.write("\n")
    
# TODO
def generateGlobalConsts(f):
    print("generateGlobalConsts placeholder")
    
# TODO
def generateFuncs(f):
    print("generateFuncs placeholder")
    
# DefActor: 'actor' ActorName '{' ActorItem* '}'
def generateActors(f, count):
    # IndentCounter (IC)
    IC = 0
    for _ in range(count):
        f.write("actor " +
                randomIdentifier() +
                " {\n")
        generateActorItems(f, random.randint(1, 1), IC + 1)
        f.write("}\n")
       
# ActorItem: DefHSM | DefActorOn | DefMember | DefMethod
# 0 -> DefHSM
# 1 -> DefActorOn (TODO)
# 2 -> DefMember (TODO)
# 3 -> DefMethod (TODO)
def generateActorItems(f, count, IC):
    actorItems = []
    for _ in range(count):
        actorItems.append(random.randint(0, 0))
    
    for item in actorItems:
        if (item == 0):
            generateHSM(f, IC)
        #if (item == 1):
            # DefActorOn
        #if (item == 2):
            # DefMember
        #if (item == 3):
            # DefMethod

# DefHSM:   'statemachine' '{' StateItem* '}'
def generateHSM(f, IC):
    indent(f, IC)
    f.write("statemachine {\n")
    generateStateItems(f, random.randint(0, 3), IC + 1)
    indent(f, IC)
    f.write("}\n")
    
# StateItem: DefOn | DefEntry | DefExit | DefMember | DefMethod | DefState | InitialState
# 0 -> DefOn (TODO)
# 1 -> DefEntry (TODO)
# 2 -> DefExit (TODO)
# 3 -> DefMember (TODO)
# 4 -> DefMethod (TODO)
# 5 -> DefState
# 6 -> InitialState (TODO)
def generateStateItems(f, count, IC):
    stateItems = []
    for _ in range(count):
        stateItems.append(random.randint(5, 5))
        
    for item in stateItems:
        #if (item == 0):
            #generateOnBlock(f, IC)
        #if (item == 1):
            # 1
        #if (item == 2):
            # 2
        #if (item == 3):
            # 3
        #if (item == 4):
            # 4
        if (item == 5):
            generateState(f, IC)
        #if (item == 6):
            # 6

# DefOn: 'on' EventMatch OnBody
def generateOnBlock(f, IC):
    indent(f, IC)
    f.write("on ")
    # EventMatch
    # OnBody
    
# DefState: 'state' StateName '{' StateItem* '}'
def generateState(f, IC):
    indent(f, IC)
    f.write("state " +
            randomIdentifier() +
            " {\n")
    # generateStateItems()
    indent(f, IC)
    f.write("}\n")
    
    
# EventMatch: EventName '{' [VarName (',' VarName)*] '}'
#def generateEventMatch():
    
# --------------------------- Helper functions ------------------------------------------

def indent(f, IC):
    f.write("    " * IC)

# We assume Proteus accepts identifiers of the from [a..z A..Z] [a..Z 0..1]*
def randomIdentifier():
    length = random.choice(range(1,10))
    alphabetic = string.ascii_letters
    alphanumeric = alphabetic + string.digits
    toReturn = ''.join(random.choice(alphabetic))
    toReturn += ''.join(random.choices(alphabetic + alphanumeric, k=length))
    return toReturn

# Random list of types for event definition
def randomTypes():
    length = random.choice(range(0, 5))
    # Proteus compiler currently doesnt support actorname/statename/eventname
    types = ["int", "string", "bool"]
    if (length == 0):
        toReturn = ''
    if (length == 1):
        toReturn = random.choice(types)
    if (length > 1):
        toReturn = ", ".join(random.choices(types, k=length))
    
    return toReturn
    
# ---------------------------------------------------------------------------------------

main()
