#Read a number between 1-10 and display it in words
'''usr_number = eval(input("Enter the number between 1 to 10"))
if usr_number == 1:
    print("ONE")
elif usr_number == 2:
    print("TWO")
elif usr_number == 3:
    print("THREE")
elif usr_number == 4:
    print("FOUR")
elif usr_number == 5:
    print("FIVE")
elif usr_number == 6:
    print("SIX")
elif usr_number == 7:
    print("SEVEN")
elif usr_number == 8:
    print("EIGHT")
elif usr_number == 9:
    print("NINE")
elif usr_number == 10:
    print("TEN")
else:
    print("Please enter the number between 1 to 10")
 '''   
 #instead of writing so many lines we can use a dictionary.
user_number = eval(input("Enter the number between 1 to 10: "))
num = {1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE", 10:"TEN"}

if user_number in [1,2,3,4,5,6,7,8,9,10]:
     print("The number is valid", num.get(user_number))
     
else:
     print("Enter the number between 1 to 10")
