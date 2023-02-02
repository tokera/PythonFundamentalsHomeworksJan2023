from math import sqrt, floor

first_line_x1 = float(input())
first_line_y1 = float(input())
first_line_x2 = float(input())
first_line_y2 = float(input())
second_line_x1 = float(input())
second_line_y1 = float(input())
second_line_x2 = float(input())
second_line_y2 = float(input())


def measure_line_between_points(x1, y1, x2, y2):
    distance = sqrt((((x2 - x1) ** 2) + ((y2 - y1) ** 2)))

    return distance


def print_closest_point_coordinates(x1_f, y1_f, x2_s, y2_s):
    distance_f = sqrt(((x1_f ** 2) + (y1_f ** 2)))
    distance_s = sqrt(((x2_s ** 2) + (y2_s ** 2)))

    if distance_f <= distance_s:
        print(f"({floor(x1_f)}, {floor(y1_f)})({floor(x2_s)}, {floor(y2_s)})")
    else:
        print(f"({floor(x2_s)}, {floor(y2_s)})({floor(x1_f)}, {floor(y1_f)})")


first_line_length = measure_line_between_points(first_line_x1, first_line_y1, first_line_x2, first_line_y2)
second_line_length = measure_line_between_points(second_line_x1, second_line_y1, second_line_x2, second_line_y2)

if first_line_length >= second_line_length:
    print_closest_point_coordinates(first_line_x1, first_line_y1, first_line_x2, first_line_y2)
else:
    print_closest_point_coordinates(second_line_x1, second_line_y1, second_line_x2, second_line_y2)
