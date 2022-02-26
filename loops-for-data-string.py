'''my_string = "Working with for loop"
print(my_string)

#for i in my_string: #If we want to print the characters one by one
    #print(i)
print("\n".join(my_string))# this is also we can use

#--------------#
#list
my_list = [1,2,3,4,5,6,7]
for i in my_list:
    print(i)'''
#tuple    
'''my_list = [(1,2), (4,5), (6,7)]
#for i in my_list:
    #print (i)
#we can also separate the values with for loop
for i,j in my_list:   #we are assigning first value to i and second value to j
    print(i)
    print(j)'''
my_dict = {"a": 1, "b": 2, "c": 3}
#for i in my_dict:
    #print(i) #If we will take one variable then we will get only keys
for i,j in my_dict.items(): #to get the key and value from the dictonary we need to write this way
   
   #print(i)
   #print(j)
   print(i,j) #we can print this way or that way
   #It is very important in case of dictionary. We need to take key and value.