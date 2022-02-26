def main():
   a = eval(input("Enter the number"))
   b = eval(input("Enter the number"))
   result = addition(a,b) #here the return value from the function will be saved inside the variable
   print("The sum value of two numbers are:", result)
   return None

def addition(a,b):
    sum = a + b
    #print("The addition of two numbers are: ", sum) #Lets say I do not want to print the sum here
    #I will print the sum in main function. So I need to return the value of sum
    return sum #We will use none, where we do not need to return any value.

main()
