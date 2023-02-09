students_per_hour_f_employee = int(input())
students_per_hour_s_employee = int(input())
students_per_hour_t_employee = int(input())
students_count = int(input())

hours = 0

while students_count:
    hours += 1

    if hours % 4 == 0:
        continue

    students_count -= students_per_hour_f_employee + students_per_hour_s_employee + students_per_hour_t_employee

    if students_count < 0:
        students_count = 0


print(f"Time needed: {hours}h.")
