class Human:
    """This class represntes a Human."""

    def __init__(self, name):
        self.name = name

    def welcome_msg(self):
        print(f"Hello, {self.name}.")

    @classmethod
    def species(cls):
        print("Species: Homosapiens")

    @staticmethod
    def message():
        print("Have a good day.")

human1 = Human("Bill")
human1.welcome_msg()
human1.species()
human1.message()
