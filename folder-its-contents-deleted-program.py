import shutil
import os
if os.path.exists("folder1"):
    shutil.rmtree("folder1")
    print("folder deleted")
else:
    print("folder does not exit")