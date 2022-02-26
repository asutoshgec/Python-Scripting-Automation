#If I want to read a csv file
'''import csv
req_file = input("Enter the csv file path: ")
f = open(req_file, "r")
csv_reader = csv.reader(f,delimiter="|") #If the separator in the csv file is other than the ","
for i in csv_reader:
    print(i)

f.close()'''

#How to get header and no of rows in a csv file
import csv
req_file = input("Enter the csv file path: ")
f = open(req_file, "r")
csv_reader = csv.reader(f,delimiter="|") #If the separator in the csv file is other than the ","
#print(f"The header is: \n {list(csv_reader)[0]}")
#Else we can use next function, so that it will move the cursor to the next line.
header = next(csv_reader)
print(header)
#If only want header, no need for loop
#Then if we need the number of rows after the header
print(f"The number of rows are : {len(list(csv_reader))}")
#Now in csv_reader there is only two rows.
#for i in csv_reader:
    #print(i)

f.close()