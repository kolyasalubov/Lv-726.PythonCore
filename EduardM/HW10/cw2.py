def list_animals(animals: list) -> str:
    list = ''
    for i, animal in enumerate(animals):
        list += f"{i + 1}. {animal}\n"
    return list
