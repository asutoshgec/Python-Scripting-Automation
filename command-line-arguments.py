import sys
#We are not going to use input commadn here.We will use command line arguments
#We can also add one error message here, if the length of the arguments are less than 3
if len(sys.argv) != 3:
    print("Usage:")
    print(f"{sys.argv[0]} <string-name> <lower|upper|title>")
    sys.exit()
usr_str = sys.argv[1]
usr_action = sys.argv[2]
if usr_action == "lower":
    print(usr_str.lower())
elif usr_action == "upper":
    print(usr_str.upper())
elif usr_action == "title":
    print(usr_str.title())
else:
    print("Your option is invalid please select validate option like (lower/upper/title)")
