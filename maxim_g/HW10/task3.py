

class Employee:
    number_of_employees = 0
    all_employees = dict()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.number_of_employees += 1
        Employee.add_new_employee(self.name, self.salary)

    @classmethod
    def show_info_about_all_employees(cls):
        all_empl = 'All employees'
        for emp in Employee.all_employees:
            all_empl += f'\nName is {emp} and salary is {Employee.all_employees[emp]}'
        print(all_empl)

    @classmethod
    def add_new_employee(cls, name, salary):
        Employee.all_employees[name] = salary

    @classmethod
    def show_umber_of_employees(cls):
        print(f"Count of all employees is {Employee.number_of_employees}")


emp1 = Employee("Maxim", 3000)
emp2 = Employee("Ben", 1700)
emp1 = Employee("Marta", 444)

Employee.show_umber_of_employees()
Employee.show_info_about_all_employees()

