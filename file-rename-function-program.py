import os
if os.path.exists("rahul.txt"):
    os.rename("rahul.txt","rohit.txt")
    print("file rename")
else:
    print("file does not exit")