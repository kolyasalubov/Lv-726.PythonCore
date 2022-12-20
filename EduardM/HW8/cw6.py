def count_sheeps(sheep: list) -> int:
    return len([x for x in sheep if x is True])
