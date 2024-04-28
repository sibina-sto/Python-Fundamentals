# 04-03. FUNCTIONS [More Exercises]
# 02. Center Point

from math import sqrt


def cartesian_near(x1, y1, x2, y2):
    d1 = sqrt((x1 - 0) ** 2 + (y1 - 0) ** 2)
    d2 = sqrt((x2 - 0) ** 2 + (y2 - 0) ** 2)
    if d1 <= d2:
        return x1, y1
    else:
        return x2, y2


x_near, y_near = cartesian_near(float(input()), float(input()), float(input()), float(input()))

print(f'({int(x_near)}, {int(y_near)})')
