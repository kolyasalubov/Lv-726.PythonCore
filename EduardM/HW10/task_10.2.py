from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int
    sex: str

    def welcome_human(self) -> str:
        return f"Welcome, {self.name}"

    @classmethod
    def species(cls) -> str:
        return "Species: Homosapiens"

    @staticmethod
    def arbitrary() -> str:
        return "An arbitrary message"


human = Human("Edik")
human.welcome_human()
human.species()
human.arbitrary()
