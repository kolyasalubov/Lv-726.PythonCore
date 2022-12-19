from random import choice


class Ghost:
    def __init__(self, color: str = None):
        self.color = self.set_color()

    def set_color(self) -> str:
        return choice(["white", "yellow", "purple", "red"])
