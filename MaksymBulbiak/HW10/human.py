class Human():
    def hello(self):
        print('Hello everybody!')

    @classmethod
    def species(cls):
        print('Hello Homosapiens')

    @staticmethod
    def arbitary():
        print("Are you here?")


obj = Human()

obj.hello()
obj.species()
obj.arbitary()


