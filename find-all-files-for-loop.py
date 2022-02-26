#Find all files in a directory with required extension .py/.sh/.log/.txt etc...
import os
req_path = input("Enter the required path: ")
if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file. Please enter the path of the directory")
else:
    req_ext = input("Enter the required file extention.(.py/.sh/.txt): ")
    list_dir = os.listdir(req_path)
    req_list = []
    for i in list_dir:
        if i.endswith(req_ext): #As the file names are string we are adding the function endswith
            #print(i)
           req_list.append(i) #If we want to display the result in a list.
    print(req_list)    