import os
path = "/Users/ASUTOSH/COURSES/python-scripting-automation/Asutosh"

'''#print(list(os.walk(path)))
print("=======================")
#with for loop we can separate the each tupple it is creating for each path
for i in list(os.walk(path)):
    print(i)'''
for r,d,f in os.walk(path):
    if len(f) !=0:  #It will display the file list where the length  of file lists is not equal to zero
       print(r)
       for i in f:
          #print(i) #It will display the files separately without the list.
           print(os.path.join(r,i)) #this will join the output and give us the full path of the file