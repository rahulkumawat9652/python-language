import os
#deleting an empty folder
if os.path.exists("folder1"):
    os.rmdir("folder1")
    print("folder deleted")
else:
    print("folder does not exit")