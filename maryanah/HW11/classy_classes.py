class Person:
    def __init__(self, name: str, age: int, info=''):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"

    def info(self):
        return self.info