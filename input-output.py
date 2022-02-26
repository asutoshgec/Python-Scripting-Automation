'''
x = int(input("Enter the value of x" ))

y = int(input("Enter the value of y"))
'''
#This will only take the int value or the float value as mentioned.

#This will take any value we give and python will decide what type it is
x = eval(input("Enter the value of x" ))

y = eval(input("Enter the value of y"))

print(f"The value of x is {x} and the type of x is {type(x)}") 

print(f"The value of x is {y} and the type of y is {type(y)}") 

print(f"The addition of {x} and {y} is {x + y}")

