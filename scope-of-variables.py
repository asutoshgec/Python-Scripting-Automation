#calling a function from another function

def myfunction1():
    x =10       #here the value of x can be used by only myfunction1, this is called local variable.
    print("Welcome to functions")
    print("The value is", x)
    #myfunction2()
    return None

def myfunction2(y): #here the value passed to the function is called parameter.
    print("Thank you!!")
    print("The value is", y)
    return None
#sometimes we need to call one function in another function.
#x = 10 #So here the value can be access by both the function, called scope of variable. This is global variable.
#myfunction1()

#lets say I am writing another function called main and I am calling function1 from main

def main():
    #global x
    x =20 #here x is not global to function2, it is local to main()
    myfunction1()
    #there is another way to pass the value to function2
    myfunction2(x)  #here the value passed to the function is called argument.
    #Now this variable x and the variable y are diferent.
    return None

main()