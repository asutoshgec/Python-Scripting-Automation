'''usr_string = input("Enter the string: ")
usr_cnf = input("Do you want to convert it to the lower case? say yes or no: ")
if usr_cnf == "yes":
    print(usr_string.lower())
'''
my_even_number = [0,2,4,6,8,10]

usr_input = eval(input("Enter the number: "))

if usr_input in my_even_number:
    print("The given number is even")
else:
    print("The number is not in the list")
