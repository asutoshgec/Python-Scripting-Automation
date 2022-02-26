#Exception Handling for Known Exceptions
#print(a)
#here we will get Name Error NameError: name 'a' is not defined

#print(4+"string")
#here we will get type error. TypeError: unsupported operand type(s) for +: 'int' and 'str'

#fo = open("file.out")
#Here we are getting file not found. FileNotFoundError: [Errno 2] No such file or directory: 'file.out'

#print(5/0)
#here we will get zero division error  
# to avoid or to handle the known runtime errors we can do below
#here we know the types of errors, so we can handle directly.
try:
    print(a)
    #print(4+"string")
    #open("file.out")
    #print(5/0)
    import fabric
except NameError:
    print("The value is not defined.")
except TypeError:
    print("not possible")
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Not possible with zero division")
except ImportError:
    print("No module")
except Exception as e:
    print(e)
#So if no exception is mentioned then it will go to the last line and print the error.

#If two lines are enabled under the try: and first line itself will give the exception error, then the next line will not exceute.
finally:
    print("finally this block will execute")
#It means after trying with all the blocks finally final block will execute.