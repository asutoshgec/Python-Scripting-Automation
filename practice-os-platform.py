#(write a single python script to clear terminal of any Operating system)
import os
import platform

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")
