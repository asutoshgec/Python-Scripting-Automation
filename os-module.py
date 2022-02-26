import os
#print(os.sep)
#print(os.getcwd())
#os.chdir("/Users/ASUTOSH/COURSES/python-scripting-automation")
#print(os.getcwd())
#print(os.listdir())
#print(os.listdir("/Users/ASUTOSH/COURSES/python-scripting-automation"))
#os.mkdir("Asutosh")
#print(os.environ)
#print(os.getpid())
#print(os.getuid())
#path = "/Users/ASUTOSH/COURSES/python-scripting-automation"
#print(os.path.basename(path))
#print(os.path.dirname(path))
#We use os.system to execute operating system commands.

print(os.system("pwd"))
print(os.system("ls -lh"))

#We will right a asimple script.
cmd = "date" #here we have given wrong command. If the command is wrong, then it will give a error value.
rt = os.system(cmd) 
print(rt)
if rt == 0:
    print("The command completed succdessfully")
else:
    print("command was failed")
