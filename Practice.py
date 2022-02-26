#Practice: Display given string at left/right/center of a line in title format
import os
t_w = os.get_terminal_size().columns
my_string = input("Enter the string:")
print(my_string.center(t_w).title())
print(my_string.ljust(t_w).title())
print(my_string.rjust(t_w).title())

#os.terminal_size().columns <=====This will get the terminal column size on any platform.




