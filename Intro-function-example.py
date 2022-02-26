#write a program that will clear the screen and also give us the list of the files as per the platform
import os
import time
import platform

def mycode(cmd1,cmd2):
    print("Clearing the screen........")
    time.sleep(2)
    os.system(cmd1)
    print("Listing directories and files....")
    time.sleep(2)
    os.system(cmd2)

if platform.system == "Windows":
    mycode("cls","dir")
else:
    mycode("clear","ls -lrt")
#here no need to run the code, again and again. We can use a function and can call it anytime.