#Read a path and check if given path is a file or a directory
import os
path = input("Enter the path: ")
#before chaking of the file or directory we need to check if the path is existing or not.
if os.path.exists(path):
    print(f"The given path {path} is valid ")
    if os.path.isfile(path):
          print(f"The given path: {path} is a file")
    else:
          print(f"The given path: {path} is a directory")
else:
    print(f"The given path {path} is not a valid path")