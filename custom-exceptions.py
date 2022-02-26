#How to raise userdefined exceptions
'''raise Exception("This is an Exception")

raise NameError("Value not defined")
'''
#for example
'''age = 25
if age > 30:
    print("valid Age")
else:
    raise ValueError("Age is less than 30")
#this is the way we can raise the existing exception
'''
#Another method is assert is used to create assertion error.
#assert will raise error if the condition written inside is false.
#assert (4<3)
#assert (4>3)

age = 31

try:
    assert age<30
    print("Valid age")
#If want to handle the assertion error
except AssertionError:
    print("Raised with assert because age is greater than 30")
except:
    print("exception occured")
