import os
import sys
import datetime
age = 600
req_path = input("Enter the path: ")
if not os.path.exists(req_path):
    print("Enter valid path")
    sys.exit(1)
if os.path.isfile(req_path):
    print("please enter the directory path")
    sys.exit(2)

list_dir = os.listdir(req_path)
#As we are working with files we need to filter the complete path
today = datetime.datetime.now()
for i in list_dir:
    each_file_path = os.path.join(req_path,i)
    if os.path.isfile(each_file_path): #here we will get all the paths like dir/file, I want to skip the dir paths
       file_cre_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
       #print(each_file_path,datetime.datetime.fromtimestamp(os.path.getctime(each_file_path)))
       #print(dir(today - file_cre_date))
       diff_days = (today - file_cre_date).days
       if diff_days > age:
          print(each_file_path,diff_days)
          #os.remove(each_file_path)
#This os.path.getctime(each_file_path will give us the ctime in seconds
#this datetime.datetime.fromtimestamp(os.path.getctime(each_file_path)) convert the seconds in date and time
#I do not bother about the hours I want to print in days output.
#print(each_file_path,(today - file_cre_date).days)
#If we want to find out which function we can use, we can run 
#print(dir(today - file_cre_date))
#Now if we want to remove this thing, we need to concentrate on os module
     