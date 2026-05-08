import os
if os.path.exists("rahul.txt"):
    os.remove("rahul.txt")
    print("file remove")
else:
    print("file does not exit")