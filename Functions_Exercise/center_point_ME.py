from math import sqrt, floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def print_closest_point_coordinates(x1_f, y1_f, x2_s, y2_s):
    distance_f = sqrt(((x1_f ** 2) + (y1_f ** 2)))
    distance_s = sqrt(((x2_s ** 2) + (y2_s ** 2)))

    if distance_f <= distance_s:
        print(f"({floor(x1_f)}, {floor(y1_f)})")
    else:
        print(f"({floor(x2_s)}, {floor(y2_s)})")


print_closest_point_coordinates(x1, y1, x2, y2)
