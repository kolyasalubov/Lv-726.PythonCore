def distance(x1, y1, x2, y2):
    """
    (tuple of int) -> float
    Given two ordered pairs calculate the distance between them.
    Round to two decimal places. This should be easy to do in 0(1) timing.
    """
    dist = ((x2 - x1)**2 + (y2 - y1)**2) ** (0.5)
    return float('{:.2f}'.format(dist))
    
print(distance(1, 1, 0, 0))