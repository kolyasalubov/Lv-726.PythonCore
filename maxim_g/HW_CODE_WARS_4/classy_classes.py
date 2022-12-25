class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = self.get_info()

    def get_info(self):
        return f"{self.name}s age is {self.age}"

