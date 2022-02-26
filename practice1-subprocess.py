#Find bash version of linux os
#Only the version
import subprocess
cmd = ["bash", "--version"] #list version of cmd
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait() #It will wait for sometime to execute the code
out,err = sp.communicate()

if rc == 0:
    #print(f"The output is: {out.splitlines()}")#out.splitlines() convert the output in string
     for each_line in out.splitlines():
         #print(each_line)
         if "version" in each_line and "release" in each_line:
             print(each_line.split()[3].split("(")[0]) #this will convert the output into string, index 3 value
else:        #split("(") This will split the value in two strings and we need the index 0
    print(f"The command is not valid and the error is: {err.splitlines()}") #This will give us error if the command is invalid
