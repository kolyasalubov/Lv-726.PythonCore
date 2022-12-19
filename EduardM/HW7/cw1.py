def distance(x1, y1, x2, y2) -> float:
    res = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)
    return float("{:.2f}".format(res))


print(distance(1, 1, 0, 0))
