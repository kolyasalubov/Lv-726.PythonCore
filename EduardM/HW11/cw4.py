class Person:
    def __init__(self, name: str, age: int, info: str = None):
        self.name = name
        self.age = age
        self.info = self.get_info()

    def get_info(self) -> str:
        return f"{self.name}s age is {self.age}"
