# https://www.codewars.com/kata/58b309e4bffc6b0a09000036/train/python

def distance(x1, y1, x2, y2):
    return round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5), 2)


print(distance(1, 1, 0, 0))  # correct data - 1.41

