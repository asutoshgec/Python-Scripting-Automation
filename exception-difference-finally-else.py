try:
    #a =10
    print(a)
except NameError:
    print("value not found")
except Exception as e:
    print(e)
#whether exception is there or not, whatever the code is there in finally is going to exceute.
else:
    print("This will execute if there is no exceptions in try block")

finally:
    print("this will execute always")
