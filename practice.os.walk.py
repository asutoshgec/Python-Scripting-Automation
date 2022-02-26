#How to do a system wide search for a file with os.walk
import os
required_file = input("Enter the file name to search: ")

for r,d,f in os.walk("/"):
    for each_file in f:
        if each_file == required_file:
            print(os.path.join(r,each_file))
