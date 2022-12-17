class Employee:
    """This class represents an employee info."""
    num_empl = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_empl += 1

    def __del__(self):
        Employee.num_empl -= 1

    @classmethod
    def empl_num(cls):
        print(f"The total number of employees: {Employee.num_empl}")

    def empl_info(self):
        print(f"Employee name: {self.name}\nTotal salary: {self.salary}\n")

employee1 = Employee('Borys Johnson', 1_500)
Employee.empl_num()
employee1.empl_info()

employee2 = Employee("Monica Geller", 2_000)
Employee.empl_num()
employee2.empl_info()

employee3 = Employee("Bill Gates", 100_000)
Employee.empl_num()
employee3.empl_info()

employee4 = Employee("Bill Taylor", 1_000)
Employee.empl_num()
employee4.empl_info()

del employee3

print("Number of employees after deleting.")
Employee.empl_num()