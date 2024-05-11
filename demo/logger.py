import os
from datetime import datetime
from paths import Paths
 
class Logger():
    @staticmethod
    def __log_message(message):
        date_str = datetime.now().strftime("%Y-%m-%d")
        log_file_name = f"{date_str}.txt"
        log_folder_path = os.path.join(Paths.LOG_PATH)
        os.makedirs(log_folder_path, exist_ok=True)
        log_file_path = os.path.join(log_folder_path, log_file_name)

        with open(log_file_path, 'a') as log_file:
            log_file.write(f"{message}\n")

    @staticmethod   
    def list_files_in_folder(folder_path):
        files = []
        # Check if the folder exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # List all files
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        else:
            print(f"Folder not found: {folder_path}\n")
        return files

    @staticmethod
    def deletion(file_path):
        Logger.__log_message(f"Deleted From: {file_path}\n")
        files = Logger.list_files_in_folder(file_path)
        
        for i in range(0, len(files), 5):
            chunk = files[i:i+5]
            Logger.__log_message(f"File Deleted: {', '.join(chunk)}")
            
        Logger.__log_message("-" * 125)
        Logger.__log_message("\n")

    @staticmethod
    def creation(file_path):
        Logger.__log_message(f"Written To: {file_path}\n")
        files = Logger.list_files_in_folder(file_path)
        
        for i in range(0, len(files), 5):
            chunk = files[i:i+5]
            Logger.__log_message(f"File Created: {', '.join(chunk)}")
            
        Logger.__log_message("-" * 125)
        Logger.__log_message("\n")