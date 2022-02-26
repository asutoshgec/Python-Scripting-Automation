import json
'''req_file = input("Enter the path of the json file: ")
fo = open(req_file, "r")
#print(fo.read()) #We can also run fo.read to get the normal output in json format
print(json.load(fo)) #We can process json data because that is string, so we load json data and that will convert it into a "Dictionary".


fo.close()'''
#How I can store data into a json file
#When we are processing json data as a distionary, so we should have our data as a dictionary to insert the data into a json file.

my_dict = {"Name": "Asutosh", "Skills":["Python","Shell","K8s"], "Salary": 3000}
req_file = input("Enter the file name: ")
fo = open(req_file, "w")
json.dump(my_dict,fo,indent=4)

fo.close()