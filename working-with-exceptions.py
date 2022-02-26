#print("Welcome to exceptions concept") #If I will do a mistake in the first line, will not get the output for 2nd line.
#print("Now it is fine")
#print(4/0)
#Basically errors are two types, syntax error and exception error
'''  File "/Users/ASUTOSH/COURSES/python-scripting-automation/working-with-exceptions.py", line 3
    print(4/0)
    ^
SyntaxError: invalid syntax <================
(base) ASUTOSH-MACBOOK-PRO:python-scripting-automation ASUTOSH$ /usr/local/bin/python3 /Users/ASUTOSH/COURSES/python-scripting-automation/working-with-exceptions.py
Welcome to exceptions concept
Now it is fine
Traceback (most recent call last):
  File "/Users/ASUTOSH/COURSES/python-scripting-automation/working-with-exceptions.py", line 3, in <module>
    print(4/0)
ZeroDivisionError: division by zero <================
these errors are called runtime errors====> exception error'''
#We can handle the runtime errors/exceptions

'''fo = open("newfile.out", "r")#So here the file is not present so "FileNotFound Error" Exception
fo.read()
fo.close()'''
#We can run above code in below format, SO that the program will not terminate with error
'''try:                  #If the file is there then the (try) block will execute
    fo = open("newfile.out", "r")
    print(fo.read())
    fo.close()
#except :               #If file is not there then except block will run.
    #print("There is some problrem with the file")
#Or we acn also print the exception error with except
except Exception as e:
    print(e)
'''
#Try to print my_list
'''
my_list = [1,2,3,4,5]
#print(my_list[5])
#here we are getting "index out of range" error, because there is no 5th index.
try:
    print(my_list[5])
except Exception as e:
    print(e)
#After getting error also the next line will executes
print("This line will also exceutes")'''
#I want to import a module called fabric
try:
  import fabric
except Exception as e:
    print(e)

#here we are getting import error.ModuleNotFoundError: No module named 'fabric'
