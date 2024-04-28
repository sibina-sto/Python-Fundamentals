# 04-03. FUNCTIONS [More Exercises]
# 03. Longer Line

from math import sqrt


def cartesian_near(x1, y1, x2, y2, x3, y3, x4, y4):
    l1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    l2 = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    if l1 >= l2:
        d1 = sqrt((x1 - 0) ** 2 + (y1 - 0) ** 2)
        d2 = sqrt((x2 - 0) ** 2 + (y2 - 0) ** 2)
        if d1 <= d2:
            return x1, y1, x2, y2
        else:
            return x2, y2, x1, y1
    else:
        d3 = sqrt((x3 - 0) ** 2 + (y3 - 0) ** 2)
        d4 = sqrt((x4 - 0) ** 2 + (y4 - 0) ** 2)
        if d3 <= d4:
            return x3, y3, x4, y4
        else:
            return x4, y4, x3, y3


long_x_near, long_y_near, long_x_far, long_y_far = cartesian_near(float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()))

print(f'({int(long_x_near)}, {int(long_y_near)})({int(long_x_far)}, {int(long_y_far)})')
