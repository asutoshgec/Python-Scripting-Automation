import subprocess
cmd = "java -version"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
out,err = sp.communicate()
if rc == 0:
    if bool(out) == True:
        print(out)
    if bool(out)==False and bool(err)==True:
         print(err.splitlines()[0].split()[2].strip("\""))   #I do not want the quotations, will strip them
else:
    print(f"The given command is invalid and the error is {err.splitlines()}")
