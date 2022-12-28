class Human():
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()


def God():
    man = Man()
    woman = Woman()
    return man, woman


paradise = God()
