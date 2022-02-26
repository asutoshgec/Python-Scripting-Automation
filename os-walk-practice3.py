#Read a directory path and identify all files and directories
import os
import sys
path = input("Enter your directory path: ")
if os.path.exists(path):
   print("The given path is valid")
   df_l = os.listdir(path)
else:
    print("Please provide a avalid path")
    sys.exit()
#so if we need to identify the values are directory or file, I need to separate.
#But first we need to get the complete path of the files/directories
#Now we can do it through for loop
list_dir = os.listdir(path)
for i in list_dir:
    l_f_d = os.path.join(path,i) #this will join and print all the dir/files under that path
    if os.path.isfile(l_f_d):
        print(f"{l_f_d} is a file")
    else:
        print(f"{l_f_d} is a directory")
    

