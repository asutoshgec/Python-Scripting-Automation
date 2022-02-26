'''#Reading or writing data into the text files
#create an empty file
#Always we should have cursor position
fo = open("newfile.txt", "w") #fo is the file object will give us the cursor position
#Here I am creating an empty file
#I want to see in which mode the file is opened.
print(fo.mode) #This will give us the mode.
fo.close()

#I want to create a new file and write ito it
my_content = ["This is data1 \n", "This is data2 \n", "This is data3"]
fo = open("random.txt", "w")
#If I want to add second line, we need to add \n on every line, so the cursor will go to next line.
fo.write("This is a test file \n")
fo.write("This is the second line \n")
#To Write multiple lines, we do not need to add multiple line s in code, we can use writelines
fo.writelines(my_content)
fo.close()
#When we will open a file in "w" mode, then python will simply remove this file and create a new file.
'''
#Lets try to write files with the help of loop

'''my_content=["This is data1", "this is data2", "This is data3", "This is data4"]

fo = open("new-random.txt", "w")
for i in my_content:
    fo.write(i+"\n")
fo.close()'''
'''
#Want to open the file in append mode
my_content=["This is data1", "this is data2", "This is data3", "This is data4"]

fo = open("new-random.txt", "a")
for i in my_content:
    fo.write(i+"\n")
fo.close()
#it will not disturb the existing data and the new data will be appended at the end.
#if the file is not there then append mode will create a new file and add the data.
'''
'''#I want to read the contents of the file.
fo = open("new-random.txt", "r")
contents = fo.read()
print(contents)
fo.close()
'''
'''#I want to read data line by line
fo = open("new-random.txt", "r")
contents = fo.readline()
print(contents)
fo.close()'''

#If I want to read all the data and print the data into a list

fo = open("new-random.txt", "r")
contents = fo.readlines()
print(contents)
fo.close()
#If I want to print only the first 3 lines(we need to take the index value)
for i in range(0,3):
    print(contents[i])
#If I want to print the last line
print(contents[-1])

