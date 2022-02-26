def addition(a,b):
    result = a + b
    print("The result is :" , result)
    return None
def subtraction(a,b):
    print(f"The subtraction of two numbers is {a-b}")
    return None

def main():
  x = 9
  y = 10
  addition(x,y)
  subtraction(x,y)
  return None

if __name__ == "__main__": #So while we are importing script1 in script2, the __name__ changed to script1, so the if condition is not true, so it will not exceute the main function. So we will not get the output from the script1.
    main()
#So now if we will run script2, we will only get the output of script2, no script1.
#we need to use functions from script1 in another script
#print("This is script1",__name__)
