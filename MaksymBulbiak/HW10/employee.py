class Employee():
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    num = 0
    

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num += 1

    def __del__(self):
        Employee.num -= 1

    def employees_info(self):
        print(f"Employees name: {self.name} Salary: {self.salary}")

    @classmethod
    def employees_num(cls):
        print(f"Number of employees: {Employee.num}")



employee1 = Employee('Max', 5000)
Employee.employees_num()
employee1.employees_info()

employee2 = Employee("Michael", 6000)
Employee.employees_num()
employee2.employees_info()

employee3 = Employee("Mattew", 2000)
Employee.employees_num()
employee3.employees_info()

employee4 = Employee("Meri", 3000)
Employee.employees_num()
employee4.employees_info()

del employee1

print("After deleting", end=' ')
Employee.employees_num()

# print(f"Number of employees after deleting {Employee.employees_num()}")


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)