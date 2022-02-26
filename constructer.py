class emp:
    count=0
    def __init__(self):  #This will be called automatically whenever the object will be initialized.
        #print("This is a constructor")
        #lets add emp count in the constructor.
        emp.count = emp.count+1
    def get_employees(self):
        print("This is a display function")

emp1=emp()
emp2=emp()
print("The employee count is: ", emp.count) #There is no object created, so no output.After creating object
#emp1.get_employees()
#emp2.get_employees()   
