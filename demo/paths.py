import os

# Want to change the name of your folders? Do it in this file
def define_root():
    # User is using windows
    if os.name == "nt":
        return "..\\ProteusTestCaseGen"
    # User is using MacOS or Linux
    else:
        return "../ProteusTestCaseGen"
    
ROOT = define_root()
SAVED = "Saved"                 
LOGS = "Logs"                   
SAVED_SESH = "SavedSessions"    
SESSIONS = "TestingSession"     
FAILURE = "Failures"            
SUCCESS = "Successes"           
GENERATED = "GeneratedTests"    

class Paths():
    FAIL_PATH = os.path.join(SESSIONS, FAILURE)
    SUCCESS_PATH = os.path.join(SESSIONS, SUCCESS)
    GENERATED_PATH = os.path.join(SESSIONS, GENERATED)
    LOG_PATH = os.path.join(SAVED, LOGS)
    SESSION_PATH = os.path.join(SAVED, SAVED_SESH)