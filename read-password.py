#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
'''db_pass = input("Enter password")'''
#With this password would be visible while typing
import getpass
db_pass = getpass.getpass(prompt= "Enter the db password: ") #if I want to prompt for password
print(f"The database passowrd is {db_pass}")

print(getpass.getuser())
