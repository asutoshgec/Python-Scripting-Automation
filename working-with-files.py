#Copy the content of a source file into the destination file
#When trying to read or write into a file, please give the complete path
#sfn = "/Users/ASUTOSH/COURSES/python-scripting-automation/new-random.txt"
#dfn = "/Users/ASUTOSH/COURSES/python-scripting-automation/random-new.txt"
#I want to read the source file and the destination file location while running the script.
sfn = input("Enter the source file destination. Give full path: ")
dfn = input("Enter the destination file location.Give the fulll path: ")

sfo = open(sfn,"r")
contents = sfo.read()
sfo.close()

dfo = open(dfn,"w")
dfo.write(contents)
dfo.close()
#If we will open the file without any mode, so by default it will be in read mode.
