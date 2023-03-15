# students = {}
# filtered_students = {}
#
# while True:
#     line = input()
#     if ":" not in line:
#         course = " ".join(line.split("_"))
#         filtered_students = {key: item[0] for (key, item) in students.items() if item[1] == course}
#         break
#
#     command = line.split(":")
#     student_name = command[0]
#     student_id = command[1]
#     course = command[2]
#
#     students[student_name] = [student_id, course]
#
# [print(f"{student_name} - {student_id}") for (student_name, student_id) in filtered_students.items()]


students_dict = {}

command = input()
while ":" in command:
    name, stud_id, course = command.split(":")

    if course not in students_dict:
        students_dict[course] = {}

    students_dict[course][stud_id] = name

    command = input()

course = " ".join(command.split("_"))

if course in students_dict:
    for student_id, name in students_dict[course].items():
        print(f"{name} - {student_id}")

# for key, value in students_dict.items():
#     if key == course:
#         for student_id, name in value.items():
#             print(f"{name} - {student_id}")
