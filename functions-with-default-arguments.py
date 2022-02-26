'''def display(a=10):
    print("The value of a is:" , a)
    return None
display() #This function will need one argument.If we are not passing a value here, we need to pass default value
display(6)
'''
'''
#Function with keyword-based arguments
def display(a,b):
    print(f"a = {a}")
    return None

display(3,4)
display(a=3,b=4)
display(a=4,b=3)'''
#Functions with variable length arguments
def display(*arg):  #we can do that by adding *arg
    print(arg)
    return None
display() #This function will need one argument.If we are not passing a value here, we need to pass default value
display(6,7,8)
#generaly we can not give arguments more than the parameters assigned. But we can do that