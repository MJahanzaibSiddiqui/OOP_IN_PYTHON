
# #EXAMPLE CODE:

class Employee:
    # Create __init__() method
    def __init__(self, name, salary):
        # Create the name and salary attributes
        self.name= name
        self.salary= salary
    
    # From the previous lesson
    def give_raise(self, amount=2000):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi",9000)
print(emp.name)
print(emp.salary) 
emp.give_raise()    
print("Salary after giving a raise:", emp.salary)
print("Monthly Salary:", emp.monthly_salary())

#ambiguity ka concept hai is code me. 
