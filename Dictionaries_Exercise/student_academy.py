n = int(input())
students = {}
for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

[print(f"{student} -> {(sum(grades) / len(grades)):.2f}")
 for student, grades in students.items() if sum(grades) / len(grades) >= 4.5]
