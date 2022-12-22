

class Human:
    h_count = 0

    def __init__(self, name):
        self.name = name
        Human.h_count += 1

    def show_count_created_human(self):
        print(f"The number of people that was created is equal to {Human.h_count}")

    def welcome(self):
        print(f"Hello, a new human with name {self.name}, have a good day :)")

    @classmethod
    def type_of_human(cls):
        return "its a homosapiens"

    @staticmethod
    def nothing():
        print('This method doesn\'t do anything')


human1 = Human("Maxim")
human1.show_count_created_human()
human1.welcome()

human2 = Human("Viktor")
human2.show_count_created_human()
human2.welcome()

