class Employee:
    num_of_employees = 0

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        Employee.num_of_employees += 1

    def __del__(self):
        Employee.num_of_employees -= 1

    def employees_info(self):
        print(f"Employee's name: {self.name}\nSalary: {self.salary}\n")

    @classmethod
    def employees_num(cls):
        print(f"Number of employees: {Employee.num_of_employees}")


employee1 = Employee('Edik', 11000)
Employee.employees_num()
employee1.employees_info()

employee2 = Employee("Bob", 3200)
Employee.employees_num()
employee2.employees_info()

del employee1

print("Number of employees after deleting.", Employee.employees_num())
