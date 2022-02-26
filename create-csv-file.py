#create csv file using python
import csv
req_file = "/Users/ASUTOSH/COURSES/python-scripting-automation/demo.csv"
fo = open(req_file, "w",newline="") #To delete the empty line after every entry.
csv_writer = csv.writer(fo,delimiter=",")
#csv_writer.writerow(["S_NO", "Name", "Salary", "Skill"])
#When we are going to add the lines one by one or got new data to add, we can use above operations
#Now instead of writing every line, we can enter the data in list of lists
data = [["SL_No","Name","Salary","Skill"],["1","Asutosh","3000","Python"]]
csv_writer.writerows(data)

fo.close