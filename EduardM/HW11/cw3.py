def God() -> list:
    return [Man("Adam"), Woman("Eva")]


class Human:
    def __init__(self, name: str):
        self.name = name


class Man(Human):
    def __init__(self, name: str, sex: str = "man"):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name: str, sex: str = "woman"):
        super().__init__(name)
