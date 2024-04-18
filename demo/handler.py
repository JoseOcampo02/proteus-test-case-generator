import os
import shutil
from paths import Paths
from delete import Delete
from fail_case_gen import generate_fail_case
from logger import Logger
from SafeTestGenerator import returnProtey

'''
Useless fucntion I made, GG
def move_file(file_path, target_folders):
    full_target_path = [ROOT] + target_folders
    target_path = os.path.join(*full_target_path)
    os.makedirs(target_path, exist_ok=True)
    target_file_path = os.path.join(target_path, os.path.basename(file_path))
    shutil.move(file_path, target_file_path)

# Example usage
move_file(ROOT + '/test.txt', [SAVED, 'Logs'])
'''

def bruh():
    skill_issues = input("How many fail cases do you want? ")
    not_skill_issues=input("How many passing cases do you want? ")
    case_names = input("What do you want to name them?\n(They'll be the name you entered followed by the order they were generated in) ")

    Logger.deletion(Paths.FAIL_PATH)
    Delete.new_session()

    for i in range(int(not_skill_issues)):
        with open(os.path.join(Paths.SUCCESS_PATH, f"PASS_{case_names}_{i + 1}.proteus"),"w", encoding='utf-8') as file:
            file.write(returnProtey())

    for i in range(int(skill_issues)):
        with open(os.path.join(Paths.FAIL_PATH, f"FAIL_{case_names}_{i + 1}.proteus"),"w", encoding='utf-8') as file:
            file.write(generate_fail_case())

    print("Tests have been stored into the TestingSession Directory under their respective directories.")


    
    Logger.creation(Paths.FAIL_PATH)