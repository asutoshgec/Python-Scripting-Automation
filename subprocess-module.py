import subprocess
'''cmd = "ls"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
out,err = sp.communicate()
print(f"The return code is: {rc}")
print(f"The output is: \n{out.splitlines()}")
print(f"The error is: \n{err.splitlines()}")
'''
cmd = ["ls", "lh"]
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
out,err = sp.communicate()
print(f"The return code is: {rc}")
print(f"The output is: \n{out.splitlines()}")
print(f"The error is: \n{err.splitlines()}")
#here python will not open a new shell
