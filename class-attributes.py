class employee:
    #If we want to count the number of employees.
    count = 0 #This is class attribute.
    def get_emp_age_sal_name(self,name,age,sal): #We are creating a method to get the employee details
        self.name = name   #These are class object attributes
        self.age = age
        self.sal = sal
        #if we want to call the display function here itself to display the data.
        #self.display_data()
        #We can add the employee count in the method itself to call the method employee_count.
        self.employee_count()
    def employee_count(self):
        employee.count = employee.count+1
    def display_data(self):
        print("The name of the employee is", self.name)
        print(f"The age of the employee is {self.age}")
        print(f"The salary of the employee is {self.sal}")

emp1 = employee()

emp2 = employee()
#we are storing the whole class template in the object emp1 and emp2.
emp1.get_emp_age_sal_name("Asutosh",33,50000)
#emp1.employee_count()
emp2.get_emp_age_sal_name("Ankita",26,50000)
#emp2.employee_count()
emp1.display_data()
emp2.display_data()
print(employee.count)


