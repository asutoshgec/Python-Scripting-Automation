class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.display() #we are calling the method inside the constructor
    def display(self):
        print("The name is :", self.name)
        print("The salary is:", self.salary)

#Now if we will create object, the __init__ method will call automatically, so it needs arguments to pass.So we have to pass the arguments while creating objects.
emp1=employee("Asutosh",90000) #here we are assigning arguments to the method.
emp2 = employee("Abhinash",100000)
#emp1.display()
#emp2.display()
#Now if we will call the method display() inside the method __init__ itself, then we do not need to call the method