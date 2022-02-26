my_value = ["asutosh", "ankita", "sarang", "prajakta", 3, 10, 90]
'''empthy_list = []
print(my_value[1], type(my_value))
print(bool(my_value))
print(bool(empthy_list)) #boolean of empty list is false.

print(my_value[-1]) #it will print the last value

print(my_value[3][1]) #SO it will show us the index[1] of the string/value[3] "prajakta" index 1 is r
print(my_value[:]) #This will give me the entire list

print(my_value[1:3]) #it will print the index 1 and 3.
print(my_value[1:]) #it will print from 1 to last
#If we want to assign a value to any index
my_value[4] = 100
print(my_value)'''

print(my_value.index(90)) # It will tell the index of value 90
print(my_value.count(90)) # It will count the number of times
#print(my_value.clear()) # It will clear the list
#print(my_value)
print(my_value.append(200)) #It will add the value given into the list
my_value.insert(1,5)
print(my_value)