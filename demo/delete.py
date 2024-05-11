import os
import shutil
from paths import Paths
 
class Delete():
    # Helper function, delete stuff in just one folder
    @staticmethod
    def __clear_folder(folder):
        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)

            except Exception as e:
                print(f"Failed to delete {path} because {e}\n")
    
    # Delete content in specific folder
    del_successes = staticmethod(lambda: Delete.__clear_folder(Paths.SUCCESS_PATH))
    del_failures = staticmethod(lambda: Delete.__clear_folder(Paths.FAIL_PATH))
    del_tests = staticmethod(lambda: Delete.__clear_folder(Paths.GENERATED_PATH))
    del_logs = staticmethod(lambda: Delete.__clear_folder(Paths.LOG_PATH))
    del_sessions = staticmethod(lambda: Delete.__clear_folder(Paths.SESSION_PATH))

    # Delete content in just Successes, Failures, and GeneratedTests
    @staticmethod
    def new_session():
        Delete.del_successes()
        Delete.del_failures()
        Delete.del_tests()
    
    @staticmethod
    def clear_all():
        Delete.new_session()
        Delete.del_logs()
        Delete.del_sessions()