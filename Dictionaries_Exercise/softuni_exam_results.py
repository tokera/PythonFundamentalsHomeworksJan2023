exam = input()
statistics = {}
submissions = {}
while exam != "exam finished":
    exam_args = exam.split("-")
    username = exam_args[0]

    if exam_args[1] == "banned":
        statistics.pop(username)
        exam = input()
        continue

    language = exam_args[1]
    points = int(exam_args[2])

    if username not in statistics:
        statistics[username] = points
    else:
        if statistics[username] < points:
            statistics[username] = points

    if language not in submissions:
        submissions[language] = 0
    submissions[language] += 1

    exam = input()

print("Results:")
for student, points in statistics.items():
    print(f"{student} | {points}")
print("Submissions:")
for language, count_of_submissions in submissions.items():
    print(f"{language} - {count_of_submissions}")
